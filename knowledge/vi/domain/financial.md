---
id: vi/domain/financial
type: domain
target_lang: vi
name: Tai lieu Tai chinh - Ke toan (Bao cao Tai chinh, Thue, So sach)
description: Quy tac dich thuat cho tai lieu tai chinh, bao cao ke toan, bao cao thue va bao cao kiem toan sang tieng Viet
---

## Reader Model

**Who reads this document and what do they expect?**

Financial document readers in the Vietnamese market are auditors (kiem toan vien), accountants (ke toan vien), tax authorities (Co quan Thue), financial analysts, investment managers, and regulatory bodies (Uy ban Chung khoan Nha nuoc). They rely on the document for statutory reporting, tax compliance, investment analysis, and audit verification. They expect:

- **Absolute numerical precision** — financial statements in Vietnam are submitted to Co quan Thue and Co quan Dang ky Kinh doanh. Every digit must match the source exactly. An incorrect value can lead to tax reassessment, penalties, or audit qualifications.
- **Vietnamese Accounting Standards (VAS) terminology** — Vietnam has its own set of accounting standards (Chuan muc Ke toan Viet Nam - VAS), which are based on IFRS but with significant local adaptations. Terminology must follow VAS, not IFRS terminology directly, unless the document explicitly follows IFRS (which some Vietnamese consolidated reports now do).
- **Proper numerical formatting for VND** — Vietnamese financial documents use the dot as thousands separator (1.000.000) and the comma as decimal separator (1.000.000,50). The currency indicator "d" or "VND" follows the amount. Mixing up separators is a critical error.
- **He thong Tai khoan Ke toan (Account System) awareness** — Vietnam has a mandatory chart of accounts (He thong Tai khoan Ke toan Viet Nam) prescribed by Bo Tai chinh. Account numbers (e.g., TK 111 for cash, TK 131 for receivables, TK 331 for payables) follow a standardized numbering system.
- **Tax law compliance context** — Vietnamese financial documents are closely tied to tax reporting. Terms must reflect the current Luat Thue (Tax Law) and its implementing Nghi dinh and Thong tu. Key taxes: Thue TNDN (Corporate Income Tax), Thue GTGT (VAT), Thue TNCN (Personal Income Tax), Thue Nha thau (Foreign Contractor Tax).

**What would break their trust?**
- A numerical error that changes a reported financial figure, misrepresenting the entity's financial position.
- An incorrectly converted decimal/thousands separator that changes the value by a factor of 1,000.
- Using IFRS terminology instead of VAS terminology, making the document non-compliant with Vietnamese reporting requirements.
- An incorrect tax code reference or tax rate that could lead to a tax filing error.
- A mistranslated financial statement line item that maps to the wrong account code.

## Decision Framework

### 1. Numerical Formatting for Vietnamese Financial Documents

| Source Format | Vietnamese Convention Decision | Notes |
|---|---|---|
| Dot as decimal separator (e.g., 100.00) | Convert to comma: 100,00 | Vietnam uses comma as decimal separator |
| Comma as thousands separator (e.g., 1,234) | Convert to dot: 1.234 | Vietnam uses dot as thousands separator |
| Space as thousands separator (e.g., 1 234) | Convert to dot: 1.234 | Remove space, use dot |
| No thousands separator (1234567) | Add dots: 1.234.567 | Vietnamese thousands grouping |
| VND amount with "d" or "VND" | Format: 1.000.000d or 1.000.000 VND | The symbol "d" follows the amount without space |
| Amount in thousands (VND 000s) | "Don vi tinh: 1.000 VND" | Standard notation in financial statements |
| Negative value in parentheses | Preserve parentheses: (1.000.000) | Vietnamese financial reports use parentheses for negatives |
| Percentage with dot decimal (15.5%) | Convert to comma decimal: 15,5% | Vietnamese convention for percentages |
| USD or foreign currency in VND report | Preserve foreign currency amount AND add VND equivalent in parentheses or adjacent column | Vietnamese financial statements of foreign entities require dual reporting |

### 2. Financial Statement Terminology (VAS vs IFRS)

