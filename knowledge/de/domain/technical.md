---
id: de/domain/technical
type: domain
target_lang: de
domain: technical
aliases: [technische-Dokumentation, DIN-Normen, technisches-Deutsch, engineering-German, technische-Redaktion]
---

# Technical Domain: German Translation Standards

## Reader Model

**Primary Reader:** German-speaking engineer, technician, or quality manager (Fachkraft, technischer Redakteur, Ingenieur). The reader expects precision, unambiguous terminology, and strict adherence to German industrial norms (DIN/ISO/EN). They scan documents for actionable information, safety instructions, and specification data. The reader tolerates no ambiguity in torque values, tolerances, material grades, or safety classifications. They are accustomed to DIN A4 formatted documentation, structured according to DIN EN 82079-1 (Gebrauchsanleitungen) or VDI 4500 (Technische Dokumentation).

**Secondary Reader:** Regulatory auditor (TÜV, ZLS, BG, DGUV) or standards body reviewer. They verify compliance with applicable DIN EN ISO standards, Maschinenrichtlinie (2006/42/EG), Niederspannungsrichtlinie (2014/35/EU), and Betriebssicherheitsverordnung (BetrSichV). Deviations from normative terminology are grounds for rejection or certificate revocation. Every safety warning must follow the prescribed hazard severity levels (Gefahrenstufen).

**Tertiary Reader:** Service technician or operator in the field who relies on the documentation for installation, maintenance, and troubleshooting. They need clear, unambiguous instructions. Compound nouns (Komposita) should be formed for precision but kept readable.

**Reader Priorities:**
1. Correct normative references (DIN EN ISO 1234 instead of simply "ISO 1234")
2. Consistent terminology within document and across product family (Terminologiearbeit)
3. Safety warnings in prescribed Hazard Severity Levels (Gefahrenstufen nach ANSI Z535 / DIN EN 82079-1 / ISO 3864-2)
4. Numerical accuracy: decimal comma, thousand separator according to DIN 1333
5. Passive constructions for process description, imperative for warnings and instructions
6. Compound noun formation (Kompositum) according to Duden standards with readability limits
7. Standardized abbreviations (z. B., usw., d. h., max., mind.)
8. DIN 5008 document formatting: date, time, units, number ranges, lists, tables

---

## Decision Framework

### Table 1: DIN-Referenced Terminology — Mandatory Equivalence

| Source Term | German Normative Term | Standard | Notes |
|-------------|----------------------|----------|-------|
| emergency stop device | NOT-HALT-Einrichtung | DIN EN ISO 13850 | All-caps NOT-HALT per standard |
| emergency off | NOT-AUS | DIN EN ISO 13850 | Distinct from NOT-HALT |
| protective earth conductor | Schutzleiter (PE) | DIN VDE 0100-540 | |
| limit switch | Endschalter / Positionsschalter | DIN EN 60947-5-1 | |
| safety relay | Sicherheitsschaltgerät / Sicherheitsrelais | DIN EN 62061 | |
| guard / protective device | Schutzeinrichtung / trennende Schutzeinrichtung | DIN EN ISO 14120 | |
| interlocking device | Verriegelungseinrichtung | DIN EN ISO 14119 | |
| two-hand control device | Zweihandschaltung / Zweihandbedienung | DIN EN ISO 13851 | |
| enabling device | Zustimmschaltung / Zustimmtaster | DIN EN ISO 13851 | |
| sensitive protective equipment | berührungslos wirkende Schutzeinrichtung (BWS) | DIN EN 61496 | |
| electromagnetic compatibility | Elektromagnetische Verträglichkeit (EMV) | DIN EN 55011 | |
| programmable logic controller | Speicherprogrammierbare Steuerung (SPS) | DIN EN 61131 | |
| human-machine interface | Mensch-Maschine-Schnittstelle (MMS) / Bediengerät | DIN EN ISO 9241 | |
| rated voltage | Bemessungsspannung / Nennspannung | DIN VDE 0100 | |
| overload protection | Überlastschutz | DIN VDE 0100 | |
| short-circuit protection | Kurzschlussschutz | DIN VDE 0100 | |
| thermal protection | Thermoschutz / Temperaturüberwachung | DIN VDE | |

