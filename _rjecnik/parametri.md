---
layout: term
title: "Parametri"
english: "parameters (model size)"
term_slug: parametri
description: "Parametri su vrijednosti koje određuju ponašanje modela: težine i pomaci (bias), naučeni tokom treniranja (training)."
sort_key: "parametri"
letter: "P"
related: ["tezine"]
source: blackboard/terminology/parameters.md
generated_by: scripts/build_rjecnik.py
---

Parametri su vrijednosti koje određuju ponašanje modela: težine i pomaci (bias), naučeni tokom treniranja (training). Njihov broj je uobičajena mjera veličine jezičkog modela. Meta je Llamu 2 objavila u veličinama od 7, 13 i 70 milijardi parametara, što se piše 7B, 13B i 70B. Ti brojevi su zaokruženi: model nazvan "7B" u prvom LLaMA radu ima 6,7 milijardi parametara. Proizvođači ne broje uvijek isto. Kartica modela Qwen3-8B navodi 8,2 milijarde parametara ukupno i 6,95 milijardi bez embeddinga. Parametre modela ne treba miješati s podešavanjima programa, koja se također zovu parametri.

**Izvori:**
- [Deep Learning, pogl. 5.1.4 – Goodfellow et al., MIT Press 2016](https://www.deeplearningbook.org)
- [Llama 2: Open Foundation and Fine-Tuned Chat Models – Touvron et al., Meta 2023](https://arxiv.org/abs/2307.09288v2)
- [LLaMA: Open and Efficient Foundation Language Models – Touvron et al., Meta 2023](https://arxiv.org/abs/2302.13971v1)
- [Qwen3-8B – Qwen, Hugging Face](https://huggingface.co/Qwen/Qwen3-8B)
