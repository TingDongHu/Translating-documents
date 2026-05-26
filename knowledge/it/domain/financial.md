---
id: it/domain/financial
type: domain
target_lang: it
name: Financial Domain (Settore Finanziario)
description: Italian Financial domain terminology and translation rules
---

# Financial Domain (Settore Finanziario)

## Reader Model: Destinatario della Traduzione Finanziaria

### Primary Reader Profiles

| Profile | Description | Language Expectation | Review Lens |
|---------|-------------|---------------------|-------------|
| **Dottore commercialista** (Chartered Accountant) | Native Italian, prepares financial statements, tax returns. Deep knowledge of OIC (Organismo Italiano di Contabilita) and IAS/IFRS. | Requires precise accounting terminology matching OIC principles and Italian GAAP. Rejects calques from English accounting (e.g., "ricavo" not "revenoo"). | Cross-references balance sheet items with OIC guidance. Checks that financial statement classifications follow Italian format (Art. 2424 cc). Verifies footnote disclosures. |
| **CFO / Direttore finanziario** | Manages corporate finance, budgeting, reporting. Bilingual but needs Italian versions for board, Italian banks, and regulators. | Expects consistency in financial reporting terminology. Needs clear distinction between IFRS and Italian GAAP when both are referenced. | Verifies consolidation terminology, impairment tests, fair value hierarchy. Checks cash flow statement format (direct vs. indirect method). |
| **Analista finanziario** (Financial Analyst) | Reads annual reports, earnings releases, analyst reports. | Requires correct translation of financial ratios, performance metrics, and market terminology. | Scans for key performance indicators, EBITDA, adjusted earnings. Verifies that Italian terms for non-GAAP metrics are clearly defined. |
| **Revisore contabile / Auditor** | External or internal auditor reviewing financial statements. | Demands exact correspondence between source and target for audit-relevant assertions. Footnotes must be scrupulously accurate. | Checks consistency between financial statement line items and footnote references. Verifies that audit opinion terminology matches Italian auditing standards. |
| **Responsabile amministrazione** (Administration Manager) | Prepares statutory accounts, manages day-to-day accounting. | Needs operational accounting terminology: journal entries, account reconciliation, closing procedures. | Verifies transaction descriptions, account names, posting logic in translated accounting procedures. |

### Reading Scenarios and Document Types

| Document Type | Typical Length | Urgency | Key Translation Challenge |
|--------------|---------------|---------|-------------------------|
| Bilancio d'esercizio (Financial Statements) | 30-200 pp. | High | Balance sheet format (Art. 2424 cc), income statement (Art. 2425 cc), OIC vs. IFRS classifications |
| Relazione sulla gestione (Management Report) | 10-50 pp. | High | Narrative reporting; mix of financial and non-financial KPIs; "fair review" language |
| Relazione di revisione (Audit Report) | 5-15 pp. | Very High | Standardized audit opinion language; verbatim accuracy expected |
| Prospetto informativo (Prospectus) | 100-500 pp. | Very High | Regulatory language (CONSOB), risk factors, legal disclaimers |
| Contratto di finanziamento (Loan Agreement) | 20-100 pp. | High | Financial covenants, representations, events of default, interest calculation |
| Report di analisi / Equity research | 10-50 pp. | Medium | Valuation terminology, DCF, multiples, target price |
| Comunicato stampa finanziario (Press Release) | 2-5 pp. | Very High | Earnings announcements; market-sensitive information; precise numbers |
| Verbale del CDA / Board minutes | 5-20 pp. | Medium | Resolutions, voting, formal register, approval of financial statements |
| Bilancio consolidato (Consolidated FS) | 50-300 pp. | High | Consolidation scope, elimination entries, goodwill, NCI terminology |
| Nota integrativa (Notes to FS) | 20-100 pp. | High | Detailed disclosures; accounting policy descriptions; cross-references to OIC or IFRS |

### The IFRS vs. Italian GAAP Challenge

Italian companies may report under:
- **Italian GAAP (OIC)**: Required for most non-listed Italian companies. Based on Codice Civile (Art. 2423-2435-ter) and OIC standards. Very prescriptive format.
- **IFRS (IAS/IFRS)**: Required for listed companies (EU Regulation 1606/2002) and optional for some others. More principles-based.

