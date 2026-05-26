---
id: tr/rules/base
type: rules
target_lang: tr
name: Turkish Translation Base Rules
description: Turkish base translation rules
---

# Turkish Translation Base Rules

This document defines the foundational rules for translating documents into Turkish. All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **decimal comma** (virgül) is used in Turkish: `3,14` (not `3.14`).
- Decimal places are separated by a comma with **no space** before or after: `0,25`, `12,5`, `100,99`.
- Trailing zeros after the decimal comma are preserved when they carry significance: `5,00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **period** (nokta) is used as the thousands separator: `1.000`, `25.000`, `1.000.000`.
- Do NOT use comma, space, or apostrophe as thousands separator: `1,000` is WRONG.
- Four-digit numbers may optionally omit the period: `1000` is acceptable, `1.000` is preferred.
- No thousands separator is used after the decimal comma: `1.000,50` (not `1.000,50` — this is actually correct; the period groups thousands, comma separates decimals).

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3,14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1.000,00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a non-breaking space: `%25` or `% 25`.
- Both forms are acceptable in modern Turkish, but `%25` (no space) is more common in technical/financial texts.
- Choose one form and maintain consistency throughout the document.
- Percentage ranges: `%10-%20` or `%10 ila %20`.

### 1.5 Ordinal Numbers
- Ordinal numbers in Turkish use a period after the numeral: `1.` (birinci), `2.` (ikinci), `3.` (üçüncü).
- Example: `20. yüzyıl` (20th century), `3. madde` (article 3), `5. sırada` (in 5th place).
- The period is NOT a full stop; it is a ordinal suffix marker.

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).

### 1.7 Numerals in Text
- Numbers from zero to nine (or up to ten, depending on context) are typically written as words in running text: `üç`, `yedi`, `on`.
- Numbers above nine are written as digits: `42`, `1.250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

---

## 2. Currency

### 2.1 Turkish Lira (TRY/₺)
- Symbol: `₺` (TL is also accepted, but `₺` is preferred in modern usage).
- **Symbol placement**: The currency symbol is placed **after** the amount, separated by a space: `100,00 ₺`, `1.500,50 ₺`.
- ISO code may be used in technical/financial contexts: `100,00 TRY`.
- NEVER place the ₺ symbol before the amount (`₺100,00` is WRONG).

### 2.2 US Dollar
- Symbol: `$`.
- **Symbol placement**: `$` is placed **after** the amount, separated by a space: `100,00 $`.
- Alternative (ISO code): `100,00 USD`.
- In Turkish texts, `$` after the amount is preferred to maintain visual consistency with `₺`.

### 2.3 Euro
- Symbol: `€`.
- **Symbol placement**: `€` is placed **after** the amount, separated by a space: `100,00 €`.
- Alternative (ISO code): `100,00 EUR`.

### 2.4 Other Currencies
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies: `100,00 GBP`, `100,00 JPY`, `100,00 CHF`.

### 2.5 Currency Translation Rules
- Translate currency names in running text: "dollars" → `dolar`, "euros" → `avro/euro`.
- `avro` is the official TDK-recommended term for euro, though `euro` is widely used in practice.
- `dolar` (not dolar) — the circumflex is sometimes used (`dolar`) but standard spelling is `dolar`.
- "pence" → `peni`, "cents" → `sent`.
- Maintain the original currency amounts; do NOT convert to Turkish Lira unless explicitly instructed.

### 2.6 Formatting Rules
- Decimal comma applies to all currency amounts: `100,00` (not `100.00`).
- Thousands period applies: `1.000,00 ₺` (not `1000,00 ₺`).
- Use exactly two decimal places for financial amounts: `50,00 ₺` (not `50 ₺`).

---

## 3. Date and Time

### 3.1 Date Format
- Turkish date format: **DD.MM.YYYY** (day.month.year).
- The dot is the standard separator: `25.05.2026`.
- Alternative separator (less common): hyphen `25-05-2026` or slash `25/05/2026`. But the dot is preferred.
- Leading zeros are used for single-digit days and months: `01.04.2026` (not `1.4.2026`).

### 3.2 Month Names (Turkish)
- Months are written in **lowercase** in Turkish (unlike English).
- Turkish month names:

| English | Turkish | Abbreviation |
|---------|---------|-------------|
| January | ocak | Oca |
| February | şubat | Şub |
| March | mart | Mar |
| April | nisan | Nis |
| May | mayıs | May |
| June | haziran | Haz |
| July | temmuz | Tem |
| August | ağustos | Ağu |
| September | eylül | Eyl |
| October | ekim | Eki |
| November | kasım | Kas |
| December | aralık | Ara |

- Day-month-year with month name: `25 mayıs 2026` (no comma between components).
- Preposition "on" before dates is not translated; Turkish does not use a preposition.
- Centuries: `20. yüzyıl`, `21. yüzyıl`.

### 3.3 Day Names (Turkish)
- Written in lowercase: `pazartesi`, `salı`, `çarşamba`, `perşembe`, `cuma`, `cumartesi`, `pazar`.
- Abbreviations: `Pzt`, `Sal`, `Çar`, `Per`, `Cum`, `Cmt`, `Paz`.

