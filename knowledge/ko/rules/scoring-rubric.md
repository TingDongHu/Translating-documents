---
id: ko/rules/scoring-rubric
type: rules
target_lang: ko
name: Korean (ko) QA Scoring Rubric
description: Korean translation quality scoring rubric
---

# Korean (ko) QA Scoring Rubric

> Target language: Korean (한국어)
> ISO 639-1: `ko` | ISO 639-2: `kor`
> Version: 1.0 / 2026-05-25

---

## Overview

This rubric defines six quality dimensions for evaluating Korean translations. Each dimension is scored on a six-band scale (100 / 90 / 80 / 70 / 60 / <50), and the weighted sum produces a final score out of 100.

### Dimension Weighting

| # | Dimension | Weight |
|---|-----------|--------|
| 1 | Numerical Accuracy | 30% |
| 2 | Terminology Consistency | 20% |
| 3 | Semantic Fidelity | 25% |
| 4 | Format Compliance | 10% |
| 5 | Completeness | 10% |
| 6 | Inference/OCR Quality | 5% |
| **Total** | | **100%** |

### Zero-Tolerance Rule

Any **critical error** in **any dimension** caps the **maximum possible final score at 60**. Critical errors include:
- Number/digit transposition or omission
- Date or currency value error
- Reversed meaning (translating the opposite of the source)
- Untranslated source-language segments
- Complete omission of a required section
- Use of wrong honorific level causing offense
- Wrong company name or proper noun

---

## Dimension 1: Numerical Accuracy (30%)

**Evaluates correctness of all numbers, digits, dates, currencies, percentages, units, and numerical expressions.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | All numbers, dates, currencies exactly match source. Decimal separators, thousands separators, 만/억/조 conversion are correct. | Source `$1,234,567.89` → `1,234,567.89달러` or `약 123만 달러` (context-appropriate). All digits match source. |
| 90 | Near-perfect | All numbers and dates correct. One minor formatting deviation (e.g., using `-` for range instead of `~`, or using 만 when source is 1,000,000 but context called for comma format). | Source `10,000` → `10,000` correct, but range `10-20` instead of `10~20` (format style issue, not accuracy issue). |
| 80 | Good | All numbers correct. One or two minor issues: missing decimal zero (e.g., `3.5` instead of `3.50`) or inconsistent use of 만/억/조 within same document. | Source `3.50` → `3.5` (significant digit dropped); source `1,500,000` and `2,000,000` → `150만` and `200만` inconsistent. |
| 70 | Adequate | All core numbers correct but 2-4 presentation issues. Decimal comma not converted (e.g., source `3,14` (FR) → KO `3,14` instead of `3.14`). Some unit conversions missing. | Source `3,14 m` (French) → `3.14m` (wrong: should be `3.14 m` with space). Or `100°F` not converted to `38°C`. |
| 60 | Poor | One or more **number substitution errors** (wrong digit). Multiple formatting violations. This band automatically applies if any single critical number error is found. | Source `$1,000` → `100달러` (dropped a zero -- CRITICAL). Or `2024` → `2025` (wrong year). |
| <50 | Failing | Multiple number errors. Dates off by day/month/year. Currency amounts wrong. Percentage values incorrect. | Source `$50,000` → `5,000원` (both amount and currency wrong). Source `2024/03/15` → `2025년 13월 15일`. Score drops below 50. |

### Zero-Tolerance Items for Numerical Accuracy

| Item | Why Zero-Tolerance | Consequence |
|---|---|---|
| Any digit transposition (e.g., 12,345 vs 12,435) | Financial/legal risk | Automatic max 60 cap |
| Wrong year/month/day in dates | Schedule/compliance risk | Automatic max 60 cap |
| Currency conversion error (wrong unit) | Financial risk | Automatic max 60 cap |
| Percentage sign omitted or misplaced | Data integrity risk | Automatic max 60 cap |
| Decimal comma not converted (source `3,14` remains `3,14`) | Format violation | -20 per occurrence |

### KO-Specific Numerical Checks

