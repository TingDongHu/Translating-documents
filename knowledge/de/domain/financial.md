---
id: de/domain/financial
type: domain
target_lang: de
domain: financial
aliases: [Finanzen, Jahresabschluss, Buchhaltung, Bilanz, Rechnungswesen, Finanzberichterstattung, HGB]
---

# Financial Domain: German Translation Standards

## Reader Model

**Primary Reader:** German accountant (Bilanzbuchhalter, Steuerfachangestellter), auditor (Wirtschaftsprüfer, vereidigter Buchprüfer), tax advisor (Steuerberater), or CFO (Finanzvorstand). The reader expects precise mapping of accounts (Kontenrahmen), correct application of German accounting standards (GoB, HGB, DRS), and flawless numerical accuracy. The reader cross-references every figure against supporting documentation. They are trained to identify inconsistencies in account classification, revenue recognition, and tax treatment at a glance. A mistranslated account name can trigger a failed audit or incorrect tax assessment.

**Secondary Reader:** German tax authority (Finanzamt — Betriebsprüfer) or regulatory body (BaFin, Deutsche Bundesbank). They examine the translation for compliance with German tax law (AO, EStG, KStG, UStG, GewStG) and regulatory reporting requirements (Solvabilitätsverordnung, Rechnungslegungsstandards). A mistranslated revenue category or incorrect provision classification can trigger a tax audit (Betriebsprüfung) or regulatory fine.

**Tertiary Reader:** International investor or analyst comparing German GAAP (HGB) financial statements with IFRS equivalents. They need clear mapping between the two accounting frameworks (Überleitungsrechnung). The translation must identify which accounting framework is used and where differences arise.

**Reader Priorities:**
1. Correct account classification mapping (IFRS -> HGB using SKR 03/04 terminology)
2. Numerical zero tolerance (decimal comma, digit grouping, no transposition of digits)
3. German chart of accounts terminology (DATEV-Kontenrahmen SKR 03/04)
4. Tax law terminology (Vorsteuer, Umsatzsteuer, Körperschaftsteuer, Gewerbesteuer)
5. Financial statement structure (Bilanz, GuV, Anhang, Lagebericht, Kapitalflussrechnung)
6. Currency formatting (EUR with decimal comma and period thousand separator)
7. HGB vs. IFRS distinction — never mix terminology across frameworks without clear labeling
8. Proper use of Rückstellung vs. Rücklage (provision vs. reserve — a critical distinction)

---

## Decision Framework

### Table 1: Financial Statement Structure — HGB vs. IFRS

| Statement Component | HGB German Term | IFRS German Term | HGB Reference |
|--------------------|-----------------|------------------|---------------|
| Balance sheet | Bilanz | Bilanz / Vermögensaufstellung | § 266 HGB |
| Income statement | Gewinn- und Verlustrechnung (GuV) | Gesamtergebnisrechnung | § 275 HGB |
| Cash flow statement | Kapitalflussrechnung | Kapitalflussrechnung | DRS 21 / IAS 7 |
| Statement of changes in equity | Eigenkapitalveränderungsrechnung | Eigenkapitalveränderungsrechnung | DRS 22 / IAS 1 |
| Notes | Anhang | Anhang | §§ 284–288 HGB |
| Management report | Lagebericht | Lagebericht | § 289 HGB / DRS 20 |
| Segment report | Segmentberichterstattung | Segmentberichterstattung | DRS 28 / IFRS 8 |
| Related party disclosures | Angaben über Beziehungen zu nahe stehenden Unternehmen | Angaben über nahe stehende Unternehmen | § 285 HGB / IAS 24 |
| Corporate governance statement | Entsprechenserklärung zum DCGK | Entsprechenserklärung | § 161 AktG |
| Remuneration report | Vergütungsbericht | Vergütungsbericht | § 162 AktG |

### Table 2: HGB Balance Sheet — Asset Side (Aktiva, § 266 HGB)

| HGB Position (§ 266) | English Equivalent | Account Group | Notes |
|----------------------|--------------------|---------------|-------|
| A. Anlagevermögen | Fixed assets | | |
| I. Immaterielle Vermögensgegenstände | Intangible assets | Includes goodwill (Geschäfts- oder Firmenwert) | |
| II. Sachanlagen | Property, plant and equipment | Land, buildings, technical equipment, other equipment | |
| III. Finanzanlagen | Financial assets | Shares, loans, securities | |
| B. Umlaufvermögen | Current assets | | |
| I. Vorräte | Inventories | Raw materials, work in progress, finished goods | |
| II. Forderungen und sonstige Vermögensgegenstände | Receivables and other assets | Trade receivables, other receivables | |
| III. Wertpapiere | Securities | Current securities | |
| IV. Kasse, Bank, Guthaben | Cash and cash equivalents | Bank balances, cash on hand | |
| C. Rechnungsabgrenzungsposten | Prepaid expenses / deferred items | | |
| D. Aktive latente Steuern | Deferred tax assets | § 274 HGB | |

