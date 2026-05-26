---

id: nl/domain/technical
type: domain
target_lang: nl
name: "Technisch Nederlands — Domain File: Technical Translation"
description: Dutch Technical domain terminology and translation rules
---

# Technisch Nederlands — Domain File: Technical Translation

## 1. Reader Model

### Primary Reader: Dutch Technical Professional

| Attribute | Description |
|-----------|-------------|
| **Role** | Engineer, technician, safety officer, technical reviewer, NEN committee member |
| **Language Expectation** | Precise, unambiguous Standard Dutch (AN); anglicisms accepted only when no Dutch equivalent exists in NEN; strict adherence to technical terminology |
| **Knowledge Level** | High domain expertise; expects exact NEN references, correct SI usage, and safety classifications |
| **Tolerance for Ambiguity** | Extremely low — any vague phrasing is rejected. Every measurement, tolerance, and safety level must be explicit |
| **Formatting Expectation** | Structured with numbered clauses, sub-clauses, tables, cross-references to NEN/EN/ISO standards |
| **Key Concern** | Safety compliance, liability avoidance, correct execution of technical specifications |

### Secondary Reader: Legal/Compliance Reviewer

| Attribute | Description |
|-----------|-------------|
| **Role** | Corporate legal, insurance assessor, regulatory auditor |
| **Language Expectation** | Precise normative language using modal verbs: *moeten* (obligation), *mogen* (permission), *dienen te* (formal obligation), *behoren te* (should) |
| **Key Concern** | That the Dutch text creates no ambiguity about obligations, liabilities, or safety requirements |

---

## 2. Decision Framework

### Table T1: Modal Verbs — Obligation and Permission

| English | Dutch (Technical) | Context | Notes |
|---------|-------------------|---------|-------|
| shall | **moet / moeten** | Normative requirements (NEN-EN 1990) | Use for mandatory requirements. Never use *zal* as a future tense in specs. |
| shall not | **mag niet / mogen niet** | Prohibitions | Equivalent to *is niet toegestaan* |
| must | **dient te / dienen te** | Formal obligation, procedural | Stronger than *moeten* in formal administrative technical texts |
| should | **behoort te / behoren te** | Recommendations, best practice | Non-mandatory. Equivalent to *wordt aanbevolen* |
| should not | **behoort niet te / behoren niet te** | Discouraged practices | Non-mandatory prohibition |
| may | **mag / mogen** | Permission | Alternative: *is toegestaan* |
| need not | **hoeft niet / hoeven niet** | Optional | Equivalent to *is niet vereist* |
| can | **kan / kunnen** | Possibility or capability | Do not use for permission. Use *kan* only for physical possibility. |

### Table T2: Technical Units and Quantities

| English | Dutch | Rule |
|---------|-------|------|
| mm / cm / m / km | **mm / cm / m / km** | Keep SI symbols unchanged. Never translate unit symbols. |
| kilogram | **kilogram (kg)** | Full name is lowercase, unit symbol unchanged |
| litre / liter | **liter (l of L)** | Dutch uses *liter*. Symbol l or L both accepted (NEN 1000) |
| metre / meter | **meter (m)** | Dutch spelling *meter*, symbol m |
| Celsius | **graden Celsius** or **°C** | *Celsius* capitalised; *graden* lowercase (contrary to English) |
| percentage | **procent** | Always one word in Dutch. Symbol: % |
| per cent | **procent** | Never *percent*; never *procentueel* unless necessary |
| voltage | **spanning** (V) | *Spanning* for electrical. *Voltage* is an anglicism. |
| current | **stroom** (A) | *Stroom* or *stroomsterkte*. Not *current*. |
| power | **vermogen** (W) | *Vermogen*. *Power* is an anglicism in this context. |
| force | **kracht** (N) | *Kracht*. Not *force*. |
| pressure | **druk** (Pa) | *Druk*. Not *pressure*. |
| temperature | **temperatuur** | *Temperatuur*. Not *temperatuur* (spelling note: one 'u'). |
| length | **lengte** | *Lengte*. Not *length*. |
| width | **breedte** | *Breedte* |
| height | **hoogte** | *Hoogte* |
| depth | **diepte** | *Diepte* |
| diameter | **diameter** | Same in Dutch, but lowercase in running text |
| radius | **straal** | *Straal*. Not *radius* except in mathematical context. |

### Table T3: Safety Level Terminology

