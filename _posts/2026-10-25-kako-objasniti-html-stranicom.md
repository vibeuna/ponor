---
layout: post
title: "Objasni HTML stranicom: vještina za interaktivna objašnjenja"
date: 2026-10-25
category: ai-za-sve
image: /assets/images/2026-10-25-kako-objasniti-html-stranicom.svg
read_time: 8
description: "Vještina koja uči chatbota da objasni pojam stranicom s kontrolama: vještina za kopiranje, primjer s biljnom ćelijom i gdje stranice mogu raditi."
tags: [ai-agenti, skills]
---

Pitate chatbota šta se desi s biljnom ćelijom kad joj nestane vode. Dobijete nekoliko pasusa. Isti odgovor može biti presjek ćelije s klizačem za vodu: spustite ga i vidite kako se membrana odvaja od zida, a vakuola smanjuje.

## Ukratko

[Vještina](/rjecnik/vjestina/) (engl. skill) `objasni-html-stranicom` uči chatbota da na pitanja o pojmu s promjenljivim vrijednostima odgovori jednom HTML stranicom: najviše tri kontrole, stvarne konstante i lista pojednostavljenja. Ispod je vještina za kopiranje, na bosanskom. Urednik ju je isprobao na jednom primjeru, stranici o biljnoj ćeliji ispod. Pravilo "1 do 3 kontrole" je orijentir autora vještine i nema izvor.

## Kada stranica vrijedi više od dijagrama?

Dijagram je jedna slika. Dobar je kad se struktura ne mijenja: ko s kim komunicira, koji korak slijedi. Ne pokazuje šta se dešava kad promijenite ulaznu vrijednost. Stranica s kontrolama to pokazuje. Zato opis vještine traži slučajeve s promjenljivim vrijednostima, pragovima ili koracima, i slučajeve u kojima bi statičan dijagram sakrio kako ulaz mijenja rezultat.

