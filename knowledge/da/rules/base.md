---
id: da/rules/base
type: rules
target_lang: da
name: Danish Translation Base Rules
description: Danish base translation rules
---

# Danish Translation Base Rules

This document defines the foundational rules for translating documents into Danish (dansk). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **decimal comma** is used in Danish: `3,14` (not `3.14`).
- Decimal places are separated by a comma with **no space** before or after: `0,25`, `12,5`, `100,99`.
- Trailing zeros after the decimal comma are preserved when they carry significance: `5,00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **period** (point) is used as the thousands separator: `1.000`, `25.000`, `1.000.000`.
- Do NOT use comma, space, or apostrophe as thousands separator: `1,000` is WRONG.
- Four-digit numbers may optionally omit the period: `1000` is acceptable, `1.000` is preferred.
- No thousands separator is used after the decimal comma: `1.000,50`.

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3,14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1.000,00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a non-breaking space: `25 %` or `25%`.
- Both forms are acceptable in modern Danish, but `25 %` (with space) is more common in formal/technical texts.
- Choose one form and maintain consistency throughout the document.
- Percentage ranges: `10-20 %` or `10 % til 20 %`.

### 1.5 Ordinal Numbers
- Ordinal numbers in Danish use a period after the numeral: `1.` (første), `2.` (anden), `3.` (tredje).
- Example: `20. århundrede` (20th century), `3. paragraf` (article 3), `5. plads` (5th place).
- The period is NOT a full stop; it is an ordinal suffix marker.

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).

### 1.7 Numerals in Text
- Numbers from zero to nine (or up to ten, depending on context) are typically written as words in running text: `tre`, `syv`, `ti`.
- Numbers above nine are written as digits: `42`, `1.250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Danish Krone (DKK/kr.)
- Symbol: `kr.` (placed after the amount, separated by a space: `100,00 kr.`).
- ISO code: `DKK` (used in financial/technical contexts: `100,00 DKK`).
- NEVER place the `kr.` symbol before the amount.
- The period after `kr.` is part of the abbreviation and should be preserved.

### 2.2 Other Currencies
- Euro: `€` placed after the amount: `100,00 €` (ISO: `EUR`).
- US Dollar: `$` placed after the amount: `100,00 $` (ISO: `USD`).
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies.

### 2.3 Currency Translation Rules
- Translate currency names in running text: "dollars" → `dollar`, "euros" → `euro`.
- Maintain the original currency amounts; do NOT convert to Danish kroner unless explicitly instructed.

### 2.4 Formatting Rules
- Decimal comma applies to all currency amounts: `100,00` (not `100.00`).
- Thousands period applies: `1.000,00 kr.` (not `1000,00 kr.`).
- Use exactly two decimal places for financial amounts: `50,00 kr.` (not `50 kr.`).

---

## 3. Date and Time

### 3.1 Date Format
- Danish date format: **DD.MM.YYYY** (day.month.year) or **DD/MM/YYYY**.
- The dot is the standard separator: `25.05.2026`.
- Leading zeros are used for single-digit days and months: `01.04.2026` (not `1.4.2026`).
- ISO format (YYYY-MM-DD) is also acceptable in technical contexts.

### 3.2 Month Names (Danish)
- Months are written in **lowercase** in Danish (unlike English).

| English | Danish | Abbreviation |
|---------|--------|-------------|
| January | januar | jan. |
| February | februar | feb. |
| March | marts | mar. |
| April | april | apr. |
| May | maj | maj |
| June | juni | jun. |
| July | juli | jul. |
| August | august | aug. |
| September | september | sep. |
| October | oktober | okt. |
| November | november | nov. |
| December | december | dec. |

- Day-month-year with month name: `25. maj 2026` (with dot after day).
- Centuries: `20. århundrede`, `21. århundrede`.

### 3.3 Day Names (Danish)
- Written in lowercase: `mandag`, `tirsdag`, `onsdag`, `torsdag`, `fredag`, `lørdag`, `søndag`.
- Abbreviations: `man.`, `tir.`, `ons.`, `tor.`, `fre.`, `lør.`, `søn.`

