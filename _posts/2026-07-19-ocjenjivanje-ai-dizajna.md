---
layout: post
title: "Kako ocijeniti AI-generisani UI dizajn: zašto LLM nije dovoljan"
date: 2026-07-19
category: ai-u-praksi
audience: designers
read_time: 9
description: "AI danas može generisati desetine UI dizajna za nekoliko sekundi. Ali kako znati koji je zaista dobar? Objašnjavamo tri sloja evaluacije i zašto LLM nikada ne bi trebao imati posljednju riječ."
image: /assets/images/2026-07-19-ocjenjivanje-ai-dizajna.svg
---

Alat vam za nekoliko sekundi izbaci gotov ekran: raspored, komponente, boje, tekst, čak i markup. Problem nije više u tome da se dizajn napravi. Problem je u tome da procijenite je li dobar prije nego što ga pošaljete korisnicima. Generisanje je postalo jeftino i brzo; provjera je ostala spora, ručna i ovisna o iskustvu. To usko grlo, a ne kreativni dio, danas određuje koliko AI-a zaista možete pustiti u proizvod.

Za dizajnere ovo mijenja opis posla. Sve češće nećete crtati prvi ekran nego ocjenjivati tuđi, gdje je taj "tuđi" model. A da biste ocjenjivali kako treba, morate znati čime ocjenjujete i, još važnije, šta svaki od tih alata sistematski ne vidi. Dobra vijest je da su načini evaluacije danas prilično jasni. Loša je što svaki ima imenljive slijepe tačke, i što su dokazi o njihovoj pouzdanosti još rani.

Napomena o dokazima: sve što slijedi oslanja se na male, rane studije, prošireni sažeci s konferencija i modeli s početka 2025. Ovo su tendencije koje se naziru, ne utvrđene činjenice. Tretirajte ih kao smjernice za razmišljanje, ne kao mjerne vrijednosti na koje se možete pozvati.

## Tri načina da se ocijeni AI-generisani dizajn

U praksi postoje tri pristupa, i najčešće se koriste zajedno, ne umjesto jedan drugog.

Prvi je **LLM-as-judge (LLM u ulozi ocjenjivača, u nastavku LLM-as-judge)**: uzmete jezički model i date mu da pregleda dizajn, dijagnostikuje probleme u upotrebljivosti i predloži popravke. Model postaje neka vrsta reviewer agenta (agent koji provjerava rezultate) nad vašim UI-jem. Ovdje se dizajn ocjenjuje strukturiranim izvještajem: model prolazi kroz rubriku i za svaku dimenziju daje ocjenu i obrazloženje.

Drugi je **automatska heuristička i benchmark provjera**: alati poput axe i Lighthouse, pravila za omjer kontrasta, provjere rasporeda i strukture. Ovo su determinističke provjere. Ne "misle" o dizajnu; provjeravaju da li su ispunjena mjerljiva pravila. Brze su, jeftine, ponavljljive i idealne za regresijske provjere u pipeline-u.

Treći je **ljudska evaluacija**: ekspertski pregled, heuristička evaluacija, testiranje upotrebljivosti i, presudno, stvarni korisnici pomoćnih tehnologija, poput osoba koje se oslanjaju na čitač ekrana. Ovo je najsporije i najskuplje, ali jedino hvata ono što ostala dva ne mogu.

Ključno je da svaki od ova tri sloja pripada drugom mjestu u toku rada. Automatska provjera je kapija na ulazu. LLM-as-judge je trijaža koja odvaja ono što vrijedi gledati od šuma. Ljudi su tu za odluke koje nose rizik. Miješanje ovih uloga, na primjer davanje modelu da potpiše da je nešto pristupačno, je gdje nastaju problemi.

{% include diagram.html name="ocjenjivanje-ai-dizajna" caption="Tri sloja evaluacije: jeftina automatska kapija, LLM-as-judge kao trijaža, i ljudska evaluacija koja nosi presudu. Materijal se spušta i sužava; potpis ostaje kod čovjeka." alt="Lijevak s tri sloja evaluacije AI-generisanog dizajna, od automatske kapije preko LLM trijaže do ljudske evaluacije." %}

