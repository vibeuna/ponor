---
layout: post
title: "Prompt, tok rada ili agent: kako izabrati"
date: 2026-10-12
category: ai-u-praksi
image: /assets/images/2026-10-12-agentski-obrasci.svg
read_time: 7
description: "Jedan prompt, tok rada ili agent? Savjeti Anthropica, OpenAI-ja i Googlea, pet obrazaca toka rada i šta istraživanja kažu o cijeni i pouzdanosti agenata."
tags: [ai-agenti]
---

Firma želi "AI agenta" koji će svako jutro sažeti pristigle mejlove. Za to joj agent ne treba. Dovoljan je jedan dobro napisan prompt za svaki mejl i malo koda koji ga pokreće. To je već najjednostavniji tok rada, a ne agent. Po procjeni redakcije, agent bi isti posao radio skuplje i manje predvidivo. Ovaj vodič pokazuje kako prepoznati koliko samostalnosti zadatak zaista traži.

## Ukratko

Anthropic, OpenAI i Google savjetuju isto: počnite od najjednostavnijeg rješenja. Za sažimanje, prijevod ili razvrstavanje teksta dovoljan je jedan prompt. Tok rada, u kojem kod unaprijed određuje korake, pogodan je za zadatke čiji je redoslijed poznat. Agent, kod kojeg model sam bira sljedeći korak, ima smisla tek kada se koraci ne mogu predvidjeti. Agenti troše više tokena, a istraživanja (uglavnom radovi koji još nisu recenzirani) pokazuju da složenija rješenja često nisu bolja od jednostavnijih.

## Tri opcije: prompt, tok rada i agent

Razlika se svodi na jedno pitanje: ko odlučuje o sljedećem koraku, kod ili model?

- **Jedan [prompt](/rjecnik/prompt/)** (uputa ili upit koji dajete modelu). [Veliki jezički model (large language model, LLM)](/rjecnik/veliki-jezicki-model/) dobije uputu i vrati odgovor. Sljedećeg koraka nema.
- **Tok rada (workflow).** Model se poziva više puta, ali redoslijed poziva unaprijed određuje kod koji je napisao programer. Model popunjava korake, ali ih ne bira.
- **[Agent](/rjecnik/agent/).** Model sam odlučuje šta će sljedeće uraditi i koje će [alate](/rjecnik/alat/) pozvati. Odluku donosi na osnovu onoga što mu okruženje vrati, i tako u krug. Taj ciklus zove se [agentska petlja](/rjecnik/agentska-petlja/).

U Ponoru izraz "tok rada" koristimo upravo u tom značenju: putanju određuje kod, a ne model.

{% include diagram.html name="agentski-obrasci" caption="Ljestve odluke: počnite od jednog prompta i penjite se više tek kad niža prečka nije dovoljna." alt="Tri prečke, odozdo prema gore: jedan prompt; tok rada u kojem kod određuje korake (ulančavanje promptova, usmjeravanje, paralelizacija, orkestrator i radnici, petlja ocjenjivanja); agent u kojem model sam bira sljedeći korak. Lijeva osa: na dnu o sljedećem koraku odlučuje kod, na vrhu model. Desna osa: trošak i nepredvidivost rastu prema vrhu." %}

## Pet obrazaca toka rada

Pet obrazaca opisano je u Anthropicovom vodiču "Building effective agents" (decembar 2024). Anthropic je naknadno dodao napomenu da su se mnogi alati za izradu agenata u međuvremenu promijenili. Po našoj ocjeni, obrasci su i dalje korisna mapa.

1. **Ulančavanje promptova (prompt chaining).** Fiksan niz poziva u kojem svaki korak koristi rezultat prethodnog. Između koraka kod može provjeriti međurezultat prije nego što zadatak ide dalje. Primjer: prvo nacrt teksta, zatim provjera dužine, pa prijevod.
2. **Usmjeravanje (routing).** Ulaz se najprije razvrsta, a zatim proslijedi specijaliziranom promptu ili modelu. Naprimjer, reklamacije idu jednom promptu, a tehnička pitanja drugom.
3. **Paralelizacija (parallelization).** Više poziva radi istovremeno, a rezultati se potom spajaju. Postoje dvije varijante: podjela, kada svaki poziv obrađuje zaseban podzadatak, i glasanje, kada se isti zadatak pokrene više puta.
4. **Orkestrator i radnici (orchestrator-workers).** Centralni model tek u toku rada dijeli zadatak na podzadatke, prosljeđuje ih drugim pozivima modela i spaja rezultate. Okvir i dalje određuje kod, pa je ovo tok rada, a ne agent. Od svih pet obrazaca, ovaj je najbliži agentu.
5. **Petlja ocjenjivanja (evaluator-optimizer).** Jedan poziv piše, a drugi, ocjenjivač (judge), provjerava rezultat prema jasnim kriterijima. Petlja se ponavlja sve dok rezultat ne prođe provjeru.

