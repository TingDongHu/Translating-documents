---
id: da/domain/financial
type: domain
target_lang: da
domain: financial
name: Domain: Financial (Danish — DA)
aliases: [finans, økonomi, regnskab, bogføring, financial-Danish, dansk økonomi]
---

# Financial Domain: Danish Translation Standards

## Reader Model

**Primary Reader:** Danish financial analyst (analytiker), auditor (revisor), or accountant (bogholder). The reader expects precise financial terminology conforming to Danish and EU accounting standards (årsregnskabsloven). They read numbers with extreme precision — every decimal, every currency symbol, every date format must be exact. The reader is familiar with Nasdaq Copenhagen conventions and Danish Financial Supervisory Authority (Finanstilsynet) terminology.

**Secondary Reader:** CFO (administrerende direktør / finansdirektør) or board member (bestyrelsesmedlem) reviewing financial statements or investment documents. They expect professional formatting consistent with Danish annual report conventions (årsrapport).

**Tertiary Reader:** International investor or partner reading Danish financial documents with translation support. Danish financial terminology must be consistent and accurate for cross-border comparison.

**Reader Priorities:**
1. Numerical precision (Danish number format: 1.000,00 — dot thousands, comma decimal)
2. Correct financial terminology (e.g. "omsætning" not "indtægt" for "revenue"; "resultat" not "overskud" for "result")
3. Currency formatting (DKK/kr. conventions)
4. Date format consistency (DD.MM.YYYY)
5. Compliance with Danish årsregnskabsloven terminology
6. Consistent use of chart of accounts terminology (kontoplan)

---

## Decision Framework

### Table 1: Financial Statement Terminology

