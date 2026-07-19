---
layout: post
title: "NotebookLM postaje Gemini Notebook: Google dodaje izvršavanje koda i dublju integraciju"
date: 2026-07-20
category: ai-u-praksi
image: /assets/images/2026-07-20-gemini-notebook.svg
audience: businesses
read_time: 9
description: "Google je preimenovao NotebookLM u Gemini Notebook i dodao izvršavanje koda nad vašim izvorima. Objašnjavamo šta to mijenja za poslovnu analizu dokumenata, ko ima pristup i gdje su stvarne granice."
---

Google je 16. jula 2026. preimenovao NotebookLM u "Gemini Notebook" i istovremeno dodao mogućnost da alat samostalno piše i izvršava kod nad vašim vlastitim izvorima. Za firme koje razmišljaju kako organizovati internu analizu dokumenata, promjena imena je manje bitna od dvije stvari ispod nje: šta alat sada radi i ko mu ima pristup. Google navodi da alat koristi 30 miliona ljudi i preko 600.000 organizacija, ali te brojke dolaze bez definicije šta se računa kao aktivni korisnik, pa ih treba čitati kao vendorovu procjenu, a ne kao neutralan podatak.

## Šta se desilo

Preimenovanje je stupilo na snagu 16. jula. Gemini Notebook ostaje zaseban proizvod, ali se sada formalno vezuje za Gemini brend i ekosistem. Konkretno, notebook-e sada možete kreirati i otvarati unutar Gemini aplikacije, uz sinhronizaciju između aplikacija, tako da isti izvori i bilješke prate korisnika kroz Google okruženje. Google najavljuje i da će notebook-i "uskoro" biti dostupni i u AI Mode režimu unutar Search-a, ali za to nema datuma i funkcija još nije isporučena.

Odvojeno od preimenovanja, Google uvodi ono što naziva "secure cloud computer" po svakom notebook-u. To je mehanizam koji omogućava da alat piše i izvršava kod direktno, radi, kako Google kaže, "kompleksne analize podataka utemeljene na vašim izvorima". Ranije audio i "study" funkcije NotebookLM-a ostaju nepromijenjene; ovo je dodatak, ne zamjena.

Za poslovnog korisnika bitna je razlika između ta tri sloja najave: preimenovanje je gotova stvar, izvršavanje koda se stvarno isporučuje (o rasporedu pristupa niže), a integracija u Search je za sada obećanje na mapi puta.

## "Secure cloud computer": šta to zapravo znači

"Secure cloud computer" je Googleov marketinški naziv za ono što je tehnički sandbox (izolovano okruženje za izvršavanje koda) vezan za pojedinačni notebook. Umjesto da samo generiše tekstualni odgovor o vašim podacima, alat u tom sandboxu može napisati kod, pokrenuti ga i vratiti rezultat, sve unutar granica koje to okruženje postavlja.

Dvije stvari je ovdje važno razdvojiti. Prvo, ovo je runtime (izvršno okruženje) za kod, a ne promjena samog modela. Sposobnost izvršavanja koda ne znači da je ispod novi ili jači model; to je zaseban sloj infrastrukture. Drugo, Google opisuje i "potpuno nove formate izlaza i dublju analizu", ali u primarnoj najavi ne navodi koji su to formati konkretno. Zato ih ovdje ne nabrajamo, jer bi to bilo nagađanje preko onoga što je Google zaista objavio.

Praktični smisao sandboxa je u tome da analiza ostaje utemeljena na vašim dokumentima. Umjesto da model "iz glave" procjenjuje, recimo, trend u tabeli, on može napisati kod koji tu tabelu stvarno obradi i vrati izračunat rezultat. Za analizu brojki to je bitna razlika, jer smanjuje prostor za izmišljanje vrijednosti koje zvuče uvjerljivo ali nisu tačne.

## Utemeljena analiza naspram običnog chatbota

Za firme, najzanimljiviji ugao nije samo tehnički, nego u čemu se ovakav alat razlikuje od općeg chatbota kada treba analizirati interne podatke.

Opći chatbot odgovara iz onoga što je model naučio i iz konteksta koji mu date u razgovoru. Kada ga pitate nešto o vašim brojkama, on generiše tekst koji izgleda kao odgovor, ali nema garantovanog mehanizma da je taj odgovor izveden iz vaših stvarnih podataka. Gemini Notebook je izgrađen oko suprotnog principa: izvori koje ubacite čine vašu knowledge base, a odgovori se vezuju uz grounding (utemeljenje odgovora u konkretnim, priloženim izvorima umjesto u općem znanju modela). Dodavanjem izvršavanja koda, to utemeljenje se proširuje s "citiraj iz teksta" na "izračunaj iz podataka".

Za tipičan poslovni scenario upotrebe to znači sljedeće. Ako tim treba da pregleda stotinu ugovora, kvartalne izvještaje ili zapisnike podrške i izvuče strukturirane zaključke, alat koji radi nad definisanim skupom izvora i može izvršiti kod nad njima manje je sklon da "popuni rupe" nego opći chatbot. To ne uklanja potrebu za ljudskom provjerom, ali mijenja profil rizika: greška je lakše uočljiva jer je vezana za konkretan izvor i konkretan izračun.

Ovdje treba biti trijezan. Utemeljenje u izvorima smanjuje jednu klasu grešaka, ali ne garantuje tačnost. Ako su ulazni dokumenti nepotpuni, zastarjeli ili pogrešno pripremljeni, i utemeljena analiza će vratiti pogrešan zaključak, samo uvjerljivije. Alat pomjera gdje se kontrola kvaliteta dešava, a ne ukida potrebu za njom.

