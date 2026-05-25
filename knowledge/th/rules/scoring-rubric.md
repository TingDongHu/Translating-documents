# Thai Translation Quality Scoring Rubric

> Applicable to: All Thai-language document translation outputs
> Scoring scale: 0 (fail) to 5 (excellent) per dimension
> Maximum raw score: 30 (6 dimensions x 5)
> Weighted maximum: 100

---

## Global Constraints

### Zero-Tolerance Items

The following errors trigger an **automatic score of 0 for the dimension regardless of other performance**:

| ID  | Error Type                           | Affected Dimension         | Rule                                                                 |
|-----|--------------------------------------|----------------------------|----------------------------------------------------------------------|
| ZT1 | Missing Buddhist Era conversion      | Numerical Accuracy         | Any Gregorian year not converted to พ.ศ. (+543) in date context |
| ZT2 | Incorrect BE year (off by != 543)    | Numerical Accuracy         | BE must be CE + 543 exactly                                          |
| ZT3 | Missing ราชาศัพท์ for royal subjects | Terminology Consistency    | Royal figures require royal vocabulary; substitution with ordinary vocabulary is a critical error |
| ZT4 | Missing polite particles (ครับ/ค่ะ)  | Format Compliance          | All formal declarative sentences require sentence-final particles    |
| ZT5 | Untranslated source text             | Completeness               | Any source segment left in original language without translation     |

### Critical Error Cap (CEC)

- If any single dimension scores **0** (due to zero-tolerance or otherwise), the **overall weighted score is capped at 60/100** regardless of other dimension scores.
- This cap signals that the output is **not deployable** without revision.
- Two or more dimensions scoring 0 = automatic fail (score 0/100).

---

## Dimension 1: Numerical Accuracy (Weight: 30%)

Measures correctness of all number-related conversions including year, currency, units of measure, percentages, and digit formatting.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 30.0 | All numbers correctly converted. BE years exact (+543). Currency converted to THB/บาท format where required. Metric conversions correct. Decimal/thousands separators conform to Thai conventions. Percentages correctly formatted. 100% accuracy. |
| 4    | 24.0 | One or two minor numerical formatting issues (e.g., comma placement, decimal style) that do not affect meaning. All BE years correct. No factual numerical errors. |
| 3    | 18.0 | Several formatting inconsistencies OR one substantive numerical error (wrong number transferred). BE years correct but potentially missing in one or two non-critical locations. |
| 2    | 12.0 | Multiple numerical formatting errors. One or two BE years missing or incorrectly calculated. A factual numerical error present (wrong value, misplaced decimal). |
| 1    | 6.0  | Pervasive numerical formatting issues. Multiple BE year errors. Several factual numerical errors that affect document usability. |
| 0    | 0.0  | Any BE year missing or wrong in a primary date context [ZT1/ZT2]. OR numerical section essentially untranslated. Automatic critical cap applies. |

---

## Dimension 2: Terminology Consistency (Weight: 20%)

Measures consistent use of Thai terminology, classifiers, proper noun treatment, and domain-specific vocabulary.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 20.0 | Perfect terminology consistency throughout. Same Thai term used for same source concept every time. Classifiers applied correctly and consistently. Proper nouns handled via RTGS or established Thai forms. Royal vocabulary correctly applied where needed. |
| 4    | 16.0 | One or two minor inconsistencies (e.g., one term used in two variants, with both being correct). Classifiers correct. No mistranslated domain terms. Royal vocabulary correct. |
| 3    | 12.0 | A few inconsistent term choices. One instance of an incorrect classifier. One or two proper nouns not following RTGS consistently. Royal vocabulary acceptable but slightly imprecise. |
| 2    | 8.0  | Noticeable term inconsistency (multiple synonyms used for the same concept without reason). Several classifier errors. Proper nouns haphazardly transcribed. |
| 1    | 4.0  | Pervasive inconsistency. Wrong classifiers frequently. Proper nouns unrecognizable. Domain vocabulary confused or mistranslated. |
| 0    | 0.0  | Missing ราชาศัพท์ for royal subjects [ZT3]. OR terminology is completely chaotic/unusable. Critical cap applies. |

---

## Dimension 3: Semantic Fidelity (Weight: 25%)

Measures how accurately the meaning of the source text is conveyed in Thai, independent of lexical choices.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 25.0 | Meaning perfectly preserved. All nuances, tone, and intent of the source carried into Thai. No omissions, additions, or distortions. Reads as natural Thai while fully faithful to source meaning. |
| 4    | 20.0 | Meaning preserved with very minor losses (e.g., a slight nuance of tone not fully carried over). No factual misrepresentations. No added or omitted information of substance. |
| 3    | 15.0 | Meaning generally accurate but with some loss of nuance. One or two minor semantic shifts (e.g., a conditional expressed as a certainty, or vice versa). No major distortion. |
| 2    | 10.0 | Noticeable semantic errors. Several clauses mistranslated or misinterpreted. The general gist is still discernible but detail-level meaning is compromised. |
| 1    | 5.0  | Pervasive semantic errors. Large sections convey a different meaning than the source. The output misleads or confuses on key points. |
| 0    | 0.0  | Meaning is unrecognizable relative to source. Major content fabricated or completely misinterpreted. Not usable. |

---

## Dimension 4: Format Compliance (Weight: 10%)

