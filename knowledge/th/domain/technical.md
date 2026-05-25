# Thai Technical Domain (เทคนิค) — Domain Knowledge for Thai Technical Document Translation

---

## Reader Model

### Primary Reader Persona: Thai Engineer / Technical Reviewer (วิศวกร)

| Attribute | Description |
|-----------|-------------|
| **Title** | วิศวกร (Engineer), นักวิชาการ (Technical Officer), ผู้ควบคุมงาน (Supervisor) |
| **Education** | Thai engineering degree (ปริญญาตรี/โท วิศวกรรมศาสตร์); trained under สภาวิศวกร (Thai Engineering Council) |
| **English Proficiency** | Moderate-high technical reading; familiar with English loanwords transliterated into Thai (สเปก = spec, ดีไซน์ = design) |
| **Key Concern** | Translated specs, safety levels, measurements, and standards must match TIS exactly; any deviation invalidates regulatory approval |
| **Work Context** | Government agency (กรมโรงงานอุตสาหกรรม), private engineering firm, or manufacturing QA/QC |
| **Expectations** | Metric units mandatory; TIS references preserved; safety classifications use Thai-defined categories; no ambiguity in critical parameters |

### Secondary Reader: TISI Certification Officer (เจ้าหน้าที่มาตรฐาน สมอ.)

| Attribute | Description |
|-----------|-------------|
| **Role** | Reviews translated docs for มอก. (mandatory TIS certification); non-standard translations result in application rejection |
| **Expectations** | Exact compliance with TIS terminology; compares against original TIS standard text |

---

## Decision Framework

### 1. Unit of Measurement — Metric System Enforcement

| Source | Thai Target | Rule |
|--------|------------|------|
| inch | นิ้ว | Provide metric equivalent in parentheses |
| foot | ฟุต | Convert to meters |
| psi | ปอนด์ต่อตารางนิ้ว | Convert to kPa/MPa with original |
| gallon (US) | แกลลอนสหรัฐ | Convert to liters |
| BTU | บีทียู | Add kJ equivalent |

**Default**: All measurements in SI units. Imperial equivalents in parentheses.

### 2. TIS Standard Number Rendering

| Source | Thai Rendering | Rule |
|--------|---------------|------|
| TIS 123-2547 | มอก. 123-2547 | มอก. = มาตรฐานผลิตภัณฑ์อุตสาหกรรม |
| TIS 123-2004 | มอก. 123-2547 | CE + 543 = BE year |
| TIS 123-2547 Section 5 | มอก. 123-2547 ข้อ 5 | Use ข้อ for clause |
| ISO 9001:2015 | ISO 9001:2015 | Keep ISO numbers as-is |

**Always convert CE year to BE year (พ.ศ. = CE + 543) for TIS references.**

### 3. Safety Level Terminology

| Source | Thai Equivalent | Usage |
|--------|----------------|-------|
| Hazard | อันตราย | General danger |
| Risk | ความเสี่ยง | Risk assessment |
| Danger | อันตรายร้ายแรง | Red-level / life-threatening |
| Warning | คำเตือน | Yellow-level / medium |
| Caution | ข้อควรระวัง | Blue-level / advisory |
| Safety factor | ค่าความปลอดภัย | Engineering margin |
| Fail-safe | ปลอดภัยเมื่อขัดข้อง | Default safe on failure |
| Emergency stop | หยุดฉุกเฉิน | Machine safety |
| Protective earth | สายดินป้องกัน | Electrical |
| Insulation class | ระดับฉนวน | Equipment classification |
| Ingress Protection | ระดับการป้องกัน IP | IP rating |
| Explosion-proof | กันระเบิด | Hazardous area |
| Lockout/Tagout | การล็อก/ป้ายนิรภัย | LOTO |

### 4. Engineering Material Terminology

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Steel | เหล็ก | General |
| Stainless steel | เหล็กกล้าไร้สนิม | SS304, SS316 |
| Carbon steel | เหล็กกล้าคาร์บอน | |
| Alloy steel | เหล็กกล้าผสม | |
| Aluminum | อะลูมิเนียม | Royal Institute spelling |
| Copper | ทองแดง | |
| Cast iron | เหล็กหล่อ | |
| Concrete | คอนกรีต | |
| Reinforced concrete | คอนกรีตเสริมเหล็ก | |
| Prestressed concrete | คอนกรีตอัดแรง | |
| Polymer | พอลิเมอร์ | |
| Plastic | พลาสติก | Generic |
| Rubber | ยาง | ยางธรรมชาติ = natural |
| Ceramic | เซรามิก | |
| Composite | วัสดุเชิงประกอบ | |
| Galvanized | ชุบสังกะสี | Hot-dip = ชุบแบบจุ่มร้อน |

