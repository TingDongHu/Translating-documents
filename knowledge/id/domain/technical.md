---

id: id/domain/technical
type: domain
target_lang: id
name: "Domain: Technical (Teknis) — Indonesian"
description: Indonesian Technical domain terminology and translation rules
---

# Domain: Technical (Teknis) — Indonesian

## 1. Reader Model: How to Read Indonesian Technical Documents

### 1.1 Macro-Level Architecture

Indonesian technical documents follow a layered structure governed by SNI (Standar Nasional Indonesia) layout conventions and, where applicable, ASEAN/commonwealth-derived engineering documentation standards. The typical document hierarchy is:

```
[Judul / Title] — Mencantumkan nomor SNI jika berlaku
    → [Prakata / Foreword] — Latar belakang, tujuan, dan ruang lingkup
        → [Ruang Lingkup / Scope] — Batasan dan bidang penerapan
            → [Acuan Normatif / Normative References] — Daftar SNI dan/atau ISO yang dirujuk
                → [Istilah dan Definisi / Terms and Definitions] — Glosarium teknis
                    → [Persyaratan / Requirements] — Inti teknis: tabel, rumus, gambar
                        → [Metode Uji / Test Methods] — Prosedur pengujian
                            → [Lampiran / Annex] — Informasi tambahan (normatif atau informatif)
```

Key macro-level signals in Indonesian technical writing:

| Indonesian Signal | English Equivalent | Function |
|---|---|---|
| "Pasal" | Article / Clause | Legislative or regulatory numbered paragraph |
| "Ayat" | Paragraph / Sub-clause | Sub-division of a Pasal |
| "Butir" | Item / Point | Sub-division within an Ayat |
| "Lampiran normatif" | Normative annex | Legally binding appendix |
| "Lampiran informatif" | Informative annex | Non-binding reference appendix |

### 1.2 Meso-Level Patterns

Indonesian technical prose exhibits distinct rhetorical moves:

**Move 1: Statement of Authority (Pernyataan Kewenangan)**
- Signals: *"Berdasarkan SNI..."*, *"Sesuai dengan peraturan perundang-undangan..."*, *"Mengacu pada..."*
- Translation posture: Retain the authority reference; do not localize standards bodies.

**Move 2: Deontic Modality (Modalitas Kewajiban)**
- "harus" = "shall" (mandatory requirement)
- "sebaiknya" / "disarankan" = "should" (recommendation)
- "dapat" / "boleh" = "may" (permission)
- "tidak boleh" = "shall not" (prohibition)

**Move 3: Conditional Requirements (Persyaratan Bersyarat)**
- *"Dalam hal..."* = "In the case of..." / "Where..."
- *"Apabila..."* = "If..." / "When..."
- *"Kecuali..."* = "Unless..."

### 1.3 Micro-Level Patterns

**Passive-impersonal constructions:**
Indonesian technical language heavily uses passive voice with prefix *di-* to maintain impersonality:
- *"dilakukan"* → "shall be carried out"
- *"diperiksa"* → "shall be inspected"
- *"ditentukan"* → "shall be determined"

