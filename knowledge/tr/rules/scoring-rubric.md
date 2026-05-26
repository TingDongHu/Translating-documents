---
id: tr/rules/scoring-rubric
type: rules
target_lang: tr
name: Turkish Translation Scoring Rubric
description: Turkish translation quality scoring rubric
---

# Turkish Translation Scoring Rubric

This rubric defines quality evaluation criteria for Turkish translations. Each dimension is scored on a 6-band scale (0-5). Scores are weighted and summed to produce a final quality score out of 100.

---

## Zero-Tolerance Rules

The following errors are **automatic failures** regardless of overall score. If any zero-tolerance violation is detected, the translation receives a **maximum score of 60** (or lower, if other errors further reduce it).

| Rule | Violation Example | Rationale |
|------|-------------------|-----------|
| Comma/Period in Decimals | Using period as decimal separator (`3.14` instead of `3,14`) or comma as thousands separator | Changes numerical meaning; critical in financial/technical documents |
| Date Format | Using MM.DD.YYYY or any format other than DD.MM.YYYY | Ambiguous dates (05/06 = May 6 or June 5); critical for legal/contractual precision |
| Sen/Siz Register | Switching between `sen` and `siz` for the same audience; using `sen` in formal legal/business context where `siz` is required | Register inconsistency damages professional credibility and audience trust |

---

## Scoring Dimensions

### Dimension 1: Numerical Accuracy (Weight: 30%)

Evaluates correctness of all numerical expressions including numbers, currencies, dates, times, percentages, and mathematical notation.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | Perfect numerical accuracy. All decimal commas, thousands periods, date formats (DD.MM.YYYY), 24h times, currency formats, and percentages are correct. Zero errors. |
| **Proficient** | **4** | Minor numerical issues that do not affect understanding. E.g., a single missing thousands period (`1000` instead of `1.000`), or a trailing zero inconsistency. |
| **Adequate** | **3** | Several numerical formatting errors but no meaning-changing mistakes. E.g., mixed decimal separators in 2-3 places, or inconsistent currency symbol placement. |
| **Limited** | **2** | Significant numerical formatting problems. E.g., wrong decimal separator in multiple places, dates in wrong format, or inconsistent number formatting across tables. |
| **Poor** | **1** | Pervasive numerical errors. Meaning is compromised in multiple instances. Numbers in different locales mixed inconsistently. |
| **Unacceptable** | **0** | Numerical information is unreliable. Decimal errors change values. Dates are ambiguous. Translation would cause real-world errors if used. |

**Scoring guidelines:**
- A single zero-tolerance violation (comma/period decimal or date format) automatically caps the translation at 60 overall and this dimension at maximum band 2 (score 2).
- Every zero-tolerance violation beyond the first reduces this dimension score by an additional 1 band.

---

### Dimension 2: Terminology Consistency (Weight: 20%)

Evaluates consistency of domain terminology, brand names, proper nouns, and key terms throughout the document.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | Perfect terminology consistency. Every term is translated consistently throughout. Proper nouns are handled correctly (Turkish special characters: ç/ğ/ı/ö/ş/ü/C/Ğ/İ/Ö/Ş/Ü). Foreign names are transcribed or preserved correctly. Acronyms are handled uniformly. |
| **Proficient** | **4** | One or two minor inconsistencies (e.g., a term translated differently once, or a proper noun missing Turkish characters in one instance). Overall terminology is well managed. |
| **Adequate** | **3** | Several inconsistent terms (3-5 instances). Some proper nouns lack Turkish special characters. Acronyms are introduced inconsistently. |
| **Limited** | **2** | Noticeable terminology drift. Key terms are translated 2-3 different ways. Proper nouns have recurring character errors (e.g., `Istanbul` instead of `İstanbul` throughout). |
| **Poor** | **1** | Pervasive inconsistency. The same term has 3+ variants. Proper nouns are systematically wrong (missing dotted İ, missing cedillas). Terminology appears careless. |
| **Unacceptable** | **0** | No evidence of terminology management. Terms are translated ad-hoc. Proper nouns are unrecognizable. Document reads as if multiple unrelated translators worked without coordination. |

