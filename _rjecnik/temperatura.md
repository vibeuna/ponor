---
layout: term
title: "Temperatura"
english: "temperature"
term_slug: temperatura
description: "Temperatura (temperature) je postavka koja se zadaje uz zahtjev jezičkom modelu i određuje koliko su odgovori nasumični: niža vrijednost daje fokusiranije i..."
sort_key: "temperatura"
letter: "T"
related: ["token", "veliki-jezicki-model"]
source: blackboard/terminology/temperature.md
generated_by: scripts/build_rjecnik.py
---

Temperatura (temperature) je postavka koja se zadaje uz zahtjev jezičkom modelu i određuje koliko su odgovori nasumični: niža vrijednost daje fokusiranije i predvidljivije odgovore, viša raznovrsnije. Univerzalna skala ne postoji. Kod OpenAI-ja raspon je 0–2, a zadana vrijednost 1; prema OpenAI-ju, vrijednost poput 0,8 daje nasumičnije, a 0,2 fokusiranije i determinističnije odgovore. Kod Anthropica raspon je 0,0–1,0, zadana vrijednost 1,0, a preporuka je vrijednost blizu 0 za analitičke i blizu 1 za kreativne zadatke. Anthropic upozorava da ni temperatura 0,0 ne daje potpuno determinističke rezultate.

**Izvori:**
- [OpenAI OpenAPI specifikacija, Chat Completions temperature – OpenAI](https://github.com/openai/openai-openapi)
- [Messages API – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/api/messages)
