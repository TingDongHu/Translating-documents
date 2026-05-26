---
id: it/domain/technical
type: domain
target_lang: it
name: Technical Domain (Settore Tecnico)
description: Italian Technical domain terminology and translation rules
---

# Technical Domain (Settore Tecnico)

## Reader Model: Destinatario della Traduzione Tecnica

### Primary Reader Profiles

| Profile | Description | Language Expectation | Review Lens |
|---------|-------------|---------------------|-------------|
| **Ingegnere progettista** (Design Engineer) | Native Italian speaker, reads EN technical documentation daily. Familiar with UNI standards. | Expects precise technical terminology. Tolerates anglicisms only when no Italian equivalent exists per UNI norms. | Verifies dimensional accuracy, material specs, tolerance values. Rejects ambiguous translations. |
| **Tecnico specializzato** (Specialized Technician) | Works with machinery, electrical systems, civil engineering. May have limited English. | Requires clear, unambiguous Italian. Safety information must be immediately comprehensible. | Scans for safety warnings, numerical values, measurement units. Confirms procedural steps are actionable. |
| **Responsabile qualità** (Quality Manager) | Audits documentation for ISO 9001 / UNI EN ISO compliance. Bilingual but demands regulatory precision. | Requires faithful rendering of normative references. Terminology must match UNI/CEN/ISO glossaries. | Cross-references standard numbers, dates, normative paragraphs. Checks disclaimer and certification statements. |
| **Traduttore tecnico junior** (Junior Technical Translator) | Learning the domain. Consults this guide as reference. | Needs explicit mapping rules, warnings about false friends, examples of correct/incorrect translations. | Uses decision tables to validate choices. Checks for consistency with prior translations in same project. |

### Reading Scenarios and Document Types

| Document Type | Typical Length | Urgency | Key Translation Challenge |
|--------------|---------------|---------|-------------------------|
| Manuale d'uso e manutenzione | 50-300 pp. | Medium | Consistent terminology across repetitive content |
| Specifica tecnica (capitolato) | 10-100 pp. | High | Numerical precision, normative cross-references |
| Relazione tecnica / calcoli | 5-50 pp. | Medium | Mathematical notation preserved, prose in natural IT |
| Certificato di conformità | 1-5 pp. | Very High | Legal weight; verbatim accuracy of standard references |
| Scheda di sicurezza (SDS) | 5-50 pp. | Critical | Regulated structure (REACH/CLP), hazard phrases from official EU translations |
| Brevetto / domanda di brevetto | 10-50 pp. | High | Claims language; narrow literal translation required |
| Norma UNI / CEI / ISO tradotta | 5-200 pp. | Medium | Must follow drafting rules of the standards body |

### Expectations and Cognitive Load

Technical readers operate under **high cognitive load**: they are focused on extracting actionable information, not appreciating prose style. Every ambiguity forces a pause that breaks concentration. Therefore:

1. **Terminological consistency is paramount**: A given EN term must map to the same IT term throughout the entire document. Synonym variation (e.g., using "spegnimento" and "arresto" interchangeably for "shutdown") is harmful.
2. **Syntax should be lightweight**: Avoid nested subordinate clauses. Prefer active voice ("premere il pulsante X") over passive ("il pulsante X deve essere premuto").
3. **Visual alignment**: Warnings, notes, and list structures must mirror the source layout. If the source uses a warning box, the target must too.
4. **False friends are forbidden**: "Attualmente" does not mean "actually" (it means "currently"); "eventualmente" does not mean "eventually" (it means "if needed/possibly").

---

## Decision Framework: Translation Tables

