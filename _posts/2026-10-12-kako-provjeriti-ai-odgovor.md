---
layout: post
title: "Kako provjeriti odgovor chatbota: šest navika"
date: 2026-10-12
category: ai-za-sve
image: /assets/images/2026-10-12-kako-provjeriti-ai-odgovor.svg
read_time: 7
description: "Šest navika za provjeru odgovora chatbota, poredanih po snazi dokaza: šta zaista pomaže, šta ne i gdje AI najčešće griješi."
tags: [llm]
---

Chatbot vam za dvije sekunde ponudi odgovor, ime autora, naslov rada i poveznicu. Sve izgleda uredno. Ali uredan odgovor nije nužno i tačan, a chatbot vam razliku neće pokazati. Istraživanja od 2023. do 2025. pokazuju koje provjere zaista imaju uporište u dokazima, a koje samo umiruju.

## Ukratko

Prema jednom radu koji još nije recenziran, chatbotovi daju uvjerljive, a netačne odgovore uglavnom zato što ih način ocjenjivanja više nagrađuje za pogađanje nego za "ne znam". Po našoj procjeni, najkorisnije je otvoriti izvor koji chatbot navede i pročitati ga. Čak i kad poveznica postoji, tvrdnje u izvoru često nema. Odmah iza toga dolazi provjera u nezavisnom izvoru. Ponavljanje pitanja u novom razgovoru pomoglo je automatskim sistemima da otkriju izmišljene tvrdnje, ali to nije ispitano na ljudima. Kod zadataka zaključivanja (reasoning) pitanje "jesi li siguran?" ne pomaže, a može i pokvariti tačan odgovor. Najrizičnije su rijetke i lokalne činjenice, pravo, medicina i nedavni događaji.

## Zašto chatbot radije pogađa nego kaže "ne znam"

