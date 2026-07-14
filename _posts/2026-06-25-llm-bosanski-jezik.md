---
layout: post
title: "Zašto LLM-ovi loše rade na bosanskom - i šta možete učiniti"
date: 2026-06-28
category: vodici
audience: developers
read_time: 13
description: "Ako gradite softver za bosanskogovornu publiku i koristite LLM API-je, vaš model troši 1,8 do 2,5 puta više tokena po bosanskoj riječi nego po engleskoj - i to je samo početak problema."
diagram: /assets/diagrams/llm-bosanski-jezik.svg
image: /assets/images/2026-06-25-llm-bosanski-jezik.svg
---

Ako gradite softver za bosanskogovornu publiku i koristite LLM API-je, vaš model troši 1,8 do 2,5 puta više tokena po bosanskoj riječi nego po engleskoj. To znači veći račun, sporija inferencija, i kraći efektivni kontekst - a to je problem koji se pojavljuje i prije nego što uopće počnete mjeriti kvalitet odgovora.

Degradacija kvaliteta je realna i mjerljiva. Bosanski je jezik s malo resursa (low-resource language) - podzastupljen i u trening podacima velikih modela i u samom tokenizeru. U ovom tekstu prolazimo kroz mehanike oba problema i šta možete s tim kao developer.

---

## Trošak tokenizacije (tokenization)

Svaki poziv LLM API-ju naplaćuje se po tokenima. Token nije riječ - to je podriječ (subword), fragment koji tokenizer BPE algoritmom izvlači iz teksta. Tokenizeri trenirani na engleskom tekstu nauče da česte engleske kombinacije slova čine jedan token. Bosanski, sa sedam morfoloških padeža, gramatičkim rodom i bogatom glagolskom konjugacijom, proizvodi oblike koje BPE tokenizer nije vidio dovoljno puta da bi ih naučio kao cjelinu. Rezultat: svaka bosanska fleksijska forma se fragmentira u više podriječi.

Fertilnost (fertility) tokenizera - broj tokena po riječi - kvantificira ovaj efekat direktno. Occiglot evaluacija je izmjerila fertilnost za nekoliko modela na hrvatskom i srpskom (za bosanski nema posebnih mjerenja; hrvatski je najbliži dostupni proxy zbog identičnog pisma i gotovo identične morfologije):

| Jezik | Mistral 7B | Llama | Phi | Gemma |
|---|---|---|---|---|
| Hrvatski | 2,48 | 2,39 | 2,66 | 2,08 |
| Srpski | 2,41 | 2,02 | **5,84** | 2,11 |
| Engleski (ref.) | ~1,42 | ~1,42 | ~1,50 | ~1,40 |

*Izvor: Occiglot EU tokenizer evaluation*

Phi tokenizer pokazuje ekstremnu degradaciju na srpskom (5,84) zbog nedosljednog tretmana ćirilice. Gemma, sa rječnikom od 256.000 tokena nasuprot 32.000 kod Mistrala i Llame, postiže fertilnost ~2,08–2,11 za južnoslavenske jezike - najniži od svih testiranih tokenizera.

"Tokenizer Tax" studija (arXiv 2605.24718, 2026) mjeri srednju fertilnost za hrvatski na 2,31 tokena po riječi naspram 1,23 za engleski - **1,88× veći trošak**. Konkretno u praksi: poziv koji na engleskom koristi 1.000 tokena konteksta na bosanskom troši ~1.880 tokena za isti informacijski sadržaj. U modelu s kontekstnim prozorom od 128k tokena to znači efektivno korisni kontekst od ~68k tokena za bosanski tekst. Faktor troška inferencije je proporcionalan.

### Primjer fragmentacije

Engleski glagol "work" ostaje jedan token: `work`. Bosanska paradigma istog pojma razbija se na fragmente:

```
"raditi"   → ["rad", "iti"]
"radi"     → ["rad", "i"]  
"radimo"   → ["rad", "imo"]
"radićemo" → ["rad", "ić", "emo"]
```

Svaka infleksija producira drugačiji skup podriječi - model ne vidi morfološku vezu između oblika na isti način na koji je vidi za engleski, gdje su oblici malobrojniji i zastupljeniji u trening podacima.

