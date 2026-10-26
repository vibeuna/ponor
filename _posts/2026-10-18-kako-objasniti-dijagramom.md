---
layout: post
title: "Objasni dijagramom: Vještina za Claude, ChatGPT i Gemini"
date: 2026-10-18
category: ai-za-sve
image: /assets/images/2026-10-18-kako-objasniti-dijagramom.svg
last_modified_at: 2026-10-26
read_time: 6
description: "Kako naučiti chatbota da objašnjava dijagramom: spremna vještina za kopiranje, objašnjenje kako radi i uputstvo za instalaciju u Claudeu, ChatGPT-u i Geminiju."
tags: [ai-agenti, skills]
---

Kada pitate chatbota kako radi prenos novca između dvije banke, obično dobijete nekoliko dugačkih pasusa. Isti odgovor bio bi puno jasniji vizuelno uz nekoliko pravougaonika i par strelica.

Jednostavan fajl pod nazivom `SKILL.md` omogućava umjetnoj inteligenciji da prepozna ovakva pitanja i na njih odgovori dijagramom. U nastavku donosimo gotov fajl, detaljno objašnjenje njegovih dijelova i uputstvo gdje ga sačuvati u Claudeu, ChatGPT-u i Geminiju.

*Ažurirano 26. oktobra 2026: opšti opis vještina i uslovi po alatima prebačeni su u članak [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/). Ispravljeni su koraci za Claude (šta dijalog prihvata) i ChatGPT (putanja i planovi).*

## Ukratko

[Vještina](/rjecnik/vjestina/) (engl. skill) je obični folder s fajlom `SKILL.md`. U njemu se nalaze upute koje chatbot učitava samo kada vaše pitanje odgovara opisu te vještine. 

Vještina `objasni-dijagramom` uči model da na pitanja tipa "kako ovo radi" odgovori vizuelno. Upute traže da model sam izabere najbolju vrstu dijagrama, da ga nacrta u SVG formatu, da ne izmišlja podatke i da dijagram ostane jednostavan.

Vještine rade u Claudeu, Geminiju i ChatGPT-u, ali uslovi se razlikuju po alatu i planu. Detalji su u članku [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/#gdje-radi).

Na našem testu, vještina je odlično radila u Claudeu. Gemini je povremeno imao problema s njenim aktiviranjem, dok na besplatnom ChatGPT-u ova opcija uopšte ne postoji.

## Šta je vještina?

Vještina je folder čiji je glavni dio fajl `SKILL.md`. Na vrhu fajla su naziv i opis, a ispod njih upute u Markdownu. AI na početku vidi samo naziv i opis, a cijele upute učitava tek kad pitanje odgovara opisu. Zato neiskorištene vještine ne opterećuju [kontekstni prozor](/rjecnik/kontekstni-prozor/). Pravila formata su u [specifikaciji Agent Skills](https://agentskills.io/specification), a ograničenja i sigurnost u članku [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/).

{% include diagram.html name="kako-objasniti-dijagramom" caption="Instalirane vještine zauzimaju vrlo malo memorije. Upute se učitavaju tek kada pitanje odgovara opisu." alt="Dijagram prikazuje kako AI učitava vještinu objasni-dijagramom tek kada korisnik postavi pitanje o prenosu novca." %}

AI ne prepoznaje uvijek kada treba upotrijebiti vještinu, pa opis mora biti jasan i precizan.

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

Putanje su onakve kakve ih vidimo u aplikacijama (oktobar 2026). Pomoćne stranice proizvođača ih ponegdje opisuju drugačije, a uslovi (plan, uključeno izvršavanje koda, godine, Keep Activity) i ograničenja su u članku [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/#gdje-i-kako-je-dodati).

### Claude

1. Otvorite **Settings**, pa u dijelu **Customize** izaberite **Skills**.
2. Kliknite **+ Add**, pa **Upload skill**.
3. Prevucite fajl `SKILL.md` ili ga izaberite putem opcije **browse**. Dijalog prihvata i `.zip` ili `.skill` fajl koji sadrži `SKILL.md`.

### Gemini

1. Otvorite **Settings**, pa u dijelu **Preferences** izaberite **Skills**.
2. Kliknite **Create**, pa **Upload**.
3. Otpremite fajl `SKILL.md` (dijalog navodi PDF, CSV, PY, TXT i MD fajlove).

### ChatGPT

OpenAI vještine navodi za planove Business, Enterprise, Healthcare i Edu. U bočnoj traci otvorite **Plugins**, zatim karticu **Skills**, pa **Create** i **Upload from your computer**.

---

## Povezano

- [Šta je SKILL i kako radi?](https://www.ponor.ba/clanci/sta-je-skill/) – Šta je vještina, kako se učitava, gdje radi i na šta paziti.
- [ASD-STE100: Avionska pravila pisanja za vaš chatbot](https://www.ponor.ba/clanci/asd-ste100-llm/) – Kako podesiti trajna pravila stila pisanja.
- [CLAUDE.md i AGENTS.md: Upute za AI agente](https://www.ponor.ba/clanci/claude-md-agent-md/) – Razlika između trajnih uputa i vještina.

## Izvori

- [Specification, Agent Skills](https://agentskills.io/specification)
- [Skills in ChatGPT, OpenAI Help Center](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Scalable Vector Graphics (SVG) 2, W3C](https://www.w3.org/TR/SVG2/)
- [Larkin & Simon, Why a Diagram is (Sometimes) Worth Ten Thousand Words](https://doi.org/10.1111/j.1551-6708.1987.tb00863.x)