The translator must know which framework the document follows, because the same concept may have different Italian names under each framework:

| Concept | OIC (Italian GAAP) | IFRS (in Italian) |
|---------|-------------------|-------------------|
| Financial statements | Bilancio d'esercizio | Prospetti contabili / Bilancio IFRS |
| Income statement | Conto economico | Prospetto di conto economico complessivo |
| Other comprehensive income | (Not used in OIC) | Altre componenti di conto economico complessivo (OCI) |
| Cash flow statement | Rendiconto finanziario | Rendiconto finanziario |
| Notes | Nota integrativa | Note al bilancio |
| Property, plant & equipment | Immobilizzazioni materiali | Immobilizzazioni materiali (same) |
| Intangible assets | Immobilizzazioni immateriali | Attivita immateriali / immobilizzazioni immateriali |
| Impairment | Riduzione di valore / Svalutazione | Perdita per riduzione di valore (Impairment) |
| Goodwill | Avviamento | Avviamento (same) |
| Provision | Accantonamento / Fondo | Accantonamento / Fondo |

---

## Decision Framework: Translation Tables

### Table 1: Balance Sheet (Stato Patrimoniale) -- Assets

| English (IFRS) | Italian (OIC / Codice Civile) | Art. 2424 cc Reference | Notes |
|---------------|------------------------------|----------------------|-------|
| Non-current assets | Attivo immobilizzato | Art. 2424, Attivo, Sez. B | "Immobilizzazioni" = fixed assets. |
| Property, plant and equipment | Immobilizzazioni materiali | B.II | Includes land, buildings, plant, machinery, equipment. |
| Intangible assets | Immobilizzazioni immateriali | B.I | Includes goodwill, development costs, patents, licenses. |
| Goodwill | Avviamento | B.I.5 | Capitalized only if acquired for consideration. |
| Investments in subsidiaries | Partecipazioni in imprese controllate | B.III.1 | "Controllate" = subsidiaries. "Collegate" = associates. |
| Investments in associates | Partecipazioni in imprese collegate | B.III.2 | Significant influence (20-50%). |
| Deferred tax assets | Attivita per imposte anticipate | C.II.4-bis / B.II (OIC) | "Imposte anticipate" = deferred tax assets (DTAs). |
| Current assets | Attivo circolante | C | "Circolante" = current/working capital. |
| Inventories | Rimanenze | C.I | Raw materials, WIP, finished goods. |
| Trade receivables | Crediti verso clienti | C.II.1 | "Crediti commerciali" also used. |
| Cash and cash equivalents | Disponibilita liquide | C.IV | "Cassa e banche" in older terminology. |
| Accruals and deferrals | Ratei e risconti | D | "Ratei attivi" = accrued income. "Risconti attivi" = prepaid expenses. |

### Table 2: Balance Sheet (Stato Patrimoniale) -- Liabilities and Equity

| English (IFRS) | Italian (OIC / Codice Civile) | Art. 2424 cc Reference | Notes |
|---------------|------------------------------|----------------------|-------|
| Equity | Patrimonio netto | A | "Capitale proprio" is also used. |
| Share capital | Capitale sociale | A.I | "Capitale" not "capitale azionario" (anglicism). |
| Share premium reserve | Riserva sovrapprezzo azioni | A.II | Premium above par value. |
| Legal reserve | Riserva legale | A.IV | Mandatory reserve: 5% of profits until 20% of capital. |
| Retained earnings | Utili portati a nuovo / Riserva utili | A.VII | "Portati a nuovo" = carried forward. |
| Profit (loss) for the year | Utile (Perdita) dell'esercizio | A.IX | "Esercizio" = financial year. |
| Non-current liabilities | Passivita non correnti | D | "Fondi" and "Debiti" with maturity > 12 months. |
| Provisions for risks and charges | Fondi per rischi e oneri | B | "Fondo" = provision. Distinguished from "Trattamento di Fine Rapporto" (TFR). |
| Employee termination benefits | Trattamento di Fine Rapporto (TFR) | C | Italian-specific: severance/end-of-service benefit. |
| Trade payables | Debiti verso fornitori | D.7 | "Fornitori" = suppliers. |
| Financial liabilities (bank debt) | Debiti verso banche | D.4 | "Debiti finanziari" is also used. |
| Current liabilities | Passivita correnti | D (portion < 12 months) | Separated by maturity. |
| Deferred tax liabilities | Passivita per imposte differite | D.13 | "Fondo imposte differite" also used. |

