---
layout: term
title: "Model u oblaku"
english: "cloud model"
term_slug: model-u-oblaku
description: "Model u oblaku je jezički model koji radi na serverima firme koja nudi uslugu, a ne na računaru korisnika."
sort_key: "model u oblaku"
letter: "M"
related: ["lokalni-model"]
source: blackboard/terminology/cloud-model.md
generated_by: scripts/build_rjecnik.py
---

Model u oblaku je jezički model koji radi na serverima firme koja nudi uslugu, a ne na računaru korisnika. Korisnik šalje prompt preko interneta i dobija odgovor nazad. U Ollami takve modele označava oznaka `cloud`, npr. `gemma4:cloud`: program je instaliran lokalno, ali model radi na Ollaminim serverima. Ollama navodi da te promptove obrađuje, ali ih ne čuva i ne koristi za treniranje. To je tvrdnja firme koja se ne može nezavisno provjeriti. Funkcije u oblaku u Ollami su uključene odmah nakon instalacije i isključuju se postavkom `OLLAMA_NO_CLOUD=1`.

**Izvori:**
- [FAQ – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/faq.mdx)
