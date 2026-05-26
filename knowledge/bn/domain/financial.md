---
id: bn/domain/financial
type: domain
target_lang: bn
name: Domain: Financial (Bengali — BN)
description: Translation rules for financial documents into Bengali
---

## Reader Model

**Who reads this document and what do they expect?**

Financial document readers in Bengali are accountants, auditors, banking professionals, investors, regulators, and business owners. They read the document to assess financial health, compliance, and investment decisions. They expect:

- **Numerical precision** — every figure must be accurate and properly formatted. A misplaced decimal or wrong grouping undermines credibility.
- **Regulatory compliance** — financial terms must align with Bangladesh Bank regulations, Companies Act 1994, and IFRS/Bangladesh Accounting Standards (BAS).
- **Consistent terminology** — the same financial concept must use the same Bengali term throughout the document.
- **Formal register** — financial documents require professional language. Colloquial phrasing signals incompetence.
- **Standard format** — balance sheets, income statements, and cash flow statements follow established formats that must be preserved.

**What would break their trust?**
- A mistranslated financial term that changes the meaning (e.g., "assets" vs "liabilities").
- Inconsistent number formatting that makes comparison impossible.
- Wrong currency conversion or mixing of currency systems.
- Missing or altered financial statement line items.

## Decision Framework

### 1. Financial Statement Terms

| Source Term | Bengali Decision |
|---|---|
| Balance Sheet | ব্যালেন্স শীট / সম্পদ ও দায়ের তালিকা |
| Income Statement | আয়ের বিবরণ / লাভক্ষতির হিসাব |
| Cash Flow Statement | নগদ প্রবাহের বিবরণ |
| Profit and Loss | লাভ ও ক্ষতি |
| Shareholders' Equity | শেয়ারহোল্ডারদের ইকুইটি / শেয়ারহোল্ডারদের মালিকানা |
| Retained Earnings | সঞ্চিত লাভ |

### 2. Banking and Central Bank Terms

| Source Term | Bengali Decision |
|---|---|
| Bangladesh Bank | বাংলাদেশ ব্যাংক |
| Monetary Policy | আর্থিক নীতি |
| Interest Rate | সুদের হার |
| Exchange Rate | বিনিময় হার |
| Foreign Reserve | বৈদেশিক মুদ্রা সংরক্ষণ |
| Non-Performing Loan (NPL) | অসঞ্চালিত ঋণ |

### 3. Mobile Financial Services (Bangladesh-Specific)

| Source Term | Bengali Decision |
|---|---|
| bKash | বিকাশ (brand name — preserve as-is) |
| Nagad | নগদ (brand name — preserve as-is) |
| Mobile Financial Services (MFS) | মোবাইল আর্থিক সেবা |
| Agent Banking | এজেন্ট ব্যাংকিং |
| Mobile Wallet | মোবাইল ওয়ালেট |

### 4. Currency and Amount Formatting

| Condition | Decision |
|---|---|
| Bangladeshi Taka amounts | Use `৳` symbol before amount: `৳5,00,000` |
| Large amounts in Taka | Use Indian grouping: `৳1,00,000` (1 lakh), `৳1,00,00,000` (1 crore) |
| Foreign currency amounts | Use ISO code: `USD 50,000`, `EUR 25,000` |
| Percentage figures | Use `%` after number: `12.5%`, `7.5%` |
| Mixed currency in same document | Clearly label each: `৳5,00,000 (BDT)`, `USD 10,000` |

### 5. Financial Periods

