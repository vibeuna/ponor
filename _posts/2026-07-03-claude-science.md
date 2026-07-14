---
layout: post
title: "Anthropic pokrenuo Claude Science, beta workbench za naučna istraživanja"
date: 2026-07-03
description: "Claude Science objedinjuje alate, baze podataka i pristup računarskim resursima za naučnike u jednu aplikaciju — plus program koji do 50 istraživačkih projekata finansira sa do 30.000 dolara u compute credits."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-07-03-claude-science.svg
---

Anthropic je 30. juna 2026. objavio Claude Science — workbench (radno okruženje s integrisanim alatima) namijenjen naučnicima, koji u jednu aplikaciju objedinjuje alate, baze podataka i pristup računarskim resursima. Proizvod je u beta fazi i radi na postojećim Claude modelima, uključujući Claude Opus 4.8 — Anthropic izričito navodi da ne uvodi novi ili specijalizovani model za biologiju.

## Šta se desilo

Claude Science je aplikacija za macOS i Linux, dostupna korisnicima Pro, Max, Team i Enterprise planova (za Team i Enterprise uz administratorsko omogućavanje). U njenoj osnovi je orchestrator (koordinatorski agent) sa više od 60 unaprijed konfigurisanih alata (skills/konektora) za genomiku, analizu na nivou pojedinačnih ćelija, proteomiku, strukturnu biologiju i hemioinformatiku. Integrisani su izvori podataka poput UniProt, PDB, Ensembl, Reactome, ClinVar, ChEMBL i GEO.

Svaki rezultat i figura koju workbench proizvede nosi provenance (evidenciju porijekla rezultata: kod, okruženje, opis) — tačan kod, okruženje izvršavanja i opis na razumljivom jeziku. Cijela istorija sesije se čuva radi kasnije provjere, a korisnici mogu koristiti session forking (grananje sesije radi istraživanja varijanti analize) da odvoje varijantu analize bez gubitka prethodnog toka rada.

Alat uključuje i reviewer agent (agent koji provjerava rezultate) — poseban agent koji pregleda izlaze tražeći figure ili citate bez jasnog porijekla i neslaganja između koda i dobijenih rezultata. Anthropic navodi da ovaj mehanizam poboljšava pouzdanost izlaza; koliko je taj mehanizam u praksi tačan u hvatanju grešaka nije nezavisno provjereno, pa ovu tvrdnju treba čitati kao tvrdnju proizvođača, ne kao potvrđenu činjenicu.

Uz proizvod, Anthropic pokreće i program finansiranja: do 50 vanjskih istraživačkih projekata dobiće compute credits (dodijeljena sredstva za korištenje računarskih resursa) u vrijednosti do 30.000 dolara po projektu, uz dodatnih do 2.000 dolara po projektu koje obezbjeđuje Modal. Rok za prijave je 15. juli 2026, obavještenja o odabranim projektima stižu do 31. jula, a odabrani projekti se izvode od 1. septembra do 1. decembra 2026.

## Zašto je važno

Za programere je ovo prvenstveno primjer arhitekture, a ne novi model. Anthropic eksplicitno kaže da Claude Science "nije novi AI model niti sposobniji model za biologiju" — riječ je o proizvodnom sloju iznad postojećih modela. Ono što je stvarno novo jeste kombinacija: orchestrator sa desetinama unaprijed integrisanih konektora prema specijalizovanim naučnim bazama podataka, ugrađeno praćenje provenance na nivou svakog izlaza i reviewer agent kao dodatni sloj provjere.

Model provenance — kod, okruženje i opis vezani uz svaki rezultat, plus puna istorija sesije — je obrazac primjenjiv daleko izvan naučnog konteksta. Svaki agentni pipeline kojem je potrebna revizija (auditability) rezultata — od finansijske analize do inženjerskih izvještaja — suočava se s istim problemom: kako dokazati da je izlaz reproducibilan i kako je nastao. Claude Science pokazuje jedan konkretan način da se to riješi na nivou proizvoda, ne samo kao interna praksa tima.

## Šta to znači u praksi

Za programere koji grade slične sisteme, relevantne su tri stvari:

- **Obrazac orkestracije alata.** 60+ konektora organizovanih oko jednog orchestratora je konkretan primjer kako skalirati broj alata bez pretvaranja prompta u haos — vrijedi pogledati kako Anthropic strukturira otkrivanje i biranje alata (tool discovery) u ovakvom obimu.
- **Provenance kao dizajn-obrazac.** Bilježenje koda, okruženja i opisa uz svaki izlaz nije specifično za nauku — isti obrazac se može primijeniti na bilo koji agentni sistem gdje je reproducibilnost rezultata bitna.
- **Rok za prijavu na compute credits je 15. juli 2026.** Za timove koji rade na istraživačkim projektima u oblastima koje Anthropic pokriva (genomika, proteomika, strukturna biologija, hemioinformatika), ovo je konkretan i vremenski ograničen izvor besplatnih računarskih resursa.

Vrijedi napomenuti da su i reproducibilnost u praksi i stvarna preciznost reviewer agenta tvrdnje Anthropica, ne nezavisno potvrđene — korisno je testirati na sopstvenim podacima prije nego što se rezultati workbencha uzmu kao gotova činjenica.

## Izvori

- [Claude Science: an AI workbench for scientific research — Anthropic](https://www.anthropic.com/news/claude-science-ai-workbench)
