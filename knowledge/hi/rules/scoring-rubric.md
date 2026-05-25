# Hindi Translation Quality Scoring Rubric

## Scoring Framework

Each dimension is scored on a 6-band scale (0–5), then weighted to produce a weighted score out of 5. The final quality score is the sum of all weighted dimension scores, converted to a percentage.

### Band Definitions

| Band | Label | Meaning |
|---|---|---|
| 5 | Excellent | Fully meets standards; no errors or negligible |
| 4 | Good | Minor issues; does not affect comprehension |
| 3 | Adequate | Noticeable issues but still functional |
| 2 | Deficient | Significant issues affecting usability |
| 1 | Poor | Major issues; largely unusable |
| 0 | Unacceptable | Complete failure; unusable |

### Global Rule: Critical Defects

If any **critical defect** is found in the entire document, the **maximum possible score across all dimensions is capped at Band 3 (60%)**. Critical defects are defined per dimension and include:

- Numerical errors (decimal format, lakh/crore misuse)
- Date format violations (MM/DD/YYYY instead of DD/MM/YYYY)
- Register violations (आप/तू misuse)
- Untranslated segments in an otherwise translated document
- Factual errors introduced in translation

---

## Dimension 1: Numerical Accuracy (Weight: 30%)

| Band | Criteria |
|---|---|
| 5 | All numbers, dates, currencies, percentages, and units translated flawlessly. Indian numbering (lakh/crore) used correctly. Decimal points, commas, and digit grouping perfect. |
| 4 | One or two minor numerical errors (e.g., spacing around ₹ symbol, inconsistent digit grouping) that do not affect the meaning. |
| 3 | Several numerical errors affecting clarity but not changing factual meaning. Lakh/crore used inconsistently or partially incorrect. |
| 2 | Frequent numerical errors. Indian numbering not applied where needed. Decimal/grouping errors propagate. |
| 1 | Widespread numerical errors making numbers unreliable. Units converted incorrectly. |
| 0 | Virtually all numbers incorrect or untranslated. Numerical section unusable. |

### Zero-Tolerance Checks (Numerical Accuracy)
- [ ] Are all decimal points correctly placed? (3.14 not 3,14)
- [ ] Are lakh/crore used instead of million/billion?
- [ ] Is the Indian numbering grouping applied (12,34,567)?
- [ ] Are dates in DD/MM/YYYY format?
- [ ] Is the ₹ symbol correctly placed before the amount?
- [ ] Are percentages formatted consistently (% or प्रतिशत)?
- [ ] Are ordinals correctly gendered in Hindi?

### Critical Defects (Numerical Accuracy)
- Decimal comma used instead of decimal point → **critical**
- Lakh/crore where million/billion should be converted → **critical**  
- MM/DD/YYYY date format used → **critical**
- Currency conversion error (wrong exchange rate applied) → **critical**
- Zero amount mistranslated as non-zero → **critical**

---

## Dimension 2: Terminology Consistency (Weight: 20%)

| Band | Criteria |
|---|---|
| 5 | Perfect terminology consistency. Same Hindi term used for same English concept throughout. Glossary followed if provided. Standard Hindi terms used. |
| 4 | One or two inconsistencies in minor terms. No confusion caused. |
| 3 | Multiple terms used inconsistently for key concepts. Some confusion possible but meaning recoverable. |
| 2 | Frequent inconsistent terminology causing noticeable confusion. Key technical terms switched mid-document. |
| 1 | Terminology chaotic. Same concept translated 3+ different ways. Meaning obscured. |
| 0 | No discernible terminology system. Random word choices throughout. |

### Zero-Tolerance Checks (Terminology Consistency)
- [ ] Is the same Hindi term used for each repeated English term?
- [ ] Are proper names transliterated consistently?
- [ ] Are honorifics (श्री/श्रीमती/सुश्री) used consistently?
- [ ] Is the glossary (if provided) followed without deviation?
- [ ] Are acronyms handled consistently (translated vs. retained)?

### Critical Defects (Terminology Consistency)
- Same English proper noun transliterated 3+ different ways → **critical**
- Key technical term (e.g., "liability" → दायित्व/उत्तरदायित्व/ज़िम्मेदारी) used inconsistently in a critical section → **critical**
- Glossary violated for 30%+ of glossary terms → **critical**

---

## Dimension 3: Semantic Fidelity (Weight: 25%)