### Table 3: HGB Balance Sheet — Liabilities Side (Passiva, § 266 HGB)

| HGB Position (§ 266) | English Equivalent | Account Group | Notes |
|----------------------|--------------------|---------------|-------|
| A. Eigenkapital | Equity | | |
| I. Gezeichnetes Kapital | Subscribed capital | Share capital | |
| II. Kapitalrücklage | Capital reserve | Share premium | |
| III. Gewinnrücklagen | Revenue reserves | Statutory, voluntary reserves | |
| IV. Gewinnvortrag/Verlustvortrag | Retained earnings / accumulated losses | | |
| V. Jahresüberschuss/Jahresfehlbetrag | Net income / Net loss for the year | | |
| B. Rückstellungen | Provisions | | |
| I. Rückstellungen für Pensionen | Pension provisions | § 249 HGB | |
| II. Steuerrückstellungen | Tax provisions | | |
| III. Sonstige Rückstellungen | Other provisions | | |
| C. Verbindlichkeiten | Liabilities | | |
| I. Anleihen | Bonds | | |
| II. Verbindlichkeiten ggü. Kreditinstituten | Bank loans | | |
| III. Verbindlichkeiten aus Lieferungen und Leistungen | Trade payables | | |
| IV. Sonstige Verbindlichkeiten | Other liabilities | | |
| D. Passive Rechnungsabgrenzungsposten | Deferred income | | |
| E. Passive latente Steuern | Deferred tax liabilities | | |

### Table 4: IFRS to HGB Terminology Mapping

| IFRS (English) | IFRS (German) | HGB (German) | Key Differences |
|----------------|---------------|--------------|-----------------|
| Statement of Financial Position | Bilanz / Vermögensaufstellung | Bilanz | HGB uses fixed format (§ 266) |
| Property, Plant and Equipment | Sachanlagevermögen | Sachanlagen | Same term, different measurement (HGB: cost less depreciation; IFRS: may use revaluation) |
| Intangible Assets | Immaterielle Vermögenswerte | Immaterielle Vermögensgegenstände | IFRS includes more intangibles; HGB restricts capitalization |
| Goodwill | Geschäfts- oder Firmenwert (GoF) | Geschäfts- oder Firmenwert | HGB: amortization; IFRS: impairment only |
| Financial Assets | Finanzinstrumente / Finanzanlagen | Finanzanlagen | IFRS: fair value; HGB: lower of cost or market (gemildertes Niederstwertprinzip) |
| Inventories | Vorräte | Vorräte | Similar but IFRS: no LIFO |
| Trade Receivables | Forderungen aus Lieferungen und Leistungen | Forderungen aus Lieferungen und Leistungen | Same |
| Cash and Cash Equivalents | Zahlungsmittel und Zahlungsmitteläquivalente | Kassenbestand, Guthaben bei Kreditinstituten | Different classification |
| Equity | Eigenkapital | Eigenkapital | Similar |
| Non-controlling Interests | Nicht beherrschende Anteile | Anteile anderer Gesellschafter | Terminology differs |
| Provisions | Rückstellungen | Rückstellungen | Similar (but IFRS: no Rückstellung for future operating losses) |
| Contingent Liabilities | Eventualverbindlichkeiten | Eventualverbindlichkeiten | Same |
| Revenue | Umsatzerlöse | Umsatzerlöse | IFRS 15 vs. HGB rules |
| Cost of Sales | Umsatzkosten | Umsatzkosten | Only in UKV, not GKV |
| Other Operating Income | Sonstige betriebliche Erträge | Sonstige betriebliche Erträge | Same |
| Income Tax Expense | Steuern vom Einkommen und vom Ertrag | Steuern vom Einkommen und vom Ertrag | Same |
| Deferred Tax Assets | Aktive latente Steuern | Aktive latente Steuern | HGB: stricter recognition |
| Deferred Tax Liabilities | Passive latente Steuern | Passive latente Steuern | Same |
| Earnings Per Share | Ergebnis je Aktie | Ergebnis je Aktie | Same |