**Rule:** Always verify the standard reference for each technical term. The DIN/EN/ISO designation takes priority over colloquial industry usage. On first occurrence in a document, include the full standard reference: "NOT-HALT-Einrichtung (DIN EN ISO 13850)".

### Table 2: Safety Warning Levels (DIN EN 82079-1 / ANSI Z535 / ISO 3864-2)

| English Signal Word | German Signal Word | Color (ISO 3864-2) | Meaning | Hazard Level |
|--------------------|--------------------|--------------------|---------|-------------|
| DANGER | GEFAHR | Red background, white text | Imminent hazard causing death or serious injury | Highest |
| WARNING | WARNUNG | Orange background, black text | Potential hazard that could cause death or serious injury | High |
| CAUTION | VORSICHT | Yellow background, black text | Potential hazard that could cause minor or moderate injury | Medium |
| NOTICE | HINWEIS | Yellow background, black text (or blue) | Property damage only, no personal injury | Low |
| SAFETY INSTRUCTION | SICHERHEITSHINWEIS | Green (safe condition) | Safety-related information / safe condition | Informational |
| IMPORTANT | WICHTIG | (No specific color) | Important operational information | Informational |

**Warning structure (4-block format per DIN EN 82079-1):**
1. Signalwort (signal word): "GEFAHR"
2. Art und Quelle der Gefahr (type and source of hazard): "Berühren spannungsführender Teile"
3. Folge bei Nichtbeachtung (consequence): "führt zu lebensgefährlichem Stromschlag"
4. Maßnahmen zur Vermeidung (measures to avoid): "Vor Wartungsarbeiten allpolig vom Netz trennen"

**Example:**
```
GEFAHR

Berühren spannungsführender Teile führt zu lebensgefährlichem Stromschlag.
Vor Wartungsarbeiten allpolig vom Netz trennen und Spannungsfreiheit feststellen.
```

### Table 3: Numerical Formatting (DIN 1333, DIN 5008)

| Element | English Convention | German Convention (DIN 1333/5008) | Example |
|---------|--------------------|------------------------------------|---------|
| Decimal separator | Period (3.14) | Comma (3,14) | "3,14" not "3.14" |
| Thousand separator | Comma (1,234) | Period or thin space (1.234 / 1 234) | "12.345,67" or "12 345,67" |
| Tolerance notation | ± with space | Same, but with German decimals | "10 ± 0,5" |
| Dimensions | 5 mm x 10 mm | 5 mm x 10 mm | "x" not "×"; spaces around x |
| Range | 5-10 mm | 5 mm bis 10 mm / 5-10 mm | "bis" preferred in formal texts |
| Fraction | 1/2 | 1/2 (same) | Fractions use same symbol |
| Angular degrees | 90 degrees / 90° | 90° / 90 Grad | "90°" with space? DIN 5008: no space |
| Percentage | 5% | 5 % | Mandatory space before % |
| Significant digits | 3.0 | 3,0 | Trailing zero kept for precision |
| Engineering notation | 1.2e3 | 1,2e3 / 1,2 · 10^3 | Decimal comma in mantissa |
| Units | 5mm | 5 mm | Mandatory space between number and unit |

### Table 4: Compound Noun Formation (Kompositum)

| Rule | English Example | German Compound | Notes |
|------|----------------|-----------------|-------|
| Two stems, simple | pressure valve | Druckventil | Direct combination |
| Two stems, with linker | safety device | Sicherheit-e-s-vorrichtung | -e- linker |
| Three stems | high-pressure pump | Hochdruckpumpe | No linker |
| Three stems, with linker | pressure relief valve | Druckentlastung-s-ventil | -s- linker |
| Four stems | surface mount technology | Oberflächenmontage-technologie | -n- linker |
| Five stems | high-pressure fuel injection pump | Hochdruck-Kraftstoff-Einspritzpumpe | Hyphenation recommended |
| Six+ stems | compressed air maintenance unit | Druckluft-Wartungseinheit | Hyphenation required |
| With number | 12-pin connector | 12-poliger Stecker / 12-Pol-Stecker | Adjectival or hyphenated |
| English loan compound | cloud-based solution | Cloud-basierte Lösung / Cloud-Lösung | Hyphenate Anglicism compounds |
| Proper noun in compound | M8 thread | M8-Gewinde | Hyphen before proper noun part |

