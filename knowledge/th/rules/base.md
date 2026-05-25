# Thai Language Translation Rules (Base)

> Language pair target: Any source language -> Thai (ภาษาไทย)
> Register: Formal written Thai (ภาษาทางการ)
> Encoding: UTF-8

---

## 1. Number Format

### 1.1 Digit Systems

Thai has two parallel digit systems. **Arabic numerals (0-9) are the default** in modern formal Thai documents, government publications, and commercial contexts. Thai numerals (เลขไทย) appear in:

- Religious texts and temple documents
- Traditional certificates and official royal decrees
- Historical or culturally traditional contexts
- Some government forms for ceremonial use

**Thai numeral set:**

| Arabic | Thai  | Arabic | Thai  |
|--------|-------|--------|-------|
| 0      | ๐     | 5      | ๕     |
| 1      | ๑     | 6      | ๖     |
| 2      | ๒     | 7      | ๗     |
| 3      | ๓     | 8      | ๘     |
| 4      | ๔     | 9      | ๙     |

**Rule:** Preserve the digit system used in the source. If the source uses Arabic numerals, keep Arabic numerals in Thai output. If the source uses Thai numerals, retain Thai numerals. Do NOT convert between systems unless the document style guide explicitly requires it.

### 1.2 Decimal Point

Thai uses the **full stop (.)** as the decimal point, identical to English. Examples:

- 3.14 -> 3.14
- 0.5 -> 0.5

### 1.3 Thousands Separator

Thai uses the **comma (,)** as the thousands separator, identical to English:

- 1,234,567.89

### 1.4 Negative Numbers

Use the minus sign (-) placed immediately before the number with no space:

- -25.5
- -1,000

### 1.5 Percentages

Use the percent sign (%) directly after the number with no space. In formal Thai prose, the word ร้อยละ (roy-la) is preferred over the % symbol:

- 25% or ร้อยละ 25 (preferred in formal documents)
- Note: ร้อยละ is followed by a space before the number

### 1.6 Ordinal Numbers

Ordinals use ที่ (thi) + number:

- ที่ 1 (first), ที่ 2 (second), ที่ 3 (third)

The word ลําดับที่ (lam-dap-thi) is used in formal lists.

### 1.7 Fractions

Fractions are expressed as เศษ (numerator) ส่วน (denominator):

- 1/2 -> หนึ่งส่วนสอง or เศษหนึ่งส่วนสอง
- 3/4 -> สามส่วนสี่

---

## 2. Currency

### 2.1 Primary Currency Sign

The Thai Baht sign (฿) is placed **before** the amount with **no space**:

- ฿500
- ฿1,250.75

### 2.2 Currency Code

The ISO 4217 code **THB** is used in international contexts, placed after the amount with a space:

- 500 THB
- 1,250.75 THB

### 2.3 Satang (Subunit)

1 Baht = 100 Satang (สตางค์). Express satang after the decimal point:

- ฿25.50 (twenty-five baht fifty satang)
- In formal prose: ยี่สิบห้าบาทห้าสิบสตางค์

### 2.4 Written-out Currency

In formal Thai prose, write บาท (baht) after the number and สตางค์ (satang) after the fractional part:

- จำนวนเงิน 500 บาท (amount: 500 baht)
- จำนวนเงิน 125.75 บาท (one hundred twenty-five baht seventy-five satang)

### 2.5 Foreign Currencies

Retain the original currency symbol or use the three-letter ISO code. On first mention in a document, consider providing the Thai name in parentheses:

- $50 or USD 50 (ดอลลาร์สหรัฐ)
- EUR 100 (ยูโร)

---

## 3. Date and Time

### 3.1 Buddhist Era (พ.ศ.)

Thailand uses the **Buddhist Era (พ.ศ. = พุทธศักราช)** which is **543 years ahead** of the Gregorian calendar (ค.ศ.):

