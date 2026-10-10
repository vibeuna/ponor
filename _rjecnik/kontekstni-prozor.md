---
layout: term
title: "Kontekstni prozor"
english: "context window"
term_slug: kontekstni-prozor
description: "Kontekstni prozor je sav tekst koji jezički model može uzeti u obzir dok generiše odgovor, uključujući i sam odgovor."
sort_key: "kontekstni prozor"
letter: "K"
related: ["veliki-jezicki-model", "token"]
source: blackboard/terminology/context-window.md
generated_by: scripts/build_rjecnik.py
---

Kontekstni prozor je sav tekst koji jezički model može uzeti u obzir dok generiše odgovor, uključujući i sam odgovor. To je radna memorija modela, odvojena od teksta iz kojeg je model učio. Mjeri se u tokenima. U prozor ulaze upute aplikacije, svaka poruka u razgovoru, priloženi dokumenti, rezultati alata i generisani odgovor, pa se u dugom razgovoru postepeno puni. Anthropic navodi da tačnost modela opada kako se prozor puni. Prema istraživanju Liua i saradnika, modeli informacije s početka i kraja često koriste bolje od onih iz sredine. Šta se dešava kad se prozor napuni, zavisi od proizvođača; neke chat aplikacije izbacuju najstarije poruke.

**Izvori:**
- [Context windows – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Lost in the Middle: How Language Models Use Long Contexts – Liu et al., TACL 2023](https://arxiv.org/abs/2307.03172)