**Guidelines:**
- Maximum ~6 constituent stems before hyphenation is recommended
- Linking elements (-e-, -en-, -er-, -n-, -s-, -es-) follow Duden rules, not guesswork
- When in doubt, check Duden Online or the relevant DIN standard for the established compound
- Hyphenated compounds are increasingly acceptable in technical German for clarity
- Do not create compounds that combine German and English stems (e.g., not "Fehler-detection-system" but "Fehlererkennungssystem")

### Table 5: Verb Position and Sentence Structure — Technical German

| Text Type | English Example | German Translation | Grammatical Rule |
|-----------|----------------|-------------------|------------------|
| Process description | "The device measures temperature." | "Das Gerät misst die Temperatur." | Present tense, active, verb position 2 |
| Specification | "The housing is made of stainless steel." | "Das Gehäuse besteht aus Edelstahl." | Present tense, active or sein-passive |
| Function description | "When the button is pressed, the motor starts." | "Wird der Taster gedrückt, startet der Motor." | V1 conditional, verb-final in subordinate clause |
| Instruction (manual action) | "Press the button." | "Taste drücken." | Infinitive phrase (common in manuals) |
| Instruction (formal) | "The button must be pressed." | "Die Taste ist zu drücken." | "ist zu" + infinitive (modal passive) |
| Instruction (imperative) | "Press the button." | "Drücken Sie die Taste." | Formal imperative (less common in manuals) |
| Safety warning | "Do NOT touch live parts." | "Spannungsführende Teile nicht berühren." | Negated infinitive |
| Condition | "If pressure exceeds 10 bar, the valve opens." | "Überschreitet der Druck 10 bar, öffnet sich das Ventil." | V1 conditional (standard in technical German) |
| Result | "As a result, the system shuts down." | "Infolgedessen schaltet das System ab." | Adverb at position 1, verb at position 2 |
| List item | "Check the seal." | "Dichtung prüfen." | Accusative object + infinitive (Nominalstil) |

### Table 6: Anglicism Evaluation in Technical German

| English Term | Preferred German Equivalent | Acceptable Anglicism? | Standard Source |
|-------------|----------------------------|----------------------|-----------------|
| actuator | Stellantrieb | No (except specific contexts) | DIN VDE/VDI |
| controller | Regler / Steuerung | No (use "Controller" only for game controllers) | DIN |
| sensor | Sensor | Yes (established international) | DIN |
| actuator (process) | Stellglied / Aktor | "Aktor" acceptable in automation engineering | DIN |
| cloud computing | Cloud-Computing | Yes (hyphenated per Duden) | Duden |
| dashboard (IT) | Dashboard / Armaturenbrett (vehicle) | Yes (IT), No (vehicle) | Context-dependent |
| drive | Antrieb | No | DIN |
| encoder | Drehgeber / Encoder | Both accepted | DIN/VDI |
| fieldbus | Feldbus | No (established German term) | DIN EN |
| firmware | Firmware | Yes | |
| gateway | Gateway | Yes (technical) | |
| hardware | Hardware | Yes | |
| interface | Schnittstelle | No (except IT where "Interface" is used) | DIN |
| machine learning | Maschinelles Lernen | Both accepted | |
| maintenance | Wartung | No | DIN 31051 |
| actuator (hydraulic) | Arbeitszylinder / Stellzylinder | No | |
| PCB / printed circuit board | Leiterplatte (LP) | No (not "PCB") | DIN |
| PLC | SPS (Speicherprogrammierbare Steuerung) | No (use German abbreviation) | DIN EN 61131 |
| repair | Instandsetzung | No | DIN 31051 |
| sensor | Sensor | Yes | |
| software | Software | Yes | |
| torque | Drehmoment | No | DIN |
| valve | Ventil | Yes (international) | |

### Table 7: Standardized German Abbreviations in Technical Documents

