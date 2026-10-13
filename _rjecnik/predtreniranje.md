---
layout: term
title: "Predtreniranje"
english: "pre-training"
term_slug: predtreniranje
description: "Predtreniranje je prva, opšta faza treniranja (training) jezičkog modela, u kojoj model uči iz velike količine neoznačenog teksta."
sort_key: "predtreniranje"
letter: "P"
related: ["treniranje", "fino-podesavanje"]
source: blackboard/terminology/pre-training.md
generated_by: scripts/build_rjecnik.py
---

Predtreniranje je prva, opšta faza treniranja (training) jezičkog modela, u kojoj model uči iz velike količine neoznačenog teksta. Razlog je praktičan: neoznačenog teksta ima u izobilju, a označenih podataka za pojedinačne zadatke malo. Nakon predtreniranja slijedi fino podešavanje (fine-tuning) za konkretan zadatak. Šta model tačno uči zavisi od pristupa. OpenAI-jev model GPT iz 2018. predviđa sljedeći token, a Googleov BERT pogađa namjerno sakrivene tokene u rečenici.

**Izvori:**
- [Improving Language Understanding by Generative Pre-Training – Radford et al., OpenAI 2018](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding – Devlin et al., Google 2018](https://arxiv.org/abs/1810.04805)
