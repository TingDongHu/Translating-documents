---
id: en/rules/base
type: rules
target_lang: en
name: English Base Translation Rules
description: Universal rules for translating any source language into English
---

## Number Format

- Preserve all numerical values exactly — do NOT round, convert, or recalculate
- Convert number formatting to English conventions:
  - Comma decimal → dot decimal (e.g., 100,00 → 100.00)
  - Dot thousands separator → comma (e.g., 1.234 → 1,234)
  - Space thousands separator → comma (e.g., 1 234 → 1,234)
  - Mixed format (dot thousands + comma decimal): 1.234,56 → 1,234.56
- Keep currency amounts with their original value; only adjust formatting
- Percentages: preserve the value, format per English convention (15.5% not 15,5 %)

## Currency

- "100,00 EUROS" → "100.00 EUR" or "100.00 euros"
- "1 500,00 €" → "1,500.00 EUR"
- "€" can stay as "€" or be written as "EUR"
- Keep the numerical value identical

## Date and Time

- Maintain DD/MM/YYYY format (do NOT convert to MM/DD/YYYY)
- Written-out dates: convert month names to English (e.g., "27 février 2026" → "27 February 2026")
- Keep time in 24h format unless the source locale uses 12h
- Preserve exact date values — do not shift dates

## Addresses

- Preserve address structure (street, number, postal code, city)
- Do NOT transliterate place names
- Add punctuation for readability if missing in the source
- Example: "Bureau 1467 37 passage du Ponceau" → "Office 1467, 37 passage du Ponceau"

## Proper Nouns

- Names of people, companies, and institutions: keep original spelling
- Do NOT transliterate unless there is an established English form
- Legal entity types should be translated to English equivalents

## Punctuation

- Convert punctuation to English conventions:
  - Guillemets « » → "quotation marks"
  - Remove extra spaces before colons, semicolons
  - Use English dash conventions (em dash for parentheticals)

## Formatting

- Preserve heading hierarchy (#, ##, ###, etc.)
- Preserve list formatting (bulleted, numbered)
- Preserve table structure where applicable
- Maintain paragraph breaks as in the source

## Grammar

- Prefer active voice over passive where natural in English
- Use "we" for first-person plural in formal documents
- Restructure relative clauses for natural English flow
- Use indicative mood where the source uses subjunctive

## Formality

- Use formal register for legal, official, and business documents
- Use "shall" for obligations in legal texts
- Use "the Company" instead of "it" when referring to the subject entity
- Maintain professional tone throughout

## OCR Artifacts

- If a word appears corrupted or nonsensical, do NOT silently guess
- Mark with inference tag: `[inferred: original "{word}", consistent across versions, contextually inferred as "{correction}", {reason}]`
- If uncertain, keep the original and flag: `[OCR: unable to determine original intent]`

## Translation Philosophy: 信达雅 (Faithfulness, Expressiveness, Elegance)

- **Faithfulness (信)**: Faithfully convey the original meaning — no additions, no omissions. Numerical values, dates, and proper nouns must be exact.
- **Expressiveness (达)**: The translation must read naturally in the target language. Avoid translationese — write as a native speaker would.
- **Elegance (雅)**: Beyond faithfulness and expressiveness, pursue linguistic quality. Formal documents should be dignified, commercial documents should flow smoothly, technical documents should be precise.

Priority: Faithfulness > Expressiveness > Elegance. When in conflict, accuracy first, then fluency, then style.

## Creative Language Strategies

Advertising, marketing, and brand copy often use creative language that cannot be translated literally.

### Homophonic Puns (谐音梗)
Chinese ads commonly substitute characters with similar-sounding ones (e.g., "倍儿棒" written as "蓓儿棒" to embed a brand name).
Steps:
1. **Decode**: Identify the intended characters (not the surface characters) and understand the real meaning
2. **Annotate**: Keep the original text, add a note explaining the intended meaning
3. **Adapt**: Find an equivalent rhetorical device in the target language
   - English: pun, rhyme, alliteration, assonance
   - French: jeu de mots, calembour
4. **Brand names**: Transliterate + add explanatory translation

Example:
- "船灶限倍儿壮增腐就用根蓓士"
  → Decoded: "船造线倍儿壮，增幅就用根蓓士"
  → Translation: "Genbeishi — Makes Your Crops X Times Stronger"
  (Brand name transliterated + effect description, preserving advertising impact)

### Slogan Translation
1. Never translate slogans literally — their power lies in rhythm and memorability
2. Analyze the original rhetoric (rhyme, parallelism, hyperbole, pun)
3. Recreate an equivalent slogan in the target language, preserving the core selling point
4. If you cannot preserve both sound and meaning, prioritize meaning; transliterate the brand name separately

### Brand Name Localization
- Transliteration: Preserve the sound, choose characters with positive connotations (e.g., Coca-Cola → 可口可乐)
- Meaning-based: Translate the brand meaning (e.g., Microsoft → 微软)
- Sound + meaning: Approximate the sound while conveying meaning (e.g., BMW → 宝马)
- Keep original: International brands may not need translation (e.g., Google, Amazon)

## Non-standard Language (Dialects, Slang, Jargon)

### Dialects
- Identify dialect markers (e.g., regional vocabulary, non-standard grammar)
- Strategy: Use equivalent colloquial/slang expressions in the target language, preserving the register
- If no equivalent exists, use standard translation + annotate that the source was dialect

### Internet Slang / Neologisms
- Identify internet abbreviations and homophonic substitutions (e.g., Chinese "yyds" = "永远的神" = "the greatest of all time")
- Strategy: Use equivalent internet slang in the target language, or explain in standard language
- Preserve the tone and emotional intensity of the original

### Industry Jargon / Argot
- Identify industry-specific terms (e.g., finance: "韭菜" = "retail investors getting fleeced", IT: "造轮子" = "reinventing the wheel")
- Strategy: Use the equivalent industry term in the target language
- If no equivalent exists, use standard terminology + add a note

## Source Quality Issues

### OCR Errors
- Common patterns: l/I/1 confusion, 0/O confusion, rn/m confusion, similar-looking Chinese characters
- Strategy: Infer the correct text from context, mark with `[推断: ...]` tag
- Do NOT preserve OCR errors in the translation

### Incomplete / Truncated Text
- Identify truncation points (incomplete sentences, interrupted paragraphs)
- Strategy: Translate the known portions, mark truncation with `[...]`
- Do NOT fabricate content to complete truncated sections

### Mixed-language Documents
- Identify language switching points (e.g., Chinese-English mixed text, French-English mixed text)
- Strategy: Translate non-target-language portions per translation rules; keep target-language portions as-is
- Proper nouns and brand names always remain in their original form
