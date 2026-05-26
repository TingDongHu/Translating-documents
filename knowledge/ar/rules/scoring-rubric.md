---
id: ar/rules/scoring-rubric
type: rules
target_lang: ar
name: Arabic (ar) Translation Scoring Rubric — معيار تقييم جودة الترجمة العربية
description: Arabic translation quality scoring rubric
---

# Arabic (ar) Translation Scoring Rubric — معيار تقييم جودة الترجمة العربية

> Version 1.0 | Last updated: 2026-05-25
> Applies to: All scoring of Arabic (ar) document translations in the pipeline.
> Each dimension receives a band score (100, 90, 80, 70, 60, or <50). The weighted sum determines the final quality score.

---

## Zero-Tolerance Rules (قواعد عدم التسامح)

Certain errors are critical and automatically cap the entire translation score at **maximum 60**, regardless of performance in other dimensions.

| ID | Rule | Rationale |
|----|------|-----------|
| **ZT-1** | Mixing Arabic digits (١٢٣) and Western digits (123) in the same document | Confuses readers, signals extreme carelessness |
| **ZT-2** | Wrong calendar system (Hijri هـ vs Gregorian م) without proper context or mixing both incorrectly | Changes meaning of dates |
| **ZT-3** | Wrong gender agreement (مذكر/مؤنث) on verbs, adjectives, or pronouns that changes meaning | Grammatical error that impairs comprehension |
| **ZT-4** | Missing or incorrectly translated critical numerical values | Can cause financial or legal consequences |
| **ZT-5** | Left-to-right formatting for Arabic text (LTR instead of RTL) | Renders text unreadable in its script |
| **ZT-6** | Using العامية (dialectal Arabic) instead of الفصحى (MSA) in formal documents | Violates the core translation mandate |

If **any** zero-tolerance violation is detected:
- **Global cap**: Final score ≤ 60
- The dimension(s) affected get a band score of no higher than 60.
- An explicit flag must be raised in the scoring notes.

---

## Dimension 1: Numerical Accuracy (الدقة الرقمية)
**Weight: 30%**

This is the highest-weighted dimension because numerical errors have the most severe consequences in translated documents.

### Band Descriptors

| Band | Score | Criteria | Error Tolerance |
|------|-------|----------|-----------------|
| **Perfect** | **100** | Every number is correctly converted to the Arabic digit set (Eastern or Western, as chosen) with proper separators, negative signs, and percentages. All numeric values match the source exactly. | 0 errors |
| **Excellent** | **90** | Numbers are fully correct. Minor formatting issues only (e.g., thin space vs. thousands separator) that do not affect readability or meaning. | ≤1 minor formatting issue |
| **Good** | **80** | Numbers are correct but use inconsistent separator styles (e.g., sometimes comma, sometimes space for thousands). All digits belong to the same set. | ≤2 minor issues |
| **Adequate** | **70** | Most numbers are correct. One or two numbers may have minor digit mismatches (e.g., a single Western digit in an otherwise Arabic-digit document). | ≤3 issues, none affecting meaning |
| **Poor** | **60** | Several numbers are incorrectly formatted. Digit set is mostly consistent but has scattered errors. Separators are missing or wrong in multiple places. | 4–6 issues |
| **Fail** | **<50** | Widespread numerical errors. Digit set mixing is present (zero-tolerance if mixed throughout). Missing numbers, wrong values, or format so poor numbers are unreadable. | 7+ issues or any ZT-1/ZT-4 violation |

### Examples by Band

| Band | Translation | Issues |
|------|-------------|--------|
| 100 | بلغت الإيرادات ١٬٢٠٠٬٠٠٠ ﷼ في ٢٠٢٥م | Perfect: consistent Eastern Arabic digits, correct thousands separator, proper currency placement |
| 90 | بلغت الإيرادات ١,٢٠٠,٠٠٠ ﷼ في ٢٠٢٥م | Minor: Western comma used as thousands separator in an Arabic-digit context — acceptable but suboptimal |
| 80 | بلغت الإيرادات 1,200,000 ﷼ في 2025 | Mixed digits (Western 1,2,0 and Arabic digits elsewhere) — borderline, needs correction |
| 70 | بلغت الإيرادات ١٢٠٠٠٠٠ ﷼ | No thousands separator — readable but poor formatting |
| 60 | الإيرادات ١٢٠٠٠٠٠ ريال في ٢٠٢٥ | No separators, inconsistent — barely acceptable |
| <50 | الإيرادات 1,200,000 ریال في ٢٠٢٥ | Mixed digit sets (ZT-1 violation), wrong ی vs ي — automatic fail |

