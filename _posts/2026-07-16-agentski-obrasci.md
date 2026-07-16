---
layout: post
title: "Agentni obrasci: ljestve, a ne meni"
date: 2026-07-16
category: vodici
audience: developers
read_time: 13
description: "Svih sedam agentnih obrazaca svode se na jedno pitanje: ko drži kontrolu toka, kod ili model? Vodič kroz izbor obrasca, uz jasan stav da je agent trošak, a ne odredište."
image: /assets/images/2026-07-16-agentski-obrasci.svg
---

Većina odluka o "agentnoj arhitekturi" nije odluka o arhitekturi. To je odluka o jednoj jedinoj stvari: ko drži **kontrolu toka (control flow)** – vaš kod ili model. Kad kod odlučuje koji korak ide sljedeći, gradite radni tok. Kad model to odlučuje u hodu, gradite agenta. Sve ostalo – sedam obrazaca koje ćete sresti u dokumentaciji frameworka – samo su tačke na toj jednoj osi.

Ovaj tekst je mapa izbora, ne pregled mehanike. Kako agentna petlja zaista radi (ciklus posmatraj–rezonuj–djeluj, mehanika poziva alatu (tool), uvjeti zaustavljanja) opisano je zasebno u tekstu [Agentni loop: kako LLM zaista izvršava višekorake zadatke](/clanci/agentni-loop/). Ovdje je pitanje drugačije: dat vam je zadatak – koji od sedam oblika birate, i trebate li ijedan.

## Jedna osa: ko drži kontrolu toka

Radni tok (workflow) je sistem u kojem su koraci unaprijed određeni kodom. Putanja je fiksna, predvidljiva, testabilna i jeftina. Model popunjava pojedine korake, ali redoslijed i grananje pripadaju vama.

Agent je sistem u kojem model sam bira sljedeći potez na osnovu povratne informacije iz okruženja. Model odlučuje koliko koraka treba, kojim alatima da posegne i kada je gotov. To donosi fleksibilnost za probleme čiju putanju ne možete nacrtati unaprijed – i uzima determinizam, jeftinoću i lakoću debugiranja kao cijenu.

Ta razmjena je cijela poenta. Fleksibilnost nije besplatna: plaćate je latencijom, nepredvidljivošću i sistemom koji je teško reprodukovati. Zato agenti u ovom tekstu nisu vrhunac zrelosti kojem svi treba da težimo. Oni su trošak koji preuzimate samo kad vam jednostavnija stvar demonstrativno zakaže.

### Ljestve, ne meni

Iz toga slijedi pravilo koje drži cijeli tekst: obrasci nisu meni sa kojeg birate po ukusu, nego ljestve po kojima se penjete odozdo.

1. **Najniža prečka: jedan dobar prompt.** Prije ikakvog sistema, pitajte može li jedan dobro dizajniran prompt (uz dohvatanje (retrieval) i par primjera) obaviti posao. Ako može, tu stanite. Za to je dovoljno razumjeti šta [veliki jezički model](/clanci/sta-su-veliki-jezicki-modeli/) zapravo radi – ostatak ljestava gradi se na toj osnovi.
2. **Srednje prečke: radni tokovi.** Ako je putanja poznata u trenutku dizajna, ostajete u zemlji radnih tokova. Kod drži kontrolu toka; birate oblik prema zadatku.
3. **Najviša prečka: agent.** Samo ako putanja iskreno nije predvidljiva – broj koraka se ne da ograničiti unaprijed – penjete se na agenta.

Na sljedeću prečku se penjete tek kad ona ispod demonstrativno zakaže, a ne zato što je "naprednija". Ovo je i teza Anthropicovog vodiča "Building Effective Agents" i, nezavisno, OpenAI-jevog "A Practical Guide to Building Agents": koristite najjednostavniju stvar koja radi, i dodajte agentnost tek kad njena fleksibilnost nadjača trošak.

