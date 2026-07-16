---
layout: post
title: "Self-Harness: agentni framework koji sam popravlja vlastiti harness"
date: 2026-06-24
description: "Istraživači iz Shanghai AI Lab-a objavili su Self-Harness – trostepeni framework u kojemu LLM agent autonomno identificira vlastite slabosti i mijenja harness bez dotaknuća težina modela. Na Terminal-Bench 2.0 relativni pomak kreće se od 33% do 60%, ovisno o modelu."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-06-24-self-harness.svg
---

Istraživači iz Shanghai Artificial Intelligence Laboratory objavili su [Self-Harness](https://arxiv.org/html/2606.09498v1): trostepeni framework koji LLM agentu daje mogućnost da autonomno detektuje vlastite slabosti u izvođenju i prerađuje vlastiti harness – bez izmjene težina modela.

## Šta se desilo

Paper "Self-Harness: Harnesses That Improve Themselves" (arXiv:2606.09498v1) objavljen je 8. juna 2026. Osnovna ideja: harness agenta – sistem promptovi, definicije alata, pravila izvođenja, logika oporavka od grešaka – tretira se kao verzionisani artefakt koji se može mijenjati, ne kao statična konfiguracija.

Framework prolazi kroz tri koraka u petlji:

1. **Weakness Mining** – agent izvodi zadatke, a trace (trag izvršavanja) se klasteruje prema uzorcima grešaka. Ne traži se tačan odgovor kao signal; signal su konkretni uzroci pada u trace-ovima.
2. **Harness Proposal** – za svaki klaster grešaka generišu se K minimalnih, ciljanih izmjena harness-a. Cilj je kirurška korekcija, ne generalno prepisivanje.
3. **Proposal Validation** – svaka izmjena prolazi regresijsku kapiju: mora poboljšati rezultat na held-out skupu, a istovremeno ne smije degradovati held-in skup. Izmjene koje ne prođu oba kriterija se odbacuju.

Evaluacija je provedena na Terminal-Bench 2.0, skupu zadataka u izolovanim terminalnim okruženjima (kontejnerizovani zadaci; isključeni su zadaci s nestabilnim eksternim ovisnostima i multimodalni zadaci). Testirana su tri modela na 64-zadatnom podskupu:

| Model | Held-out (prije) | Held-out (poslije) | Relativni pomak |
|---|---|---|---|
| MiniMax M2.5 | 40,5% | 61,9% | +53% |
| Qwen3.5-35B-A3B | 23,8% | 38,1% | +60% |
| GLM-5 | 42,9% | 57,1% | +33% |

Konkretne izmjene koje je framework predložio znatno se razlikuju po modelu. Za MiniMax M2.5: pravilo za prekidanje beskonačnih petlji (maks. 50 poziva alata) i obavezno kreiranje artefakta na kraju zadatka. Za Qwen3.5: provjera ovisnosti prije izvođenja, disciplina ponovnih pokušaja (bez duplikata komandi), oporavak aktiviran kreiranjem artefakta. Za GLM-5: trajni PATH između shell sesija, ograničenje eksternih preuzimanja, eksplicitna tranzicija iz faze istraživanja u fazu implementacije.

## Zašto je važno

Dosadašnji pristupi optimizaciji promptova – DSPy, APE i slični – optimiziraju prompt prema skupu označenih tačnih odgovora. Self-Harness koristi samo trace grešaka: nema ciljnog izlaza, samo kauzalni signal iz samog izvođenja. To je bitno drugačiji signal.

Regresijska kapija je konkretan projektni obrazac koji se može primijeniti i van ovog rada: niko ko gradi agentne sisteme ne želi izmjenu harness-a koja poboljšava jedan slučaj ali kvari deset prethodnih.

## Šta to znači u praksi

Za developere koji grade agentne pipeline-ove, rad nudi dva konkretna obrasca. Harness kao verzionisani artefakt: sistem promptovi i definicije alata trebaju imati historiju verzija i testove – diff između verzija nosi signal o tome što je bilo slomljeno. I regresijska kapija: svaka izmjena harness-a mora poboljšati held-out skup a ne degradovati held-in, i vrijedi primjenjivati je i bez punog Self-Harness framework-a. Poboljšanja su model-specifična – svaki od testiranih modela dobio je drugačije izmjene, pa postupak treba ponoviti za svaki model kojeg koristite.

Framework zahtijeva deterministički verifikator koji pouzdano ocjenjuje je li zadatak izveden ispravno. To odmah isključuje domene gdje je tačnost subjektivna ili kontekstno zavisna (medicinska podrška, generativni sadržaj, upravljanje procesima u realnom vremenu). Nema nezavisne replikacije na drugim benchmark testovima, a autori napominju da prihvaćene izmjene mogu odražavati obrasce specifične za Terminal-Bench 2.0. Tih 33–60% relativnog poboljšanja vrijedi čitati kao signal da je ideja tehnički izvediva, ne kao garantovani pomak u produkcijskim okruženjima.

## Izvori

- [arXiv:2606.09498v1 – "Self-Harness: Harnesses That Improve Themselves", Shanghai Artificial Intelligence Laboratory](https://arxiv.org/html/2606.09498v1)
