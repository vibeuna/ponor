---
layout: post
title: "Šta je AI agent i kako radi?"
date: 2026-10-11
category: vodici
image: /assets/images/2026-10-11-sta-je-ai-agent.svg
read_time: 6
description: "Po čemu se AI agent razlikuje od chatbota, kako u petlji koristi alate i zašto samostalnost ima cijenu: agent radi sporije, skuplji je, a greške mu se mogu gomilati."
tags: [ai-agenti]
---

Chatbot koji odgovara na poruke, skripta koja u tri unaprijed zadana koraka poziva [veliki jezički model (large language model, LLM)](/rjecnik/veliki-jezicki-model/) i sistem koji sam odlučuje šta će sljedeće uraditi: u svijetu umjetne inteligencije (artificial intelligence, AI) sve se to danas naziva "AI agentom". Prema vodičima kompanija Anthropic i OpenAI, [agent](/rjecnik/agent/) je samo ovaj posljednji. Razlika nije samo teorijska. Od nje zavisi koliko sistem košta, koliko često griješi i gdje mu je potreban čovjek.

## Ukratko

AI agent je sistem u kojem veliki jezički model sam bira sljedeći korak. Model poziva alate (pretraživanje, izvršavanje koda, baze podataka), čita šta su vratili i to ponavlja u petlji, sve dok ne obavi zadatak ili dok ga ne zaustavi uslov za završetak, npr. najveći dozvoljeni broj koraka. Time se razlikuje od chatbota, koji samo odgovara, i od toka rada (workflow), u kojem redoslijed koraka unaprijed određuje programer. Nezavisna mjerenja iz 2024. pokazala su da su agenti tada često griješili: na benchmarku (referentnom testu) τ-bench čak su i agenti zasnovani na tada najjačim modelima rješavali manje od polovine zadataka.

## Agent, tok rada ili chatbot?

Anthropic je u decembru 2024. objavio vodič ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents) u kojem razlikuje dvije vrste sistema. U toku rada model i alati idu putanjama koje je programer unaprijed definisao u kodu. Kod agenta model sam vodi proces i sam bira alate. Obje vrste Anthropic naziva "agentskim sistemima", ali agentom smatra samo drugu.

OpenAI u [vodiču iz 2025.](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) agente opisuje kao sisteme koji "samostalno obavljaju zadatke u vaše ime". Presudno je pitanje da li jezički model upravlja redoslijedom koraka. Po toj definiciji obični chatbotovi i modeli koji na jedan upit daju jedan odgovor nisu agenti.

Ove definicije se ne poklapaju u potpunosti, a nijedna nije zvanična. Ipak, iz obje proizlazi isto praktično pravilo:

- **Chatbot** odgovara na poruke. Ne izvršava radnje i ne odlučuje šta dalje.
- **Tok rada** poziva model, ali redoslijed koraka unaprijed je odredio programer.
- **Agent** sam odlučuje šta će sljedeće uraditi, na osnovu onoga što je dobio u prethodnom koraku.

[Sistemi s više agenata](/rjecnik/sistem-s-vise-agenata/), u kojima nekoliko agenata dijeli posao, tema su za zaseban tekst.

## Kako funkcioniše

OpenAI agenta dijeli na tri dijela: model, [alate](/rjecnik/alat/) i upute koje sadrže jasna pravila i zaštitna ograničenja. Alati su vanjske funkcije ili servisi kojima se pristupa preko API-ja (programskog interfejsa). Anthropic cijeli mehanizam sažima u jednu rečenicu: agenti su "obično samo jezički modeli koji u petlji koriste alate na osnovu povratnih informacija iz okruženja".

Pojednostavljeno, ta [agentska petlja](/rjecnik/agentska-petlja/) izgleda ovako:

1. Na osnovu zadatka, uputa i dosadašnjih rezultata model odlučuje da li mu treba alat ili je zadatak završen.
2. Ako mu treba alat, slijedi [pozivanje alata (tool calling)](/rjecnik/pozivanje-alata/): model piše strukturiran zahtjev s nazivom alata i argumentima.
3. Aplikacija izvršava taj zahtjev.
4. Rezultat se vraća modelu i krug počinje iznova.

{% include diagram.html name="sta-je-ai-agent" caption="Agentska petlja: model bira sljedeći korak, alat vraća rezultat, a petlja se zaustavlja kad se ispuni uslov za završetak." alt="Dijagram: model dobija zadatak i upute i odlučuje da li mu treba alat. Pozivanje alata, uz opcionalno odobrenje čovjeka za rizične radnje, pokreće alat, a rezultat se vraća modelu. Petlja se ponavlja dok se ne ispuni uslov za završetak, npr. konačan odgovor, greška ili najveći dozvoljeni broj koraka. Donji red: chatbot samo odgovara, u toku rada korake određuje programer, a kod agenta model bira sljedeći korak." %}

Anthropic naglašava da se agent u svakom koraku mora oslanjati na stvarne podatke iz okruženja, npr. na rezultat izvršenog koda, a ne samo na vlastitu procjenu.

