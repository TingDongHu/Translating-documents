---
id: fa/rules/base
type: rules
target_lang: fa
name: Persian Translation Base Rules
description: Persian base translation rules
---

# Persian Translation Base Rules

This document defines the foundational rules for translating documents into Persian (Farsi). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Decimal Separator
- The **decimal point** (نقطه اعشار) is used in Persian: `3.14` (not `3,14`).
- Decimal places are separated by a dot with **no space** before or after: `0.25`, `12.5`, `100.99`.
- Trailing zeros after the decimal point are preserved when they carry significance: `5.00` (if precision matters), otherwise `5`.

### 1.2 Thousands Separator
- The **comma** (کاما) is used as the thousands separator: `1,000`, `25,000`, `1,000,000`.
- Do NOT use dot, space, or apostrophe as thousands separator in modern Persian: `1.000` is ambiguous (may be read as the number one).
- Four-digit numbers may optionally omit the comma: `1000` is acceptable, `1,000` is preferred for clarity.
- No thousands separator is used after the decimal point: `1,000.50`.

### 1.3 Negative Numbers
- Negative numbers use the minus sign (`−`) placed directly before the digits: `−5`, `−3.14`.
- The minus sign is the same width as the digits (not an en-dash or em-dash).
- In financial contexts, parentheses may alternatively indicate negatives: `(1,000.00)`.

### 1.4 Percentages
- The percent symbol (`%`) is placed **after** the number with a non-breaking space: `25%` or `25 %`.
- Both forms are acceptable, but `25%` (no space) is more common in technical/financial texts.
- Choose one form and maintain consistency throughout the document.
- Percentage ranges: `10%-20%` or `10% تا 20%`.

### 1.5 Ordinal Numbers
- Ordinal numbers in Persian use the suffix `-اُم` (e.g., `۱اُم`, `۲اُم`, `۳اُم`).
- Alternatively, the suffix `-م` is used: `اول`, `دوم`, `سوم`, `چهارم`, `پنجم`.
- Written numerals: `۱اُم` (first), `۲اُم` (second), `۳اُم` (third).
- Example: `قرن بیستاُم` (20th century), `ماده سوم` (article 3).

### 1.6 Fractions
- Fractions are written with a slash or as decimal numbers: `1/2`, `3/4`.
- Mixed numbers: `2 1/2` (space between the integer and fraction).
- Persian-specific fractions are common: `نصف` (1/2), `یک‌سوم` (1/3), `یک‌چهارم` (1/4).

