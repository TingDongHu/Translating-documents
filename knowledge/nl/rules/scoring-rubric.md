---
id: nl/rules/scoring-rubric
type: rules
target_lang: nl
name: Dutch Translation Scoring Rubric
description: Dutch translation quality scoring rubric
---

# Dutch Translation Scoring Rubric

This rubric defines the scoring criteria for evaluating Dutch translations. It is used for quality assurance (QA), review, and revision scoring of translated output. Each dimension has a weight and six performance bands. Final scores are calculated as weighted averages and may be adjusted by zero-tolerance or global-issue penalties.

---

## Scoring Overview

| Dimension | Weight | Focus |
|---|---|---|
| 1. Numerical Accuracy | 30 % | Numbers, dates, currencies, percentages |
| 2. Terminology Consistency | 20 % | Domain terms, glossary adherence, named entities |
| 3. Semantic Fidelity | 25 % | Meaning preservation, intent, nuance |
| 4. Format Compliance | 10 % | Style guide rules, punctuation, structure |
| 5. Completeness | 10 % | Omissions, additions, untranslated segments |
| 6. Inference/OCR Quality | 5 % | Reconstructed text, handling of illegible source |
| **Zero-Tolerance Penalties** | — | Critical errors → automatic caps |
| **Global Quality Adjustment** | — | Systemic issues → max 60/100 |

### Band Definitions

All six dimensions use the following six-band scale:

| Band | Score | Description |
|---|---|---|
| A (Excellent) | 100 | No errors; exemplary in every respect. |
| B (Good) | 85 | Minor, non-substantive issues; reads naturally. |
| C (Adequate) | 70 | Some errors but meaning is clear; acceptable with minor revision. |
| D (Below Average) | 55 | Noticeable errors affecting clarity; requires revision. |
| E (Poor) | 40 | Significant errors; major rework needed. |
| F (Unacceptable) | 0 | Fundamental failures; segment must be retranslated. |

---

## Dimension 1: Numerical Accuracy

**Weight: 30 %**

Assesses correctness of all numerical content, including numbers, currencies, dates, times, percentages, and units of measurement.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | All numbers, dates, and currencies are perfectly transcribed/converted. Formatting (decimal comma, thousands separator, currency symbol placement) follows Dutch conventions without exception. |
| B | 85 | One or two trivial numerical formatting issues (e.g., inconsistent thousands separator style) that do not change the value. All values are factually correct. |
| C | 70 | Minor numerical error that does not materially affect understanding (e.g., a single rounding discrepancy in a long table). Or consistent but wrong thousands separator format (e.g., English period-as-decimal throughout on a short segment). |
| D | 55 | One numerical value is wrong or incorrectly converted. Or multiple formatting errors that partially obscure meaning. Date in wrong format (e.g., MM-DD-YYYY in Dutch text). |
| E | 40 | Multiple numerical errors or significant conversion mistakes. Currency amounts incorrect. |
| F | 0 | Critical numerical failure. Values are systematically wrong, or a central number (total, key figure) is incorrect. |

### What Is Assessed

- Decimal comma: **3,14** (not 3.14)
- Thousands separator: **1.000** or **1 000** (not 1,000)
- Currency symbol placement: **€ 100,00** (not 100,00 €)
- Date format: **31 december 2024** or **31-12-2024** (not 12/31/2024)
- Time format: **24-hour** (not AM/PM except in direct quotes)
- Percentage format: **25 %** (space before %)
- Unit conversions: metric conversion correct, recalculated accurately
- Ordinal numbering: **1e** or **1ste** (not 1st)

---

## Dimension 2: Terminology Consistency

**Weight: 20 %**

Assesses consistent use of domain terminology, adherence to glossaries or term bases, and correct handling of proper nouns and named entities.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | Perfect terminological consistency. All domain terms match the glossary (if provided). Proper nouns are preserved or correctly adapted. No internal contradictions. |
| B | 85 | One instance of inconsistent terminology (e.g., using two different translations for the same source term in different places). All other terms are correct. |
| C | 70 | Two or three inconsistent terms, or a minor proper-noun error (e.g., incorrect tussenvoegsel capitalization). Glossary is followed for the majority of terms. |
| D | 55 | Multiple inconsistent terms or failure to follow glossary on key terms. Proper nouns are inconsistently handled. |
| E | 40 | Systematic inconsistency; the same concept is translated differently throughout the document without justification. Glossary largely ignored. |
| F | 0 | Terminology is chaotic or completely ad-hoc. Named entities are corrupted. No discernible terminological discipline. |

### What Is Assessed

- Domain-specific terms translated consistently
- Proper noun preservation (company names, product names, trademarks unchanged)
- Tussenvoegsels (van/der/de) capitalization rules followed
- Dutch company forms (BV/NV) used correctly for foreign equivalents
- Acronyms and abbreviations handled consistently

