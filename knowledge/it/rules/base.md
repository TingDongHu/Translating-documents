---
id: it/rules/base
type: rules
target_lang: it
name: Regole di Localizzazione Italiana — Base
description: Italian base translation rules
---

# Regole di Localizzazione Italiana — Base

Questo documento definisce le regole fondamentali per la localizzazione di contenuti in lingua italiana. Deve essere consultato per ogni traduzione dal russo (o da altre lingue) all'italiano.

---

## 1. Formato dei Numeri

### 1.1 Separatore decimale

- **Regola obbligatoria**: la virgola (`,`) è il separatore decimale.
- Il punto (`.`) **non** viene mai usato come separatore decimale.
- Esempi:
  - `3,14` (corretto) — ~~`3.14`~~ (errato, interpretato come 3 014)
  - `0,99` — ~~`0.99`~~
  - `100,5` — ~~`100.5`~~

### 1.2 Separatore delle migliaia

- **Regola obbligatoria**: il punto (`.`) separa le migliaia.
- Esempi:
  - `1.000` (mille)
  - `15.000` (quindicimila)
  - `2.500.000` (due milioni e mezzo)
  - `1.234.567,89`
- **Non usare** spazi, apostrofi o altri caratteri come separatore delle migliaia.
- Eccezione: negli anni (es. `2025`) e in codici numerici (CAP, partita IVA, numeri di telefono) non si inserisce il punto.

### 1.3 Numeri negativi

- Il segno meno `−` (o `-`) precede il numero, senza spazio:
  - `−5`, `−12,75`
  - `−1.500,00`
- Nelle parentesi: `(−5)`.

### 1.4 Percentuali

