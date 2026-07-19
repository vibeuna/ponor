---
layout: post
title: "Nova pravila dizajna softverskih sistema"
date: 2026-07-18
category: ai-u-praksi
audience: developers
read_time: 16
description: "Produkcijski sistem danas se ne dizajnira samo tako da ga developer razumije, nego tako da ga AI agent može koristiti u cjelini. Šta to konkretno mijenja u arhitekturi i gdje ta logika prestaje da vrijedi."
image: /assets/images/2026-07-18-dizajn-za-agenta.svg
---

Prototip napravljen kroz vibe coding radi savršeno u demou i počne pucati čim ga pustite u produkciju. Poznata priča. Manje poznat je oblik koji ta priča ima 2026: sistem koji je AI agent mogao sastaviti za sat vremena, isti taj agent kasnije ne može održavati – jer ga više ne može ni pročitati u cjelini. Logika je razasuta po pet servisa, tri repozitorija i nekoliko konzola koje agent nikad ne vidi u istom kontekstu.

Teza ovog teksta je namjerno oštra: produkcijski sistem danas ne dizajnirate samo tako da ga developer razumije, nego tako da njime AI agent može upravljati u cjelini. Nije riječ o tome da agent piše kod umjesto vas. Riječ je o tome da agent – kroz svoj harness, sa svojim ograničenim kontekstom – bude sposoban da pročita sistem, promijeni ga i pokrene, bez da mu developer prethodno mora ručno sklopiti sliku iz deset izvora.

## Prototip koji agent napravi, ali ne može održavati

Klasičan razlog zašto vibe-coded prototip pada u produkciji je poznat: nedostaju rukovanje greškama, validacija, testovi, granični slučajevi. To se nije promijenilo. Promijenilo se to da je danas najproduktivniji "developer" na projektu često AI agent, a agent ima ograničenje koje čovjek nema na isti način: kontekstni prozor.

Čovjek gradi mentalnu mapu sistema kroz mjesece i drži je u glavi. Agent nema tu memoriju između sesija. Svaki put kreće od nule i rekonstruiše sistem iz onoga što u tom trenutku može pročitati. Ako je "istina" o tome kako sistem radi razbacana po polyrepou, ručno pisanom glue kodu i podešavanjima u tri različite cloud konzole, agent tu istinu ne može sastaviti. Napravit će izmjenu koja izgleda ispravno lokalno, a lomi nešto što nikad nije vidio.

To je nova dimenzija starog problema. Nije dovoljno da sistem bude ispravan – mora biti *čitljiv i upravljiv iz jednog konteksta*.

## Preokret: dizajnirajte za agenta, ne samo za developera

Dobra arhitektura oduvijek optimizuje za ljudsko razumijevanje: modularnost, jasne granice, dokumentacija. Dizajn za agenta ne poništava to – nego drugačije rangira prioritete. Tri svojstva odjednom postaju vrjednija nego prije:

- **Jedno mjesto za gledanje.** Agent treba da pronađe kako nešto radi u jednom prolazu kroz codebase, ne kroz šest sistema koje ne može istovremeno učitati.
- **Jedna površina za djelovanje.** Što je manje odvojenih mjesta na kojima se stanje i logika mijenjaju, to je manje površine koju agent može pogrešno pročitati.
- **Kontekst dohvatljiv u cjelini.** Ono što agentu treba da bi radio mora stati u domet njegovog harness-a – bez skrivenog znanja koje živi samo u nečijoj glavi ili u ručno klikanoj konfiguraciji.

Isti nagon vodi i izbor alata. Agent najbolje radi sa stvarima koje su bile guste u njegovim podacima za treniranje: široko korišteni, dobro dokumentovani servisi. Egzotičan, slabo dokumentovan alat tjera agenta da nagađa. To nije argument za slijepo praćenje popularnosti, nego trezveno priznanje da agentu "poznat" alat smanjuje broj grešaka. Praktične posljedice ovog preokreta razložit ćemo kroz pet konkretnih odluka.

## Monorepo je kontekst agenta