### Evaluation Checklist

- [ ] Are all digits from the same set (Eastern Arabic ٠–٩ or Western 0–9)?
- [ ] Is the decimal separator correct (٫ or .)?
- [ ] Are thousands grouped with the correct separator (٬ or space)?
- [ ] Are negative signs properly placed before the number?
- [ ] Are percentage symbols after the number with proper spacing?
- [ ] Do ordinal numbers use Arabic ordinals (الأول، الثاني...) not cardinals?
- [ ] Do numbers 3–10 show correct gender agreement with counted nouns?
- [ ] Is the dual form used for exactly 2?

---

## Dimension 2: Terminology Consistency (تناسق المصطلحات)
**Weight: 20%**

### Band Descriptors

| Band | Score | Criteria | Error Tolerance |
|------|-------|----------|-----------------|
| **Perfect** | **100** | Every term is translated consistently throughout the document. Technical terms, proper nouns, and key concepts use exactly the same Arabic equivalent every time. Glossary compliance is 100%. | 0 inconsistencies |
| **Excellent** | **90** | One or two minor inconsistencies that do not affect understanding (e.g., using الحاسوب once and الكمبيوتر elsewhere — both acceptable but inconsistent). | ≤2 minor inconsistencies |
| **Good** | **80** | Clear but not severe inconsistencies. A key term is translated two different ways in different sections. The meaning is still clear but the inconsistency is noticeable. | ≤3 inconsistencies |
| **Adequate** | **70** | Several terms are translated inconsistently. A reader may need to cross-reference to confirm meaning. Glossary compliance is below 80%. | 4–5 inconsistencies |
| **Poor** | **60** | Frequent inconsistencies across the document. Same English term appears with 3+ different Arabic translations. Technical terms are confused. | 6–8 inconsistencies |
| **Fail** | **<50** | Chaotic terminology. No consistent translation for key terms. Reader cannot rely on term-meaning mapping. Glossary compliance below 50%. | 9+ inconsistencies |

### Examples by Band

| Source Term | Band 100 | Band 80 | Band 60 |
|-------------|----------|---------|---------|
| "contract" (throughout) | العقد (every instance) | العقد once, الاتفاقية once | العقد، الاتفاقية، العقدة (wrong!) |
| "payment" | الدفع consistently | الدفع once, السداد once | الدفع، السداد، التسديد mixed |
| "software" | البرمجيات consistently | البرمجيات, البرامج | برمجيات، سوفتوير، البرامج |
| "auditor" | المراجع consistently | المدقق, المراجع | المدقق، المراجع، المفوض |

### Evaluation Checklist

- [ ] Is every key term mapped to a single Arabic equivalent?
- [ ] Are brand names and proper nouns consistent?
- [ ] Is there a project glossary? Does the translation follow it?
- [ ] Are loanword/transliteration choices consistent (e.g., always إيميل or always بريد إلكتروني)?
- [ ] Are abbreviation expansions consistent?

---

## Dimension 3: Semantic Fidelity (الدقة الدلالية)
**Weight: 25%**

### Band Descriptors

| Band | Score | Criteria |
|------|-------|----------|
| **Perfect** | **100** | Meaning is perfectly preserved. Every sentence conveys exactly the same information as the source. No additions, omissions, or distortions. Natural Arabic expression does not compromise accuracy. |
| **Excellent** | **90** | Meaning is fully preserved. Minor differences in emphasis or stylistic choices that do not change the information content. All facts, figures, and assertions are correctly transmitted. |
| **Good** | **80** | Meaning is preserved but with some loss of nuance. Complex sentences may lose some detail or clarity. Key points are all present but the Arabic expression is slightly imprecise. |
| **Adequate** | **70** | The gist of the source is preserved but significant details are lost or altered. Some sentences are ambiguous in Arabic. A few concepts are mistranslated, but the overall message survives. |
| **Poor** | **60** | Multiple sentences are mistranslated. The Arabic version diverges from the source in meaning for several passages. Key facts or claims are distorted. Meaning is recoverable but unreliable. |
| **Fail** | **<50** | Widespread mistranslation. The Arabic text conveys a different meaning from the source for critical passages. The translation is unreliable for any purpose. |

