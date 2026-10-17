---
layout: term
title: "Težine"
english: "model weights"
term_slug: tezine
description: "Težine su naučeni brojevi u modelu koji određuju koliko svaki ulaz utiče na rezultat."
sort_key: "tez{ine"
letter: "T"
related: ["parametri", "otvorene-tezine", "treniranje"]
source: blackboard/terminology/model-weights.md
generated_by: scripts/build_rjecnik.py
---

Težine su naučeni brojevi u modelu koji određuju koliko svaki ulaz utiče na rezultat. Ne zadaje ih programer: postavlja ih treniranje (training), koje ih malim koracima mijenja dok greška modela na primjerima ne opadne. Same po sebi težine ne rade ništa. Definicija Open Source Initiative (OSAID 1.0) opisuje ih kao skup naučenih parametara koji se postavljaju na arhitekturu modela, pa tek zajedno s njom daju izlaz. Kad proizvođač objavi težine bez podataka za treniranje i koda, govori se o otvorenim težinama. Težine i pomaci (bias) zajedno čine parametre modela.

**Izvori:**
- [Deep Learning, pogl. 5.1.4 – Goodfellow et al., MIT Press 2016](https://www.deeplearningbook.org)
- [The Open Source AI Definition 1.0 – Open Source Initiative](https://opensource.org/ai/open-source-ai-definition)
