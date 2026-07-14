---
layout: post
title: "Alibaba gasi Qwenove agente s funkcijom persistent memory prije kineske regulacije o antropomorfnim AI uslugama"
date: 2026-07-07
description: "Alibaba će 10. jula isključiti Qwenove antropomorfne interaktivne agente pred kineski rok od 15. jula za usklađivanje s novim propisima o antropomorfnim AI uslugama — bez najavljenog perioda za izvoz podataka."
category: vijesti
image: /assets/images/2026-07-07-qwen-memory-shutdown.svg
audience: developers
read_time: 3
---

Alibaba će 10. jula isključiti Qwenove antropomorfne interaktivne agente i korisnički kreirane agentne (agentic) funkcije — dan prije nego što u Kini stupe na snagu Privremene mjere o upravljanju antropomorfnim interaktivnim AI uslugama (Interim Measures for the Administration of AI Anthropomorphic Interactive Services), koje na snagu stupaju 15. jula 2026. Puno gašenje agentnih funkcija i usluga planirano je za 15. jul, kada će korisnici izgubiti i pristup historiji ranijih razgovora — Qwen do sada nije objavio nikakav period ili mehanizam za izvoz podataka.

## Šta se desilo

Finalni tekst mjera objavila je kineska Cyberspace Administration (CAC) 10. aprila 2026, zajedno s NDRC, MIIT, Ministarstvom javne sigurnosti i SAMR-om ([CAC](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm)); nacrt je bio poznat od decembra 2025, a engleski prevod finalnog teksta objavio je [China Law Translate](https://www.chinalawtranslate.com/human-like-ai/). Qwen je promjenu interno opisao kao "prilagodbu proizvodnih funkcija" ("product function adjustments") — nijedna zvanična izjava kompanije ne navodi regulaciju kao razlog gašenja.

ByteDance-ov Doubao slijedi isti rok od 15. jula, ali korisnicima ostavlja tromjesečni period samo za čitanje (read-only), do 15. oktobra, prije brisanja podataka. Qwen tu opciju nije ponudio. Za kontekst razmjera, prema [SCMP](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom): Doubao ima oko 345 miliona aktivnih korisnika mjesečno, Qwen znatno manje — oko 166 miliona. Ova dva broja se u dosadašnjem izvještavanju često pobrkaju, pa vrijedi razdvojiti ih po kompaniji.

## Zašto je važno

Mjere ne regulišu AI generalno, nego usko ciljaju jednu kategoriju: AI koji simulira ličnost, način razmišljanja ili komunikacijski stil radi produžene emocionalne interakcije. Produktivni alati, korisnička podrška i Q&A botovi su eksplicitno izuzeti. Za usluge koje spadaju u kategoriju, mjere traže: obavezno obilježavanje da je riječ o AI, detekciju prekomjerne zavisnosti korisnika s podsjetnicima, obavezno upozorenje nakon dva sata neprekidne interakcije, trenutni izlaz na zahtjev korisnika, te sigurnosnu procjenu za usluge s više od milion registrovanih ili 100.000 aktivnih korisnika mjesečno.

Bitno je razdvojiti ovo gašenje — kompanijski, dobrovoljni potez prije stupanja zakona na snagu — od suspenzije koju bi nametnula država nekom već postojećem proizvodu. Qwen ovdje sam isključuje funkciju da bi izbjegao neusklađenost, ne čeka nalog. Nijedna kompanija do sada nije objavila da li i kada se planira usklađena verzija agenta s pamćenjem vratiti.

## Šta to znači u praksi

Za inžinjere koji grade slične agentne proizvode, ovo je konkretan slučaj strukturnog sukoba: zahtjevi za trenutnim izlazom i detekcijom prekomjerne zavisnosti stoje u direktnoj tenziji s tipičnim dizajnom agenta koji koristi persistent memory kroz sesije — sistem mora istovremeno pamtiti korisnika i biti spreman da ga odmah "pusti" na zahtjev, bez pokušaja retencije.

Ostaje otvoreno pitanje da li se gašenje odnosi samo na Qwenovu potrošačku aplikaciju za chat ili i na developer-facing API i agentne alate — do sada nema izvora koji to potvrđuje u bilo kojem smjeru, pa to ne treba tretirati kao riješeno. Ako gradite proizvod s komponentom emocionalne interakcije za kineski ili širi azijski tržišni prostor, vrijedi ovo pratiti i šire: slična regulatorna logika postoji i u drugim jurisdikcijama, npr. u EU. Regulatorni pritisak na ovu kategoriju proizvoda nije samo kineska priča.

## Izvori
- [CAC — zvanično objavljivanje finalnih Mjera (kineski)](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm)
- [China Law Translate — engleski prevod Mjera](https://www.chinalawtranslate.com/human-like-ai/)
- [South China Morning Post — detalji gašenja na nivou kompanija](https://www.scmp.com/tech/big-tech/article/3359482/bytedance-and-alibaba-disable-humanlike-ai-custom-agents-new-rules-loom)
