---
id: nl/rules/base
type: rules
target_lang: nl
name: Dutch Language Rules for Translation
description: Dutch base translation rules
---

# Dutch Language Rules for Translation

This document defines the standard Dutch language rules that must be applied when translating or localizing content into Dutch (Nederlands). These rules cover formatting, grammar, punctuation, and stylistic conventions for the Nederlandse Taalunie standard variety of Dutch (Algemeen Nederlands).

---

## 1. Number Format

### 1.1 Decimal Separator

Dutch uses the **decimal comma** (komma), not the decimal point.

| Correct (NL) | Incorrect |
|---|---|
| 3,14 | 3.14 |
| 0,50 | 0.50 |
| 12,75 | 12.75 |
| 100,00 | 100.00 |

- Decimals are written with a comma: **3,14** (three point one four).
- No space before or after the decimal comma.
- For amounts less than one, a leading zero is used: **0,50** (not **,50**).

### 1.2 Thousands Separator

Dutch uses either a **period** (punt) or a **non-breaking space** (spatie) as the thousands separator. The period is more traditional; the space is increasingly common in modern usage.

| Method | Example |
|---|---|
| Period | 1.000 / 15.000 / 1.000.000 |
| Spaced | 1 000 / 15 000 / 1 000 000 |

- **Consistency is required**: pick one method per document and apply it throughout.
- Never use a comma as a thousands separator (that is English convention).
- For four-digit numbers, the separator may be omitted: **1000** or **1.000** both acceptable, as long as the document is consistent.
- ISO recommendation: use a thin space for thousands separation.

### 1.3 Negative Numbers

- Negative numbers are written with a minus sign (minteken): **−12** (U+2212, preferably) or a hyphen-minus: **-12**.
- The minus sign is placed directly before the number, no space: **−5,5**.
- In financial contexts, parentheses may also be used: **(125,00)**.

### 1.4 Percentages

- Written with a space between the number and the percent sign: **25 %**.
- In tables or compact contexts, the space may be omitted for alignment reasons, but standard prose requires the space: *De rente stijgt met 2,5 %*.

### 1.5 Ordinal Numbers

- Written with a period after the number: **1e** (sometimes **1ste**), **2e** (or **2de**), **3e** (or **3de**).
- The **e** form (1e, 2e, 3e) is preferred in modern Dutch; **1ste/2de/3de** is more formal.
- For higher ordinals: **10e**, **21e**, **100e**.

### 1.6 Fractions

- Written with a comma, not a point: **½** or **0,5**.
- Vulgar fractions (½, ⅓, ¼) are acceptable in informal contexts.

### 1.7 Numerals vs. Words

- Numbers up to **twenty** are typically written out in words in running text: *Er waren twaalf deelnemers.*
- Numbers above twenty may be written as digits: *Er waren 35 deelnemers.*
- Large round numbers are often written as a combination: *2,5 miljoen* (not *2.500.000* in running text).

---

## 2. Currency

### 2.1 Currency Symbol Placement

The currency symbol is placed **before** the amount, with a space:

| Currency | Format | Example |
|---|---|---|
| Euro | € + space + amount | € 100,00 |
| US Dollar | US$ + space + amount | US$ 50,00 |
| British Pound | £ + space + amount | £ 25,00 |

### 2.2 Decimal Format for Currency

- Always use **two decimal places** for currency amounts: **€ 100,00** (not € 100).
- Exception: whole amounts in tables or financial statements may omit decimals if all entries are whole numbers, but the document must be consistent.
- Use the decimal comma: € 100,00 (not € 100.00).

### 2.3 ISO Currency Codes

In international or technical contexts, ISO 4217 currency codes may be used:

| ISO Code | Currency | Example |
|---|---|---|
| EUR | Euro | EUR 100,00 |
| USD | US Dollar | USD 50,00 |
| GBP | British Pound | GBP 25,00 |
| CHF | Swiss Franc | CHF 30,00 |

- ISO code typically appears **before** the amount with a space.
- Style guides differ on code vs. symbol; within a single document, use one style consistently.
- When localizing from another currency to EUR, convert and recalculate if context requires.

### 2.4 Cent and Subunits

- Centen (cents) are written after the comma: **€ 0,50** (vijftig cent).
- The word *cent* is written in lowercase and separated: *50 cent*.
- For amounts less than one euro: *99 cent* (not *€ 0,99* when using the word *cent*).
- The abbreviation for cent is **ct**: *50 ct*.

### 2.5 Currency Names

- Euro (het euro) — plural: euro's (informally unchanged: *euro*).
- Dollar — *de dollar*, plural *dollars*.
- Pond — *het pond*, plural *ponden*.

---

## 3. Date and Time

### 3.1 Date Format

Dutch uses the **DD-MM-YYYY** format. Both periods and slashes are acceptable, but periods are more common.

| Format | Example |
|---|---|
| Periods (preferred) | 31 december 2024 |
| Numeric with periods | 31-12-2024 |
| Numeric with slashes | 31/12/2024 |

- **Day-month-year** order is mandatory. MM-DD-YYYY (American) or YYYY-MM-DD (ISO) are incorrect for Dutch prose.
- Leading zero for day and month is optional: **01-01-2024** or **1-1-2024**.
- In formal correspondence, month names are preferred over numeric dates: *31 december 2024*.

### 3.2 Month Names

Dutch month names are written in **lowercase** (not capitalized):

| Dutch | English |
|---|---|
| januari | January |
| februari | February |
| maart | March |
| april | April |
| mei | May |
| juni | June |
| juli | July |
| augustus | August |
| september | September |
| oktober | October |
| november | November |
| december | December |

