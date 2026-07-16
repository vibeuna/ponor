---
layout: post
title: "GitHub Copilot prelazi na naplatu po tokenu: šta to znači za vaš tim"
date: 2026-06-30
description: "GitHub je od 1. juna 2026. zamijenio kvote za premium zahtjeve novim sistemom AI Credits, gdje se potrošnja mjeri direktno po tokenu prema objavljenoj tablici cijena po modelu."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-06-30-github-copilot-billing.svg
---

Od 1. juna 2026., GitHub je zamijenio dosadašnji model kvota za premium zahtjeve novim sistemom naplate baziranim na upotrebi – AI Credits. Cijena je $0,01 po kreditu, a potrošnja se mjeri direktno na nivou tokena, ne po zahtjevu. Migracija je automatska za sve korisnike na mjesečnim planovima; godišnji pretplatnici prelaze tek istekom trenutnog plana.

## Šta se desilo

GitHub je [zvanično objavio](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) gašenje modela "premium requests" kvota koji je bio na snazi na svim Copilot planovima. Novi sistem – AI Credits – troši se proporcijalno broju tokena (ulaznih, izlaznih i kešovanih) prema objavljenoj tablici cijena po modelu dostupnoj u [GitHub dokumentaciji](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing).

Raspon cijena po modelu je značajan: GPT-5 nano košta $0,20/$1,25 po milion ulaznih/izlaznih tokena, dok Claude Fable 5 stoji $10/$50. Koji model koristite sada direktno utječe na brzinu trošenja kredita.

Važan izuzetak: dopunjavanja koda (code completions) i Next Edit Suggestions ostaju **van sistema AI Credits** na svim plaćenim planovima – neograničena upotreba. Ovo štiti najčešći dnevni slučaj upotrebe od neočekivanih troškova.

Prema [GitHub Docs stranici za individualne planove](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals), mjesečne kvote kredita su: Pro plan 1.500 kredita ($15 vrijednosti), Pro+ plan 7.000 kredita ($70 vrijednosti). Napomena: GitHub Blog je objavio različite iznose ($10 za Pro, $39 za Pro+) – ove cifre se razlikuju od onih u GitHub Docs-u, te do pojašnjenja koristimo Docs kao referentni izvor.

## Zašto je važno

Prijelaz s naplate po zahtjevu na naplatu po tokenu mijenja ekonomiku agentnih radnih tokova. Jedan zahtjev prema chatu koji pokreće višestepeni agentni radni tok – s pozivima alata, pretraživanjem po kodu i višestrukim modelskim prolazima – sada može konzumirati višestruko više kredita od jednostavnog upita. Ovo nije skriveni trošak, već trošak koji je sada vidljiv i mjerljiv.

GitHub navodi da je stari model "prestao biti održiv" zbog rastuće potrošnje inferencije u agentnim scenarijima – ovo je GitHub-ovo vlastito objašnjenje, ne nezavisno verificirana tvrdnja.

## Šta to znači u praksi

Za individualne developere koji koriste Copilot Chat, CLI i cloud agent, ključna promjena je **selekcija modela kao faktor troška**. Dok ste ranije birali model po kvalitetu odgovora, sada imate i cjenovnu dimenziju. Slanje dugačkih kontekstnih prozora skupljim modelima u petljama može brzo iscrpiti kvotu.

Za Business i Enterprise timove: krediti se pohranjuju na razini organizacije (pooling), a dostupni su granularni budžetski limiti na razini korisnika, cost-centra i enterprise-a. Ovo je operativna promjena – Copilot potrošnja postaje linija u budžetu s mogućnošću kontrole, a ne paušal.

Praktični koraci:

- Provjerite koji modeli su aktivni u vašim Copilot Chat sesijama i agentnim radnim tokovima.
- Za Business/Enterprise planove: konfigurirajte budžetske limite prije nego korisnici počnu s agentnim modovima.
- Godišnji pretplatnici nemaju pritisak – migracija dolazi tek istekom plana, ali vrijedi razumjeti mehaniku unaprijed.

## Kontekst

Prelaz na naplatu po tokenu slijedi isti obrazac koji su usvojili svi veći AI vendor-i (OpenAI, Anthropic, Google): flat-fee modeli s neograničenim premium zahtjevima pokazuju se ekonomski neodrživi kada korisnici prelaze s jednokratnih upita na agentne petlje koje troše redove veličine više tokena po sesiji.

## Izvori

- [GitHub Blog: GitHub Copilot prelazi na usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
- [GitHub Docs: Usage-based billing za individualne planove](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)
- [GitHub Docs: Modeli i cijene po tokenu](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing)
