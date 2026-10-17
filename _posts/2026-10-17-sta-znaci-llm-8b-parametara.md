---
layout: post
title: 'Šta znači "8B parametara" kod jezičkog modela'
date: 2026-10-17
category: vodici
image: /assets/images/2026-10-17-sta-znaci-llm-8b-parametara.svg
read_time: 6
description: "Šta su parametri i težine jezičkog modela, šta znači 8B u nazivu i koliko memorije 8B model traži u različitim preciznostima i nakon kvantizacije."
tags: [llm]
---

Ollama za model `qwen3:8b` navodi veličinu od 5,2 GB, a kartica modela (model card) na Hugging Face-u kaže da Qwen3-8B ima 8,2 milijarde parametara. Kad bi se svaki parametar zapisao sa 16 bita, samo bi parametri, po Ponorovom računu, zauzeli oko 16 GB. Otkud razlika? Odgovor su tri stvari: šta je parametar, šta se tačno broji u "8B" i s kojom se preciznošću ti brojevi zapisuju.

## Ukratko

[Parametri](/rjecnik/parametri/) (parameters) su brojevi koji određuju kako se model ponaša: [težine](/rjecnik/tezine/) (weights) i pomaci (bias). Model ih nauči tokom [treniranja](/rjecnik/treniranje/) (training). "8B" znači otprilike osam milijardi parametara. Taj broj u nazivu je zaokružen, a proizvođači ne broje uvijek iste dijelove modela.

Koliko memorije model traži, zavisi od preciznosti zapisa. U 16-bitnom zapisu svaki parametar zauzima dva bajta, pa težine 8B modela, po Ponorovom računu, traže oko 16 GB. Kvantizacija (quantization) težine zapisuje s manje bita, pa na 4 bita staju u oko 4 GB. Ollamin `qwen3:8b` u formatu Q4_K_M ima 5,2 GB jer taj format neke dijelove modela čuva u većoj preciznosti, a u fajlu su i podaci koji nisu težine. Kad su težine objavljene, model možete pokrenuti na vlastitom računaru.

## Parametri i težine

LLM (large language model) je [neuronska mreža](/rjecnik/neuronska-mreza/) (neural network): model koji ulaz pretvara u izlaz kroz ogroman broj uzastopnih računskih koraka. Kako će ti koraci izgledati, određuju parametri.

