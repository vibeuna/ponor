---
layout: term
title: "Fino podešavanje"
english: "fine-tuning"
term_slug: fino-podesavanje
description: "Fino podešavanje je dodatno treniranje (training) već predtreniranog modela za određeni zadatak ili ponašanje, najčešće na označenim primjerima."
sort_key: "fino podes{avanje"
letter: "F"
related: ["predtreniranje", "treniranje"]
source: blackboard/terminology/fine-tuning.md
generated_by: scripts/build_rjecnik.py
---

Fino podešavanje je dodatno treniranje (training) već predtreniranog modela za određeni zadatak ili ponašanje, najčešće na označenim primjerima. Dolazi nakon predtreniranja (pre-training): opće znanje o jeziku model je već stekao iz velike količine teksta, a sada uči konkretan posao. Građa modela pri tome ostaje gotovo ista. Googleovom BERT-u, prema njegovim autorima, na izlazu se dodaje samo jedan dodatni dio. Ilustracije radi, opći jezički model može se fino podesiti da recenzije razvrstava na pozitivne i negativne. Pojam je širok: OpenAI ga u radu iz 2022. koristi i za učenje iz primjera koje su napisali ljudi i za učenje iz ljudskog rangiranja odgovora.

**Izvori:**
- [Improving Language Understanding by Generative Pre-Training – Radford et al., OpenAI 2018](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding – Devlin et al., Google 2018](https://arxiv.org/abs/1810.04805)
- [Training language models to follow instructions with human feedback – Ouyang et al., OpenAI 2022](https://arxiv.org/abs/2203.02155)
