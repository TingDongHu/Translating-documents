---
id: mn/rules/scoring-rubric
type: rules
target_lang: mn
name: Mongolian Quality Scoring Rubric
description: Standardized scoring criteria for the six inspection dimensions for Mongolian (Cyrillic) translations
---

## Scoring Bands

| Band | Meaning | Action Required |
|------|---------|----------------|
| 100 | Алдаагүй / Flawless | None |
| 90-99 | Бага зэргийн алдаа, ойлгоход саад болохгүй | Optional fix |
| 70-89 | Хэд хэдэн алдаа, засах шаардлагатай | Recommended fix |
| 50-69 | Системийн алдаа, заавал засварлах | Must revise |
| <50 | Энэ хэмжүүрт унасан, дахин орчуулах | Full retranslation needed |

A translation with any **critical** issue cannot score above 60 overall.

---

## 1. Numerical Accuracy (30% weight)

| Score | Criteria |
|-------|----------|
| 100 | All numerical values, units, dates, percentages, quantities match source exactly |
| 90 | 1-2 minor formatting differences (e.g., spacing before unit, decimal separator style) that don't affect the value |
| 80 | 1-2 numerical format inconsistencies (e.g., comma vs space in thousands, inconsistent unit abbreviation) |
| 70 | 3-5 numerical formatting issues or 1 wrong value that is contextually minor |
| 60 | More than 1 actual value mismatch; or 5+ formatting issues; or any date misinterpretation |
| <50 | Any critical numerical error: wrong amount, inverted date, converted unit without permission, currency mismatch |

**Zero-tolerance items (professional level):** Amounts, dates, percentages — any mismatch is automatically critical.

**Mongolian-specific checks:**
- Chinese 万/亿 properly converted to numeric values
- Date format: YYYY оны MM сарын DD or YYYY.MM.DD
- Currency symbols preserved (¥, ₮) with correct placement
- Ordinals use -дугаар/-дүгээр correctly

---

## 2. Terminology Consistency (20% weight)

| Score | Criteria |
|-------|----------|
| 100 | All recurring terms use exactly one translation; glossary 100% followed |
| 90 | 1-2 minor terminology variations that are contextually justified |
| 80 | 1-2 unjustified terminology inconsistencies; or 1 glossary violation |
| 70 | 3-5 terminology inconsistencies or 2-3 glossary violations |
| 60 | 5+ terminology inconsistencies; systematic confusion of key terms |
| <50 | Glossary systematically ignored; key terms translated differently each time, causing confusion |

**Mongolian-specific checks:**
- Brand name transliteration consistent throughout (Лө Юань, not alternating with Леюан)
- Loanword vs. native term consistency (e.g., use either компани or байгууллага consistently)
- Case suffix consistency for recurring noun phrases
- Vowel harmony respected in native Mongolian words

---

## 3. Semantic Fidelity (25% weight)

| Score | Criteria |
|-------|----------|
| 100 | Complete semantic equivalence — no omissions, no additions, no distortions |
| 90 | 1-2 minor paraphrases that preserve meaning but slightly shift emphasis |
| 80 | 1-2 instances of omission/addition that don't change the overall meaning |
| 70 | 3-5 minor omissions or added clarifications; or 1 sentence with shifted meaning |
| 60 | Missing sentences; added content not in source; 2+ sentences with wrong meaning |
| <50 | Paragraphs with fundamentally wrong meaning; key information lost; systematic omissions |

**Mongolian-specific checks:**
- Chinese idioms (成语) correctly interpreted, not mechanically mapped
- Topic-comment structures correctly restructured to SOV
- Definite vs. indefinite objects distinguished (accusative -ыг/-г only for definite)
- бөгөөд, болон, ба used correctly for logical connectors

---

## 4. Format Compliance (10% weight)

| Score | Criteria |
|-------|----------|
| 100 | All formats (numbers, addresses, punctuation, typography) follow Mongolian Cyrillic conventions |
| 90 | 1-2 minor format deviations |
| 80 | 2-3 format inconsistencies or mixed locale conventions |
| 70 | 4-5 format issues; systematic use of Chinese formatting (e.g., Chinese punctuation in Mongolian text) |
| 60 | Widespread format issues; inconsistent punctuation style throughout |
| <50 | Format makes the document look unprofessional; critical locale violations |

**Mongolian-specific checks:**
- Full-width Chinese punctuation → half-width Cyrillic (，→ , 。→ . ：→ :)
- Chinese enumeration comma 、→ standard comma or болон
- Quotation marks: «» (guillemets, no internal spaces), not "" or 「」
- Em dash — without spaces (текст—текст)
- Өө and Үү render correctly (UTF-8)
- Date format: YYYY.MM.DD or YYYY оны MM сарын DD, not Chinese YYYY年MM月DD日

---

## 5. Completeness (10% weight)

| Score | Criteria |
|-------|----------|
| 100 | Every paragraph translated; all [Pn] markers present; no missing sections |
| 90 | 1-2 paragraphs with untranslated fragments; or 1 missing [Pn] marker with no gap |
| 80 | 1-2 completely untranslated paragraphs; or a minor section heading left untranslated |
| 70 | 3-5 paragraphs untranslated or missing; or one section omitted |
| 60 | 5+ paragraphs untranslated; or content truncated at document boundary |
| <50 | Large sections missing; document incomplete; systematic gaps |

**Note:** IMAGE tags and their content are NOT translated per user instruction. Ensure all image captions like `[IMAGE: ...]` and `[SIC: ...]` are preserved as-is.

---

## 6. Inference/OCR Quality (5% weight)

| Score | Criteria |
|-------|----------|
| 100 | All inference markers are reasonable, well-justified, and correctly tagged with `[inferred:]` |
| 90 | 1 inference marker with slightly weak but still defensible reasoning |
| 80 | 1-2 cases where inference could be wrong but is clearly tagged |
| 70 | 2-3 questionable inferences; or 2 untagged inferences |
| 60 | Multiple questionable inferences; systematic over-guessing without tags |
| <50 | Hallucinated content passed off as translation; fabricated numbers or facts |

**Principle:** Better to tag uncertain content as `[OCR: ...]` or `[inferred: ...]` than to silently guess.
