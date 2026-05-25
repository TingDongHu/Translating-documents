---
id: vi/domain/technical
type: domain
target_lang: vi
name: Tai lieu ky thuat (Tieu chuan Viet Nam)
description: Quy tac dich thuat cho tai lieu ky thuat, tieu chuan, huong dan su dung va thong so ky thuat sang tieng Viet
---

## Reader Model

**Who reads this document and what do they expect?**

Technical document readers in the Vietnamese market are engineers, technicians, factory managers, maintenance staff, and regulatory inspectors who consult documents to install, operate, and maintain equipment safely and in compliance with TCVN (Tieu chuan Viet Nam) standards. They expect:

- **Absolute precision in specifications** — every dimension, tolerance, operating parameter, and material specification must be rendered exactly. An incorrect value in a Vietnamese technical translation can lead to equipment damage, production stoppages, or safety incidents in factories and construction sites across Vietnam.
- **TCVN-aligned terminology** — Vietnamese technical language follows established TCVN standards for terminology in each field (co khi, dien, xay dung, hoa chat). Using non-standard terms confuses readers and may cause rejection during regulatory review.
- **Consistent component naming** — if a part is called "cum truc" on page 5, it must not become "bo phan truc" on page 20. Vietnamese technical readers rely on exact term consistency to locate information quickly, especially in large maintenance manuals.
- **Clear procedural language** — step-by-step instructions must use imperative mood (An nut, Xoay van, Kiem tra). Ambiguous procedure language can lead to operational errors.
- **Proper safety communication** — Vietnamese workplace safety laws (Luat An toan ve sinh lao dong 2015) require clear hazard communication. Safety warnings must follow the signal word hierarchy established in TCVN and international standards.

**What would break their trust?**
- A mistranslated model or part number that causes procurement of the wrong component for a Vietnamese assembly line.
- An incorrect TCVN standard reference number, which renders the compliance claim invalid.
- A safety level changed from "NGUY HIEM" to "Canh bao" when the original indicated immediate life-threatening hazard.
- A measurement value altered or unit incorrectly converted, leading to mechanical fit failure.
- Inconsistent cross-references that make the manual unusable for maintenance technicians.

## Decision Framework

### 1. TCVN and QCVN Standard References

| Condition | Decision |
|---|---|
| Source references a national or international standard (ISO, IEC, ASTM) | Preserve the standard number exactly. On first occurrence, add the equivalent TCVN reference in brackets if one exists (e.g., ISO 9001:2015 [TCVN 9001:2015]). |
| Source references a standard that has been adopted as TCVN | Use the TCVN number as the primary reference and place the international standard in parentheses. The TCVN adoption carries legal weight in Vietnam. |
| Standard reference includes a year of publication | Preserve the year exactly. TCVN standards follow the format TCVN XXXX:YYYY. Do not omit or alter the year. |
| Document cites QCVN (Quy chuan Viet Nam) | These are mandatory technical regulations issued by Vietnamese ministries. Preserve QCVN references exactly (e.g., QCVN 01:2021/BXD). They carry legal force. |
| Source references a withdrawn or superseded TCVN | Check the current TCVN catalog. If the standard has been replaced, note both the old and new references in a translator's note. |

### 2. Units of Measurement (He don vi do luong)

| Condition | Decision |
|---|---|
| Source uses SI metric units | Preserve the exact value and unit. Vietnam uses the metric system (He SI). No conversion needed. |
| Source uses imperial units (inch, foot, psi, etc.) | Preserve the original imperial value AND provide the SI equivalent in parentheses on first occurrence. Vietnamese technicians work primarily in metric but encounter imperial in imported equipment. |
| Temperature in Celsius | Keep as do C. Vietnam uses Celsius for all technical measurements. No Fahrenheit conversion needed. |
| Temperature in Fahrenheit | Preserve Fahrenheit value and add Celsius in parentheses. |
| Compound technical unit (N-m, kg/cm2, m3/h) | Preserve the unit symbol exactly. Follow TCVN 7870 (ISO 80000 adoption) for unit formatting. |
| Unit abbreviation in Vietnamese context (m, kg, A, V, W) | Use the international symbol. Vietnam uses the same SI unit symbols as international practice. |

