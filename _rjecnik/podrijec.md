---
layout: term
title: "Podriječ"
english: "subword"
term_slug: podrijec
description: "Podriječ je dio riječi koji model tretira kao zaseban token."
sort_key: "podrijec{"
letter: "P"
related: ["token", "tokenizacija"]
source: blackboard/terminology/subword.md
generated_by: scripts/build_rjecnik.py
---

Podriječ je dio riječi koji model tretira kao zaseban token. Podriječi su srednji put između cijelih riječi i pojedinačnih znakova. Vokabular (skup tokena koje model poznaje) ostaje ograničen, a rijetke i nove riječi i dalje se mogu zapisati kao nizovi podriječi. Ako vokabular sadrži i sve pojedinačne znakove ili bajtove, tako se može zapisati svaka riječ. Sennrich i saradnici ističu da je ovakav zapis ispod nivoa riječi posebno potreban jezicima u kojima se lako tvore nove riječi, npr. slaganjem, ili koji imaju mnogo oblika iste riječi. Podriječ je statistička jedinica, ne gramatički dio riječi. Riječ „nezaboravnog“ mogla bi se, ilustracije radi, podijeliti na „nezabo“ + „ravnog“, mimo prefiksa, korijena i nastavka.

**Izvori:**
- [Neural Machine Translation of Rare Words with Subword Units – Sennrich et al., ACL 2016](https://aclanthology.org/P16-1162/)
- [Tokenization algorithms – Hugging Face, Transformers dokumentacija](https://huggingface.co/docs/transformers/tokenizer_summary)
