---
layout: post
title: "Alibaba objavio Qwen-Robot Suite: otvoreni modeli za navigaciju i manipulaciju robota"
date: 2026-06-20
description: "Qwen-Robot Suite donosi tri foundation modela za embodied AI - otvorene težine za navigaciju i manipulaciju, world model samo kao tehnički rad bez weighta."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-06-20-qwen-robot-suite.svg
---

Alibabina Qwen ekipa objavila je 16. juna 2026. tri foundation modela namijenjena embodied AI za robote - pod zajedničkim imenom Qwen-Robot Suite. Dva od tri modela dolaze s javno dostupnim težinama; treći je za sada samo tehnički rad bez objavljenih težina.

## Šta se desilo

Suite sadrži tri modela s jasno razdvojenim domenama:

**Qwen-RobotNav** pokreće navigaciju robota kroz fizički prostor. Izgrađen na Qwen3-VL osnovi, dostupan je u veličinama 2B, 4B i 8B parametara, treniran na 15,6 miliona uzoraka iz pet navigacijskih domena. Na benchmark-u VLN-CE RxR postiže 76,5% stope uspješnosti (success rate), na HM3Dv2 75,6%, a na NAVSIM benchmark-u 91,4 PDMS bodova - prema rezultatima koje su autori prijavili u tehničkom izvještaju (arXiv 2606.18112). GitHub repozitorij i težine su javno dostupni.

**Qwen-RobotManip** cilja fizičku manipulaciju - upravljanje robotskom rukom. Arhitektura kombinuje Qwen3.5-4B jezički model s action head-om baziranim na flow matching DiT (Diffusion Transformer) pristupu. Model je pretreniran na otprilike 38.100 sati javno dostupnih snimaka robota i ljudskih demonstracija. Na RoboChallenge Table30-v1 benchmark-u zauzima prvo mjesto prema samoprijavljenim rezultatima ekipe, kao i na EBench benchmark-u. Težine su javno dostupne.

**Qwen-RobotWorld** predstavlja world model - model koji iz video sekvenci uči predviđati stanja okoline uslovljena akcijama. Arhitektura se oslanja na 60-slojni MMDiT (Multimodal Diffusion Transformer) uz zamrznuti Qwen2.5-VL enkoder, a treniran je na 8,6 miliona video-tekstualnih parova (200 miliona frejmova). Za sada je objavljen isključivo kao tehnički rad (arXiv 2606.17030) - bez težina, bez API pristupa i bez najavljenog datuma objave.

## Zašto je važno

Za developere koji rade na robotičkim sistemima ili prate stanje u toj oblasti, relevantan signal nije u marketinškim najavama nego u konkretnom: dvije od tri komponente suite-a mogu se pokrenuti odmah. Qwen-RobotNav i Qwen-RobotManip su dostupni putem QwenLM GitHub repozitorija ([github.com/QwenLM/Qwen-VLA](https://github.com/QwenLM/Qwen-VLA)).

Pristup otvorenim težinama znači da je moguće evaluirati modele na vlastitim robotičkim platformama, prilagoditi ih fino podešavanjem (fine-tuning) na domenski specifičnim podacima, ili koristiti kao polaznu točku za istraživanje. Pretraining pipeline za RobotManip dokumentiran je u tehničkom izvještaju i u principu je reproducibilan - corpus je sastavljen isključivo iz javnih skupova podataka.

## Šta to znači u praksi

Nekoliko tehničkih detalja vrijedi pažnje:

**VLA arhitektura za manipulaciju:** Izbor LLM backbone + flow matching DiT action head za RobotManip razlikuje se od direktnih policy pristupa (MLP ili CNN glava na jezičkom enkoderu) i od čisto diffusion-based modela. Flow matching pristup nudi brzu inferenciju u usporedbi s iterativnom denoising diffusion procedurom - detalji su u arXiv 2606.17846.

**Šta se može pokrenuti danas vs. šta je samo papir:** RobotNav (2B/4B/8B) i RobotManip imaju potvrđene GitHub repozitorije i objavljene težine. RobotWorld nema ni jedno ni drugo - zanimljiv arhitekturalni doprinos, ali ne i nešto što možete integrirati.

**Licenciranje:** Qwen ekipa nije eksplicitno potvrdila uvjete licenciranja za otvorene težine. Prethodni Qwen modeli koristili su Qwen-specifične licence s klauzulama o komercijalnoj upotrebi - ne standardne Apache 2.0 ili MIT. Provjerite licence prije upotrebe u komercijalnim projektima.

**Benchmark tvrdnje:** Svi benchmark rezultati su samoprijavljeni u tehničkim izvještajima Alibabe - neovisna replika u trećoj strani literaturi za sada ne postoji. Rangirani rezultati ("1. mjesto na RoboChallenge") trebaju se tretirati kao polazište za evaluaciju, ne kao etablirana činjenica.

Prema dostupnim izvještajima, RobotWorld pilot testiranje odvija se s odabranim Alibaba Cloud enterprise klijentima u robotičkom sektoru - javni API nije najavljen.

## Izvori

- [Qwen-Robot Suite - zvanični blog](https://qwen.ai/blog?id=qwen-robotsuite)
- [arXiv 2606.17030 - Qwen-RobotWorld tehnički izvještaj](https://arxiv.org/abs/2606.17030)
- [arXiv 2606.17846 - Qwen-RobotManip tehnički izvještaj](https://arxiv.org/abs/2606.17846)
- [arXiv 2606.18112 - Qwen-RobotNav tehnički izvještaj](https://arxiv.org/abs/2606.18112)
- [QwenLM GitHub - Qwen-VLA repozitorij](https://github.com/QwenLM/Qwen-VLA)