## Kada je agent zaista potreban?

Sva tri proizvođača postavljaju sličan prag.

**Anthropic** savjetuje da se traži "najjednostavnije moguće rješenje" i da se složenost povećava samo kada je to potrebno, što "može značiti i da se agentski sistem uopće ne gradi". U istom vodiču piše da je za mnoge primjene obično dovoljno doraditi pojedinačne pozive modela, uz generisanje potpomognuto pretraživanjem (retrieval-augmented generation, RAG) i primjere u promptu.

**OpenAI** u vodiču iz aprila 2025. preporučuje agenta tamo gdje rješenja zasnovana na fiksnim pravilima zakazuju: kod složenih odluka, pravila koja je teško održavati i nestrukturiranih podataka. U ostalim slučajevima može biti dovoljno rješenje čije korake određuje kod.

**Google** piše da je, ako se zadatak može obaviti jednim pozivom modela, možda isplativije razmotriti rješenje bez agenta. Kao primjere daje sažimanje, prevođenje i razvrstavanje.

Isto važi i za broj agenata. OpenAI savjetuje da se najprije iskoristi sve što može jedan agent. Na više agenata treba preći tek kada logika ima previše grananja ili kada agent ima previše alata koji se preklapaju. Pritom nije presudan sam broj alata: neki agenti dobro rade s više od 15 jasno razgraničenih alata, dok se drugi muče i s manje od 10 alata koji se preklapaju.

## Šta autonomija košta

**Tokeni.** Prema Anthropicovim internim podacima iz teksta o sistemu Research, agenti troše oko četiri puta više [tokena](/rjecnik/token/) (osnovnih jedinica teksta koje model obrađuje) nego običan razgovor s modelom, a [sistemi s više agenata](/rjecnik/sistem-s-vise-agenata/) oko 15 puta više. To su podaci jedne firme, a ne opće pravilo za sve agente. Isti izvor navodi da sistemi s više agenata nisu dobar izbor za većinu programerskih zadataka. Navodi i da je Anthropicov sistem s više agenata na internoj evaluaciji bio 90,2% bolji od jednog agenta s istim glavnim modelom. Nezavisne provjere tog broja nema.

**Istraživanja.** Radovi u nastavku objavljeni su na arXivu. Ni za jedan nismo našli potvrdu da je prošao recenziju, pa ih treba čitati kao preprinte (radove koji još nisu recenzirani).

- *AI Agents That Matter* (2024): uz sličnu tačnost, troškovi različitih pristupa razlikuju se "gotovo za dva reda veličine", odnosno skoro stotinu puta. Na benchmarku (referentnom testu) HumanEval pristup LATS bio je više od 50 puta skuplji od jednostavnog pristupa s ponovljenim pokušajima, bez značajne razlike u tačnosti.
- *Agentless* (2024): fiksan tok rada u tri faze riješio je 32,00% zadataka na SWE-bench Lite, uz prosječan trošak od 0,70 dolara po zadatku. Prema autorima, to je tada bio bolji rezultat od svih agenata za programiranje otvorenog koda.
- *Why Do Multi-Agent LLM Systems Fail?* (2025): autori polaze od zapažanja da sistemi s više agenata na popularnim benchmarkima često donose tek minimalne dobitke i istražuju zašto je tako. Opisuju 14 načina na koje takvi sistemi zakazuju.
- *Towards a Science of Scaling Agent Systems* (2025, dopunjeno 2026): u poređenju s jednim agentom, rezultati sistema s više agenata kretali su se od +80,8% na finansijskim zadacima koji se mogu podijeliti na dijelove do −70,0% na zadacima koji traže planiranje korak po korak. Glavni nalaz: kada jedan agent već radi dobro, dodatni agenti donose sve manju korist.
- *Do More Agents Help?* (2026, dopunjeno u oktobru 2026, model GPT-4.1): od šest postavki s više agenata samo je jedna u prosjeku bila bolja od jednog agenta (79,70% naspram 76,65%). Ostalih pet zaostajalo je za 1,71 do 8,76 procentnih poena. Na pojedinim testovima dobici su ipak veliki: jedna postavka bila je bolja za 9,67 poena na HumanEvalu, a druga za 22,25 poena na IFEvalu, ali uz 1,39, odnosno 4,34 puta veću potrošnju tokena.

