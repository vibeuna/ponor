---
layout: post
title: "RAG je dao pogrešan odgovor. Evo redoslijeda kojim to dijagnosticirate"
date: 2026-07-14
category: vodici
audience: developers
read_time: 6
description: "Prvi instinkt je da dodate reranker ili povećate top-k. Prije nego što bilo šta promijenite: sedam mehanički različitih tačaka kvara u RAG pipeline-u, i redoslijed kojim ih provjeravate."
diagram: /assets/diagrams/rag-failure-modes.svg
image: /assets/images/2026-07-14-rag-failure-modes.svg
---

RAG (retrieval-augmented generation) sistem je upravo vratio pogrešan ili nepotpun odgovor. Prvi instinkt je da se doda reranker, promijeni embedding model ili poveća top-k. Taj instinkt je problem: prema [Barnett i dr. (2024)](https://arxiv.org/html/2401.05856v1), postoji najmanje sedam mehanički različitih tačaka kvara u RAG pipeline-u, i svaka zahtijeva drugačiji popravak. Prije nego što bilo šta promijenite, treba znati koja je tačka zapravo kriva - inače popravljate simptom nasumično, a pravi uzrok ostaje.

## Zašto je redoslijed bitan

RAG pipeline ima jasan tok podataka: korpus → index → dohvatanje (retrieval) → sklapanje konteksta → generisanje odgovora. Svaki korak može otkazati na svoj način, i kvar nizvodno može izgledati identično kvaru uzvodno - pogrešan odgovor izgleda kao "halucinacija (hallucination)" bez obzira da li je uzrok to što odgovor nikad nije bio dostupan modelu ili to što ga je model imao pred sobom i ipak zeznuo. Zato dijagnostiku vodite od korpusa prema generisanju, ne obrnuto.

{% include diagram.html name="rag-failure-modes" caption="Sedam koraka dijagnoze, mapirano na RAG pipeline - od korpusa do odgovora." alt="Dijagram RAG pipeline-a sa sedam obilježenih tačaka kvara (K1–K7), od korpusa i indeksa preko dohvatanja i sklapanja konteksta do generisanja odgovora." %}

## Korak 1: da li odgovor uopšte postoji u korpusu

Prvo pitanje nije "zašto je dohvatanje promašilo" nego "da li je informacija ikad bila indexirana". Ako odgovora nema u korpusu, nikakvo podešavanje dohvatanja to neće riješiti - ovo je zaseban tip kvara od lošeg rangiranja, i vrijedi ga provjeriti prije bilo kakvog podešavanja rangiranja. Ručno pretražite korpus (grep, full-text search, bilo šta van vašeg RAG pipeline-a) za ključne pojmove iz query-ja. Ako ništa ne nađete, problem je u prikupljanju sadržaja, ne u modelu.

## Korak 2: da li je dohvatanje promašilo indexirani chunk

Ako je odgovor u korpusu, sljedeće pitanje je da li je relevantni chunk uopšte dospio u top-k rezultata dohvatanja. Ovo je čest problem kad se oslanjate isključivo na dense embedding pretragu: embeddingovi dobro hvataju semantičku sličnost, ali loše hvataju tačna podudaranja - šifre grešaka, ID-jeve, SKU brojeve, verzije proizvoda. Query koji sadrži tačan token koji mora da se poklopi (a ne samo značenje) je klasičan kandidat za promašaj. Ovo je i glavni razlog zašto hybrid search (kombinacija sparse BM25 pretrage i dense embeddinga) postoji kao standardna praksa, a ne kao opcionalni dodatak - vidite da li je problematičan chunk uopšte bio u kandidatskom skupu prije rerankinga, ne samo u finalnom top-k.

## Korak 3: da li je chunk tu, ali zakopan u sredini konteksta

Ako je relevantan chunk stigao do modela, provjerite gdje se nalazi unutar konteksta koji šaljete. Studija "Lost in the Middle" ([Liu i dr., 2023](https://arxiv.org/abs/2307.03172), Stanford/UC Berkeley) pokazuje da je tačnost modela najveća kad je relevantna informacija na početku ili kraju konteksta, a opada kad je zakopana u sredini - i ovo vrijedi i za modele koji se reklamiraju kao long-context. Veći kontekstni prozor ne rješava problem redoslijeda i pozicioniranja. Ako vaš pipeline gura 10-20 chunkova u kontekst bez razmišljanja o rasporedu, "lost in the middle" efekat je ozbiljan kandidat - pokušajte premjestiti najrelevantniji chunk na početak ili kraj i provjerite da li se odgovor popravlja.

## Korak 4: da li je chunking uništio sadržaj prije nego što je uopšte stigao do indexa

Fiksna veličina chunk-a (fixed-size chunking) po broju tokena rutinski siječe rečenice na pola, dijeli tabele u komade koji gube smisao, i odsijeca stavke liste od naslova koji im daje kontekst. Ovo je kvar koji se dešava prije indexiranja i utiče i na dohvatanje (chunk bez konteksta se lošije poklapa s query-jem) i na generisanje (model dobije fragment bez rečenice koja mu daje kontekst). Provjerite sirovi chunk koji je zapravo dohvaćen - ne rezultat, nego tačan tekst koji je ušao u prompt. Ako je chunk polovina tabele ili rečenica bez subjekta, problem je u granicama chunkova ili nedovoljnom overlap-u, ne u modelu ni embeddingu.

## Korak 5: da li je dohvaćeni sadržaj zastario

Sličnost embeddinga ne nosi vremenski signal - zastarjeli dokument se poklapa s query-jem identično kao svjež, sve dok je semantički sličan. Ovo je zato podmukao kvar: ne izgleda kao jedan očigledno pogrešan odgovor, nego kao postepeno opadanje tačnosti kroz mnogo query-ja, jer index i dalje sadrži staru verziju uz (ili umjesto) novu. Ako je odgovor bio tačan prije nekoliko sedmica ili mjeseci, a sad nije, provjerite datum dokumenta koji je stvarno dohvaćen - ne datum posljednjeg indexiranja pipeline-a.

## Korak 6: da li je dohvatanje bilo ispravno, a model ipak omašio

Ako je pravi chunk dohvaćen, dobro pozicioniran i ažuran, a odgovor je i dalje pogrešan, kvar je nizvodno od dohvatanja. Barnett i dr. dokumentuju nekoliko odvojenih načina da ovo otkaže: model ne izvuče odgovor iako je prisutan u kontekstu, ignoriše traženi format izlaza, da pogrešnu specifičnost (previše generalno ili previše precizno), ili izostavi dio dostupne informacije. Ovo je suptilna razlika za developere: dohvatanje uspješno ne znači da je generisanje uspješno. Popularni opis ovoga kao "RAG halucinira" je često netačan - model vjerno i koherentno sažima nepotpun ili loše postavljen kontekst, što je kvar dohvatanja obučen u odjeću generisanja, a ne halucinacija u klasičnom smislu izmišljanja činjenica.

## Korak 7: da li vaša evaluacija uopšte može razlikovati ova dva sloja

Ako gore navedeni koraci djeluju kao previše ručnog posla za svaki loš odgovor, uzrok je najčešće to što evaluacija (evaluation) ne razdvaja slojeve. [Ragas](https://docs.ragas.io/en/v0.1.21/concepts/metrics/), kao jedan od standardnih evaluacijskih frameworka za RAG, eksplicitno definiše zasebne metrike za dohvatanje (context precision, context recall) i za generisanje (faithfulness, answer relevance) - upravo zato što generator može imati visok faithfulness rezultat dok vjerno sažima nepotpun ili pogrešan dohvaćeni kontekst. End-to-end ocjenjivanje odgovora ("izgleda dobro/loše") ne hvata ovu razliku; multi-hop query-ji posebno umiju izgledati koherentno dok je context recall ispod ivice. Ako nemate odvojene metrike za dohvatanje i generisanje, gradite dijagnostiku na nagađanju, ne na podacima.

## Šta NIJE rješenje

Nekoliko uobičajenih "popravki" rješava samo jedan od sedam koraka, a prodaje se kao univerzalno rješenje:

- **Reranking** je drugi sloj preciznosti primijenjen na kandidatski skup (obično top 50–100 iz prvog stepena) - ne može vratiti dokument koji je prvi stepen dohvatanja potpuno promašio (korak 2). Ako je problem u koraku 1, reranker ne pomaže.
- **Veći kontekstni prozor** ne rješava "lost in the middle" efekat (korak 3) niti chunking probleme (korak 4) - Liu i dr. pokazuju da ovo vrijedi i za modele s velikim kontekstom.
- **"RAG halucinira"** kao dijagnoza je često netačna etiketa za ono što je zapravo kvar dohvatanja (koraci 1–5), pogrešno pripisan generisanju (korak 6). Prava halucinacija - model izmišlja činjenicu koje nema nigdje u kontekstu - je samo jedan od mogućih uzroka pogrešnog odgovora, ne podrazumijevani.

## Izvori

- ["Seven Failure Points When Engineering a Retrieval Augmented Generation System" (Barnett i dr.)](https://arxiv.org/html/2401.05856v1)
- ["Lost in the Middle: How Language Models Use Long Contexts" (Liu i dr.)](https://arxiv.org/abs/2307.03172)
- [Ragas dokumentacija - definicije metrika](https://docs.ragas.io/en/v0.1.21/concepts/metrics/)
- [Pinecone dokumentacija - hybrid search](https://docs.pinecone.io/guides/search/hybrid-search)
- [Superlinked VectorHub - optimizacija RAG-a hybrid search-om i rerankingom](https://superlinked.com/vectorhub/articles/optimizing-rag-with-hybrid-search-reranking)
- [Unstructured.io - izazovi RAG pipeline-a od ingestije do dohvatanja](https://unstructured.io/insights/rag-pipeline-challenges-from-data-ingestion-to-retrieval)