| English | Dutch | Standard | Notes |
|---------|-------|----------|-------|
| safety | **veiligheid** | NEN-EN-ISO 12100 | General term |
| danger | **gevaar** | NEN-EN-ISO 12100 | Source of potential harm |
| hazard | **gevaar** / **risicobron** | NEN-EN-ISO 12100 | *Gevaar* preferred; *risicobron* when distinction needed |
| risk | **risico** | NEN-EN-ISO 12100 | Combination of severity and probability |
| residual risk | **restrisico** | NEN-EN-ISO 12100 | Risk remaining after protective measures |
| tolerable risk | **aanvaardbaar risico** | NEN-EN-ISO 12100 | *Aanvaardbaar* not *tolerabel* |
| protective measure | **beschermende maatregel** | NEN-EN-ISO 12100 | |
| safeguarding | **beveiliging** | NEN-EN-ISO 12100 | |
| Safety Integrity Level | **SIL (veiligheidsintegriteitsniveau)** | NEN-EN-IEC 62061 | Keep SIL acronym; provide Dutch expansion at first use |
| Performance Level | **PL (prestatieniveau)** | NEN-EN-ISO 13849 | Keep PL acronym; provide Dutch expansion at first use |
| emergency stop | **noodstop** | NEN-EN-IEC 60204-1 | One word in Dutch |
| emergency off | **nooduitschakeling** | NEN-EN-IEC 60204-1 | |
| warning | **waarschuwing** | NEN-EN-ISO 7010 | Safety sign signal word |
| caution | **voorzichtig** | NEN-EN-ISO 7010 | Safety sign signal word |
| danger (signal word) | **gevaar** | NEN-EN-ISO 7010 | Safety sign signal word |
| notice | **opmerking** | NEN-EN-ISO 7010 | Safety sign signal word |
| guard | **afscherming** | NEN-EN-ISO 14120 | Physical barrier |
| interlock | **vergrendeling** | NEN-EN-ISO 14119 | |

### Table T4: NEN Standard References

| English Pattern | Dutch Pattern | Example |
|-----------------|--------------|---------|
| "in accordance with ISO 1234" | **volgens NEN-EN-ISO 1234** | *volgens NEN-EN-ISO 12100* |
| "as per EN 1234" | **overeenkomstig NEN-EN 1234** | *overeenkomstig NEN-EN 1990* |
| "complies with standard X" | **voldoet aan norm X** | *voldoet aan NEN-EN-IEC 60204-1* |
| "standard requires" | **de norm vereist** | *NEN-EN-ISO 13849-1 vereist* |
| "harmonised standard" | **geharmoniseerde norm** | Under EU New Approach |
| "national standard" | **nationale norm** | |
| "technical specification" | **technische specificatie** | |
| "code of practice" | **praktijkrichtlijn** | NPR (Nederlandse Praktijkrichtlijn) |

### Table T5: Technical Documentation Structure

| English Element | Dutch Equivalent | Notes |
|-----------------|------------------|-------|
| Table of Contents | **Inhoudsopgave** | |
| Scope | **Toepassingsgebied** | Not *scope* |
| Normative references | **Normatieve verwijzingen** | |
| Terms and definitions | **Termen en definities** | |
| Symbols and abbreviations | **Symbolen en afkortingen** | |
| General requirements | **Algemene eisen** | |
| Test method | **Beproevingsmethode** | Not *testmethode* |
| Annex | **Bijlage** | Capitalise: *Bijlage A* |
| Bibliography | **Bibliografie** | |
| Foreword | **Voorwoord** | |
| Introduction | **Inleiding** | |
| Technical report | **Technisch rapport** | TR |
| Specification | **Specificatie** | |
| Clause | **Artikel** (in standards) / **Paragraaf** (in general docs) | |
| Sub-clause | **Subparagraaf** / **Lid** | |
| Figure | **Figuur** | Keep abbreviation: *Fig.* or *Figuur* |
| Table | **Tabel** | |
| Equation | **Vergelijking** | Not *equatie* |

### Table T6: Material and Process Terminology

| English | Dutch | Domain | Notes |
|---------|-------|--------|-------|
| steel | **staal** | Materials | |
| stainless steel | **roestvast staal (RVS)** | Materials | RVS is standard abbreviation |
| cast iron | **gietijzer** | Materials | |
| aluminium / aluminum | **aluminium** | Materials | EN spelling |
| copper | **koper** | Materials | |
| brass | **messing** | Materials | |
| plastic | **kunststof** | Materials | *Plastic* only for consumer context |
| polymer | **polymeer** | Materials | |
| composite | **composiet** | Materials | |
| concrete | **beton** | Civil | |
| reinforcement | **wapening** | Civil | *Wapening* not *versterking* for rebar |
| timber / wood | **hout** | Civil | |
| coating | **coating** / **deklaag** | Surface | *Coating* is accepted; *deklaag* preferred |
| welding | **lassen** | Manufacturing | |
| weld | **las** | Manufacturing | |
| machined | **bewerkt** | Manufacturing | *Gefreesd* / *gedraaid* for specific operations |
| tolerance | **tolerantie** | Manufacturing | |
| fit | **passing** | Manufacturing | |
| clearance | **speling** | Manufacturing | *Speling* not *clearance* |
| torque | **aanhaalmoment** / **koppel** | Fasteners | *Aanhaalmoment* for bolts; *koppel* for shafts |

