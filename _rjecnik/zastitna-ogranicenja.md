---
layout: term
title: "Zaštitna ograničenja"
english: "guardrails"
term_slug: zastitna-ogranicenja
description: "Zaštitna ograničenja (guardrails) su provjere ulaza u jezički model i izlaza iz njega koje rade dok se aplikacija izvršava, izvan samog modela."
sort_key: "zas{titna ogranic{enja"
letter: "Z"
related: ["ljudski-nadzor", "agent"]
source: blackboard/terminology/guardrails.md
generated_by: scripts/build_rjecnik.py
---

Zaštitna ograničenja (guardrails) su provjere ulaza u jezički model i izlaza iz njega koje rade dok se aplikacija izvršava, izvan samog modela. Po tome se razlikuju od ponašanja koje model nauči tokom treniranja. Rebedea i saradnici navode šta takve provjere mogu: blokirati štetne teme, držati razgovor na unaprijed zadanom toku i nametnuti stil odgovora. U biblioteci OpenAI Agents SDK ulazna ograničenja provjeravaju korisnikov zahtjev, a izlazna odgovor agenta. Ako provjera ne prođe, izvršavanje se zaustavlja. Zaštitna ograničenja smanjuju rizik, ali ga ne uklanjaju.

**Izvori:**
- [NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails – Rebedea et al., EMNLP 2023](https://arxiv.org/abs/2310.10501)
- [Guardrails – OpenAI Agents SDK dokumentacija](https://openai.github.io/openai-agents-python/guardrails/)