- [ ] 만/억/조 units: Are large numbers expressed naturally for the genre?
- [ ] Decimal: Is `.` used (not `,`)?
- [ ] Thousands: Is `,` used correctly?
- [ ] Range: Is `~` used for ranges (not `-`)?
- [ ] Unit spacing: Is there a space between number and unit (`5 km`, not `5km`)?
- [ ] Currency: Is `원` placed after the number (`10,000원`)?
- [ ] Counters: Are Korean counters correct (`5명`, `3개`, `2권`)?

---

## Dimension 2: Terminology Consistency (20%)

**Evaluates consistency of term usage, loanword transcription, and avoidance of unjustified variation. Tolerates legitimate loanword variation where both forms are established.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | Every source term maps to exactly one KO term throughout. Loanwords follow 외래어 표기법. No arbitrary variation. | Source "file" → always `파일` (never `파일`/`화일`/`문서` mixed). |
| 90 | Near-perfect | One minor inconsistency across the entire document. Loanwords correctly transcribed. | Source "update" used 15 times: 14 times `업데이트`, once `갱신` in a compound term where it is legitimate (e.g., `갱신 주기`). |
| 80 | Good | 2-3 inconsistent terms. Loanword transcription is mostly correct with 1 deviation from 외래어 표기법. | Source "schedule" → mixed `스케줄` and `일정`. Or source "feedback" → `피드백` correctly but "feature" → `피쳐` instead of `기능` or `피처`. |
| 70 | Adequate | 4-6 inconsistent terms. Noticeable loanword transcription errors. Some terms vary arbitrarily between sections. | Source "management" → `경영`, `관리`, `매니지먼트` mixed across sections. Source "service" → `서비스` correct but "device" → `디바이스` instead of `장치`. |
| 60 | Poor | 7+ inconsistent terms. Systematic loanword errors. Key technical terms vary without reason. Wrong 외래어 표기법 applied. | Source "data" → `데이타` instead of `데이터`. Source "quality" → `퀄리티` in formal report where `품질` required. Multiple critical terms inconsistent. |
| <50 | Failing | Chaotic terminology. Same term translated 3+ different ways. Loanwords unrecognizable. No terminological discipline. | Source "algorithm" → `알고리즘`, `알고리듬`, `계산법`, `알고리즘` all in same paragraph. Source "system" → `시스템`, `체계`, `시스템즈`. |

### Loanword Variation Tolerance

Korean permits certain loanword variations. The following are **acceptable** (both forms are correct):

| Term | Variant 1 | Variant 2 | Status |
|---|---|---|---|
| algorithm | 알고리즘 | 알고리듬 | Both acceptable |
| data | 데이터 | 데이타 | 데이터 preferred (standard) |
| schedule | 스케줄 | 스케쥴 | 스케줄 preferred |
| file | 파일 | 화일 | 파일 preferred (화일 is older) |
| internet | 인터넷 | 인테넷 | 인터넷 is ONLY correct |
| computer | 컴퓨터 | 콤퓨터 | 컴퓨터 is ONLY correct |
| tip | 팁 | 팁 (same) | No variation |
| piano | 피아노 | 피아노 (same) | No variation |
| radio | 라디오 | 라디오 (same) | No variation |

**Decision rule:** When both variants are established, choose the one listed first in the Standard Korean Language Dictionary (표준국어대사전) and use it consistently.

### Zero-Tolerance Items for Terminology

| Item | Why Zero-Tolerance | Consequence |
|---|---|---|
| Company/brand name wrong | Legal/trademark risk | Automatic max 60 cap |
| Person name transcribed differently in same doc | Identity confusion | -20 per occurrence |
| Critical technical term reversed (e.g., input/output swapped) | Functional risk | Automatic max 60 cap |
| Formal document uses casual loanword where formal term exists | Tone violation | -10 per occurrence |

### KO-Specific Terminology Checks

- [ ] Are all company names using their official Korean registration?
- [ ] Are person names consistently transcribed?
- [ ] Is 외래어 표기법 followed for new terms?
- [ ] Does the document mix formal Korean (품질) and loanword (퀄리티) without reason?
- [ ] Are naturalized loanwords (콘텐츠, 데이터, 서비스) used correctly?