- Abbreviations: jan., feb., mrt., apr., mei, jun., jul., aug., sep., okt., nov., dec.
- Note: *mei* and *juni/juli* have unusual abbreviation patterns (no dot for mei, no abbreviation for juni/juli in some style guides).

### 3.3 Day Names

Dutch day names are written in **lowercase**:

| Dutch | English |
|---|---|
| maandag | Monday |
| dinsdag | Tuesday |
| woensdag | Wednesday |
| donderdag | Thursday |
| vrijdag | Friday |
| zaterdag | Saturday |
| zondag | Sunday |

- Abbreviations: ma., di., wo., do., vr., za., zo.

### 3.4 Time Format

Dutch uses the **24-hour clock** almost exclusively.

| Format | Example |
|---|---|
| Full | 14:30 |
| With seconds | 14:30:15 |
| Informal/spoken | 2 uur 's middags |

- The separator is a **colon** (dubbele punt): **14:30** (not 14.30, though that is seen in older Flemish usage).
- Leading zero for hours is optional in the 24-hour format: **09:00** or **9:00**.
- **12-hour format** (AM/PM) is not used in Dutch except in very informal contexts or direct quotes from English sources.
- Time ranges: **14:00–16:30** (with an en dash or gedachtestreepje).
- Midnight: **00:00** (beginning of day) or **24:00** (end of day).

### 3.5 Combined Date and Time

- Order: date first, then time: *31 december 2024 om 14:30*.
- Preposition: **om** for time (om 14:30 uur), **op** for dates (op 31 december).
- *Uur* is optional after explicit times: *om 14:30* (not *om 14:30 uur*, though this is acceptable).

### 3.6 ISO 8601 (Technical Context)

In metadata or technical fields, ISO 8601 is acceptable: **2024-12-31T14:30:00**.
- This should only appear in machine-readable fields, not in prose text meant for human readers.

---

## 4. Addresses

### 4.1 Dutch Address Structure

The standard Dutch address format follows this order:

1. **Street name + house number** (straatnaam + huisnummer)
2. **Postal code** (postcode) — format: 4 digits + 2 uppercase letters, with a space
3. **City/locality** (plaats)
4. **Country** (land) — only required for international mail

**Example:**
```
Keizersgracht 123
1016 CJ Amsterdam
Nederland
```

### 4.2 House Number Conventions

- House number is placed **after** the street name: *Keizersgracht 123* (not *123 Keizersgracht*).
- Suffixes (toevoegingen) are written after the number, separated by a space: *Keizersgracht 123 A*, *Dorpsstraat 45-bis*.
- Common suffixes: -I, -II, -A, -B, -Z (Zuid), -N (Noord), -O (Oost), -W (West), *bis*, *ter*, *onder*, *boven*.

### 4.3 Postal Code Format

Dutch postal codes use the format: **1234 AB**
- Exactly 4 digits followed by a space and 2 uppercase letters.
- Letters may not be vowels (A, E, I, O, U) in the second position of the letter pair — though this is a historical rule and some newer codes may deviate.
- Special postal codes (PO boxes): **Postbus 1234, 1000 AB Amsterdam**.
- The postal code is written on the same line as the city, separated by a space: *1016 CJ Amsterdam*.

### 4.4 International Addresses

When translating documents that originate in other countries, adapt the address to the local convention unless preserving the original address as a proper noun:

- **Belgium (Flanders)**: follows similar format: *Sint-Katelijnevest 54, 2000 Antwerpen, Belgie*.
- **Suriname**: *Dr. J.C. de Miranda straat 12, Paramaribo, Suriname*.
- **Other countries**: keep the local format but add the country name in Dutch: *Verenigde Staten*, *Duitsland*, *Frankrijk*.

### 4.5 Country Names in Dutch

| English | Dutch |
|---|---|
| Netherlands | Nederland |
| Germany | Duitsland |
| France | Frankrijk |
| United Kingdom | Verenigd Koninkrijk |
| United States | Verenigde Staten |
| Belgium | Belgie |
| Switzerland | Zwitserland |
| Austria | Oostenrijk |

### 4.6 Address Line Wrapping

- Line 1: Street and number (and suffix if applicable)
- Line 2: Postcode + City
- Line 3: Country (if not obvious from context)
- In tables or constrained layouts: use comma notation: *Keizersgracht 123, 1016 CJ Amsterdam, Nederland*.

---

## 5. Proper Nouns

### 5.1 Dutch Diacritics

Dutch uses several diacritical marks. These must be preserved and correctly applied:

| Diacritic | Example | Usage |
|---|---|---|
| trema (diaeresis) | ideeen, financiele, geeindigd | Marks vowel separation in compound words |
| acute accent | beeindigen, cafe, logische | Stress mark, or in loanwords |
| grave accent | he, hè, bèta, caissière | Rare; marks specific pronunciation |
| circumflex | zône, enquête, maître | Mostly in loanwords from French |
| cedille | c, ça, garcon | Rare; mainly in French loanwords |

- The **trema** is the most important Dutch diacritic. It indicates that two adjacent vowels should be pronounced separately rather than as a digraph: *ideeën* (ideas), *geïnd* (indicated), *reünie* (reunion).
- The **acute accent** is used:
  - On **e** to indicate stress: *bééindigen*.
  - On loanwords: *café*, *logisch*.
  - To distinguish minimal pairs: *een* (a/an) vs. *één* (one).
- The **grave accent** is used on **è** in words like *hè* (eh?) and *bèta*; its use is declining.
- **Never strip diacritics** from Dutch text — doing so changes meaning or creates spelling errors.

### 5.2 Foreign Names and Loanwords

