---
id: fr/domain/financial
type: domain
target_lang: fr
name: Documents financiers (francais)
description: Terminologie et regles pour les documents financiers traduits en francais
term_mappings:
  "balance sheet": "bilan"
  "income statement": "compte de resultat"
  "cash flow statement": "tableau des flux de tresorerie"
  "revenue": "chiffre d'affaires"
  "net income": "resultat net"
  "gross profit": "marge brute"
  "operating profit": "resultat d'exploitation"
  "EBITDA": "EBE (excedent brut d'exploitation)"
  "total assets": "total actif"
  "total liabilities": "total passif"
  "equity": "capitaux propres"
  "share capital": "capital social"
  "retained earnings": "report a nouveau"
  "depreciation": "amortissements"
  "provisions": "provisions"
  "accounts receivable": "creances clients"
  "accounts payable": "dettes fournisseurs"
  "working capital": "fonds de roulement"
  "cash": "tresorerie"
  "VAT": "TVA"
  "tax return": "declaration fiscale"
  "tax credit": "credit d'impot"
  "audit": "audit"
  "auditor": "commissaire aux comptes"
  "invoice": "facture"
  "purchase order": "bon de commande"
  "quotation": "devis"
  "due date": "echeance"
  "bank transfer": "virement bancaire"
  "IFRS": "IFRS (normes internationales)"
  "GAAP": "PCG (Plan Comptable General)"
  "goodwill": "ecart d'acquisition"
  "impairment": "depreciation"
  "fair value": "juste valeur"
  "fixed assets": "immobilisations"
  "current assets": "actif circulant"
  "non-current assets": "actif non courant"
  "intangible assets": "immobilisations incorporelles"
  "tangible assets": "immobilisations corporelles"
  "financial assets": "immobilisations financieres"
  "inventory": "stocks"
  "trade receivables": "creances d'exploitation"
  "cash equivalents": "equivalents de tresorerie"
  "trade payables": "dettes d'exploitation"
  "accruals": "comptes de regularisation"
  "deferred income": "produits constates d'avance"
  "prepaid expenses": "charges constatees d'avance"
  "accrued expenses": "charges a payer"
  "accrued income": "produits a recevoir"
  "share premium": "prime d'emission"
  "legal reserve": "reserve legale"
  "statutory reserve": "reserves statutaires"
  "free reserves": "reserves libres"
  "dividends": "dividendes"
  "interim dividend": "acompte sur dividende"
  "treasury shares": "actions propres"
  "earnings per share": "resultat par action"
  "diluted earnings per share": "resultat dilue par action"
  "book value": "valeur comptable"
  "market value": "valeur de marche"
  "cost of goods sold": "cout des marchandises vendues"
  "selling expenses": "frais de vente"
  "administrative expenses": "frais administratifs"
  "operating expenses": "charges d'exploitation"
  "financial expenses": "charges financieres"
  "exceptional items": "elements exceptionnels"
  "income tax": "impot sur les benefices"
  "deferred tax": "impot differe"
  "tax base": "base imposable"
  "taxable income": "resultat fiscal"
  "tax loss carryforward": "report en avant des deficits"
  "withholding tax": "retenue a la source"
  "corporate income tax": "impot sur les societes (IS)"
  "value added tax": "taxe sur la valeur ajoutee (TVA)"
  "transfer pricing": "prix de transfert"
  "thin capitalization": "sous-capitalisation"
  "consolidation": "consolidation"
  "pooling of interests": "mise en commun d'interets"
  "acquisition method": "methode d'acquisition"
  "equity method": "mise en equivalence"
  "proportionate consolidation": "integration proportionnelle"
  "full consolidation": "integration globale"
  "non-controlling interests": "interets ne donnant pas le controle"
  "associate": "entreprise associee"
  "joint venture": "coentreprise"
  "subsidiary": "filiale"
  "parent company": "societe mere"
  "group": "groupe"
  "financial year": "exercice comptable"
  "accounting period": "periode comptable"
  "closing date": "date de cloture"
  "opening balance": "solde d'ouverture"
  "closing balance": "solde de cloture"
  "trial balance": "balance generale"
  "general ledger": "grand livre"
  "journal entry": "ecriture comptable"
  "double entry": "partie double"
  "debit": "debit"
  "credit": "credit"
  "chart of accounts": "plan comptable"
  "account number": "numero de compte"
  "auxiliary ledger": "compte auxiliaire"
  "reconciliation": "rapprochement"
  "bank reconciliation": "rapprochement bancaire"
  "amortization": "amortissement"
  "depreciation period": "duree d'amortissement"
  "straight-line depreciation": "amortissement lineaire"
  "declining balance depreciation": "amortissement degressif"
  "impairment loss": "perte de valeur"
  "reversal of impairment": "reprise de depreciation"
  "provision for bad debts": "provision pour creances douteuses"
  "capital increase": "augmentation de capital"
  "capital reduction": "reduction de capital"
  "share buyback": "rachat d'actions"
  "merger": "fusion"
  "acquisition": "acquisition"
  "demerger": "scission"
  "liquidation": "liquidation"
  "insolvency": "insolvabilite"
  "bankruptcy": "faillite"
  "receivership": "redressement judiciaire"
  "compulsory liquidation": "liquidation judiciaire"
  "debt restructuring": "restructuration de dette"
  "refinancing": "refinancement"
  "covenant": "engagement / clause"
  "default": "defaut"
  "cross-default": "defaut croise"
  "collateral": "garantie / surete"
  "pledge": "nantissement"
  "mortgage": "hypotheque"
  "guarantee": "cautionnement"

