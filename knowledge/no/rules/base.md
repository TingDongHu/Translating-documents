---
id: no/rules/base
type: rules
target_lang: no
name: Norwegian Translation Base Rules
description: Norwegian base translation rules
---

# Norwegian Translation Base Rules

This document defines the foundational rules for translating documents into Norwegian (Bokmal). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **decimal comma** is used in Norwegian: `3,14` (not `3.14`).
- Decimal places are separated by a comma with **no space** before or after: `0,25`, `12,5`, `100,99`.
- Trailing zeros after the decimal comma are preserved when they carry significance: `5,00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **narrow non-breaking space** (Unicode U+202F) is used as the thousands separator: `1 000`, `25 000`, `1 000 000`.
- In practice, a regular space is also commonly used: `1 000`, `25 000`.
- Do NOT use period or comma as thousands separator: `1.000` and `1,000` are WRONG in Norwegian.
- Four-digit numbers may optionally omit the separator: `1000` is acceptable, `1 000` is preferred in formal texts.
- The thousands separator is NEVER used after the decimal comma: `1 000,50` (space groups thousands, comma separates decimals).

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3,14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1 000,00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a space: `25 %`, `3,5 %`.
- The space before `%` is mandatory in Norwegian typography.
- Percentage ranges: `10–20 %` or `10 % til 20 %`.
- Choose one form and maintain consistency throughout the document.

### 1.5 Ordinal Numbers
- Ordinal numbers in Norwegian use a period after the numeral: `1.`, `2.`, `3.`
- Example: `20. arhundre` (20th century), `3. ledd` (paragraph 3), `5. plass` (5th place).
- The period is NOT a full stop; it is an ordinal suffix marker.

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).

### 1.7 Numerals in Text
- Numbers from one to nine (or up to twelve, depending on context) are typically written as words in running text: `en`, `tre`, `sju`, `tolv`.
- Numbers above twelve are written as digits: `42`, `1 250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Norwegian Krone (NOK/kn)
- Symbol: `kr` (placed **after** the amount, separated by a space: `100,00 kr`, `1 500,50 kr`).
- ISO code: `NOK` (used in technical/financial contexts: `100,00 NOK`).
- NEVER place `kr` before the amount (`kr100,00` is WRONG).
- The plural of krone is kroner: `1 krone`, `5 kroner`, `100 kroner`.
- Ore (subunit): `100 ore = 1 krone`. In modern usage, ore is rarely used; prices are rounded to whole kroner.

### 2.2 US Dollar
- Symbol: `$`.
- **Symbol placement**: `$` is placed **after** the amount, separated by a space: `100,00 $`.
- Alternative (ISO code): `100,00 USD`.

### 2.3 Euro
- Symbol: `EUR` (ISO code preferred in Norwegian texts).
- **Symbol placement**: Amount first, then code: `100,00 EUR`.
- The euro symbol `EUR` is more common than `€` in Norwegian financial texts.

### 2.4 Other Currencies
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies: `100,00 GBP`, `100,00 JPY`, `100,00 CHF`.

### 2.5 Currency Translation Rules
- Translate currency names in running text: "dollars" → `dollar`, "euros" → `euro`.
- "pence" → `pence`, "cents" → `cent`.
- Maintain the original currency amounts; do NOT convert to Norwegian kroner unless explicitly instructed.

### 2.6 Formatting Rules
- Decimal comma applies to all currency amounts: `100,00` (not `100.00`).
- Thousands space applies: `1 000,00 kr` (not `1000,00 kr`).
- Use exactly two decimal places for financial amounts: `50,00 kr` (not `50 kr`).

---

## 3. Date and Time

### 3.1 Date Format
- Norwegian date format: **DD.MM.YYYY** (day.month.year).
- The dot is the standard separator: `25.05.2026`.
- Alternative separator (less common): hyphen `25-05-2026`. But the dot is preferred.
- Leading zeros are used for single-digit days and months: `01.04.2026` (not `1.4.2026`).

### 3.2 Month Names (Norwegian)
- Months are written in **lowercase** in Norwegian (unlike English).
- Norwegian month names:

