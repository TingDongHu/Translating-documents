---
id: bn/rules/base
type: rules
target_lang: bn
name: Bengali Translation Base Rules
description: Bengali base translation rules
---

# Bengali Translation Base Rules

This document defines the foundational rules for translating documents into Bengali (বাংলা). All translations MUST conform to these rules unless explicitly overridden by project-specific instructions.

---

## 1. Number Format

### 1.1 Indian Numbering System (Primary)
- Bengali texts commonly use the **Indian numbering system** with comma grouping: `1,00,000` (1 lakh), `10,00,000` (10 lakh), `1,00,00,000` (1 crore).
- The first group from the right is three digits; subsequent groups are two digits each.
- Example: `12,34,56,789` (not `123,456,789`).

### 1.2 Western Numbering System (Secondary)
- Western grouping (`100,000`, `1,000,000`) is also understood, especially in international and technical contexts.
- Use Indian system as default unless the target audience is international or the source uses Western grouping.

### 1.3 Decimal Separator
- The **decimal point** (`.`) is used in Bengali: `3.14`, `0.25`, `12.5`.
- No comma as decimal separator — Bengali follows the English convention.

### 1.4 Thousands Separator
- In Indian system, comma after the first three digits from the right, then every two: `1,00,000`.
- No thousands separator is used after the decimal point.

### 1.5 Negative Numbers
- Negative numbers use the minus sign (`-`) placed directly before the digits: `-5`, `-3.14`.
- In financial contexts, parentheses may indicate negatives: `(1,00,000)`.

### 1.6 Percentages
- The percent symbol (`%`) is placed **after** the number with a space: `25 %` or `25%`.
- Both forms are acceptable; choose one and maintain consistency.
- Percentage ranges: `10%–20%` or `10% থেকে 20%`.

### 1.7 Ordinal Numbers
- Ordinal numbers in Bengali use suffixes: `-তম` (masculine) or `-তমা` (feminine), or the more common `-তম`.
- Examples: `1st` → `1ম` or `প্রথম`, `2nd` → `2য়` or `দ্বিতীয়`, `3rd` → `3য়` or `তৃতীয়`.
- In running text, Bengali ordinals are commonly written with Bengali numerals: `১ম`, `২য়`, `৩য়`.

### 1.8 Numerals in Text
- Numbers from one to ten (or up to twelve) may be written as words in running text: `এক`, `দুই`, `তিন`, `চার`, `পাঁচ`.
- Larger numbers are written as digits: `42`, `1,250`.
- Consistency within a sentence or paragraph takes precedence.
- A sentence may begin with a digit in Bengali (unlike some other languages).

### 1.9 Bengali Numerals
- Bengali has its own numeral system: `০ ১ ২ ৩ ৪ ৫ ৬ ৭ ৮ ৯`.
- Bengali numerals are used in formal and literary Bengali, especially in Bangladesh.
- Western Arabic numerals (`0 1 2 3 4 5 6 7 8 9`) are widely used in technical, financial, and international contexts.
- In modern business and technical documents, Western Arabic numerals are preferred. Bengali numerals are preferred in literary, governmental, and cultural contexts.

---

## 2. Currency

### 2.1 Bangladeshi Taka (BDT/৳)
- Symbol: `৳` (Unicode U+09F3) or `BDT`.
- **Symbol placement**: The currency symbol may be placed **before** the amount: `৳500`, `BDT 500`.
- ISO code in technical/financial contexts: `BDT 500`.
- Taka amounts use two decimal places for financial contexts: `৳500.00`.

### 2.2 Indian Rupee (INR/₹)
- Symbol: `₹` (Unicode U+20B9) or `INR`.
- **Symbol placement**: Before the amount: `₹500`, `INR 500`.
- Used in Bengali translations concerning West Bengal (India) context.

### 2.3 US Dollar
- Symbol: `$`.
- Placement: Before the amount: `$100`, `USD 100`.
- Alternative: `US$100` to distinguish from other dollar currencies.