### 5. Engineering Process and Quality Terms

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Specification | ข้อกําหนด / รายการละเอียด | |
| Standard | มาตรฐาน | |
| Tolerance | ค่าความคลาดเคลื่อน | |
| Deviation | การเบี่ยงเบน | |
| Inspection | การตรวจสอบ | |
| Testing | การทดสอบ | |
| Quality control | การควบคุมคุณภาพ | QC |
| Quality assurance | การประกันคุณภาพ | QA |
| Calibration | การสอบเทียบ | |
| Verification | การตรวจพิสูจน์ | |
| Validation | การทวนสอบ | |
| Non-conformance | ความไม่สอดคล้อง | NC |
| Corrective/Preventive action | การแก้ไข / การป้องกัน | CAPA |
| Certificate of Analysis | ใบรับรองผลวิเคราะห์ | CoA |
| Certificate of Conformity | ใบรับรองความสอดคล้อง | CoC |

### 6. Electrical and Electronic Engineering

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Voltage | แรงดันไฟฟ้า | |
| Current | กระแสไฟฟ้า | |
| Resistance | ความต้านทาน | |
| Power | กําลังไฟฟ้า | |
| Frequency | ความถี่ | |
| Phase | เฟส | เฟสเดียว (1-ph), สามเฟส (3-ph) |
| Alternating current | ไฟฟ้ากระแสสลับ | AC |
| Direct current | ไฟฟ้ากระแสตรง | DC |
| Transformer | หม้อแปลง | |
| Circuit breaker | เบรกเกอร์ / สวิตช์ตัดตอน | |
| Fuse | ฟิวส์ | |
| Relay | รีเลย์ | |
| Ground/Earth | สายดิน | |
| Short circuit | ไฟฟ้าลัดวงจร | |
| Overload | โหลดเกิน | |
| PCB | แผ่นวงจรพิมพ์ | Printed circuit board |
| PLC | พีแอลซี / ตัวควบคุมแบบโปรแกรมได้ | |
| Sensor | เซนเซอร์ / ตัวตรวจรู้ | |
| Actuator | ตัวกระทํา / อุปกรณ์ขับเคลื่อน | |

### 7. Mechanical Engineering

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Pressure | ความดัน | |
| Temperature | อุณหภูมิ | |
| Flow rate | อัตราการไหล | |
| Torque | แรงบิด | |
| Stress | ความเค้น | |
| Strain | ความเครียด | |
| Fatigue | ความล้า | |
| Vibration | การสั่นสะเทือน | |
| Bearing | ตลับลูกปืน | |
| Gear | เฟือง | |
| Shaft | เพลา | |
| Valve | วาล์ว | |
| Pump | ปั๊ม | |
| Compressor | คอมเพรสเซอร์ | |
| Flange | หน้าแปลน | |
| Gasket | ปะเก็น | |
| Weld | รอยเชื่อม | การเชื่อม = welding |
| Heat treatment | การอบชุบทางความร้อน | |
| Dimension | มิติ | |

### 8. Environmental and Safety Signs

| Source | Thai | Signage |
|--------|------|---------|
| Flammable | ไวไฟ | Red |
| Explosive | วัตถุระเบิด | Orange |
| Toxic | เป็นพิษ | |
| Corrosive | กัดกร่อน | |
| Radioactive | กัมมันตรังสี | |
| Biohazard | อันตรายทางชีวภาพ | |
| Wear gloves/ goggles /hard hat | สวมถุงมือ/แว่นตา/หมวกนิรภัย | PPE |
| High voltage area | บริเวณไฟฟ้าแรงสูง | |
| Confined space | พื้นที่อับอากาศ | |
| No smoking | ห้ามสูบบุหรี่ | |
| Emergency exit | ทางออกฉุกเฉิน | |
| First aid | ปฐมพยาบาล | |

### 9. Construction and Civil Engineering

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Foundation | ฐานราก | |
| Pile | เสาเข็ม | |
| Column | เสา | |
| Beam | คาน | |
| Slab | พื้น | |
| Reinforcement | เหล็กเสริม | Rebar = เหล็กข้ออ้อย |
| Formwork | แบบหล่อ | |
| Aggregate | มวลรวม | |
| Cement | ปูนซีเมนต์ | |
| Load | น้ำหนักบรรทุก | Live = จร, Dead = คงที่ |
| Excavation | การขุดดิน | |
| Backfill | การถมกลับ | |
| Drainage | การระบายน้ำ | |
| Waterproofing | การกันน้ำ | |