| Source (IFRS/English) | Vietnamese (VAS) Equivalent | Notes |
|---|---|---|
| Balance Sheet | Bang Can doi Ke toan (BCKTD) | Or "Bang can doi ke toan" — standard term |
| Income Statement | Bao cao Ket qua Hoat dong Kinh doanh (BCKQHDKD) | Standard VAS term |
| Cash Flow Statement | Bao cao Luu chuyen Tien te (BCLCTT) | Standard VAS term |
| Statement of Changes in Equity | Thuyet minh Bien dong Von Chu so huu | Or included in notes |
| Notes to Financial Statements | Ban Thuyet minh Bao cao Tai chinh (BCTC) | Essential component of VAS financial statements |
| Revenue / Turnover | Doanh thu ban hang va cung cap dich vu | Separate from "Doanh thu hoat dong tai chinh" (financial income) |
| Cost of Goods Sold | Gia von hang ban (GVHB) | Standard VAS term |
| Gross Profit | Loi nhuan gop | Standard VAS term |
| Selling Expenses | Chi phi ban hang (CPBH) | Standard VAS account classification |
| Administrative Expenses | Chi phi quan ly doanh nghiep (CPQLDN) | Standard VAS account classification |
| Operating Profit | Loi nhuan thuan tu hoat dong kinh doanh | VAS format |
| Financial Income | Doanh thu hoat dong tai chinh (DTTC) | Includes interest, dividends, FX gains |
| Financial Expenses | Chi phi tai chinh (CPTC) | Includes interest expense, FX losses |
| Other Income | Thu nhap khac | Non-operating income |
| Other Expenses | Chi phi khac | Non-operating expenses |
| Net Profit | Loi nhuan sau thue (LNST) | Net profit after tax |
| Retained Earnings | Loi nhuan sau thue chua phan phoi | Undistributed profit |
| Fixed Assets | Tai san co dinh (TSCD) | Tangible + Intangible |
| Intangible Assets | Tai san co dinh vo hinh | Standard VAS classification |
| Accounts Receivable | Cac khoan phai thu (KPT) | Short-term: "Phai thu ngan han" |
| Accounts Payable | Cac khoan phai tra (KPT) | Short-term: "Phai tra ngan han" |
| Inventory | Hang ton kho (HTK) | Standard VAS valuation |
| Prepaid Expenses | Chi phi tra truoc | Short-term and long-term classified |
| Share Capital | Von dau tu cua Chu so huu / Von dieu le | "Von dieu le" for charter capital |
| Undistributed Profit | Loi nhuan sau thue chua phan phoi | VAS term |
| Reserves | Cac quy | "Quy dau tu phat trien", "Quy khen thuong, phuc loi" |

### 3. Vietnamese Account Classification (He thong Tai khoan Ke toan)

| Account Range | Classification | Key Accounts |
|---|---|---|
| 111 - 112 | Cash and bank deposits | TM (111 - Tien mat), TG (112 - Tien gui ngan hang) |
| 131 | Accounts receivable - customers | Phai thu khach hang |
| 133 | Input VAT | Thue GTGT duoc khau tru |
| 138 | Other receivables | Phai thu khac |
| 141 | Advances | Tam ung |
| 151 | Goods in transit | Hang mua dang di duong |
| 152 - 156 | Inventory | Nguyen vat lieu (152), Cong cu dung cu (153), Hang hoa (156) |
| 211 | Fixed assets - tangible | Tai san co dinh huu hinh |
| 213 | Fixed assets - intangible | Tai san co dinh vo hinh |
| 214 | Accumulated depreciation | Hao mon luy ke TSCD |
| 241 | Construction in progress | Xay dung co ban do dang |
| 242 | Prepaid expenses | Chi phi tra truoc |
| 311 - 315 | Short-term payables | Phai tra nguoi ban (331), Thue (333), Phai tra CNV (334) |
| 341 | Loans and borrowings | Vay va no thue tai chinh |
| 411 | Share capital | Von dau tu cua chu so huu |
| 421 | Retained earnings | Loi nhuan sau thue chua phan phoi |
| 511 | Revenue | Doanh thu ban hang va cung cap dich vu |
| 515 | Financial income | Doanh thu hoat dong tai chinh |
| 621 | Raw material costs | Chi phi nguyen vat lieu truc tiep |
| 622 | Labor costs | Chi phi nhan cong truc tiep |
| 627 | Manufacturing overhead | Chi phi san xuat chung |
| 632 | Cost of goods sold | Gia von hang ban |
| 635 | Financial expenses | Chi phi tai chinh |
| 641 | Selling expenses | Chi phi ban hang |
| 642 | Administrative expenses | Chi phi quan ly doanh nghiep |
| 711 | Other income | Thu nhap khac |
| 811 | Other expenses | Chi phi khac |
| 821 | Corporate income tax expense | Chi phi thue thu nhap doanh nghiep |
| 911 | Profit and loss determination | Xac dinh ket qua kinh doanh |