---

## Dimension 3: Semantic Fidelity (25%)

**Evaluates how accurately the translation conveys the meaning, nuance, intent, and pragmatic force of the source text.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | Full semantic equivalence. Meaning, nuance, register, and pragmatics all match source. No addition, omission, or distortion. | Source "The committee carefully reviewed the proposal." → `위원회는 제안서를 면밀히 검토했습니다.` All semantic components present. |
| 90 | Near-perfect | Very minor nuance shift that does not affect meaning. Slight register difference. | Source "considerable resources" → `상당한 자원` (perfect); but `꽤 많은 자원` carries slightly different tone. Meaning intact. |
| 80 | Good | Minor detail omitted or added but core meaning preserved. Some stylistic flattening (idiom → plain language). | Source "He bent over backwards to help" → `그는 도와주려고 매우 노력했다` (idiom lost but meaning kept). Or source "carefully examined" → `검토했다` (carefully dropped). |
| 70 | Adequate | Noticeable meaning loss or added interpretation. Source nuance partially lost. Reader may need to infer missing information. | Source "The results suggest a possible correlation" → `결과는 상관관계를 보여준다` (hedging/uncertainty lost; "suggest possible" ≠ "show"). |
| 60 | Poor | Significant meaning distortion. Key information wrong. This band applies automatically if **any critical semantic error** is found. | Source "He resigned from his position" → `그는 해고당했다` (resigned vs fired -- opposite meaning). Or source "We recommend against" → `찬성합니다` (opposite). |
| <50 | Failing | Complete misrepresentation of source meaning. Translation says the opposite of the source. Gibberish or hallucinated content. | Source "Turn left at the intersection" → `교차로에서 우회전하세요` (left vs right). Source unrelated to target. |

### Critical Semantic Errors (Any One Triggers Max 60 Cap)

| Error Type | Example |
|---|---|
| Meaning reversal | Source "increase" → `감소` (decrease) |
| Yes/No inversion | Source "Do not open" → `열어도 됩니다` (may open) |
| Negation error | Source "not applicable" → `적용 가능` (applicable) |
| Direction/polarity error | Source "above 0°C" → `영하` (below zero) |
| Legal/contractual meaning error | Source "shall not" → `할 수 있다` (may) |
| Medical/safety meaning error | Source "take 1 tablet" → `2정 복용` (2 tablets) |

### KO-Specific Semantic Checks

- [ ] Are Korean particles correct for the intended meaning (은/는 topic vs 이/가 subject)?
- [ ] Is the passive/active voice correct for the meaning?
- [ ] Has English "it" been resolved to a concrete Korean referent?
- [ ] Are false cognates avoided (`가지다` for "have," `놓치다` for "miss")?
- [ ] Does the KO honorific level correctly reflect the source relationship?
- [ ] Are culturally specific concepts adapted or annotated?
- [ ] Has 당신 been avoided when the source uses "you"?

---

## Dimension 4: Format Compliance (10%)

**Evaluates adherence to Korean formatting conventions: punctuation, spacing, title hierarchy, list style, table structure, and layout.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | All punctuation and spacing follow Korean rules. Quotation marks converted. Title hierarchy consistent. Tables and lists properly formatted. | CJK 。→ `.`, 、→ `,`, 「」→ `""`. Correct spacing. Consistent heading levels. |
| 90 | Near-perfect | One minor format deviation. E.g., one instance of CJK period (。) not converted, or one table header not translated. | Source "Chapter 1" translated as `Chapter 1` instead of `제1장` in one place. |
| 80 | Good | 2-3 format issues. Some punctuation not converted. Occasional spacing errors. | 2 remaining CJK quotation marks. One table with untranslated EN header. Occasional missing spaces after particles. |
| 70 | Adequate | 4-6 format issues. Systematic punctuation conversion incomplete. Title hierarchy inconsistent. | Half the CJK 。 converted. Title levels jump from H1 to H3 inconsistently. Multiple spacing errors. |
| 60 | Poor | 7+ format violations. Major formatting elements not converted. Unacceptable for publication. | Most CJK punctuation retained. No consistent heading system. Raw EN table headers in KO document. |
| <50 | Failing | Formatting completely broken. No punctuation conversion. No consistent structure. | Raw 。、、「」 everywhere. No headings. Tables collapsed. Unreadable formatting. |