### Table 1: Measurement Units and Quantities

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| 12.5 mm | Dimensions | 12,5 mm | Replace decimal point with decimal comma. Use narrow non-breaking space before unit. | "12,5 mm" not "12.5 mm" |
| 1,000 rpm | Rotational speed | 1 000 giri/min | Use space as thousands separator (period is decimal). Convert rpm to "giri al minuto" or "giri/min" only in running text; in tables/figures, unit symbol stands. | "Velocita: 3 000 giri/min" |
| 100 °F | Temperature (non-EU) | 37,8 °C | Convert Fahrenheit to Celsius in parentheses: "100 °F (37,8 °C)" for informational contexts. In specs, preserve original and add converted value. | "Temperatura massima: 100 °F (37,8 °C)" |
| 5 ft 8 in | Height (imperial) | 1,73 m | Convert to metric with original in parentheses for context. | "Altezza: 1,73 m (5 ft 8 in)" |
| 10 gallons | Volume (US) | 37,85 L | Convert US gallons (not imperial). Specify "US gal" if ambiguous. | "Capacita: 37,85 L (10 US gal)" |

### Table 2: Technical Standards References

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| ISO 9001:2015 | Normative reference | ISO 9001:2015 | Standard numbers are NEVER translated. The standard number, year, and title are kept in the original language. Only the title may be parenthetically translated. | "secondo la ISO 9001:2015" |
| complies with EN 60204-1 | Declaration | conforme alla EN 60204-1 | "EN" becomes "EN" (European Norm kept). In Italian context, often written as "UNI EN 60204-1" when adopted nationally. Use "conforme a" not "compiante con". | "conforme alla UNI EN 60204-1" |
| according to ASTM D4236 | US standard reference | secondo ASTM D4236 | ASTM standards keep their designation. No translation of the standard body name. | "secondo ASTM D4236" |
| CE marking | Regulatory | marcatura CE | "CE" is kept. "marcatura CE" is the official Italian term. Note: CE stands for "Conformite Europeenne" and is not expanded. | "La marcatura CE e obbligatoria." |
| ANSI/ASME B16.5 | US pipe flange standard | ANSI/ASME B16.5 | Never translate. If describing the scope, use Italian description: "flange per tubazioni secondo ANSI/ASME B16.5". | "secondo ANSI/ASME B16.5" |

### Table 3: Safety Level Terminology

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| DANGER | Imminent hazard | PERICOLO | Always uppercase, bold, in Italian. Signal words are mandated by UNI 7547 and UNI EN ISO 7010. | "PERICOLO: Tensione pericolosa." |
| WARNING | Potential hazard | AVVERTENZA | Following UNI 7547 signal word hierarchy. | "AVVERTENZA: Superficie calda." |
| CAUTION | Minor hazard | ATTENZIONE | Lower severity than AVVERTENZA in Italian convention, though some standards map CAUTION to ATTENZIONE. | "ATTENZIONE: Rischio di schiacciamento." |
| NOTICE | Property damage | NOTA / AVVISO | Use NOTA for operational notes, AVVISO for property damage. Check client preference. | "NOTA: Serraggio a 5 Nm." |
| Danger: Moving parts | Safety sign text | Pericolo: organi in movimento | Safety message translated in full. Follow UNI EN ISO 7010 graphical symbol + text layout. | "PERICOLO: Organi in movimento." |

### Table 4: Verb Mood in Procedures

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| Press the button | Step-by-step instruction | Premere il pulsante | Italian uses the infinitive for imperative instructions in technical manuals, NOT the conjugated imperative. | "Premere il pulsante ON." |
| Do not open the cover | Prohibition | Non aprire il coperchio | Negative instruction uses "Non" + infinitive. | "Non aprire il coperchio quando il motore e in funzione." |
| The operator must wear PPE | Obligation | L'operatore deve indossare i DPI | "Deve" + infinitive for requirement. Formal register. | "L'operatore deve indossare guanti protettivi." |
| Ensure that... | Precaution | Accertarsi che... / Verificare che... | Reflexive impersonal form is preferred. | "Accertarsi che l'alimentazione sia disinserita." |
| It is recommended to... | Suggestion | Si raccomanda di... | "Si" impersonale + verb. | "Si raccomanda di effettuare la manutenzione annualmente." |

