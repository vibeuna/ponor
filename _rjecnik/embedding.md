---
layout: term
title: "Embedding"
english: "embedding"
term_slug: embedding
description: "Embedding je niz brojeva kojim se predstavlja tekst, tako da tekstovi sličnog značenja dobiju međusobno bliske nizove."
sort_key: "embedding"
letter: "E"
related: ["token", "veliki-jezicki-model"]
source: blackboard/terminology/embedding.md
generated_by: scripts/build_rjecnik.py
---

Embedding je niz brojeva kojim se predstavlja tekst, tako da tekstovi sličnog značenja dobiju međusobno bliske nizove. Takav niz zove se i embedding vektor. Udaljenost između dva niza mjeri koliko su tekstovi povezani: što je manja, to su sličniji. Na tome počivaju pretraga po značenju, grupisanje sličnih tekstova, preporuke i otkrivanje neuobičajenih unosa. Ilustracije radi, rečenice „auto mi je u kvaru“ i „vozilo ne radi“ nemaju nijednu zajedničku riječ, ali imaju slično značenje, pa bi trebale dobiti bliske nizove. Mikolov i saradnici iz Googlea pokazali su 2013. da naučeni zapisi riječi bilježe gramatičke i značenjske sličnosti. Embedding postoji i unutar velikog jezičkog modela (large language model, LLM): model svaki token prvo pretvara u embedding.

**Izvori:**
- [Embeddings – OpenAI, API dokumentacija](https://developers.openai.com/api/docs/guides/embeddings)
- [Efficient Estimation of Word Representations in Vector Space – Mikolov et al., Google 2013](https://arxiv.org/abs/1301.3781)
