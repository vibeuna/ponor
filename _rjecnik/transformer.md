---
layout: term
title: "Transformer"
english: "transformer"
term_slug: transformer
description: "Transformer je arhitektura modela na kojoj se zasnivaju veliki jezički modeli (large language models, LLM)."
sort_key: "transformer"
letter: "T"
related: ["veliki-jezicki-model"]
source: blackboard/terminology/transformer.md
generated_by: scripts/build_rjecnik.py
---

Transformer je arhitektura modela na kojoj se zasnivaju veliki jezički modeli (large language models, LLM). Predstavljen je 2017. u Googleovom radu „Attention Is All You Need“. Njegova osnova je mehanizam pažnje (attention mechanism): pri obradi svake riječi model odmjerava koliko su za nju važne ostale riječi u istom tekstu. Za razliku od ranijih modela, transformer ne obrađuje tekst korak po korak, riječ za riječju. Zato se posao lakše raspoređuje na više procesora istovremeno, a treniranje (training) je brže. Pošto ne čita redom, redoslijed riječi mu se daje posebno, kao dodatni podatak o položaju. Prvi transformer bio je model za prevođenje, testiran na parovima engleski–njemački i engleski–francuski, a ne chatbot.

**Izvori:**
- [Attention Is All You Need – Vaswani et al., Google 2017](https://arxiv.org/abs/1706.03762)
- [A Survey of Large Language Models – Zhao et al., arXiv 2023](https://arxiv.org/abs/2303.18223)
