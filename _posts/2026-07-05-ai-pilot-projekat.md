---
layout: post
title: "AI pismenost za menadžere: šta odobriti prije pilot projekta"
date: 2026-07-05
category: ai-u-praksi
audience: businesses
read_time: 7
description: "Checklist od osam pitanja koja menadžer treba postaviti prije nego odobri AI pilot projekat - prije izbora modela, prije potpisa budžeta."
diagram: /assets/diagrams/ai-pilot-projekat.svg
image: /assets/images/2026-07-05-ai-pilot-projekat.svg
---

Vaš product lead dolazi sa prezentacijom: LLM chatbot za korisničku podršku, obećanje da će prepoloviti vrijeme odgovora, tražen budžet i tri mjeseca za pilot. Slajdovi izgledaju uvjerljivo, demo radi glatko, i pritisak da se "ne zaostane" je stvaran. Prije nego što potpišete, postoji osam pitanja koja rijetko neko postavi na prvom sastanku - a upravo ona određuju hoće li pilot projekat završiti u produkciji ili tiho nestati sa liste prioriteta za šest mjeseci.

## Zašto ovo zaslužuje petnaest minuta prije potpisa

Većina rasprave o AI pilot projektima fokusira se na izbor modela - koji LLM, koji vendor, koja tačnost na kojem benchmarku. To je pogrešno mjesto za početak. Odluka koja stvarno određuje ishod pilota donosi se prije nego što se model uopšte izabere: da li je ishod definisan, da li su podaci spremni, i da li neko konkretno odgovara za rezultat.

Jedna, često citirana MIT-ova studija iz 2025. (prenesena u Fortuneu) navodi da velika većina pilot projekata generativne AI u kompanijama ne uspije proizvesti mjerljivu poslovnu vrijednost. Vrijedi je uzeti kao jedno istraživanje, ne kao ustaljenu statistiku struke - ali smjer nalaza se poklapa sa onim što se ponavlja u praksi konsultanata za AI implementaciju: većina pilota ne propada zato što model ne radi. Propadaju zato što niko unaprijed nije definisao šta bi značilo da pilot uspije, ko je vlasnik ishoda, ili šta se dešava kad podaci nisu onakvi kakvi su izgledali u prezentaciji.

Checklist koji slijedi nije tehnička specifikacija. To je set pitanja koja menadžer - bez potrebe da razumije arhitekturu modela - može i treba postaviti prije nego što odobri budžet i vrijeme tima. Razlika između pilota koji stigne do produkcije i onog koji se tiho zaboravi rijetko leži u tome koji je LLM izabran - leži u tome da li su ova pitanja postavljena na prvom sastanku ili tek kad se pojavi prvi problem.

## Osam stavki prije nego kažete da

**1. Imenovan, mjerljiv ishod - prije obima projekta.**
Ako sponzor pilota ne može u jednoj rečenici reći koju metriku pilot treba pomjeriti - "skratiti vrijeme ručne obrade prijava sa pet dana na jedan", ne "poboljšati efikasnost korisničke podrške" - pilot je nedefinisan i, što je važnije, neopovrgljiv. Bez konkretne metrike, na kraju pilota nema objektivnog načina da se kaže da li je uspio ili nije. Umjesto toga, odluka o nastavku postaje pitanje osjećaja: "izgleda da radi dobro." To je znak da treba vratiti prijedlog na doradu, ne odobriti ga.

**2. Provjera spremnosti podataka - ne izbor modela.**
Najveći dio truda potrebnog da pilot stigne do produkcije nije izbor ili podešavanje modela - to je inženjering podataka, integracija i upravljanje pristupom. Postavite pitanje direktno: da li su podaci na koje se pilot oslanja stvarno dostupni, ažurni i kompletni, ili je to pretpostavka iz prezentacije? Timovi koji grade demo često koriste ručno očišćen, reprezentativan uzorak podataka - recimo, hiljadu pažljivo odabranih tiketa korisničke podrške koji lijepo pokazuju šta model umije. Sistem u produkciji mora raditi sa svim tiketima, uključujući one na dijalektu koji model nije viđao, sa pogrešno unesenim brojem narudžbe, ili duplirane zbog pada sistema prošle sedmice. Ako niko u sobi ne zna odgovoriti odakle dolaze podaci, ko ih održava i koliko su stari, pilot testira demo, ne realnost.