### 2.4 Euro
- Symbol: `€`.
- Placement: Before the amount: `€100`, `EUR 100`.

### 2.5 Currency Translation Rules
- Translate currency names in running text: "dollars" → `ডলার`, "euros" → `�উরো`, "pounds" → `পাউন্ড`.
- Maintain original currency amounts; do NOT convert currencies unless explicitly instructed.
- Use ISO 4217 codes for less common currencies.

### 2.6 Formatting Rules
- Decimal point applies to all currency amounts: `৳500.50` (not `৳500,50`).
- Indian comma grouping applies: `৳1,00,000` (not `৳100,000`).
- Use exactly two decimal places for financial amounts when precision is required: `৳50.00`.

---

## 3. Date and Time

### 3.1 Date Format
- Common Bengali date format: **DD/MM/YYYY** (day/month/year).
- ISO format also accepted: **YYYY-MM-DD**.
- Example: `27/05/2026` or `2026-05-27`.
- Leading zeros are used for single-digit days and months: `01/04/2026`.

### 3.2 Bengali Calendar Dates
- Bengali calendar (বাংলা পঞ্জিকা / Bangla Panjika) is used in Bangladesh and West Bengal.
- Bengali calendar months: বৈশাখ, জ্যৈষ্ঠ, আষাঢ়, শ্রাবণ, ভাদ্র, আশ্বিন, কার্তিক, অগ্রহায়ণ, পৌষ, মাঘ, ফাল্গুন, চৈত্র.
- Bengali calendar year 1433 corresponds approximately to 2026 CE.
- When Bengali calendar dates appear, preserve them: `১৪৩২ বৈশাখ ১৫`.

### 3.3 Month Names (Bengali)
- Bengali month names (Gregorian calendar):

| English | Bengali | Bengali (Formal) |
|---------|---------|-----------------|
| January | জানুয়ারি | জানুয়ারী |
| February | ফেব্রুয়ারি | ফেব্রুয়ারী |
| March | মার্চ | মার্চ |
| April | এপ্রিল | এপ্রিল |
| May | মে | মে |
| June | জুন | জুন |
| July | জুলাই | জুলাই |
| August | আগস্ট | আগস্ট |
| September | সেপ্টেম্বর | সেপ্টেম্বর |
| October | অক্টোবর | অক্টোবর |
| November | নভেম্বর | নভেম্বর |
| December | ডিসেম্বর | ডিসেম্বর |

- Month names with dates: `২৭ মে ২০২৬` or `27 মে 2026`.

### 3.4 Day Names (Bengali)

| English | Bengali |
|---------|---------|
| Sunday | রবিবার |
| Monday | সোমবার |
| Tuesday | মঙ্গলবার |
| Wednesday | বুধবার |
| Thursday | বৃহস্পতিবার |
| Friday | শুক্রবার |
| Saturday | শনিবার |

### 3.5 Time Format
- **12-hour format** is commonly used in Bengali: `সকাল ১০:৩০`, `রাত ৮:০০`.
- **24-hour format** is used in official and technical contexts: `14:30`, `20:00`.
- Bengali time-of-day terms:

| Bengali | Approximate Period |
|---------|-------------------|
| ভোর | Dawn (4:00–6:00) |
| সকাল | Morning (6:00–12:00) |
| দুপুর | Afternoon (12:00–17:00) |
| বিকাল | Late afternoon (17:00–18:00) |
| সন্ধ্যা | Evening (18:00–20:00) |
| রাত | Night (20:00–4:00) |

- Hours and minutes separated by colon: `১০:৩০` or `10:30`.
- Seconds when included: `14:30:25`.

### 3.6 Combined Date and Time
- Date and time separated by a space: `27 মে 2026, 14:30`.
- Formal: `27 মে 2026 সাল, বিকাল ৪টা ৩০ মিনিট`.

---

## 4. Bengali Script Rules

