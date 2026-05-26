---
id: fi/rules/base
type: rules
target_lang: fi
name: Finnish Translation Base Rules
description: Finnish base translation rules
---

# Finnish Translation Base Rules

This document defines the foundational rules for translating documents into Finnish. All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **comma** (pilkkumerkki) is used as the decimal separator in Finnish: `3,14` (not `3.14`).
- Decimal places are separated by a comma with **no space**: `0,25`, `12,5`, `100,99`.
- Trailing zeros after the decimal comma are preserved when they carry significance: `5,00` (for precision), otherwise `5`.

### 1.2 Thousands Separator
- The **space** (narrow non-breaking space, U+202F) is used as the thousands separator: `1 000`, `25 000`, `1 000 000`.
- Do NOT use period or comma as thousands separator: `1.000` and `1,000` are both WRONG in Finnish.
- Four-digit numbers also use the space separator: `1 000` (not `1000` without space).
- In some digital contexts, no separator is used for four-digit numbers (`1000`), but the space-separated form is the official convention.

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3,14`.
- In financial contexts, parentheses may alternatively indicate negatives: `(1 000,00)`.
- The minus sign should be followed by a space in running text: `- 5 miljoonaa` (some style guides prefer no space).

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a space: `25 %` (preferred) or `25%`.
- The space before `%` is the official Finnish convention, though `25%` (no space) is increasingly common in digital contexts.
- Choose one form and maintain consistency throughout the document.
- Percentage ranges: `10-20 %` or `10 % - 20 %`.

### 1.5 Ordinal Numbers
- Ordinal numbers in Finnish use a period after the numeral: `1.`, `2.`, `3.`.
- Example: `20. vuosisata` (20th century), `3. pykälä` (section 3), `5. sija` (5th place).
- The period is NOT a full stop; it is an ordinal suffix marker.

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).

### 1.7 Numerals in Text
- Numbers from one to ten (yksi to kymmenen) are typically written as words in running text.
- Numbers above ten are written as digits: `42`, `1 250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Euro (EUR)
- Symbol: `euro` (the word) is preferred in Finnish text. The `EUR` ISO code is used in financial/technical contexts.
- **Symbol placement**: The euro symbol `EUR` is placed **after** the amount, separated by a space: `100,00 EUR`, `1 500,50 EUR`.
- In running text, use the word form: `100 euroa`, `1 500,50 euroa`.
- Note the partitive case for amounts: `euroa` (singular partitive), `euroa` (plural partitive — same form).
- The Finnish word `euro` inflects: `euron` (genitive), `eurona` (essive), `eurosta` (elative).

### 2.2 US Dollar
- Symbol: `$`.
- In Finnish texts, `$` is placed **after** the amount: `100,00 $`.
- Alternative (ISO code): `100,00 USD`.
- Word form in text: `dollari` (e.g., `100 dollaria`).

### 2.3 Other Currencies
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies: `100,00 GBP`, `100,00 JPY`, `100,00 CHF`.
- Translate currency names in running text: "pounds" → `punta`, "yen" → `jeni`.

### 2.4 Formatting Rules
- Decimal comma applies to all currency amounts: `100,00` (not `100.00`).
- Thousands space applies: `1 000,00 EUR` (not `1.000,00 EUR`).
- Use exactly two decimal places for financial amounts: `50,00 EUR` (not `50 EUR`).
- Maintain the original currency amounts; do NOT convert to EUR unless explicitly instructed.

---

## 3. Date and Time

### 3.1 Date Format
- Finnish date format: **DD.MM.YYYY** (day.month.year).
- The dot is the standard separator: `25.05.2026`.
- Leading zeros are used for single-digit days and months: `01.04.2026` (not `1.4.2026`).
- Alternative separators: hyphen `25-05-2026` or slash `25/05/2026` are less common but understood.

### 3.2 Month Names (Finnish)
- Month names are written in **lowercase** in Finnish (unlike English).

