# Polish Technical Domain: Reader Model + Decision Framework + Standards

---

## PART 1: READER MODEL

### 1.1 Target Reader Profile

| Attribute | Description |
|-----------|-------------|
| **Primary audience** | Polish engineers, technical translators, QA/QC inspectors, construction managers, certified welders, electricians (uprawnienia SEP), IT specialists |
| **Language variant** | Polski techniczny -- substandard of Standard Polish using heavy nominalization, impersonal passive constructions, and precise measurement terminology |
| **Proficiency required** | C1+ in general Polish + specialized vocabulary in engineering domain |
| **Expected text types** | Norms (normy PN/PN-EN), technical datasheets (karty katalogowe), installation manuals (instrukcje montazu), safety instructions (instrukcje BHP), technical approvals (aprobaty techniczne), declarations of performance (deklaracje wlasciwosci uzytkowych) |
| **Reader priorities** | Precision of measurement units, unambiguous procedural sequencing, traceability to standards, legal liability minimization |

### 1.2 Reader Expectations

| Expectation | Manifestation |
|-------------|---------------|
| **Metric-only system** | All measurements in SI units (mm, cm, m, kg, N, MPa, kW, kWh, deg C). No imperial units ever. |
| **Standard references** | Every technical claim must cite a PN, PN-EN, or PN-ISO standard number. E.g., "zgodnie z PN-EN 1993-1-1" |
| **Passive constructions** | "Nalezy wykonac..." / "Powinno sie stosowac..." / "Montaz przeprowadza sie..." |
| **Nominal style** | Nouns preferred over verbs: "wykonanie montazu" not "zamontowac"; "przeprowadzenie kontroli" not "skontrolowac" |
| **Polish comma rules** | Decimal comma (,) not decimal point (.). Thousands separator is space or period. |
| **Unambiguous yes/no** | "Tak" (yes) / "Nie" (no) -- avoid ambiguous affirmative particles |

---

## PART 2: DECISION FRAMEWORK

### 2.1 Polish Orthography Decision Trees

#### Table T1: Capitalization Rules in Technical Polish

| Context | Rule | Example |
|---------|------|---------|
| Standard designation | Always uppercase PN/PN-EN/PN-ISO | PN-EN 1993-1-1 |
| Unit symbols | Lowercase except L, deg C | m, kg, s, A, K, mol, cd, L, deg C |
| Unit names (full) | Lowercase | metr, kilogram, sekunda, amper, stopien Celsjusza |
| Proper names in standards | Keep original capitalization | Badania nieniszczace (NDT) |
| Months/dates | Lowercase in Polish | 15 stycznia 2024 r. |
| Titles of standards | Sentence case | "Norma dotycząca obciążeń śniegiem" |

#### Table T2: Punctuation Rules

| Context | Rule | Example |
|---------|------|---------|
| Decimal separator | Comma (,) | 12,5 mm (NOT 12.5 mm) |
| Thousands separator | Space or period | 12 500 mm or 12.500 mm |
| List introduction | Colon | Materialy: stal, aluminium, miedz |
| Dimensions | Multiplication sign (x) or × | 100 x 200 mm or 100 × 200 mm |
| Range | En dash (-) or hyphen (-) | 10-50 mm or 10–50 mm |
| Quotation marks | Polish lower-upper: ,,..." | ,,Material zgodny z norma" |
| Units after numbers | Space between number and unit | 25 mm (NOT 25mm) |

#### Table T3: Grammar Considerations in Technical Translation

| Source (EN) | Target (PL) | Notes |
|-------------|-------------|-------|
| "must be..." | "nalezy..." / "musi byc..." | Impersonal obligation |
| "should be..." | "zaleca sie..." / "powinno sie..." | Recommendation |
| "may be..." | "mozna..." / "dopuszcza sie..." | Permission |
| "is made of" | "jest wykonany z..." | Passive |
| "shall be verified" | "nalezy zweryfikowac" | Modal passive |
| Gerund "-ing" | Rzeczownik odczasownikowy | "spawanie" for "welding" |
| Adjective order | Noun + adjective (mostly) | "stal nierdzewna" (NOT "nierdzewna stal") |

### 2.2 Polish Technical Terminology Decision Tables

