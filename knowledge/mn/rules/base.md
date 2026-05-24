---
id: mn/rules/base
type: rules
target_lang: mn
name: Mongolian (Cyrillic) Base Translation Rules
description: Universal rules for translating any source language into Mongolian (Cyrillic script, as used in Mongolia)
---

## Монгол Кирилл Цагаан Толгой / Mongolian Cyrillic Alphabet

Mongolian Cyrillic has 35 letters (33 Russian + Өө and Үү). Written left-to-right.

**Vowels (13):** Аа, Ээ, Ии, Оо, Уу, Өө, Үү, Яя, Ее, Ёё, Юю, ы, ь
**Long vowels:** Written as doubled (аа, ээ, ий, оо, уу, өө, үү)
**Key distinction:** Өө /o/ and Үү /u/ are unique to Mongolian — ensure correct encoding (UTF-8).

### Vowel Harmony (Эгшиг Зохицох Ёс)

All native Mongolian words follow vowel harmony. Suffixes change form based on root vowels:

| Category | Vowel Group | Vowels | Suffix Vowels |
|----------|------------|--------|---------------|
| Male (back) | эр | А, О, У, Я, Ё, Ю | а, о, у |
| Female (front) | эм | Э, Ө, Ү, Е | э, ө, ү |
| Neutral | саармаг | И, ь | Usually treated as female |

**Rule:** A word contains only male OR only female vowels (never mixed). Suffixes harmonize accordingly.
- Male root → male suffix: аав-аас "from father"
- Female root → female suffix: ээж-ээс "from mother"
- Loanwords may break harmony; this is acceptable for proper nouns.

## Word Order

Mongolian is strictly **SOV** (Subject-Object-Verb). This is the most critical structural difference from SVO source languages.

- The main verb ALWAYS goes to the end of the clause
- All modifiers precede what they modify
- Postpositions replace prepositions
- Questions use particles (-уу/-үү, -бэ/-вэ) at clause end

## Case System (Тийн Ялгал)

Mongolian has 7 cases, marked by suffixes:

| Case | Suffix (male/female) | Function |
|------|---------------------|----------|
| Nominative | (none) | Subject, indefinite object |
| Genitive | -ын/-ийн/-ы/-ны/-гийн | Possession |
| Dative-Locative | -д/-т | Location, direction, indirect object |
| Accusative | -ыг/-ийг/-г | Definite direct object |
| Ablative | -аас/-ээс/-оос/-өөс | From, than (comparison) |
| Instrumental | -аар/-ээр/-оор/-өөр | By, with, via |
| Comitative | -тай/-тэй/-той | With, together with |

**Note:** Accusative is only used for DEFINITE objects. Indefinite objects use nominative form.

## Number Format

- Preserve all numerical values exactly — do NOT round, convert, or recalculate
- Decimal separator: `. ` (period) — e.g., 3.14
- Thousands separator: space or comma — e.g., 1 500 000 or 1,500,000
- Chinese 万 (10,000) and 亿 (100,000,000): convert to numeric values
- Percentages: number + space + % — e.g., 35 %
- Ordinals: suffix -дугаар/-дүгээр — e.g., 1-р, 2-р

## Currency

- Keep original currency values; do not convert
- Mongolian Tugrik: ₮ (MNT)
- Foreign currency: keep ISO code or symbol — e.g., ¥35 тэрбум (CNY)
- Symbol before or after amount: ₮5000 or 5000 ₮

## Date and Time

- Formal: `YYYY оны MM сарын DD өдөр` — e.g., 2024 оны 5 сарын 15 өдөр
- Business: `YYYY.MM.DD` — e.g., 2024.05.15
- Month names are ordinal: 1-р сар, 2-р сар, ..., 12-р сар
- Preserve exact date values — do not shift dates
- Year + event: `1998 онд` — e.g., 1998 онд байгуулагдсан

## Addresses

- Preserve original address structure
- Transliterate Chinese place names to Cyrillic using standard conventions
- Add country name for clarity: БНХАУ (PRC), Монгол Улс (Mongolia)

## Proper Nouns

- **People names:** Transliterate from Pinyin to Cyrillic — e.g., 姚晨 → Яо Чэнь
- **Company names:** Keep Latin form first mention with Cyrillic transliteration — e.g., Leyuan Health (Лө Юань Эрүүл Мэнд)
- **Brand names:** Transliterate; add explanatory translation in parentheses on first mention
- **Place names:** Use standard Cyrillic forms — e.g., 浙江 → Жөжян, 杭州 → Ханжоу
- **Acronyms (ISO, HACCP, NFC, etc.):** Keep as-is; translate full name on first mention