### 10. Chemical Engineering Safety

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Concentration | ความเข้มข้น | |
| pH | พีเอช | |
| Catalyst | ตัวเร่งปฏิกิริยา | |
| Solvent | ตัวทําละลาย | |
| Distillation | การกลั่น | |
| Filtration | การกรอง | |
| Viscosity | ความหนืด | |
| Density | ความหนาแน่น | |
| MSDS/SDS | เอกสารข้อมูลความปลอดภัย | |
| Hazardous substance | สารอันตราย | |
| Chemical formula | สูตรเคมี | Do not translate |
| CAS number | เลขทะเบียน CAS | Keep as-is |

### 11. Types of Technical Documents

| English | Thai |
|---------|------|
| Technical Specification | ข้อกําหนดทางเทคนิค |
| Data Sheet | ข้อมูลจําเพาะ |
| User Manual | คู่มือผู้ใช้ |
| Installation Manual | คู่มือการติดตั้ง |
| Operation Manual | คู่มือการปฏิบัติงาน |
| Maintenance Manual | คู่มือการบํารุงรักษา |
| Safety Manual | คู่มือความปลอดภัย |
| Standard Operating Procedure (SOP) | วิธีการปฏิบัติงานมาตรฐาน |
| Inspection/Test Report | รายงานผลการตรวจสอบ/ทดสอบ |
| Calibration Certificate | ใบรับรองการสอบเทียบ |
| Bill of Materials (BOM) | รายการวัสดุ |
| P&ID | แผังท่อและเครื่องมือวัด |
| Wiring Diagram | แผังการเดินสายไฟ |
| As-built Drawing | แบบก่อสร้างจริง |
| Risk Assessment | การประเมินความเสี่ยง |

---

## Standard Conventions

### 1. TIS Standard References

- **Format**: มอก. [number]-[year in BE] (e.g., มอก. 123-2547)
- **CE-to-BE**: Year + 543
- **Clause**: Use ข้อ (e.g., ข้อ 5.1)
- **Annex**: ภาคผนวก (e.g., ภาคผนวก ก)
- **Table/Figure**: ตารางที่ / รูปที่

### 2. Unit Formatting

- SI units mandatory; separate numeral from unit with thin space: 50 มม.
- Abbreviations: มม. (mm), ซม. (cm), ม. (m), กม. (km), กก. (kg), ล. (liter)
- Temperature: °C (องศาเซลเซียส), °F (องศาฟาเรนไฮต์)
- Pressure: กิโลปาสกาล (kPa), เมกะปาสกาล (MPa), บาร์ (bar)
- Energy: จูล (J), กิโลจูล (kJ)
- Power: วัตต์ (W), กิโลวัตต์ (kW)
- Electrical: โวลต์ (V), แอมแปร์ (A), เฮิรตซ์ (Hz)
- Percentage: ร้อยละ or % (ร้อยละ preferred in formal)
- Decimal: period (.); thousands: comma (,)

### 3. Date Conventions in Technical Documents

- Formal: วันที่ 15 เดือนมกราคม พ.ศ. 2550
- Short numeric: วว/ดด/ปปปป (15/01/2550)
- Time: 14.30 น. (hours.minutes)
- Months: มกราคม, กุมภาพันธ์, มีนาคม, เมษายน, พฤษภาคม, มิถุนายน, กรกฎาคม, สิงหาคม, กันยายน, ตุลาคม, พฤศจิกายน, ธันวาคม

### 4. Engineering Drawing Title Block Fields

- หมายเลขแบบ (Drawing No.), รุ่น (Revision), ผู้เขียนแบบ (Drawn by), ตรวจ (Checked by), อนุมัติ (Approved by)
- มาตราส่วน (Scale), หน่วย (Unit), หมายเหตุ (Notes)

### 5. Warning Label Convention (Three-Tier)

| Level | Thai | Color |
|-------|------|-------|
| 1 - Danger | อันตราย (อันตรายร้ายแรง) | Red on White |
| 2 - Warning | คำเตือน | Yellow/Amber |
| 3 - Caution | ข้อควรระวัง | Blue |

### 6. Safety Data Sheet (SDS) Sections

