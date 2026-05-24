---
id: en/domain/financial
type: domain
target_lang: en
name: Financial Documents
description: Translation rules for financial and accounting documents into English
---

## Reader Model

**Who reads this document and what do they expect?**

Financial document readers are auditors, accountants, tax authorities, investors, and financial analysts who rely on the document for reporting, compliance, and decision-making. They expect:

- **Precision in every figure** — financial statements are legally attestable documents. A single digit error can misrepresent the financial position of an organization.
- **Consistent application of accounting standards** — terminology must align with GAAP, IFRS, or other applicable standards. Readers expect terms they can map to standard accounting concepts.
- **Unambiguous numerical formatting** — decimals, thousands separators, and currency indicators must follow target-market conventions without altering values.
- **Audit-ready structure** — tables, footnotes, cross-references, and supporting schedules must be preserved so that every figure can be traced and verified.

**What would break their trust?**
- A numerical value that differs from the source — even by a rounding error — invalidates the document.
- A currency symbol that suggests a different currency than intended.
- An incorrectly labeled financial statement line item that misleads analysis.
- A date range that does not align with the reporting period.

## Decision Framework

### 1. Numerical Formatting

| Source Format | English Convention Decision |
|---|---|
| Comma as decimal separator (e.g., 100,00) | Convert to dot: 100.00 |
| Dot as thousands separator (e.g., 1.234) | Convert to comma: 1,234 |
| Space as thousands separator (e.g., 1 234) | Convert to comma: 1,234 |
| No thousands separator (e.g., 1234567) | Add commas: 1,234,567 |
| Percentage with comma decimal (e.g., 15,5%) | Convert to dot decimal: 15.5% |

### 2. Currency Handling

| Condition | Decision |
|---|---|
| Currency code appears (e.g., USD, EUR) | Preserve the three-letter ISO code exactly. |
| Currency symbol appears (e.g., $, EUR) | Keep the symbol if it is unambiguous for the source market. For formal documents, consider adding the ISO code in parentheses on first use. |
| Source expresses value in a non-English currency | Preserve the original currency and value. Do NOT convert to a different currency unless explicitly instructed by the client. |
| Source includes a financial total in words + numerals | Preserve both forms. Ensure they match. |
| Exchange rate appears in the document | Preserve the rate exactly. Translate the labels (e.g., "buying rate", "selling rate"). |

### 3. Financial Statement Terminology

| Condition | Decision |
|---|---|
| Standard IFRS/GAAP concept | Use the standard English term as defined by the applicable accounting framework. |
| Source uses a non-standard label | Use the standard English equivalent for the line item. Add a translator's note if the source term differs materially. |
| Subtotal or total line | Preserve the hierarchical structure. Translate labels consistently (e.g., "Subtotal", "Total", "Grand Total"). |

### 4. Date Ranges and Reporting Periods

| Condition | Decision |
|---|---|
| Single date | Use unambiguous format: "31 December 2025" or "2025-12-31". |
| Date range for a reporting period | Use "for the year ended 31 December 2025" or "for the period from 1 January 2025 to 31 December 2025". |
| Fiscal year reference | Use "FY2025" or "fiscal year 2025" consistently. |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Numerical value altered** | Any change to a digit — even rounding — misstates the financial position. |
| **Decimal/comma separator incorrectly converted** | Changing 1.500 (one thousand five hundred) to 1.50 (one point five zero) changes the value by a factor of 1,000. |
| **Currency code or symbol changed** | Mistaking USD for CAD or EUR changes the financial magnitude. |
| **Currency conversion performed without authorization** | Converting the value to a different currency introduces exchange rate risk and breaks the audit trail. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Locale-specific number format not fully converted** | Every number in the document must be checked. Mixed formats (dot in one table, comma in another) create confusion. |
| **Currency symbol ambiguous** | "$" could be USD, CAD, AUD, or others. In formal documents, use ISO codes or disambiguate: "USD 1,000". |
| **Date range format inconsistent** | Mixing "2025/01/01 - 2025/12/31" with "1 Jan to 31 Dec 2025" in the same document is unprofessional and risks misinterpretation. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **Negative value formatting** | Some locales use parentheses for negatives (e.g., (100.00)), others use a minus sign. Preserve the source convention unless the style guide specifies otherwise. |
| **Rounding notation** | "Rounded to nearest thousand" or figures in "USD 000s" must be explicitly stated and preserved. |
| **Zero versus dash in empty cells** | A dash ("--") means "not applicable" in financial tables; "0.00" means zero. These are not interchangeable. |
| **Footnote reference numbers** | Footnote markers that tie to numerical disclosures must be preserved exactly. |

## Domain-Specific Reference

### Standard Financial Table Structure

| Element | Preservation Rule |
|---|---|
| Column headers | Translate exactly; maintain alignment (left/right/center) |
| Row labels | Use standard English financial terminology |
| Subtotal rows | Preserve indentation and bold formatting |
| Total rows | Preserve underlines, double underlines, and bold formatting |
| Currency column | Indicate currency at top of column or per row |
| Notes references | Preserve superscript numbers or symbols |

### Decimal Precision Rules

| Context | Decimal Places | Example |
|---|---|---|
| General financial figures | 2 | 1,234.56 |
| Unit prices / per-share values | 4 or as in source | 12.3456 |
| Exchange rates | 4 or as in source | 1.2345 |
| Percentages | 2 | 15.25% |
| Tax rates | As in source | 10.00% |

### ISO Currency Codes (Common)

| Code | Currency | Symbol |
|---|---|---|
| USD | United States Dollar | $ |
| EUR | Euro | EUR |
| GBP | Pound Sterling | GBP |
| JPY | Japanese Yen | JPY |
| CNY | Chinese Yuan Renminbi | CNY |
| CHF | Swiss Franc | CHF |
| CAD | Canadian Dollar | CAD |
| AUD | Australian Dollar | AUD |
| HKD | Hong Kong Dollar | HKD |
| SGD | Singapore Dollar | SGD |

### Common Financial Statement Line Items

| Source Concept | English Equivalent |
|---|---|
| Balance Sheet | Balance Sheet |
| Income Statement / Profit and Loss | Income Statement / Profit and Loss Account |
| Revenue / Turnover | Revenue / Turnover |
| Cost of Goods Sold | Cost of Goods Sold |
| Gross Profit | Gross Profit |
| Operating Expenses | Operating Expenses |
| Net Income / Net Profit | Net Income / Net Profit |
| Cash Flow | Cash Flow |
| Fixed Assets | Fixed Assets |
| Depreciation | Depreciation |
| Accounts Receivable | Accounts Receivable |
| Accounts Payable | Accounts Payable |
| Share Capital | Share Capital |
| Retained Earnings | Retained Earnings |
| Reserves | Reserves |
| Value Added Tax | VAT (Value Added Tax) |
