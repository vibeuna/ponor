---
layout: post
title: "Kako provjeriti odgovor chatbota: šest navika"
date: 2026-10-12
category: ai-za-sve
image: /assets/images/2026-10-12-kako-provjeriti-ai-odgovor.svg
read_time: 7
description: "Šest navika za provjeru odgovora chatbota, poredanih po snazi dokaza: šta zaista pomaže, šta ne pomaže i gdje AI najčešće griješi."
tags: [llm]
---

Chatbot vam za dvije sekunde da odgovor, ime autora, naslov rada i poveznicu. Sve izgleda uredno. Problem je što uredan odgovor i tačan odgovor nisu isto, a chatbot ne pokazuje razliku. Istraživanja iz 2023–2025. pokazuju koje provjere imaju dokaze iza sebe, a koje samo djeluju umirujuće.

## Ukratko

Prema jednom još nerecenziranom radu, chatbotovi daju uvjerljive netačne odgovore uglavnom zato što ih način ocjenjivanja nagrađuje za pogađanje više nego za "ne znam". Po našoj procjeni, najkorisnija provjera je otvoriti izvor koji chatbot navede i pročitati ga: i kad je poveznica stvarna, tvrdnja često nije u izvoru. Slijedi provjera u nezavisnom izvoru. Ponovljeno pitanje u novom razgovoru pomoglo je otkriti izmišljeno u automatskim sistemima, ali nije ispitano na ljudima. Kod zadataka zaključivanja (reasoning) pitanje "jesi li siguran?" ne pomaže i može pokvariti tačan odgovor. Najveći rizik su rijetke i lokalne činjenice, pravo, medicina i svježi događaji.

## Zašto chatbot radije pogađa nego kaže "ne znam"