---

## Dimension 3: Semantic Fidelity

**Weight: 25 %**

Assesses how faithfully the translation conveys the meaning, intent, nuance, and register of the source text.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | Meaning is perfectly preserved. All nuances, tone, and register of the source are accurately reflected. The translation reads naturally in Dutch (native-level quality). |
| B | 85 | Minor semantic shift that does not alter the meaning or tone. One idiomatic expression could be more natural. Overall very faithful. |
| C | 70 | Noticeable semantic difference in one section — a nuance is lost, or the meaning is slightly distorted. Register may drift (e.g., too formal for context). |
| D | 55 | Meaning is altered in a significant way in one or more passages. The reader would understand something different from the source. Register is inconsistent or inappropriate. |
| E | 40 | Substantial portions of the meaning are lost or distorted. The translation is unreliable. False friends (schijnverwanten) present. |
| F | 0 | The translation communicates a fundamentally different message than the source. No semantic fidelity. |

### What Is Assessed

- Core meaning preserved
- Tone and register match source (formal/informal)
- Idiomatic expressions correctly translated (not literal)
- False friends (schijnverwanten) avoided
- Polysemy handled correctly (correct sense chosen)
- Cultural references appropriately adapted for Dutch readership

---

## Dimension 4: Format Compliance

**Weight: 10 %**

Assesses adherence to the Dutch formatting and style rules defined in the base language guide.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | All formatting rules are followed: correct quotation marks, comma usage (no Oxford comma), title capitalization (sentence case), list formatting, table alignment. |
| B | 85 | One or two minor formatting deviations (e.g., using straight quotes instead of Dutch quotation marks). No structural issues. |
| C | 70 | Multiple minor formatting errors. Or one structural error (e.g., list parallelism broken, table caption placement wrong). |
| D | 55 | Several formatting rules violated. Quotation marks are mixed. Comma rules not followed. Title case used instead of sentence case. |
| E | 40 | Widespread formatting issues. The document structure is compromised. Significant rework of formatting needed. |
| F | 0 | Formatting is entirely inconsistent or absent. No attempt to follow Dutch conventions. |

### What Is Assessed

- Quotation marks: „...” (preferred) or "..." (consistent)
- Comma rules: no Oxford comma, correct use before conjunctions
- Title capitalization: sentence case
- List formatting: parallel structure, correct punctuation
- Table formatting: captions above, alignment, column headers
- Dash usage: koppelteken (-), aandachtsstreepje (–), gedachtestreepje (—)
- Date/time formatting
- Apostrophe and diacritic placement

---

## Dimension 5: Completeness

**Weight: 10 %**

Assesses whether all content from the source has been translated and nothing has been omitted or added without justification.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | Every segment of the source is translated. No omissions, no spurious additions. Nothing is left in English by mistake. |
| B | 85 | One very minor omission (e.g., single word or short phrase that is not critical to understanding). No additions. |
| C | 70 | A sentence or equivalent content is omitted. Or a small amount of unnecessary content has been added. The overall completeness is acceptable. |
| D | 55 | A paragraph or significant block of text is missing. Or substantial unnecessary content has been added. |
| E | 40 | Multiple sections omitted. The document is clearly incomplete. |
| F | 0 | Less than half of the source content is translated. Major gaps throughout. |

### What Is Assessed