| English Abbreviation | German Equivalent | Full German Form | DIN Source |
|---------------------|-------------------|------------------|------------|
| e.g. | z. B. | zum Beispiel | DIN 5008 |
| i.e. | d. h. | das heißt | DIN 5008 |
| etc. | usw. | und so weiter | DIN 5008 |
| cf. | vgl. | vergleiche | DIN 5008 |
| vs. | ggü. | gegenüber | |
| approx. | ca. | circa / zirka | |
| max. | max. | maximal (same) | |
| min. | mind. | mindestens | Not to be confused with "min." for Minute |
| min. (time) | Min. | Minute | Context-dependent |
| no. / # | Nr. | Nummer | |
| RPM | 1/min | Umdrehungen pro Minute | "1/min" in standards; "U/min" in operations |
| Pcs. / pcs. | St. / Stck. | Stück | |
| mm | mm | Millimeter (same) | |
| kg | kg | Kilogramm (same) | |
| A | A | Ampere (same) | |
| V | V | Volt (same) | |
| W | W | Watt (same) | |
| Hz | Hz | Hertz (same) | |
| Nm | Nm | Newtonmeter (same) | |
| bar | bar | Bar (same) | |
| l/min | l/min | Liter pro Minute (same) | |
| °C | °C | Grad Celsius (same) | |
| mm² | mm² | Quadratmillimeter | Superscript 2 |
| ID | ID / Kennung | Identifikation / Identifikator | "ID" acceptable |
| SN | Serien-Nr. | Seriennummer | |
| Art. No. | Art.-Nr. | Artikelnummer | |
| Order No. | Best.-Nr. | Bestellnummer | |

### Table 8: Measurement Units and Formatting (DIN 5008 / DIN 1301 / DIN 1302)

| Unit Type | Standard | Format Rule | Example |
|-----------|----------|-------------|---------|
| SI base units | DIN 1301 | Space before unit, lowercase except L | "5 m", "10 kg", "3 A" |
| SI derived (named) | DIN 1301 | Space before unit | "12 N", "24 V", "100 W" |
| Temperature | DIN 1301 | Space before °C | "25 °C" |
| Pressure | DIN 1301 | Space before unit | "10 bar" (not "bar" capitalized) |
| Angle | DIN 1301 | No space before ° symbol | "90°" (but "90 Grad" with space) |
| Time (short) | DIN 5008 | Colon separator | "14:30 Uhr" |
| Time (long) | DIN 5008 | "Stunden, Minuten" | "3 Stunden 15 Minuten" |
| Date (numeric) | DIN 5008 / ISO 8601 | Dots or hyphens | "31.12.2025" or "2025-12-31" |
| Date (text) | DIN 5008 | Day + month name + year | "31. Dezember 2025" |
| Currency | DIN 5008 | Space between amount and symbol | "12,50 EUR" or "EUR 12,50" |
| Telephone | DIN 5008 | Country code, area code, subscriber | "+49 711 1234-567" |
| Speed | DIN 1301 | Slash for "per" | "50 km/h" (not "kmh") |

### Table 9: List and Table Formatting (DIN 5008)

| Element | English Convention | German Convention | Example (German) |
|---------|--------------------|-------------------|------------------|
| Bullet list items | Capitalize each, end with period | Lowercase start, semicolon internal, period final | "- Funktion A aktivieren; - Funktion B prüfen." |
| Numbered steps | Imperative, each ends with period | Imperative (infinitive), each ends with period | "1. Gerät ausschalten. 2. Netzstecker ziehen." |
| Table headers | Capitalize each word (title case) | Capitalize first word only (Nominalstil) | "| Produkt | Menge | Preis |" |
| Table caption | "Table 1: ..." | "Tabelle 1: ..." | "Tabelle 1: Technische Daten" |
| Figure caption | "Figure 1: ..." | "Bild 1: ..." or "Abbildung 1: ..." | "Bild 1: Aufbau des Geräts" |
| Note / remark | "Note:" | "Anmerkung:" / "Hinweis:" | "Anmerkung: Die Werte gelten bei 20 °C." |
| Warning in table | (Red row/column) | "Achtung:" or "Vorsicht:" | "Achtung: Nur für geschultes Personal." |
| Cross-reference | "see Table 1" | "siehe Tabelle 1" | "Siehe auch Abschnitt 3.2" |

### Table 10: Technical Drawing and Dimensioning Terms

