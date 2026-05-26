---
id: hr/rules/base
type: rules
target_lang: hr
name: Croatian Translation Base Rules
description: Croatian base translation rules
---

# Croatian Translation Base Rules

This document defines the foundational rules for translating documents into Croatian (hr). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **decimal comma** is used in Croatian: `3,14` (not `3.14`).
- Decimal places are separated by a comma with **no space** before or after: `0,25`, `12,5`, `100,99`.
- Trailing zeros after the decimal comma are preserved when they carry significance: `5,00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **period** is used as the thousands separator in Croatian: `1.000`, `25.000`, `1.000.000`.
- Do NOT use a space or comma as thousands separator: `1 000` and `1,000` are WRONG in Croatian.
- Four-digit numbers may optionally omit the separator: `1000` is acceptable, `1.000` is preferred in formal texts.
- The thousands separator is NEVER used after the decimal comma: `1.000,50` (period groups thousands, comma separates decimals).

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3,14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1.000,00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with **no space**: `25%`, `3,5%`.
- Some Croatian texts add a thin space before `%`: `25 %` — but the compact form is more common.
- Percentage ranges: `10–20%` or `10 % do 20 %`.
- Choose one form and maintain consistency throughout the document.

### 1.5 Ordinal Numbers
- Ordinal numbers in Croatian use a period after the numeral: `1.`, `2.`, `3.`
- Example: `20. stoljeće` (20th century), `3. stavak` (paragraph 3), `5. mjesto` (5th place).
- The period is NOT a full stop; it is an ordinal suffix marker.

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).

### 1.7 Numerals in Text
- Numbers from one to nine (or up to twelve, depending on context) are typically written as words in running text: `jedan`, `tri`, `sedam`, `dvanaest`.
- Numbers above twelve are written as digits: `42`, `1.250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Euro (EUR)
- Croatia adopted the **euro** as its official currency on 1 January 2023, replacing the Croatian kuna (HRK).
- Symbol: `EUR` (ISO code preferred in Croatian texts).
- **Symbol placement**: Amount first, then code: `100,00 EUR`.
- The euro symbol `EUR` is more common than `€` in Croatian financial texts, though `€` is also acceptable.
- In informal contexts, `€` may be placed before the amount: `€100,00`.
- The name of the currency in Croatian: `euro` (singular), `eura` (genitive), `eurima` (dative/locative).

### 2.2 US Dollar
- Symbol: `$`.
- **Symbol placement**: `$` is placed **after** the amount, separated by a space: `100,00 $`.
- Alternative (ISO code): `100,00 USD`.

### 2.3 Other Currencies
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies: `100,00 GBP`, `100,00 JPY`, `100,00 CHF`.

### 2.4 Currency Translation Rules
- Translate currency names in running text: "dollars" → `dolari`, "euros" → `euri`.
- "pence" → `pence`, "cents" → `centi`.
- Maintain the original currency amounts; do NOT convert to euros unless explicitly instructed.

### 2.5 Formatting Rules
- Decimal comma applies to all currency amounts: `100,00` (not `100.00`).
- Thousands period applies: `1.000,00 EUR` (not `1000,00 EUR`).
- Use exactly two decimal places for financial amounts: `50,00 EUR` (not `50 EUR`).

---

## 3. Date and Time

### 3.1 Date Format
- Croatian date format: **DD.MM.YYYY.** (day.month.year with a trailing period).
- The trailing period after the year is common in Croatian dates: `25.05.2026.` (not `25.05.2026`).
- Leading zeros are used for single-digit days and months: `01.04.2026.` (not `1.4.2026.`).

### 3.2 Month Names (Croatian)
- Months are written in **lowercase** in Croatian (unlike English).
- Croatian month names:

| English | Croatian | Abbreviation |
|---------|----------|-------------|
| January | siječanj | sij. |
| February | veljača | velj. |
| March | ožujak | ožu. |
| April | travanj | tra. |
| May | svibanj | svib. |
| June | lipanj | lip. |
| July | srpanj | srp. |
| August | kolovoz | kol. |
| September | rujan | ruj. |
| October | listopad | lis. |
| November | studeni | stu. |
| December | prosinac | pro. |