### Zero-Tolerance Items for Format

| Item | Why Zero-Tolerance | Consequence |
|---|---|---|
| CJK 。 retained as period | KO does not use 。 | -15 per occurrence; systematic failure → max 60 |
| CJK 、 retained as comma | KO does not use 、 | -10 per occurrence |
| Heading hierarchy broken (missing levels) | Structural integrity | -10 per occurrence |
| Table structure destroyed | Data integrity | -15 per occurrence |

### KO-Specific Format Checks

- [ ] Punctuation: 。 → `.` , 、 → `,` , 「」→ `""` ?
- [ ] Ranges: Are `~` used instead of `-` for spans?
- [ ] Spacing: Are particles attached (학교에, not 학교 에)?
- [ ] Titles: Are chapter/section labels in Korean (제1장, not Chapter 1)?
- [ ] Lists: Are bullet styles consistent?
- [ ] Tables: Are all headers translated?
- [ ] Ellipsis: Are `...` used (not `。。`) ?

---

## Dimension 5: Completeness (10%)

**Evaluates whether all source content has been translated -- no missing sentences, paragraphs, sections, footnotes, captions, or metadata.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | 100% of source content translated. Every heading, caption, footnote, alt-text, label, and marginal note is covered. | Source has 15 paragraphs, 3 tables, 2 footnotes, 5 figure captions -- all translated. |
| 90 | Near-perfect | One very minor omission (e.g., one alt-text label or one footnote reference mark missed). | Source figure caption `Fig. 1: Results` → `그림 1: 결과` (all present) but one `(continued)` label missed. |
| 80 | Good | One sentence or short phrase omitted. Non-critical content gap. | A parenthetical comment `(see above)` not translated. Source list item 4 of 10 omitted. |
| 70 | Adequate | 2-4 sentences omitted OR one entire short paragraph omitted. Noticeable content gap. | Source second paragraph of section 3.2 entirely missing. Or 3 footnote texts not translated. |
| 60 | Poor | 5+ sentences or 1+ significant paragraph omitted. Missing content affects understanding. This band applies automatically if a **required section** is entirely missing. | Entire concluding paragraph missing. Or a section heading is absent. |
| <50 | Failing | Large portions of text untranslated. Multiple paragraphs or entire sections missing. Reader cannot follow the document. | 30%+ of source text untranslated. Multiple section headings in EN. |

### Zero-Tolerance Items for Completeness

| Item | Why Zero-Tolerance | Consequence |
|---|---|---|
| Entire section/paragraph missing | Structural gap | Automatic max 60 cap |
| Legal/required clause omitted | Legal risk | Automatic max 60 cap |
| Figure/table caption missing | Reference broken | -15 per occurrence |
| Source language text left untranslated | Readability failure | -10 per occurrence |

### KO-Specific Completeness Checks

- [ ] Are all figure/table references translated? (`Fig. 1` → `그림 1`)
- [ ] Are all footnotes/endnotes translated?
- [ ] Are all appendix sections translated?
- [ ] Are all table headers and cell contents translated?
- [ ] Are all UI strings (buttons, menus, messages) translated?
- [ ] Are all headers, footers, page numbers, and running heads translated?
- [ ] Is metadata (document properties, keywords) translated if specified?

---

## Dimension 6: Inference/OCR Quality (5%)

**Evaluates handling of OCR-originated text: correct restoration, proper notation of uncertain text, and handling of degraded source quality.**