**3. Jasno vlasništvo nad neuspjehom.**
Imenujte ko vlasnik granice podataka, ko pregleda kvalitet izlaza sistema, ko je vlasnik odluke o povlačenju (rollback) i ko odgovara kada sistem pogriješi. Nejasno ili podijeljeno vlasništvo - poslovna strana vlasnik cilja, inženjering vlasnik sistema, niko vlasnik veze između njih - jedan je od najčešće navedenih uzroka zašto pilot projekti stanu bez formalnog otkazivanja. Projekat jednostavno prestane dobijati pažnju jer nema osobu čiji je posao da je gura naprijed.

**4. Human-in-the-loop tačke definisane unaprijed.**
Prije lansiranja pilota, odlučite koje odluke sistem smije donijeti bez nadzora i koje zahtijevaju potpis čovjeka prije nego što se sprovedu - te definišite putanju eskalacije kad sistem nije siguran ili kad korisnik ospori rezultat. Ovo nije tehnički detalj koji se rješava naknadno. Ako se human-in-the-loop tačke definišu tek kad se pojavi prvi ozbiljan incident, tim reaguje pod pritiskom umjesto po planu - i povjerenje u sistem (interno i kod klijenata) trpi.

**5. Troškovni model iznad budžeta pilota.**
Trošak pilot projekta rijetko liči na trošak istog sistema u produkciji. Cijena inferencije po upitu, inženjering integracije, kontinuirano održavanje i praćenje performansi pri stvarnom obimu korištenja - to su troškovi koji se pojave tek kad pilot preraste u alat koji koristi cijela kompanija, ne pet ljudi u testnoj grupi. Ako je budžet odobren kao kapex za alat i licence, a stvarni trošak nastaje kontinuirano po broju upita mjesečno, brojke iz odluke o odobrenju pilota neće se poklopiti sa brojkama iz odluke o skaliranju. Tražite od sponzora projekciju troška pri deset puta većem obimu korištenja, ne samo cijenu pilota. Pilot testiran sa pet zaposlenih i produkcijski sistem koji koristi cijelo odjeljenje korisničke podrške nisu isti trošak - a odluka o skaliranju često se donosi na osnovu brojki iz prve faze.

**6. Vendor lock-in i uslovi izlaska.**
Prije potpisa, provjerite prenosivost podataka, trošak prelaska na drugi model ili vendora, i šta se dešava ako vendor promijeni cijenu ili bude preuzet od strane drugog vendora. Vendor lock-in rizik nije apstraktan - u praksi znači da promjena strategije godinu dana kasnije može koštati višestruko više nego što je pilot ikad predviđao, jer su podaci, integracije i procesi tima izgrađeni oko jednog specifičnog API-ja ili formata. Pitanje za sponzora prijedloga: da smo za godinu dana morali promijeniti vendora, koliko bi to koštalo i koliko bi trajalo?

**7. Regulatorna klasifikacija - jedna stavka checklist-e, ne poseban projekat.**
Provjerite da li slučaj upotrebe potencijalno spada u neku od kategorija koje EU AI Act navodi kao high-risk (npr. odabir kandidata za posao ili kreditno bodovanje - ovo su primjeri, ne konačna pravna procjena; stvarna klasifikacija zahtijeva pravnu provjeru) - ovo treba biti jedno pitanje na sastanku, ne zaseban trud koji blokira odluku o pilotu. Detaljno objašnjenje EU AI Act obaveza i rokova nalazi se u [EU AI Act: šta svaka kompanija mora znati prije augusta 2026](/clanci/eu-ai-act-article/); ovdje je dovoljno da neko na sastanku zna odgovoriti da li je klasifikacija provjerena, ili da eksplicitno stoji na listi otvorenih pitanja prije nastavka.

