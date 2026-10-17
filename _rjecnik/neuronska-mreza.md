---
layout: term
title: "Neuronska mreža"
english: "neural network"
term_slug: neuronska-mreza
description: "Neuronska mreža je model koji ulaz pretvara u izlaz kroz niz povezanih računskih koraka, a ponašanje mu određuju naučeni brojevi, parametri."
sort_key: "neuronska mrez{a"
letter: "N"
related: ["parametri", "tezine", "treniranje"]
source: blackboard/terminology/neural-network.md
generated_by: scripts/build_rjecnik.py
---

Neuronska mreža je model koji ulaz pretvara u izlaz kroz niz povezanih računskih koraka, a ponašanje mu određuju naučeni brojevi, parametri. Prema udžbeniku Goodfellowa, Bengija i Courvillea, mreža tokom treniranja (training) sama uči vrijednosti svojih parametara, umjesto da ih neko ručno zada. Parametri su težine, koje određuju koliko svaki ulaz utiče na rezultat, i pomaci (bias). Pri treniranju propagacija unazad šalje informaciju o grešci kroz mrežu od izlaza prema ulazu i tako izračuna gradijent: koliko bi se greška promijenila pri maloj promjeni svakog parametra. Parametri se zatim pomjeraju tako da greška opada. Veliki jezički model (large language model, LLM) je neuronska mreža s milijardama parametara.

**Izvori:**
- [Deep Learning, pogl. 4.3, 6 – Goodfellow et al., MIT Press 2016](https://www.deeplearningbook.org)
- [Llama 2: Open Foundation and Fine-Tuned Chat Models – Touvron et al., Meta 2023](https://arxiv.org/abs/2307.09288v2)