### Table 5: German Tax Terminology — Precision Required

| English | German (Official) | Abbreviation | Statute | Notes |
|---------|------------------|-------------|---------|-------|
| Income Tax | Einkommensteuer | ESt | EStG | Personal income tax |
| Corporate Income Tax | Körperschaftsteuer | KSt | KStG | Corporate income tax |
| Trade Tax | Gewerbesteuer | GewSt | GewStG | Municipal business tax (rate varies) |
| Value Added Tax | Umsatzsteuer | USt | UStG | Standard rate 19%, reduced 7% |
| Input VAT | Vorsteuer | VSt | § 15 UStG | Deductible input tax |
| Solidarity Surcharge | Solidaritätszuschlag | SolZ | SolZG | 5.5% of KSt/ESt (partially phased out) |
| Church Tax | Kirchensteuer | KiSt | KiStG | 8-9% of ESt |
| Withholding Tax (capital) | Kapitalertragsteuer | KapSt / KESt | § 43 EStG | 25% flat withholding |
| Withholding Tax (general) | Abzugsteuer / Quellensteuer | | § 50a EStG | Non-resident withholding |
| Wage Tax | Lohnsteuer | LSt | §§ 38 ff. EStG | Employer-withheld payroll tax |
| Payroll Tax | Lohnsteuer / Abgaben | LSt / SV | EStG / SGB | Includes social security |
| Real Property Tax | Grundsteuer | GrSt | GrStG | Municipal property tax |
| Real Property Transfer Tax | Grunderwerbsteuer | GrESt | GrEStG | Varies by state (3.5-6.5%) |
| Inheritance Tax | Erbschaftsteuer / Schenkungsteuer | ErbSt | ErbStG | Covers gifts as well |
| VAT ID Number | Umsatzsteuer-Identifikationsnummer | USt-IdNr. | § 27a UStG | EU cross-border |
| Tax Identification Number | Steuerliche Identifikationsnummer | Steuer-ID / IdNr. | § 139b AO | Personal tax ID |
| Tax Number | Steuernummer | St.-Nr. | AO | Business-specific |
| Assessment Notice | Steuerbescheid | | AO | Tax assessment document |
| Tax Audit | Betriebsprüfung / Außenprüfung | BP | AO | |
| Tax Return | Steuererklärung | | AO / EStG | Annual filing |
| Preliminary Return | Steueranmeldung | | (monthly/quarterly) | VAT, wage tax |

### Table 6: Numerical Zero Tolerance — Financial Figures

| Aspect | English Convention | German Convention | Correct Example | Incorrect Example |
|--------|--------------------|-------------------|-----------------|-------------------|
| Decimal separator | Period (.) | Comma (,) | 1.234,56 | 1,234.56 |
| Thousand separator | Comma (,) | Period (.) or thin space | 1.234.567,89 or 1 234 567,89 | 1,234,567.89 |
| Negative amounts | -1,234.56 | -1.234,56 or (1.234,56) | -1.234,56 | (1,234.56) |
| Positive amounts | 1,234.56 (no +) | 1.234,56 (no +) | 1.234,56 | +1,234.56 |
| Zero | 0.00 | 0,00 | 0,00 | 0.00 |
| Currency symbol | $1,234.56 | 1.234,56 EUR / EUR 1.234,56 | 1.234,56 EUR | EUR 1,234.56 |
| Currency in IFRS | EUR 1,234 | EUR 1.234 / 1.234 EUR | 1.234 EUR | 1,234 EUR |
| Rounding | 1,234.6 | 1.234,6 | 1.234,6 | 1,234.6 |
| Large numbers (million) | $1.2M | 1,2 Mio. EUR / EUR 1,2 Mio | 1,2 Mio. EUR | 1.2 M EUR |
| Large numbers (billion) | $1.2B | 1,2 Mrd. EUR | 1,2 Mrd. EUR | 1.2 B EUR |
| Percentage | 5.5% | 5,5 % | 5,5 % | 5.5 % |
| Share price | EUR 12.50 | 12,50 EUR | 12,50 EUR | EUR 12.50 |

**Verification protocol (for every figure):**
1. Read source number aloud digit by digit
2. Compare with target number character by character
3. Confirm decimal comma replaced decimal point
4. Confirm thousand separator is period in target (not comma)
5. Verify no digit transposition (e.g., 123,45 instead of 132,45)
6. For rounded amounts, verify the rounding is identical

