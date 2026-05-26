---
id: ms/rules/base
type: rules
target_lang: ms
name: Malay Translation Base Rules
description: Malay base translation rules
---

# Malay Translation Base Rules

This document defines the foundational rules for translating documents into Malay (Bahasa Melayu / Bahasa Malaysia). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **dot** (titik) is used in Malay as the decimal separator: `3.14` (not `3,14`).
- Decimal places are separated by a dot with **no space** before or after: `0.25`, `12.5`, `100.99`.
- Trailing zeros after the decimal dot are preserved when they carry significance: `5.00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **comma** (koma) is used as the thousands separator: `1,000`, `25,000`, `1,000,000`.
- Do NOT use dot, space, or apostrophe as thousands separator in running text.
- Four-digit numbers may optionally omit the comma: `1000` is acceptable, `1,000` is preferred in formal/financial contexts.
- No thousands separator is used after the decimal dot: `1,000.50`.

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3.14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1,000.00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a non-breaking space: `50 %`.
- Alternatively, the word `peratus` is used in formal/literary text: `50 peratus`.
- Choose one form and maintain consistency throughout the document.
- Percentage ranges: `10 % - 20 %` or `10 peratus hingga 20 peratus`.

### 1.5 Ordinal Numbers
- Ordinal numbers in Malay use the prefix `ke-`: `pertama` (1st), `kedua` (2nd), `ketiga` (3rd).
- In numeric form: `ke-1`, `ke-2`, `ke-3` (no period after the numeral).
- Example: `ke-20 abad` (20th century), `Perkara ke-3` (Article 3), `kedudukan ke-5` (5th place).

### 1.6 Fractions
- Fractions are written as decimal numbers or with a slash: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).
- In Malay, fractions commonly use the word `per`: `satu per dua` (1/2), `tiga per empat` (3/4).

### 1.7 Numerals in Text
- Numbers from one to ten are typically written as words in running text: `satu`, `dua`, `tiga`, `empat`, `lima`, `enam`, `tujuh`, `lapan`, `sembilan`, `sepuluh`.
- Numbers above ten are written as digits: `42`, `1,250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Malaysian Ringgit (MYR/RM)
- Symbol: `RM`.
- **Symbol placement**: The currency symbol is placed **before** the amount, no space: `RM100.00`, `RM1,500.50`.
- ISO code may be used in technical/financial contexts: `MYR 100.00`.
- RM is the standard abbreviation used in all Malaysian contexts.

### 2.2 US Dollar
- Symbol: `$`.
- **Symbol placement**: `$` is placed **before** the amount: `$100.00`.
- Alternative (ISO code): `USD 100.00`.

### 2.3 Euro
- Symbol: `€`.
- **Symbol placement**: `€` is placed **before** the amount: `€100.00`.
- Alternative (ISO code): `EUR 100.00`.

### 2.4 Other Currencies
- Follow the same pattern: currency symbol before the amount.
- Use ISO 4217 codes for less common currencies: `GBP 100.00`, `JPY 100.00`, `SGD 100.00`.

### 2.5 Currency Translation Rules
- Translate currency names in running text: "dollars" → `dolar`, "euros" → `euro`.
- "cents" → `sen`, "pence" → `pens`.
- Maintain the original currency amounts; do NOT convert to Ringgit unless explicitly instructed.
- In Malaysian context, "Ringgit" or "RM" is the standard term for the local currency.

### 2.6 Formatting Rules
- Decimal dot applies to all currency amounts: `100.00` (not `100,00`).
- Thousands comma applies: `1,000.00 RM` → `RM1,000.00`.
- Use exactly two decimal places for financial amounts: `RM50.00` (not `RM50`).

---

## 3. Date and Time

### 3.1 Date Format
- Malaysian date format: **DD/MM/YYYY** (day/month/year) is the most common.
- Alternative ISO format: **YYYY-MM-DD** (used in technical/formal documents).
- The slash or hyphen is the standard separator: `27/05/2026` or `2026-05-27`.
- Leading zeros are used for single-digit days and months: `01/04/2026` (not `1/4/2026`).

### 3.2 Month Names (Malay)

| English | Malay | Abbreviation |
|---------|-------|-------------|
| January | Januari | Jan |
| February | Februari | Feb |
| March | Mac | Mac |
| April | April | Apr |
| May | Mei | Mei |
| June | Jun | Jun |
| July | Julai | Jul |
| August | Ogos | Ogo |
| September | September | Sep |
| October | Oktober | Okt |
| November | November | Nov |
| December | Disember | Dis |