### 3.4 Time Format
- **24-hour format** is mandatory: `14:30` (not `2:30 PM`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours: `08:00` (not `8:00`).
- AM/PM notation is NOT used in Turkish.

### 3.5 Combined Date and Time
- Date and time are separated by a space or "saat" (at/to):
  - `25.05.2026 14:30`
  - `25 mayıs 2026 saat 14:30` (formal/literary)
- The word `saat` (hour/o'clock) is used when reading time aloud or in formal prose.

### 3.6 Weeks and Days
- "Week 12" → `12. hafta` (ordinal period).
- "Day 5" → `5. gün`.
- ISO week numbering may be used in technical contexts: `2026-W22`.

### 3.7 Time Zones
- Turkish time zone is typically TRT (UTC+3), but preserve original time zone designations in translated documents unless localizing.
- Time zone abbreviations in Turkish may use `TSİ` (Türkiye Saati İle): `14:30 TSİ`.

---

## 4. Addresses

### 4.1 Turkish Address Format (Addresses within Turkey)
Turkish addresses flow from **smallest to largest** unit:

1. **Mahalle** (neighborhood) — may include `Mah.` abbreviation.
2. **Cadde/Sokak** (avenue/street) — `Cad.` or `Sok.`/`Sk.`.
3. **Numara/No** (building number and apartment/flat).
4. **İlçe** (district).
5. **İl** (province).
6. **Posta kodu** (postal code — 5 digits).

Example: `Atatürk Mah., Çiçek Sok. No:12/3, Kadıköy, İstanbul 34722`

### 4.2 Address Components

| English | Turkish | Abbreviation |
|---------|---------|-------------|
| Street | Sokak | Sok. / Sk. |
| Avenue | Cadde | Cad. |
| Boulevard | Bulvar | Bulv. |
| Alley | Çıkmazı | Çıkm. |
| Road | Yol | — |
| Highway | Otoyol | — |
| Neighborhood | Mahalle | Mah. |
| District | İlçe | — |
| Province | İl | — |
| Apartment/Flat | Daire | D. |
| Building No | Bina No | No |
| Postcode | Posta Kodu | PK |
| P.O. Box | Posta Kutusu | PK |

### 4.3 Foreign Addresses in Turkish Texts
- Foreign addresses should generally be **preserved in their original form** (not translated).
- Address labels like "Street", "Avenue" may optionally be translated for comprehension.
- Country names ARE translated into Turkish.

### 4.4 Address Prepositions
- Turkish does not use prepositions like "at" or "in" for addresses.
- Location is expressed through locative case suffix (`-de/-da/-te/-ta`): `İstanbul'da`, `Kadıköy'de`.
- Direction uses dative case (`-e/-a/-ye/-ya`): `Kadıköy'e`, `İstanbul'a`.

### 4.5 Postal Codes
- Turkish postal codes are 5 digits: `34000`, `34722`.
- Foreign postal codes are preserved as-is.

### 4.6 Address Translation Guidance
- When translating documents containing addresses, translate the surrounding text but preserve the address itself in its original language.
- Exception: If the entire document is being localized for a Turkish audience, addresses within Turkey may be formatted according to Turkish conventions.

---

## 5. Proper Nouns

### 5.1 Turkish Special Characters
Proper nouns in Turkish MUST use the Turkish alphabet's special characters correctly:

| Upper | Lower | Example |
|-------|-------|---------|
| Ç | ç | Çamlıca, çay |
| Ğ | ğ | Dağ, ağaç |
| İ | i (dotted) | İstanbul, Iskenderun (note: İstanbul with dotted İ) |
| I | ı (undotted) | Işık, ırmak |
| Ö | ö | Özge, göl |
| Ş | ş | Şişli, aşçı |
| Ü | ü | Üsküdar, gül |

- **Critical distinction**: `İ` (dotted capital I) and `I` (undotted capital I) are distinct letters.
  - Capital `İ` corresponds to lowercase `i`: `İstanbul` → `istanbul`.
  - Capital `I` corresponds to lowercase `ı`: `Işık` → `ışık`.
- Failure to use the correct dotted/undotted I is a **major error** (meaning change: `kar` = snow vs. `kâr` = profit, though the circumflex also plays a role here).

### 5.2 Foreign Name Transcription
- Foreign personal names are generally **preserved in their original spelling**.
- Common/historical names follow Turkish orthography: `Shakespeare` → `Shakespeare` (preserved), but historical figures may have established Turkish forms.
- Established Turkish forms for well-known names/places:
  - `Washington` → `Vaşington` (established form).
  - `Paris` → `Paris` (same spelling, different pronunciation).
  - `London` → `Londra`.
  - `Moscow` → `Moskova`.
  - `New York` → `New York` (preserved).
  - `Rome` → `Roma`.
  - `Athens` → `Atina`.
  - `Beijing` → `Pekin`.
  - `Germany` → `Almanya`.
  - `Greece` → `Yunanistan`.
- When in doubt, **preserve the original spelling** rather than inventing a Turkish transcription.

### 5.3 Capitalization Rules for Proper Nouns
- Proper nouns are capitalized: `Ahmet`, `Türkiye`, `Ankara`.
- Titles preceding names are capitalized: `Prof. Dr. Ahmet Yılmaz`, `Cumhurbaşkanı Recep Tayyip Erdoğan`.
- Geographic names: `Karadeniz`, `Ege Denizi`, `Toros Dağları`, `Nil Nehri`.
- Institutions: `Türkiye Büyük Millet Meclisi`, `İstanbul Üniversitesi`.
- Capitalization is NOT used for:
  - Days of the week (unless part of a proper name).
  - Months (unless part of a specific date or proper name).
  - Languages: `Türkçe`, `İngilizce`, `Fransızca` (ARE capitalized in Turkish — unlike English, language names are proper nouns).
  - Religions and their adherents: `Müslüman`, `Hristiyan`, `İslam`, `Hristiyanlık` (capitalized in Turkish).

### 5.4 Possessive Suffix with Proper Nouns
- The Turkish possessive suffix is attached to proper nouns with an **apostrophe (kesme işareti)**:
  - `Ahmet'in arabası` (Ahmet's car).
  - `İstanbul'un nüfusu` (Istanbul's population).
  - `Türkiye'nin başkenti` (Turkey's capital).
  - `Ankara'da` (in Ankara).
- This apostrophe is mandatory and **distinct from the English possessive apostrophe** — it is a grammatical marker in Turkish.

### 5.5 Company and Brand Names
- Company and brand names are **preserved in their original form**.
- Legal suffixes (Inc., Ltd., GmbH, A.Ş., Ltd. Şti.) may be translated to Turkish equivalents:
  - `Inc.` → `A.Ş.` (Anonim Şirket) for Turkish equivalents.
  - `Ltd.` → `Ltd. Şti.` (Limited Şirket).
  - `GmbH` → `Ltd. Şti.` (approximate equivalent).
- When in doubt, preserve the original legal form.

### 5.6 Geographic Name Translation
- Geographic features: translate common nouns, keep proper name.
  - `Sahara Desert` → `Sahra Çölü`.
  - `Atlantic Ocean` → `Atlas Okyanusu`.
  - `Himalaya Mountains` → `Himalaya Dağları`.
- Country names with established Turkish forms use those forms:
  - `United States` → `Amerika Birleşik Devletleri (ABD)`.
  - `United Kingdom` → `Birleşik Krallık`.
  - `United Arab Emirates` → `Birleşik Arap Emirlikleri`.

---

## 6. Punctuation

### 6.1 Turkish-Specific Punctuation Rules
Turkish punctuation follows Turkish Language Association (TDK) rules, which differ from English in several key respects.

### 6.2 Comma (,)
- Used to separate items in a list: `elma, armut, muz ve portakal`.
  - Turkish typically uses `ve` (and) before the last item, preceded by a comma (Oxford comma is NOT used in Turkish).
- Used before relative clauses and after introductory phrases.
- NOT used before `ki` in most cases (unlike English "that" clauses).
- NOT used to separate clauses in conditional sentences as freely as in English.
- Used after interjections and address forms: `Evet, haklısın.`, `Arkadaşlar, toplantı başlıyor.`

### 6.3 Semicolon (;)
- Used to separate closely related independent clauses (same as English).
- Used to separate items in a complex list where commas are already present.
- Usage is generally less frequent than in English.

### 6.4 Colon (:)
- Used to introduce a list, explanation, or quotation (same as English).
- The letter following a colon is NOT automatically capitalized (lowercase unless it begins a proper noun or independent quoted sentence).

### 6.5 Period (.)
- Used at the end of declarative sentences (same as English).
- Used after ordinal numbers (see Section 1.5).
- Used in abbreviations: `Prof.`, `Dr.`, `Cad.`, `Mah.`, `No.`
- NOT used after titles in isolation on business cards or letterheads in modern usage (varies by style guide).
- In URLs and email addresses, periods are NOT followed by a space.

### 6.6 No Double Punctuation
- Turkish does NOT use double punctuation. NEVER combine punctuation marks:
  - `"Geldim." dedi.` (correct: one period inside quotes is sufficient).
  - `"Nasılsın?" diye sordu.` (question mark inside quotes, no additional punctuation needed).
- Avoid sequences like `,!`, `?.`, `!,` — these are NOT valid in Turkish.

### 6.7 Quotation Marks (Tırnak İşareti)
- Primary quotation: Turkish uses `"..."` (same as English in most modern texts).
- Alternative/standard Turkish quotation marks: `«...»` (köşeli tırnak / French guillemets) — used in formal/academic Turkish texts.
- Single quotation marks: `'...'` for quotes within quotes.
- The closing quotation mark is placed AFTER the sentence-ending punctuation in Turkish (unlike English):
  - Turkish: `"Yarın gel."` (period inside quotes, as in English — this is the same in practice).
  - However, when quoting a sentence fragment, punctuation goes outside.
- Quotation marks in Turkish typography:
  - Opening: lower-double quotation mark „ (preferred in some formal Turkish typography).
  - Closing: upper-double quotation mark ".
  - In practice, straight quotes (" ") are widely accepted.

### 6.8 Apostrophe (Kesme İşareti) (')

The Turkish apostrophe is a **critical grammatical marker**. It is used for:

1. **Proper noun suffixes**: Separates proper nouns from inflectional suffixes:
   - `Ahmet'in` (Ahmet's), `İstanbul'da` (in Istanbul), `Ali'ye` (to Ali).
   - `Türkiye'nin`, `Ankara'ya`, `Ayşe'yle` (with Ayşe).

2. **Abbreviation suffixes**: `ABD'ye` (to the USA), `TBMM'nin` (of the parliament), `Prof.'un` (of the professor).

3. **Dates**: `2026'da` (in 2026), `25 Mayıs'ta` (on May 25).

4. **Letters/symbols**: `A'sı` (the A of it), `+'nın` (of the plus sign).

The apostrophe is NOT used:
- Before the possessive suffix `-ki`: `elimdeki` (not `elimde'ki`).
- Before the conjunction `-yle/-yla` on common nouns (but used with proper nouns).
- In compound words where the second word begins with a vowel: `İstanbul Üniversitesi` (not `İstanbul Üniversite'si`).

### 6.9 Hyphen (-) and Dash (—)
- Hyphen (-): used in compound words (`İngiliz-Türk ilişkileri`), line breaks, and number ranges (`10-15`).
- En dash (–): used for number ranges in formal typography (`10–15`), but a hyphen is acceptable.
- Em dash (—): used for parenthetical interruptions in sentences — different from English usage.
- No spaces around em dashes in Turkish.

### 6.10 Question Mark and Exclamation Mark
- Usage is the same as English.
- Question word order does not change; the question mark indicates interrogative force (Turkish uses the question particle `mi`).
- Multiple question/exclamation marks (`???`, `!!!`) are informal and should NOT appear in formal translations.

### 6.11 Ellipsis (...)
- Three dots with spaces around them or not, depending on style.
- Used for unfinished sentences or omissions.
- Four dots (....) when it coincides with the end of a sentence.

### 6.12 Slash (/)
- Used for alternatives (`ve/veya`), fractions (`1/2`), and dates (`25/05/2026` — though dot is preferred).
- No spaces around the slash.

### 6.13 Parentheses
- Usage is the same as English.
- Period placement: if the parenthetical is a complete sentence, the period goes inside; if a fragment, outside.

---

## 7. Formatting

### 7.1 Title Capitalization
- In Turkish, **only the first word** of a title is capitalized (sentence case) — this is the **most common and correct convention**.
- Proper nouns within titles remain capitalized.
- Example: `Savaş ve Barış` (War and Peace), `Bir İnsanı Tanımak` (To Know a Person).
- Exception: ALL CAPS may be used for very short titles or headings in specific contexts.
- Exception: Some formal/official document titles may use Title Case (each major word capitalized), but sentence case is preferred in modern Turkish.

### 7.2 Headings and Subheadings
- Heading hierarchy should be clear and consistent.
- Use sentence case for headings: `Bu bir başlıktır` (not `Bu Bir Başlıktır`).
- No period at the end of headings.
- Subheadings follow the same rule.

### 7.3 Lists

**Bulleted Lists:**
- Each item starts with a lowercase letter (unless it is a complete sentence or proper noun).
- Items that are complete sentences end with a period.
- Items that are phrases do NOT end with punctuation.

**Numbered Lists:**
- Use ordinal format for list markers: `1.`, `2.`, `3.` (with period).
- Or use parentheses: `a)`, `b)`, `c)` for secondary lists.

**Nested Lists:**
- Sub-items use different markers (dash, asterisk, or lowercase letters).
- Maintain parallel structure: if one item is a complete sentence, all items should be complete sentences.

### 7.4 Tables
- Column headers should be clear and concise.
- Alignment: text is left-aligned, numbers are right-aligned.
- Currency amounts in table columns should align on the decimal point.
- Use consistent formatting within a column (all dates same format, all numbers same decimal places).
- Table titles should be in sentence case.

### 7.5 Bold and Italic
- Bold: used for headings, key terms, and emphasis.
- Italic: used for foreign words, book/movie titles, and emphasis.
- Turkish uses italic for book titles (not quotation marks, which is common in English).

### 7.6 Spacing
- Single space after periods, colons, and semicolons (not double space).
- No space before punctuation marks (comma, period, question mark, exclamation).
- One space before opening parentheses and after closing parentheses when embedded in text.

### 7.7 Paragraphs
- Paragraphs should be coherent units of thought.
- First-line indent: optional, but if used, should be consistent throughout.
- Block paragraphs (no indent, space between paragraphs) are common in modern Turkish business writing.

### 7.8 Line Breaks and Page Breaks
- Preserve original line and page breaks where structurally meaningful.
- Do not hyphenate words across pages unnecessarily.
- In tables, avoid breaking rows across pages.

### 7.9 Abbreviations
- Common Turkish abbreviations:
  - `vb.` (ve benzeri — etc.), `vd.` (ve diğerleri — et al.).
  - `örn.` (örneğin — e.g.), `yani` (i.e. — no standard abbreviation, use full word).
  - `bkz.` (bakınız — cf./see).
  - `No` or `no` (numara — number).
  - `s.` (sayfa — page), `ss.` (sayfalar — pages).
- Abbreviations take a period after each abbreviated segment: `ABD` (no periods for acronyms), `Prof. Dr.` (periods after each).
- SI unit abbreviations do NOT take a period: `kg`, `m`, `cm`, `km/s`, `C` (for Celsius).

---

## 8. Grammar

### 8.1 Sentence Structure (SOV)
Turkish is a **Subject-Object-Verb** (SOV) language, unlike English which is SVO.

- English: `Ali eats an apple.` (SVO).
- Turkish: `Ali bir elma yer.` (SOV).

**Translation implication**: Verb-final structure is mandatory in neutral declarative sentences. Placing the verb earlier changes emphasis or creates a marked/colloquial tone.

### 8.2 Agglutinative Nature
Turkish is an **agglutinative** language — suffixes are appended to root words to express grammatical relationships:

- `ev` (house) → `evler` (houses) → `evlerim` (my houses) → `evlerimde` (in my houses) → `evlerimizde` (in our houses).
- A single Turkish word can correspond to an entire English phrase.
- Suffixes follow a strict order: plural → possessive → case → question particle.

### 8.3 Vowel Harmony
Turkish has **vowel harmony**, a fundamental phonological rule that suffix vowels must match the last vowel of the root word:

**Two-fold harmony (e/a)**: Suffixes have two forms — with `e` or `a`:
- `-de` / `-da` (locative case): `evde` (in the house), `okulda` (at school).
- `-den` / `-dan` (ablative case): `evden` (from the house), `okuldan` (from school).
- `-ler` / `-lar` (plural): `evler` (houses), `okullar` (schools).

**Four-fold harmony (i/ı/ü/u)**: Suffixes have four forms:
- `-i` / `-ı` / `-ü` / `-u` (accusative case): `evi` (the house), `okulu` (the school), `gölü` (the lake), `adımı` (my step).
- `-di` / `-dı` / `-dü` / `-du` (past tense): `geldi` (came), `bakdı` → `baktı` (looked — also consonant devoicing).

**Translation implication**: When translating, ensure all suffixes follow vowel harmony with their root word. This is automatic for native speakers but must be verified for translated terms.

### 8.4 Noun Cases
Turkish has six noun cases expressed through suffixes:

| Case | Suffix | Example | Meaning |
|------|--------|---------|---------|
| Nominative | (none) | ev | house (subject) |
| Genitive | -in/-ın/-ün/-un | evin | of the house |
| Dative | -e/-a | eve | to the house |
| Accusative | -i/-ı/-ü/-u | evi | the house (object) |
| Locative | -de/-da | evde | in the house |
| Ablative | -den/-dan | evden | from the house |

### 8.5 Possessive Suffixes
Possession is expressed through suffixes on the possessed noun (not separate possessive pronouns like English):

| Person | Suffix | Example | Meaning |
|--------|--------|---------|---------|
| 1st sing | -(i)m | evim | my house |
| 2nd sing | -(i)n | evin | your house |
| 3rd sing | -(s)i | evi | his/her/its house |
| 1st plur | -(i)miz | evimiz | our house |
| 2nd plur | -(i)niz | eviniz | your house |
| 3rd plur | -leri | evleri | their house |

- Possessive suffixes are attached to the noun directly (no space).
- Third person suffix `-(s)i` uses `s` as a buffer when the noun ends in a vowel: `araba+sı` (his/her car).

### 8.6 No Grammatical Gender
Turkish has **no grammatical gender**. The pronoun `o` covers he/she/it.

- Translation implication: When translating from a gendered language (e.g., English he/she, French le/la), the gender must be inferred from context or left ambiguous.
- If gender is critical to the meaning, disambiguate through context or explicit nouns (`erkek doktor` / `kadın doktor`).

### 8.7 Verb Conjugation
Turkish verbs conjugate for person, number, tense, mood, and aspect through suffix sequences.

**Simple present (Geniş zaman — aorist)**:
- `gelirim` (I come), `gelirsin` (you come), `gelir` (he/she comes)
- `geliriz` (we come), `gelirsiniz` (you come), `gelirler` (they come)

**Present continuous (Şimdiki zaman)**:
- `geliyorum` (I am coming), `geliyorsun`, `geliyor`, `geliyoruz`, `geliyorsunuz`, `geliyorlar`

**Past tense (Geçmiş zaman — görülen/di'li)**:
- `geldim`, `geldin`, `geldi`, `geldik`, `geldiniz`, `geldiler`

**Narrative past (Geçmiş zaman — duyulan/miş'li)**:
- `gelmişim`, `gelmişsin`, `gelmiş`, `gelmişiz`, `gelmişsiniz`, `gelmişler`

### 8.8 No Definite Article
Turkish does not have a definite article ("the"). Definiteness is expressed through:
- The accusative case suffix for direct objects: `kitabı okudum` (I read the book).
- Context and word order.
- The number `bir` functions as an indefinite article: `bir kitap` (a book).

### 8.9 Question Particle (mi)
- The question particle `mi` (and its vowel-harmony variants `mı`, `mü`, `mu`) is written as a **separate word**: `Geldi mi?` (Did he come?).
- It is NOT attached to the verb (unlike other suffixes).
- It follows the word being questioned and undergoes vowel harmony.

### 8.10 Negation
- Verbs are negated with the infix `-me-/-ma-` before tense/mood suffixes: `gelmedi` (he did not come), `gelmiyor` (he is not coming).
- The negative copula `değil` (is not) is used for nominal sentences: `O öğretmen değil` (He is not a teacher).
- `yok` is used for existential negation: `Param yok` (I have no money — lit. my money doesn't exist).
- Double negation IS possible but less common than in English.

### 8.11 Relative Clauses
- Turkish uses participle-based relative clauses rather than relative pronouns (who, which, that).
- Subject relatives: `-en/-an` participle: `gelen adam` (the man who comes).
- Object relatives: `-diği/-dığı/-düğü/-duğu` + possessive: `geldiğim adam` (the man whom I came to).
- Translating English relative clauses into Turkish often requires restructuring the sentence.

---

## 9. Formality

### 9.1 Siz vs. Sen (You — Formal vs. Informal)

Turkish has a T-V distinction (tu/vous equivalent):

| Pronoun | Level | Usage |
|---------|-------|-------|
| Sen | Informal | Friends, family, children, close colleagues, God, subordinates (in some contexts) |
| Siz | Formal/Singular | Strangers, superiors, elders, customer service, professional settings |
| Siz | Plural | Multiple people (regardless of formality level) |
| Sizler | Emphatic plural | Multiple people (emphasizing each individual, formal) |

**Critical rule**: When translating English "you" to Turkish, you MUST determine the appropriate register:
- Business correspondence → `siz` (formal singular).
- Marketing material targeting young audience → `sen` (informal).
- Legal/medical/government documents → `siz` (formal).
- Software UI → generally `sen` (modern convention), but varies by audience.

**Register consistency**: Once a register is chosen (sen/siz), maintain it throughout the entire document. Switching between sen and siz for the same audience is a **major error**.

### 9.2 Formal Correspondence

| English | Turkish (Formal) |
|---------|-----------------|
| Dear Mr. Yılmaz | Sayın Ahmet Yılmaz |
| Dear Ms. Demir | Sayın Ayşe Demir |
| Dear Sir/Madam | Sayın Yetkili |
| To whom it may concern | İlgili Makama |
| Sincerely | Saygılarımla |
| Best regards | Saygılarımla / İyi çalışmalar |
| Yours faithfully | Saygılarımla (less common than "Saygılarımla") |

Note: `Sayın` precedes full name or surname, NOT given name alone: `Sayın Yılmaz` (correct), `Sayın Ahmet` (incorrect unless the person is known by their given name in context).

### 9.3 Resmi Dil (Official/Formal Language)
- Formal Turkish uses longer, more complex sentence structures.
- The passive voice is common in formal/official Turkish: `toplantı yapılacaktır` (the meeting will be held).
- The future-calendar suffix `-acak/-ecek` is used in formal commitments: `belge gönderilecektir` (the document will be sent).
- Formal language avoids:
  - Contractions.
  - Slang or colloquial expressions.
  - English loanwords where Turkish equivalents exist.
  - The informal narrative past (`-miş`) for factual statements.
- Official documents often use the aorist tense for regulations: `Bu yönetmelik ... kapsar` (This regulation covers ...).

### 9.4 Register Adaptation
- When translating, adapt the register to the target audience:
  - **Academic**: Formal, nominalized structures, technical terminology, passive voice.
  - **Business**: Semi-formal, clear and direct, professional terminology.
  - **Legal**: Highly formal, precise terminology, archaic structures where standard.
  - **Marketing**: Conversational or informal, engaging, idiomatic.
  - **Technical**: Precise, clear, consistent terminology, moderate formality.
  - **Children's content**: Simple vocabulary, clear sentence structures, `sen` register.

### 9.5 Honorifics and Titles

| Turkish | Usage |
|---------|-------|
| Sayın | General formal address (Mr./Ms.) |
| Bey | After first name (informal-formal): `Ahmet Bey` |
| Hanım | After first name (informal-formal): `Ayşe Hanım` |
| Hocam | "My teacher" — respectful address for professors/experts |
| Efendim | Very formal/respectful "sir/madam" |
| Bay | Formal equivalent of Mr. (used before surname in very formal contexts): `Bay Yılmaz` |
| Bayan | Formal equivalent of Ms. (usage declining; `Sayın` preferred) |

### 9.6 Formality in Commands and Requests
- Direct imperative (`yap!`) is informal.
- Polite request uses `-ir misiniz` (aorist + question): `Yapar mısınız?` (Would you do it?).
- Very polite uses `-ebilir miyim` / `-ebilir misiniz`: `Yapabilir misiniz?` (Could you do it?).
- Third-person imperative for formal instructions: `yapılmalıdır` (it must be done), `yapınız` (do — formal command).

---

## 10. OCR Artifacts

### 10.1 Handling OCR Artifacts in Turkish

When source documents contain OCR (Optical Character Recognition) artifacts that affect Turkish text:

### 10.2 Turkish-Specific OCR Issues

| Issue | Example (Source) | Correct (Turkish) | Notes |
|-------|-------------------|-------------------|-------|
| Missing diacritics | Istanbul | İstanbul | Capital I vs İ confusion |
| Dotted/undotted I | ıstanbul | İstanbul | Wrong dot direction |
| Cedilla | c, s | ç, ş | ç/ş confused with c/s |
| Breve/Circumflex | kar | kâr | Changes meaning (snow vs profit) |
| Dot on i | ı | i | Lowercase undotted/dotted confusion |
| Tilde on n | n | — | Ñ is not Turkish |
| Umlaut confusion | o | ö, ü | ö/ü confused with plain vowels |

### 10.3 OCR Artifact Markup
- OCR artifacts that are corrected MUST be marked using the following format:

  `[geri yüklendi: doğru metin]`

  Example: `İstanbul` becomes flagged if OCR produced `Istanbul`, correction noted as:
  `[geri yüklendi: İstanbul]`

- Use `[geri yüklendi: ...]` for individual word/phrase corrections where OCR introduced errors in Turkish characters specifically.

### 10.4 Correction Scope
- Only correct OCR artifacts that produce **invalid Turkish** or **meaning changes**.
- Do NOT correct regional spelling variations (e.g., some web text vs. formal TDK spelling).
- Do NOT correct original source language text that happens to look like an OCR error (e.g., the English word "Istanbul" vs. the Turkish "İstanbul" in an English original).

### 10.5 Ambiguous Characters
- In older OCR outputs, distinguish between:
  - Letter `O` vs digit `0` — context-dependent; flag `[geri yüklendi: O/0 belirsiz]` if genuinely ambiguous.
  - Letter `I` (lowercase `ı`) vs digit `1` — especially problematic in Turkish due to the undotted I.
  - Double-check the Turkish dotted `i` in words like `çalışma`, `işlem`, `bilgi`.

### 10.6 Preservation of Original Artifacts
- If the source itself contains OCR artifacts (e.g., a scanned PDF that was OCR'd poorly), the translator should correct them silently in the target text.
- If the source OCR is ambiguous and the correct Turkish text cannot be determined with confidence, use:

  `[geri yüklendi: metin belirsiz — orijinal: ...]`

- Do NOT carry OCR artifacts from the source into the Turkish translation. The translation MUST be clean.

### 10.7 Character Encoding
- Turkish text must be encoded in **UTF-8**.
- Verify that the following encoded characters are rendered correctly:
  - `Ç` = U+00C7, `ç` = U+00E7
  - `Ğ` = U+011E, `ğ` = U+011F
  - `İ` = U+0130, `i` = U+0069
  - `I` = U+004C, `ı` = U+0131
  - `Ö` = U+00D6, `ö` = U+00F6
  - `Ş` = U+015E, `ş` = U+015F
  - `Ü` = U+00DC, `ü` = U+00FC
- If the file encoding is not UTF-8, convert it before processing.

### 10.8 Numeric OCR Artifacts
- Check for confused characters in numbers:
  - Comma `.` vs period `,` in numerical contexts — CRITICAL in Turkish (comma is the decimal separator).
  - Digit `1` vs lowercase `l` vs uppercase `I`.
  - Digit `0` vs letter `O`.
- Flag with `[geri yüklendi: rakam düzeltmesi]` format when numbers are corrected.

---

## 11. Translation Philosophy

### 11.1 Natural Turkish
The primary goal is to produce **natural-sounding Turkish** that reads as if it were originally written in Turkish, not translated from another language.

**Principles:**
- Avoid calques (direct structural borrowings from the source language).
- Do not preserve source-language sentence structure when it violates natural Turkish SOV order.
- Use idiomatic Turkish expressions where they convey the same meaning as the source, not literal translations.
- Prefer Turkish vocabulary over borrowed/foreign words where a well-established Turkish equivalent exists.

### 11.2 Vowel Harmony Maintenance
Vowel harmony is **non-negotiable** in Turkish translation. Every suffix must harmonize with its root:

**Verification checklist:**
- Locative suffix: `-de` after front vowels (e/i/ö/ü), `-da` after back vowels (a/ı/o/u).
- Plural suffix: `-ler` after front vowels, `-lar` after back vowels.
- Accusative suffix: `-i` after front unrounded, `-ı` after back unrounded, `-ü` after front rounded, `-u` after back rounded.
- Genitive suffix: follow four-fold harmony.

**Exception handling:**
- Loanwords that violate vowel harmony internally (e.g., `kitap`, `evlat`, `saat`) still govern suffix harmony based on their LAST vowel:
  - `kitap` (last vowel = `a` → back) → `kitapta` (not kitapte).
  - `saat` (last vowel = `a` → back) → `saatte` (wait — `a` is back, but `saat` typically takes `-te` due to consonant devoicing; the vowel in suffix is still `-e` after `a`? No, `saatte` is actually `saat` + `-te` but the vowel `e` does NOT harmonize with `a`? Actually, `saat` has the vowel `a` (back) but `saat` takes `-te` not `-ta` because of consonant devoicing of `t` — but wait, `-de`/`-da` is the locative suffix, and the consonant devoices to `-te`/`-ta`. After `t`, it's `saatte` — the `e` here... actually I need to correct this. `saat` ends in `t`, so the locative suffix devoices to `-te`/`-ta`. The last vowel of `saat` is `a` (back), so it should be `saatta`. But actually, `saat` is commonly `saatte` in Turkish — this is because `saat` is a loanword from Arabic and certain loanwords have exceptional behavior. Actually no, the common form IS `saatte`. Let me not get into this edge case in the rules document.)

**Actually, let me correct the example for the document:**
- `kitap` → `kitapta` (last vowel `a` → back → `-da`, devoiced to `-ta`).
- `göz` → `gözde` (last vowel `ö` → front → `-de`).
- `okul` → `okulda` (last vowel `u` → back → `-da`).

(This is fine as a general rule; edge cases exist but do not need exhaustive treatment in a style guide.)

### 11.3 Agglutination Rules
Turkish builds words through suffix stacking. Translation must respect:

1. **Correct suffix order**: root + (voice) + (causative) + (negative) + (tense) + (person).
2. **Buffer consonants**: When a suffix starting with a vowel attaches to a root ending in a vowel, buffer consonant `y`, `n`, `s`, or `ş` is inserted:
   - `araba` + `-i` → `arabayı` (buffer `y`).
   - `masa` + `-da` → `masada` (no buffer needed — suffix starts with consonant).
3. **Consonant devoicing (Ünsüz yumuşaması)**: Final `p`, `ç`, `t`, `k` in a root become `b`, `c`, `d`, `ğ` when followed by a vowel-initial suffix:
   - `kitap` + `-ı` → `kitabı` (not `kitapı`).
   - `ağaç` + `-a` → `ağaca` (not `ağaça`).
   - `at` + `-a` → `ada` (not `ata` — wait, `at` → `ata` actually. Let me check: `at` + `-a` = `ata` (to the horse). The `t` does NOT devoice here because `t` only devoices... actually, `t` devoices irregularly. This is `at` (horse) → `ata`; but `ad` (name) → `ada` (to the name). The two merge in dative. Let me use a clearer example.)
   
   Let me use a better example:
   - `kitap` → `kitabı` (p → b before vowel).
   - `ağaç` → `ağaca` (ç → c before vowel).
   - `renk` → `rengi` (k → ğ before vowel).

4. **Consonant elision**: Some roots drop a vowel when a suffix is added:
   - `akıl` → `aklı` (vowel dropped).
   - `şehir` → `şehri` (vowel dropped).

### 11.4 Meaning Preservation
- Translate meaning, not words. If the literal translation sounds unnatural, find a Turkish expression that conveys the same meaning.
- Preserve the **pragmatic intent**: a request should remain a request, a warning a warning, etc.
- Preserve the **tone**: formal/informal, serious/lighthearted, technical/accessible.
- Preserve **idioms**: replace source-language idioms with Turkish idioms of equivalent meaning, not literal translations.
- Preserve **cultural references**: if a cultural reference would not be understood by a Turkish audience, consider adding a brief explanation or adapting it to a comparable Turkish reference.

### 11.5 Domain-Specific Terminology
- Use established Turkish terminology for the relevant domain.
- For technical/scientific translation, consult Turkish terminology resources:
  - TDK (Türk Dil Kurumu) for standard terminology.
  - TÜBA (Türkiye Bilimler Akademisi) for scientific terminology.
  - Industry-specific glossaries for specialized domains.
- When no Turkish equivalent exists, the foreign term may be used, typically italicized with a Turkish explanation on first use.

### 11.6 Sentence Length and Complexity
- Turkish sentences tend to be longer than English sentences, with more subordination.
- However, for modern business and technical translation, clear and manageable sentence lengths are preferred.
- Break overly long English sentences into shorter Turkish sentences if needed for clarity.
- Use nominalization (verbal nouns) — a hallmark of formal Turkish — where appropriate.

### 11.7 Back-Translation Test
- After translating, consider whether a back-translation to the source language would convey the same meaning.
- If the back-translation would be significantly different in meaning (not just structure), revise.

### 11.8 Language Register Consistency
- Once a register (formal/informal, sen/siz, technical vocabulary level) is chosen, it must be maintained consistently throughout the document.
- Do not mix `sen` and `siz` for the same audience.
- Do not mix technical and colloquial vocabulary levels unless justified by the context (e.g., a direct quote in colloquial speech).

### 11.9 Neologisms and Loanwords
- Turkish has a rich tradition of language reform. Where possible, prefer Turkish-derived terms over Arabic, Persian, French, or English loanwords.
- Practical rule: use the word that a Turkish reader would most naturally encounter in the given context.
  - `bilgisayar` (computer — Turkish coinage) over `kompüter`.
  - `yanıt` (reply — Turkish) over `cevap` (Arabic origin), though both are common.
  - `bölüm` (department/section — Turkish) over `departman` (from French/English).
- Do not be purist to the point of unnaturalness: some loanwords are fully integrated (`merhaba` from Arabic, `telefon` from French/English).

### 11.10 Untranslatable Elements
- Some elements may legitimately remain in the source language:
  - Brand names and product names: `iPhone`, `Windows`, `Google`.
  - Foreign titles: `Mr.`, `Mrs.` when referring to foreign individuals in foreign contexts (translate `Sayın` for Turkish contexts).
  - Acronyms: preserve original but provide Turkish expansion on first use if helpful.
  - Quoted foreign language text within the source: leave as-is unless the surrounding context clearly demands translation.

---

*End of Turkish Translation Base Rules. These rules should be read in conjunction with the scoring rubric and any project-specific guidelines provided.*