### Table 7: Reserve vs. Provision — Critical Distinction

| English | German | HGB Reference | Section | Nature |
|---------|--------|---------------|---------|--------|
| Provision (liability) | Rückstellung | § 249 HGB | Liabilities (Passiva B) | Uncertain timing or amount; probable outflow |
| Reserve (equity) | Rücklage | § 272 HGB | Equity (Passiva A) | Part of shareholders' equity |
| Capital reserve | Kapitalrücklage | § 272 Abs. 2 HGB | Equity | Share premium, capital contributions |
| Revenue reserve | Gewinnrücklage | § 272 Abs. 3 HGB | Equity | Retained earnings appropriated |
| Legal reserve | gesetzliche Rücklage | § 150 AktG | Equity (AG only) | Mandatory 5% until 10% of capital |
| Pension provision | Pensionsrückstellung | § 249 HGB, § 6a EStG | Provisions | Retirement obligations |
| Tax provision | Steuerrückstellung | § 249 HGB | Provisions | Uncertain tax liabilities |
| Warranty provision | Rückstellung für Gewährleistungen | § 249 HGB | Provisions | Expected warranty costs |
| Bad debt allowance | Einzelwertberichtigung (EWB) | GoB | Deduction from receivables | Specific doubtful accounts |
| General bad debt allowance | Pauschalwertberichtigung (PWB) | GoB | Deduction from receivables | General credit risk |
| Revaluation reserve | Neubewertungsrücklage | (IFRS only) | Equity | IFRS revaluation surplus |
| Hidden reserve | Stille Reserve | § 253 HGB | (Not shown separately) | Created by lower-of-cost-or-market rule |

**Critical distinction error:** Translating "provision" as "Rücklage" (which is equity) instead of "Rückstellung" (which is a liability) produces a materially incorrect financial statement. This is a zero-tolerance error.

### Table 8: Audit and Auditor Terminology (IDW PS)

| English | German | IDW Standard | Notes |
|---------|--------|---------------|-------|
| Audit | Prüfung / Abschlussprüfung | IDW PS 200 | Annual statutory audit |
| Auditor | Wirtschaftsprüfer (WP) | IDW | Qualified auditor |
| Audit firm | Wirtschaftsprüfungsgesellschaft | IDW | |
| Unqualified opinion | uneingeschränkter Bestätigungsvermerk | IDW PS 400 | "Clean" opinion |
| Qualified opinion | eingeschränkter Bestätigungsvermerk | IDW PS 400 | Except for... |
| Adverse opinion | versagter Bestätigungsvermerk | IDW PS 400 | Financial statements are misleading |
| Disclaimer of opinion | Versagung des Bestätigungsvermerks | IDW PS 400 | Unable to form opinion |
| Emphasis of matter | Hinweis auf besondere Umstände / Hervorhebung | IDW PS 450 | Without modifying opinion |
| Materiality | Wesentlichkeit / Prüfungsschwelle | IDW PS 220 | Quantitative and qualitative |
| Audit evidence | Prüfungsnachweise | IDW PS 300 | |
| Risk assessment | Risikobeurteilung / risikoorientierter Prüfungsansatz | IDW PS 261 | |
| Internal control system | Internes Kontrollsystem (IKS) | IDW PS 260 | |
| Going concern | Unternehmensfortführung / Going-Concern-Prämisse | IDW PS 270 | |
| Review | prüferische Durchsicht | IDW PS 900 | Lower assurance than audit |
| Agreed-upon procedures | Auftrag zur Durchführung besonderer Prüfungshandlungen | IDW PS 950 | |
| Consolidation | Konsolidierung | DRS 23-28 | |
| Consolidated financial statements | Konzernabschluss | § 290 HGB | |
| Group auditor | Konzernprüfer | IDW PS 320 | |

**Standard audit opinion opening (IDW PS 400 wording):**
"Wir haben den Jahresabschluss der XYZ GmbH — bestehend aus der Bilanz zum 31. Dezember 2025, der Gewinn- und Verlustrechnung für das Geschäftsjahr vom 1. Januar bis zum 31. Dezember 2025 sowie dem Anhang — unter Einbeziehung der Buchführung geprüft."

### Table 9: Chart of Accounts — SKR 03/04 Key Accounts