# =============================================================================
# MODELE DE LECTURE / READER MODEL
# =============================================================================

Ce modele decrit comment lire et interpreter un document financier source en
vue de sa traduction en francais. Il identifie les differences entre les
normes PCG et IFRS, les conventions numeriques et les pieges terminologiques.

## 1. Identification du type de document financier

| Type de document                 | Marqueurs source                        | Registre            |
|----------------------------------|-----------------------------------------|----------------------|
| Bilan                            | "Assets" "Liabilities" "Equity"         | Comptable            |
| Compte de resultat               | "Revenue" "Operating expenses" "Net income" | Comptable        |
| Tableau des flux de tresorerie   | "Cash flows from operating activities"  | Financier            |
| Annexe aux comptes               | "Notes to the financial statements"     | Descriptif           |
| Rapport de gestion               | "Management report" "Business review"   | Narratif             |
| Rapport d'audit                  | "Independent auditor's report"          | Certificatif         |
| Prospectus                       | "Securities offered" "Risk factors"     | Reglementaire        |
| Note d'information               | "Information memorandum"                | Financier/juridique  |
| Communique de presse financier   | "Press release" "Results"               | Public               |
| Presentation investisseurs       | "Investor presentation" "Highlights"    | Marketing/financier  |
| Contrat de credit                | "Credit agreement" "Loan"               | Juridique/financier  |
| Rapport annuel                   | "Annual report" "Chairman's statement"  | Mixte                |
| Etat de rapprochement            | "Reconciliation statement"              | Technique            |

## 2. Conventions numeriques et formats

| Element                  | Format anglais           | Format francais          | Regle de conversion         |
|--------------------------|--------------------------|--------------------------|------------------------------|
| Separateur decimal        | 3.14                     | 3,14                     | Remplacer . par ,            |
| Separateur milliers       | 1,234,567.89             | 1 234 567,89             | Remplacer , par espace       |
| Monnaie (euro)            | EUR 1,234.56 / 1,234.56 EUR | 1 234,56 EUR / 1 234,56 euro | Symbole apres le montant   |
| Monnaie (dollar)          | $1,234.56 / USD 1,234.56 | 1 234,56 USD / 1 234,56 $US | Adapter au format francais |
| Monnaie (livre sterling)  | 1,234.56 / GBP 1,234.56 | 1 234,56 GBP / 1 234,56 livre sterling | Adapter                |
| Pourcentage               | 15.5%                    | 15,5 %                   | Avec espace avant %          |
| Taux de change            | 1 EUR = 1.12 USD        | 1 EUR = 1,12 USD         | Virgule au lieu du point     |
| Actions / parts            | 1,234,567 shares         | 1 234 567 actions        | Terme "actions" ou "titres"  |
| Ratio                     | 2.5x                     | 2,5 x                    | Virgule + x                  |
| Multiple                  | 10.5x EBITDA             | 10,5 x EBE               | Conversion de l'indicateur   |
| Date                      | December 31, 2025        | 31 decembre 2025         | Ordre jour/mois/an           |
| Annee fiscale             | FY2025                   | Exercice 2025            | "Exercice" plutot que "annee" |
| Semestre                  | H1 2025 / H2 2025       | S1 2025 / S2 2025        | "S" pour semestre            |
| Trimestre                 | Q1 2025                  | T1 2025                  | "T" pour trimestre           |

## 3. Faux-amis financiers

| Faux-ami anglais        | Traduction erronee          | Traduction correcte                      |
|--------------------------|-----------------------------|------------------------------------------|
| "amortization"           | "amortissement" (dette)     | "amortissement" (immobilisation corporelle) / "remboursement" (dette) |
| "depreciation"           | "depreciation" (devaluation)| "amortissement" (PCG) / "depreciation" (IFRS) |
| "turnover"               | "rotation / renouvellement" | "chiffre d'affaires"                     |
| "stock"                  | "stock"                     | "actions" / "titres" (financier) / "stocks" (marchandises) |
| "share"                  | "part"                      | "action" (titre de propriete)             |
| "treasury"               | "tresorerie"                | "Tresor" (ministere) / "tresorerie" dans "treasury shares" = actions propres |
| "margin"                 | "marge" (correct)           | "marge" MAIS aussi "depot de garantie"    |
| "provision"              | "provision"                 | "provision" (correct) MAIS "prestation" (en assurance) |
| "recoverable"            | "recouvrable"               | "recuperable" / "encaissable"            |
| "liability"              | "liberte"                   | "passif" / "dette" / "responsabilite"    |
| "equity"                 | "equite"                    | "capitaux propres"                       |
| "appreciation"           | "appreciation"              | "augmentation de valeur"                 |
| "facility"               | "facilite"                  | "ligne de credit" / "credit revolving"   |
| "commitment"             | "engagement"                | "engagement" MAIS "commission d'engagement" vs "irrevocable" |
| "fund"                   | "fonds"                     | "fonds" (argent) vs "fonds de commerce" (goodwill) |
| "impairment"             | "degradation"               | "depreciation" / "perte de valeur"       |
| "redemption"             | "redemption"                | "remboursement" / "rachat"               |
| "sinking fund"           | "fonds noyade"              | "fonds d'amortissement"                  |
| "allowance"              | "allocation"                | "provision" / "provision pour depreciation" |
| "carrying amount"        | "montant du transport"      | "valeur comptable nette"                 |
| "stock option"           | "option sur stock"          | "stock-option" / "option sur titres"     |
| "warrant"                | "mandat"                    | "bon de souscription"                    |
| "call option"            | "option d'achat"            | "option d'achat" / "call"                |
| "put option"             | "option de vente"           | "option de vente" / "put"                |
| "swap"                   | "echange"                   | "swap" / "echange financier"             |
| "hedge"                  | "haie"                      | "couverture"                             |
| "yield"                  | "rendement"                 | "rendement" (correct)                    |
| "rebate"                 | "rabais"                    | "ristourne"                              |

