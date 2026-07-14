---
layout: post
title: "Agentni loop: kako LLM zaista izvršava višekorake zadatke"
date: 2026-07-02
category: vodici
audience: developers
read_time: 9
description: "Agentni loop je kontrolni obrazac koji LLM-u daje sposobnost iterativnog izvršavanja višefaznih zadataka - pozivanjem alata, primanjem rezultata, i ponovnim razmišljanjem - sve do uvjeta za zaustavljanje."
image: /assets/images/2026-06-30-agentni-loop.svg
---

LLM sam po sebi je stateless transformer teksta: prima tokene, vraća tokene. Bez pamćenja prethodnih koraka, bez pristupa vanjskim sistemima. Agentni loop (petlja) mijenja tu jednačinu - strukturiranjem izvršavanja kao višekornog razgovora u kojem model može tražiti akcije, primati rezultate, i iterirati. Ovo nije marketinški termin. To je konkretan kontrolni obrazac s jasnom mehanikom, definisanim uvjetima zaustavljanja, i skupom poznatih načina na koje može otkazati.

---

## Šta je agentni loop

Osnovna ideja je jednostavna. LLM-u se daje pristup skupa alata (tools) - funkcija koje harness može izvršiti u ime modela. Model prima akumuliranu historiju razgovora (sve prethodne korake i njihove rezultate), rasuđuje nad njom, i donosi jednu od dvije odluke: pozvati alat ili dati finalni odgovor.

Kada model odluči pozvati alat, harness (neparametarski scaffolding) koji okružuje model preuzima kontrolu: detektira signal, izvršava operaciju, dodaje rezultat u listu poruka, i ponovo poziva model. Ovaj ciklus se ponavlja dok se ne dostigne uvjet zaustavljanja.

Ključna podjela odgovornosti: model odlučuje *šta* treba uraditi; harness to *radi*. Model nikada direktno ne izvršava ništa - samo emituje zahtjev. Ova separacija nije samo arhitekturna elegancija - ona je i sigurnosna granica.

Sa svakim ciklusom context window se povećava. Svaki poziv alatu i svaki rezultat dodaju tokene u historiju. Duži zadaci neizbježno pritiskaju granicu prozora, što je jedno od fundamentalnih ograničenja agentnih sistema.

{% include diagram.html name="agentni-loop" caption="Agentni loop: LLM emituje tool_use signal, harness izvršava alat, tool_result se vraća u historiju - ciklus se ponavlja dok nema end_turn." alt="Dijagram agentnog loopa: zadatak ulazi u LLM, koji šalje tool_use harnessu, harness izvršava alate i vraća tool_result, sve dok model ne emituje finalni odgovor." %}

---

## Mehanika poziva alatu

Na nivou API-a, mehanika je standardizirana između glavnih providera. Uzmimo Anthropic API kao reprezentativan primjer.

Harness šalje `messages` niz zajedno s `tools` nizom koji sadrži JSON-schema definicije dostupnih alata. Kada model odluči pozvati alat, API odgovor vraća `stop_reason: "tool_use"` i jedan ili više `tool_use` blokova sadržaja - svaki s identifikatorom, imenom alata, i JSON ulaznim parametrima.

Harness zatim:
1. Izvlači `tool_use` blokove
2. Izvršava svaki alat (paralelno, ako ih ima više)
3. Sastavlja `tool_result` blokove vezane za originalne identifikatore
4. Dodaje ih u razgovor kao poruku s `user` ulogom
5. Ponovo poziva model

OpenAI API je strukturno identičan: `finish_reason: "tool_calls"` signalizira poziv alatu; `tool_choice` parametar kontrolira mod.

Jedan detalj koji se često propušta: Anthropic server-side alati (npr. web_search koji se izvršava unutar Anthropic infrastrukture) imaju vlastiti unutarnji izvršni loop. Ako taj unutarnji loop dostigne vlastiti limit, API vraća `stop_reason: "pause_turn"` umjesto finalnog odgovora - harness mora ponovo podnijeti zahtjev da bi nastavio. Harness koji to ne obrađuje tiho će izgubiti progres.