### Specific Checks for Arabic Semantic Fidelity

| Aspect | Good | Poor |
|--------|------|------|
| Idiom translation | "Break the ice" → كسر الحاجز / كسر الجمود (idiomatic equivalent) | "Break the ice" → كسر الثلج (literal, meaningless) |
| Passive voice | "It was decided" → تقرر (natural Arabic passive) | "It was decided" → تم اتخاذه القرار (grammatically wrong) |
| Hypotheticals | "If we had known" → لو كنا نعلم (correct conditional) | "If we had known" → إذا كنا نعلم (wrong conditional particle) |
| Negation scope | "Not all students came" → لم يأت جميع الطلاب | "Not all students came" → جميع الطلاب لم يأتوا (ambiguous: could mean "none came") |
| Quantifiers | "Several studies" → عدة دراسات | "Several studies" → سبع دراسات (wrong: seven ≠ several) |

### Evaluation Checklist

- [ ] Does every sentence in the Arabic match the source in propositional content?
- [ ] Are idioms handled with Arabic equivalents (not literal translations)?
- [ ] Are complex sentences (multiple clauses) properly decomposed into natural Arabic?
- [ ] Are quantifiers, negations, and modals correctly translated?
- [ ] Is pragmatic meaning (implicature, tone) preserved?
- [ ] Are ambiguous source sentences disambiguated correctly in Arabic?
- [ ] Does the translation add or omit any information?

---

## Dimension 4: Format Compliance (الالتزام بالتنسيق)
**Weight: 10%**

### Band Descriptors

| Band | Score | Criteria |
|------|-------|----------|
| **Perfect** | **100** | Perfect RTL layout. Right-aligned paragraphs, RTL lists with right-side numbering, correct table direction. Arabic punctuation (، ؟ ;) used consistently. No LTR layout artifacts. |
| **Excellent** | **90** | RTL layout is correct. One or two minor formatting issues (e.g., a single Western punctuation mark, minor spacing inconsistency). |
| **Good** | **80** | Most formatting is correct. Some paragraphs may be left-aligned incorrectly, or Western commas are used in a few places. Lists are mostly RTL but may have one LTR list. |
| **Adequate** | **70** | RTL is applied but inconsistently. Several paragraphs are left-aligned. Punctuation is mixed (Arabic and Western). Lists may display in wrong direction. |
| **Poor** | **60** | Significant formatting problems. Large sections are left-aligned. Arabic punctuation is rarely used. Lists and tables follow LTR conventions. RTL is partially broken. |
| **Fail** | **<50** | Document is formatted as LTR despite containing Arabic text. Right-to-left rendering is broken. Text may appear reversed or jumbled. (ZT-5 violation). |

### Key Checks for Arabic Formatting

| Element | Correct | Incorrect |
|---------|---------|-----------|
| Paragraph alignment | Right-aligned | Left-aligned or centered |
| Bullet direction | Bullet on right | Bullet on left |
| Numbered list | ٣. ٢. ١. | 1. 2. 3. |
| Arabic comma | ، | , |
| Arabic question mark | ؟ | ? |
| Arabic semicolon | ؛ | ; |
| Kashida usage | None (unless calligraphic) | Extraneous kashida |
| Quotation marks | " " or « » | Improperly oriented quotes |
| Table direction | RTL (first column is header on right) | LTR table layout |
| Mixed bidi | Proper LRM/RLM marks | Text overlaps or displays out of order |
| Parentheses spacing | (النص) | ( النص ) (spaces inside) |

### Format Compliance Examples

