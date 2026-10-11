---
layout: post
title: "Šta je kontekstni prozor i zašto LLM zaboravlja?"
date: 2026-10-11
category: vodici
image: /assets/images/2026-10-11-sta-je-kontekstni-prozor.svg
read_time: 6
description: "Šta sve ulazi u kontekstni prozor, zašto je ograničen, zašto model slabije koristi sredinu prozora i zašto na bosanskom u isti prozor stane manje teksta."
tags: [llm]
---

Recimo da u prvoj poruci dugog razgovora s chatbotom napišete da imate budžet od 2.000 KM. Nekoliko desetina poruka kasnije model predloži rješenje koje taj budžet zanemaruje. Model nije zaboravio onako kako zaboravlja čovjek. Sve što model u datom trenutku vidi nalazi se u njegovom [kontekstnom prozoru (context window)](/rjecnik/kontekstni-prozor/). Taj prozor je ograničen, a model ga ne koristi jednako dobro od početka do kraja.

## Ukratko

Kontekstni prozor je sav tekst koji model uzima u obzir dok generiše odgovor: upute aplikacije, poruke, priloženi dokumenti, rezultati alata i sam odgovor. Mjeri se u [tokenima](/rjecnik/token/) (osnovnim jedinicama teksta koje model obrađuje – riječima ili dijelovima riječi). Ograničen je, između ostalog, zato što količina računanja u mehanizmu pažnje raste s kvadratom dužine teksta. Šta se dešava kad se prozor napuni zavisi od proizvođača: model može vratiti grešku, prekinuti odgovor, izbaciti najstarije poruke ili raniji dio razgovora zamijeniti sažetkom. Kvalitet opada i prije nego što se prozor napuni. U testovima su modeli bolje koristili informacije s početka i kraja nego one iz sredine. Bosanskog teksta u isti prozor stane manje nego engleskog.

## Šta sve ulazi u kontekstni prozor?

