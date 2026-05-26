---
id: fi/domain/financial
type: domain
target_lang: fi
name: Domain: Financial (Finnish -- FI)
description: Finnish financial domain terminology and translation rules
---

# Finnish Financial Domain Translation

## Reader Model

### Target Reader Profile
- **Primary Reader**: Finnish financial analysts, accountants (tilintarkastajat), auditors, CFOs (talousjohtajat)
- **Secondary Reader**: Banking professionals, insurance specialists, investment advisors, tax authorities (Vero)
- **Tertiary Reader**: Corporate boards, shareholders (osakkeenomistajat), regulators (Finanssivalvonta)

### Reader Expectations
1. **Accounting Terminology Precision**: All terms must correspond to Finnish Accounting Standards (kirjanpito-ohjeet) and International Financial Reporting Standards (IFRS) as adopted in Finnish.
2. **Currency Consistency**: EUR formatting with Finnish conventions (decimal comma, thousands space).
3. **Legal Entity Accuracy**: Correct Finnish company types (Oy, Oyj, Tmi, etc.).
4. **Statutory Compliance**: Financial statements terminology must align with the Finnish Accounting Act (Kirjanpitolaki, 1336/1997).
5. **Tax Terminology**: Correct Finnish tax terms (vero, veroilmoitus, arvonlisävero, etc.).

### Reader Expectation Matrix

| Expectation | Importance | Consequence if Unmet |
|-------------|------------|---------------------|
| Finnish accounting terminology | Critical | Financial misinterpretation |
| EUR format compliance | High | Audit failure |
| Correct company types | Critical | Legal confusion |
| IFRS/Finnish GAAP alignment | High | Regulatory non-compliance |
| Tax terminology accuracy | Critical | Tax filing errors |
| Numerical precision | Critical | Financial loss |

---

## Decision Framework

### Table F1: Financial Statements Terminology (Kirjanpito)

| English | Finnish | Legislation Reference | Description |
|---------|---------|----------------------|-------------|
| Financial statements | tilinpäätös | KPL 3:9 | Complete financial report |
| Balance sheet | tase | KPL 3:9 | Statement of financial position |
| Income statement | tuloslaskelma | KPL 3:9 | Profit and loss statement |
| Cash flow statement | rahavirtatilasto | KPL 3:9 | Cash flow report |
| Notes to financial statements | liitteet / erittelyt | KPL 3:9 | Supporting disclosures |
| Annual report | vuosikertomus | KPL | Yearly company report |
| Auditor's report | tilintarkastajanlausunto | KPL 3:10 | Audit opinion |
| Audit opinion | tilintarkastajanlausunto | KPL | Auditor's conclusion |
| Going concern | jatkuva toiminta | IAS 1 | Assumption of continued operation |
| Materiality | olennaisuus | ISA | Significance threshold |
| Depreciation | poisto | KPL | Asset value reduction |
| Amortisation | arvonalentuminen | KPL | Intangible asset reduction |
| Impairment | arvonalentuminen | IAS 36 | Asset write-down |
| Goodwill | liikearvo | IAS 38 | Excess purchase price |
| Intangible assets | aineettomat vastaavat | KPL | Non-physical assets |
| Tangible assets | aineelliset vastaavat | KPL | Physical assets |
| Current assets | vastaavat / lyhytaikaiset vastaavat | KPL | Short-term assets |
| Non-current assets | pitkäaikaiset vastaavat | KPL | Long-term assets |
| Liabilities | vastattavat / velat | KPL | Obligations |
| Equity | oma pääoma | KPL | Net assets |
| Share capital | osakepääoma | ARVL | Registered capital |
| Retained earnings | edellisten tilikausien voitto/ tappio | KPL | Accumulated profits/losses |
| Dividend | osinko | ARVL | Profit distribution |

### Table F2: Banking and Investment Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Deposit | talletus | Bank deposit |
| Loan | laina | Borrowed capital |
| Mortgage | kiinnitys | Property-secured loan |
| Interest | korko | Cost of borrowing |
| Interest rate | korkokanta | Rate of interest |
| Credit | luotto | Loan/credit facility |
| Collateral | vakuus | Security for obligation |
| Securities | arvopaperi | Financial instruments |
| Share | osake | Equity security |
| Bond | jouluvelkakirja / obligaatio | Debt security |
| Fund | rahasto | Investment fund |
| Portfolio | salkku | Investment portfolio |
| Dividend | osinko | Profit share |
| Yield | tuotto | Return on investment |
| Return on investment | sijoituksen tuotto | ROI |
| Risk | riski | Uncertainty of outcome |
| Liquidity | likviditeetti / rahaliikkuvuus | Ability to meet obligations |
| Solvency | maksuvalmius | Ability to pay debts |
| Asset management | omaisuudenhoito | Management of assets |
| Wealth management | varallisuudenhoito | Wealth administration |

### Table F3: Tax Terminology

