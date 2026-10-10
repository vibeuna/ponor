---
layout: term
title: "Agentska petlja"
english: "agent loop"
term_slug: agentska-petlja
description: "Agentska petlja je ciklus koji se ponavlja dok agent radi: model zatraži alat, aplikacija ga izvrši i vrati rezultat, a model na osnovu tog rezultata nastavlja."
sort_key: "agentska petlja"
letter: "A"
related: ["agent", "pozivanje-alata"]
source: blackboard/terminology/agent-loop.md
generated_by: scripts/build_rjecnik.py
---

Agentska petlja je ciklus koji se ponavlja dok agent radi: model zatraži alat, aplikacija ga izvrši i vrati rezultat, a model na osnovu tog rezultata nastavlja. Petlja traje dok god model traži nove alate. Uslove za završetak izvori navode različito. Kod OpenAI-ja to su, npr., konačan odgovor, greška ili najveći dozvoljeni broj koraka. Kod Anthropica petlja staje čim se model zaustavi iz bilo kojeg razloga osim zahtjeva za alat. Prema Anthropicu, agent u svakom koraku dobija stvarne podatke iz okruženja, a ograničenje broja koraka čuva kontrolu nad njim. Izraz je radni naziv iz dokumentacije OpenAI-ja i Anthropica, a ne ustaljen standard. Akademski prethodnik je ReAct (2022), pristup u kojem model smjenjuje zaključivanje (reasoning) i radnje.

**Izvori:**
- [How tool use works – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [Building effective agents – Anthropic, 2024](https://www.anthropic.com/engineering/building-effective-agents)
- [A practical guide to building agents – OpenAI, 2025](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [ReAct: Synergizing Reasoning and Acting in Language Models – Yao et al., arXiv 2022](https://arxiv.org/abs/2210.03629)
