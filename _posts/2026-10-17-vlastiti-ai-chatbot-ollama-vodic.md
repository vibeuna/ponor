---
layout: post
title: "Vlastiti AI chatbot na računaru: Ollama vodič od nule"
date: 2026-10-17
category: ai-u-praksi
image: /assets/images/2026-10-17-vlastiti-ai-chatbot-ollama-vodic.svg
read_time: 7
description: "Kako instalirati Ollamu na Ubuntuu, preuzeti mali model otvorenih težina i razgovarati s njim u terminalu, bez slanja upita u oblak."
tags: [llm]
---

Ollama je program koji preuzima LLM (velike jezičke modele) i pokreće ih na vašem računaru. Na Ubuntu-u su za prvi razgovor dovoljne tri komande. Prva instalira Ollamu, druga preuzima model, a treća otvara razgovor u terminalu. Vodič se oslanja na Ollaminu dokumentaciju, koju smo provjerili 17. oktobra 2026. Tada je aktuelna verzija bila [0.40.5](https://github.com/ollama/ollama/releases). Pokriva sve, od provjere hardvera do potpunog uklanjanja. Ollama postoji i za macOS i Windows, ali ovdje su samo koraci za Ubuntu.

## Ukratko

Ollamu na Ubuntuu instalirate jednom komandom: `curl -fsSL https://ollama.com/install.sh | sh`. Skripta postavlja servis koji radi u pozadini. Model preuzimate i pokrećete komandom `ollama run gemma4:e2b`. Grafička kartica (GPU) nije obavezna. Bez nje Ollama radi samo na procesoru (CPU). Četiri mala modela iz ovog vodiča zauzimaju od 2 do 4,6 GB, a nijedan od njih ne navodi bosanski među dokumentovanim jezicima. Funkcije u oblaku uključene su odmah nakon instalacije. Isključujete ih postavkom `OLLAMA_NO_CLOUD=1`.

{% include diagram.html name="vlastiti-ai-chatbot-ollama-vodic" caption="Tri komande vode od instalacije do prvog razgovora, a sve radi na vašem računaru." alt="Tri koraka u Ollami na Ubuntuu: instalacija komandom curl, preuzimanje modela komandom ollama pull gemma4:e2b i razgovor komandom ollama run gemma4:e2b. Ispod je poređenje lokalnog modela i modela u oblaku." %}

## Šta je model otvorenih težina

LLM čine kod i ogroman skup naučenih brojeva. Ti brojevi su težine (weights). Kad kažemo da model ima 3 milijarde parametara, mislimo na broj tih vrijednosti.

Model otvorenih težina (open-weight) je model čije težine možete preuzeti i pokrenuti na svom računaru. To nije isto što i otvoreni kod (open source). Definicija [Open Source Initiative](https://opensource.org/ai/open-source-ai-definition) (OSAID 1.0) za AI traži tri stvari: informacije o podacima za treniranje (training), kompletan kod za treniranje i pokretanje modela te parametre. Nijedan od četiri modela u ovom vodiču ne objavljuje podatke za treniranje. Google na [stranici modela Gemma](https://huggingface.co/google/gemma-4-E2B-it) i sam piše da su to modeli otvorenih težina. Mistral za [Ministral](https://huggingface.co/mistralai/Ministral-3-3B-Instruct-2512) piše "open-source", ali njegova licenca Apache 2.0 pokriva težine, a ne cijeli sistem onako kako ga definiše OSAID.

Licence se razlikuju. Gemma, Qwen i Ministral koriste Apache 2.0. [Licenca za Llamu 3.2](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/LICENSE) postavlja dodatne uslove: posebnu licencu za usluge s više od 700 miliona aktivnih korisnika mjesečno, oznaku "Built with Llama" pri daljoj distribuciji i [pravila prihvatljive upotrebe](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/USE_POLICY.md). Prema tim pravilima, osobe s prebivalištem i firme sa sjedištem u EU ne dobijaju prava iz licence za multimodalne modele Llama 3.2, to jest one koji uz tekst primaju i slike. Ograničenje ne važi za krajnje korisnike proizvoda zasnovanih na tim modelima, a BiH nije članica EU. Tekstualni model od 3 milijarde parametara iz ovog vodiča to ionako ne pogađa.

## Treba li vam grafička kartica?

Ne. Grafička kartica nije uslov. Ako je nema, instalacijska skripta ispiše "No NVIDIA/AMD GPU detected. Ollama will run in CPU-only mode". To znači da će Ollama raditi samo na procesoru. Ollama ne navodi minimalnu količinu RAM-a (radne memorije) ni prostora na disku. Za prostor se vodite veličinom modela u tabeli niže.

Ako imate grafičku karticu, [zahtjevi](https://github.com/ollama/ollama/blob/main/docs/gpu.mdx) su ovakvi:

- **NVIDIA:** drajver verzije 550 ili noviji, a za dio kartica 570 ili noviji. Tačan spisak kartica je u dokumentaciji.
- **AMD:** drajver ROCm v7.
- **Ostale kartice:** rade preko Vulkana.

Vlasnici NVIDIA kartica mogu provjeriti drajver ovom komandom. Ispis pokazuje karticu i verziju drajvera.

```bash
nvidia-smi
```

## Korak 1: instalacija

Instalacija je jedna komanda. `curl` preuzima [instalacijsku skriptu](https://ollama.com/install.sh), a `| sh` je odmah pokreće. Skripta radi na procesorima arhitekture x86_64 i aarch64. Dio posla obavlja preko `sudo`, komande koja druge komande pokreće s administratorskim pravima, pa će Ubuntu tražiti vašu lozinku. Skriptu možete otvoriti u pregledniku i pročitati prije pokretanja.

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Skripta instalira Ollamu u `/usr/local`, pravi sistemskog korisnika `ollama` i postavlja systemd servis, odnosno pozadinski proces koji se pokreće zajedno sa sistemom. Na kraju ispiše "The Ollama API is now available at 127.0.0.1:11434." Ako pronađe NVIDIA karticu bez drajvera, sama ga instalira, pa će možda trebati ponovo pokrenuti računar.

Skripti treba i program zstd. Ako ga nema, zaustavi se i ispiše komandu za njegovu instalaciju. Pokrenite tu komandu, pa ponovite instalaciju.

```bash
sudo apt-get install zstd
```

## Korak 2: provjera

Prva komanda ispisuje verziju Ollame, a druga pokazuje stanje servisa.

```bash
ollama -v
sudo systemctl status ollama
```

Ako nešto ne radi, poruke servisa možete pratiti ovom komandom ([dokumentacija](https://github.com/ollama/ollama/blob/main/docs/troubleshooting.mdx)):

```bash
journalctl -u ollama --no-pager --follow --pager-end
```

## Korak 3: prvi model

Kao primjer koristimo Googleov `gemma4:e2b`. Dio iza dvotačke je oznaka (tag) koja bira varijantu modela. Prva komanda preuzima model veličine 4,6 GB.

```bash
ollama pull gemma4:e2b
```

Druga otvara razgovor ([uputstvo za početak](https://github.com/ollama/ollama/blob/main/docs/quickstart.mdx)). Upišete pitanje i pritisnete Enter, a razgovor zatvarate sa `/bye`.

```bash
ollama run gemma4:e2b
```

Na Linuxu se modeli čuvaju u `/usr/share/ollama/.ollama/models`. Nakon posljednjeg pitanja model ostaje učitan u memoriji još 5 minuta. Ollama podrazumijevano koristi [kontekstni prozor](/rjecnik/kontekstni-prozor/) (context window) od 4096 [tokena](/rjecnik/token/). Token je osnovna jedinica teksta koju model obrađuje, a to su riječi ili dijelovi riječi. Prema [dokumentaciji o dužini konteksta](https://github.com/ollama/ollama/blob/main/docs/context-length.mdx), toliki prozor dobijaju računari s manje od 24 GiB memorije grafičke kartice (VRAM). Uz više VRAM-a prozor je veći.

Jedno upozorenje: oznake koje sadrže `cloud`, npr. `gemma4:cloud` ili `gemma4:31b-cloud`, pokreću model na Ollaminim serverima, a ne na vašem računaru. Ako vam treba lokalni model, zaobiđite ih.

## Koji mali model izabrati?

Tabela navodi četiri mala lokalna modela. Veličina je ona koju Ollama na Linuxu preuzima podrazumijevano.

| Oznaka | Parametri (prema proizvođaču) | Veličina | Licenca | Bosanski dokumentovan? |
|---|---|---|---|---|
| [`llama3.2:3b`](https://ollama.com/library/llama3.2) | 3 milijarde | 2,0 GB | Llama 3.2 Community License | Ne: među 8 službenih jezika nema ni bosanskog, ni hrvatskog, ni srpskog |
| [`ministral-3:3b`](https://ollama.com/library/ministral-3) | 3,4 milijarde | 3,0 GB | Apache 2.0 | Ne: navodi 11 jezika, među njima nijedan od ova tri |
| [`qwen3.5:4b`](https://ollama.com/library/qwen3.5) | 4 milijarde | 3,3 GB | Apache 2.0 | Nije dokumentovano: navodi 201 jezik i dijalekt, bez spiska |
| [`gemma4:e2b`](https://ollama.com/library/gemma4) | 2,3 milijarde efektivnih (ukupno 5,1) | 4,6 GB | Apache 2.0 | Nije dokumentovano: navodi podršku za više od 35 jezika i treniranje na više od 140, bez spiska |

Za Gemmu 4 E2B Google navodi 2,3 milijarde efektivnih parametara, a 5,1 milijardu kad se uračunaju i [embeddingovi](/rjecnik/embedding/). Stranice za Gemmu 4 i Qwen 3.5 navode raspon veličina (4,6–7,5 GB i 3,3–4,0 GB). Podrazumijevano preuzimanje je ono s donje granice.

Tabela ne rangira kvalitet. Proizvođači svoje modele hvale superlativima, npr. Google za Gemmu piše "frontier-level performance at each size". To su njihove tvrdnje, a ne nezavisni rezultati. Ponor ove modele nije testirao na bosanskom.

Preuzete modele prikazuje `ollama ls`. Komanda `ollama ps` pokazuje koji su modeli učitani i koliko svaki od njih radi na procesoru, a koliko na grafičkoj kartici.

```bash
ollama ls
ollama ps
```

## Privatnost: isključite funkcije u oblaku

Ollamin [FAQ](https://github.com/ollama/ollama/blob/main/docs/faq.mdx) kaže da Ollama radi lokalno i da firma ne vidi vaše promptove (upite koje unosite modelu) ni podatke dok radite lokalno. Funkcije u oblaku su ipak uključene odmah nakon instalacije. Model u oblaku obrađuje vaše promptove na Ollaminim serverima. Ollama tvrdi da taj sadržaj ne čuva i ne koristi za treniranje, ali to se ne može nezavisno provjeriti.

Postavka `OLLAMA_NO_CLOUD=1` uklanja modele u oblaku i pretraživanje weba. Servis radi kao korisnik `ollama`, pa je najpouzdanije upisati je direktno u servis. Prva komanda otvara uređivač teksta:

```bash
sudo systemctl edit ollama
```

U njega upišite ove dvije linije i sačuvajte:

```ini
[Service]
Environment="OLLAMA_NO_CLOUD=1"
```

Zatim učitajte izmjenu i ponovo pokrenite servis:

```bash
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

Ollama se na Linuxu ne ažurira sama. Novu verziju dobijate tako što ponovo pokrenete instalacijsku komandu iz prvog koraka. Dokumentacija za Linux ne spominje ni slanje podataka o korištenju ni automatsku provjeru novih verzija.

## Chatbot iz drugih programa: lokalni API

Servis nudi API (programski interfejs) na adresi `localhost`, to jest na vašem računaru, na portu 11434. Preko njega drugi programi mogu slati pitanja modelu. Ova komanda šalje jedno pitanje:

```bash
curl http://localhost:11434/api/chat -d '{"model": "gemma4:e2b", "messages": [{"role": "user", "content": "Objasni ukratko šta je kontekstni prozor."}], "stream": false}'
```

`"stream": false` znači da odgovor stiže odjednom. Tekst odgovora nalazi se u polju `"content"`. Ollama za Linux nema zvanični grafički interfejs. [README](https://github.com/ollama/ollama/blob/main/README.md) navodi programe drugih autora, npr. Open WebUI i Alpaca. Ponor ih nije testirao.

## Zaustavljanje, brisanje i deinstalacija

Prva komanda odmah izbacuje model iz memorije, a druga ga briše s diska.

```bash
ollama stop gemma4:e2b
ollama rm gemma4:e2b
```

Za potpuno uklanjanje [dokumentacija](https://github.com/ollama/ollama/blob/main/docs/linux.mdx) navodi ove komande. One zaustavljaju servis te brišu program, korisnika i grupu `ollama` i sve preuzete modele.

```bash
sudo systemctl stop ollama
sudo systemctl disable ollama
sudo rm /etc/systemd/system/ollama.service
sudo rm -r $(which ollama | tr 'bin' 'lib')
sudo rm $(which ollama)
sudo userdel ollama
sudo groupdel ollama
sudo rm -r /usr/share/ollama
```

Četvrta komanda radi ispravno samo ako je Ollama instalirana u `/usr/local/bin` ili `/usr/bin`, a skripta je podrazumijevano tamo instalira. Uputstvo ne briše folder `~/.ollama` u vašem kućnom folderu, u kojem su postavke i ključevi. Ako želite ukloniti baš sve, obrišite ga ručno.

## Povezano

- [Šta je LLM i kako radi?](https://www.ponor.ba/clanci/sta-je-llm/) – šta je zapravo model koji ste upravo pokrenuli.
- [Šta je kontekstni prozor i zašto LLM zaboravlja?](https://www.ponor.ba/clanci/sta-je-kontekstni-prozor/) – šta se dešava kad se prozor od 4096 tokena napuni.
- [Kako provjeriti odgovor chatbota: šest navika](https://www.ponor.ba/clanci/kako-provjeriti-ai-odgovor/) – odgovore lokalnog modela provjeravajte kao i odgovore bilo kojeg chatbota.

## Izvori

- [Linux – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/linux.mdx)
- [Instalacijska skripta – Ollama](https://ollama.com/install.sh)
- [FAQ – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/faq.mdx)
- [Hardware support – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/gpu.mdx)
- [Troubleshooting – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/troubleshooting.mdx)
- [CLI Reference – Ollama dokumentacija](https://github.com/ollama/ollama/blob/main/docs/cli.mdx)
- [The Open Source AI Definition 1.0 – Open Source Initiative](https://opensource.org/ai/open-source-ai-definition)
