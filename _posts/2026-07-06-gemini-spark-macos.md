---
layout: post
title: "Gemini Spark stiže na macOS: Google agent sad sortira i vaše fajlove"
date: 2026-07-06
description: "Google širi Gemini Spark na macOS u beta verziji — agent sad može sortirati fajlove i raditi sa lokalnim podacima na Mac računaru, uz cijenu od 99,99 dolara mjesečno i dostupnost ograničenu na SAD."
category: vijesti
audience: general
read_time: 4
image: /assets/images/2026-07-06-gemini-spark-macos.svg
---

Google širi Gemini Spark, svog agentnog AI asistenta unutar aplikacije Gemini, na macOS, u beta verziji. Riječ je o nastavku majske najave: Spark je tada predstavljen kao cloud agent (AI agent koji radi na serverima, ne na vašem uređaju), a macOS podrška je bila najavljena kao "uskoro" (coming soon), bez konkretnog datuma. Sada je ta najava postala beta stvarnost. Umjesto da samo odgovara na pitanja u razgovoru, Spark sad može direktno raditi s fajlovima na vašem Mac računaru: sortirati ih, preimenovati i izvlačiti podatke iz njih.

## Šta se desilo

Google je 30. juna 2026. na svom [zvaničnom blogu](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/) najavio da Spark, agentni AI asistent unutar aplikacije Gemini, počinje rollout na macOS — za sada u beta verziji, počevši od verzije aplikacije Gemini 1.80.15.516.

Osim rada s lokalnim fajlovima, Spark se povezuje i s Google Workspace aplikacijama (Calendar, Tasks, Keep), kao i s konektorima (connectors) za usluge trećih strana — Canva, Dropbox, Instacart, OpenTable i Zillow Rentals. Google u objavi pokazuje konkretne primjere: sortiranje PDF dokumenata u foldere i automatsko popunjavanje budžetske tabele na osnovu lokalnih računa, po unaprijed zadanom rasporedu.

Pristup pojedinim folderima korisnik kontroliše kroz bočnu traku (sidebar) s dozvolama — svaki folder se posebno odobrava, a pristup se u svakom trenutku može povući. Nezavisne provjere ovog mehanizma za sada ne postoje; oslanjamo se na Googleov opis.

Najavljena je i funkcija daljinskog pokretanja zadataka — da s telefona pokrenete zadatak na Mac računaru — ali ta mogućnost je označena kao "uskoro" (coming soon) i još nije dostupna.

## Zašto je važno

Ovo je prvi put da Spark dobija ovlaštenje da mijenja fajlove direktno na disku korisnika. Do sada je Spark radio isključivo u cloud-u — kroz razgovor, Google Workspace aplikacije i povezane usluge trećih strana — bez pristupa lokalnim fajlovima ni na jednoj drugoj platformi (web, mobilni, Android); Windows verzija nije ni najavljena. Spark time ne prelazi "na uređaj" — sam agent i dalje se izvršava na Googleovim serverima, dakle ostaje cloud agent u punom smislu te riječi. Ono što se mijenja jeste da taj cloud agent sada dobija dozvoljeni (permissioned) pristup za čitanje i pisanje fajlova na disku Mac računara s kojim je povezan: proširuje domet, ne mijenja gdje se izvršava.

Za sada je beta ograničena na pretplatnike Google AI Ultra paketa, korisnike starije od 18 godina, i dostupna je samo u SAD-u. Prema [9to5Google](https://9to5google.com/2026/06/30/gemini-spark-mac-app/), Google AI Ultra pretplata potrebna za pristup Sparku košta 99,99 dolara mjesečno (Google to u objavi o macOS rolloutu ne navodi) — što automatizaciju fajlova pozicionira kao skup dodatak, a ne besplatnu funkciju.

Integracije za web i mobilne uređaje stižu unutar sedmice od najave, dok macOS-specifične integracije slijede u narednim sedmicama — dio funkcionalnosti opisanih u objavi trenutno nije u potpunosti dostupan ni beta korisnicima.

## Šta to znači u praksi

Ako imate Google AI Ultra pretplatu, ste u SAD-u i imate 18+ godina, možete zatražiti pristup beta verziji Gemini aplikacije za macOS i dati Sparku pristup odabranim folderima. U praksi to znači zadatke poput automatskog sortiranja skeniranih računa ili PDF-ova po folderima, ili generisanja budžetske tabele iz faktura koje već imate na disku — bez ručnog kopiranja podataka.

Za sve ostale, uključujući korisnike izvan SAD-a ili one bez Ultra pretplate, ovo za sada ostaje najava, ne dostupna funkcija.

## Kontekst

Google u istoj objavi potvrđuje da Spark dobija podršku za MCP (Model Context Protocol — protokol za kontekst modela) radi povezivanja s vanjskim aplikacijama, što korisnicima omogućava da sami dodaju prilagođene konektore. Ovo nije nagađanje sekundarnih izvora — Google to eksplicitno navodi u objavi, a potvrđuje i [9to5Google](https://9to5google.com/2026/06/30/gemini-spark-apps-more/). Vrijedi napomenuti: MCP je otvoreni standard koji je uveo Anthropic, a danas ga koriste brojni proizvođači — Googleovo usvajanje MCP-a je primjena postojećeg protokola, a ne vlastita inovacija.

## Izvori

- [Gemini Spark Updates — Google Blog, 30. juna 2026.](https://blog.google/innovation-and-ai/products/gemini-app/gemini-spark-updates-june-2026/)
- [Gemini Spark rolling out to macOS app for local tasks, automation — 9to5Google](https://9to5google.com/2026/06/30/gemini-spark-mac-app/)
- [Gemini Spark now supports 3rd-party apps, including MCP — 9to5Google](https://9to5google.com/2026/06/30/gemini-spark-apps-more/)
