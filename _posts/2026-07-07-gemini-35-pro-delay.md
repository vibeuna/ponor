---
layout: post
title: "Gemini 3.5 Pro navodno kasni — Google ne potvrđuje, DeepMind gubi dva istraživača"
date: 2026-07-07
description: "Gemini 3.5 Pro navodno kasni prema jednom nepotvrđenom insajderskom izvještaju, dok Google DeepMind u razmaku od jednog dana gubi Gemini ko-vođu Noama Shazeera i potpredsjednika Johna Jumpera."
category: vijesti
image: /assets/images/2026-07-07-gemini-35-pro-delay.svg
audience: developers
read_time: 4
---

Google navodno pomjera lansiranje Gemini 3.5 Pro modela, prema jednom insajderskom izvještaju koji Google nije potvrdio niti demantovao. Izvještaj se poklapa s odlaskom dva viša istraživača iz DeepMind-a — Noama Shazeera i Johna Jumpera — ali veza između ta dva događaja nije utvrđena, uprkos tome što je dio medija tako izvještavao.

## Šta se desilo

Noam Shazeer, ko-vođa Gemini tima, prešao je u OpenAI oko 18. juna — potvrdio je to sam objavom na X-u, a prenijeli su CNBC, Axios i Fast Company. Dan kasnije, John Jumper, potpredsjednik DeepMind-a i ko-tvorac AlphaFold-a, objavio je prelazak u Anthropic; prenijeli su ga Bloomberg, TechCrunch i CNBC. Oba odlaska su dobro potvrđena, nezavisno od izvještaja o kašnjenju.

Tvrdnja o kašnjenju Gemini 3.5 Pro modela stoji na znatno slabijim nogama. Cijela priča vodi do jednog izvještaja Business Insider-a, distribuiranog kroz Reuters-ov newswire feed na TradingView-u — tekst je iza paywall-a i nije nezavisno provjeren u cijelosti. Google je u svom blogu do sada objavio postove o Gemini 3.5 Flash modelu, ali ništa o kašnjenju ili arhitektonskoj prepravci Pro verzije. Google-ov glasnogovornik je, prema sekundarnim izvještajima, "odbio komentar" — što nije potvrda, samo odsustvo demantija.

Prema više sekundarnih izvora, koji se ne mogu nezavisno potvrditi kao primarni, Gemini 3.5 Pro trenutno ostaje u ograničenoj fazi rane verzije (preview) za Vertex AI enterprise korisnike, uz testiranje na Antigravity i LMArena platformama.

## Zašto je važno

Za developere koji procjenjuju Gemini kao opciju, trenutni pristup je jasniji signal od bilo kakvog spekulisanog datuma: model je dostupan samo kroz ograničenu fazu rane verzije na Vertex AI, a ne u širokoj dostupnosti. Svaka procjena performansi trenutno je zasnovana na ograničenom uzorku enterprise testera, ne na produkcijskom releasu — vrijedi to imati na umu prije donošenja zaključaka o zrelosti modela.

Odlasci Shazeera i Jumpera ne treba tretirati kao dokaz da kasni baš ovaj model — poklapanje u vremenu nije isto što i uzročnost, a izvještaji koji tvrde suprotno oslanjaju se na istu slabu sekundarnu podlogu kao i sama tvrdnja o kašnjenju. Za developere koji procjenjuju Gemini kao dugoročnu opciju, relevantnije je ono što ovi odlasci mogu signalizirati o kontinuitetu tima: kada ko-vođa Gemini tima i potpredsjednik DeepMind-a napuste kompaniju u razmaku od jednog dana, to je razlog da pratite stabilnost plana razvoja i brzinu iteracije prije nego što produkcijsku arhitekturu vežete za jedan API — ne zato što to dokazuje kašnjenje, nego zato što utiče na predvidljivost onoga na šta se oslanjate.

## Šta to znači u praksi

Kada se tvrdnja o kašnjenju modela svodi na jedan neimenovani insajderski izvor, jedan paywalled članak i "odbijamo komentar" od vendora, to nije potvrda — to je materijal za oprez, ne za planiranje. Ne vežite integracije ili rokove za datum koji sam vendor nije potvrdio; pratite umjesto toga Google-ov zvanični blog i changelog za Vertex AI, gdje se stvarne promjene u dostupnosti prve vide.

To ne znači da odlasci istraživača nisu relevantni. U industriji gdje je koncentracija talenta direktno vezana za brzinu iteracije modela, kretanje ključnih ljudi između labova jeste podatak vrijedan praćenja. Ali tretirajte ga kao poseban signal o konkurentskoj dinamici, ne kao potvrdu za nepotvrđenu tvrdnju o kašnjenju — dva odvojena podatka ne postaju jedan dokaz samo zato što se poklapaju u vremenu.

## Izvori
- [Noam Shazeer na X-u — objava o prelasku u OpenAI](https://x.com/NoamShazeer/status/2067400851438932297)
- [CNBC — "Google Gemini co-lead Noam Shazeer leaves for OpenAI"](https://www.cnbc.com/2026/06/18/google-gemini-co-lead-noam-shazeer-leaves-for-openai.html)
- [Axios — "Top AI researcher leaves Google for OpenAI"](https://www.axios.com/2026/06/18/noam-shazeer-google-openai-characterai)
- [Fast Company — "Google AI leader Noam Shazeer leaves company for OpenAI"](https://www.fastcompany.com/91562193/google-ai-leader-noam-shazeer-leaves-company-for-openai)
- [John Jumper na X-u — objava o prelasku u Anthropic](https://x.com/JohnJumperSci/status/2068001285173834106)
- [Bloomberg — "Nobel Winner John Jumper to Leave Google DeepMind for Anthropic"](https://www.bloomberg.com/news/articles/2026-06-19/nobel-winner-john-jumper-to-leave-google-deepmind-for-anthropic)
- [TechCrunch — "Nobel laureate John Jumper is leaving DeepMind for rival Anthropic"](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/)
- [CNBC — "John Jumper to leave Google DeepMind for Anthropic"](https://www.cnbc.com/2026/06/19/john-jumper-to-leave-google-deepmind-for-anthropic.html)
- [TradingView (Reuters newswire, prema Business Insider-u) — "Google Delays Gemini 3.5 Pro Launch To July As It Tweaks Its New Frontier AI Model"](https://www.tradingview.com/news/reuters.com,2026:newsml_FWN42W0FW:0-google-delays-gemini-3-5-pro-launch-to-july-as-it-tweaks-its-new-frontier-ai-model-business-insider/)