Udžbenik [Deep Learning](https://www.deeplearningbook.org) (Goodfellow, Bengio i Courville) parametre opisuje kao vrijednosti koje upravljaju ponašanjem sistema. Najjednostavniji primjer je linearni model. Svaki ulaz se pomnoži svojom težinom, a ta težina određuje koliko on utiče na rezultat. Na kraju se doda pomak (bias): broj koji rezultat pomjera nezavisno od ulaza. Težine i pomaci zajedno čine parametre modela.

Neuronska mreža slaže mnogo takvih računa jedan na drugi. Pravila joj niko ne piše ručno. Mreža sama uči vrijednosti svojih parametara, a upravo to je treniranje.

## Kako treniranje postavlja težine

Treniranje mijenja težine sve dok model ne počne davati dobre rezultate na primjerima. Za to su potrebne tri stvari.

Funkcija gubitka (loss function) jednim brojem mjeri koliko model griješi. Gradijent (gradient) pokazuje kako bi se taj broj promijenio kad bismo svaku težinu malo pomjerili. Gradijentni spust (gradient descent) zatim težine pomjera u malim koracima, suprotno od gradijenta, tamo gdje gubitak opada.

Mreža ima milijarde težina, a gradijent se mora izračunati za svaku od njih. Taj posao radi propagacija unazad (back-propagation): informacija o grešci putuje kroz mrežu od izlaza prema ulazu i usput daje gradijent. Goodfellow i saradnici ističu da su to dvije različite stvari. Propagacija unazad samo računa gradijent, a učenje radi drugi algoritam, na primjer varijanta gradijentnog spusta koja u svakom koraku gleda mali, nasumično odabrani dio podataka.

Kod LLM-a težine svoje vrijednosti dobijaju tokom [predtreniranja](/rjecnik/predtreniranje/) (pre-training) i kasnijih faza, koje su opisane u tekstu [Šta je LLM i kako radi?](/clanci/sta-je-llm/). Na kraju dobijemo fajl s težinama.

## Šta se tačno broji u "8B"

"B" dolazi od engleske riječi *billion*, što znači milijarda. Broj u nazivu je zaokružen. U prvom [LLaMA radu](https://arxiv.org/abs/2302.13971v1) Meta navodi da model nazvan "7B" ima 6,7 milijardi parametara, a "33B" 32,5 milijardi. Za [Llamu 3.1 8B](https://arxiv.org/abs/2407.21783v3) Meta piše samo "8B". Ollama na stranici modela [`llama3.1:8b`](https://ollama.com/library/llama3.1:8b) navodi 8,03 milijarde, a za [`qwen3:8b`](https://ollama.com/library/qwen3:8b) 8,19 milijardi.

Drugi razlog za razlike je to šta se uopšte broji. Model svaki [token](/rjecnik/token/) (osnovna jedinica teksta, riječ ili dio riječi) iz svog [vokabulara](/rjecnik/vokabular/) (skup tokena koje model poznaje) predstavlja nizom brojeva, a to je [embedding](/rjecnik/embedding/). I ti brojevi su parametri. [Kartica Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) navodi 8,2 milijarde parametara ukupno i 6,95 milijardi bez embeddinga. Po Ponorovom računu, embeddingovi čine oko 15 posto modela.

Neki autori embeddinge ne računaju. [Kaplan i saradnici](https://arxiv.org/abs/2001.08361v1) su u radu iz 2020. veličinu modela računali bez njih. Google na [kartici modela Gemma 4](https://ai.google.dev/gemma/docs/core/model_card_4) posebno navodi efektivne parametre, tj. broj bez dodatnih velikih tabela embeddinga. Brojke za Gemmu možete naći u našem [vodiču za Ollamu](/clanci/vlastiti-ai-chatbot-ollama-vodic/). Dva modela sa "8B" u nazivu zato ne moraju imati isti broj parametara, a ni isti način brojanja.

Broj parametara sam po sebi ne određuje kvalitet. [Hoffmann i saradnici](https://arxiv.org/abs/2203.15556v1) trenirali su Chinchillu sa 70 milijardi parametara, uz istu količinu računanja kao za Gopher (280 milijardi). Prema autorima, Chinchilla dosljedno i znatno nadmašuje i Gopher i GPT-3 (175 milijardi).

## Koliko memorije treba 8B model?

Svaki parametar je broj, a broj se zapisuje u nekom formatu. Format određuje preciznost (precision), odnosno koliko bita zauzima jedan broj. Osam bita čini jedan bajt (byte). [PyTorch dokumentacija](https://docs.pytorch.org/docs/2.14/tensor_attributes.html) navodi nekoliko formata brojeva, među njima:

- FP32: 32-bitni broj s pokretnim zarezom (floating point), 4 bajta.
- FP16 i BF16: dva različita 16-bitna formata s pokretnim zarezom, po 2 bajta.
- int8: 8-bitni cijeli broj, 1 bajt.

Na osnovu toga, evo Ponorovog računa za same težine modela s osam milijardi parametara:

| Preciznost | Bajta po parametru | Težine 8B modela |
|---|---|---|
| FP32 | 4 | oko 32 GB |
| FP16 / BF16 | 2 | oko 16 GB |
| 8 bita | 1 | oko 8 GB |
| 4 bita | 0,5 | oko 4 GB |

{% include diagram.html name="sta-znaci-llm-8b-parametara" caption="Isti 8 milijardi parametara zauzima od oko 32 GB (FP32) do oko 4 GB (4 bita). Ponorov račun, samo težine." alt="Stubičasti prikaz memorije za težine 8B modela u četiri preciznosti, s oznakom za Ollamin qwen3:8b od 5,2 GB." %}

Taj račun (8 milijardi × broj bajta) nije podatak proizvođača i odnosi se samo na težine. Za pokretanje modela treba i dodatna memorija, bilo u RAM-u (radna memorija) bilo u memoriji grafičke kartice (GPU), koja se zove VRAM.

Ollamin `qwen3:8b` od 5,2 GB koristi format Q4_K_M. Taj format kombinuje više načina zapisa, a neke dijelove modela čuva u većoj preciznosti. U prosjeku to izađe na otprilike 4 do 5 bita po težini. U fajlu su i podaci koji nisu težine, pa se veličina fajla ne može tačno izračunati iz broja parametara. `llama3.1:8b` u istom formatu ima 4,9 GB. Ollama te veličine može promijeniti u novim verzijama.

## Kvantizacija: manje bita po težini

Kvantizacija težine zapisuje s manjom preciznošću, pa je model manji i troši manje memorije. Otvoreno pitanje je koliko pri tome gubi na kvalitetu. Dva rada iz 2022. dala su odgovore za tadašnje modele:

- [Dettmers i saradnici](https://arxiv.org/abs/2208.07339v2) (LLM.int8()) navode da 8-bitni zapis upola smanjuje memoriju potrebnu za pokretanje modela. Prema autorima, pada performansi nema čak ni kod modela sa 175 milijardi parametara.
- [Frantar i saradnici](https://arxiv.org/abs/2210.17323v2) (GPTQ) težine svode na 3 ili 4 bita po težini, uz, kako kažu, zanemariv pad tačnosti. Model sa 175 milijardi parametara tako staje na jednu grafičku karticu.

Oba rezultata su mjerenja samih autora, na modelima iz 2022. Ona ne govore koliko kvaliteta gubi Qwen3-8B u formatu Q4_K_M, niti kako se kvantizacija odražava na tekst na bosanskom.

## Zašto je važno da su težine objavljene

Open Source Initiative u definiciji [OSAID 1.0](https://opensource.org/ai/open-source-ai-definition) težine opisuje kao skup naučenih parametara koji se primjenjuju na arhitekturu modela (model architecture). Arhitektura je plan računanja, a težine su brojevi koji u taj plan ulaze. Bez težina, arhitektura nije ni od kakve koristi.

Kad proizvođač objavi težine, dobijamo [model otvorenih težina](/rjecnik/otvorene-tezine/) (open-weight). Ako licenca to dozvoljava, takav model možete preuzeti, sami kvantizovati i pokrenuti kao [lokalni model](/rjecnik/lokalni-model/), na vlastitom računaru.

Ipak, objavljene težine nisu isto što i [otvoreni kod](/rjecnik/otvoreni-kod/) (open source). Da bi se po OSAID 1.0 smatrale otvorenim kodom, uz težine moraju biti objavljeni i informacije o podacima i kod kojim su dobijene, i to pod uslovima koje OSI odobrava. Šta smijete raditi sa samim težinama, određuje licenca. Qwen3-8B objavljen je pod licencom Apache 2.0, a Llama 3.1 pod Metinom vlastitom licencom, [Llama 3.1 Community License](https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE).

## Šta ovo znači pri izboru modela

- Tačan broj parametara potražite na kartici modela, a ne u nazivu.
- Za grubu procjenu memorije pomnožite broj parametara s brojem bajta po parametru i ostavite rezervu za pokretanje. Na 4 bita težine 8B modela traže oko 4 GB, a Ollamini fajlovi imaju 4,9 do 5,2 GB.
- Više parametara ne znači automatski bolji model.
- Tvrdnje da kvantizacija ne smanjuje kvalitet važe samo za modele i testove na kojima su mjerene.

## Povezano

- [Šta je LLM i kako radi?](/clanci/sta-je-llm/) – kako model generiše tekst i kroz koje faze treniranja prolazi.
- [Vlastiti AI chatbot na računaru: Ollama vodič od nule](/clanci/vlastiti-ai-chatbot-ollama-vodic/) – kako 8B model zaista pokrenuti na svom računaru.
- [Šta je LLM token i kako radi tokenizacija?](/clanci/sta-je-llm-token/) – šta su tokeni čiji embeddingovi zauzimaju dio parametara.

## Izvori

- [Deep Learning, pogl. 4.3, 5.1.4, 6 – Goodfellow, Bengio, Courville, MIT Press 2016](https://www.deeplearningbook.org)
- [Qwen3-8B – Qwen, Hugging Face](https://huggingface.co/Qwen/Qwen3-8B)
- [LLaMA: Open and Efficient Foundation Language Models – Touvron et al., Meta 2023](https://arxiv.org/abs/2302.13971v1)
- [Tensor Attributes – PyTorch 2.14 dokumentacija](https://docs.pytorch.org/docs/2.14/tensor_attributes.html)
- [LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale – Dettmers et al., 2022](https://arxiv.org/abs/2208.07339v2)
- [GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers – Frantar et al., 2022](https://arxiv.org/abs/2210.17323v2)
- [The Open Source AI Definition 1.0 – Open Source Initiative](https://opensource.org/ai/open-source-ai-definition)
