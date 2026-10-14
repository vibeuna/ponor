---
layout: term
title: "Tokenizator"
english: "tokenizer"
term_slug: tokenizator
description: "Tokenizator je program koji tekst dijeli na tokene: cijele riječi, dijelove riječi, pojedinačne znakove ili bajtove."
sort_key: "tokenizator"
letter: "T"
related: ["tokenizacija", "token", "fertilnost-tokenizatora", "vokabular"]
source: blackboard/terminology/tokenizer.md
generated_by: scripts/build_rjecnik.py
---

Tokenizator je program koji tekst dijeli na tokene: cijele riječi, dijelove riječi, pojedinačne znakove ili bajtove. Česte riječi obično ostaju cijele, a rijetke se dijele na podriječi (subword). Glavni algoritmi su BPE, koji koriste Llama, Gemma i Qwen2, zatim Unigram (T5) i WordPiece (BERT). Sennrich, Haddow i Birch primijenili su BPE u mašinskom prevođenju (machine translation) da bi model mogao obraditi i riječi kojih kao cjeline nema u vokabularu (skup tokena koje model poznaje): složenice, imena i posuđenice. Svaka porodica modela ima vlastiti tokenizator, pa broj tokena za isti tekst nije uporediv između modela.

**Izvori:**
- [Neural Machine Translation of Rare Words with Subword Units – Sennrich, Haddow, Birch, ACL 2016](https://arxiv.org/abs/1508.07909)
- [Tokenization algorithms – Hugging Face, Transformers dokumentacija](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)
