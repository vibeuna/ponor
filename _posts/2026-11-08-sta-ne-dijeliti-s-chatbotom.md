---
layout: post
title: "Šta ne lijepiti u chatbot i šta se s tim dešava"
date: 2026-11-08
category: ai-za-sve
image: /assets/images/2026-11-08-sta-ne-dijeliti-s-chatbotom.svg
read_time: 7
description: "Brisanje razgovora, isključivanje treniranja i ljudski pregled nisu isto. Šta kažu ChatGPT, Claude i Gemini i šta ne lijepiti u chatbot."
tags: [llm]
---

Nalaz iz laboratorije, ugovor o radu, poruka kolegi: takve tekstove ljudi kopiraju u [chatbot](/rjecnik/chatbot/) da bi dobili sažetak. Šta se s tekstom poslije dešava, zavisi od tri odvojena pitanja.

## Ukratko

Brisanje razgovora, isključivanje [treniranja](/rjecnik/treniranje/) (training) i ljudski pregled su tri različite stvari, a jedna postavka obično ne rješava sva tri pitanja. Prema stranicama koje je Ponor pročitao od 8. do 15. 11. 2026, ChatGPT na ličnim planovima po zadanim postavkama koristi razgovore za treniranje, a Gemini ih koristi za razvoj usluga dok je uključen Keep Activity. Kod Claudea korisnik [bira pri registraciji](https://www.anthropic.com/news/updates-to-our-consumer-terms), a stranice pomoći ne navode zadani položaj prekidača. Zato u chatbot ne lijepite identifikatore, zdravstvene podatke, lozinke, tuđe podatke ni radne dokumente. To su tvrdnje proizvođača, ne revizija.

## Po čemu se razlikuju brisanje, treniranje i ljudski pregled?

Tri stanja se lako pomiješaju.

**Obrisano iz vašeg prikaza.** Razgovor nestaje iz historije, ali kopija može ostati na serverima. Anthropic navodi da se obrisan razgovor odmah uklanja iz historije, a iz pozadinskih sistema u roku od 30 dana. Google navodi da se razgovori koje su pregledali ljudi čuvaju do tri godine i da se ne brišu kad obrišete svoju aktivnost.

**Nije korišteno za treniranje.** Isključena opcija znači da proizvođač razgovor ne koristi za treniranje modela. Ne znači da je razgovor obrisan. OpenAI izričito navodi da isključivanje treniranja ne briše razgovore. Isključivanje ne djeluje unazad na ono što je model već naučio: Anthropic piše da podaci koji su već ušli u istrenirani model ostaju u njemu, a treniranja koja su u trenutku promjene već u toku nastavljaju s tim podacima.

**Ne vide ljudi.** Sva tri proizvođača navode da ljudi mogu vidjeti dio razgovora. Razlikuju se po tome koliko o tome pišu i šta mijenja isključeno treniranje. Google piše da ljudski recenzenti pregledaju podskup razgovora. Googleove postavke ne upravljaju anonimiziranim podacima ni sigurnosnom obradom, pa i s isključenim Keep Activity Google razgovore obrađuje, uz pomoć ljudskih recenzenata, radi zaštite Googlea, korisnika i javnosti. [OpenAI navodi](https://help.openai.com/en/articles/7039943-how-openai-handles-data-in-consumer-services) da ograničen broj ovlaštenih zaposlenika i pouzdanih pružalaca usluga može pristupiti sadržaju razgovora radi istrage zloupotrebe ili sigurnosnog incidenta, podrške, pravnih pitanja i, ako niste isključili treniranje, poboljšanja modela. [Anthropic navodi](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations) da razgovore za koje ste dozvolili treniranje prije svakog pregleda odvaja od vašeg korisničkog ID-a i da im pristupa mali broj osoba koje rade na treniranju. Razgovore označene za sigurnosni pregled Anthropic može koristiti i analizirati bez obzira na postavku. Google i OpenAI izričito traže da ne unosite podatke koje ne biste željeli da neko pregleda.

Postoji i izuzetak koji važi uprkos isključenom treniranju. Kod OpenAI-ja i Anthropica povratna ocjena (palac gore ili dolje) može cijeli razgovor učiniti dostupnim za treniranje, i kad ste ga isključili. Kod OpenAI-ja zasebne postavke imaju i glasovni način i Codex okruženja, a program Trusted Access može koristiti sadržaj i kad je treniranje isključeno. Kod Googlea, uz isključen Keep Activity, povratna informacija znači da Google koristi i kontekst, uključujući razgovore iz posljednja 24 sata. Takve povratne informacije i pripadajuće razgovore pregledaju posebno obučeni timovi i čuvaju ih do 3 godine, odvojeno od Google računa.

{% include diagram.html name="sta-ne-dijeliti-s-chatbotom" caption="Brisanje, treniranje i ljudski pregled su tri odvojena pitanja; jedna postavka obično ne rješava sva tri." alt="Dijagram: poruka zalijepljena u chatbot prolazi kroz tri odvojena pitanja, brisanje, treniranje i ljudski pregled. Jedna postavka obično ne rješava sva tri, pa ono što pošaljete kontrolišete samo djelimično." %}

## Šta kaže koji proizvođač?

Tabela sažima ono što su stranice za lične planove (ChatGPT Free, Plus i Pro; Claude Free, Pro i Max, a novije stranice pomoći navode i Ultra; Gemini Apps) govorile od 8. do 15. 11. 2026. Stranice se mijenjaju: Googleova je označena kao ažurirana 26. 10. 2026. "Privremeni razgovor" u tabeli je Temporary Chat kod OpenAI-ja i Googlea, a Incognito kod Anthropica.

| | Treniranje | Privremeni razgovor | Čuvanje |
|---|---|---|---|
| OpenAI | Uključeno po zadanim postavkama | Temporary Chat: ne koristi se za treniranje, nema historije, ne pravi i ne mijenja pamćenje (u načinu Personalized može koristiti postojeće); može se čuvati do 30 dana iz sigurnosnih razloga | Sačuvani razgovori ostaju dok ih ne obrišete. [Obrisani](https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt): iz prikaza odmah, iz sistema zakazano brisanje u roku od 30 dana, osim ako ih OpenAI mora zadržati iz sigurnosnih ili pravnih razloga ili su već odvojeni od računa. Isključivanje treniranja ne briše razgovore |
| Anthropic | Koristi se ako korisnik to dozvoli; bira se pri registraciji, zadani položaj prekidača nije naveden | [Incognito](https://support.claude.com/en/articles/12260368-use-incognito-chats): ne koristi se za treniranje čak ni kad je postavka uključena, ne ulazi u historiju ni pamćenje; čuva se 30 dana | Obrisano: iz historije odmah, iz pozadine do 30 dana. Treniranje dozvoljeno: do 5 godina, odvojeno od korisničkog ID-a, za nove ili nastavljene razgovore nakon uključivanja. Povratna ocjena: cijeli razgovor do 5 godina. Označeno zbog kršenja pravila: do 2 godine, a ocjene klasifikatora do 7 godina |
| Google | Keep Activity uključen: aktivnost se koristi za razvoj usluga, uključujući treniranje generativnih AI modela. Keep Activity isključen i bez povratne ocjene: buduće razgovore Google ne koristi za poboljšanje svojih AI modela | Temporary chats i isključen Keep Activity: čuva se uz račun 72 sata, ne koristi se za treniranje | Automatsko brisanje: 3, 18 (zadano), 36 mjeseci ili nikad. Razgovori koje su pregledali ljudi: do 3 godine, odvojeno od računa |

Postavke ne pokrivaju sve. Kod OpenAI-ja isključeno pamćenje ne isključuje ograničen, sigurnosno relevantan kontekst u rijetkim visokorizičnim situacijama. Planovi Business, Enterprise i Edu te API (programski interfejs) kod OpenAI-ja po zadanim postavkama nisu u treniranju; za druge proizvođače to Ponor nije čitao.

## Šta ne treba lijepiti u chatbot?

Pravilo prati tabelu: ono što jednom pošaljete, kontrolišete samo djelimično.

- **Podatke kojima se možete identifikovati.** Ime, identifikacioni broj, podaci o lokaciji ili mrežni identifikator. Zakon (član 4) ih navodi kao primjere identifikatora.
- **Zdravlje i druge posebno zaštićene podatke.** Nalazi i dijagnoze te druge kategorije koje zakon zasebno izdvaja (vidi niže).
- **Lozinke i ključeve.** Pristupni podaci i API ključevi.
- **Tuđe podatke.** Poruku prijatelja, dosije klijenta, snimak razgovora s kolegom. Te osobe nisu u razgovoru i ne mogu odlučiti šta će se s njihovim podacima desiti.
- **Radne dokumente.** Tabele klijenata, ugovore, izvorni kod firme. Provjerite pravila poslodavca. OpenAI za poslovne planove navodi drugačija pravila (vidi iznad); na ličnom ChatGPT planu ta zadana zaštita ne postoji.

Ako vam model ipak treba za osjetljiv tekst, postoji drugi put: [lokalni model](/rjecnik/lokalni-model/), koji se pokreće na vašem računaru. [Ollama u svom FAQ-u](https://github.com/ollama/ollama/blob/main/docs/faq.mdx) navodi da ne vidi [promptove](/rjecnik/prompt/) ni podatke korisnika kad radite lokalno. To je tvrdnja firme. Funkcije u oblaku Ollama se mogu isključiti (postavka `OLLAMA_NO_CLOUD=1`); [model u oblaku](/rjecnik/model-u-oblaku/) obrađuje prompt na Ollaminim serverima.

## Kako podesiti postavke?

Koraci su provjereni od 8. do 15. 11. 2026. Imena opcija ostavljamo onako kako ih pišu stranice.

**ChatGPT.** Settings > Data controls > "Improve the model for everyone", isključiti. Alternativa je "Do not train on my content" u Privacy Portalu; dovoljna je jedna od dvije. Promjena važi za nove razgovore. Za jednokratan upit koristi se Temporary Chat. Pamćenje je zasebna postavka.

**Claude.** Settings > Privacy > "Help Improve our AI models", isključiti. Na mobilnom je put isti: ime u meniju, Settings, Privacy. Za jednokratan upit služi Incognito. Imajte na umu rok od 5 godina ako je treniranje dozvoljeno, i da povratna ocjena produžava čuvanje cijelog razgovora. [Pamćenje](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context) je na Free, Pro, Max i Ultra planovima uključeno po zadanim postavkama; isključuje se u Settings > Your Claude > "Generate memory from chats", a za jedan razgovor u meniju "+" > "Memory".

**Gemini.** U Gemini Apps Activity isključite Keep Activity ili podesite automatsko brisanje aktivnosti (zadano 18 mjeseci; može 3 ili 36 mjeseci ili bez automatskog brisanja); to je rok čuvanja aktivnosti, a ne zasebna postavka treniranja. Audio te video i dijeljenje ekrana iz Gemini Live imaju zasebnu postavku i po zadanim postavkama se ne koriste za poboljšanje Googleovih usluga. Sažetak pamćenja (Memory summary) možete pregledati, urediti ili isključiti; za razgovor koji Gemini ne treba pamtiti koristite Temporary chat.

## Šta o tome kaže zakon u BiH?

Ovo nije pravni savjet. Ponor je od 8. do 15. 11. 2026. pročitao tekst Zakona o zaštiti ličnih podataka (Službeni glasnik BiH 12/25) i ponavlja samo ono što stoji u njemu.

- Član 1(2): zakonom se vrši usklađivanje s odredbama GDPR-a, Uredbe (EU) 2016/679, i Direktive (EU) 2016/680.
- Član 6(2): zakon se primjenjuje i na obradu podataka osoba u BiH koju vrši kontrolor ili obrađivač podataka (firma koja odlučuje o obradi ili obrađuje podatke za drugoga) bez sjedišta u BiH, ako je obrada povezana s nuđenjem roba ili usluga tim osobama, uz naplatu ili bez nje, ili s praćenjem njihovog ponašanja u BiH.
- Član 11(1): obrada posebnih kategorija podataka je zabranjena, uz izuzetke iz člana 11(2), među kojima je izričit pristanak, osim kad poseban zakon propisuje da se obrada ne može zasnivati na pristanku. Kategorije su rasno ili etničko porijeklo, politička mišljenja, vjerska ili filozofska uvjerenja, članstvo u sindikatu, genetski podaci, biometrijski podaci za jedinstvenu identifikaciju, podaci o zdravlju i podaci o seksualnom životu ili orijentaciji.
- Zakon je [objavljen u Službenom glasniku BiH 12/25 od 28. 2. 2025.](https://csd.pravosudje.ba/vstvfo/B/142/article/145996) Stupa na snagu osmog dana od objave, a primjenjuje se nakon isteka 210 dana od stupanja na snagu (član 120), tj. od oktobra 2025.

Ponor nije procjenjivao da li potrošačke chat usluge ChatGPT-a, Claudea i Geminija potpadaju pod član 6(2), niti šta bi iz toga slijedilo za vaša prava prema proizvođaču. To pitanje traži pravnika.

## Povezano

- [Vlastiti AI chatbot na računaru: Ollama vodič od nule](https://www.ponor.ba/clanci/vlastiti-ai-chatbot-ollama-vodic/) – opisuje lokalni model kao način da promptovi ostanu na vašem računaru
- [Koji AI najbolje prevodi na bosanski?](https://www.ponor.ba/clanci/ai-prevod-bosanski/) – poređenje DeepL-a, Google Translatea i ChatGPT-a, uz kratku provjeru privatnosti svakog od njih

## Izvori

- [How your data is used to improve model performance – OpenAI](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
- [Data controls in ChatGPT – OpenAI](https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt)
- [How OpenAI handles data in consumer services – OpenAI](https://help.openai.com/en/articles/7039943-how-openai-handles-data-in-consumer-services)
- [Chat and file retention in ChatGPT – OpenAI](https://help.openai.com/en/articles/8983778-chat-and-file-retention-in-chatgpt)
- [Updates to our consumer terms – Anthropic](https://www.anthropic.com/news/updates-to-our-consumer-terms)
- [Is my data used for model training? – Anthropic Privacy Center](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- [How long do you store my data? – Anthropic Privacy Center](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)
- [Who can view my conversations? – Anthropic](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations)
- [Use incognito chats – Anthropic](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- [Use Claude's chat search and memory – Anthropic](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
- [Gemini Apps Privacy Hub – Google](https://support.google.com/gemini/answer/13594961)
- [Zakon o zaštiti ličnih podataka, Službeni glasnik BiH 12/25](https://bhas.gov.ba/data/Dokumenti/pdf/Zakon_o_zastiti_licnih_podataka_12-25_BS.pdf)
- [Zakon o zaštiti ličnih podataka, Službeni glasnik BiH 12/25 – Centar za sudsku dokumentaciju VSTV-a](https://csd.pravosudje.ba/vstvfo/B/142/article/145996)
- [Uredba (EU) 2016/679 (GDPR) – EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
