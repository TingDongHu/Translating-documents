---
id: ms/domain/financial
type: domain
target_lang: ms
name: Domain: Financial (Malay — MS)
description: Translation rules for financial documents into Malay
---

## Reader Model

**Who reads this document and what do they expect?**

Financial document readers in Malaysia are investors, auditors, regulators (Securities Commission, Bursa Malaysia), CFOs, accountants, and financial analysts. They read the document to assess financial health, compliance, and investment decisions. They expect:

- **Precision with numbers** — every figure must be exact and consistently formatted. A misplaced decimal or wrong currency symbol erodes trust immediately.
- **Regulatory compliance** — Malaysian financial documents must comply with Companies Act 2016, Malaysian Financial Reporting Standards (MFRS), and Bursa Malaysia Listing Requirements.
- **Consistent terminology** — financial terms have precise meanings. Inconsistent usage creates ambiguity that can mislead investors.
- **Formal register** — financial documents demand the highest register of formal Malay. Colloquial expressions have no place.
- **Standardized structure** — financial statements follow prescribed formats (statement of financial position, income statement, etc.).

**What would break their trust?**
- Incorrect number formatting that changes the value (e.g., `1.000` vs `1,000`).
- Mistranslated financial terms that alter the meaning of disclosures.
- Inconsistent currency formatting within a document.
- Misformatted dates that could affect financial period reporting.

## Decision Framework

### 1. Financial Statement Terminology

| English | Malay | Notes |
|---|---|---|
| Statement of Financial Position | Penyata Posisi Kewangan | Balance sheet equivalent |
| Income Statement | Penyata Pendapatan | Profit & loss |
| Statement of Cash Flows | Penyata Aliran Tunai | Cash flow statement |
| Statement of Changes in Equity | Penyata Perubahan Ekuiti | Equity changes |
| Notes to the Financial Statements | Nota kepada Penyata Kewangan | Accompanying notes |
| Auditor's Report | Laporan Audit | External auditor opinion |
| Board of Directors | Lembaga Pengarah | Board |
| Shareholders | Pemegang Saham | Equity holders |
| Revenue | Pendapatan | Total revenue |
| Net Profit | Untung Bersih / Keuntungan Bersih | After deductions |
| Gross Profit | Untung Kasar / Keuntungan Kasar | Before operating expenses |
| Total Assets | Jumlah Aset | Sum of all assets |
| Total Liabilities | Jumlah Liabiliti | Sum of all obligations |
| Shareholders' Equity | Ekuiti Pemegang Saham | Net assets |
| Current Assets | Aset Semasa | Due within 12 months |
| Non-current Assets | Aset Bukan Semasa | Due after 12 months |
| Current Liabilities | Liabiliti Semasa | Due within 12 months |
| Non-current Liabilities | Liabiliti Bukan Semasa | Due after 12 months |
| Earnings Per Share (EPS) | Keuntungan Seunit (KSU) | Per-share metric |
| Dividend | Dividen | Distribution to shareholders |
| Depreciation | Susut Nilai | Asset value reduction |
| Amortization | Pelunasan | Intangible asset reduction |
| Working Capital | Modal Kerja | Current assets minus current liabilities |

### 2. Ringgit and Currency Formatting

| Element | Convention |
|---|---|
| Malaysian Ringgit | `RM` placed before amount, no space: `RM1,000.00` |
| Thousand separator | Comma: `1,000,000` |
| Decimal separator | Dot: `0.00` |
| Decimal places | Two places for financial: `RM100.00` |
| Negative values | Parentheses in tables: `(RM500.00)` or minus sign in text: `-RM500.00` |
| Currency in text | `Ringgit Malaysia (RM)` on first mention, then `RM` |
| Foreign currency | Preserve original symbol: `$100.00`, `€50.00`, `¥10,000` |
| ISO code (formal) | `MYR 1,000.00` in international contexts |

### 3. Bursa Malaysia Terminology

| English | Malay | Notes |
|---|---|---|
| Bursa Malaysia | Bursa Malaysia (preserved) | Malaysian stock exchange |
| Securities Commission | Suruhanjaya Sekuriti | Market regulator |
| Listed company | Syarikat tersenarai | Publicly listed |
| Initial Public Offering (IPO) | Penawaran Awam Permulaan (PAP) | IPO in Malay |
| Annual General Meeting (AGM) | Mesyuarat Agung Tahunan (MAT) | Annual meeting |
| Extraordinary General Meeting (EGM) | Mesyuarat Agung Luar Biasa (MALB) | Special meeting |
| Quarterly report | Laporan suku tahunan | Quarterly disclosure |
| Annual report | Laporan tahunan | Annual disclosure |
| Market capitalization | Pemodelan pasaran / Nilai pasaran | Total market value |
| Stock code / ticker | Kod saham | Trading symbol |
| Trading volume | Volume dagangan | Shares traded |
| Share price | Harga saham | Market price |
| Dividend yield | Hasil dividen | Return metric |
| Price-to-Earnings (P/E) ratio | Nisbah harga untung | Valuation metric |