Kontekstni prozor možete zamisliti kao radnu memoriju [velikog jezičkog modela (large language model, LLM)](/rjecnik/veliki-jezicki-model/). To nije isto što i tekst na kojem je model treniran. Prema dokumentaciji [Anthropica](https://platform.claude.com/docs/en/build-with-claude/context-windows) i [OpenAI-ja](https://developers.openai.com/api/docs/guides/conversation-state), u prozor se računaju:

- sistemski [prompt](/rjecnik/prompt/) (system prompt), odnosno upute koje aplikacija daje modelu prije nego što razgovor počne;
- sve poruke u razgovoru, i vaše i odgovori modela;
- priloženi dokumenti i slike;
- rezultati alata, npr. pretraživanja weba;
- opisi alata koje model smije koristiti;
- sam odgovor, uključujući zaključivanje (reasoning) koje neki modeli generišu prije konačnog odgovora.

Sve se to mjeri u tokenima, a ne u riječima ili stranicama.

## Kako funkcioniše

Veliki jezički modeli zasnivaju se na arhitekturi koja se zove [transformer](/rjecnik/transformer/). Njena osnova je mehanizam pažnje (attention mechanism): za svaki token model procjenjuje koliko su za njega važni svi ostali tokeni u prozoru. [Vaswani i saradnici](https://arxiv.org/abs/1706.03762v7), autori rada u kojem je predstavljen transformer, navode da je računska složenost tog koraka po sloju srazmjerna n²·d. Pri tome je `n` broj tokena, a `d` veličina interne reprezentacije svakog tokena. Kad je tekst dvostruko duži, ovaj dio modela ima oko četiri puta više računanja. 

Zato prozor ima gornju granicu. GPT-3 je imao prozor od 2.048 tokena ([Brown i saradnici](https://arxiv.org/abs/2005.14165v4)). U oktobru 2026. proizvođači za aktuelne modele Claude i GPT navode prozore od oko milion tokena. To je deklarisani kapacitet. Ne znači da model cijeli prozor koristi jednako dobro.

## Šta se dešava kad se prozor napuni?

To zavisi od proizvođača:

- Anthropic vraća grešku ("prompt is too long") ako već sam ulaz duži od prozor. Kod Claude modela od verzije 4.5 naovamo generisanje odgovora staje kad dosegne granicu.
- Chat aplikacije poput claude.ai mogu same upravljati prozorom tako što izbacuju najstarije poruke.
- OpenAI navodi da se tokeni preko granice mogu odsjeći.

Oba proizvođača nude i sažimanje (compaction): raniji dijelovi razgovora zamjenjuju se sažetkom da bi se oslobodio prostor. To je jedno moguće objašnjenje primjera s početka: ako aplikacija izbaci najstarije poruke, budžet iz prve poruke više nije u prozoru i model ga ne vidi. Postoji i drugo objašnjenje, koje važi čak i kad prozor nije ni blizu pun.

## Zašto model zaboravlja i prije nego što se prozor napuni?

Anthropic u dokumentaciji piše da s rastom broja tokena opadaju tačnost i sposobnost prisjećanje. [Chroma](https://www.trychroma.com/research/context-rot), kompanija koja prodaje infrastrukturu za pretraživanje, testirala je 18 modela na zadacima iste težine. Prema njenim rezultatima, modeli su sve nepouzdaniji što je ulaz duži.

Drugi efekt zavisi od toga gdje se informacija nalazi u prozoru. Izmjerio ga je rad ["Lost in the Middle"](https://arxiv.org/abs/2307.03172v3) Liua i saradnika sa Stanforda, Berkeleyja i iz kompanije Samaya AI. Testirali su modele iz 2023, među njima GPT-3.5-Turbo i Claude-1.3. Model je dobijao pitanje i 20 dokumenata, a istraživači su mijenjali poziciju dokumenta u kojem je odgovor.

{% include diagram.html name="sta-je-kontekstni-prozor" caption="GPT-3.5-Turbo s 20 dokumenata: kad je odgovor u sredini, tačnost pada ispod rezultata bez ijednog dokumenta (Liu i saradnici, 2023)." alt="Stubičasti dijagram tačnosti GPT-3.5-Turbo prema poziciji dokumenta s odgovorom: 1. pozicija 75,8%, 5. 57,2%, 10. 53,8%, 15. 55,4%, 20. 63,2%. Isprekidana linija na 56,1% označava tačnost bez ijednog dokumenta." %}

| Pozicija dokumenta s odgovorom | Tačnost GPT-3.5-Turbo |
|---|---|
| 1. | 75,8% |
| 5. | 57,2% |
| 10. | 53,8% |
| 15. | 55,4% |
| 20. | 63,2% |
| bez ijednog dokumenta | 56,1% |

Rezultati čine krivu u obliku slova U. Model najbolje koristi informacije s početka i kraja, a najslabije one iz sredine. Kad je odgovor bio u sredini, GPT-3.5-Turbo je odgovarao lošije nego kad nije dobio nijedan dokument i oslanjao se samo na ono što je naučio tokom treniranja. Verzije modela s proširenim prozorom ponašale su se gotovo isto kao osnovne.

Kriva nije jednako izražena kod svih modela. Kod Claude-1.3 bila je gotovo ravna: 59,9% na prvoj poziciji, 56,8% na desetoj i 60,1% na dvadesetoj.

## Koliko prozora model zaista koristi?

Deklarisana dužina konteksta je dužina koju navodi proizvođač. Efektivna dužina konteksta (effective context length) je dužina do koje model na testu još radi pouzdano. Jedan od testova kojima se ona mjeri je benchmark (referentni test) [RULER](https://arxiv.org/abs/2404.06654v3), koji su objavili istraživači iz NVIDIA-e.

Na RULER-u je testirano 17 modela. Svi deklarišu najmanje 32K (oko 32 hiljade tokena), ali na toj dužini samo polovina prelazi prag. Prag iznosi 85,6%, što je rezultat modela Llama2-7B na 4K. Autori su taj prag izabrali kao referencu, pa efektivna dužina zavisi i od tog izbora.

| Model | Deklarisano | Efektivno (RULER) |
|---|---|---|
| GPT-4 | 128K | 64K |
| GLM4 | 1M | 64K |
| LWM | 1M | manje od 4K |

Gemini-1.5-Pro je ostao iznad praga i na 128K, najvećoj dužini koju je RULER testirao. RULER je objavljen 2024. i mjerio je tadašnje modele.
Nezavisna mjerenja efektivne dužine za današnje modele s najvećim prozorima nismo provjerili.

## Zašto na bosanskom stane manje teksta?

Prozor se mjeri u tokenima, a isti tekst na različitim jezicima troši različit broj tokena. [Petrov i saradnici](https://arxiv.org/abs/2305.15425v2) izmjerili su da tokenizator cl100k_base, koji su ChatGPT i GPT-4 koristili 2023, za iste rečenice treba 1,87 puta više tokena na bosanskom nego na engleskom. To znači da u isti prozor stane samo oko 53% teksta na bosanskom u odnosu na engleski. Autori kao jednu od posljedica navode upravo manji iskoristivi kontekst. Ovaj podatak odnosi se na tokenizator iz 2023. i ne mora važiti za današnje.

## Praktične implikacije

- U testovima iz 2023. modeli su najbolje koristili početak i kraj teksta. Najvažnije podatke stavite na početak ili kraj prompta, a ključni uslov ne zakopavajte u sredinu dugog teksta.
- Kad se razgovor oduži ili skrene na drugu temu, započnite novi. Na početku navedite sve što model mora znati.
- Ne lijepite cijeli dokument ako vam treba samo jedan njegov dio. Za velike zbirke dokumenata često se koristi generisanje potpomognuto pretraživanjem (retrieval-augmented generation, RAG): sistem pronađe relevantne dijelove i u prozor ubaci samo njih.
- Na bosanskom računajte s manje prostora nego što pokazuje deklarisana brojka.

## Šta NIJE

- **Kontekstni prozor nije znanje modela.** Ono što je model naučio ranije ne zauzima prozor. Prozor sadrži samo ono što je ubačeno u taj poziv.
- **Prozor nije trajna memorija.** Ono što ispadne iz prozora model u tom razgovoru više ne vidi.
- **Veći prozor ne znači bolje razumijevanje dugog teksta.** GLM4 i LWM deklarišu 1M tokena, a na RULER-u pouzdano rade na 64K, odnosno ispod 4K.
- **Nije svejedno gdje je informacija.** U testovima iz 2023. ista informacija na početku i u sredini prozora nije davala isti rezultat.

## Povezano

- [Šta je LLM i kako radi?](/clanci/sta-je-llm/) – kako model generiše tekst token po token, osnova za ovaj tekst.
- [Šta je token](/clanci/sta-je-llm-token/) – jedinica u kojoj se prozor mjeri.
- [Kako napisati dobar prompt: recite chatbotu jezik, situaciju i oblik odgovora](/clanci/kako-napisati-dobar-prompt/) – kako jasno navesti jezik i uslove koje model treba poštovati.

## Izvori

- [Context windows – Anthropic, Claude dokumentacija](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Conversation state – OpenAI, API dokumentacija](https://developers.openai.com/api/docs/guides/conversation-state)
- [Lost in the Middle: How Language Models Use Long Contexts – Liu et al., arXiv v3](https://arxiv.org/abs/2307.03172v3)
- [RULER: What's the Real Context Size of Your Long-Context Language Models? – Hsieh et al., NVIDIA, COLM 2024](https://arxiv.org/abs/2404.06654v3)
- [Language Models are Few-Shot Learners – Brown et al., OpenAI](https://arxiv.org/abs/2005.14165v4)
- [Attention Is All You Need – Vaswani et al., Google](https://arxiv.org/abs/1706.03762v7)
- [Context Rot – Chroma, 14. juli 2025.](https://www.trychroma.com/research/context-rot)
- [Language Model Tokenizers Introduce Unfairness Between Languages – Petrov et al.](https://arxiv.org/abs/2305.15425v2)