### Table T7: Electrical and Electronic Terminology

| English | Dutch | Standard | Notes |
|---------|-------|----------|-------|
| voltage | **spanning** | NEN-EN-IEC | *Spanning* not *voltage* |
| current | **stroom** | NEN-EN-IEC | *Stroomsterkte* for full clarity |
| resistance | **weerstand** | NEN-EN-IEC | |
| capacitance | **capaciteit** | NEN-EN-IEC | |
| inductance | **inductie** / **zelfinductie** | NEN-EN-IEC | |
| impedance | **impedantie** | NEN-EN-IEC | Accepted loanword |
| frequency | **frequentie** | NEN-EN-IEC | |
| power supply | **voeding** | NEN-EN-IEC | *Voedingsspanning* for supply voltage |
| earth / ground | **aarde** | NEN-EN-IEC | *Aarding* for earthing system |
| protective earth | **beschermingsaarde (PE)** | NEN-EN-IEC | |
| neutral | **nul (N)** | NEN-EN-IEC | |
| live conductor | **fasedraad (L)** | NEN-EN-IEC | |
| switch | **schakelaar** | | |
| circuit breaker | **installatieautomaat** | | |
| fuse | **smeltveiligheid** / **zekering** | | *Zekering* is most common |
| transformer | **transformator** | | |
| motor | **motor** | | Same in Dutch |
| drive | **aandrijving** | | *Drive* only for electronic drives |
| sensor | **sensor** | | Accepted |
| actuator | **aandrijfelement** / **actuator** | | *Actuator* accepted but *aandrijfelement* preferred |
| programmable logic controller | **programmeerbare logische controller (PLC)** | | Keep PLC acronym |
| Human-Machine Interface | **Mens-Machine-Interface (MMI)** / **HMI** | | HMI more common even in NL |

### Table T8: Measurement and Inspection Terminology

| English | Dutch | Notes |
|---------|-------|-------|
| measurement | **meting** | |
| to measure | **meten** | |
| measuring instrument | **meetinstrument** | |
| calibration | **kalibratie** | Not *ijking* (which is legal metrology) |
| verification | **verificatie** | |
| validation | **validatie** | |
| accuracy | **nauwkeurigheid** | |
| precision | **precisie** | |
| repeatability | **herhaalbaarheid** | |
| reproducibility | **reproduceerbaarheid** | |
| uncertainty | **meetonzekerheid** | |
| tolerance | **tolerantie** | |
| deviation | **afwijking** | |
| error | **fout** | *Fout* not *error* |
| inspection | **inspectie** | |
| non-destructive testing | **niet-destructief onderzoek (NDO)** | NEN-EN-ISO 9712 |
| visual inspection | **visuele inspectie** | |
| dimensional check | **maatcontrole** | |

### Table T9: Drawings and CAD Terminology

| English | Dutch | Notes |
|---------|-------|-------|
| drawing | **tekening** | Technische tekening |
| detail drawing | **detailtekening** | |
| assembly drawing | **samenstellingstekening** | |
| part drawing | **onderdeeltekening** | |
| dimension | **maat** | |
| dimension line | **maatlijn** | |
| extension line | **hulplijn** | |
| centre line | **middellijn** | |
| cross-section | **doorsnede** | |
| section view | **doorsnede-aanzicht** | |
| view | **aanzicht** | |
| scale | **schaal** | *Schaal 1:2* |
| projection | **projectie** | |
| tolerance | **tolerantie** | |
| surface finish | **oppervlakteruwheid** | |
| welding symbol | **lassymbool** | NEN-EN-ISO 2553 |
| parts list | **stuklijst** | |
| revision | **revisie** | |
| title block | **titellblok** | |
| layout | **lay-out** / **opstelling** | *Lay-out* accepted in technical drawing context |

### Table T10: Quality and Testing

