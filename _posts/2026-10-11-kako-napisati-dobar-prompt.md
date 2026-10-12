---
layout: post
title: "Kako napisati dobar prompt: jezik, situacija, oblik odgovora"
date: 2026-10-11
category: ai-za-sve
image: /assets/images/2026-10-11-kako-napisati-dobar-prompt.svg
read_time: 7
description: "Praktični savjeti za pisanje promptova za ChatGPT i Gemini, uz naš test: kako dobiti odgovor na bosanskom, ijekavicom i s cijenama u KM."
tags: [llm]
---

Kad smo pitali "Objasni mi šta je inflacija.", Gemini je odgovorio ekavicom ("cena", "sledeće", "vrednost"), s cijenama u eurima i engleskim izrazima poput "Demand-Pull". ChatGPT je pisao ijekavicom, ali je i on računao u eurima. Onda smo istom [promptu](/rjecnik/prompt/) (uputi ili upitu koji upisujete chatbotu) dodali da odgovor treba biti na bosanskom jeziku, ijekavicom, s primjerima cijena u KM. Ovaj put su oba chatbota odgovorila ijekavicom i računala u KM.

Ovo je jedan od četiri para promptova iz našeg testa u kojem smo uporedili dva chatbota zasnovana na umjetnoj inteligenciji (engl. artificial intelligence, AI). U oba chatbota tekst piše [veliki jezički model (engl. large language model, LLM)](/rjecnik/veliki-jezicki-model/), u nastavku samo model. Svaki zadatak zadali smo dvaput: jednom kao kratko pitanje, a jednom kao detaljan prompt. Testirali smo 11. oktobra 2026. u besplatnim verzijama ChatGPT-a (model GPT-6) i aplikacije Gemini (Gemini 3.6 Flash), prijavljeni na svoj nalog. Svaki prompt poslali smo samo jednom. Isti prompt sljedeći put može dati drugačiji odgovor, pa rezultate shvatite kao primjere, a ne kao mjerenje.

## Ukratko

