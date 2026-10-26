---
layout: post
title: "Šta je SKILL i kako radi?"
date: 2026-10-26
category: vodici
image: /assets/images/2026-10-26-sta-je-skill.svg
read_time: 6
description: "Vještina je folder s uputama koje AI učitava tek kad zatrebaju. Kako se učitava, gdje radi, koliko pouzdano se aktivira i na šta paziti."
tags: [ai-agenti]
---

Neko svake sedmice u chatbot zalijepi isti tekst od dvadeset redova: kakav ton da koristi, koje naslove da stavi, kako da formatira tabelu. Zadatak se ponavlja, upute su iste, a zalijepi ih ručno svaki put. [Vještina](/rjecnik/vjestina/) (engl. skill) je način da se te upute jednom spreme i da ih model sam pronađe kad zatrebaju.

## Ukratko

Vještina je folder s fajlom SKILL.md. Na vrhu fajla su naziv i opis, ispod su upute. Model na početku vidi samo naziv i opis, a cijele upute obično učitava tek kad zahtjev odgovara opisu. Vještinu možete pozvati i po nazivu. Format je objavio Anthropic, a podržavaju ga Claude, Codex, GitHub Copilot i Cursor. Aktiviranje nije zajamčeno: jedini eksperiment koji smo našli, firme Tessl na jednom alatu, pokazuje aktiviranje u 41% zadataka bez izričitog zahtjeva. Vještine iz nepoznatih izvora mogu biti opasne.

## Šta je vještina?

Vještina je folder. Obavezan je samo fajl `SKILL.md`. Uz njega mogu stajati folderi `scripts/` (skripte), `references/` (dodatni dokumenti) i `assets/` (šabloni i slični fajlovi), a dozvoljeni su i drugi fajlovi.