Ideja nije nova. Rad [ReAct](https://arxiv.org/abs/2210.03629) (Yao i saradnici, 2022) opisuje model koji naizmjenično ispisuje korake zaključivanja (reasoning) i izvodi radnje, npr. pretražuje Wikipediju preko API-ja. U testnim okruženjima ALFWorld i WebShop takav pristup povećao je uspješnost za 34, odnosno 10 procentnih poena u odnosu na metode s kojima su ga autori poredili.

Petlja se mora negdje i završiti. OpenAI navodi pet takvih uslova: model pozove alat za konačni odgovor, vrati odgovor u unaprijed zadanom formatu, naiđe na grešku, dostigne najveći dozvoljeni broj koraka ili odgovori bez ijednog poziva alata. Anthropic kao primjer također navodi najveći dozvoljeni broj ponavljanja.

Petlja može imati i tačke na kojima agent čeka čovjeka. To se naziva ljudskim nadzorom (human-in-the-loop). Prema Anthropicu, agent može zastati i zatražiti povratnu informaciju od čovjeka. OpenAI preporučuje da čovjek preuzme kontrolu kad agent prekorači dozvoljeni broj neuspjelih pokušaja, kao i prije visokorizičnih radnji poput otkazivanja narudžbi, odobravanja velikih povrata novca ili plaćanja.

## Koliko su agenti pouzdani?

[τ-bench](https://arxiv.org/abs/2406.12045) iz 2024. testira agente koji pozivaju alate. Prema autorima, čak i agenti zasnovani na tada najjačim modelima, poput gpt-4o, rješavaju manje od 50% zadataka. Autori su mjerili i dosljednost: kad se isti zadatak iz maloprodajnog dijela testa pokrene osam puta, agent ga riješi u svih osam pokušaja u manje od 25% slučajeva. Za sistem koji se koristi svakodnevno dosljednost je važnija od pojedinačnog uspjeha.

Sva mjerenja u ovom dijelu potiču iz 2024. i s početka 2025. i odnose se na tadašnje najnovije modele. Noviji modeli na istim testovima mogu imati drugačije rezultate.

Istraživači organizacije METR [mjerili su 2025.](https://arxiv.org/abs/2503.14499) koliko duge programerske zadatke modeli mogu završiti. Claude 3.7 Sonnet uspijevao je u polovini zadataka za koje je ljudima trebalo oko 50 minuta. Od 2019. dužina takvih zadataka udvostručuje se otprilike svakih sedam mjeseci, a autori navode da se taj rast 2024. možda i ubrzao. Riječ je o trendu izračunatom iz dosadašnjih podataka, a ne o prognozi. Autori i sami upozoravaju da se rezultati s njihovog skupa zadataka ne moraju preslikati na stvaran posao.

Proizvođači objavljuju i vlastite brojke, koje treba čitati s tom rezervom. Anthropic je u [oktobru 2024.](https://www.anthropic.com/news/3-5-models-and-computer-use) u javnu probnu verziju pustio upravljanje računarom (computer use), funkciju kojom Claude upravlja računarom na osnovu snimaka ekrana. Prema Anthropicu, model je na benchmarku OSWorld riješio 14,9% zadataka koristeći samo snimke ekrana (22,0% s više dozvoljenih koraka), a prvi sljedeći sistem 7,8%. Anthropic je i sam funkciju opisao kao eksperimentalnu, "ponekad nezgrapnu i sklonu greškama".

Procenti s različitih benchmarka nisu međusobno uporedivi jer svaki mjeri drugu vrstu zadataka.

## Praktične implikacije

- **Krenite od najjednostavnijeg rješenja.** Prema Anthropicu, agenti bolji rezultat plaćaju sporijim radom i višom cijenom. Što je samostalnost veća, veći su i troškovi, a greške se mogu gomilati iz koraka u korak. OpenAI dodaje da za zadatke bez složenih procjena, nepreglednih pravila ili nestrukturiranih podataka može biti dovoljan i običan program s fiksnim pravilima.
- **Tri pitanja za svaki proizvod koji nosi oznaku "agent".** Ko određuje sljedeći korak, model ili programer? Šta zaustavlja petlju? Gdje čovjek odobrava radnje?
- **O visokorizičnim radnjama odlučuje čovjek.** OpenAI preporučuje da čovjek preuzme kontrolu prije plaćanja, velikih povrata novca i otkazivanja narudžbi.

## Šta NIJE

- **Agent nije nova, pametnija vrsta modela.** Pokreće ga jezički model iste vrste kao i chatbot. Razliku čine alati, petlja i sloboda da sam bira sljedeći korak.
- **Nije agent sve što se tako zove.** Oznaka se koristi vrlo široko, pa i za sisteme koji po definicijama Anthropica i OpenAI-ja nisu agenti.
- **Slikovito poređenje nije dokaz.** OpenAI u vodiču agenta za otkrivanje prevara poredi s iskusnim istražiteljem, ali to je analogija, a ne mjerenje.

## Povezano

- [Šta je LLM i kako radi?](https://www.ponor.ba/clanci/sta-je-llm/) – o modelu koji pokreće svakog agenta: tokenima, predviđanju sljedećeg tokena i kontekstnom prozoru.

## Izvori

- [Anthropic: Building effective agents (19. 12. 2024)](https://www.anthropic.com/engineering/building-effective-agents)
- [OpenAI: A practical guide to building agents (2025)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Yao i sar.: ReAct (arXiv, 2022)](https://arxiv.org/abs/2210.03629)
- [Yao, Shinn, Razavi, Narasimhan: τ-bench (arXiv, 2024)](https://arxiv.org/abs/2406.12045)
- [Kwa i sar. (METR): Measuring AI Ability to Complete Long Software Tasks (arXiv, 2025)](https://arxiv.org/abs/2503.14499)
- [Anthropic: najava modela Claude 3.5 i upravljanja računarom (22. 10. 2024)](https://www.anthropic.com/news/3-5-models-and-computer-use)