#### Table T4: Construction and Building (Budownictwo)

| English | Polish | PN Standard Reference |
|---------|--------|---------------------|
| Load-bearing wall | Sciana nosna | PN-EN 1996 |
| Reinforced concrete | Zelbet / Beton zbrojony | PN-EN 1992 |
| Steel structure | Konstrukcja stalowa | PN-EN 1993 |
| Foundation | Fundament / Lawa fundamentowa | PN-EN 1997-1 |
| Thermal insulation | Izolacja termiczna / Ocieplenie | PN-EN ISO 6946 |
| Waterproofing | Izolacja przeciwwodna / Hydroizolacja | PN-EN 13967 |
| Scaffolding | Rusztowanie | PN-EN 12811-1 |
| Reinforcement bar | Pret zbrojeniowy | PN-EN 10080 |
| Concrete cover | Otulina betonowa | PN-EN 1992-1-1 |
| Compressive strength | Wytrzymalosc na sciskanie | PN-EN 12390-3 |

#### Table T5: Mechanical Engineering (Mechanika)

| English | Polish | Notes |
|---------|--------|-------|
| Tensile strength | Wytrzymalosc na rozciaganie (Rm) | |
| Yield point | Granica plastycznosci (Re) | |
| Fatigue limit | Granica zmeczenia | |
| Torque | Moment obrotowy | Unit: Nm |
| Bearing | Lozysko | |
| Gear | Kolo zebate / Przekladnia zebata | |
| Shaft | Wal / Os | |
| Tolerance | Tolerancja wymiarowa | PN-EN ISO 286-1 |
| Surface roughness | Chropowatosc powierzchni | PN-EN ISO 1302 |
| Weld | Spoina / Zlacze spawane | PN-EN ISO 5817 |

#### Table T6: Electrical Engineering (Elektrotechnika)

| English | Polish | SEP Qualification Level |
|---------|--------|------------------------|
| Overhead power line | Linia napowietrzna | E (eksploatacja) |
| Underground cable | Kabel ziemny | D (dozory) |
| Switchgear | Rozdzielnica | |
| Circuit breaker | Wyłącznik nadprądowy / Safety: Bezpiecznik | |
| Short-circuit current | Prad zwarciowy | |
| Grounding / Earthing | Uziemienie | |
| Rated voltage | Napiecie znamionowe | Unit: V, kV |
| Frequency | Częstotliwość | Unit: Hz |
| Active power | Moc czynna (P) | Unit: W, kW |
| Apparent power | Moc pozorna (S) | Unit: VA, kVA |
| Power factor | Współczynnik mocy (cos phi) | |
| Protection class | Klasa ochronnosci | I, II, III |
| Ingress protection | Stopien ochrony IP | PN-EN 60529 |
| Electric shock | Porażenie prądem elektrycznym | |

#### Table T7: Welding Technology (Spawalnictwo)

| English | Polish | Standard |
|---------|--------|----------|
| Welding procedure specification (WPS) | Specyfikacja procedury spawania (WPS) | PN-EN ISO 15609-1 |
| Welding procedure qualification | Kwalifikacja technologii spawania | PN-EN ISO 15614-1 |
| Welder qualification | Kwalifikacja spawacza | PN-EN ISO 9606-1 |
| Butt weld | Doczołowy zlacze spawane / Spoina doczołowa | |
| Fillet weld | Spoina pachwinowa | |
| Root pass | Scieg graniowy / Scieg denny | |
| Filler material | Material dodatkowy do spawania | PN-EN ISO 544 |
| Shielding gas | Gaz oslonowy | PN-EN ISO 14175 |
| Non-destructive testing (NDT) | Badania nieniszczace (NDT/BN) | PN-EN ISO 9712 |
| Visual testing (VT) | Badania wizualne (VT) | PN-EN ISO 17637 |
| Radiographic testing (RT) | Badania radiograficzne (RT) | PN-EN ISO 17636-1 |
| Ultrasonic testing (UT) | Badania ultradzwiekowe (UT) | PN-EN ISO 17640 |
| Magnetic particle testing (MT) | Badania magnetyczno-proszkowe (MT) | PN-EN ISO 9934-1 |
| Leak test | Proba szczelnosci | PN-EN 1779 |
| Hardness test | Badanie twardosci | PN-EN ISO 6507-1 |