{% include diagram.html name="llm-bosanski-jezik" caption="Isti glagol, četiri oblika - svaki bosanski oblik producira 2–3 tokena tamo gdje engleski producira jedan." alt="Animirani dijagram: engleski glagolski oblici work/works/worked/working svaki ostaje jedan token; bosanski oblici raditi/radi/radimo/radićemo fragmentiraju se u 2–3 podriječi." %}

---

## Jaz u trening podacima

Tokenizacija je vidljiv simptom; pravi uzrok je strukturni nedostatak BCS podataka u pre-trainingu (prethodno treniranje) velikih modela.

Llama 2 data card dokumentuje engleski na 89,7% pre-trening tokena. Ruski - najzastupljeniji slavenski jezik - procjenjuje se na 0,13–0,53%. Hrvatski i srpski nisu navedeni kao zasebne kategorije u Llama 2 data cardu. Za bosanski nema dokumentirane zastupljenosti.

Za modele poslije Llame 2 - GPT-4o, Claude 3.5, Llama 3 - precizne proporcije po jeziku nisu javno objavljene. Trend se vjerovatno poboljšava s uključivanjem Common Crawl podataka iz šire regije, ali mjerljivi podaci ne postoje.

Šta ovaj jaz znači u praksi:

- **Zaključivanje (reasoning):** Model koji je vidio milion puta engleskih primjera logičkih lanaca vidio je tek djelić ekvivalentnih BCS primjera. Strukturni obrasci zaključivanja naučeni su primarno na engleskom.
- **Praćenje uputa:** Fino podešavanje (fine-tuning) za praćenje uputa koristi pretežno engleski RLHF data. Bosanski promptovi aktiviraju tu sposobnost manje pouzdano.
- **Faktografija:** Modeli generirani iz pre-training podataka imaju manje izloženosti bosanskim izvorima i kontekstu regije, što se manifestuje u lošijem faktografskom pokriću lokalnih tema.

---

## Što pokazuje istraživanje

### Interne reprezentacije

Direktan pokazatelj koliko dobro model razumije jezik je kosinusna sličnost između embedding vektora istih pojmova na tom jeziku i na engleskom. Studija "Quantifying Multilingual Performance of Large Language Models" (arXiv 2404.11553) mjeri:

- LLaMA 2 7B: srpsko-engleska sličnost = **0,555**
- Mistral 7B: srpsko-engleska sličnost = **0,408**
- Qwen 7B: srpsko-engleska sličnost = **0,588**

Za visoko zastupljene jezike te vrijednosti dosežu 0,7–0,8. Framing koji ponekad cirkulira - da modeli "interno prevode u engleski" - nije precizan. Tačnija slika je da je geometrija reprezentacijskog prostora biasirana prema engleskom: BCS koncepti su mapirani u susjedstvo koje je strukturirano engleskim trening signalom, a ne da se odvija eksplicitni prijevod. Praktična posljedica je ista - model se oslanja na engleske obrasce tamo gdje bi trebao koristiti BCS-specifičnu strukturu - ali mehanika je drugačija.

### YugoGPT

YugoGPT je Mistral 7B fino podešen na desetinama milijardi HBS (hrvatsko-bosansko-srpskih) tokena, objavljen pod Apache 2.0 licencom. Prema evaluaciji autora na Serbian LLM Eval benchmarku (Hellaswag, Winogrande, PIQA, ARC, OpenbookQA), YugoGPT "značajno nadmašuje" Mistral 7B i Llama 2 7B na zadacima zaključivanja u srpskom. Precizne delta vrijednosti iz W&B izvještaja nisu javno dostupne. Ovo je snažan dokaz zajednice, ali nije recenzirani akademski rad - tretirati ga kao takav.

### BERTić

BERTić (Ljubešić & Lauc 2021, arXiv 2104.09243) je ELECTRA model treniran na 8+ milijardi BCS tokena. Na POS tagiranju, NER-u, geolokaciji i COPA-HR benchmarku (65,76%) nadmašuje multilingualni BERT. Ovo je recenzirani rad koji potvrđuje vrijednost BCS-specifičnog treninga za klasifikacijske zadatke. Važna napomena: parity ili superiornost na klasifikaciji ne znači parity na generativnim zadacima - ne generalizirati.

### Few-shot prompting na slavenskim jezicima