{% include diagram.html name="agentski-obrasci" caption="Ljestve agentskih obrazaca: penji se od jednog prompta, preko radnog toka, do agenta – a osa je jedno pitanje: ko drži kontrolu toka, kod ili model." alt="Dijagram ljestava s tri prečke koje se čitaju odozdo prema gore: najniža je jedan prompt, srednja je radni tok (kod drži kontrolu toka; sadrži pet obrazaca – ulančavanje promptova, usmjeravanje, paralelizacija, orchestrator–radnici i evaluator–optimizator), a najviša je agent (model drži kontrolu toka; ReAct i refleksija). Vertikalna osa lijevo pokazuje da kontrola toka prelazi s koda na model kako se penjete, uz poruku da je agent trošak, a ne cilj." %}

## Radni tokovi: kod drži kontrolu toka

Pet obrazaca u kojima vi pišete kontrolu toka. Za svaki: šta je, kanonski slučaj, konkretan primjer, glavni način otkazivanja i okidač za posezanje.

### Ulančavanje promptova (prompt chaining)

**Šta je:** zadatak razložen na fiksan niz koraka, gdje izlaz jednog koraka ulazi u sljedeći, često uz programsku provjeru između njih.

**Slučaj:** podzadaci su poznati i čisto razdvojivi, a spremni ste žrtvovati latenciju za tačnost.

**Primjer:** generiši strukturu dokumenta → **validaciona kapija (validation gate)** provjeri da struktura ima sve obavezne sekcije → tek onda napiši puni tekst. Ili: napiši marketinški tekst → prevedi ga. Kapija između koraka je obična programska provjera (regex, schema, brojač) koja mora proći da bi lanac nastavio.

**Kako otkazuje:** krutost. Korak koji autor nije predvidio nema putanju kroz lanac. Ako se pojavi ulaz koji ne pripada nijednom predviđenom koraku, lanac nema kud.

**Posegni za ovim kad:** se zadatak svaki put razlaže na isti način.

### Usmjeravanje (routing)

**Šta je:** klasifikuj ulaz, pa ga proslijedi specijalizovanoj nizvodnoj putanji. Kratko: klasifikacija pa usmjeravanje.

**Slučaj:** ulazi padaju u jasno različite kategorije kojima je bolje rukovati posebno, a klasifikacija je pouzdana.

**Primjer:** tiketi podrške → redovi za povrat novca / tehničke probleme / opšte upite, svaki sa svojim promptom. Druga česta primjena je usmjeravanje po cijeni: jeftini, rutinski upiti idu jeftinijem modelu, teški ka sposobnijem. Konkretan izbor "jeftin naspram sposoban model" mijenja se iz mjeseca u mjesec – vrijedi kao obrazac, ne kao fiksna preporuka modela.

**Kako otkazuje:** pogrešna klasifikacija tiho šalje posao niz krivu putanju. Greška se ne vidi na mjestu nastanka nego tek na kraju, u pogrešnom odgovoru.

**Posegni za ovim kad:** su kategorije jasno različite i klasifikator ih pouzdano razlikuje.

### Paralelizacija (parallelization)

**Šta je:** više poziva modelu izvršenih istovremeno, pa agregacija rezultata. Ima dva pod-oblika. **Sekcioniranje (sectioning)** dijeli zadatak na nezavisne podzadatke koji teku paralelno. **Glasanje (voting)** pokreće isti zadatak više puta i agregira rezultate radi pouzdanosti.

**Slučaj:** brzina kroz podjelu (sekcioniranje) ili pouzdanost kroz konsenzus (glasanje).

**Primjer:** dok jedan poziv provjerava ulaz na neprikladan sadržaj, drugi paralelno formuliše odgovor (sekcioniranje). Ili: N nezavisnih prolaza traži ranjivost u kodu, pa većina odlučuje (glasanje).

