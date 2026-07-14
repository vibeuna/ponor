---
layout: post
title: "xAI objavio Grok Imagine Video 1.5: native audio i 720p za dizajnere koji rade s AI videom"
date: 2026-06-20
description: "Grok Imagine Video 1.5 generiše video s native audio u single-pass-u, 720p, $4,20/min API - trenutno #1 na Image-to-Video Arena leaderboardu."
category: vijesti
audience: designers
read_time: 4
image: /assets/images/2026-06-20-grok-video.svg
---

Prema sekundarnom izvještavanju iz više neovisnih izvora, xAI je lansirao Grok Imagine Video 1.5 - model koji iz jednog teksta ili slike generiše video klip s automatski sinhroniziranim zvukom. Za dizajnere koji eksperimentišu s AI videom u prototipiraniju i client deliverables, ovo donosi promjenu koja nije arhitekturalna, nego praktična: audio više nije poseban korak.

## Šta se desilo

Preview verzija je prema izvorima bila dostupna 31. maja 2026; opšta dostupnost je najavljena 17. juna 2026. Model generira klipove od 6 do 15 sekundi u rezolucijama 480p ili 720p, pri 24 fps. Prema xAI (prema sekundarnom izvještavanju - primarni izvor, x.ai/news/grok-imagine-video-1-5, nije bio dostupan zbog HTTP 403 greške), audio se - dijalog, SFX, ambijent, muzika - generiše u single-pass-u, bez posebnog modela za sinhronizaciju.

Paralelno s tim, dostupna je i brža varijanta, Video 1.5 Fast, koja generira 6-sekundni 720p klip za oko 25 sekundi, u poređenju s 40+ sekundi koliko je trebalo verziji 1.0.

Model je dostupan putem Imagine API-ja, grok.com/imagine platforme te iOS i Android aplikacija.

## Zašto je važno za dizajnere

Dosad je AI video za dizajnere bio pretežno tihi alat - koristan za moodboards i animirane mockupe, ali nepotpun kao isporučivi materijal. Native audio mijenja taj omjer: klip koji izlazi iz modela bliže je finaliziranom artefaktu koji možete pokazati klijentu ili ugraditi u prototip. Naravno, "bliže" ne znači "gotov" - kvalitet govora i sinhronizacije nije nezavisno testiran i ne postoje objavljene evaluacije izvan vendor-odabranih primjera.

Cijenovna tačka je posebno relevantna za manje studije i indie dizajnere: prema sekundarnom izvještavanju, API košta $4,20 po minuti, u poređenju s oko $30 po minuti za Sora 2 Pro. Ta razlika od sedam puta ne znači nužno isti output quality-per-dollar - upscaling, visual fidelity i konzistentnost rezultata ovise o promptu i nisu poredivi na osnovu samog omjera cijena. Ali onima kojima je $30/min bila administrativna barijera, ova tačka otvara praktično eksperimentisanje bez posebnog budžeta.

## Šta to znači u praksi

Brzina inferencije direktno određuje upotrebljive interakcijske obrasce. Dvadesetpet sekundi za 6-sekundni klip nije dovoljno brzo za real-time feedback, ali je sasvim prihvatljivo za asinkroni radni tok: submitujete prompt, radite nešto drugo, klip je spreman za kratko. Za UI dizajn to znači da progress affordances moraju biti dizajnirani za čekanje od 20–60 sekundi - spinner koji korisnik može minimizirati, background task notifikacija, ili batch interface koji paralelno procesira više klipova.

Grok Imagine Video 1.5 trenutno drži prvo mjesto na Image-to-Video Arena leaderboardu (arena.ai) s Elo skorom blizu 1.330, što je porast od 52 Elo poena u odnosu na verziju 1.0. Važno je razumjeti šta taj leaderboard zapravo mjeri: radi se o skupnim glasovima stvarnih korisnika koji u blind A/B poređenjima biraju koji od dva video klipa izgleda bolje - crowd-sourced preferencija, ne automatizirani benchmark na objektivnim metrikama. Ranking odražava estetsku preferenciju na općenitim promptovima i mijenja se kontinuirano dok pristižu novi glasovi. Na leaderboardu ispred sebe ostavlja Sora 2, Veo 3.1, Seedance 2.0 i Kling, prema izvještavanju iz više izvora - ali ove pozicije nisu fiksne.

"Bolja fizika i pokret" je tvrdnja iz vendor materijala, demonstrirana samo u vendor-odabranim primjerima. Nije nezavisno verifikovano.
  
## Kontekst

Grok Imagine Video 1.0 je postojao ranije; verzija 1.5 donosi tri stvari koje 1.0 nije imao: native audio u single-pass-u, brži inference variant, i novi product-layer features (Projects sidebar, multi-agent paralelna generacija, pretraga biblioteke). Arena #1 pozicija je nova - verzija 1.0 je nije imala.

Za dizajnerski workflow, ključno pitanje nije je li ovo "best" model - leaderboard pozicija to ne garantuje za vaš specifičan use case - već ima li to smisla kao alat za konkretni zadatak: animirani brief za klijenta, prototype s audio feedbackom, mood reel za prezentaciju. Na toj razini, $4,20/min API uz 25-sekundnu brzinu inferencije i native audio čini ga dostupnim alatom za testiranje.

## Izvori

- [TechTimes - Grok Imagine Video 1.5 goes live](https://www.techtimes.com/articles/318635/20260618/grok-imagine-video-15-goes-live-xai-tops-ai-video-leaderboard-86-percent-below-sora.htm) - TechTimes, 18. juni 2026.
- [The Decoder - xAI updates Grok Imagine to 1.5](https://the-decoder.com/xai-updates-grok-imagine-to-1-5-with-image-to-video-generation-at-720p-resolution/) - The Decoder
- [Digg - Grok Imagine Video 1.5](https://digg.com/ai/mgbaou3r) - Digg, citira arena.ai leaderboard podatke
- [explainx.ai - Grok Imagine Video 1.5 release](https://explainx.ai/blog/grok-imagine-video-1-5-xai-release-2026) - explainx.ai
- [xAI zvanična objava](https://x.ai/news/grok-imagine-video-1-5) - HTTP 403; nije korišteno kao izvor
