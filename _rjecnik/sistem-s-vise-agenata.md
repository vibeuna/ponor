---
layout: term
title: "Sistem s više agenata"
english: "multi-agent system"
term_slug: sistem-s-vise-agenata
description: "Sistem s više agenata je sistem u kojem nekoliko agenata radi na istom zadatku, svaki na svom dijelu posla."
sort_key: "sistem s vis{e agenata"
letter: "S"
related: ["agent", "orkestracija"]
source: blackboard/terminology/multi-agent-system.md
generated_by: scripts/build_rjecnik.py
---

Sistem s više agenata je sistem u kojem nekoliko agenata radi na istom zadatku, svaki na svom dijelu posla. Anthropic opisuje obrazac u kojem glavni agent pokreće podagente koji rade paralelno. OpenAI navodi dva obrasca: menadžerski, u kojem centralni agent poziva druge agente kao alate, i decentralizovani, u kojem agenti jedan drugom predaju zadatak. Prema Anthropicu, takvi sistemi troše oko 15 puta više tokena od običnog razgovora s modelom, pa se isplate samo za vrijedne zadatke. Anthropic navodi i da loše odgovaraju zadacima u kojima agenti trebaju zajednički kontekst ili mnogo zavise jedan od drugog, uključujući većinu programerskih zadataka.

**Izvori:**
- [How we built our multi-agent research system – Anthropic, 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- [A practical guide to building agents – OpenAI, 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