**Pouzdanost.** Agent koji je zadatak riješio jednom ne mora ga riješiti i sljedeći put. Rad *On the Reliability of Computer Use Agents* (2026) testira Agent S3 s modelom GPT-5 na OSWorldu, benchmarku za upravljanje računarom (computer use), u kojem model radi na računaru na osnovu snimaka ekrana. Agent S3 riješio je oko 78% zadataka barem jednom u deset pokušaja, ali samo oko 36% u svih deset. Rad *Beyond pass@1* (2026) pokazuje da se jaz između onoga što agent može uraditi i onoga što uradi pouzdano širi što je zadatak duži.

## Kako odlučiti u praksi

Ovo je savjet redakcije Ponora, izveden iz navedenih izvora, a ne rezultat istraživanja.

1. **Počnite od jednog prompta.** Ako rezultat nije dobar, prvo popravite prompt: jasno postavite zadatak, dajte kontekst i odredite oblik odgovora.
2. **Ako zadatak ima poznate korake, napravite tok rada.** Izaberite obrazac koji odgovara problemu: niz koraka, razvrstavanje, paralelne pozive ili petlju ocjenjivanja.
3. **Agenta uvedite tek kada se koraci ne mogu predvidjeti** i kada ste na vlastitim primjerima izmjerili da jednostavnije rješenje ne radi. Tada postavite zaštitna ograničenja i ljudski nadzor (human-in-the-loop) za radnje koje se ne mogu poništiti.
4. **Kada vam neko nudi "AI agenta", pitajte ko odlučuje o sljedećem koraku.** Ako to radi kod, kupujete tok rada. To nije mana, ali cijena i očekivanja trebaju biti u skladu s tim.

## Šta NIJE

- **Agent nije napredniji tok rada.** To je drugačiji kompromis: više prilagodljivosti po cijenu većeg troška i manje predvidivosti.
- **Više agenata ne znači bolji rezultat.** Navedena istraživanja pokazuju i dobitke i gubitke, zavisno od zadatka.
- **"Workflow" ne znači svugdje isto.** OpenAI tim izrazom opisuje slijed koraka koji izvršava agent. Google agentom naziva i sistem čije korake redom određuje kod. Kada čitate vodiče, provjerite šta autor pod tim podrazumijeva.

## Povezano

- [Šta je AI agent i kako radi?](https://www.ponor.ba/clanci/sta-je-ai-agent/) – definicije agenta, agentska petlja i ranija mjerenja pouzdanosti.
- [Kako napisati dobar prompt: jezik, situacija, oblik odgovora](https://www.ponor.ba/clanci/kako-napisati-dobar-prompt/) – prvi korak prije svakog toka rada ili agenta.
- [Šta je LLM token i kako radi tokenizacija?](https://www.ponor.ba/clanci/sta-je-llm-token/) – zašto potrošnja tokena određuje cijenu.

## Izvori

- [Building effective agents – Anthropic, 2024](https://www.anthropic.com/engineering/building-effective-agents)
- [How we built our multi-agent research system – Anthropic, 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- [A practical guide to building agents – OpenAI, 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Choose a design pattern for your agentic AI system – Google Cloud](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- [AI Agents That Matter – arXiv 2024](https://arxiv.org/abs/2407.01502)
- [Agentless: Demystifying LLM-based Software Engineering Agents – arXiv 2024](https://arxiv.org/abs/2407.01489)
- [Why Do Multi-Agent LLM Systems Fail? – arXiv 2025](https://arxiv.org/abs/2503.13657)
- [Towards a Science of Scaling Agent Systems – arXiv 2025](https://arxiv.org/abs/2512.08296)
- [Do More Agents Help? Evaluating Accuracy and Cost in LLM Multi-Agent Workflows – arXiv 2026](https://arxiv.org/abs/2606.05670)
- [On the Reliability of Computer Use Agents – arXiv 2026](https://arxiv.org/abs/2604.17849)
- [Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents – arXiv 2026](https://arxiv.org/abs/2603.29231)