{% include diagram.html name="gemini-notebook" caption="Obični chatbot odgovara iz memorije modela; Gemini Notebook izračunava odgovor iz vaših izvora u sandboxu – izvršavanje koda je sloj infrastrukture, ne nova verzija modela." alt="Dijagram poređenja dva puta do odgovora na pitanje o vlastitim podacima: lijevo obični chatbot odgovara iz memorije modela i konteksta razgovora bez garantovane veze s podacima, desno Gemini Notebook utemeljuje odgovor u priloženim izvorima i u sandboxu piše i pokreće kod koji izračunava rezultat." %}

## Ko sada ima pristup i zašto je to pitanje budžeta

Izvršavanje koda ne dobijaju svi odjednom, i tu se krije stvarna poslovna odluka. Prema Googleu, pristup je trenutno ograničen na:

- korisnike AI Ultra pretplate,
- Workspace poslovne korisnike s AI Ultra Access ili AI Expanded Access paketima.

Za sve Pro korisnike na webu Google najavljuje pristup "u narednim sedmicama", bez preciznog datuma.

Ovakvo stepenovanje po nivoima pretplate znači da najzanimljivija nova funkcija dolazi na najskupljim planovima. Za firmu koja procjenjuje alat, to postavlja klasično pitanje "kupiti ili graditi" u konkretnu formu: da li rani pristup izvršavanju koda opravdava skok na Ultra ili prošireni Workspace paket, ili je jeftinije sačekati da funkcija stigne na niži nivo? Odgovor zavisi od toga koliko je vaš radni tok analize podataka zaista vezan uz ovu sposobnost, a ne uz ono što niži planovi već nude.

Trošak nije samo cijena pretplate. Ako oko ovog alata izgradite radne tokove, obučite ljude i vežete interne procese za njegov način rada, nastaje zavisnost koju kasnije nije jednostavno razmotati. To je klasičan vendor lock-in: što dublje alat uđe u svakodnevni rad, to je promjena vendora skuplja, čak i kada se pojavi konkurentska opcija. Preporuka nije izbjegavati alat zbog toga, nego svjesno odlučiti koliko procesa vezati za jedan proizvod dok je pristup još u fazi rollout-a i dok se uslovi mogu mijenjati.

## Ekosistemska konsolidacija: dublja zavisnost o Googleu

Preimenovanje u Gemini Notebook nije samo kozmetika. Vezivanjem alata za Gemini brend, kreiranjem notebook-a unutar Gemini aplikacije i najavom ulaska u Search, Google gura notebook dublje u svoj ekosistem. Za korisnika to donosi udobnost: isti izvori i bilješke dostupni su na više mjesta bez ponovnog uvoza.

Ta ista udobnost je i strateški rizik za firmu. Što više vašeg istraživanja, interne dokumentacije i analitičkih radnih tokova živi unutar Google okruženja, to ste zavisniji od jednog hyperscalera za sloj koji dodiruje vaše osjetljive interne podatke. To nije razlog za paniku, jer je oslanjanje na velike cloud provajdere ionako uobičajeno, ali jeste razlog da se pitanje portabilnosti postavi rano: možete li izvući svoje izvore, rezultate i strukturu rada ako odlučite promijeniti alat? Odgovor na to pitanje danas je jeftiniji nego za godinu dana.

Za regulatorno osjetljive podatke, kao što su lični podaci klijenata ili povjerljivi ugovori, ubacivanje u alat vezan za vanjski ekosistem otvara pitanja o obradi i lokaciji podataka koja izlaze iz okvira ovog teksta i zahtijevaju zasebnu procjenu usklađenosti. Prije nego što interne podatke stavite u bilo koji ovakav alat, to pitanje treba riješiti s pravne i sigurnosne strane.

## Šta još nije stiglo i šta nije potvrđeno

Trezveno čitanje najave znači razdvojiti isporučeno od obećanog:

- **Integracija u Search AI Mode** je najavljena, ali nema datum i još nije isporučena. Tretirajte je kao mapu puta, ne kao dostupnu funkciju.
- **"Novi formati izlaza"** nisu specificirani u Googleovoj primarnoj najavi. Dok Google ne kaže koji su, nema osnova nabrajati ih.
- **Nadogradnja modela na "Gemini 3.5" i "Antigravity"** pojavljuje se samo u sekundarnom izvještavanju (9to5Google), a nije prisutna u zvaničnoj Googleovoj najavi. Google je sam nije potvrdio, pa je ovdje navodimo isključivo kao nepotvrđen izvještaj jednog medija, ne kao činjenicu. Bitno je i da je to, ako se potvrdi, promjena modela, potpuno odvojena od "secure cloud computer" mehanizma za izvršavanje koda o kojem govori ovaj tekst.

## Šta ovo znači u praksi

Za firmu koja procjenjuje alate za rad sa znanjem, poruka je jednostavna. Gemini Notebook je od organizatora izvora prerastao u alat koji može i računati nad tim izvorima, što ga čini ozbiljnijim kandidatom za internu analizu dokumenata nego opći chatbot. Najkonkretnija nova sposobnost, izvršavanje koda, za sada je zaključana na skupljim nivoima, pa je pametna odluka procijeniti da li vaš stvarni radni tok opravdava rani pristup ili je isplativije sačekati širi rollout. Paralelno, vrijedi rano definisati koliko dubine zavisnosti o Google ekosistemu ste spremni prihvatiti i kako biste, ako zatreba, izašli iz nje.

## Izvori
- [NotebookLM je sada Gemini Notebook – zvanična Google najava](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)
- [NotebookLM postaje Gemini Notebook – 9to5Google (izvor nepotvrđene tvrdnje o Gemini 3.5 / Antigravity)](https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/)
