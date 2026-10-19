---
layout: term
title: "Vještina"
english: "skill (Agent Skills; Claude, ChatGPT, Gemini \"Skills\")"
term_slug: vjestina
description: "Vještina je folder s uputama koje chatbot ili agent učitava tek kad zahtjev korisnika odgovara njenom opisu."
sort_key: "vjes{tina"
letter: "V"
related: ["prompt"]
source: blackboard/terminology/skill.md
generated_by: scripts/build_rjecnik.py
---

Vještina je folder s uputama koje chatbot ili agent učitava tek kad zahtjev korisnika odgovara njenom opisu. Glavni dio vještine je fajl SKILL.md. Na njegovom vrhu je zaglavlje s nazivom i opisom, a ispod su upute u Markdown formatu. Uz njega mogu stajati skripte, dodatni dokumenti i drugi fajlovi. Na početku rada model vidi samo naziv i opis, oko 100 tokena po vještini. Ostatak se učitava kad zatreba, pa vještine koje se ne koriste gotovo ne zauzimaju kontekstni prozor. Za razliku od trajnih uputa, vještina se ne primjenjuje u svakom razgovoru. Format je opisan u otvorenoj specifikaciji Agent Skills.

**Izvori:**
- [Specification, Agent Skills](https://agentskills.io/specification)
- [Agent Skills (overview), Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