### Table 5: Technical False Friends (Falsi Amici Critici)

| English Term | Italian False Friend | Correct Translation | Explanation |
|-------------|---------------------|-------------------|-------------|
| actually | attualmente (= currently) | effettivamente, in realta | "Attualmente il sistema e offline" means "the system is currently offline", not "actually offline". |
| eventually | eventualmente (= if needed) | alla fine, infine | "Eventualmente, sostituire il filtro" means "replace the filter if needed", not "eventually replace the filter". |
| sensitive | sensibile (= responsive) | delicato, critico | "Dati sensibili" means "sensitive data" (personal data), but "componente sensibile" usually means "responsive component", not "critical component". |
| argument | argomento (= topic) | discussione, controversia | "L'argomento della tesi" = thesis topic, not "thesis argument" in the sense of a point being argued. |
| instructive | istruttivo (= educational) | informativo, con istruzioni | "Manuale istruttivo" is awkward; prefer "manuale con istruzioni" or "manuale informativo". |
| attend | attendere (= wait) | partecipare, presenziare | "Attendere la riunione" means "wait for the meeting", not "attend the meeting". |

### Table 6: Electrical and Electronic Terminology

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| ground (US) / earth (UK) | Electrical | terra, messa a terra | "Terra" for the physical connection. "Messa a terra" for the safety system. | "Collegare a terra prima della manutenzione." |
| mains power supply | Electrical | alimentazione di rete | "Rete" for mains. NOT "principale" (false friend). | "Tensione di alimentazione di rete." |
| wire / cable | General | cavo | "Filo" = single conductor (wire). "Cavo" = cable (insulated assembly). | "Cavo a 3 fili." |
| conduit | Cable protection | tubo protettivo, canalina | "Condotto" is a duct for air. For electrical: "tubo protettivo" or "canalina portacavi". | "Passare i cavi nella canalina." |
| circuit breaker | Overcurrent protection | interruttore automatico, disgiuntore | "Salvavita" is the residual-current device (RCD). "Interruttore automatico" is the correct term for circuit breaker. | "Interruttore automatico magnetotermico." |
| fuse | Overcurrent protection | fusibile | Straightforward. "Fusibile" is the exact term. | "Fusibile da 10 A." |

### Table 7: Materials Terminology

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| stainless steel AISI 304 | Material spec | acciaio inossidabile AISI 304 | Grade designation is kept. "Acciaio inox" is acceptable in less formal contexts. | "Acciaio inossidabile AISI 304." |
| mild steel | Carbon steel | acciaio al carbonio, acciaio dolce | "Acciaio dolce" is the traditional term; "acciaio al carbonio" is more common in modern specs. | "Pannello in acciaio al carbonio." |
| cast iron | Material | ghisa | No variation. | "Corpo in ghisa." |
| high-density polyethylene | Plastic | polietilene ad alta densita (PE-HD) | Abbreviation in parentheses on first use. | "PE-HD (polietilene ad alta densita)." |
| tempered glass | Glass treatment | vetro temperato | NOT "vetro temprato" (archaic). | "Finestra in vetro temperato." |

### Table 8: Software and UI Terminology

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| click / double-click | UI action | fare clic / fare doppio clic | "Cliccare" is widely used but considered informal. Formal documentation: "fare clic". | "Fare clic su OK per confermare." |
| scroll | UI action | scorrere | "Scrollare" is an anglicism. Use "scorrere". | "Scorrere verso il basso." |
| drag and drop | UI action | trascinamento | "Trascinamento" is the standard term. "Drag and drop" is understood but avoid. | "Funzione di trascinamento." |
| dropdown menu | UI element | menu a tendina, elenco a discesa | Both terms are used. "Elenco a discesa" is preferred in formal UI specs. | "Selezionare dal menu a tendina." |
| checkbox | UI element | casella di controllo | Official Microsoft term in Italian. "Checkbox" is understood but not recommended. | "Selezionare la casella di controllo." |
| placeholder text | UI element | testo segnaposto | "Placeholder" is common in developer speech; use "testo segnaposto" in UI strings. | "Inserire il testo segnaposto." |