| Account Description (English) | SKR 03 Account | SKR 04 Account | German Account Name |
|------------------------------|---------------|---------------|---------------------|
| Fixed assets (tangible) | 0010-0699 | 0020-0090 | Sachanlagen |
| Intangible assets | 0020-0040 | 0010-0015 | Immaterielle Vermögensgegenstände |
| Financial assets | 0700-0745 | 0100-0180 | Finanzanlagen |
| Raw materials | 3000-3099 | 1140-1150 | Rohstoffe |
| Work in progress | 3100-3199 | 1170-1180 | Unfertige Erzeugnisse |
| Finished goods | 3200-3299 | 1190-1200 | Fertige Erzeugnisse |
| Trade receivables | 2000-2099 | 1400-1430 | Forderungen aus LuL |
| Bank balances | 2800-2899 | 1800-1830 | Bankguthaben |
| Cash on hand | 2900-2909 | 1840-1850 | Kassenbestand |
| Equity (GmbH) | 0800-0899 | 2100-2180 | Eigenkapital |
| Capital reserve | 0830 | 2110 | Kapitalrücklage |
| Revenue reserves | 0840-0860 | 2120-2150 | Gewinnrücklagen |
| Tax provisions | 0920 | 2810 | Steuerrückstellungen |
| Pension provisions | 0950 | 2850 | Pensionsrückstellungen |
| Other provisions | 0960-0990 | 2860-2890 | Sonstige Rückstellungen |
| Trade payables | 3300-3399 | 3400-3440 | Verbindlichkeiten aus LuL |
| Bank loans | 3000-3099 | 3100-3150 | Verbindlichkeiten gegenüber Kreditinstituten |
| Revenue (domestic, 19%) | 8100 | 4400 | Umsatzerlöse Inland 19 % |
| Revenue (EU) | 8120 | 4420 | Erlöse EU |
| Revenue (export) | 8130 | 4430 | Erlöse Drittland |
| Other operating income | 2700-2740 | 4900-4930 | Sonstige betriebliche Erträge |
| Cost of materials | 4000-4199 | 5000-5100 | Materialaufwand |
| Personnel costs | 4100-4199 | 6000-6200 | Personalaufwand |
| Depreciation | 4800-4899 | 6300-6390 | Abschreibungen |
| Other operating expenses | 4900-4999 | 6400-6990 | Sonstige betriebliche Aufwendungen |
| Interest income | 7100-7110 | 7200-7260 | Zinserträge |
| Interest expense | 7300-7330 | 7300-7360 | Zinsaufwendungen |
| Income taxes | 7600-7609 | 7600-7680 | Steuern vom Einkommen und vom Ertrag |
| VAT (output, 19%) | 1770 | 3800 | Umsatzsteuer 19 % |
| VAT (input) | 1570 | 1400 | Vorsteuer |

### Table 10: Financial Ratios and KPIs

| English | German | Formula (English) | Formula (German) | Notes |
|---------|--------|-------------------|------------------|-------|
| Equity ratio | Eigenkapitalquote | Equity / Total assets | Eigenkapital / Gesamtkapital | Financial stability |
| Debt-to-equity | Verschuldungsgrad | Total liabilities / Equity | Fremdkapital / Eigenkapital | Leverage |
| Return on Equity (RoE) | Eigenkapitalrentabilität | Net income / Equity | Jahresüberschuss / Eigenkapital | Profitability |
| Return on Assets (RoA) | Gesamtkapitalrentabilität | EBIT / Total assets | EBIT / Gesamtkapital | Asset efficiency |
| Return on Sales (RoS) | Umsatzrentabilität | Net income / Revenue | Jahresüberschuss / Umsatzerlöse | Margin |
| Gross margin | Rohertragsmarge / Bruttomarge | Gross profit / Revenue | Rohertrag / Umsatzerlöse | |
| EBIT margin | EBIT-Marge | EBIT / Revenue | EBIT / Umsatzerlöse | |
| EBITDA margin | EBITDA-Marge | EBITDA / Revenue | EBITDA / Umsatzerlöse | |
| Current ratio | Liquidität 3. Grades | Current assets / Current liabilities | Umlaufvermögen / kurzfristige Verbindlichkeiten | |
| Quick ratio | Liquidität 2. Grades | (Current assets - Inventory) / Current liabilities | (Umlaufvermögen - Vorräte) / kurzfristige Verbindlichkeiten | |
| Cash ratio | Liquidität 1. Grades | Cash / Current liabilities | Liquide Mittel / kurzfristige Verbindlichkeiten | |
| Working capital | Working Capital / Nettoumlaufvermögen | Current assets - Current liabilities | Umlaufvermögen - kurzfristige Verbindlichkeiten | |
| Days sales outstanding (DSO) | Forderungslaufzeit | (Receivables / Revenue) x 365 | (Forderungen / Umsatzerlöse) x 365 | |
| Inventory turnover | Lagerumschlagshäufigkeit | COGS / Average inventory | Materialaufwand / durchschnittlicher Lagerbestand | |
| Book value per share | Buchwert je Aktie | Equity / Shares outstanding | Eigenkapital / Aktienanzahl | |

