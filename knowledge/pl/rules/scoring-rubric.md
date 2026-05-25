# Polish Translation Scoring Rubric

> This rubric defines how translation quality is evaluated for Polish-language document translation.
> All reviewers score translations using these dimensions and bands.
> Version: 1.0

---

## Scoring Overview

Each dimension is scored on a **0–5 band scale**. The weighted total determines the final quality score (0–100).

### Band Descriptors

| Band | Label          | Description                                                  |
|------|----------------|--------------------------------------------------------------|
| 5    | Excellent      | Fully meets requirements; no errors or negligible issues.    |
| 4    | Good           | Mostly meets requirements; minor, non-systemic issues.       |
| 3    | Adequate       | Meets core requirements; some errors but meaning preserved.  |
| 2    | Poor           | Notable deficiencies; meaning partially affected.            |
| 1    | Very Poor      | Pervasive errors; meaning frequently obscured.               |
| 0    | Unacceptable   | Wholly fails to meet requirements; unusable.                 |

### Weighted Scoring Formula

```
Total Score = (NA × 30%) + (TC × 20%) + (SF × 25%) + (FC × 10%) + (CM × 10%) + (IQ × 5%)
```

Where each dimension score = (band_value / 5) × 100 before weighting.

### Global Score Modifiers

| Condition                                              | Modifier               |
|--------------------------------------------------------|------------------------|
| Any single zero-tolerance violation (see below)        | Automatic cap at 60    |
| Two or more zero-tolerance violations                  | Automatic cap at 40    |
| Three or more zero-tolerance violations                | Automatic score of 0   |

---

## Dimension 1: Numerical Accuracy (NA) — Weight: 30%

Evaluates correctness of all numeric content: digits, decimals, percentages, currency amounts, dates, times, and numeric formatting.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | All numbers translated with perfect accuracy. Decimal commas, thousands separators, currency placement, date formats, and percentages comply with Polish rules. No transposition or truncation errors. |
| 4    | Near-perfect numerical accuracy. One or two minor formatting deviations (e.g., spacing around percent sign) that do not affect interpretation. |
| 3    | Multiple formatting inconsistencies (mixed comma/period in decimals, inconsistent thousands separators). All numeric values still factually correct. |
| 2    | Factual numerical errors present (wrong amounts, transposed digits). Some values are incorrect. |
| 1    | Widespread numerical errors. Large number of values are wrong or inconsistently formatted. Meaning is substantially compromised. |
| 0    | Numerical content is unacceptably inaccurate. Systematic decimal, currency, or date errors throughout. |

### Zero-Tolerance Checks (Numerical)

The following flaws in this dimension trigger a **zero-tolerance global cap**:

- Using a **period** as a decimal separator where Polish requires a comma (e.g., `3.14` instead of `3,14`). One occurrence = cap at 60; two or more = cap at 40.
- Using **MM/DD/YYYY** or any non-Polish date format instead of **DD.MM.YYYY**. One occurrence = cap at 60.

---

## Dimension 2: Terminology Consistency (TC) — Weight: 20%

Evaluates consistent use of domain-specific terms, adherence to project glossary, and avoidance of unjustified synonym variation.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | Perfect consistency. Every source term maps to exactly one Polish equivalent throughout. Glossary terms are followed without deviation. |
| 4    | High consistency. One or two instances of unnecessary synonym variation that do not cause confusion. Glossary followed in all substantive terms. |
| 3    | Moderate consistency. Several instances of term inconsistency. The same source concept is rendered by different Polish words without justification. Glossary partially followed. |
| 2    | Low consistency. Frequent unjustified variation. Glossary followed inconsistently. Reader may be confused about whether different Polish terms refer to the same concept. |
| 1    | Very low consistency. Terms vary chaotically. Key domain terms are rendered differently each time they appear. Glossary largely ignored. |
| 0    | No discernible pattern of term usage. Equivalent source terms receive different Polish translations without reason. Glossary not used. |

### Guidance

- If the source deliberately uses different terms for different concepts, the translation must also differentiate them.
- If the source uses the same term consistently, the translation must match that consistency.
- Acronym expansions must be consistent throughout.