ACL 2023 studija "Resources and Few-shot Learners for In-context Learning in Slavic Languages" (arXiv 2304.01922) pokazuje da few-shot (mali broj primjera) pristup poboljšava performanse na slavenskim jezicima; 1–4 primjera nadmašuje pristupe bazirane na prevodu za sumarizaciju i klasifikaciju. Međutim, u specijaliziranim domenama few-shot primjeri mogu degradirati performanse - efekt je task-dependent.

---

## Mitigacije: što stvarno pomaže

Evo praktičnog rangiranja strategija prema kvalitetu dokaza:

### 1. Izbor tokenizera / modela (objavljeni dokazi)

Gemma tokenizer (256k rječnik) konzistentno postiže najnižu fertilnost za južnoslavenske jezike od svih testiranih tokenizera. Phi je aktivan problem za srpsku ćirilicu (fertilnost 5,84). Za aplikacije gdje je trošak tokena bitan faktor ili gdje radite sa ograničenim kontekstnim prozorom, izbor baznog modela s većim rječnikom direktno utiče na trošak i kapacitet.

```python
# Fertilnost ~2.08 za BCS
model = "google/gemma-2-9b-it"   # 256k rječnik

# Fertilnost 2.39–2.48 za BCS  
model = "mistralai/Mistral-7B-Instruct-v0.3"  # 32k rječnik

# IZBJEGAVATI za srpsku ćirilicu
model = "microsoft/phi-2"  # fertilnost 5.84 na srpskom
```

### 2. BCS-specifični modeli (objavljeni dokazi)

Za zadatke gdje je kvalitet odgovora na BCS kritičan, a ne samo engleski output:

- **YugoGPT** (`gordicaleksa/YugoGPT` na HuggingFace) - za generativne zadatke, open-source, Apache 2.0. Bazira se na Mistral 7B; deployment zahtijeva self-hosted setup.
- **BERTić** - za klasifikaciju, NER, POS tagging. Pouzdan akademski benchmark za te zadatke. Ne koristiti za generativne zadatke.

Oba modela zahtijevaju self-hosted deployment - nisu dostupni kao managed API.

### 3. Engleski promptovi za zadatke zaključivanja (objavljeni dokazi, indirektni)

Istraživanje na arapskom (arXiv 2409.07054) pokazuje da engleski promptovi nadmašuju native promptove na zadacima zaključivanja. Mješoviti promptovi - upute na nativnom jeziku, labele na engleskom - nadmašuju čisto native promptove za 7–8% u nekim postavkama. Direktnih BCS dokaza nema, ali mehanički razlog je isti: geometrija reprezentacijskog prostora biasirana je prema engleskom.

Praktičan obrazac:

```python
# Za reasoning-heavy zadatke: engleski sistem prompt
system = "You are a helpful assistant. Respond in Bosnian."
user = "Analyze the following contract clause and identify risk factors: ..."

# Vs. sve na bosanskom - može biti lošije za složeno zaključivanje
system = "Ti si pomoćni asistent."
user = "Analiziraj sljedeću klauzulu ugovora i identifikuj faktore rizika: ..."
```

Ovo nije preporuka da korisnicima servira engleski - to je preporuka za interni prompt dizajn gdje kontrolirate koji dio ide modelu na kom jeziku.

### 4. Few-shot primjeri na ciljnom jeziku (objavljeni dokazi, task-dependent)

Few-shot primjeri u BCS nadmašuju pristupe bazirane na prevodu za sumarizaciju i klasifikaciju. Optimalni broj je 1–4 primjera; više ne garantira bolje rezultate i može naškoditi u specijaliziranim domenama.

```python
# Few-shot obrazac za ekstrakciju iz bosanskog teksta
examples = [
    {
        "input": "Ugovor je potpisan 15. Januara 2026. između firme Alfa d.o.o. i firme Beta d.d.",
        "output": '{"datum": "2026-01-15", "strane": ["Alfa d.o.o.", "Beta d.d."]}'
    },
    {
        "input": "Sporazum od 3. Marta 2025. između Gamme S.A. i Delte GmbH.",
        "output": '{"datum": "2025-03-03", "strane": ["Gamma S.A.", "Delta GmbH"]}'
    }
]
```