| English | Finnish | Legislation Reference | Description |
|---------|---------|----------------------|-------------|
| Tax | vero | VerVL | Compulsory payment |
| Income tax | tulovero | VerVL | Tax on income |
| Corporate tax | yhtiövero | VerVL | Company tax |
| Value Added Tax (VAT) | arvonlisävero (ALV) | ALVL | Consumption tax |
| Tax return | veroilmoitus | VerVL | Annual tax filing |
| Tax assessment | verotusarvio | VerVL | Tax calculation |
| Tax deduction | verovähennys | VerVL | Amount subtracted from tax |
| Tax credit | verohyvitys | VerVL | Amount reducing tax liability |
| Tax rate | veroprosentti | VerVL | Percentage applied |
| Tax-free | verovapaa | VerVL | Exempt from tax |
| Tax year | verovuosi | VerVL | Fiscal year for tax |
| Withholding tax | lähdevero | VerVL | Tax at source |
| Double taxation | kaksinkertainen verotus | VerVL | Taxed twice |

### Table F4: Stock Exchange and Market Terminology

| English | Finnish | Description |
|---------|---------|-------------|
| Stock exchange | pörssi | Securities market |
| Nasdaq Helsinki | Nasdaq Helsinki (Helsingin pörssi) | Finnish stock exchange |
| Share price | osakekurssi | Current share value |
| Market capitalization | markkina-arvo | Total market value |
| Trading volume | vaihto | Volume of shares traded |
| IPO | ensimmäinen julkinen tarjous (IPO) | Initial public offering |
| Bull market | nousumarkkina | Rising market |
| Bear market | laskumarkkina | Declining market |
| Index | indeksi | Market indicator |
| Helsinki 25 (OMXH25) | OMX Helsinki 25 (OMXH25) | Finnish benchmark index |
| Broker | välittäjä | Intermediary |
| Custody account | hallintatili | Account for holding securities |

---

## Error Pattern Library

### EP-F1: EUR Formatting Errors
- **Common Error**: Using period as thousands separator (`1.000,00 EUR`) instead of space (`1 000,00 EUR`).
- **Correct**: Finnish convention requires a space (narrow non-breaking space, U+202F) for thousands: `1 000,00 EUR`.
- **Rule**: Always use space-separated thousands with decimal comma for EUR amounts in Finnish.

### EP-F2: Partitive for Financial Amounts
- **Common Error**: Using nominative case for monetary amounts where partitive is required.
- **Correct**: `500 euroa` (partitive), not `500 euro`. Partitive is required after numerals in Finnish.
- **Rule**: After numerals, Finnish requires partitive case for the counted noun.

### EP-F3: Company Type Confusion
- **Common Error**: Translating `Ltd.` as `Oyj` (public company) instead of `Oy` (private company).
- **Correct**: `Ltd.` = `Oy` (Osakeyhtiö — limited private company). `Oyj` = public limited company.
- **Rule**: Verify whether the source refers to a public or private entity.

### EP-F4: Balance Sheet Terminology
- **Common Error**: Using `tase` for individual line items instead of `vastaavat`/`vastattavat`.
- **Correct**: `Tase` is the entire balance sheet. `Vastaavat` (assets) and `vastattavat` (liabilities/equity) are the two sides.
- **Rule**: `Tase` = the report; `vastaavat`/`vastattavat` = the sections.

---

## Domain-Specific Reference

### Finnish Accounting Standards
- **Kirjanpitolaki** (1336/1997) — Finnish Accounting Act, the primary legislation governing accounting.
- **Kirjanpito-ohjeet** — Finnish accounting standards issued by the Accounting Board (Kirjanpitolautakunta).
- **IFRS** adopted in Finland for listed companies (Oyj) since 2005.
- **EU directives** implemented in Finnish accounting law.

### Finnish Financial Reporting Structure
1. **Tase** (Balance Sheet) — assets (vastaavat) and liabilities/equity (vastattavat/omaisuus ja vastattavat).
2. **Tuloslaskelma** (Income Statement) — revenue (liikevaihto), expenses (kulut), result (tulos).
3. **Rahavirtatilasto** (Cash Flow Statement) — operating, investing, financing activities.
4. **Liitteet** (Notes) — accounting policies and detailed disclosures.
5. **Vuosiselvitys** (Management Report) — narrative review of operations.

### Finnish Financial Abbreviations
- `KPL` = Kirjanpitolaki (Accounting Act)
- `VerVL` = Vero- ja maksueräasetus (Tax and Payment Decree)
- `ALVL` = Arvonlisäverolaki (VAT Act)
- `ARVL` = Arvopaperilaki (Securities Act)
- `IFRS` = Kansainväliset tilinpäätösstandardit (International Financial Reporting Standards)
- `ALV` = Arvonlisävero (VAT)
- `VAT` = Value Added Tax (used in English-language Finnish contexts)