- Foreign names retain their original spelling and diacritics: *München*, *São Paulo*, *François*, *José*.
- Foreign place names that have a Dutch exonym should use the Dutch form: *Parijs* (not Paris), *Berlijn* (not Berlin), *Londen* (not London), *Rome* (not Roma).
- If no Dutch exonym exists, retain the original name.
- Company names and trademarks are never translated: *Microsoft*, *Apple*, *Siemens*.
- Loanwords that are fully adopted into Dutch follow Dutch spelling rules: *computer*, *manager*, *internet*. The Nederlandse Taalunie (Groene Boekje) is the authoritative source.

### 5.3 Dutch Company Forms

| Dutch | English equivalent | Example |
|---|---|---|
| BV (Besloten Vennootschap) | Private Limited Company | Jansen Beheer BV |
| NV (Naamloze Vennootschap) | Public Limited Company | Philips NV |
| CV (Commanditaire Vennootschap) | Limited Partnership | Janssen & Partners CV |
| VOF (Vennootschap onder Firma) | General Partnership | Bakker & Zn VOF |
| Stichting | Foundation | Stichting Lezen & Schrijven |
| Vereniging | Association | Vereniging Eigen Huis |

- The abbreviation follows the name, often preceded by a comma: *Philips NV* or *Philips, NV*.
- *BV* and *NV* are capitalized without periods.
- When translating foreign company forms, use the Dutch equivalent: *Ltd.* → *BV*; *Inc.* → *NV*; *GmbH* → *BV* (approximately — legal advice may be needed for formal documents).

### 5.4 Capitalization of Proper Nouns

- Personal names: capitalize the first name and surname: *Jan van der Waal*, *Mevrouw De Boer* (note: *tussenvoegsels* like *van*, *der*, *de* may be capitalized or not depending on context — see 5.5).
- Place names: capitalize: *Amsterdam*, *Den Haag*, *Rotterdam*.
- Street names: capitalize: *Keizersgracht*, *Leidsestraat*, *Dorpsstraat*.
- Organization names: capitalize: *Ministerie van Onderwijs*, *De Nederlandsche Bank*.
- Brand names: retain original capitalization: *Bol.com*, *Rabobank*, *KLM*.

### 5.5 Tussenvoegsels (Name Prefixes)

Dutch surnames often include tussenvoegsels (*van*, *der*, *de*, *den*, *ter*, *van der*, *van den*, etc.). Capitalization depends on **context**:

| Context | Example |
|---|---|
| First name + surname (lowercase) | Jan van der Waal |
| Surname alone at start of sentence (capitalize) | **Van der Waal** is gearriveerd |
| Surname alone in a list (capitalize) | Aanspreekpersoon: **Van der Waal** |
| Initials + surname (lowercase) | J. van der Waal |
| Without given name/initials, in running text | de heer **Van der Waal** (formal) or de heer **van der Waal** |

- There is regional variation (Dutch vs. Belgian conventions differ). The above represents standard Netherlands usage.

---

## 6. Punctuation

### 6.1 Quotation Marks

Dutch traditionally uses **lower quotation marks** at the start and **upper quotation marks** at the end:

| Style | Opening | Closing |
|---|---|---|
| Traditional Dutch (preferred) | **„** (U+201E) | **”** (U+201D) |
| Alternative | **"** (U+0022) | **"** (U+0022) |
| Single quotes | **‚** (U+201A) | **'** (U+2018) |

- **„...”** is the standard Dutch quotation style for narrative and direct speech.
- If the character set does not support guillemets or low-high quotes, straight double quotes **"..."** may be used as a fallback, but only if applied consistently.
- Single quotes („...' -> actually ‚...') are used for quotes within quotes.
- **Chevron quotes (guillemets)**: «...» are used in Flemish (Belgian Dutch) contexts and some formal publications. In Netherlands Dutch, they are less common but acceptable.

### 6.2 Comma Rules

- **No Oxford comma**: In Dutch, a serial comma is **not** placed before *en* (and) or *of* (or) in a list of three or more items.
  - Correct: *Ik kocht appels, peren en bananen.*
  - Incorrect: *Ik kocht appels, peren, en bananen.*
- **Required commas**:
  - Between clauses: *Ik kom, omdat ik je wil zien.*
  - Before *maar* (but): *Het is duur, maar wel goed.*
  - In lists of three or more: *rood, wit en blauw.* (no comma before *en*)
  - After introductory phrases: *Daarnaast, hebben we nog andere opties.*
  - Around non-restrictive clauses: *Mijn vader, die in Utrecht woont, komt morgen.*
- **No comma**:
  - Between subject and verb.
  - Before *dan* in comparisons: *Hij is groter dan ik.*
  - Before *als* in comparisons: *Ze is net zo oud als hij.*

### 6.3 Dash and Hyphen

| Symbol | Dutch Name | Usage |
|---|---|---|
| - (hyphen, verbindingsstreepje) | Koppelteken | Compound words: *auto-ongeluk*, *actie-reactie*; vowel collisions: *zee-egel* |
| – (en dash) | Aandachtsstreepje | Ranges: *2010–2020*, *10–15*; connections: *Amsterdam–Rotterdam* |
| — (em dash) | Gedachtestreepje | Parenthetical — like this — or interruptions |

- **Gedachtestreepje** (—, em dash): Used in pairs to set off parenthetical content, or alone to indicate an abrupt break. In Dutch, an em dash is often surrounded by spaces: *Hij zei — en dit is belangrijk — dat hij niet komt.*
- **Aandachtsstreepje** (–, en dash): Used for ranges and connections without spaces: *pagina 10–20*, *trein Amsterdam–Parijs*.
- **Koppelteken** (-, hyphen): Used in compound words and to avoid vowel collision: *auto-ongeluk* (not *autoongeluk*). Also used in numbers: *eenentwintig* (but *21-jarige* with hyphen).

### 6.4 Apostrophe