| English | Finnish | Abbreviation |
|---------|---------|-------------|
| January | tammikuuta | tammi |
| February | helmikuuta | helmi |
| March | maaliskuuta | maalis |
| April | huhtikuuta | huhti |
| May | toukokuuta | touko |
| June | kesäkuuta | kesä |
| July | heinäkuuta | heinä |
| August | elokuuta | elo |
| September | syyskuuta | syys |
| October | lokakuuta | loka |
| November | marraskuuta | marras |
| December | joulukuuta | joulu |

- Day-month-year with month name: `25. toukokuuta 2026`.
- Note: Finnish uses the **partitive** form of month names in dates (`tammikuuta`, not `tammikuu`).
- Centuries: `1800-luku` (19th century), `2000-luku` (21st century).

### 3.3 Day Names (Finnish)
- Written in lowercase: `maanantai`, `tiistai`, `keskiviikko`, `torstai`, `perjantai`, `lauantai`, `sunnuntai`.
- Abbreviations: `ma`, `ti`, `ke`, `to`, `pe`, `la`, `su`.

### 3.4 Time Format
- **24-hour format** is standard: `14.30` (Finnish uses a **dot**, not colon, between hours and minutes).
- Hours and minutes are separated by a dot: `09.15`, `23.45`.
- Seconds, when included: `14.30.25`.
- Leading zero for hours: `08.00` (not `8.00`).
- AM/PM notation is NOT used in Finnish.
- The prefix `klo` (lyhenne sanasta "kello") is used: `klo 15.30` (at 15:30).

### 3.5 Combined Date and Time
- Date and time are separated by a space or the word `klo`:
  - `25.05.2026 klo 14.30`
  - `25.5.2026 klo 14.30`
- The word `klo` is standard in schedules, timetables, and formal contexts.

### 3.6 Weeks and Days
- "Week 12" → `viikko 12` (or `vko 12`).
- "Day 5" → `päivä 5`.
- ISO week numbering may be used in technical contexts: `2026-W22`.

### 3.7 Time Zones
- Finnish time zone is EET (UTC+2) / EEST (UTC+3 in summer).
- Finnish time zone abbreviation: `HAI` (Helsingin aika / Helsinki time) or `EET`/`EEST`.

---

## 4. Addresses

### 4.1 Finnish Address Format
Finnish addresses flow from **smallest to largest** unit:

1. **Katu** (street) with name and number.
2. **Postinumero** (postal code — 5 digits).
3. **Postitoimipaikka** (post office town/city).

Example: `Mannerheimintie 1, 00100 Helsinki`

### 4.2 Address Components

| English | Finnish | Abbreviation |
|---------|---------|-------------|
| Street | katu | katu / ktu |
| Road | tie | tie |
| Avenue | bulevaari | bulev. |
| Alley | kuja | kja |
| Highway | valtatie | vt. |
| District | kaupunginosa | — |
| Municipality | kunta | — |
| Postal code | postinumero | p.nro / pnro |
| P.O. Box | postilokero | p.l. |

### 4.3 Foreign Addresses in Finnish Texts
- Foreign addresses should generally be **preserved in their original form**.
- Address labels may optionally be translated for comprehension.
- Country names ARE translated into Finnish (e.g., `Saksa` for Germany, `Ranska` for France).

---

## 5. Proper Nouns

### 5.1 Finnish Special Characters
Finnish uses the following special characters:

| Upper | Lower | Example |
|-------|-------|---------|
| A | a | — |
| A with ring | a with ring | Aalto, mäki |
| A with diaeresis | a with diaeresis | — |
| O with diaeresis | o with diaeresis | Järvi, öljy |
| A with umlaut | a with umlaut | — |

- Finnish has `ä` and `ö` as **separate letters** (not variants of `a` and `o`).
- `ä` sorts after `z` in the Finnish alphabet; `ö` sorts after `ä`.
- Incorrect substitution of `a` for `ä` or `o` for `ö` changes word meaning (e.g., `kato` = disappearance vs. `katto` = roof).