Paralelni pozivi alatu su uobičajeni u produkciji. Model može u jednom koraku emitovati više `tool_use` blokova - harness ih izvršava konkurentno, što reducira latenciju.

---

## Imenovani obrasci

Istraživačka zajednica je dokumentovala nekoliko specifičnih varijanti agentnog loopa.

**ReAct** (Yao et al., 2022, [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)) je prvo sistematsko pokazivanje da kombinovanje razmišljanja u prirodnom jeziku s upotrebom alata nadmašuje svaki pristup posebno. Obrazac je trostepeni: *Thought* (verbalno razmišljanje), *Action* (poziv alatu), *Observation* (rezultat). Autori izvještavaju +34% apsolutno nad RL-baselines na ALFWorld i +10% na WebShop benchmarku, prema vlastitoj evaluaciji u radu.

**MRKL** (Karpas et al., 2022) postavlja LLM kao router koji preusmjerava pod-upite specijaliziranim modulima - kalkulatorima, bazama podataka, retrieval engineima.

**Plan-and-Execute** odvaja planiranje od izvršavanja: planer generiše dekompoziciju zadatka; executor je prolazi korak po korak. Slabost je krhkost plana - ako rani koraci ne uspiju, executor često nema mehanizam za replaniranje.

**Reflexion** (Shinn et al., 2023) dodaje post-failure korak refleksije: model generiše verbalnu kritiku vlastite greške, pamti je, i koristi pri ponovnom pokušaju.

**Tree of Thoughts** (Yao et al., 2023) proširuje svaki korak na eksploraciju više grana razmišljanja koristeći BFS ili DFS s evaluatorom trajektorija. Skuplje po tokenima, prikladnije za zadatke koji zahtijevaju planiranje unaprijed.

---

## Uvjeti zaustavljanja

Svaki agentni loop mora imati definirane uvjete koji ga terminiraju. Nedostatak ovdje je najčešći uzrok zaglavljivanja u produkciji.

**Prirodna terminacija** - model emituje `stop_reason: "end_turn"` (Anthropic) ili `finish_reason: "stop"` (OpenAI).

**Tvrdi iterativni cap** - harness-enforced maksimum. LangGraph `recursion_limit` defaultuje na 25; OpenAI Agents SDK koristi `max_turns`.

**Token / troškovni budžet** - loop izlazi kada kumulativna potrošnja tokena pređe prag. Agentni zadaci troše otprilike 4× više tokena od jednokratnih poziva prema internom OpenAI guidance za Agents SDK - heuristika, ne izmjerena vrijednost; može se razlikovati za druge harness implementacije.

**Human-in-the-loop kapija** - izvršavanje pauzira čekajući ljudsku potvrdu. LangGraph koristi `interrupt`; Anthropic vraća `pause_turn`. Kritično za visoko-rizične operacije.

Korisna tehnika: **"finish action" pattern** - model dobiva eksplicitni `finish` alat kojim signalizira dovršetak. Čini terminaciju eksplicitnom i reducira lažne rane izlaske.

---

## Načini otkazivanja

**Beskonačni / tijesni loopovi** - model poziva isti alat s istim argumentima iznova. Mitigacija: detekcija bez progresa (hash provjera naziva alata i argumenata); iterativni cap.

**Halucinacije (hallucination) u pozivima alatu** - model poziva alat koji nije definiran, ili prosljeđuje argumente koji ne odgovaraju schema definiciji. Mitigacija: striktna schema validacija na harness nivou.

**Tihe greške alata** - alat vraća prazan string na grešku; model to tretira kao uspjeh. Mitigacija: strukturirani error objekti.

**Overflow kontekstnog prozora** - svaka iteracija dodaje tokene; dugi zadaci pune prozor. Mitigacija: periodična sumarizacija, sliding window pristup.

**Retry storms** - više agenata koji svaki nezavisno ponavljaju neuspjeli poziv alatu saturiraju downstream servis. Mitigacija: exponential backoff s jitterom; circuit breaker pattern.