Measures adherence to Thai punctuation rules, spacing conventions, paragraph structure, list formatting, and polite particles.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 10.0 | Perfect format compliance. All sentences end with correct polite particles (ครับ/ค่ะ consistent with writer gender). No extraneous word-internal spaces. Thai punctuation (ไม้ยมก, ไปยาลน้อย, ไปยาลใหญ่) used correctly. Angle quotes or quotation marks consistent. Date/time format consistent. |
| 4    | 8.0  | Minor issues: one or two missing or wrong polite particles. One or two spacing errors. Punctuation generally correct but with a single inconsistency. |
| 3    | 6.0  | Several missing or inconsistent polite particles. Noticeable spacing issues (extra spaces between Thai words). Punctuation style inconsistent (mixing Thai and Western conventions). |
| 2    | 4.0  | Frequent polite particle errors (missing in 25%+ of sentences). Significant spacing issues. Punctuation applied haphazardly. |
| 1    | 2.0  | Polite particles largely absent or used incorrectly. Spacing follows source-language conventions, not Thai. Punctuation errors throughout. |
| 0    | 0.0  | Complete absence of polite particles [ZT4]. OR format makes the document unreadable as Thai. Critical cap applies. |

---

## Dimension 5: Completeness (Weight: 10%)

Measures whether all source content has been translated and nothing is omitted.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 10.0 | Every segment of the source is translated. No omissions. Headers, footers, captions, footnotes, sidebar text, and document metadata all covered. |
| 4    | 8.0  | One or two minor omissions (e.g., a single figure caption, a short footnote). Nothing structural or meaning-bearing omitted. |
| 3    | 6.0  | Several small omissions or one meaningful omission (a paragraph or key term left untranslated). 90-95% of content covered. |
| 2    | 4.0  | Noticeable gaps. One or more entire paragraphs or sections omitted. 75-89% coverage. |
| 1    | 2.0  | Large sections missing. Less than 75% coverage. Substantial rework required. |
| 0    | 0.0  | Source text left completely untranslated [ZT5]. OR critical content (disclaimers, warnings, legal text) omitted. Critical cap applies. |

---

## Dimension 6: Inference / OCR Quality (Weight: 5%)

Measures handling of damaged, illegible, or ambiguous source content, including proper use of the [กู้คืน: ...] marker format.

| Band | Score | Description |
|------|-------|-------------|
| 5    | 5.0  | All damaged/uncertain passages correctly flagged with [กู้คืน: ...] markers. OCR errors identified and either corrected (with high confidence) or flagged (with uncertainty). No silent omission of unreadable text. |
| 4    | 4.0  | Most damaged passages flagged. One instance where an uncertain passage was silently rendered without flagging. Otherwise good handling. |
| 3    | 3.0  | Several damaged passages handled inconsistently — some flagged, some silently rendered. One clear OCR error propagated into output without correction or flag. |
| 2    | 2.0  | Frequent poor handling. Multiple damaged passages silently dropped or rendered without flagging. OCR errors reproduced in output. |
| 1    | 1.0  | Pervasive mishandling. The [กู้คืน: ...] format not used at all despite extensive damage. OCR garbage rendered as if it were valid text. |
| 0    | 0.0  | Complete failure to handle source damage. Illegible content fabricated into plausible-sounding but invented text without any flagging. |

---

## Scoring Summary

### Per-Dimension Scoring Table

| Dimension                       | Weight | Band 5 | Band 4 | Band 3 | Band 2 | Band 1 | Band 0 |
|---------------------------------|--------|--------|--------|--------|--------|--------|--------|
| 1. Numerical Accuracy           | 30%    | 30.0   | 24.0   | 18.0   | 12.0   | 6.0    | 0.0    |
| 2. Terminology Consistency      | 20%    | 20.0   | 16.0   | 12.0   | 8.0    | 4.0    | 0.0    |
| 3. Semantic Fidelity            | 25%    | 25.0   | 20.0   | 15.0   | 10.0   | 5.0    | 0.0    |
| 4. Format Compliance            | 10%    | 10.0   | 8.0    | 6.0    | 4.0    | 2.0    | 0.0    |
| 5. Completeness                 | 10%    | 10.0   | 8.0    | 6.0    | 4.0    | 2.0    | 0.0    |
| 6. Inference / OCR Quality      | 5%     | 5.0    | 4.0    | 3.0    | 2.0    | 1.0    | 0.0    |

### Final Score Calculation

```
weighted_score = sum of all dimension weighted scores
```

### Pass/Fail Thresholds

| Score Range     | Verdict | Action                                                |
|-----------------|---------|-------------------------------------------------------|
| 90 - 100        | Pass    | Output ready for delivery                             |
| 75 - 89         | Conditional Pass | Minor revisions required, re-check flagged items |
| 60 - 74         | Revise  | Significant revision needed, re-enter pipeline        |
| Below 60        | Fail    | Must be retranslated from source. Do not patch.       |
| Any dimension 0 | Capped  | Score automatically <= 60. Investigate zero-tolerance violation. |

### Zero-Tolerance Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────────┐
│ THAI ZERO-TOLERANCE CHECKLIST                                      │
│                                                                     │
│ [ ] All years converted to พ.ศ. (+543)?                            │
│ [ ] Royal vocabulary used for royal subjects?                       │
│ [ ] Polite particles (ครับ/ค่ะ) on every sentence?                  │
│ [ ] No untranslated source segments?                                │
│ [ ] No source-language spacing in Thai text?                        │
│                                                                     │
│ ANY failure = dimension 0 + global cap 60.                          │
└─────────────────────────────────────────────────────────────────────┘
```

---

> **Rubric Version:** 1.0
> **Last Updated:** 2026-05-25
> **Review Frequency:** Update when zero-tolerance rules or dimension weights change.
