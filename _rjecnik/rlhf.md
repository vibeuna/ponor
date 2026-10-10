---
layout: term
title: "RLHF"
english: "RLHF"
term_slug: rlhf
description: "RLHF (reinforcement learning from human feedback) je tehnika finog podešavanja (fine-tuning) u kojoj model uči davati odgovore kakve ljudi preferiraju, na os..."
sort_key: "rlhf"
letter: "R"
related: ["fino-podesavanje", "treniranje"]
source: blackboard/terminology/rlhf.md
generated_by: scripts/build_rjecnik.py
---

RLHF (reinforcement learning from human feedback) je tehnika finog podešavanja (fine-tuning) u kojoj model uči davati odgovore kakve ljudi preferiraju, na osnovu toga kako ljudi rangiraju njegove odgovore. Christiano i saradnici pokazali su 2017., na igrama Atari i zadacima iz robotike, da cilj mogu odrediti poređenja ljudi bez stručnog znanja, bez ručno zapisanog pravila nagrađivanja. OpenAI-jev InstructGPT (2022) prvo se trenira na odgovorima koje su napisali ljudi. Zatim ljudi porede i rangiraju njegove odgovore na isti prompt. Na kraju model dobija nagradu za više rangirane odgovore i uči da ih češće daje. Prema OpenAI-ju, ocjenjivači su češće birali manji InstructGPT nego znatno veći GPT-3, ali samo na promptovima korisnika OpenAI-jevih modela. InstructGPT i dalje pravi jednostavne greške.

**Izvori:**
- [Deep Reinforcement Learning from Human Preferences – Christiano et al., OpenAI/DeepMind 2017](https://arxiv.org/abs/1706.03741)
- [Training language models to follow instructions with human feedback – Ouyang et al., OpenAI 2022](https://arxiv.org/abs/2203.02155)
