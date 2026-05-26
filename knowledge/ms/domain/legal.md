---
id: ms/domain/legal
type: domain
target_lang: ms
name: Domain: Legal (Malay — MS)
description: Translation rules for legal documents into Malay
---

## Reader Model

**Who reads this document and what do they expect?**

Legal document readers in Malaysia are lawyers, judges, regulators, contract managers, and parties to an agreement. They read the document to determine rights, obligations, and legal consequences. They expect:

- **Ambiguity is liability** — every word may be scrutinized in litigation. Translators must preserve legal intent precisely and avoid introducing interpretive gaps.
- **Formal register throughout** — Malaysian legal Malay follows established conventions of syntax and vocabulary. Colloquial or informal phrasing undermines enforceability.
- **Preservation of legal structure** — recitals, operative clauses, definitions, signatures, and schedules each have distinct functions. Their structure must be maintained.
- **Consistent defined terms** — a defined term must be rendered identically every time it appears. Variation can inadvertently create new meanings.
- **Jurisdictional awareness** — Malaysia has a dual legal system (common law and Sharia). Concepts that exist in one system may have no direct equivalent in the other. The translator must bridge without misrepresenting.

**What would break their trust?**
- A mistranslated obligation that changes who bears risk or liability.
- An invented legal concept that has no basis in Malaysian law.
- An inconsistent defined term that creates ambiguity.
- An error in a date, reference number, or signature block that could invalidate a clause.

## Decision Framework

### 1. Obligation Language ("Shall" and Its Equivalents)

| Source Intent | Malay Decision |
|---|---|
| Binding obligation | Use ` hendaklah` — the subject is required to perform. |
| Prohibition | Use `tidak boleh` or `dilarang` — the subject is forbidden from performing. |
| Permission / discretion | Use `boleh` — the subject is permitted but not required. |
| Declaration / statement of fact | Use the indicative present tense — no modal verb needed. |
| Conditional obligation | Use `dengan syarat bahawa` or `bersyarat` to introduce condition. |

### 2. Common Law vs Sharia Concepts

| Condition | Decision |
|---|---|
| Concept has a direct equivalent in Malaysian common law | Use the common law term in Malay. It will be understood by the target reader. |
| Concept exists only in the source jurisdiction | Use a descriptive equivalent, not a false equivalent. Add an explanatory note on first occurrence. |
| Entity type has no Malaysian equivalent | Keep the original entity type abbreviation and add a description in parentheses on first mention. Do not substitute a different legal form. |
| Court or tribunal name is jurisdiction-specific | Keep the original name and add the English translation or description in parentheses on first mention. |
| Sharia law concept | Use the established Malay Sharia terminology: `hakam`, `kadi`, `mahkamah syariah`, `Undang-Undang Keluarga Islam`. |

### 3. Malaysian Court System Terminology

| English | Malay | Notes |
|---|---|---|
| Federal Court | Mahkamah Persekutuan | Highest court |
| Court of Appeal | Mahkamah Rayuan | Appellate court |
| High Court | Mahkamah Tinggi | Trial court |
| Sessions Court | Mahkamah Sesyen | Intermediate court |
| Magistrate Court | Mahkamah Majistret | Lower court |
| Sharia Court | Mahkamah Syariah | Islamic family/personal law |
| Industrial Court | Mahkamah Perusahaan | Employment disputes |
| Court of Judicature | Mahkamah Kehakiman | Historical term |
| Lord President | Ketua Hakim Negara | Historical title (pre-1994) |
| Chief Justice | Ketua Hakim Negara | Current title |
| Attorney General | Peguam Negara | Chief legal officer |
| Public Prosecutor | Pendakwa Raya | Criminal prosecution |

### 4. Contract Terminology

| English | Malay | Usage Notes |
|---|---|---|
| Party / Parties | Pihak | Always singular in Malay for both singular and plural |
| Hereinafter referred to | seterusnya dirujuk sebagai | Standard clause language |
| Whereas | Memandangkan | Recitals |
| Now therefore | Maka dengan ini | Operative clause opener |
| In witness whereof | Sebagai tanda bukti | Before signature block |
| Indemnify | Memberi pampasan / Menanggung kerugian | Context-dependent |
| Representations and warranties | Pernyataan dan jaminan | Standard contract section |
| Force majeure | Force majeure (kept in English) or Keadaan di luar kawalan | French term often preserved |
| Governing law | undang-undang yang mentadbir | Standard clause |
| Jurisdiction | bidang kuasa | Standard clause |
| Severability | boleh diasingkan | Standard clause |
| Entire agreement | perjanjian keseluruhan | Standard clause |
| Amendment | pindaan | Standard clause |
| Waiver | pelepasan / pengecualian | Context-dependent |

