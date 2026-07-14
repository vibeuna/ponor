---
layout: post
title: "CLAUDE.md i AGENTS.md: kako AI coding assistanti pamte kontekst projekta"
date: 2026-06-20
category: ai-u-praksi
audience: developers
read_time: 9
description: "Svaka Claude Code sesija počinje ispočetka - osim ako niste postavili CLAUDE.md. Šta je taj fajl, čemu služi AGENTS.md i kako ih podesiti za tim koji koristi više alata."
diagram: /assets/diagrams/2026-06-23-claude-md-agent-md.svg
image: /assets/images/2026-06-23-claude-md-agent-md.svg
---

Pokrenete Claude Code na novom projektu. Alat ne zna ništa o vašoj arhitekturi, konvencijama imenovanja, niti o tome da `npm run build:staging` ne smije biti pokrenut na `main` branchu. Svaka sesija počinje ispočetka. CLAUDE.md postoji da to promijeni, a AGENTS.md proširuje isti princip na sve ostale alate u timu.

## CLAUDE.md - pamćenje sesije u Claude Code

Claude Code čita `CLAUDE.md` automatski na početku svake sesije, prije prvog tokena razgovora. To je jedini mehanizam u alatu koji nosi kontekstni prozor (context window) između sesija - Claude Code sam po sebi nema trajno pamćenje. Sve što agent treba znati o projektu, a ne može pročitati iz koda, ide u taj fajl.

Fajl se učitava prema hijerarhiji triju nivoa:

```
~/.claude/CLAUDE.md          # globalni / lični (primjenjuje se na sve projekte)
./CLAUDE.md                  # root projekta (commituje se u repo)
./.claude/CLAUDE.md          # alternativna lokacija za root
./src/payments/CLAUDE.md     # subdirektorij (učitava se lazy — samo kad agent čita fajlove u tom direktorijumu)
```

Sva tri nivoa se spajaju. Globalni fajl možete koristiti za lične preference koje ne idu u repo (npr. stilovi odgovora, jezičke preference), dok projektni fajl nosi informacije relevantne za cijeli tim.

Za lične overridove koji ne trebaju biti commitovani, postoji `CLAUDE.local.md` - isti mehanizam, ali po konvenciji ide u `.gitignore`. Korisno kada radite na projektu čiji `CLAUDE.md` kontrolira neko drugi.

**Šta ide u CLAUDE.md:**
- Komande za build, test i deployment (naročito one nestandardne)
- Arhitekturalne odluke koje nisu vidljive iz koda
- Konvencije imenovanja i organizacije fajlova
- Putanje koje se ne diraju (generisani kod, vendor direktorijumi)
- Radni tokovi specifični za projekt

## Šta NE ide u CLAUDE.md

Najčešća greška je trpanje pravila kodnog stila u ovaj fajl. To je i skupo i kontraproduktivno.

CLAUDE.md troši prostor u kontekstnom prozoru (context window). Svaki redak koji ste dodali tamo zauzima kapacitet koji bi inače bio dostupan za vaš kod i razgovor. Prema zajedničkoj praksi razvojnih timova koji koriste Claude Code, fajlovi iznad otprilike 200 linija počinju negativno utjecati na kvalitet slijeđenja uputa — model ne ignoriše ostatak, ali mu prioritizacija slabi.

Pravila poput "uvijek koristi single quotes", "indent je 2 razmaka", "ne koristi `var`" - to je posao lintera (lint alata). Prettier, ESLint, Black, rustfmt izvršavaju ta pravila deterministički, bez trošenja kontekstnog prozora. Agent koji čita "koristi single quotes" iz CLAUDE.md i agent koji dobije grešku od ESLinta jer je napisao double quotes - isti ishod, drastično različiti troškovi.

**Praktično pravilo:** ako pravilo može biti pokriveno linterom ili formatterom, tamo i spada.

## AGENTS.md — široko prihvaćena konvencija za višealatne timove

`AGENTS.md` je open standard — nije u vlasništvu Anthropica, nije vezan za Claude Code. To je obična Markdown datoteka bez obaveznog YAML frontmattera, čija jedina posebnost je da ju alati za AI-asistiranu izradu softvera prepoznaju po imenu i čitaju automatski.

Prema dostupnoj dokumentaciji i zajedničkoj praksi, više od 30 alata čita `AGENTS.md`: OpenAI Codex, GitHub Copilot, Cursor, Gemini CLI, Google Jules, Aider, Devin i drugi. Claude Code je ne čita direktno - ali to se rješava s jednom linijom.

**Sadržaj je identičan kao za CLAUDE.md:** build komande, test procedure, konvencije, off-limits putanje. Razlika je u dosegu: `AGENTS.md` na root-u projekta čita svaki alat koji prepoznaje standard, bez ikakve dodatne konfiguracije s vaše strane.