- Used for contractions: *'s ochtends*, *'s avonds*, *'s-Hertogenbosch*.
- Used for plurals of words ending in vowels: *auto's*, *oma's*, *foto's*.
- Used for genitive with proper nouns ending in vowels or certain consonants: *Anna's boek*, *Max' auto* (or *Max zijn auto* in informal usage).
- **Not used** for possessive pronouns: *zijn* (not *zijn'*), *haar* (not *haar'*).

### 6.5 Colon and Semicolon

- **Colon** (dubbele punt): Used to introduce a list, explanation, or quote. No capital letter after the colon unless the colon is followed by a full sentence or a proper noun: *Dit zijn de opties: snel, goedkoop of betrouwbaar.*
- **Semicolon** (puntkomma): Used to connect two related clauses without a conjunction: *Hij kwam te laat; de vergadering was al begonnen.* Less common in Dutch than in English.

### 6.6 Parentheses and Brackets

- Parentheses (ronde haken): Used for supplementary information. Standard usage.
- Square brackets (vierkante haken): Used for editorial insertions, corrections, or clarifications in quoted text. Also used for OCR artifacts (see Section 10).

### 6.7 Ellipsis

- Three dots (…, U+2026) or three periods with spaces: *Hij zei... niets.*
- In Dutch, the ellipsis may be surrounded by spaces or not, depending on context. Be consistent within a document.

### 6.8 Space Before Punctuation

- Dutch never places a space before a period, comma, colon, semicolon, question mark, or exclamation point.
- An exception is the **gedachtestreepje** (em dash) in some style guides: space before and after.

---

## 7. Formatting

### 7.1 Title Capitalization

Dutch uses **sentence case** for titles, headings, and captions — not title case.

| Correct (sentence case) | Incorrect (title case) |
|---|---|
| De geschiedenis van Amsterdam | De Geschiedenis van Amsterdam |
| Hoe u uw belastingaangifte doet | Hoe U Uw Belastingaangifte Doet |
| Een nieuw begin | Een Nieuw Begin |

- **Capitalize only**:
  - The first word of the title/heading.
  - Proper nouns and adjectives derived from proper nouns: *Amsterdamse grachten*, *Franse kaas*.
  - The first word after a colon if what follows is a complete sentence.
- **Do not capitalize**: articles (de, het, een), prepositions (in, op, van, met, door), conjunctions (en, of, maar, want), and other function words — unless they are the first word.
- This rule applies to: article titles, book titles, chapter headings, section headings, table captions, figure captions.

### 7.2 Lists (Opsommingen)

- **Unordered lists**: introduce with a colon, use bullet points (— or * or •).
- **Ordered lists**: use numbers (1., 2., 3.) or letters (a., b., c.).
- **Punctuation in lists**:
  - If list items are sentence fragments (not complete sentences): each item starts lowercase and ends with a semicolon (except the last, which ends with a period).
  - If list items are complete sentences: each item starts with a capital letter and ends with a period.
  - If list items are single words or short phrases: no period needed.
- **Parallel structure**: all items in a list must follow the same grammatical structure (all nouns, all imperative verbs, all complete sentences, etc.).
- Introduce a list with a colon. Do not use a colon after *zijn* or *zijn* equivalents (*Dit zijn: ...* is incorrect; use *Dit zijn de volgende punten:*).

### 7.3 Tables

- **Alignment**: text columns are left-aligned; number columns are right-aligned.
- **Column headers**: use sentence case (see 7.1).
- **Decimal alignment**: numbers should align on the decimal comma where practicable.
- **Currency columns**: align right, with the currency symbol on the first entry only, or on every row as needed.
- **Table captions**: placed above the table (unlike English, where they are often below).
- Use *Tabel 1* (capitals for *Tabel*) preceding the caption: *Tabel 1: Overzicht van resultaten*.

### 7.4 Bold and Italic

- **Bold** (vet): Used for headings, key terms at first mention, and emphasis in technical documents.
- *Italic* (cursief): Used for:
  - Foreign words (*comme ci, comme ca*).
  - Titles of books, films, artworks (*De aanslag*, *Turks fruit*).
  - Emphasis (sparingly).
  - Words being discussed as words: *Het woord *fiets* is een zelfstandig naamwoord.*
- Do not use bold or italic for entire paragraphs. Use them sparingly for maximum effect.

### 7.5 Abbreviations

- Common abbreviations use a period: *b.v.*, *d.m.v.*, *i.v.m.*, *t.a.v.*, *m.b.t.*, *o.a.*, *enz.*, *etc.*
- Some abbreviations omit the period in modern usage: *bv* (bijvoorbeeld), *nl* (namelijk). Follow the target publication's style guide.
- Latin abbreviations commonly used in Dutch: *etc.* (et cetera), *ca.* (circa), *e.g.* (exempli gratia — less common; use *bijv.* instead).
- Units of measurement: no period after the abbreviation: *kg*, *m*, *cm*, *km*, *l*, *ml*.
- In Dutch, *etc.* is often replaced with *enz.* (enzovoorts) — preferred in formal Dutch.

### 7.6 Numbers in Headings

- Numbers in headings follow the same rules as numbers in body text.
- Avoid starting a heading with a numeral if it can be written out.
- If a heading contains a numbered section reference, use the digit form: *Hoofdstuk 1: Inleiding*.

### 7.7 Footnotes and Endnotes

- Footnote markers are superscript numbers placed **after** the punctuation mark: *De inflatie steeg met 2,5 %.¹*
- Footnotes are numbered sequentially per chapter or per document.
- Footnote text ends with a period.

---

## 8. Grammar

### 8.1 Word Order (Woordvolgorde)

Dutch word order is SVO in main clauses but **SOV in subordinate clauses** (bijzinnen). This is a critical difference from English.