**Scoring guidelines:**
- Create a terminology glossary from the source document and check each occurrence.
- Turkish character errors on proper nouns (`Istanbul` for `İstanbul`, `Izmır` for `İzmir`) reduce the score.
- Inconsistent translation of the same English term to different Turkish terms is penalized.

---

### Dimension 3: Semantic Fidelity (Weight: 25%)

Evaluates how accurately the translation conveys the source meaning, including nuance, tone, pragmatics, and domain-specific meaning.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | Perfect semantic transfer. All meaning, nuance, tone, and intent are preserved. No additions, omissions, or distortions. Idioms are appropriately adapted. The Turkish reader receives exactly the same information as the source reader. |
| **Proficient** | **4** | Very minor semantic shifts that do not affect overall meaning. E.g., a slightly weaker synonym, or a minor omission that does not impact comprehension. |
| **Adequate** | **3** | Some semantic errors. Occasional mistranslation of individual words or phrases. A few instances where the Turkish would be misunderstood differently from the source. Overall meaning is still recoverable. |
| **Limited** | **2** | Frequent semantic errors. Several sentences convey different meaning from the source. Key information is missing or distorted. Reader would get a notably different understanding in places. |
| **Poor** | **1** | Pervasive semantic errors. Large portions of the text convey different meaning. Critical information is lost or added. The translation is unreliable as a representation of the source. |
| **Unacceptable** | **0** | The translation does not represent the source. Meaning is fundamentally different. Would be considered a mistranslation. |

**Scoring guidelines:**
- Compare the translation against the source sentence by sentence.
- Check for false cognates and literal translations that distort meaning.
- Verify that technical/specialized terms carry the correct domain meaning.
- Assess whether pragmatic intent (warnings, requests, offers, etc.) is preserved.

---

### Dimension 4: Format Compliance (Weight: 10%)

Evaluates adherence to Turkish formatting standards, document structure, and layout rules.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | Perfect format compliance. All Turkish formatting rules followed: sentence-case titles, proper punctuation (Turkish quotation marks or consistent use), no double punctuation, proper kesme işareti usage with proper nouns, correct address format, correct list formatting. Document structure is preserved. |
| **Proficient** | **4** | Minor formatting issues. E.g., a single heading with incorrect capitalization, one instance of double punctuation, or one missing apostrophe on a proper noun suffix. |
| **Adequate** | **3** | Several formatting issues. Inconsistent title capitalization, recurring apostrophe errors (missing kesme işareti on proper noun suffixes), occasional double punctuation. Lists inconsistently formatted. |
| **Limited** | **2** | Significant formatting problems. Wrong quotation mark style throughout. Systematic apostrophe errors. Headings inconsistent. Tables not aligned properly. Document structure degraded. |
| **Poor** | **1** | Pervasive formatting errors. Turkish formatting rules largely ignored. English formatting conventions applied throughout. Kesme işareti missing systematically. Punctuation errors in most paragraphs. |
| **Unacceptable** | **0** | No attempt to follow Turkish formatting rules. Document is formatted according to source-language conventions. Structure is broken or missing. |

**Scoring guidelines:**
- Check the first 3 pages/paragraphs in detail, then scan the remainder for consistency.
- Verify: title case, apostrophe usage (kesme işareti), quotation marks, list formatting, and heading hierarchy.
- Pay special attention to possessive suffixes on proper nouns (`Ahmet'in`, `İstanbul'da`).

---

### Dimension 5: Completeness (Weight: 10%)

Evaluates whether all source content is present in the translation, including text, numbers, footnotes, captions, headers, and metadata.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | 100% complete. Every segment of the source is translated. No omissions. No content is left in the source language (except permissible untranslatables: brand names, proper names). Headers, footers, footnotes, captions, callouts, and metadata are all translated. |
| **Proficient** | **4** | Very minor omissions. E.g., one short caption left untranslated, or one footnote missed. No omission affects understanding of the core content. |
| **Adequate** | **3** | Some omissions. Multiple short segments left untranslated or skipped. An entire paragraph may be missing in one section. Core content is still mostly complete. |
| **Limited** | **2** | Significant omissions. Entire paragraphs or sections are missing. Multiple instances of untranslated source text. Reader cannot fully understand the document from the translation alone. |
| **Poor** | **1** | Large portions of the document are missing. More than 20% of content is absent or untranslated. Essential information is lacking. |
| **Unacceptable** | **0** | The translation is fundamentally incomplete. Major sections missing. The document cannot serve its purpose in Turkish. |