# =============================================================================
# CADRE DECISIONNEL / DECISION FRAMEWORK
# =============================================================================

## Table 1 : Equivalence postes du bilan (PCG vs IFRS)

| IFRS (anglais)                  | PCG (francais)                         | Decision                              |
|----------------------------------|----------------------------------------|---------------------------------------|
| "Non-current assets"             | "Actif immobilise" / "Actif non courant" | Selon referentiel                    |
| "Intangible assets"              | "Immobilisations incorporelles"        | Conserver                             |
| "Goodwill"                       | "Ecart d'acquisition" / "Goodwill"    | "Ecart d'acquisition" (PCG) / "Goodwill" (IFRS) |
| "Property, plant and equipment"  | "Immobilisations corporelles"          |                                     |
| "Right-of-use assets"            | "Droit d'utilisation"                  | IFRS 16                               |
| "Investment property"            | "Immeubles de placement"               | IFRS / PCG different                    |
| "Investments in associates"      | "Titres mis en equivalence"            |                                     |
| "Deferred tax assets"            | "Imports diffuses actif"               | "Actif d'impot differe"              |
| "Current assets"                 | "Actif circulant" / "Actif courant"    | Selon referentiel                     |
| "Inventories"                    | "Stocks"                               | Conserver                             |
| "Trade and other receivables"    | "Creances clients et comptes rattaches"|                                     |
| "Cash and cash equivalents"      | "Tresorerie et equivalents de tresorerie" |                                   |
| "Total assets"                   | "Total de l'actif"                     |                                     |
| "Equity"                         | "Capitaux propres"                     |                                     |
| "Share capital"                  | "Capital social"                       |                                     |
| "Share premium"                  | "Prime d'emission"                     |                                     |
| "Retained earnings"              | "Report a nouveau"                     |                                     |
| "Non-controlling interests"      | "Interets ne donnant pas le controle"  | "Minoritaires" (ancien)               |
| "Non-current liabilities"        | "Passif non courant" / "Dettes a long terme" |                               |
| "Deferred tax liabilities"       | "Imports diffuses passif"              | "Passif d'impot differe"             |
| "Lease liabilities"              | "Dettes locatives"                     | IFRS 16                               |
| "Current liabilities"            | "Passif courant" / "Dettes a court terme" |                                    |
| "Trade and other payables"       | "Dettes fournisseurs et comptes rattaches" |                                    |
| "Total liabilities"              | "Total du passif"                      |                                     |

## Table 2 : Equivalence postes du compte de resultat

| IFRS (anglais)                       | PCG (francais)                                  |
|--------------------------------------|-------------------------------------------------|
| "Revenue" / "Sales"                  | "Chiffre d'affaires" / "Ventes de marchandises" |
| "Cost of sales" / "Cost of goods sold" | "Cout d'achat des marchandises vendues"       |
| "Gross profit" / "Gross margin"      | "Marge brute" / "Marge commerciale"            |
| "Selling and distribution expenses"  | "Frais de vente et de distribution"            |
| "Administrative expenses"            | "Frais administratifs"                          |
| "Research and development costs"     | "Frais de recherche et developpement"          |
| "Other operating income"             | "Autres produits d'exploitation"                |
| "Other operating expenses"           | "Autres charges d'exploitation"                 |
| "Operating profit"                   | "Resultat d'exploitation"                       |
| "Finance income"                     | "Produits financiers"                           |
| "Finance costs"                      | "Charges financieres"                           |
| "Share of profit of associates"      | "Quote-part de resultat des societes mises en equivalence" |
| "Profit before tax"                  | "Resultat avant impots"                         |
| "Income tax expense"                 | "Impôt sur les benefices" / "Charge d'impôt"    |
| "Profit from continuing operations"  | "Resultat des activites poursuivies"            |
| "Profit from discontinued operations"| "Resultat des activites abandonnees"            |
| "Profit for the period"              | "Resultat net de la periode"                     |
| "Net profit attributable to owners"  | "Resultat net - part du groupe"                 |
| "Net profit attributable to NCI"     | "Resultat net - part des minoritaires"          |
| "Earnings per share" (basic)         | "Resultat de base par action"                   |
| "Earnings per share" (diluted)       | "Resultat dilue par action"                      |
| "EBITDA"                             | "EBE (Excedent Brut d'Exploitation)"            |
| "EBIT"                               | "Resultat d'exploitation"                       |

