---
id: ms/domain/technical
type: domain
target_lang: ms
name: Domain: Technical (Malay — MS)
description: Translation rules for technical and engineering documents into Malay
---

## Reader Model

**Who reads this document and what do they expect?**

Technical document readers in Malaysia are engineers, IT professionals, system administrators, technicians, researchers, and technical managers. They read the document to understand specifications, follow procedures, troubleshoot systems, or implement technical solutions. They expect:

- **Terminological precision** — technical Malay has established terminology for most fields. Using the wrong term can cause confusion or incorrect implementation.
- **Consistency** — technical documents demand consistent terminology throughout. A single term must map to a single concept.
- **Clarity over elegance** — technical translation prioritizes accuracy and readability over literary style. Sentences should be clear and direct.
- **Appropriate loanword usage** — many technical terms are borrowed from English. The translator must decide whether to use the English loanword or the Malay equivalent based on industry convention.
- **Standard formatting** — technical documents follow established conventions for units, measurements, abbreviations, and code references.

**What would break their trust?**
- Mistranslated technical terms that change the meaning of specifications.
- Inconsistent terminology that makes the document confusing.
- Incorrect unit conversions or formatting.
- Unnecessary Malay-ization of universally recognized English technical terms.

## Decision Framework

### 1. Technology Terminology: Loanword vs Malay

Malay technical vocabulary exists on a spectrum from fully adopted English loanwords to purely Malay-origin terms. The translator must choose based on industry convention.

| Category | Recommendation | Examples |
|---|---|---|
| Universally recognized tech terms | Keep English loanword | `internet`, `WiFi`, `Bluetooth`, `GPS`, `USB`, `CPU`, `RAM` |
| Common IT terms with standard Malay | Use Malay term where established | `perisian` (software), ` perkakasan` (hardware), ` rangkaian` (network) |
| Emerging tech with no standard Malay | Keep English or use descriptive Malay | `cloud computing` / `pengkomputeran awan` |
| Engineering terms with standard Malay | Use Malay term | `gear` → `gear` (preserved), `bearing` → `galas`, `welding` → `kimpalan` |
| Industry-specific jargon | Keep English if industry uses it | `API`, `SDK`, `DevOps`, `agile`, `scrum` |

**Critical rule**: When in doubt, check whether Dewan Bahasa dan Pustaka (DBP) has published an official Malay equivalent. If DBP has a published term, use it. If not, the English loanword is acceptable.

### 2. IT and Software Terminology

| English | Malay (DBP) | English Loanword (common) | Notes |
|---|---|---|---|
| Software | Perisian | Software | Both accepted; `perisian` preferred in formal |
| Hardware | Perkakasan | Hardware | Both accepted; `perkakasan` preferred in formal |
| Database | Pangkalan data | Database | `Pangkalan data` is DBP standard |
| Algorithm | Algoritma | Algorithm | Same spelling |
| Encryption | Penyulitan | Encryption | `Penyulitan` is DBP standard |
| Firewall | Tembok api | Firewall | `Tembok api` is literal but recognized |
| Server | Pelayan | Server | Both used |
| Client | Pelanggan | Client | Context-dependent (`pelanggan` also means "customer") |
| Network | Rangkaian | Network | `Rangkaian` is standard |
| Bandwidth | Lebar jalur | Bandwidth | `Lebar jalur` is DBP standard |
| Cloud | Awan | Cloud | `Awan` is the Malay word |
| Download | Muat turun | Download | `Muat turun` is DBP standard |
| Upload | Muat naik | Upload | `Muat naik` is DBP standard |
| Login | Log masuk | Login | Both used |
| Logout | Log keluar | Logout | Both used |
| Password | Kata laluan | Password | `Kata laluan` is DBP standard |
| User name | Nama pengguna | Username | `Nama pengguna` is standard |
| Interface | Antara muka | Interface | `Antara muka` is DBP standard |
| Platform | Platform | Platform | Loanword widely used |
| Bug | Pepijat | Bug | `Pepijat` is DBP term; `bug` is also common |
| Update | Kemas kini | Update | `Kemas kini` is standard |
| Installation | Pemasangan | Installation | `Pemasangan` is standard |
| Compiler | Pengkompil | Compiler | `Pengkompil` is DBP term |
| Debugger | Penyahpijat | Debugger | `Penyahpijat` is DBP term |