### Table 3: Income Statement (Conto Economico)

| English (IFRS) | Italian (OIC / Codice Civile) | Art. 2425 cc Reference | Notes |
|---------------|------------------------------|----------------------|-------|
| Revenue | Ricavi delle vendite e delle prestazioni | A.1 | "Ricavi" (not "revenoo" or "faturato" -- "fatturato" is informal). |
| Cost of goods sold | Costi per materie prime, sussidiarie, di consumo | B.6 | "Costo del venduto" is a management accounting term, not statutory. |
| Cost of services | Costi per servizi | B.7 | External services: consulting, utilities, maintenance. |
| Personnel costs | Costi per il personale | B.9 | Salaries, social security, TFR, pension costs. |
| Depreciation and amortization | Ammortamenti e svalutazioni | B.10 | "Ammortamento" = systematic allocation. "Svalutazione" = impairment. |
| Other operating income | Altri ricavi e proventi | A.5 | Non-core income: gains on disposals, grants. |
| Financial income | Proventi finanziari | C.16 | Interest income, dividends, foreign exchange gains. |
| Financial expenses | Oneri finanziari | C.17 | Interest expense, foreign exchange losses. |
| Income tax expense | Imposte sul reddito dell'esercizio | E.20 | Current and deferred taxes. |
| Profit (loss) from continuing operations | Risultato prima delle imposte (EBT) | D.18 | "Risultato ante imposte" also used. |
| Net profit (loss) | Utile (Perdita) dell'esercizio | E.23 | Final bottom-line result. |
| EBITDA | EBITDA / Margine operativo lordo (MOL) | Not a statutory line | "MOL" = Margine Operativo Lordo. EBITDA is also used in Italian financial reporting. |
| EBIT | EBIT / Risultato operativo | Not a statutory line | "Risultato operativo" or "Reddito operativo". |

### Table 4: Cash Flow Statement (Rendicontazione Finanziaria)

| English (IFRS) | Italian (OIC 10) | Notes |
|---------------|------------------|-------|
| Cash flow statement | Rendiconto finanziario | Required for all companies exceeding certain size thresholds (OIC 10). |
| Cash flows from operating activities | Flussi finanziari da attivita operativa | "Flussi finanziari" = cash flows. "Attivita operativa" = operating activities. |
| Cash flows from investing activities | Flussi finanziari da attivita di investimento | Purchase/sale of property, equipment, intangible assets, investments. |
| Cash flows from financing activities | Flussi finanziari da attivita di finanziamento | Borrowings, repayments, equity transactions, dividends. |
| Net cash flow | Flusso finanziario netto | Net increase/(decrease) in cash. |
| Cash and cash equivalents at beginning of period | Disponibilita liquide all'inizio dell'esercizio | Opening balance. |
| Cash and cash equivalents at end of period | Disponibilita liquide alla fine dell'esercizio | Closing balance. |
| Indirect method | Metodo indiretto | Most common in Italy: starts with net profit, adjusts for non-cash items. |
| Direct method | Metodo diretto | Less common. Shows actual cash receipts and payments. |
| Change in working capital | Variazione del capitale circolante netto | Key adjustment in indirect method. |

### Table 5: Key Financial Ratios and Metrics