### Table 11: Currency and Foreign Exchange (IAS 21 / HGB)

| English | German | Source | Example |
|---------|--------|--------|---------|
| Functional currency | Funktionale Währung | IAS 21 | "Der Euro ist die funktionale Währung." |
| Presentation currency | Darstellungswährung | IAS 21 | |
| Foreign currency | Fremdwährung | IAS 21 | "Fremdwährung USD" |
| Exchange rate | Wechselkurs / Devisenkurs | IAS 21 / AStG | "1 EUR = 1,05 USD" |
| Spot rate | Kassakurs / Tageskurs | IAS 21 | |
| Average rate | Durchschnittskurs | IAS 21 | |
| Closing rate | Stichtagskurs / Devisenkurs am Bilanzstichtag | IAS 21 / § 256a HGB | |
| Exchange gain | Kursgewinn / Währungsgewinn | IAS 21 | |
| Exchange loss | Kursverlust / Währungsverlust | IAS 21 | |
| Currency translation | Währungsumrechnung | IAS 21 / DRS 25 | |
| Translation reserve | Rücklage aus Währungsumrechnung | IAS 21 | |
| Hedge accounting | Bilanzielle Sicherungsbeziehung / Hedge Accounting | IFRS 9 / HGB | |
| Hedging instrument | Sicherungsinstrument | IFRS 9 | |
| Hedged item | Grundgeschäft | IFRS 9 | |

### Table 12: Revenue Recognition (IFRS 15 vs. HGB)

| English | IFRS 15 German | HGB German | Key Difference |
|---------|---------------|------------|----------------|
| Revenue | Umsatzerlöse | Umsatzerlöse | IFRS 15: five-step model; HGB: risk/reward transfer |
| Performance obligation | Leistungsverpflichtung | (Kein direkter Begriff) | IFRS-specific term |
| Transaction price | Transaktionspreis | Entgelt / Gegenleistung | |
| Variable consideration | Variables Entgelt | (keine gesonderte Regelung) | IFRS: estimate; HGB: realized only |
| Stand-alone selling price | Einzelveräußerungspreis | (keine gesonderte Regelung) | IFRS: allocation |
| Contract asset | Vertragsvermögenswert | (Forderung) | IFRS: performance before billing |
| Contract liability | Vertragsverbindlichkeit | Erhaltene Anzahlungen | IFRS 15: new term for advances |
| Significant financing component | Wesentlicher Finanzierungsanteil | (keine gesonderte Regelung) | IFRS: adjust for time value |
| Principal vs. agent | Grundsatz / Beauftragter | Eigenhändler / Vermittler | |
| Licensing of IP | Lizenzierung von geistigem Eigentum | (keine gesonderte Regelung) | IFRS 15: distinct guidance |
| Costs to obtain a contract | Kosten der Vertragsanbahnung | (Aktivierung nicht üblich) | IFRS: capitalize; HGB: expense |

### Table 13: Subsequent Events and Going Concern

| English | German | Standard | Notes |
|---------|--------|----------|-------|
| Events after the reporting period | Ereignisse nach dem Bilanzstichtag | IAS 10 / § 252 HGB | |
| Adjusting event | Wertaufhellender Vorgang / wertbegründender Vorgang (within balance sheet date) | IAS 10 / HGB | HGB: Wertaufhellungstheorie (events up to balance sheet preparation date) |
| Non-adjusting event | Wertbegründender Vorgang (after balance sheet date) | IAS 10 | |
| Going concern | Unternehmensfortführung / Going Concern | IAS 1 / § 252 HGB | Fundamental accounting assumption |
| Going concern assumption | Going-Concern-Prämisse | IDW PS 270 | |
| Going concern risk | Bestandsgefährdung / Bestandsrisiko | IDW PS 270 | |
| Liquidation | Liquidation / Abwicklung | HGB | |
| Insolvency | Insolvenz | InsO | |
| Material uncertainty | Wesentliche Unsicherheit | IAS 1 / IDW PS 270 | Disclosure required |

### Table 14: Consolidated Financial Statements (Konzernabschluss)

