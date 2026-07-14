---
layout: post
title: "Mistral objavio Leanstral 1.5, model za formalno dokazivanje teorema"
date: 2026-07-06
description: "Mistral je objavio Leanstral 1.5, open weights model za formalno dokazivanje teorema i verifikaciju Lean 4 koda — sa benchmark rezultatima koji zavise od budžeta tokena više nego što headline brojka pokazuje."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-07-06-mistral-leanstral-1-5.svg
---

Mistral je objavio Leanstral 1.5, nadogradnju martovskog Leanstral modela specijalizovanog za formalno dokazivanje teorema (formal theorem proving) i agentne radne tokove za verifikaciju koda u Lean 4. Model dolazi kao open weights pod Apache 2.0 licencom, uz besplatan, vremenski ograničen pristup preko Mistralovog "Labs" API tier-a.

## Šta se desilo

Leanstral 1.5 je sparse mixture-of-experts (MoE) model sa 119 milijardi ukupnih i otprilike 6 do 6,5 milijardi aktivnih parametara, te kontekstnim prozorom (context window) od 256k tokena ([model card](https://docs.mistral.ai/models/model-cards/leanstral-1-5)). Treniran je reinforcement learning-om (RL) kroz dva okruženja: iterativno dokazivanje uz povratnu informaciju kompajlera i agentni razvoj na nivou cijelog repozitorija, sa pristupom fajl-sistemu, bash-u i language server-u (LSP).

Na benchmark testovima, Mistral navodi potpuno zasićenje miniF2F-a (100%), 587/672 na PutnamBench-u, 87% na FATE-H i 34% na FATE-X, te 28,9% (pass@1) odnosno 43,2% (pass@8) na FLTEval-u ([Mistralov blog](https://mistral.ai/news/leanstral-1-5/)). Originalni Leanstral iz marta (120B/6B aktivnih parametara) je pri objavi izvještavao samo FLTEval rezultate (pass@16: 31,9) — 1.5 dodaje PutnamBench, miniF2F i agentni use case za pronalaženje grešaka u kodu.

Model je dostupan besplatno preko Mistral Labs API-ja (`labs-leanstral-1-5`), s tim da je Mistral najavio gašenje tog pristupa 30. septembra 2026. Težine su objavljene na Hugging Faceu, što znači da je moguće lokalno hostovano (self-hosted) korištenje bez zavisnosti o API-ju.

Odnos ukupnih i aktivnih parametara (119B naspram ~6–6,5B) je standardna MoE karakteristika: model tokom inferencije aktivira samo dio mreže po tokenu, pa je stvarni računski trošak po zahtjevu bliži modelu od 6-7 milijardi aktivnih parametara nego modelu od 119 milijardi. To olakšava lokalno hostovano pokretanje u odnosu na dense model (model koji aktivira sve parametre po tokenu) iste ukupne veličine, iako 119B ukupnih parametara i dalje zahtijeva ozbiljnu memorijsku infrastrukturu za smještaj svih ekspertskih blokova.

## Zašto je važno

Headline broj sa PutnamBench-a (587/672) zavisi direktno od budžeta tokena po pokušaju: prema Mistralovim podacima, model rješava 44 zadatka uz 50k tokena po pokušaju, 244 uz 200k, 493 uz 1M i tek 587 uz 4M tokena. Za programere koji procjenjuju praktičnu upotrebljivost, ovo je bitnija informacija od same brojke — odnos je izrazito neproporcionalan, ne linearan: skok sa 493 na 587 riješenih zadataka (94 dodatna zadatka) zahtijeva učetverostručenje budžeta, sa 1M na 4M tokena. Drugim riječima, lakši zadaci se rješavaju relativno jeftino, a svaki naredni riješeni zadatak pri kraju skale dolazi uz nesrazmjerno veći trošak tokena — "puni" rezultat od 587 pretpostavlja izuzetno velik i sve skuplji budžet po problemu.

Mistral tvrdi da to i dalje iznosi oko 4 dolara po riješenom problemu, naspram navodnih 300+ dolara kod Seed-Provera — ali to je Mistralova vlastita procjena tuđeg proizvoda, ne nezavisno provjeren podatak. Isto vrijedi za tvrdnju da Leanstral 1.5 nadmašuje Claude Opus 4.6 na FLTEval-u uz sedam puta nižu cijenu — riječ je o Mistralovom cross-benchmark poređenju, ne o nezavisnoj verifikaciji.

## Šta to znači u praksi

Za timove koji rade sa formalnom verifikacijom koda, agentni pristup — model sa pristupom fajl-sistemu, bash-u i LSP-u koji radi na nivou cijelog repozitorija — je zanimljiviji signal od samih benchmark brojki. To je najava pravca u kojem formalno dokazani (Lean 4-verifikovani) kod prestaje biti isključivo akademska vježba i postaje dio agentnih razvojnih radnih tokova.

Praktični savjet: pristup preko Labs API-ja je besplatan, ali privremen — vrijedi testirati prije 30. septembra 2026. Za dugoročnu upotrebu, open weights opcija znači da je lokalno hostovano pokretanje dostupno od početka, bez čekanja na eventualno gašenje API-ja.

Vrijedi biti oprezan i sa poređenjima naspram ranijim modelima za formalno dokazivanje teorema: DeepSeek-Prover-V2 je, na primjer, prijavio 49/658 na PutnamBench-u ([arXiv](https://arxiv.org/abs/2504.21801)) — dakle na skupu od 658 zadataka, a ne 672 kao kod Leanstral-a 1.5. Različiti radovi koriste različite verzije i veličine istih benchmark skupova, pa direktno poređenje brojki bez provjere veličine skupa daje lažni utisak preciznosti.

## Izvori

- [Mistral — Leanstral 1.5, službena najava](https://mistral.ai/news/leanstral-1-5/)
- [Mistral — model card za Leanstral 1.5](https://docs.mistral.ai/models/model-cards/leanstral-1-5)
- [Mistral — originalna najava Leanstral modela (mart 2026)](https://mistral.ai/news/leanstral/)
- [DeepSeek-Prover-V2 — arXiv paper](https://arxiv.org/abs/2504.21801)