### 3. Safety Warnings (Canh bao an toan)

| Condition | Decision |
|---|---|
| Signal word indicates immediate life-threatening hazard | Map to **NGUY HIEM** (white text on red background). This is the highest hazard level under TCVN and Vietnamese labor safety law. |
| Signal word indicates potential hazard with possible serious injury | Map to **CANH BAO** (black text on orange background). Indicates a hazardous situation that could result in serious injury or death. |
| Signal word indicates minor or moderate injury risk | Map to **THAN TRONG** (black text on yellow background). Indicates a hazardous situation that could result in minor or moderate injury. |
| Signal word indicates property damage only (CAUTION without personal injury risk) | Map to **CHU Y** (black text on yellow background). Indicates risk of equipment or property damage only. |
| Source has a safety symbol or pictogram | Preserve the symbol reference exactly. Translate only the accompanying text. Vietnamese safety labels commonly use the same ISO hazard pictograms. |
| Safety message includes legal consequence (e.g., "Violators will be prosecuted") | Preserve the severity. Vietnamese legal phrasing: "Nguoi vi pham se bi truy cuu trach nhiem hinh su" or similar depending on severity. |

### 4. Technical Procedural Language

| Condition | Decision |
|---|---|
| Procedure step in imperative mood | Use Vietnamese imperative verb form. Vietnamese uses the same imperative mood as English: "An nut..." (Press the button), "Xoay van..." (Turn the valve), "Kiem tra..." (Check). |
| Condition or prerequisite before a step | Use "Truoc khi" (Before) or "Dam bao rang" (Ensure that). Vietnamese: "Truoc khi tiep tuc, dam bao rang..." |
| Procedural note or tip | Use "Ghi chu" for notes and "Meo" or "Luu y" for tips. Distinguish from warnings. "Luu y: Thao tac nay giup tang tuoi tho thiet bi." |
| Result of a procedure step | Use observed-result phrasing. Vietnamese: "Den bao hieu se sang mau xanh" (The indicator light will turn green). |

### 5. Technical Terminology (Thuat ngu ky thuat)

| Condition | Decision |
|---|---|
| English technical compound noun (e.g., "pressure relief valve") | Translate as Vietnamese compound: "van xa ap" (van + xa + ap). Vietnamese technical compounds follow the head-modifier order (classifier + specifier). |
| International technical acronym (PLC, HMI, CNC, SCADA, PID) | Preserve the English acronym. Vietnamese texts universally use these acronyms unchanged. Add Vietnamese explanation in parentheses on first use. |
| Engineering software name or version | Preserve exactly. Software names (AutoCAD, SolidWorks, MATLAB) are international trademarks. Do not translate. |
| Material specification (grade, alloy, standard) | Preserve the material designation exactly. Vietnamese steel grades often follow TCVN or JIS standards; do not substitute equivalent grades unless explicitly instructed. |
| Tool or equipment name with trademark | Preserve the brand name. Translate the generic description. "Makita impact wrench" -> "may van bu loong Makita (Makita impact wrench)". |

### 6. Vietnamese Technical Abbreviations

| Source Abbreviation | Vietnamese Equivalent | Notes |
|---|---|---|
| max | toi da (toi da) | Used universally in technical documents |
| min | toi thieu (toi thieu) | Used universally in technical documents |
| approx | xap xi (approx.) | Or "khoang" for approximate values |
| ref | tham khao (TK) | Used for cross-references |
| std | tieu chuan (TC) | Standard abbreviation in TCVN context |
| dia | duong kinh (DK or Ø) | Diameter symbol Ø is also used |
| RPM | vong/phut (v/ph) | Vietnamese uses v/ph for rotational speed |
| No. | so (STT for serial/order number) | "So" for number, "STT" for sequence |
| temp | nhiet do (nd) | Temperature abbreviation in technical drawings |

