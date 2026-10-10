---
layout: term
title: "Prompt"
english: "prompt"
term_slug: prompt
description: "Prompt je uputa ili upit koji unosite jezičkom modelu: pitanje, zadatak ili tekst koji treba obraditi."
sort_key: "prompt"
letter: "P"
related: ["token", "veliki-jezicki-model"]
source: blackboard/terminology/prompt.md
generated_by: scripts/build_rjecnik.py
---

Prompt je uputa ili upit koji unosite jezičkom modelu: pitanje, zadatak ili tekst koji treba obraditi. Model ga tretira kao početak teksta koji treba nastaviti. Kroz prompt se modelu može zadati i potpuno nov zadatak, bez ikakve izmjene samog modela. Ako prompt sadrži nekoliko riješenih primjera, model može nastaviti po istom obrascu. Ilustracije radi, to mogu biti tri rečenice s prijevodom i četvrta bez njega. Brown i saradnici iz OpenAI-ja opisali su ovaj pristup 2020. U širem smislu, prompt je sve što model primi, uključujući upute aplikacije i cijeli dosadašnji razgovor. Sve to zauzima prostor u kontekstnom prozoru (context window).

**Izvori:**
- [Language Models are Few-Shot Learners – Brown et al., OpenAI 2020](https://arxiv.org/abs/2005.14165)
- [Pre-train, Prompt, and Predict – Liu et al., CMU 2021](https://arxiv.org/abs/2107.13586)
- [Context windows – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/build-with-claude/context-windows)