| Band | Criteria |
|---|---|
| 5 | Meaning perfectly preserved. All nuances, tone, and intent of the source text transferred accurately to Hindi. No additions, omissions, or distortions. |
| 4 | Minor semantic shifts that do not change the meaning. Optional nuance may be slightly altered. |
| 3 | Some meaning loss or distortion. A key point may be slightly weakened or generalized. Overall intent still clear. |
| 2 | Significant meaning loss. Important facts or claims misrepresented. Reader would get a different understanding. |
| 1 | Major distortion of meaning. The Hindi text contradicts the source on important points. |
| 0 | Meaning completely lost. Translation bears no relation to source content. |

### Zero-Tolerance Checks (Semantic Fidelity)
- [ ] Are all factual claims preserved?
- [ ] Is the tone/register matched (formal/informal)?
- [ ] Are idioms and metaphors appropriately translated (not literal)?
- [ ] Is the subject-verb-object mapping correct?
- [ ] Are negations correctly handled? (Not accidentally reversed)
- [ ] Are conditional statements preserved correctly?

### Critical Defects (Semantic Fidelity)
- Factual error introduced (wrong year, wrong name, wrong statistic) → **critical**
- Negation reversed ("is not" translated as "is") → **critical**
- Key warning or disclaimer omitted → **critical**
- Source text's opinion/perspective reversed → **critical**
- Untranslated segment left in source language → **critical**

---

## Dimension 4: Format Compliance (Weight: 10%)

| Band | Criteria |
|---|---|
| 5 | Full format preservation. Headings, lists, tables, paragraphs, line breaks, and special formatting (bold, italic) perfectly maintained. All placeholders and variables correctly handled. |
| 4 | Minor formatting deviations (e.g., one missed bullet, a slightly different heading style). Not affecting readability. |
| 3 | Noticeable formatting issues. Some structure lost but content still navigable. Table alignment off. |
| 2 | Significant formatting problems. Lists collapsed, headings missing, tables broken. Navigation difficult. |
| 1 | Major format failure. Document structure largely unrecognizable from source. |
| 0 | No format preserved. Plain text dump with no structure. |

### Zero-Tolerance Checks (Format Compliance)
- [ ] Are all headings translated and at the correct level?
- [ ] Are bullet lists preserved as lists?
- [ ] Are table structures (rows/columns/cells) maintained?
- [ ] Are placeholders/variables (e.g., {name}, {{template}}) preserved?
- [ ] Are hyperlinks and references preserved?
- [ ] Are numbered lists in correct sequence?
- [ ] Are code blocks, if any, preserved untranslated?

### Critical Defects (Format Compliance)
- Placeholder/variable corrupted or deleted → **critical**
- Table data merged or split incorrectly, changing meaning → **critical**
- All headings removed or merged into paragraphs → **critical**
- File format changed (e.g., .docx to plain text without instruction) → **critical**

---

## Dimension 5: Completeness (Weight: 10%)

| Band | Criteria |
|---|---|
| 5 | 100% complete. Every sentence, heading, footnote, caption, and piece of text from the source is present in the Hindi output. |
| 4 | One or two minor omissions (e.g., a caption, a footnote). Does not affect understanding. |
| 3 | Several sentences or a paragraph omitted (~5–10% missing). Noticeable gaps. |
| 2 | Substantial content missing (~10–25%). Sections skipped. Reader would notice missing information. |
| 1 | Major content omitted (~25–50%). Large sections untranslated or absent. |
| 0 | More than half the content missing or untranslated. Document is incomplete. |

### Zero-Tolerance Checks (Completeness)
- [ ] Is every paragraph/segment represented in the Hindi output?
- [ ] Are all footnotes/endnotes translated?
- [ ] Are all table cells filled (not left blank)?
- [ ] Are image captions and alt text translated?
- [ ] Are headers, footers, page numbers addressed?
- [ ] Are appendixes/annexures included?
- [ ] Are legal boilerplate and disclaimers included?

### Critical Defects (Completeness)
- An entire section missing → **critical**
- All footnotes/endnotes omitted → **critical**
- All table headers left in source language while body translated → **critical**
- Disclaimer/legal notice omitted → **critical**
- 10%+ of content missing → **critical**

---

## Dimension 6: Inference / OCR Quality (Weight: 5%)

| Band | Criteria |
|---|---|
| 5 | Flawless handling of OCR artifacts. All illegible/uncertain text properly marked with `[पुनर्स्थापित: ...]`. No hallucinated content. |
| 4 | One or two minor OCR issues (e.g., a missed restoration marker) that do not affect meaning. |
| 3 | Several OCR artifacts mishandled. Some restored text is incorrect or missing restoration markers. Content still understandable. |
| 2 | Frequent OCR mishandling. Restored text often wrong. Restoration markers missing where needed. |
| 1 | Pervasive OCR errors. Hallucinated content present. Restored text unreliable. |
| 0 | OCR artifacts completely ignored or fabricated. Text cannot be trusted. |