## Table 3 : Equivalence flux de tresorerie

| IFRS (anglais)                          | PCG (francais)                              |
|-----------------------------------------|---------------------------------------------|
| "Cash flows from operating activities"  | "Flux de tresorerie lies a l'exploitation" / "Flux d'exploitation" |
| "Cash receipts from customers"          | "Encaissements recus des clients"           |
| "Cash paid to suppliers and employees"  | "Decaissements verses aux fournisseurs et au personnel" |
| "Interest paid"                         | "Interets verses"                           |
| "Income taxes paid"                     | "Impots sur les benefices verses"           |
| "Net cash from operating activities"    | "Flux net de tresorerie d'exploitation"     |
| "Cash flows from investing activities"  | "Flux de tresorerie lies aux operations d'investissement" |
| "Purchase of property, plant and equipment" | "Acquisitions d'immobilisations corporelles" |
| "Proceeds from sale of equipment"       | "Produits de cession d'immobilisations"     |
| "Dividends received"                    | "Dividendes recus"                          |
| "Net cash from investing activities"    | "Flux net de tresorerie d'investissement"   |
| "Cash flows from financing activities"  | "Flux de tresorerie lies aux operations de financement" |
| "Proceeds from issuance of shares"      | "Produits d'emission d'actions"             |
| "Proceeds from borrowings"              | "Nouveaux emprunts"                         |
| "Repayment of borrowings"               | "Remboursement d'emprunts"                  |
| "Dividends paid"                        | "Dividendes verses"                         |
| "Net cash from financing activities"    | "Flux net de tresorerie de financement"     |
| "Net increase/(decrease) in cash"       | "Variation nette de la tresorerie"          |
| "Cash at beginning of period"           | "Tresorerie d'ouverture"                    |
| "Cash at end of period"                 | "Tresorerie de cloture"                     |

## Table 4 : Ratios financiers - Traduction et formule

| Ratio (anglais)              | Ratio (francais)                   | Formule                                                  |
|------------------------------|------------------------------------|----------------------------------------------------------|
| "Current ratio"              | "Ratio de liquidite generale"      | Actif courant / Passif courant                           |
| "Quick ratio" / "Acid test"  | "Ratio de liquidite reduite"       | (Actif courant - Stocks) / Passif courant                |
| "Cash ratio"                 | "Ratio de liquidite immediate"     | Tresorerie / Passif courant                               |
| "Debt-to-equity ratio"       | "Ratio d'endettement"              | Dettes nettes / Capitaux propres                          |
| "Gearing ratio"              | "Ratio de levier"                  | Dettes financieres / (Capitaux propres + Dettes financieres) |
| "Interest coverage ratio"    | "Couverture des interets"          | EBE / Interets financiers                                 |
| "Debt service coverage"      | "Couverture du service de la dette"| EBE / (Interets + Remboursement)                         |
| "Return on equity (ROE)"    | "Rentabilite des capitaux propres" | Resultat net / Capitaux propres                           |
| "Return on assets (ROA)"    | "Rentabilite economique"           | Resultat d'exploitation / Total actif                     |
| "Return on invested capital (ROIC)" | "Rentabilite des capitaux investis" | NOPAT / Capitaux investis                     |
| "Gross margin"              | "Taux de marge brute"              | Marge brute / Chiffre d'affaires                          |
| "Net margin"                | "Taux de marge nette"              | Resultat net / Chiffre d'affaires                         |
| "Operating margin"          | "Taux de marge operationnelle"     | Resultat d'exploitation / Chiffre d'affaires              |
| "Asset turnover"            | "Rotation de l'actif"              | Chiffre d'affaires / Total actif                          |
| "Inventory turnover"        | "Rotation des stocks"              | CMV / Stock moyen                                         |
| "Days sales outstanding"    | "Delai moyen de reglement clients" | (Creances clients / CA TTC) x 360                         |
| "Days payable outstanding"  | "Delai moyen de reglement fournisseurs" | (Dettes fournisseurs / Achats TTC) x 360              |
| "Cash conversion cycle"    | "Cycle de conversion de tresorerie" | DSO + DIO - DPO                                           |
| "EBITDA margin"            | "Taux d'EBE / Taux de marge d'EBITDA" | EBE / Chiffre d'affaires                               |
| "P/E ratio"                | "PER (Price Earning Ratio)"         | Cours de bourse / Resultat par action                     |
| "Price-to-book ratio"     | "Ratio valeur de marche / VNC"      | Cours de bourse / Valeur comptable par action             |
| "Dividend yield"           | "Taux de rendement du dividende"    | Dividende par action / Cours de bourse                    |
| "Payout ratio"             | "Taux de distribution"              | Dividende / Resultat net                                   |
| "Net debt / EBITDA"         | "Dette nette / EBE"                 | (Dettes financieres - Tresorerie) / EBE                   |

