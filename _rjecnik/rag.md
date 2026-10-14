---
layout: term
title: "RAG"
english: "retrieval-augmented generation (RAG)"
term_slug: rag
description: "Generisanje potpomognuto pretraživanjem (retrieval-augmented generation, RAG) je postupak u kojem komponenta za pretraživanje prvo pronađe relevantne dokumen..."
sort_key: "rag"
letter: "R"
related: ["kontekstni-prozor", "embedding"]
source: blackboard/terminology/rag.md
generated_by: scripts/build_rjecnik.py
---

Generisanje potpomognuto pretraživanjem (retrieval-augmented generation, RAG) je postupak u kojem komponenta za pretraživanje prvo pronađe relevantne dokumente, a jezički model ih zatim koristi dok generiše odgovor. Pristup su 2020. predstavili Lewis i saradnici. Polazili su od problema znanja koje model nosi u sebi nakon treniranja: do njega je teško doći i teško ga je ažurirati. U njihovom radu sistem je pretraživao Wikipediju, a odgovori su bili konkretniji i činjenično tačniji nego bez pretraživanja. Halucinacije (izmišljanje netačnih informacija) time nisu isključene: RAG ne garantuje tačnost, a odgovor zavisi od pronađenih dokumenata.

**Izvori:**
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks – Lewis et al., NeurIPS 2020](https://arxiv.org/abs/2005.11401)