| English | German | Standard | Notes |
|---------|--------|----------|-------|
| Parent company | Mutterunternehmen / Konzernmutter | § 290 HGB | |
| Subsidiary | Tochterunternehmen | § 290 HGB | |
| Associate | Assoziiertes Unternehmen | IAS 28 / § 311 HGB | |
| Joint venture | Gemeinschaftsunternehmen | IFRS 11 / § 310 HGB | |
| Group | Konzern | § 290 HGB | |
| Consolidated financial statements | Konzernabschluss | § 290 HGB | |
| Consolidation | Konsolidierung | DRS 23-28 | |
| Full consolidation | Vollkonsolidierung | § 300 HGB | |
| Equity method | Equity-Methode / At-Equity-Bewertung | § 311 HGB | |
| Proportional consolidation | Quotenkonsolidierung | (Not permitted under IFRS 11) | |
| Consolidation of liabilities | Schuldenkonsolidierung | § 303 HGB | |
| Elimination of intercompany profits | Zwischenergebniseliminierung | § 304 HGB | |
| Gain on bargain purchase | Negativer Unterschiedsbetrag / Badwill | § 301 HGB | |
| Purchase Price Allocation (PPA) | Kaufpreisallokation | IFRS 3 | |
| Non-controlling interests | Nicht beherrschende Anteile (IFRS) / Anteile anderer Gesellschafter (HGB) | IFRS 10 / § 307 HGB | Terminology differs |
| Goodwill | Geschäfts- oder Firmenwert (GoF) | IFRS 3 / § 246 HGB | |

---

## Standard Conventions

### German Accounting Principles (GoB)

The Grundsätze ordnungsmäßiger Buchführung (GoB) are unwritten principles derived from commercial practice and HGB provisions. Key principles that affect translation:

1. **Bilanzklarheit (clarity):** Balance sheet must be clear and structured per § 266 HGB format
2. **Bilanzwahrheit (truth):** No false or misleading figures
3. **Vorsichtsprinzip (prudence):** Anticipate losses, do not anticipate gains (§ 252 Abs. 1 Nr. 4 HGB)
4. **Realisationsprinzip (realization):** Profits only when realized (§ 252 Abs. 1 Nr. 4 HGB)
5. **Imparitätsprinzip (impairment):** Recognize all expected losses immediately
6. **Stichtagsprinzip (cutoff):** Transactions allocated to proper period
7. **Wertaufhellungstheorie:** Consider events between balance sheet date and preparation date that clarify asset/liability values

### HGB Accounting Format Specifics

- **Bilanz — Kontoform (account form):** Assets left, liabilities right, per § 266 HGB
- **GuV — Gesamtkostenverfahren (GKV, nature of expense method):** Default for HGB, § 275 Abs. 2
- **GuV — Umsatzkostenverfahren (UKV, cost of sales method):** Optional, § 275 Abs. 3
- **Anhang (notes):** Must include all § 284-288 HGB disclosures
- **Lagebericht (management report):** Must follow DRS 20 — includes business performance, risks, outlook

### Currency Format Rules

- **EUR amounts in German accounting:** Always decimal comma: "EUR 1.234,56"
- **Foreign currencies:** ISO code after amount with space: "1.234,56 USD"
- **Translation footnote:** Always state the exchange rate used and the date: "Umrechnungskurs: 1 EUR = 1,05 USD (Stichtag: 31.12.2025)"
- **Thousands in tables:** Leading zeros not needed, but decimal alignment is critical
- **Multi-currency accounts:** Must show both original currency and EUR equivalent

### Annual Financial Statement Components

A full German Jahresabschluss (for corporations) consists of:
1. Bilanz (balance sheet, § 266 HGB)
2. Gewinn- und Verlustrechnung (income statement, § 275 HGB)
3. Anhang (notes, §§ 284-288 HGB)
4. Lagebericht (management report, § 289 HGB) — for medium and large companies
5. Kapitalflussrechnung (cash flow statement, DRS 21) — for large companies
6. Eigenkapitalveränderungsrechnung (statement of changes in equity, DRS 22) — for large companies
7. Segmentberichterstattung (segment report, DRS 28) — for capital market-oriented companies

### Zero Tolerance Rules for Financial Translation

