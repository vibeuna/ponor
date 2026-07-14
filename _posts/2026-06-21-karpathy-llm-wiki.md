---
layout: post
title: "LLM Wiki: Karpathy-ev obrazac za knowledge base koji agent sam održava"
date: 2026-06-30
category: ai-u-praksi
audience: developers
read_time: 9
description: "Karpathy-ev LLM Wiki obrazac: tri sloja, tri operacije, i zašto mali knowledge base ne treba RAG. Praktični vodič s bosanskim prijevodima promptova."
diagram: /assets/diagrams/2026-06-21-karpathy-llm-wiki.svg
image: /assets/images/2026-06-21-karpathy-llm-wiki.svg
---

Andrej Karpathy je u Aprilu 2026. objavio GitHub Gist pod nazivom `llm-wiki.md` s opisom obrasca koji je koristio pri istraživanju: umjesto da svaki put čita izvore iznova ili gradi RAG (retrieval-augmented generation) pipeline, podesio je agenta da postepeno gradi i održava dosljedan wiki u plain-text markdown fajlovima. Ono što ovu ideju čini interesantnom nije vizija, nego konkretna arhitektura koju možete pokrenuti danas, s alatima koje već koristite.

Ovaj tekst objašnjava kako obrazac funkcioniše, zašto vrijedi razmišljati o njemu za lične ili timske projekte, i prikazuje tri osnovna prompta s bosanskimm prijevodom, jer razumijevanje šta agent zapravo radi zahtijeva da čitate te upute, ne samo da ih kopirate.

## Tri sloja arhitekture

LLM Wiki ima tri sloja, svaki s jasnom ulogom:

**`raw/`** je nepromjenjivo odlagalište izvora. Svi dokumenti koje unosite - PDF-ovi, HTML izvori, Markdown bilješke, transkripti - idu ovdje. Agent ih nikad ne mijenja. Ovo je vaš pravi istinski izvor informacija.

**`wiki/`** je LLM-ov radni prostor. Agent ovdje kreira i ažurira Markdown stranice - stranice za entitete (osobe, modeli, alati), konceptualne stranice, sinteze. Dva fajla su obavezna:
- `wiki/index.md` - katalog svih stranica s jednorečnim sažetcima, organiziran po kategorijama. Agent ga ažurira pri svakom ingestu.
- `wiki/log.md` - append-only kronološki zapis svake operacije. Nikad se ne briše, samo se dodaje.

**`CLAUDE.md`** (ili `AGENTS.md` za Codex, Gemini i druge) je schema - "ustav" wiki-ja. Ovaj fajl definira tipove stranica, format metapodataka, pravila cross-referenciranja, i standarde kvaliteta. Agent ga čita pri svakoj operaciji i ponaša se prema tim pravilima. Bez njega imate haotičan skup Markdown fajlova; s njim imate strukturirani, dosljedan wiki.

Karpathy-eva ključno zapažanje, citirano direktno iz Gista: *"The tedious part of maintaining a knowledge base is not reading or thinking - it's bookkeeping."* Obrazac prebacuje bookkeeping na agenta.

{% include diagram.html name="2026-06-21-karpathy-llm-wiki" caption="Tri sloja LLM Wiki arhitekture: raw/ i CLAUDE.md schema konvergiraju u agenta, koji piše i održava wiki/ sloj." alt="Dijagram LLM Wiki arhitekture s tri sloja i tri operacije" %}

## Kompajliraj, ne dohvataj

Razlika između LLM Wiki obrasca i RAG-a nije tehnička - radi se o tome kada i koliko puta agent "misli".

U RAG-u, svaki upit pokreće retrieval: sistem dohvata relevantne fragmente iz vector store-a i prosljeđuje ih modelu kao kontekst. Model generira odgovor, pa taj odgovor nestaje. Sljedeći upit počinje od nule.

LLM Wiki radi obrnuto: kada unesete novi izvor, agent jednom pročita taj materijal, sintetizira ga u trajne wiki stranice s cross-referencama, i ažurira index. Sljedeći upit ne traži po raw izvorima - čita wiki, koji je već distiliran i međupovezan.

Ovo je ono što Karpathy naziva "compile, don't retrieve" framingom. Znanje se akumulira. Svaki novi izvor koji dodate ne samo da dodaje informacije - obogaćuje mrežu veza između postojećih stranica.

**Kada ovo funkcioniše bolje od RAG-a?**

Na skali do ~100–200 dokumenata, index.md i relevantne wiki stranice stanu u kontekstni prozor (context window) jednog poziva. Nema potrebe za embedding vektorima, vector store-om, niti retrieval infrastrukturom. Upit je jednostavan: agent čita index, identifikuje relevantne stranice, čita te stranice, i odgovara s citiranjem.