Na vrhu `SKILL.md` je [zaglavlje](https://agentskills.io/specification) (YAML) s dva obavezna polja:

- `name`: do 64 znaka, mala slova, cifre i crtice, jednak nazivu foldera.
- `description`: do 1.024 znaka, šta vještina radi i kada je treba koristiti.

Ispod zaglavlja su upute u Markdownu, bez ograničenja oblika. Specifikacija preporučuje tijelo kraće od 5.000 [tokena](/rjecnik/token/) i 500 redova.

Anthropic je format objavio 16. oktobra 2025. Dana 18. decembra 2025. dodao je napomenu da je Agent Skills objavljen kao otvoreni standard. Specifikacija je javna i razvija se otvoreno. Nijedna stranica koju smo pročitali ne imenuje nezavisno tijelo koje njime upravlja.

## Kako funkcioniše

Prema Claude dokumentaciji, vještina se učitava u tri nivoa, da ne zauzima [kontekstni prozor](/rjecnik/kontekstni-prozor/) unaprijed. Detalji se razlikuju od alata do alata.

1. **Pri pokretanju:** naziv i opis svake vještine ulaze u [sistemski prompt](/rjecnik/sistemski-prompt/), oko 100 tokena po vještini.
2. **Pri poklapanju:** kad zahtjev odgovara opisu, učitava se cijelo tijelo `SKILL.md`.
3. **Po potrebi:** fajlovi iz `scripts/`, `references/` i `assets/` čitaju se tek kad ih upute traže. U Claudeu se skripte pokreću kroz bash (komandnu liniju), a u kontekst ulazi samo njihov izlaz, ne i kod.

Skripte traže okruženje za izvršavanje koda. U Claudeu na webu mora biti uključeno, a Gemini aplikacije [ne podržavaju skripte koje trebaju internet](https://support.google.com/gemini/answer/17094296). Šta vještina radi kad je izvršavanje koda isključeno, stranice koje smo čitali ne kažu.

Odluku obično donosi model: poredi zahtjev s opisima ([Claude dokumentacija](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)). Izuzetak je [Gemini CLI](https://geminicli.com/docs/cli/skills/), gdje model predlaže, a korisnik odobrava svako aktiviranje. Korisnik vještinu može pozvati i po nazivu: `/naziv` u Claude Code i Cursoru, `@` u ChatGPT-u i Codexu. Neki alati dozvoljavaju da se automatsko korištenje isključi. U Claude Code to radi polje `disable-model-invocation: true`, a u Codexu se implicitno pozivanje podešava opcijom `allow_implicit_invocation`.

{% include diagram.html name="sta-je-skill" caption="Prozor se puni korak po korak: nazivi i opisi su uvijek u njemu, tijelo vještine ulazi kad opis odgovara, a kod skripte nikad." alt="Dijagram u tri koraka prikazuje šta ulazi u kontekstni prozor: nazivi i opisi vještina na početku, tijelo SKILL.md kad zahtjev odgovara opisu, a po potrebi dokument iz references i samo izlaz skripte." %}

**Primjer (izmišljen).** Vještina `sedmicni-izvjestaj` ima opis "Pretvara bilješke sa sastanaka u sedmični izvještaj od jedne stranice. Koristi se kad korisnik traži izvještaj ili sažetak sedmice." Korisnik napiše: "Pripremi izvještaj iz ovih bilješki." Model u opisu prepozna poklapanje i učita tijelo. Tijelo kaže da izvještaj slijedi šablon iz `references/sablon.md` i da se prije slanja pokrene `scripts/provjeri.py`. Model pročita šablon, pokrene skriptu i u kontekst dobije samo njen izlaz, na primjer "3 problema". Ostale vještine za to vrijeme zauzimaju samo svojih oko 100 tokena.

## Po čemu se razlikuje od ostalog?

- **Trajne upute.** Važe u svakom razgovoru. [Help Center](https://support.claude.com/en/articles/12512176-what-are-skills) ih opisuje kao upute koje se primjenjuju na sve razgovore, dok su vještine vezane za zadatak.
- **Fajlovi s uputama (CLAUDE.md).** Claude Code dokumentacija kaže da se, za razliku od sadržaja CLAUDE.md, tijelo vještine učitava samo kad se koristi. Više o [fajlovima s uputama](https://www.ponor.ba/clanci/claude-md-agent-md/).
- **Prompt.** Prompt su upute na nivou razgovora, za jednokratan zadatak. Vještina je sačuvana i višekratna.
- **MCP.** Prema Help Centeru, MCP povezuje Claude s vanjskim uslugama, a vještine daju proceduralno znanje. [OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) to kaže slično: vještine su višekratne upute, a aplikacije povezuju ChatGPT s uslugama. Više o [MCP-u](https://www.ponor.ba/clanci/sta-je-mcp/).
- **Komande oblika /naziv.** Stari fajlovi u `.claude/commands/` i dalje rade i prave iste komande. Vještine dodaju prateće fajlove, kontrolu pozivanja i automatsko učitavanje.
- **Podagent.** Claude Code može pokrenuti vještinu u podagentu (agentu kojem glavni agent povjerava dio posla), pomoću polja `context: fork`.

## Gdje radi?

Podaci sa stranica samih proizvođača, 26. oktobra 2026:

| Alat | Navodi li stranica proizvođača otvoreni standard? | Napomena |
|---|---|---|
| Claude (claude.ai, API) | Anthropic je autor formata | [Help Center](https://support.claude.com/en/articles/12512180-using-skills-in-claude) navodi planove Free, Pro, Max, Team i Enterprise; API je u beta fazi |
| Claude Code | da | [dokumentacija](https://code.claude.com/docs/en/skills) |
| ChatGPT | ne | OpenAI [ih navodi](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) za planove Business, Enterprise, Healthcare i Edu |
| Codex | da | [dokumentacija](https://learn.chatgpt.com/docs/build-skills) |
| Gemini aplikacije | ne | [vještine postoje](https://support.google.com/gemini/answer/17094296), standard se ne spominje; kompatibilnost ne tvrdimo |
| GitHub Copilot | da | [stranica](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) ne navodi status (preview ili opšta dostupnost) |
| Cursor | da | [dokumentacija](https://cursor.com/docs/context/skills) |

Stranice se razilaze oko planova i menija, pa su gornji podaci samo orijentacija. Putanje za instalaciju su u tekstu [Objasni dijagramom](https://www.ponor.ba/clanci/kako-objasniti-dijagramom/).

Alati dodaju polja izvan specifikacije, na primjer `when_to_use`, `paths`, `context` ili `disable-model-invocation`, a Codex i poseban fajl `agents/openai.yaml`. Ponorov zaključak: u drugim alatima sigurno radi samo vještina koja koristi polja iz specifikacije.

## Kako napisati dobru vještinu?

Smjernice u [Claude dokumentaciji](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) kažu:

- **Opis** piše se u trećem licu ("Obrađuje Excel fajlove"), kaže šta vještina radi i kada se koristi, i sadrži ključne pojmove. Opis "Pomaže s dokumentima" je preširok. Claude vještinu bira upravo po opisu, među potencijalno više od 100 dostupnih (u izvorniku: "from potentially 100+ available Skills").
- **Tijelo** do 500 redova. Veći sadržaj ide u zasebne fajlove, jedan nivo duboko.
- **Samo ono što model ne zna.** Ne objašnjavati opšte poznato.
- **Prije pisanja** napraviti barem tri evaluacije i uporediti rezultat s radom bez vještine. Dokumentacija priznaje da trenutno ne postoji ugrađen način za njihovo pokretanje.

Ponorov savjet: ako opis ne pogađa zahtjev, prvo ga prepravite, pa tek onda dopisujte tijelo.

## Aktivira li se pouzdano?

Nismo našli nijednog proizvođača koji objavljuje stope aktiviranja. [Claude Help Center](https://support.claude.com/en/articles/12512180-using-skills-in-claude) savjetuje da vještinu imenujete u zahtjevu ako je Claude preskoči.

Jedini podatak koji smo našli je eksperiment firme [Tessl](https://tessl.io/blog/a-proposed-framework-for-evaluating-skills-research-eng-blog), koja nije autor testiranog alata. Tessl je 15. aprila 2026. u Claude Code (model nije imenovan) pokrenuo po 2.286 zadataka u svakom uslovu. Bez prisile, vještina se aktivirala u 41% zadataka (929). Kad je zahtjev to izričito tražio, u 98% (2.240). U istom tekstu stoji i rečenica "only half of the times" (engl., "samo u pola slučajeva") o aktiviranju bez prisile, koja se ne slaže s njihovom vlastitom tabelom. Riječ je o jednom eksperimentu jedne firme, pa rezultat ne važi nužno za druge alate i modele.

## Je li sigurna?

Claude dokumentacija upozorava da vještine treba koristiti samo iz pouzdanih izvora, svojih ili Anthropicovih. Zlonamjerna vještina može dovesti do krađe podataka i neovlaštenog pristupa sistemu. Treba pregledati sve priložene fajlove, a vještine koje dohvataju vanjske adrese rizičnije su. Čak i pouzdana vještina može postati opasna ako se promijene vanjske zavisnosti. Pregled važi i za vještinu koju je podijelio kolega. [OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) skenira vještine koje korisnici dodaju, ali piše da to ne zamjenjuje vaš vlastiti pregled.

Dva nezavisna istraživanja pokazuju da rizik nije teoretski. Njihovi uzorci i definicije se razlikuju, pa brojke ne poredimo.

- **[Snyk, "ToxicSkills"](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)** (blog, 5. februar 2026, izvještaj dobavljača sigurnosnih alata): 3.984 vještine s ClawHub i skills.sh; 36,82% ima barem jednu manu bilo koje ozbiljnosti, 13,4% (534) kritičnu, a ljudski pregled potvrdio je 76 zlonamjernih sadržaja (engl. malicious payloads). Izvještaj ne govori ništa o vještinama koje je objavio Anthropic.
- **[arXiv 2601.10338](https://arxiv.org/abs/2601.10338)** (15. januar 2026, preprint (rad koji još nije prošao recenziju)): od 42.447 prikupljenih vještina s dvije neimenovane platforme analizirano je 31.132, a 26,1% ima barem jednu ranjivost. Nalaz dolazi iz automatskog skenera čija je preciznost 86,7%, a odziv 82,5% (podaci iz sažetka). Autori pišu da su vještine sa skriptama "2.12x more likely" (engl.) ranjive, ali je statistika omjer izgleda (engl. odds ratio) od 2,12 uz p < 0,001, što nije isto što i "2,12 puta češće".

Ponorov savjet: instalirajte samo vještine čiji izvor poznajete, pročitajte `SKILL.md` i sve skripte prije prvog korištenja i pazite na vještine koje pozivaju vanjske adrese.

## Šta NIJE

- **Nije način da se model poveže s uslugama.** Za to služe MCP serveri i aplikacije. Vještina daje upute kako nešto raditi.
- **Nije zajamčeno da će se aktivirati.** Automatsko korištenje je namjera dizajna, a ne izmjerena pouzdanost (vidi gore: 41% u jednom eksperimentu).
- **"Otvoreni standard" ne znači nezavisno upravljanje.** Znači da je specifikacija javna i da se razvija otvoreno. Tijelo koje njome upravlja nismo našli.
- **Popularnost nije kvalitet.** Repozitorij [anthropics/skills](https://github.com/anthropics/skills) ima oko 183.800 zvjezdica (stanje 26. oktobra 2026), ali to mjeri interes. Sam repozitorij navodi da su primjeri namijenjeni demonstraciji i obrazovanju.

## Povezano

- [Objasni dijagramom: vještina za Claude, ChatGPT i Gemini](https://www.ponor.ba/clanci/kako-objasniti-dijagramom/) – konkretna vještina s putanjama za instalaciju u Claude, ChatGPT i Gemini.
- [Šta je MCP i kako AI povezuje s alatima?](https://www.ponor.ba/clanci/sta-je-mcp/) – drugi način proširenja asistenta: veza s uslugama, a ne upute.
- [CLAUDE.md i AGENTS.md: upute koje agent čita prije posla](https://www.ponor.ba/clanci/claude-md-agent-md/) – fajlovi s uputama koje Claude Code čita prije posla, za razliku od vještine koja se učitava po potrebi.

## Izvori

- [Specification, Agent Skills](https://agentskills.io/specification)
- [Agent Skills (overview), Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Equipping agents for the real world with Agent Skills, Anthropic Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Using skills in Claude, Claude Help Center](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Extend Claude with skills, Claude Code Docs](https://code.claude.com/docs/en/skills)
- [Skill authoring best practices, Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale, arXiv 2601.10338](https://arxiv.org/abs/2601.10338)
