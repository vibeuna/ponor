---
layout: post
title: "EU AI Act: šta svaka kompanija mora znati prije augusta 2026"
date: 2026-06-26
category: ai-u-praksi
audience: businesses
read_time: 5
description: "Šta je EU AI Act, šta spada pod njegovu regulativu, i koji rokovi zahtijevaju akciju - praktični pregled za poslovne ljude."
diagram: /assets/diagrams/2026-06-22-eu-ai-act-article.svg
image: /assets/images/2026-06-22-eu-ai-act-article.svg
---

Od februara 2025. godine, jedan dio EU AI Act-a već je na snazi i nosi konkretne zabrane. Do Augusta 2026., najveći dio regulacije postaje obavezan za kompanije koje koriste ili razvijaju AI sisteme na tržištu Evropske unije. Ako niste sigurni spada li vaše poslovanje pod ova pravila - ovaj tekst odgovara na to pitanje.

## Šta je EU AI Act

EU AI Act (Regulation (EU) 2024/1689) je prva sveobuhvatna i pravno obavezujuća regulativa o vještačkoj inteligenciji na svijetu. Europski parlament i Vijeće usvojili su je i objavili u Službenom listu EU 12. Jula 2024. Na snagu je stupila 1. Augusta 2024., no sam taj datuma nije donio nikakve neposredne obaveze - regulativa se primjenjuje fazno, kroz četiri ključna roka.

Regulativa vrijedi u svim državama članicama EU bez potrebe za nacionalnim zakonima koji bi je prenosili. Za kompanije izvan EU: ako vaš AI sistem stavljate na tržište EU, ili ako se rezultati vašeg sistema koriste u EU, pravila se primjenjuju i na vas.

Pristup nije "sve ili ništa". Regulativa dijeli AI sisteme u kategorije prema riziku koji nose - i obaveze rastu proporcionalno tom riziku.

## Četiri kategorije: gdje se vaša kompanija vjerovatno nalazi

**Zabranjeni AI sistemi** su u potpunosti isključeni s tržišta EU od Februara 2025. Primjeri koje regulativa eksplicitno navodi: sistemi za social scoring (rangiranje ili klasifikacija građana od strane javnih vlasti na osnovu njihovog ponašanja), određene tehnike manipulacije koje zaobilaze svjesnu odluku korisnika, te sistemi za prepoznavanje emocija na radnom mjestu ili u obrazovnim institucijama u određenim kontekstima. Ova kategorija ne tiče se većine komercijalnih kompanija - ali je važna za svakoga ko razvija ili razmatra primjenu AI-ja u javnom sektoru ili sigurnosnim kontekstima.

**High-risk AI sistemi** nose najveći teret usklađenosti za kompanije koje ih razvijaju. Sektori koje regulativa taksativno navodi uključuju: biometriju, kritičnu infrastrukturu, obrazovanje i stručno osposobljavanje, upravljanje radnom snagom i zapošljavanje, ključne privatne i javne usluge (uključujući procjenu kreditne sposobnosti), provođenje zakona, migraciju i upravljanje pravosudnim postupcima.

**Sistemi s ograničenom transparentnošću** (primjer: chatbotovi koji komuniciraju s ljudima) imaju jednu konkretnu obavezu: korisnik mora biti obaviješten da razgovara s AI sistemom.

**Minimalni rizik** - spam filteri, sistemi preporuka, alati za prijevod, standardni chatbotovi koji ne donose odluke s pravnim ili sličnim efektima - ne nose nikakve obavezne zahtjeve usklađenosti. Ovdje se nalazi najveći dio AI alata koje kompanije danas svakodnevno koriste.

{% include diagram.html name="2026-06-22-eu-ai-act-article" caption="EU AI Act dijeli AI sisteme u četiri kategorije rizika, s različitim obavezama i rokovima za svaku." alt="Dijagram četiri kategorije EU AI Act-a: zabranjeni AI sistemi, high-risk, ograničena transparentnost i minimalni rizik" %}

## Provider ili deployer: koja je vaša uloga

Ovo je razlika koja određuje koliko obaveza pada na vas.

**Provider** je svaka kompanija ili osoba koja razvija AI sistem ili General Purpose AI (GPAI) model i plasira ga na tržište pod vlastitim imenom - neovisno o tome naplaćuje li ga ili nudi besplatno. Provider ste i ako preuzimate tuđi AI sistem i stavljate ga na tržište pod vlastitim brendom, ili ako pravite značajne izmjene u postojećem sistemu. Obveze providera su opsežne: conformity assessment prije plasmana, tehnička dokumentacija, registracija, upravljanje rizicima, post-market nadzor.

**Deployer** je svaka kompanija koja koristi AI sistem pod vlastitim ovlastima u profesionalnom kontekstu. Ako vaš HR tim koristi alat trećih strana za probir životopisa, vi ste deployer. Ako banka koristi kreditni scoring softver koji je razvio vendor - banka je deployer. Obaveze deployera high-risk sistema su realne, ali uže: pratiti upute za upotrebu, implementirati ljudski nadzor, čuvati logove najmanje 6 mjeseci, prijavljivati rizike nadležnim tijelima.