### 7. Dimensions and Tolerances

| Condition | Decision |
|---|---|
| Dimension with tolerance (+/- value) | Preserve the dimension and tolerance exactly. Vietnamese engineering drawings follow the same ISO 2768 tolerance standards. Format: "50 +/- 0.05 mm" or "50(0)/(-0,05) mm". |
| Surface finish specification | Preserve Ra value exactly. Use the Vietnamese term "do nham be mat" for surface roughness. |
| Thread specification (M10x1.5) | Preserve exactly. Vietnam uses metric threads (ISO 68-1). No conversion needed. |
| Weld symbol or specification | Preserve the welding standard reference. Translate accompanying text. Vietnamese welding standards follow TCVN 6119 (ISO 2553). |
| Angular dimension | Preserve degrees/minutes/seconds format. Use the degree symbol as in the source. |

### 8. Quality and Certification Terminology

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Quality control | kiem soat chat luong (KSCL) | Standard term in Vietnamese manufacturing |
| Quality assurance | dam bao chat luong (DBCL) | Used in ISO documentation |
| Inspection | kiem tra / kiem dinh | "Kiem dinh" for formal/mandatory inspection |
| Calibration | hieu chuan (HC) | Standard term per TCVN 6165 |
| Certificate of conformity | Giay chung nhan hop quy | For QCVN compliance certification |
| Test report | Bien ban thu nghiem | Used in laboratory and factory testing |
| Non-conformance | su khong phu hop (KPH) | Standard ISO 9001 term in Vietnamese |
| Corrective action | hanh dong khac phuc (HDKP) | Standard ISO term |
| Preventive action | hanh dong phong ngua (HDPN) | Standard ISO term |
| Traceability | kha nang truy xuat (KN TX) | Used in manufacturing and supply chain |

### 9. Electrical and Electronic Terminology

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Voltage | dien ap | Measured in V (von) |
| Current | dong dien | Measured in A (am-pe) |
| Power | cong suat | Measured in W (o-at) |
| Frequency | tan so | Measured in Hz (hec) |
| Ground / Earth | tiep dat / mass | Both terms used; "tiep dat" is preferred in formal documents |
| Phase | pha | Single-phase: "mot pha", Three-phase: "ba pha" |
| Circuit breaker | may cat / CB | "CB" (pronounced "xe-be") is common in Vietnamese industry |
| Fuse | cau chi | Always use "cau chi" |
| Transformer | may bien ap (MBA) | Standard electrical term |
| Motor | dong co (DC) | "Dong co dien" for electric motor |
| Switch | cong tac / chuyen mach | "Cong tac" for general switch; "chuyen mach" for selector switch |
| Sensor | cam bien (CB) | "Cam bien" for generic sensor; specific types: cam bien ap suat, cam bien nhiet do |
| Controller | bo dieu khien (BDK) | PLC: "bo dieu khien logic kha trinh" |
| Actuator | co cau chap hanh / actuator | Both terms used; "actuator" is common in imported equipment docs |

### 10. Construction and Civil Engineering Terminology

| Source Term | Vietnamese Equivalent | Notes |
|---|---|---|
| Reinforced concrete | be tong cot thep (BTCT) | Standard construction term |
| Steel structure | ket cap thep (KC thep) | Common in construction drawings |
| Foundation | mong / nen mong | "Mong" for foundation structure; "nen mong" for foundation soil |
| Load bearing | chiu luc | "Tuong chiu luc" (load-bearing wall) |
| Compressive strength | cuong do chiu nen | Measured in MPa (kG/cm2 in older Vietnamese docs) |
| Tensile strength | cuong do chiu keo | Standard term in material testing |
| Waterproofing | chong tham | Used in construction and civil engineering |
| Fire resistance | chong chay / kha nang chiu lua | "Chong chay" for fireproofing; "kha nang chiu lua" for fire resistance rating |
| Floor slab | san be tong | "San" for floor; "San BTCT" for reinforced concrete floor slab |
| Column | cot | Structural column; "cot be tong cot thep" for RCC column |

