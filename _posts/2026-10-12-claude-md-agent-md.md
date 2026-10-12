---
layout: post
title: "CLAUDE.md i AGENTS.md: upute koje agent čita prije posla"
date: 2026-10-12
category: ai-u-praksi
image: /assets/images/2026-10-12-claude-md-agent-md.svg
read_time: 8
description: "Šta su CLAUDE.md i AGENTS.md, kako ih čitaju Claude Code, Codex i drugi alati, na koju zamku nailaze timovi koji koriste više alata i šta o tome kažu istraživanja iz 2026."
tags: [ai-agenti]
---

[Agent](/rjecnik/agent/) za programiranje (coding agent) iz jedne sesije u drugu pamti samo ono što je zapisano u fajlovima. Ono što nije zapisano, nova sesija ne zna: kojom se naredbom pokreću testovi, koje fajlove agent ne smije mijenjati, pa ni to da tim komentare u kodu piše na bosanskom. Sve to agentu možete reći jednom, u običnom tekstualnom fajlu koji pročita prije nego što počne raditi. Claude Code taj fajl zove CLAUDE.md, a mnogi drugi alati AGENTS.md.

## Ukratko

CLAUDE.md i AGENTS.md su fajlovi s uputama za agente za programiranje. To je običan Markdown tekst s pravilima projekta, koji agent učita na početku sesije. CLAUDE.md čita Claude Code. AGENTS.md je zajednički format koji, prema stranici agents.md, čitaju Codex, Cursor i drugi alati. Claude Code od verzije 2.1.277 čita i AGENTS.md. Anthropic preporučuje da fajl ima manje od 200 redova. Istraživanja iz 2026., od kojih većina još nije prošla recenziju, daju neujednačenu sliku. Nijedno nije pokazalo da agent uz običan fajl projekta piše statistički značajno bolji kod, a nalazi o brzini i trošku se razilaze.

## Šta je fajl s uputama (instruction file)

Fajl s uputama (instruction file) je tekst koji agent automatski ubacuje u svoj [kontekstni prozor (context window)](/rjecnik/kontekstni-prozor/), odnosno u dio teksta koji model vidi dok radi. Obično se nalazi u repozitoriju, tj. u folderu projekta čiju historiju promjena prati Git. U njega se upisuje ono što agent ne može sam zaključiti iz koda: kako se projekat pokreće i testira, kojih se pravila tim drži i šta se ne smije dirati.

Ustalila su se dva naziva:

- **CLAUDE.md** je fajl s uputama za Claude Code, Anthropicovog agenta za programiranje.
- **AGENTS.md** je format koji nije vezan za jedan alat. Prema stranici [agents.md](https://agents.md), nastao je u saradnji OpenAI Codexa, Ampa, Julesa, Cursora i Factoryja, a danas o njemu brine Agentic AI Foundation, pod okriljem Linux Foundationa. To je čist Markdown, bez obaveznih polja. Ista stranica navodi da ga koristi više od 60.000 projekata s javno dostupnim kodom i prikazuje logotipe 23 alata koji ga podržavaju.

## Kako Claude Code učitava CLAUDE.md

Prema [Anthropicovoj dokumentaciji](https://code.claude.com/docs/en/memory), CLAUDE.md može postojati na četiri nivoa, od najšireg prema najužem:

1. fajl koji organizacija postavlja za sve korisnike na računaru,
2. lični fajl korisnika, koji važi za sve projekte,
3. fajl projekta, u korijenu repozitorija ili u folderu `.claude/`,
4. `CLAUDE.local.md`, u istom folderu kao CLAUDE.md projekta.

Claude Code ne bira jedan od njih, nego ih spaja redom, pa bliži fajlovi dolaze poslije daljih. Na svakom nivou CLAUDE.local.md dolazi poslije CLAUDE.md. [Dokumentacija za Agent SDK](https://code.claude.com/docs/en/agent-sdk/claude-code-features) kaže da među nivoima nema strogog pravila prednosti: ako su upute u sukobu, ishod zavisi od toga kako ih Claude protumači. Stranica o CLAUDE.md dodaje da Claude u tom slučaju "može proizvoljno izabrati jednu" ("may pick one arbitrarily").

Ne učitava se sve odjednom. Fajlovi u trenutnom folderu i u folderima iznad njega učitavaju se pri pokretanju. Fajl iz nekog podfoldera učitava se tek kad agent počne raditi s fajlovima u tom podfolderu.

CLAUDE.md može jednim redom uvesti (import) drugi fajl:

```
@docs/upute-za-testove.md
```

Putanja je relativna u odnosu na fajl koji uvozi, a lanac uvoza može ići najviše četiri koraka u dubinu. Uvoz pomaže preglednosti, ali ne štedi prostor: i uvezeni fajl se učitava pri pokretanju i zauzima jednako mjesta u kontekstnom prozoru.

Kad je riječ o dužini, Anthropic daje konkretnu preporuku: manje od 200 redova po fajlu, jer duži fajlovi "troše više konteksta i smanjuju praćenje uputa" ("consume more context and reduce adherence"). Anthropic savjetuje da se upute koje važe samo za dio projekta presele u zasebna pravila u folderu `.claude/rules/` i vežu za određene putanje.

CLAUDE.md nije jedino što Claude Code prenosi iz sesije u sesiju. Postoji i automatsko pamćenje (auto memory), koje je lokalno uključeno po zadanoj postavci. U njemu agent sam bilježi zapažanja u fajl MEMORY.md, a pri pokretanju učitava prvih 200 redova ili 25 KB tog fajla.

## Kako Claude Code čita AGENTS.md

Od verzije 2.1.277 Claude Code čita AGENTS.md bez ikakvog podešavanja, ali pod jednim uslovom. Po zadanoj postavci (vrijednost `claude-md-or-agents-md`) AGENTS.md se čita samo ako u trenutnom folderu ili iznad njega ne postoji ni CLAUDE.md, ni `.claude/CLAUDE.md`, ni CLAUDE.local.md. Lični CLAUDE.md korisnika i fajl organizacije pri tome se ne računaju. Uz vrijednost `claude-md-and-agents-md` Claude Code čita oba fajla, i to u svakom folderu prvo CLAUDE.md.

Dokumentacija navodi još dva rješenja. Prvo, CLAUDE.md može uvesti AGENTS.md:

```
@AGENTS.md
```

Drugo, na Linuxu i macOS-u CLAUDE.md može biti simbolička veza (symlink) na AGENTS.md:

```
ln -s AGENTS.md CLAUDE.md
```

Ovdje vreba zamka: ako neko u projekat koji ima samo AGENTS.md doda CLAUDE.local.md, Claude Code po zadanoj postavci prestaje čitati AGENTS.md.

{% include diagram.html name="claude-md-agent-md" caption="Šta Claude Code čita po zadanoj postavci, u četiri različite situacije." alt="Četiri reda: ako postoji samo AGENTS.md, čita se AGENTS.md; ako postoje CLAUDE.md i AGENTS.md, čita se samo CLAUDE.md; ako CLAUDE.md uvozi AGENTS.md, čitaju se oba; dodani CLAUDE.local.md isključuje AGENTS.md." %}

## Kako ga čitaju drugi alati

Prema [agents.md](https://agents.md), prednost ima fajl koji je najbliži fajlu na kojem agent radi, a izričita uputa korisnika u razgovoru nadjačava sve ostalo. Pojedinosti se razlikuju od alata do alata:

| Alat | Fajl koji čita | Fajlovi iz više foldera | Ograničenja i napomene |
|---|---|---|---|
| Claude Code | CLAUDE.md; AGENTS.md po zadanoj postavci samo ako nema CLAUDE.md | spaja sve nivoe, bliži fajl dolazi kasnije | ne čita AGENTS.override.md ni AGENTS.local.md |
| [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | AGENTS.md; u svom folderu ga zamjenjuje AGENTS.override.md | spaja fajlove od korijena projekta do trenutnog foldera, najviše jedan po folderu | po zadanoj postavci najviše 32 KiB ukupno; granica se mijenja postavkom `project_doc_max_bytes` |
| [Cursor](https://cursor.com/docs/context/rules) | AGENTS.md | spaja fajl iz podfoldera s fajlovima iz foldera iznad | – |
| [Gemini CLI](https://geminicli.com/docs/cli/gemini-md) | GEMINI.md | – | naveden na stranici agents.md, ali AGENTS.md čita tek kad se podesi `context.fileName` |
| [GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | AGENTS.md | prednost ima najbliži fajl | GitHub ne navodi koji dijelovi Copilota ga čitaju |

## Šta pokazuje istraživanje

Ovaj pregled zasniva se na pretrazi arXiva i možda nije potpun. Do oktobra 2026. objavljeno je najmanje pet radova koji mjere kako fajl s uputama utiče na rad agenta. Samo je jedan prihvaćen na naučnom skupu, i to kao kratak rad na radionici. Ostala četiri objavljena su na arXivu kao preprinti (radovi koji još nisu prošli recenziju).

**Lulla i saradnici** u radu od pet stranica za radionicu JAWs, održanu uz konferenciju ICSE 2026, zadali su Codexu 124 male izmjene koje su ranije već bile prihvaćene, svaku jednom s AGENTS.md i jednom bez njega. Uz fajl je medijan vremena pao sa 98,57 na 70,34 sekunde, a medijan broja [tokena](/rjecnik/token/) (osnovnih jedinica teksta koje model obrađuje) koje agent generiše smanjio se za 16,58%. Ukupan broj tokena, ulaznih i izlaznih, gotovo se nije promijenio (+1,29%). Autori nisu mjerili da li je kod bio ispravan. Rad, dakle, ne pokazuje da agent uz fajl radi bolje, nego samo da brže završi posao.

**Gloaguen i saradnici** (ETH Zurich i LogicStar.ai) imaju najveći uzorak: tri agenta, četiri modela, benchmark (referentni test) SWE-bench Lite i još 138 zadataka iz 12 projekata u kojima su programeri sami napisali fajl s uputama. Autori razlikuju dvije vrste fajlova. Fajlovi koje je model generisao naredbom `/init` nisu uticali na uspješnost, a rad su poskupili za 20–23%. Fajlovi koje su napisali programeri podigli su uspješnost za 2,4 procentna poena, što nije statistički značajno, a trošak za do 19%. Ipak, bili su značajno bolji od generisanih i, prema radu, pomogli su svim agentima osim Claude Codea. Agenti se uputa zaista drže: alat koji se spominje u fajlu koristili su znatno češće. Prva verzija rada tvrdila je da fajlovi uspješnost obično smanjuju, a treća kaže da značajnog efekta nema.

**Khatri** je na 17 zadataka testirao Claude Code i Codex u tri postavke: s AGENTS.md u svakom koraku, s uputama koje agent otvara po potrebi i bez uputa. Razlike nije bilo, ali uzorak je mali: studija ne može pouzdano otkriti razliku manju od otprilike 30 procentnih poena.

Dva preprinta bilježe poboljšanje, svaki na samo jednom modelu. Kod **Zhanga i saradnika** svih sedam varijanti s opštim pravilima koja dijeli zajednica nadmašilo je osnovnu uspješnost od 50%, ali nijedna razlika pojedinačno nije statistički značajna. Nasumično izabrana pravila dala su otprilike iste rezultate kao pažljivo odabrana, pa sadržaj pravila nije bio presudan. Kod autora **Shepard i Albrecht** uspješnost je bez fajla bila 25,5%, sa statičnim fajlom 28,3%, a s fajlom koji su autori postepeno doterivali na osnovu rezultata 33,0%, što je statistički značajno. Poboljšanje dolazi od većeg broja izmjena koje su se mogle ocijeniti, a ne od veće preciznosti pojedinačne izmjene (ona je ostala oko 59%).

| Rad | Status | Agenti i modeli | Zadaci | Ispravnost koda | Brzina i trošak |
|---|---|---|---|---|---|
| [Lulla i sar.](https://arxiv.org/abs/2601.20404) | radionica JAWs, ICSE 2026 | Codex | 124 izmjene, 10 repozitorija | nije mjerena | vrijeme −28,6%, izlazni tokeni −16,6% |
| [Gloaguen i sar.](https://arxiv.org/abs/2602.11988) | preprint | Claude Code, Codex, Qwen Code; 4 modela | 438 | bez značajne razlike (−2 do +2,4 poena) | trošak +19–23% |
| [Khatri](https://arxiv.org/abs/2607.27250) | preprint | Claude Code, Codex CLI | 17, 3 repozitorija | bez značajne razlike | bez promjene (Codex) |
| [Zhang i sar.](https://arxiv.org/abs/2604.11088) | preprint | Claude Code, Opus 4.6 | 58 | +6,9–13,8 poena, pojedinačno nije značajno | – |
| [Shepard i Albrecht](https://arxiv.org/abs/2606.20512) | preprint | Qwen3.5-35B-A3B | SWE-bench Verified | +7,5 poena uz doterivani fajl (značajno) | – |

Svi radovi koji mjere ispravnost koriste isključivo Python projekte. Nijedan nije pokazao da običan fajl projekta, bilo ručno napisan bilo generisan, daje statistički značajno bolji kod. Nalazi o trošku se razilaze, ali radovi mjere različite stvari i na zadacima različite veličine.

## Praktične implikacije

Ovo su naše preporuke, izvedene iz dokumentacije i radova navedenih gore.

- **Ako koristite samo Claude Code:** držite CLAUDE.md u korijenu repozitorija i neka bude kraći od 200 redova. Detalje za pojedine dijelove projekta prebacite u `.claude/rules/`.
- **Ako tim koristi više alata:** AGENTS.md je zajednički nazivnik. Claude Code ga sam čita ako CLAUDE.md ne postoji. Ako vam ipak treba i CLAUDE.md, upišite u njega `@AGENTS.md`, da ne morate održavati upute na dva mjesta.
- **Prije nego što dodate CLAUDE.local.md** u projekat koji ima samo AGENTS.md, provjerite postavku. U suprotnom AGENTS.md bez upozorenja prestaje važiti.
- **Za Gemini CLI i Copilot** nemojte pretpostaviti da čitaju AGENTS.md, nego provjerite u dokumentaciji.
- **Fajl koji napravi `/init`** pregledajte i dopunite onim što zna samo vaš tim. U najvećoj studiji takvi fajlovi nisu pomogli, a rad su poskupili.
- **Pazite da upute ne protivrječe jedna drugoj**, jer nijedan alat ne garantuje koja će prevladati.
- **Pregledajte ono što agent uradi.** Fajl s uputama utiče na to kako agent radi, ali rezultat ne provjerava.

## Šta NIJE

- **Nije naredba koju agent mora izvršiti.** Fajl je samo još jedan tekst u kontekstu. I sam Anthropic upozorava da agent slabije prati upute iz dužih fajlova, a agents.md navodi da izričita uputa u razgovoru nadjačava fajl.
- **Nije garancija boljeg koda.** Nijedan od pet radova iz 2026. nije pokazao da običan fajl projekta daje statistički značajno bolji kod. Četiri rada su preprinti, i svi su rađeni na Python projektima.
- **Nije jedino pamćenje između sesija.** Claude Code ima i automatsko pamćenje u MEMORY.md.
- **Ne čitaju ga svi podagenti.** Prema [Anthropicovoj dokumentaciji](https://code.claude.com/docs/en/sub-agents), ugrađeni podagenti (subagents), tj. pomoćni agenti kojima glavni agent prepušta dio posla, Explore i Plan u Claude Codeu preskaču CLAUDE.md. Za podagente koje sami napravite čitanje se može isključiti.

## Povezano

- [Šta je AI agent i kako radi?](/clanci/sta-je-ai-agent/) – šta agent jeste i zašto mu za svaki korak treba kontekst.
- [Šta je kontekstni prozor i zašto LLM zaboravlja?](/clanci/sta-je-kontekstni-prozor/) – zašto dug fajl s uputama ima svoju cijenu.
- [LLM Wiki: agent vodi bazu znanja, vi birate izvore](/clanci/karpathy-llm-wiki/) – isti fajlovi kao pravilnik za wiki koji vodi agent.

## Izvori

- [Memory (CLAUDE.md) – Anthropic, Claude Code dokumentacija](https://code.claude.com/docs/en/memory)
- [Claude Code features u Agent SDK-u – Anthropic, dokumentacija](https://code.claude.com/docs/en/agent-sdk/claude-code-features)
- [agents.md – stranica formata AGENTS.md](https://agents.md)
- [Lulla et al., arXiv 2601.20404 (ICSE JAWs 2026)](https://arxiv.org/abs/2601.20404)
- [Gloaguen et al., arXiv 2602.11988 (preprint)](https://arxiv.org/abs/2602.11988)
- [Shepard i Albrecht, arXiv 2606.20512 (preprint)](https://arxiv.org/abs/2606.20512)
- [AGENTS.md – OpenAI Codex dokumentacija](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
