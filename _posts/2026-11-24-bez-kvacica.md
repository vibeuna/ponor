---
layout: post
title: "U Ponorovom testu ChatGPT, Claude i Gemini razumjeli su bosanski i bez kvačica"
date: 2026-11-24
category: ai-za-sve
image: /assets/images/2026-11-24-bez-kvacica.svg
read_time: 12
description: "ChatGPT, Claude i Gemini dobili su deset promptova bez kvačica. Nijedna riječ nije pogrešno pročitana, a tokena je bilo tek 1–2% manje."
tags: [llm]
---

"Sto si kupio novi sto?" U ovoj rečenici ista riječ bez kvačica znači dvije različite stvari: prva je "što" (zašto), druga "sto" (komad namještaja). Ta rečenica bila je dio jednog od deset promptova (prompt je uputa ili upit koji se unosi modelu) koje je Ponorov test poslao u ChatGPT, Claude i Gemini bez č, ć, š, ž i đ. Nijedna aplikacija nije pogrešno pročitala nijednu riječ. Tekst ispod objašnjava šta je testirano, zašto je rezultat manje iznenađujući nego što izgleda i gdje se ipak pojavila razlika koja, barem kod ChatGPT-a, nema veze s kvačicama.

## Ukratko

Pisanje bez kvačica nije zbunilo nijedan od tri testirana chatbota. U Ponorovom testu od 23. 11. 2026. ChatGPT, Claude i Gemini dobili su po deset promptova s kvačicama i bez njih. U 60 odgovora nije bilo nijedne pogrešno pročitane riječi, uključujući dvosmislene parove kao što su sto/što, kos/koš i sal/šal. Svi odgovori koji nisu bili na engleskom napisani su s kvačicama. Na tokenizatorima tri modela otvorenih težina broj tokena (jedinica teksta koje model obrađuje) skoro se ne mijenja: bez kvačica 1–2% manje. Preliminarno zapažanje: kad prompt ne imenuje jezik, ChatGPT i Gemini ponekad odgovaraju ekavicom, ChatGPT jednako s kvačicama i bez njih.

## Koliko ljudi piše bez kvačica?

Za bosanski jezik Ponor nije našao objavljeno mjerenje. Najbliži podaci su za hrvatski i srpski, i odnose se na Twitter od 2013. do 2015. godine.