### Table 9: Numerical Formatting

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| 3.14 | Mathematical constant | 3,14 | Replace period with comma as decimal separator. | "Valore di pi greco: 3,14159." |
| 1,000,000 | Large number | 1.000.000 or 1 000 000 | Period or space as thousands separator. Both are acceptable per UNI 9999. Space is preferred in tables to avoid confusion with decimal comma. | "Popolazione: 1 000 000." |
| 50% | Percentage | 50 % | Space between number and percent sign (Italian typographic rule). | "Rendimento: 85 %." |
| 25°C | Temperature | 25 °C | Space between number and degree symbol when followed by C/F. No space for standalone degrees (e.g., 90° angle). | "Temperatura: 25 °C." |
| 10:30 AM | Time (12h) | 10:30 | Convert to 24h format in running text. Use "h" in tables: "10:30" or "10.30" (both accepted). | "Alle ore 10:30." |

### Table 10: Technical Documentation Structure

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| Table of Contents | Front matter | Indice / Sommario | Use "Indice" for documents with numbered sections. "Sommario" for brief overview. | "Indice" |
| Revision History | Document control | Cronologia delle revisioni | Standard heading in Italian technical docs. | "Cronologia delle revisioni" |
| Scope | Section title | Scopo / Campo di applicazione | "Scopo" for short; "Campo di applicazione" for formal standards documents. | "Campo di applicazione" |
| Intended Use | Section title | Destinazione d'uso | Specific to EU regulatory context (MDR, IVDR, etc.) | "Destinazione d'uso" |
| Installation | Section title | Installazione | Simple translation. | "Installazione" |
| Maintenance | Section title | Manutenzione | "Manutenzione ordinaria" = routine maintenance; "Manutenzione straordinaria" = major maintenance. | "Manutenzione ordinaria" |
| Troubleshooting | Section title | Ricerca guasti / Risoluzione dei problemi | "Ricerca guasti" is traditional; "Risoluzione dei problemi" is also used (calque from EN). | "Ricerca guasti" |
| Technical Data | Section title | Dati tecnici | Use "Dati tecnici" (plural, masculine). NOT "Dato tecnico" (singular). | "Dati tecnici" |

### Table 11: Abbreviations and Acronyms

| Source Element (EN) | Context | Translation Decision (IT) | Rule | Example |
|---------------------|---------|--------------------------|------|---------|
| RPM | Abbreviation | giri/min | Expand on first use at document level. "RPM" may be kept in figures/diagrams for space. | "Velocita: 1 500 giri/min" |
| PPE | Acronym | DPI | "Dispositivi di Protezione Individuale". Acronym DPI is standard. | "Indossare sempre i DPI." |
| ESD | Acronym | ESD / scarica elettrostatica | ESD is internationally standardized. Italian text adds "scarica elettrostatica" on first use. | "Protezione ESD (scarica elettrostatica)." |
| PLC | Abbreviation | PLC | "Programmable Logic Controller" = "PLC" (kept). Definition in Italian: "controllore logico programmabile". | "PLC (controllore logico programmabile)." |
| HMI | Abbreviation | HMI | "Human-Machine Interface" = "HMI" (kept). Italian: "interfaccia uomo-macchina (IUM)". | "HMI (interfaccia uomo-macchina)." |

### Table 12: Warning and Caution Language Patterns