### 4. Tax Terminology (Thue Viet Nam)

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Corporate Income Tax (CIT) | Thue Thu nhap Doanh nghiep (Thue TNDN) | Standard rate: 20% (certain sectors differ) |
| Value Added Tax (VAT) | Thue Gia tri Gia tang (Thue GTGT) | Standard rate: 10%; reduced: 5%, 8% |
| Personal Income Tax (PIT) | Thue Thu nhap Ca nhan (Thue TNCN) | Progressive rates from 5% to 35% |
| Foreign Contractor Tax (FCT) | Thue Nha thau (FCT) | Applicable to foreign contractors doing business in Vietnam |
| Import Duty | Thue Xuat khau, Thue Nhap khau | "Thue nhap khau" for import duties |
| Special Consumption Tax | Thue Tieu thu Dac biet (Thue TTDB) | On alcohol, tobacco, luxury goods |
| Natural Resources Tax | Thue Tai nguyen | On mining, natural resource extraction |
| Environmental Protection Tax | Thue Bao ve Moi truong | On fuel, plastic, certain chemicals |
| License Fee | Le phi Mon bai / Le phi kinh doanh | Annual business fee |
| Land Tax | Thue Su dung Dat / Tien thue dat | "Tien thue dat" for land lease payments |
| Taxable income | Thu nhap chiu thue | Income subject to CIT |
| Deductible expenses | Chi phi duoc tru / Chi phi hop ly | Expenses deductible for CIT |
| Non-deductible expenses | Chi phi khong duoc tru | Expenses not deductible |
| Tax loss | Lo tinh thue | Loss carried forward (up to 5 years under Vietnamese law) |
| Tax period | Ky tinh thue / Ky quyet toan thue | Calendar year or fiscal year |
| Tax declaration | To khai thue / To khai quyet toan thue | "Quyet toan thue nam" for annual finalization |
| Tax refund | Hoan thue | VAT refund or CIT refund |
| Tax audit | Kiem tra thue / Thanh tra thue | "Thanh tra" is more formal/invasive |
| Transfer pricing | Gia giao dich lien ket (Gia chuyen nhuong) | Heavily scrutinized by Vietnamese tax authorities |
| Thin capitalization | Ty le von vay tren von chu so huu | Controlled transaction rules |

### 5. Vietnamese Financial Statement Structure (VAS Format)