Prva odluka: svi klijenti i backend u jednom stablu. Monorepo agentu daje ono što polyrepo ne može – mogućnost da pretraži sistem s kraja na kraj i da refaktoriše preko granica atomično. Kad promjena API-ja na backendu dodiruje web klijent, mobilnu aplikaciju i desktop verziju, agent u monorepou to vidi i mijenja u jednom potezu. U polyrepou vidi samo repozitorij u kojem se trenutno nalazi.

Alat je ovdje sporedan – Turborepo (Vercel) je jedan popularan build sistem za monorepo sa keširanjem, ali princip ne zavisi od njega. Zavisi od toga da je granica sistema ujedno i granica onoga što agent može učitati.

Ovo nije univerzalno bolje, nego kompromis. Polyrepo daje nezavisno verzionisanje i čistije vlasništvo nad dijelovima – prednost kad više nezavisnih timova radi različitim ritmom. Monorepo daje kontekst po cijenu tooling-a i CI-ja koji na velikim stablima počinju da stenju. Za tim koji se oslanja na agente kao glavnu radnu snagu, kontekst obično vrijedi više. Za desetak nezavisnih timova sa vlastitim ciklusima izdavanja, ne mora.

## Jedan control plane, jedan izvor istine

Druga odluka: neka jedan autoritativan backend definiše i podatke i logiku. To je control plane (upravljački sloj) sistema – mjesto na kojem agent rezonuje o *jednoj* površini umjesto o njih N. Kad su podaci u jednoj bazi, poslovna logika u funkcijama uz tu bazu, a raspored poslova u istom sistemu, agent ima jedinstveni izvor istine o tome kako sistem radi.

{% include diagram.html name="dizajn-za-agenta" caption="Sve klijentske površine i izolovane usluge idu kroz jedan control plane; samo on dodiruje bazu, a klijent nikad direktno." alt="Hub-and-spoke dijagram: WEB, MOBILNI, DESKTOP, ADMIN i izolovani SANDBOX povezani su na centralni control plane (izvor istine), koji je jedini spojen na bazu iza njega; direktan pristup klijenta bazi je precrtan kao zabranjen." %}

Konkretan primjer takvog pristupa je Convex – upravljani backend (BaaS, Backend as a Service) u kojem su baza, funkcije i logika izraženi kao kod na jednom mjestu. Ali princip je vendor-neutralan. Alternativa je ručno sklapanje iz sirovih dijelova hyperscalera: baza na RDS-u, kompjut na EC2, redovi na SQS-u, sve povezano vlastitim glue kodom. Taj put daje maksimalnu kontrolu i minimalan vendor lock-in, ali plaća se površinom: više odvojenih sistema koje agent (i čovjek) mora držati usklađenim, i više mjesta na kojima se istina može razići.

Ovdje vrijedi jedno pojašnjenje kao istorijski okvir, ne kao specifikacija: mnogi "developer-friendly" upravljani servisi su nastali kao sloj apstrakcije nad sirovim cloudom – Vercel nad AWS-om, PlanetScale nad MySQL-om i Vitessom. To olakšava rad, ali "to je samo wrapper" je nepotpuna slika: PlanetScale danas nudi i vlastitu infrastrukturu (Metal), pa granica između "wrappera" i "vlastite platforme" nije čvrsta. Poentu tretirajte kao narativ o tome odakle ti alati dolaze, ne kao tvrdnju o tome šta tačno jesu danas.

## Klijent nikad ne dodiruje bazu

Treća odluka je stara mudrost koju agentni svijet čini još važnijom: klijent nikad ne razgovara direktno s bazom. Tok je uvijek klijent → server → baza → server → klijent. Sav pristup podacima prolazi kroz jednu tačku, i time na jednom mjestu kupujete autentifikaciju, validaciju i observability (uvid u rad sistema).

To je svjestan izbor naspram suprotnog obrasca koji nude neki BaaS sistemi (Supabase, Firebase), gdje klijent dobija ključ i piše u bazu direktno, a sigurnost se drži pravilima pristupa na nivou reda (RLS). Taj pristup je brz za prototip, ali raspršuje mjesto na kojem se odluke o pristupu donose. Jedna tačka prolaza znači da agent – kad treba da doda provjeru prava ili da uđe u trag problemu – ima tačno jedno mjesto koje mora razumjeti.