| English | German | Standard |
|---------|--------|----------|
| dimension | Maß / Abmaß (tolerance) | DIN ISO |
| nominal dimension | Nennmaß | DIN ISO 2768 |
| tolerance | Toleranz | DIN ISO 2768 |
| upper deviation | oberes Abmaß (ES/es) | DIN ISO 286 |
| lower deviation | unteres Abmaß (EI/ei) | DIN ISO 286 |
| fit | Passung | DIN ISO 286 |
| clearance fit | Spielpassung | DIN ISO 286 |
| interference fit | Übermaßpassung / Presspassung | DIN ISO 286 |
| transition fit | Übergangspassung | DIN ISO 286 |
| surface finish | Oberflächenbeschaffenheit | DIN EN ISO 1302 |
| roughness | Rautiefe / Rauheit | DIN EN ISO 4287 |
| centre line | Mittellinie | DIN ISO 128 |
| projection | Ansicht / Projektion | DIN ISO 128 |
| section view | Schnittansicht / Schnitt | DIN ISO 128 |
| detail view | Detailansicht / Einzelheit | DIN ISO 128 |
| scale | Maßstab | "M 1:2" (not "scale 1:2") |
| thread | Gewinde | DIN 13 (metric), DIN EN 10226 (pipe) |
| chamfer | Fase / Anfasung | DIN ISO 13715 |
| radius | Radius (R) | "R 5" |
| diameter | Durchmesser (Ø / D) | "Ø 10 mm" |
| welding symbol | Schweißzeichen | DIN EN ISO 2553 |
| material specification | Werkstoffangabe | DIN EN / Werkstoffnummer |

### Table 11: Maintenance and Inspection Terminology

| English | German | DIN Standard | Definition |
|---------|--------|--------------|------------|
| maintenance | Instandhaltung | DIN 31051 | Oberbegriff (umbrella term) |
| servicing / maintenance | Wartung | DIN 31051 | Maßnahmen zur Verzögerung des Abbaus des Abnutzungsvorrats |
| inspection | Inspektion | DIN 31051 | Feststellung und Beurteilung des Ist-Zustands |
| repair | Instandsetzung | DIN 31051 | Maßnahmen zur Rückführung in den funktionsfähigen Zustand |
| improvement | Verbesserung | DIN 31051 | Steigerung der Funktionssicherheit |
| overhaul | Generalüberholung | | Complete refurbishment |
| preventive maintenance | vorbeugende Instandhaltung | DIN 31051 | |
| predictive maintenance | zustandsorientierte Instandhaltung | DIN 31051 | |
| corrective maintenance | korrektive Instandhaltung | DIN 31051 | |
| scheduled maintenance | planmäßige Instandhaltung | DIN 31051 | |
| lubrication | Schmierung | | |
| calibration | Kalibrierung | DIN EN ISO/IEC 17025 | |
| adjustment | Justierung | DIN 1319 | |
| verification | Verifizierung / Überprüfung | DIN EN ISO 9000 | |
| validation | Validierung | DIN EN ISO 9000 | |
| functional test | Funktionstest / Funktionsprüfung | | |

### Table 12: Normative Cross-Reference Format

| Element | English Format | German Format | Example |
|---------|---------------|---------------|---------|
| Standard with year | ISO 13857:2019 | DIN EN ISO 13857:2020-06 | Full reference with month |
| Standard without year | ISO 13857 | DIN EN ISO 13857 | Implicitly latest version |
| Directive | Directive 2006/42/EC | Richtlinie 2006/42/EG | |
| Regulation | EU Regulation 2016/425 | EU-Verordnung 2016/425 | |
| In-text reference | "according to ISO 13857" | "nach DIN EN ISO 13857" | "nach" preferred over "gemäß" |
| In-text section | "Section 5.2" | "Abschnitt 5.2" | |
| In-text table | "see Table 3" | "siehe Tabelle 3" | |
| Amendment | "ISO 13857:2019/Amd 1:2021" | "DIN EN ISO 13857:2020-06/A1:2021" | |
| Withdrawn standard | "withdrawn" | "zurückgezogen" | Mark clearly if replacing |

### Table 13: Technical Documentation Structure (VDI 4500 / DIN EN 82079-1)

