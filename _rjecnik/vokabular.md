---
layout: term
title: "Vokabular"
english: "vocabulary (of a model or tokenizer)"
term_slug: vokabular
description: "Vokabular je fiksan skup tokena koje tokenizator može proizvesti, odnosno skup tokena koje model poznaje."
sort_key: "vokabular"
letter: "V"
related: ["tokenizator", "token", "podrijec", "bpe"]
source: blackboard/terminology/vocabulary.md
generated_by: scripts/build_rjecnik.py
---

Vokabular je fiksan skup tokena koje tokenizator može proizvesti, odnosno skup tokena koje model poznaje. BPE ga gradi postepeno: spaja parove koji se najčešće javljaju zajedno, sve dok vokabular ne dostigne zadanu veličinu. GPT-2 ima vokabular od 50.257 tokena: 256 osnovnih bajtova, 50.000 spajanja i jedan poseban token za kraj teksta. Llama 3 ima vokabular od 128 hiljada tokena, a Meta tvrdi da taj model zahvaljujući tome „mnogo efikasnije kodira jezik“.

**Izvori:**
- [Tokenization algorithms – Hugging Face, Transformers dokumentacija](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)
- [Introducing Meta Llama 3 – Meta AI, 2024](https://ai.meta.com/blog/meta-llama-3/)
