---
layout: term
title: "Jezik s malo resursa"
english: "low-resource language"
term_slug: jezik-s-malo-resursa
description: "Jezik s malo resursa je jezik za koji postoji malo podataka dostupnih za modele: neoznačenog teksta i označenih podataka."
sort_key: "jezik s malo resursa"
letter: "J"
related: ["veliki-jezicki-model", "treniranje"]
source: blackboard/terminology/low-resource-language.md
generated_by: scripts/build_rjecnik.py
---

Jezik s malo resursa je jezik za koji postoji malo podataka dostupnih za modele: neoznačenog teksta i označenih podataka. Resurs ovdje znači podatke, ne broj govornika. Joshi i saradnici (2020) svrstali su više od 7.000 jezika u šest klasa prema dostupnim podacima i pokazali velike razlike među njima. Fiksna granica ne postoji: oznaka je relativna i zavisi od zadatka. Posljedice su praktične. Petrov i saradnici (2023) pokazali su da isti tekst preveden na različite jezike može imati i do 15 puta više tokena. To utiče na cijenu, brzinu i to koliko teksta stane u kontekstni prozor (context window). Prema istoj studiji, modeli su slabiji izvan glavnih jezika, posebno kod jezika s malo resursa.

**Izvori:**
- [The State and Fate of Linguistic Diversity and Inclusion in the NLP World – Joshi et al., ACL 2020](https://aclanthology.org/2020.acl-main.560/)
- [Language Model Tokenizers Introduce Unfairness Between Languages – Petrov et al., NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/74bb24dca8334adce292883b4b651eda-Abstract.html)