| Section | Content | Language Style | Required for CE? |
|---------|---------|---------------|------------------|
| Deckblatt / Titelblatt | Product name, document ID, date, version | Nominal | Yes |
| Inhaltsverzeichnis | Table of contents | Nominal | Yes |
| Einleitung / Zweck | Purpose, target audience | Descriptive, present tense | Yes |
| Sicherheit / Grundlegende Sicherheitshinweise | General safety instructions | Warnings per hazard levels | Yes |
| Bestimmungsgemäße Verwendung | Intended use | Declarative, precise | Yes |
| Technische Daten | Specifications | Table format, nominal | Yes |
| Transport und Lagerung | Transport and storage | Imperative/infinitive | Yes |
| Montage / Installation | Assembly / installation | Step-by-step, imperative | Yes |
| Inbetriebnahme | Commissioning / startup | Step-by-step, imperative | Yes |
| Bedienung | Operation | Imperative, procedural | Yes |
| Wartung | Maintenance | Imperative, periodic tasks | Yes |
| Störungsbehebung | Troubleshooting | Table: problem -> cause -> remedy | Yes |
| Außerbetriebnahme / Entsorgung | Decommissioning / disposal | Imperative, environmental | Yes |
| Kundendienst / Service | Customer service contact | Contact details | Yes |
| EG-Konformitätserklärung | EC Declaration of Conformity | Fixed legal text | Yes |
| Anhang / Anlagen | Appendices | Diagrams, parts lists | Optional |

### Table 14: Electrical Engineering — VDE Terminology

| English | German | VDE/DIN Standard |
|---------|--------|------------------|
| low voltage | Niederspannung | DIN VDE 0100-200 |
| extra-low voltage | Kleinspannung | DIN VDE 0100-200 |
| safety extra-low voltage (SELV) | Sicherheitskleinspannung (SELV) | DIN VDE 0100-410 |
| protective extra-low voltage (PELV) | Schutzkleinspannung (PELV) | DIN VDE 0100-410 |
| overvoltage category | Überspannungskategorie | DIN VDE 0110 |
| insulation coordination | Isolationskoordination | DIN VDE 0110 |
| degree of protection (IP) | Schutzart (IP) | DIN EN 60529 |
| protection class (equipment) | Schutzklasse (SK I / SK II / SK III) | DIN VDE 0100 |
| rated current | Bemessungsstrom / Nennstrom | DIN VDE |
| rated voltage | Bemessungsspannung / Nennspannung | DIN VDE |
| short-circuit current | Kurzschlussstrom | DIN VDE 0102 |
| residual current device (RCD) | Fehlerstromschutzeinrichtung (RCD / FI-Schalter) | DIN VDE 0664 |
| circuit breaker | Leitungsschutzschalter (LS-Schalter) | DIN VDE 0641 |
| grounding / earthing | Erdung | DIN VDE 0100-540 |
| potential equalization | Potentialausgleich | DIN VDE 0100-410 |
| electric shock | elektrischer Schlag | DIN VDE 0100 |
| arc fault | Störlichtbogen / Lichtbogenfehler | DIN VDE |

---

## Standard Conventions

### DIN 5008 General Formatting Rules for Technical Documents

- **Paper size:** DIN A4 (210 mm x 297 mm) — standard for all technical documentation
- **Font:** DIN 1451 (DIN-Schrift) for warnings; standard sans-serif (Arial, Helvetica) for body text
- **Margins:** Left 2.5 cm, right 1.5 cm (minimum), top/bottom 2 cm
- **Line spacing:** 1.5 lines for body text; single for tables
- **Page numbers:** Bottom right or center; title page often unnumbered

### Numeric Literacy (Zahlenverständnis)

In technical German, numbers are read and written with the decimal comma. This is critical for:
- **Torque values:** "5,5 Nm" (not 5.5 Nm) — a misplaced dot changes the meaning
- **Tolerances:** "10 ± 0,5 mm" (not 10 ± 0.5 mm)
- **Temperatures:** "37,5 °C" (not 37.5 °C)
- **Percentages:** "4,5 %" (not 4.5%)
- **Current:** "2,5 A" (not 2.5 A)

### Product Identification

German technical documents use standardized product identification:
- **Type plate (Typenschild):** Contains: Hersteller, Typ, Serien-Nr., Baujahr, technische Daten
- **Article number:** "Art.-Nr.: 1234-5678"
- **Serial number:** "Serien-Nr.: SN-2025-00042"
- **Version / Revision:** "Version 1.2 / Rev. 03 / Stand: Januar 2025"
- **Document number:** "Dok.-Nr.: BA-1234-DE" (BA = Betriebsanleitung)

### Use of German in Technical Writing

- Avoid English filler words: "please note" -> "beachten Sie" / "zu beachten"
- Use "siehe" for cross-references (not "see")
- Use "Hinweis" for notes (not "Note")
- Use "Vorsicht" for CAUTION-level property damage warnings
- Use "Achtung" is falling out of favor; "Vorsicht" is preferred for CAUTION
- Use "WARNUNG" and "GEFAHR" consistently per ISO 3864-2 color coding