1. ข้อมูลเกี่ยวกับสารเคมีและบริษัทผู้ผลิต
2. ข้อมูลอันตราย
3. องค์ประกอบ/ข้อมูลเกี่ยวกับส่วนผสม
4. มาตรการปฐมพยาบาล
5. มาตรการผจญเพลิง
6. มาตรการเมื่อมีการรั่วไหล
7. การจัดการและการเก็บรักษา
8. การควบคุมการสัมผัสและการป้องกันส่วนบุคคล
9. คุณสมบัติทางกายภาพและเคมี
10. ความเสถียรและการเกิดปฏิกิริยา
11. ข้อมูลทางพิษวิทยา
12. ข้อมูลเชิงนิเวศ
13. ข้อพิจารณาในการกําจัด
14. ข้อมูลการขนส่ง
15. ข้อมูลเกี่ยวกับกฎข้อบังคับ
16. ข้อมูลอื่นๆ

### 6c. Chemical Engineering Safety Terms

| Source | Thai Equivalent | Notes |
|--------|----------------|-------|
| Concentration | ความเข้มข้น | |
| pH | พีเอช | |
| Catalyst | ตัวเร่งปฏิกิริยา | |
| Solvent | ตัวทําละลาย | |
| Distillation | การกลั่น | |
| Filtration | การกรอง | |
| Viscosity | ความหนืด | |
| Density | ความหนาแน่น | |
| Specific gravity | ความถ่วงจําเพาะ | |
| MSDS/SDS | เอกสารข้อมูลความปลอดภัย | Safety Data Sheet |
| Hazardous substance | สารอันตราย | |
| Chemical formula | สูตรเคมี | Do not translate |
| CAS number | เลขทะเบียน CAS | Keep as-is |

### 7. Technical Writing Style

| Rule | Guideline |
|------|-----------|
| Voice | Active preferred; passive acceptable |
| Tense | Present for specs; past for test results |
| Structure | Short-medium sentences; avoid nested clauses |
| Foreign terms | English in parentheses on first use |
| Loanwords | Royal Institute transliteration: คอมพิวเตอร์, อินเทอร์เน็ต |
| Cross-refs | "ดังแสดงในรูปที่ X" (as shown in Fig. X) |
| Modality | ต้อง (must), ควร (should), อาจ (may) |

### 8. Common Structural Phrases

| English | Thai |
|---------|------|
| This specification covers... | ข้อกําหนดนี้ครอบคลุม... |
| The equipment shall comply with... | อุปกรณ์ต้องเป็นไปตาม... |
| Unless otherwise specified... | เว้นแต่จะระบุไว้เป็นอย่างอื่น... |
| In accordance with... | ตามที่ / เป็นไปตาม... |
| Rated voltage: | แรงดันไฟฟ้าที่กําหนด: |
| Maximum operating pressure: | ความดันใช้งานสูงสุด: |
| Ambient temperature range: | ช่วงอุณหภูมิแวดล้อม: |
| Warranty period: | ระยะเวลารับประกัน: |
| Service life: | อายุการใช้งาน: |

### 8b. Quality Certifications in Thailand

| Certification | Thai Name | Notes |
|---------------|-----------|-------|
| TIS (มอก.) | มาตรฐานผลิตภัณฑ์อุตสาหกรรม | Mandatory for 100+ product categories |
| Thai Green Label | ฉลากเขียว | Environmental certification |
| BOI promotion | สิทธิประโยชน์จาก BOI | Tax and duty privileges |
| ISO 45001 | ระบบจัดการอาชีวอนามัยฯ | OHS management |
| FDA Thailand | อย. | Food and Drug Admin registration |

### 9. Sign-off Block for Technical Documents

| Role (English) | Role (Thai) | Abbreviation |
|----------------|-------------|--------------|
| Designed by | ผู้เขียนแบบ | อก. |
| Checked by | ผู้ตรวจแบบ | ตร. |
| Approved by | ผู้อนุมัติ | อน. |

**Block format**:
```
| อก. | [Name] | [Date] |
| ตร. | [Name] | [Date] |
| อน. | [Name] | [Date] |
```

### 10. Handling Numerical Precision

- Maintain same precision as source
- Tolerance: ± ค่าความคลาดเคลื่อน (e.g., 100 ± 2 มม.)
- Range: ระหว่าง...ถึง... or ...-...
- Minimum/Maximum: ค่าต่ําสุด / ค่าสูงสุด
- Nominal value: ค่าประจํา (e.g., แรงดันประจํา = nominal voltage)

---

**End of technical.md**