## Table 5 : Termes de fiscalite

| Anglais                           | Francais                                     |
|-----------------------------------|----------------------------------------------|
| "Corporate income tax"            | "Impôt sur les societes (IS)"                |
| "Personal income tax"             | "Impôt sur le revenu (IR)"                   |
| "Value added tax"                 | "Taxe sur la valeur ajoutee (TVA)"            |
| "VAT rate"                        | "Taux de TVA"                                |
| "Standard VAT rate"               | "TVA au taux normal (20%)"                    |
| "Reduced VAT rate"                | "TVA a taux reduit (10%, 5,5%, 2,1%)"         |
| "VAT-exempt"                      | "Exonere de TVA"                              |
| "Input VAT"                       | "TVA deductible"                              |
| "Output VAT"                      | "TVA collectee"                               |
| "VAT return"                      | "Declaration de TVA (CA3)"                    |
| "VAT refund"                      | "Remboursement de TVA"                        |
| "Tax consolidation"              | "Integration fiscale"                         |
| "Group tax relief"               | "Regime d'integration fiscale"               |
| "Tax base"                        | "Base imposable"                              |
| "Taxable income"                  | "Resultat imposable"                          |
| "Tax rate"                        | "Taux d'imposition"                           |
| "Effective tax rate"              | "Taux effectif d'imposition"                  |
| "Nominal tax rate"                | "Taux nominal d'imposition"                   |
| "Deferred tax"                    | "Impôt differe"                               |
| "Tax credit"                      | "Credit d'impot"                              |
| "Research tax credit"             | "Credit d'impot recherche (CIR)"              |
| "Competitiveness and employment tax credit" | "Credit d'impot pour la competitivite et l'emploi (CICE)" |
| "Tax incentive"                   | "Incitation fiscale"                          |
| "Tax holiday"                     | "Exoneration temporaire"                      |
| "Tax exemption"                   | "Exoneration fiscale"                          |
| "Tax ruling"                      | "Rescrit fiscal"                              |
| "Tax audit"                       | "Controle fiscal" / "Verification de comptabilite" |
| "Tax reassessment"               | "Redressement fiscal"                          |
| "Tax penalty"                     | "Penalite fiscale"                             |
| "Tax appeal"                      | "Reclamation fiscale"                          |
| "Transfer pricing"                 | "Prix de transfert"                            |
| "Thin capitalization rules"       | "Regles de sous-capitalisation"               |
| "Withholding tax"                 | "Retenue a la source"                          |
| "CbCR (Country-by-Country Reporting)" | "Declaration pays par pays"                   |
| "Exit tax"                        | "Exit tax" / "Impôt de sortie"                |
| "Surtax"                          | "Contribution additionnelle" / "Surtaxe"      |
| "Social security contributions"   | "Cotisations sociales"                         |
| "Payroll taxes"                   | "Taxes sur les salaires"                       |
| "Property tax"                    | "Taxe fonciere"                                |
| "Business property contribution"  | "Contribution fonciere des entreprises (CFE)"  |
| "Business value added contribution" | "Cotisation sur la valeur ajoutee des entreprises (CVAE)" |
| "Local economic contribution"     | "Contribution economique territoriale (CET)"   |

## Table 6 : Termes du Plan Comptable General (PCG)

| Classe | Intitule                                  | Comptes principaux                             |
|--------|-------------------------------------------|------------------------------------------------|
| Classe 1 | Comptes de capitaux                     | 101 Capital, 106 Reserves, 11 Report a nouveau, 12 Resultat |
| Classe 2 | Comptes d'immobilisations                | 201 Frais de developpement, 205 Concessions, 211 Terrains, 213 Constructions, 215 Installations tech., 218 Autres, 261 Titres de participation |
| Classe 3 | Comptes de stocks et en-cours            | 31 Matieres premieres, 32 Autres approvisionnements, 33 En-cours, 35 Stocks de produits, 37 Stocks de marchandises |
| Classe 4 | Comptes de tiers                         | 401 Fournisseurs, 411 Clients, 421 Personnel, 431 Securite sociale, 444 Etat impots, 445 TVA, 461 Debiteurs divers |
| Classe 5 | Comptes financiers                       | 512 Banques, 53 Caisses, 58 Virements internes, 519 Concours bancaires |
| Classe 6 | Comptes de charges                       | 60 Achats, 61 Services exterieurs, 62 Autres services exterieurs, 63 Impots et taxes, 64 Charges de personnel, 65 Autres charges gestion courante, 66 Charges financieres, 67 Charges exceptionnelles, 68 Dotations amortissements |
| Classe 7 | Comptes de produits                      | 70 Ventes, 71 Production stockee, 72 Production immobilisee, 74 Subventions, 75 Autres produits, 76 Produits financiers, 77 Produits exceptionnels, 78 Reprises amortissements |

## Table 7 : Types de societes et formes juridiques (aspects financiers)

