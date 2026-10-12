---
layout: post
title: "LLM Wiki: agent vodi bazu znanja, vi birate izvore"
date: 2026-10-11
category: ai-u-praksi
image: /assets/images/2026-10-11-karpathy-llm-wiki.svg
read_time: 7
description: "Karpathyjev LLM Wiki: agent od vaših izvora gradi i održava wiki. Kako obrazac funkcioniše, koliko wiki može narasti, gdje zapinje i šta vam treba za početak."
tags: [ai-agenti]
---

Ko god skuplja članke i bilješke, zna kako to obično završi: folder je pun materijala, a kad vam zatreba odgovor, sve čitate ispočetka. Slično je i s chatbotom kojem date dokumente: svako pitanje ponovo kreće od istih sirovih tekstova. Andrej Karpathy je u aprilu 2026. opisao drugačiji pristup i nazvao ga LLM Wiki. [Agent](/rjecnik/agent/) zasnovan na [velikom jezičkom modelu (large language model, LLM)](/rjecnik/veliki-jezicki-model/) od vaših izvora sam gradi i održava wiki. Tako se znanje vremenom nakuplja, umjesto da ga za svako pitanje iznova otkrivate.

## Ukratko

LLM Wiki je obrazac koji je Andrej Karpathy objavio u aprilu 2026. Agent čita izvore koje mu date i na osnovu njih piše i održava wiki, odnosno skup međusobno povezanih Markdown stranica. Vi dodajete izvore i postavljate pitanja, a agent ažurira stranice i poveznice. Pravila rada zapisana su u posebnom fajlu. Prema Karpathyju, pristup dobro radi dok je baza umjerene veličine: oko 100 izvora i nekoliko stotina stranica. Jedan praktičar koji ga je primijenio na wiki od nekoliko stotina stranica naveo je zastarjele odjeljke, kontradikcije koje niko nije primijetio i indeks koji je prerastao [kontekstni prozor (context window)](/rjecnik/kontekstni-prozor/).

## Šta je LLM Wiki

Karpathy je 2. aprila 2026. u objavi na mreži X opisao kako vodi svoju bazu znanja (knowledge base). Nedugo zatim na GitHubu je objavio kratak tekst llm-wiki.md. To nije program, nego opis ideje koji zalijepite u agenta, npr. Codex, Claude Code ili OpenCode. Karpathy kaže da je tekst "namjerno apstraktan": kako će ideja izgledati u praksi, odlučuje vaš agent.

U ovom obrascu wiki je skup Markdown fajlova, odnosno običnog teksta s jednostavnim oznakama za naslove i poveznice. Prema Karpathyju, wiki nije ništa drugo nego skup takvih fajlova, pa ga možete čuvati u Gitu. Za čitanje preporučuje Obsidian, a podjelu uloga objašnjava poređenjem s programiranjem: Obsidian je alat u kojem programer pregleda kod, LLM je programer, a wiki je sam kod.

Zašto bi to uopšte funkcionisalo, Karpathy objašnjava jednom rečenicom: "Zamorni dio održavanja baze znanja nije čitanje ni razmišljanje – nego vođenje evidencije." (*"The tedious part of maintaining a knowledge base is not the reading or the thinking – it's the bookkeeping."*) Prema njegovom prijedlogu, taj dio preuzima agent.

## Kako funkcioniše

Obrazac ima tri sloja:

- **Izvori (raw sources).** Članci, bilješke i drugi dokumenti koje ste prikupili. Karpathy piše da su oni "nepromjenjivi – LLM ih čita, ali ih nikad ne mijenja".
- **Wiki.** Markdown stranice koje generiše LLM i koje, kako piše Karpathy, LLM "u potpunosti posjeduje". Vi ih čitate, a agent ih piše.
- **Pravilnik (schema).** Dokument sa stalnim pravilima kojih se agent drži, npr. CLAUDE.md za Claude Code ili AGENTS.md za Codex. "Vi i LLM ga s vremenom zajedno razvijate", piše Karpathy.

Uz to postoje i dva posebna fajla. Indeks (index.md) je katalog wikija i agent ga čita prvi. Dnevnik (log.md) je zapis u koji se samo dodaje, a ništa se ne briše. Karpathy navodi ovakav primjer zapisa: `## [2026-04-02] ingest | Article Title`.

