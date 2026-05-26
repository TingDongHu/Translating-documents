---
id: bn/domain/legal
type: domain
target_lang: bn
name: Legal Documents (Bengali — BN)
description: Translation rules for legal and official documents into Bengali
---

## Reader Model

**Who reads this document and what do they expect?**

Legal document readers in Bangladesh and West Bengal are lawyers, judges, regulators, contract managers, and parties to an agreement. They read the document to determine rights, obligations, and legal consequences. They expect:

- **Ambiguity is liability** — every word may be scrutinized in litigation. Translators must preserve legal intent precisely and avoid introducing interpretive gaps.
- **Formal register throughout** — Bengali legal language follows established conventions of syntax and vocabulary. Colloquial or informal phrasing undermines enforceability.
- **Preservation of legal structure** — recitals, operative clauses, definitions, signatures, and schedules each have distinct functions. Their structure must be maintained.
- **Consistent defined terms** — a defined term must be rendered identically every time it appears. Variation can inadvertently create new meanings.
- **Jurisdictional awareness** — concepts that exist in one legal system (e.g., Indian Evidence Act, Bangladesh Penal Code) may have no direct equivalent in another. The translator must bridge without misrepresenting.

**What would break their trust?**
- A mistranslated obligation that changes who bears risk or liability.
- An invented legal concept that has no basis in the target jurisdiction.
- An inconsistent defined term that creates ambiguity.
- An error in a date, reference number, or signature block that could invalidate a clause.

## Decision Framework

### 1. Obligation Language

| Source Intent | Bengali Decision |
|---|---|
| Binding obligation | Use `করতে হবে` or `করণীয়` — the subject is required to perform. |
| Prohibition | Use `করা যাবে না` or `নিষিদ্ধ` — the subject is forbidden. |
| Permission / discretion | Use `করতে পারেন` or `করার অধিকার আছে` — permitted but not required. |
| Declaration / statement of fact | Use indicative present tense — no modal equivalent needed. |
| Conditional obligation | Use `শর্তানুসারে` or `এর অধীনে` to introduce conditions. |

### 2. Bangladesh vs India Legal Concepts

| Condition | Decision |
|---|---|
| Concept has a direct equivalent in Bengali legal usage | Use the established Bengali legal term. |
| Concept exists only in the source jurisdiction | Use a descriptive equivalent, not a false equivalent. Add an explanatory note on first occurrence. |
| Entity type has no Bengali equivalent | Keep the original entity type and add a description in parentheses on first mention. Do not substitute a different legal form. |
| Court or tribunal name is jurisdiction-specific | Keep the original name and add the Bengali translation or description in parentheses on first mention. |

### 3. Recitals, Operative Clauses, and Signature Blocks

| Document Section | Decision |
|---|---|
| Recitals (যেহেতু clauses) | Use `যেহেতু` for each recital paragraph. Maintain the preamble structure. |
| Operative clauses | Use `ধারা` (clause) or `অনুচ্ছেদ` (section) numbering consistent with the source. |
| Signature block | Preserve the layout. Translate signatory titles. Keep personal names in original form. |
| Date in signature block | Use unambiguous format: "day month year" (e.g., "২৭ মে ২০২৬"). |

### 4. "And/Or" Constructions

| Condition | Decision |
|---|---|
| Source uses three-element pattern (A, B, and/or C) | Preserve the "এবং/অথবা" construction. It has accepted meaning in Bengali legal usage. |
| Source uses only "or" where both alternatives and cumulative application are possible | Evaluate context. If both are intended, use "এবং/অথবা". If only alternatives, use "অথবা" alone. |

### 5. Date Format in Contracts

