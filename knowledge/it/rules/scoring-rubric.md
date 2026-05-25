# Rubrica di Valutazione — Localizzazione Italiana

Questa rubrica definisce i criteri di valutazione per la qualita delle traduzioni verso l'italiano. Ogni dimensione viene valutata su 6 bande (0–5) e moltiplicata per il peso corrispondente. Il punteggio globale e la somma pesata, espressa in percentuale.

---

## Struttura della valutazione

| Fascia | Punteggio | Descrizione sintetica |
|--------|-----------|----------------------|
| 5 | 100 % | Eccellente — supera gli standard, nessun intervento necessario |
| 4 | 80 % | Buono — lievi imperfezioni, intervento minimo |
| 3 | 60 % | Sufficiente — accettabile, richiede revisione mirata |
| 2 | 40 % | Scarso — problemi diffusi, richiede revisione significativa |
| 1 | 20 % | Gravemente insufficiente — non accettabile, da rifare |
| 0 | 0 % | Nullo — non valutabile o completamente assente |

### Calcolo del punteggio

Per ogni dimensione: `punteggio_dimensione = peso × (voto_banda / 5)`

Punteggio globale: `Σ punteggi_dimensione` (espresso in %)

### Soglie di accettazione

| Giudizio | Intervallo | Azione |
|----------|------------|--------|
| Superato | ≥ 85 % | Approvato |
| Condizionato | 70–84 % | Revisione mirata richiesta |
| Non superato | 50–69 % | Revisione approfondita obbligatoria |
| Critico | < 50 % | Rifiutato — ritraduzione necessaria |

---

## Dimensioni di valutazione

---

## 1. Accuratezza Numerica — Peso: 30 %

Verifica che tutti i valori numerici, le unita di misura, le percentuali, le date e gli importi siano correttamente convertiti nel formato italiano.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Tutti i formati numerici sono corretti in italiano. Decimali con virgola, migliaia con punto, date in DD/MM/YYYY, ore in 24h, valuta con simbolo dopo l'importo. Zero errori. |
| 4 | Buono | Almeno il 95 % dei formati è corretto. Fino a 2 errori minori (es. spaziatura della valuta, ordinale non corretto). Nessun errore su decimali/migliaia. |
| 3 | Sufficiente | Almeno l'85 % dei formati è corretto. Fino a 5 errori, inclusi al massimo 1 errore su decimali o migliaia. Date e ore generalmente corrette. |
| 2 | Scarso | Almeno il 70 % dei formati è corretto. Errori diffusi su date, ore o valute. Presenza di 2 o piu errori su decimali/migliaia. |
| 1 | Gravemente insufficiente | Meno del 70 % dei formati è corretto. Errori sistematici su decimali, migliaia, date o valute. |
| 0 | Nullo | I formati numerici non sono stati affatto convertiti (tutto in formato originale russo/inglese). |

### Zero tolerance

Un singolo errore di **scambio tra punto e virgola nei decimali** (es. `3.14` invece di `3,14`) o un **formato data errato** (es. `12/25/2024` invece di `25/12/2024`) abbassa automaticamente il voto a 0 per questa dimensione, indipendentemente dal resto.

---

## 2. Coerenza Terminologica — Peso: 20 %

Valuta la consistenza nell'uso dei termini tecnici, dei nomi propri, delle sigle e del lessico specialistico in tutto il documento.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Terminologia perfettamente coerente in tutto il documento. Ogni termine tecnico ha una e una sola traduzione. Sigle e acronimi sono gestiti correttamente (definizione alla prima occorrenza). |
| 4 | Buono | Coerenza terminologica molto elevata. 1–2 oscillazioni minori che non compromettono la comprensione. Sigle e acronimi gestiti correttamente. |
| 3 | Sufficiente | Coerenza terminologica complessivamente accettabile. 3–5 oscillazioni o incongruenze, nessuna su termini chiave. Qualche sigla non definita alla prima occorrenza. |
| 2 | Scarso | Coerenza terminologica insufficiente. 6–10 oscillazioni, incluso qualche termine chiave tradotto in modo diverso in punti diversi del documento. Sigle non definite. |
| 1 | Gravemente insufficiente | Coerenza terminologica gravemente carente. Oltre 10 oscillazioni. Termini chiave tradotti in modo erratico. Uso di sinonimi non giustificato. |
| 0 | Nullo | Nessuna coerenza terminologica. I termini sono tradotti in modo casuale, senza uno schema riconoscibile. |

