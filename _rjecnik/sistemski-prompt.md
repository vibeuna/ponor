---
layout: term
title: "Sistemski prompt"
english: "system prompt"
term_slug: sistemski-prompt
description: "Sistemski prompt (system prompt) je skup uputa koje aplikacija daje modelu prije razgovora s korisnikom, na primjer cilj ili uloga koju model treba preuzeti."
sort_key: "sistemski prompt"
letter: "S"
related: ["prompt", "kontekstni-prozor"]
source: blackboard/terminology/system-prompt.md
generated_by: scripts/build_rjecnik.py
---

Sistemski prompt (system prompt) je skup uputa koje aplikacija daje modelu prije razgovora s korisnikom, na primjer cilj ili uloga koju model treba preuzeti. Kod Anthropica je to zaseban parametar `system`, a ne poruka u samom razgovoru. OpenAI takve upute opisuje kao upute programera koje model treba slijediti bez obzira na poruke korisnika; od modela o1 nadalje one idu kroz poruke s ulogom `developer` umjesto `system`. Naziv i tehnička izvedba razlikuju se od proizvođača do proizvođača. Krajnji korisnik sistemski prompt obično ne vidi, a ništa ne garantuje da će ga model u potpunosti poštovati.

**Izvori:**
- [Messages API, parametar system – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/api/messages)
- [OpenAI OpenAPI specifikacija, Developer message – OpenAI](https://github.com/openai/openai-openapi)
