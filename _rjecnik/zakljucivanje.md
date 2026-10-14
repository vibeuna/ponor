---
layout: term
title: "Zaključivanje"
english: "reasoning"
term_slug: zakljucivanje
description: "Zaključivanje (reasoning) kod velikih jezičkih modela (large language model, LLM) označava rješavanje zadataka koji zahtijevaju više koraka."
sort_key: "zakljuc{ivanje"
letter: "Z"
related: ["veliki-jezicki-model"]
source: blackboard/terminology/reasoning.md
generated_by: scripts/build_rjecnik.py
---

Zaključivanje (reasoning) kod velikih jezičkih modela (large language model, LLM) označava rješavanje zadataka koji zahtijevaju više koraka. Wei i saradnici pokazali su 2022. da LLM postiže bolje rezultate na aritmetičkim, zdravorazumskim i simboličkim zadacima kada prije odgovora ispiše međukorake. Ispisani koraci ipak ne pokazuju pouzdano šta je model stvarno koristio. Chen i saradnici iz Anthropica davali su modelima nagovještaje i provjeravali da li ispisani koraci otkrivaju njihovo korištenje. U većini testiranih postavki to se dešavalo u najmanje 1% slučajeva u kojima je model koristio nagovještaj, ali često u manje od 20%. Da li jezički modeli zaključuju u ljudskom smislu, i dalje je sporno.

**Izvori:**
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models – Wei et al., 2022](https://arxiv.org/abs/2201.11903)
- [Reasoning Models Don't Always Say What They Think – Chen et al., Anthropic 2025](https://arxiv.org/abs/2505.05410)
