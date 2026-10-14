---
layout: post
title: "Koji AI najbolje prevodi na bosanski?"
date: 2026-10-14
category: ai-za-sve
image: /assets/images/2026-10-14-ai-prevod-bosanski.svg
read_time: 7
description: "DeepL, Google Translate ili ChatGPT? U našem testu s 20 rečenica kvalitet je sličan, a razlike se vide u hrvatskim i srpskim riječima, privatnosti i radu s dokumentima."
tags: [llm]
---

Treba vam prevod poslovnog pisma, uputstva ili poruke za rodbinu u inostranstvu. Na raspolaganju su vam DeepL, Google Translate i ChatGPT, i sva tri imaju besplatnu verziju. Koji izabrati?

## Ukratko

Kod kratkih, svakodnevnih tekstova razlika u kvalitetu je mala. U našem testu s 20 rečenica sva tri alata prevela su gotovo sve tačno, a nijedan se nije jasno izdvojio. U prevodu s bosanskog na engleski samo je Google pogriješio u značenju, ali taj dio testa imao je samo četiri rečenice. Prave razlike su drugdje: u hrvatskim i srpskim riječima (žlica, košara, istorija), u tome šta se dešava s tekstom koji zalijepite i u radu s dokumentima. Za kratku poruku poslužit će bilo koji alat, samo provjerite izbor riječi. Povjerljiv tekst ne lijepite u verziju koja ga koristi za treniranje. Ako prevodite cijeli dokument, DeepL najjasnije navodi šta besplatna verzija dozvoljava.

## Šta se poredi