| English | Norwegian | Abbreviation |
|---------|-----------|-------------|
| January | januar | jan. |
| February | februar | feb. |
| March | mars | mar. |
| April | april | apr. |
| May | mai | mai |
| June | juni | jun. |
| July | juli | jul. |
| August | august | aug. |
| September | september | sep. |
| October | oktober | okt. |
| November | november | nov. |
| December | desember | des. |

- Day-month-year with month name: `25. mai 2026` (dot after day, no comma between components).
- Centuries: `20. arhundre`, `21. arhundre`.

### 3.3 Day Names (Norwegian)
- Written in lowercase: `mandag`, `tirsdag`, `onsdag`, `torsdag`, `fredag`, `lordag`, `sondag`.
- Abbreviations: `man.`, `tir.`, `ons.`, `tor.`, `fre.`, `lor.`, `son.`.

### 3.4 Time Format
- **24-hour format** is standard: `14:30` (not `2:30 PM`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours: `08:00` (not `8:00`).
- AM/PM notation is NOT used in Norwegian.
- The word `kl.` (klokka) may precede the time in formal/literary contexts: `kl. 14:30`.

### 3.5 Combined Date and Time
- Date and time are separated by a space: `25.05.2026 14:30`.
- In formal prose: `25. mai 2026 klokka 14:30`.

### 3.6 Time Zones
- Norwegian time zone is CET (UTC+1) in winter and CEST (UTC+2) in summer.
- Time zone abbreviations: `CET`, `CEST`.
- Norway also has two non-standard time zones: `UTC+1` (mainland) and `UTC+1` (Svalbard, with different DST rules).

---

## 4. Norwegian Special Characters

### 4.1 The Norwegian Alphabet
The Norwegian alphabet has 29 letters, including three unique characters:

| Upper | Lower | Name | Example |
|-------|-------|------|---------|
| AE | ae | ae | are, gra |
| O with stroke | o with stroke | o | son, bo, for |
| A with ring | a with ring | a | are, dag, hand |

### 4.2 Critical Character Distinctions
- **ae (æ)**: A single letter, NOT a combination of 'a' and 'e'. It represents a distinct vowel sound.
- **o (ø)**: NOT the same as 'o' or 'oe'. It represents a distinct front rounded vowel.
- **a (å)**: NOT the same as 'a'. It represents a long open back vowel.
- These characters have uppercase forms: AE, O, A (used at sentence beginnings and in proper nouns).

### 4.3 Common Spelling Errors to Avoid
- Do NOT substitute `ae` for `æ`: `vaere` is WRONG, `vaere` is WRONG, `vaere` is WRONG — correct: `vaere`.
- Do NOT substitute `oe` for `ø`: `koebenhavn` is WRONG — correct: `kobenhavn` (but the city name is `Kobenhavn` in Danish/Norwegian).
- Do NOT substitute `aa` for `å`: `Aas` is an old spelling; modern: `As`.
- Do NOT merge `ae` into `a` or `e`: `vaere` → `vaere` (WRONG).

### 4.4 Character Encoding
- Norwegian text MUST be encoded in **UTF-8**.
- Verify that the following encoded characters are rendered correctly:
  - `ae` = U+00E6, `AE` = U+00C6
  - `o` = U+00F8, `O` = U+00D8
  - `a` = U+00E5, `A` = U+00C5

---

## 5. Bokmal vs. Nynorsk

### 5.1 Two Written Standards
Norwegian has TWO official written standards:
- **Bokmal** (Book Norwegian): Used by approximately 85-90% of the population. Based on Danish-Norwegian written tradition.
- **Nynorsk** (New Norwegian): Used by approximately 10-15% of the population, primarily in western Norway.

### 5.2 Default to Bokmal
- **ALL translations MUST default to Bokmal** unless explicitly instructed otherwise.
- Bokmal is the dominant standard in business, government, media, and international communication.
- Nynorsk is mainly used in western Norway, in some government documents, and in education.

### 5.3 Key Differences Between Bokmal and Nynorsk

| Feature | Bokmal | Nynorsk |
|---------|--------|---------|
| "I" | jeg | eg |
| "You" | du | du |
| "He" | han | han |
| "We" | vi | me |
| "Is" | er | er |
| "Was" | var | var |
| "House" | hus | hus |
    "Book" | bok | bok |
| "Water" | vann | vatn |
    "Good" | god | god |
| "To go" | ga | gjekk |
| "To say" | si | seie |
| "Here" | her | her |
    "There" | der | der |

### 5.4 Common Bokmal Forms to Use
- Use `ikke` (not `ikkje`).
- Use `meg` (not `meg`).
- Use `vi` (not `me`).
- Use `var` (not `var`).
- Use `har` (not `har`).
- Use `skal` (not `skal`).

---

## 6. Formality

### 6.1 The Du-Reformen (The You-Reform)
Norway completed the **du-reformen** in the 1970s, which abolished the formal `De` (you) in favor of universal `du` (you).

| Pronoun | Level | Usage |
|---------|-------|-------|
| du | Universal | Used for ALL contexts: formal, informal, business, government |
| De | Archaic/formal | Only in extremely formal religious or ceremonial contexts |

### 6.2 Implications for Translation
- **NEVER use `De`** in modern Norwegian translations. It sounds archaic and unnatural.
- **ALWAYS use `du`** regardless of context: business letters, government correspondence, legal documents, marketing materials.
- This is a MAJOR difference from many other European languages (French vous, German Sie, etc.).
- English "you" always translates to `du` in Norwegian.

### 6.3 Formal Correspondence

| English | Norwegian |
|---------|-----------|
| Dear Mr. Smith | Vaer sa venlig, hr. Smith / Kjare hr. Smith |
| Dear Ms. Smith | Vaer sa venlig, fru Smith / Kjare fru Smith |
| Dear Sir/Madam | Vaer sa venlig |
| To whom it may concern | Til den det ma anga |
| Sincerely | Med vennlig hilsen |
| Best regards | Med vennlig hilsen / Mange hilsener |
| Kind regards | Vennlig hilsen |

### 6.4 Title Usage
- `Hr.` (herre) = Mr.
- `Fru` = Mrs.
- `Froenn` = Ms. (increasingly replaced by `fru` for all women).
- `Dr.` = Doctor (same as English).
- Titles precede the surname: `Hr. Hansen`, `Fru Nordmann`.

### 6.5 Register Adaptation
- **Business**: Semi-formal, clear, direct. Use `du` and `deg`. Professional but not stiff.
- **Legal**: Formal but modern. Use `du` even in legal documents. Precise terminology.
- **Marketing**: Conversational, engaging. Use `du` and `deg`. Avoid overly formal language.
- **Technical**: Precise, clear, consistent terminology. Moderate formality. Use `du`.
- **Academic**: Formal, well-structured, technical terminology. Use `du`.

---

## 7. Punctuation

### 7.1 Quotation Marks
- Primary quotation: `"..."` (same as English).
- Alternative (formal/academic): `...` (guillemets) — used in some formal Norwegian texts.
- Single quotation marks: `'...'` for quotes within quotes.
- Norwegian uses the same quotation mark conventions as English in most modern texts.

### 7.2 Comma (,)
- Used to separate items in a list: `epler, pearer, bananer og druer`.
- Norwegian uses `og` (and) before the last item, preceded by a comma (Oxford comma is used in Norwegian).
- Used before relative clauses and after introductory phrases.
- Used after interjections: `Ja, det stemmer.`

### 7.3 Colon (:)
- Used to introduce a list, explanation, or quotation (same as English).
- The letter following a colon is NOT automatically capitalized (lowercase unless it begins a proper noun or independent quoted sentence).

### 7.4 Period (.)
- Used at the end of declarative sentences (same as English).
- Used after ordinal numbers: `1.`, `2.`, `3.` (this is NOT a full stop but an ordinal marker).
- Used in abbreviations: `f.eks.`, `dvs.`, `ca.`

### 7.5 Apostrophe (')
- Used for genitive: `Pettersens bil` (Petersen's car) — NO apostrophe in Norwegian genitive.
- Used to indicate omitted letters: `det'` (short for `det er`), `kan'` (short for `kan ikke`).
- Used in some loanwords: `sukker'`, `idé'`.

### 7.6 Hyphen (-) and Dash (—)
- Hyphen (-): used in compound words (`engelsk-norsk`), line breaks, and number ranges (`10-15`).
- En dash (–): used for number ranges in formal typography (`10–15`), but a hyphen is acceptable.
- Em dash (—): used for parenthetical interruptions in sentences.

### 7.7 No Double Punctuation
- Norwegian does NOT use double punctuation. NEVER combine punctuation marks:
  - `"Han kom." sa han.` (correct: one period inside quotes is sufficient).
  - `"Hva skjer?" spurte han.` (question mark inside quotes, no additional punctuation needed).

---

## 8. Formatting

### 8.1 Title Capitalization
- In Norwegian, **only the first word** of a title is capitalized (sentence case) — this is the **most common and correct convention**.
- Proper nouns within titles remain capitalized.
- Example: `Krig og fred` (War and Peace), `A kjenne et menneske` (To Know a Person).

### 8.2 Headings and Subheadings
- Use sentence case for headings: `Dette er en overskrift` (not `Dette Er En Overskrift`).
- No period at the end of headings.

### 8.3 Lists

**Bulleted Lists:**
- Each item starts with a lowercase letter (unless it is a complete sentence or proper noun).
- Items that are complete sentences end with a period.
- Items that are phrases do NOT end with punctuation.

**Numbered Lists:**
- Use ordinal format for list markers: `1.`, `2.`, `3.` (with period).

### 8.4 Abbreviations
- Common Norwegian abbreviations:
  - `osv.` (og sa videre — etc.), `bla.` (blant annet — among others).
  - `f.eks.` (for eksempel — e.g./for example).
  - `dvs.` (det vil si — i.e./that is).
  - `ca.` (cirka — approximately).
  - `m.m.` (med mer — and more).
  - `nr.` (nummer — number).
  - `s.` (side — page), `ss.` (sider — pages).
- Abbreviations take a period after each abbreviated segment: `f.eks.`, `d.v.s.`

### 8.5 Spacing
- Single space after periods, colons, and semicolons (not double space).
- No space before punctuation marks (comma, period, question mark, exclamation).
- One space before opening parentheses and after closing parentheses when embedded in text.

---

## 9. Translation Philosophy

### 9.1 Natural Norwegian
The primary goal is to produce **natural-sounding Norwegian** (Bokmal) that reads as if it were originally written in Norwegian, not translated from another language.

**Principles:**
- Avoid calques (direct structural borrowings from the source language).
- Do not preserve source-language sentence structure when it violates natural Norwegian word order.
- Use idiomatic Norwegian expressions where they convey the same meaning as the source.
- Prefer Norwegian vocabulary over borrowed/foreign words where a well-established Norwegian equivalent exists.

### 9.2 Compound Words
Norwegian (like other Germanic languages) uses extensive compounding:
- `datamaskin` (computer — literally "data machine").
- `programvare` (software — literally "program ware").
- `internett` (internet).
- When translating, combine concepts into natural Norwegian compounds where appropriate.

### 9.3 Definiteness and Indefiniteness
Norwegian uses suffixed articles for definiteness:
- Indefinite: `en bok` (a book), `et hus` (a house).
- Definite: `boka`/`boken` (the book), `huset` (the house).
- When translating, ensure the correct article form is used based on gender (masculine, feminine, neuter).

### 9.4 Domain-Specific Terminology
- Use established Norwegian terminology for the relevant domain.
- For technical/scientific translation, consult Norwegian terminology resources:
  - Sprakradet (The Language Council of Norway).
  - Industry-specific glossaries for specialized domains.
- When no Norwegian equivalent exists, the foreign term may be used, typically with a Norwegian explanation on first use.

### 9.5 Untranslatable Elements
- Some elements may legitimately remain in the source language:
  - Brand names and product names: `iPhone`, `Windows`, `Google`.
  - Foreign titles: `Mr.`, `Mrs.` when referring to foreign individuals in foreign contexts.
  - Acronyms: preserve original but provide Norwegian expansion on first use if helpful.
  - Quoted foreign language text within the source: leave as-is unless the surrounding context clearly demands translation.

---

*End of Norwegian Translation Base Rules. These rules should be read in conjunction with any project-specific guidelines provided.*