- พ.ศ. = ค.ศ. + 543
- ค.ศ. 2025 = พ.ศ. 2568
- ค.ศ. 2026 = พ.ศ. 2569

**CRITICAL RULE (Zero-Tolerance):** Buddhist Era year conversion is mandatory. A missing or incorrect BE year conversion is a critical error. Always add 543 to the Gregorian year when converting to พ.ศ.

### 3.2 Standard Thai Date Format

The standard formal Thai date format is:

**วันที่ DD เดือน MonthName พ.ศ. YYYY**

Example: วันที่ 15 เดือนมกราคม พ.ศ. 2568

The month name is the Thai name (not a number), and the year is in Buddhist Era.

### 3.3 Short/Numeric Date Format

The numeric format is: **DD/MM/YYYY** (day/month/year, not month/day/year)

- 15/01/2568 (January 15, 2025 BE)
- Note: The year is in Buddhist Era even in numeric format

### 3.4 Thai Month Names

| English    | Thai Month (เดือน) | Abbreviation |
|------------|-------------------|--------------|
| January    | มกราคม            | ม.ค.         |
| February   | กุมภาพันธ์        | ก.พ.         |
| March      | มีนาคม            | มี.ค.        |
| April      | เมษายน            | เม.ย.        |
| May        | พฤษภาคม           | พ.ค.         |
| June       | มิถุนายน          | มิ.ย.        |
| July       | กรกฎาคม           | ก.ค.         |
| August     | สิงหาคม           | ส.ค.         |
| September  | กันยายน           | ก.ย.         |
| October    | ตุลาคม            | ต.ค.         |
| November   | พฤศจิกายน         | พ.ย.         |
| December   | ธันวาคม           | ธ.ค.         |

### 3.5 24-Hour Time Format

Thai formal documents use the **24-hour clock** (ไม่ใช้ a.m./p.m.):

- 09:30 น. (9:30 a.m.)
- 14:45 น. (2:45 p.m.)
- 00:00 น. (midnight)
- 12:00 น. (noon)

The particle น. (นาฬิกา) follows the time.

### 3.6 Traditional Time (6-hour clock)

In informal speech, a traditional 6-hour clock system exists but should **NOT** be used in formal translation. Only use the 24-hour format.

### 3.7 Days of the Week

| English  | Thai      | Abbreviation |
|----------|-----------|--------------|
| Monday   | วันจันทร์ | จ.           |
| Tuesday  | วันอังคาร | อ.           |
| Wednesday| วันพุธ    | พ.           |
| Thursday | วันพฤหัสบดี | พฤ.        |
| Friday   | วันศุกร์  | ศ.           |
| Saturday | วันเสาร์  | ส.           |
| Sunday   | วันอาทิตย์ | อา.         |

---

## 4. Addresses

### 4.1 Thai Address Structure (Top-Down)

Thai addresses are written from **smallest to largest unit** (opposite of Western format):

```
บ้านเลขที่ 123 หมู่ที่ 4
ซอย/ตรอก [soi/alley name]
ถนน [street name]
ตำบล/แขวง [sub-district]
อำเภอ/เขต [district]
จังหวัด [province]
รหัสไปรษณีย์ [postal code]
```

### 4.2 Address Components

| English Term      | Thai Translation       | Abbreviation |
|-------------------|------------------------|--------------|
| House number      | บ้านเลขที่              | -            |
| Village/Group     | หมู่ที่ / หมู่บ้าน      | ม.           |
| Alley/Lane        | ซอย                    | ซ.           |
| Street/Road       | ถนน                    | ถ.           |
| Sub-district      | ตำบล (rural) / แขวง (urban) | ต. / แขวง |
| District          | อำเภอ (rural) / เขต (urban) | อ. / เขต |
| Province          | จังหวัด                 | จ.           |
| Postal code       | รหัสไปรษณีย์            | -            |

### 4.3 Address Translation Rule