**Kako otkazuje:** trošak se množi s N. Kod glasanja logika agregacije može sakriti neslaganje – ako tri od pet prolaza griješe na isti način, "većina" vam daje pogrešan odgovor sa lažnim samopouzdanjem.

**Posegni za ovim kad:** su podzadaci istinski nezavisni, ili kad vam treba glas povjerenja nad istim zadatkom.

### Orchestrator–radnici (orchestrator-workers)

**Šta je:** centralni **orchestrator** (koordinatorski agent) razlaže zadatak na podzadatke *u toku izvršavanja* i delegira ih radnicima, pa sintetiše rezultate. Ključna razlika u odnosu na paralelizaciju: podzadaci nisu poznati unaprijed.

**Slučaj:** broj i oblik podzadataka zavise od ulaza, pa se ne mogu unaprijed nabrojati.

**Primjer:** izmjena koda koja dodiruje neodređen broj fajlova; istraživanje koje se grana na onoliko izvora koliko ih tema zahtijeva. Radnici su u pravilu [sub-agenti](/clanci/claude-md-agent-md/), svaki sa vlastitim kontekstom i konfiguracijom.

**Kako otkazuje:** kontekst orchestratora raste sa svakim delegiranim podzadatkom, a koordinacija i sinteza su najteži i najskuplji dio. Rast konteksta po iteraciji je isti fundamentalni pritisak opisan u tekstu [Kontekstni prozor u praksi](/clanci/context-window-praksa/) – ovdje se samo umnožava po radniku.

**Posegni za ovim kad:** ne možete unaprijed nabrojati podzadatke, ali kod i dalje drži strukturu najvišeg nivoa. Primijetite: ovo je i dalje radni tok, iako je dinamičan – vi ste napisali petlju delegiranja, model bira samo sadržaj podzadataka.

### Evaluator–optimizator (evaluator-optimizer)

**Šta je:** jedan poziv modelu generiše, drugi ga evaluira prema eksplicitnim kriterijima, i petlja se vrti generisanje → evaluacija → dorada dok ne prođe.

**Slučaj:** postoje jasni kriteriji ocjene, iteracija mjerljivo pomaže, a model daje korisnu povratnu informaciju.

**Primjer:** književni prijevod koji se dorađuje kroz više rundi radi nijanse; višekružna pretraga koja se sužava dok ne pokrije upit.

**Kako otkazuje:** petlje koje ne konvergiraju i protraćene iteracije kad je kriterij nejasan. Ako "dobro" nije provjerljivo, evaluator vrti krugove bez napretka.

**Posegni za ovim kad:** je "dobro" provjerljivo i prvi prolaz pouzdano nije dovoljno dobar.

> Razlika koja se često miješa: evaluator–optimizator razdvaja generatora i evaluatora u dvije uloge. To nije isto što i refleksija, gdje jedan isti model introspektira nad vlastitim izlazom.

## Agenti: model drži kontrolu toka

Kad nijedan radni tok ne pokriva zadatak jer se putanja ne da nacrtati, penjete se na agenta. Dva obrasca su dovoljna za mapu izbora. Namjerno ih držimo tankim: *kako* petlja radi iznutra pripada tekstu [Agentni loop](/clanci/agentni-loop/); ovdje je samo *kada* posegnuti za autonomijom.

### ReAct

**ReAct** (obrazac 'rezonuj pa djeluj') je agent koji sam vodi svoju upotrebu alata u petlji protiv povratne informacije iz okruženja, sam birajući broj koraka. Posežete za njim za otvorene probleme gdje se broj koraka ne da predvidjeti – rješavanje prijavljenog softverskog problema kroz nepoznat niz izmjena, ili computer use (sposobnost AI modela da upravlja grafičkim sučeljima). (Rezultati na zadacima poput SWE-bench-a i computer use su demonstracije sposobnosti iz objava proizvođača, ne gotova produkcijska rješenja.) Cijena: nedeterminizam, akumulirajuće greške, latencija i trošak koji lete, i sistem koji je težak za debugiranje.