**8. Definisan rok izlaska.**
Odobrite jedan uzak slučaj upotrebe, jedan put pregleda rezultata i jedan datum na koji se donosi odluka: pilot se gasi, produžava ili promoviše u produkciju. Pilot bez datuma završetka nije eksperiment - to je trajna obaveza koja se nikad formalno ne evaluira, jer uvijek postoji razlog da se "još malo sačeka."

{% include diagram.html name="ai-pilot-projekat" caption="Razlika između pilota koji tiho nestane i pilota koji stigne do produkcije rijetko je u izboru modela - leži u osam pitanja postavljenih prije potpisa." alt="Poređenje dva puta odobravanja AI pilot projekta: bez checklist-e pilot tiho nestaje, sa osam-stavki checklist-om stiže do odluke o produkciji" %}

## Zašto pilot projekti tiho propadaju

Obrasci neuspjeha se ponavljaju bez obzira na industriju ili veličinu kompanije, i uglavnom nisu tehnički:

- **Pilot je optimizovan za utisak na demu, ne za imenovanu poslovnu metriku.** Kad dođe trenutak odluke, nema objektivnog kriterija naspram kojeg se pilot mjeri - samo opšti osjećaj da je "impresivan."
- **Problemi sa kvalitetom i pristupom podacima izađu na vidjelo tek kad pilot krene ka stvarnoj integraciji.** Ono što se u žargonu naziva "posljednja milja" gotovo uvijek je vodovod podataka, ne sposobnost modela.
- **Niko nije vlasnik ishoda od početka do kraja.** Poslovna strana vlasnik je cilja, inženjering vlasnik sistema - a veza između njih nema vlasnika. Kad nešto krene po zlu, nema jasne adrese odgovornosti, pa projekat gubi zamah tiho, bez formalne odluke da se prekine.
- **Change management dug.** Zaposleni zaobilaze alat jer se ne uklapa u njihov stvarni tok rada, čak i kad model tehnički radi dobro u izolaciji. Tipičan primjer: agent za podršku i dalje kopira odgovor u svoj stari alat prije slanja, jer novi sistem ne podržava korak koji je oduvijek radio ručno - i pilot se u izvještajima bilježi kao "korišten", iako stvarno ne mijenja ništa u toku rada.
- **Odnos troška i vrijednosti postaje nejasan ili nepovoljan kad se izmjeri pri stvarnom obimu korištenja.** Cijena po upitu i trošak održavanja pri produkcijskom obimu rijetko liče na ekonomiju pilota rađenog sa desetak korisnika.

Zajednički imenilac ovih obrazaca: nijedan se ne otkriva testiranjem modela. Svi se otkrivaju - ili sprječavaju - checklist-om odobrenim prije nego što pilot uopšte krene.

## Umjesto zaključka

Ako sljedeći put kad neko zatraži odobrenje za AI pilot projekat postavite samo tri pitanja - koju metriku ovo pomjera, ko je vlasnik ishoda ako sistem pogriješi, i na koji datum donosimo odluku o nastavku - vjerovatno ćete uhvatiti većinu problema prije nego što postanu skupi. Ostatak checklist-e (podaci, human-in-the-loop tačke, troškovni model, vendor lock-in, regulatorna provjera) rješava se u istom sastanku, ne u zasebnom projektu. Cilj nije usporiti odobravanje AI pilota - cilj je da odluka koju donesete bude odluka, a ne nada.

## Izvori

Ovaj tekst ne izvještava o jednom vanjskom događaju ili objavi - sintetiše ustaljenu praksu upravljanja AI projektima, nabavke i MLOps-a iz više izvora, bez jednog primarnog izvora na koji bi se cijeli okvir oslanjao. Nalaz MIT-ove studije pomenut u tekstu prenesen je putem Fortunea (august 2025.) i naveden je kao jedno istraživanje, ne kao utvrđena statistika. Za regulatorni dio checklist-e, pogledajte postojeći tekst na sajtu: [EU AI Act: šta svaka kompanija mora znati prije augusta 2026](/clanci/eu-ai-act-article/).