### Casi particolari

- Un glossario di progetto approvato deve essere rispettato al 100 %. Ogni deviazione dal glossario conta come 1 errore.
- Per termini non presenti nel glossario, si valuta la coerenza interna al documento.
- Nomi propri e marchi: la loro alterazione (es. traduzione di un marchio registrato) conta come errore grave.

---

## 3. Fedelta Semantica — Peso: 25 %

Misura la corrispondenza del significato tra testo originale e testo tradotto, escludendo gli aspetti puramente formali.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Significato perfettamente preservato. Nessuna omissione, aggiunta o distorsione. Sfumature, tono e intenzioni comunicative rese fedelmente. |
| 4 | Buono | Significato sostanzialmente preservato. Lievi differenze semantiche che non alterano la comprensione. Al massimo 1 omissione o aggiunta minore irrilevante. |
| 3 | Sufficiente | Significato generale preservato. 2–3 imprecisioni semantiche o omissioni minori. Il messaggio complessivo rimane comprensibile e corretto. |
| 2 | Scarso | Significato parzialmente alterato. 4–6 errori semantici, omissioni o aggiunte indebite. Il messaggio originale e percepibile ma con distorsioni significative. |
| 1 | Gravemente insufficiente | Significato ampiamente alterato. Numerosi errori semantici (7+), omissioni di intere frasi o paragrafi, aggiunte non giustificate. |
| 0 | Nullo | Il testo tradotto non corrisponde all'originale. Significato completamente diverso o inventato. |

### Avvertenze

- La fedelta semantica non significa traduzione letterale; una riformulazione che preserva il significato e migliore di una traduzione parola per parola.
- Le aggiunte giustificate da differenze grammaticali o culturali (es. articoli, preposizioni, esplicitazioni) **non** sono considerate errori.
- Le omissioni di dettagli irrilevanti per il contesto italiano (es. riferimenti a normative russe non applicabili) sono accettabili se documentate.

---

## 4. Conformita Formale — Peso: 10 %

Valuta l'aderenza del testo tradotto alle regole di formattazione, punteggiatura, spaziatura e struttura definite in base.md.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Formattazione perfetta. Tutti gli elementi (titoli, elenchi, tabelle, spaziatura, punteggiatura) seguono le regole italiane. Virgolette `« »` usate correttamente. |
| 4 | Buono | Formattazione molto buona. 1–3 violazioni minori delle regole (es. una virgoletta dritta invece di caporale, uno spazio mancante dopo la punteggiatura). |
| 3 | Sufficiente | Formattazione complessivamente adeguata. 4–8 violazioni, inclusi errori di punteggiatura o spaziatura. Struttura del documento preservata. |
| 2 | Scarso | Formattazione insufficiente. 9–15 violazioni. Errori ricorrenti di punteggiatura, spaziatura o struttura. Tabelle o elenchi malformati. |
| 1 | Gravemente insufficiente | Formattazione gravemente carente. Oltre 15 violazioni. Struttura del documento compromessa. Uso sistematico di virgolette e trattini errati. |
| 0 | Nullo | La formattazione originale non e stata preservata ne adattata. Il testo e privo di struttura, titoli, o punteggiatura corretta. |

### Elementi controllati