| Forme juridique | Capital minimum | Responsabilite     | Comptes annuels obligatoires | Commissaire aux comptes   |
|-----------------|-----------------|--------------------|------------------------------|---------------------------|
| SARL            | Aucun           | Limitee aux apports| Oui (bilan, CR, annexe)     | > seuils legaux           |
| EURL            | Aucun           | Limitee aux apports| Oui (bilan, CR, annexe)     | > seuils legaux           |
| SA              | 37 000 EUR      | Limitee aux apports| Oui                          | Obligatoire               |
| SAS             | Aucun           | Limitee aux apports| Oui (bilan, CR, annexe)     | > seuils legaux           |
| SNC             | Aucun           | Solidaire et indefinie | Oui                      | > seuils legaux           |
| SCI             | Aucun           | Limitee aux apports| Oui                          | > seuils legaux           |

## Table 8 : Termes de fusion-acquisition

| Anglais                          | Francais                                    |
|----------------------------------|---------------------------------------------|
| "Merger"                         | "Fusion"                                    |
| "Acquisition"                    | "Acquisition"                               |
| "Takeover"                       | "Offre publique d'achat (OPA)"              |
| "Hostile takeover"               | "OPA hostile"                               |
| "Friendly takeover"              | "OPA amicale"                               |
| "Demerger" / "Spin-off"          | "Scission"                                  |
| "Carve-out"                      | "Scission partielle"                        |
| "Buyout"                         | "Rachat" / "Acquisition avec effet de levier" |
| "Leveraged buyout (LBO)"         | "Rachat par effet de levier (LBO)"          |
| "Management buyout (MBO)"        | "Rachat par les dirigeants (MBO)"           |
| "Due diligence"                  | "Audit d'acquisition" / "Due diligence"     |
| "Vendor due diligence"           | "Audit d'acquisition cote vendeur"          |
| "Purchase price allocation"      | "Affectation du prix d'acquisition"         |
| "Earn-out"                      | "Complement de prix"                        |
| "Locked box"                     | "Compartiment prix ferme"                   |
| "Completion accounts"            | "Comptes de cloture"                        |
| "Representations and warranties" | "Declarations et garanties"                 |
| "Warranty and indemnity insurance" | "Assurance garantie de passif"            |
| "Closing conditions"             | "Conditions suspensives"                    |
| "Signing"                        | "Signature"                                 |
| "Closing"                        | "Realisation" / "Cloture"                   |
| "Long-stop date"                 | "Date butoir"                               |
| "Material adverse change"        | "Changement significatif defavorable"        |
| "Break fee"                      | "Indemnite d'immobilisation"                |
| "Non-compete clause"             | "Clause de non-concurrence"                 |
| "Share purchase agreement"       | "Contrat de cession d'actions"             |
| "Asset purchase agreement"       | "Contrat de cession d'actifs"              |
| "Business transfer agreement"    | "Contrat de cession de fonds de commerce"  |
| "Merger plan"                    | "Traite de fusion"                          |
| "Exchange ratio"                 | "Parite d'echange"                          |
| "Appraisal rights"               | "Droit de retrait"                          |
| "Minority squeeze-out"           | "Expropriation des minoritaires"            |
| "Delisting"                      | "Radiation de la cote"                     |

## Table 9 : Termes de marche financier

| Anglais                          | Francais                                    |
|----------------------------------|---------------------------------------------|
| "Stock market"                   | "Bourse des valeurs" / "Marche financier"   |
| "Stock exchange"                 | "Bourse"                                    |
| "Euronext Paris"                 | "Euronext Paris" (ne pas traduire)          |
| "Paris Stock Exchange"           | "Bourse de Paris"                           |
| "Listed company"                 | "Societe cotee"                             |
| "Listing"                        | "Cotation" / "Introduction en bourse"       |
| "IPO (Initial Public Offering)"  | "Introduction en bourse" / "IPO"            |
| "Secondary offering"             | "Augmentation de capital" / "Offre secondaire" |
| "Capital increase"               | "Augmentation de capital"                   |
| "Rights issue"                   | "Augmentation de capital avec DPS"          |
| "Pre-emptive rights"             | "Droit preferentiel de souscription (DPS)"  |
| "Book building"                  | "Construction du livre d'ordres"            |
| "Market capitalization"          | "Capitalisation boursiere"                  |
| "Free float"                     | "Flottant"                                  |
| "Market maker"                   | "Teneur de marche"                          |
| "Liquidity provider"             | "Contrat de liquidite"                      |
| "Index"                          | "Indice boursier"                           |
| "CAC 40"                         | "CAC 40" (ne pas traduire)                  |
| "SBF 120"                        | "SBF 120" (ne pas traduire)                 |
| "Blue chip"                      | "Valeur vedette" / "Blue chip"              |
| "Mid cap"                        | "Moyenne capitalisation"                    |
| "Small cap"                      | "Petite capitalisation"                     |
| "Growth stock"                   | "Valeur de croissance"                      |
| "Value stock"                    | "Valeur de rendement"                       |
| "Defensive stock"                | "Valeur defensive"                          |
| "Cyclical stock"                 | "Valeur cyclique"                           |
| "Penny stock"                    | "Titre a tres faible valeur"                |
| "Spread"                         | "Fourchette"                                |
| "Bid price"                      | "Cours acheteur"                            |
| "Ask price"                      | "Cours vendeur"                             |
| "Order book"                     | "Carnet d'ordres"                           |
| "Limit order"                    | "Ordre a cours limite"                      |
| "Market order"                   | "Ordre au marche"                           |
| "Stop order"                     | "Ordre stop"                                |
| "Buy"                            | "Achat" (A)                                 |
| "Sell"                           | "Vente" (V)                                 |
| "Short selling"                  | "Vente a decouvert"                         |
| "Margin call"                    | "Appel de marge"                            |
| "Collateral"                     | "Garantie"                                  |
| "Hedge fund"                     | "Fonds speculatif" / "Fonds alternatif"    |
| "Mutual fund"                    | "OPCVM" / "Fonds commun de placement"       |
| "ETF"                            | "ETF (Fonds indiciel cote)"                 |
| "Private equity"                 | "Capital-investissement" / "Private equity" |
| "Venture capital"                | "Capital-risque"                            |
| "Growth capital"                 | "Capital developpement"                     |
| "Buyout fund"                    | "Fonds de LBO"                              |
| "Infrastructure fund"            | "Fonds d'infrastructure"                    |
| "Real estate fund"               | "Fonds immobilier" / "SCPI / OPCI"          |
| "Sovereign wealth fund"          | "Fonds souverain"                           |
| "Pension fund"                   | "Fonds de pension"                          |

