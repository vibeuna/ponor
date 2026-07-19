---
layout: post
title: "Šta su veliki jezički modeli i kako ih koristiti"
date: 2026-06-28
category: vodici
audience: general
read_time: 7
description: "ChatGPT, Claude, Gemini - svi su izgrađeni na velikom jezičkom modelu. Šta je to, kako radi, i zašto ponekad griješi?"
diagram: /assets/diagrams/2026-06-28-sta-su-veliki-jezicki-modeli.svg
image: /assets/images/2026-06-28-sta-su-veliki-jezicki-modeli.svg
---

Upisali ste pitanje u ChatGPT i dobili povezan, uvjerljiv odgovor. Ali šta se zapravo desilo ispod površine? Iza svake te interakcije stoji veliki jezički model (large language model, LLM) - softverski sistem koji, u osnovi, predviđa koji tekst treba da dođe sljedeći. Razumijevanje tog mehanizma mijenja i to kako ćete ga koristiti i koliko ćete mu vjerovati.

## LLM: šta je to?

Veliki jezički model (large language model, LLM) je softverski sistem treniran da predvidi najvjerovatniji nastavak teksta na osnovu svega što je do tog trenutka napisano. To je osnovna mehanika - sve ostalo iz toga proizilazi.

Naziv "veliki" odnosi se na razmjer: modeli se treniraju s milijardama numeričkih parametara koji se prilagođavaju tokom treninga. ChatGPT, Claude i Gemini su primjeri chatbotova izgrađenih na ovakvim modelima. Bitna razlika: LLM je tehnologija koja stoji ispod; chatbot je produkt koji korisnik vidi. Isti LLM može napajati chatbot, API za programere i alat ugrađen u drugi softver.

LLM-ovi ne pretražuju internet u realnom vremenu (osim ako im se to eksplicitno omogući kao posebna funkcija), ne znaju za događaje nakon svog datuma treninga, i ne pamte prethodne razgovore po defaultu.

## Kako se modeli treniraju?

Trening velikog jezičkog modela prolazi kroz nekoliko faza.

**Pretrening.** Model čita ogromne količine teksta - knjige, web stranice, naučne radove, kod - i uči statističke obrasce: koje riječi prate koje, kako su rečenice strukturirane, koje činjenice se pojavljuju u tekstu. Uči jednostavnom metodom: predvidi sljedeću riječ, provjeri je li bila tačna, ispravi greške. Ovaj proces se ponavlja milijardama puta na hiljadama grafičkih procesora tokom sedmica ili mjeseci. Rezultat je model koji može koherentno nastaviti bilo koji tekst, ali još nije koristan kao asistent.

**Fino podešavanje (fine-tuning).** Bazni model iz pretreninga generiše tekst, ali ne slijedi uputstva. Fino podešavanje trenira model na manjim, visokokvalitetnim skupovima podataka s primjerima ljudski napisanih odgovora na pitanja i zahtjeve. Ovdje model uči da odgovara na pitanja, prati instrukcije i ponaša se kao asistent.

**Učenje iz povratne informacije.** U zadnjoj fazi, ljudski ocjenjivači evaluiraju odgovore modela i ocjenjuju koji su bolji. Model uči da proizvodi odgovore koje ljudi preferiraju - tačnije, korisnije, sigurnije. Ova faza je razlog zašto modeli obično odgovaraju pristojno i izbjegavaju štetne sadržaje.

## Tokeni i tokenizacija

LLM ne procesuira tekst slovo po slovo niti riječ po riječ. Procesuira tokene: token (osnovna jedinica teksta koju model procesuira) je tipično komad od nekoliko slova ili cijela kratka riječ, ne uvijek čitava riječ. Tokenizacija (tokenization) je proces razbijanja ulaznog teksta na te komade.

Token je najčešće komad riječi: na engleskom, 1.000 riječi odgovara otprilike 750 tokena. Slavenski jezici, uključujući bosanski, tokenizuju manje efikasno - zbog deklinacija i kompleksnije morfologije, ista poruka u bosanskom tipično zahtijeva više tokena nego njen engleski ekvivalent.

{% include diagram.html name="2026-06-28-sta-su-veliki-jezicki-modeli" caption="Tekst se razbija na tokene; tokeni pune kontekstni prozor; model predviđa sljedeći token na osnovu svega u prozoru." alt="Dijagram tokenizacije i kontekstnog prozora" %}