- Il simbolo `%` va dopo il numero, separato da uno spazio **non** divisibile:
  - `15 %` o preferibilmente `15%` (senza spazio — l'uso oscillante è accettato, ma **la norma tipografica italiana** preferisce lo spazio; per coerenza interna del progetto si adotta **con spazio**).
  - `10,5 %`
- Variazioni: `−5 %`, `+3 %`.
- Scorporo: `IVA al 22 %`.
- In tabelle con colonna dedicata, il simbolo `%` può essere omesso dall'intestazione.

### 1.5 Numeri ordinali

- Uso del grado maschile `°` e femminile `ª`:
  - `1°`, `2°`, `3°`, `4°` (primo, secondo, terzo, quarto)
  - `1ª` (prima)
- Preferire la forma estesa nei testi formali: `primo`, `seconda`, `terzo`.

### 1.6 Frazioni e numeri romani

- Le frazioni comuni si scrivono in cifre: `1/2`, `3/4`.
- I numeri romani si usano per: secoli (`XXI secolo`), re/papi (`Luigi XIV`), capitoli (`Capitolo IV`).

### 1.7 Arrotondamenti

- Negli ambiti finanziari e statistici, arrotondare a 2 decimali salvo diversa indicazione.
- Usare le regole di arrotondamento standard (5 → superiore).

---

## 2. Valuta

### 2.1 Simbolo della valuta

- Il simbolo dell'euro (`€`) va **dopo l'importo**, separato da uno spazio:
  - `100,00 €` (corretto)
  - ~~`100.00€`~~, ~~`€ 100,00`~~ (errati)
- Centesimi: sempre due cifre decimali negli importi ufficiali:
  - `25,50 €`, `0,99 €`, `1.200,00 €`
- Arrotondamento a 2 decimali per transazioni.

### 2.2 Codici ISO

- Per contesti internazionali o tabellari: `EUR`, `USD`, `GBP`, `RUB`, `CHF`, `JPY`.
- Il codice ISO precede l'importo, separato da spazio:
  - `EUR 100,00`, `USD 50,50`
- **Non** combinare simbolo e codice ISO nella stessa espressione.

### 2.3 Valute diverse dall'euro

- Convertire o riportare con codice ISO se non esiste simbolo comune.
- Per il rublo russo (RUB): usare `RUB` o `₽` con le stesse regole posizionali dell'euro.
- Dollaro statunitense: `$ 50,00` o `USD 50,00`. Il simbolo `$` può precedere l'importo (uso internazionale), ma nei testi italiani si preferisce il codice ISO dopo.

### 2.4 Centesimi e frazioni monetarie

- `centesimo` / `centesimi`: forma abbreviata `c.` (es. `50 c.`).
- Evitare frazioni diverse da 2 decimali negli importi.
- Scrittura estesa: `€ 100,50 (cento euro e cinquanta centesimi)`.

### 2.5 Formati tabellari

- Allineamento a destra per colonne di importi.
- Segno negativo tra parentesi o con prefisso `−`.
- Totale in **grassetto** o con linea di separazione.

---

## 3. Data e Ora

### 3.1 Formato data

- **Regola obbligatoria**: `GG/MM/AAAA` o `DD/MM/YYYY`.
  - `25/12/2025` (corretto)
  - ~~`12/25/2025`~~ (errato — formato americano)
- Separatore: barra `/`. In contesti formali il trattino `-` è accettabile: `25-12-2025`.
- Data estesa (preferita nei documenti formali): `25 dicembre 2025` (senza articolo, senza `di`).

### 3.2 Nomi dei mesi

- **Minuscolo obbligatorio** (i mesi in italiano non si maiuscolano):
  - `gennaio, febbraio, marzo, aprile, maggio, giugno, luglio, agosto, settembre, ottobre, novembre, dicembre`
- Forma estesa sempre preferita; abbreviazioni consentite solo in spazi ristretti:
  - `gen., feb., mar., apr., mag., giu., lug., ago., set., ott., nov., dic.`

### 3.3 Nomi dei giorni

- Minuscolo:
  - `lunedì, martedì, mercoledì, giovedì, venerdì, sabato, domenica`
- Accento su `lunedì` (í = ì nella grafia piana), `martedì`, `mercoledì`, `giovedì`, `venerdì`.

### 3.4 Formato ora

- **24 ore** obbligatorio. Formato `HH:MM`:
  - `14:30` (corretto)
  - ~~`2:30 PM`~~ (errato in italiano)
- Secondi: `HH:MM:SS` dove necessario.
- Separatore: due punti `:`.
- Mezzogiorno: `12:00`. Mezzanotte: `00:00`.

### 3.5 Data e ora combinati

- Separatore: `alle` o `ore`:
  - `25/12/2025 alle 14:30`
  - `25 dicembre 2025, ore 14:30`

### 3.6 Intervalli temporali

- Trattino medio o `–` senza spazi:
  - `10:00–12:30`, `15/05–20/05`
  - `dal 10 al 15 gennaio 2025`
- Per anni: `2020–2025` (trattino, non slash).

### 3.7 Fusi orari

- Specificare il fuso quando rilevante: `UTC+1`, `CET`, `CEST`.
- In documenti per pubblico italiano, l'ora locale italiana è sottintesa.

### 3.8 Stagioni e periodi

- `primavera 2025`, `estate 2025` (minuscolo).
- Decenni: `gli anni Novanta` o `gli anni '90` (apostrofo, non virgoletta singola aperta).

---

## 4. Indirizzi

### 4.1 Struttura dell'indirizzo italiano

Sequenza obbligatoria:
```
Via [nome via], [numero civico], [CAP] [Città] ([Provincia]), [Regione]
```

Esempio:
```
Via Roma, 12, 20121 Milano (MI), Lombardia
```

### 4.2 Elementi specifici

- **Via**: può essere `Via` / `Viale` / `Corso` / `Piazza` / `Largo` / `Borgo` etc. Maiuscolo iniziale se è parte del nome proprio della via.
- **Numero civico**: preceduto da virgola. Abbreviazione `n.` facoltativa: `Via Verdi, 15` o `Via Verdi, n. 15`.
  - Appartamenti: `presso`, `int.` (interno), `sc.` (scala).
- **CAP** (Codice Avviamento Postale): 5 cifre, preceduto da spazio. Obbligatorio.
- **Città**: iniziale maiuscola.
- **Provincia**: sigla di 2 lettere tra parentesi tonde. Obbligatoria (tranne per stati esteri).
- **Regione**: facoltativa, in documenti formali.

### 4.3 Indirizzi esteri

- Localizzare l'intestazione (es. `via`, `viale`) ma mantenere il nome della via originale.
- Adattare la struttura a quella italiana dove possibile.
- Esempi:
  - `ул. Тверская, 5, Москва, Россия` → `Via Tverskaya, 5, Mosca, Russia`
  - Mantenere il nome della via in traslitterazione, aggiungendo il tipo di via italiano.

### 4.4 CAP estero

- Non tradurre `CAP` in contesto estero; usare `codice postale` o lasciare il formato locale.
- Se noto, aggiungere il codice postale del paese estero.

### 4.5 Formati multi-riga

```
Via Garibaldi, 45
20122 Milano (MI)
Italia
```

### 4.6 Indicazioni di direzione

- `destra`, `sinistra`, `dritto`, `angolo`, `incrocio`, `semaforo`, `rotonda`.
- Primo piano, secondo piano: `1° piano`, `2° piano`.

---

## 5. Nomi Propri

### 5.1 Accenti nei nomi comuni e propri italiani

- Accento grave (`à`, `è`, `ì`, `ò`, `ù`) su vocali aperte:
  - Città, falò, tribù, caffè, cioè, può.
- Accento acuto (`é`, `ó`) su vocali chiuse:
  - Perché, né, sé, cioè, scoiattolo.
- `è` (voce del verbo essere, terza persona singolare — con accento grave).
- Nei nomi propri: accento significativo — `Rossi`, `Bianchi` (senza accento), ma `Morò`, `Cosè` se accentati.

### 5.2 Articoli con nomi propri

- Di norma, **nessun articolo** davanti a nomi propri di persona:
  - `Mario Rossi`, ~~`il Mario Rossi`~~.
- Articolo con cognomi femminili in contesti burocratici: `la Rossi`, `la Bianchi`.
- Articolo con personaggi storici: `il Petrarca`, `l'Ariosto`, `il Manzoni`.

### 5.3 Nomi russi / cirillici

- **Traslitterazione**: sistema ISO 9 (o scientifico) per la conversione.
- Conservare la radice riconoscibile.
- Tabella di traslitterazione comune cirillico → latino:

| Cirillico | Latino | Cirillico | Latino |
|-----------|--------|-----------|--------|
| А → **A** | | Р → **R** |
| Б → **B** | | С → **S** |
| В → **V** | | Т → **T** |
| Г → **G** | | У → **U** |
| Д → **D** | | Ф → **F** |
| Е → **E** / **Ye** (iniziale) | | Х → **Kh** / **Ch** |
| Ё → **Yo** / **E** | | Ц → **Ts** / **C** |
| Ж → **Zh** | | Ч → **Ch** |
| З → **Z** | | Ш → **Sh** |
| И → **I** | | Щ → **Shch** |
| Й → **Y** / **I** | | Ы → **Y** |
| К → **K** | | Ь → `'` (apostrofo) / omesso |
| Л → **L** | | Э → **E** |
| М → **M** | | Ю → **Yu** |
| Н → **N** | | Я → **Ya** |
| О → **O** | | П → **P** |

- Desinenze: `-ий` → `-ij` o `-y`; `-ый` → `-yj` o `-y` (secondo l'uso consolidato).
- Nomi noti in italiano: usare la forma italianizzata tradizionale (es. `Mosca` non ~~`Moskva`~~, `Dostoevskij` non ~~`Dostoevskiy`~~, `Ciajkovskij` non ~~`Tchaikovsky`~~).

### 5.4 Titoli e onorificenze

- `Dott.`, `Dott.ssa`, `Prof.`, `Prof.ssa`, `Avv.`, `Ing.`, `Rag.`, `Geom.`, `Sig.`, `Sig.ra`, `Sig.na`.
- Possono essere abbreviati ma **sempre con il punto**.
- Forma estesa preferita nei testi formali: `Dottor Rossi`, `Professor Bianchi`.

### 5.5 Forme societarie italiane

- `SRL` / `S.r.l.` (Società a Responsabilità Limitata)
- `SPA` / `S.p.A.` (Società per Azioni)
- `SAPA` / `S.a.p.A.`
- `SNC` / `S.n.c.`
- `SAS` / `S.a.s.`
- `Società Cooperativa` / `Soc. Coop.`
- `di` + cognome per ditte individuali: `Studio Commercialista Rossi`
- Inserire la forma abbreviata dopo il nome: `Mario Rossi S.r.l.` o `Mario Rossi Srl`.

### 5.6 Nomi di istituzioni

- Tradurre il nome descrittivo ma mantenere la sigla originale tra parentesi la prima volta:
  - `Ministero della Salute`, `Agenzia delle Entrate`
  - `Organizzazione delle Nazioni Unite (ONU)`
  - `Banca Centrale della Federazione Russa (CBR)`
- Per entità russe: traslitterare + traduzione:
  - `Ministero delle Finanze della Federazione Russa (Minfin)`

### 5.7 Nomi geografici

- Forma italiana consolidata per capitali e stati:
  - `Mosca`, `San Pietroburgo`, `Roma`, `Parigi`, `Londra`, `Berlino`, `Vienna`, `Atene`, `Madrid`.
  - `Russia`, `Italia`, `Stati Uniti`, `Regno Unito`, `Germania`, `Francia`.
- Regioni italiane: sempre in italiano. Province: sigla di 2 lettere maiuscole.
- Fiumi, monti, laghi: tradurre se esiste forma italiana consolidata: `Volga`, `Danubio`, `Alpi`, `Appennini`.

### 5.8 Nomi di marche e prodotti

- **Non tradurre** nomi di marchi registrati, prodotti commerciali, titoli di opere (salvo diversa indicazione).
- Articolo determinativo davanti a marchi stranieri secondo il genere italiano: `la Apple`, `il Microsoft Word`, `la Ferrari`.
- Mantenere la grafia originale del marchio (maiuscole, minuscole, spazi).

### 5.9 Nomi di persona con particelle

- `de`, `della`, `di`, `del`, `degli`, `De`, `Del`, `Van`, `von`, `van der`: rispettare l'uso del portatore.
- `Leonardo da Vinci`, `Ludovico Ariosto`, `Van Gogh`, `von Goethe`.

---

## 6. Punteggiatura

### 6.1 Virgolette

- **Caporali** `« »`: le virgolette primarie in italiano.
  - Usate per discorsi diretti, citazioni, titoli di articoli.
  - Spazio prima di `«` e dopo `»` **solo** se seguono/precedono una parola.
  - `«Questo è un discorso diretto», disse.`
- **Verghette** `“ ”` (virgolette alte doppie): virgolette di secondo livello (citazioni dentro citazioni).
  - `«Mi disse: “Verrò domani” e se ne andò.»`
- **Virgolette singole** `‘ ’`: terzo livello, o per significati particolari.
- **Apice diritto** `'`: solo come apostrofo, non come virgoletta.

### 6.2 Trattini

- **Trattino breve** `-` (hyphen): parole composte, divisione in sillabe.
  - `auto-aggiornante`, `nord-est`, `taglia-cuce`, `portoghese-brasiliano`
- **Trattino medio** `–` (en-dash): intervalli, opposizioni, estensione.
  - `2010–2025`, `Roma–Milano`, `10:00–12:00`
  - **Senza spazi** attorno.
- **Trattino lungo** `—` (em-dash o lineetta): incisi — come questo.
  - Con spazi attorno (uso italiano) o senza (uso inglese). **Preferire con spazi** in italiano.
  - `Il risultato — sorprendente — ha stupito tutti.`

### 6.3 Spazio dopo la punteggiatura

- **Regola**: uno spazio dopo ogni segno di punteggiatura (`.` , `?` , `!` , `:` , `;` , `,`).
- **Nessuno spazio prima** dei segenti punti: `. , ? ! : ;`.
- Dopo l'apertura di parentesi o virgolette: nessuno spazio.
- Prima della chiusura di parentesi o virgolette: nessuno spazio.

### 6.4 Punto dopo le abbreviazioni

- Le abbreviazioni **richiedono il punto**:
  - `dott.`, `dott.ssa`, `avv.`, `ing.`, `sig.`, `sig.ra`, `ecc.`, `etc.`
  - `es.` (esempio), `cioè`, `n.` (numero), `p.` (pagina), `pp.` (pagine), `vol.`, `voll.`
  - `S.p.A.`, `S.r.l.`
- `ecc.` (eccetera) — con punto — a fine elenco.
- Evitare il punto in: acronimi (`ONU`, `CEE`, `IVA`), sigle di province (`MI`, `RM`), e codici ISO (`EUR`).

### 6.5 Puntini di sospensione

- Sempre tre punti `...` (o `…`, carattere unico).
- In italiano: preceduti e seguiti da spazio? L'uso oscillante è accettato; per coerenza: ` ... ` (con spazio prima e dopo).
- `Vorrei dire ... ma non so.`
- Non usare più di tre punti.

### 6.6 Punto e virgola

- Separa elementi di un elenco complesso, o proposizioni coordinate lunghe.
- **Non** sostituisce il punto fermo.
- Preferibile usarlo quando gli elementi contengono già virgole al loro interno.

### 6.7 Due punti

- Introducono elenchi, spiegazioni, discorsi diretti.
- Maiuscola dopo i due punti solo se introducono un discorso diretto o una citazione:
  - `Disse: «Arrivo subito.»`
  - `Ecco cosa serve: carta, penna e righello.`

### 6.8 Punto fermo

- Chiude frasi e paragrafi.
- Nessuna doppia spaziatura dopo il punto.
- Nei titoli e intestazioni: il punto finale è **omesso** (salvo se il titolo è una frase completa in corpo testo).

### 6.9 Punto interrogativo ed esclamativo

- Possono combinarsi solo in contesti informali: `?!` o `!?` (preferire `?!` in italiano).
- **Mai** raddoppiati (~~`??`~~, ~~`!!`~~).
- In italiano non esiste il punto interrogativo rovesciato (~~`¿`~~).

---

## 7. Formattazione

### 7.1 Maiuscole e minuscole nei titoli

- **Regola**: solo la prima parola e i nomi propri prendono la maiuscola nei titoli (sentence case).
  - `Guida all'uso del prodotto` (non ~~`Guida All'Uso Del Prodotto`~~)
  - `Manuale di installazione e manutenzione`
  - `Norme tecniche per l'edilizia`
- Eccezioni: titoli di opere d'arte, libri, film, leggi, decreti possono seguire convenzioni specifiche:
  - `La Divina Commedia` (nome proprio dell'opera)
  - `Il Nome della Rosa` (title case per opere)
  - `Decreto Legislativo 81/2008`

### 7.2 Elenchi puntati e numerati

- **Elenco puntato**: ogni punto inizia con minuscola, termina con punto e virgola (tranne l'ultimo che termina con punto).
  - Se ogni punto è una frase completa, iniziale maiuscola e punto fermo.
- **Elenco numerato**: stessa logica.
- Introdurre sempre l'elenco con i due punti.
- Coerenza di punteggiatura all'interno dello stesso elenco.

### 7.3 Tabelle

- Intestazioni: iniziale maiuscola, **sentence case**.
- Allineamento: testo a sinistra, numeri a destra.
- Unità di misura nel titolo tra parentesi o dopo slash:
  | Altezza (m) | Peso (kg) |
  | Prezzo € |
- Separatore di riga: trattini.
- Non usare righe verticali se non necessario.
- Cella vuota: trattino medio `–`.

### 7.4 Grassetto e corsivo

- **Grassetto**: per titoli, etichette, termini chiave, avvertenze.
- *Corsivo*: per parole straniere non assimilate (`software`, ma in corsivo se evidenziato), titoli di opere, enfasi leggera.
- Non abusare del grassetto: massimo 1-2 parole per paragrafo.
- In italiano, il corsivo si usa anche per i termini tecnici la prima volta che compaiono, seguiti dalla definizione.

### 7.5 Sottolineatura e MAIUSCOLO

- **Sottolineatura**: evitare; usare grassetto o corsivo.
- **MAIUSCOLO**: solo per acronimi (ONU, IVA, CERN). Non usare per enfasi (equivale a gridare).
- MAIUSCOLETTO: accettabile per nomi di autori in bibliografie.

### 7.6 Spaziature

- Rientro paragrafo: nessuno (stile blocco moderno) o 1,27 cm (stile tradizionale).
- Interlinea: 1,15 o 1,5 per documenti formali.
- Spazio tra paragrafi: 6-12 pt.
- **Nessuna doppia spaziatura** dopo il punto.

### 7.7 Elenchi complessi (nidificati)

- Struttura:
  1. Primo livello (numeri arabi con punto)
     - Secondo livello (trattino)
       - Terzo livello (trattino lungo)
- Allineare il testo indentato con il primo carattere del testo dell'elemento superiore.

---

## 8. Grammatica

### 8.1 Ordine delle parole (SVO)

- L'italiano è una lingua **SVO** (Soggetto-Verbo-Oggetto), ma l'ordine può variare per enfasi:
  - `Mario mangia la mela.` (SVO)
  - `La mela, la mangia Mario.` (OSV, enfasi sull'oggetto)
- Nelle traduzioni dal russo: **non** ricalcare la struttura russa (SOV frequente). Ristrutturare in SVO italiano.
- Non separare il verbo dal suo complemento oggetto con incisi lunghi.

### 8.2 Genere e numero (articoli determinativi)

| Maschile sing. | Femminile sing. | Maschile pl. | Femminile pl. |
|----------------|-----------------|--------------|---------------|
| `il` (consonante) | `la` (consonante) | `i` | `le` |
| `lo` (s+cons., gn, ps, x, z, y) | `l'` (vocale) | `gli` | `le` |
| `l'` (vocale) | | | |

- `lo studente, lo gnomo, lo psicologo, lo xilofono, lo zaino, lo yogurt`
- `gli` + vocale: `gli amici`, `gli uomini`
- `il` + vocale: ~~`il amico`~~ → `l'amico`

### 8.3 Articoli indeterminativi

- `un` (maschile, davanti a consonante e vocale): `un libro`, `un amico`
- `uno` (maschile, davanti a s+cons., gn, ps, x, z): `uno studente`, `uno zaino`
- `una` (femminile, davanti a consonante): `una casa`
- `un'` (femminile, davanti a vocale): `un'amica`

### 8.4 Preposizioni articolate

- `di + il = del`, `di + lo = dello`, `di + l' = dell'`, `di + i = dei`, `di + gli = degli`, `di + le = delle`
- `a + il = al`, `a + lo = allo`, `a + l' = all'`, `a + i = ai`, `a + gli = agli`, `a + le = alle`
- `da + il = dal`, `da + lo = dallo`, `da + l' = dall'`, `da + i = dai`, `da + gli = dagli`, `da + le = dalle`
- `in + il = nel`, `in + lo = nello`, `in + l' = nell'`, `in + i = nei`, `in + gli = negli`, `in + le = nelle`
- `su + il = sul`, `su + lo = sullo`, `su + l' = sull'`, `su + i = sui`, `su + gli = sugli`, `su + le = sulle`
- `con + il = col` (arcaico, preferire `con il` in italiano moderno)

### 8.5 Coniugazione verbale

- **Tre coniugazioni**: `-are`, `-ere`, `-ire`.
- **Presente indicativo**: regolare (parl-are → parlo, parli, parla, parliamo, parlate, parlano).
- **Passato prossimo** vs **passato remoto**:
  - **Passato prossimo** (avere/essere + participio passato): azioni recenti, con rilevanza nel presente.
    - `Ho parlato con lui ieri.`
    - `Sono andato a Roma.` (con `essere` per verbi di moto e riflessivi)
  - **Passato remoto**: azioni concluse nel passato lontano, senza legame con il presente. Usato nella narrativa e nella storia.
    - `Dante scrisse la Divina Commedia.`
    - `Nel 1492 Colombo scoprì l'America.`
  - **Attenzione**: nel Nord Italia il passato prossimo sostituisce spesso il remoto. Nel Sud Italia il remoto è più usato anche per azioni recenti. Per un italiano standard, seguire la norma: remoto per eventi storici e narrativi lontani, prossimo per il passato recente o con effetti presenti.

### 8.6 Congiuntivo (modo)

- Usato in subordinate che esprimono dubbio, opinione, possibilità, desiderio, emozione:
  - `Penso che **sia** giusto.`
  - `Benché **fosse** tardi, rimase.`
  - `Se **avessi** tempo, verrei.`
- Tempi: presente, imperfetto, passato, trapassato.
- **Attenzione**: il congiuntivo è obbligatorio dopo verbi di opinione (`credere`, `pensare`, `ritenere`), verbi impersonali (`è necessario che`, `è importante che`), congiunzioni (`benché`, `sebbene`, `affinché`, `purché`).
- **Evitare** l'uso scorretto dell'indicativo dove serve il congiuntivo (errore comune nel parlato informale, ma inaccettabile nel testo formale).

### 8.7 Condizionale

- Presente: `direi`, `vorrei`, `potrei`.
- Passato: `avrei detto`, `sarei andato`.
- Usato per: cortesia (`Vorrei un caffè`), condizione (`Se potessi, verrei`), futuro nel passato (`Disse che sarebbe venuto`).

### 8.8 Concordanza dei tempi

| Principale | Subordinata (contemporaneità) | Subordinata (anteriorità) |
|------------|-------------------------------|---------------------------|
| Presente | Congiuntivo presente | Congiuntivo passato |
| Passato prossimo | Congiuntivo imperfetto | Congiuntivo trapassato |
| Passato remoto | Congiuntivo imperfetto | Congiuntivo trapassato |
| Futuro | Indicativo presente | Congiuntivo passato |

### 8.9 Pronomi

- **Diretti**: `mi`, `ti`, `lo/la`, `ci`, `vi`, `li/le`.
- **Indiretti**: `mi`, `ti`, `gli/le`, `ci`, `vi`, `loro`.
- **Combinati** (doppi): `me lo`, `te lo`, `glielo`, `gliela`, `glieli`, `gliele`.
  - ~~`gli lo`~~ → `glielo`
- **Particella `ne`**: sostituisce `di` + qualcosa. `Ne parliamo.` (parliamo di ciò).
- Posizione: prima del verbo (tranne imperativo e infinito): `Lo vedo.`, `Dimmelo.`, `Per vederlo.`

### 8.10 Concordanza participio passato

- Con `avere`: invariato (salvo pronomi diretti): `Ho visto Maria.` / `L'ho **vista**.`
- Con `essere`: concorda con il soggetto: `Sono **andato**` (M), `Sono **andata**` (F), `Sono **andati**` (M pl), `Sono **andate**` (F pl).

### 8.11 Forma passiva

- Costruzione: `essere` + participio passato (+ `da` agente):
  - `Il libro è stato letto da Maria.`
- Alternativa con `si` passivante: `Si vendono libri.` (= libri sono venduti).

---

## 9. Formalità

### 9.1 Lei vs Tu

- **Lei** (terza persona singolare femminile, ma per persone di qualsiasi genere):
  - Uso formale: sconosciuti, superiori, clienti, autorità, corrispondenza ufficiale.
  - Verbo alla 3ª persona singolare.
  - `Lei ha ricevuto la mia email?`
  - `Posso offrirLe qualcosa?` (maiuscola enclitica di cortesia)
- **Tu** (seconda persona singolare):
  - Uso informale: amici, familiari, colleghi di pari livello, bambini.
  - Verbo alla 2ª persona singolare.
- **Loro** (arcaico, forma di cortesia plurale): usato solo in contesti molto formali o storici.
  - Oggi sostituito da `Voi` (plurale informale) o `Loro` (plurale formale, ma raro).
  - Nell'italiano contemporaneo, `Lei` vale anche per il plurale formale, o si usa `Voi` come cortese.

### 9.2 Maiuscola di cortesia

- **Regola**: nei pronomi e aggettivi possessivi riferiti alla persona cui ci si rivolge con `Lei`, si usa la maiuscola:
  - `La` (oggetto diretto): `La ringrazio.`
  - `Le` (oggetto indiretto): `Le scrivo.`
  - `Suo/Sua/Suoi/Sue`: `La Sua richiesta.`
  - `Ella` (raro, molto formale).
- Oggi la maiuscola di cortesia tende a scomparire nella corrispondenza elettronica; conservarla in documenti ufficiali e cartacei.

### 9.3 Formule di apertura (corrispondenza formale)

- A una persona:
  - `Egregio Signore / Egregio Sig.` (molto formale, tipicamente per uomo)
  - `Gentile Signora / Gentile Sig.ra` (per donna)
  - `Gentile Dottore / Gentile Dott.ssa` (con titolo)
  - `Spettabile` (per aziende: `Spett.le`)
  - `Alla cortese attenzione di` (nei documenti)
- Al plurale:
  - `Egregi Signori`, `Gentili Signore e Signori`
- Meno formali:
  - `Caro`, `Cara`, `Cari`, `Care` (con nome di battesimo)

### 9.4 Formule di chiusura

- `Distinti saluti.` (standard)
- `Cordiali saluti.` (leggermente meno formale)
- `Con osservanza.` (molto formale, burocratico)
- `In fede.` / `Fede.` (formale)
- `RingraziandoLa anticipatamente, porgo cordiali saluti.` (molto formale)
- `A disposizione per chiarimenti.` (semi-formale, commerciale)
- `Resto a disposizione per eventuali chiarimenti.`
- `Cordiali saluti.` + nome

### 9.5 Titoli nella corrispondenza

- `Dott.` / `Dott.ssa`: per laureati (uso esteso).
- `Prof.` / `Prof.ssa`: per docenti universitari e di scuola.
- `Avv.`: per avvocati.
- `Ing.`: per ingegneri.
- `Rag.`: per ragionieri.
- `Geom.`: per geometri.
- `Sig.` / `Sig.ra`: trattamento generico di cortesia.
- Usare il titolo sia nell'intestazione che nella formula di apertura.

### 9.6 Espressioni di cortesia

- `Per favore`, `per cortesia`, `gentilmente`.
- `La prego di ...`
- `Le sarei grato se ...`
- `Voglia scusare ...`
- `La ringrazio per ...`
- `Mi scusi per il disturbo.`

### 9.7 Registro linguistico per tipo di documento

| Tipo documento | Registro | Formula apertura | Formula chiusura |
|----------------|----------|------------------|------------------|
| Contratto | Molto formale | — | — |
| Lettera commerciale | Formale | Gentile / Spett.le | Distinti saluti |
| Comunicazione interna | Semi-formale | Caro/Cara | Cordiali saluti |
 | Email a cliente | Formale | Gentile / Egregio | Cordiali saluti |
| Manuale utente | Neutro | — | — |
| Pubblicità | Informale/diretta | Tu | — |
| Documento tecnico | Formale/neutro | — | — |
| Social media | Informale | Tu | — |
| Documento legale | Molto formale | Egregio | Con osservanza |

---

## 10. Manufatti OCR

### 10.1 Formato standard per ripristini

Quando l'OCR produce testo corrotto, ricostruito o incerto, il ripristino va segnalato con la seguente convenzione:

```
[ripristinato: testo corretto originale]
```

- Le parentesi quadre sono **obbligatorie**.
- La parola `ripristinato` è in **minuscolo**, in italiano, senza accento.
- Dopo i due punti, uno spazio, poi il testo **così come è stato ricostruito**.
- Il testo ripristinato può essere una parola, un numero, o un'intera frase.

### 10.2 Casi d'uso

- Caratteri illeggibili: `[ripristinato: 100,00 €]`
- Parole danneggiate: `Il [ripristinato: pagamento] è stato effettuato.`
- Numeri incerti: `l'importo di [ripristinato: 1.500,75] euro`
- Date dubbie: `in data [ripristinato: 15/03/2024]`
- Nomi propri: `Il Sig. [ripristinato: Mario Rossi]`
- Sigle: `[ripristinato: S.p.A.]`

### 10.3 Testo con più interpretazioni

Se l'OCR è ambiguo e ci sono più ipotesi di ripristino:

```
[ripristinato: ipotesi preferita|ipotesi alternativa]
```

Usare la barra verticale `|` per separare le alternative. La prima è la preferita.

### 10.4 Integrità della frase

- Il testo ripristinato deve essere integrato nella frase in modo che la lettura sia fluida.
- Non spezzare parole a metà del ripristino.
- Se l'intera frase è danneggiata, segnalare l'intera frase, non singole parole.

### 10.5 Mancata ricostruzione

Se il testo originale non è ricostruibile con certezza:

```
[ripristinato: illeggibile]
```

In casi di dubbio sulla correttezza del ripristino già effettuato, aggiungere un commento a margine (non nel testo tradotto) per il revisore.

### 10.6 Casi particolari

- **Numeri in formato russo**: se l'OCR produce un numero in formato russo (virgola come separatore migliaia, punto come decimale), il ripristino deve convertire nel formato italiano:
  - OCR errato: `1.500,75` (in russo = 1,50075) → ripristino: `[ripristinato: 1.500,75]` (italiano: millecinquecento virgola 75)
  - OCR errato: `5,200.50` (in russo = 5.200,50) → ripristino: `[ripristinato: 5.200,50]`
- **Date**: OCR russo `05.12.2024` → `[ripristinato: 05/12/2024]` (se è il 5 dicembre, non il 12 maggio).

### 10.7 Numeri di telefono e codici

- Non applicare formattazione automatica ai numeri di telefono.
- Se l'OCR li danneggia, ripristinare nel formato originale senza spaziature forzate:
  - `[ripristinato: +7 495 123-45-67]`

### 10.8 Tabella riepilogativa

| Situazione | OCR originale | Output atteso |
|---|---|---|
| Parola danneggiata | pa**amento | pagamento |
| Numero incerto | 1.5OO,75 | 1.500,75 |
| Data illeggibile | ##/03/2024 | 15/03/2024 |
| Nome corrotto | Ma***o Rossi | Mario Rossi |
| Formato russo data | 05.12.2024 | 05/12/2024 |
| Importo danneggiato | 1OO,€€ | 100,00 € |
| Illeggibile completo | ████████ | illeggibile |

---

## 11. Filosofia della Traduzione

### 11.1 Principio generale: italiano naturale

- La traduzione **deve suonare come scritta originariamente in italiano** da un madrelingua.
- **Non** ricalcare la sintassi della lingua di partenza.
- Leggere la traduzione ad alta voce mentalmente: se non "suona" naturale, va riformulata.
- Obiettivo: un lettore italiano **non** deve percepire che si tratta di una traduzione.

### 11.2 Registro e contesto

- Identificare il tipo di testo (tecnico, commerciale, legale, narrativo, pubblicitario) prima di tradurre.
- Mantenere coerenza di registro per tutto il documento.
- Non mescolare registri (es. forma colloquiale in un contratto).
- Adattare il livello di formalità al pubblico target.

### 11.3 Lunghezza delle frasi

- Le frasi russe tendono a essere più lunghe e complesse. **Spezzarle** in frasi italiane più brevi.
- Una frase italiana non dovrebbe superare le 25-30 parole in testi tecnici, 35-40 in testi narrativi.
- Riorganizzare i periodi: una frase = un'idea principale.

### 11.4 Falsi amici e interferenze

- Attenzione ai falsi amici russo-italiano:
  - `магазин` (magazin) = negozio, ~~non~~ rivista
  - `фабрика` (fabrika) = fabbrica, non fabrica
  - `президент` (prezident) = presidente
- Evitare calchi sintattici dal russo:
  - ~~`Il libro di cui sto parlando...`~~ → `Il libro di cui parlo...` (preferire forme più concise)
  - ~~`Lui ha detto che...`~~ → `Ha detto che...` (soggetto sottinteso)
- Non tradurre letteralmente: rendere il significato.

### 11.5 Regionalismi e varietà dell'italiano

- **Italiano standard**: basato sulla varietà fiorentina con influenze settentrionali e meridionali.
- **Evitare** regionalismi marcati:
  - Settentrionali: ~~`essere dietro a fare`~~ → `stare facendo`
  - Toscani: ~~`babbo`~~ → `papà` (salvo contesto specifico)
  - Romaneschi: ~~`annamo`~~ → `andiamo`
  - Meridionali: ~~`tenere`~~ (per `avere`) in contesti formali
- Usare regionalismi **solo** se il contesto del documento lo richiede (es. dialoghi, narrativa ambientata in una regione specifica).
- In documenti tecnici e commerciali: italiano standard **sempre**.

### 11.6 Terminologia tecnica

- Preferire il termine tecnico italiano consolidato quando esiste.
- Se il termine inglese/russo è più diffuso in Italia dell'equivalente italiano, usare quello:
  - `computer` (preferibile a `elaboratore`)
  - `mouse` (non ~~`topo`~~)
  - `file` (non ~~`archivio informatico`~~)
- Mantenere un glossario di progetto per garantire coerenza terminologica.
- Alla prima occorrenza di un termine tecnico, fornire una breve spiegazione se necessario.

### 11.7 Nomi di funzioni e comandi

- Tradurre le etichette di pulsanti e comandi **visibili nell'interfaccia utente** se localizzata.
- Se l'interfaccia è in inglese, tenere i nomi in inglese e tradurre solo la descrizione.
- Per comuni funzioni di sistema: `Salva`, `Apri`, `Stampa`, `Chiudi`, `Annulla`, `OK`, `Applica`.
- **Maiuscola**: solo la prima parola nelle etichette brevi (`Salva con nome`).

### 11.8 Adattamento culturale

- Adattare riferimenti culturali, unità di misura, esempi.
- Convertire le misure russe (piedi, verste, libbre) in metrico dove appropriato:
  - 1 pud ≈ 16,38 kg
  - 1 versta ≈ 1,067 km
  - 1 aršin ≈ 71,12 cm
- Sostituire esempi e metafore culturalmente specifiche:
  - `come una matrioška` → può rimanere se il riferimento è noto in Italia
  - `come il presepe` (sostituire metafore russe non note con equivalenti italiani)
- Adattare esempi di nomi e luoghi per il pubblico italiano.

### 11.9 Coerenza e leggibilità

- Una volta scelta una traduzione per un termine, usarla **sistematicamente** in tutto il documento.
- Usare sinonimi solo se funzionali alla varietà stilistica, non per semplice evitamento di ripetizioni.
- La coerenza prevale sull'eleganza formale.
- La lingua italiana tollera bene la ripetizione di termini tecnici — preferirla alla sinonimia confusa.

### 11.10 Gestione dell'ambiguità

- Se il testo originale è ambiguo, **non** riprodurre l'ambiguità nella traduzione.
- Scegliere l'interpretazione più probabile e tradurre in modo chiaro.
- Se l'ambiguità è intenzionale (es. testo letterario, gioco di parole), preservarla.
- Documentare i casi ambigui per il revisore.

### 11.11 Citazioni e riferimenti

- Tradurre le citazioni se la loro lunghezza lo giustifica; mantenere la citazione originale se si tratta di opera d'arte.
- Per testi normativi e legali: citare la versione italiana ufficiale se disponibile, altrimenti tradurre.
- Riferimenti a leggi italiane: indicare il numero e l'anno (`d.lgs. 81/2008`).
- Riferimenti a leggi russe: tradurre il nome mantenendo il riferimento al numero.

### 11.12 Note a piè di pagina e annotazioni

- Le note nella lingua originale vanno tradotte.
- Le note del traduttore vanno chiaramente segnalate come `[N.d.T.]`.
- Inserire `[N.d.T.]` solo quando strettamente necessario (per spiegare un gioco di parole, un riferimento culturale, o un'ambiguità irrisolvibile).

### 11.13 Revisione finale

- Ogni traduzione deve essere riletta in isolamento dal testo originale per verificarne la naturalezza.
- Verificare la coerenza terminologica con eventuali traduzioni precedenti dello stesso progetto.
- Controllare che non ci siano interferenze sintattiche dalla lingua di partenza.
- Verificare che i numeri, le date e gli importi siano correttamente formattati in italiano.
- Leggere ad alta voce i passaggi dubbi.

---

*Documento conforme alle principali convenzioni editoriali italiane. Per dubbi specifici non coperti, consultare il manuale di stabilità del progetto o il revisore linguistico.*