**Krhkost plana** - Plan-and-Execute pristup puca kada rani koraci ne uspiju. Mitigacija: Reflexion-style logovanje grešaka; triggeri za replaniranje.

**Provider `finish_reason` nepodudarnost** - određeni OpenAI-kompatibilni provideri vraćaju `stop` u `finish_reason` čak i kada su `tool_calls` prisutni. Harnesovi koji na osnovu `finish_reason` odlučuju o terminaciji tada prijevremeno izlaze iz loopa. Zabilježeno u februaru 2026.; status u trenutnim verzijama nije verificiran.

---

## Multi-agent proširenja

Jednoagentni loop ima strukturna ograničenja: kontekstni prozor koji se puni, nemogućnost paralelizacije, nedostatak specijalizacije.

**Orchestrator–sub-agent obrazac**: orchestrator (koordinatorski agent) prima zadatak, dekomponuje ga, i delegira pod-zadatke specijaliziranim sub-agentima, od kojih svaki pokreće vlastiti unutarnji loop. Sub-agenti su stateless s perspektive orchestratora. Handoff se odvija putem poziva alatu ili direktnog prosljeđivanja poruka.

**Peer / swarm** arhitektura: agenti komuniciraju putem zajedničke message bus ili dijeljenog pamćenja, bez centralnog koordinatora. Emergentna koordinacija, ali teža za debugging.

Praktično pravilo za prijelaz: jednoagentni sistem je jednostavniji i jeftiniji. Multi-agent je opravdan kada je (a) overflow kontekstnog prozora realan problem, (b) izolacija zadataka neophodna, ili (c) paralelizacija smisleno smanjuje wall-clock vrijeme. Trošak tokena raste super-linearno u multi-agent sistemima.

MCP (Model Context Protocol - protokol za kontekst modela) pruža unificiran mehanizam za deklarisanje alata koji može koristiti bilo koji kompatibilni harness. Još je u fazi aktivnog razvoja s breaking changes.

---

## Šta ovo znači u praksi

**Uvjeti zaustavljanja su obavezni.** Svaki harness mora imati tvrdi iterativni cap. Loop bez capa je produkcijska greška.

**Strukturirajte greške alata eksplicitno.** Prazan string kao error odgovor je gotovo uvijek greška dizajna. Error objekt s jasnim statusom i porukom je minimum.

**Pratite trošak tokena po pozivu.** Agentni zadaci imaju karakteristično drugačiji troškovni profil od batch API poziva.

**Debugging zahtijeva vidljivost u svaki korak loopa.** Logujte svaki `tool_use` zahtjev i svaki `tool_result` odgovor s timestampom i identifikatorom sesije.

**Validacija scheme nije opcija.** Schema validacija `tool_use` argumenata na harness nivou blokira cijelu kategoriju halucinacija u pozivima alatu.

---

## Zaključak

Agentni loop nije apstraktni koncept - to je konkretan kontrolni obrazac s dobro razumljenim načinima otkazivanja. ReAct, Reflexion, Plan-and-Execute nisu marketinški nazivi nego istraživački dokumentovani obrasci s jasnim trade-off profilima. Razlika između agentnog sistema koji funkcioniše u produkciji i onog koji ne funkcioniše rijetko je u izboru modela - obično je u harness dizajnu: stopping conditions, error handling, i vidljivost u svaki korak.

Tooling (LangGraph, OpenAI Agents SDK, Anthropic agent primitives) razvija se brzo s breaking changes - pratite verzioniranje. Temeljna struktura observe–reason–act loopa, međutim, stabilna je i neće se promijeniti.

---

## Izvori

- [Yao et al. (2022) - ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)
- [Lilian Weng - "LLM Powered Autonomous Agents" (2023)](https://lilianweng.github.io/posts/2023-06-23-agent/)
- [Anthropic - How tool use works (developer docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)
- [OpenAI Agents SDK - Running agents (developer docs)](https://developers.openai.com/api/docs/guides/agents/running-agents)
- [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