**Zašto vas to zanima kao korisnika?** Dva razloga. Prvo, komercijalni API-ji naplaćuju obradu po tokenima. Drugo - i važnije za svakodnevnu upotrebu - model ima ograničen broj tokena koje može "vidjeti" odjednom.

## Kontekstni prozor: radna memorija modela

Kontekstni prozor (context window) je maksimalan broj tokena koji model može procesirati u jednoj interakciji. Sve izvan tog prozora modelu je nevidljivo - nema sjećanja na prethodne razgovore osim onih koji su eksplicitno uključeni u trenutni kontekst.

Prozori se razlikuju po modelu: stariji GPT-3.5 je imao oko 4.000 tokena (otprilike 3.000 riječi). Prema specifikacijama iz juna 2026., GPT-4o ima 128.000 tokena; Claude 3.5 Sonnet i Haiku 200.000 tokena; Gemini 1.5 Pro doseže milion tokena.

Ali veći kontekstni prozor ne garantuje savršeno procesuiranje. Istraživanja pokazuju da modeli bolje obrađuju informacije na početku i kraju konteksta nego one zakopane u sredini dugih unosa - fenomen koji se u literaturi naziva "izgubljen u sredini" (lost in the middle). Dugačak kontekst je korisna opcija, ali ne zamjena za dobro strukturiran upit.

## Kako koristiti LLM-ove efektivno

**Budite konkretni.** "Napiši profesionalni email kojim odbijam sastanak" daje bolji rezultat od "napiši email." Što više konteksta dajete, to je izlaz precizniji.

**Recite ko ste i šta vam treba.** "Ja sam nastavnica koja priprema sat za učenike od deset godina. Objasni fotosintezu jednostavno." Informacija o vašoj ulozi i cilju dramatično poboljšava odgovor.

**Dijelite složene zadatke na korake.** Umjesto da tražite cijeli dokument odjednom, tražite prvo strukturu, pa sekciju po sekciju. Iteracija daje bolje rezultate od jednog sveobuhvatnog prompta.

**Provjeravajte činjenice.** Halucinacija (hallucination) - pojava gdje LLM generiše uvjerljive, ali netačne informacije s punim samopouzdanjem - nije rijedak kvar koji čeka ispravku: to je fundamentalno ograničenje načina na koji ovi modeli funkcionišu. Nikada ne vjerujte LLM-u za specifične datume, statistike, citiranu literaturu ili pravne i medicinske detalje bez nezavisne provjere.

**Koristite kontekstni prozor namjerno.** Ulijepite relevantne dokumente, emailove ili pozadinske informacije u razgovor. Model koristi samo ono što je u prozoru - ako mu ne date relevantne informacije, popunit će praznine nagađanjem.

## Šta LLM-ovi nisu

**Nisu pretraživači.** LLM ne pronalazi dokumente - generira tekst na osnovu onoga što je naučio tokom treninga. Kada odgovara na pitanje o nekom događaju, ne pretražuje web; rekonstruira vjerovatni odgovor iz statističkih obrazaca.

**Ne "razumiju" u ljudskom smislu.** LLM nema ciljeve, uvjerenja niti razumijevanje. To je sofisticirani sistem za dopunjavanje uzoraka koji na osnovu prethodnog teksta predviđa što bi trebalo doći sljedeće. Rezultati mogu biti impresivni; mehanizam je matematički, ne mentalni.

**Nisu nepogrešivi.** Halucinacije su norma, ne iznimka. Kalibrišite povjerenje u skladu s tim: LLM je koristan za generisanje nacrta, brainstorming, sažimanje teksta koji sami imate pred sobom i objašnjavanje pojmova - manje pouzdan za pronalaženje provjerenih činjenica bez dodatne provjere.

**Ne čitaju vaše misli.** Neodređeni promptovi daju generičke odgovore. Specifičnost je vaša osnovna poluga kao korisnika.

## Izvori

- Brown et al. (2020). *Language Models are Few-Shot Learners.* [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) – Temeljni GPT-3 rad koji je postavio osnovu za modernu eru LLM-ova.
- Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* [arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172) – Stanford istraživanje o ograničenjima dugih kontekstnih prozora.
- Anthropic. *Claude model documentation.* [anthropic.com/claude](https://www.anthropic.com/claude)
