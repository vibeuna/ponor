---
layout: post
title: "Mistral objavio Robostral Navigate: navigacija robota iz jedne RGB kamere"
date: 2026-07-16
description: "Mistral je 8. Jula 2026. predstavio Robostral Navigate, model od 8B parametara koji navigira robote iz jedne RGB kamere bez LiDAR-a – uz rezultate koji za sada dolaze isključivo iz simulacije."
category: vijesti
image: /assets/images/2026-07-16-robostral-navigate.svg
audience: developers
read_time: 3
---

Mistral je 8. jula 2026. predstavio Robostral Navigate, model od 8 milijardi parametara koji upravlja navigacijom robota koristeći samo jednu RGB kameru i instrukciju napisanu običnim jezikom – bez LiDAR-a i bez senzora dubine. Mistral ga predstavlja kao svoj prvi embodied AI model. Svi objavljeni rezultati za sada dolaze isključivo iz simulacije (benchmark R2R-CE), ne iz nezavisnog testiranja na stvarnom hardveru.

## Šta se desilo

Robostral Navigate je VLM (vision-language model) od 8B parametara, inicijaliziran iz Mistralovog grounding-specijaliziranog VLM-a. Ulaz je jedna RGB kamera; Mistral eksplicitno navodi da nema LiDAR-a ni senzora dubine.

Model je treniran u potpunosti u simulaciji – oko 2,4 miliona trajektorija kroz 350.000 scena. Trening ima dvije faze: supervised learning, a zatim online reinforcement learning (RL) algoritmom CISPO.

Kao izlaz, model predviđa cilj u obliku koordinate u ravni slike plus orijentaciju (Mistral to zove "pointing"). Kada cilj nije u vidnom polju, prelazi na lokalni pomak umjesto apsolutne mete.

## Zašto je važno

Za developere je najkonkretniji signal senzorski minimalizam: samo RGB kamera, bez skupih LiDAR sklopova. To načelno spušta cijenu hardvera i pojednostavljuje integraciju. Mistral model predstavlja kao hardverski neovisan i kao prvi korak u ono što naziva "physical AI".

Ključna ograda: cijeli trening i sve prijavljene brojke dolaze iz simulacije. Prijenos iz simulacije na stvarni hardver (sim-to-real) nije potkrijepljen nijednim benchmarkom na fizičkom robotu.

## Šta to znači u praksi

Rezultate treba čitati precizno. Na R2R-CE model postiže 76,6% uspješnosti na validacijskom skupu neviđenih scena (val-unseen) i 79,4% na viđenim scenama (val-seen). To je validacijski split, ne test leaderboard tog benchmarka. Mistral tvrdi prednost od +9,7 postotnih poena nad najboljim pristupom s jednom kamerom i +4,5 nad višesenzorskim pristupima – to su tvrdnje proizvođača, bez nezavisne reprodukcije u trenutku objave.

Na strani treninga, Mistral navodi da prefix-caching smanjuje broj tokena za trening 22 puta u odnosu na obradu po vremenskom koraku, te da je RL faza dodala 3,2% uspješnosti.

Tvrdnje da model radi na robotima na točkovima, nogama i letjelicama te da se prilagođava preprekama demonstrirane su u Mistralovoj prezentaciji, ali nisu nezavisno provjerene. Pitanje latencije i dovoljne pouzdanosti za rad uživo ostaje otvoreno.

## Pristup

Ništa od onoga što bi developeru trebalo za evaluaciju nije objavljeno: nema API-ja, nema podataka o open weights, cijeni, licenci ni rasporedu izlaska. Dok se to ne pojavi, model se ne može ni integrirati ni nezavisno provjeriti – sve što imamo su brojke iz simulacije i demonstracije.

## Izvori

- [Mistral – Robostral Navigate (zvanična najava)](https://mistral.ai/news/robostral-navigate/)
- [Mistral News – indeks (potvrda datuma 8.7.2026.)](https://mistral.ai/news/)