**Scoring guidelines:**
- Compare the translated document against the source document page by page.
- Check headers, footers, page numbers, table of contents, figure captions, and footnotes specifically (these are most commonly missed).
- Verify that all text in images/charts has been addressed.

---

### Dimension 6: Inference / OCR Quality (Weight: 5%)

Evaluates how well OCR artifacts are handled and how appropriately contextual inference is applied. Relevant when the source document is a scan or contains OCR artifacts.

| Band | Score | Description |
|------|-------|-------------|
| **Exemplary** | **5** | Excellent handling. All OCR artifacts that affect Turkish text are correctly identified and fixed. Turkish special characters are restored (ç/ğ/ı/ö/ş/ü/İ). Corrections are marked with `[geri yüklendi: ...]` where required by the project. Inferred text is accurate and justified. |
| **Proficient** | **4** | Good handling. Most OCR artifacts corrected. One or two minor issues remain (e.g., a single missed diacritic, or one instance where an unclear character was not flagged). |
| **Adequate** | **3** | Acceptable handling. Some OCR artifacts addressed, but several remain. Turkish character errors from OCR are partially corrected. A few instances of incorrect inference (guessing wrong word). |
| **Limited** | **2** | Poor OCR handling. Many OCR artifacts remain in the translation. Turkish characters are frequently wrong. The translator appears not to have reviewed the text for OCR issues. |
| **Poor** | **1** | Very poor OCR handling. OCR artifacts systematically carried into the translation. Turkish diacritics are missing or wrong in many words. Text is hard to read due to uncorrected OCR noise. |
| **Unacceptable** | **0** | No OCR cleanup performed. The translation is contaminated with source OCR errors. Turkish text is garbled with wrong characters. Unreadable in places. |

**Scoring guidelines:**
- Check for the most common Turkish OCR errors: `I` vs `İ`, missing cedillas (c → ç, s → ş), missing umlauts (o → ö, u → ü), and undotted/dotted i confusion.
- Verify that `[geri yüklendi: ...]` markers are present if required.
- Assess whether the translator made reasonable inferences for illegible source text.

---

## Scoring Calculation

### Weighted Score Formula

```
Total Score = (NA × 30) + (TC × 20) + (SF × 25) + (FC × 10) + (CP × 10) + (IQ × 5)
```

Where:
- NA = Numerical Accuracy score (0-5)
- TC = Terminology Consistency score (0-5)
- SF = Semantic Fidelity score (0-5)
- FC = Format Compliance score (0-5)
- CP = Completeness score (0-5)
- IQ = Inference/OCR Quality score (0-5)

Each dimension's weighted contribution:
- NA contributes 0-150 points (before normalization)
- TC contributes 0-100 points
- SF contributes 0-125 points
- FC contributes 0-50 points
- CP contributes 0-50 points
- IQ contributes 0-25 points

**Raw total range**: 0-500 points.

### Normalization

```
Final Score = Raw Total / 5
```

**Final score range**: 0-100.

### Global Cap

If any **zero-tolerance** rule is violated:
- The **Final Score is capped at a maximum of 60**, regardless of performance on other dimensions.
- The cap is applied after normalization.

### Overall Quality Bands

| Final Score | Quality Band | Interpretation |
|-------------|--------------|----------------|
| 90-100 | **Excellent** | Ready for delivery. Minor improvements optional. |
| 75-89 | **Good** | Minor revisions recommended before delivery. |
| 50-74 | **Fair** | Significant revisions required. Not deliverable as-is. |
| 25-49 | **Poor** | Major rework or retranslation needed. |
| 0-24 | **Unacceptable** | Complete retranslation required. |

### Cap Impact Illustration