Naučni preprint ([arxiv 2601.20404](https://arxiv.org/pdf/2601.20404)) ispituje utjecaj `AGENTS.md` fajlova na efikasnost AI agenata u kodiranju - što govori o dovoljnoj adopciji da privuče akademsku pažnju.

## Preporučeni uzorak: jedno mjesto, sva pravila

Ako koristite Claude Code zajedno s bilo kojim drugim alatom (Cursor, Copilot, Codex), duplikacija instrukcija brzo postaje problem. Rješenje je `@import` direktiva (dokumentovana u zajedničkim vodičima za Claude Code):

```markdown
# CLAUDE.md

@import AGENTS.md

## Claude-specifično

- Pokreni testove prije svakog commita
- Uvijek napravi checkpoint u blackboard/ kada završiš istraživačku fazu
```

Sa ovim postavljanjem, `AGENTS.md` na root-u projekta postaje jedini autoritativni izvor instrukcija za cijeli tim. `CLAUDE.md` ga importuje i dodaje samo ono što je specifično za Claude Code. Nijedna instrukcija nije napisana na dva mjesta.

Preporučena struktura direktorijuma:

```
my-project/
├── AGENTS.md              # canonical context file — čitaju svi alati
├── CLAUDE.md              # @import AGENTS.md + Claude-specific dodaci
├── CLAUDE.local.md        # osobni overridovi (u .gitignore)
└── .claude/
    └── agents/
        ├── review.md      # definicija sub-agenta za code review
        └── research.md    # definicija sub-agenta za istraživanje
```

{% include diagram.html name="2026-06-23-claude-md-agent-md" caption="Tri fajla, tri različite namjene: kanonski kontekst, Claude-specifična proširenja, i definicije sub-agenata." alt="Dijagram koji prikazuje odnos između AGENTS.md, CLAUDE.md i .claude/agents/ fajlova" %}

## .claude/agents/ — definicija custom sub-agenata

Fajlovi u `.claude/agents/` su poseban mehanizam, odvojen od CLAUDE.md i AGENTS.md. Svaki fajl definira jednog custom sub-agenta s YAML frontmatterom i Markdown tijelom:

```markdown
---
name: review
description: Code review fokusiran na sigurnost i performanse
tools: [Read, Bash]
model: claude-opus-4-5
---

Ti si senior inženjer koji pregledava kod. Fokusiraj se na...
```

Ove definicije kontrolišu autonomnu delegaciju — koji alati su dostupni sub-agentu, koji model koristi, koja podešavanja (settings) i dozvole (permissions) važe. Prompt koji piše developer u tijelu fajla postaje system prompt sub-agenta.

Napomena o scope-u: globalni sub-agenti idu u `~/.claude/agents/` i dostupni su u svim projektima; projektni sub-agenti idu u `.claude/agents/` i važe samo za taj projekt.

## Bitna zamka za Agent SDK

Ovo je najčešći izvor zabune za developere koji grade programske agente: **CLAUDE.md fajlovi se po defaultu NE učitavaju u Agent SDK-u**.

Kada koristite Claude Code programski (TypeScript ili Python SDK), morate eksplicitno omogućiti učitavanje projektnih fajlova kroz parametar `settingSources` (TypeScript) ili `setting_sources` (Python) sa vrijednošću `['project']`. Bez ovog parametra, agent radi bez ikakvog konteksta iz CLAUDE.md - bez build komandi, bez konvencija, bez ograničenja koja ste definisali. Greška je tiha: agent ne javlja da nešto nedostaje, jednostavno ne zna. Tačna sintaksa ovisi o verziji SDK-a; provjerite [zvaničnu dokumentaciju](https://docs.anthropic.com/en/docs/claude-code/settings).

Prema dokumentaciji Claude Code, ugrađeni sub-agenti `Explore` i `Plan` namjerno preskaču CLAUDE.md fajlove - dizajnerska odluka radi brzine i manjeg trošenja kontekstnog prozora za istraživačke zadatke. Svi ostali ugrađeni i custom sub-agenti fajl učitavaju normalno.

## Sažetak

Tri mehanizma, tri različite namjene:

| Fajl | Ko ga čita | Namjena |
|------|------------|---------|
| `AGENTS.md` | 30+ alata (svi) | Kanonski kontekst projekta |
| `CLAUDE.md` | Samo Claude Code | @import + Claude-specifična proširenja |
| `.claude/agents/<ime>.md` | Samo Claude Code | Definicija custom sub-agenata |

Preporučeni radni tok: `AGENTS.md` na root-u kao jedini izvor istine, `@import` u `CLAUDE.md`, custom sub-agenti u `.claude/agents/`. Bez duplikacije, bez kontradikcija između alata.

## Izvori

- [Anthropic: Claude Code Memory (CLAUDE.md dokumentacija)](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Anthropic: Claude Code Sub-agents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- [Anthropic: Claude Code Settings i loading order](https://docs.anthropic.com/en/docs/claude-code/settings)
- [BuildThisNow: AGENTS.md vs CLAUDE.md — strukturalna usporedba](https://www.buildthisnow.com/blog/guide/mechanics/agents-md-vs-claude-md)
- [MorphLLM: AGENTS.md specifikacija i pregled](https://www.morphllm.com/agents-md-guide)
- [HumanLayer: Praktični vodič za pisanje dobrog CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)
- [arxiv 2601.20404: Peer-reviewed studija o utjecaju AGENTS.md na efikasnost agenata](https://arxiv.org/pdf/2601.20404)