Na većim skalama - enterprise dokumentacija, desetine hiljada dokumenata - RAG ostaje relevantan. Karpathy-ev zahtjev je precizan: ovaj obrazac je za osobne i projektne veličine, ne za korporativne korpuse.

## Tri operacije

Cijela funkcionalna logika wiki-ja svodi se na tri operacije: ingest, query, i lint. Svaka ima odgovarajući prompt.

### Ingest (unos novog izvora)

Ingest je operacija kojom unosite novi dokument u wiki. Agent pročita izvor, identifikuje entitete i koncepte, kreira ili ažurira odgovarajuće wiki stranice, uspostavi cross-reference veze, ažurira `index.md`, i doda zapis u `log.md`. Jedno izvršavanje ingesta tipično se dotakne 10–15 stranica.

**Prompt za ingest - originalni engleski (rekonstruiran iz sekundarnih izvora; nije Karpathy-ev doslovni tekst):**

```
Read [source file]. Following the schema in CLAUDE.md:
discuss key takeaways, write/update summary and entity pages,
update index.md, append to log.md.
```

**Bosanski prijevod - uputa agenta za ingest:**

```
Pročitaj [naziv fajla]. Slijedeći schema iz CLAUDE.md:
razmotre ključne zaključke, napiši ili ažuriraj
sažetak i stranice entiteta, ažuriraj index.md,
dodaj zapis u log.md.
```

Primjetite šta prompt ne govori: ne kaže agentu kako da organizira stranice, koje metapodatke da koristi, niti kako da formatira cross-reference. To sve definiše `CLAUDE.md`. Prompt je namjerno kratak jer schema nosi svu kompleksnost.

### Query (postavljanje upita)

Query je osnovna operacija pretraživanja. Agent čita `index.md`, pronalazi relevantne stranice, čita ih, i daje odgovor s citiranjem wiki stranica (ne raw izvora). Dobri odgovori na upite mogu se pohraniti natrag kao nove wiki stranice - "odgovori postaju stranice" je eksplicitni dio obrasca, koji pretvara efemerni retrieval u trajnu sintezu.

**Prompt za query - originalni engleski (rekonstruiran iz sekundarnih izvora; nije Karpathy-ev doslovni tekst):**

```
Using index.md to navigate, find relevant pages and
synthesize an answer to: [question]. Cite pages used.
```

**Bosanski prijevod - uputa agenta za query:**

```
Koristeći index.md za navigaciju, pronađi relevantne
stranice i sintetizuj odgovor na: [pitanje].
Navedi koje stranice si koristio.
```

Imperativno je da prompt traži citiranje. Bez toga agent može halucinirati ili miješati sadržaj iz različitih stranica bez traga.

### Lint (provjera zdravlja wiki-ja)

Lint je periodična operacija koja provjerava strukturni integritet wiki-ja. Agent skenira sve stranice i traži: stranice bez ulaznih linkova (orphan pages), neispravne cross-reference veze, kontradikcije između stranica, zastarjele sažetke, i praznine u dokumentaciji. Što može popraviti - popravlja. Što zahtijeva ljudski uvid - označava.

**Prompt za lint - originalni engleski (rekonstruiran iz sekundarnih izvora; nije Karpathy-ev doslovni tekst):**

```
Scan all wiki/ pages for: orphan pages with no inbound links,
broken cross-references, contradictions between pages,
stale claims, data gaps. Fix what you can;
flag what needs human input.
```

**Bosanski prijevod - uputa agenta za lint:**

```
Skeniraj sve stranice u wiki/ i pronađi: orphan stranice
bez dolaznih linkova, neispravne cross-reference veze,
kontradikcije između stranica, zastarjele tvrdnje,
praznine u dokumentaciji. Popravi što možeš;
označi šta zahtijeva ljudski uvid.
```

Lint je skup na velikim wiki-jima - treba da čita svaku stranicu. Karpathy-ev prijedlog je da se pokreće tjedno ili po potrebi, ne pri svakom ingestu.

## Postavljanje: korak po korak

Evo konkretnog postupka za pokretanje wiki-ja od nule. Pretpostavljamo Claude Code, ali isti obrazac radi s Codex CLI-jem, Cursorom, Copilotom, Gemini CLI-jem - svakim agentom koji može čitati i pisati fajlove.

**1. Kreirajte strukturu direktorijuma:**

```bash
mkdir my-wiki
cd my-wiki
mkdir raw wiki
touch wiki/index.md wiki/log.md
```

**2. Napišite `CLAUDE.md` - ovo je najvažniji korak.**

Schema definiše ontologiju vašeg wiki-ja. Minimalna verzija:

```markdown
# Wiki Schema

## Tipovi stranica
- **Entitet**: osoba, alat, model, organizacija - jedna stranica po entitetu
- **Koncept**: objašnjenje ideje ili termina
- **Sažetak**: pregled izvora iz raw/
- **Sinteza**: cross-source zaključci na jednu temu

## Metadata format (na vrhu svake stranice)
-
tip: entitet | koncept | sažetak | sinteza
kreirano: YYYY-MM-DD
ažurirano: YYYY-MM-DD
srodne-stranice: [stranica-a.md, stranica-b.md]
-

## Pravila
- Svaka nova stranica mora biti linkana iz index.md
- Svaki ingest mora dodati zapis u log.md (format: `YYYY-MM-DD: Ingestovan [naziv fajla]`)
- Cross-reference se piše kao [[naziv-stranice]] ili kao Markdown link
- Kontradikcije između stranica se označavaju tagom `[KONFLIKT]` i bilježe u log.md
- Orphan stranice (bez dolaznih linkova) nisu dozvoljene
```

**3. Bacite prvi dokument u `raw/` i pokrenite ingest:**

```
Pročitaj raw/prvi-izvor.md. Slijedeći schema iz CLAUDE.md:
razmotre ključne zaključke, napiši ili ažuriraj
sažetak i stranice entiteta, ažuriraj index.md,
dodaj zapis u log.md.
```

**4. Postavljajte upite odmah nakon prvog ingesta** da provjerite radi li index ispravno.

**5. Pokrenite lint nakon svakih 5–10 ingesta** ili sedmično.

**6. Refinišite `CLAUDE.md` kako model domene sazrijeva.** Početna schema je hipoteza. Nakon 20–30 dokumenata, razumjet ćete koji tipovi stranica nedostaju, koje veze su se pokazale korisne, i koje konvencije treba precizirati. Ažurirajte shemu, zatim pokrenite lint koji će primijeniti nova pravila retroaktivno.

## Poznate slabosti obrasca

Zajednica koja je implementirala ovaj obrazac prijavila je tri konzistentna problema:

**Synthesis decay**: Agent ponekad prepiše starije sinteze kada unosi novi materijal koji ih kontradikuje, umjesto da eksplicitno dokumentuje konflikt. Rješenje: dodati pravilo u `CLAUDE.md` koje eksplicitno zabranjuje brisanje prethodnih sinteza bez `[KONFLIKT]` taga i log zapisa.

**Trošak linta na skali**: Na wiki-ju s 500+ stranica, lint prolaz čita sve stranice - skupo u tokenima i sporom. Ovo je inherentna cijena ne-RAG pristupa na većoj skali. Praktična opcija: parcialni lint po kategorijama stranica.

**Stvrdnjavanje zastarjelih sažetaka**: Stranice koje nisu dodirnute u više ingesta-ciklusa mogu sadržavati tvrdnje koje su postale netačne. `log.md` pomaže - date stamp otkriva koliko je stara stranica - ali automatska detekcija zastarjelosti nije ugrađena u obrazac. Treba je dodati u schema pravila.

Ovo nisu greške u dizajnu koje diskvalifikuju obrazac. Sva tri problema su poznata i rješiva pravilima u `CLAUDE.md`. Poenta je da ih postavite proaktivno, ne reaktivno.

## Kompatibilnost s alatima i zajednica

Osim Karpathy-evog originalnog Gista, nezavisne implementacije su se pojavile brzo:

- `Pratiyush/llm-wiki` (GitHub) - implementacija koja cilja Claude Code, Codex, Cursor, Copilot, i Gemini sesije
- `rohitg00` LLM-Wiki-v2 gist - proširuje obrazac s "agent memory lessons", posebnom kategorijom stranica koje bilježe što agent ne smije raditi
- `nashsu/llm_wiki` - desktop aplikacija izgrađena na obrascu

Nijedna od ovih implementacija nije Karpathy-eva zvanična nadogradnja - to su nezavisne interpretacije. Gist ostaje kanonski referentni dokument.

## Zaključak

LLM Wiki obrazac je koristan jer stavlja na papir nešto što je prethodno bilo implicitno: da je LLM agent bolji bookkeeper nego što je bolji retriever, a da knowledge base čija organizacija kompajlira znanje jedanput vrijedi više od sistema koji ga svaki put iznova dohvata iz sirovih izvora.

Ako radite na projektu s dokumentima u rasponu stotina, a ne desetina hiljada - istraživanje, interna dokumentacija tima, osobno učenje u novom domenu - vrijedi pokušati. Minimalni setup je jedan direktorijum, jedan `CLAUDE.md` fajl, i agent koji već imate.

## Izvori

- [Karpathy LLM Wiki Gist (karpathy/442a6bf555914893e9891c11519de94f)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) - kanonski tehnički referentni dokument
- [Karpathy originalni X post (x.com/karpathy/status/2039805659525644595)](https://x.com/karpathy/status/2039805659525644595) - originalna objava, April 2026.
- [Pratiyush/llm-wiki (GitHub)](https://github.com/Pratiyush/llm-wiki) - community implementacija za više agenata
