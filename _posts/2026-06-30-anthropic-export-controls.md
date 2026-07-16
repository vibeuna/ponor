---
layout: post
title: "SAD zabranio pristup Anthropicovim modelima Fable 5 i Mythos 5 – globalno"
date: 2026-06-30
description: "Američki Odjel za trgovinu naredio je Anthropicu da odmah suspendira globalni pristup modelima Fable 5 i Mythos 5, pozivajući se na jailbreak tehniku koja je navodno otvorila kibersigurnosne sposobnosti modela."
category: vijesti
audience: businesses
read_time: 4
image: /assets/images/2026-06-30-anthropic-export-controls.svg
---

Američki Odjel za trgovinu izdao je 12. juna 2026. hitnu direktivu kojom je naložio kompaniji Anthropic da odmah obustavi pristup modelima Fable 5 i Mythos 5 za sve strane državljane. Anthropic je, umjesto da pokušava filtrirati korisnike po nacionalnosti, isključio oba modela za sve kupce širom svijeta – uključujući i vlastite zaposlenike koji nisu američki državljani.

## Šta se desilo

Direktiva je stigla u Anthropicove sisteme u petak, 12. juna 2026. u 17:21 po istočnom američkom vremenu. Povod koji je navela Vlada SAD je otkrivanje [jailbreak (tehnika zaobilaženja sigurnosnih mjera modela)](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/) tehnike koja je navodno omogućila pristup kibersigurnosnim sposobnostima modela Mythos 5 – konkretno sposobnosti detekcije softverskih ranjivosti koje bi, prema navodima vladinih zvaničnika, mogle biti iskorištene za razvoj kibernetičkog oružja.

Anthropic je [javno osporio](https://x.com/AnthropicAI/status/2065597531644743999) proporcionalnost mjere. Kompanija je saopštila da je predmetni jailbreak "uzak" i da "ne zaobilazi sve sigurnosne mjere modela", te da vladino pismo nije sadržalo konkretne tehničke detalje koji bi potkrijepili nalog. Unatoč tome, suspenzija je stupila na snagu odmah.

Ostali modeli iz Anthropicovog portfelja – uključujući Claude Opus 4.8 i ostale Claude modele – direktiva nije obuhvatila i ostali su dostupni.

## Zašto je važno

Ovo je dokumentovana primjena izvoznih ograničenja na komercijalno dostupan frontier AI model od strane američke Vlade – pravnog instrumenta koji se dosad uglavnom koristio u kontekstu hardvera i poluvodiča, a ne softvera koji se isporučuje putem API-ja.

Za kompanije koje su izgradile proizvode ili radne procese na Fable 5 ili Mythos 5, posljedica je bila neočekivan globalni prekid pristupa bez prethodne najave. Anthropic nije mogao selektivno isključiti samo strane korisnike – tehnička i pravna složenost takve segmentacije primorala je kompaniju na potpuni globalni isklop. Ovaj ishod direktno ilustruje rizik koji nose frontier modeli dostupni isključivo kao cloud usluge: jedna regulatorna odluka u jednoj jurisdikciji može prekinuti pristup svim korisnicima, bez obzira na njihovu lokaciju ili ugovorni odnos.

## Šta to znači u praksi

Kompanije koje koriste frontier AI modele putem API-ja sada se suočavaju s regulatornim rizikom koji se teško predviđa i koji nije pod kontrolom ni korisnika ni dobavljača. Konkretan scenario koji se ovdje odigrao: dobavljač modela primio je direktivu i isključio uslugu u roku od sati.

Preporuke koje iz ovog slučaja logično slijede za firme koje grade na frontier modelima:

- **Redundancija dobavljača.** Ovisnost o jednom modelu ili jednoj kompaniji povećava izloženost regulatornim šokovima. Arhitekture koje podržavaju zamjenski model (fallback) postaju operativna nužnost, ne samo tehnička preferencija.
- **Pregled ugovornih odredbi.** Standardni SLA ugovori s AI dobavljačima tipično ne pokrivaju vladine direktive kao oblik "force majeure" – vrijedi pregledati šta je zapravo regulisano.
- **Pratiti regulatorni kontekst.** Ova direktiva nije bila izolovani incident. Februara 2026. Trump je naredio federalnim agencijama da prestanu koristiti Anthropicove modele; u martu 2026. Pentagon je klasifikovao Anthropic kao "rizik za lanac nabavke." Regulatorni kontekst oko AI dobavljača iz SAD-a mijenja se brzo.

## Kontekst

Primjena izvoznih ograničenja na cloud AI modele nije bila anticipirana kao realan scenarij od strane većine korisnika. Dosadašnja primjena takvih instrumenata bila je uglavnom ograničena na fizičku robu – čipove, hardver za napredne računalne sisteme. Ovaj slučaj pokazuje da američka Vlada smatra da neke AI sposobnosti potpadaju pod isti regulatorni okvir, bez obzira na to što se pristup modelu odvija putem mreže, a ne fizičkim izvozom.

## Izvori

- [Fortune – Anthropic disables Fable and Mythos over export controls, June 13 2026](https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/)
- [Al Jazeera – US orders Anthropic to disable AI models for all foreign nationals, June 13 2026](https://www.aljazeera.com/news/2026/6/13/us-orders-anthropic-to-disable-ai-models-for-all-foreign-nationals)
- [Anthropic – public statement on X, June 2026](https://x.com/AnthropicAI/status/2065597531644743999)
- [Forbes – What happened after Anthropic disabled Fable 5 and Mythos 5, June 16 2026](https://www.forbes.com/sites/anishasircar/2026/06/16/anthropic-disabled-fable-5-and-mythos-5-after-a-us-export-control-order-heres-what-happened/)