## Table 10 : Termes de dette et financement

| Anglais                          | Francais                                    |
|----------------------------------|---------------------------------------------|
| "Loan"                           | "Pret" / "Emprunt"                          |
| "Senior debt"                    | "Dette senior"                              |
| "Junior debt"                    | "Dette junior"                              |
| "Subordinated debt"              | "Dette subordonnee"                         |
| "Mezzanine debt"                 | "Dette mezzanine"                           |
| "Secured debt"                   | "Dette garantie"                            |
| "Unsecured debt"                 | "Dette non garantie"                        |
| "Revolving credit facility"      | "Credit revolving" / "Ligne de credit renouvelable" |
| "Term loan"                      | "Pret amortissable" / "Pret terme"          |
| "Bridge loan"                    | "Pret relais"                               |
| "Syndicated loan"                | "Pret syndique"                             |
| "Bilateral loan"                 | "Pret bilateral"                            |
| "Bond"                           | "Obligation"                                |
| "Convertible bond"               | "Obligation convertible"                    |
| "Exchangeable bond"              | "Obligation echangeable"                    |
| "Green bond"                     | "Obligation verte / green bond"             |
| "High-yield bond"                | "Obligation a haut rendement"               |
| "Investment grade"               | "Categorie investissement"                  |
| "Credit rating"                  | "Note de credit" / "Rating"                 |
| "Moody's / S&P / Fitch"          | Conserver les noms                          |
| "Maturity"                       | "Echeance" / "Maturite"                     |
| "Tenor"                          | "Duree" / "Terme"                           |
| "Amortization schedule"          | "Tableau d'amortissement"                   |
| "Bullet repayment"               | "Remboursement in fine"                     |
| "Grace period"                   | "Periode de differe / Franchise"            |
| "Interest rate"                  | "Taux d'interet"                             |
| "Fixed rate"                     | "Taux fixe"                                 |
| "Floating rate"                  | "Taux variable"                             |
| "LIBOR / EURIBOR"                | Conserver le nom de l'indice               |
| "Margin"                         | "Marge" (sur le taux)                       |
| "Spread"                         | "Marge" / "Spread"                          |
| "All-in cost"                    | "Cout tout compris"                         |
| "Arrangement fee"               | "Frais de montage"                           |
| "Commitment fee"                | "Commission d'engagement"                    |
| "Agency fee"                     | "Commission d'agence"                       |
| "Prepayment premium"            | "Prime de remboursement anticipe"            |
| "Default interest"              | "Interet de retard"                          |
| "Financial covenants"           | "Engagements financiers / Covenants"         |
| "Maintenance covenant"          | "Covenant de maintien"                       |
| "Incurrence covenant"           | "Covenant de souscription"                   |
| "Net debt / EBITDA covenant"    | "Covenant dette nette / EBE"                |
| "Interest cover covenant"       | "Covenant de couverture des interets"        |
| "Leverage covenant"             | "Covenant de levier"                         |
| "Security"                       | "Surete / Garantie"                          |
| "Pledge"                         | "Nantissement"                               |
| "Charge" (UK)                    | "Hypotheque"                                 |
| "Negative pledge"               | "Clause de non-affectation" / "Negative pledge" |
| "Pari passu"                     | "De meme rang"                               |
| "Cross-default"                  | "Defaut croise / Clause de defaut croise"    |
| "Material adverse change"       | "Changement significatif defavorable"        |
| "Events of default"             | "Cas de defaut"                              |
| "Acceleration"                   | "Exigibilite anticipee"                      |
| "Representations"                | "Declarations"                               |
| "Conditions precedent"          | "Conditions suspensives"                     |

## Table 11 : Termes d'assurance et risque