When translating an address from a Western format, **reverse the order** from largest-to-smallest (source) to smallest-to-largest (Thai). For foreign addresses being kept in original format, add "ประเทศ [country]" at the end if needed.

### 4.4 Prefixes for Locations

Use the classifier/prefix words before place names:

- จังหวัดเชียงใหม่ (NOT เชียงใหม่ alone in formal address)
- กรุงเทพมหานคร (full formal name for Bangkok)
- อนุรักษ์ village name as-is

---

## 5. Proper Nouns

### 5.1 Thai Romanization (RTGS)

The **Royal Thai General System of Transcription (RTGS)** is the official system for transcribing Thai into Latin script. Key rules:

- No tone marks in RTGS
- No vowel length distinction
- Uses specific consonant mappings (e.g., ค -> kh, ฆ -> kh, ท -> th, ฒ -> th)

**Rule:** When a Thai proper noun has an established RTGS form (e.g., Bangkok = กรุงเทพฯ, Chiang Mai = เชียงใหม่), use the well-known spelling. For lesser-known terms, apply RTGS consistently.

### 5.2 Royal and Noble Titles

| Title           | Thai           | Usage Context                          |
|-----------------|----------------|----------------------------------------|
| King            | พระบาทสมเด็จพระเจ้าอยู่หัว | Full formal reference      |
| Queen           | สมเด็จพระนางเจ้าฯ            | Full formal reference      |
| Prince/Princess | สมเด็จพระเจ้าลูกเธอ เจ้าฟ้าฯ | Varies by rank           |
| Royal family    | พระบรมวงศานุวงศ์             | Collective reference       |

**Critical Rule:** Royal references require ราชาศัพท์ (royal vocabulary). Never use ordinary verbs for royal actions. Use specialized royal vocabulary (see Section 9).

### 5.3 Foreign Names

Transliterate foreign names into Thai based on **pronunciation**, not spelling. Use the most widely accepted Thai form if one exists. For less common names, apply a consistent phonetic transcription using Thai consonant and vowel mappings.

- **Preserve** the original name in parentheses (or Latin script) on first mention if the name is non-obvious.
- Do **NOT** translate personal names semantically.
- For East Asian names (Chinese, Japanese, Korean), use the established Thai transcription if one exists.

### 5.4 Geographic Names

Use the standard Thai name for well-known locations:

- England -> ประเทศอังกฤษ (not a phonetic rendering of "England")
- France -> ประเทศฝรั่งเศส
- United States -> สหรัฐอเมริกา or สหรัฐฯ

For lesser-known locations, transliterate phonetically and add the geographic classifier (จังหวัด, เมือง, ประเทศ).

### 5.5 Organizational Names

Translate the organizational type but keep the proper name in transcription:

- "Harvard University" -> มหาวิทยาลัยฮาร์วาร์ด
- "United Nations" -> องค์การสหประชาชาติ (fully translated)

If an organization has an official Thai name, use that (do not retransliterate).

---

## 6. Punctuation

### 6.1 Sentence Spacing

**Thai has no explicit word spacing between words** in a sentence. Spaces appear only:

- Between sentences (as in Latin scripts)
- Before and after certain punctuation
- Around numbers and units in some contexts
- To separate items in lists

**Critical Rule:** Do NOT insert spaces between Thai words within a sentence. Only use spaces at sentence boundaries and where punctuation requires them.

### 6.2 ไม้ยมก (ๆ) — Repetition Mark

ๆ (ไม้ยมก, mai-yamok) indicates that the preceding word or phrase is repeated:

- เด็ก ๆ (dek dek = children, lit. child child)
- เร็ว ๆ (reo reo = quickly, lit. fast fast)
- สวย ๆ (suay suay = beautiful, lit. beautiful beautiful)

**Usage rule:** No space before ๆ. The mark is placed immediately after the word being repeated. When ๆ falls at the end of a sentence, the sentence-ending space or punctuation follows normally.

### 6.3 ไปยาลน้อย (ฯ) — Abbreviation Mark