### 4.1 Unicode Range
- Bengali script occupies Unicode block **U+0980–U+09FF** (Bengali).
- Devanagari (Hindi) occupies a different block (U+0900–U+097F) — do NOT mix scripts.
- Assamese script shares some characters but has distinct forms for ক, খ, গ, ঘ, etc.

### 4.2 Key Bengali Characters
- Vowels (স্বরবর্ণ): অ, আ, ই, ঈ, উ, ঊ, ঋ, এ, ঐ, ও, ঔ.
- Consonants (ব্যঞ্জনবর্ণ): ক, খ, গ, ঘ, ঙ, চ, ছ, জ, ঝ, ঞ, ট, ঠ, ড, ঢ, ণ, ত, থ, দ, ধ, ন, প, ফ, ব, ভ, ম, য, র, ল, শ, ষ, স, হ, ড়, ঢ়, য়, ৎ, ং, ঃ, ঁ.
- The Chandrabindu (ঁ) marks nasalization: `মন্ত্র`, `সঁই`.

### 4.3 Character Spacing
- Bengali is an abugida — vowels modify consonants through diacritics, not separate characters.
- The **hasant** (্) marks consonant conjuncts: `ক্` + `ষ` = `ক্ষ`.
- Proper rendering of conjuncts is critical — incorrect conjuncts change meaning.

### 4.4 Full Stop
- Bengali uses the **dari** (।) as a full stop in formal/literary texts.
- The Latin period (`.`) is commonly used in modern, technical, and business Bengali.
- Use dari (`।`) for literary and formal Bengali; use period (`.`) for technical and international contexts.

---

## 5. Formality and Register

### 5.1 আপনি vs তুমি (Formal vs Informal "You")

| Pronoun | Level | Usage |
|---------|-------|-------|
| আপনি | Formal | Strangers, superiors, elders, customers, professional settings, formal documents |
| তুমি | Informal | Friends, family, children, close colleagues |
| তুই | Intimate/Very informal | Very close friends, children, subordinates (can be rude) |
| আপনারা | Formal plural | Multiple people (formal) |
| তোমরা | Informal plural | Multiple people (informal) |

**Critical rule**: Business, legal, technical, and government documents MUST use `আপনি`. Never use `তুমি` in formal contexts.

### 5.2 Formal Correspondence

| English | Bengali (Formal) |
|---------|-----------------|
| Dear Sir/Madam | সম্মানিত মহোদয়/মহোদয়া |
| Dear Mr. Rahman | সম্মানিত জনাব রহমান |
| Dear Ms. Begum | সম্মানিত জনাবা বেগম |
| To whom it may concern | সংশ্লিষ্ট ব্যক্তি/কর্তৃপক্ষের জন্য |
| Yours faithfully | বিশ্বাসী, / বিনীত, |
| Best regards | শুভেচ্ছান্ত, / সাদর বিনম্র, |
| Sincerely | সৎভাবে, / আন্তরিকভাবে, |

### 5.3 Honorifics and Titles

| Bengali | Usage |
|---------|-------|
| জনাব | Mr. (before name, formal) |
| জনাবা | Ms./Mrs. (before name, formal) |
| মহোদয় | Sir (very formal) |
| মহোদয়া | Madam (very formal) |
| ড. / ডক্টর | Dr. (before name) |
| প্রফেসর | Professor (before name) |
| শ্রী | Mr. (formal, less common than জনাব in Bengali) |

### 5.4 Imperative Mood
- Formal imperative uses `করুন` (please do) or `করবেন` (will do, polite request).
- Informal uses `করো` (you do) or `করোনা` (please do, informal).
- Technical UI uses formal: `ক্লিক করুন` (Click here), `পাসওয়ার্ড লিখুন` (Enter your password).

### 5.5 Register Consistency
- Once a register is chosen (আপনি/তুমি), maintain it throughout the entire document.
- Switching between registers for the same audience is a **major error**.
- Formal register avoids slang, colloquialisms, and contractions.

---

## 6. Punctuation

