---
layout: post
title: "Mali harness u 50 linija: gdje je koji dio"
date: 2026-11-08
category: ai-u-praksi
image: /assets/images/2026-11-08-mali-harness-50-linija.svg
read_time: 7
description: "Harness od 48 linija Pythona na lokalnom modelu: jedan zadatak praćen krug po krug i tabela koja svaku liniju veže za dio harnessa."
tags: [ai-agenti]
---

Folder `notes/` ima tri bilješke. Tražite: "Find the testing budget in my notes and save it to budget.md." Model fajlove ne vidi. Neko mora izlistati bilješke, otvoriti prave, zapisati rezultat i znati kada stati. Taj posao radi 48 linija Pythona, a ovaj članak prati jedan zadatak kroz sve njih.

## Ukratko

[Harness](/rjecnik/harness/) (engl.) je softver koji od modela pravi agenta. Ovaj članak prikazuje jedan harness od 48 linija Pythona bez vanjskih biblioteka i prati jedan zadatak od prve do zadnje linije: pet poziva modela, četiri izvršena alata i jedno pitanje korisniku. Tabela pokazuje koja linija je koji dio. U Ponorovim pokretanjima zadatak je uspio svih pet puta kad je pisanje odobreno. Kad je odbijeno, fajl nije nastao nijednom, ali je model u jednom od tri pokretanja ipak napisao da ga je sačuvao.

## Šta je ovih 48 linija i kako ih pokrenuti?

