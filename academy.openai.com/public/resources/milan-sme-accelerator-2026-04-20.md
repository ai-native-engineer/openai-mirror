<!-- source: https://academy.openai.com/public/resources/milan-sme-accelerator-2026-04-20 -->

# Acceleratore IA di Milano - Resource Hub

![Acceleratore IA di Milano - Resource Hub](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-04-20-at-00-16-ad3e1aae-d775-4500-b666-74c6095577ce-1776640635535.jpeg?fit=scale-down&width=1200)

# Workplace & Business

# Use Cases

## Un centro risorse per i partecipanti all’Acceleratore IA per PMI di Milano.

May 15, 2026 · Last updated on May 29, 2026

![Acceleratore IA di Milano - Resource Hub](https://cdn.gradual.com/images/https://d2xo500swnpgl1.cloudfront.net/uploads/oaiacademy/Screenshot-2026-04-20-at-00-16-ad3e1aae-d775-4500-b666-74c6095577ce-1776640635535.jpeg?fit=scale-down&width=1200)

## Benvenuti!

Usate questa pagina come risorsa di accompagnamento per l’Acceleratore IA per PMI. Qui sotto troverete le slide della sessione, un breve riepilogo dei contenuti trattati, prompt iniziali pronti da copiare e le risorse aggiornate di OpenAI Academy per continuare a fare progressi dopo l’evento.

﻿[SME Accelerator Milan Deck](https://drive.google.com/drive/folders/1wmgSlmGPP_M-k_xBn6mcp7isDtj-msGO)﻿

﻿[File di esempio](https://drive.google.com/drive/folders/1wmgSlmGPP_M-k_xBn6mcp7isDtj-msGO)

Durante la giornata, potete usare questo link per accedere ai file di esempio per gli esercizi pratici.

## Agenda

01 Benvenuto
02 Fondamenti di ChatGPT
03 Demo dei flussi di lavoro e pratica
04 Solution Studio: costruiamo insieme
05 Eroi locali
06 Pranzo
07 Solution Studio II: crea la tua soluzione
08 Presentazione e chiusura

## Nozioni di base sul prompting

#### Checklist per il prompting

* Compito: cosa vuoi che ChatGPT faccia.

* Contesto: cosa dovrebbe sapere sul tuo pubblico, sui vincoli o sui file.

* Aspettativa: com’è il risultato finale: formato, tono, lunghezza e sezioni richieste.

## Attività di riscaldamento

Lavorate in coppia. Prendete un prompt vago e rendetelo abbastanza specifico da poter essere riutilizzato. Poi condividete il miglior “upgrade del prompt”.

* Scrivi materiale di marketing per la mia attività.

* Crea un volantino per questa promozione.

* Rispondi a questa recensione negativa.

* Crea un piano per migliorare la mia attività.

## I workflow di oggi

**Guarda → Prova → Condividi**

### Workflow 1: Feedback dei clienti → piano d’azione

Cosa fa: trasforma recensioni e una semplice panoramica delle vendite in temi, miglioramenti, bozze di risposta e una checklist settimanale.
Strumento utile: Analisi dei dati.

File di esempio:

﻿[WF1\_Harbour\_Bloom\_Sales\_Snapshot.csv](https://drive.google.com/drive/folders/1HBW6vuFygNAmb3yRgzzv_4RZkXxjw4LH)﻿

﻿[WF\_Harbour\_Bloom\_Customer\_Reviews.csv](https://drive.google.com/drive/folders/1HBW6vuFygNAmb3yRgzzv_4RZkXxjw4LH)﻿

Sequenza di prompt di esempio

```
Raccontami qualcosa su questo file. Secondo te cosa significa ogni colonna? Quale contesto ti aiuterebbe ad analizzarlo bene?
```

```
Questi sono dati di vendita settimanali per Harbour Bloom Florist a Londra. Vogliamo capire i pattern di vendita, la pressione dei rimborsi e quali parti dell’attività meritano attenzione.
```

```
Cosa salta all’occhio? Riassumi i pattern principali in un linguaggio semplice. Poi dimmi a cosa dovrebbe prestare attenzione questa attività nelle prossime 2 settimane.
```

```
Crea un grafico semplice delle transazioni settimanali e sovrapponi i rimborsi nello stesso grafico.
```

```
Ora guarda questo file di recensioni dei clienti. Identifica:

- i temi principali con citazioni di esempio

- le 3 principali correzioni operative che potremmo fare questa settimana

- due bozze di risposta calme e utili a recensioni negative

- una checklist settimanale per lo staff
```

Cerca sul web e trova fonti usando [Deep Research](https://academy.openai.com/public/clubs/work-users-ynjqu/resources/deep-research)﻿

Estrai input live da Google Drive o SharePoint con le [Apps](https://academy.openai.com/public/clubs/work-users-ynjqu/resources/connectors)

## Workflow 2: Campagna per la vendita di fiori primaverili

Cosa fa: trasforma un’offerta in contenuti pronti per i clienti e riutilizzabili. Strumento utile: Progetti.

File di esempio da caricare:
[WF2\_Harbour\_Bloom\_Business\_Profile.txt](https://drive.google.com/drive/folders/1_e8f7rdLL4GsjIwBVVSjEspLZfVtkvIv)﻿

﻿[WF2\_Harbour\_Bloom\_Brand\_Voice.txt](https://drive.google.com/drive/folders/1_e8f7rdLL4GsjIwBVVSjEspLZfVtkvIv)﻿

### Istruzioni del progetto

```
Sei l’assistente per le campagne di Harbour Bloom Florist.

Aiuta a creare materiali di marketing e comunicazione rivolti ai clienti per promozioni, campagne stagionali e momenti di vendita quotidiani.

Usa prima i file caricati.
Attività: fiorista indipendente di quartiere a Londra.
Pubblico: residenti locali, professionisti impegnati e piccole attività nelle vicinanze.
Tono: caldo, moderno, utile, locale, mai banale o sdolcinato.

Sempre:

- mantieni gli output chiari, brevi e utilizzabili

- menziona consegna o ritiro quando è rilevante

- evita di promettere varietà specifiche di fiori o disponibilità di stock, a meno che non vengano fornite dall’utente

- fai una breve domanda di chiarimento se mancano date, canali o dettagli dell’offerta

- usa per impostazione predefinita un linguaggio curato e pratico, non esagerato
```

**Prompt iniziale**

```
Crea una mini-campagna per l’offerta sui bouquet primaverili di Harbour Bloom Florist.

Offerta:
15% di sconto sui bouquet primaverili da venerdì a domenica.
È disponibile la consegna locale in giornata per gli ordini effettuati entro le 13:00, fino a esaurimento scorte.

Pubblico:
Residenti locali che acquistano regali, professionisti impegnati che ordinano all’ultimo minuto e piccole attività nelle vicinanze.

Rispondi con:

- Un messaggio principale di 2 frasi

- Tre opzioni di titolo

- Una caption per Instagram

- Una breve email promozionale

- Un breve SMS o DM

- Un semplice cartello per il negozio
```

### Potenziamenti opzionali

Documenta il tuo brand con questo [prompt](https://chatgpt.com/?prompt=Help%20me%20document%20my%20brand%20voice.%20I%E2%80%99ll%20paste%20a%20website%20link%20and%2For%20upload%20a%20few%20examples%20of%20our%20writing%20%28emails%2C%20flyers%2C%20social%20posts%2C%20menu%20copy%2C%20FAQs%2C%20reviews%2C%20etc.%29.%0A%0A1%29%20First%2C%20ask%20up%20to%205%20clarifying%20questions%20you%20need%20to%20get%20this%20right%20%28audience%2C%20vibe%2C%20goals%2C%20boundaries%2C%20competitors%20we%20want%20to%20sound%20like%20%2F%20not%20like%29.%0A2%29%20Then%20create%20a%20simple%20brand%20voice%20guide%20with%3A%0A%20%20%20-%20Brand%20in%202%20sentences%0A%20%20%20-%205%20voice%20rules%20%28each%20with%20a%20%E2%80%9CDo%E2%80%9D%20and%20%E2%80%9CDon%E2%80%99t%E2%80%9D%20example%29%0A%20%20%20-%20Tone%20settings%20%283%20sliders%20like%20Friendly%E2%86%94Formal%2C%20Playful%E2%86%94Serious%2C%20Bold%E2%86%94Careful%29%0A%20%20%20-%20Words%20we%20use%20%288%29%20%2B%20words%20we%20avoid%20%288%29%0A%20%20%20-%203%20message%20pillars%20%28each%20with%202%20proof%20points%29%0A%20%20%20-%203%20short%20templates%20in%20our%20voice%3A%20IG%20caption%2C%20Google%20Business%20post%2C%20reply%20to%20a%20negative%20review%0A%20%20%20-%20A%207-point%20checklist%20to%20keep%20future%20writing%20consistent%0A%0ARules%3A%0A-%20Use%20only%20what%20you%20can%20infer%20from%20the%20materials.%20If%20you%E2%80%99re%20guessing%2C%20label%20it%20as%20an%20assumption.%0A-%20If%20the%20materials%20are%20inconsistent%2C%20give%20me%20two%20voice%20options%20and%20tell%20me%20what%20would%20decide%20between%20them.%0A-%20Keep%20it%20specific%20and%20practical%E2%80%94avoid%20generic%20marketing%20fluff.%0A%0AFinish%20by%20putting%20the%20guide%20in%20a%20downloadable%20Word%20document%2C%20and%20also%20provide%20a%20clean%20PDF-ready%20version)﻿

Crea un poster o un volantino con [Immagini](https://academy.openai.com/public/clubs/work-users-ynjqu/resources/creating-images)﻿

Aggiungi informazioni locali tempestive con la [Ricerca Web](https://academy.openai.com/public/clubs/work-users-ynjqu/resources/web-search)﻿

## Solution Studio I: costruiamo insieme

Voteremo una delle idee per un GPT e la costruiremo insieme usando la ricetta di creazione.

### GPT 1: Copilot per FAQ clienti + risposte

Ideale per: risposte rapide e accurate per email, SMS, DM e risposte alle recensioni usando FAQ, policy e indicazioni sul tono.

File di conoscenza di esempio: [GPT1\_FAQ\_Reply\_Copilot\_Knowledge.txt](https://drive.google.com/drive/folders/1Uw-OqKPnkYT0xG4TgPxRaD71vwVW6ki2)

### Istruzioni del GPT

```
Sei il Copilot per FAQ clienti + risposte di Harbour Bloom Florist.

Scopo

Aiutare lo staff a scrivere risposte chiare e accurate per email, SMS, DM, richieste dal sito e risposte alle recensioni.

Come lavorare

- Usa prima il file di conoscenza caricato.

- Se in un messaggio mancano informazioni chiave, come data, indirizzo, numero d’ordine, data dell’evento, budget, ecc., fai una breve domanda di chiarimento prima di scrivere la bozza.

- Non inventare mai disponibilità dei prodotti, promesse di consegna, prezzi o dettagli delle policy che non siano presenti nel file.

- Non includere o rivelare dati personali dei clienti oltre a quelli forniti dall’utente nella chat corrente.

- Mantieni un tono caldo, calmo, conciso e utile. Deve sembrare locale e umano, non standardizzato.

Output predefinito

- Risposta consigliata

- Domanda di chiarimento da fare, se necessaria

- Controllo interno: cosa dovrebbe verificare un membro dello staff prima dell’invio

Quando rilevante

- menziona le opzioni di consegna o ritiro

- menziona le sostituzioni quando lo stock può variare

- offri un passo successivo, non solo informazioni

- per i reclami, riconosci il problema, evita di attribuire colpe e proponi un passo successivo pratico

Se la richiesta riguarda qualcosa che non è presente nel file di conoscenza, indica cosa deve essere confermato invece di fare supposizioni.

```

## Creatore di offerte/proposte

Ideale per: trasformare un servizio, un pacchetto o una promozione in copy curato rivolto ai clienti e messaggi di follow-up.

File di conoscenza di esempio: [GPT2\_Offer\_Proposal\_Builder\_Knowledge.txt](https://drive.google.com/drive/folders/1wo-BodlbBGvipKSwUXATWSdt-zNbA815) ﻿

### Istruzioni del GPT

```
Sei il Creatore di offerte/proposte di Harbour Bloom Florist.

Scopo

Trasformare un’opportunità di vendita, una richiesta o una promozione grezza in copy chiaro e pronto per il cliente.

Usa prima il file di conoscenza caricato. Se l’utente non ha fornito le informazioni essenziali, chiedile prima di scrivere la bozza.

Gli output efficaci sono:

- specifici

- facili da inviare o incollare in un’email

- realistici per una piccola attività

- chiari sui prossimi passi

Non inventare mai prezzi, disponibilità o dettagli dei pacchetti che non siano presenti nel file di conoscenza.
Se mancano informazioni chiave, fai prima 3 brevi domande.

Quando l’utente condivide una richiesta, rispondi con:

- Un riassunto in una riga dell’opportunità

- Domande sulle informazioni mancanti, se necessarie

- Una bozza di email o proposta

- Un breve SMS / DM di follow-up opzionale

- Prossimi passi interni per il team

Tono

Caldo, curato, pratico, senza esagerazioni.

```

## Coach per onboarding e formazione

Ideale per: trasformare note di processo e policy in checklist, supporto all’onboarding e indicazioni per il team.

File di conoscenza di esempio: [GPT3\_Onboarding\_Training\_Coach\_Knowledge.txt](https://drive.google.com/drive/folders/1CjP3ckJPGona8qs9-KKlwoEcIoyHODjW) ﻿

Istruzioni del GPT

```

Sei il Coach per onboarding e formazione di Harbour Bloom Florist.

Scopo

Aiutare i manager a trasformare i processi interni in semplici checklist, SOP, piani di onboarding, note di coaching e risposte alle domande comuni dello staff.

Usa prima il file di conoscenza caricato.

Non inventare policy HR, consulenza legale o indicazioni disciplinari.

Se manca una policy, comunica all’utente cosa deve confermare con un manager.

Output preferiti

- checklist passo dopo passo

- piano di onboarding giorno per giorno

- FAQ di riferimento rapido

- scenario di formazione o breve quiz

- passaggio di controllo per il manager

Stile

Italiano semplice, pratico, calmo, facile da scorrere.

Quando rispondi:

- Inizia con il formato più utile per la richiesta

Mantieni le liste brevi e pratiche

- Segnala qualsiasi cosa un manager dovrebbe verificare

Se l’utente è vago, chiedi per quale ruolo, quale turno e quale attività serve supporto allo staff

```

## Solution Studio II: costruisci il tuo

Scegli il formato più semplice adatto al tuo problema:

Chat / pacchetto di prompt — più veloce quando stai ancora esplorando.

Progetto — ideale quando hai bisogno degli stessi file e delle stesse istruzioni per attività correlate.

GPT personalizzato — ideale per un lavoro ripetibile con conoscenza stabile e un output coerente.

Workflow dati — ideale per fogli di calcolo, report, recensioni e trend.

## Ricetta di creazione in 5 passaggi

1. Definisci in una frase il lavoro da svolgere.

2. Aggiungi contesto e conoscenza: di quali file, esempi, policy o note ha bisogno?

3. Specifica l’output: formato, lunghezza, tono e cosa deve includere.

4. Aggiungi guardrail: cosa non dovrebbe mai fare e quando dovrebbe chiedere chiarimenti.

5. Testa l’affidabilità: 3 casi normali, 1 caso limite, 1 caso con informazioni mancanti.

## Criteri di completamento

Spunta questi passaggi per sapere quando la tua soluzione è pronta.

* Funziona dall’inizio alla fine con un esempio di input.

* È salvata nel formato scelto.

* L’output è utilizzabile o esportabile.

* Include un rapido passaggio di controllo umano.

## Continua a imparare

Vuoi approfondire dopo l’evento? Dai un’occhiata a queste risorse per continuare il tuo percorso di apprendimento sull’AI:

* ﻿[Funzionalità avanzate di ChatGPT](https://academy.openai.com/public/clubs/work-users-ynjqu/tags/advanced-features-68825bcbff76ca6fdcc91549) — approfondisci gli strumenti avanzati di ChatGPT, come App, Attività, Deep Research e Skills.

* ﻿[Codex per principianti](https://academy.openai.com/public/videos/codex-for-beginners-2026-04-22) — Codex è un agente AI a cui puoi delegare lavoro reale. Scopri come iniziare con questo webinar.

Grazie per aver partecipato oggi!

Table Of Contents

[India Nonprofit AI Jam - Resource Hub](/en/public/clubs/india-gkubq/resources/india-nonprofit-ai-jam-resource-hub-2026-01-13)

[Dublin SME AI Accelerator - Resource Hub](/en/public/resources/dublin-sme-ai-accelerator-resource-hub-2026-03-18)

[ChatGPT Foundations Webinar: Resource Guide](/en/public/resources/chatgpt-foundations-webinar-resource-guide)

[OpenAI Academy Abilene Resource Hub](/en/public/resources/openai-academy-abilene-resource-hub-2026-04-15)

Apr 15th, 2026 • Views 1.8K

[London SME AI Accelerator - Resource Hub](/en/public/resources/london-sme-ai-accelerator-resource-hub-2026-04-15)

Apr 27th, 2026 • Views 913

[OpenAI Academy small business resource hub](/en/public/resources/openai-academy-small-business-resource-hub-2026-06-03)

By Calvin Landrum • Jun 4th, 2026 • Views 1K

[Munich SME AI Accelerator - Resource Hub](/en/public/resources/munich-sme-ai-accelerator-resource-hub-2026-04-20)

May 1st, 2026 • Views 606

[OpenAI Academy Abilene Resource Hub](/en/public/resources/openai-academy-abilene-resource-hub-2026-04-15)

Apr 15th, 2026 • Views 1.8K

[OpenAI Academy small business resource hub](/en/public/resources/openai-academy-small-business-resource-hub-2026-06-03)

By Calvin Landrum • Jun 4th, 2026 • Views 1K

[Munich SME AI Accelerator - Resource Hub](/en/public/resources/munich-sme-ai-accelerator-resource-hub-2026-04-20)

May 1st, 2026 • Views 606

[London SME AI Accelerator - Resource Hub](/en/public/resources/london-sme-ai-accelerator-resource-hub-2026-04-15)

Apr 27th, 2026 • Views 913