[Halucinacija](/rjecnik/halucinacija/) (izmišljanje netačnih informacija) nije rijedak kvar. [Istraživači OpenAI-ja i Georgia Techa](https://arxiv.org/abs/2509.04664v1) u radu iz septembra 2025. tvrde da je glavni uzrok način na koji se modeli ocjenjuju, a ne samo način na koji se treniraju (training). To je preprint (rad koji još nije prošao recenziju), pa ga čitajte kao argument autora, a ne kao utvrđenu činjenicu.

Argument je jednostavan. Na većini benchmarka (referentnih testova) tačan odgovor donosi bod, a "ne znam" i pogrešan odgovor donose nulu. Model koji pogađa zato bolje prolazi od modela koji priznaje da ne zna. Najjasniji primjer su rijetke činjenice. Ako se 20% datuma rođenja u podacima za treniranje pojavi samo jednom, autori očekuju da će model pogriješiti na barem petini takvih pitanja.

Konkretne brojke postoje, ali ih objavljuje sam proizvođač i brzo zastarijevaju. U sigurnosnoj dokumentaciji (system card) [za o3 i o4-mini iz aprila 2025.](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf) OpenAI navodi rezultate na benchmarku PersonQA, koji sadrži pitanja o osobama. Model o3 halucinirao je u trećini odgovora, o4-mini u 48%, a stariji o1 u 16%. U [system cardu za GPT-5 iz augusta 2025.](https://cdn.openai.com/gpt-5-system-card.pdf) OpenAI je mjerio netačne tvrdnje u stvarnim razgovorima u ChatGPT-u s uključenom pretragom interneta: 4,5% kod gpt-5-thinking, 9,6% kod gpt-5-main, 12,7% kod o3 i 12,9% kod GPT-4o. Odgovore je ocjenjivao OpenAI-jev vlastiti model, koji se s ljudskim ocjenjivačima slagao u 75% slučajeva. Od tada su izašli noviji modeli, a brojke s različitih mjerenja nisu međusobno uporedive.

## Šest navika, od najjače do najslabije

Redoslijed je naša procjena. Zasnovan je na tome koliko je svaka navika ispitana i na kome.

{% include diagram.html name="kako-provjeriti-ai-odgovor" caption="Šest navika provjere, od najjačih dokaza do najslabijih. Redoslijed je naša procjena." alt="Pet navika provjere odgovora chatbota, poredanih po snazi dokaza, i šesta navika, pitanje jesi li siguran, označena kao nekorisna." %}

### 1. Otvorite izvor i pročitajte ga

Ako chatbot navede izvore, otvorite ih. Poveznica sama po sebi nije dokaz. To što izvor postoji ne znači da u njemu piše ono što chatbot tvrdi.

Bez pretrage chatbotovi često izmišljaju i same izvore. U [studiji iz 2023.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980/), u kojoj je provjereno 636 referenci, GPT-3.5 je izmislio više od polovine svojih referenci, a GPT-4 skoro petinu. U [testu iz juna 2025.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395/) GPT-4o je izmislio otprilike svaku petu referencu, a skoro polovina stvarnih referenci sadržavala je greške.

Pretraga rješava jedan problem, ali ne i drugi. [Studija u časopisu Nature Communications](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003634/) nije našla izmišljene poveznice kod GPT-4o i Geminija s uključenom pretragom. Ipak, 50–90% odgovora nije bilo u potpunosti potkrijepljeno izvorima koje su modeli sami naveli. Alati ni sam izvor ne prepoznaju uvijek tačno. [Tow Center pri Columbia Journalism Review](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) testirao je osam alata za pretragu zasnovanih na umjetnoj inteligenciji (artificial intelligence, AI). Alati su dobili odlomke iz novinskih članaka i trebali su navesti naslov članka, izdavača i poveznicu. Na 1.600 takvih zadataka pogriješili su u više od 60% slučajeva.

Ni chatbotovo objašnjenje nije pouzdana prečica. [U eksperimentu s 80 učesnika](https://arxiv.org/abs/2310.12558v2) oni koji su se oslanjali na objašnjenja chatbota bili su ukupno jednako tačni kao oni koji su koristili pretragu. Ali kad je objašnjenje bilo pogrešno, previše su mu vjerovali. Sigurnije je bilo čitati same pronađene tekstove.

### 2. Provjerite u nezavisnom izvoru

Nemojte se zadržati samo na odgovoru i njegovim poveznicama. Potražite istu tvrdnju negdje drugdje: na službenoj stranici institucije, u zakonu, u drugom mediju. [Jedna studija iz 2019.](https://purl.stanford.edu/yk133ht8603) posmatrala je kako profesionalni provjerivači činjenica procjenjuju nepoznatu stranicu. Oni brzo napuste stranicu i provjere ko stoji iza nje. Historičari i studenti čitali su stranicu od vrha do dna i lakše su nasjedali. Studija se nije bavila chatbotovima, ali smatramo da ista navika vrijedi i za njihove odgovore.

### 3. Za činjenična pitanja uključite pretragu, ali joj ne vjerujte naslijepo

Ako chatbot može pretraživati internet, uključite tu opciju za činjenična pitanja. Studije o rijetkim činjenicama (vidi niže) pokazuju da kod njih pretraga pomaže više od većeg modela. Ipak, greške su česte i s pretragom. [EBU i BBC](https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants) su u maju i junu 2025. testirali besplatne verzije četiri chatbota na pitanjima o vijestima. Skoro polovina odgovora (45%) imala je barem jedan ozbiljan problem, najčešće s izvorima, a zatim s tačnošću.

### 4. Postavite isto pitanje ponovo i uporedite

Otvorite novi razgovor i postavite isto pitanje. Ako se odgovori razlikuju u ključnoj činjenici, ta činjenica je sumnjiva. Metoda [SelfCheckGPT](https://arxiv.org/abs/2303.08896v3) (2023) zasniva se na istoj ideji: tvrdnje koje model ponavlja u više odgovora češće su tačne od onih koje se mijenjaju. Ali oprez: metoda je testirana automatski, na modelima iz 2023, a ne na ljudima koji sami ponovo postavljaju pitanje. Ni slaganje odgovora nije dokaz, jer model može uporno ponavljati istu grešku.

### 5. Rastavite odgovor na pojedinačne tvrdnje

Umjesto "je li sve ovo tačno?", izdvojite jednu konkretnu tvrdnju i pitajte samo za nju, najbolje u novom razgovoru. Metoda [Chain-of-Verification](https://arxiv.org/abs/2309.11495v2) (CoVe), zasnovana na toj ideji, otprilike je udvostručila udio tačnih stavki u odgovorima tipa "nabroji...". Najbolje je radila kad je model na kontrolna pitanja odgovarao odvojeno od prvog odgovora. I ova metoda je testirana automatski, na modelima iz 2023, a ne na korisnicima.

### 6. Ne pitajte samo "jesi li siguran?"

Ova navika djeluje razumno, ali dokazi govore protiv nje. U [jednoj studiji](https://arxiv.org/abs/2310.01798v2) modeli su trebali sami preispitati svoje odgovore, bez ikakve nove informacije. Na zdravorazumskim pitanjima GPT-3.5 je izgubio otprilike polovinu tačnih odgovora jer ih je mijenjao u netačne. I GPT-4 je nakon preispitivanja bio lošiji na matematičkim zadacima. Prema autorima, raniji radovi koji su pokazali poboljšanje modelu su posredno davali do znanja da je odgovor pogrešan. Ovaj rezultat vrijedi za zadatke zaključivanja. Za provjeru činjenica preporučujemo navike 1, 2 i 5.

## Gdje greške najčešće nastaju

Rizik nije jednak za sva pitanja. Prema dostupnim studijama, budite najoprezniji kod:

- **Malo poznatih i lokalnih činjenica.** [Dvije](https://arxiv.org/abs/2212.10511v4) [studije](https://arxiv.org/abs/2211.08411v2) iz 2023. pokazale su da tačnost zavisi od toga koliko se o nekoj temi piše. Kod rijetkih tema veći model jedva da pomaže, a pretraga pomaže. Po našoj procjeni, u tu grupu spadaju lokalna firma, općinska odluka ili manje poznata osoba u BiH.
- **Prava.** [Jedna studija](https://arxiv.org/abs/2401.01301v2) izmjerila je halucinacije u 58–88% odgovora na provjerljiva pitanja o američkim saveznim sudskim predmetima, zavisno od modela.
- **Medicine, posebno manje istraženih tema.** Ranije spomenuti test iz 2025. našao je 6% izmišljenih referenci za depresiju, a 28–29% za manje istražene poremećaje.
- **Rijetkih pojedinačnih podataka.** Za datume, imena i brojeve koji se u podacima za treniranje pojave samo jednom, autori rada o uzrocima halucinacija predviđaju da će model pogađati. Savjetujemo da provjerite svaki takav podatak na koji se oslanjate.
- **Nedavnih događaja.** EBU zastarjele informacije računa kao grešku u tačnosti. Napominjemo da model bez pretrage ne može znati šta se desilo nakon prikupljanja njegovih podataka za treniranje.

Nijedna studija ovo nije mjerila za bosanski jezik. Rezultati za druge jezike nisu jednoznačni. Studija [Multi-FAct](https://arxiv.org/abs/2402.18045v3) (devet jezika) našla je da su odgovori na engleskom dosljedno tačniji. [Druga, s 19 jezika](https://arxiv.org/abs/2410.18270v1), našla je više grešaka na [jezicima s malo resursa](/rjecnik/jezik-s-malo-resursa/) (low-resource language). [Treća, s 30 jezika, uključujući srpski](https://arxiv.org/abs/2502.12769v4), nije našla vezu između učestalosti halucinacija i količine teksta koja na nekom jeziku postoji na internetu, kad se uzme u obzir dužina odgovora. EBU-ova studija nije uključila nijednog emitera s našeg govornog područja. Zato ne znamo griješe li chatbotovi više na bosanskom. Ipak, lokalnih činjenica u podacima za treniranje ima malo, pa ih po našoj procjeni treba provjeravati strože.

## Povezano

- [Kako napisati dobar prompt: jezik, situacija, oblik odgovora](https://www.ponor.ba/clanci/kako-napisati-dobar-prompt/) – dobar prompt daje bolji odgovor, ali ne garantuje i tačan.
- [Šta je LLM i kako radi?](https://www.ponor.ba/clanci/sta-je-llm/) – kako model generiše tekst i zašto ne radi kao baza podataka.

## Izvori

- [Kalai i sar., Why Language Models Hallucinate (arXiv, 2025)](https://arxiv.org/abs/2509.04664v1)
- [Wu i sar., An automated framework for assessing how well LLMs cite relevant medical references, Nature Communications (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003634/)
- [EBU i BBC, News Integrity in AI Assistants (2025)](https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants)
- [Manakul i sar., SelfCheckGPT (EMNLP 2023)](https://arxiv.org/abs/2303.08896v3)
- [Huang i sar., Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)](https://arxiv.org/abs/2310.01798v2)
- [Mallen i sar., When Not to Trust Language Models (ACL 2023)](https://arxiv.org/abs/2212.10511v4)
- [Islam i sar., How Much Do LLMs Hallucinate across Languages? (EMNLP 2025)](https://arxiv.org/abs/2502.12769v4)
