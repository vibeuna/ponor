---
layout: post
title: "Šta je harness i kako radi?"
date: 2026-11-07
category: vodici
image: /assets/images/2026-11-07-sta-je-harness.svg
read_time: 7
description: “Harness je softver koji upravlja LLM-om. Saznajte šta sadrži, kako radi njegova petlja i zašto isti model daje različite rezultate u različitim harnessima.”
tags: [ai-agenti]
---

Claude Code i Codex nisu jezički modeli. To su agenti. Svaki agent sadrži jezički model i softver oko njega. Taj softver čita datoteke i pokreće komande. On pamti urađeni posao i odlučuje kada treba stati. Ovaj softver se zove harness. Ponašanje agenta zavisi od modela, ali i od harnessa.

## Ukratko

Harness (engl.) je softver koji od jezičkog modela pravi [agenta](/rjecnik/agent/). Model samo generiše tekst. Harness radi ostalo. On pokreće [agentsku petlju](/rjecnik/agentska-petlja/) i izvršava [alate](/rjecnik/alat/) koje model zatraži. On također upravlja [kontekstnim prozorom](/rjecnik/kontekstni-prozor/) i dozvolama.

Izraz nije standardizovan. Proizvođači ga definišu različito. Neki koriste riječi "agent" i "harness" kao sinonime. Preprinti ne daju jasan odgovor na pitanje da li harness mijenja rezultate istog modela.

## Šta je harness?

Anthropic opisuje harness u tekstu o svojim Managed Agents. Tamo je harness petlja koja poziva Claude i usmjerava njegove pozive alata ka odgovarajućoj infrastrukturi ("the loop that calls Claude and routes Claude's tool calls to the relevant infrastructure"). Isti tekst kaže da harness nosi pretpostavke o tome šta model ne može uraditi sam. Kako modeli napreduju, te pretpostavke mogu zastarjeti.

Drugi izvori naglašavaju druge dijelove iste stvari:

- **Anthropic, Claude Code:** [Dokumentacija](https://code.claude.com/docs/en/how-claude-code-works) opisuje Claude Code kao sloj oko modela. Taj sloj daje modelu alate i upravlja kontekstom. Dokumentacija ga zove agentski harness.
- **OpenAI, Codex:** OpenAI piše "our agent (or "harness")". Za OpenAI je harness osnovna agentska petlja i logika izvršavanja. Na njoj rade sve Codex aplikacije.
- **Zhang i saradnici:** Ovaj preprint (rad koji još nije prošao recenziju) definiše harness kao infrastrukturni sloj oko modela. Taj sloj gradi kontekst, radi s alatima, koordinira korake i provjerava rezultate.
- **Arjmandi:** Ovaj preprint opisuje harness kroz tri dijela: alate, promptove i tok kontrole. Zajedno oni od chat modela prave autonomnog softverskog inženjera.

Definicije se preklapaju, ali nisu iste. Na primjer, u arhitekturi Managed Agents harness je samo jedan dio sistema. Sandbox i zapis sesije su odvojeni dijelovi.

Izraz ima i drugo značenje: harness za evaluaciju. Anthropic tako zove infrastrukturu koja izvodi evaluacije od početka do kraja. Anthropic jasno razlikuje ovaj harness od agentskog. Ovaj članak govori samo o agentskom harnessu.

## Šta ulazi u harness?

Sastav zavisi od proizvoda. [Dokumentacija Claude Agent SDK-a](https://code.claude.com/docs/en/agent-sdk/agent-loop) navodi ove dijelove:

- **Izvršavanje alata.** Model traži [pozivanje alata](/rjecnik/pozivanje-alata/) (tool calling). Harness alat izvrši i modelu vrati rezultat.
- **Dozvole.** Režimi dozvola i pravila o tome šta je dopušteno, a šta zabranjeno, određuju šta agent smije raditi.
- **Hooks.** Tako SDK naziva kod koji se pokreće prije ili poslije poziva alata, pri zaustavljanju i prije sažimanja.
- **Sažimanje (compaction).** Kada se kontekstni prozor (context window) napuni, harness starije dijelove razgovora zamijeni sažetkom. OpenAI upravljanje kontekstnim prozorom navodi kao jednu od odgovornosti agenta.
- **Podagenti i sesije.** Podagenti preuzimaju dio posla, a sesija se može nastaviti kasnije.
- **Ograničenja.** Najveći dozvoljeni broj turnova (max turns) i budžet.

Claude Code tome dodaje fajlove s uputama (CLAUDE.md i auto-memoriju). Codex u svoj prompt ubacuje AGENTS.md, metapodatke o [vještinama](/rjecnik/vjestina/) (engl. skill) i podatke o okruženju, kao što su radni direktorij i vrsta terminala (shell).

Sandbox je poseban slučaj. Prema OpenAI-ju, Codex u sandboxu izvršava samo svoj alat za pokretanje komandi u terminalu (shell). Alati povezani preko [MCP-a](https://www.ponor.ba/clanci/sta-je-mcp/) nisu u Codexovom sandboxu i sami su odgovorni za svoja zaštitna ograničenja.

## Kako radi petlja?

OpenAI ovako opisuje Codexovu petlju. Harness sastavi prompt i pošalje ga modelu. Model ili odgovori, ili zatraži poziv alata. Ako zatraži alat, harness ga izvrši, doda rezultat u prompt i ponovo se obrati modelu. Ovo se ponavlja sve dok model ne prestane tražiti alate i ne napiše poruku. Time se završava jedan turn. OpenAI tim izrazom označava cijeli put od korisnikove poruke do odgovora, a taj put može obuhvatiti mnogo krugova petlje.

{% include diagram.html name="sta-je-harness" caption="Petlja harnessa: model traži alate, harness ih izvršava, a rezultat se vraća u prompt sve dok model ne napiše odgovor." alt="Dijagram: zadatak ulazi u harness. Harness sastavi prompt, pošalje ga modelu i provjeri da li model traži alat. Ako traži, harness izvrši alat, doda rezultat u prompt i petlja se ponavlja. Ako ne traži, model piše odgovor. Harness upravlja i dozvolama i sandboxom, fajlovima s uputama, sažimanjem i podagentima." %}

Dokumentacija Agent SDK-a petlju opisuje u pet koraka: SDK primi prompt, Claude ga procijeni, SDK izvrši alate, sve se ponavlja, a rezultat se vraća kada odgovor više ne sadrži poziv alata. U SDK-u turn znači jedan krug petlje, dakle manju jedinicu nego kod OpenAI-ja. Petlja se zaustavlja kod konačnog odgovora, kada dostigne ograničenje broja turnova ili budžeta, ili kada nastane greška.

Ovo su dva odvojena opisa dva različita proizvoda, a ne jedna te ista lista. Uslove izlaska iz petlje koje OpenAI navodi u svom vodiču za agente obrađuje članak [Šta je AI agent i kako radi?](https://www.ponor.ba/clanci/sta-je-ai-agent/).

## Mijenja li harness rezultate istog modela?

Dokazi ovdje idu u oba smjera. Svi radovi objavljeni su na arXivu. Zhang i saradnici iznose tezu (position paper), Arjmandijev rad je preprint, a rad Vatsa i Goleva je preliminarni rad za radionicu, koji je još u recenziji. Anthropicov tekst je tvrdnja proizvođača.

**Za.** Zhang i saradnici (maj 2026) tvrde da je kod dugoročnih zadataka, među vodećim modelima sličnih mogućnosti, harness često važniji za učinak od samog modela. To je teza rada, a ne utvrđena činjenica. Osim toga, Anthropic u [tekstu o dugotrajnim aplikacijama](https://www.anthropic.com/engineering/harness-design-long-running-apps) navodi da je Opus 4.5 kao jedan agent radio 20 minuta uz trošak od 9 dolara, a s potpunim harnessom 6 sati uz trošak od 200 dolara. I to je tvrdnja proizvođača. Metrike kvaliteta nema, jer je rezultat ocijenjen kvalitativno.

**Protiv.** Arjmandi (septembar 2026) je na 80 privatnih zadataka uporedio proizvođačev harness s neutralnim. Opus 4.8 je sa svojim harnessom riješio 48,8% zadataka, a s neutralnim 50,0%. GPT-5.5 je sa svojim harnessom riješio 55,6%, a s neutralnim 54,4%. Razlike su oko 1,2 procentna poena, u suprotnim smjerovima, a intervali povjerenja obuhvataju nulu. Zato autor ne nalazi da ijedna strana u prosjeku ima prednost. Intervali su ipak široki (za Opus od −10,0 do +7,5 poena), pa manji učinak nije isključen. Kod Opusa podskupovi idu u suprotnim smjerovima. Na 61 zadatku iz repozitorija proizvođačev harness zaostaje 9,0 poena, a na 19 takmičarskih zadataka vodi za 23,7 poena. Autor je ovu podjelu napravio tek nakon što je vidio podatke i traži replikaciju. Neutralni harness koštao je 1,2 do 1,6 puta više po riješenom zadatku. Međutim, za 58 pokušaja na autorovom Anthropic računu nema zapisa o potrošnji, pa ostaje otvoreno koji je harness jeftiniji po stvarno naplaćenom trošku.

**Mješovito.** [Vats i Golev](https://arxiv.org/abs/2607.22585) (preliminarni rad predan na radionicu ICML-a, još u recenziji) uporedili su modele Qwen 3.6 Plus i MiniMax M2.5 u tri otvorena harnessa na 50 zadataka. Kod istog modela stopa uspjeha razlikovala se za 0 do 8 procentnih poena. Intervali povjerenja obuhvataju nulu, osim kod najveće razlike. Potrošnja tokena po riješenom zadatku razlikovala se i do 40 puta.

Iz ovoga ne slijedi ni da je harness važniji od modela, ni da je nevažan. Slijedi samo da se rezultati mjerenja razlikuju zavisno od zadataka, modela i metodologije. Radovi su objavljeni na arXivu, pa ih treba čitati kao rane nalaze.

## Zašto dugi zadaci traže posebnu pažnju?

U novembru 2025. Anthropic je opisao greške koje agenti prave kada rade kroz više sesija. Pokušavaju sve uraditi odjednom, predaju nedovršene funkcionalnosti, prerano proglašavaju uspjeh i označavaju funkcionalnost gotovom bez testa. Rješenja su ugrađena u harness: JSON lista funkcionalnosti, jedna funkcionalnost po sesiji, fajl s napretkom, git commit na kraju svake sesije i testiranje kroz automatizaciju preglednika.

U martu 2026. Anthropic je objavio [drugi tekst](https://www.anthropic.com/engineering/harness-design-long-running-apps). U njemu opisuje "context anxiety", pojavu da agent u blizini granice kontekstnog prozora počne žuriti da završi posao, te pristranost agenta kada ocjenjuje vlastiti rad. Kao odgovor uvedeni su reset konteksta uz predaju bilješki i poseban agent koji ocjenjuje rad. Prema Anthropicu, Opus 4.5 je ovu anksioznost uglavnom otklonio. To je primjer zastarijevanja pretpostavki o kojem je bilo riječi na početku članka.

## Praktične implikacije

- Kada čitate rezultate nekog agenta za programiranje, pitajte koji je harness korišten. Poređenje dva agenta može biti poređenje dva harnessa, a ne samo dva modela.
- Isti model se može ponašati različito u različitim proizvodima, jer se razlikuju dozvole, sažimanje i fajlovi s uputama.
- Kada procjenjujete prednost nekog harnessa, gledajte i cijenu, a ne samo stopu uspjeha.
- Zaštitna ograničenja zavise od toga gdje se provode. Kod Codexa sandbox ne obuhvata alate povezane preko MCP-a.

## Šta NIJE harness

- **Nije model.** Model generiše tekst, a harness odlučuje šta će se s tim tekstom dalje desiti.
- **Nije harness za evaluaciju.** To je infrastruktura za testiranje, a ne za rad agenta.
- **Nema jednu definiciju.** Anthropic, OpenAI i autori preprinta različito postavljaju njegove granice.
- **Nije dokazano presudan.** Nalazi o njegovom utjecaju dolaze iz preprinta. Jedni govore za, drugi protiv.

## Povezano

- [Šta je AI agent i kako radi?](https://www.ponor.ba/clanci/sta-je-ai-agent/) – agentska petlja i uslovi izlaska iz nje, koje ovaj članak ne ponavlja u cijelosti.
- [CLAUDE.md i AGENTS.md: upute koje agent čita prije posla](https://www.ponor.ba/clanci/claude-md-agent-md/) – detaljno o fajlovima s uputama kao dijelu harnessa.
- [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/) – vještine kao jedna od funkcija harnessa.

## Izvori

- [Demystifying evals for AI agents – Anthropic](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Scaling Managed Agents – Anthropic](https://anthropic.com/engineering/managed-agents)
- [Effective harnesses for long-running agents – Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [How the agent loop works (Agent SDK) – Anthropic](https://code.claude.com/docs/en/agent-sdk/agent-loop)
- [Unrolling the Codex agent loop – OpenAI](https://openai.com/index/unrolling-the-codex-agent-loop)
- [Stop Comparing LLM Agents Without Disclosing the Harness – arXiv 2605.23950](https://arxiv.org/abs/2605.23950)
- [Harness or Model? Isolating the Harness Effect – arXiv 2609.11987](https://arxiv.org/abs/2609.11987)