Bitna napomena: ova podjela nije uvijek jednoznačna u praksi. Kompanija koja fine-tunes (podešava) tuđi model za vlastitu upotrebu može preuzeti provider obaveze, ovisno o opsegu modifikacija.

## Praktični vremenski okvir: šta do kada

| Datum | Šta stupa na snagu |
|---|---|
| 2. Februar 2025. | Zabranjeni AI sistemi (član 5) + obaveze AI pismenosti (član 4) |
| 2. August 2025. | GPAI obaveze (Poglavlje V) + uspostava tijela za nadzor + pravila o sankcijama |
| 2. August 2026. | Opća primjena: većina high-risk obaveza, uključujući sve Annex III sisteme |
| 2. August 2027. | High-risk sistemi ugrađeni u regulirane proizvode (medicinski uređaji, strojevi); GPAI modeli plasirani prije Augusta 2025. |

Za većinu kompanija, August 2026. je ključni rok. Do tada moraju biti usklađeni oni koji razvijaju ili profesionalno koriste high-risk AI sisteme iz Annex III kategorija (zapošljavanje, kreditni scoring, obrazovanje itd.).

Rok 2027. odnosi se specifično na high-risk sisteme ugrađene u već regulirane proizvode (npr. softver koji je sigurnosna komponenta medicinskog uređaja ili mašinerije). Ova razlika između Annex I i Annex III kategorija zahtijeva provjeru s pravnim savjetnikom za kompanije u tim sektorima.

## Koga regulativa NE pogađa direktno

Ovo je jednako važno kao i lista koga pogađa.

Fizička lica koja koriste AI u čisto privatne svrhe nisu subjekti regulacije. Kompanije koje koriste isključivo alate minimalnog rizika - standardne chatbotove, filtere neželjene pošte, alate za prijevod, sisteme preporuka koji ne donose pravno relevantne odluke - nemaju obaveznih zahtjeva.

Istraživanje i razvoj prije plasmana na tržište ima određena izuzeća, uz uvjete.

Što se tiče malih i srednjih preduzeća: ne postoji kategorijalni izuzetak za veličinu kompanije. Ako razvijate ili koristite high-risk AI sistem, veličina vaše kompanije ne eliminira obavezu. Regulativa predviđa određene olakšice (pristup regulatornim sandbox okruženjima, pojednostavljena dokumentacija), ali sam prag obaveze nije niži.

## Najčešće zablude koje skupo koštaju

**"Regulativa zabranjuje AI u zapošljavanju."** Netačno. Klasificira AI sisteme za upravljanje radnom snagom kao high-risk - što znači conformity assessment i dokumentacija, ne zabrana.

**"Sve kompanije koje koriste AI moraju biti usklađene."** Netačno. Samo provideri i deployeri AI sistema koji spadaju u regulirane kategorije rizika. Kompanija koja koristi isključivo alate minimalnog rizika nema nikakvih mandatornih obaveza.

**"Open-source AI je potpuno izuzet."** Netačno. Ovo se odnosi na GPAI modele otvorenog koda: izuzeti su od većine obaveza Poglavlja V, ali ne od zahtjeva vezanih za autorska prava i podatke za treniranje; prag sistemskog rizika primjenjuje se bez obzira na licencu.

## Šta napraviti do augusta 2026.

Konkretni koraci za kompanije koje još nisu počele:

1. **Mapirajte AI sisteme koje koristite ili razvijate.** Za svaki sistem utvrdite: je li to high-risk kategorija po Annex III? Jeste li provider ili deployer?
2. **Provjerite obaveze deployera za high-risk sisteme.** Čak i ako ne razvijate AI, ako ga koristite u HR-u, kreditnom ocjenjivanju ili sličnim domenima - imate konkretne obaveze.
3. **Angažirajte pravnog savjetnika za granične slučajeve.** Posebno za Annex I / Annex III distinkciju, za situacije gdje postoji nesigurnost o ulozi (provider ili deployer), i za kompanije koje vrše izmjene tuđih AI sistema.

Regulativa je već dijelom aktivna. August 2026. nije daleko.

---

*Napomena: Ovaj tekst je informativni pregled EU AI Act-a i ne predstavlja pravni savjet. Za ocjenu konkretnih obaveza vaše kompanije, konsultujte pravnog savjetnika.*

## Izvori

- [Regulation (EU) 2024/1689 — Official Journal text, EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng)
- [Article 113 — Applicability timeline (annotated)](https://artificialintelligenceact.eu/article/113/)
- [Implementation timeline summary](https://artificialintelligenceact.eu/implementation-timeline/)
- [European Commission — Regulatory Framework for AI](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [Annex III — High-risk AI categories](https://artificialintelligenceact.eu/annex/3/)
- [Article 5 — Prohibited AI practices](https://artificialintelligenceact.eu/article/5/)