| Line Item (Vietnamese) | English Equivalent | Notes |
|---|---|---|
| **Bang Can doi Ke toan (Mau B 01-DN)** | Balance Sheet | VAS mandatory format |
| Tai san | ASSETS | Divided into A and B sections |
| Tai san ngan han | Current Assets | Section A |
| Tien va tuong duong tien | Cash and Cash Equivalents | Code 110 |
| Cac khoan phai thu | Accounts Receivable | Code 130 |
| Hang ton kho | Inventory | Code 140 |
| Tai san dai han | Long-term / Non-current Assets | Section B |
| Tai san co dinh | Fixed Assets | Code 220 |
| **Nguon von** | EQUITY AND LIABILITIES | |
| No phai tra | Liabilities | Section C |
| No ngan han | Current Liabilities | Code 310 |
| No dai han | Long-term Liabilities | Code 320 |
| Von chu so huu | Equity | Section D |
| **Bao cao Ket qua Hoat dong Kinh doanh (Mau B 02-DN)** | Income Statement | VAS mandatory format |
| Doanh thu ban hang | Revenue | Code 01 |
| Cac khoan giam tru doanh thu | Revenue deductions | Code 02 |
| Doanh thu thuan | Net Revenue | Code 10 |
| Gia von hang ban | Cost of Goods Sold | Code 11 |
| Loi nhuan gop | Gross Profit | Code 20 |
| Doanh thu hoat dong tai chinh | Financial Income | Code 21 |
| Chi phi tai chinh | Financial Expenses | Code 23 |
| Chi phi ban hang | Selling Expenses | Code 25 |
| Chi phi quan ly doanh nghiep | Administrative Expenses | Code 26 |
| Loi nhuan thuan tu HDKD | Operating Profit | Code 30 |
| Thu nhap khac | Other Income | Code 31 |
| Chi phi khac | Other Expenses | Code 32 |
| Loi nhuan truoc thue | Profit Before Tax | Code 50 |
| Chi phi thue TNDN | CIT Expense | Code 51 |
| Loi nhuan sau thue | Net Profit After Tax | Code 60 |

### 6. Audit Terminology (Kiem toan)

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Audit | Kiem toan | "Kiem toan doc lap" for external audit |
| Auditor | Kiem toan vien | "Kiem toan vien hanh nghe" for certified auditor |
| Audit firm | Cong ty Kiem toan | E.g., "Cong ty TNHH Kiem toan Ernst & Young Viet Nam" |
| Audit report | Bao cao Kiem toan | Standard deliverable |
| Audit opinion | Y kien Kiem toan | Types below |
| Unqualified opinion | Y kien chap thuan toan phan | "Clean" opinion |
| Qualified opinion | Y kien chap thuan tung phan | With exceptions |
| Adverse opinion | Y kien trai nguoc | Material misstatement |
| Disclaimer of opinion | Tu choi dua ra y kien | Scope limitation |
| Going concern | Hoat dong lien tuc | VAS 21 / VSA 570 |
| Materiality | Trong yeu | Key audit concept |
| Internal control | Kiem soat noi bo (KSNB) | VAS 610 |
| Audit evidence | Bang chung kiem toan | VAS 500 series |
| Working papers | Ho so kiem toan | Auditor's documentation |
| Audit procedure | Thu tuc kiem toan | Substantive and compliance procedures |
| Sampling | Lay mau kiem toan | Statistical or judgmental selection |
| Subsequent events | Su kien phat sinh sau ngay khoa so ke toan | VAS 560 |
| Related party | Ben lien quan | Disclosure requirements under VAS 26 |
| Statutory audit | Kiem toan bao cao tai chinh | Annual requirement for certain companies |

### 7. Banking and Treasury Terminology

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Bank account | Tai khoan ngan hang (TKNH) | "Tai khoan thanh toan" for current account |
| Deposit account | Tai khoan tien gui | "Tien gui co ky han" for time deposit |
| Loan agreement | Hop dong tin dung / Hop dong vay | "Khoan vay" for a specific loan facility |
| Overdraft | Thau chi / Ghi No | Overdraft facility |
| Interest rate | Lai suat | "Lai suat cho vay" (lending) vs "Lai suat huy dong" (deposit) |
| Principal | Goc / So tien goc | "Tra goc" for principal repayment |
| Maturity date | Ngay dao han | "Dao han" for maturity |
| Collateral | Tai san bao dam / Tai san the chap | "The chap" for mortgage; "Cam co" for pledge |
| Guarantee | Bao lanh | "Bao lanh thanh toan" for payment guarantee |
| Letter of credit | Thu tin dung (L/C) | "L/C tra ngay" (sight) vs "L/C tra cham" (usance) |
| Loan covenant | Dieu kien giai ngan / Dieu kien tin dung | Conditions attached to a loan agreement |
| Non-performing loan | No xau (NPL) | "No duoi tieu chuan" for substandard debt |
| Foreign exchange | Ngoai te / Hoi doai | "Ty gia hoi doai" for exchange rate |
| Remittance | Chuyen tien / Kien hoi | "Kien hoi" for formal remittance |
| SWIFT | SWIFT / Ma SWIFT | Used universally in Vietnamese banking |
| IBAN | Not used in Vietnam | Vietnam uses account number + bank code |