### 5. Statute and Regulation References

| Condition | Decision |
|---|---|
| Malaysian statute name | Use the official Malay title: `Kanun Prosedur Jenayah`, `Akta Kontrak 1950` |
| Section reference | ` Seksyen 3 Akta X` (not `Section 3`) |
| Article reference | `Perkara 3 Perlembagaan` (not `Article 3`) |
| Regulation reference | `Peraturan X` or `Kaedah-kaedah X` |
| Bill/proposed law | `Rang Undang-Undang X` |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Over-translating entity types** | Replacing a foreign legal entity abbreviation with a Malaysian equivalent changes the legal nature of the entity. Keep the original abbreviation and explain in parentheses on first use. |
| **Mis-translating obligation language** | Using `boleh` (may) where `hendaklah` (shall) is intended converts a binding obligation into a discretionary permission. This changes the legal effect entirely. |
| **Inconsistent defined terms** | A defined term that appears in two different forms creates two potential meanings. Every occurrence must be identical. |
| **Clause numbering changed** | Cross-references rely on exact clause numbers. Renumbering breaks the entire reference system. |
| **Wrong court name translation** | Using `Mahkamah` + wrong modifier creates a non-existent court. Verify against the Malaysian court hierarchy. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Register inconsistency** | Legal documents demand consistent formal register. Avoid mixing `hendaklah` with casual constructions like `kena` or `perlu`. |
| **Misplaced `adalah`** | The copula `adalah` is NOT used before verbs in Malay. `Adalah` only appears before nouns and noun phrases. |
| **Signature block formatting changed** | Preserve the exact layout of signature lines, date lines, and witness lines. Formatting is part of the legal validity. |
| **Incorrect `di-` passive usage** | The `di-` passive is correct in formal legal Malay, but ensure the agent is expressed with `oleh` when specified. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False equivalent across legal systems** | A term that appears equivalent may carry different legal consequences in different jurisdictions. Research the concept in Malaysian law. |
| **Missing explanatory note on first use of foreign concept** | When a term has no Malay equivalent, the first occurrence must include an explanation. Subsequent occurrences use the term alone. |
| **Singular versus plural in defined terms** | Malay `pihak` covers both singular and plural. Ensure the context makes clear whether one or multiple parties are referenced. |

## Domain-Specific Reference

### Signature Block Formatting (Malaysian Convention)

| Block Element | Malay Convention |
|---|---|
| Signatory name | Preserve original spelling; do not translate |
| Title / position | Translate to Malay title (e.g., "Peguam Cara", "Pengarah Urusan") |
| Signature line | `Tandatangan:` or a ruled line for signing |
| Date line | `Tarikh:` with DD/MM/YYYY format |
| Witness line | `Saksi:` with name and signature lines |
| Company representation | `Bagi pihak dan atas nama [Nama Syarikat]` |
| Seal / stamp area | Indicate with `(Cop)` or describe the stamp location |

### Number Format in Legal Documents

| Element | Convention |
|---|---|
| Monetary amounts | Write in words followed by numerals in parentheses: `lima puluh ribu Ringgit Malaysia (RM50,000.00)` |
| Percentages | Write in words and numerals: `lima peratus (5 %)` |
| Time periods | Write in words: `tiga puluh (30) hari` |
| Large numbers | Use standard grouping: `satu juta (1,000,000)` |

### Common Malaysian Legal Documentary Structure

| Section | Malay Title |
|---|---|
| Title / Preamble | Tajuk / Muka surat |
| Recitals (Whereas clauses) | Memandangkan |
| Definitions | Takrifan |
| Operative clauses | Perkara operasi |
| Representations and warranties | Pernyataan dan jaminan |
| Indemnification | Pampasan |
| Termination | Penamatan |
| Governing law and jurisdiction | Undang-undang yang mentadbir dan bidang kuasa |
| Signature block | Blok tandatangan |

### Malaysian Legal System Overview

| System | Jurisdiction | Governing Body |
|---|---|---|
| Common Law / Civil Courts | All Malaysians | Federal Court → Court of Appeal → High Court → Sessions Court → Magistrate Court |
| Sharia Courts | Muslims only | Federal Sharia Court (proposed) → State Sharia Courts |
| Industrial Court | Employment disputes | Mahkamah Perusahaan |
| Land Court | Land matters | Mahkamah Tanah |
| Family Court | Family matters | Mahkamah Keluarga |