### 3. Engineering Terminology

| English | Malay | Notes |
|---|---|---|
| Torque | Tork | From English; Malay equivalent rare in practice |
| Welding | Kimpalan | Standard Malay |
| Drilling | Penggerudian | Standard Malay |
| Machining | Pemesinan | Standard Malay |
| CNC (Computer Numerical Control) | CNC (Kawalan Numerik Berkomputer) | Acronym preserved |
| CAD (Computer-Aided Design) | Rekabentuk Berbantukan Komputer (RBK) | Or simply `CAD` |
| CAM (Computer-Aided Manufacturing) | Pembuatan Berbantukan Komputer | Or simply `CAM` |
| Tolerance |alaran | Engineering precision term |
| Dimension | Dimensi | Loanword widely used |
| Diameter | Diameter | Loanword widely used |
| Voltage | Voltan | Loanword widely used |
| Current | Arus | Standard Malay |
| Resistance | Rintangan | Standard Malay |
| Capacity | Kapasiti | Loanword widely used |
| Load | Beban | Standard Malay |
| Stress | Tegangan | Context-dependent |
| Strain | Peregangan / Regangan | Engineering context |
| Friction | Geseran | Standard Malay |
| Insulation | Penebat | Standard Malay |
| Conductor | Konduktor / Pengalir | Both used |

### 4. Units and Measurements

| Element | Convention |
|---|---|
| SI units | Use standard SI abbreviations: `m`, `kg`, `s`, `A`, `K`, `mol`, `cd` |
| No period after SI units | `kg` (not `kg.`), `m` (not `m.`) |
| Space between number and unit | `10 kg` (not `10kg`) |
| Temperature | `°C` or `darjah Celcius` (note: `Celsius` not `Centigrade`) |
| Electrical | `V` (volt), `A` (ampere), `Ω` or `ohm` (resistansi) |
| Computer storage | `KB`, `MB`, `GB`, `TB` (capital letters for binary) |
| Binary prefixes | `KiB`, `MiB`, `GiB`, `TiB` (when precision is needed) |
| Percentages | `50 %` (space before `%`) or `50 peratus` |
| Ranges | `10 mm - 20 mm` or `10 mm hingga 20 mm` |
| Approximation | `lebih kurang 10 mm` or `≈ 10 mm` |

### 5. Documentation and UI Terms

| English | Malay | Notes |
|---|---|---|
| User Manual | Manual Pengguna | Standard |
| User Guide | Panduan Pengguna | Standard |
| Installation Guide | Panduan Pemasangan | Standard |
| Quick Start Guide | Panduan Permulaan Pantas | Standard |
| Troubleshooting | Penyelesaian masalah | Standard |
| Frequently Asked Questions (FAQ) | Soalan Lazim (SL) | Standard |
| Terms and Conditions | Terma dan Syarat | Standard |
| Privacy Policy | Dasar Privasi | Standard |
| Click | Klik | Loanword universally used |
| Double-click | Dwiklik / Klik dua kali | Both used |
| Right-click | Klik kanan | Standard |
| Drag and drop | Seret dan lepas | Standard |
| Scroll | Tatal | Standard |
| Menu | Menu | Loanword universally used |
| Toolbar | Bar alat | Standard |
| Checkbox | Kotak semak | Standard |
| Dropdown | Senarai turun / Juntai bawah | Both used |
| Dialog box | Kotak dialog | Standard |
| Error message | Mesej ralat | Standard |
| Warning | Amaran | Standard |
| Save | Simpan | Standard |
| Cancel | Batal | Standard |
| Submit | Hantar | Standard |
| Search | Cari | Standard |
| Settings | Tetapan | Standard |
| Help | Bantuan | Standard |