The following are **never acceptable** in financial German translations:
1. Decimal POINT used instead of decimal COMMA in any financial figure
2. Comma used as thousand separator (e.g., "1,234" instead of "1.234")
3. "Rücklage" used when "Rückstellung" is meant (or vice versa)
4. "Aufwand" substituted for "Ertrag" (or vice versa) — opposite side
5. "Forderung" used when "Verbindlichkeit" is meant (asset vs. liability reversal)
6. Mistranslation of "Umsatzerlöse" as "Einnahmen" (revenue is not cash received)
7. Confusion between SKR 03 and SKR 04 account groups

---

## Standards Reference

| Standard / Source | Scope | Key Requirements |
|-------------------|-------|-----------------|
| HGB §§ 238-342e | Handelsrechtliche Rechnungslegung | Bookkeeping, inventory, financial statement format |
| HGB §§ 264-289 | Kapitalgesellschaften | Corporation-specific rules |
| GoB (Grundsätze ordnungsmäßiger Buchführung) | Accounting principles | Documentation, completeness, clarity, period accrual |
| DRS (Deutsche Rechnungslegungsstandards) | Accounting standards (DRSC) | Consolidated statements, cash flow, segment reporting |
| IDW PS (Prüfungsstandards) | Audit standards | Audit opinion format, audit procedures |
| EStG / KStG / GewStG / UStG | Tax law | Tax basis, rates, exemptions, deduction rules |
| AO (Abgabenordnung) | Tax procedure | Tax assessment, audit, appeals |
| IFRS / IAS (EU-endorsed) | International accounting | Official German translation per EU regulation |
| BilMoG (Bilanzrechtsmodernisierungsgesetz) | Accounting reform | HGB modernization (2009) |
| MicroBilG | Micro-entity accounting | Simplified balance sheet |
| PubG (Publizitätsgesetz) | Disclosure requirements | Publication of financial statements |
| DIN 5008 | Numerical formatting | Decimal comma, thousand separators, currency |
| DATEV Kontenrahmen SKR 03/04 | Chart of accounts | Standard account names |
| AktG (Aktiengesetz) | Stock corporation law | Corporate governance, Vorstand, Aufsichtsrat |
| GmbHG | GmbH law | GmbH-specific accounting |
| DCGK (Deutscher Corporate Governance Kodex) | Corporate governance | Governance statement format |
| WpHG (Wertpapierhandelsgesetz) | Securities trading | Capital market terminology |
| WpPG (Wertpapierprospektgesetz) | Securities prospectus | Prospectus terminology |

## Glossary (Financial German)

| English | German | Notes |
|---------|--------|-------|
| balance sheet | Bilanz | § 266 HGB format |
| profit and loss statement | Gewinn- und Verlustrechnung (GuV) | § 275 HGB |
| annual financial statements | Jahresabschluss | Bilanz + GuV + Anhang |
| consolidated financial statement | Konzernabschluss | § 290 HGB |
| management report | Lagebericht | § 289 HGB |
| fixed assets | Anlagevermögen | § 266 HGB |
| current assets | Umlaufvermögen | § 266 HGB |
| equity | Eigenkapital | § 266 HGB |
| liabilities (trade) | Verbindlichkeiten | § 266 HGB |
| provisions | Rückstellungen | § 249 HGB |
| revenue | Umsatzerlöse | Not "Einnahmen" |
| operating result | Betriebsergebnis | |
| financial result | Finanzergebnis | |
| net income | Jahresüberschuss | Positive result |
| net loss | Jahresfehlbetrag | Negative result |
| retained earnings | Gewinnvortrag | |
| appropriation of profit | Gewinnverwendung | |
| cash flow from operations | Cashflow aus laufender Geschäftstätigkeit | DRS 21 |
| depreciation | Abschreibung (planmäßig / außerplanmäßig) | |
| amortization | Abschreibung immaterieller Vermögenswerte | |
| impairment (tangible) | außerplanmäßige Abschreibung | |
| impairment (financial) | Wertminderung / Abschreibung auf Finanzanlagen | |
| consolidation | Konsolidierung | |
| goodwill | Geschäfts- oder Firmenwert (GoF) | |
| capital increase | Kapitalerhöhung | |
| capital reduction | Kapitalherabsetzung | |
| dividend | Dividende | |
| profit participation | Gewinnbeteiligung / Tantieme (management) | |
| subscription right | Bezugsrecht | |
| nominal value | Nennbetrag / Nennwert | |
| market value | Marktwert / Verkehrswert (HGB) / beizulegender Zeitwert (IFRS) | |
| fair value | beizulegender Zeitwert (IFRS) / Marktwert | |
| impairment test | Wertminderungstest / Impairment-Test | IFRS |