Ako pitanje ima fiksnu strukturu, bolji izbor je vještina iz članka [Objasni dijagramom](/clanci/kako-objasniti-dijagramom/). Tamo su i koraci instalacije vještine u Claudeu, Geminiju i ChatGPT-u, pa ih ovdje ne ponavljamo. Uslovi i ograničenja po alatima su u članku [Šta je SKILL i kako radi?](/clanci/sta-je-skill/#gdje-i-kako-je-dodati).

## Vještina za kopiranje

Ovo je vještina na bosanskom jeziku. Urednik ju je isprobao na jednom primjeru, stranici o biljnoj ćeliji niže. Naziv vještine je `objasni-html-stranicom`.

````markdown
---
name: objasni-html-stranicom
description: "Pravi interaktivnu HTML stranicu u jednom fajlu koja objašnjava pojam, algoritam, sistem ili dio koda. Koristi ovu vještinu kad korisnik želi razumjeti nešto što ima promjenljive vrijednosti, parametre, pragove ili korake koje vrijedi isprobati, ili traži interaktivno, vizuelno ili animirano objašnjenje, objašnjenje 'u HTML-u', demonstraciju, prostor za isprobavanje ili model koji se može pokretati. Koristi je i kad bi statičan dijagram sakrio kako ulazne vrijednosti mijenjaju rezultat."
---

# Objasni HTML stranicom

## Stil pisanja
Odgovaraj na bosanskom jeziku. Piši otprilike 80% puta do ASD-STE100 (načela prenesena na bosanski). Piši kratke rečenice. Koristi aktiv. U svakoj rečenici jedna misao. Biraj jednostavne riječi. Zadrži stručne termine i objasni ih kad se prvi put pojave.

## 1. Planiraj prije izrade
Prvo odgovori na ova tri pitanja:
- Koji je jedan glavni mehanizam koji treba pokazati?
- Koje 1 do 3 vrijednosti najviše mijenjaju rezultat? One postaju kontrole.
- Koji obrazac najbolje odgovara?
  - Trake za podešavanje s rezultatom uživo (parametri, pragovi)
  - Prolazak korak po korak s dugmadima Dalje i Nazad (algoritmi, procesi)
  - Sistem u vremenu s dugmadima Pokreni i Pauziraj (sistemi koji se mijenjaju tokom vremena)
  - Pregled podataka s filterima (skupovi podataka)

## 2. Pravila izrade
- Jedan samostalan `.html` fajl. CSS i JavaScript u samom fajlu. Bez posebnog koraka izgradnje.
- Bez gotovih razvojnih okvira, osim ako tema to traži. Ako koristiš biblioteku, učitaj je s CDN-a i navedi tačnu verziju.
- Raspored koji se prilagođava veličini ekrana. Podrži svijetli i tamni način rada.
- Čist, ravan dizajn. Čitljive veličine slova. Bez ukrasa radi ukrasa.

## 3. Sadržaj na stranici
- Na vrhu: naslov i 2 do 3 rečenice koje kažu šta stranica pokazuje.
- Kontrole: svaka ima oznaku i jedinicu.
- Kratka linija "Probaj ovo", na primjer: "Postavi brzinu iznad 20 i gledaj kako se upozorenje mijenja."
- Na dnu: navedi svako pojednostavljenje. Primjer: "Ovaj model ne uzima u obzir smjer prema objektu."

## 4. Tačnost
- Logiku uzmi iz stvarnog koda ili izvora. Koristi stvarne konstante.
- Ako pojednostaviš logiku, napiši to na stranici.
- Zaokruži svaki broj koji prikazuješ.

## 5. Izlaz
Uvijek isporuči samostalnu HTML stranicu. Ne koristi ugrađeni prikaz u razgovoru, osim ako korisnik to traži.

U Claude Codeu:
- Sačuvaj u `./explainers/<tema>.html`. Napravi folder ako ne postoji.
- Otvori je: `open` na macOS-u, `xdg-open` na Linuxu, `start` na Windowsu.
- Ako postoji preglednik koji radi bez prozora (na primjer Playwright), napravi snimak ekrana i provjeri raspored.

U claude.ai:
- Upiši fajl u `/mnt/user-data/outputs/<tema>.html`.
- Objavi ga kao artifact ako je alat Artifact dostupan. Inače predaj fajl.

## 6. Neka bude za jednokratnu upotrebu
Ova stranica služi za razumijevanje, ne za produkciju. Ne dodavaj testove, pakovanje ni apstrakcije.
````

**Gdje je sačuvati u Claudeu.** Put je (oktobar 2026.): **Settings → Customize → Skills → Add → Create a skill**. Obrazac ima polja **Skill name** i **Description** te veliko polje za upute. U prva dva upišite naziv `objasni-html-stranicom` i opis iz zaglavlja bloka iznad. U veliko polje zalijepite tekst ispod zaglavlja, od naslova "# Objasni HTML stranicom". Pretpostavljamo da zaglavlje između crtica ne treba lijepiti jer obrazac ima posebna polja, ali nismo provjerili šta bi se desilo da ga zalijepite. Postoji i **Upload skill**: urednik u dijalogu vidi da `.md` fajl mora sadržavati naziv i opis u YAML zaglavlju, a `.zip` ili `.skill` fajl mora sadržavati `SKILL.md`. Blok iznad možete dakle sačuvati kao `SKILL.md` i otpremiti. Koraci za Gemini i ChatGPT su u člancima [Objasni dijagramom](/clanci/kako-objasniti-dijagramom/) i [Šta je SKILL i kako radi?](/clanci/sta-je-skill/#gdje-i-kako-je-dodati).

<figure id="fig-obrazac-vjestina" class="ponor-diagram" role="figure" aria-label="Obrazac Create a skill u Claudeu, popunjen tekstom iz ovog članka">
  <img src="/assets/images/2026-10-25-kako-objasniti-html-stranicom-obrazac-vjestina.png" alt="Obrazac Create a skill u Claudeu. U polju Skill name piše objasni-html-stranicom, u polju Description je opis vještine, a u velikom polju ispod počinju upute naslovom Objasni HTML stranicom." loading="lazy" width="1200" height="615">
  <figcaption class="ponor-diagram-caption">Obrazac Create a skill, popunjen tekstom iz ovog članka.</figcaption>
</figure>

## Kako metoda radi

**Stil pisanja.** Pravilo traži oko 80% puta do ASD-STE100, kao i u članku o [Simplified Technical English (STE)](/clanci/asd-ste100-llm/). Standard važi za engleski, pa je u ovoj vještini to prenos načela, ne primjena standarda.

{% include diagram.html name="kako-objasniti-html-stranicom" caption="Četiri koraka vještine: odluka o kontrolama pada u prvom." alt="Upit „Objasni html stranicom, šta je biljna ćelija?“ prolazi četiri koraka vještine (plan, izrada, sadržaj, tačnost) i postaje jedna HTML stranica s kontrolama. Plan je istaknut jer se u njemu bira jedna do tri kontrole." %}

**1. Plan.** Tri pitanja traže da model prije koda izabere jedan mehanizam i najviše tri kontrole. Koliko se model toga drži, nismo mjerili. Pravilo "1 do 3 kontrole" nema izvor: to je orijentir autora vještine. Četiri obrasca su: trake za podešavanje, koraci naprijed i nazad, pokretanje u vremenu i filtriran pregled podataka.

**2. Pravila izrade.** Jedan fajl s CSS-om i JavaScriptom unutra otvara se dvoklikom, bez servera. Tačna verzija biblioteke sprečava da se stranica pokvari kad se biblioteka promijeni. Raspored se prilagođava ekranu, a stranica radi u svijetlom i tamnom načinu rada.

**3. Sadržaj.** Naslov, dvije do tri rečenice, kontrole s jedinicama, linija "Probaj ovo" i lista svih pojednostavljenja. Posljednja stavka štiti čitaoca od pogrešnog zaključka: stranica sama kaže šta izostavlja.

**4. Tačnost.** Stvaran kod ili izvor, stvarne konstante, zaokruženi brojevi. Model koji izmisli konstantu napravi stranicu koja izgleda uvjerljivo, a pogrešno.

**5. Izlaz.** Uvijek samostalna stranica, ne prikaz unutar razgovora. U Claude Codeu fajl ide u `./explainers/<tema>.html` i otvara se. U claude.ai ide u `/mnt/user-data/outputs/` i objavljuje se kao artifact.

**6. Jednokratno.** Bez testova, pakovanja i apstrakcija. Stranica služi za razumijevanje.

## Primjer: biljna ćelija

Urednik je stranicu o biljnoj ćeliji napravio u Claudeu, uz ovu vještinu. Upit je glasio: "Objasni html stranicom, sta je Biljna Celija / Stanica." Navodimo ga doslovno, uključujući pravopis. Stranica uglavnom prati pravila vještine. Pokazuje presjek jedne ćelije. Dijelove na slici možete kliknuti da vidite šta rade. Kontrole su dva klizača, svjetlost i voda, oba u procentima, i klik na dijelove ćelije. Očitanje pokazuje relativnu brzinu fotosinteze i turgor, to jest koliko je ćelija napeta od vode. Ispod slike je lista dijelova ćelije i lista onoga što je pojednostavljeno. Odstupa u jednoj stvari: uvod ima četiri rečenice umjesto 2 do 3.

Vještina traži kratku liniju "Probaj ovo". Stranica je ima i vodi kroz jedan slučaj: spustite vodu ispod 50%, pa se membrana odvaja od zida, a vakuola smanjuje. Ispod 40% voda ograničava i fotosintezu.

Isprobajte stranicu ovdje ili je [otvorite u zasebnom prozoru](/assets/explainers/biljna-celija.html).

<div class="explainer-embed">
<iframe id="explainer-biljna-celija" src="/assets/explainers/biljna-celija.html" title="Biljna ćelija: stranica s kontrolama" loading="lazy" style="width:100%;height:1000px;border:1px solid #d5dce3;border-radius:10px"></iframe>
<script>
// Same-origin embed: copy the site's theme into the frame and fit the frame to its content.
(function () {
  var f = document.getElementById('explainer-biljna-celija');
  function theme() {
    try {
      var d = f.contentDocument;
      if (d) d.documentElement.dataset.theme = document.documentElement.classList.contains('dark') ? 'dark' : 'light';
    } catch (e) {}
  }
  function fit() {
    try {
      var d = f.contentDocument;
      if (d && d.body) f.style.height = (d.body.offsetHeight + 4) + 'px';
    } catch (e) {}
  }
  f.addEventListener('load', function () {
    theme(); fit();
    var d = f.contentDocument;
    if (window.ResizeObserver && d && d.body) new ResizeObserver(fit).observe(d.body);
  });
  new MutationObserver(theme).observe(document.documentElement, { attributes: true, attributeFilter: ['class'] });
})();
</script>
</div>

Brojevi na stranici su ilustracija, a stranica to kaže u listi pojednostavljenja:
- Prag od 40% vode za fotosintezu i prag od 50% za odvajanje membrane od zida (plazmolizu) su ilustracija.
- Rast fotosinteze sa svjetlošću prati krivulju zasićenja s izmišljenom konstantom 25.
- Slika je dvodimenzionalni presjek, a veličine dijelova nisu u razmjeri.
- Endoplazmatski retikulum, citoskelet i peroksizomi nisu nacrtani. Na slici je šest hloroplasta i dva mitohondrija, a prava ćelija lista ima desetine.
- Fotosinteza je relativna brzina: 100% znači punu svjetlost i dovoljno vode.

Naša napomena: biološke tvrdnje na stranici nismo provjeravali prema izvoru. Stranica služi kao primjer onoga što vještina pravi, ne kao udžbenik. Jedan primjer ne pokazuje koliko često vještina daje ovakav rezultat.

## Gdje HTML stranice mogu raditi

**Claude.** [Pomoćna stranica o artifactima](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) opisuje artifacte u claude.ai i navodi pakete Free, Pro, Max, Team i Enterprise. Mora biti uključena opcija "Cloud code execution and file creation" (u novijem rasporedu "Create and edit files"). Stranica spominje i jednostavne web stranice i male interaktivne alate. Druga je stvar objavljivanje iz Claude Codea. [Njegova dokumentacija](https://code.claude.com/docs/en/artifacts) navodi pakete Pro, Max, Team i Enterprise i traži prijavu komandom `/login`. Ona opisuje stroga ograničenja: stranica se služi iz izolovanog sandboxa, skripte se učitavaju samo s nekoliko navedenih adresa i vanjske slike su blokirane. Stranica može ponuditi preuzimanje fajla samo ako račun ima tu funkciju.

**Upozorenje.** Anthropic savjetuje da artifact koji je napravio neko drugi tretirate kao fajl od nepoznatog pošiljaoca. Pokrećete tuđi kod. To je naša napomena, ne Anthropicova: i stranicu koju model napravi na vašem računaru, na primjer pomoću ove vještine u Claude Codeu, otvarate kao kod koji niste pisali.

**Gemini.** [Canvas](https://support.google.com/gemini/answer/16047321) pravi dokumente, aplikacije, prezentacije i kod, uz pregled aplikacije i opciju "Show console". Zahtijeva prijavu. Javni link radi samo na gemini.google.com, ne u mobilnoj aplikaciji. Stranica ne spominje HTML izričito, a ne navodi ni ograničenja mreže.

**ChatGPT.** Prikaz HTML-a nismo mogli potvrditi: odgovarajuća pomoćna stranica OpenAI-ja nije bila dostupna.

Pravila o izlazu u vještini (putanja `/mnt/user-data/outputs`, naredba `xdg-open`, zabrana prikaza unutar razgovora) pisana su za Claude i Claude Code. U Geminiju i ChatGPT-u ne moraju važiti. Ostatak vještine ne spominje nijednu aplikaciju.

Vještinu u Claudeu, Geminiju i ChatGPT-u instalirate kao vještinu iz prethodnog članka. Uslovi i ograničenja po alatima su u članku [Šta je SKILL i kako radi?](/clanci/sta-je-skill/#gdje-i-kako-je-dodati). Za Claude postoje i [službene upute o vještinama](https://support.claude.com/en/articles/12512180-using-skills-in-claude). Prikazuje li svaka aplikacija stranicu koju model napravi, ovdje nismo provjerili.

## Šta NIJE

- **Nije biološki izvor.** Pragovi i konstante na stranici u primjeru su ilustracija, a lista pojednostavljenja kaže gdje se odstupa.
- **Nije garancija da model prati pravila.** Nismo našli da neki proizvođač objavljuje koliko se tačno vještina pokrene kad treba, a vještinu je urednik isprobao samo na jednom primjeru.
- **Nije zamjena za izvor.** Stranica pojednostavljuje. Prije nego što joj vjerujete, pročitajte šta izostavlja.

## Povezano

- [Šta je SKILL i kako radi?](/clanci/sta-je-skill/) – šta je vještina, kako se učitava, gdje radi i na šta paziti.
- [Objasni dijagramom: vještina za Claude, ChatGPT i Gemini](/clanci/kako-objasniti-dijagramom/) – prethodna vještina i koraci instalacije.
- [ASD-STE100: avionska pravila pisanja za vaš chatbot](/clanci/asd-ste100-llm/) – odakle dolazi pravilo "80% puta do STE-a".

## Izvori

- [What are artifacts and how do I use them, Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Share session output as artifacts, Claude Code Docs](https://code.claude.com/docs/en/artifacts)
- [Create and use Canvas in Gemini Apps, Gemini Apps Help](https://support.google.com/gemini/answer/16047321)
- [Use skills in Claude, Claude Help Center](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