#### Table T8: Quality and Inspection (Jakosc i Kontrola)

| English | Polish | Standard |
|---------|--------|----------|
| Quality control | Kontrola jakosci / Sterowanie jakoscia | |
| Quality assurance | Zapewnienie jakosci | PN-EN ISO 9001 |
| Inspection plan | Plan kontroli / Plan inspekcji | |
| Test certificate | Swiadectwo badan / Certyfikat badan | |
| Conformity assessment | Ocena zgodnosci | |
| Declaration of performance | Deklaracja wlasciwosci uzytkowych (DoP) | CPR 305/2011 |
| CE marking | Oznakowanie CE | |
| Factory production control | Zakladowa kontrola produkcji (ZKP) | PN-EN ISO 9001 |
| Calibration | Wzorcowanie / Kalibracja | PN-EN ISO/IEC 17025 |
| Traceability | Identyfikowalnosc / Mozliwosc wywiedzenia | |
| Non-conformity | Niezgodnosc | |
| Corrective action | Dzialanie korygujace | |
| Preventive action | Dzialanie zapobiegawcze | |

#### Table T9: Safety and BHP (Bezpieczenstwo i Higiena Pracy)

| English | Polish | Regulation |
|---------|--------|------------|
| Occupational safety | Bezpieczenstwo i higiena pracy (BHP) | Kodeks pracy |
| Risk assessment | Ocena ryzyka zawodowego | Rozporzadzenie MRPiPS |
| Personal protective equipment | Srodki ochrony indywidualnej (SOI) / Sprzet ochronny | PN-EN ISO 13688 |
| Safety helmet | Kask ochronny / Helm ochronny | PN-EN 397 |
| Safety glasses | Okulary ochronne | PN-EN 166 |
| Safety gloves | Rekawice ochronne | PN-EN 388 |
| Safety shoes | Obuwie ochronne | PN-EN ISO 20345 |
| Safety harness | Szelki bezpieczenstwa / Uprzaz | PN-EN 361 |
| Fall arrest system | System asekuracji przed upadkiem z wysokosci | PN-EN 363 |
| Warning sign | Znak ostrzegawczy | PN-EN ISO 7010 |
| Fire extinguisher | Gasnica przeciwpozarowa | |
| First aid kit | Apteczka pierwszej pomocy | |
| Safety data sheet (SDS) | Karta charakterystyki (SDS) | Rozporzadzenie REACH |
| Permit to work | Zezwolenie na prowadzenie prac / Pozwolenie na prace | |
| Lockout/tagout (LOTO) | Procedura blokady/oznakowania (LOTO) | |

#### Table T10: Units and Measurements

| Quantity | Unit | Polish Name | Notes |
|----------|------|-------------|-------|
| Length | m | metr | Also mm, cm, km |
| Mass | kg | kilogram | Also g, t (tona) |
| Force | N | niuton | 1 N = 1 kg*m/s^2 |
| Pressure | Pa | paskal | MPa, kPa, bar (dopuszczalny) |
| Stress | MPa | megapaskal | Most common in engineering |
| Energy | J | dżul | Also kJ, MJ, kWh |
| Power | W | wat | kW, MW |
| Temperature | deg C | stopien Celsjusza | |
| Electric current | A | amper | |
| Voltage | V | wolt | kV, mV |
| Frequency | Hz | herc | |
| Area | m^2 | metr kwadratowy | |
| Volume | m^3 | metr szescienny | L (litr) dopuszczalny |

#### Table T11: Measurement Prefixes

| Prefix | Symbol | Polish | Example |
|--------|--------|--------|---------|
| giga- | G | giga- | GW (gigawat) |
| mega- | M | mega- | MPa (megapaskal) |
| kilo- | k | kilo- | kW (kilowat) |
| hekto- | h | hekto- | hPa (hektopaskal) |
| decy- | d | decy- | dB (decybel) |
| centy- | c | centy- | cm (centymetr) |
| mili- | m | mili- | mm (milimetr) |
| mikro- | u (my) | mikro- | um (mikrometr) |

#### Table T12: Polish Industrial Safety Signs (PN-EN ISO 7010)

