---
layout: post
title: "Anthropic uveo Claude Tag: AI agent koji ostaje u vašem Slack kanalu"
date: 2026-06-24
description: "Anthropic je pokrenuo Claude Tag, cloud agent koji se @-spominje u Slack kanalima i samostalno izvršava zadatke asinkrono — dostupan Enterprise i Team korisnicima kao rana verzija."
category: vijesti
audience: businesses
read_time: 4
image: /assets/images/2026-06-24-claude-tag-slack.svg
---

Anthropic je 23. juna 2026. objavio Claude Tag — cloud agent koji ostaje stalno prisutan u Slack kanalima, izvršava zadatke bez stalnog nadzora i ostavlja vidljiv trag rada svim članovima tima. Dostupan je Enterprise i Team korisnicima kao rana verzija (research preview).

## Šta se desilo

Umjesto da odgovara na pojedinačna pitanja kao ranije, [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) funkcioniše kao stalni učesnik u Slack kanalu. Kada ga @-spomentete, preuzima zadatak, rastavlja ga na korake i izvršava ih asinkrono — rezultate objavljuje u threadu koji svi u kanalu mogu pratiti. Zadaci se ne moraju završiti u jednoj sesiji: Claude može nastaviti rad i van radnog vremena i sam pratiti šta je ostalo nedovršeno.

Anthropic opisuje i takozvani "ambient" mod, u kojem bi Claude proaktivno obilježavao relevantne informacije u kanalu ili se vraćao na zaglavljene threadove bez eksplicitnog poziva. Prema Anthropicovom saopćenju, ova funkcionalnost je do sada potvrđena samo u internoj upotrebi — ponašanje u eksternom okruženju na velikom broju korisnika nije neovisno potvrđeno.

Claude Tag zamjenjuje prethodnu Claude in Slack aplikaciju. Administratori imaju 30-dnevni prozor za migraciju.

## Zašto je važno

Do sada su AI asistenti u Slacku radili kao chatbotovi: pitanje–odgovor, bez pamćenja prethodnog razgovora, bez kontinuiteta između sesija. Claude Tag mijenja model: isti cloud agent nastavlja raditi na zadatku dok ga tim ne preuzme — ili dok se zadatak ne završi.

Za timove koji rade u više zona ili s ograničenim kapacitetom, to znači da workload koji inače čeka na dostupnost osobe može teći naprijed. Za menadžere koji prate šta AI radi u timovima, audit log koji bilježi svaku akciju nije samo sigurnosna mjera — to je i osnova za procjenu stvarne vrijednosti alata.

## Šta to znači u praksi

**Kontrola pristupa po kanalu.** Administratori mogu ograničiti kojim kanalima i alatima Claude Tag ima pristup. Moguće je kreirati odvojene "identitete" Claudea za različite timove — primjerice, sales verzija ne može čitati sadržaj engineering kanala. Ovo je relevantan odgovor na pitanje koje svaki direktor treba postaviti prije rollout-a: ko vidi šta.

**Troškovi su ograničeni, ali nisu transparentni.** Moguće je postaviti limite potrošnje tokena na nivou kanala i organizacije. Međutim, Anthropic nije objavio cijene za Claude Tag odvojeno od postojećih Enterprise i Team pretplata. Budžetiranje ostaje neizvjesno dok ne dođe do pune komercijalne verzije.

**Rana verzija nosi rizik.** "Rana verzija" nije marketinška skromnost — znači da se proizvod može promijeniti, da greške nisu neuobičajene i da stabilnost nije garantovana. Timovi koji razmatraju širu upotrebu trebaju to uzeti u obzir.

**Vendor zavisnost.** Claude Tag je trenutno dostupan samo za Slack. Ekspanzija na druge platforme opisana je kao "u razvoju" bez konkretnog roka. Ako koristite Teams ili drugi alat, opcija još ne postoji.

**Zaposlenici i compliance.** Treće strane, uključujući [TNW](https://thenextweb.com/news/anthropic-claude-tag-slack-always-on-ai-teammate), napominju da će stalno prisutan AI koji prati razgovore u kanalima naići na pitanja od zaposlenika i compliance timova — posebno u reguliranim industrijama. Ovo nije problem koji Anthropic rješava umjesto vas. Za kompanije u EU, to može uključivati i pitanja radnog prava i GDPR-a u kontekstu praćenja poslovnih razgovora.

## Izvori

- [Anthropic — Introducing Claude Tag (zvanična objava)](https://www.anthropic.com/news/introducing-claude-tag)
- [Fortune — tržišni kontekst i konkurentska pozicija](https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/)
- [The Next Web — analiza i pitanja oko radnog mjesta](https://thenextweb.com/news/anthropic-claude-tag-slack-always-on-ai-teammate)