- Day-month-year with month name: `25. svibnja 2026.` (dot after day, no comma between components).
- Centuries: `20. stoljeće`, `21. stoljeće`.

### 3.3 Day Names (Croatian)
- Written in lowercase: `ponedjeljak`, `utorak`, `srijeda`, `četvrtak`, `petak`, `subota`, `nedjelja`.
- Abbreviations: `pon.`, `uto.`, `sri.`, `čet.`, `pet.`, `sub.`, `ned.`.

### 3.4 Time Format
- **24-hour format** is standard: `14:30` (not `2:30 PM`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours: `08:00` (not `8:00`).
- AM/PM notation is NOT used in Croatian.
- The word `sati` (hours) may precede the time in formal contexts: `14:30 sati`.

### 3.5 Combined Date and Time
- Date and time are separated by a space: `25.05.2026. 14:30`.
- In formal prose: `25. svibnja 2026. u 14:30 sati`.

### 3.6 Time Zones
- Croatian time zone is CET (UTC+1) in winter and CEST (UTC+2) in summer.
- Time zone abbreviations: `CET`, `CEST`.

---

## 4. Croatian Special Characters

### 4.1 The Croatian Alphabet
The Croatian alphabet has 30 letters, including five unique characters:

| Upper | Lower | Name | Example |
|-------|-------|------|---------|
| C with caron | c with caron | ce | cest, ocevi |
| C with acute | c with acute | ce | ucenik, naravno |
| D with stroke | d with stroke | de | djed, dodir |
| S with caron | s with caron | se | sjever, pas |
| Z with caron | z with caron | ze | zivot, jezik |

### 4.2 Critical Character Distinctions
- **c with caron (c)**: A single letter, NOT a combination of 'c' and 'h'. It represents the "ch" sound in English "church".
- **c with acute (c)**: NOT the same as 'c'. It represents the "ts" sound.
- **d with stroke (d)**: NOT the same as 'd'. It represents a soft "dj" sound (like "j" in "jump").
- **s with caron (s)**: NOT the same as 's'. It represents the "sh" sound.
- **z with caron (z)**: NOT the same as 'z'. It represents the "zh" sound (like "s" in "pleasure").
- These characters have uppercase forms: C, C, D, S, Z (used at sentence beginnings and in proper nouns).

### 4.3 Common Spelling Errors to Avoid
- Do NOT substitute `ch` for `c`: `cestitka` is WRONG — correct: `čestitka`.
- Do NOT substitute `ts` for `c`: `ucenik` is WRONG — correct: `učenik`.
- Do NOT substitute `dj` for `d`: `djevojka` is WRONG — correct: `djevojka`.
- Do NOT substitute `sh` for `s`: `sjever` is WRONG — correct: `sjever`.
- Do NOT substitute `zh` for `z`: `zivot` is WRONG — correct: `život`.
- Croatian uses ONLY Latin script — never Cyrillic in modern Croatian documents.

### 4.4 Character Encoding
- Croatian text MUST be encoded in **UTF-8**.
- Verify that the following encoded characters are rendered correctly:
  - `c` = U+010D, `C` = U+010C
  - `c` = U+0107, `C` = U+0106
  - `d` = U+0111, `D` = U+0110
  - `s` = U+0161, `S` = U+0160
  - `z` = U+017E, `Z` = U+017D

---

## 5. Formality

### 5.1 Vi (formal) vs ti (informal)
Croatian uses a **T-V distinction** for second-person address:

| Pronoun | Level | Usage |
|---------|-------|-------|
| Vi | Formal | Business, government, formal correspondence, addressing strangers |
| ti | Informal | Friends, family, close colleagues, casual contexts |

### 5.2 Implications for Translation
- **DEFAULT to `Vi`** in business, legal, and formal translations.
- **Use `ti`** only when the source text clearly uses informal register (e.g., marketing to young audiences, internal team communication).
- English "you" maps to `Vi` (formal) or `ti` (informal) depending on context.
- When `Vi` is used, verbs are conjugated in the 3rd person plural: `Vi ste` (you are), `Vi možete` (you can).

### 5.3 Formal Correspondence

| English | Croatian |
|---------|----------|
| Dear Mr. Smith | Poštovani gospodine Smithu |
| Dear Ms. Smith | Poštovana gospođice Smith |
| Dear Sir/Madam | Poštovani / Poštovani gospodine / Poštovana gospođo |
| To whom it may concern | Kome se to može odnositi |
| Sincerely | S poštovanjem |
| Best regards | Srdačni pozdravi |
| Kind regards | Lijepi pozdravi |

### 5.4 Title Usage
- `gospodin` (Mr.) / `gosp.` (abbreviated)
- `gospođa` (Mrs./Ms.) / `gđa` (abbreviated)
- `gospodična` (Miss) / `gđica` (abbreviated)
- `dr.` (doctor)
- Titles precede the surname: `gospodin Smith`, `gospođa Smith`.

### 5.5 Register Adaptation
- **Business**: Formal, professional. Use `Vi` and formal conjugation. Clear and respectful.
- **Legal**: Highly formal. Use `Vi`. Precise terminology, formal grammar.
- **Marketing**: Can range from formal to conversational. Match target audience.
- **Technical**: Precise, clear, consistent terminology. Moderate formality. Use `Vi`.
- **Academic**: Formal, well-structured, technical terminology. Use `Vi`.

---

## 6. Grammar

### 6.1 Cases
Croatian has **seven grammatical cases** (excluding vocative in some analyses):

| Case | Name | Function | Example (singular, m. anim.) |
|------|------|----------|------------------------------|
| Nominative | Nominativ | Subject | student |
| Genitive | Genitiv | Possession, partitive | studenta |
| Dative | Dativ | Indirect object | studentu |
| Accusative | Akuzativ | Direct object | studenta |
| Vocative | Vokativ | Direct address | studente |
| Locative | Lokativ | Location (with prepositions) | studentu |
| Instrumental | Instrumental | Means/instrument | studentom |

### 6.2 Gender
Croatian has three grammatical genders:

| Gender | Noun ending (nom.) | Pronoun | Example |
|--------|-------------------|---------|---------|
| Masculine (muški) | consonant | on | student, stol |
| Feminine (ženski) | -a | ona | knjiga, žena |
| Neuter (srednje) | -o, -e | ono | dijete, pismo |

### 6.3 Word Order
- Croatian default word order is **SVO** (Subject-Verb-Object), but it is highly flexible due to the case system.
- Word order changes emphasize different parts of the sentence.
- In formal writing, SVO is preferred for clarity.
- Questions are formed with intonation, not word order inversion.

---

## 7. Punctuation

### 7.1 Quotation Marks
- Primary quotation: `"..."` (same as English).
- Alternative (formal/academic): `„..."` (German-style low-high quotation marks — also common in Croatian).
- Single quotation marks: `'...'` for quotes within quotes.

### 7.2 Comma (,)
- Used to separate items in a list: `jabuke, kruške, banane i grožđe`.
- Croatian uses `i` (and) before the last item, preceded by a comma (Oxford comma is used).
- Used before relative clauses and after introductory phrases.
- Used after interjections: `Da, točno je.`

### 7.3 Colon (:)
- Used to introduce a list, explanation, or quotation (same as English).
- The letter following a colon is NOT automatically capitalized.

### 7.4 Period (.)
- Used at the end of declarative sentences.
- Used after ordinal numbers: `1.`, `2.`, `3.` (this is NOT a full stop but an ordinal marker).
- Used in abbreviations: `npr.`, `tj.`, `sl.`

### 7.5 Apostrophe (')
- Croatian does NOT use an apostrophe for genitive: `Petrov auto` (not `Petrov's auto`).
- Apostrophes are rare in Croatian; they may appear in some loanwords.

### 7.6 Hyphen (-) and Dash (—)
- Hyphen (-): used in compound words (`hrvatsko-engleski`), line breaks, and number ranges (`10-15`).
- En dash (–): used for number ranges in formal typography (`10–15`), but a hyphen is acceptable.
- Em dash (—): used for parenthetical interruptions in sentences.

### 7.7 No Double Punctuation
- Croatian does NOT use double punctuation. NEVER combine punctuation marks:
  - `"On je došao." rekao je.` (correct: one period inside quotes is sufficient).
  - `"Što se događa?" pitao je.` (question mark inside quotes, no additional punctuation needed).

---

## 8. Formatting

### 8.1 Title Capitalization
- In Croatian, **only the first word** of a title is capitalized (sentence case) — this is the **most common and correct convention**.
- Proper nouns within titles remain capitalized.
- Example: `Rat i mir` (War and Peace), `Upoznati čovjeka` (To Know a Person).

### 8.2 Headings and Subheadings
- Use sentence case for headings: `Ovo je naslov` (not `Ovo Je Naslov`).
- No period at the end of headings.

### 8.3 Lists

**Bulleted Lists:**
- Each item starts with a lowercase letter (unless it is a complete sentence or proper noun).
- Items that are complete sentences end with a period.
- Items that are phrases do NOT end with punctuation.

**Numbered Lists:**
- Use ordinal format for list markers: `1.`, `2.`, `3.` (with period).

### 8.4 Abbreviations
- Common Croatian abbreviations:
  - `npr.` (na primjer — for example).
  - `tj.` (to jest — that is).
  - `sl.` (slika — figure/image).
  - `str.` (stranica — page).
  - `stav.` (stavak — paragraph).
  - `itd.` (i tako dalje — etc.).
  - `odn.` (odnosno — respectively).
  - `cca.` (cca. — approximately).
- Abbreviations take a period after each abbreviated segment: `npr.`, `tj.`

### 8.5 Spacing
- Single space after periods, colons, and semicolons (not double space).
- No space before punctuation marks (comma, period, question mark, exclamation).
- One space before opening parentheses and after closing parentheses when embedded in text.

---

## 9. Translation Philosophy

### 9.1 Natural Croatian
The primary goal is to produce **natural-sounding Croatian** that reads as if it were originally written in Croatian, not translated from another language.

**Principles:**
- Avoid calques (direct structural borrowings from the source language).
- Do not preserve source-language sentence structure when it violates natural Croatian word order.
- Use idiomatic Croatian expressions where they convey the same meaning as the source.
- Prefer Croatian vocabulary over borrowed/foreign words where a well-established Croatian equivalent exists.

### 9.2 Compound Words
Croatian (like other Slavic languages) uses compounding:
- `računalo` (computer — literally "computing machine").
- `softver` (software — loanword).
- `hardver` (hardware — loanword).
- When translating, combine concepts into natural Croatian compounds where appropriate.

### 9.3 Definiteness and Indefiniteness
Croatian does not use articles (no "a" or "the"). Definiteness is expressed through:
- Word order (definite nouns tend to appear earlier in the sentence).
- Demonstrative pronouns: `taj`, `ta`, `to` (that).
- Possessive pronouns: `moj`, `tvoj`, `njegov` (my, your, his).
- When translating, ensure the correct level of definiteness is conveyed through context.

### 9.4 Domain-Specific Terminology
- Use established Croatian terminology for the relevant domain.
- For technical/scientific translation, consult Croatian terminology resources:
  - Hrvatski jezični portal (Croatian Language Portal).
  - Matica hrvatska terminology resources.
  - Industry-specific glossaries.
- When no Croatian equivalent exists, the foreign term may be used, typically with a Croatian explanation on first use.

### 9.5 Untranslatable Elements
- Some elements may legitimately remain in the source language:
  - Brand names and product names: `iPhone`, `Windows`, `Google`.
  - Foreign titles: `Mr.`, `Mrs.` when referring to foreign individuals in foreign contexts.
  - Acronyms: preserve original but provide Croatian expansion on first use if helpful.
  - Quoted foreign language text within the source: leave as-is unless the surrounding context clearly demands translation.

---

*End of Croatian Translation Base Rules. These rules should be read in conjunction with any project-specific guidelines provided.*
