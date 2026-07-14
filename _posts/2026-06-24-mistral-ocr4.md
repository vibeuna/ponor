---
layout: post
title: "Mistral objavio OCR 4: strukturirani izlaz, 170 jezika i lokalno hostovanje za enterprise"
date: 2026-06-24
description: "Mistral AI je 23. juna 2026. objavio OCR 4, model za ekstrakciju dokumenata koji vraća granične okvire, ocjene pouzdanosti po riječima i block klasifikaciju — dostupan i kao single-container za lokalno hostovanje."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-06-24-mistral-ocr4.svg
---

Mistral AI je 23. juna 2026. objavio OCR 4, navodeći da model za razliku od prethodnih verzija vraća ne samo tekst nego i prostorne metapodatke: granične okvire (bounding boxes) po bloku, klasifikaciju tipa bloka (naslovi, tabele, jednadžbe, potpisi) i ocjene pouzdanosti (confidence scores) po riječima. Model je dostupan putem Mistral API-ja, Mistral Studija, Amazon SageMakera i Microsoft Foundryja, a za enterprise korisnike i kao lokalno hostovano (self-hosted) rješenje u jednom kontejneru.

## Šta se desilo

OCR 4 procesira PDF, DOC, PPT i OpenDocument fajlove i podržava 170 jezika u 10 jezičnih grupa. Na javnom OlmOCRBench benchmarku model postiže skor 85.20, a na OmniDocBench 93.07 — oba su publički referentni testovi u document AI prostoru. Mistral tvrdi da su njeni anotatori preferirali OCR 4 u 72% slučajeva u usporedbi s konkurentskim sistemima, ali je to interna evaluacija koja nije neovisno potvrđena, a takmičarski sistemi nisu navedeni po imenu.

Cijenovno: standardni API košta $4 po 1.000 stranica, Batch API $2 po 1.000 stranica (50% popust za veće volumene). Postoji i poseban tier pod nazivom **Document AI** po $5/1.000 stranica koji OCR izlaz propušta kroz `mistral-small-2603` radi oblikovanja JSON izlaza prema zadanoj shemi. Taj korak znači dodatni model call — što utiče na latenciju i trošak inferencije, a nije prominentno istaknuto u marketinškim materijalima.

Mistral navodi i korisničke studije slučaja — obje prema Mistralovoj vlastitoj objavi, bez neovisne verifikacije, a takmičarski sistemi nisu navedeni po imenu: Rogo navodi 8× niži trošak i 17× manju latenciju u odnosu na "vodeće agentne parsere", a Anaqua 4× bržu obradu po stranici.

## Zašto je važno

Za developere koji grade RAG (retrieval-augmented generation) pipeline-ove, izlaz OCR 4-a je direktno upotrebljiv bez dodatnog preprocessinga: granični okviri i klasifikacija blokova omogućavaju semantički chunking na osnovu strukture dokumenta, a ocjene pouzdanosti po riječima otvaraju mogućnost za human-in-the-loop tokove gdje se niskopouzdani segmenti šalju na manualnu provjeru.

Single-container self-hosted opcija je relevantan detalj za timove koji rade u reguliranim sektorima — finansije, pravo, zdravstvo — ili pod GDPR i data residency mandatima. Jedini je deployment path koji drži dokumente izvan Mistralove cloud infrastrukture. Nije potvrđeno da li self-hosted kontejner uključuje i Document AI tier ili samo ekstrakciju.

## Šta to znači u praksi

Nekoliko konkretnih tačaka za procjenu:

- **Batch API po $2/1.000 str.** je cijenovno konkurentan za pipeline-ove s visokim volumenom (digitalizacija arhiva, automatska indeksacija dokumenata). Preporučuje se uporediti sa stvarnim potrebama latencije — Batch API tipično nosi viši red čekanja.

- **Document AI tier sa `mistral-small-2603`** je praktičan za direktno dobivanje JSON-a prema zadanoj shemi, ali nije jednoprolazna inferencija. Planiranje arhitekture s tim u vidu znači: latencija = OCR pass + LLM pass, a naplaćuje se $5/str. a ne $4.

- **Granični okviri i ocjene pouzdanosti** su korisni za pipeline-ove koji kombinuju OCR s vizualnom provjerom ili LLM re-rankerom — nema potrebe za zasebnim modelom za detekciju blokova ako OCR 4 to već vraća u izlazu.

- **Snowflake integracija** je najavljena ali bez datuma — za timove koji rade na Snowflakeu, ovo je za pratiti, nije za planirati odmah.

OlmOCRBench skor 85.20 je konkretan rezultat na javnom benchmarku. "SOTA" tvrdnja iz Mistralovog saopćenja se oslanja na taj jedan benchmark — u document AI prostoru postoji više referentnih testova i konačna rang-lista zavisi od toga koji se koristi.

## Izvori

- [Mistral AI — OCR 4 objava (23. juna 2026.)](https://mistral.ai/news/ocr-4/)
