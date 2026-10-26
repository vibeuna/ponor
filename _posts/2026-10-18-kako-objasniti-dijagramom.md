---
layout: post
title: "Objasni dijagramom: Vještina za Claude, ChatGPT i Gemini"
date: 2026-10-18
category: ai-za-sve
image: /assets/images/2026-10-18-kako-objasniti-dijagramom.svg
last_modified_at: 2026-10-26
read_time: 7
description: "Kako naučiti chatbota da objašnjava dijagramom: spremna vještina za kopiranje, objašnjenje kako radi i uputstvo za instalaciju u Claudeu, ChatGPT-u i Geminiju."
tags: [llm]
---

Kada pitate chatbota kako radi prenos novca između dvije banke, obično dobijete nekoliko dugačkih pasusa. Isti odgovor bio bi puno jasniji vizuelno uz nekoliko pravougaonika i par strelica.

Jednostavan fajl pod nazivom `SKILL.md` omogućava umjetnoj inteligenciji da prepozna ovakva pitanja i na njih odgovori dijagramom. U nastavku donosimo gotov fajl, detaljno objašnjenje njegovih dijelova i uputstvo gdje ga sačuvati u Claudeu, ChatGPT-u i Geminiju.

*Ažurirano 26. oktobra 2026: ispravljeni koraci za Claude (šta dijalog prihvata) i ChatGPT (putanja i planovi).*

## Ukratko

[Vještina](/rjecnik/vjestina/) (engl. skill) je obični folder s fajlom `SKILL.md`. U njemu se nalaze upute koje chatbot učitava samo kada vaše pitanje odgovara opisu te vještine. 

Vještina `objasni-dijagramom` uči model da na pitanja tipa "kako ovo radi" odgovori vizuelno. Upute traže da model sam izabere najbolju vrstu dijagrama, da ga nacrta u SVG formatu, da ne izmišlja podatke i da dijagram ostane jednostavan.

Dostupnost opcije se razlikuje po aplikacijama:
* **Claude:** Radi na paketima Free, Pro, Max, Team i Enterprise (potrebno je uključiti opciju za izvršavanje koda).
* **Gemini:** Radi uz prijavu na račun, navršenih 18 godina i uključen opciju "Keep Activity".
* **ChatGPT:** OpenAI vještine navodi za planove Business, Enterprise, Healthcare i Edu.

Na našem testu, vještina je odlično radila u Claudeu. Gemini je povremeno imao problema s njenim aktiviranjem, dok na besplatnom ChatGPT-u ova opcija uopšte ne postoji.

## Šta je vještina i kako radi?