### 11. Vietnamese National Standards Numbering System

| Standard Type | Format | Example | Notes |
|---|---|---|---|
| TCVN (National Standard) | TCVN XXXX:YYYY | TCVN 6900:2010 | Issued by Bo Khoa hoc va Cong nghe |
| TCVN adoption of ISO | TCVN ISO XXXX:YYYY | TCVN ISO 9001:2015 | Vietnamese adoption of ISO standard |
| QCVN (National Technical Regulation) | QCVN XX:YYYY/B... | QCVN 01:2021/BXD | Mandatory; issued by ministry (BXD = Bo Xay dung) |
| TCXDVN (Construction Standard) | TCXDVN XXX:YYYY | TCXDVN 356:2005 | Construction-specific standards (being replaced by TCVN) |
| TCCS (Grassroots/Enterprise Standard) | TCCS XX:YYYY | TCCS 01:2020/VNPT | Internal standards of enterprises/agencies |
| 22TCN (Sector Standard) | 22TCN XXX-YY | 22TCN 272-05 | Older sector standards, gradually being phased out |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **TCVN/QCVN reference number mistranslated or omitted** | A wrong standard reference invalidates compliance claims. In Vietnam, technical documents submitted for regulatory approval (Bo Khoa hoc va Cong nghe, Bo Xay dung) must cite the correct TCVN or QCVN. |
| **Measurement value altered or unit changed** | Any change to a dimension, tolerance, rating, or specification value is unacceptable. In Vietnamese manufacturing and construction, even minor deviations can cause structural failure or equipment malfunction. |
| **Safety signal word downgraded** | Changing "NGUY HIEM" (DANGER) to "Canh bao" (Warning) reduces the perceived hazard level and creates legal liability under Luat An toan ve sinh lao dong 2015. |
| **Model/part number changed** | Leads to ordering incorrect spare parts. Vietnamese factories and workshops rely on exact part numbers for procurement. |
| **Acronym used inconsistently** | Once an acronym is introduced in Vietnamese text, it must remain consistent. Mixing "PLC" and "bo dieu khien logic" creates confusion about whether these are the same component. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Decimal comma confusion** | Vietnam uses the comma as decimal separator (3,14) and dot as thousands separator (1.234). When translating into Vietnamese FROM a locale that uses the opposite convention, convert: 3.14 -> 3,14 and 1,234 -> 1.234. |
| **Inconsistent component naming** | Once a component is named (e.g., "van an toan" for safety valve), do not switch to synonyms ("van bao ve", "van xa ap"). Use a glossary. |
| **Active/passive misuse in procedures** | Use imperative mood for all instructional steps. Passive voice ("can be opened", "should be checked") is acceptable in descriptions but not in step-by-step instructions. |
| **Omission of unit symbols** | In Vietnamese technical writing, the unit symbol always follows the value with a space: "5 kg", not "5kg". Always include the space. |
| **Untranslated titles or section headings** | All headings, table headers, figure captions, and callouts must be translated. Leaving UI labels in English is common (acceptable), but section titles must be in Vietnamese. |
| **English article "the" carried over** | Vietnamese has no definite article. "The valve opens" -> "Van mo ra", never "Cai van mo ra" in technical context. Omit "the" in Vietnamese translations. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False friends in Vietnamese technical terms** | Some Vietnamese technical terms have different meanings in different fields. Example: "cam bien" means "sensor"; but "cam bien ap" means "pressure sensor" not "voltage sensor" ("cam bien dien ap"). Verify in a domain glossary. |
| **Tone mark errors in critical terms** | A missing tone mark can change meaning. "may" (machine) vs. "may" (which); "mo" (open) vs. "mo" (grease/oil). In technical documents, tone mark errors are especially dangerous in safety warnings. |
| **Vietnamese compound word hyphenation** | Vietnamese technical compounds may or may not use hyphens. "dong co dien" is standard for "electric motor." Check TCVN terminology for the approved compound form for your field. |
| **QCVN year mismatch** | QCVN standards are periodically updated. Referencing an outdated QCVN year may result in non-compliance. Always verify the current effective year. |
| **Vietnamese punctuation in technical context** | Vietnamese uses the same basic punctuation as English for technical content, but the decimal comma and thousands dot are reversed from English convention. Ensure consistent application throughout. |