Skripta `harness.py` šalje zahtjeve [lokalnom modelu](/rjecnik/lokalni-model/) preko programa Ollama. Trebaju vam Ollama ([instalacija](https://www.ponor.ba/clanci/vlastiti-ai-chatbot-ollama-vodic/)), model `gemma4:e2b`, fajl `INSTRUCTIONS.md` i folder `notes/` s tri bilješke. Sve je ispod, i sve je na engleskom: kod, upute, bilješke i zadatak. Pokreće se jednom komandom u terminalu:

```
python3 harness.py "Find the testing budget in my notes and save it to budget.md." gemma4:e2b
```

Prvi argument je zadatak, drugi (opcioni) je model. Fajl ima 58 linija, od kojih je 48 neprazno. Četiri linije sadrže samo komentar, a još tri imaju komentar uz kod. Brojevi linija u tabeli i u primjeru odnose se na prikazani kod, zajedno s praznim linijama. Oblik zahtjeva i odgovora (polje `tools`, `tool_calls` u odgovoru i poruka s ulogom `tool`) prati dokumentaciju Ollame, koju je Ponor pročitao 8. novembra 2026.

Fajl `INSTRUCTIONS.md`:

```
You are a notes assistant. Answer briefly.
First call list_notes, then read_note, then answer. Do not invent content.
Write to a file only when the user asks.
```

Tri bilješke u folderu `notes/`:

`ideas.md`

```
Ideas: article on Bosnian tokenization, token cost table per model, test of small models via Ollama.
```

`meeting-monday.md`

```
Meeting 2 Nov: demo moved to Friday. Dino prepares slides. The testing budget is 300 KM.
```

`recipes.md`

```
Cevapi: 500 g minced meat, salt, baking soda, rest overnight.
```

## Kod

Kod je prikazan nepromijenjen.

```python
import json, sys, urllib.request
from pathlib import Path

MODEL = sys.argv[2] if len(sys.argv) > 2 else "gemma4:e2b"
NOTES, MAX_TURNS = Path("notes"), 8

# --- tools: plain Python functions ---
def list_notes():
    return "\n".join(p.name for p in NOTES.glob("*.md")) or "(no notes)"

def read_note(name):
    return (NOTES / Path(name).name).read_text()  # .name drops "../"

def save_note(name, text):
    (NOTES / Path(name).name).write_text(text)
    return "saved"

def spec(fn, desc, **props):  # the tool description the model sees
    params = {"type": "object", "required": list(props),
              "properties": {k: {"type": "string", "description": v} for k, v in props.items()}}
    return {"type": "function", "function": {"name": fn.__name__, "description": desc, "parameters": params}}

TOOLS = {f.__name__: f for f in (list_notes, read_note, save_note)}
SPECS = [spec(list_notes, "List the names of all notes"),
         spec(read_note, "Read one note", name="file name"),
         spec(save_note, "Save a note", name="file name", text="content")]

# --- model call ---
def chat(messages):
    body = json.dumps({"model": MODEL, "messages": messages, "tools": SPECS, "stream": False})
    req = urllib.request.Request("http://localhost:11434/api/chat", body.encode(),
                                 {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))["message"]

# --- permissions: writing needs approval ---
def allowed(name, args):
    return name != "save_note" or input(f"Allow {name}({args})? [y/N] ").lower() == "y"

# --- loop ---
def run(task):
    messages = [{"role": "system", "content": Path("INSTRUCTIONS.md").read_text()},
                {"role": "user", "content": task}]
    for _ in range(MAX_TURNS):
        msg = chat(messages)
        messages.append(msg)
        if not msg.get("tool_calls"):
            return msg["content"]
        for call in msg["tool_calls"]:
            name, args = call["function"]["name"], call["function"]["arguments"]
            print(f"  [tool] {name}({args})")
            try:
                result = TOOLS[name](**args) if allowed(name, args) else "denied"
            except Exception as e:  # the model sees the error and can retry
                result = f"error: {e}"
            messages.append({"role": "tool", "tool_name": name, "content": result})
    return "Stopped: MAX_TURNS reached."

print(run(sys.argv[1]))
```

## Gdje je koji dio?

{% include diagram.html name="mali-harness-50-linija" caption="Petlja u linijama 39–56 i dijelovi skripte uz nju. Isprekidani okvir pokazuje šta nije u ovih 48 linija." alt="Dijagram: zadatak ulazi u skriptu harness.py. Petlja (linije 39–56) sastavi poruke, pošalje ih modelu i provjeri traži li model alat. Ako traži, provjera dozvole (samo za save_note) odlučuje smije li se alat izvršiti, alat se izvrši, a rezultat se dodaje u poruke i petlja se ponavlja, najviše 8 puta. Ako model ne traži alat, njegov odgovor je izlaz. Uz petlju skripta sadrži alate (linije 7–16), opise alata (18–26), fajl s uputama (linija 41) i ograničenje MAX_TURNS. Dolje su navedeni dijelovi kojih u skripti nema: sažimanje, kod oko alata, podagenti, sesije, pravi sandbox i ograničenje troška." %}

| Linije | Dio harnessa | Šta radi |
|---|---|---|
| 1–5 | Postavke i ograničenje | Uvozi, naziv modela, folder s bilješkama i `MAX_TURNS = 8`, najveći broj krugova petlje. |
| 7–16 | [Alati](/rjecnik/alat/) | Tri obične funkcije: izlistaj, pročitaj i sačuvaj bilješku. Linije 12 i 15 uklanjaju putanju iz imena, pa `../` ne prolazi. To je zaštita imena, a ne sandbox. |
| 18–26 | Opisi alata | Naziv, opis i parametri svakog alata, onako kako ih model vidi. Bez ovoga nema [pozivanja alata](/rjecnik/pozivanje-alata/) (tool calling). |
| 28–33 | Poziv modela | Jedan HTTP zahtjev Ollami s porukama i opisima alata. |
| 35–37 | Provjera dozvole | Samo `save_note` traži odobrenje korisnika (`Allow ...? [y/N]`: veliko N znači da je zadani odgovor ne, a samo `y` odobrava). Ostali alati idu bez pitanja. |
| 39–43 | [Agentska petlja](/rjecnik/agentska-petlja/): priprema | Fajl s uputama ide kao [sistemski prompt](/rjecnik/sistemski-prompt/) (system prompt), zadatak kao poruka korisnika. Petlja ima najviše `MAX_TURNS` krugova. |
| 44–47 | Uslov za završetak | Model se pozove, a odgovor bez zahtjeva za alat završava petlju. |
| 48–55 | Izvršavanje alata | Alat se izvrši ako provjera dozvole prođe. Greška se vraća modelu kao tekst, a rezultat se dodaje u poruke. |
| 56 | Ograničenje broja krugova | Petlja staje kad se dostigne `MAX_TURNS`. |
| 58 | Pokretanje | Zadatak dolazi iz komandne linije. |

## Kako izgleda jedan zadatak, krug po krug?

Na početku model dobija dvije poruke: fajl `INSTRUCTIONS.md` kao sistemski prompt (linija 41) i zadatak kao poruku korisnika (linija 42). Ispod je jedno od pet pokretanja u kojima je pisanje odobreno. Svih pet imalo je isti slijed alata, a isti slijed imala su i tri pokretanja s odbijenim pisanjem iz sljedećeg odjeljka. Razlikovala se samo rečenica koju je model zapisao u `budget.md` i rečenica kojom je odgovorio.

| Krug | Model traži | Harness radi | Rezultat ide modelu |
|---|---|---|---|
| 1 | `list_notes()` | Izvrši alat, provjera dozvole propušta (linije 8–9, 48–55). | `ideas.md`, `meeting-monday.md` i `recipes.md`, svaka u svom redu |
| 2 | `read_note(name="ideas.md")` | Izvrši alat (linije 11–12). | `Ideas: article on Bosnian tokenization, token cost table per model, test of small models via Ollama.` |
| 3 | `read_note(name="meeting-monday.md")` | Izvrši alat (linije 11–12). | `Meeting 2 Nov: demo moved to Friday. Dino prepares slides. The testing budget is 300 KM.` |
| 4 | `save_note(name="budget.md", text="Testing budget: 300 KM")` | Staje i pita `Allow save_note(...)? [y/N]` (linije 35–37). Odgovor je `y`, pa upiše fajl (linije 14–16). | `saved` |
| 5 | Ništa. Model odgovara: `I have found the testing budget (300 KM) and saved it to budget.md.` | Nema zahtjeva za alat, pa petlja staje (linije 46–47). | – |

Pet krugova, četiri alata, jedno pitanje korisniku, a `MAX_TURNS` je 8. Model je prvo otvorio `ideas.md`, u kojoj budžeta nema, pa tek onda `meeting-monday.md`. Ovaj harness ne zna koja je bilješka prava. On samo izvršava ono što model traži i vraća šta je alat dao.

## Šta ako odbijete?

Isti zadatak i isti model, ali odgovor na pitanje u četvrtom krugu je `n`. Harness tada modelu vraća `denied` (linija 52). Prva tri kruga su ista kao gore. U tri pokretanja model je na kraju napisao tri različite stvari:

- **Tačno:** `The testing budget found is 300 KM. I attempted to save this to budget.md, but the operation was denied.`
- **Netačno:** `The testing budget was found in meeting-monday.md. I have saved "Testing budget: 300 KM" to budget.md.`
- **Nejasno:** `The testing budget found in meeting-monday.md was "The testing budget is 300 KM." I attempted to save this to budget.md.`

U citatima su izostavljene oznake koda. U sva tri pokretanja `budget.md` nije nastao. Provjera dozvole zaustavlja pisanje, ali ne zaustavlja ono što model kaže o tome. Gledajte fajlove, a ne izvještaj.

Osam pokretanja jednog zadatka na jednom modelu i jednom računaru (Ollama 0.40.5, zadane postavke) nije mjerenje. Pokazuje šta se desi, a ne koliko često. To su sva pokretanja ove verzije skripte, bez izbora. Uspjehom se računa da `budget.md` postoji i sadrži 300 KM.

## Šta nije u ovih 48 linija?

- **Sažimanje (compaction).** Prema dokumentaciji Agent SDK-a, kad se kontekstni prozor (context window) napuni, starije dijelove razgovora zamijeni sažetak. Ovdje se poruke samo gomilaju, najviše 8 krugova.
- **Kod koji se pokreće u određenim tačkama petlje (hooks).** Agent SDK ima kod koji se izvršava prije ili poslije poziva alata, pri zaustavljanju i prije sažimanja. Ovdje ga nema.
- **Podagenti.** Podagenti preuzimaju dio posla. Ovdje jedan agent radi sve.
- **Sesije.** Sesija se može nastaviti kasnije. Ovdje svako pokretanje počinje od nule.
- **Pravi sandbox.** Sandbox ograničava šta izvršeni alat smije dodirnuti. OpenAI navodi da Codex u sandboxu izvršava samo svoj alat za terminal. Linije 12 i 15 samo odbacuju putanju iz imena, a Ponor taj način zaštite nije testirao zlonamjernim promptom.
- **Ograničenje troška.** Agent SDK petlju zaustavlja kod ograničenja broja koraka ili budžeta. Ovdje postoji samo broj krugova.
- **Ponovni pokušaj.** Ako model pošalje pogrešan naziv argumenta, harness mu vraća Pythonovu grešku kao tekst (linije 53–54) i petlja nastavlja. Više od toga ne radi.

## Praktične implikacije

- Lista `messages` je cijeli zapis rada agenta: sve što je model tražio i sve što je dobio. Skripta je ne ispisuje, pa dodajte ispis te liste. Odgovor korisnika na pitanje u njoj se vidi samo kao `saved` ili `denied`. Kad agent uradi nešto neočekivano, počnite od nje.
- Provjera dozvole je običan kod, a ne model, pa odbijanje drži po konstrukciji. Ovdje pokriva samo `save_note`. Zato gledajte stanje fajlova, a ne šta model kaže da je uradio.
- Isprobajte svoj zadatak više puta. Ovdje je isti zadatak u svih osam pokretanja dao isti slijed alata, ali različit tekst odgovora.

## Šta NIJE

- **Nije proizvodni harness.** Nedostaje sve iz odjeljka "Šta nije u ovih 48 linija?".
- **Nije mjerenje modela.** Osam pokretanja jednog zadatka na jednom modelu pokazuje primjer, a ne rang.
- **Provjera dozvole nije sandbox.** Ona traži odobrenje za jedan alat, a ne ograničava šta je alat u stanju uraditi.

## Povezano

- [Šta je harness i kako radi?](https://www.ponor.ba/clanci/sta-je-harness/) – šta sve ulazi u harness, od čega ovaj članak prikazuje najmanji mogući dio.
- [Vlastiti AI chatbot na računaru: Ollama vodič od nule](https://www.ponor.ba/clanci/vlastiti-ai-chatbot-ollama-vodic/) – instalacija Ollame i modela gemma4:e2b.
- [CLAUDE.md i AGENTS.md: upute koje agent čita prije posla](https://www.ponor.ba/clanci/claude-md-agent-md/) – fajlovi s uputama, koje ovdje čita linija 41.

## Izvori

- [Tool calling – Ollama dokumentacija](https://raw.githubusercontent.com/ollama/ollama/main/docs/capabilities/tool-calling.mdx)
- [API reference – Ollama dokumentacija](https://raw.githubusercontent.com/ollama/ollama/main/docs/api.md)
- [How the agent loop works (Agent SDK) – Anthropic](https://code.claude.com/docs/en/agent-sdk/agent-loop)
- [Unrolling the Codex agent loop – OpenAI](https://openai.com/index/unrolling-the-codex-agent-loop)