Praktična kalkulacija je pitanje cijene i posljedice. Automatska provjera je gotovo besplatna po pokretanju, pa je razumno da radi neprekidno, na svakoj varijanti, kao pozadinska higijena. LLM-as-judge košta nešto po pozivu i vrijedi ga zvati kada imate previše materijala za ručni pregled, a premalo vremena. Ljudska evaluacija je najskuplja i najsporija, pa je čuvate za tačke gdje pogrešna odluka stvarno boli, gdje korisnik ostaje zaključan izvan proizvoda, gdje nova funkcija zbuni umjesto da pomogne, gdje ton promaši publiku. Cilj nije da jedan sloj pobijedi ostale, nego da svaki radi tačno onaj dio posla koji drugi ne mogu.

## Šta LLM-as-judge hvata, a šta promašuje

Ovaj pristup je privlačan iz očiglednog razloga: model piše tečno, obrazlaže uvjerljivo i vraća uredno strukturiran izvještaj. Djeluje kao iskusan recenzent. Upravo tu je zamka.

Rad koji se najdirektnije bavi ovim pitanjem je UXBench (arXiv 2606.16262), koji mjeri **actionability** kritika koje LLM generiše o UX-u. Postavka je poučna: osam vodećih modela proizvodi strukturirane izvještaje preko sedam dimenzija rubrike, a ocjenjuje ih metrika nazvana **repair-lift**, to jest može li naknadni agent za popravke zaista poboljšati UI na osnovu te kritike, uz slijepu ljudsku validaciju. Drugim riječima, ne pita se "zvuči li kritika pametno" nego "vodi li kritika do boljeg dizajna".

Nalaz je otrežnjujući. Modeli se, prema tom radu, značajno razlikuju u tome koliko su njihovi izvještaji zaista upotrebljivi, i vodstvo se mijenja od jedne kategorije UI-ja do druge. Nema univerzalnog, pouzdanog ocjenjivača. Model koji je odličan u ocjenjivanju formi može biti osrednji na navigaciji, i obrnuto.

(Napomena o imenu: postoji drugi rad istog imena, arXiv 2606.09570, koji se bavi dijalogom AI asistenata, ne kritikom UI-ja. To nije isti rad i ne treba ih miješati.)

Za dizajnera je praktična pouka jednostavna: **tečnost kritike nije isto što i upotrebljivost kritike.** LLM će skoro uvijek proizvesti nešto što zvuči razumno. Hoće li vas to odvesti do boljeg ekrana je zasebno pitanje, i ovisi o modelu, o kategoriji UI-ja, i o tome imate li način da provjerite. Ako od modela tražite ocjenu i uzmete je zdravo za gotovo jer lijepo zvuči, u opasnosti ste da gradite na kritici koja je uvjerljiva, ali prazna. To je bliski rođak halucinacije (hallucination) u tekstu: samopouzdan iskaz bez pokrića.

Gdje LLM-as-judge ipak radi dobro jeste trijaža. Kada imate deset varijanti ekrana i trebate brzo odvojiti tri koje vrijedi pažljivo gledati od sedam koje ne vrijede, model je koristan filter. On sužava prostor. Ono što ne smije raditi je davati završnu ocjenu.

Postoji i praktičan način da se ublaži varijabilnost koju UXBench opisuje: ne pitajte model za apstraktnu ocjenu ("je li ovaj ekran dobar"), nego za konkretne, provjerljive tvrdnje ("koji elementi nemaju vidljivo stanje fokusa", "gdje redoslijed radnji odstupa od očekivanog"). Što je zadatak konkretniji, to lakše provjeravate izlaz i to manje prostora ima tečnost da vas povede. Kritika koju možete provjeriti u par sekundi vrijedi više od ocjene koju morate uzeti na vjeru, bez obzira koliko uvjerljivo zvučala.

## Šta automatska provjera sistematski ne vidi