| Anglais                               | Francais                                     |
|---------------------------------------|----------------------------------------------|
| "Insurance"                           | "Assurance"                                  |
| "Premium"                             | "Prime"                                      |
| "Deductible"                          | "Franchise"                                  |
| "Coverage"                            | "Couverture"                                 |
| "Policy"                              | "Police d'assurance" / "Contrat d'assurance" |
| "Claim"                               | "Sinistre" / "Declaration de sinistre"       |
| "Insurer"                             | "Assureur"                                   |
| "Insured"                             | "Assure"                                     |
| "Policyholder"                        | "Souscripteur"                               |
| "Beneficiary"                         | "Beneficiaire"                               |
| "Actuary"                             | "Actuaire"                                   |
| "Underwriting"                        | "Souscription"                               |
| "Reinsurance"                         | "Reassurance"                                |
| "Risk management"                     | "Gestion des risques"                        |
| "Risk mitigation"                     | "Reduction des risques"                      |
| "Risk transfer"                       | "Transfert de risque"                       |

# =============================================================================
# NORMES ET STANDARDS
# =============================================================================

## Plan Comptable General (PCG) - Structure

Le PCG francais est reglemente par le Reglement ANC (Autorite des Normes
Comptables) n°2014-03 et ses mises a jour.

- Principe de prudence, de regularite et de sincerite
- Principe d'independance des exercices
- Principe de continuite d'exploitation
- Principe des couts historiques (sauf IFRS)
- Principe de non-compensation
- Principe d'intangibilite du bilan d'ouverture

## Seuils legaux en France

| Obligation                                          | Seuil (3 criteres sur 3)                            |
|------------------------------------------------------|------------------------------------------------------|
| Comptes annuels (bilan, CR, annexe)                  | Toutes les societes                                  |
| Commissaire aux comptes (SARL)                       | CA > 8 000 000 EUR, Total bilan > 4 000 000 EUR, > 50 salariés (2 sur 3) |
| Commissaire aux comptes (SA)                         | Obligatoire sans condition de seuil                  |
| Publication des comptes annuels                      | Toutes les societes                                  |
| Rapport de gestion                                   | Depassement de 2 des 3 seuils : 4 M EUR total bilan, 8 M EUR CA, 50 salariés |
| Consolidation des comptes                            | Controle exclusif ou conjoint d'une ou plusieurs filiales |

## Formats de depots legaux (liasse fiscale)

Le depot des comptes annuels s'effectue selon le formulaire Cerfa (liasse
fiscale) compose de :
- Bilan actif (n° 2050)
- Bilan passif (n° 2051)
- Compte de resultat (n° 2052 et 2053)
- Immobilisations (n° 2054)
- Amortissements (n° 2055)
- Provisions (n° 2056)
- Creances et dettes (n° 2057)
- Variation des capitaux propres (n° 2058)
- Determination du resultat fiscal (n° 2058-A a 2058-G)

## IFRS vs PCG : principales differences

| Point de difference           | PCG                                      | IFRS                                     |
|-------------------------------|------------------------------------------|------------------------------------------|
| Cadre conceptuel              | ANC reglementaire                        | IASB / IFRS Foundation                   |
| Presentation                  | Format impose (liasse fiscale)           | Libre (IAS 1)                           |
| Evaluation                    | Cout historique principalement           | Juste valeur frequent                    |
| Amortissement goodwill       | Amortissement lineaire (5-20 ans)        | Test de depreciation annuel             |
| Frais de developpement        | Activable (conditions strictes)          | Activable (IAS 38)                       |
| Frais de R&D                 | Charges ou immobilisation                | Generalement charges                     |
| Contrats de location          | Classification credit-bail / location    | IFRS 16 : quasi-generalisation           |
| Impots diffuses               | Limites strictes                         | Full provision (IAS 12)                  |
| Stocks                        | FIFO ou cout moyen pondere               | FIFO ou cout moyen (LIFO interdit)       |
| Instruments financiers        | Classification tripartite                | Classification IFRS 9                    |
| Abandons de creances          | Comptabilisation specifique              | Evaluation a la juste valeur             |
| Etats financiers intermediaires| Non obligatoires                        | IAS 34 (si publies)                     |

## Format des dates et references temporelles

| Reference anglaise      | Reference francaise        |
|--------------------------|----------------------------|
| "FY2025" / "Fiscal year 2025" | "Exercice 2025"        |
| "Calendar year 2025"    | "Annee civile 2025"        |
| "Year ended December 31, 2025" | "Exercice clos le 31 decembre 2025" |
| "Six months ended June 30, 2025" | "Semestre clos le 30 juin 2025" |
| "Quarter ended March 31, 2025" | "Trimestre clos le 31 mars 2025" |
| "As of [date]"          | "Au [date]" / "Arrete au [date]" |
| "Year to date"          | "Cumul depuis le debut de l'exercice" |
| "Period from ... to ..." | "Periode du ... au ..."    |
| "Comparative period"    | "Periode comparable"       |
| "Prior year"            | "Exercice precedent"       |
| "Current year"          | "Exercice en cours"        |
| "Reporting date"        | "Date de cloture"          |
| "Subsequent events"     | "Evenements posterieurs a la cloture" |