| English (EN) | Italian (IT) | Formula | Notes |
|-------------|-------------|---------|-------|
| Return on Equity (ROE) | ROE / Rendimento del capitale proprio | Utile netto / Patrimonio netto | Key profitability metric for shareholders. |
| Return on Investment (ROI) | ROI / Rendimento dell'investimento | Reddito operativo / Capitale investito | Operating profitability. |
| Return on Sales (ROS) | ROS / Redditivita delle vendite | Reddito operativo / Ricavi | Operating margin. "Margine operativo" also used. |
| Debt-to-Equity ratio | Rapporto di indebitamento / Leverage | Debiti finanziari / Patrimonio netto | Gearing ratio. "Leverage" is also used. |
| Current ratio | Indice di liquidita corrente | Attivo circolante / Passivita correnti | Liquidity measure. |
| Quick ratio | Indice di liquidita primaria (acid test) | (Attivo circolante - Rimanenze) / Passivita correnti | Stricter liquidity measure. |
| Net Financial Position (NFP) | Posizione Finanziaria Netta (PFN) | Debiti finanziari - Disponibilita liquide - Crediti finanziari correnti | Critical metric in M&A. Also "Indebitamento Finanziario Netto". |
| Earnings Before Interest, Taxes, Depreciation, Amortization | EBITDA / Margine Operativo Lordo (MOL) | Risultato operativo + Ammortamenti + Svalutazioni | Note: MOL sometimes includes other items. Always check the definition. |
| Earnings per Share (EPS) | Utile per azione (EPS) | Utile netto / Numero azioni | "EPS" is more common than the Italian translation. |
| Dividend per share | Dividendo per azione | Dividendo / Numero azioni | "Dividendo unitario" also used. |

### Table 6: Financial Statement Footnotes (Nota Integrativa)

| English (IFRS) | Italian (OIC) | Notes |
|---------------|--------------|-------|
| Accounting policies | Principi contabili / Criteri di valutazione | "Criteri di valutazione" is the standard OIC heading for measurement policies. |
| Significant accounting estimates | Stime contabili significative | Required disclosure about estimation uncertainty. |
| Going concern assumption | Continuita aziendale / Going concern | "Presupposto della continuita aziendale" is the full phrase. |
| First-time adoption of IFRS | Prima adozione dei principi contabili internazionali | IFRS 1. |
| Segment reporting | Informativa di settore | IFRS 8 / OIC 6 (for Italian GAAP). |
| Related party transactions | Operazioni con parti correlate | "Parti correlate" = related parties. |
| Contingent liabilities | Passivita potenziali | Possible obligations not recognized. |
| Commitments | Impegni | Contractual obligations. |
| Subsequent events | Fatti intervenuti dopo la chiusura dell'esercizio | Events after the reporting period. |
| Business combinations | Aggregazioni aziendali | IFRS 3 / OIC 4. |
| Discontinued operations | Attivita cessate / Attivita non correnti possedute per la vendita | IFRS 5. |

### Table 7: Audit Opinion Terminology

| English (ISA) | Italian (SA Italia / Principi di Revisione) | Notes |
|---------------|---------------------------------------------|-------|
| Audit opinion | Giudizio / Parere | "Giudizio" is the official term in Italian auditing standards. |
| Unqualified opinion | Giudizio senza modifica / Giudizio positivo | Clean audit opinion. |
| Qualified opinion | Giudizio con modifica / Giudizio con rilievi | "Rilievi" = qualifications. |
| Adverse opinion | Giudizio negativo | Material, pervasive misstatements. |
| Disclaimer of opinion | Dichiarazione di impossibilita di esprimere un giudizio | Scope limitation. |
| True and fair view | Rappresentazione veritiera e corretta | The fundamental audit concept. Derived from Art. 2423 cc "deve rappresentare in modo veritiero e corretto". |
| Materiality | Significativita / Rilevanza | "Principio della rilevanza" = materiality principle. |
| Audit evidence | Elementi probativi | Evidence gathered during audit. |
| Internal controls | Controllo interno | "Sistema di controllo interno" = internal control system. |
| Key Audit Matters (KAM) | Questioni chiave della revisione contabile | ISA 701. |
| Going concern | Continuita aziendale | Auditor evaluates whether going concern assumption is appropriate. |
| Emphasis of matter | Richiamo di attenzione | A paragraph drawing attention to a matter without modifying the opinion. |
| Other matter | Altri aspetti | A paragraph addressing matters other than those presented in the FS. |

### Table 8: Corporate Finance Terminology