- **DeepL** je alat za mašinsko prevođenje (machine translation). Njegova [dokumentacija za API (programski interfejs)](https://developers.deepl.com/docs/getting-started/supported-languages) navodi bosanski. U našem testu besplatna web verzija DeepL-a nudila je bosanski kao ciljni jezik.
- **Google Translate** ima bosanski na [listi podržanih jezika](https://translate.google.com/about/languages/). U decembru 2025. Google je [najavio](https://blog.google/products/search/gemini-capabilities-translation-upgrades/) prevođenje uz pomoć Geminija i opisao ga kao "state-of-the-art". Ta najava odnosi se na prevođenje između engleskog i "gotovo 20 jezika". Nova verzija prvo je pokrenuta u SAD-u i Indiji, a Google ne navodi bosanski među tim jezicima. Ne znamo koji sistem trenutno prevodi na bosanski.
- **ChatGPT** je chatbot zasnovan na [velikom jezičkom modelu](/rjecnik/veliki-jezicki-model/) (large language model, LLM). Nije namijenjen isključivo prevođenju, ali prevodi kad to od njega zatražite. Nismo pronašli nijednu OpenAI-jevu evaluaciju koja uključuje bosanski.

## Poređenje

### Kvalitet: naš test

Redakcija Ponora je 13. oktobra 2026. svim alatima dala istih 20 rečenica: 16 s engleskog na bosanski (službeni i tehnički tekst, idiomi, svakodnevni govor) i 4 s bosanskog na engleski. ChatGPT smo testirali dvaput: prvi put s kratkim [promptom](/rjecnik/prompt/) "Prevedi na bosanski:", a drugi put s uputom da koristi ijekavicu i bosanski standard, a ne hrvatski ili srpski. Aplikacija je kao model prikazivala "GPT-6". Koristili smo besplatne verzije, a svaki alat pokrenuli smo samo jednom.

Prevode je ocijenio urednik Ponora, izvorni govornik, ocjenama od 1 do 5 za tačnost (da li je značenje očuvano) i prirodnost (da li bi izvorni govornik tako napisao). Prevodi su bili izmiješani i bez oznake alata. Ipak, urednik je i sam pokretao testove, pa ocjenjivanje nije bilo potpuno naslijepo.

Ovaj test je ilustracija, a ne benchmark. Na osnovu jednog ocjenjivača, 20 rečenica i jednog prolaza alati se ne mogu rangirati. Isti alat sutra može dati drugačiji prevod.

| Postavka | Tačnost EN→BS | Prirodnost EN→BS | Hrvatske/srpske riječi | Tačnost BS→EN |
|---|---|---|---|---|
| DeepL | 5,00 | 4,44 | 2 (košaru, žlice) | 5,00 |
| Google Translate | 4,88 | 4,69 | 1 (istorije) | 4,25 |
| ChatGPT, kratki prompt | 4,94 | 4,56 | 0 | 5,00 |
| ChatGPT, s uputom | 4,94 | 4,62 | 1 (košaru) | 5,00 |

Prosjeci za EN→BS izračunati su na 16 rečenica, a za BS→EN na četiri. U prevodu s bosanskog na engleski oba ChatGPT pokušaja dala su identičan tekst.

Od 64 prevoda na bosanski, njih 59 dobilo je ocjenu 5 za tačnost. Kratke rečenice ne razdvajaju alate, a neki prevodi bili su identični od riječi do riječi. Razlika u prirodnosti između najboljeg i najslabijeg rezultata iznosi 0,25. Uz jednog ocjenjivača i 16 rečenica, to je premalo da bi nešto značilo.

Razlike su se pokazale u pojedinačnim riječima:

- "Where did you put the spoons?" DeepL: "Gdje si stavio **žlice**?" Ostali: "kašike".
- "Don't put all your eggs in one basket." DeepL i ChatGPT s uputom: "jednu **košaru**". Google i ChatGPT bez upute: "korpu".
- "...the history teacher was the only reason..." Google: "profesor **istorije**". Ostali: "historije".
- S bosanskog: "Hajde navrati na kahvu kad budeš imao vakta." Google: "Let's stop by for coffee when you have time", čime se mijenja ko kome dolazi. DeepL: "Come by for coffee when you have some free time."

{% include diagram.html name="ai-prevod-bosanski" caption="Riječi koje je urednik u našem testu označio kao hrvatske ili srpske, po alatu." alt="Tabela: tri engleske riječi i izbor riječi za četiri postavke. DeepL: žlice i košaru (hrvatski). Google Translate: istorije (srpski). ChatGPT s kratkim promptom: nema takvih riječi. ChatGPT s uputom: košaru (hrvatski)." %}

Dodatna uputa nije mjerljivo popravila ChatGPT-ove prevode. Promijenila je pojedine riječi, a prosječne ocjene ostale su gotovo iste. Štaviše, ChatGPT je uprkos uputi "ne hrvatski" napisao "košaru", iako je bez upute na istom mjestu napisao "korpu". U prevodu s bosanskog jedino je Google promašio značenje, ali četiri rečenice su premalo za zaključak.

Alati su ponekad dodavali i ono što niko nije tražio. ChatGPT je jednom dopisao objašnjenje ("Doslovno: 'Slomi nogu!'"). Google je jednom dodao "i popila", a u drugoj rečenici sam je izabrao ženski rod ("preživjela"), iako u originalu za to nije bilo nikakvog nagovještaja. To su sitnice, ali u službenom tekstu mogu biti važne.

### Kvalitet: objavljena istraživanja

Jedino direktno poređenje za bosanski koje smo pronašli potiče iz 2023. godine. [Robinson i saradnici](https://aclanthology.org/2023.wmt-1.40) mjerili su kvalitet prevoda s engleskog na bosanski na skupu rečenica FLORES-200, koristeći automatske mjere koje porede mašinski prevod s ljudskim. Google Translate postigao je 44,0 spBLEU, a OpenAI-jev gpt-3.5-turbo 40,0, i to bez primjera u promptu. Riječ je o starom modelu, a GPT-4 u toj studiji nije testiran na bosanskom.

Novije studije ne uključuju bosanski. Rezultate za srpski i hrvatski navodimo samo kao posredan pokazatelj, a ne kao dokaz za bosanski:

- Na takmičenju [WMT25](https://aclanthology.org/2025.wmt-1.22) ljudski ocjenjivači su za prevod s engleskog na srpski (ćirilica) dali Gemini-2.5-Pro 94,2, GPT-4.1 92,5, a anonimnom komercijalnom sistemu ONLINE-B 90,6. Kad je za srpski tražena latinica, dva komercijalna sistema su ipak 98–99% teksta napisala ćirilicom.
- [WMT24++](https://arxiv.org/abs/2502.12404) je testirao DeepL, Google Translate i GPT-4o na hrvatskom i srpskom. Veliki jezički modeli bili su na vrhu za svaki jezik. Kvalitet je mjeren samo automatski, a autori iz Googlea i sami upozoravaju da poređenje možda nije pošteno.

Nismo pronašli studiju o miješanju ekavice i ijekavice niti o gubljenju kvačica.

### Privatnost

Po našoj procjeni, ovdje su razlike veće nego kod kvaliteta. U nastavku prenosimo šta same kompanije navode o svojim uslugama. Te izjave ne govore o tome kako se zakoni o zaštiti podataka primjenjuju u BiH ili EU.

- **DeepL:** prema [politici privatnosti](https://www.deepl.com/en/privacy) (oktobar 2026), tekst unesen u besplatnu verziju obrađuje se "ograničeno vrijeme" i koristi se za [treniranje](/rjecnik/treniranje/) (training) i poboljšanje DeepL-ovih sistema. U Pro verziji tekst se briše nakon prevoda i ne koristi se za poboljšanje usluge.
- **ChatGPT:** OpenAI na [stranici pomoći](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance) navodi da se razgovori koriste za treniranje, osim ako to ne isključite u postavkama.
- **Google Translate:** za besplatni Google Translate nismo pronašli izjavu o tome da li se uneseni tekst koristi za treniranje. Googleova izjava za plaćeni Cloud Translation API ne odnosi se na besplatnu aplikaciju.

### Dokumenti, ograničenja i cijena

Prema [DeepL-ovoj stranici s planovima](https://www.deepl.com/en/pro) (njemačka verzija, cijene u eurima), u oktobru 2026. besplatna verzija DeepL Free omogućava prevod do 50.000 znakova i jednog dokumenta do 5 MB mjesečno. Pro Individual košta 7,49 eura mjesečno uz godišnje plaćanje. DeepL nudi i glosar, odnosno listu vlastitih prevoda za određene pojmove, ali ne i za bosanski.

Ograničenja i cijene za Google Translate i ChatGPT nismo mogli potvrditi iz primarnih izvora, pa ih ne navodimo.

## Kada izabrati šta

- **Kratka poruka ili pismo:** po našoj procjeni, poslužit će bilo koji od tri alata. Pročitajte prevod i obratite pažnju na riječi koje se razlikuju u bosanskom, hrvatskom i srpskom.
- **Povjerljiv tekst** (ugovor, zdravstveni podaci, poslovna prepiska): ne lijepite ga u besplatnu verziju koja tekst koristi za treniranje. DeepL navodi da Pro verzija briše tekst nakon prevoda. U ChatGPT-u prvo u postavkama isključite korištenje razgovora za treniranje. Za besplatni Google Translate nemamo potvrdu ni za jedno ni za drugo.
- **Cijeli dokument:** DeepL nudi prevođenje dokumenata i jasno navodi ograničenja besplatne verzije. Za druga dva alata ograničenja nismo uspjeli potvrditi.
- **Bosanski tekst s lokalizmima:** u našem testu svi alati su tačno razumjeli "kahvu" i "vakat", ali je Google pogrešno preveo ko kome dolazi. Kod takvog teksta provjerite značenje, a ne samo pojedine riječi.

## Šta se mijenja

- Nezavisno poređenje za bosanski s aktuelnim verzijama alata, više ocjenjivača i više teksta.
- Potvrda da li Google za bosanski koristi Gemini.
- Izmjene politike privatnosti kod bilo kojeg od tri alata.
- DeepL-ov glosar za bosanski, koji bi olakšao dosljednu terminologiju.
- Promjene ograničenja besplatnih verzija ili cijena.

## Povezano

- [Kako provjeriti odgovor chatbota: šest navika](https://www.ponor.ba/clanci/kako-provjeriti-ai-odgovor/) – iste navike važe i za provjeru prevoda.
- [Šta je LLM i kako radi?](https://www.ponor.ba/clanci/sta-je-llm/) – kako ChatGPT generiše tekst, pa i prevod.

## Izvori

- [DeepL, Supported languages (API dokumentacija)](https://developers.deepl.com/docs/getting-started/supported-languages)
- [DeepL, Privacy Policy (oktobar 2026)](https://www.deepl.com/en/privacy)
- [Google, Bringing state-of-the-art Gemini translation capabilities to Google Translate (2025)](https://blog.google/products/search/gemini-capabilities-translation-upgrades/)
- [OpenAI, How your data is used to improve model performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
- [Robinson i sar., ChatGPT MT: Competitive for High- (but not Low-) Resource Languages (WMT 2023)](https://aclanthology.org/2023.wmt-1.40)
- [Kocmi i sar., Findings of the WMT25 General Machine Translation Shared Task (WMT 2025)](https://aclanthology.org/2025.wmt-1.22)
- [Deutsch i sar., WMT24++: Expanding the Language Coverage of WMT24 to 55 Languages & Dialects (2025)](https://arxiv.org/abs/2502.12404)
