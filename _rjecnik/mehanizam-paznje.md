---
layout: term
title: "Mehanizam pažnje"
english: "attention mechanism"
term_slug: mehanizam-paznje
description: "Mehanizam pažnje (attention mechanism) omogućava modelu da, dok proizvodi sljedeći token, sam pronađe dijelove ulaznog teksta koji su za njega najvažniji."
sort_key: "mehanizam paz{nje"
letter: "M"
related: ["veliki-jezicki-model"]
source: blackboard/terminology/attention-mechanism.md
generated_by: scripts/build_rjecnik.py
---

Mehanizam pažnje (attention mechanism) omogućava modelu da, dok proizvodi sljedeći token, sam pronađe dijelove ulaznog teksta koji su za njega najvažniji. Bahdanau, Cho i Bengio opisali su ga 2014. u radu o mašinskom prevođenju (machine translation), objavljenom na konferenciji ICLR 2015: model uči da za svaku riječ prijevoda „pretražuje“ relevantne dijelove izvorne rečenice. Vaswani i saradnici predstavili su 2017. transformer, arhitekturu koja se oslanja samo na pažnju i napušta ranije gradivne elemente takvih modela. Transformer se brže trenira i lakše paralelizira, a danas je osnova velikih jezičkih modela (large language model, LLM). Pažnja modela nije isto što i ljudska pažnja.

**Izvori:**
- [Neural Machine Translation by Jointly Learning to Align and Translate – Bahdanau, Cho, Bengio, ICLR 2015](https://arxiv.org/abs/1409.0473)
- [Attention Is All You Need – Vaswani et al., 2017](https://arxiv.org/abs/1706.03762)
