---
id: fi/domain/legal
type: domain
target_lang: fi
name: Domain: Legal (Finnish -- FI)
description: Finnish legal domain terminology and translation rules
---

# Finnish Legal Domain Translation

## Reader Model

### Target Reader Profile
- **Primary Reader**: Finnish lawyers (asianajajat), judges (tuomarit), legal advisors (oikeusneuvonantajat), notaries (notaarit)
- **Secondary Reader**: Corporate legal counsel (yrityksen oikeusavustajat), contract managers, compliance officers
- **Tertiary Reader**: Courts (oikeudet), arbitration panels (välitysmiehet), enforcement officers (ulosottomiehet), public auditors

### Reader Expectations
1. **Terminology Precision**: Every legal term must correspond to established Finnish legal terminology defined in legislation (laki, asetus). Near-synonyms must not be confused.
2. **Legislation Compliance**: Contract law terms must align with the Finnish Contracts Act (varallisuusoikeussopimuslaki, 1929/20.4) and related case law.
3. **Sentence Structure**: Finnish legal language uses long, subordination-heavy sentence structures; short sentences may sometimes be insufficient.
4. **Official Correspondence Format**: Petitions, contracts, and formal notices follow established templates.
5. **Latin Terms**: Latin legal terms are used in their established Finnish forms (ex parte, bona fide, etc.).

### Reader Expectation Matrix

| Expectation | Importance | Consequence if Unmet |
|-------------|------------|---------------------|
| Statutory terminology compliance | Critical | Legal invalidity, case loss |
| Finnish court system terminology | Critical | Misidentification of court level |
| Official correspondence format | High | Document not accepted |
| Correct use of Latin terms | High | Meaning drift, misinterpretation |
| Passive voice in formal texts | Medium | Unnatural text |
| Partitive vs. total object distinction | Critical | Ambiguity in obligations |

---

## Decision Framework

### Table L1: Finnish Court System Terminology

| English | Finnish | Level | Description |
|---------|---------|-------|-------------|
| District Court | käräjäoikeus | 1st instance | General trial court of first instance |
| Court of Appeal | hovioikeus | 2nd instance | Appellate court hearing appeals from district courts |
| Supreme Court | korkein oikeus | 3rd instance | Highest court for matters of general legal importance |
| Administrative Court | hallinto-oikeus | 1st instance | Administrative law matters |
| Supreme Administrative Court | korkein hallinto-oikeus | 2nd instance | Appeals from administrative courts |
| Market Court | markkinaoikeus | Specialized | Competition and market law disputes |
| Labour Court | työtuomioistuin | Specialized | Collective labour disputes |
| Insurance Court | vakuutusoikeus | Specialized | Social insurance disputes |
| Compensation Court | korvausoikeus | Specialized | Compensation claims |

### Table L2: Contract and Obligation Law Terminology

| English | Finnish | Legislation Reference | Description |
|---------|---------|----------------------|-------------|
| Contract | sopimus | VarOSL | Binding agreement between parties |
| Agreement | sopimus / yhteisymmärrys | VarOSL | General term for agreement |
| Party | osapuoli | VarOSL | Party to a contract |
| Offer | tarjous | VarOSL | Binding proposal |
| Acceptance | vastaanotto / hyväksyntä | VarOSL | Acceptance of offer |
| Consideration | vastike | VarOSL | Counter-performance |
| Breach of contract | sopimuksen rikkominen | VarOSL | Failure to perform obligations |
| Force majeure | ylivoimainen este / force majeure | VarOSL | Unforeseeable event |
| Damages | vahingonkorvaus | VarOSL | Compensation for loss |
| Penalty clause | sakko- tai rikosuhuarvovelvoite | VarOSL | Penalty provision |
| Warranty | takaus | VarOSL | Guarantee of quality |
| Liability | vastuu / velvollisuus | VarOSL | Legal responsibility |
| Indemnity | vahingonkorvaus / vapauttaminen | VarOSL | Loss reimbursement |
| Assignment | luovutus / siirtäminen | VarOSL | Transfer of rights |
| Termination | irtisanominen / purkaminen | VarOSL | Ending a contract |
| Rescission | purkaminen | VarOSL | Unwinding of contract |
| Null and void | mitätön | VarOSL | Legally void |
| Voidable | kumottavissa | VarOSL | Can be annulled |

### Table L3: Criminal Law Terminology