---

## Standards Reference

| Standard | Scope | Key Requirements for Translation |
|----------|-------|--------------------------------|
| DIN EN 82079-1 | Erstellen von Gebrauchsanleitungen | Warning structure, language level, formatting |
| DIN EN ISO 20607 | Sicherheit von Maschinen — Betriebsanleitungen | Content structure for machine manuals |
| DIN 5008 (2020) | Schreib- und Gestaltungsregeln | Formatting, numerals, dates, units, lists |
| DIN 1333 | Zahlenangaben | Decimal comma, significant digits, rounding |
| DIN 1301 | Einheiten | SI unit names, symbols, prefixes |
| DIN 1302 | Mathematische Zeichen | Mathematical notation conventions |
| DIN 1451 | Schriften — Serifenlose Linear-Antiqua | Typeface for warnings (DIN-Schrift) |
| DIN EN ISO 17100 | Übersetzungsdienstleistungen | Quality requirements, review process |
| VDI 4500 (Blatt 1-7) | Technische Dokumentation | Terminology management, translation processes |
| DIN 2342 | Begriff der Terminologielehre | Terminology principles |
| ISO 704 | Terminology work | Term formation principles (incl. Kompositum) |
| DIN 2330 | Begriffe und Benennungen | Concept systems and term formation |
| DIN 31051 | Instandhaltung | Maintenance terminology |
| DIN VDE 0100 | Errichten von Niederspannungsanlagen | Electrical installation terminology |
| DIN EN ISO 13849-1 | Sicherheit von Maschinen — Steuerungen | Safety-related control systems |
| DIN EN ISO 12100 | Risikobeurteilung | Risk assessment terminology |
| DIN EN 60204-1 | Elektrische Ausrüstung von Maschinen | Machine electrical equipment |
| Maschinenrichtlinie 2006/42/EG | Machine Directive (EU) | CE marking, safety requirements |
| BetrSichV | Betriebssicherheitsverordnung | German implementation of MD |
| ProdSG | Produktsicherheitsgesetz | German product safety law |

## Glossary (Normative German Technical Terms)

| English | German (Normative) | Standard Source |
|---------|--------------------|-----------------|
| user manual / instructions | Betriebsanleitung / Gebrauchsanleitung | DIN EN 82079-1 |
| safety instruction | Sicherheitshinweis | DIN EN 82079-1 |
| intended use | bestimmungsgemäße Verwendung | DIN EN ISO 12100 |
| reasonably foreseeable misuse | vernünftigerweise vorhersehbare Fehlanwendung | DIN EN ISO 12100 |
| maintenance | Wartung | DIN 31051 |
| repair | Instandsetzung | DIN 31051 |
| inspection | Inspektion | DIN 31051 |
| improvement | Verbesserung | DIN 31051 |
| rated voltage | Bemessungsspannung | DIN VDE 0100 |
| overload protection | Überlastschutz | DIN VDE 0100 |
| limit switch | Endschalter | DIN EN 60947 |
| programmable logic controller | Speicherprogrammierbare Steuerung (SPS) | DIN EN 61131 |
| electromagnetic compatibility | Elektromagnetische Verträglichkeit (EMV) | DIN EN 55011 |
| technical report | Technischer Bericht | DIN 5008 |
| technical data sheet | Technisches Datenblatt | VDI 4500 |
| functional safety | Funktionale Sicherheit | DIN EN 61508 |
| risk assessment | Risikobeurteilung | DIN EN ISO 12100 |
| residual risk | Restrisiko | DIN EN ISO 12100 |
| protective measure | Schutzmaßnahme | DIN EN ISO 12100 |
| commissioning | Inbetriebnahme | DIN EN 82079-1 |
| decommissioning | Außerbetriebnahme | DIN EN 82079-1 |
| troubleshooting | Störungsbehebung / Fehlersuche | DIN EN 82079-1 |
| spare parts list | Ersatzteilliste | VDI 4500 |
| type plate | Typenschild | DIN EN |
| CE marking | CE-Kennzeichnung | EU legislation |
| declaration of conformity | Konformitätserklärung | EU legislation |
| degree of protection | Schutzart (IP) | DIN EN 60529 |