| English (EN) | Italian (IT) | Notes |
|-------------|-------------|-------|
| Merger | Fusione | "Fusione per unione" = consolidation merger. "Fusione per incorporazione" = merger by absorption. |
| Demerger / Spin-off | Scissione | "Scissione totale" = full demerger. "Scissione parziale" = partial demerger. |
| Acquisition | Acquisizione | "Acquisizione" is used. "Takeover" = scalata or OPA. |
| Purchase price allocation | Allocazione del prezzo di acquisto (Purchase price allocation / PPA) | IFRS 3 requirement. |
| Due diligence | Due diligence / Verifica di conformita | "Due diligence" is standard Italian financial jargon. |
| Valuation | Valutazione | "Valutazione d'azienda" = business valuation. |
| Discounted Cash Flow (DCF) | Discounted Cash Flow (DCF) / Flusso di cassa attualizzato | "DCF" is commonly used. "Attualizzato" = discounted. |
| Net Present Value (NPV) | Valore Attuale Netto (VAN) | "VAN" is the standard Italian abbreviation. |
| Internal Rate of Return (IRR) | Tasso Interno di Rendimento (TIR) | "TIR" is standard. |
| Enterprise Value / Equity Value | Enterprise Value (EV) / Valore dell'impresa; Equity Value / Valore del capitale netto | "EV" is very common in Italian financial reporting. |
| Market capitalization | Capitalizzazione di mercato | "Market cap" is also used. |
| Initial Public Offering (IPO) | Offerta Pubblica Iniziale (IPO) | "IPO" is very common. "Quotazione in Borsa" = stock exchange listing. |
| Rights issue | Aumento di capitale con diritto di opzione | "Aumento di capitale" = capital increase. |

### Table 9: Banking and Lending Terminology

| English (EN) | Italian (IT) | Notes |
|-------------|-------------|-------|
| Loan agreement | Contratto di finanziamento | "Mutuo" = mortgage loan (secured by property). "Finanziamento" = general loan. |
| Borrower / Lender | Mutuatario / Mutuante | Or "Finanziato / Finanziatore". |
| Principal | Capitale | "Quota capitale" = principal repayment. |
| Interest rate | Tasso di interesse | "Tasso fisso" = fixed rate. "Tasso variabile" = floating rate. |
| Base rate | Tasso base / Euribor | EURIBOR is the most common base rate for euro loans. |
| Spread | Spread / Margine | The margin above the base rate. |
| Margin | Margine | Same as spread in lending context. |
| Arrangement fee | Commissione di strutturazione | Upfront fee. |
| Commitment fee | Commissione di impegno | Fee on undrawn amounts. |
| Covenant | Covenant / Impegno finanziario | Often kept in English. "Impegno" is used in Italian contracts. |
| Event of default | Evento di risoluzione / Causa di risoluzione anticipata | "Risoluzione anticipata" = acceleration/termination. |
| Cross-default | Clausola di cross-default / Effetto domino | Where default under one agreement triggers default under another. |
| Negative pledge | Clausola di negative pledge | Covenant not to create security interests in favor of others. |
| Pari passu | Clausola di pari passu | Equal ranking with other unsecured creditors. |
| Acceleration clause | Clausola di decadenza dal beneficio del termine | Right to demand immediate repayment. |

### Table 10: Regulatory and Compliance Terminology (CONSOB, Banca d'Italia)

| English (EN) | Italian (IT) | Regulator | Notes |
|-------------|-------------|-----------|-------|
| Listed company | Societa quotata | CONSOB / Borsa Italiana | "Quotata" = listed. |
| Issuer | Emittente | CONSOB | Entity issuing financial instruments. |
| Prospectus | Prospetto informativo | CONSOB (Reg. 11971/1999) | Must be approved by CONSOB. |
| Inside information | Informazione privilegiata | CONSOB / MAR | Market Abuse Regulation. "Privilegiata" = price-sensitive. |
| Market abuse | Abuso di mercato | CONSOB | Covers insider dealing and market manipulation. |
| Insider trading | Insider trading / Abuso di informazioni privilegiate | CONSOB | "Insider trading" is used in Italian. |
| Related party | Parte correlata | CONSOB (Reg. 17221/2010) | Specific rules for transactions with related parties. |
| Corporate governance | Corporate governance / Governo societario | CONSOB / Codice di Corporate Governance | "Governo societario" is the Italian term. "Corporate governance" is also used. |
| Financial reporting | Informativa finanziaria | CONSOB / Banca d'Italia | Periodic reporting obligations. |
| Significant holding / Stake | Partecipazione rilevante | CONSOB | Threshold notification requirements. |
| Tender offer | Offerta Pubblica di Acquisto (OPA) | CONSOB | Mandatory bid rules. "OPA obbligatoria" = mandatory tender offer. |
| Squeeze-out | Diritto di acquisto / Squeeze-out | CONSOB (Art. 111 TUF) | Right to buy out minority shareholders. |

