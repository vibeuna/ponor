---
layout: post
title: "Google ugrađuje computer use direktno u Gemini 3.5 Flash"
date: 2026-06-30
description: "Google je integrirao computer use kao ugrađeni alat u standardni model gemini-3.5-flash, eliminirajući potrebu za zasebnim modelom za upravljanje grafičkim sučeljima."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-06-30-gemini-35-flash-computer-use.svg
---

Google je 24. juna 2026. objavio da je computer use (sposobnost AI modela da upravlja grafičkim sučeljima) sada dostupan kao ugrađeni alat unutar standardnog modela `gemini-3.5-flash` — istog modela koji programeri već koriste za pozive funkcija, pretraživanje i Maps integraciju. Mogućnost je dostupna kroz Gemini API u ranoj verziji, uz uvjete primjene Pre-GA odredbi.

## Šta se desilo

Do ovog tjedna, computer use na Googleovim modelima zahtijevao je usmjeravanje zahtjeva na zasebni Gemini 2.5 computer-use model u ranoj verziji. Nova promjena eliminiše to razdvajanje: `gemini-3.5-flash` sada sam po sebi podržava computer use kao alat, ravnopravno s ostalim ugrađenim alatima tog modela.

Prema [Googleovoj objavi na blogu](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) i [Gemini API changelogu](https://ai.google.dev/gemini-api/docs/changelog), uz ovo izdanje dolaze tri poboljšanja:

- **Radnje zasnovane na namjeri** (*intent-based actions*) — umjesto specificiranja piksel-koordinata, agent opisuje što želi postići, a model prevodi u konkretne GUI akcije.
- **Podrška za browser, mobilne i desktop okruženja** — deklarirana podrška za tri tipa sučelja, mada Google Cloud sandbox [dokumentacija](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use) opisuje konkretizovano browser-only kontejnersko okruženje s VNC nadzorom i WebSocket/CDP konekcijom.
- **Detekcija prompt injekcije** — ciljani adversarijalni trening za otkrivanje prompt injekcije (prompt injection) iz sadržaja koji agent obrađuje na ekranu.

Uz API dostupnost, Google je objavio Browserbase-hosted demo okruženje i referentnu implementaciju na GitHubu.

## Zašto je važno

Za programere koji grade agentne radne tokove, eliminisanje zasebnog computer-use modela znači jedan API poziv umjesto dva i manje overhead-a pri upravljanju kontekstom između modela. Ako vaš agent već koristi `gemini-3.5-flash` za strukturirane alate, computer use se dodaje kao još jedan alat u istoj sesiji — bez prekida ili promjene modela u sredini toka.

Vrijedi naglasiti: rana verzija dolazi s Pre-GA uvjetima, što znači da API, ponašanje i dostupnost mogu biti promijenjeni bez prethodne najave. Za produkcijske primjene, ovo je relevantna napomena.

## Šta to znači u praksi

**Integracija** je neposredna za postojeće korisnike Gemini API-ja: computer use se aktivira kao alat unutar standardnog `generateContent` poziva, bez preusmjeravanja na drugi endpoint.

**Sigurnosna površina** ostaje najvažniji faktor u primjeni. Kod GUI agenata koji čitaju ekran i izvršavaju akcije, napadač može ugraditi prompt injekciju u sadržaj na stranici — reklamu, dokument, obrazac — i time preoteti agentov tok izvršavanja. Google navodi tri mitigacijske mjere: adversarijalni trening, automatsko zaustavljanje zadatka po detekciji injekcije, i opcionalnu human-in-the-loop potvrdu za osjetljive akcije. Nijedna od ovih mjera nije izuzetak od potrebe za defanzivnom arhitekturom na strani aplikacije.

**Praktični opseg primjene** leži u legacy aplikacijama bez API-ja i radnim tokovima koji zahtijevaju interakciju s grafičkim sučeljima (web forme, desktop softveri, mobilne aplikacije). Za sisteme koji imaju strukturiran API, direktna API integracija ostaje pouzdanija i predvidljivija opcija.

**Latencija** u Google Cloud sandboxu je, prema dokumentaciji, optimizirana za niski promet, dok na višim volumenima raste. Ako planirate skalabilan deployment, ovo je varijabla koju treba izmjeriti, a ne pretpostaviti.

## Kontekst

Anthropic je computer use za Claude modele objavio u oktobru 2024. OpenAI je sličnu mogućnost uveo s Operator-om u januaru 2025. Googleova integracija u `gemini-3.5-flash` nije prva implementacija u industriji, ali jeste prva koja computer use tretira kao ravnopravni ugrađeni alat unutar generalnog flash modela, a ne kao izoliranu specijalnost.

## Izvori

- [Google Blog: Introducing computer use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)
- [Gemini API Changelog — jun 2026](https://ai.google.dev/gemini-api/docs/changelog)
- [Google Cloud: Agent Platform Computer Use Sandbox](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sandbox/computer-use)
