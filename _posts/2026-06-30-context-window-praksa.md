---
layout: post
title: "Kontekstni prozor u praksi: gdje modeli gube nit"
date: 2026-06-24
category: vodici
audience: developers
read_time: 7
description: "Prodavač kaže milijun tokena. Model ignoriše upravo onu informaciju iz sredine. Nije bug – to je osnovna karakteristika transformera. Kako to oblikuje arhitekturalne odluke."
diagram: /assets/diagrams/2026-06-30-context-window-praksa.svg
image: /assets/images/2026-06-30-context-window-praksa.svg
---

Ponuđač kaže da model podržava milijun tokena. Vi napunite kontekst, pokrenete query - i odgovor izostavi upravo onu informaciju koju ste stavili u sredinu. Nije bug u vašem kodu. To je osnovna karakteristika kako transformeri obrađuju duge kontekste.

Ovaj tekst pretpostavlja da znate što je kontekstni prozor (context window) i koliko su veliki današnji prozori. Pitanje ovdje nije veličina - nego šta se zapravo dešava unutar tog prostora, i kako to oblikuje arhitekturalne odluke u LLM aplikacijama.

## Izgubljeno u sredini

Studija "Lost in the Middle" (Liu i dr., 2023, TACL) ispitala je kako GPT-3.5-turbo-16k, GPT-4, Claude 1.3 i nekoliko open-source modela koriste informacije u dugim kontekstima. Eksperiment je bio precizan: 20 dokumenata, jedan tačan odgovor, a pozicija tog dokumenta varira od prvog do zadnjeg mjesta.

Rezultat prati U-krivu. Kada je relevantan dokument na prvoj poziciji, tačnost prelazi 70%. Kada je na zadnjoj, tačnost ostaje visoka. Kada je u sredini - pada ispod 50%. Razlika između najboljeg i najgoreg slučaja iznosi otprilike 20 procentnih poena, konzistentno kroz sve testirane modele.

Mehanizam je u mehanizmu pažnje (attention mechanism): tokom treninga, modeli su češće vidjeli relevantne informacije na početku ili kraju sekvenci. Tokeni iz srednjeg dijela konteksta primaju proporcionalno manje pažnje tokom generiranja odgovora - efektivno su prisutni u KV (Key-Value) cache-u, ali se rjeđe "konsultuju".

Praktična posljedica: puni kontekstni prozor nije ravnopravna memorija. To je prostor s jačim i slabijim zonama.

{% include diagram.html name="2026-06-30-context-window-praksa" caption="Tačnost modela pada kada se relevantan dokument nalazi u sredini konteksta – pozicije 1 i 20 su pouzdane, sredina nije." alt="Bar chart showing U-shaped accuracy curve across 5 document positions in a 20-document context window" %}

## Efektivni vs. nominalni prozor

Vendori objavljuju maksimalnu veličinu prozora. Efektivno iskorišten prozor - tamo gdje model dosljedno koristi sve što je ubačeno - manji je. Prema procjenama iz prakse (jednog praktičara, bez objavljene metodologije, uzet kao smjer a ne kao tačan broj): efektivna iskoristivost kreće se između 30 i 60% nominalne veličine.

Postoji i sintetički benchmark koji ovo čini vidljivim: needle-in-a-haystack testovi mjere može li model pronaći jedan podatak zakopan u dugom tekstu. Tačnost na tim testovima - koji traže jednu činjenicu - može biti visoka. Ali realistični upiti koji zahtijevaju sintezu više informacija istovremeno pokazuju značajan pad već pri manjim punjenjima konteksta.

Zaključak za dizajn sistema: ne oslanjajte se na nominalni limit. Projektujte za efektivni kapacitet.

## RAG vs. dugi kontekst: okvir za odlučivanje

Kada biramo između RAG-a (retrieval-augmented generation) i direktnog punjenja konteksta, pet je relevantnih faktora:

**1. Veličina korpusa.** Ako je baza znanja veća od onoga što stane u prozor - RAG je jedina opcija. Ako stane, direktni kontekst je tehnički moguć.

**2. Omjer relevantnosti.** Koliko posto ubačenog sadržaja je zapravo relevantno za dati query? Ako je omjer nizak (npr. 5 od 100 dokumenata), punite procesor šumom i aktivirate 'lost in the middle' efekat. RAG koji dohvaća samo relevantan sadržaj daće bolje rezultate.

**3. Kašnjenje.** RAG pipeline koji uključuje dohvatanje (retrieval), reranking i rekonstrukciju konteksta može dodati kašnjenje, ali inferencija nad kratkim kontekstom je brža nego nad dugim. Direktno punjenje dugog konteksta gotovo uvijek znači sporiji odgovor.