### 3.4 Time Format
- **24-hour format** is standard: `15:30` (not `3:30 PM`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours is common but not mandatory: `08:00` or `8:00`.
- AM/PM notation is NOT used in Danish.

### 3.5 Combined Date and Time
- Date and time are separated by a space: `25.05.2026 14:30`.
- The word `kl.` (klokken) is used when reading time aloud or in formal prose: `25. maj 2026 kl. 14:30`.

### 3.6 Time Zones
- Danish time zone is CET (UTC+1) / CEST (UTC+2 in summer).
- Time zone abbreviation: `CET`, `CEST` or `dansk tid` (Danish time).

---

## 4. Addresses

### 4.1 Danish Address Format
Danish addresses flow from **smallest to largest** unit:

1. **Street name + number** (Vejnavn + nummer): `Vesterbrogade 120, 3. th.`
2. **Postal code + city** (Postnummer + bynavn): `1620 København V`

Example: `Vesterbrogade 120, 3. th., 1620 København V`

### 4.2 Address Components

| English | Danish | Abbreviation |
|---------|--------|-------------|
| Street | vej / gade | v. / g. |
| Avenue | allé | — |
| Road | vej | v. |
| Square | plads | — |
| Floor | etage | sal |
| Left/Right | venstre / højre | v. / h. |
| Apartment | lejlighed | lejl. / l. |
| Postcode | postnummer | — |
| P.O. Box | postboks | pb. |

### 4.3 Postal Codes
- Danish postal codes are 4 digits: `1000`, `2100`, `8200`.
- Foreign postal codes are preserved as-is.

---

## 5. Proper Nouns

### 5.1 Danish Special Characters
Danish uses three special characters in addition to the basic Latin alphabet:

| Upper | Lower | Name | Example |
|-------|-------|------|---------|
| Æ | æ | æ (ae-ligatur) | Brød, København |
| Ø | ø | ø (o-slash) | Første, søn |
| Å | å | å (a-ring) | Århus, gå |

- These are **separate letters** in the Danish alphabet, not diacritical variants.
- They sort after z in the alphabet: æ is the 27th letter, ø is the 28th, å is the 29th.
- Failure to use the correct special character is a **spelling error**, not a stylistic choice.

### 5.2 Danish Stød (Glottal Stop)
- Danish has a unique suprasegmental feature called **stød** (glottal stop or laryngealization).
- Stød is not marked in standard orthography but affects word meaning.
- When adapting loanwords into Danish, stød patterns may apply naturally to speakers.
- Translators should be aware that stød distinguishes some minimal pairs (e.g., `hun` "she" vs. `hund` "dog" — though stød is not the only differentiator).

### 5.3 Foreign Name Transcription
- Foreign personal names are generally **preserved in their original spelling**.
- Established Danish forms exist for well-known names/places:
  - `London` → `London` (same)
  - `Paris` → `Paris` (same)
  - `Washington` → `Washington` (same)
  - `Germany` → `Tyskland`
  - `Sweden` → `Sverige`
  - `Norway` → `Norge`
  - `Finland` → `Finland`
  - `Beijing` → `Beijing` / `Peking`
- When in doubt, **preserve the original spelling**.

### 5.4 Capitalization Rules
- Proper nouns are capitalized: `København`, `Danmark`, `Madsen`.
- Titles preceding names are capitalized: `Direktør Jensen`, `Professor Hansen`.
- Languages ARE capitalized in Danish: `dansk`, `engelsk`, `tysk` — NOTE: unlike Turkish, language names are lowercase in Danish.
- Days of the week and months are lowercase (see Section 3).

---

## 6. Punctuation

### 6.1 Danish-Specific Punctuation Rules
Danish punctuation largely follows the same conventions as English, with some important differences.

### 6.2 Comma (,)
- Used to separate items in a list: `æbler, pærer og bananer`.
- Danish typically does NOT use the Oxford comma (no comma before `og` in simple lists).
- Used before relative clauses and after introductory phrases.
- Used after interjections and address forms.

### 6.3 Quotation Marks
- Primary quotation: Danish uses `"...""` (same as English) or `»...«` (guillemets, common in formal/printed texts).
- Single quotation marks: `'...'` for quotes within quotes.
- In modern Danish, straight quotes (" ") are widely accepted.

### 6.4 Colon (:)
- Used to introduce a list, explanation, or quotation.
- The letter following a colon is NOT automatically capitalized (same as English).

### 6.5 Period (.)
- Used at the end of declarative sentences.
- Used after ordinal numbers: `1.`, `2.`, `3.`
- Used in abbreviations: `ca.` (cirka), `evt.` (eventuelt), `dvs.` (det vil sige).

### 6.6 Hyphen (-) and Dash (—)
- Hyphen (-): used in compound words and number ranges (`10-15`).
- En dash (–): used for number ranges in formal typography (`10–15`).
- Em dash (—): used for parenthetical interruptions, with spaces on both sides: `tekst — mere tekst`.

### 6.7 No Double Punctuation
- Danish does NOT use double punctuation. NEVER combine punctuation marks like `,.`, `?!`, `!,`.

---

## 7. Formatting

### 7.1 Title Capitalization
- In Danish, **only the first word** of a title is capitalized (sentence case) — this is the standard convention.
- Proper nouns within titles remain capitalized.
- Example: `Krig og fred` (War and Peace), `At kende et menneske` (To Know a Person).

### 7.2 Lists
- Bulleted lists: each item starts with a lowercase letter (unless it is a complete sentence or proper noun).
- Numbered lists: use ordinal format `1.`, `2.`, `3.` (with period).
- Nested lists: use different markers (dash, asterisk, or lowercase letters).

### 7.3 Spacing
- Single space after periods, colons, and semicolons (not double space).
- No space before punctuation marks (comma, period, question mark, exclamation).
- One space before opening parentheses and after closing parentheses when embedded in text.

---

## 8. Grammar Essentials for Translators

### 8.1 Danish Word Order
Danish is a **Subject-Verb-Object** (SVO) language, like English. However, Danish has **V2 word order** (verb-second): in main clauses, the finite verb must be the second constituent.

- `I dag går jeg i skole.` (Today I go to school.) — verb `går` is second.
- `Jeg går i skole i dag.` (I go to school today.) — verb still second.

In subordinate clauses, the verb moves to the end:
- `Jeg ved, at jeg går i skole i dag.`

### 8.2 Articles
- **Definite article**: `en` (common gender) / `et` (neuter gender) as indefinite; suffixed `-en`/`-et`/`-ne` for definite.
  - `en bog` (a book) → `bogen` (the book)
  - `et hus` (a house) → `huset` (the house)
- Danish has **two grammatical genders**: common (fælleskøn) and neuter (intetkøn).

### 8.3 Compound Words
Danish, like other Germanic languages, forms **compound words** by joining words together:
- `arbejde` (work) + `plads` (place) = `arbejdsplads` (workplace)
- The connecting element is often `-s-` or `-e-` or nothing.

### 8.4 Passive Voice
Danish passive is formed with `blive` + past participle or the `-s` suffix:
- `Rapporten blev skrevet af direktøren.` (The report was written by the director.)
- `Rapporten skrives af direktøren.` (The report is written by the director.)

### 8.5 Negation
- Negation uses `ikke`: `Jeg forstår ikke` (I don't understand) or `Jeg forstår det ikke`.
- `Ingen` (no/none) for noun negation: `Ingen adgang` (No access).

### 8.6 Pronouns

| Person | Subject | Object | Possessive |
|--------|---------|--------|------------|
| 1st sing | jeg | mig | min/mit |
| 2nd sing | du | dig | din/dit |
| 3rd sing | han/hun/den/det | ham/henem/den/det | hans/hendes/dens/dets |
| 1st plur | vi | os | vores |
| 2nd plur | I | jer | jeres |
| 3rd plur | de | dem | deres |

### 8.7 Modal Verbs

| English | Danish | Nuance |
|---------|--------|--------|
| shall / must | skal | Obligation or future tense |
| must | måste / er nødt til | Strong obligation |
| may (permission) | må / kan | Permission (må) or possibility (kan) |
| should | bør | Recommendation |
| will | vil / kommer til at | Future / intention |
| can | kan | Ability / possibility |

**Important**: In legal Danish, **skal** is the standard modal for expressing obligation (equivalent to English "shall" in legal texts). **Må** indicates permission. The distinction between **skal** and **bør** is critical in contract translation.

---

*End of Danish Translation Base Rules. These rules should be read in conjunction with any project-specific guidelines provided.*