| Source Phrase (EN) | Translation Decision (IT) | Rule |
|--------------------|--------------------------|------|
| Do not operate this equipment without reading this manual. | Non utilizzare l'apparecchiatura senza aver letto il presente manuale. | Formal register: "il presente manuale" not "questo manuale". |
| Risk of electrical shock. | Rischio di scossa elettrica. | "Scossa elettrica" (not "shock elettrico"). |
| Keep away from children. | Tenere lontano dalla portata dei bambini. | Standard EU safety phrase. "Dalla portata dei bambini" = out of reach of children. |
| Use only in well-ventilated areas. | Utilizzare solo in aree ben ventilate. | "Ben ventilate" is standard. |
| Do not expose to moisture. | Non esporre all'umidita. | "Umidita" with no article following "a + l'". |
| Disconnect power before servicing. | Scollegare l'alimentazione prima della manutenzione. | "Scollegare" (not "disconnettere" which is for network connections). |

---

## Standards and Conventions

### Primary Standards Bodies Relevant to Italian Technical Translation

| Body | Full Name | Role in Translation |
|------|-----------|-------------------|
| **UNI** | Ente Nazionale Italiano di Unificazione | National standards body. Publishes UNI standards. Many are adoptions of EN/ISO standards. Translator must check if a UNI adoption exists. |
| **CEI** | Comitato Elettrotecnico Italiano | Electrical/electronic standards (Italian adoption of IEC/EN standards). |
| **CEN** | Comite Europeen de Normalisation | European standards body. EN standards adopted by EU member states including Italy. |
| **CENELEC** | Comite Europeen de Normalisation Electrotechnique | European electrotechnical standards. |

### Key Standards for Technical Documentation in Italian

| Standard | Title | Relevance |
|----------|-------|-----------|
| UNI 9999 | Regole per la scrittura dei numeri e delle misure | Defines decimal comma, thousands separator conventions. |
| UNI 7547 | Segnaletica di sicurezza | Defines safety sign signal words (Pericolo, Avvertenza, Attenzione). |
| UNI EN ISO 7010 | Simboli grafici. Colori e segnali di sicurezza | Internationally harmonized safety symbols. |
| UNI EN ISO 9001 | Sistemi di gestione per la qualita | Quality management; relevant for disclaimer and documentation structure translation. |
| UNI EN 82079-1 | Redazione delle istruzioni per l'uso | Rules for writing instructions. Relevant for manual structure. |
| UNI EN IEC 82045-1 | Principi e metodi per la gestione dei documenti | Document management principles. |

### Italian Typographic Conventions for Technical Documents

| Convention | Rule | Example |
|------------|------|---------|
| Decimal separator | Comma (not period) | 3,14 kg |
| Thousands separator | Period or space | 1.500.000 or 1 500 000 |
| Quotation marks | « » (preferred) or " " | «Messaggio di errore» |
| Dimensions | "x" or "×" | 100 × 200 mm |
| Range | "..." or "-" (EN-dash) | 10...50 °C or 10-50 °C |
| Time | 24h format | 14:30 (not 2:30 PM) |
| Date | DD/MM/YYYY or DD.MM.YYYY | 25/05/2026 |
| Units | Space before unit symbol | 10 kg (not 10kg) |

### Verification Checklist for Technical Translations

1. **Numerical accuracy**: Every number, decimal, and unit has been verified against source.
2. **Standard references**: UNI/EN/ISO standard numbers have not been translated.
3. **Safety terminology**: Signal words (Pericolo/Avvertenza/Attenzione) are correct for the hazard level.
4. **Terminology consistency**: Same EN term maps to same IT term throughout.
5. **False friends audit**: Checked for attualmente/eventualmente/sensibile and similar traps.
6. **Abbreviation protocol**: All acronyms defined on first use, UNI-standard abbreviations used.
7. **Procedural voice**: Infinitives used for step-by-step instructions.
8. **Visual structure**: Lists, warnings, and callout boxes preserved from source.
9. **Metric conversion**: Imperial-to-metric conversions applied, properly formatted.
10. **Registration marks**: Trademarks (TM, (R)) preserved from source per Italian law.