| Score | Band | Criteria | Korean Example |
|---|---|---|---|
| 100 | Perfect | All OCR artifacts correctly identified and restored. Restoration notation `[복원: ...]` used correctly and consistently. No undetected corruption. | OCR `ΩI 己卜ΩI` → `[복원: ΩI 己卜ΩI → 여기 있어요]`. All ambiguous chars annotated. |
| 90 | Near-perfect | One minor restoration not annotated, OR one annotation used where not needed. | OCR `안녕하세Ω` → `안녕하세요` without annotation (minor; or annotation present but slightly awkward). |
| 80 | Good | 2-3 restoration issues. Some OCR corruption silently passed through (restored without notation). Some unnecessary annotations. | OCR `cjalfdls` → `확인합니다` (restored correctly but no annotation showing the original was corrupt). |
| 70 | Adequate | 4-6 restoration issues. Some corrupted text not caught. Notation format inconsistent. | Mix of `[복원:]` and `[추정:]` without clear distinction. Some illegible characters silently skipped. |
| 60 | Poor | 7+ restoration issues. Significant OCR corruption passed through without annotation. Restoration notation missing for key illegible passages. | Entire corrupted sentence restored without `[복원:]` notation. Reader has no way to know text was restored from OCR. |
| <50 | Failing | OCR corruption completely mishandled. Wrong restoration (guessed wrong character). No notation used at all. | OCR `ql` → left as `ql` (not restored). Or OCR `ΩI` → restored as `01` (should be `이` but guessed numbers instead). |

### Zero-Tolerance Items for OCR/Inference

| Item | Why Zero-Tolerance | Consequence |
|---|---|---|
| Corrupted text left as garbage characters | Unreadable | -20 per occurrence |
| Wrong restoration (guessed incorrectly) | Disinformation risk | -20 per occurrence; critical → max 60 cap |
| No notation where text is clearly corrupt | Transparency failure | -10 per occurrence |
| Original meaning changed during restoration | Data integrity breach | Automatic max 60 cap |

### KO-Specific OCR/Inference Checks

- [ ] Are common KO OCR confusions caught (Ω→요, OI→이, ql→을)?
- [ ] Is `[복원: ...]` notation used for restored text?
- [ ] Is `[복원불가]` used for unrecoverable text?
- [ ] Are Hangul jamo-level OCR errors (ㄱ→ㅋ, ㅓ→ㅏ) caught?
- [ ] Are Latin-character misrecognitions of Hangul caught?
- [ ] Is the restoration faithful to the original meaning (not paraphrasing)?

---

## Scoring Calculation

### Weighted Score Formula

```
Final Score = (NA × 0.30) + (TC × 0.20) + (SF × 0.25) + (FC × 0.10) + (CM × 0.10) + (IQ × 0.05)
```

Where:
- NA = Numerical Accuracy score
- TC = Terminology Consistency score
- SF = Semantic Fidelity score
- FC = Format Compliance score
- CM = Completeness score
- IQ = Inference/OCR Quality score

### Score Bands and Action

| Final Score | Grade | Action Required |
|---|---|---|
| 100 | S | Perfect. No changes needed. |
| 90-99 | A | Near-perfect. Minor tweaks only. |
| 80-89 | B | Good. Light revision needed. |
| 70-79 | C | Adequate. Moderate revision needed. |
| 60-69 | D | Poor. Major revision needed. |
| <60 | F | Failing. Re-translate from source. |

### Max-60 Cap Rule