### Table 11: Budgeting and Forecasting Terminology

| English (EN) | Italian (IT) | Notes |
|-------------|-------------|-------|
| Budget | Budget | "Budget" is used in Italian business. "Preventivo" is for quotations. |
| Forecast | Previsione / Forecast | "Previsione" is the general term. "Forecast" is also used in finance. |
| Actual | Consuntivo | "Dati consuntivi" = actual figures. |
| Variance | Scostamento / Varianza | "Scostamento" = deviation from budget. |
| Variance analysis | Analisi degli scostamenti | Key management accounting tool. |
| Plan | Piano / Pianificazione | "Piano industriale" = business plan. "Piano triennale" = three-year plan. |
| Rolling forecast | Rolling forecast / Previsione scorrevole | "Scorrevole" = rolling/sliding. |
| Zero-based budgeting | Budget a base zero (ZBB) | Budgeting method where all expenses must be justified. |
| Capital expenditure (CAPEX) | CAPEX / Spese in conto capitale / Investimenti | "Investimenti" is the common Italian term. "CAPEX" is used. |
| Operating expenditure (OPEX) | OPEX / Costi operativi | "OPEX" is common. "Costi operativi" is the Italian term. |
| Profit center | Centro di profitto | Responsibility center measured by profit. |
| Cost center | Centro di costo | Responsibility center measured by costs. |

### Table 12: Tax Terminology

| English (EN) | Italian (IT) | Reference | Notes |
|-------------|-------------|-----------|-------|
| Corporate income tax | Imposta sul Reddito delle Societa (IRES) | D.P.R. 917/1986 (TUIR) | 24% rate (as of 2025). |
| Regional business tax | Imposta Regionale sulle Attivita Produttive (IRAP) | D.Lgs. 446/1997 | 3.9% standard rate (varies by region). |
| Value Added Tax | Imposta sul Valore Aggiunto (IVA) | D.P.R. 633/1972 | Standard rate 22%. |
| Withholding tax | Ritenuta alla fonte / Ritenuta d'acconto | D.P.R. 600/1973 | Applied to dividends, interest, professional fees. |
| Tax consolidation | Consolidato fiscale | TUIR Art. 117-129 | "Tassazione di gruppo" = group taxation. |
| Transfer pricing | Prezzi di trasferimento | TUIR Art. 110 para 7 | Arm's length principle. |
| Tax avoidance | Elusione fiscale | Abuse of law (Art. 10-bis L. 212/2000) | "Elusione" = avoidance (legal but contrary to purpose). |
| Tax evasion | Evasione fiscale | Criminal offense | "Evasione" = illegal evasion. |
| Fiscal representative | Rappresentante fiscale | For non-resident entities with VAT obligations in Italy. |
| VAT group | Gruppo IVA | D.Lgs. 192/2021 | Optional VAT grouping. |
| Cross-border transaction | Operazione transfrontaliera | Cross-border M&A, financing, supply. |
| Permanent establishment | Stabile organizzazione | Art. 162 TUIR | Tax presence in a jurisdiction. |

### Table 13: Corporate Governance Terminology