Dobar prompt chatbotu kaže četiri stvari: na kojem jeziku da odgovori, šta treba znati o vašoj situaciji, kakav oblik odgovora želite i šta da uradi ako mu nešto nedostaje. [Google](https://support.google.com/a/users/answer/14200040) i [Microsoft](https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5) u svojim vodičima savjetuju slično: budite konkretni, navedite kontekst i opišite oblik odgovora. Ako želite odgovor na bosanskom, najvažnije je izričito navesti jezik, ijekavicu i KM. Ni dobar prompt ne garantuje tačan odgovor, pa ga i dalje morate sami provjeriti.

## Kako dobiti odgovor na bosanskom?

Napišite to izričito. Kad prompt nije navodio jezik, tri odgovora u našem testu bila su na ekavici, a tri su sadržavala hrvatske riječi. Ekavicu i hrvatske riječi prepoznavali smo sami, po izboru riječi. Hrvatske riječi ("tvrtka", "računalu", "tečajeve") pojavile su se u oba odgovora na inače detaljan prompt za CV. Taj prompt je precizno opisao posao, ali o jeziku nije rekao ništa.

Anthropic u [uputama za rad s drugim jezicima](https://platform.claude.com/docs/en/build-with-claude/multilingual-support) savjetuje da jezik odgovora navedete izričito i da tražite prirodan izraz, kakav bi koristio izvorni govornik. Nijedan izvor koji smo pregledali ne bavi se razlikom između bosanskog, hrvatskog i srpskog. Za to imamo samo vlastiti test.

U našem testu djelovala je ova rečenica:

> Piši na bosanskom jeziku, ijekavicom (npr. "vrijeme", "mlijeko"), latinicom.

Ako je riječ o novcu, dodajte "cijene u KM". Ako želite jednostavan jezik, dopišite i "bez stručnih izraza".

Da ne biste ovo kucali svaki put, uputu možete sačuvati za sve razgovore (pogledajte sljedeći odjeljak).

## Kako sačuvati upute za svaki razgovor?

Upute o jeziku ne morate ponavljati u svakom promptu. I Gemini i ChatGPT imaju postavku u koju ih upišete jednom, a chatbot ih zatim primjenjuje u svakom razgovoru.

**Gemini (web):**

1. Otvorite meni i izaberite **Settings & help**.
2. Kliknite **Personal context**.
3. Pod **Your instructions for Gemini** kliknite **Add**, upišite uputu i potvrdite klikom na **Submit**.

U aplikaciji na telefonu ista opcija nalazi se pod: meni → vaša profilna slika → **Personal context**. Google [navodi](https://support.google.com/gemini/answer/16598625) da upute mogu dodati svi korisnici s ličnim Google nalogom, ali ne i oni s poslovnim ili školskim nalogom.

**ChatGPT (web):**

1. Kliknite na svoje ime.
2. Izaberite **Personalization**.
3. U polje **Custom Instructions** upišite uputu i kliknite **Save**.

Na primjer:

```
Uvijek piši na bosanskom jeziku, ijekavicom, latinicom. Cijene navodi u KM. Piši jednostavno, bez stručnih izraza.
```

Ovu uputu testirali smo samo unutar prompta, a ne kao sačuvanu uputu.

## Šta chatbot treba znati o vašoj situaciji?

Model ne zna ništa o vama osim onoga što napišete. Anthropic u [vodiču za pisanje promptova](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) savjetuje da ga zamislite kao pametnog kolegu koji je tek došao i ne zna kontekst. Ako bi vaša uputa zbunila takvog kolegu, zbunit će i model.

U našem testu kratki prompt "Napiši mi email šefu da sutra ne mogu doći." dao je šablon s praznim mjestima. ChatGPT je umjesto imena ostavio "[Vaše ime]", a Gemini "[Tvoje ime]" i još jedno prazno mjesto za razlog. U detaljnoj verziji naveli smo ime šefice, razlog (dijete ima temperaturu), dva prijedloga (rad od kuće popodne i sastanak u srijedu), željeni ton i ograničenje od najviše 80 riječi. ChatGPT je napisao email od 42 riječi, s razlogom i oba prijedloga, spreman za slanje.

{% include diagram.html name="kako-napisati-dobar-prompt" caption="Isti zahtjev, dva prompta: doslovni odgovori ChatGPT-a iz našeg testa." alt="Kratak prompt daje opšti šablon s praznim mjestom za ime; detaljan prompt sa zadatkom, kontekstom, prijedlozima i oblikom daje email od 42 riječi, spreman za slanje." %}

Napišite i zašto nešto tražite. Anthropic navodi da model bolje slijedi uputu kad zna razlog za nju. Umjesto "bez skraćenica" napišite "ovo ću naglas čitati nani, pa izbjegavaj skraćenice".

Pazite i na ono što model doda na svoju ruku. Oba chatbota pretpostavila su da email piše žena, a Gemini je temperaturu opisao kao "visoku", iako to nismo napisali.

## Kako tražiti tačan oblik odgovora?

Recite kako odgovor treba izgledati: tabela, spisak ili pasusi, kolike dužine i kojim tonom. Microsoft i Google oblik odgovora navode kao poseban dio dobrog prompta.

Na prompt "Treba mi plan ishrane." oba chatbota su umjesto plana postavila pitanja. U detaljnoj verziji tražili smo sedmični plan večera za četveročlanu porodicu s budžetom od oko 100 KM, bez svinjetine, u tabeli s četiri kolone, uz spisak za kupovinu raspoređen po odjeljcima marketa. Oba chatbota dala su tabelu i spisak kakve smo tražili. Cijene je dodao samo ChatGPT, pa se samo kod njega moglo provjeriti da li se plan uklapa u budžet. Pojedinačne cijene nismo provjeravali.

Ako želite određeni stil, mogu pomoći primjeri. OpenAI u [svom vodiču](https://developers.openai.com/api/docs/guides/reasoning-best-practices) piše da modelima sa zaključivanjem (engl. reasoning) primjeri često nisu potrebni. To su modeli koji prije odgovora sami prolaze kroz korake rješavanja. Ako vaš chatbot ima takav način rada, počnite bez primjera, a dodajte ih tek ako odgovor promaši.

## Neka chatbot prvo pita vas

Kad niste sigurni šta sve model treba znati, zamolite ga da vam postavi pitanja. Na kratko "Pomozi mi napisati CV." oba chatbota su i sama postavila pitanja, ali uopštena. ChatGPT je čak na početku spomenuo Austriju i Njemačku i ponudio CV na njemačkom.

Detaljna verzija glasila je: "Želim napisati CV za posao administratorice u općini. Prije nego išta napišeš, postavi mi pet pitanja o mom iskustvu i obrazovanju koja su ti potrebna. Čekaj moje odgovore." Oba chatbota postavila su tačno pet pitanja vezanih za taj posao. Gemini je, naprimjer, pitao za iskustvo s urudžbiranjem dokumenata. Razlika, dakle, nije u tome da li model pita, nego šta pita.

## Prvi odgovor je nacrt

Prvi odgovor rijetko je i konačan. Google i Microsoft savjetuju da odgovor dorađujete kroz razgovor: "kraće", "formalnije", "dodaj primjer iz BiH". Microsoft navodi da većina korisnika tako i radi i da isti prompt može dati različite rezultate.

Veće zadatke podijelite na manje dijelove, kako izričito savjetuje Google. Prvo zatražite plan seminarskog rada, zatim uvod, pa svako poglavlje zasebno. Tako svaki korak možete provjeriti prije nego pređete na sljedeći.

## Česte zablude

**Uloga koju dodijelite modelu ne čini odgovor nužno tačnijim.** Google u svojim savjetima ulogu navodi na prvom mjestu ("Ti si iskusni ekonomista..."). [Zheng i saradnici](https://arxiv.org/abs/2311.10054v3) u radu iz 2024. testirali su 162 uloge na 2.410 činjeničnih pitanja i utvrdili da uloge nisu poboljšale rezultate u odnosu na prompt bez uloge. Uloga može promijeniti ton, ali su dokazi da utiče na tačnost slabi.

**"Razmisli korak po korak" više nije univerzalni trik.** [Kojima i saradnici](https://arxiv.org/abs/2205.11916v4) pokazali su da ta rečenica podiže tačnost na računskim zadacima sa 17,7 na 78,7 posto, ali na modelu iz 2022. godine. Za novije modele, koji prije odgovora sami prolaze kroz korake zaključivanja, OpenAI piše da je takva uputa nepotrebna i da ponekad može čak i odmoći.

**Dobar prompt ne garantuje tačan odgovor.** Gemini je na detaljan prompt o inflaciji naveo cijene u KM i predstavio ih kao stvarne. U istom odgovoru hljeb je prvo poskupio sa 1,00 na 1,80 KM, a zatim sa 1,50 na 1,80 KM. ChatGPT je bar naznačio da su njegove cijene izmišljene. U odgovorima je bilo i pravopisnih grešaka. Modeli i dalje mogu izmišljati podatke, a ta pojava naziva se [halucinacija](/rjecnik/halucinacija/). I Microsoft upozorava da Copilot može pogriješiti i da njegove odgovore treba provjeriti.

## Prompt koji možete kopirati

Popunite uglaste zagrade i obrišite redove koji vam ne trebaju:

```
Piši na bosanskom jeziku, ijekavicom, latinicom.
Zadatak: [šta ti tačno treba da uradiš]
Za koga i zašto: [ko će ovo čitati i u kojoj situaciji]
Šta trebaš znati: [važne činjenice, ograničenja, budžet u KM]
Oblik: [tabela / spisak / email], najviše [broj] riječi, ton [kakav].
Ako ti nešto nedostaje, prvo mi postavi pitanja i sačekaj moje odgovore.
```

## Povezano

- [Šta je LLM i kako radi?](/clanci/sta-je-llm/) – šta se dešava s vašim promptom unutar modela.
- [Šta je LLM token i kako radi tokenizacija?](/clanci/sta-je-llm-token/) – zašto isti tekst na bosanskom troši više tokena nego na engleskom.

## Izvori

- [Prompting best practices – Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Multilingual support – Anthropic](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)
- [Reasoning best practices – OpenAI](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- [Tips to write prompts for Gemini – Google](https://support.google.com/a/users/answer/14200040)
- [Manage what Gemini remembers about you and customize responses – Google](https://support.google.com/gemini/answer/16598625)
- [Large Language Models are Zero-Shot Reasoners – Kojima i saradnici](https://arxiv.org/abs/2205.11916v4)
- [When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models – Zheng i saradnici, Findings of EMNLP 2024](https://arxiv.org/abs/2311.10054v3)