---

## Dimension 3: Semantic Fidelity (SF) — Weight: 25%

Evaluates how accurately the translation conveys the meaning of the source. Includes correct verb aspect, case usage, register, false friends, and preservation of nuance.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | Perfect semantic transfer. Meaning, tone, nuance, and intent fully preserved. Verb aspect, case usage, and register are all correct. No false friends or calques. |
| 4    | Near-perfect. Minor issues that do not affect meaning (e.g., slightly awkward phrasing, a single case error in a low-impact position). |
| 3    | Some meaning is lost or distorted. Occasional incorrect verb aspect or case choices. A few false friends or calques present but main ideas are still communicated. |
| 2    | Notable semantic divergence. Several instances of incorrect verb aspect, systematic case errors, or register mismatches. The reader must infer intended meaning. |
| 1    | Frequent semantic errors. Meaning is regularly distorted. Aspect, case, and register errors are pervasive. Substantial portions are misleading or incorrect. |
| 0    | The translation does not convey the source meaning. It is semantically disconnected or incomprehensible as a representation of the source. |

### Key Semantic Factors (Polish-Specific)

- **Verb aspect** (perfective vs. imperfective): Wrong aspect changes meaning (habitual vs. one-time action, completed vs. ongoing).
- **Case errors** after prepositions, numerals, and negation can change meaning (e.g., "na stole" vs. "na stół" — location vs. direction).
- **False friends** (e.g., "aktualnie" for "actually") can completely change the intended message.
- **Double negation** omission or misapplication changes the logical meaning.

---

## Dimension 4: Format Compliance (FC) — Weight: 10%