| Dimension Scores | Raw Total | Normalized | Capped? | Final |
|-----------------|-----------|------------|---------|-------|
| All 5s | 500 | 100 | No | 100 |
| NA:5, TC:5, SF:5, FC:5, CP:5, IQ:5 | | | | |
| Near-perfect with ZT violation | 480 | 96 | Yes (ZT) | 60 |
| NA:4, TC:5, SF:5, FC:4, CP:5, IQ:5 | | | | |
| Moderate quality with ZT violation | 350 | 70 | Yes (ZT) | 60 |
| NA:3, TC:4, SF:3, FC:3, CP:4, IQ:4 | | | | |
| Moderate quality, no ZT violation | 350 | 70 | No | 70 |
| NA:3, TC:4, SF:3, FC:3, CP:4, IQ:4 | | | | |
| Poor quality with ZT violation | 200 | 40 | Yes (ZT) | 40 |
| NA:2, TC:2, SF:2, FC:2, CP:1, IQ:1 | | | | |

---

## Quality Review Checklist

For each translation, verify the following before scoring:

### Mandatory Checks (all documents)
- [ ] Decimal comma used throughout (not period)
- [ ] Thousands period used (not comma)
- [ ] Date format is DD.MM.YYYY
- [ ] 24-hour time format
- [ ] Sen/Siz register is consistent and appropriate
- [ ] Turkish special characters correct (ç/ğ/ı/ö/ş/ü/İ)
- [ ] Kesme işareti (apostrophe) used for proper noun suffixes
- [ ] Currency symbol placed after the amount
- [ ] Title case: sentence case used (first word only capitalized)
- [ ] Vowel harmony maintained in suffixes
- [ ] All source content is present
- [ ] SOV word order in declarative sentences

### Domain-Specific Checks
- [ ] Legal: Formal register, passive constructions, precise terminology
- [ ] Financial: Numerical accuracy critical, currency formatting verified
- [ ] Medical: Correct anatomical/medical terminology, no literal translation of drug names
- [ ] Technical: Consistent technical glossary, loanwords evaluated
- [ ] Marketing: Tone and register appropriate for target audience
- [ ] Academic: Nominalized structures, formal register, citation formats

### OCR-Specific Checks (if applicable)
- [ ] Dotted İ vs undotted I systematically checked
- [ ] Cedilla (ç/ş) restored correctly
- [ ] Umlaut (ö/ü) restored correctly
- [ ] Numeric OCR artifacts verified (0 vs O, 1 vs I/l)
- [ ] Corrections marked per project guidelines

---

## Scoring Examples

### Example 1: Financial Report (English → Turkish)

**Issue**: Decimal comma used correctly (`3,14`), but thousands separator is wrong (`,` used instead of `.`).

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| NA | 3 | Thousands separator error, but decimal comma is correct. Does not affect meaning. |
| TC | 4 | Terminology consistent. One minor proper noun issue. |
| SF | 5 | Perfect semantic transfer. |
| FC | 4 | One formatting issue (thousands separator). |
| CP | 5 | Complete. |
| IQ | 5 | No OCR issues. |

**Calculation**: `(3×30) + (4×20) + (5×25) + (4×10) + (5×10) + (5×5)` = `90 + 80 + 125 + 40 + 50 + 25` = `410` → `410/5 = 82.0`

**Result**: 82 (Good). Minor revisions recommended.

### Example 2: Technical Manual with OCR

**Issue**: Source was OCR'd. Several `Istanbul` instead of `İstanbul`, one `c` instead of `ç`. All corrected. One decimal period found: `0.5` instead of `0,5`.

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| NA | 1 | Zero-tolerance violation (decimal period). Capped at 60 overall. |
| TC | 5 | All terms and proper nouns correct after OCR correction. |
| SF | 5 | Perfect meaning transfer. |
| FC | 4 | Minor format issues. |
| CP | 5 | Complete. |
| IQ | 5 | OCR artifacts correctly handled. |

**Raw score**: `(1×30) + (5×20) + (5×25) + (4×10) + (5×10) + (5×5)` = `30 + 100 + 125 + 40 + 50 + 25` = `370` → `370/5 = 74`

**Global cap applied**: 60.

**Result**: 60 (Fair). The zero-tolerance violation (decimal period) caps the score despite otherwise high quality.

---

*End of Turkish Translation Scoring Rubric. This rubric should be applied consistently across all translation quality evaluations.*