| English | Dutch | Standard | Notes |
|---------|-------|----------|-------|
| quality | **kwaliteit** | NEN-EN-ISO 9000 | |
| quality management | **kwaliteitsmanagement** | NEN-EN-ISO 9001 | |
| quality control | **kwaliteitscontrole** | | |
| quality assurance | **kwaliteitsborging** | | |
| non-conformity | **afwijking** / **non-conformiteit** | NEN-EN-ISO 9000 | *Afwijking* preferred |
| corrective action | **corrigerende maatregel** | NEN-EN-ISO 9000 | |
| preventive action | **preventieve maatregel** | NEN-EN-ISO 9000 | |
| continuous improvement | **continue verbetering** | NEN-EN-ISO 9000 | |
| audit | **audit** | NEN-EN-ISO 19011 | |
| test | **beproeving** | | *Test* accepted in IT context |
| inspection | **inspectie** | | |
| certificate of conformity | **conformiteitsverklaring** | | |
| type examination | **typeonderzoek** | | |
| production surveillance | **productiebewaking** | | |
| factory production control | **fabrieksproductiecontrole (FPC)** | | |
| CE marking | **CE-markering** | | Keep CE; *markering* not *merk* |
| notified body | **aangemelde instantie** | | |

### Table T11: Numerical and Mathematical Conventions

| English Convention | Dutch Convention | Example (EN -> NL) |
|--------------------|------------------|-------------------|
| Decimal point (.) | **Decimale komma (,** ) | 3.14 -> 3,14 |
| Thousands separator (,) | **Punt (.)** or **spatie** | 1,234,567 -> 1.234.567 or 1 234 567 |
| Digit grouping | Groups of 3, space optional | 25 000 (preferred) or 25.000 |
| Percentage spacing | 50 % (space) | 50% (no space) OR 50 % (space) — be consistent |
| Range dash | **tot en met / t/m** or **en dash (–)** | 10-15 mm -> 10 mm tot en met 15 mm OR 10 mm–15 mm |
| Multiplication sign | **x** or **·** | 2 x 3 or 2 · 3 |
| Dimensions order | Same as English | 10 x 20 x 30 mm |
| Equation punctuation | None after displayed equation | Follow English convention |
| Variable names | **cursief (italic)** | Same as English |
| Units after number | **space** (hard space preferred) | 25 mm (with space) |

### Table T12: Common Anglicisms to Avoid

| Incorrect Anglicism | Correct Dutch | Reason |
|---------------------|---------------|--------|
| *voltage* | **spanning** | Pure anglicism |
| *current* | **stroom** / **stroomsterkte** | Pure anglicism |
| *pressure* | **druk** | Pure anglicism |
| *power* (electrical) | **vermogen** | False friend |
| *event* | **gebeurtenis** / **situatie** | Anglicism in safety context |
| *scenario* | **situatie** / **scenario** | *Scenario* is acceptable in risk analysis |
| *implement* | **implementeren** / **uitvoeren** | *Uitvoeren* preferred; *implementeren* accepted formally |
| *initial* | **initieel** / **aanvankelijk** / **eerste** | *Aanvankelijk* preferred |
| *optimaliseren* | OK — fully accepted | Dutch verb fully adopted |
| *configureren* | OK — fully accepted | Dutch verb fully adopted |
| *specification* | **specificatie** | Accepted |
| *guarantee* | **garantie** | Accepted (note: 'g' not 'u') |
| *design* | **ontwerp** | *Design* is an anglicism; use *ontwerp* |
| *engineer* | **ingenieur (ing./ir.)** | Use Dutch academic titles |
| *maintenance* | **onderhoud** | Anglicism; use *onderhoud* |
| *performance* | **prestatie** | *Prestatie* not *performance* |
| *tolerance* | **tolerantie** | Accepted |
| *failure* | **storing** / **fout** / **defect** | Context-dependent |

---

## 3. Standards

### 3.1 NEN Standards System

| Standard Series | Domain | Relevance |
|-----------------|--------|-----------|
| NEN-EN-ISO 12100 | Safety of machinery — general principles | Fundamental safety terminology |
| NEN-EN-ISO 13849-1 | Safety-related parts of control systems | PL determination |
| NEN-EN-IEC 62061 | Functional safety — machinery | SIL determination |
| NEN-EN-IEC 60204-1 | Electrical equipment of machines | Electrical safety in machinery |
| NEN-EN 1990 series | Eurocode — structural design | Civil/structural engineering |
| NEN-EN 1090 series | Execution of steel/aluminium structures | CE marking of structural components |
| NEN-EN-ISO 9001 | Quality management | Quality terminology |
| NEN-EN-ISO 14001 | Environmental management | Environmental terminology |
| NEN 1000 | SI units — rules for use | Unit conventions |
| NEN-EN-ISO 80000-1 | Quantities and units — general | Quantity conventions |
| NEN-EN 45020 | Standardisation and related activities | Standardisation terminology |
| NEN-EN-ISO 17025 | Testing and calibration laboratories | Laboratory terminology |
| NEN-EN-ISO 9712 | NDT personnel qualification | Inspection terminology |
| NEN 3210 | Technical drawings — dimensioning | Drawing conventions |
| NPR 5310 | Maintenance terminology | Maintenance terms (NPR = practical guideline) |