Agent nad ovim slojevima izvodi tri operacije:

**Unos (ingest).** Dodate novi izvor, a agent ga obradi i ažurira wiki. "Jedan izvor može zahvatiti 10–15 wiki stranica", piše Karpathy. On sam radije unosi izvore jedan po jedan, jer, kako kaže, unos više izvora odjednom znači manje nadzora.

**Upit (query).** Postavite pitanje, a agent odgovara na osnovu wikija. Prema Karpathyju, dobri odgovori mogu se "vratiti u wiki kao nove stranice". Tako i vaša pitanja postaju dio baze znanja.

**Provjera (lint).** Povremeni pregled stanja wikija. Agent traži kontradikcije među stranicama, zastarjele tvrdnje, stranice bez poveznica (orphan pages), pojmove koji još nemaju svoju stranicu, poveznice koje nedostaju i praznine u podacima.

Karpathyjev tekst ne sadrži gotove promptove (upute koje dajete modelu). Evo kako bi naredbe agentu mogle izgledati. Primjeri su naši, ne Karpathyjevi:

> Unesi izvor izvori/solarni-paneli.md. Ažuriraj stranice koje se tiču te teme i dodaj zapis u log.md.

> Provjeri wiki. Napravi spisak kontradikcija i stranica bez poveznica.

{% include diagram.html name="karpathy-llm-wiki" caption="LLM Wiki prema Karpathyjevom opisu: agent čita izvore, drži se pravilnika i kroz tri operacije piše i održava wiki." alt="Dijagram: izvori, koje agent samo čita, i pravilnik (CLAUDE.md ili AGENTS.md) ulaze u agenta. Agent izvodi tri operacije: unos (novi izvor ažurira 10–15 wiki stranica), upit (dobri odgovori postaju nove stranice) i provjeru (kontradikcije, zastarjele tvrdnje, stranice bez poveznica). Agent piše wiki s indeksom (index.md) i dnevnikom (log.md), a pri upitu čita wiki, počevši od indeksa." %}

## Koliko velik može biti wiki?

Čvrsta granica ne postoji. Karpathy piše da pristup s indeksom "iznenađujuće dobro radi na umjerenoj veličini (~100 izvora, ~stotine stranica)". Na toj veličini, dodaje, nije potrebna infrastruktura za generisanje potpomognuto pretraživanjem (retrieval-augmented generation, RAG) zasnovana na [embeddingu](/rjecnik/embedding/). Međutim, "kako wiki raste, treba vam prava pretraga". Prema objavi na X-u, njegov wiki ima oko 100 članaka i oko 400.000 riječi, a on to smatra malim obimom.

To ne znači da RAG više nije potreban. Karpathy govori o umjerenoj veličini, a ne o bilo kojoj.

## Gdje zapinje

Karpathy i sam priznaje dva ograničenja. Prvo, unos više izvora odjednom znači manje nadzora. Drugo, jezički modeli, kako piše, ne mogu izvorno, u jednom prolazu, pročitati Markdown sa slikama umetnutim u tekst. Svoju postavku ne predstavlja ni kao uglađen alat: na X-u je naziva "improvizovanom kolekcijom skripti".

Michael Tuszynski je u augustu 2026. objavio izvještaj o tome kako je obrazac primijenio na wiki od nekoliko stotina stranica. Naveo je sljedeće probleme:

- Odjeljci s referencama vremenom zastarijevaju.
- Kontradikcije prolaze neprimijećeno: "dvije stranice postoje, svaka je sama po sebi dosljedna, i nijedna ne zna za drugu".
- Stranice bez poveznica i poveznice koje ne vode nikamo promaknu provjeri ako se ona radi rijetko.
- Ništa ne sprečava više agenata da istovremeno mijenjaju wiki.
- Indeks više ne staje u kontekstni prozor kad aktivni sadržaj dostigne oko 100.000 tokena (token je osnovna jedinica teksta koju model obrađuje – riječ ili dio riječi).
- Bez pravilnika čovjek teško prati konvencije po kojima je wiki uređen.