Vještina se nalazi u folderu čiji je glavni dio fajl `SKILL.md`. Na samom vrhu fajla stoji zaglavlje (YAML) s dva obavezna polja: naziv (`name`) i opis (`description`). Ispod zaglavlja pišu se upute u običnom Markdown formatu. Folder može sadržavati i dodatne skripte ili dokumente. Sva pravila su opisana u otvorenoj [specifikaciji Agent Skills](https://agentskills.io/specification).

Naziv vještine ima stroga pravila: do 64 znaka, samo mala slova, brojevi i crtice (bez razmaka i specijalnih znakova). Naziv fajla i foldera moraju biti potpuno identični. Opis može imati do 1.024 znaka i precizno objašnjava šta vještina radi i kada je AI treba pokrenuti.

Glavna prednost vještina u odnosu na stalne upute jeste ušteda memorije. Stalne upute AI čita u svakom razgovoru, što zauzima prostor. Kod vještina, AI na početku vidi samo naziv i opis (oko 100 tokena). Cijeli fajl se učitava tek kada postavite pitanje koje odgovara opisu. Zbog toga neiskorištene vještine uopšte ne opterećuju [kontekstni prozor](/rjecnik/kontekstni-prozor/).

{% include diagram.html name="kako-objasniti-dijagramom" caption="Instalirane vještine zauzimaju vrlo malo memorije. Upute se učitavaju tek kada pitanje odgovara opisu." alt="Dijagram prikazuje kako AI učitava vještinu objasni-dijagramom tek kada korisnik postavi pitanje o prenosu novca." %}

Važno je znati da AI ne prepoznaje uvijek savršeno kada treba upotrebiti vještinu. Zato opis mora biti napisan što jasnije i preciznije.

## Kod za kopiranje

Ovo je pripremljena i testirana verzija vještine na bosanskom jeziku. Slobodno je kopirajte. Folder i fajl nazovite `objasni-dijagramom`.

````markdown
---
name: objasni-dijagramom
description: "Objašnjava kod, sisteme, procese ili pojmove dijagramom. Koristi ovu vještinu kad korisnik pita kako nešto radi, kako su dijelovi povezani, šta šta poziva, kakav je tok ili životni ciklus, ili traži dijagram arhitekture, dijagram toka, dijagram sekvence ili dijagram stanja. Koristi je i kad odgovor ima jasnu strukturu (koraci, grananja, dijelovi, stanja), čak i ako korisnik nije tražio dijagram."
---
# Objasni dijagramom

## Stil pisanja

Odgovaraj na bosanskom jeziku. Piši kratke rečenice. Koristi aktiv. U svakoj rečenici jedna misao. Biraj jednostavne riječi. Zadrži stručne termine i objasni ih kad se prvi put pojavuju.

## 1. Izaberi vrstu dijagrama

- Koraci ili odluke: dijagram toka
- Ko s kim komunicira i kojim redom: dijagram sekvence
- Stanja i prelazi između njih: dijagram stanja
- Dijelovi sistema i veze među njima: dijagram toka s dijelovima grupisanim u cjeline
- Strukture podataka: dijagram klasa ili ER dijagram
- Događaji kroz vrijeme: vremenska linija

## 2. Izaberi format

- Generiši isključivo čist SVG kod (`<svg>...</svg>`).

## 3. Osloni se na izvor

- Pročitaj relevantne fajlove prije nego što crtaš.
- Koristi stvarne nazive iz koda (moduli, funkcije, servisi).
- Ne izmišljaj dijelove. Ako nešto pretpostaviš, označi to s "(pretpostavka)".

## 4. Neka bude čitljivo

- Najviše 10 čvorova ili glavnih komponenti.
- Natpis čvora/dugmeta: najviše 5 riječi.
- Procesi idu odozgo nadolje ili slijeva nadesno.
- Boju koristi samo kad nešto znači (npr. put greške, vanjski sistem). Najviše 3 boje.

## 5. Odgovor

- Pokaži SVG dijagram.
- Nakon toga dodaj 2 do 4 kratke rečenice. Objasni samo ono što dijagram ne može pokazati.
````

## Objašnjenje dijelova vještine

**Stil pisanja.** Pravila traže kratke rečenice, aktiv i jednostavne riječi. Ova pravila su preuzeta iz standarda ASD-STE100 (*Simplified Technical English*), koji se koristi za pisanje jasne tehničke dokumentacije.

**1. Vrsta dijagrama.** Ova sekcija uči AI kako da izabere pravi oblik za podatke:
* **Dijagram toka:** za korake i odluke.
* **Dijagram sekvence:** za komunikaciju i hronološki redoslijed.
* **Dijagram stanja:** za promjene stanja sistema.
* **ER ili dijagram klasa:** za strukture podataka.
* **Vremenska linija:** za hronološke događaje.

Istraživanja (Larkin & Simon, 1987) potvrđuju da dijagrami smanjuju trud pri čitanju jer drže povezane informacije na jednom mjestu. Richard Mayer (2009) je kroz 11 eksperimenata dokazao da kombinacija teksta i slika daje znatno bolje rezultate u učenju nego sam tekst.

**2. Format.** Vještina traži isključivo čist SVG kod. SVG je standardni format za vektorsku grafiku zapisan kao tekst, što znači da ga AI lako generiše, a korisnik ga može naknadno uređivati.

**3. Izvori.** AI prvo mora pročitati priložene fajlove i koristiti stvarna imena iz koda ili dokumentacije. Sve što nije potvrđeno u tekstu mora označiti kao pretpostavku.

**4. Čitljivost.** Ograničenje na maksimalno 10 elemenata, 5 riječi po natpisu i 3 boje osigurava da dijagram ostane pregledan i razumljiv na prvi pogled.

**5. Odgovor.** AI prvo prikazuje dijagram, a zatim dodaje samo 2 do 4 kratke rečenice za detalje koji se ne vide na slici.

## Primjer: Kako radi inzulin

Urednik je testirao vještinu pitanjem: *"Kako radi inzulin, objasni dijagramom?"*

<figure id="fig-primjer-inzulin" class="ponor-diagram" role="figure" aria-label="Primjer odgovora: dijagram toka o tome kako radi inzulin">
  <img src="/assets/images/2026-10-18-kako-objasniti-dijagramom-primjer-inzulin.png" alt="Dijagram toka koji objašnjava djelovanje inzulina u organizmu." loading="lazy" width="1201" height="1170">
  <figcaption class="ponor-diagram-caption">Odgovor modela uz primjenu vještine. (Primjer izlaza, nije medicinski savjet).</figcaption>
</figure>

Dijagram u potpunosti poštuje pravila: ima sedam elemenata, jasne natpise i usmjeren je odozgo prema dolje. Boje jasno razdvajaju funkcije: ljubičasta prikazuje pankreas i inzulin, a zelena ciljne ćelije.

## Gdje i kako sačuvati vještinu

### Claude

1. Otvorite **Settings**, pa u dijelu **Customize** izaberite **Skills**.
2. Kliknite **+ Add**, pa **Upload skill**.
3. Prevucite fajl ili ga izaberite putem opcije **browse**. Dijalog prihvata `.md` fajl (mora sadržavati naziv i opis u YAML zaglavlju) ili `.zip` odnosno `.skill` fajl koji sadrži `SKILL.md`.

*Napomena:* U opcijama mora biti uključena stavka "Code execution and file creation". Ako koristite Claude Code, fajl ubacite u folder `~/.claude/skills/`.

### Gemini

1. Otvorite **Settings**, pa u dijelu **Preferences** izaberite **Skills**.
2. Kliknite **Create**, pa **Upload**.
3. Ubacite fajlove ili cijeli folder (podržani su PDF, CSV, PY, TXT i MD fajlovi).

### ChatGPT

OpenAI vještine navodi za planove Business, Enterprise, Healthcare i Edu. U bočnoj traci otvorite **Plugins**, zatim karticu **Skills**, pa **Create** i **Upload from your computer**. Dostupnost zavisi od postavki radnog prostora.

---

## Povezano

- [ASD-STE100: Avionska pravila pisanja za vaš chatbot](https://www.ponor.ba/clanci/asd-ste100-llm/) – Kako podesiti trajna pravila stila pisanja.
- [CLAUDE.md i AGENTS.md: Upute za AI agente](https://www.ponor.ba/clanci/claude-md-agent-md/) – Razlika između trajnih uputa i vještina.
- [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/) – Šta je vještina, kako se učitava, gdje radi i na šta paziti.

## Izvori

- [Specification, Agent Skills](https://agentskills.io/specification)
- [Agent Skills (overview), Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Use skills in Claude, Claude Help Center](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [Skills in ChatGPT, OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Create & manage skills for Gemini Apps, Gemini Apps Help](https://support.google.com/gemini/answer/17094296)
- [Scalable Vector Graphics (SVG) 2, W3C](https://www.w3.org/TR/SVG2/)
- [Larkin & Simon, Why a Diagram is (Sometimes) Worth Ten Thousand Words](https://doi.org/10.1111/j.1551-6708.1987.tb00863.x)