ฯ (ไปยาลน้อย, pai-yan-noi) marks an abbreviation or shortened form:

- กรุงเทพฯ (Bangkok, shortened from กรุงเทพมหานคร)
- ฯ is placed at the end of the shortened word with no preceding space.

### 6.4 ไปยาลใหญ่ (ฯลฯ) — Etcetera Mark

ฯลฯ (ไปยาลใหญ่, pai-yan-yai) means "etc." and is used to indicate that a list continues:

- สินค้า ได้แก่ โทรศัพท์ คอมพิวเตอร์ ฯลฯ

Usage: A space precedes ฯลฯ (or it follows a space after the last list item). The mark itself contains no internal spaces.

### 6.5 Angle Quotes

Thai uses **angle quotation marks** (เครื่องหมายอัญประกาศ) for quotations:

- « » (left/right double angle quotes) — for main quotations
- ‹ › (single angle quotes) — for nested quotations

In practice, Thai documents also accept the Latin quotation marks " " (double) and ' ' (single), especially in digital contexts. **Choose one system and be consistent.**

### 6.6 Other Punctuation Marks

| Mark    | Thai Name           | Usage                                           |
|---------|---------------------|-------------------------------------------------|
| .       | มหัพภาค (full stop) | End of sentence, abbreviations, decimal point   |
| ,       | จุลภาค (comma)      | Separating items, thousands separator           |
| ?       | ปรัศนี (question)   | Direct questions (same as English)              |
| !       | อัศเจรีย์ (exclamation) | Exclamations (same as English)              |
| :       | ทวิภาค (colon)      | Introducing lists, explanations                 |
| ;       | อัฒภาค (semicolon)  | Separating related clauses                      |
| -       | ยัติภังค์ (hyphen)   | Compound words, line breaks                     |
| —       | เส้นประ (em dash)   | Parenthetical phrases or emphasis               |

### 6.7 วรรคตอน (Whitespace Rules)

- One space between sentences (NOT two spaces as in some English styles)
- No space before punctuation marks
- One space after punctuation marks (period, comma, colon, semicolon)
- No space inside parentheses or quotation marks with the enclosed text
- Spaces around em dashes ( — ), not attached

---

## 7. Formatting

### 7.1 Paragraph Conventions

Thai paragraphs follow the same structural logic as English paragraphs (one main idea per paragraph). Key differences:

- **No indentation** at the start of paragraphs in modern digital Thai documents (traditional manuscripts may have an initial indentation).
- Paragraphs are separated by a blank line (one line space).
- Justified alignment is common in formal documents.

### 7.2 List Markers

Bullet lists use standard markers:

- Hyphen ( - ) with space after
- Bullet (•) with space after
- Numbered lists: 1. 2. 3. (Arabic numerals followed by a period and space)
- Lettered lists: ก. ข. ค. (Thai consonants in alphabetical order)

### 7.3 Table Formatting

- Tables should be left-aligned or justified
- Headers are typically bold
- Column alignment follows content type (numbers right-aligned, text left-aligned)
- Thai text in table cells follows all the same spacing and punctuation rules as running text

### 7.4 Headings