### 3.2 Spelling and Terminology Rules

1. **SI unit symbols are never translated**: mm, cm, m, km, kg, g, N, Pa, W, V, A, Hz, etc. Always use international symbols.
2. **SI unit names are Dutch**: *meter*, *kilogram*, *seconde*, *ampère*, *kelvin*, *candela*, *mol*. Never capitalise unit names in running text (except *ampère* and *kelvin* when they begin a sentence).
3. **Decimal comma**: Always use the decimal comma (3,14) not decimal point (3.14).
4. **Thousands separator**: Use a dot or (preferred in modern NL) a thin space: 1.234.567 or 1 234 567.
5. **NEN standard references**: Prepend *NEN-* to EN and ISO standards (e.g., ISO 12100 becomes NEN-EN-ISO 12100). Exception: when the DUTCH national annex differs, explicitly note *NEN-EN* plus the Dutch national annex reference.
6. **Modal verb consistency**: Use *moeten* for binding requirements, *behoren te* for recommendations, *mogen* for permissions. Never mix within a single document.
7. **Compound nouns**: Always write as one word unless this creates ambiguity: *veiligheidsvoorziening*, *noodstop*, *grenswaarde*, *meetnauwkeurigheid*.
8. **Anglicisms**: Where a Dutch equivalent exists in NEN standards, use the Dutch term. Loanwords fully adopted (e.g., *computer*, *sensor*, *protocol*) are acceptable.
9. **Hyphenation**: Use hyphen in compounds where vowel collision occurs (e.g., *auto-ongeval*, *na-apen*). In technical compounds, hyphenate only when needed for readability.
10. **Abbreviations**: Define at first use. Use standard Dutch abbreviations (e.g., *m.b.t.* = met betrekking tot, *o.a.* = onder andere, *d.m.v.* = door middel van).

### 3.3 Document Structure Standards

- **Normative text** uses present tense, active voice when possible, passive voice for procedures.
- **Clause numbering** follows NEN-EN-ISO style: 1, 1.1, 1.1.1 (max 4 levels).
- **Tables** are numbered sequentially (Tabel 1, Tabel 2) and referenced as *Tabel 1*.
- **Figures** are numbered sequentially (Figuur 1, Figuur 2).
- **Equations** are numbered in parentheses (1), (2).
- **Notes** use the format: OPMERKING 1, OPMERKING 2 (always *opmerking* not *noot*).
- **Examples** use: VOORBEELD 1, VOORBEELD 2.
- **Cross-references**: *zie Tabel 1*, *zie Figuur 2*, *zie artikel 5.3.2*.

### 3.4 Safety Sign and Warning Text Translation

| English Signal Word | Dutch Signal Word | Colour | When Used |
|---------------------|-------------------|--------|-----------|
| DANGER | **GEVAAR** | Red/white | Imminent hazardous situation |
| WARNING | **WAARSCHUWING** | Orange/black | Potentially hazardous situation |
| CAUTION | **VOORZICHTIG** | Yellow/black | Minimally hazardous situation |
| NOTICE | **OPMERKING** | Blue/white | Property damage / important info |

- Signal words are always uppercase and bold in Dutch.
- The warning text that follows uses sentence case.
- Safety messages follow the structure: **GEVAAR**: [consequence] + [avoidance action].
- Use the imperative mood for avoidance actions: *Draag beschermende handschoenen*, *Schakel spanning uit vóór onderhoud*.

### 3.5 Quality Assurance Notes for Translators

1. Verify all NEN/EN/ISO standard numbers against the NEN catalog before finalising.
2. Ensure every SI unit uses the correct international symbol with a space before the value.
3. Confirm that decimal commas are used consistently throughout — many documents mix comma and point.
4. Check that all modal verbs are consistent with the normative status of each clause.
5. Cross-reference all safety level designations (SIL, PL, Category) with the applicable NEN standard.
6. Verify that compound nouns are correctly spelled as one word per the *Groene Boekje*.
7. For CE-marking documentation, ensure that the translation matches the EU Official Journal terminology.