Uz to ide i način na koji klijent dobija podatke. Convexovi upiti su, na primjer, reaktivni po defaultu: umjesto da klijent ispituje server u petlji, upiti u realnom vremenu (real-time queries) se sami ponovo izvršavaju kad se podaci na koje se oslanjaju promijene. To nije nužno za argument o control planeu, ali smanjuje količinu ručne sinhronizacije koju bi agent inače morao napisati i održavati.

## Trajno izvršavanje za agente koji nadžive sesiju

Četvrta odluka tiče se poslova koji traju duže od jednog zahtjeva. Agent koji istražuje, generiše kod, testira ga pa ispravlja može raditi minutama ili satima, i mora preživjeti restart servera, timeout i privremeni pad vanjskog API-ja. Za to postoji trajno izvršavanje (durable execution): izvršavanje modelovano kao mašina stanja koja se perzistira, nastavlja tačno tamo gdje je stala, garantuje da se korak izvrši tačno jednom i automatski ponavlja korake koji padnu.

Uz to ide red zadataka koji kontroliše koliko poslova ide paralelno. Convex ovo nudi kroz komponente `workflow` (trajno izvršavanje sa podesivim ponovnim pokušajima po koraku) i `workpool` (red zadataka koji ograničava paralelizaciju (parallelization) da vam sto agenata odjednom ne obori vanjski servis). Standardne alternative za isti posao su Temporal i AWS Step Functions, a u najjednostavnijem obliku ručno sklopljen red zadataka plus cron. Izbor alata je otvoren; ono što nije opciono, ako gradite agente koji nadžive sesiju, jeste da ovo stanje bude eksplicitno i trajno, a ne implicitno u memoriji procesa koji svaki restart briše.

Ovdje obično žive i cloud agenti – agenti koji rade na serverima, ne na korisnikovom uređaju – jer upravo njima treba izvršavanje koje preživljava prekide.

## Izolovane usluge: svaki agent u svom sandboxu

Peta odluka: kad agent izvršava kod koji je sam generisao, taj kod ide u izolovano okruženje, ne u vaš glavni proces. Sandbox ograničava domet štete – agentov pogrešan `rm -rf` ili beskonačna petlja ostaju unutar svojih zidova.

Daytona je jedan primjer: docker-izolovani, stateful sandboxi koji se, po podacima proizvođača, pokreću za manje od 90 ms preko SDK-a, namijenjeni baš izvršavanju AI-generisanog koda. (Latencije koje proizvođači navode tretirajte kao marketinški podatak dok ih sami ne izmjerite.) U svom tutorijalu Ras Mic pokazuje i primjer u kojem agent koristi snimak ekrana sandboxa da sam ispravi grešku – to je njegova demonstracija toka rada, ne dokumentovana sposobnost samog alata, pa je i tretirajte tako.

Princip je opet nezavisan od alata i poznat iz sigurnosti: izolacija ograničava blast radius. Sandbox je za agenta ono što je zaštitna ograda za autonomiju – mehanizam koji autonomiju čini prihvatljivom time što joj ograničava domet.

## Iskreni kompromisi: kada ovo NE raditi

Sve gore ima cijenu, i pošten prikaz mora je izložiti eksplicitno.

**Vendor lock-in.** Backend izražen kao kod uz proprietarne komponente je ugodan dok ste unutra, ali semantika trajnog izvršavanja i reaktivnih upita ne prenosi se čisto na drugi sistem. Migracija nije `export`/`import` – to je ponovno pisanje. Što se dublje oslonite na jedan upravljani backend, to je izlaz skuplji.

**Trošak na skali.** Upravljane usluge se naplaćuju po metrima koji se množe: po aktivnom korisniku, po konekciji, po pozivu funkcije, po minuti sandboxa. Na niskom i srednjem obimu to je jeftinije od tima koji održava vlastitu infrastrukturu. Na visokom, stabilnom obimu sirovi cloud kod hyperscalera gotovo uvijek postane jeftiniji. Tvrdnja "skaliranje je samo nadogradnja plana, ne ponovna arhitektura" vrijedi unutar sretnog scenarija – tretirajte je kao stav, ne kao garanciju.