- Uso di `« »` (caporali) come virgolette primarie
- Trattino medio `–` per intervalli, trattino lungo `—` per incisi
- Spaziatura corretta dopo punteggiatura
- Punto dopo abbreviazioni (dott., sig., ecc.)
- Sentence case nei titoli
- Struttura di elenchi e tabelle
- Assenza di doppie spaziature

---

## 5. Completezza — Peso: 10 %

Verifica che tutto il contenuto dell'originale sia stato tradotto, senza omissioni, tagli o salti ingiustificati.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Traduzione completa al 100 %. Tutte le frasi, i paragrafi, le note, le didascalie, le intestazioni e i contenuti delle tabelle sono tradotti. |
| 4 | Buono | Traduzione completa al 95–99 %. Fino a 3 elementi minori non tradotti (parole singole, frasi brevi, righe di tabella). |
| 3 | Sufficiente | Traduzione completa all'85–94 %. Fino a 10 elementi non tradotti, o 1 paragrafo/frase di media lunghezza saltato. |
| 2 | Scarso | Traduzione completa al 70–84 %. Interi paragrafi o sezioni non tradotti. Elementi strutturali (titoli, didascalie) saltati. |
| 1 | Gravemente insufficiente | Traduzione completa al 50–69 %. Meta del documento o piu non tradotta. Mancano sezioni significative. |
| 0 | Nullo | Meno del 50 % del contenuto e tradotto. Il documento e prevalentemente in lingua originale. |

### Esclusioni

- Elementi che per policy di progetto **non** devono essere tradotti (es. marchi registrati, nomi di comandi in interfacce non localizzate, indirizzi email, URL).
- Note come `[N.d.T.]` e annotazioni del traduttore chiaramente segnalate.
- Contenuti esplicitamente contrassegnati come da non tradurre nelle istruzioni di progetto.

---

## 6. Qualita dell'Inferenza / OCR — Peso: 5 %

Valuta la qualita del ripristino di testo proveniente da OCR o documenti danneggiati, e la capacita di inferire correttamente il testo originale da frammenti.

### Bande

