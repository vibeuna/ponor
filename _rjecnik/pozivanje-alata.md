---
layout: term
title: "Pozivanje alata"
english: "tool calling / function calling"
term_slug: pozivanje-alata
description: "Pozivanje alata je mehanizam kojim jezički model traži od aplikacije da izvrši neku radnju i vrati mu rezultat."
sort_key: "pozivanje alata"
letter: "P"
related: ["alat", "agentska-petlja"]
source: blackboard/terminology/tool-calling.md
generated_by: scripts/build_rjecnik.py
---

Pozivanje alata je mehanizam kojim jezički model traži od aplikacije da izvrši neku radnju i vrati mu rezultat. Model pri tome sam ništa ne izvršava. Aplikacija mu pošalje popis dostupnih alata, model vrati strukturiran zahtjev s nazivom alata i argumentima, a aplikacija izvrši radnju i vrati rezultat. Model zatim odgovara ili poziva sljedeći alat. Ilustracije radi, na pitanje o današnjem vremenu model može zatražiti pretragu weba umjesto da odgovori iz sjećanja. Po zadanim postavkama model u svakom koraku sam odlučuje hoće li pozvati alat ili odgovoriti direktno. Argumente može popuniti i vrijednostima koje korisnik nije naveo. OpenAI i Anthropic koriste i naziv function calling za isti mehanizam.

**Izvori:**
- [Function calling – OpenAI, API dokumentacija](https://developers.openai.com/api/docs/guides/function-calling)
- [Tool use with Claude – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