- All source sentences accounted for in target
- No accidental omissions
- No untranslated segments (unless explicitly instructed to preserve)
- No editorial additions (unless marked as translator's notes)
- Footnotes, endnotes, and annotations are translated
- Table cells, figure captions, callouts all translated
- Headers, footers, watermarks, and metadata translated where applicable

---

## Dimension 6: Inference/OCR Quality

**Weight: 5 %**

Assesses the quality of handling OCR artifacts, reconstructed text, illegible source passages, and other source-quality issues.

### Band Criteria

| Band | Score | Criteria |
|---|---|---|
| A | 100 | OCR artifacts are perfectly handled. Uncertain passages are correctly marked with [hersteld: ...]. No incorrect reconstructions. |
| B | 85 | One minor OCR handling issue (e.g., [hersteld] note is slightly imprecise or uses English instead of Dutch). All reconstructions are correct. |
| C | 70 | One reconstruction is incorrect or a genuine OCR artifact was missed. Or [hersteld] notes are inconsistently formatted. |
| D | 55 | Multiple missed or mishandled OCR artifacts. Reconstructions are unreliable in places. |
| E | 40 | Widespread mishandling of OCR artifacts. Illegible text is guessed without annotation. Significant reconstruction errors. |
| F | 0 | OCR artifacts are completely ignored. Illegible text is silently guessed or omitted. No annotation is provided. |

### What Is Assessed

- Correct use of **[hersteld: ...]** annotation
- Accuracy of text reconstruction for illegible or damaged source passages
- Proper formatting of OCR annotations
- Flagging for human review when OCR quality is poor (>10 % of segment affected)
- Handling of page-break artifacts, merged/split words, wrong characters
- Numerical reconstructions checked for accuracy

---

## Zero-Tolerance Errors

Certain errors are considered **critical failures** regardless of the overall score. If any zero-tolerance error is detected, the translation receives an automatic penalty.

### Zero-Tolerance Violations

| Rule | Description |
|---|---|
| **Comma/Period Decimal** | Using a decimal point instead of a decimal comma (or vice versa) where it changes the numerical value. Example: writing 1.000 when 1,000 is intended (meaning one thousand vs. one point zero zero zero). |
| **Date Format** | Using any format other than DD-MM-YYYY or DD/MM/YYYY in Dutch prose. MM-DD-YYYY (American format) is an automatic violation. |
| **U/Jij Mismatch** | Mixing formal (u) and informal (jij/je) address within the same document without a clear justification. |

### Zero-Tolerance Penalties

| Severity | Penalty |
|---|---|
| Single zero-tolerance violation in an otherwise clean document | Deduct 15 points from the weighted total. |
| Multiple zero-tolerance violations of the same type | Deduct 25 points from the weighted total. |
| Zero-tolerance violations across multiple categories | Deduct 30 points from the weighted total. |
| Systematic zero-tolerance violation throughout the document | Maximum score cap of 60 (see Global Quality Adjustment). |

---

## Global Quality Adjustment

If the assessor determines that the translation has **systemic quality issues** that affect the document as a whole, the final score may be capped at **60 out of 100**, regardless of the weighted and zero-tolerance-adjusted score.

### Conditions That Trigger Global Cap

| Condition | Description |
|---|---|
| Systematic register failure | The entire document is in the wrong register (e.g., je/jij throughout a formal legal document). |
| Systematic formatting failure | Every heading uses title case instead of sentence case; or quotation marks are consistently wrong. |
| Systematic terminology failure | A key term is translated incorrectly throughout. |
| Systematic numerical failure | All dates use the wrong format; or all decimals use a point instead of a comma. |
| Translation by non-native Dutch speaker | Readily identifiable Dutch grammar errors (SOV violations, article errors) appear systematically throughout. |
| Machine translation without post-editing | Characteristic MT patterns (word-for-word translation, unnatural phrasing) are present throughout with no evidence of human review. |

### Global Cap Effects

| Cap Applied | Maximum possible score |
|---|---|
| Yes | **60 %** of the weighted total (i.e., max 60 points). |
| No | Standard calculation up to 100 points. |

If a global cap is applied, document this explicitly in the QA report along with the justification.

---

## Score Calculation

### Step 1: Calculate Weighted Score

```
Weighted Score = (D1 × 0.30) + (D2 × 0.20) + (D3 × 0.25) + (D4 × 0.10) + (D5 × 0.10) + (D6 × 0.05)
```

### Step 2: Apply Zero-Tolerance Penalties

```
After ZT = Weighted Score − ZT Penalty
```

### Step 3: Apply Global Cap (if applicable)

```
Final Score = min(After ZT, 60)   [if global cap applies]
Final Score = After ZT             [if no global cap]
```

### Example Calculations

**Example A — Good translation, minor issues:**

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| D1 Numerical Accuracy | 85 | 30 % | 25.5 |
| D2 Terminology Consistency | 85 | 20 % | 17.0 |
| D3 Semantic Fidelity | 85 | 25 % | 21.25 |
| D4 Format Compliance | 70 | 10 % | 7.0 |
| D5 Completeness | 85 | 10 % | 8.5 |
| D6 Inference/OCR Quality | 85 | 5 % | 4.25 |
| **Weighted Total** | | | **83.5** |

No zero-tolerance violations. No global cap. **Final score: 84 (Good).**

**Example B — Numerical error with zero-tolerance:**

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| D1 Numerical Accuracy | 55 | 30 % | 16.5 |
| D2 Terminology Consistency | 85 | 20 % | 17.0 |
| D3 Semantic Fidelity | 85 | 25 % | 21.25 |
| D4 Format Compliance | 85 | 10 % | 8.5 |
| D5 Completeness | 85 | 10 % | 8.5 |
| D6 Inference/OCR Quality | 85 | 5 % | 4.25 |
| **Weighted Total** | | | **76.0** |

Zero-tolerance: Decimal point used instead of comma (15-point penalty).  
After ZT: 76 − 15 = 61.  
No global cap. **Final score: 61 (Below Average).**

**Example C — Systemic issues with global cap:**

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| D1 Numerical Accuracy | 40 | 30 % | 12.0 |
| D2 Terminology Consistency | 40 | 20 % | 8.0 |
| D3 Semantic Fidelity | 55 | 25 % | 13.75 |
| D4 Format Compliance | 40 | 10 % | 4.0 |
| D5 Completeness | 55 | 10 % | 5.5 |
| D6 Inference/OCR Quality | 40 | 5 % | 2.0 |
| **Weighted Total** | | | **45.25** |

Zero-tolerance: mixed u/jij throughout, American date format.  
ZT penalty: 30 points. After ZT: 45.25 − 30 = 15.25.  
Global cap applied (systematic register failure). Cap = 60.  
**Final score: min(15.25, 60) = 15 (Unacceptable).**

---

## Score Interpretation

| Final Score Range | Grade | Meaning | Action Required |
|---|---|---|---|
| 90–100 | A | Excellent | None; ready for delivery. |
| 75–89 | B | Good | Minor revisions; can be resolved in review. |
| 60–74 | C | Adequate | Requires revision before delivery. |
| 40–59 | D | Below Average | Significant revision needed; consider partial retranslation. |
| 20–39 | E | Poor | Major rework required; retranslate affected sections. |
| 0–19 | F | Unacceptable | Full retranslation required. |

---

## Review Checklist

When scoring a translation, the assessor should verify the following items. This checklist corresponds to the rubric dimensions.

### Numerical Accuracy Checklist

- [ ] Decimal comma used throughout (not decimal point)
- [ ] Thousands separator correct (period or space, not comma)
- [ ] Currency symbol before amount with correct spacing
- [ ] Date format is DD-MM-YYYY or DD/MM/YYYY
- [ ] Time uses 24-hour format (no AM/PM)
- [ ] Percentage format: space before % sign
- [ ] Metric conversions are accurate (if applicable)
- [ ] All totals and calculations are correct

### Terminology Checklist

- [ ] Glossary terms followed (if glossary provided)
- [ ] Consistent term usage across the document
- [ ] Proper nouns preserved correctly
- [ ] Tussenvoegsels capitalized correctly per context
- [ ] Company forms (BV/NV) correctly applied
- [ ] Acronyms defined at first use (if applicable)

### Semantic Fidelity Checklist

- [ ] Core meaning preserved in every segment
- [ ] Register matches the source text
- [ ] Idiomatic expressions translated naturally, not literally
- [ ] No false friends (schijnverwanten)
- [ ] Cultural references appropriately adapted

### Format Compliance Checklist

- [ ] Quotation marks: „...” or consistently "..." (not mixed)
- [ ] No Oxford comma
- [ ] Title capitalization: sentence case
- [ ] List parallelism maintained
- [ ] Dash types correct (hyphen, en dash, em dash)
- [ ] Apostrophes and diacritics correctly placed

### Completeness Checklist

- [ ] All source segments accounted for
- [ ] No untranslated English text (except as instructed)
- [ ] No accidental omissions
- [ ] Footnotes and annotations translated
- [ ] Table content and captions fully translated

### Inference/OCR Checklist

- [ ] OCR artifacts correctly identified and annotated
- [ ] [hersteld: ...] format correctly applied
- [ ] Reconstructions are plausible and accurate
- [ ] Poor-quality source segments flagged for review
- [ ] OCR annotations in Dutch

### Zero-Tolerance Checklist

- [ ] No decimal point used as decimal separator where comma is required
- [ ] No MM-DD-YYYY dates
- [ ] No mixed u/jij usage within the document

---

## Appendix: Quick Reference for Scoring Common Issues

| Issue | Dimension Affected | Typical Band |
|---|---|---|
| Single decimal comma missing | D1 Numerical Accuracy | C (70) |
| All decimals use point instead of comma | D1 Numerical Accuracy | E (40) |
| Date in American format | D1 Numerical Accuracy | D (55) + ZT penalty |
| Glossary term translated inconsistently (1 instance) | D2 Terminology Consistency | B (85) |
| Key term translated wrong throughout | D2 Terminology Consistency | E (40) |
| One sentence meaning lost | D3 Semantic Fidelity | C (70) |
| Register drift (formal ↔ informal) | D3 Semantic Fidelity | C–D (55–70) |
| Quotation marks mixed throughout | D4 Format Compliance | D (55) |
| Title case used instead of sentence case | D4 Format Compliance | C (70) |
| One paragraph missing | D5 Completeness | D (55) |
| Multiple paragraphs missing | D5 Completeness | E (40) |
| One missed OCR artifact | D6 Inference/OCR Quality | B (85) |
| Mixed u/jij | — | Zero-tolerance + possible global cap |

---

*This rubric is designed for use by human reviewers and automated QA tooling. Scores should be accompanied by a written justification for any band below B (85) and for all zero-tolerance or global-cap actions.*