### 5.2 Capitalization Rules
- Proper nouns are capitalized: `Helsinki`, `Suomi`, `Mannerheim`.
- Geographic names: `Suomi`, `Pohjola`, `Jäämeri`.
- Institutions: `Suomen Pankki`, `Helsingin Yliopisto`.
- Language names ARE capitalized in Finnish: `suomi`, `englanti`, `ruotsi` (lowercase is standard).
- Days and months are lowercase: `maanantai`, `tammikuu`.

### 5.3 Company and Brand Names
- Company and brand names are **preserved in their original form**.
- Legal suffixes may be translated to Finnish equivalents:
  - `Inc.` → `Oy` (Osakeyhtiö — limited company).
  - `Ltd.` → `Oy`.
  - `GmbH` → `Oy` (approximate equivalent).
  - `Ab` (Swedish) → `Oy` (Finnish equivalent).
- Finnish company types:
  - `Oy` (Osakeyhtiö) — Limited company.
  - `Oyj` (Julkinen osakeyhtiö) — Public limited company.
  - `Tmi` (Toiminimi) — Sole proprietorship.
  - `Ay` (Avoin yhtiö) — General partnership.
  - `Ky` (Kommandiittiyhtiö) — Limited partnership.

### 5.4 Geographic Name Translation
- Finnish has established forms for many foreign geographic names:
  - `Germany` → `Saksa`.
  - `France` → `Ranska`.
  - `Sweden` → `Ruotsi`.
  - `Russia` → `Venäjä`.
  - `London` → `Lontoo`.
  - `Paris` → `Pariisi`.
  - `Rome` → `Rooma`.
  - `Moscow` → `Moskova`.
  - `United States` → `Yhdysvallat` (pl. `Yhdysvallat`).
  - `United Kingdom` → `Yhdistynyt kuningaskunta`.

---

## 6. Grammar Overview

### 6.1 Sentence Structure (SVO)
Finnish is a **Subject-Object-Verb** (SVO) language, like English. However, word order is more flexible than in English due to the case system:
- Neutral: `Mies lukee kirjaa.` (The man reads a book.)
- Emphatic object: `Kirjaa mies lukee.` (It is the book that the man reads.)

**Translation implication**: SVO is the default, but emphasis and topicalization can shift word order. Maintain natural Finnish word order rather than slavishly following English order.

### 6.2 Agglutinative Nature
Finnish is an **agglutinative** language — suffixes are appended to root words to express grammatical relationships:
- `talo` (house) → `taloja` (houses) → `taloni` (my house) → `talossani` (in my house) → `talostani` (from my house).
- A single Finnish word can correspond to an entire English phrase.
- Suffixes follow a strict order: stem + plural + possessive + case.

### 6.3 Vowel Harmony
Finnish has **vowel harmony** for certain suffixes: back vowels (a, o, u) and front vowels (ä, ö, y) do not mix within a word:
- `-ssa/-ssä` (inessive): `talossa` (in the house), `mäessä` (on the hill).
- `-sta/-stä` (elative): `talosta` (from the house), `mäestä` (from the hill).
- `-n/-n` (genitive): vowel harmony applies to other suffixes, not the genitive `-n`.