## Punctuation

- Quotation marks: « » (guillemets, no internal spaces) — replace all "" and 「」 
- Nested quotes: «...„ "...» 
- Em dash — : no spaces — текст—текст
- En dash – : ranges — 2020–2025
- Chinese enumeration comma 、→ standard comma , or conjunction болон/ба
- Chinese full-width punctuation → half-width: ，→ ,  。→ .  ：→ :
- No spaces before punctuation; one space after . , ; : ! ?

## Formatting

- Preserve heading hierarchy (#, ##, ###, etc.)
- Preserve list formatting (bulleted, numbered)
- Preserve table structure where applicable
- Maintain paragraph breaks as in the source
- Bullet points: use — (em dash) or • consistently

## Grammar

- SOV word order: restructure all clauses
- Agglutination: Chinese compound nouns become suffixed Mongolian words
- No articles (Mongolian has none)
- No grammatical gender
- No systematic classifier/measure word system — numeral + noun directly
- Connect parallel clauses with бөгөөд (and), ба/болон (and)
- Use converbs (-ж/-ч, -аад/-ээд, -вал/-вэл, -н, -аар/-ээр) for subordinate clauses

## Formality

- Use formal register for business and official documents
- Second person: use Та (formal "you") not Чи (informal)
- Topic marker: use нь/бол after the subject
- Predicative: use юм, байна, болно as sentence-final markers
- Avoid colloquial contractions in formal text

## OCR Artifacts

- If a word appears corrupted or nonsensical, do NOT silently guess
- Mark with inference tag: `[ inferred: original "{word}", contextually inferred as "{correction}", {reason} ]`
- If uncertain, keep the original and flag: `[ OCR: unable to determine original intent ]`

## Translation Philosophy: 信达雅 (Үнэнч, Ойлгомжтой, Гоёмсог)

- **Faithfulness (信 / Үнэнч байдал):** Faithfully convey the original meaning — no additions, no omissions. Numerical values, dates, proper nouns must be exact.
- **Expressiveness (达 / Ойлгомжтой байдал):** Write as a native Mongolian speaker would. Avoid translationese. Restructure for natural SOV flow.
- **Elegance (雅 / Гоёмсог байдал):** Pursue linguistic quality appropriate to the document type. Formal documents should be dignified; commercial documents should flow smoothly.

Priority: Faithfulness > Expressiveness > Elegance.

## Creative Language Strategies

### Chinese Idioms (成语) in Mongolian

Chinese four-character idioms have no direct Mongolian equivalent. Strategies (in order of preference):
1. Find equivalent Mongolian proverb/saying
2. Explain the meaning in plain Mongolian prose
3. Paraphrase while keeping the core message

Examples:
- 正心诚意 → чин сэтгэл, шударга санаа
- 知行合一 → мэдлэг, үйл хэргийн нэгдэл
- 惠人达己 → бусдад туслахуй, өөртөө хүрэхүй
- 精益求精 → тасралтгүй сайжруулах

### Slogan Translation
1. Never translate slogans literally — recreate the impact
2. Analyze the original rhetoric (rhyme, parallelism, hyperbole)
3. Recreate equivalent slogan in Mongolian preserving the core message
4. Chinese parallelism (对仗) cannot be replicated in Mongolian — prioritize clarity over form

### Brand Name Localization
- Transliterate from Pinyin to Cyrillic (not from Chinese characters)
- Keep established Latin brand names alongside Cyrillic
- Add explanatory translation on first mention

## Source Quality Issues

### OCR Errors
- Common patterns in Chinese: similar-looking characters, missing strokes
- Strategy: Infer correct text from context, mark with `[推断: ...]` tag
- Do NOT preserve OCR errors in the translation

### Incomplete / Truncated Text
- Mark truncation with `[...]`
- Do NOT fabricate content to complete truncated sections

### Mixed-language Documents
- Keep English/Latin terms (acronyms, brand names) as-is in Mongolian text
- Transliterate Chinese terms to Cyrillic
- Numbers and dates follow target conventions

## Spatial Expansion

Mongolian translations are typically **30-50% longer** than Chinese source text due to agglutination and grammatical explicitness. Plan accordingly for any layout-constrained output.