| Sign Type | Polish Name | Color | Meaning |
|-----------|-------------|-------|---------|
| Zakaz | Znak zakazu | Red circle | Zakaz palenia, Zakaz wstepu |
| Nakaz | Znak nakazu | Blue circle | Nakaz noszenia kasku, Nakaz noszenia okularow |
| Ostrzezenie | Znak ostrzegawczy | Yellow triangle | Uwaga! Niebezpieczenstwo |
| Informacja | Znak informacyjny | Green square | Wyjscie ewakuacyjne, Apteczka |
| Ppoz | Znak przeciwpozarowy | Red square | Gasnica, Przycisk ppoz |

#### Table T13: Technical Documentation Types

| English | Polish | Notes |
|---------|--------|-------|
| Design documentation | Dokumentacja projektowa | |
| As-built documentation | Dokumentacja powykonawcza | |
| Technical specification | Specyfikacja techniczna (ST) / Opis techniczny | |
| Bill of quantities | Przedmiar robót / Przedmiar | |
| Cost estimate | Kosztorys | |
| Execution drawing | Rysunek wykonawczy / Rysunek warsztatowy | |
| Assembly drawing | Rysunek zlozeniowy | |
| Schematic diagram | Schemat ideowy | |
| Wiring diagram | Schemont polaczen / Schemat montazowy | |
| P&ID diagram | Schemat technologiczny / P&ID | |
| Flow chart | Schemat blokowy / Diagram przeplywu | |
| Maintenance manual | Instrukcja utrzymania / Instrukcja konserwacji | |
| Operator's manual | Instrukcja obslugi | |
| Spare parts catalog | Katalog czesci zamiennych | |
| Test report | Protokol badan / Raport z testow | |
| Calibration certificate | Swiadectwo wzorcowania | |

#### Table T14: Common Technical Verb Constructions

| English Construction | Polish Equivalent | Usage Context |
|---------------------|-------------------|---------------|
| "X shall be Y" | "X powinien byc Y" / "X nalezy Y" | Standards, specs |
| "It is recommended to..." | "Zaleca sie..." | Best practice |
| "It is prohibited to..." | "Zabrania sie..." / "Nie wolno..." | Safety |
| "X must not exceed Y" | "X nie moze przekraczac Y" | Tolerances |
| "X is defined as Y" | "X definiuje sie jako Y" | Definitions |
| "X shall comply with Y" | "X powinien spelniac wymagania Y" / "X zgodny z Y" | Standards compliance |
| "X is subjected to Y" | "X poddaje sie Y" | Testing |
| "X is performed by Y" | "X wykonuje sie przez Y" / "Y wykonuje X" | Procedures |
| "In the event of X..." | "W przypadku X..." / "W razie wystapienia X..." | Contingencies |
| "X shall be carried out..." | "X nalezy przeprowadzic..." | Procedures |
| "X is measured in Y" | "X mierzy sie w Y" / "Jednostka X jest Y" | Metrology |
| "X depends on Y" | "X zalezy od Y" | Relationships |

#### Table T15: False Friends and Traps

| English Word | False Friend in Polish | Correct Polish Translation |
|-------------|----------------------|---------------------------|
| Actually | Aktualnie (=currently) | Faktycznie, w rzeczywistosci |
| Eventually | Eventualnie (=possibly) | Ostatecznie, w koncu |
| Fabric | Fabryka (=factory) | Tkanina, material; konstrukcja |
| Application | Aplikacja (IT app only) | Zastosowanie, podanie |
| Construction | Konstrukcja (=structure) | Budowa (process) |
| Insulator | Izolator (electrical) | Material izolacyjny (thermal) |
| Conductor | Konduktor (=train attendant in PL) | Przewodnik, przewod |
| Paragraph | Paragraf (=section of law) | Akapit (text), ustęp |
| Cabinet | Gabinet (=office/room) | Szafka |
| Carton | Karton (=cardboard) | Pudlo tekturowe |
| Data | Dany (=given) in plural | Dane (pluralia tantum) |
| Glass | Glaz (=tile, also rock) | Szklo (material) |
| Lift | Lift (PL = ski lift) | Winda (elevator) |
| Path | Pas (=belt, strip) | Sciezka, droga |
| Perspective | Perspektywa (=prospect) | Widok z perspektywy |