### Refleksija (reflection) / samokritika

**Refleksija** je sloj u kojem model kritikuje i revidira vlastiti izlaz kroz dodatne poteze; **samokritika** je konkretan čin u kojem model nalazi grešku u svom radu. Koristite je štedljivo, tek kad samoprovjera demonstrativno podigne kvalitet. Cijena: dodatni potezi i dodatni tokeni, a samokritika ume racionalizovati umjesto da ispravi – model "objasni" zašto je pogriješio umjesto da popravi. Posegnite za njom tek nakon izmjerenog dobitka na kvalitetu.

Autonomiju uzimate uz **zaštitne ograde (guardrails)** i, gdje operacija nosi rizik, uz human-in-the-loop provjeru. Autonomija sama po sebi nije vrlina – to je trošak koji opravdavate samo kad putanju iskreno ne možete unaprijed odrediti.

## Pravilo izbora

Cijela mapa staje u tri koraka koja se izvršavaju redom:

1. **Može li jedan dobro dizajniran prompt (uz dohvatanje, uz primjere) obaviti posao?** Ako može – isporučite to. Ne gradite sistem.
2. **Je li kontrola toka poznata u trenutku dizajna?** Ako jeste, ostajete u radnim tokovima. Birajte prema obliku:
   - fiksan niz → ulančavanje promptova
   - grananje po kategoriji → usmjeravanje
   - nezavisno-ili-glasanje → paralelizacija
   - razlaganje u toku izvršavanja → orchestrator–radnici
   - provjerljivo-i-iterativno → evaluator–optimizator
3. **Tek ako je putanja iskreno nepredvidljiva** – broj koraka se ne da ograničiti – penjite se na agenta, dodajte zaštitne ograde i sandbox, i prihvatite porez na latenciju, trošak i debugiranje.

OpenAI-jev vodič daje isti smjer sa dvije konkretne granice za dijeljenje jednog agenta na više njih: podijelite tek kad prompt izraste u mnoštvo if-then-else grana, ili kad alati postanu toliko slični da model bira pogrešan. Sam broj alata nije okidač.

## Kad NE graditi agenta

Negativni prostor je jednako važan kao i mapa. Agent je pogrešan izbor kad:

- **Putanja je vezana latencijom.** Interaktivni UX i real-time putanje ne trpe višekružnu petlju – uzmite radni tok ili jedan poziv.
- **Putanja je osjetljiva na trošak pri velikom obimu.** Agentni prolaz košta osjetno više po zadatku od jednog poziva. Prateći tekst navodi heuristiku od otprilike 4× tokena za agentne zadatke u odnosu na jednokratne pozive – heuristika iz proizvođačkog uputstva, ne izmjerena vrijednost, i zavisi od implementacije harness-a.
- **Trebate mogućnost debugiranja i reviziju.** Nedeterministička kontrola toka teško se reprodukuje i sertifikuje – što je važno za regulisane i sigurnosno-kritične kontekste.
- **Zahtjev je deterministički.** Ako isti ulaz mora svaki put dati istu putanju, kodom definisan radni tok pobjeđuje kontrolu vođenu modelom.

Iskrena slika je da najveći dio produkcijske vrijednosti danas leži u radnim tokovima, ne u agentima. Agent je alat za usko definisanu klasu problema, a ne cilj razvoja. Kad krenete da ga gradite, prvo dokažite da prečka ispod ne radi.

## Izvori

- [Building Effective Agents – Anthropic (Dec 2024)](https://www.anthropic.com/engineering/building-effective-agents)
- [A Practical Guide to Building Agents – OpenAI (2025, PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Yao et al. (2022) – ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)
- [Shinn et al. (2023) – Reflexion (arXiv:2303.11366)](https://arxiv.org/abs/2303.11366)
- [Lilian Weng – LLM Powered Autonomous Agents (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/)