Automatski alati za pristupačnost i kvalitet imaju suprotnu osobinu: pouzdani su, ali usko gledaju. Oni hvataju **sintaksne** prekršaje. Nedostaje `alt`? Prijaviće. Nema `aria-label`? Prijaviće. Omjer kontrasta ispod praga? Prijaviće. To je vrijedno i treba ga imati kao prvu kapiju.

Ali ono što ti alati po prirodi ne mogu procijeniti jeste da li je sadržaj **smislen**. I tu ulazimo u najvažniji primjer u cijeloj priči.

### Jaz u semantičkoj pristupačnosti

Rad Calò i saradnika, *Measuring the Semantic Accessibility Gap in LLM-Generated Web UIs* (CHI 2026 Extended Abstracts), opisuje pojavu koju vrijedi zapamtiti pod imenom: **jaz u semantičkoj pristupačnosti (semantic accessibility gap)**. Radi se o UI-ju koji prolazi automatske provjere pristupačnosti, a ipak je za korisnika čitača ekrana neupotrebljiv.

Kako to izgleda konkretno? Model generiše dugme s `aria-label`-om, samo je taj label besmislen, na primjer "button" ili nasumičan niz umjesto opisa radnje. Slika ima `alt` atribut, ali `alt` glasi "image" i ne govori ništa. Linter je zadovoljan, atribut postoji. Korisnik koji ne vidi ekran čuje "dugme" i nema pojma šta to dugme radi. Isto vrijedi za redoslijed čitanja: vizuelno raspored izgleda ispravno, ali redoslijed elemenata u kodu je pobrkan, pa čitač ekrana čita stranicu redom koji nema smisla.

Ovo je precizno mjesto gdje se automatska i ljudska evaluacija razilaze. Alat provjerava postojanje atributa. Čovjek, ili korisnik pomoćne tehnologije, provjerava ima li atribut značenje. Model je odlično naučio da popuni polja koja se provjeravaju, a to je upravo ono što ga čini opasnim: proizvodi UI koji izgleda pristupačno po metrici, a nije pristupačno po iskustvu. Sawicki i saradnici u zasebnoj studiji dolaze do srodnog zaključka, da LLM-generisani UI-ji "teško zadovoljavaju standarde pristupačnosti".

Držite na umu da su oba ova nalaza rana i uskog obima, jedan prošireni sažetak i jedna mala kvalitativna studija. Smjer je jasan, ali veličina jaza i njegova postojanost kroz novije modele još nisu utvrđeni.

**Napomena o propisima.** Kada se govori o pristupačnosti, brzo iskrsnu WCAG, EU AI Act i European Accessibility Act. Ovaj tekst nije pravni savjet i ne tvrdi da bilo koji dizajn, ljudski ili AI-generisan, jeste ili nije usklađen s bilo kojim od njih. Usklađenost je pravno pitanje, vezano za konkretnu jurisdikciju (ovdje govorimo o kontekstu EU) i traži kvalifikovanu pravnu procjenu. Ono što se iz istraživanja može reći jeste tehnički, ne pravni: prolazak automatske provjere ne znači da je proizvod stvarno upotrebljiv za sve korisnike. Pravni zaključci iz toga nisu na dizajneru niti na ovom tekstu.

## Ukus, kontekst i novina: sud o baš ovom proizvodu

Treći sloj slijepih tačaka nema veze ni sa sintaksom ni sa semantikom, nego s prosuđivanjem. Sawicki i saradnici testirali su tri modela s početka 2025. (GPT o3-mini-high, DeepSeek R1, Claude 3.5 Sonnet) na dizajnu grafičkih interfejsa. Nalaz: modeli proizvode kompetentne, uredno strukturirane rasporede, ali pokazuju "nedovoljnu svijest o kontekstu" i tek djelimično se prilagođavaju zadanoj personi korisnika.

Prevedeno na jezik dizajna: model zna kako izgleda dobar ekran uopšte. Ne zna nužno kako izgleda dobar ekran za baš ove korisnike, u baš ovom proizvodu, s baš ovim ograničenjima. Zna obrazac, ne kontekst. A većina stvarnih dizajnerskih odluka su odluke o kontekstu: ovaj tok je za korisnike pod stresom, ova funkcija je nova i zahtijeva objašnjenje, ovaj element krši očekivani obrazac namjerno jer smo u istraživanju vidjeli da tako bolje radi.