---

## PART 3: STANDARDS REFERENCE

### 3.1 Polish Standards System (Polski Komitet Normalizacyjny -- PKN)

| Standard Prefix | Scope | Equivalent |
|-----------------|-------|------------|
| PN | Polska Norma -- Polish national standard | -- |
| PN-EN | Polish adoption of European standard (CEN/CENELEC) | EN |
| PN-ISO | Polish adoption of International Standard (ISO) | ISO |
| PN-EN ISO | Polish adoption of EN ISO standard | EN ISO |
| PN-HD | Polish adoption of Harmonization Document (CENELEC) | HD |
| PN-ETS | Polish adoption of European Telecommunications Standard | ETS |
| PN-B | Polish standard -- Budownictwo (Construction) | Formerly BN |
| PN-M | Polish standard -- Mechanika (Mechanics) | Formerly BN |
| PN-E | Polish standard -- Elektrotechnika (Electrical) | Formerly BN |

### 3.2 Key Eurocodes Adopted as PN-EN

| Standard | Title (Polish) | Title (English) |
|----------|---------------|-----------------|
| PN-EN 1990 | Podstawy projektowania konstrukcji | Basis of structural design |
| PN-EN 1991 | Oddziaływania na konstrukcje | Actions on structures |
| PN-EN 1992 | Projektowanie konstrukcji z betonu | Concrete structures |
| PN-EN 1993 | Projektowanie konstrukcji stalowych | Steel structures |
| PN-EN 1994 | Projektowanie konstrukcji zespolonych stalowo-betonowych | Composite steel-concrete |
| PN-EN 1995 | Projektowanie konstrukcji drewnianych | Timber structures |
| PN-EN 1996 | Projektowanie konstrukcji murowych | Masonry structures |
| PN-EN 1997 | Projektowanie geotechniczne | Geotechnical design |
| PN-EN 1998 | Projektowanie sejsmiczne konstrukcji | Earthquake resistance |
| PN-EN 1999 | Projektowanie konstrukcji aluminiowych | Aluminium structures |

### 3.3 Key Testing Standards

| Standard | Title (Polish) | Application |
|----------|---------------|-------------|
| PN-EN ISO 6892-1 | Metale -- Proba rozciagania -- Cz. 1 | Tensile testing of metals |
| PN-EN ISO 148-1 | Metale -- Proba udarnosci metoda Charpy'ego | Charpy impact test |
| PN-EN ISO 6507-1 | Metale -- Pomiar twardosci metoda Vickersa | Vickers hardness |
| PN-EN ISO 6508-1 | Metale -- Pomiar twardosci metoda Rockwella | Rockwell hardness |
| PN-EN ISO 9001 | Systemy zarzadzania jakoscia -- Wymagania | Quality management |
| PN-EN ISO 14001 | Systemy zarzadzania srodowiskowego | Environmental management |
| PN-EN ISO 45001 | Systemy zarzadzania bezpieczenstwem i higiena pracy | OH&S management |
| PN-EN ISO 3834-2 | Wymagania jakosci dotyczace spawania -- Cz. 2 | Welding quality |
| PN-EN 10204 | Rodzaje dokumentow kontroli wyrobow | Inspection documents for metals |
| PN-EN 13001 | Bezpieczenstwo -- Suwnice | Crane safety |

### 3.4 Polish Legal Metrology (Prawo o miarach)