**Main clause (hoofdzin) — SVO:**
| Position 1 | Position 2 | Middle | End |
|---|---|---|---|
| Ik | heb | gisteren | een boek gekocht. |
| Gisteren | heb | ik een boek | gekocht. |

**Subordinate clause (bijzin) — SOV:**
| Conjunction | Subject | Objects | Verb(s) at end |
|---|---|---|---|
| ...omdat | ik | gisteren een boek | heb gekocht. |
| ...dat | hij | de brief | heeft geschreven. |

**Key rules:**
- The **finite verb** is always in **second position** in main clauses (V2 rule).
- In subordinate clauses, **all verbs go to the end**.
- When translating a complex English sentence, identify whether the Dutch clause is a hoofd- or bijzin and place verbs accordingly.

### 8.2 Separable Verbs (Scheidbare Werkwoorden)

Dutch has many separable verbs where the prefix separates from the stem in certain conjugations:

| Infinitive | Present (separated) | Past participle | Subordinate clause (together) |
|---|---|---|---|
| **op**bellen (to call) | Ik **bel** je morgen **op**. | Ik heb je **op**gebeld. | ...dat ik je **opbel**. |
| **uit**nodigen (to invite) | Zij **nodigt** hem **uit**. | Zij heeft hem **uit**genodigd. | ...dat zij hem **uitnodigt**. |
| **na**denken (to think) | Hij **denkt** erover **na**. | Hij heeft erover **na**gedacht. | ...dat hij erover **nadenkt**. |

- Common prefixes: aan-, af-, bij-, door-, in-, mee-, na-, op-, uit-, voor-, weg-.
- In main clauses, the prefix goes to the end: *Ik **maak** de deur **open**.*
- In subordinate clauses, the prefix stays attached to the verb: *...dat ik de deur **openmaak**.*
- In past participle, the ge- goes between prefix and stem: *open**ge**maakt*.

### 8.3 Gender (De/Het)

Dutch has two grammatical genders for nouns: **common gender** (de-woorden) and **neuter gender** (het-woorden). There is no reliable rule; gender must be memorized per noun.

| Article | Usage | Example |
|---|---|---|
| **de** | Masculine/feminine nouns (~75 % of nouns) | de man, de vrouw, de tafel, de auto |
| **het** | Neuter nouns (~25 % of nouns) | het huis, het boek, het kind, het water |
| **een** | Indefinite article (both genders) | een man, een huis |

**Tips for het-woorden:**
- Diminutives (ending in -je) are always **het**: *het huisje, het mannetje*.
- Infinitives used as nouns are **het**: *het lopen, het zwemmen*.
- Words ending in -isme, -ment, -sel are typically **het**: *het idealisme, het fundament, het schepsel*.
- Most words ending in -ing, -ie, -ij, -heid, -teit, -de, -te are **de**: *de regeling, de koffie, de maatschappij, de waarheid, de universiteit, de liefde, de hoogte*.
- Loanwords from English are overwhelmingly **de**: *de computer, de manager, de website, de laptop*.

**Demonstrative pronouns:**
- **De** words: *deze* (this/these), *die* (that/those).
- **Het** words: *dit* (this), *dat* (that).

**Relative pronouns:**
- **De** words: *die* (who/which).
- **Het** words: *dat* (which/that).
- *Waar + preposition* for things: *de stoel waarop ik zit*.

### 8.4 Verb Conjugation

**Present tense (tegenwoordige tijd):**

| Pronoun | werken (to work) | nemen (to take) | zijn (to be) |
|---|---|---|---|
| ik | werk | neem | ben |
| jij/je | werkt/werk jij? | neemt/neem jij? | bent/ben jij? |
| hij/zij/het | werkt | neemt | is |
| wij/we | werken | nemen | zijn |
| jullie | werken | nemen | zijn |
| zij/ze | werken | nemen | zijn |

- **Inversion rule**: When the subject follows the verb (jij after the verb in questions or inversion), the -t is dropped: *Werk **jij** morgen?* (not *Werkt jij*).
- **U form**: always takes -t: *U werkt, U neemt, U bent* (also *U heeft* / *U hebt* — both acceptable).

**Past tense (verleden tijd):**

| Type | Weak (regular) | Strong (irregular) |
|---|---|---|
| Singular | ik werkte | ik nam |
| Plural | wij werkten | wij namen |
| Past participle | **ge**werk**t** | **ge**nom**en** |