### 6.1 Bengali-Specific Punctuation
- **Dari (।)**: Used as a sentence terminator in formal/literary Bengali. Equivalent to the Latin period.
- **Question mark (?)**: Same as English, used at the end of interrogative sentences.
- **Exclamation mark (!)**: Same as English.
- **Comma (,)**: Same as English usage.

### 6.2 Quotation Marks
- Bengali uses `"..."` (double quotation marks) as in English.
- Alternative: `«...»` (guillemets) in some formal contexts.
- Single quotation marks: `'...'` for quotes within quotes.

### 6.3 Apostrophe
- Used for English loanwords: `ওয়ার্ক` (work), `ফোন` (phone).
- Not used as a grammatical marker in Bengali (unlike Turkish).

### 6.4 Hyphen and Dash
- Hyphen (`-`) used in compound words and ranges: `১০-১৫`, `১০-১৫`.
- Em dash (`—`) used for parenthetical interruptions.
- No spaces around em dashes.

### 6.5 Ellipsis
- Three dots with no spaces: `...` or with spaces: `. . .`.
- Used for unfinished sentences or omissions.

### 6.6 Parentheses
- Usage is the same as English.
- Period placement: if the parenthetical is a complete sentence, the period goes inside; if a fragment, outside.

---

## 7. Translation Philosophy

### 7.1 Natural Bengali
The primary goal is to produce **natural-sounding Bengali** that reads as if it were originally written in Bengali, not translated from another language.

**Principles:**
- Bengali follows **SOV (Subject-Object-Verb)** word order — verbs come at the end of sentences.
- Avoid calques (direct structural borrowings) from the source language.
- Use idiomatic Bengali expressions where they convey the same meaning.
- Prefer Bengali vocabulary over English loanwords where well-established Bengali equivalents exist.

### 7.2 SOV Word Order
- Bengali is a **Subject-Object-Verb** language.
- English: `I eat rice.` (SVO) → Bengali: `আমি ভাত খাই।` (SOV)
- **Translation implication**: Verb-final structure is mandatory in neutral declarative sentences.
- Placing the verb earlier changes emphasis or creates a marked tone.

### 7.3 Postpositions
- Bengali uses **postpositions** (after the noun) instead of prepositions (before the noun).
- English: `in the house` → Bengali: `ঘরে` (house-in).
- Common postpositions: `-তে` (in/at), `-র` (of), `-ত` (at), `-য়` (in), `-কে` (to/object marker).

### 7.4 Gender
- Bengali has **natural gender** only (masculine and feminine for animate beings).
- No grammatical gender for inanimate objects.
- Verb forms may agree with gender for animate subjects.

### 7.5 Definiteness
- Bengali uses the postposition `-টি` (definite) or `-টা` (informal definite) to mark definiteness.
- English "the" → Bengali `-টি` (formal) or `-টা` (informal): `ঘরটি` (the room), `ঘরটা` (the room, informal).

### 7.6 Sentence Length and Complexity
- Bengali sentences tend to be longer than English sentences, with more subordination.
- For modern business and technical translation, clear and manageable sentence lengths are preferred.
- Break overly long English sentences into shorter Bengali sentences if needed for clarity.

### 7.7 Back-Translation Test
- After translating, consider whether a back-translation to the source language would convey the same meaning.
- If the back-translation would be significantly different in meaning, revise.

### 7.8 Language Register Consistency
- Once a register is chosen, it must be maintained consistently throughout the document.
- Do not mix `আপনি` and `তুমি` for the same audience.
- Do not mix technical and colloquial vocabulary levels unless justified by context.

### 7.9 Untranslatable Elements
- Some elements may legitimately remain in the source language:
  - Brand names and product names: `iPhone`, `Google`, `Samsung`.
  - Foreign titles: `Mr.`, `Mrs.` when referring to foreign individuals.
  - Acronyms: preserve original but provide Bengali expansion on first use if helpful.

---

*End of Bengali Translation Base Rules. These rules should be read in conjunction with the scoring rubric and any project-specific guidelines provided.*