- **GUM**: Glowny Urzad Miar -- Central Office of Measures (Poland's NMI)
- ** UKE**: Urzad Komunikacji Elektronicznej -- electronic communications
- **OIML**: International Organization of Legal Metrology
- **Dz.U.**: Dziennik Ustaw (Journal of Laws) -- publication of metrology regulations
- Legal measuring instruments must bear: **legalizacja** (verification) mark or **legalizacja ponowna** (re-verification) mark
- **Jednostki legalne**: SI units as defined by ustawa z dnia 11 maja 2001 r. -- Prawo o miarach

### 3.5 Construction Law (Prawo budowlane)

| Term | Polish | Notes |
|------|--------|-------|
| Construction Law | Prawo budowlane | Ustawa z dnia 7 lipca 1994 r. |
| Building permit | Pozwolenie na budowe | Issued by starosta (district governor) |
| Notice of construction | Zgloszenie budowy | For simpler structures |
| Occupancy permit | Pozwolenie na uzytkowanie | Required before use |
| Construction log | Dziennik budowy | Mandatory document on site |
| Geotechnical survey | Badania geotechniczne / Opinia geotechniczna | |
| Energy performance certificate | Swiadectwo charakterystyki energetycznej | Required for sale/lease |
| Fire safety certificate | Ekspertyza przeciwpozarowa / Swiadectwo | |
| Supervision inspection | Kontrola nadzoru budowlanego | By PINB (Powiatowy Inspektorat Nadzoru Budowlanego) |

### 3.6 Technical Approval System (Aprobaty Techniczne)

- **ITB**: Instytut Techniki Budowlanej -- main issuer of technical approvals for construction
- **Aprobata Techniczna ITB**: replaces old "Aprobata Techniczna" certificate for construction products
- **Krajowa Ocena Techniczna (KOT)**: National Technical Assessment -- replaced Aprobaty Techniczne since 2017
- **Europejska Ocena Techniczna (ETA)**: European Technical Assessment
- **CNBOP**: Centrum Naukowo-Badawcze Ochrony Przeciwpozarowej -- fire protection approvals
- **Certyfikat Zgodnosci**: Certificate of Conformity with PN standard
- **Znak B**: Polish voluntary safety mark (building products)
- **Znak CE**: mandatory CE marking under CPR

### 3.7 SEP Qualifications (Uprawnienia SEP)

| Qualification | Scope | Valid for |
|---------------|-------|-----------|
| SEP E (eksploatacja) | Operation of electrical devices up to 1 kV / above 1 kV | 5 years |
| SEP D (dozor) | Supervision of electrical installations | 5 years |
| SEP G (gaz) | Gas installations | 5 years |
| ENERGETYKA | Energy certificate | 5 years |
| UDT (Urzad Dozoru Technicznego) | Pressure equipment, hoisting devices | Indefinite with periodic checks |

### 3.8 Polish Materials Designations

| Polish Symbol | English Equivalent | Standard |
|---------------|-------------------|----------|
| St3S | S235JR (1.0038) | PN-EN 10025-2 |
| St3SX | S275JR (1.0044) | PN-EN 10025-2 |
| 18G2A | S355JR (1.0045) | PN-EN 10025-2 |
| OH18N9 | X5CrNi18-10 / 304 (1.4301) | PN-EN 10088-1 |
| 1H13 | X12Cr13 / 410 (1.4006) | PN-EN 10088-1 |
| AlCu4Mg1 | EN AW-2024 | PN-EN 573-3 |
| PA6 | Polyamide 6 | PN-EN ISO 16396 |
| PE-HD | HDPE | PN-EN ISO 17855 |
| Stal zbrojeniowa RB500W | B500SP | PN-EN 10080 |

### 3.9 Polish Welding Designations

| Abbreviation | Polish Full Name | English |
|-------------|------------------|---------|
| WPS | Specyfikacja procedury spawania | Welding Procedure Specification |
| WPQR | Protokol kwalifikacji technologii spawania | Welding Procedure Qualification Record |
| NDT | Badania nieniszczace | Non-destructive testing |
| VT | Badania wizualne | Visual Testing |
| MT | Badania magnetyczno-proszkowe | Magnetic Particle Testing |
| PT | Badania penetracyjne | Penetrant Testing |
| RT | Badania radiograficzne | Radiographic Testing |
| UT | Badania ultradzwiekowe | Ultrasonic Testing |
| PWHT | Obróbka cieplna po spawaniu | Post-Weld Heat Treatment |
| HAZ | Strefa wpływu ciepla (SWC) | Heat-Affected Zone |
| FCAW | Spawanie łukowe proszkiem metalicznym z rdzeniem | Flux-Cored Arc Welding |
| MAG | Spawanie w oslonie gazu aktywnego (MAG) | Metal Active Gas |
| TIG | Spawanie metodą TIG (wolframowa) | Tungsten Inert Gas |
| SAW | Spawanie łukiem krytym | Submerged Arc Welding |

---

*End of Polish Technical Domain File*