### 4. Banking and Monetary Terms

| English | Malay | Notes |
|---|---|---|
| Bank Negara Malaysia | Bank Negara Malaysia (preserved) | Central bank |
| Base lending rate | Kadar pinjaman asas | Lending benchmark |
| Overnight Policy Rate (OPR) | Kadar dasar semalaman | Monetary policy rate |
| Fixed deposit | Deposit tetap | Time deposit |
| Savings account | Akaun simpanan | Deposit account |
| Current account | Akaun semasa | Checking account |
| Loan | Pinjaman | Borrowing facility |
| Interest | Faedah / Bunga | Cost of borrowing |
| collateral | Cagaran | Security for loan |
| Non-performing loan | Pinjaman tidak berprestasi | Bad debt |
| Capital adequacy ratio | Nisbah kecukupan modal | Bank solvency metric |
| Liquidity ratio | Nisbah kecairan | Cash availability |

### 5. Audit and Accounting Terms

| English | Malay | Notes |
|---|---|---|
| Generally Accepted Accounting Principles (GAAP) | Prinsip Perakaunan Yang Diterima Umum | Accounting standards |
| Malaysian Financial Reporting Standards (MFRS) | Standard Pelaporan Kewangan Malaysia (SPKM) | Local standards |
| International Financial Reporting Standards (IFRS) | Standard Pelaporan Kewangan Antarabangsa | Global standards |
| Audit opinion | Pendapat audit | Auditor's conclusion |
| Material misstatement | Salah nyata material | Significant error |
| Going concern | Kelangsungan operasi | Business continuity assumption |
| Internal control | Kawalan dalaman | Governance mechanism |
| Risk management | Pengurusan risiko | Risk framework |
| Tax return | Borang cukai | Tax filing |
| Withholding tax | Cukai pendahuluan | Tax deducted at source |
| Goods and Services Tax (GST) | Cukai Barang dan Perkhidmatan (CBP) | Sales tax (replaced by SST) |
| Sales and Services Tax (SST) | Cukai Jualan dan Perkhidmatan (CJP) | Current consumption tax |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Swapped decimal and thousands separators** | Using `1.000` (one thousand) where `1,000` is intended, or `1,50` where `1.50` is intended. This changes the numeric value entirely. |
| **Wrong RM placement** | `100 RM` instead of `RM100` violates Malaysian convention and may confuse readers. |
| **Inconsistent currency formatting** | Mixing `RM1,000` and `RM1.000` in the same document is a fundamental error. |
| **Mistranslated financial statement line items** | Wrong terminology changes what the line item represents, misleading readers. |
| **Date format ambiguity** | `04/05/2026` is ambiguous. Use `04/05/2026` consistently or write `4 Mei 2026`. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Incorrect passive voice in financial text** | Financial Malay uses `di-` passive: `untung diperoleh` (profit is obtained), not `untung memperoleh`. |
| **Wrong thousand separator in tables** | Tables must use consistent comma separators: `1,000,000` not `1.000.000`. |
| **Missing RM symbol on financial figures** | Every monetary figure should have the `RM` symbol or be in a clearly labeled column. |
| **Mixed formal/informal register** | Financial documents must maintain Bahasa Baku throughout. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False friend terminology** | `Modal` in Malay can mean "capital" (accounting) or "capital" (general). Ensure the financial meaning is clear in context. |
| **Pluralization errors** | Malay does not typically pluralize financial terms: `aset` (not `aset-aset` unless for emphasis). |
| **Inconsistent date formats** | Some parts may use `DD/MM/YYYY` and others `YYYY-MM-DD`. Choose one and maintain consistency. |

## Domain-Specific Reference

### Financial Statement Format (Malaysian Standard)

| Statement | Key Line Items (Malay) |
|---|---|
| Penyata Posisi Kewangan | Aset, Liabiliti, Ekuiti |
| Penyata Pendapatan | Pendapatan, Kos Jualan, Untung Kasar, Perbelanjaan Operasi, Untung Bersih |
| Penyata Aliran Tunai | Aktiviti Operasi, Aktiviti Pelaburan, Aktiviti Pembiayaan |
| Nota kepada Penyata Kewangan | Dasar perakaunan, Butiran terperinci, Pengakuan |

### Regulatory Bodies

| Body | Malay Name | Role |
|---|---|---|
| Securities Commission Malaysia | Suruhanjaya Sekuriti Malaysia | Market regulation |
| Bursa Malaysia | Bursa Malaysia | Stock exchange operator |
| Bank Negara Malaysia | Bank Negara Malaysia | Central bank |
| Companies Commission of Malaysia | Suruhanjaya Syarikat Malaysia (SSM) | Company registration |
| Malaysian Accounting Standards Board | Lembaga Standard Perakaunan Malaysia | Accounting standards |
| Financial Reporting Foundation | Yayasan Pelaporan Kewangan | Oversight body |