Evaluates adherence to target-language formatting rules for the document type. Includes punctuation, quotation marks, title capitalization, list formatting, table structure, and heading hierarchy.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | Perfect format compliance. Polish quotation marks („...") used throughout. Em dashes properly spaced. Title sentence-case capitalization. Heading hierarchy preserved. Lists and tables correctly formatted. |
| 4    | High compliance. One or two minor deviations (e.g., a single heading with incorrect capitalization, one instance of English-style quotes). |
| 3    | Moderate compliance. Several formatting deviations. Mixed quotation mark styles. Inconsistent title casing. Some list/table formatting issues. |
| 2    | Low compliance. Frequent use of incorrect punctuation. Titles capitalized incorrectly throughout. Lists and tables poorly formatted or non-functional. |
| 1    | Very low compliance. Pervasive formatting errors. Document structure is degraded. Quotation marks, dashes, and spacing are predominantly incorrect. |
| 0    | Format requirements ignored. Document formatting is unusable — incorrect throughout all categories. |

### Format Checklist

- Polish quotation marks „..." (or secondary « » for nested quotes)
- Em dash (—) spaced on both sides
- Sentence-style title capitalization
- No comma before "że" / "iż" / "niż"
- DD.MM.YYYY date format
- 24-hour time notation
- Single space after periods

---

## Dimension 5: Completeness (CM) — Weight: 10%

Evaluates whether all source content is present in the translation. Includes text, numbers, footnotes, headers, footers, captions, and metadata.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | Complete. Every element from the source is present in the translation. No omissions, truncations, or skipped segments. |
| 4    | Near-complete. One or two trivial omissions (e.g., a minor caption, a single footnote) that do not affect document usability. |
| 3    | Several omissions present. An entire paragraph or multiple footnotes missing. Non-critical but noticeable. |
| 2    | Notable content gaps. Sections or substantial blocks of text omitted. Reader will notice missing content. |
| 1    | Large portions missing. More than 20% of source content omitted. Document is significantly incomplete. |
| 0    | Major incompleteness. Most of the source is missing or untranslated. |

### Completeness Checklist

- [ ] All paragraphs and sentences present
- [ ] All numerical data points present
- [ ] All table cells populated (or marked as intentionally blank)
- [ ] All footnotes and endnotes present
- [ ] All headers and footers translated
- [ ] All captions for figures, tables, and images translated
- [ ] All metadata (document title, subject, keywords) translated
- [ ] All hyperlink text translated (not the URLs themselves unless specified)

---

## Dimension 6: Inference / OCR Quality (IQ) — Weight: 5%

Evaluates how well the translator has handled degraded source text (scanned documents, OCR output, illegible sections). Applicable primarily when the source is not a clean digital text.

| Band | Criteria                                                                    |
|------|-----------------------------------------------------------------------------|
| 5    | Excellent handling. All illegible or degraded sections correctly reconstructed or marked. OCR artifacts properly identified and handled. Use of [przywrócono: ...] and other markers is appropriate, consistent, and minimal. |
| 4    | Good handling. Most degraded text correctly reconstructed. Minor inconsistency in marking convention (e.g., missing a marker for one restored section). |
| 3    | Adequate handling. Some degraded text left unresolved or incorrectly reconstructed. Markers used inconsistently. A few OCR artifacts passed through uncleaned. |
| 2    | Poor handling. Multiple instances of unresolved illegible text. Reconstruction errors present. Markers missing where needed. OCR artifacts in output. |
| 1    | Very poor handling. Widespread failure to reconstruct or mark degraded text. Significant OCR artifacts remain in output. |
| 0    | Unacceptable. No attempt to handle degraded text. Raw OCR output present throughout. Markers not used. |

### Handling Conventions

See Section 10 of base.md for full details. Key markers:

| Marker                          | Usage                                                   |
|---------------------------------|---------------------------------------------------------|
| [przywrócono: tekst]            | Reconstructed / restored text segment                   |
| [nierozpoznano]                 | Completely illegible, cannot be reconstructed            |
| [nierozpoznano: ~N znaków]     | Illegible segment of approximately N characters          |
| [niejasne: proponowany odczyt] | Uncertain transcription with proposed reading            |
| [błąd OCR]                      | Unresolvable OCR artifact in the original                |
| [obraz: treść niedostępna]      | Image content that could not be processed                |

---

## Scoring Procedure

### Step-by-Step

1. **Read the entire source and translation side by side.**
2. **Score each dimension independently.** Do not let a poor score in one dimension influence another.
3. **Calculate raw dimension scores:**
   ```
   Raw_Dimension_Score = (Band_Value / 5) × 100
   ```
4. **Calculate weighted dimension scores:**
   ```
   Weighted_Score = Raw_Dimension_Score × Weight_Percentage
   ```
5. **Sum all weighted scores** to obtain the Total Score (0–100).
6. **Check for zero-tolerance violations.** Apply global cap if triggered.
7. **Assign final grade:**

| Total Score | Grade     | Interpretation                                              |
|-------------|-----------|-------------------------------------------------------------|
| 90–100      | A         | Excellent. Ready for delivery.                              |
| 75–89       | B         | Good. Minor revisions recommended before delivery.          |
| 60–74       | C         | Adequate. Revision required before delivery.                |
| 40–59       | D         | Poor. Significant revision required.                        |
| 0–39        | F         | Unacceptable. Must be retranslated.                         |

### Quick Reference: Band-to-Weighted Points

| Band | NA (30%) | TC (20%) | SF (25%) | FC (10%) | CM (10%) | IQ (5%) |
|------|----------|----------|----------|----------|----------|---------|
| 5    | 30.00    | 20.00    | 25.00    | 10.00    | 10.00    | 5.00    |
| 4    | 24.00    | 16.00    | 20.00    | 8.00     | 8.00     | 4.00    |
| 3    | 18.00    | 12.00    | 15.00    | 6.00     | 6.00     | 3.00    |
| 2    | 12.00    | 8.00     | 10.00    | 4.00     | 4.00     | 2.00    |
| 1    | 6.00     | 4.00     | 5.00     | 2.00     | 2.00     | 1.00    |
| 0    | 0.00     | 0.00     | 0.00     | 0.00     | 0.00     | 0.00    |

### Scoring Example

| Dimension | Band | Raw Score | Weight | Weighted |
|-----------|------|-----------|--------|----------|
| NA        | 5    | 100       | 30%    | 30.00    |
| TC        | 4    | 80        | 20%    | 16.00    |
| SF        | 3    | 60        | 25%    | 15.00    |
| FC        | 4    | 80        | 10%    | 8.00     |
| CM        | 5    | 100       | 10%    | 10.00    |
| IQ        | 4    | 80        | 5%     | 4.00     |
| **Total** |      |           |        | **83.00** |

No zero-tolerance violations → Grade B (Good). Minor revisions recommended.

---

## Zero-Tolerance Violations — Definitive List

The following are **critical errors**. A single occurrence of any of these caps the Total Score at **60**. Two or more distinct occurrences (of any combination) cap at **40**. Three or more distinct occurrences result in an automatic **score of 0**.

### Zero-Tolerance Rules

| #  | Rule                              | Dimension | Description                                                                                             |
|----|-----------------------------------|-----------|---------------------------------------------------------------------------------------------------------|
| 1  | Decimal comma violation           | NA        | Using period instead of comma as decimal separator (e.g., `3.14` instead of `3,14`).                    |
| 2  | Date format violation             | NA        | Using non-Polish date format (e.g., `MM/DD/YYYY` or `YYYY/MM/DD`) instead of `DD.MM.YYYY`.              |
| 3  | Register mismatch (formal/informal)| SF       | Using "ty" verb forms (2nd person singular) where "Pan"/"Pani"/"Państwo" is required in a formal document.|
| 4  | Currency placement error          | NA        | Placing zł before the amount (e.g., `zł 100,00` instead of `100,00 zł`).                                |
| 5  | Wholesale diacritic omission      | NA/SF     | Systematic removal of Polish diacritics (ą, ć, ę, ł, ń, ó, ś, ź, ż) across the document.              |

### Zero-Tolerance Procedure

1. If a reviewer detects any ZT violation, they immediately flag it.
2. Count the **distinct type** of ZT violation (not the number of occurrences).
   - Five decimal-comma errors = 1 violation type.
   - Two decimal-comma errors + one date format error = 2 violation types.
3. Apply the cap:
   - 1 violation type → max score = 60.
   - 2 violation types → max score = 40.
   - 3+ violation types → score = 0.
4. The cap applies to the **final weighted total**, not to individual dimension scores.
5. Document all ZT violations in the review report.

---

## Reviewer Notes

### General Principles

- **Score the translation, not the source.** Poor source quality does not excuse translation errors.
- **Consider document purpose.** A legal contract demands higher precision than an internal memo. Adjust expectations proportionally but do not lower the rubric standards.
- **Document all findings.** For each dimension, note specific examples of errors and strengths.
- **One pass per dimension** is recommended to reduce halo effect (where an overall impression of quality colors individual dimension scores).

### Common Polish-Specific Pitfalls to Watch For

- **Decimal comma**: The most frequent and most critical error. Check every number.
- **Pan/Pani/ty**: Critical for formal documents. Scan for 2nd person singular verb forms.
- **Quotation marks**: „..." is the Polish standard, not "straight quotes".
- **That-comma rule**: No comma before "że", "iż", "niż" when they introduce a subordinate clause.
- **Sentence-case titles**: Only the first word and proper nouns capitalized in titles.
- **Double negation**: Required in Polish (e.g., "nikt nie przyszedł") — missing "nie" is an error.
- **Verb aspect**: Check that perfective/imperfective choices match the source meaning.

### Revision Categories

| Category     | Description                                                       | Action                           |
|--------------|-------------------------------------------------------------------|----------------------------------|
| Critical     | Zero-tolerance violation or error that changes meaning.           | Must be fixed before delivery.   |
| Major        | Error that affects comprehension but not a ZT violation.          | Should be fixed before delivery. |
| Minor        | Stylistic issue, awkward phrasing, or non-standard formatting.   | Recommend fix, may be optional.  |
| Suggestion   | Alternative wording that improves quality but is not an error.    | Optional.                        |

---

*This rubric is part of the Polish language knowledge base for the translating-documents skill. Reviewers should be trained on these criteria before scoring.*