| Voto | Criterio | Descrizione |
|------|----------|-------------|
| 5 | Eccellente | Tutti i ripristini OCR sono corretti e segnalati nel formato `[ripristinato: ...]`. Le inferenze sono accurate e contestualmente appropriate. |
| 4 | Buono | Almeno il 90 % dei ripristini e corretto. 1–2 errori minori di ripristino (es. parola simile ma non identica all'originale). Formato delle parentesi corretto. |
| 3 | Sufficiente | Almeno il 75 % dei ripristini e corretto. 3–5 errori, inclusi alcuni numeri o date recuperati in modo impreciso. Formato `[ripristinato: ...` non sempre coerente. |
| 2 | Scarso | Almeno il 50 % dei ripristini e corretto. Errori diffusi nel recupero del testo. Formato delle segnalazioni incoerente o assente. |
| 1 | Gravemente insufficiente | Meno del 50 % dei ripristini e corretto. Testo ricostruito in modo arbitrario o errato. Segnalazioni di ripristino assenti o sistematicamente errate. |
| 0 | Nullo | Nessun tentativo di ripristino. Il testo corrotto e lasciato cosi com'e, o il ripristino e completamente inventato senza base nell'originale. |

### Criteri specifici

- Correttezza del ripristino: il testo ricostruito deve corrispondere all'originale (o alla migliore ipotesi).
- Completezza della segnalazione: ogni ripristino deve essere marcato con `[ripristinato: ...]`.
- Coerenza del formato: stessa convenzione per tutto il documento.
- Gestione dei numeri: i numeri in formato russo devono essere riconvertiti nel formato italiano.
- Gestione delle date: le date in formato russo (GG.MM.AAAA) devono essere convertite in formato italiano (GG/MM/AAAA).

---

## Zero Tolerance — Errori Critici

I seguenti errori sono considerati **critici** e comportano le conseguenze indicate:

| Errore | Conseguenza |
|--------|-------------|
| Scambio punto/virgola nei decimali (es. `3.14` per `3,14`) | Dimensione 1: voto 0 |
| Formato data errato (es. formato americano MM/DD/AAAA) | Dimensione 1: voto 0 |
| Uso di `Tu` in contesto formale dove serve `Lei` (o viceversa) | Dimensione 3: voto 0 |
| Testo originale non tradotto per intere sezioni (oltre il 30 %) | Dimensione 5: voto 0 |
| Invenzione di contenuto senza corrispondenza nell'originale | Dimensione 3: voto 0 |

### Impatto sul giudizio globale

- Se **una qualsiasi** dimensione riceve voto 0, il punteggio globale **non puo superare 60 %** (giudizio: Non superato).
- Due o piu dimensioni a voto 0: giudizio **Critico** (< 50 %) indipendentemente dal calcolo.

---

## Tabella riepilogativa

| # | Dimensione | Peso | Zero tolerance | Bande |
|---|------------|------|----------------|-------|
| 1 | Accuratezza Numerica | 30 % | Si (decimale, data) | 0–5 |
| 2 | Coerenza Terminologica | 20 % | No | 0–5 |
| 3 | Fedelta Semantica | 25 % | Si (Lei/Tu, invenzione) | 0–5 |
| 4 | Conformita Formale | 10 % | No | 0–5 |
| 5 | Completezza | 10 % | Si (>30 % non tradotto) | 0–5 |
| 6 | Qualita Inferenza/OCR | 5 % | No | 0–5 |

---

## Esempi di calcolo

### Esempio 1: Traduzione superata

| Dimensione | Voto | Peso | Contributo |
|------------|------|------|------------|
| Accuratezza Numerica | 5 | 30 % | 30,00 % |
| Coerenza Terminologica | 4 | 20 % | 16,00 % |
| Fedelta Semantica | 5 | 25 % | 25,00 % |
| Conformita Formale | 4 | 10 % | 8,00 % |
| Completezza | 5 | 10 % | 10,00 % |
| Inferenza/OCR | 4 | 5 % | 4,00 % |
| **Globale** | | **100 %** | **93,00 %** |

Giudizio: **Superato** (>= 85 %)

### Esempio 2: Traduzione condizionata

| Dimensione | Voto | Peso | Contributo |
|------------|------|------|------------|
| Accuratezza Numerica | 3 | 30 % | 18,00 % |
| Coerenza Terminologica | 4 | 20 % | 16,00 % |
| Fedelta Semantica | 4 | 25 % | 20,00 % |
| Conformita Formale | 3 | 10 % | 6,00 % |
| Completezza | 4 | 10 % | 8,00 % |
| Inferenza/OCR | 3 | 5 % | 3,00 % |
| **Globale** | | **100 %** | **71,00 %** |

Giudizio: **Condizionato** (70–84 %)

### Esempio 3: Traduzione critica (zero tolerance)

| Dimensione | Voto | Peso | Contributo |
|------------|------|------|------------|
| Accuratezza Numerica | **0** | 30 % | 0,00 % |
| Coerenza Terminologica | 3 | 20 % | 12,00 % |
| Fedelta Semantica | 4 | 25 % | 20,00 % |
| Conformita Formale | 4 | 10 % | 8,00 % |
| Completezza | 4 | 10 % | 8,00 % |
| Inferenza/OCR | 3 | 5 % | 3,00 % |
| **Globale** | | **100 %** | **51,00 %** |

Giudizio: **Non superato** (< 85 % e dimensione 1 a 0 → max 60 %). La traduzione ha un errore zero-tolerance sui decimali, quindi il punteggio globale non puo superare il 60 %, anche se il calcolo da 51 %.

---

*Documento conforme al sistema di valutazione del progetto di localizzazione. Le soglie e i pesi possono essere rivisti per specifici tipi di documento con approvazione del responsabile di progetto.*