| Issue | Fails At... | Because |
|-------|-------------|---------|
| Left-aligned Arabic body text | ≤70 | Fundamental RTL violation |
| Western comma instead of ، | ≤80 | Arabic punctuation rule |
| Bullet list with bullets on left | ≤80 | List direction is wrong |
| Kashida in every word | ≤70 | OCR residue / style error |
| Numbers in LTR direction within RTL paragraph | 100 if correct | This is actually correct bidi behavior — numbers are LTR in RTL |
| Table headers on left column | ≤70 | Table direction is LTR in Arabic |
| Mixing « and " randomly | ≤80 | Inconsistent quotation style |

### Evaluation Checklist

- [ ] Are all paragraphs right-aligned?
- [ ] Are list markers on the right side?
- [ ] Is Arabic punctuation used for Arabic text (، ؟ ؛)?
- [ ] Are Western punctuation marks used only for embedded LTR text?
- [ ] Are quotation marks consistently styled?
- [ ] Are tables in RTL orientation?
- [ ] Is bidi content (mixed English/Arabic) rendered correctly?
- [ ] Are there no extraneous kashida/tatweel characters?

---

## Dimension 5: Completeness (الاكتمال)
**Weight: 10%**

### Band Descriptors

| Band | Score | Criteria |
|------|-------|----------|
| **Perfect** | **100** | Every segment of the source is translated. No omissions. All headings, footnotes, captions, alt text, table cells, and marginal content are present. |
| **Excellent** | **90** | One minor omission (e.g., a single caption or footnote) that does not affect document comprehension. |
| **Good** | **80** | A small section (1–2 sentences) is omitted from the translation. All major content is present. |
| **Adequate** | **70** | Several sentences or one paragraph is omitted. A section heading may be missing. Missing content affects flow but not core message. |
| **Poor** | **60** | A substantial section (one or more paragraphs) is missing. Multiple headings or table rows are untranslated. |
| **Fail** | **<50** | Large portions of the document are untranslated. Key sections, entire tables, or critical content is missing. |

### Specific Checks for Arabic Completeness

| Content Type | Check |
|-------------|-------|
| Body text | Every paragraph has an Arabic equivalent |
| Headings | All section headings and subheadings translated |
| Table headers | Header row/cell is translated |
| Table data | Every cell has Arabic content |
| Captions | Figure and table captions are translated |
| Footnotes/Endnotes | All notes are present |
| Page headers/footers | Running headers and page numbers |
| Alt text | Image descriptions (if present) are translated |
| Legal disclaimers | All disclaimers, copyright notices translated |
| Watermarks | Any text in watermarks is addressed |

### Evaluation Checklist

- [ ] Is every paragraph translated?
- [ ] Are all headings and subheadings present in Arabic?
- [ ] Are all table cells filled?
- [ ] Are footnotes and endnotes translated?
- [ ] Are captions and labels translated?
- [ ] Are page header/footer elements translated?
- [ ] Is the total page count comparable to the source (accounting for Arabic text expansion)?

---

## Dimension 6: Inference / OCR Quality (جودة الاستنتاج ومعالجة OCR)
**Weight: 5%**

### Band Descriptors

| Band | Score | Criteria |
|------|-------|----------|
| **Perfect** | **100** | No OCR artifacts present. All restored/ inferred text is properly marked with [تم الاستعادة: ...] where applicable. Contextual restorations are accurate and well-justified. |
| **Excellent** | **90** | OCR artifacts are fully cleaned. One or two minor issues such as an unnecessary restoration marker or a missed diacritic. |
| **Good** | **80** | Most OCR issues resolved. Some residual errors (e.g., taa marbuta ة vs هـ confusion, a few kashida characters remaining). |
| **Adequate** | **70** | Several OCR artifacts remain. Occasional ghost characters, split ligatures (لا → ل ا), or wrong dot counts. Restorations are present but a few are incorrect. |
| **Poor** | **60** | Many OCR issues uncorrected. Multiple wrong letters, uncleaned kashida, missing hamza/alif. Restoration markers used inconsistently. |
| **Fail** | **<50** | Heavy OCR contamination. Text is unreliable due to uncorrected recognition errors. Restoration markers missing or wrong. Characters are frequently confused. |

### Arabic-Specific OCR Issues Checklist