Use a hierarchical heading structure (e.g., ## for section, ### for subsection). Headings in Thai should be concise and parallel in structure.

### 7.5 Emphasis

- **Bold** for strong emphasis and key terms
- *Italic* for foreign words, titles, and secondary emphasis
- Underline used sparingly (mostly in handwritten contexts)

---

## 8. Grammar

### 8.1 Word Order (SVO)

Thai is an **SVO (Subject-Verb-Object)** language, like English:

- ฉัน กิน ข้าว (I eat rice)
- เขา อ่าน หนังสือ (He reads a book)

Maintain SVO order in translation. Do not rearrange to match the source language's syntax (e.g., German SOV, Japanese SOV) unless the meaning demands it.

### 8.2 No Verb Conjugation

Thai verbs do **not** conjugate for:

- **Tense:** Expressed through time words (เมื่อวาน = yesterday, พรุ่งนี้ = tomorrow) or aspect markers (กำลัง = -ing, แล้ว = already)
- **Number:** The verb does not change for singular/plural subjects
- **Person:** No change for first/second/third person
- **Gender:** No gender agreement on verbs

### 8.3 No Noun Declension

Nouns do not change form for case, number, or gender. Plurals are expressed through:

- Repetition (เด็ก ๆ = children)
- Plural words (หลาย = many, ทั้งหลาย = all)
- Classifiers (see 8.4)
- Context

### 8.4 Classifiers (คำลักษณนาม)

Thai requires **classifiers** when counting or specifying nouns with numbers. The structure is:

**Noun + Number + Classifier**

| Noun          | Classifier | Example               | Translation          |
|---------------|------------|-----------------------|----------------------|
| คน (person)   | คน         | คน 3 คน               | three people         |
| รถ (car)      | คัน        | รถ 2 คัน              | two cars             |
| หนังสือ (book)| เล่ม       | หนังสือ 5 เล่ม        | five books           |
| ผลไม้ (fruit) | ผล / ลูก  | ผลไม้ 4 ผล            | four fruits          |
| ดินสอ (pencil)| แท่ง       | ดินสอ 3 แท่ง          | three pencils        |
| ต้นไม้ (tree) | ต้น        | ต้นไม้ 2 ต้น          | two trees            |
| จดหมาย (letter)| ฉบับ     | จดหมาย 3 ฉบับ         | three letters        |
| สัตว์ (animal) | ตัว       | สัตว์ 10 ตัว          | ten animals          |
| ใบไม้ (leaf)  | ใบ         | ใบไม้ 5 ใบ            | five leaves          |

**Critical rule:** Never omit the classifier when using a number with a noun. "คน 3" (without คน as classifier) is grammatically incomplete. The pattern "สามคน" without a number word is acceptable (just the number + classifier).

### 8.5 Particles (คำลงท้าย)

Thai uses sentence-final particles to indicate politeness, mood, and question type:

| Particle | Gender of Speaker | Meaning/Function              |
|----------|-------------------|-------------------------------|
| ครับ     | Male              | Polite statement/answer       |
| คะ       | Female            | Polite question               |
| ค่ะ      | Female            | Polite statement/answer       |
| จ๊ะ      | Either (informal) | Familiar/affectionate         |
| จ้ะ / จ๋า| Either (informal) | Emphatic familiar             |
| นะ       | Either            | Softening/emphasis/suggestion |
| สิ       | Either            | Emphasis/encouragement        |

**Rule in formal translation:** Use ครับ for male speakers and ค่ะ for female speakers consistently.

### 8.6 Negation

Negation uses **ไม่** (mai) placed immediately before the verb:

- ฉันไม่กิน (I do not eat)
- เขาไม่มา (He is not coming)

Double negatives are possible but stylistically avoided in formal Thai.

### 8.7 Questions

Questions are formed through:

- Question particles: ไหม (mai, yes/no), หรือ (rue, or), หรือไม่ (rue-mai)
- Question words: ใคร (who), อะไร (what), ที่ไหน (where), เมื่อไร (when), ทําไม (why), อย่างไร (how)
- The question mark (?) is used in written Thai (less common in traditional texts but standard in modern writing)

---

## 9. Formality

### 9.1 Register Overview

Thai has a multi-layered register system. Formal written Thai sits between everyday spoken Thai and royal/ceremonial Thai.

| Register          | Usage Context                             | Key Features                    |
|-------------------|-------------------------------------------|---------------------------------|
| ภาษาทางการ (Formal) | Official documents, news, academic writing | Polite particles, full词汇 |
| ภาษากึ่งทางการ (Semi-formal) | Business correspondence, reports | Polite particles, some formal vocabulary |
| ภาษาพูด (Colloquial) | Everyday conversation                   | No polite particles needed, shortened forms |
| ราชาศัพท์ (Royal) | Referring to royalty                     | Specialized vocabulary          |

**Rule:** Target **formal register (ภาษาทางการ)** for translated documents unless context explicitly requires otherwise.

### 9.2 ราชาศัพท์ (Royal Vocabulary)

ราชาศัพท์ is a specialized vocabulary set used when speaking **to** or **about** royalty. Key categories:

**Verbs for Royal Actions (replacing ordinary verbs):**

| Ordinary Thai | ราชาศัพท์        | English Meaning    |
|---------------|------------------|--------------------|
| กิน            | เสวย              | eat                |
| นอน           | บรรทม             | sleep              |
| พูด           | ตรัส              | speak              |
| ให้            | พระราชทาน        | give               |
| ไป            | เสด็จ             | go                 |
| อยู่          | ประทับ            | stay/be (located)  |
| รู้            | ทรงทราบ           | know               |
| ตาย          | สวรรคต            | die (king/queen)   |
| ตาย          | ทิวงคต            | die (prince/princess) |

**Nouns with Royal Prefixes:**

Add พระราช (phra-rach), พระ (phra), or ราช (rach) prefixes:

- รถ (car) -> พระราชยาน (royal vehicle)
- หนังสือ (book) -> หนังสือหลวง or พระราชนิพนธ์ (if authored by royalty)
- คําสั่ง (order) -> พระราชโองการ (royal command)

**Critical rule:** If the source text refers to a Thai monarch or royal family member, ราชาศัพท์ is mandatory. Omission is a critical error.

### 9.3 Polite Particles in Formal Writing

Every declarative sentence in formal Thai should end with a polite particle:

- ครับ (male speaker/writer)
- ค่ะ (female speaker/writer)

**Rule:** Add polite particles to the end of each sentence in the target text when the register is formal, regardless of whether the source language has such particles.

### 9.4 Honorifics

| Term      | Usage                                                       |
|-----------|-------------------------------------------------------------|
| คุณ (khun) | General honorific for Mr./Mrs./Ms. placed before the name  |
| นาย (nai)  | Formal title for men (Mr.)                                 |
| นาง (nang) | Formal title for married women (Mrs.)                       |
| นางสาว (nang-sao) | Formal title for unmarried women (Ms.)           |
| ดร. (do-ro) | Doctor (academic or medical)                              |
| ศ. (so.)   | Professor (ศาสตราจารย์)                                    |
| รศ. (ro-so.) | Associate Professor (รองศาสตราจารย์)                    |
| ผศ. (pho-so.) | Assistant Professor (ผู้ช่วยศาสตราจารย์)               |

Honorifics are placed **before** the full name.

### 9.5 Pronouns in Formal Thai

| Person   | Formal Pronoun | Notes                                    |
|----------|----------------|------------------------------------------|
| I (male) | ผม             | Default for male speakers                |
| I (female)| ดิฉัน         | Default for female speakers              |
| You      | ท่าน           | Very formal "you"                        |
| You      | คุณ            | Standard formal "you"                    |
| He/She   | เขา            | Standard third-person pronoun            |
| They     | พวกเขา         | Standard third-person plural             |

Avoid using informal pronouns (กู, มึง, ฉัน [informal]) in formal translations.

---

## 10. OCR Artifacts

### 10.1 Handling Unrecoverable Text

When source text is damaged or illegible (e.g., from a scanned document with physical damage, faded ink, or OCR corruption), use the following format:

```
[กู้คืน: description of what was recovered or uncertain]
```

### 10.2 Standard Recovery Markers

| Marker                                     | Meaning                          |
|--------------------------------------------|----------------------------------|
| [กู้คืน: ไม่สามารถระบุข้อความได้]          | Text could not be identified     |
| [กู้คืน: ข้อความบางส่วนเสียหาย]           | Partial text damage              |
| [กู้คืน: ต้องมีการตรวจสอบ]                 | Needs verification               |
| [กู้คืน: ข้อความในต้นฉบับเลือนราง]        | Original text is faint/blurred   |
| [กู้คืน: คาดว่า...]                         | Best guess follows               |

### 10.3 Preservation Rules

- OCR artifacts (garbled characters, stray marks, misrecognized glyphs) should be **identified and flagged**, not silently corrected unless certainty is high.
- If a word is clearly an OCR error (e.g., "0" misrecognized as "O" in a numeric context), correct it silently and add no note.
- If uncertainty remains, use the [กู้คืน: ...] format.
- Do NOT propagate OCR errors from the source into the target text.

### 10.4 Structural Artifacts

- Page numbers, headers, and footers from the source should be preserved in the output format.
- If the source has multi-column layout that OCR incorrectly linearized, restore the correct reading order when possible.
- Tables that were flattened by OCR should be reconstructed as tables.

---

## 11. Translation Philosophy

### 11.1 Natural Thai (ภาษาไทยที่เป็นธรรมชาติ)

The primary goal is to produce Thai that reads as if it were **originally written in Thai**, not translated. Avoid:

- **Calques** (literal structural borrowings from the source language)
- **Syntactic inversion** that follows the source word order when unnatural in Thai
- **Foreign punctuation patterns** (e.g., English comma splices)
- **Overuse of possessive constructions** (ของ) when Thai would use juxtaposition

### 11.2 Polite Register

Maintain a **consistently polite register** throughout:

- End sentences with ครับ/ค่ะ
- Use คุณ or ท่าน for "you"
- Use formal vocabulary choices over colloquial equivalents
- Err on the side of politeness when register is ambiguous

### 11.3 Avoiding Literal Structure

Do NOT translate word-for-word. Thai and the source language may share SVO order, but:

- Relative clause structure differs (Thai uses ที่ + clause)
- Serial verb constructions are common in Thai but rare in English
- Topic-comment structure is more frequent in Thai
- Thai prefers active voice over passive voice (use ถูก only for adversative passives)

### 11.4 Readability Over Fidelity

When a trade-off is necessary:

1. **Clarity and naturalness** in Thai take priority over preserving source syntax
2. **Terminology accuracy** takes priority over stylistic elegance
3. **Semantic fidelity** (meaning) takes priority over lexical fidelity (word choice)
4. **Format compliance** (dates, numbers, polite particles) is non-negotiable

### 11.5 Adapting Cultural References

- Idioms: Replace with Thai equivalents that convey the same meaning, not a literal translation
- Measurements: Convert to metric (Thai uses metric system). If the source uses imperial, convert and label.
- Proper nouns: See Section 5
- Legal/administrative concepts: Use the closest Thai equivalent and add a translator's note if needed

### 11.6 Consistency

Within a single document:

- Use the same Thai term for the same source term throughout (establish a glossary)
- Maintain consistent register (do not switch between formal and colloquial)
- Use consistent date/time format (once you choose a format, do not vary)
- Apply the same classifier for the same noun every time it is counted

### 11.7 Review Checklist

Before finalizing a translation, verify:

- [ ] All years converted to พ.ศ. (+543)?
- [ ] Polite particles (ครับ/ค่ะ) present on all sentences?
- [ ] Thai numerals vs Arabic numerals consistent?
- [ ] Classifiers correct for all counted nouns?
- [ ] Addresses reversed (smallest to largest)?
- [ ] Royal vocabulary applied where needed?
- [ ] No extraneous word spacing inside sentences?
- [ ] Date format consistent throughout?
- [ ] All OCR artifacts flagged with [กู้คืน: ...]?
- [ ] Translation reads as natural Thai, not source-language calque?

---

> **Document Version:** 1.0
> **Last Updated:** 2026-05-25
> **Scope:** Knowledge base for Thai translation tasks in the translating-documents skill.
