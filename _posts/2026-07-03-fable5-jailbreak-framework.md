---
layout: post
title: "Anthropic objavljuje detalje o cyber-safeguard klasifikatorima za Fable 5 i predlaže zajednički okvir za mjerenje ozbiljnosti jailbreak napada"
date: 2026-07-03
description: "Anthropic je, zajedno sa Amazonom, Microsoftom i Googleom, predstavio rani nacrt okvira za ocjenjivanje ozbiljnosti jailbreak napada — Cyber Jailbreak Severity — i detaljno opisao klasifikatore koji štite Fable 5."
category: vijesti
audience: developers
read_time: 4
image: /assets/images/2026-07-03-fable5-jailbreak-framework.svg
---

Anthropic je 2. jula 2026. objavio tehničke detalje o classifier (klasifikator, sistem za kategorizaciju zahtjeva) sistemu koji štiti Fable 5 od zloupotrebe u kibersigurnosnom kontekstu, te zajedno sa Amazonom, Microsoftom i Googleom predstavio rani nacrt okvira za ocjenjivanje ozbiljnosti jailbreak napada — Cyber Jailbreak Severity (CJS).

## Šta se desilo

Anthropic je opisao četiri nivoa na kojima classifier kategorizuje zahtjeve vezane za kibersigurnost koji stižu Fable 5: zabranjeni zahtjevi (razvoj ransomwarea, malwarea), visokorizični zahtjevi dvostruke namjene (dual-use) (penetration testing, razvoj exploita — blokirani dok se ne uspostave kontrole pristupa), niskorizični zahtjevi dvostruke namjene (skeniranje mreža, OSINT (obavještajni rad iz otvoreno dostupnih izvora) — nadgledani, ali dozvoljeni) i benigni zahtjevi (sigurno programiranje, zakrpe — potpuno dozvoljeni).

Uz to, četiri kompanije su pod nazivom Project Glasswing predstavile prijedlog CJS skale ozbiljnosti: jailbreak tehnike se boduju na logaritamskoj skali od 0 do 10, podijeljenoj u pojasove od CJS-0 do CJS-4, prema četiri dimenzije — koliko napadaču daje sposobnosti iznad postojećih alata, koliko je širok raspon ofanzivnih zadataka koje omogućava, koliko je lako naoružati ga u praksi i koliko je lako otkriti da je iskorišten. Anthropic izričito naglašava da CJS nije finalizovan niti usvojen kao industrijski standard — riječ je o ranom nacrtu koji su zajednički razvile četiri kompanije.

Objava dolazi nakon što je Fable 5 bio suspendovan 12. juna zbog američke direktive o izvoznim ograničenjima (nakon što su Amazonovi istraživači pronašli propust koji je omogućavao zaobilaženje sigurnosnih mjera), a zatim ponovo globalno pušten u rad 1. jula sa poboljšanim classifierom.

## Zašto je važno

Za developere koji grade na Claude Platform-i, ovo je prvi put da Anthropic javno detaljno opisuje kako se zahtjevi vezani za kibersigurnost automatski kategorizuju i gejtuju na nivou modela — što direktno utiče na to koji API pozivi prolaze, a koji se blokiraju ili preusmjeravaju.

CJS je značajan i kao presedan: ovo je prvi javno predstavljen pokušaj da četiri velika AI labaratorija — Anthropic, Amazon, Microsoft i Google — dogovore zajedničku taksonomiju za mjerenje ozbiljnosti jailbreak napada, umjesto da svaka kompanija koristi sopstvenu internu skalu. Anthropic navodi da namjerava primjenjivati mjere ublažavanja "čim se ozbiljnost potvrdi" za najteže kategorije jailbreak napada, te da je uspostavio nadzor kanala za prijavu jailbreak pokušaja 24 sata dnevno — ovo je Anthropicova vlastita tvrdnja o vlastitom proizvodu, ne nezavisno potvrđena činjenica.

## Šta to znači u praksi

Za developere i istraživače sigurnosti postoji konkretan kanal za učešće: aktivan je HackerOne program za prijavu kandidata za jailbreak Fable 5, kao i posvećena email adresa (cyber-safeguards@anthropic.com). Ko gradi alate ili agente koji dodiruju kibersigurnosne zadatke — bilo penetration testing, skeniranje ranjivosti ili automatizovano pisanje sigurnosnih zakrpa — treba računati na to da će zahtjevi prolaziti kroz ove classifier nivoe, te da se ponašanje modela može mijenjati kako se CJS okvir razvija.

Vrijedi napomenuti da CJS, iako ambiciozan, za sada ostaje nacrt bez formalnog upravljačkog tijela ili usvojenog standarda — nije uporediv sa zrelim, formalno upravljanim standardima poput onih koje održava FIRST.org u drugim domenima kibersigurnosti. Google i Microsoft su potvrdili saradnju na razvoju okvira, ali konkretni rokovi za implementaciju CJS-a u njihovim proizvodima za sada nisu poznati.

## Izvori

- [More details on Fable 5's cyber safeguards and our jailbreak framework — Anthropic](https://www.anthropic.com/news/fable-safeguards-jailbreak-framework)
- [Redeploying Fable 5 — Anthropic](https://www.anthropic.com/news/redeploying-fable-5)