**4. Svježina podataka.** RAG indeks se može ažurirati neovisno od modela. Ako se podaci mijenjaju svakodnevno, RAG je prirodniji pristup. Ako je korpus stabilan, razlika nestaje.

**5. Volumen query-ja.** Kod visoko-frekvencijskih sistema, trošak tokena pri svakom pozivanju direktno udara po budžetu. Ovdje treba kvantificirati.

## Troškovni model

Trošak nije linearan sa veličinom konteksta - on je proporcionalan broju tokena koji prolaze kroz model pri svakoj inferenciji. Svaki turn u multi-turn razgovoru ponovo šalje cijeli akumulirani kontekst.

Procjene iz prakse (iz praktičarskih izvora bez nezavisne verifikacije, uzeti kao ilustracija reda veličine):

| Pristup | Trošak po queryu | Latencija |
|---|---|---|
| RAG (tipičan) | ~$0.00008 | ~1s |
| Dugi kontekst (tipičan) | $0.20–$2.00 | 20–60s |

Razlika može biti više redova veličine. Konkretni brojevi zavise od modela, providera i veličine prozora - ali smjer je konzistentan: dugi kontekst je skuplji i sporiji od dobro dizajniranog dohvatanja.

**Prompt caching** (koji nude Anthropic i drugi) amortizuje dio ovog troška za statični sadržaj koji se ponavlja između poziva - npr. dugačak system prompt ili nepromijenjena dokumentacija. Ono nije rješenje za dinamični sadržaj koji se mijenja između turnova.

**Progressive summarization** (tehnika kompresije starijih turnova u sažetke) je tehnika za upravljanje kontekstom u dugim sesijama: umjesto da stariji turnovi ostaju cijeli u prozoru, komprimuju se u kratke sažetke. Prema iskustvima iz prakse, ovo smanjuje potrošnju tokena po sesiji za 40–60%, uz minimalan gubitak relevantnih informacija. Kompromis: sažetak gubi preciznost detalja - što može biti bitno u aplikacijama gdje svaki detalj prethodnog dijaloga ima težinu.

## Arhitekturalne implikacije: kratak vodič

Ono što iz ovoga slijedi za svakodnevni razvoj:

**Ubacujte važne informacije na rubove konteksta.** Ključne instrukcije, najvažniji dokumenti i zadnji korisnički upit idu na početak ili kraj. Sredina je nesigurna zona.

**Mjerite efektivni kapacitet.** Pokrenite needle-in-a-haystack testove na svom konkretnom modelu s vašim konkretnim podacima. Nemojte pretpostavljati da nominalni limit opisuje stvarno ponašanje.

**Koristite RAG za selektivnost, ne samo za skaliranje.** Čak i kada cijeli korpus stane u kontekst, RAG koji dohvaća samo relevantan sadržaj može dati bolje rezultate od punjavanja svega - jer smanjuje šum.

**Pratite trošak po sesiji, ne samo po pozivu.** U multi-turn aplikacijama, cjelokupan trošak tokena raste brzo bez aktivnog upravljanja kontekstom.

**Kombinirajte pristupe.** Hibridna arhitektura - RAG za dohvatanje, dugi kontekst za sintezu - daje fleksibilnost bez potpunog oslanjanja na jedan mehanizam. Kratki, relevantni chunkovi ubacuju se u kontekst, ali na promišljene pozicije.

## Šta ovo nije

Nominalni prozor od milijun tokena nije garancija da će model pouzdano koristiti sve što stoji unutar njega. To je tehnički limit, ne opis pouzdanog ponašanja. Vendorske tvrdnje o veličini prozora opisuju šta model može primiti - ne šta može dosljedno iskoristiti.

Niti je 'lost in the middle' efekat riješen jednim trikovanjem s pozicijom. To je uvid o distribuciji pažnje, a ta distribucija se razlikuje između modela, između zadataka, i između dužina konteksta. Pretvaranje ovog uvida u konkretne arhitekturalne odluke zahtijeva testiranje na vašem specifičnom slučaju upotrebe.

## Izvori

- [Liu i dr. (2023), "Lost in the Middle: How Language Models Use Long Contexts", TACL](https://arxiv.org/abs/2307.03172)
- [Tian Pan (2026), "Long Context vs. RAG: Production Decision Framework"](https://tianpan.co/blog/2026-04-09-long-context-vs-rag-production-decision-framework)
- ["Long Context vs. RAG for LLMs: An Evaluation and Revisits" (2025)](https://arxiv.org/abs/2501.01880)