## Error Pattern Library

### Critical Errors (zero tolerance)

| Error | Why It Is Critical |
|---|---|
| **Wrong technical term** | Using `pelayan` (server) where `pelanggan` (client) is intended changes the entire technical meaning. Verify terms carefully. |
| **Incorrect unit formatting** | `10kg` (no space) vs `10 kg` (correct) — the space is required by SI convention. |
| **Mixed measurement systems** | Do not mix metric and imperial without conversion. Malaysia uses metric. |
| **Wrong number formatting** | `1.000 mm` (one thousand mm) vs `1,000 mm` (same in English) — ensure correct separator for Malay context. |

### Common Errors (frequent in practice)

| Error | Guidance |
|---|---|
| **Over-Malay-izing universal terms** | Do not translate `WiFi`, `Bluetooth`, `USB`, `CPU` — these are universal. Use the established Malay term only if DBP has one. |
| **Inconsistent terminology** | If you use `pangkalan data` for "database" once, use it every time. Do not switch to `database` mid-document. |
| **Missing abbreviation expansion** | Always expand abbreviations on first use: `Perisian Berjenama Terbuka (PBT)` then `PBT` thereafter. |
| **Wrong passive construction** | Technical Malay uses active voice more than formal Malay: `Sistem mengesahkan data` (active) is often preferred over `Data disahkan oleh sistem` (passive) in technical writing. |

### Subtle Errors (easy to miss)

| Error | Guidance |
|---|---|
| **False cognates** | `Aktual` means "current/relevant" in Malay, not "actual." Use `sebenar` for "actual." |
| **Code formatting** | Code snippets, variable names, and function names should NOT be translated. Keep them in English: `function getData()` (not `function dapatData()`). |
| **Inconsistent capitalization of borrowed terms** | Some terms are always lowercase in Malay (`internet`, `software`) while acronyms are always uppercase (`CPU`, `RAM`). Follow standard conventions. |

## Domain-Specific Reference

### Technical Document Structure

| Section | Malay Title | Purpose |
|---|---|---|
| Abstract | Abstrak | Brief summary |
| Introduction | Pengenalan | Background and objectives |
| Methodology | Kaedah | How the work was done |
| Results | Keputusan / Hasil | Findings |
| Discussion | Perbincangan | Analysis of results |
| Conclusion | Kesimpulan | Summary and implications |
| References | Rujukan | Sources cited |
| Appendix | Lampiran | Supporting materials |

### Common Technical Abbreviations

| Abbreviation | Malay | English |
|---|---|---|
| API | API (preserved) | Application Programming Interface |
| SQL | SQL (preserved) | Structured Query Language |
| HTML | HTML (preserved) | Hypertext Markup Language |
| CSS | CSS (preserved) | Cascading Style Sheets |
| IoT | IoT (preserved) | Internet of Things |
| AI | AI (preserved) | Artificial Intelligence |
| ML | ML (preserved) | Machine Learning |
| VR | VR (preserved) | Virtual Reality |
| AR | AR (preserved) | Augmented Reality |
| POS | POS (preserved) | Point of Sale |
| ERP | ERP (preserved) | Enterprise Resource Planning |
| CRM | CRM (preserved) | Customer Relationship Management |

### Engineering Drawing Annotations (Malay)

| Element | Malay | ISO Standard |
|---|---|---|
| Diameter | Diameter (dia.) | ISO 128 |
| Radius | Radius (R) | ISO 128 |
| Depth | Kedalaman (Kd.) | ISO 128 |
| Counterbore | Lubang bekas (Lb.) | ISO 128 |
| Countersink | Lubang runcing (Lr.) | ISO 128 |
| Surface finish | Kemasan permukaan | ISO 1302 |
| Tolerance | Keizinan /alaran | ISO 2768 |
| Material | Bahan | — |
| Scale | Skala | — |
| Weight | Berat | — |