| English (EN) | Italian (IT) | Notes |
|-------------|-------------|-------|
| Board of Directors | Consiglio di Amministrazione (CdA) | May also be "Collegio Sindacale" for the supervisory board in the dual system. |
| Chairman | Presidente del Consiglio di Amministrazione | Chairman of the Board. |
| Chief Executive Officer (CEO) | Amministratore Delegato (AD) | "CEO" is also used in Italian companies. |
| Chief Financial Officer (CFO) | Direttore Finanziario / CFO | "CFO" is common. "Direttore Amministrazione, Finanza e Controllo" is the full title. |
| Statutory auditor | Sindaco | Member of the "Collegio Sindacale" (board of statutory auditors). |
| Independent director | Amministratore indipendente | Independence criteria per Codice di Corporate Governance. |
| Non-executive director | Amministratore non esecutivo | Director without management responsibilities. |
| Supervisory board | Consiglio di Sorveglianza | In the dual governance system. |
| Management board | Consiglio di Gestione | In the dual governance system. |
| Shareholders' meeting | Assemblea dei soci / Assemblea degli azionisti | "Assemblea ordinaria" = ordinary. "Assemblea straordinaria" = extraordinary. |
| Resolution | Delibera | "Delibera del CdA" = board resolution. |
| Minutes of meeting | Verbale | "Verbale dell'assemblea" = meeting minutes. |

### Table 14: Currency and Numerical Conventions in Financial Contexts

| English Format | Italian Format | Rule |
|---------------|---------------|------|
| EUR 1,250,000.00 | EUR 1.250.000,00 | Thousands separator = period; decimal = comma. "EUR" precedes the amount. |
| $50 million | 50 milioni di USD | Currency symbol replaced with ISO code in running text. |
| 10 bps (basis points) | 10 pb (punti base) | "pb" = punti base. 100 pb = 1%. |
| 5.25% interest rate | Tasso di interesse del 5,25% | Comma for decimal. |
| EPS of 2.5x | EPS di 2,5x | EPS remains in English; comma for decimal. |
| 3:1 ratio | Rapporto di 3:1 | Ratio format is same. |
| 1.5 million shares | 1,5 milioni di azioni | Comma for decimal; "milioni di azioni". |
| Fiscal year 2025 | Esercizio 2025 / FY 2025 | "Esercizio" not "anno fiscale" for corporate financial year. |
| Year ended December 31, 2025 | Esercizio chiuso al 31 dicembre 2025 | "Chiuso al" + date. |
| As of December 31, 2025 | Al 31 dicembre 2025 | "Al" for reference date. |

### Table 15: Management Report Language (Relazione sulla Gestione)

| English (EN) | Italian (IT) | Notes |
|-------------|-------------|-------|
| Performance during the year / Business review | Andamento della gestione | Art. 2428 cc requires a "fair review" (analisi fedele, equilibrata ed esauriente). |
| Operating performance | Andamento operativo | |
| Significant events after year-end | Fatti di rilievo intervenuti dopo la chiusura dell'esercizio | |
| Outlook / Business outlook | Evoluzione prevedibile della gestione | Forward-looking information. |
| Risk management | Gestione dei rischi | "Risk management framework" is also used. |
| Principal risks and uncertainties | Principali rischi e incertezze | |
| Research and development activities | Attivita di ricerca e sviluppo | |
| Treasury shares / Own shares | Azioni proprie | Disclosure required by Art. 2428 cc. |
| Relationships with subsidiaries | Rapporti con imprese controllate | |
| Alternative performance measures (APM) | Misure di Performance Alternative (MPA) | ESMA guidelines on APMs are followed in Italy. |

---

## Standards and Conventions

### Primary Accounting Standards Bodies and References

| Body / Standard | Full Name | Relevance |
|----------------|-----------|-----------|
| **OIC** | Organismo Italiano di Contabilita | Italian accounting standard-setter. Publishes OIC principles (OIC 1 through OIC 34) covering Italian GAAP. Translators must reference OIC terminology for non-IFRS financial statements. |
| **IASB** | International Accounting Standards Board | Sets IFRS, which are translated into Italian by OIC. The official Italian translation of IFRS is published in the EU Official Journal. |
| **CONSOB** | Commissione Nazionale per le Societa e la Borsa | Italian securities regulator. Regulates listed companies, prospectuses, market abuse. |
| **Banca d'Italia** | Banca d'Italia | Central bank; regulates banks and financial intermediaries. |
| **CNDCEC** | Consiglio Nazionale dei Dottori Commercialisti e degli Esperti Contabili | Professional body for accountants. Publishes interpretation guidance. |
| **Codice Civile** | Regio Decreto 16 marzo 1942, n. 262 | Art. 2423-2435-ter contain the legal framework for financial statements. |
| **TUF** | D.Lgs. 58/1998 (Testo Unico della Finanza) | Consolidated Law on Finance -- governs listed companies, markets, intermediaries. |