Zato dvije Karpathyjeve tvrdnje treba uzeti s rezervom. Prva je da je trošak održavanja "gotovo nula". Ta procjena ne uključuje tokene koje agent troši ni vrijeme koje provedete provjeravajući njegov rad. Druga je da se modeli "ne dosađuju" i ne zaboravljaju ažurirati poveznicu. Tuszynskijevo iskustvo govori suprotno, iako je riječ o iskustvu samo jednog praktičara.

## Šta treba za početak?

Treba vam agent koji može čitati i pisati fajlove u folderu na vašem računaru. Na raspolaganju su:

- **Claude Cowork** (u aplikaciji Claude Desktop). Čita i piše samo u "folderima koje ste povezali, kroz desktop aplikaciju, i samo dok je otvorena". Dostupan je na planovima Pro i Max. Verzija u oblaku je u beta fazi za planove Team i Enterprise.
- **ChatGPT/Codex desktop aplikacija** (macOS, Windows, Linux). Prema OpenAI-ju, "može koristiti fajlove i kontekst s lokacije koju izaberete". Izvor ne navodi koji su planovi potrebni.
- **Claude Code, Codex i OpenCode**, agenti koje Karpathy spominje. U tom obliku pokreću se kucanjem naredbi.
- **Obsidian** za čitanje wikija. Nije obavezan, jer su stranice obični tekstualni fajlovi.

Iz dostupnih izvora nije jasno nekoliko stvari: mogu li agenti na besplatnim planovima pisati u fajlove, koji su planovi potrebni za ChatGPT i čitaju li desktop aplikacije pravilnik same, kao što to rade agenti koji se pokreću naredbama. Naš savjet: ako niste sigurni, na početku rada recite agentu da pročita pravilnik.

Iz opisanih slabosti proizlaze prva tri praktična pravila, a četvrto je naša preporuka:

- Izvore držite u zasebnom folderu i ne dozvolite agentu da ih mijenja.
- Unosite izvore jedan po jedan, barem dok ne vidite kako agent radi.
- Provjeru radite redovno, a ne tek kad nešto zapne.
- Čitajte stranice koje agent piše. Wiki je pouzdan onoliko koliko ga pregledate.

## Šta NIJE

- **Nije gotov program.** Karpathyjev tekst je opis ideje, a izvedba je prepuštena vašem agentu. Čak je i njegova vlastita postavka, kako sam kaže, kolekcija skripti.
- **Nije zamjena za pretragu velikih razmjera.** Karpathy kaže da pristup s indeksom dobro radi na umjerenoj veličini, a za veći wiki i sam savjetuje pravu pretragu.
- **Ne održava se sam od sebe i besplatno.** Agent troši tokene, a kontradikcije i mrtve poveznice ne nestaju same od sebe.
- **Nije razgovor s chatbotom.** Znanje ne ostaje zarobljeno u jednom razgovoru, nego u fajlovima koje možete čitati i bez ikakvog AI alata.

## Povezano

- [Šta je AI agent i kako radi?](/clanci/sta-je-ai-agent/) – o vrsti sistema koji u ovom obrascu piše i održava wiki.
- [Šta je kontekstni prozor i zašto LLM zaboravlja?](/clanci/sta-je-kontekstni-prozor/) – zašto indeks u nekom trenutku više ne stane u model.
- [Kako napisati dobar prompt: jezik, situacija, oblik odgovora](/clanci/kako-napisati-dobar-prompt/) – stalne upute u chatbotu imaju sličnu ulogu kao pravilnik.

## Izvori

- [llm-wiki.md – Andrej Karpathy, GitHub Gist, april 2026.](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [LLM Knowledge Bases – Andrej Karpathy, objava na X-u, 2. april 2026.](https://x.com/karpathy/status/2039805659525644595)
- [Izvještaj o primjeni LLM Wikija na većoj skali – Michael Tuszynski, mpt.solutions, 13. august 2026.](https://www.mpt.solutions/karpathys-llm-wiki-works-heres-what-broke-when-i-ran-it-at-real-scale/)
- [Claude Cowork, pristup fajlovima – Claude Help Center](https://support.claude.com/en/articles/15520349-use-cowork-on-web-desktop-and-mobile)
- [ChatGPT i Codex desktop aplikacija – OpenAI](https://learn.chatgpt.com/docs/app)