- Strong verb patterns: there are about 200 strong verbs in Dutch with vowel changes in past tense.
- The past participle of weak verbs ends in -t or -d (depending on the voicing of the last consonant — 't kofschip rule).

### 8.5 't Kofschip Rule

For regular (weak) verbs, the past tense suffix depends on the final consonant of the stem:

- If the stem ends in one of **t, k, f, s, ch, p** (remember: *'t kofschip*): past tense = **-te(n)**, participle = **-t**.
- Otherwise: past tense = **-de(n)**, participle = **-d**.

| Stem | Past tense | Past participle |
|---|---|---|
| werk- (k) | werkte | gewerkt |
| fiets- (t) | fietste | gefietst |
| bel- (l) | belde | gebeld |
| leef- (f) | leefde | geleefd |

- For verbs with stems ending in a voiced consonant: -de(n) / -d.
- For verbs with stems ending in an unvoiced consonant: -te(n) / -t.

### 8.6 Modal Verbs

| Infinitive | Present | Past |
|---|---|---|
| kunnen (can) | ik kan | ik kon |
| moeten (must) | ik moet | ik moest |
| mogen (may) | ik mag | ik mocht |
| willen (want) | ik wil | ik wilde/wou |
| zullen (shall) | ik zal | ik zou |
| weten (to know) | ik weet | ik wist |

- In main clauses, the modal verb is in position 2, and the main verb goes to the end: *Ik **kan** morgen niet **komen**.*
- In subordinate clauses, both verbs go to the end: *...omdat ik morgen niet **kan komen**.*
- With a perfect tense, the infinitive is often used instead of the past participle (the *vervangingsregel*): *Ik had kunnen komen* (not *gekund*).

### 8.7 Plural Formation

| Rule | Singular | Plural |
|---|---|---|
| Add **-en** | huis | huizen |
| Add **-s** | tafel | tafels |
| Add **-en** (vowel change) | stad | steden |
| Add **-eren** | kind | kinderen |
| Words ending in -ie | koffie | koffies (but: *kopie* → *kopieeen* or *kopies*) |

- The choice between -en and -s depends on the word's ending and stress pattern.
- Diminutives always add -s: *het huisje, de huisjes*.

### 8.8 Adjective Inflection

- **Attributive adjectives** (before a noun) almost always take **-e**:
  - *Een **groot** huis* (het-word, indefinite) — no -e.
  - *Het **grote** huis* (het-word, definite) — with -e.
  - *De **grote** auto* (de-word, any) — always with -e.
  - ***Grote** auto's* (plural, any) — always with -e.

- **Predicative adjectives** (after the verb *zijn*) never take -e:
  - *Het huis is **groot**.*
  - *De auto is **groot**.*

### 8.9 Prepositions

Dutch prepositions do not always map one-to-one to English prepositions:

| Dutch | Common usage | Example |
|---|---|---|
| in | in/inside | in het huis |
| op | on/at/for | op tafel, op school |
| aan | at/on/by | aan de muur, aan tafel |
| bij | at/near/by | bij de deur, bij mij |
| met | with | met de auto |
| van | of/from | van Amsterdam, de fiets van Jan |
| naar | to/towards | naar school, naar huis |
| voor | for/before | voor jou, voor de deur |
| achter | behind | achter het huis |
| door | through/by | door het raam, door mij |

- The preposition frequently changes meaning depending on context.
- Many Dutch prepositions combine with verbs to form idiomatic expressions that must be learned as units: *wachten **op*** (wait for), *denken **aan*** (think of), *houden **van*** (love/like), *zich verheugen **op*** (look forward to).

---

## 9. Formality

### 9.1 U vs. Jij/Je

Dutch has a T-V distinction (formal vs. informal address). Choosing correctly is essential for natural translation.

**Informal (jij/je):**
- Used with: friends, family, colleagues of equal rank, children, people of the same age group, informal settings.
- Verb: jij/je takes **-t**: *jij werkt, je hebt* (but inversion drops -t: *werk jij?*).
- Possessive: **jouw/je** (your).

**Formal (u):**
- Used with: strangers, elderly people, superiors, clients, official correspondence, professional emails, customer service.
- Verb: u always takes **-t**: *u werkt* (also *u heeft* and *u hebt* both correct).
- Possessive: **uw** (your).
- *U* is always capitalized in formal letters (*U*), though in running text some style guides write it lowercase.

### 9.2 Formal Correspondence

**Salutations (aanhef):**

| Context | Formal salutation |
|---|---|
| Dear Sir (name unknown) | Geachte heer, |
| Dear Madam (name unknown) | Geachte mevrouw, |
| Dear Mr. Jansen | Geachte heer Jansen, |
| Dear Ms. Jansen | Geachte mevrouw Jansen, |
| Dear Sir/Madam | Geachte heer/mevrouw, |
| Dear all (team) | Geacht team, / Beste allen, |

- *Geachte* is the most formal. *Beste* is semi-formal.
- After the salutation, a comma is standard (not a colon).
- The first word after the salutation begins with a **lowercase** letter (continuing the sentence): *Geachte heer Jansen, hierbij stuur ik u...*

**Closing (afsluiting):**

| Context | Formal closing |
|---|---|
| Very formal (official letters) | Hoogachtend, |
| Formal (business) | Met vriendelijke groet, |
| Semi-formal | Vriendelijke groet, / Met vriendelijke groeten, |
| Informal | Groetjes, / Hartelijke groet, / Doei, |

- *Hoogachtend* is used for official letters, legal correspondence, and applications.
- *Met vriendelijke groet* is the standard business closing (roughly "Sincerely" or "Best regards").
- Closings are followed by a comma, then a new line for the signature.

### 9.3 Pronoun Choice in Translation

When translating from a language without T-V distinction (e.g., English *you*):

| Context in source | Dutch translation |
|---|---|
| Marketing to consumers | **je/jij** (informal, approachable) |
| B2B communication | **u** (formal, professional) |
| Legal documents | **u** (always formal) |
| Software UI (consumer) | **je** (or avoid pronoun entirely) |
| Software UI (enterprise) | **u** |
| Instructions/manuals | Either; **u** is safer; imperative form avoids the issue |

- **Consistency**: do not switch between u and je/jij within the same document or system.
- When in doubt, default to **u** — overly formal is safer than overly familiar in professional contexts.

### 9.4 Passive Voice in Formal Dutch

Formal Dutch uses the passive voice more readily than modern English:

| English (active) | Dutch (formal) |
|---|---|
| We have decided... | Er is besloten... |
| You will find... | U treft... aan / Er wordt... |
| We attach... | Hierbij is gevoegd... / Als bijlage treft u aan... |

- In formal/correspondence contexts, the passive can help maintain distance and formality.
- In informal or marketing contexts, prefer active voice: *Wij hebben besloten...*.

### 9.5 Titles and Forms of Address

| Person | Formal address |
|---|---|
| Dr. | dr. / Doctor |
| Prof. | prof. / Professor |
| Mr. (law degree, NL) | mr. (meester in de rechten) |
| Ing. (engineering degree) | ing. |
| Drs. (multiple master's degrees) | drs. |

- These academic titles are used before the name: *dr. Jansen*, *prof. dr. De Vries*.
- In salutations, the title may be written out: *Geachte professor De Vries*.

### 9.6 Regional Formality Differences

- **Netherlands**: Generally more informal; *je/jij* is common even in many business contexts.
- **Flanders (Belgium)**: More formal; *u* is used more broadly and for longer into a relationship.
- **Suriname**: Closer to Netherlands conventions.
- When the target audience is unknown, default to Netherlands conventions.

---

## 10. OCR Artifacts

### 10.1 Handling OCR Uncertainty

When translating from scanned documents or OCR-generated text, artifacts must be handled carefully. The standard Dutch format for marking OCR corrections is:

**`[hersteld: ...]`**

This is a Dutch adaptation of the typical `[sic]` or `[corrected: ...]` annotation, used to indicate that the original source had an error or OCR defect that has been corrected in the translation.

### 10.2 OCR Artifact Categories

| Category | Example source artifact | In translation |
|---|---|---|
| Illegible character | "bedrag: 1.2S0" | bedrag: 1.250 [hersteld: S → 5] |
| Missing text | "totaal [ ]" | totaal [hersteld: bedrag ontbreekt in origineel] |
| Merged words | "dekosten" | de kosten [hersteld: aan elkaar in origineel] |
| Split words | "de kosten" | dekosten [hersteld: los in origineel] |
| Wrong character | "0% rente" | 0 % rente [hersteld: O → 0] |
| Reconstructed text | "[illegible]" | [hersteld: onleesbaar in origineel] |
| Page break artifact | "ver-volg" | vervolg [hersteld: afgebroken aan paginagrens] |
| Skewed/hallucinated number | "€ 1.0S0,00" | € 1.050,00 [hersteld: OCR-fout in cijfer] |

### 10.3 When to Use [hersteld]

- Use **only** when the original document's text is genuinely unclear, damaged, or corrupted by the scanning process.
- Do **not** use [hersteld] for ordinary spelling corrections or normalization — those are part of standard translation.
- Do **not** use [hersteld] for translation choices or disambiguation (use a translator's note for that, if needed).
- The annotation follows the corrected text, in square brackets.

### 10.4 Formatting Rules

- **`[hersteld: uitleg]`** — lowercase *h* in *hersteld* (not sentence-initial).
- The explanation inside the brackets should be concise and in Dutch.
- If the original text is completely illegible and cannot be reconstructed: **`[onleesbaar]`** (illegible) or **`[hersteld: onleesbaar in origineel]`**.
- If a reconstruction is uncertain: **`[hersteld: vermoedelijk ...]`** (presumably ...).
- For numbers where OCR may have introduced errors, apply numerical zero-tolerance checks (see also the scoring rubric).

### 10.5 Preserving Original Formatting

- When an OCR artifact involves formatting (e.g., a line break in the middle of a word), the formatting of the translation should follow target-language rules, not the source artifact.
- Only annotate the semantic content issue, not the formatting issue.
- Example: if the original scans "ver-\nvolgen" because of a line break, translate as "vervolgen" and note only if the OCR genuinely misread the word.

### 10.6 Multiple Artifacts

- If multiple corrections are needed in the same passage, apply them sequentially: *De uitslag was 25,50 [hersteld: komma toegevoegd] — 26,00 [hersteld: cijfer gecorrigeerd].*

### 10.7 Quality Threshold

- If more than 10 % of the text in a segment is annotated with [hersteld] or [onleesbaar], flag the segment for human review.
- OCR quality should be monitored during the translation process; if the source document is severely degraded, escalate to the project manager.

---

## 11. Translation Philosophy

### 11.1 Natural Dutch (Natural NL)

The primary goal is to produce Dutch that reads as if it were originally written in Dutch, not translated from another language.

**Guidelines:**
- **Avoid anglicisms**: Many English constructions and idioms have direct Dutch equivalents. Prefer the Dutch expression.
  - *In terms of* → *wat betreft* / *qua* (not *in termen van*).
  - *On a daily basis* → *dagelijks* (not *op een dagelijkse basis*).
  - *In order to* → *om te* (not *in order om te*).
- **Avoid literal word-for-word translation**: Rely on the meaning, not the structure of the source sentence.
- **Use Dutch idioms**: Replace English idioms with Dutch equivalents where possible.
  - *It's raining cats and dogs* → *Het regent pijpenstelen*.
  - *To kill two birds with one stone* → *Twee vliegen in een klap*.
- **Read aloud test**: If a translated sentence feels awkward when read aloud in Dutch, revise it.

### 11.2 Concise Style (Beknopte Stijl)

Dutch prefers conciseness. Where English may use multiple words, Dutch often uses one.

| English (wordy) | Dutch (concise) |
|---|---|
| In the event that | Indien / Als |
| With regard to | Met betrekking tot / Over |
| In the near future | Binnenkort / Op korte termijn |
| A large number of | Veel / Een groot aantal |
| It is important to note that | Let op: / Belangrijk: |

- **Germanic preference**: Dutch (as a Germanic language) naturally prefers shorter, compound words over prepositional phrases: *arbeidsvoorwaarden* instead of *voorwaarden voor de arbeid*.
- **Avoid redundant modifiers**: *opnieuw hervatten* (resume again) → *hervatten*; *volledig geheel* (full total) → *geheel*.

### 11.3 Het/De Accuracy

Accuracy in article (het/de) choice is non-negotiable. An incorrect article is immediately noticeable to native speakers and damages credibility.

**Resources for article lookup:**
- *Woordenlijst Nederlandse Taal* (het Groene Boekje) — authoritative.
- *Van Dale Groot Woordenboek van de Nederlandse Taal* — standard dictionary.
- *Algemene Nederlandse Spraakkunst* (ANS) — grammar reference.

**Common trouble areas:**
- **Het/de** for the same word in different meanings: *de pad* (toad) vs. *het pad* (path); *de nier* (kidney) vs. *het nier* (kidney as food — rare).
- **Loanwords**: When a new loanword enters Dutch, it typically becomes a **de** word. If unsure, default to **de** for new loanwords.
- **Plural forms**: *de* is used for all plural nouns regardless of singular gender: *de huizen* (even though *het huis*).
- **Diminutives**: always *het*.

### 11.4 Register Consistency

Maintain a consistent register throughout the translation:

| Register | When to use | Characteristics |
|---|---|---|
| Formal (formeel) | Legal, official, corporate, academic | U form, passive voice, formal vocabulary, no contractions, Hoogachtend |
| Neutral (neutraal) | General business, manuals, journalism | U or avoided pronoun, moderate sentence length, standard vocabulary |
| Informal (informeel) | Consumer marketing, social media, internal comms | Je form, active voice, contractions, idiomatic expressions |

- **Never mix registers** within a single document. A manual that starts with *u* should not switch to *je*.
- Translate to the register that best matches the source text's register and the target audience's expectations.

### 11.5 Handling Culture-Specific References

- **Measurements**: Convert to metric system: *inches* → *centimeter*, *feet* → *meter*, *miles* → *kilometer*, *pounds* → *kilogram*, *Fahrenheit* → *Celsius*.
- **Currency**: Convert to EUR unless the original currency is part of the text's context (e.g., a US-specific report preserving USD amounts).
- **Cultural references**: 
  - If a reference is well-known in the Dutch context, use the Dutch equivalent (*Thanksgiving* → explain as *Amerikaanse feestdag*).
  - If a reference has no Dutch equivalent, keep the original and add a brief explanation if necessary for comprehension.
  - For puns and wordplay: if a direct translation loses the effect, find a Dutch pun with equivalent tone and intent.
- **Legal concepts**: Dutch legal terminology differs from common-law terminology. Consult a legal translator for formal legal documents.

### 11.6 Sentence Length and Structure

- Dutch sentences are often shorter than English sentences of equivalent information density.
- Do not replicate multi-clause English sentences with multiple subordinations. Break them into shorter sentences where natural.
- Use **SOV** correctly in subordinate clauses (see 8.1) — this is one of the most common translation errors.
- Dutch prefers **right-dislocation** (uitloop) less frequently than English uses right-branching structures. Keep modifiers before the noun where natural: *de gisteren gepubliceerde beschikking* rather than *de beschikking die gisteren gepubliceerd werd*.

### 11.7 False Friends (Schijnverwanten)

Be aware of common Dutch-English false friends:

| Dutch word | Looks like | Actually means |
|---|---|---|
| actueel | actual | current, topical |
| eventueel | eventual | possible, if needed |
| formeel | formal | formal |
| gif | gift | poison |
| immers | immerse | after all |
| intimiderend | intimidating | intimidating |
| kantoor | canter | office |
| munitie | munition | ammunition |
| notoir | notorious | notorious |
| overslag | overslag | transshipment |
| rapport | rapport | report |
| screen | screen | to scan/systematically check |
| sensatie | sensation | sensation/thrill |
| solliciteren | solicit | to apply for a job |
| staking | staking | strike (work stoppage) |
| vies | fizz | dirty, gross |
| worst | worst | sausage |
| zakelijk | sake-like | business-related, matter-of-fact |

### 11.8 Capitalization in Translated Titles

When translating document titles, book titles, headings, and captions:

1. Apply Dutch sentence-case capitalization (see 7.1).
2. Translate the title meaningfully, not literally.
3. Preserve any proper nouns in their original capitalization.
4. For subtitles after a colon: capitalize the first word: *De geschiedenis van Amsterdam: Een overzicht van de zeventiende eeuw*.

### 11.9 Special Considerations for Technical vs. Creative Translation

**Technical translation:**
- Prioritize accuracy and consistency over elegance.
- Use standard Dutch technical terminology.
- Glossaries and term bases must be followed exactly.

**Creative/marketing translation:**
- Prioritize impact and natural flow over literal accuracy.
- Recreate effects (rhyme, alliteration, humor) rather than translating words.
- May deviate from sentence-level fidelity to achieve document-level goals.

**Hybrid (e.g., mixed content):**
- Apply technical rules to technical sections, creative freedom to marketing sections.
- Flag the register boundaries for the reviewer.

### 11.10 Revision and Self-Correction

Before finalizing a translation, check:

1. **Numerical accuracy**: every number in the translation matches the source (recalculated for currency/unit conversions).
2. **Article consistency**: that each noun has the correct article (de/het) and that it is used consistently throughout.
3. **Verb placement**: is every subordinate clause SOV? Is every main clause V2?
4. **Register**: is u/je consistent? Are formal closings and salutations correct?
5. **False friends**: scan for any English-looking Dutch words that might be false friends.
6. **Comma usage**: no Oxford comma, commas present where required.
7. **Date/number format**: comma for decimals, DD-MM-YYYY for dates, no AM/PM.
8. **Diacritics**: all required trema's, acute accents, and other diacritics present.
9. **Idiomatic naturalness**: read the Dutch aloud — does it sound natural?

---

*This document is based on the spelling and stylistic conventions of the Nederlandse Taalunie (Algemeen Nederlands), the official regulatory body for the Dutch language, and follows the Woordenlijst Nederlandse Taal (het Groene Boekje) as the standard reference.*