**Kad sirovi cloud pobjeđuje.** Teška ili specifična infrastruktura, stroga rezidencija podataka, postojeći platformski tim i predvidivo opterećenje su uslovi u kojima kontrola nad sirovim slojem vrijedi više od udobnosti upravljanog. Isto vrijedi i kad vam treba specifično rubno raspoređivanje (edge) sa zahtjevima koje upravljani sloj ne pokriva.

**Kad monorepo smeta.** Mnogo nezavisnih timova sa različitim ritmom izdavanja, ili ogroman repozitorij koji davi tooling i CI – tu prednost konteksta ne nadoknađuje operativnu cijenu, i polyrepo je iskreniji izbor.

**Prekomjerna apstrakcija.** Svaki sloj apstrakcije je još jedna stvar koja može pući i još jedan sloj kroz koji se debugira. "To je samo wrapper" vrijedi tačno do trenutka dok ne udarite u plafon wrappera – tada plaćate i apstrakciju i probijanje kroz nju.

Nekoliko konkretnih komponenti pokazuje i korist i zamku ovog pristupa. Auth se danas rijetko piše ručno: WorkOS, na primjer, nudi AuthKit besplatno do reda veličine milion mjesečnih korisnika, plus SSO, SCIM, audit logove i MFA – gradivne blokove koji pomažu *vašim klijentima* da prođu SOC 2 reviziju (to nije certifikat samog WorkOS-a). Ali SSO se naplaćuje po konekciji (reda ~125 USD mjesečno), pa "besplatno" ima granicu. Naplatu preuzimaju komponente poput Autumna (kreditni i potrošni modeli nad Stripeom), review pull requestova radi Greptile (ocjena pouzdanosti po komentaru), a pristup modelima unificira OpenRouter sa failoverom preko više provajdera. Svaka je legitiman način da agentu date "poznat" gradivni blok umjesto ručnog koda. Svaka je i još jedan vendor u vašem lock-in računu.

## Zaključak

Dizajn za agenta nije nova metodologija koju treba kupiti – to je pomak u tome za koga optimizujete. Monorepo, jedan control plane, klijent koji ne dira bazu, trajno izvršavanje i izolovani sandbox nisu tu zato što su moderni, nego zato što svaki od njih smanjuje broj odvojenih površina koje agent mora držati u glavi odjednom. To su ujedno i obrasci dobrog inženjeringa; agent ih samo čini manje opcionim.

Kao i sa svakim arhitektonskim izborom, pravi potez je izložiti kompromis, ne slijediti modu. Ako gradite sistem u kojem agent radi najveći dio posla, dizajnirajte tako da ga agent može pročitati i pokrenuti u cjelini. Ako ne – ako imate platformski tim, predvidivo opterećenje i razloge da držite kontrolu nad sirovim slojem – onda vas ista logika vodi u suprotnom smjeru, i to je jednako ispravno.

## Izvori

- [Convex – Workflows (durable execution) dokumentacija](https://docs.convex.dev/agents/workflows)
- [Convex – Workflow komponenta](https://www.convex.dev/components/workflow)
- [Convex – Workpool komponenta (Stack)](https://stack.convex.dev/advanced-serverless-queuing-with-workpool-component)
- [Convex – cijene i besplatni tier](https://www.convex.dev/pricing)
- [Daytona – GitHub repozitorij](https://github.com/daytonaio/daytona)
- [Daytona – zvanična stranica](https://www.daytona.io)
- [Autumn – Convex komponenta za naplatu](https://www.convex.dev/components/autumn)
- [WorkOS – User Management / AuthKit](https://workos.com/user-management)
- [WorkOS – cijene](https://workos.com/pricing)
- [Greptile – AI PR review dokumentacija](https://www.greptile.com/docs/code-review/first-pr-review)
- [Temporal – durable execution platforma](https://temporal.io)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [OpenRouter – unificirani pristup modelima](https://openrouter.ai)
- [Ras Mic – video tutorijal (YouTube)](https://www.youtube.com/watch?v=4jy0T98dYoI)
