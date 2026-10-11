---
layout: term
title: "Fertilnost tokenizatora"
english: "tokenizer fertility"
term_slug: fertilnost-tokenizatora
description: "Fertilnost tokenizatora je prosječan broj tokena na koje tokenizator dijeli jednu riječ."
sort_key: "fertilnost tokenizatora"
letter: "F"
related: ["tokenizacija", "token", "podrijec"]
source: blackboard/terminology/tokenizer-fertility.md
generated_by: scripts/build_rjecnik.py
---

Fertilnost tokenizatora je prosječan broj tokena na koje tokenizator dijeli jednu riječ. Najmanja vrijednost je 1, kad je svaka riječ jedan token, a niža vrijednost je bolja. Visoka fertilnost znači da se riječi razbijaju na mnogo sitnih dijelova. Rust i saradnici (2021) pokazali su da tokenizator višejezičnog modela mBERT riječi na finskom, ruskom i turskom dijeli na znatno više dijelova nego tokenizatori modela napravljenih samo za te jezike. Najnižu fertilnost imao je engleski. U njihovoj studiji niža fertilnost išla je uz bolje rezultate na konkretnim zadacima, ali autori su poredili mali broj jezika i modela.

**Izvori:**
- [How Good is Your Tokenizer? On the Monolingual Performance of Multilingual Language Models – Rust et al., ACL 2021](https://aclanthology.org/2021.acl-long.243/)
