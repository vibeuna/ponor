---
layout: post
title: "MiniMax Music-3.0: generator muzike stigao na API, ali pitanje licence ostaje otvoreno"
date: 2026-07-20
category: ai-u-praksi
image: /assets/images/2026-07-20-minimax-music-3.svg
audience: designers
read_time: 5
description: "MiniMax Music-3.0 generiše cijele pjesme iz teksta. Za kreativce je privlačno, ali zvanični uslovi ćute o pravima na izlaz, pa gotovu numeru ne treba isporučivati naslijepo."
---

MiniMax je 16. jula 2026. dodao model Music-3.0 na svoju API platformu. Model iz teksta generiše cijele pjesme – sa vokalom i tekstom ili čisto instrumentalne. Za nekoga ko pravi video, prototip proizvoda ili prezentaciju, to zvuči kao rješenje za vječiti problem prateće muzike. Prije nego što takav zvuk uđe u komercijalni rad, treba razumjeti šta model zaista radi, a šta je i dalje nejasno – prije svega oko licence.

{% include diagram.html name="minimax-music-3" caption="Do MP3-a se stigne jednim API pozivom; komercijalna isporuka čeka na potvrdu prava." alt="Tok od prompta i opcionog teksta kroz MiniMax Music-3.0 (vokalni i instrumentalni režim) do MP3 artefakta, pa do provjere licence koja propušta interni prototip kao nizak rizik, a komercijalnu isporuku blokira dok se prava ne potvrde." %}

## Šta model radi

Music-3.0 se poziva preko API-ja i radi u dva režima: vokalnom, gdje uz zahtjev šaljete tekst pjesme, i instrumentalnom, gdje dobijate numeru bez pjevanja. Ako nemate gotov tekst, model ga po potrebi može i sam generisati. Sam tekst pjesme koji prosljeđujete ograničen je na 10 do 1.000 znakova, prema zvaničnoj dokumentaciji.

U primjerima koda izlaz je MP3, 44,1 kHz, 256 kbps. Dokumentacija, međutim, ne navodi da li je taj format fiksan ili se može mijenjati, pa to treba provjeriti prije nego što ga ugradite u proces koji zavisi od tačno određenog formata. Ni maksimalna dužina numere nije navedena ni u jednom zvaničnom izvoru.

Sam poziv nije komplikovan: pošaljete prompt (i opciono tekst), dobijete audio fajl. Za dizajnera to znači da se generisanje muzike može ugraditi u alat ili radni tok (workflow) na isti način kao i generisanje slika ili teksta – kao API poziv koji vraća gotov artefakt.

## Šta je zaista novo

Ovdje treba biti precizan. Instrumentalni režim i prebacivanje između režima postojali su već u verzijama 2.5 i 2.6. Ono što je stvarno novo jeste sam skok na verziju 3.0, uz tvrdnje o boljem kvalitetu.

MiniMax navodi da 3.0 bolje razumije kreativnu namjeru, realističnije reprodukuje instrumente i prirodnije generiše vokal, te da prednjači u reprodukciji kineskih instrumenata. Te tvrdnje dolaze od proizvođača i nisu nezavisno provjerene niti mjerene benchmarkom. Drugim riječima: to su marketinške i demo tvrdnje, a ne izmjereni rezultat. Dok neko izvan MiniMaxa ne uporedi izlaz sistematski, kvalitet ćete najpouzdanije procijeniti tako što ćete sami generisati nekoliko numera za svoj konkretan slučaj i poslušati ih.

Što se tiče cijene, sekundarni izvori navode oko 0,15 dolara po numeri do pet minuta, ali to nije potvrđeno ni na jednoj zvaničnoj MiniMax stranici s cijenama i treba ga tretirati kao nepotvrđeno. Za orijentaciju, konkurenti poput Suno i Udio naplaćuju mjesečne pretplate (grubo 10 do 36 dolara), no i ti brojevi dolaze iz sekundarnih poređenja iz 2026. i mijenjaju se.

## Šta to znači za kreativni radni tok

