---
id: en/rules/scoring-rubric
type: rules
target_lang: en
name: English Quality Scoring Rubric
description: Standardized scoring criteria for the six inspection dimensions
---

## Scoring Bands

| Band | Meaning | Action Required |
|------|---------|----------------|
| 100 | Flawless | None |
| 90-99 | Minor issues,不影响理解 | Optional fix |
| 70-89 | Several issues, should be fixed | Recommended fix |
| 50-69 | Systematic issues, needs revision | Must revise |
| <50 | Failed this dimension, must redo | Full retranslation needed |

A translation with any **critical** issue cannot score above 60 overall.

---

## 1. Numerical Accuracy (30% weight)

| Score | Criteria |
|-------|----------|
| 100 | All numerical values, units, dates, percentages, quantities match source exactly |
| 90 | 1-2 minor formatting differences (e.g., spacing before unit, decimal separator style) that don't affect the value |
| 80 | 1-2 numerical format inconsistencies (e.g., comma vs no comma in thousands, inconsistent unit abbreviation) |
| 70 | 3-5 numerical formatting issues or 1 wrong value that is contextually minor |
| 60 | More than 1 actual value mismatch; or 5+ formatting issues; or any date misinterpretation (e.g., 05/10 read as Oct 5 vs May 10) |
| <50 | Any critical numerical error: wrong amount, inverted date, converted unit without permission, currency mismatch |

**Zero-tolerance items (professional level):** Amounts, dates, percentages — any mismatch is automatically critical.

---

## 2. Terminology Consistency (20% weight)

| Score | Criteria |
|-------|----------|
| 100 | All recurring terms use exactly one translation; glossary 100% followed |
| 90 | 1-2 minor terminology variations that are contextually justified (e.g., synonyms for readability) |
| 80 | 1-2 unjustified terminology inconsistencies; or 1 glossary violation |
| 70 | 3-5 terminology inconsistencies or 2-3 glossary violations |
| 60 | 5+ terminology inconsistencies; systematic confusion of key terms |
| <50 | Glossary systematically ignored; key terms translated differently each time, causing confusion |

**Contextual vs unjustified variations:** A term may legitimately vary by context (e.g., "run" → "execute" for commands, "run" → "operate" for machines). Flag only when no contextual reason exists.

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

**Check method:** Read source paragraph, read target paragraph. Do they answer the same question? Does the target add information not in source? Does it leave out critical details?

---

## 4. Format Compliance (10% weight)

| Score | Criteria |
|-------|----------|
| 100 | All number formats, address formats, punctuation, and typography follow target-locale conventions |
| 90 | 1-2 minor format deviations (e.g., one missing comma in a list, one extra space) |
| 80 | 2-3 format inconsistencies or mixed locale conventions within the same document |
| 70 | 4-5 format issues; systematic use of source-locale formatting (e.g., Chinese punctuation in English text) |
| 60 | Widespread format issues; inconsistent punctuation style throughout |
| <50 | Format makes the document look unprofessional; critical locale violations |

**Common checks:**
- Decimal and thousands separators per target locale
- Quotation marks and dashes per target locale
- Date and time formats per target locale
- Unit abbreviations per target locale
- Address format per target locale

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

---

## 6. Inference/OCR Quality (5% weight)

| Score | Criteria |
|-------|----------|
| 100 | All inference markers are reasonable, well-justified, and correctly tagged with `[inferred:]` |
| 90 | 1 inference marker with slightly weak but still defensible reasoning |
| 80 | 1-2 cases where inference could be wrong but is clearly tagged; or 1 case where inference should have been used but wasn't |
| 70 | 2-3 questionable inferences; or 2 untagged inferences that should have been marked |
| 60 | Multiple questionable inferences; systematic over-guessing without tags |
| <50 | Hallucinated content passed off as translation; fabricated numbers or facts |

**Principle:** Better to tag uncertain content as inferred than to silently guess. Correct tagging that admits uncertainty is NOT a defect — it is good practice.