| English | Danish | Danish Accounting Standard | Notes |
|---------|--------|---------------------------|-------|
| Balance sheet |Balance | Årsregnskabsloven | Not "balance" in the English sense |
| Income statement | Resultatopgørelse | Årsregnskabsloven § 12 | Profit & Loss equivalent |
| Cash flow statement | Pengestrømsopgørelse | Årsregnskabsloven § 13 | IAS 7 equivalent |
| Equity | Egenkapital | Årsregnskabsloven § 12 | Not "aktiekapital" (that's share capital) |
| Revenue | Omsætning | Årsregnskabsloven | Not "indtægter" (that's income generally) |
| Net profit | Nettoresultat | Årsregnskabsloven | Not "nettooverskud" |
| Gross profit | Bruttofortjeneste | Årsregnskabsloven | Not "bruttooverskud" |
| Operating profit | Driftsresultat | Årsregnskabsloven | EBIT equivalent |
| EBITDA | EBITDA | Common usage | Same abbreviation internationally |
| Total assets | Aktiver i alt | Årsregnskabsloven | Not "samlede aktiver" |
| Total liabilities | Passiver i alt | Årsregnskabsloven | Not "samlede passiver" |
| Current assets | Omsætningsaktiver | Årsregnskabsloven | Not "kortsigtede aktiver" |
| Fixed assets | Anlægsaktiver | Årsregnskabsloven | Not "langsigtede aktiver" |
| Current liabilities | Kortfristede gældsforpligtelser | Årsregnskabsloven | Not "kortsigtede gæld" |
| Long-term debt | Langfristede gældsforpligtelser | Årsregnskabsloven | Not "langsigtede gæld" |
| Share capital | Aktiekapital | Selskabsloven | Registered capital |
| Retained earnings | Egenkapitalens reserveposter | Årsregnskabsloven | Accumulated profit |
| Depreciation | Afskrivning | Årsregnskabsloven | Annual depreciation |
| Amortisation | Nedskrivning | Årsregnskabsloven | Intangible asset amortisation |
| Impairment | Værdifald | Årsregnskabsloven | Asset write-down |
| Goodwill | Goodwill | International usage | Same in Danish |
| Audit | Revision | Revisorloven | Annual audit |

### Table 2: Investment and Banking Terminology

| English | Danish | Notes |
|---------|--------|-------|
| Stock exchange | Børs | Nasdaq Copenhagen |
| Share | Aktje | Ordinary share |
| Dividend | Udbytte | Annual dividend |
| Interest rate | Rente / rentesats | Not "interesse" (that's interest as curiosity) |
| Loan | Lån | Standard term |
| Mortgage | Realkreditlån | Property-backed loan |
| Bond | Obligation | Government or corporate bond |
| Fund | Fond / investeringsforening | Collective investment |
| Portfolio | Portefølje | Investment portfolio |
| Yield | Afkast / forrentning | Return on investment |
| Return on investment | Afkastningsgrad | ROI |
| Liquidity | Likviditet | Cash availability |
| Solvency | Solvens | Financial health |
| Credit rating | Kreditvurdering | Not "kreditbedømmelse" |
| Risk management | Risikostyring | Not "risikohåndtering" |
| Due diligence | Due diligence / gennemgang | Both used; "grundig gennemgang" for Danish |
| IPO | Børsintroduktion / IPO | Both used |
| Market capitalisation | Markedsværdi / børsværdi | Both acceptable |

### Table 3: Danish Corporate Entity Types

| Abbreviation | Full Name | English Equivalent | Minimum Capital |
|-------------|-----------|-------------------|-----------------|
| A/S | Aktieselskab | Public limited company | DKK 400.000 |
| ApS | Anpartsselskab | Private limited company | DKK 40.000 |
| IVS | Iværksætterselskab | Startup company (abolished 2019) | DKK 1 |
| P/S | Partnerselskab | Partnership limited by shares | DKK 400.000 |
| I/S | Interessentskab | General partnership | None |
| F/M | Forening | Association | None |
| AMBA | Andelsselskab med begrænset ansvar | Cooperative with limited liability | None |
| FMBA | Forening med begrænset ansvar | Association with limited liability | None |

### Table 4: Danish Tax Terminology

| English | Danish | Notes |
|---------|--------|-------|
| Corporate tax | Selskabsskat | 22% rate |
| VAT | Merværdiafgift / moms | 25% standard rate |
| Income tax | Indkomstskat | Progressive rates |
| Tax return | Selvangivelse / skatteopgørelse | Annual filing |
| Tax deduction | Fradrag | Various types |
| Tax exemption | Skattefrihed / fritagelse | Context-dependent |
| Transfer pricing | Transfer pricing / overførselspriser | Both used |
| Double taxation | Dobbeltbeskatning | Treaty context |
| Tax authority | Skattestyrelsen | Formerly SKAT |

---

## Error Pattern Library

### Common Translation Errors

| Error Type | Incorrect | Correct | Explanation |
|-----------|-----------|---------|-------------|
| Number format | "1,000.00 kr." | "1.000,00 kr." | Danish uses dot thousands, comma decimal |
| Currency | "DKK 1.000" (before amount) | "1.000,00 kr." | Symbol/code after amount |
| Account name | "Indtægter" for revenue | "Omsætning" | "Omsætning" is the specific term for revenue/sales |
| Account name | "Overskud" for profit | "Resultat" | "Resultat" is the formal accounting term |
| Entity type | "LLC" for Danish company | "ApS" or "A/S" | Use Danish entity types |
| Date | "January 15, 2026" | "15. januar 2026" | Danish date format |
| Tax term | "Moms" (informal) | "Merværdiafgift" (formal) | "moms" is colloquial; "merværdiafgift" is formal |
| Audit | "revision" (lowercase) | "Revision" (capitalized as proper noun in context) | Context-dependent capitalisation |

### Ambiguous Terms Requiring Context

| English | Danish Options | When to Use |
|---------|---------------|-------------|
| "account" | "konto" (ledger) / "regnskab" (financial statements) | "konto" for individual accounts; "regnskab" for overall statements |
| "value" | "værdi" (intrinsic) / "kurs" (market price) | "værdi" for book value; "kurs" for market price |
| "capital" | "kapital" (financial) / "egenkapital" (equity) | "kapital" general; "egenkapital" for equity specifically |
| "fund" | "fond" (collective) / "pulje" (pool/allocation) | "fond" for investment funds; "pulje" for budget allocations |
| "rate" | "rente" (interest) / "kurs" (exchange/security) / "sats" (rate/percentage) | Context-dependent |

---

## Domain-Specific Reference

### Danish Financial Reporting Standards

**Årsregnskabsloven (Danish Annual Accounts Act):** The primary statute governing financial reporting in Denmark. Key categories:
- **Class A** (small): Simplified reporting
- **Class B** (medium): Moderate reporting requirements
- **Class C** (large): Full IFRS-aligned reporting
- **Class D** (listed): Full IFRS compliance required

**Erhvervsstyrelsen (Danish Business Authority):** Registers annual reports for all Danish companies.

**Finanstilsynet (Danish FSA):** Supervises financial institutions and markets.

### Nasdaq Copenhagen Conventions

- Stock prices listed in DKK
- Bond prices as percentage of par value
- Trading hours: 09:00–17:00 CET
- Settlement: T+2 (business days)
- Index: OMX Copenhagen 25 (OMXC25)

### Key Financial Abbreviations in Danish

| Abbreviation | Danish Full Form | English |
|-------------|-----------------|---------|
| årsrapport | årsrapport | Annual report |
| halvårsrapport | halvårsrapport | Semi-annual report |
| kvartalsrapport | kvartalsrapport | Quarterly report |
| regnskabsår | regnskabsår | Financial year |
| tilgang | tilgang | Acquisition |
| afgang | afgang | Disposal |
| geninvestering | geninvestering | Reinvestment |
| nedskrivning | nedskrivning | Impairment |
| genoptjening | genoptjening | Reversal of impairment |

---

*End of Danish Financial Domain Reference.*