### 5. Prijevod ulaza → obrada na engleskom → prijevod izlaza (praksa zajednice)

Smanjuje tokenizacijski overhead i aktivira engleske sposobnosti zaključivanja. Slabosti: greške pri prijevodu se kumuliraju u oba smjera, a za kulturno-specifičan sadržaj (regionalni kontekst, lokalni zakoni, idiomi) prijevod uvodi vlastite greške. Dokazi za ovaj pristup su indirektni - nema direktnih BCS studija koje ga porede s native-language pristupom na generativnim zadacima.

### 6. Continued pre-training (nastavak pre-traininga) (istraživački pristup)

YugoGPT koristi ovaj pristup - continued pre-training (nastavak pre-traininga) Mistral 7B na desetinama milijardi HBS tokena, praćen fino podešavanjem. Nije praktično za API konzumente. Relevantno za timove koji deployaju self-hosted modele i imaju pristup dovoljnoj količini BCS podataka i GPU kapacitetu.

---

## Izbor modela: praktična tablica

| Scenarij | Preporuka | Razlog |
|---|---|---|
| API, opći zadaci na BCS | Gemma 2 9B/27B | Najniža fertilnost od managed modela |
| API, frontier kvalitet | Claude 3.5 / GPT-4o | Veći modeli kompenzuju dijelom; fertility i dalje viša nego za engleski, ali sposobnost nadoknađuje |
| Self-hosted, BCS generativni zadaci | YugoGPT (Mistral 7B) | Open 7B model treniran na HBS podacima; Apache 2.0 |
| Klasifikacija, NER, POS | BERTić | Jedini recenzirani BCS-specifični model za te zadatke |
| Izbjegavati za ćirilicu | Phi | Fertilnost 5,84 na srpskom - neopravdani trošak |

---

## Poštena ocjena stanja

Jaz je realan i kvantificiran na razini tokenizacije. Na razini trening podataka, direktni podaci za bosanski su skromni - dostupni su podaci za hrvatski i srpski koji su primjenjivi kao proxy, ali za bosanski-specifično pokriće nema objavljenih mjerenja za frontier modele.

Jedna kritična praznina ostaje: ne postoji objavljeni, recenzirani benchmark koji direktno poredi engleski i BCS na developer-relevantnim zadacima - generisanje koda, praćenje uputa, JSON ekstrakcija, faktografsko QA - na frontier modelima (GPT-4o, Claude 3.5, Llama 3). Tokenizacijski podaci su solidni. Dokazi o performansnom jazu su vjerovatni ali ne direktno izmjereni za ove scenarije.

Stanje se poboljšava. Veći rječnici (Gemma trend), više BCS podataka u web crawlovima, i projekti poput YugoGPT pomjeraju granicu. Developer koji gradi za BCS publiku danas treba ovu realnost uvrstiti u tehnički dizajn - izbor modela, prompt strukturu, i troškovni model - a ne tretirati je kao marginalni edge case.

---

## Izvori

- [Rust et al. 2021, "How Good is Your Tokenizer?" - ACL](https://aclanthology.org/2021.acl-long.243/)
- [Occiglot EU tokenizer fertility evaluation](https://occiglot.eu/posts/eu_tokenizer_perfomance/)
- ["The Tokenizer Tax Across 24 European Languages" (arXiv 2026)](https://arxiv.org/html/2605.24718)
- ["Quantifying Multilingual Performance of Large Language Models" (arXiv 2404.11553)](https://arxiv.org/html/2404.11553v1)
- [YugoGPT model card - HuggingFace](https://huggingface.co/gordicaleksa/YugoGPT)
- [Serbian LLM Eval benchmark (Gordić)](https://github.com/gordicaleksa/serbian-llm-eval)
- [BERTić - Ljubešić & Lauc 2021 (arXiv 2104.09243)](https://arxiv.org/abs/2104.09243)
- ["Resources and Few-shot Learners for In-context Learning in Slavic Languages" - ACL 2023](https://arxiv.org/pdf/2304.01922)
- ["State of the Art in Text Classification for South Slavic Languages" - arXiv 2025](https://arxiv.org/abs/2511.07989)
- ["Native vs Non-Native Language Prompting: A Comparative Analysis" (arXiv 2409.07054)](https://arxiv.org/html/2409.07054v1)