U toj studiji [Miličević i Ljubešić](https://doi.org/10.4312/slo2.0.2016.2.156-188) ručno su ispravili po 4.000 tvitova za svaki jezik. Promjene samo zbog kvačica obuhvatile su oko 2,5% riječi u hrvatskim i oko 4,8% u srpskim tvitovima. Na srpskom su kvačice izostavljane češće: oko četiri petine svih zamijenjenih slova bile su izostavljene kvačice, prema oko polovini na hrvatskom.

Te brojke nisu udio ljudi koji tako pišu. Uzorak je birao jednak broj tvitova iz četiri grupe po tome koliko odstupaju od standarda, i samo tvitove duže od 100 znakova. Nestandardni tekst je zato zastupljeniji nego na samom Twitteru. Prema ranijem radu na koji se autori pozivaju (Fišer i saradnici, 2015), oko tri četvrtine hrvatskih i dvije trećine srpskih tvitova ocijenjeno je kao standardno napisano.

Primjeri iz tog skupa podataka poznati su svakome ko čita poruke: kauc umjesto kauč, juce umjesto juče, najvece umjesto najveće.

Zašto ljudi tako pišu, nije izmjereno. [Ljubešić, Erjavec i Fišer](https://aclanthology.org/L16-1573/) navode ergonomiju, posebno na tabletima i telefonima, ali to je tvrdnja, ne rezultat. Poznata je jedna tehnička činjenica: osnovna abeceda za SMS poruke, kao i njene nacionalne dopune, ne sadrži nijedno od slova č, ć, š, ž, đ ([3GPP TS 23.038](https://www.etsi.org/deliver/etsi_ts/123000_123099/123038/17.00.00_60/ts_123038v170000p.pdf)). Poruka s njima prelazi u drugi zapis, u kojem u jednu SMS poruku stane najviše 70 znakova. Da li je to stvorilo naviku, Ponor nije našao dokaz.

## Ponorov test: šta je urađeno

Deset promptova napisano je u dvije verzije. Verzija s kvačicama je normalan bosanski tekst. Verzija bez kvačica napravljena je mehanički: č i ć postali su c, š je postalo s, ž je postalo z, a đ je postalo dj. Svaka verzija poslana je jednom u svaku od tri aplikacije, uvijek u novom razgovoru. To je 60 odgovora.

Promptovi su bili tri vrste:

- **Svakodnevni zadaci:** sažimanje obavještenja udruženja stanara, preoblikovanje bilješke u pristojnu službenu poruku šefu, pitanje o najvišem vrhu u BiH i savjet kako očistiti kamenac iz čajnika.
- **Zamke:** riječi koje bez kvačica postaju druga riječ. "Koji sal je topliji, vuneni ili pamucni?" (šal, ne salo ili sala). "Kako da naucim dijete od tri godine da baca smece u kos?" (koš, ne ptica kos). "Zasto se sto u kuhinji klima i sta da uradim?" (sto kao namještaj, ne broj 100). Peti prompt tražio je prevod pet kratkih rečenica na engleski, sa zamkama kuca/kuća, sto/što, sal/šal, kos/koš i cas/čas.
- **Opušteni stil:** "jel mozes mi objasnit sta je inflacija, ko da imam 10 godina" i zahtjev za veselu rođendansku poruku drugarici.

**Napomena o metodi.** Test je urađen 23. 11. 2026. ChatGPT i Claude korišteni su na besplatnim paketima, a Gemini na plaćenom paketu (Plus). ChatGPT nije prikazao naziv modela. Claude je prikazao Sonnet 5.5. Gemini je prikazao "Hydrogen", a nije poznato kojem modelu taj naziv odgovara. Svaki prompt poslan je jednom, pa rezultat opisuje šta se desilo u tih 60 odgovora, a ne koliko je koja aplikacija pouzdana. Ocjene tačnosti i prirodnosti dao je naslijepo drugi model u ulozi ocjenjivača (judge), bez oznake aplikacije i verzije. Urednik ih još nije provjerio, pa tekst koristi samo ono što se vidi direktno iz odgovora. Modeli u aplikacijama mijenjaju se bez najave, i isti test sutra može dati drugačiji rezultat.

## Rezultat: nijedna pogrešno pročitana riječ

U 60 odgovora nijedna riječ nije pročitana pogrešno. Sve zamke u verziji bez kvačica protumačene su kako je bilo namjeravano, u sve tri aplikacije: kuca kao kuća, sto kao namještaj ili kao što, prema mjestu u rečenici, sal kao šal, kos kao koš, cas kao čas, zasto kao zašto. U nekoliko odgovora aplikacija je izričito napisala kako je riječ shvatila.

Drugi nalaz: svi odgovori koji nisu bili na engleskom napisani su s kvačicama, i kad je prompt bio bez njih. Jedina iznimka je jedna riječ. Claude je u odgovoru na "Koji sal je topliji" dvaput ponovio korisnikovo "sal" bez kvačice, a ostatak odgovora napisao normalno.

Neki odgovori imali su tehničke ostatke, kao izgubljene slike ili tabele koje su se raspale pri kopiranju iz aplikacije. To su greške prikaza i kopiranja, ne greške jezika.

## Zašto je zadatak lakši nego što izgleda

Ponor nije našao objavljeno istraživanje o tome kako tačno [veliki jezički modeli](/rjecnik/veliki-jezicki-model/) (large language model, LLM) čitaju bosanski tekst bez kvačica. Istraživanja iz vremena prije njih ipak pokazuju zašto taj zadatak nije težak koliko se čini.

Ljubešić, Erjavec i Fišer mjerili su 2016. koliko je riječi pogrešno napisano u tekstu iz kojeg su kvačice uklonjene. Bez ikakvog ispravljanja to je oko 14% riječi na Wikipediji i 13–16% na Twitteru. To odgovara podatku iz istog rada da oko 13% riječi u hrvatskom, srpskom i slovenačkom sadrži barem jedno slovo s kvačicom. Njihov najbolji sistem za automatsko vraćanje kvačica (diacritic restoration), zasnovan na statistici iz velikih zbirki teksta, dovodi tačnost na 99,57% za hrvatsku i 99,47% za srpsku Wikipediju, te 99,38% i 99,17% za tvitove.

Ti procenti računaju sve riječi, i one koje kvačice uopšte nemaju. Preostale greške autori su detaljno analizirali samo za slovenačke tvitove. Tamo se skupljaju na dvosmislenim riječima, rijetkim riječima, vlastitim imenima i tekstu gdje nedostaju razmaci. Dvosmislene riječi čine 37% preostalih grešaka, s primjerima kao se/še i nas/naš.

Drugi podatak objašnjava zašto je osnova tako jaka. [Náplava i saradnici](https://aclanthology.org/L18-1247/) poredili su 23 jezika najjednostavnijom metodom: za svaku riječ bez kvačica uzme se oblik koji se najčešće javlja. Hrvatski je imao najmanje grešaka od svih: 0,34% riječi. Češki je imao 4,09%, rumunski 29,71%, a vijetnamski 40,53%. Drugim riječima, za veliku većinu hrvatskih riječi, a vjerovatno i bosanskih, postoji samo jedan smislen oblik s kvačicama. "Ocistim" može biti samo "očistim".

Za ostatak, kao sto/što, mora odlučiti kontekst. "Novi sto" je namještaj, a "sto si kupio" na početku pitanja je "što". Upravo na takvim riječima stariji sistemi griješili su najčešće. Ponorove zamke birane su baš iz tog tvrdog ostatka, i nijedna aplikacija nije pogriješila. To je deset promptova, a ne mjerenje na hiljadama rečenica, pa pokazuje samo da su tri aplikacije u ovim rečenicama kontekst iskoristile ispravno.

## Šta tokenizator vidi

Prije nego model "pročita" tekst, [tokenizator](/rjecnik/tokenizator/) (tokenizer) ga dijeli na [tokene](/rjecnik/token/) (osnovne jedinice teksta koje model obrađuje – riječi ili dijelove riječi). Taj korak zove se [tokenizacija](/rjecnik/tokenizacija/) (tokenization).

Na nivou računara, slova s kvačicama i bez njih nisu iste veličine. Prema standardu za UTF-8 zapis ([RFC 3629](https://www.rfc-editor.org/rfc/rfc3629)), svih pet slova č, ć, š, ž i đ, i velika i mala, zauzima po dva bajta. Obična slova c, s, z i d zauzimaju po jedan. Tekst bez kvačica je zato kraći u bajtovima.

Slovo đ ima još jednu posebnost. Mnogi programi uklanjaju kvačice i druge oznake sa slova tako što slovo rastave na osnovno slovo i dodatni znak, pa obrišu znak. Č se tako pretvori u c. Đ se ne rastavlja na taj način, pa takva rutina ostavi đ netaknutim ([Náplava i saradnici](https://aclanthology.org/L18-1247/)). Prema [Gormanu i Pinteru](https://aclanthology.org/2025.naacl-short.25/), isti postupak koriste i alati za pripremu teksta u biblioteci Hugging Face, a originalni BERT modeli koji ne razlikuju velika i mala slova trenirani su na tekstu iz kojeg su uklonjene sve oznake sa slova, pa i kvačice. Ponorov test zato nije koristio takvu rutinu, nego je svako đ zamijenio s dj, kao u "rodjendan".

{% include diagram.html name="bez-kvacica" caption="Ista rečenica s kvačicama ima dva bajta više, a broj tokena se skoro ne mijenja." alt="Rečenica 'Zašto se sto u kuhinji klima i šta da uradim?' ima 47 bajtova s kvačicama i 45 bez njih; na tri tokenizatora broj tokena ide sa 16, 17 i 18 na 16, 16 i 17. Na svih deset promptova bajtova je 3,7% manje, a tokena 1–2% manje." %}

## Košta li pisanje bez kvačica više tokena?

Ne. Ponor je prebrojao tokene za svih deset promptova, u obje verzije, s tokenizatorima tri [modela otvorenih težina](/rjecnik/otvorene-tezine/) (open-weight): gemma4:e2b, qwen3.5:0.8b i nemotron-3-nano:4b. Modeli su pokrenuti kao [lokalni modeli](/rjecnik/lokalni-model/) kroz Ollamu. To nisu tokenizatori koje koriste ChatGPT, Claude i Gemini, pa brojke pokazuju smjer, ne tačan trošak u te tri aplikacije.

| | S kvačicama | Bez kvačica | Odnos |
|---|---|---|---|
| gemma4:e2b (tokeni) | 427 | 422 | 0,988 |
| qwen3.5:0.8b (tokeni) | 445 | 435 | 0,978 |
| nemotron-3-nano:4b (tokeni) | 452 | 443 | 0,980 |
| Bajtovi (UTF-8) | 1.298 | 1.250 | 0,963 |
| Znakovi | 1.249 | 1.250 | 1,001 |

Bez kvačica tekst je kraći za 3,7% bajtova, ali za samo 1–2% tokena. Broj znakova se čak poveća za jedan, jer je jedno đ postalo dj. Po pojedinačnom promptu razlika je bila od 0 do 5 tokena. Najveća je na prevodu pet kratkih rečenica punih kvačica, gdje je, recimo, 67 tokena postalo 64. Kod dužeg obavještenja udruženja stanara jedan tokenizator je bez kvačica izbrojao dva tokena više, a drugi dva manje.

Sličan obrazac prijavljuju [Gorman i Pinter](https://aclanthology.org/2025.naacl-short.25/) za španski, mjereno na jednoj primjer-rečenici po jeziku: kad se uklone oznake iznad slova (á, é, ñ), broj tokena u modelima LLaMA, mBERT i XLM-R mijenja se tek malo. Bosanski nisu testirali. Arapski i hebrejski tekst sa znakovima iznad i ispod slova, s druge strane, troši dva do četiri puta više tokena nego isti tekst bez njih. To je drugačiji slučaj od bosanskog.

Praktični zaključak: kvačice ne treba skidati da bi se uštedjelo, niti dodavati iz straha od većeg troška. Razlika je zanemariva u oba smjera.

## Gdje se ipak pojavila razlika: ekavica

Jedna razlika u testu se ponavljala, a kod ChatGPT-a nije zavisila od kvačica. ChatGPT je na četiri prompta odgovorio ekavicom ili srpskim oblicima riječi: o kamencu u čajniku, o stolu koji se klima, o šalu i u rođendanskoj poruci. To je uradio i u verziji s kvačicama i u verziji bez njih. U odgovoru o šalu, na prompt s kvačicama, stoji "vreme" i "greje", a u rođendanskoj poruci bez kvačica "uvek". Gemini je ekavicu koristio u četiri odgovora: u rođendanskoj poruci u obje verzije, te na kamenac i šal samo u verziji bez kvačica. Kod Geminija ovaj test zato ne može isključiti ni vezu s kvačicama. U Claudeovim odgovorima ekavica nije zabilježena.

Sva četiri prompta imaju nešto zajedničko: ne kažu na kojem jeziku žele odgovor. To ipak nije dovoljno objašnjenje, jer ekavice nije bilo ni na tri druga prompta koja ne imenuju jezik (najviši vrh, koš, inflacija). Na dva prompta koja izričito kažu "na bosanskom jeziku", sažetak i službenu poruku, ekavice nije bilo ni u jednoj aplikaciji.

**Ovo je preliminarno zapažanje, ne rezultat.** Promptovi koji imenuju jezik razlikuju se od ostalih i po zadatku. Sažimanje teksta napisanog ijekavicom drugačiji je posao od pisanja rođendanske poruke od nule. Test nije razdvojio ta dva uzroka. Isti obrazac Ponor je ranije vidio u testu za [tekst o pisanju promptova](/clanci/kako-napisati-dobar-prompt/), gdje su odgovori bez navedenog jezika dolazili ekavicom ili s hrvatskim riječima, a navođenje bosanskog jezika i ijekavice to je ispravilo.

## Šta to znači u praksi

- **Pišite kako vam je lakše.** Ako na telefonu kucate bez kvačica, to u Ponorovom testu nije smetalo nijednoj aplikaciji. Nijedna riječ nije pogrešno pročitana, ni u namjerno dvosmislenim rečenicama.
- **Odgovor ćete dobiti s kvačicama.** Ne morate tražiti da ih vrati. U testu su ih sve tri aplikacije same koristile.
- **Imenujte jezik.** Ako želite bosanski i ijekavicu, napišite to u prompt: "Odgovori na bosanskom jeziku, ijekavicom." U ranijem Ponorovom testu ta uputa je uklonila ekavicu. U ovom testu ekavice nije bilo nijednom kad je jezik bio naveden.
- **Ne brinite o trošku.** Bez kvačica tekst troši 1–2% manje tokena na testiranim tokenizatorima. To ne vrijedi ni namjerno skidati ni namjerno dodavati.

## Šta NIJE

**Nije dokaz da kvačice nikad nisu važne.** Test je pokrio deset promptova, po jedan odgovor po aplikaciji, i kratke, jasne rečenice. Dugi tekstovi s mnogo vlastitih imena ili rijetkih riječi su upravo mjesto gdje su i stariji sistemi griješili najčešće. Gorman i Pinter navode i primjere gdje je sistem za [mašinsko prevođenje](/rjecnik/masinsko-prevodjenje/) (machine translation) pogrešno preveo ruske i španske rečenice, a greška je zavisila od oznaka iznad slova.

**Nije mjerenje pouzdanosti aplikacija.** Jedan odgovor po promptu ne govori koliko često neka aplikacija griješi, niti koja je bolja. U ovom testu nijedna nije pogrešno pročitala nijednu riječ.

**Nije istraživanje o bosanskom.** Ponor nije našao objavljenu evaluaciju velikih jezičkih modela na bosanskom, hrvatskom ili srpskom tekstu bez kvačica. Jedine srodne evaluacije velikih jezičkih modela koje je Ponor našao odnose se na rumunski ([Nadăș i Diosan](https://arxiv.org/abs/2511.13182v3), vraćanje oznaka na slova) i francuski (preprint, odnosno rad koji još nije prošao recenziju: [Yu i saradnici](https://arxiv.org/abs/2610.33493)). Ponorov test je mali, ali je jedini takav podatak za bosanski koji je Ponor našao.

**Nije podatak o tome koliko Bosanaca piše bez kvačica.** Postojeće brojke su hrvatski i srpski Twitter od prije desetak godina, iz uzorka koji je namjerno uzimao više nestandardnog teksta.

## Povezano

- [Šta je LLM token i kako radi tokenizacija?](/clanci/sta-je-llm-token/) – kako tokenizator dijeli tekst i zašto bosanski troši više tokena od engleskog.
- [Kako napisati dobar prompt: jezik, situacija, oblik odgovora](/clanci/kako-napisati-dobar-prompt/) – zašto navesti bosanski i ijekavicu, i kako to sačuvati kao stalnu uputu.
- [Koji AI najbolje prevodi na bosanski?](/clanci/ai-prevod-bosanski/) – raniji Ponorov test s istim problemom hrvatskih i srpskih riječi u odgovorima.

## Izvori

- [Corpus-Based Diacritic Restoration for South Slavic Languages – Ljubešić, Erjavec, Fišer, LREC 2016](https://aclanthology.org/L16-1573/)
- [Tviterasi, tviteraši or twitteraši? Producing and analysing a normalised dataset of Croatian and Serbian tweets – Miličević, Ljubešić, Slovenščina 2.0, 2016](https://doi.org/10.4312/slo2.0.2016.2.156-188)
- [Diacritics Restoration Using Neural Networks – Náplava, Straka, Straňák, Hajič, LREC 2018](https://aclanthology.org/L18-1247/)
- [Don't Touch My Diacritics – Gorman, Pinter, NAACL 2025](https://aclanthology.org/2025.naacl-short.25/)
- [RFC 3629: UTF-8, a transformation format of ISO 10646 – IETF, 2003](https://www.rfc-editor.org/rfc/rfc3629)
- [3GPP TS 23.038 v17.0.0: Alphabets and language-specific information – ETSI, 2022](https://www.etsi.org/deliver/etsi_ts/123000_123099/123038/17.00.00_60/ts_123038v170000p.pdf)
- [Evaluating Large Language Models for Diacritic Restoration in Romanian Texts: A Comparative Study – Nadăș, Diosan, 2025](https://arxiv.org/abs/2511.13182v3)