- Day-month-year with month name: `27 Mei 2026` (no comma between components).
- Capitalize the first letter of the month name.

### 3.3 Day Names (Malay)

| English | Malay | Abbreviation |
|---------|-------|-------------|
| Monday | Isnin | Is |
| Tuesday | Selasa | Se |
| Wednesday | Rabu | Ra |
| Thursday | Khamis | Kh |
| Friday | Jumaat | Jm |
| Saturday | Sabtu | Sb |
| Sunday | Ahad | Ah |

### 3.4 Time Format
- **24-hour format** is standard in formal/official contexts: `14:30` (not `2:30 PTG`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours: `08:00` (not `8:00`).
- **12-hour format** with time-of-day markers is acceptable in informal contexts:

| Malay Marker | Abbreviation | Meaning |
|---|---|---|
| pagi | PG | morning (dawn to noon) |
| tengah hari | TH | midday (around noon) |
| petang | PTG | afternoon (noon to sunset) |
| malam | MLM | evening/night (sunset onward) |

- Examples: `2:30 petang` (2:30 PM), `8:00 malam` (8:00 PM), `9:00 pagi` (9:00 AM).

### 3.5 Combined Date and Time
- Date and time are separated by a space:
  - `27/05/2026 14:30`
  - `27 Mei 2026, jam 14:30` (formal)
- The word `jam` (hour/o'clock) is used when reading time aloud or in formal prose.

### 3.6 Time Zones
- Malaysian time zone is MYT (UTC+8), also known as Waktu Piawai Malaysia.
- Time zone abbreviation in Malay may use `WPM` or simply `MYT`.
- Preserve original time zone designations in translated documents unless localizing.

---

## 4. Formality and Register

### 4.1 Bahasa Melayu vs Bahasa Malaysia

| Aspect | Bahasa Melayu | Bahasa Malaysia |
|---|---|---|
| Usage context | Brunei, Indonesia (related but distinct), general Malay world | Malaysia specifically |
| Vocabulary preference | May use more Arabic-derived words | May use more English loanwords |
| Official status | Standard Malay used in Malaysia's constitution | The term used in Malaysian education and media |
| Recommendation | Use Bahasa Malaysia conventions for Malaysian documents | Preferred for documents targeting Malaysian readers |

**Critical rule**: For documents targeting a Malaysian audience, use **Bahasa Malaysia** conventions. This means accepting certain English loanwords that are standard in Malaysian Malay (e.g., `komputer`, `internet`, `telefon`) rather than insisting on purely Malay-origin alternatives.

### 4.2 Formal Register (Bahasa Baku)

Formal Malay (Bahasa Baku) is used for:
- Government correspondence and official documents
- Legal documents and contracts
- Academic writing and research
- Formal business correspondence
- News media (print and broadcast)

Formal register characteristics:
- Standard grammar and vocabulary per Dewan Bahasa dan Pustaka (DBP) guidelines
- No contractions or colloquial expressions
- Use of passive voice (`di-` prefix) in formal/official contexts
- Use of `akan` for future tense in formal commitments
- Avoidance of unnecessary English loanwords where Malay equivalents exist

### 4.3 Informal Register (Bahasa Pasar / Bahasa Harian)

Informal Malay is used for:
- Casual conversation
- Social media posts
- Marketing aimed at youth audiences
- Internal team communications

Informal register characteristics:
- Use of colloquial contractions (e.g., `nak` instead of `ingin`, `tak` instead of `tidak`)
- Code-switching with English (Manglish) is common and acceptable in informal context
- Simplified sentence structures
- Use of `aku/kau` or `saya/awak` instead of formal pronouns

### 4.4 Address Terms

| Malay (Formal) | Malay (Informal) | English | Usage |
|---|---|---|---|
| Tuan | Bos/Bro | Sir/Mr. | Male addressee |
| Puan | Kak/Cik | Madam/Ms. | Female addressee |
| Encik | Bang | Mr. | Male (informal-formal) |
| Cik | Kak | Miss | Young female |
| Dato'/Datin | — | Title (Malaysian honorific) | State/federal title holder |
| Tan Sri/Puan Sri | — | Title | High-ranking national title |
| Yang Berhormat | — | The Honorable | Elected representative |

### 4.5 Formal Correspondence

| English | Malay (Formal) |
|---|---|
| Dear Sir/Madam | Tuan/Puan yang dihormati |
| Dear Mr. Ahmad | Tuan Ahmad yang dihormati / Encik Ahmad |
| Dear Mrs. Siti | Puan Siti yang dihormati |
| To whom it may concern | Kepada sesiapa yang berkenaan |
| Yours faithfully | Yang benar |
| Best regards | Salam hormat / Dengan ini |
| Sincerely | Dengan ikhlas |
| Thank you | Terima kasih / Dengan ini saya mengucapkan terima kasih |

---

## 5. Punctuation

### 5.1 General Punctuation Rules
- Malay punctuation largely follows English conventions.
- Single space after periods, colons, and semicolons (not double space).
- No space before punctuation marks (comma, period, question mark, exclamation).

### 5.2 Quotation Marks
- Primary quotation: `"..."` (double quotes, same as English).
- Single quotation marks: `'...'` for quotes within quotes.
- In formal/academic Malay, guillemets `«...»` are sometimes used.
- The closing quotation mark is placed AFTER the sentence-ending punctuation, consistent with English conventions.

### 5.3 Apostrophe
- The apostrophe is used for:
  - Possessive: `Ahmad's book` → `buku Ahmad` (Malay does NOT use possessive apostrophe; possession is shown through word order).
  - Elision in informal text: `nak` (want to), `tak` (not).
  - Foreign proper nouns with apostrophes: preserve as-is.

### 5.4 Hyphen (-) and Dash (—)
- Hyphen: used in compound words (`bahasa Inggeris` — no hyphen typically, but technical compounds may use one), line breaks, and number ranges (`10-15`).
- En dash (–): used for number ranges in formal typography (`10–15`).
- Em dash (—): used for parenthetical interruptions in sentences.

### 5.5 Question Mark and Exclamation Mark
- Usage is the same as English.
- Malay uses the question particle `kah` (formal) or `tak` (informal) in questions.
- Multiple question/exclamation marks (`???`, `!!!`) are informal and should NOT appear in formal translations.

---

## 6. Proper Nouns

### 6.1 Malay Alphabet
Malay uses the Latin alphabet with the following additional characters:

| Character | Name | Example |
|---|---|---|
| Ë/ë | e with diaeresis | Perak (not used in modern Malay) |

Modern standard Malay uses the 26 basic Latin letters. The special characters ç, ñ, etc. are NOT part of the standard Malay alphabet.

### 6.2 Capitalization Rules
- Proper nouns are capitalized: `Ahmad`, `Malaysia`, `Kuala Lumpur`.
- Titles preceding names are capitalized: `Tuan Ahmad`, `Dato' Seri Anwar Ibrahim`.
- Geographic names: `Sungai Klang`, `Pulau Pinang`, `Gunung Kinabalu`.
- Institutions: `Universiti Malaya`, `Dewan Bahasa dan Pustaka`, `Bank Negara Malaysia`.
- Language names are NOT capitalized in Malay (unlike English):
  - `bahasa Melayu` (not `Bahasa Melayu` unless at start of sentence)
  - `bahasa Inggeris`
  - `bahasa Cina`
- Days of the week and months are NOT capitalized (unless at start of sentence).

### 6.3 Foreign Name Transcription
- Foreign personal names are generally **preserved in their original spelling**.
- Common/historical names may follow established Malay forms.
- Established Malay forms for well-known names/places:

| English | Malay |
|---|---|
| Washington | Washington (preserved) |
| London | London (preserved) |
| Beijing | Beijing / Peking |
| Tokyo | Tokyo |
| Germany | Jerman |
| France | Perancis |
| Japan | Jepun |
| China | China / Republik Rakyat China |
| United States | Amerika Syarikat |
| United Kingdom | United Kingdom / Britain Raya |
| Saudi Arabia | Arab Saudi |

### 6.4 Company and Brand Names
- Company and brand names are **preserved in their original form**.
- Malaysian legal entity suffixes:

| Abbreviation | Full Form | Meaning |
|---|---|---|
| Sdn Bhd | Sendirian Berhad | Private Limited |
| Bhd | Berhad | Public Limited |
| Sdn | Sendirian | Private (without Berhad) |
| P.L.C. | Public Listed Company | Public Listed Company |
| P.B. | Permodalan Berahad | Investment holding |
| Koperasi | — | Cooperative |

- Do NOT translate the legal entity suffix in formal documents; keep `Sdn Bhd` as-is.
- Translate surrounding text (e.g., "the company" → `syarikat tersebut`).

### 6.5 Geographic Name Translation

| English | Malay |
|---|---|
| Strait of Malacca | Selat Melaka |
| South China Sea | Laut China Selatan |
| Indian Ocean | Lautan Hindi |
| Pacific Ocean | Lautan Pasifik |
| Mount Everest | Gunung Everest |
| River | Sungai (Sg.) |
| Lake | Tasik / Danau |
| Island | Pulau (P.) |

---

## 7. Formatting

### 7.1 Title Capitalization
- In Malay, **sentence case** is preferred for titles: `Pengenalan kepada sistem pengurusan`.
- Only the first word and proper nouns are capitalized.
- ALL CAPS may be used for very short titles or headings in specific contexts.
- Do NOT use Title Case (each major word capitalized) — this is an English convention.

### 7.2 Headings and Subheadings
- Heading hierarchy should be clear and consistent.
- Use sentence case for headings.
- No period at the end of headings.
- Subheadings follow the same rule.

### 7.3 Lists

**Bulleted Lists:**
- Each item starts with a lowercase letter (unless it is a complete sentence or proper noun).
- Items that are complete sentences end with a period.
- Items that are phrases do NOT end with punctuation.

**Numbered Lists:**
- Use numeric format: `1.`, `2.`, `3.` (with period).
- Or use parentheses: `a)`, `b)`, `c)` for secondary lists.
- Or use Roman numerals: `i)`, `ii)`, `iii)` for sub-sections.

### 7.4 Tables
- Column headers should be clear and concise.
- Alignment: text is left-aligned, numbers are right-aligned.
- Currency amounts in table columns should align on the decimal point.
- Use consistent formatting within a column.

### 7.5 Bold and Italic
- Bold: used for headings, key terms, and emphasis.
- Italic: used for foreign words, book/movie titles, and emphasis.
- Malay titles of works are italicized (e.g., *Seni Bina Melayu*).

### 7.6 Spacing
- Single space after periods, colons, and semicolons.
- No space before punctuation marks.
- One space before opening parentheses and after closing parentheses when embedded in text.
- **Malay does NOT use a space between the currency symbol and the amount**: `RM100.00` (not `RM 100.00`).

---

## 8. Grammar Notes for Translators

### 8.1 Sentence Structure (SVO)
Malay is a **Subject-Verb-Object** (SVO) language, similar to English.

- English: `The cat eats the fish.`
- Malay: `Kucing itu makan ikan itu.`

**Translation implication**: Basic word order is similar to English. However, Malay frequently uses passive constructions and topic-fronted structures.

### 8.2 Affixation System
Malay builds words through prefixes, suffixes, infixes, and circumfixes:

| Affix Type | Example | Result |
|---|---|---|
| Prefix `meN-` | tulis → menulis | to write (active) |
| Prefix `di-` | tulis → ditulis | to be written (passive) |
| Suffix `-kan` | tulis → menulis (transitive) | to write (causative) |
| Suffix `-i` | tulis → menulis (locative) | to write at/on |
| Circumfix `meN-...-kan` | jual → menjual | to sell |
| Circumfix `peN-...-an` | tulis → penulisan | writing (noun) |

### 8.3 Passive Voice
Malay uses passive voice extensively in formal/official contexts:
- Active: `Kami akan mengadakan mesyuarat.` (We will hold a meeting.)
- Passive (formal): `Mesyuarat akan diadakan.` (The meeting will be held.)
- In formal Malay, the `di-` passive is preferred for official documents.

### 8.4 No Grammatical Gender
Malay has **no grammatical gender**. The pronoun `dia` covers he/she.
- Translation implication: When translating from a gendered language, gender must be inferred from context.
- If gender is critical, use explicit nouns: `lelaki` (male), `perempuan` (female), `bapa` (father), `ibu` (mother).

### 8.5 Articles and Demonstratives
- Malay has no definite article ("the") or indefinite article ("a/an").
- Definiteness is expressed through demonstratives: `itu` (that/the), `ini` (this).
- `Yang` functions as a relative pronoun: `orang yang baik` (the person who is good).

### 8.6 Loanwords
- Malay freely borrows from Arabic, Sanskrit, Portuguese, Dutch, English, and Chinese.
- For Malaysian documents (Bahasa Malaysia), common English loanwords are accepted:
  - `komputer`, `internet`, `telefon`, `e-mel`, `aplikasi`
- For formal/pure Malay contexts, prefer Malay-origin terms where they exist:
  - `pengkomputeran` (computing), `rangkaian` (network), `turapan` (paving)

---

*End of Malay Translation Base Rules. These rules should be read in conjunction with the scoring rubric and any project-specific guidelines provided.*