| Condition | Decision |
|---|---|
| Date expressed numerically | Convert to text format: "২৭ মে ২০২৬" to eliminate ambiguity. |
| Date includes time reference | Preserve the time exactly. Use the format consistent with the rest of the document. |
| Date range for a term or period | Use "তারিখ থেকে [date] পর্যন্ত" or "[number] [unit] সময়ের জন্য". |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Over-translating entity types** | Replacing a foreign legal entity abbreviation with a domestic equivalent changes the legal nature of the entity. Keep the original abbreviation and explain in parentheses on first use. |
| **Mis-handling "and/or"** | Dropping the "/" changes the logical scope. If both alternatives and cumulative application are intended, "এবং/অথবা" must be preserved. |
| **Date format ambiguity** | "04/05/2026" is ambiguous. In legal documents, use text format: "৪ মে ২০২৬". |
| **Defined term inconsistency** | A defined term that appears in two different forms creates two potential meanings. Every occurrence must be identical. |
| **Clause numbering changed** | Cross-references rely on exact clause numbers. Renumbering breaks the entire reference system. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Register inconsistency** | Legal documents demand consistent formal register. Avoid mixing formal and informal constructions. |
| **Misplaced "শর্তানুসারে"** | "শর্তানুসারে" (subject to) subordinates the clause it introduces to another provision. Place it correctly at the beginning of the subordinated clause. |
| **Signature block formatting changed** | Preserve the exact layout of signature lines, date lines, and witness lines. Formatting is part of the legal validity. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False equivalent across legal systems** | A term that appears equivalent may carry different legal consequences in Bangladesh vs India. Research the concept in the target legal system. |
| **Missing explanatory note on first use of foreign concept** | When a term has no Bengali equivalent, the first occurrence must include an explanation. Subsequent occurrences use the term alone. |
| **Singular versus plural in defined terms** | Bengali defined terms should match the number (singular/plural) used in the source. Changing number may inadvertently narrow or expand the definition. |

## Domain-Specific Reference

### Bangladesh Court Hierarchy

| Court | Bengali |
|---|---|
| Supreme Court of Bangladesh | বাংলাদেশ সুপ্রিম কোর্ট |
| High Court Division | হাইকোর্ট বিভাগ |
| Appellate Division | আপিল বিভাগ |
| District Court | জেলা আদালত |
| Metropolitan Magistrate Court | মহানগর ম্যাজিস্ট্রেট আদালত |

### Indian Court Hierarchy (for West Bengal context)

| Court | Bengali |
|---|---|
| Supreme Court of India | ভারতের সুপ্রিম কোর্ট |
| Calcutta High Court | কলকাতা হাইকোর্ট |
| District Court | জেলা আদালত |

### Signature Block Formatting

| Block Element | Bengali Convention |
|---|---|
| Signatory name | Preserve original spelling; do not translate |
| Title / position | Translate to Bengali title (e.g., "আইনি প্রতিনিধি", "ব্যবস্থাপনা পরিচালক") |
| Signature line | `স্বাক্ষর:` or a ruled line for signing |
| Date line | `তারিখ:` with day-month-year format |
| Witness line | `সাক্ষী:` with name and signature lines |
| Company representation | `[Company Name] এর পক্ষ থেকে` |
| Seal / stamp area | Indicate with `(সীল)` or describe the stamp location |

### Common Legal Terms (English–Bengali)

| English | Bengali |
|---|---|
| Contract | চুক্তি / চুক্তিপত্র |
| Agreement | চুক্তি / সমঝোতা |
| Clause | ধারা |
| Section | অনুচ্ছেদ |
| Plaintiff | বাদী |
| Defendant | বিবাদী |
| Witness | সাক্ষী |
| Evidence | প্রমাণ |
| Verdict | রায় |
| Appeal | আপিল |
| Injunction | নিষেধাজ্ঞা |
| Liability | দায়বদ্ধতা |
| Indemnity | ক্ষতিপূরণ |
| Arbitration | গ্রামীণ বিচার / নির্দিষ্টকরণ |
| Jurisdiction | এখতিয়ার |

### Number Format in Legal Documents

| Element | Convention |
|---|---|
| Monetary amounts | Write in words followed by numerals in parentheses: `পাঁচ লাখ টাকা (৳5,00,000)` |
| Percentages | Write in words and numerals: `পাঁচ শতাংশ (5%)` |
| Time periods | Write in words: `ত্রিশ (৩০) দিন` |
| Large numbers | Use Indian grouping: `এক লাখ (১,০০,০০০)` |

### Common Legal Documentary Structure

| Section | Purpose |
|---|---|
| Title / Preamble (শিরোনাম) | Identifies the document type and parties |
| Recitals (যেহেতু clauses) | Background facts and intent |
| Definitions (সংজ্ঞা) | Terms with specific meanings assigned |
| Operative clauses (কার্যকর ধারা) | Rights, duties, conditions, and obligations |
| Representations and warranties | Statements of fact that the parties assert |
| Indemnification (ক্ষতিপূরণ) | Allocation of loss and liability |
| Termination (চুক্তি বিলোপ) | Conditions under which the agreement ends |
| Governing law and jurisdiction | Which law applies and where disputes are heard |
| Signature block (স্বাক্ষর ব্লক) | Execution by authorized representatives |