## Domain-Specific Reference

### Key Vietnamese Standards Bodies and Terms

| Acronym | Full Name | Role |
|---|---|---|
| TCVN | Tieu chuan Viet Nam | National standards of Vietnam, issued by Bo Khoa hoc va Cong nghe (Ministry of Science and Technology) |
| QCVN | Quy chuan ky thuat Quoc gia | National technical regulations; mandatory for compliance |
| Bo KHCN | Bo Khoa hoc va Cong nghe | Ministry of Science and Technology — main standards body |
| Bo XD | Bo Xay dung | Ministry of Construction — issues QCVN for construction |
| Bo CT | Bo Cong Thuong | Ministry of Industry and Trade — issues QCVN for industrial safety |
| Bo TNMT | Bo Tai nguyen va Moi truong | Ministry of Natural Resources and Environment — environmental QCVN |
| STAMEQ | Directorate for Standards, Metrology and Quality | Implementing agency for standardization, metrology, and quality |
| VILAS | Viet Nam Laboratory Accreditation Scheme | National laboratory accreditation |

### Common TCVN Standards in Key Sectors

| Sector | Key TCVN Examples | Notes |
|---|---|---|
| Quality management | TCVN ISO 9001:2015 | Adoption of ISO 9001:2015 |
| Environmental management | TCVN ISO 14001:2015 | Adoption of ISO 14001:2015 |
| Occupational health and safety | TCVN ISO 45001:2019 | Adoption of ISO 45001:2018 |
| Food safety | TCVN ISO 22000:2019 | Adoption of ISO 22000:2018 |
| Welding | TCVN 6119 series | Adoption of ISO 2553, ISO 6947, etc. |
| Mechanical drawings | TCVN 7285 series | Adoption of ISO 128 (technical drawings) |
| Electrical installations | TCVN 7447 series | Adoption of IEC 60364 |
| Concrete and reinforced concrete | TCVN 5574:2018 | National standard for concrete design |
| Steel structures | TCVN 5575:2012 | National standard for steel structure design |
| Fire safety | TCVN 2622:1995 | National fire safety standard for buildings |
| Acoustics | TCVN 7870 series | Adoption of ISO 80000 (quantities and units) |

### Unit Abbreviations in Vietnamese Technical Context

| Quantity | Unit | Symbol | Vietnamese Note |
|---|---|---|---|
| Length | milimet, centimet, met, kilomet | mm, cm, m, km | Same as international |
| Mass | gam, kilogam, tan | g, kg, t | "kg" is universally understood |
| Volume | lit, mililit | L, mL | Also "m3" for cubic meter |
| Temperature | do Celsius | °C | "do C" in running text |
| Pressure | pascal, bar | Pa, bar | "1 bar = 100 kPa" |
| Force | niuton | N | Same as international |
| Torque | niuton-met | N-m | Same as international |
| Power | oat, kilooat | W, kW | Same as international |
| Electric current | am-pe | A | Same as international |
| Voltage | von | V | Same as international |
| Frequency | hec | Hz | Same as international |
| Rotational speed | vong tren phut | v/ph | Vietnamese-specific: "vong/phut" |
| Area | met vuong | m2 | "m vuong" or "m2" |
| Energy | jun, kilo-oat gio | J, kWh | "kWh" commonly used for electricity |