### 8. Financial Analysis and Ratio Terminology

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Financial ratio | Chi so tai chinh / He so tai chinh | "He so" is more formal |
| Liquidity ratio | He so thanh khoan / He so kha nang thanh toan | "Kha nang thanh toan hien hanh" for current ratio |
| Current ratio | He so thanh toan hien tai / He so hien hanh | Current assets / Current liabilities |
| Quick ratio | He so thanh toan nhanh | (Current assets - Inventory) / Current liabilities |
| Debt-to-equity ratio | He so No / Von chu so huu | Leverage indicator |
| Return on Assets (ROA) | Ty suat Loi nhuan tren Tai san (ROA) | Standard financial metric |
| Return on Equity (ROE) | Ty suat Loi nhuan tren Von chu so huu (ROE) | Key investor metric |
| Profit margin | Ty suat Loi nhuan / Bien loi nhuan | "Bien loi nhuan gop" for gross margin |
| Earnings per Share (EPS) | Loi nhuan tren Co phieu (EPS) | Mandatory disclosure for listed companies |
| Price-to-Earnings (P/E) | He so Gia / Thu nhap (P/E) | Valuation ratio |
| Compound Annual Growth Rate (CAGR) | Ty le Tang truong Kep hang nam (CAGR) | Growth metric |
| Net Asset Value (NAV) | Gia tri Tai san Thuan (NAV) | Used in fund reporting |
| Working capital | Von luu dong | Current assets - Current liabilities |
| EBITDA | Loi nhuan truoc lai vay, thue, khau hao | Increasingly used in Vietnamese financial reporting |

### 9. Key Vietnamese Accounting Standards (Chuan muc Ke toan Viet Nam)

| VAS Number | Name | Topic | Notes |
|---|---|---|---|
| VAS 01 | Chuan muc chung | Framework | General standard for financial reporting |
| VAS 02 | Hang ton kho | Inventories | Based on IAS 2 with modifications |
| VAS 03 | Tai san co dinh huu hinh | Tangible Fixed Assets | Accounting for PPE |
| VAS 04 | Tai san co dinh vo hinh | Intangible Assets | Based on IAS 38 |
| VAS 05 | Bat dong san dau tu | Investment Property | Separate from fixed assets |
| VAS 06 | Thue tai san | Leases | Being replaced by new standard aligning with IFRS 16 |
| VAS 07 | Ke toan cac khoan dau tu vao cong ty con | Investments in Subsidiaries | Consolidation rules |
| VAS 08 | Ke toan cac khoan dau tu vao cong ty lien ket | Investments in Associates | Equity method |
| VAS 10 | Anh huong cua viec thay doi ty gia hoi doai | Foreign Exchange | FX translation |
| VAS 11 | Hop nhat kinh doanh | Business Combinations | Goodwill accounting |
| VAS 14 | Doanh thu | Revenue | Revenue recognition |
| VAS 15 | Hop dong xay dung | Construction Contracts | Percentage of completion |
| VAS 16 | Chi phi di vay | Borrowing Costs | Capitalization rules |
| VAS 17 | Thue thu nhap doanh nghiep | Income Tax | Current and deferred tax |
| VAS 18 | Cac khoan du phong | Provisions | Provisions and contingencies |
| VAS 21 | Trinh bay bao cao tai chinh | Presentation of Financial Statements | Main presentation standard |
| VAS 24 | Bao cao luu chuyen tien te | Cash Flow Statements | Direct or indirect method |
| VAS 25 | Ke toan cac khoan dau tu tai chinh | Financial Instruments | Being modernized |
| VAS 26 | Thong tin ve cac ben lien quan | Related Party Disclosures | Disclosure standard |
| VAS 27 | Bao cao tai chinh giua nien do | Interim Financial Reporting | Semi-annual reporting |
| VAS 28 | Bao cao bo phan | Segment Reporting | Operating segments |
| VAS 29 | Thay doi chinh sach ke toan | Accounting Policies, Estimates and Errors | Changes and corrections |