### 1.7 Numerals in Text
- Numbers from one to ten (or up to twelve, depending on context) are typically written as words in running text: `یک`, `دو`, `سه`, `چهار`, `پنج`.
- Numbers above ten are written as digits: `42`, `1,250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence should NEVER begin with a digit; rephrase or write the number in words.

### 1.8 Eastern Arabic Numerals
- Eastern Arabic-Indic numerals (`٠١٢٣٤٥٦٧٨٩`) are used in some Arabic-speaking countries but are NOT standard in Persian.
- Use Western Arabic numerals (`0123456789`) or Persian numerals (`۰۱۲۳۴۵۶۷۸۹`) — both are acceptable.
- Persian numerals are preferred in literary and formal contexts; Western Arabic numerals are common in technical and financial texts.
- Be consistent within a document; do not mix numeral systems.

---

## 2. Currency

### 2.1 Iranian Rial (IRR)
- Symbol: `ریال` (written after the amount): `1,000 ریال`.
- ISO code: `IRR`.
- The rial is the official currency of Iran.
- In formal financial documents, use `ریال` or `IRR`.

### 2.2 Iranian Toman (Toman)
- 1 تومان = 10 ریال. The toman is the colloquial unit of currency in Iran.
- Symbol: `تومان` (written after the amount): `100 تومان`.
- ISO code: Not officially assigned, but `IRT` is sometimes used.
- In everyday usage, prices are quoted in toman: `100,000 تومان`.
- Note: When translating financial documents, clarify whether amounts are in rial or toman.

### 2.3 US Dollar
- Symbol: `$`.
- **Symbol placement**: `$` is placed **after** the amount, separated by a space: `100 $`.
- Alternative (ISO code): `100 USD`.
- In Persian texts, `$` after the amount is preferred to maintain visual consistency.

### 2.4 Euro
- Symbol: `€`.
- **Symbol placement**: `€` is placed **after** the amount, separated by a space: `100 €`.
- Alternative (ISO code): `100 EUR`.

### 2.5 Other Currencies
- Follow the same pattern: amount first, then currency symbol/code.
- Use ISO 4217 codes for less common currencies: `100 GBP`, `100 JPY`, `100 CHF`.

### 2.6 Currency Translation Rules
- Translate currency names in running text: "dollars" → `دلار`, "euros" → `یورو`.
- "pence" → `پنس`, "cents" → `سِنت`.
- Maintain the original currency amounts; do NOT convert to rial or toman unless explicitly instructed.

### 2.7 Formatting Rules
- Decimal point applies to all currency amounts: `100.00` (not `100,00`).
- Comma applies as thousands separator: `1,000.00` (not `1.000,00`).
- Use exactly two decimal places for financial amounts: `50.00` (not `50`).

---

## 3. Date and Time

### 3.1 Iranian Solar Hijri Calendar (تقویم هجری شمسی)
- The Solar Hijri calendar is the official calendar of Iran.
- Format: **YYYY/MM/DD** (year/month/day): `1404/03/06`.
- The slash is the standard separator.
- Leading zeros are used for single-digit days and months: `1404/03/06` (not `1404/3/6`).

### 3.2 Gregorian Calendar
- When Gregorian dates appear in Persian texts, use: `YYYY/MM/DD` or `DD/MM/YYYY`.
- The Gregorian calendar is used for international correspondence.
- Clearly indicate the calendar system when ambiguity is possible: `2026/05/27 (میلادی)` or `۲۷ مه ۲۰۲۶`.

### 3.3 Solar Hijri Month Names

| Month Number | Persian Name | English Equivalent |
|-------------|-------------|-------------------|
| 1 | فروردین (Farvardin) | March 21 – April 20 |
| 2 | اردیبهشت (Ordibehesht) | April 21 – May 21 |
| 3 | خرداد (Khordad) | May 22 – June 21 |
| 4 | تیر (Tir) | June 22 – July 22 |
| 5 | مرداد (Mordad) | July 23 – August 22 |
| 6 | شهریور (Shahrivar) | August 23 – September 22 |
| 7 | مهر (Mehr) | September 23 – October 22 |
| 8 | آبان (Aban) | October 23 – November 21 |
| 9 | آذر (Azar) | November 22 – December 21 |
| 10 | دی (Dey) | December 22 – January 20 |
| 11 | بهمن (Bahman) | January 21 – February 19 |
| 12 | اسفند (Esfand) | February 20 – March 20 |

### 3.4 Gregorian Month Names (Persian)

| English | Persian | Abbreviation |
|---------|---------|-------------|
| January | ژانویه (Janviye) | ژانویه |
| February | فوریه (Furiye) | فوریه |
| March | مارس (Mars) | مارس |
| April | آوریل (Avril) | آوریل |
| May | مه (Meh) | مه |
| June | ژوئن (Juin) | ژوئن |
| July | ژوئیه (Juillet) | ژوئیه |
| August | آگوست (Agost) | آگوست |
| September | سپتامبر (Sptmbr) | سپتامبر |
| October | اکتبر (Oktbr) | اکتبر |
| November | نوامبر (Nvambr) | نوامبر |
| December | دسامبر (Dsambr) | دسامبر |

### 3.5 Day Names (Persian)
- Day names in Persian: `شنبه` (Saturday), `یکشنبه` (Sunday), `دوشنبه` (Monday), `سه‌شنبه` (Tuesday), `چهارشنبه` (Wednesday), `پنجشنبه` (Thursday), `جمعه` (Friday).
- The Persian week starts on Saturday and ends on Friday (the weekend).
- Friday (`جمعه`) is the official weekly holiday in Iran.

### 3.6 Time Format
- **24-hour format** is standard: `14:30` (not `2:30 PM`).
- Hours and minutes are separated by a colon: `09:15`, `23:45`.
- Seconds, when included: `14:30:25`.
- Leading zero for hours: `08:00` (not `8:00`).
- AM/PM notation is NOT used in Persian formal writing.
- The word `ساعت` (saat, "hour/o'clock") is used when reading time aloud or in formal prose.

### 3.7 Combined Date and Time
- Date and time are separated by a comma or the word `ساعت`:
  - `1404/03/06، 14:30`
  - `۶ خرداد ۱۴۰۴، ساعت ۱۴:۳۰`

### 3.8 Time Zones
- Iran Standard Time isIRST (UTC+3:30), Iran Summer Time IRDT (UTC+4:30).
- Time zone abbreviations: `IRST` / `IRDT`.
- Preserve original time zone designations in translated documents unless localizing.

---

## 4. Addresses

### 4.1 Persian Address Format (Addresses within Iran)
Persian addresses flow from **largest to smallest** unit (same as English):

1. **استان** (ostān, province).
2. **شهرستان** (shahrestān, county).
3. **شهر** (shahr, city/town).
4. **خیابان** (khiābān, street).
5. **کوچه** (kucheh, alley).
6. **پلاک** (pelāk, building number).
7. **واحد** (vāhed, unit/apartment).
8. **کد پستی** (code posti, postal code — 10 digits).

Example: `تهران، خیابان ولیعصر، کوچه میرزایی، پلاک ۱۲، واحد ۳، کد پستی ۱۲۳۴۵۶۷۸۹۰`

### 4.2 Address Components

| English | Persian | Notes |
|---------|---------|-------|
| Street | خیابان (Khiābān) | Abbreviated as خ. |
| Alley | کوچه (Kucheh) | Abbreviated as ک. |
| Avenue | بلوار (Bulvār) | |
| Road | جاده (Jādeh) | |
| Highway | آزادراه (Āzādrāh) | |
| Neighborhood | محله (Mahalleh) | |
| District | منطقه (Mantagheh) | |
| Province | استان (Ostān) | |
| Building Number | پلاک (Pelāk) | |
| Unit/Apartment | واحد (Vāhed) | |
| Postal Code | کد پستی (Code Posti) | 10 digits |
| P.O. Box | صندوق پستی (Sanduq-e Posti) | |

### 4.3 Foreign Addresses in Persian Texts
- Foreign addresses should generally be **preserved in their original form** (not translated).
- Address labels like "Street", "Avenue" may optionally be translated for comprehension.
- Country names ARE translated into Persian.

### 4.4 Postal Codes
- Iranian postal codes are 10 digits: `1234567890`.
- Foreign postal codes are preserved as-is.

---

## 5. Proper Nouns

### 5.1 Persian Script
- Persian uses the Arabic-based script (Perso-Arabic) written from **right to left** (RTL).
- Persian-specific letters: `پ` (pe), `چ` (che), `ژ` (zhe), `گ` (gāf).
- The letter `و` (vāv) can represent /v/, /o/, /u/, or /ow/ depending on context.
- The letter `ی` (ye) can represent /j/, /e/, or /i/ depending on context.
- Persian does NOT use the Arabic letters: `ث` (the), `ذ` (zāl), `ص` (ṣād), `ض` (ḍād), `ط` (ṭā), `ظ` (ẓā), `ء` (hamza) — except in loanwords from Arabic.

### 5.2 Foreign Name Transcription
- Foreign personal names are generally **preserved in their original spelling**.
- Common/historical names follow established Persian forms.
- Established Persian forms for well-known names/places:
  - `Washington` → `واشینگتن`
  - `Paris` → `پاریس`
  - `London` → `لندن`
  - `Moscow` → `مسکو`
  - `New York` → `نیویورک`
  - `Rome` → `رم`
  - `Athens` → `آتن`
  - `Beijing` → `پکن`
  - `Germany` → `آلمان`
  - `Greece` → `یونان`
- When in doubt, **preserve the original spelling** rather than inventing a Persian transcription.

### 5.3 Capitalization Rules
- Persian script does not have uppercase/lowercase distinction.
- All Persian text is written in a single case (no capitals).
- Proper nouns are NOT capitalized in Persian script.
- When romanized Persian uses Latin script, proper nouns follow standard romanization conventions.

### 5.4 Company and Brand Names
- Company and brand names are **preserved in their original form**.
- Legal suffixes may be translated to Persian equivalents:
  - `Inc.` → `شرکت سهامی` or `شرکت`
  - `Ltd.` → `شرکت محدود` or `شرکت با مسئولیت محدود`
  - `GmbH` → `شرکت با مسئولیت محدود`
  - `LLC` → `شرکت با مسئولیت محدود` (شرکت با مسئولیت محدود)
- When in doubt, preserve the original legal form.

### 5.5 Geographic Name Translation
- Geographic features: translate common nouns, keep proper name.
  - `Sahara Desert` → `صحرای صحرا`
  - `Atlantic Ocean` → `اقیانوس اطلس`
  - `Himalaya Mountains` → `کوه‌های هیمالیا`
- Country names with established Persian forms use those forms:
  - `United States` → `ایالات متحده آمریکا`
  - `United Kingdom` → `بریتانیا`
  - `United Arab Emirates` → `امارات متحده عربی`

---

## 6. Script Direction and Layout

### 6.1 Right-to-Left (RTL)
- Persian is written from **right to left**.
- All Persian text flows RTL; numbers and Latin-script text within Persian text are **left-to-right** (bidirectional).
- Documents in Persian should have RTL text direction set in the file/layout.

### 6.2 Bidirectional Text
- Mixed Persian/Latin text requires careful bidirectional handling.
- Numbers within Persian text are written LTR: `قیمت ۱,۰۰۰ تومان`.
- Latin abbreviations within Persian text may break the RTL flow: `سیستم عامل (OS)`.
- Use the Unicode bidirectional algorithm correctly; do not insert manual bidi marks unless necessary.

### 6.3 Punctuation Direction
- Period, comma, semicolon: placed at the end of the LTR/RTL segment as appropriate.
- Quotation marks: Persian uses `«...»` (guillemets) as primary quotation marks.
- Question mark `?` and exclamation mark `!` are placed at the end of the sentence (RTL direction).
- The Persian question mark `؟` (U+061F) is the preferred form in Persian texts.

---

## 7. Formality

### 7.1 Shomareh va Tu (Formal vs. Informal "You")
- Persian has a T-V distinction (tu/shoma equivalent):

| Pronoun | Level | Usage |
|---------|-------|-------|
| تو (Tu) | Informal | Friends, family, children, close colleagues |
| شما (Shomareh) | Formal/Singular | Strangers, superiors, elders, customer service, professional settings |
| شما (Shomareh) | Plural | Multiple people (regardless of formality level) |

- **Critical rule**: When translating English "you" to Persian, you MUST determine the appropriate register:
  - Business correspondence → `شما` (formal).
  - Marketing material targeting young audience → `تو` (informal).
  - Legal/medical/government documents → `شما` (formal).
  - Software UI → generally `شما` (formal), but varies by audience.

- **Register consistency**: Once a register is chosen (tu/shoma), maintain it throughout the entire document. Switching between tu and shoma for the same audience is a **major error**.

### 7.2 Formal Correspondence

| English | Persian (Formal) |
|---------|-----------------|
| Dear Mr. Yılmaz | جناب آقای ییلماز |
| Dear Ms. Demir | سرکار خانم دمیر |
| Dear Sir/Madam | سرکار عالی / محترم |
| To whom it may concern | به حضور محترم |
| Sincerely | با احترام |
| Best regards | با احترام / با تقدیم احترام |
| Yours faithfully | تقدیم احترام |

### 7.3 Honorifics and Titles

| Persian | Usage |
|---------|-------|
| جناب آقای (Janab-e Agha) | Very formal Mr. — used before full name |
| سرکار خانم (Sarkar Khanom) | Very formal Ms. — used before full name |
| آقای (Agha) | General Mr. — used before name |
| خانم (Khanom) | General Ms./Mrs. — used before name |
| استاد (Ostad) | Professor/Teacher — respectful academic title |
| دکتر (Doctor) | Doctor — used before name |

### 7.4 Formal vs. Informal Commands
- Direct imperative is informal: `بیا!` (come!).
- Polite request uses `لطفاً` (please): `لطفاً بیایید` (please come).
- Very polite uses `خواهش می‌کنم` or `اجازه می‌دهید`: `آیا اجازه می‌دهید بیایم؟` (may I come?).
- Formal instructions use passive or impersonal forms: `باید انجام شود` (it must be done).

---

## 8. Punctuation

### 8.1 Period (.)
- Used at the end of declarative sentences.
- In Persian, the period is placed at the **end** of the RTL sentence.

### 8.2 Comma (،)
- Persian uses the Arabic comma `،` (U+060C) as the standard comma, NOT the Latin comma `,`.
- The Arabic comma is placed at the bottom of the line, similar to the Latin comma but visually distinct.
- For maximum compatibility, some modern Persian texts use the Latin comma `,` — both are acceptable.
- Choose one form and maintain consistency.

### 8.3 Semicolon (؛)
- Persian uses the Arabic semicolon `؛` (U+061B) as the standard semicolon, NOT the Latin semicolon `;`.
- Same rules as English semicolons otherwise.

### 8.4 Colon (:)
- Same as English colon: used to introduce a list, explanation, or quotation.
- Placed at the end of the RTL text segment.

### 8.5 Question Mark (؟)
- Persian uses the Arabic question mark `؟` (U+061F), which is a reversed question mark.
- Placed at the **end** of the sentence (RTL direction).
- The Latin question mark `?` is also acceptable in modern Persian typing.

### 8.6 Quotation Marks
- Primary quotation marks: `«...»` (guillemets / French quotation marks).
- Alternative: `"..."` (standard double quotes) — widely used in modern Persian.
- Single quotation marks: `'...'` for quotes within quotes.
- The guillemets are preferred in formal/academic Persian texts.

### 8.7 Ellipsis (...)
- Three dots with no spaces: `...`
- Used for unfinished sentences or omissions.

### 8.8 Slash (/)
- Used for alternatives (`و/یا`), fractions (`1/2`), and dates (`25/05/2026`).
- No spaces around the slash.

### 8.9 Parentheses
- Usage is the same as English: `(` and `)`.
- Parentheses are placed **after** the text they enclose in RTL layout.

### 8.10 No Double Punctuation
- Persian does NOT use double punctuation. NEVER combine punctuation marks.
- Avoid sequences like `،!`, `؟.`, `!،` — these are NOT valid in Persian.

---

## 9. Formatting

### 9.1 Title Capitalization
- In Persian, there is NO capitalization distinction (Persian script is caseless).
- Titles are written in the same case as body text.
- Emphasis in titles is achieved through bold formatting, not capitalization.

### 9.2 Headings and Subheadings
- Heading hierarchy should be clear and consistent.
- No period at the end of headings.
- Subheadings follow the same rule.

### 9.3 Lists
- Bulleted lists: use `•` or `‣` as bullet markers.
- Numbered lists: use Persian numerals (`۱.`, `۲.`, `۳.`) or standard numerals (`1.`, `2.`, `3.`).
- Items that are complete sentences end with a period.
- Items that are phrases do NOT end with punctuation.

### 9.4 Tables
- Column headers should be clear and concise.
- Alignment: text is right-aligned (RTL), numbers are left-aligned (LTR).
- Currency amounts in table columns should align on the decimal point.
- Use consistent formatting within a column.

### 9.5 Bold and Italic
- Bold: used for headings, key terms, and emphasis.
- Italic: used for foreign words, book/movie titles, and emphasis.
- Persian uses italic for book titles (similar to English convention).

### 9.6 Spacing
- Single space after periods, colons, and semicolons (not double space).
- Persian uses a **half-space** (`نیم‌فاصله`, U+200C) to join compound words: `خودرو` (not `خود ر`).
- No space before punctuation marks.
- One space before opening parentheses and after closing parentheses when embedded in text.

### 9.7 Paragraphs
- Paragraphs should be coherent units of thought.
- First-line indent: optional, but if used, should be consistent throughout.
- Block paragraphs (no indent, space between paragraphs) are common in modern Persian business writing.

### 9.8 Abbreviations
- Common Persian abbreviations:
  - `م.` (ماده — article), `بند` (clause).
  - `ص.` (صفحه — page), `صص.` (صفحات — pages).
  - `ش.` (شماره — number).
  - `تاریخ` (date), `تلفن` (phone).
- SI unit abbreviations do NOT take a period: `kg`, `m`, `cm`, `km/s`.

---

## 10. Translation Philosophy

### 10.1 Natural Persian
The primary goal is to produce **natural-sounding Persian** that reads as if it was originally written in Persian, not translated from another language.

**Principles:**
- Avoid calques (direct structural borrowings from the source language).
- Do not preserve source-language sentence structure when it violates natural Persian word order.
- Use idiomatic Persian expressions where they convey the same meaning as the source.
- Prefer Persian vocabulary over borrowed/foreign words where a well-established Persian equivalent exists.

### 10.2 Ezafe Construction (کسره اضافه)
- The Ezafe is a grammatical particle linking a noun to its modifiers or possessor.
- Written as `-ِ` (unvocalized) or `-ی` after vowels: `خانهٔ بزرگ` (big house), `کتابِ علی` (Ali's book).
- In modern unvocalized text, the Ezafe is typically unwritten (implied by context and syntax).
- When translating compound nouns, the Ezafe must be correctly implied or written.

### 10.3 SOV Word Order
- Persian is a **Subject-Object-Verb** (SOV) language, unlike English which is SVO.
- English: `Ali eats an apple.` (SVO).
- Persian: `علی سیبی می‌خورد.` (SOV).
- **Translation implication**: Verb-final structure is mandatory in neutral declarative sentences.

### 10.4 Meaning Preservation
- Translate meaning, not words. If the literal translation sounds unnatural, find a Persian expression that conveys the same meaning.
- Preserve the **pragmatic intent**: a request should remain a request, a warning a warning, etc.
- Preserve **idioms**: replace source-language idioms with Persian idioms of equivalent meaning.
- Preserve **cultural references**: if a cultural reference would not be understood by a Persian audience, consider adding a brief explanation or adapting it.

### 10.5 Domain-Specific Terminology
- Use established Persian terminology for the relevant domain.
- When no Persian equivalent exists, the foreign term may be used, typically in parentheses or with a Persian explanation on first use.
- Prefer the term that a Persian reader would most naturally encounter in the given context.

---

*End of Persian Translation Base Rules. These rules should be read in conjunction with the scoring rubric and any project-specific guidelines provided.*
