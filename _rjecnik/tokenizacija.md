---
layout: term
title: "Tokenizacija"
english: "tokenization"
term_slug: tokenizacija
description: "Tokenizacija je postupak koji tekst dijeli na tokene (najmanje jedinice teksta s kojima model radi – riječi, dijelove riječi ili znakove) i svaki token pretv..."
sort_key: "tokenizacija"
letter: "T"
related: ["token", "veliki-jezicki-model"]
source: blackboard/terminology/tokenization.md
generated_by: scripts/build_rjecnik.py
---

Tokenizacija je postupak koji tekst dijeli na tokene (najmanje jedinice teksta s kojima model radi – riječi, dijelove riječi ili znakove) i svaki token pretvara u broj. Veliki jezički model (large language model, LLM) može obraditi tek takav niz brojeva. Dekodiranje radi obrnuto i vraća brojeve u tekst. Postoje tri pristupa. Podjela na cijele riječi traži ogroman vokabular (skup tokena koje model poznaje), a riječ koje u njemu nema ostaje nepoznata. Podjela na pojedinačne znakove daje mali vokabular, ali duge nizove u kojima svaka jedinica nosi malo značenja. Srednji put su podriječi (subword), a glavni algoritmi za njih su BPE, Unigram i WordPiece. U starijoj obradi jezika tokenizacija je značila samo podjelu na riječi i interpunkciju.

**Izvori:**
- [Tokenization algorithms – Hugging Face, Transformers dokumentacija](https://huggingface.co/docs/transformers/tokenizer_summary)
- [LLM Course, poglavlje 2.4: Tokenizers – Hugging Face](https://huggingface.co/learn/llm-course/chapter2/4)