**Nominalization markers:**
Suffix *-an* and circumfix *pe-an*/*per-an* convert verbs to nouns:
- *ukur* (measure) → *ukuran* (dimension/measurement), *pengukuran* (the process of measuring)

---

## 2. Decision Framework

### Table 1: Shall/Should/May Modality Mapping

| Indonesian Modality | Deontic Strength | Translation | Context |
|---|---|---|---|
| harus | Mandatory | shall | Legal/regulatory requirement, SNI clause |
| wajib | Mandatory | shall (stronger) | Safety-critical requirements |
| sebaiknya / disarankan | Recommended | should | Best practice, non-mandatory guidance |
| dapat / boleh | Permitted | may | Optional allowance |
| tidak boleh | Prohibited | shall not | Absolute prohibition |
| dilarang | Prohibited | shall not / must not | Legal prohibition |
| dikecualikan | Exempt | is exempt from | Exception to a requirement |

**Decision rule:** Map "harus" to "shall" in normative/regulatory contexts and to "must" only when the source Indonesian uses "wajib" for safety-critical items. Never downgrade "harus" to "should".

### Table 2: Unit Conversion Decision Matrix

| Source Unit (ID) | SI Equivalent | Conversion | Preserve? | Notes |
|---|---|---|---|---|
| mm | millimeter | 1:1 | Yes | SI, keep as-is |
| cm | centimeter | 1:1 | Yes | SI, keep as-is |
| m | meter | 1:1 | Yes | SI, keep as-is |
| km | kilometer | 1:1 | Yes | SI, keep as-is |
| kg | kilogram | 1:1 | Yes | SI, keep as-is |
| ton | metric ton | 1,000 kg | Yes | SI, keep as-is |
| Liter / l | liter | 1:1 | Yes | SI, keep as-is |
| ml / mL | milliliter | 1:1 | Yes | SI, keep as-is |
| kPa / MPa | kilopascal / megapascal | 1:1 | Yes | SI, keep as-is |
| N / kN | newton / kilonewton | 1:1 | Yes | SI, keep as-is |
| derajat Celcius | degrees Celsius | 1:1 | Yes | SI, keep as-is |
| PS / pk | metric horsepower | 1 PS = 0.7355 kW | Convert or bracket | Use kW with PS in brackets |
| rpm | revolutions per minute | 1:1 | Yes | Widely understood |
| inci | inch | 1 in = 25.4 mm | Convert then bracket | Non-SI, bracket SI equivalent |
| kaki | foot | 1 ft = 0.3048 m | Convert then bracket | Non-SI, bracket SI equivalent |

**Decision rule:** Convert all non-SI units to SI. For legacy imperial units in quoted material, provide SI equivalent in square brackets. Never strip units. Always verify unit symbols use correct case (e.g., "mm" not "MM", "kW" not "KW").

### Table 3: Numerical Format Decision Table

| Indonesian Convention | English Convention | Decision |
|---|---|---|
| 1.234,56 (comma as decimal) | 1,234.56 (period as decimal) | Convert: swap comma/period |
| 1.000.000 (period as thousand separator) | 1,000,000 (comma as thousand separator) | Convert: swap separators |
| Rp 1.000.000,00 | IDR 1,000,000.00 | Convert to target currency format |
| 25% (same) | 25% (same) | Preserve |
| 1:2 (same) | 1:2 (same) | Preserve |
| 10^3 | 10^3 | Preserve |
| 1 x 10^3 | 1 x 10^3 | Preserve |

**Decision rule:** Indonesian uses a period as thousands separator and comma as decimal mark. In English translation, reverse both. Never accept mixed formats (e.g., "1.234,56" in English output).

### Table 4: Acronym and Abbreviation Handling

| ID Acronym | Expansion (ID) | English Equivalent | Decision |
|---|---|---|---|
| SNI | Standar Nasional Indonesia | Indonesian National Standard | Keep SNI, gloss on first use |
| ISO | Organisasi Standardisasi Internasional | International Organization for Standardization | Use ISO (universal) |
| IEC | Komisi Elektroteknik Internasional | International Electrotechnical Commission | Use IEC (universal) |
| BSN | Badan Standardisasi Nasional | National Standardization Agency | Keep BSN, gloss on first use |
| K3 | Keselamatan dan Kesehatan Kerja | Occupational Health and Safety (OHS) | Expand or use OHS with original in brackets |
| PPE | (borrowed from English) | Personal Protective Equipment | Keep PPE (used in ID too) |
| kWh | kilowatt-jam | kilowatt-hour | Keep kWh |
| AC | arus bolak-balik / air conditioner | alternating current / air conditioner | Disambiguate by context |
| DC | arus searah | direct current | Use DC |
| Hz | hertz | hertz | Keep Hz |
| V | volt | volt | Keep V |
| A | ampere | ampere | Keep A |
| W | watt | watt | Keep W |

**Decision rule:** If the acronym is universal (SI units, ISO), preserve it. If it is Indonesia-specific (SNI, BSN), keep it and provide English expansion on first occurrence. Acronyms borrowed from English that are used verbatim in Indonesian (e.g., PPE, CAD, CNC) should be kept as-is.

### Table 5: Measurement and Tolerance Phrases

| Indonesian Phrase | Translation | Notes |
|---|---|---|
| toleransi ± X mm | tolerance of ± X mm | Direct; keep ± symbol |
| penyimpangan yang diizinkan | permissible deviation | Formal register |
| batas maksimum | maximum limit | Use "maximum" |
| batas minimum | minimum limit | Use "minimum" |
| rentang ukuran | size range | Use "range" |
| diameter nominal (DN) | nominal diameter (DN) | Keep DN abbreviation |
| ketebalan minimal | minimum thickness | Use "minimum" |
| jarak bebas | clearance | Engineering term |
| toleransi geometrik | geometric tolerance | GD&T context |
| suaian (fit) | fit | Bracket English term |
| kelonggaran | allowance / gap | Context-dependent |
| kekentalan | viscosity | Fluid mechanics |
| kekerasan | hardness | Material science |
| tegangan tarik | tensile strength | Use "tensile strength" |
| tegangan luluh | yield strength | Use "yield strength" |
| modulus elastisitas | modulus of elasticity | Use "modulus of elasticity" |
| angka keamanan | safety factor | Use "safety factor" |
| beban maksimum | maximum load | Use "maximum load" |

### Table 6: Safety Level Classification

| Indonesian Term | English Translation | Regulatory Basis |
|---|---|---|
| tingkat bahaya | hazard level / danger level | General |
| risiko rendah | low risk | SNI risk matrix |
| risiko sedang | medium risk | SNI risk matrix |
| risiko tinggi | high risk | SNI risk matrix |
| aman | safe | General |
| tidak aman | unsafe | General |
| kritis | critical | Safety-critical system |
| berbahaya | dangerous / hazardous | General |
| sangat berbahaya | extremely dangerous | High hazard |
| daerah terlarang | prohibited area | Safety zone |
| daerah terbatas | restricted area | Safety zone |
| daerah aman | safe area | Safety zone |
| alat pelindung diri (APD) | personal protective equipment (PPE) | K3 regulation |
| prosedur keselamatan | safety procedure | OHS |
| sistem pengaman | safety system / guard system | Machine safety |
| pengaman darurat | emergency stop / emergency guard | Emergency system |
| pemadaman darurat | emergency shutdown | Process safety |

**Decision rule:** Safety classifications are often mandated by SNI or Ministry of Manpower regulations. Do not soften safety language. "Berbahaya" must remain "hazardous/dangerous" — never downgrade to "caution."

### Table 7: Test Method and Specification Phrases

| Indonesian Phrase | Translation | Notes |
|---|---|---|
| metode uji | test method | Standard terminology |
| prosedur pengujian | testing procedure | Use "testing procedure" |
| sampel uji | test sample / specimen | Use "test specimen" in formal |
| benda uji | test object / test piece | Construction/material testing |
| kondisi ruang | ambient conditions | "room conditions" for lab |
| suhu ruang | room temperature | Typically 25 +/- 2 deg C in ID |
| kelembaban relatif | relative humidity | Use "relative humidity" |
| laju pengujian | test rate / testing speed | Mechanical testing |
| beban uji | test load | Use "test load" |
| alat uji | testing apparatus / test equipment | Use "testing apparatus" formally |
| hasil pengujian | test results | Use "test results" |
| laporan pengujian | test report | Use "test report" |
| sertifikat uji | test certificate | Use "test certificate" |
| pengujian contoh | type testing / sample testing | Disambiguate: "type test" for certification |
| uji terima | acceptance test | Standard term |
| uji pabrik (FAT) | factory acceptance test (FAT) | Keep FAT abbreviation |
| uji lapangan | field test | Use "field test" |
| uji tipe | type test | Standard term |
| uji rutin | routine test | Standard term |

### Table 8: Material and Property Terminology

| Indonesian Term | English Translation | Domain |
|---|---|---|
| baja karbon | carbon steel | Materials |
| baja tahan karat / stainless steel | stainless steel | Materials |
| baja paduan | alloy steel | Materials |
| besi tuang | cast iron | Materials |
| besi tempa | wrought iron | Materials |
| aluminium paduan | aluminum alloy | Materials |
| tembaga | copper | Materials |
| kuningan | brass | Materials |
| perunggu | bronze | Materials |
| karet alam | natural rubber | Materials |
| karet sintetis | synthetic rubber | Materials |
| polietilena (PE) | polyethylene (PE) | Polymers |
| polipropilena (PP) | polypropylene (PP) | Polymers |
| polivinil klorida (PVC) | polyvinyl chloride (PVC) | Polymers |
| kayu kelas I/II/III | Class I/II/III timber | Construction |
| beton bertulang | reinforced concrete | Construction |
| beton prategang | prestressed concrete | Construction |
| agregat kasar | coarse aggregate | Construction |
| agregat halus | fine aggregate | Construction |
| semen Portland | Portland cement | Construction |

### Table 9: Drawing and Dimension Phrases

| Indonesian Phrase | English Translation | Notes |
|---|---|---|
| gambar teknik | engineering drawing / technical drawing | Use "engineering drawing" |
| gambar susunan | assembly drawing | Use "assembly drawing" |
| gambar detail | detail drawing | Use "detail drawing" |
| gambar potongan | sectional view / cross-section | Use "sectional view" |
| gambar pandangan | view drawing | Use "view" |
| skala | scale | Direct |
| ukuran | dimension | Direct |
| garis pusat | center line | Use "center line" |
| garis sumbu | axis line | Use "axis line" |
| toleransi linier | linear tolerance | GD&T |
| toleransi sudut | angular tolerance | GD&T |
| tanda pengerjaan permukaan | surface finish symbol | Machining |
| kekasaran permukaan | surface roughness | Use "surface roughness" |
| urutan pengelasan | welding sequence | Use "welding sequence" |
| simbol las | welding symbol | Use "welding symbol" |

### Table 10: Quality and Inspection Terminology

| Indonesian Term | English Translation | Notes |
|---|---|---|
| mutu / kualitas | quality | "mutu" more formal, "kualitas" common |
| kendali mutu (KM) | quality control (QC) | Keep QC in English |
| jaminan mutu (JM) | quality assurance (QA) | Keep QA in English |
| sistem manajemen mutu (SMM) | quality management system (QMS) | Keep QMS |
| pemeriksaan | inspection | Direct |
| pengujian tidak merusak (NDT) | non-destructive testing (NDT) | Keep NDT |
| uji visual (VT) | visual testing (VT) | Keep VT |
| uji radiografi (RT) | radiographic testing (RT) | Keep RT |
| uji ultrasonik (UT) | ultrasonic testing (UT) | Keep UT |
| uji penetran (PT) | penetrant testing (PT) | Keep PT |
| uji magnetik (MT) | magnetic testing (MT) | Keep MT |
| cacat | defect | Use "defect" |
| cacat kritis | critical defect | Use "critical defect" |
| penyimpangan | deviation / non-conformance | Use "non-conformance" in QA |
| ketidaksesuaian (NCR) | non-conformance report (NCR) | Keep NCR |
| tindakan korektif | corrective action | Use "corrective action" |
| tindakan pencegahan | preventive action | Use "preventive action" |
| lot terima | acceptance lot | Use "accepted lot" |
| lot tolak | rejected lot | Use "rejected lot" |

---

## 3. Standards

### 3.1 SNI — Standar Nasional Indonesia

SNI is the sole national standardization body in Indonesia, managed by BSN (Badan Standardisasi Nasional). Key facts:

- **Governing law:** Undang-Undang No. 20 Tahun 2014 tentang Standardisasi dan Penilaian Kesesuaian
- **Numbering format:** SNI XXXX:YYYY (e.g., SNI 1726:2019 for earthquake-resistant building design)
- **Adoption model:** SNI adopts ISO standards (identically or with modifications) ~40%; national-origin standards ~60%
- **Enforcement:** Some SNI are mandatory (wajib) per technical regulation; most are voluntary (sukarela)
- **Mandatory SNIs include:** Building materials, electrical equipment, tires, children's toys, food products

**SNI citation format in text:**
- Full: SNI 1726:2019, *Tata cara perencanaan ketahanan gempa untuk struktur bangunan gedung dan non-gedung*
- In running text: "Sesuai dengan SNI 1726:2019" → "In accordance with SNI 1726:2019"
- Translation of title: Provide English in brackets: "SNI 1726:2019 (Procedures for seismic design of building and non-building structures)"

### 3.2 Other Standards Referenced in Indonesian Documents

| Standard Body | Full Name | Role in ID Documents |
|---|---|---|
| ISO | International Organization for Standardization | Adopted as SNI ISO XXXX |
| IEC | International Electrotechnical Commission | Adopted as SNI IEC XXXX |
| ASTM | ASTM International | Sometimes referenced directly |
| ASME | American Society of Mechanical Engineers | Pressure vessels, piping |
| API | American Petroleum Institute | Oil and gas |
| AWS | American Welding Society | Welding procedures |
| JIS | Japanese Industrial Standards | Automotive, manufacturing |
| SII | Standar Industri Indonesia | Historical (pre-SNI) |
| SPLN | Standar Perusahaan Listrik Negara | PLN (utility) standards |
| SPM | Standar Pelayanan Minimal | Minimum service standards |

### 3.3 Unit System Standards

Indonesia officially uses the **International System of Units (SI)** per:
- Undang-Undang No. 2 Tahun 1981 tentang Metrologi Legal
- SNI 19-0429-1989 (adoption of ISO 1000, now ISO 80000 series)

### 3.4 Engineering Drawing Standards

- **SNI 05-0128-1987** — Adoption of ISO 128 for drawing conventions
- **SNI 05-0579-1991** — Technical drawings — Dimensioning
- **SNI 05-0127-1987** — Drawing sheet sizes (A0-A4, same as ISO)
- **Proyeksi:** Indonesia predominantly uses first-angle projection (proyeksi sudut pertama / ISO E), though third-angle is accepted

### 3.5 Quality Management

- **SNI ISO 9001:2015** — Adoption of ISO 9001:2015
- **SNI ISO 14001:2015** — Environmental management
- **SNI ISO 45001:2018** — Occupational health and safety (formerly OHSAS 18001)

### 3.6 Key Lexical Entries for Technical Translation

| Indonesian | Part of Speech | English | Notes |
|---|---|---|---|
| persyaratan teknis | noun phrase | technical requirements | Standard term |
| spesifikasi teknis | noun phrase | technical specification | Use "specification" |
| ketentuan teknis | noun phrase | technical provisions | More regulatory |
| data teknis | noun phrase | technical data | Direct |
| informasi teknis | noun phrase | technical information | Direct |
| manual / buku petunjuk | noun | manual / instruction book | Use "manual" |
| petunjuk operasi | noun | operating instructions | Use "operating instructions" |
| petunjuk keselamatan | noun | safety instructions | Use "safety instructions" |
| buku petunjuk pemakaian | noun | user manual / instruction manual | Use "user manual" |
| perawatan | noun | maintenance | Direct |
| perbaikan | noun | repair | Direct |
| pemasangan | noun | installation | Direct |
| pengoperasian | noun | operation | Direct |
| penyimpanan | noun | storage | Direct |
| penanganan | noun | handling | Direct |
| pelumasan | noun | lubrication | Direct |
| pendinginan | noun | cooling | Direct |
| pemanasan | noun | heating | Direct |

### 3.7 Verification Checklist for Technical Translation

| Check | Description |
|---|---|
| Unit validation | All SI units correctly formatted (space between number and unit where required) |
| Decimal/thousand separators | Converted from ID to EN convention |
| Modality accuracy | "harus"=shall, "dapat"=may — never mix these up |
| SNI references preserved | SNI number format kept, English gloss supplied |
| Acronym consistency | First-use expansion, subsequent-use abbreviated |
| Safety language preserved | No downgrading of hazard terminology |
| Drawing projection noted | First-angle projection acknowledged if relevant |
| Passive voice retained | Technical impersonality maintained |
| Numerical tolerance format | "+/-" symbol preserved or "plus minus" spelled out if required |

---

**Revision History:** Initial domain knowledge base for Indonesian Technical translation.