| Source Term | Bengali Decision |
|---|---|
| Fiscal Year | অর্থবছর |
| Quarter | ত্রৈমাসিক |
| Half-yearly | আধা-বার্ষিক |
| Annual Report | বার্ষিক প্রতিবেদন |
| Audited Financial Statements | নিরীক্ষিত আর্থিক বিবরণ |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Swapping assets and liabilities** | Translating "assets" as "দায়" (liabilities) or vice versa fundamentally misrepresents financial position. |
| **Wrong number grouping** | Writing `100,000` instead of `1,00,000` in Bengali context can cause misreading of amounts. |
| **Currency symbol errors** | Mixing `৳` and `₹` for the wrong jurisdiction changes the value by approximately 1:1 but the legal entity is different. |
| **Omitted line items in financial statements** | Removing or merging line items alters the structure of the financial statement. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Inconsistent number formatting** | Choose one grouping style (Indian or Western) per document and maintain throughout. |
| **Translating brand names** | Preserve bKash, Nagad, and other financial service brand names. Do not translate them. |
| **Register inconsistency** | Financial documents must use formal register throughout. Do not mix colloquial and formal terms. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False friends in financial terminology** | "Credit" can mean different things in different contexts (banking credit, accounting credit). Ensure the Bengali term matches the specific meaning. |
| **Missing explanatory note on first use** | When introducing an IFRS/BAS term for the first time, include the English term in parentheses: `নগদ প্রবাহের বিবরণ (Cash Flow Statement)`. |
| **Date format in financial periods** | Ensure date formats are consistent and unambiguous throughout the document. |

## Domain-Specific Reference

### Bangladesh Financial Regulatory Bodies

| English | Bengali |
|---|---|
| Bangladesh Bank | বাংলাদেশ ব্যাংক |
| Bangladesh Securities and Exchange Commission | বাংলাদেশ সিকিউরিটিজ অ্যান্ড এক্সচেঞ্জ কমিশন |
| Bangladesh Financial Intelligence Unit | বাংলাদেশ আর্থিক গোয়েন্দা ইউনিট |
| Anti-Corruption Commission | দুর্নীতি দমন কমিশন |
| National Board of Revenue | জাতীয় রাজস্ব বোর্ড |

### Common Bengali Financial Terms

| English | Bengali |
|---|---|
| Asset | সম্পদ |
| Liability | দায় |
| Revenue | রাজস্ব |
| Expense | ব্যয় |
| Depreciation | হ্রাসমূল্য |
| Amortization | পরিশোধন |
| Gross Profit | মোট লাভ |
| Net Profit | নিট লাভ / পরিশোধিত লাভ |
| Dividend | লভ্যাংশ |
| Audit | নিরীক্ষা |
| Tax | কর |
| VAT | ভ্যাট / মূল্য সংযোজন কর |
| Inflation | মুদ্রাস্ফীতি |
| Deflation | মুদ্রাসংকোচন |
| GDP | জিডিপি / স্থূল অভ্যন্তরীণ উৎপাদন |
| FDI | বৈদেশিক প্রত্যক্ষ বিনিয়োগ |

### Financial Statement Format (Bangladesh)

| Element | Bengali Format |
|---|---|
| Company name | `[Company Name] লিমিটেড` |
| Statement title | `[বছর] সালের [মাস] পর্যন্ত আর্থিক বিবরণ` |
| Currency | `মুদ্রা: বাংলাদেশি টাকা (BDT)` |
| Comparative period | `[Previous year] সালের সংশ্লিষ্ট পর্যন্ত` |
| Auditor's opinion | `নিরীক্ষকের মতামত` |
| Notes to financial statements | `আর্থিক বিবরণের টীকা` |

### Number Format in Financial Documents

| Element | Convention |
|---|---|
| Small amounts | Use digits: `৳500`, `৳1,200` |
| Large amounts | Use Indian grouping: `৳5,00,000` (5 lakh), `৳1,00,00,000` (1 crore) |
| Percentages | `%` after number: `12.5%`, `7.5%` |
| Ratios | Use colon: `2:1`, `1.5:1` |
| Foreign currency | ISO code: `USD 50,000`, `EUR 25,000` |

### Accounting Equation in Bengali

| English | Bengali |
|---|---|
| Assets = Liabilities + Equity | সম্পদ = দায় + মালিকানা |
| Revenue - Expenses = Profit | রাজস্ব - ব্যয় = লাভ |