If **any** critical error (from any dimension's zero-tolerance list) is detected, the **maximum possible final score is 60**, regardless of other dimension scores. Example:

| Dimension | Score | Weighted |
|---|---|---|
| Numerical Accuracy | 60 (critical: digit wrong) | 60 × 0.30 = 18.0 |
| Terminology Consistency | 100 | 100 × 0.20 = 20.0 |
| Semantic Fidelity | 100 | 100 × 0.25 = 25.0 |
| Format Compliance | 100 | 100 × 0.10 = 10.0 |
| Completeness | 100 | 100 × 0.10 = 10.0 |
| Inference/OCR | 100 | 100 × 0.05 = 5.0 |
| **Raw weighted total** | | **88.0** |
| **Capped final (critical error)** | | **60.0** |

---

## Quick Reference: Critical Error List

| # | Error Type | Applies To Dimension | Cap |
|---|---|---|---|
| 1 | Number/digit transposition or omission | Numerical Accuracy (30%) | Max 60 |
| 2 | Wrong year/month/day | Numerical Accuracy (30%) | Max 60 |
| 3 | Currency amount or unit wrong | Numerical Accuracy (30%) | Max 60 |
| 4 | Percentage value wrong | Numerical Accuracy (30%) | Max 60 |
| 5 | Company/brand name wrong | Terminology Consistency (20%) | Max 60 |
| 6 | Critical technical term reversed | Terminology Consistency (20%) | Max 60 |
| 7 | Meaning reversal (opposite of source) | Semantic Fidelity (25%) | Max 60 |
| 8 | Yes/No / negation inverted | Semantic Fidelity (25%) | Max 60 |
| 9 | Legal/medical/safety meaning error | Semantic Fidelity (25%) | Max 60 |
| 10 | Entire section/paragraph omitted | Completeness (10%) | Max 60 |
| 11 | Legal clause omitted | Completeness (10%) | Max 60 |
| 12 | Wrong restoration of OCR text | Inference/OCR (5%) | Max 60 |
| 13 | Wrong honorific level causing offense | Semantic Fidelity (25%) | Max 60 |
| 14 | Decimal comma not converted | Numerical Accuracy (30%) | Max 60 (systematic) |

---

## Scoring Rubric Template

```
Dimension 1: Numerical Accuracy (30%)
Score: ___ / 100
Issues found:
  - [critical?] ________________________________
  - [         ] ________________________________
  - [         ] ________________________________

Dimension 2: Terminology Consistency (20%)
Score: ___ / 100
Issues found:
  - [critical?] ________________________________
  - [         ] ________________________________
  - [         ] ________________________________

Dimension 3: Semantic Fidelity (25%)
Score: ___ / 100
Issues found:
  - [critical?] ________________________________
  - [         ] ________________________________
  - [         ] ________________________________

Dimension 4: Format Compliance (10%)
Score: ___ / 100
Issues found:
  - [         ] ________________________________
  - [         ] ________________________________

Dimension 5: Completeness (10%)
Score: ___ / 100
Issues found:
  - [critical?] ________________________________
  - [         ] ________________________________

Dimension 6: Inference/OCR Quality (5%)
Score: ___ / 100
Issues found:
  - [critical?] ________________________________
  - [         ] ________________________________

--- Weighted Calculation ---
NA (___ × 0.30) = ___
TC (___ × 0.20) = ___
SF (___ × 0.25) = ___
FC (___ × 0.10) = ___
CM (___ × 0.10) = ___
IQ (___ × 0.05) = ___
Raw total: ___
Critical error found? Y / N  -->  Cap applied? Y / N
FINAL SCORE: ___ / 100
```

---

## Appendix: KO-Specific Quality Indicators

### Positive Indicators (Signal of High Quality)

| Indicator | Description |
|---|---|
| Natural particle usage | 은/는, 이/가, 을/를 used naturally and correctly |
| Appropriate formality | 합쇼체/해요체/해체 correctly matched to document type |
| Idiomatic expressions | Korean idioms used in place of English literalism |
| 당신 avoidance | Pronoun dropped or replaced with title/name |
| Proper 외래어 표기 | Loanwords follow 국립국어원 standard |
| Consistent counters | 명, 개, 분, 권 used correctly |
| Active voice preference | Most passive constructions converted to active |

### Negative Indicators (Signal of Low Quality)

| Indicator | Description |
|---|---|
| 당신 overuse | "You" translated as 당신 more than once |
| Particle errors | Missing or wrong particles (은/는, 이/가 confusion) |
| SOV violation | Verb not at end of sentence |
| English sentence structure preserved | Literal word-order carryover |
| Wrong counter | Using 개 for people, 명 for objects, etc. |
| Mixing formality levels | Switching between 합쇼체 and 해요체 in same paragraph |
| Untranslated loanwords | English words left in Hangul without proper transcription |
| CJK punctuation | 。、」 still present |
| Range with hyphen | Using `-` instead of `~` for ranges |

---

> **References:** 국립국어원 (National Institute of Korean Language) -- 한글 맞춤법, 외래어 표기법, 표준 국어 대사전, 표준 언어 예절.