### 10. Currency and Monetary Conventions

| Condition | Decision |
|---|---|
| Source amount in VND | Use "d" or "VND" after the amount. "d" after the amount (1.000.000d) is the most common Vietnamese commercial convention. |
| Source amount in USD (or other foreign currency) | State the currency clearly: "1.000 USD". In financial statements, show both the foreign currency amount and VND equivalent at the exchange rate on the transaction date. |
| Exchange rate reference | "Ty gia giao dich binh quan" for average rate; "Ty gia cuoi ky" for closing rate at period end. References are typically to the rate published by Ngan hang Nha nuoc (State Bank of Vietnam). |
| Amount in words for formal financial documents | Use standard Vietnamese number words: "Mot tram trieu dong" (100,000,000 VND). Formal financial documents require words + numerals. |
| Negative amounts in financial tables | Vietnamese convention: parentheses, e.g., (1.000.000) for a negative balance. Do not use the minus sign in formal financial statements unless the source does. |
| Unit headings | "Don vi tinh: 1.000 VND" or "Don vi: Trieu VND" is standard at the top of Vietnamese financial statement columns. |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Numerical value altered (even by rounding)** | Every digit in a financial statement carries legal significance. An altered figure can cause incorrect tax liability, misstated profits, or audit failure. |
| **Decimal/thousands separator reversed** | Changing 1.500,50 (one thousand five hundred point five) to 1,500.50 is a format shift, but writing 1.500,50 when the source meant 1,500.50 (one thousand five hundred point five zero) changes the value. However, the critical direction is: source with dot decimal -> convert to comma decimal for Vietnamese output. |
| **VAS vs IFRS terminology confusion** | Using "Loi nhuan tong hop" (IFRS total comprehensive income) when the document follows VAS (which uses "Loi nhuan sau thue") creates a compliance issue. Match terminology to the applicable accounting framework. |
| **Tax code or rate referenced incorrectly** | Citing an incorrect Thue GTGT rate (e.g., 8% instead of 10%) or an incorrect Thue TNDN rate can lead to serious tax filing errors and penalties under Luat Quan ly Thue. |
| **Account code misassigned** | Mapping a financial line item to the wrong account code (e.g., TK 635 "Chi phi tai chinh" for an item that should be TK 641 "Chi phi ban hang") distorts the financial statement classification. |
| **Currency unit not stated or ambiguous** | Failing to specify whether figures are in VND, USD, or "1.000 VND" (thousands) makes the entire financial statement uninterpretable. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Inconsistent number format across the document** | All numbers in a Vietnamese financial document must use the same separator convention. Mixing Vietnamese (1.000.000,50) and English (1,000,000.50) formats within the same document is unacceptable. |
| **Missing "Don vi tinh" header** | Vietnamese financial statements must include a "Don vi tinh" (unit of measurement) header specifying whether amounts are in VND, "1.000 VND", USD, etc. |
| **Parentheses for negatives omitted or misapplied** | In Vietnamese financial context, parentheses consistently indicate negative values. Using a minus sign may cause confusion. However, follow the source convention. |
| **"Thuyet minh" (notes) cross-references broken** | Financial statement notes (Ban Thuyet minh BCTC) are cross-referenced from the main statements. References like "Thuyet minh so 5" must be preserved exactly. |
| **Date format inconsistency in financial periods** | Use "Nam tai chinh ket thuc ngay 31/12/2025" for fiscal year. Vietnamese financial period: "Tu ngay 01/01/2025 den ngay 31/12/2025". |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **Zero vs. dash in table cells** | A dash means "not applicable" in Vietnamese financial tables. "0" or "0,00" means zero value. These are not interchangeable. |
| **Rounding notation** | "So lieu lam tron" (rounded figures) must be noted in the header. A figure shown as 1.234.567 when the note says "Don vi: 1.000 VND" actually means 1,234,567,000 VND. |
| **Footnote tie-points** | In Vietnamese financial statements, footnotes (thuyet minh) tie to specific line items via superscript numbers. These tie-points must be preserved exactly. |
| **Single vs. double underlines in totals** | Vietnamese financial statements follow specific formatting: subtotals have a single underline, grand totals have a double underline (or double line above the header). This formatting carries meaning. |
| **Comparative period references** | "Ky truoc" (prior period) and "Ky nay" (current period) must be clearly distinguished. Vietnamese financial statements present two columns: "Thuyet minh" (Note), "Cuoi nam" (Year-end), "Dau nam" (Beginning of year). |