Za dizajnere i kreativce privlačnost je jasna: umjesto pretraživanja biblioteka stok-muzike, opisujete raspoloženje i žanr u promptu i dobijate numeru skrojenu za scenu. To se lijepo uklapa u prototipiranje – privremeni zvuk za animaciju, demo aplikacije ili prezentaciju, gdje je brzina važnija od finalnog kvaliteta.

Ali baš tu prototip prelazi u zamku. Zvuk koji ste ubacili kao „privremeni" ima naviku da ostane do finalne isporuke. A za isporuku – posebno komercijalnu – pravno pitanje postaje presudno, i tu ovaj model traži oprez.

Praktičan savjet: tretirajte generisanu muziku kao materijal nejasnog statusa dok sami ne razjasnite prava, a ne kao gotov, slobodan resurs. To mijenja i dizajn iskustva ako Music-3.0 ugrađujete u proizvod za krajnje korisnike – korisnicima ne smijete implicitno obećati da je izlaz „njihov" i slobodan za upotrebu ako to niste provjerili.

## Licenca i autorska prava: nerješeni čvor

Ovo je najvažniji dio i ujedno najnejasniji.

Zvanični uslovi korištenja (ToS) za MiniMax muziku kažu da korisnik zadržava prava intelektualnog vlasništva nad onim što **unese**. O vlasništvu nad onim što model **generiše** – nad samim izlazom – ToS ćuti. Ne dodjeljuje eksplicitno nikakva prava na komercijalnu upotrebu niti royalty-free status (bez obaveze plaćanja naknade za korištenje). Istovremeno, marketinške i sekundarne stranice tvrde da je izlaz „royalty-free" i „spreman za komercijalnu upotrebu".

To je otvorena kontradikcija. Zvanični pravni dokument ne daje ono što marketinške stranice obećavaju. U toj situaciji ne smijete pretpostaviti da je generisana muzika slobodna za komercijalnu upotrebu. Prije bilo kakve komercijalne isporuke, sami provjerite licencu – najbolje u pisanoj komunikaciji direktno sa MiniMaxom – i pribavite izričitu potvrdu prava.

Nejasnoću pojačavaju još tri stvari:

- **Porijeklo podataka za treniranje** modela nije objavljeno ni u jednom dostupnom izvoru. To znači da ne možete procijeniti da li i u kojoj mjeri izlaz nosi rizik od sličnosti sa zaštićenim djelima.
- **Nadležnost i mjerodavno pravo** nisu definisani. Muzički ToS ne navodi ni mjerodavno pravo ni okvir (npr. EU ili SAD), nego samo kontakt e-mail. Za korisnika u EU to je dodatna neizvjesnost, jer nije jasno koje pravo uopšte reguliše spor.
- ToS spominje da izlaz može sadržavati ugrađene vodene žigove ili identifikatore i da je korisnik odgovoran za označavanje sadržaja kao AI-generisanog. To je pitanje provenance (evidencija porijekla rezultata: kod, okruženje, opis) – u nekim tržištima i kontekstima obavezno označavanje može uticati na to kako smijete predstaviti gotov rad.

Za kreativni tim zaključak nije „ne koristi", nego „ne isporučuj naslijepo". Music-3.0 je koristan za istraživanje, skice i interne prototipove, gdje je pravni rizik nizak. Prelazak na plaćeni, javni ili komercijalni rad zahtijeva da prava prethodno budu razjašnjena, u pisanom obliku, za vaš konkretan slučaj i tržište.

## Izvori

- [MiniMax – dokumentacija za generisanje muzike](https://platform.minimax.io/docs/guides/music-generation)
- [MiniMax – bilješke o izdanjima modela (16.7.2026.)](https://platform.minimax.io/docs/release-notes/models)
- [MiniMax – uslovi korištenja za muziku (ToS)](https://www.minimax.io/audio/doc/terms-of-service-music.html)
- [MiniMax – najava prethodne verzije Music 2.6 (kontekst)](https://www.minimax.io/news/music-26)
