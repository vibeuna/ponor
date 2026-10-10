---
layout: term
title: "BPE"
english: "BPE"
term_slug: bpe
description: "BPE (byte-pair encoding) je algoritam koji gradi vokabular (skup tokena koje model poznaje) tako što u tekstu stalno spaja najčešći par susjednih simbola u n..."
sort_key: "bpe"
letter: "B"
related: ["tokenizacija", "podrijec"]
source: blackboard/terminology/bpe.md
generated_by: scripts/build_rjecnik.py
---

BPE (byte-pair encoding) je algoritam koji gradi vokabular (skup tokena koje model poznaje) tako što u tekstu stalno spaja najčešći par susjednih simbola u novi simbol. Postupak kreće od pojedinačnih znakova. Ako se, ilustracije radi, „r“ i „a“ najčešće pojavljuju jedno do drugog, postaju jedan simbol „ra“, pa se brojanje ponavlja. Veličina vokabulara jednaka je broju početnih znakova plus broju spajanja. Ideja potiče iz kompresije podataka, a Sennrich i saradnici prilagodili su je obradi jezika 2016. Varijanta na nivou bajtova kreće od 256 mogućih vrijednosti bajta, pa nijedan tekst nije nepoznat. Hugging Face navodi BPE kao najpopularniji algoritam u svojoj biblioteci, a prema istom izvoru koriste ga Llama, Gemma i Qwen2.

**Izvori:**
- [Neural Machine Translation of Rare Words with Subword Units – Sennrich et al., ACL 2016](https://aclanthology.org/P16-1162/)
- [Tokenization algorithms – Hugging Face, Transformers dokumentacija](https://huggingface.co/docs/transformers/tokenizer_summary)
