---
layout: term
title: "Orkestracija"
english: "orchestration"
term_slug: orkestracija
description: "Orkestracija je usklađivanje rada jezičkih modela i alata u jednom sistemu: ko radi koji dio zadatka, kojim redom i kako se rezultati spajaju."
sort_key: "orkestracija"
letter: "O"
related: ["sistem-s-vise-agenata"]
source: blackboard/terminology/orchestration.md
generated_by: scripts/build_rjecnik.py
---

Orkestracija je usklađivanje rada jezičkih modela i alata u jednom sistemu: ko radi koji dio zadatka, kojim redom i kako se rezultati spajaju. Izraz nema ustaljeno značenje. Anthropic ga koristi za tokove rada (workflow), u kojima programski kod unaprijed određuje putanju. Isti izvor opisuje i obrazac u kojem centralni model, orkestrator, dijeli zadatak na dijelove, prosljeđuje ih drugim modelima i spaja njihove rezultate. OpenAI orkestraciju dijeli na sisteme s jednim agentom koji radi u petlji i sisteme s više agenata, uz preporuku da se počne jednostavno. Pojam nema veze s orkestracijom softverske infrastrukture u sistemima poput Kubernetesa.

**Izvori:**
- [Building effective agents – Anthropic, 2024](https://www.anthropic.com/engineering/building-effective-agents)
- [A practical guide to building agents – OpenAI, 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