| Issue | Example | Severity |
|-------|---------|----------|
| Kashida residue | كتاب → كـــتاب | Low (cosmetic) |
| Taa marbuta ↔ ha | مدرسة → مدرسه | Medium (spelling) |
| Alif hamza confusion | هذا الأب → هذا الاب | Medium (grammar) |
| Lam-alif separation | لا → ل ا | Medium (readability) |
| Dot count errors | شجرة → سجرة | High (meaning change) |
| Yeh vs alif maqsurah | على → علی | Low (stylistic in some fonts) |
| Missing dots entirely | ب/ت/ث/ن confusion | High (meaning change) |
| ع/غ confusion | غرفة → عرفة | High (meaning change) |
| Missing space after ال | الكتاب →الكتاب | Low (cosmetic) |
| Extra space before ال | ال كتاب → ال كتاب | Low (cosmetic) |

### Evaluation Checklist

- [ ] Are all kashida/tatweel characters removed?
- [ ] Are taa marbuta (ة) and ha (ه) correctly distinguished?
- [ ] Are all hamza variants (أ, إ, ؤ, ئ) correct?
- [ ] Are lam-alif ligatures properly formed (لا not ل ا)?
- [ ] Are dots on letters correct (no ب→ت→ث confusion)?
- [ ] Are dot-based letter pairs correct (س/ش, ح/ج/خ, ع/غ, ف/ق)?
- [ ] Are restoration markers used consistently and correctly?
- [ ] Does the text have correct spacing (especially around ال)?
- [ ] Are diacritics correct where present?
- [ ] Is alif maqsurah (ى) vs. yeh (ی) correct for the target region?

---

## Score Computation (احتساب الدرجة النهائية)

### Formula

```
Final Score = Σ (Dimension Score × Weight)
```

| Dimension | Weight | Your Score | Weighted |
|-----------|--------|------------|----------|
| 1. Numerical Accuracy | 30% | ___ | × 0.30 = ___ |
| 2. Terminology Consistency | 20% | ___ | × 0.20 = ___ |
| 3. Semantic Fidelity | 25% | ___ | × 0.25 = ___ |
| 4. Format Compliance | 10% | ___ | × 0.10 = ___ |
| 5. Completeness | 10% | ___ | × 0.10 = ___ |
| 6. Inference/OCR Quality | 5% | ___ | × 0.05 = ___ |
| **Total** | **100%** | | **___** |

### Final Score Bands

| Final Score | Grade | Action |
|-------------|-------|--------|
| 95–100 | ممتاز (Excellent) | Pass — no revision needed |
| 85–94 | جيد جدًا (Very Good) | Pass — minor corrections advised |
| 75–84 | جيد (Good) | Conditional pass — corrections required |
| 65–74 | مقبول (Adequate) | Revise and resubmit |
| 50–64 | ضعيف (Poor) | Major revision needed |
| <50 | راسب (Fail) | Complete retranslation required |

### Global Cap Application

If any zero-tolerance rule (ZT-1 through ZT-6) is violated:
1. The affected dimension(s) are capped at band 60 maximum.
2. The overall score is capped at **60 maximum**, regardless of weighted computation.
3. The translation must be flagged for revision regardless of other dimension scores.

### Scoring Notes

- **Decimal scores**: Round to one decimal place.
- **Band boundaries**: When a translation falls between two bands, use professional judgment. Document the rationale.
- **Context matters**: A 70 in one genre may be a 90 in another. Consider the document type and audience.
- **Severity weighting**: Within a dimension, a single critical error may be enough to drop the band more than several minor errors. Use judgment.

---

## Quick Reference Card

| Dimension | Weight | Key Things to Check | Zero-Tolerance? |
|-----------|--------|---------------------|-----------------|
| Numerical Accuracy | 30% | Digit set consistency, separators, gender agreement | Yes (ZT-1, ZT-4) |
| Terminology Consistency | 20% | One term = one translation, glossary compliance | No |
| Semantic Fidelity | 25% | Meaning preservation, idiom handling, nuance | No |
| Format Compliance | 10% | RTL layout, Arabic punctuation, list direction | Yes (ZT-5) |
| Completeness | 10% | All content translated, nothing missing | No |
| Inference/OCR Quality | 5% | Cleaned artifacts, correct letter forms | No |

---

> This rubric is part of the Arabic (ar) translation knowledge base. For full translation rules, see `base.md`.