### 6.4 Noun Cases
Finnish has **15 grammatical cases** (compared to English's 3). Key cases:

| Case | Suffix | Example | Meaning |
|------|--------|---------|---------|
| Nominative | (none) | talo | house (subject) |
| Genitive | -n | talon | of the house |
| Partitive | -ta/-a/-tä/-ä | taloa | house (partial object) |
| Inessive | -ssa/-ssä | talossa | in the house |
| Elative | -sta/-stä | talosta | from the house |
| Illative | -Vn / -seen | taloon | into the house |
| Adessive | -lla/-llä | talolla | at/on the house |
| Ablative | -lta/-ltä | talolta | from the house |
| Allative | -lle | talolle | to/on the house |
| Essive | -na/-nä | talona | as a house |
| Translative | -ksi | taloksi | becoming a house |
| Comitative | -ne- | taloine(n) | with (one's) houses |
| Abessive | -tta/-ttä | talotta | without a house |

### 6.5 No Grammatical Gender
Finnish has **no grammatical gender**. The pronoun `hän` covers he/she/it:
- `Hän on opettaja.` (He/She is a teacher.)
- There is no distinction between masculine and feminine in nouns, adjectives, or pronouns.
- Translation implication: When translating from a gendered language, gender must be inferred from context or left ambiguous. If gender is critical, use `hämies` (he-man) or `hanainen` (she-woman) or explicit nouns.

### 6.6 No Articles
Finnish has **no articles** (no equivalent of "a" or "the"):
- `Talo on suuri.` (The house is big. / A house is big. — context determines.)
- Definiteness is expressed through context, word order, and the use of the genitive case.

### 6.7 Formality
Finnish distinguishes **Te** (formal you, pl.) and **sinä** (informal you, sg.):
- `Te` is used in formal correspondence, with strangers, and in professional settings.
- `sinä` is used with friends, family, children, and close colleagues.
- Finnish is generally **less formal** than many other European languages; the `sinä` form is widely used even in semi-professional contexts.
- The choice of register should match the source document's tone.

### 6.8 Postpositions
Finnish uses **postpositions** (not prepositions) with the genitive case:
- `Talon edessä` (in front of the house) — literally "house's front-inessive."
- `Pöydän päällä` (on top of the table).
- Some postpositions take the adessive case: `luona` (near), `kanssa` (with).

### 6.9 Verb Conjugation
Finnish verbs conjugate for person, number, tense, and mood:
- Present: `minä puhun` (I speak), `sinä puhut` (you speak), `hän puhuu` (he/she speaks).
- Past: `minä puhuin`, `sinä puhuit`, `hän puhui`.
- Negative: `minä en puhu`, `sinä et puhu`, `hän ei puhu`.
- The negative verb `ei` is a separate word, unlike the English auxiliary "do not."

---

## 7. Punctuation

### 7.1 Comma (,)
- Used to separate items in a list: `omena, banaani ja oranges`.
- The serial (Oxford) comma is NOT used in Finnish.
- Used before conjunctions when joining independent clauses.
- NOT used before `että` (that) in most cases where English uses a comma before "that."

### 7.2 Quotation Marks
- Primary quotation: `"..."` (same as English).
- Alternative: `»...»` (Finnish guillemets) in formal/academic texts.
- Single quotation marks: `'...'` for quotes within quotes.

### 7.3 Other Punctuation
- Period, semicolon, colon, question mark, exclamation mark: same usage as English.
- Hyphen (-): used in compound words (`kansainvälinen`), line breaks, and number ranges.
- En dash (–): used for number ranges in formal typography.
- Em dash (—): used for parenthetical interruptions.
- No double punctuation: never combine `,.`, `!?`, etc.

---

## 8. Translation Philosophy

### 8.1 Natural Finnish
The primary goal is to produce **natural-sounding Finnish** that reads as if it were originally written in Finnish.

**Principles:**
- Avoid calques (direct structural borrowings from the source language).
- Use idiomatic Finnish expressions where they convey the same meaning.
- Prefer Finnish vocabulary over borrowed/foreign words where a well-established Finnish equivalent exists.
- Finnish has a rich tradition of language cultivation (`kielenhuolto`); consult established usage.

### 8.2 Vocabulary Preference
- Use the word that a Finnish reader would most naturally encounter in the given context.
- Finnish-derived terms are preferred where well-established equivalents exist:
  - `tietokone` (computer) over `datamaskiin`.
  - `sähköposti` (email) over `email` (though both are used).
  - `puhelin` (phone) over `telefoni`.
- Some loanwords are fully integrated: `bussi`, `hotelli`, `taksi`.

### 8.3 Untranslatable Elements
- Brand names and product names remain in their original form.
- Foreign titles may remain when referring to foreign individuals in foreign contexts.
- Acronyms: preserve original but provide Finnish expansion on first use if helpful.

---

*End of Finnish Translation Base Rules. These rules should be read in conjunction with the scoring rubric and any project-specific guidelines provided.*