| English | Finnish | Rikoslaki Reference | Description |
|---------|---------|---------------------|-------------|
| Crime / Offence | rikos | RL | Criminal act |
| Misdemeanor | rikkomus | RL | Lesser offence |
| Felony | vakava rikos | RL | Serious crime |
| Prosecution | syyte / syyttäminen | RL | Criminal charges |
| Defendant | syytetty / vastaaja | RL | Accused person |
| Plaintiff | kantaja | RL | Complainant |
| Verdict | tuomio | RL | Court judgment |
| Sentence | rangaistus / tuomio | RL | Penalty imposed |
| Appeal | muutoksenhaku / valitus | RL | Challenge to judgment |
| Statute of limitations | vanhentuminen | RL | Time limit for prosecution |
| Bail | takuut | RL | Security for release |
| Plea bargaining | sovittelu | RL | Negotiated resolution |

### Table L4: Property and Family Law Terminology

| English | Finnish | Legislation Reference | Description |
|---------|---------|----------------------|-------------|
| Ownership | omistusoikeus | TilL | Right of ownership |
| Mortgage | kiinnitys | TilL | Property security |
| Lease | vuokrasopimus | VarOSL | Rental agreement |
| Tenant | vuokralainen | VarOSL | Renting party |
| Landlord | vuokranantaja / isäntä | VarOSL | Property owner/lessor |
| Inheritance | perintö / periminen | periL | Succession to property |
| Heir | perillinen | periL | Person entitled to inherit |
| Will | testamentti | periL | Last will and testament |
| Marriage | avioliitto | avioliittolaki | Legal marriage |
| Divorce | avioero | avioliittolaki | Dissolution of marriage |
| Child custody | huoltajuus | huoltolaki | Legal guardianship |
| Alimony | elatusapu | huoltolaki | Spousal/child support |

---

## Error Pattern Library

### EP-L1: Court Level Confusion
- **Common Error**: Translating `hovioikeus` as "Supreme Court" (it is Court of Appeal) or `käräjäoikeus` as "Supreme Court."
- **Correct**: District Court = `käräjäoikeus`, Court of Appeal = `hovioikeus`, Supreme Court = `korkein oikeus`.
- **Rule**: Always verify the court level before translating.

### EP-L2: Partitive vs. Total Object
- **Common Error**: Using nominative/accusative for objects where partitive is required.
- **Correct**: "The company pays damages" = `Yritys maksaa vahingonkorvauksia` (partitive = ongoing/indeterminate), vs. "The company pays the damages" = `Yritys maksaa vahingonkorvaukset` (total object = specific, completed).
- **Rule**: Partitive for ongoing/incomplete actions; total object for completed/specific actions.

### EP-L3: Passive Voice Misuse
- **Common Error**: Using active voice where Finnish legal convention requires passive.
- **Correct**: `Sopimus on tarkoitettu osapuolten välistä oikeussuhdetta varten.` (The contract is intended for the legal relationship between the parties.)
- **Rule**: Finnish legal texts frequently use passive constructions; do not force active voice.

### EP-L4: Latin Term Adaptation
- **Common Error**: Using English or French Latin forms where Finnish legal Latin differs.
- **Correct**: `bona fide` (not "good faith" translated literally), `ex officio` (not "viran puolesta" in Latin-heavy contexts).
- **Rule**: When Latin terms are standard in Finnish legal texts, preserve them in their Latin form.

---

## Domain-Specific Reference

### Finnish Legal System Overview
Finland has a **bilingual** (Finnish and Swedish) legal system. All legislation exists in both languages. The court system is structured as:
1. **Käräjäoikeus** (District Court) — 31 courts, first instance for most civil and criminal matters.
2. **Hovioikeus** (Court of Appeal) — 6 courts, appellate jurisdiction.
3. **Korkein oikeus** (Supreme Court) — 1 court, final appeals on matters of general legal significance.
4. **Hallinto-oikeus** (Administrative Court) — 8 courts, administrative law first instance.
5. **Korkein hallinto-oikeus** (Supreme Administrative Court) — 1 court, final administrative appeals.

### Key Legislation References
- **Laki varallisuusoikeussopimuksista** (Contracts on Property Rights Act) — 1929/20.4
- **Rikoslaki** (Criminal Code) — 39/1889
- **Tilauslaki** (Sales Act) — various amendments
- **Asunto- ja liiketilalaki** (Housing and Business Premises Act)
- **Työsopimuslaki** (Employment Contracts Act) — 55/2001
- **Perintölaki** (Inheritance Act) — 40/1965

### Finnish Legal Style Notes
- Legal Finnish uses **partitive** extensively for obligations and rights.
- The **passive voice** is standard in legislation: `Tämän lain säännöksiä sovelletaan...` (The provisions of this Act shall be applied...).
- `Tämän lain` (of this Act) vs. `tässä laissa` (in this Act) — genitive for ownership, inessive for location.
- Legal Finnish uses `saakka` (until/unto) for deadlines: `1.1.2026 saakka` (until 1.1.2026).
- `Muun muassa` (among other things), `muuten muassa` (otherwise, among others) are common legal connectors.