### Italian Financial Reporting Conventions

| Convention | Rule | Example |
|------------|------|---------|
| Balance sheet format | Fixed assets before current assets (Art. 2424) | Immobilizzazioni -> Attivo circolante -> Ratei e risconti. |
| Income statement format | Cost-by-nature (Art. 2425) | Italy uses mainly cost-by-nature (B.6, B.7, B.8, B.9), not cost-by-function. Cost of sales format is only used in IFRS by some companies. |
| Currency rounding | Bilanci in unita di euro (no decimals) | Many Italian companies round to the nearest euro in statutory accounts. |
| Sign conventions | Parentheses for negative amounts (-10) | Parentheses are used. Red ink is traditional but less common in digital formats. |
| Comparative periods | Current year and prior year required | Two-year comparison is standard in statutory FS. |
| True and fair view override | Deroga obbligatoria (Art. 2423, comma 4) | If compliance would mislead, the company must depart from the rule. |
| Audit threshold | Limits based on Art. 2435-bis (bilancio abbreviato) | Small companies may use simplified formats. |

### Key OIC Principles (Italian GAAP)

| OIC Standard | Topic | Relevance to Translation |
|-------------|-------|------------------------|
| OIC 1 | Principi contabili generali | Framework: going concern, accruals, consistency, prudence, substance over form (prevalenza della sostanza sulla forma). |
| OIC 10 | Rendiconto finanziario | Direct vs. indirect method format. |
| OIC 11 | Bilancio d'esercizio: finalita e postulati | Purpose and postulates of financial statements. |
| OIC 12 | Composizione e schemi del bilancio | Format and structure of FS. Critical for correct line item translation. |
| OIC 13 | Rimanenze | Inventory valuation (LCM -- lower of cost or market). |
| OIC 14 | Disponibilita liquide | Cash and cash equivalents. |
| OIC 15 | Crediti | Trade receivables: measurement, impairment. |
| OIC 16 | Immobilizzazioni materiali | Property, plant and equipment: capitalization, depreciation, impairment. |
| OIC 17 | Bilancio consolidato | Consolidated financial statements. |
| OIC 18 | Ratei e risconti | Accruals and deferrals. |
| OIC 19 | Debiti | Payables: classification, measurement. |
| OIC 20 | Immobilizzazioni immateriali | Intangible assets: recognition, amortization. |
| OIC 21 | Partecipazioni | Investments: equity method vs. cost. |
| OIC 23 | Fondo TFR | Employee termination benefits. |
| OIC 24 | Imposte sul reddito | Income taxes: current, deferred, provisions. |
| OIC 31 | Fondi per rischi e oneri | Provisions for risks and charges. |
| OIC 32 | Operazioni con parti correlate | Related party transactions. |

### Verification Checklist for Financial Translations

1. **Framework identification**: Confirm whether the source document uses IFRS or Italian GAAP (OIC). Adjust terminology accordingly.
2. **Balance sheet classification**: Assets and liabilities classified per Art. 2424 cc categories (Attivo immobilizzato / Attivo circolante / Patrimonio netto / Fondi / Debiti / Ratei e risconti).
3. **Income statement format**: Cost-by-nature classification confirmed. "Ricavi" for revenue (not "fatturato" in formal FS). "Costi per materie prime" not "costo del venduto" unless IFRS by-function.
4. **OIC terminology**: Every accounting term traceable to the relevant OIC principle.
5. **Numerical accuracy**: All amounts, percentages, and ratios correctly formatted with Italian decimal/thousands conventions.
6. **Rounding consistency**: Rounding method (unita di euro / migliaia di euro) consistent throughout the document.
7. **Footnote cross-references**: All cross-references between financial statement line items and note disclosures verified.
8. **Audit opinion language**: Standard ISA Italia opinion terminology used ("giudizio senza modifica", "giudizio con rilievi", etc.).
9. **Non-GAAP / APM measures**: Clear definitions and Italian regulatory references for alternative performance measures.
10. **Acronym consistency**: IFRS, OIC, TUF, CONSOB, CdA, AD, DCF, VAN, TIR, OPA, etc. defined on first use at document level.