[Halucinacija](/rjecnik/halucinacija/) (izmišljanje netačnih informacija) nije rijedak kvar. [Istraživači OpenAI-ja i Georgia Techa](https://arxiv.org/abs/2509.04664v1) u radu iz septembra 2025. tvrde da je glavni uzrok način na koji se modeli ocjenjuju, a ne samo treniranje (training). To je preprint (rad koji još nije prošao recenziju), pa ga čitajte kao argument autora, ne kao utvrđenu činjenicu.

Argument je jednostavan. Na većini benchmarka (referentnih testova) tačan odgovor donosi bod, a "ne znam" i pogrešan odgovor donose nulu. Model koji pogađa zato prolazi bolje od modela koji priznaje da ne zna. Autori to najjasnije pokazuju na rijetkim činjenicama: ako se 20% datuma rođenja u podacima za treniranje pojavi samo jednom, očekuju da će model pogriješiti na barem petini takvih pitanja.

Brojke postoje, ali dolaze od samog proizvođača i brzo zastarijevaju. U sigurnosnoj dokumentaciji (system card) [za o3 i o4-mini iz aprila 2025.](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf) OpenAI navodi da je o3 halucinirao u trećini odgovora na benchmarku PersonQA, s pitanjima o osobama, o4-mini u 48%, a stariji o1 u 16%. U [system cardu za GPT-5 iz augusta 2025.](https://cdn.openai.com/gpt-5-system-card.pdf) OpenAI je mjerio netačne tvrdnje u stvarnim razgovorima u ChatGPT-u s uključenom pretragom interneta: 4,5% kod gpt-5-thinking, 9,6% kod gpt-5-main, 12,7% kod o3 i 12,9% kod GPT-4o. Odgovore je ocjenjivao OpenAI-jev vlastiti model, koji se s ljudskim ocjenjivačima slagao u 75% slučajeva. Od tada su izašli noviji modeli, a brojke s različitih mjerenja nisu međusobno uporedive.

## Šest navika, od najjače ka najslabijoj

Redoslijed je naša procjena, zasnovana na tome koliko je svaka navika provjerena i na kome.

{% include diagram.html name="kako-provjeriti-ai-odgovor" caption="Šest navika provjere, od najjačih dokaza prema najslabijim. Redoslijed je naša procjena." alt="Pet navika provjere odgovora chatbota poredanih po snazi dokaza, i šesta, pitanje jesi li siguran, označena kao da ne pomaže." %}

### 1. Otvorite izvor i pročitajte ga

Ako chatbot navede izvore, otvorite ih. Poveznica nije dokaz: to što izvor postoji ne znači da u njemu piše ono što chatbot tvrdi.

Bez pretrage chatbotovi često izmišljaju i same izvore. U [studiji iz 2023.](https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980/) GPT-3.5 je izmislio više od polovine od 636 provjerenih referenci, a GPT-4 skoro petinu. U [testu iz juna 2025.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395/) GPT-4o je izmislio otprilike svaku petu referencu, a skoro polovina stvarnih imala je greške.

Pretraga rješava jedan problem, ali ne i drugi. [Studija u časopisu Nature Communications](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003634/) nije našla izmišljene poveznice kod GPT-4o i Gemini s uključenom pretragom. Ipak, 50–90% odgovora nije bilo potpuno potkrijepljeno izvorima koje su sami naveli. Ni sam izvor nije uvijek tačno prepoznat. [Tow Center pri Columbia Journalism Review](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) dao je osam alata za pretragu koji koriste umjetnu inteligenciju (artificial intelligence, AI) odlomke iz novinskih članaka i tražio da prepoznaju članak: naslov, izdavača i poveznicu. Na 1.600 takvih zadataka alati su pogriješili u više od 60% slučajeva.

Ni objašnjenje chatbota nije pouzdana prečica. [U eksperimentu s 80 učesnika](https://arxiv.org/abs/2310.12558v2) ljudi koji su se oslanjali na objašnjenja chatbota bili su ukupno jednako tačni kao oni koji su koristili pretragu. Ali kad je objašnjenje bilo pogrešno, previše su mu vjerovali. Čitanje samih pronađenih tekstova bilo je sigurnije.

### 2. Provjerite u nezavisnom izvoru

Ne ostajte unutar odgovora i njegovih poveznica. Potražite istu tvrdnju negdje drugdje: na službenoj stranici institucije, u zakonu, u drugom mediju. [Jedna studija iz 2019.](https://purl.stanford.edu/yk133ht8603) posmatrala je kako profesionalni provjerivači činjenica procjenjuju nepoznatu stranicu. Oni brzo napuste stranicu i provjere ko stoji iza nje. Historičari i studenti čitali su stranicu od vrha do dna i lakše su bili zavedeni. Studija se nije bavila chatbotovima, ali ista navika važi i za njihove odgovore (naš zaključak).

### 3. Za činjenična pitanja tražite pretragu, ali joj ne vjerujte naslijepo

Ako chatbot može pretraživati internet, uključite to za činjenična pitanja. Studije o rijetkim činjenicama (vidi niže) pokazuju da tu pretraga pomaže više nego veći model. Ipak, i s pretragom greške ostaju česte. [EBU i BBC](https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants) su u maju i junu 2025. testirali besplatne verzije četiri chatbota na pitanjima o vijestima. Skoro polovina odgovora (45%) imala je barem jedan ozbiljan problem, najčešće s izvorima, a zatim s tačnošću.

### 4. Postavite isto pitanje ponovo i uporedite

Otvorite novi razgovor i pitajte isto. Ako se odgovori razlikuju u ključnoj činjenici, ta činjenica je sumnjiva. Metoda [SelfCheckGPT](https://arxiv.org/abs/2303.08896v3) (2023) zasniva se na istoj ideji: tvrdnje koje model ponavlja kroz više odgovora češće su tačne od onih koje se mijenjaju. Upozorenje: metoda je testirana automatski, na modelima iz 2023, a ne na ljudima koji ručno postavljaju pitanje ponovo. Slaganje odgovora također nije dokaz, jer model može dosljedno ponavljati istu grešku.

### 5. Razbijte tvrdnju na kratka zasebna pitanja

Umjesto "je li sve ovo tačno?", izdvojite jednu konkretnu tvrdnju i pitajte za nju posebno, najbolje u novom razgovoru. Metoda [Chain-of-Verification](https://arxiv.org/abs/2309.11495v2) (CoVe), zasnovana na toj ideji, otprilike je udvostručila udio tačnih stavki u odgovorima tipa "nabroji...". Radila je najbolje kad su pitanja za provjeru odgovarana odvojeno od prvog odgovora. I ovo je testirano na modelima iz 2023. u automatskom sistemu, ne na korisnicima.

### 6. Ne pitajte samo "jesi li siguran?"

Ova navika djeluje razumno, ali dokazi govore protiv nje. [Jedna studija](https://arxiv.org/abs/2310.01798v2) tražila je od modela da sami preispitaju svoje odgovore, bez ikakve nove informacije. GPT-3.5 je na zdravorazumskim pitanjima izgubio otprilike polovinu tačnih odgovora, jer je tačne mijenjao u netačne. GPT-4 je na matematičkim zadacima također bio lošiji nakon preispitivanja. Raniji radovi koji su pokazivali poboljšanje modelu su, prema autorima, posredno davali do znanja da je odgovor pogrešan. Rezultat važi za zadatke zaključivanja. Za činjenice savjetujemo navike 1, 2 i 5.

## Gdje greške najčešće nastaju

Rizik nije jednak za sva pitanja. Prema dostupnim studijama, budite najoprezniji kod:

- **Malo poznatih i lokalnih činjenica.** [Dvije](https://arxiv.org/abs/2212.10511v4) [studije](https://arxiv.org/abs/2211.08411v2) iz 2023. pokazale su da tačnost prati koliko se o nečemu piše. Za rijetke teme veći model jedva pomaže, a pretraga pomaže. Lokalna firma, općinska odluka ili manje poznata osoba u BiH spadaju u tu grupu (naša procjena).
- **Prava.** [Jedna studija](https://arxiv.org/abs/2401.01301v2) izmjerila je halucinacije u 58–88% odgovora na provjerljiva pitanja o američkim saveznim sudskim predmetima, zavisno od modela.
- **Medicine, posebno manje istraženih tema.** Ranije spomenuti test iz 2025. našao je 6% izmišljenih referenci za depresiju, a 28–29% za manje istražene poremećaje.
- **Rijetkih pojedinačnih podataka.** Za datume, imena i brojeve koji se u podacima za treniranje pojave samo jednom, autori rada o uzroku halucinacija predviđaju pogađanje. Provjerite svaki takav podatak na koji se oslanjate (naš savjet).
- **Svježih događaja.** EBU zastarjelu informaciju računa kao grešku u tačnosti. Model bez pretrage ne može znati šta se desilo nakon što su prikupljeni njegovi podaci za treniranje (naša napomena).

Za bosanski jezik nema studije koja ovo mjeri. Rezultati za druge jezike se razilaze. Studija [Multi-FAct](https://arxiv.org/abs/2402.18045v3) (devet jezika) našla je da su odgovori na engleskom dosljedno tačniji. [Druga, s 19 jezika](https://arxiv.org/abs/2410.18270v1), našla je više grešaka na [jezicima s malo resursa](/rjecnik/jezik-s-malo-resursa/) (low-resource language). [Treća, s 30 jezika uključujući srpski](https://arxiv.org/abs/2502.12769v4), nije našla vezu između učestalosti halucinacija, kad se uzme u obzir dužina odgovora, i količine teksta koja na jeziku postoji na internetu. EBU-ova studija nije uključila nijedan emiter s našeg govornog područja. Zato ne znamo griješe li chatbotovi više na bosanskom. Lokalne činjenice su ipak rijetke u podacima za treniranje, pa ih provjeravajte strože (naša procjena).

## Povezano

- [Kako napisati dobar prompt: jezik, situacija, oblik odgovora](https://www.ponor.ba/clanci/kako-napisati-dobar-prompt/) – dobar prompt daje bolji odgovor, ali ne garantuje tačan.
- [Šta je LLM i kako radi?](https://www.ponor.ba/clanci/sta-je-llm/) – kako model generiše tekst i zašto ne radi kao baza podataka.

## Izvori

- [Kalai i sar., Why Language Models Hallucinate (arXiv, 2025)](https://arxiv.org/abs/2509.04664v1)
- [OpenAI, o3 and o4-mini System Card (2025)](https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf)
- [OpenAI, GPT-5 System Card (2025)](https://cdn.openai.com/gpt-5-system-card.pdf)
- [Walters i Wilder, Scientific Reports (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10484980/)
- [Linardon i sar., JMIR Mental Health (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12658395/)
- [Wu i sar., An automated framework for assessing how well LLMs cite relevant medical references, Nature Communications (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12003634/)
- [Jaźwińska i Chandrasekar, AI Search Has a Citation Problem, Columbia Journalism Review (2025)](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php)
- [EBU i BBC, News Integrity in AI Assistants (2025)](https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants)
- [Si i sar., Large Language Models Help Humans Verify Truthfulness – Except When They Are Convincingly Wrong (NAACL 2024)](https://arxiv.org/abs/2310.12558v2)
- [Wineburg i McGrew, Lateral Reading and the Nature of Expertise, Teachers College Record (2019)](https://purl.stanford.edu/yk133ht8603)
- [Manakul i sar., SelfCheckGPT (EMNLP 2023)](https://arxiv.org/abs/2303.08896v3)
- [Dhuliawala i sar., Chain-of-Verification (Findings of ACL 2024)](https://arxiv.org/abs/2309.11495v2)
- [Huang i sar., Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)](https://arxiv.org/abs/2310.01798v2)
- [Mallen i sar., When Not to Trust Language Models (ACL 2023)](https://arxiv.org/abs/2212.10511v4)
- [Kandpal i sar., Large Language Models Struggle to Learn Long-Tail Knowledge (ICML 2023)](https://arxiv.org/abs/2211.08411v2)
- [Dahl i sar., Large Legal Fictions, Journal of Legal Analysis (2024)](https://arxiv.org/abs/2401.01301v2)
- [Shafayat i sar., Multi-FAct: Assessing Factuality of Multilingual LLMs using FActScore (arXiv, 2024)](https://arxiv.org/abs/2402.18045v3)
- [Chataigner i sar., Multilingual Hallucination Gaps in Large Language Models (arXiv, 2024)](https://arxiv.org/abs/2410.18270v1)
- [Islam i sar., How Much Do LLMs Hallucinate across Languages? (EMNLP 2025)](https://arxiv.org/abs/2502.12769v4)