### Zero-Tolerance Checks (Inference / OCR Quality)
- [ ] Are all `[पुनर्स्थापित: ...]` markers properly formatted?
- [ ] Is restored text plausible and contextually correct?
- [ ] Are conjunct consonants correctly rendered (क्ष, त्र, ज्ञ)?
- [ ] Are nukta characters correctly placed (क़, फ़, ज़)?
- [ ] Is the shirorekha correctly rendered across words?
- [ ] Is there any hallucinated content (text not present in source)?

### Critical Defects (Inference / OCR Quality)
- Hallucinated content (text not in source, not marked as restored) → **critical**
- `[पुनर्स्थापित: ...]` used for clear/legible text → **critical**
- Critical restored text is factually wrong (wrong name, number, date) → **critical**
- OCR conjunct errors propagate without correction (क्ष → कष throughout) → **critical**

---

## Scoring Summary Table

| Dimension | Weight | Band (0–5) | Weighted Score |
|---|---|---|---|
| 1. Numerical Accuracy | 30% | ___ | ___ |
| 2. Terminology Consistency | 20% | ___ | ___ |
| 3. Semantic Fidelity | 25% | ___ | ___ |
| 4. Format Compliance | 10% | ___ | ___ |
| 5. Completeness | 10% | ___ | ___ |
| 6. Inference / OCR Quality | 5% | ___ | ___ |
| **Total** | **100%** | | **___ / 5.00** |

### Calculation
- Dimension weighted score = (Band × Weight)
- Total score = Sum of all weighted scores
- Final percentage = (Total score / 5) × 100

### Example
| Band: | 5 | 5 | 4 | 5 | 5 | 5 |
| Weighted: | 1.50 | 1.00 | 1.00 | 0.50 | 0.50 | 0.25 |
| Total = 4.75 / 5.00 = **95%**

### Global Rule Application
- If **any** critical defect is found → maximum possible score = 60% (3.00 / 5.00)
- The 60% cap applies to the final percentage, not individual dimensions
- All critical defects must be documented with location and reason

---

## Quality Assessment Workflow

1. **Pre-check**: Scan for critical defects across all dimensions.
   - If any critical defect found → cap at 60%, note the defect location.
2. **Dimension scoring**: Score each dimension 0–5 using the band criteria.
3. **Weighted calculation**: Apply weights to each dimension score.
4. **Global cap**: Apply 60% cap if critical defects were found.
5. **Final report**: Document scores, defects, and comments.

### Quality Tiers

| Final Score | Tier | Action |
|---|---|---|
| 90–100% | Platinum | Ready for delivery |
| 75–89% | Gold | Minor revisions recommended |
| 60–74% | Silver | Revisions required before delivery |
| 40–59% | Bronze | Major revisions needed |
| Below 40% | Fail | Rework required |

---

## Defect Documentation Template

```
Defect #: ___
Dimension: [Numerical Accuracy / Terminology / Semantic Fidelity / Format / Completeness / OCR]
Type: [Minor / Major / Critical]
Location: [Section / Paragraph / Table / Page]
Source text: "..."
Hindi text: "..."
Issue: [Description of the problem]
Severity: [Why this matters]
```

---

## Quick Reference Card

### Zero-Tolerance Rules (Any violation → cap at 60%)
| Rule | Dimension |
|---|---|
| Decimal comma used instead of decimal point | Numerical Accuracy |
| Lakh/crore/million/billion misuse | Numerical Accuracy |
| MM/DD/YYYY date format | Numerical Accuracy |
| Same proper noun transliterated 3+ ways | Terminology Consistency |
| Factual error introduced | Semantic Fidelity |
| Negation reversed | Semantic Fidelity |
| Placeholder/variable corrupted | Format Compliance |
| Entire section missing | Completeness |
| Hallucinated content | OCR Quality |

### Common Hindi Translation Errors to Watch For
- Gender disagreement between noun and adjective/verb
- Postposition errors (ने/को/से/का/में/पर)
- आप/तुम/तू register violation
- Shirorekha splitting Devanagari text incorrectly
- Over-Sanskritization or under-Sanskritization
- English SVO structure carried into Hindi SOV
- Missing nukta characters in loanwords
- Inconsistent use of । vs . (purnaviram)