## Domain-Specific Reference

### Standard Financial Statement Column Headers (Vietnamese)

| Vietnamese Header | English Equivalent | Notes |
|---|---|---|
| Chi tieu | Item / Indicator | First column |
| Ma so | Code | Account or line code |
| Thuyet minh | Note reference | Cross-reference to notes |
| So cuoi nam (31/12/2025) | Year-end balance | Current year closing |
| So dau nam (01/01/2025) | Beginning balance | Prior year closing |
| Ky nay | Current period | Income statement |
| Ky truoc | Prior period | Comparative figure |
| Luy ke tu dau nam | Year-to-date | Cumulative from start of fiscal year |

### Key Vietnamese Regulatory Bodies for Finance

| Abbreviation | Full Name | Role |
|---|---|---|
| BTC | Bo Tai chinh | Ministry of Finance — issues accounting standards, tax regulations |
| CT | Co quan Thue (Tong cu Thue) | General Department of Taxation |
| Hai quan | Tong cuc Hai quan | General Department of Customs |
| NHNN | Ngan hang Nha nuoc Viet Nam | State Bank of Vietnam — central bank |
| UBCK | Uy ban Chung khoan Nha nuoc | State Securities Commission |
| KTNN | Kiem toan Nha nuoc | State Audit Office of Vietnam |
| VACPA | Hoi Kiem toan vien Hanh nghe Viet Nam | Vietnam Association of Certified Public Accountants |
| BTC-KBNN | Kho bac Nha nuoc | State Treasury |

### Vietnamese Numbers in Words (for Financial Amounts)

| Numeric Value | Vietnamese Words | Notes |
|---|---|---|
| 1.000 | Mot nghin | One thousand |
| 10.000 | Muoi nghin | Ten thousand |
| 100.000 | Mot tram nghin | One hundred thousand |
| 1.000.000 | Mot trieu | One million |
| 10.000.000 | Muoi trieu | Ten million |
| 100.000.000 | Mot tram trieu | One hundred million |
| 1.000.000.000 | Mot ty | One billion |
| 10.000.000.000 | Muoi ty | Ten billion |
| 100.000.000.000 | Mot tram ty | One hundred billion |
| 1.000.000.000.000 | Mot nghin ty | One trillion |
| 500,50 | Nam tram nam muoi xu | 500 dong and 50 xu (cents) |
| (1.000.000) | Am mot trieu dong | Negative one million VND |

### Vietnamese Fiscal Year and Reporting Deadlines

| Obligation | Deadline | Notes |
|---|---|---|
| Fiscal year | January 1 - December 31 | Standard calendar year |
| Quarterly CIT declaration | 30 days after quarter end | Provisional CIT payment |
| Annual CIT finalization | 90 days after year-end (March 31) | Quyet toan thue TNDN nam |
| Annual financial statement submission | 90 days after year-end | To Co quan Thue and Co quan Dang ky Kinh doanh |
| VAT declaration (monthly) | 20th of following month | Monthly filing most common |
| VAT declaration (quarterly) | 30th of following quarter | For small taxpayers |
| Audited financial statements | 90 days after year-end | Required for listed companies, FDI enterprises |
| Consolidated financial statements | 90-150 days after year-end | For parent companies |
| Transfer pricing documentation | 90 days after year-end | Tiered documentation requirements |