Ista granica važi za novinu i ukus. Model dobro reprodukuje ono što je često viđao. Nov obrazac interakcije, namjerno kršenje konvencije, procjena da li nešto djeluje elegantno ili trapavo, prosudba da li glas proizvoda odgovara publici, sve to izmiče modelu upravo zato što nije stvar pravila nego suda. Uz to, treba biti oprezan i s "sintetičkim korisnicima". Pristupi tipa PerceptUI (arXiv 2606.05697) nude persona-uslovljene **synthetic users** kao zamjenu za testiranje, ali tvrdnju da su "ljudski realistični" iznose sami autori i nije nezavisno potvrđena. Sintetički korisnik može simulirati prosjek; teško simulira baš vašeg korisnika.

## Kako ovo pretvoriti u tok rada

Zaključak nije "ne koristite AI za evaluaciju". Zaključak je da slojeve treba posložiti prema onome što svaki pouzdano radi, i nikad ne tražiti od sloja više nego što može.

Praktičan raspored izgleda ovako:

**Jeftina automatska kapija na ulazu.** axe, Lighthouse, provjere omjera kontrasta i strukture rasporeda. Ovo pušta ili odbija na osnovu mjerljivih pravila i hvata očigledne sintaksne propuste, nedostajuće atribute, pali kontrast, slomljen raspored. Jeftino je, pa neka radi na svakoj iteraciji.

**LLM-as-judge kao trijaža.** Ono što prođe kapiju, model može brzo pregledati i rangirati, izdvojiti kandidate koji zaslužuju ljudsku pažnju i označiti sumnjiva mjesta. Ovdje je tečnost modela prednost, jer trijaži ne treba savršenstvo, treba joj brzo sužavanje. Ali zapamtite šta pokazuje UXBench: pouzdanost varira po modelu i po kategoriji UI-ja, pa tretirajte izlaz kao prijedlog, ne kao ocjenu.

**Ljudska evaluacija na onome što nosi rizik.** Tu spadaju: potvrda pristupačnosti sa stvarnim pomoćnim tehnologijama i stvarnim korisnicima, ne samo linterom; novi obrasci interakcije; prilagođenost kontekstu i ciljevima korisnika; i ukus. Ovo se ne delegira modelu.

Jedno pravilo drži cijelu strukturu: **LLM-as-judge je trijaža, nikad potpis.** On sužava prostor koji ljudi trebaju pogledati; on ne zamjenjuje taj pogled. Onog trenutka kada model dobije zadnju riječ o tome je li nešto pristupačno, dobro ili spremno, uveli ste tečnu, uvjerljivu prazninu tačno na mjesto gdje vam treba prosudba.

Za dizajnera koji sutra dobije deset AI-generisanih ekrana, to znači konkretan refleks. Pustite alate da odbiju očigledno pokvarene. Pustite model da vam kaže gdje da prvo gledate. A onda gledajte sami, pogotovo tamo gdje je u pitanju značenje, kontekst i stvarni korisnik, jer su to upravo mjesta gdje sva tri sloja, a najviše model, najlakše prevare i vas i sebe.

## Izvori
- [UXBench: Measuring the Actionability of LLM-Generated UX Critiques (arXiv 2606.16262)](https://arxiv.org/abs/2606.16262)
- [Qualitative Evaluation of LLM-Designed GUI, Sawicki et al. (arXiv 2601.22759)](https://arxiv.org/abs/2601.22759)
- [Measuring the Semantic Accessibility Gap in LLM-Generated Web UIs, Calò et al., CHI 2026 Extended Abstracts (DOI 10.1145/3772363.3799364)](https://doi.org/10.1145/3772363.3799364)
- [PerceptUI: persona-conditioned synthetic users (arXiv 2606.05697)](https://arxiv.org/abs/2606.05697)
