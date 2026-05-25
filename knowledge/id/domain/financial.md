# Domain: Financial (Keuangan) — Indonesian

## 1. Reader Model: How to Read Indonesian Financial Documents

### 1.1 Macro-Level Architecture

Indonesian financial documents follow a structure governed by PSAK (Pernyataan Standar Akuntansi Keuangan), the Indonesian adaptation of IFRS, regulated by the Financial Services Authority (OJK — Otoritas Jasa Keuangan) and the Indonesian Institute of Accountants (IAI — Ikatan Akuntan Indonesia). Two primary frameworks exist:

- **PSAK IFRS-based:** For publicly accountable entities (full IFRS alignment)
- **SAK-ETAP (Standar Akuntansi Keuangan untuk Entitas Tanpa Akuntabilitas Publik):** For SMEs — simplified

**Typical financial statement structure (Laporan Keuangan):**

```
    [Laporan Posisi Keuangan / Statement of Financial Position] — Balance Sheet
        → [ASET / ASSETS]
            → Aset Lancar / Current Assets
                → Kas dan Setara Kas / Cash and Cash Equivalents
                → Piutang Usaha / Trade Receivables
                → Persediaan / Inventories
                → Biaya Dibayar Dimuka / Prepaid Expenses
            → Aset Tidak Lancar / Non-Current Assets
                → Aset Tetap / Fixed Assets (Property, Plant, Equipment)
                → Aset Tak Berwujud / Intangible Assets
                → Aset Pajak Tangguhan / Deferred Tax Assets
        → [LIABILITAS DAN EKUITAS / LIABILITIES AND EQUITY]
            → Liabilitas Jangka Pendek / Current Liabilities
            → Liabilitas Jangka Panjang / Non-Current Liabilities
            → Ekuitas / Equity
    [Laporan Laba Rugi dan Penghasilan Komprehensif Lain / Income Statement & OCI]
        → Pendapatan / Revenue
        → Beban Pokok Pendapatan / Cost of Revenue
        → Laba Bruto / Gross Profit
        → Beban Usaha / Operating Expenses
        → Laba Usaha / Operating Profit
        → Pendapatan/(Beban) Lain-Lain / Other Income/(Expenses)
        → Laba Sebelum Pajak / Profit Before Tax
        → Beban Pajak Penghasilan / Income Tax Expense
        → Laba Tahun Berjalan / Profit for the Year
    [Laporan Arus Kas / Statement of Cash Flows]
        → Arus Kas dari Aktivitas Operasi / Operating Activities
        → Arus Kas dari Aktivitas Investasi / Investing Activities
        → Arus Kas dari Aktivitas Pendanaan / Financing Activities
    [Laporan Perubahan Ekuitas / Statement of Changes in Equity]
    [Catatan atas Laporan Keuangan / Notes to Financial Statements]
```

**Typical internal memo structure:**

```
    [MEMORANDUM]
        → Kepada / To:
            → Dari / From:
                → Hal / Subject:
                    → Tanggal / Date:
                        → Isi / Body
```

### 1.2 Meso-Level Patterns

**Move 1: Header and Identification**
- Company name, "dan entitas anaknya" (and its subsidiaries) for consolidated statements
- Period: "Untuk tahun yang berakhir pada tanggal 31 Desember 2024" (For the year ended 31 December 2024)
- Currency: "Disajikan dalam Rupiah" (Expressed in Rupiah)

**Move 2: Accounting Policy Notes (Ikhtisar Kebijakan Akuntansi)**
- First section of Catatan atas Laporan Keuangan
- Contains: basis of preparation, functional currency, significant judgments, key accounting policies

**Move 3: Breakdown Notes**
- Systematic breakdown of each line item
- "Piutang Usaha" → aging analysis, collectibility, allowance
- "Aset Tetap" → cost, depreciation method, accumulated depreciation, carrying amount

### 1.3 Micro-Level Patterns

**Passive disclosure language:**
- "diakui" → recognized
- "dicatat" → recorded
- "disajikan" → presented
- "diukur" → measured
- "diestimasi" → estimated

**Time references:**
- "Tahun berjalan" → Current year
- "Tahun sebelumnya" / "Periode lalu" → Prior year / Previous period
- "Pada tanggal" → As at / As of (specific date)
- "Untuk tahun yang berakhir pada" → For the year ended
- "Selama tahun berjalan" → During the current year

**Comparative format:** Two columns side by side: current year and prior year.

---

## 2. Decision Framework

### Table 1: Core Financial Statement Terminology

| Indonesian (PSAK) | English Translation | Notes |
|---|---|---|
| Laporan Posisi Keuangan | Statement of Financial Position | PSAK 1 (revised) — previously "Neraca" |
| Laporan Laba Rugi dan Penghasilan Komprehensif Lain | Statement of Profit or Loss and Other Comprehensive Income | PSAK 1 |
| Laporan Arus Kas | Statement of Cash Flows | PSAK 2 |
| Laporan Perubahan Ekuitas | Statement of Changes in Equity | PSAK 1 |
| Catatan atas Laporan Keuangan (CaLK) | Notes to the Financial Statements | Standard abbreviation |
| Laporan Keuangan Konsolidasian | Consolidated Financial Statements | PSAK 4 |
| Laporan Keuangan Tersendiri | Separate Financial Statements | PSAK 4 |
| Periode Pelaporan | Reporting Period | Direct |
| Tahun Buku | Fiscal Year | Direct |
| Entitas | Entity | Direct |
| Entitas Anak | Subsidiary | PSAK 4 |
| Entitas Asosiasi | Associate | PSAK 15 |
| Perusahaan Induk | Parent Entity | Direct |
| Pengendali | Controlling Entity / Parent | Direct |
| Pihak Berelasi | Related Party | PSAK 7 |
| Segmen Operasi | Operating Segments | PSAK 5 |
| Kelompok Usaha | Group (of companies) | Direct |

### Table 2: Balance Sheet — Asset Classification

| Indonesian (PSAK) | English Translation | Notes |
|---|---|---|
| Aset Lancar | Current Assets | PSAK 1 classification |
| Kas dan Setara Kas | Cash and Cash Equivalents | PSAK 2 (includes bank deposits <3 months) |
| Piutang Usaha | Trade Receivables | From sales of goods/services |
| Piutang Lain-lain | Other Receivables | Non-trade receivables |
| Piutang Pihak Berelasi | Due from Related Parties | PSAK 7 |
| Persediaan | Inventories | PSAK 14 |
| Beban Dibayar Dimuka | Prepaid Expenses | Direct |
| Pajak Dibayar Dimuka | Prepaid Tax | Income tax prepayment |
| Uang Muka | Advances | Advance payments to suppliers |
| Aset Keuangan Lancar Lainnya | Other Current Financial Assets | Various |
| Aset Tidak Lancar (Aset Non-Lancar) | Non-Current Assets | PSAK 1 classification |
| Aset Tetap | Property, Plant, and Equipment (PPE) | PSAK 16 |
| Akumulasi Penyusutan | Accumulated Depreciation | Direct |
| Aset Tak Berwujud | Intangible Assets | PSAK 19 |
| Goodwill | Goodwill | PSAK 22 (Business Combinations) |
| Aset Pajak Tangguhan | Deferred Tax Assets | PSAK 46 |
| Aset Tetap dalam Penyelesaian | Construction in Progress | PSAK 16 |
| Aset Keuangan Tidak Lancar | Non-Current Financial Assets | Various |
| Beban Ditangguhkan | Deferred Charges | Pre-operating costs, etc. |
| Aset Tidak Lancar Lainnya | Other Non-Current Assets | Catch-all |

### Table 3: Balance Sheet — Liability and Equity Classification

| Indonesian (PSAK) | English Translation | Notes |
|---|---|---|
| Liabilitas Jangka Pendek | Current Liabilities | PSAK 1 |
| Utang Usaha | Trade Payables | Direct |
| Utang Lain-lain | Other Payables | Direct |
| Utang Bank Jangka Pendek | Short-Term Bank Loans | Direct |
| Utang Pihak Berelasi | Due to Related Parties | PSAK 7 |
| Utang Pajak | Taxes Payable | Direct |
| Beban Masih Harus Dibayar | Accrued Expenses | Direct |
| Pendapatan Diterima Dimuka | Unearned Revenue / Deferred Income | Direct |
| Utang Dividen | Dividends Payable | Direct |
| Utang Pembiayaan | Financing Payables | Leasing/finance |
| Bagian Utang Jangka Panjang Jatuh Tempo dalam Satu Tahun | Current Maturities of Long-Term Debt | Direct |
| Liabilitas Jangka Panjang | Non-Current Liabilities | PSAK 1 |
| Utang Bank Jangka Panjang | Long-Term Bank Loans | Direct |
| Utang Obligasi | Bonds Payable | Direct |
| Liabilitas Imbalan Kerja | Employee Benefits Liability | PSAK 24 |
| Liabilitas Pajak Tangguhan | Deferred Tax Liabilities | PSAK 46 |
| Liabilitas Sewa | Lease Liabilities | PSAK 73 (IFRS 16) |
| Pinjaman Pemegang Saham | Shareholder Loans | Specific |
| Provisi | Provisions | PSAK 57 |
| Ekuitas | Equity | Direct |
| Modal Saham | Share Capital | Direct |
| Modal Dasar | Authorized Capital | Company law |
| Modal Ditempatkan dan Disetor Penuh | Issued and Fully Paid Capital | Direct |
| Agio Saham / Tambahan Modal Disetor | Additional Paid-In Capital / Share Premium | Direct |
| Saldo Laba / Laba Ditahan | Retained Earnings | Direct |
| Cadangan | Reserves | Various types |
| Kepentingan Non-Pengendali (KNP) | Non-Controlling Interest (NCI) | PSAK 4 — previously "Hak Minoritas" |
| Ekuitas yang Dapat Diatribusikan kepada Pemilik | Equity Attributable to Owners | PSAK 1 |
| Rugi Tahun Berjalan | Loss for the Year | Contra-equity |

### Table 4: Income Statement Terminology

| Indonesian (PSAK) | English Translation | Notes |
|---|---|---|
| Pendapatan | Revenue | PSAK 72 (IFRS 15) |
| Pendapatan Usaha | Operating Revenue | Direct |
| Pendapatan Lainnya | Other Income | Non-operating |
| Beban Pokok Pendapatan | Cost of Revenue | Direct |
| Beban Pokok Penjualan | Cost of Goods Sold (COGS) | For product companies |
| Beban Pokok Pendapatan | Cost of Revenue | For service companies |
| Laba Bruto | Gross Profit | Direct |
| Beban Usaha | Operating Expenses | Direct |
| Beban Penjualan | Selling Expenses | Direct |
| Beban Umum dan Administrasi | General and Administrative Expenses | Direct |
| Beban Gaji dan Tunjangan | Salaries and Allowances Expense | Direct |
| Beban Penyusutan dan Amortisasi | Depreciation and Amortization Expense | Direct |
| Beban Pemasaran | Marketing Expenses | Direct |
| Beban Transportasi | Transportation Expenses | Direct |
| Beban Sewa | Rental Expense | Direct |
| Beban Keuangan | Finance Costs | Direct |
| Beban Bunga | Interest Expense | Direct |
| Pendapatan Bunga | Interest Income | Direct |
| Pendapatan Dividen | Dividend Income | Direct |
| Keuntungan/(Kerugian) Selisih Kurs | Foreign Exchange Gain/(Loss) | Direct |
| Laba/(Rugi) Usaha | Operating Profit/(Loss) | Direct |
| Laba/(Rugi) Sebelum Pajak | Profit/(Loss) Before Tax | Direct |
| Beban/(Manfaat) Pajak Penghasilan | Income Tax Expense/(Benefit) | Direct |
| Laba/(Rugi) Tahun Berjalan | Profit/(Loss) for the Year | Direct |
| Penghasilan/(Rugi) Komprehensif Lain | Other Comprehensive Income/(Loss) | PSAK 1 |
| Jumlah Laba/(Rugi) Komprehensif | Total Comprehensive Income/(Loss) | Direct |
| Laba per Saham (LPS) | Earnings Per Share (EPS) | PSAK 56 (IAS 33) |
| Laba per Saham Dasar | Basic Earnings Per Share | Direct |
| Laba per Saham Dilusian | Diluted Earnings Per Share | Direct |
| EBITDA | EBITDA | Keep (universal) |
| EBIT | EBIT | Keep (universal) |

### Table 5: Cash Flow Statement Terminology

| Indonesian | English Translation | Notes |
|---|---|---|
| Arus Kas dari Aktivitas Operasi | Cash Flows from Operating Activities | PSAK 2 |
| Penerimaan Kas dari Pelanggan | Cash Receipts from Customers | Direct |
| Pembayaran Kas kepada Pemasok dan Karyawan | Cash Payments to Suppliers and Employees | Direct |
| Pembayaran Bunga | Interest Paid | Direct |
| Penerimaan Bunga | Interest Received | Direct |
| Pembayaran Pajak Penghasilan | Income Tax Paid | Direct |
| Arus Kas Bersih dari Aktivitas Operasi | Net Cash Flows from Operating Activities | Direct |
| Arus Kas dari Aktivitas Investasi | Cash Flows from Investing Activities | PSAK 2 |
| Perolehan Aset Tetap | Acquisition of Fixed Assets | Direct |
| Hasil Penjualan Aset Tetap | Proceeds from Sale of Fixed Assets | Direct |
| Arus Kas Bersih dari Aktivitas Investasi | Net Cash Flows from Investing Activities | Direct |
| Arus Kas dari Aktivitas Pendanaan | Cash Flows from Financing Activities | PSAK 2 |
| Penerimaan Pinjaman Bank | Proceeds from Bank Loans | Direct |
| Pembayaran Pinjaman Bank | Repayment of Bank Loans | Direct |
| Pembayaran Dividen | Dividends Paid | Direct |
| Penerbitan Saham | Issuance of Shares | Direct |
| Arus Kas Bersih dari Aktivitas Pendanaan | Net Cash Flows from Financing Activities | Direct |
| Kenakan/(Penurunan) Bersih Kas dan Setara Kas | Net Increase/(Decrease) in Cash and Cash Equivalents | Direct |
| Kas dan Setara Kas Awal Tahun | Cash and Cash Equivalents at Beginning of Year | Direct |
| Kas dan Setara Kas Akhir Tahun | Cash and Cash Equivalents at End of Year | Direct |
| Metode Langsung | Direct Method | PSAK 2 (allowed) |
| Metode Tidak Langsung | Indirect Method | PSAK 2 (more common) |

### Table 6: Financial Ratios and Performance Metrics

| Indonesian | English Translation | Formula (IDR terms) |
|---|---|---|
| Rasio Lancar | Current Ratio | Aset Lancar / Liabilitas Jangka Pendek |
| Rasio Cepat (Acid Test) | Quick Ratio | (Aset Lancar - Persediaan) / Liabilitas Jangka Pendek |
| Rasio Kas | Cash Ratio | (Kas + Setara Kas) / Liabilitas Jangka Pendek |
| Rasio Hutang terhadap Ekuitas | Debt-to-Equity Ratio (DER) | Total Liabilitas / Total Ekuitas |
| Rasio Hutang terhadap Aset | Debt-to-Asset Ratio | Total Liabilitas / Total Aset |
| Margin Laba Kotor | Gross Profit Margin | Laba Bruto / Pendapatan |
| Margin Laba Usaha | Operating Profit Margin | Laba Usaha / Pendapatan |
| Margin Laba Bersih | Net Profit Margin | Laba Tahun Berjalan / Pendapatan |
| Imbal Hasil Aset (ROA) | Return on Assets (ROA) | Laba Tahun Berjalan / Total Aset |
| Imbal Hasil Ekuitas (ROE) | Return on Equity (ROE) | Laba Tahun Berjalan / Total Ekuitas |
| Perputaran Persediaan | Inventory Turnover | Beban Pokok Penjualan / Rata-rata Persediaan |
| Perputaran Piutang | Receivables Turnover | Pendapatan / Rata-rata Piutang |
| Rasio Pembayaran Dividen | Dividend Payout Ratio | Dividen / Laba Tahun Berjalan |
| Rasio Kecukupan Modal (CAR) | Capital Adequacy Ratio (CAR) | Modal / ATMR (banking) |

### Table 7: Accounting Policy Terminology

| Indonesian (PSAK) | English Translation | Notes |
|---|---|---|
| Dasar Penyusunan | Basis of Preparation | PSAK 1 |
| Mata Uang Fungsional | Functional Currency | PSAK 10 (IAS 21) |
| Mata Uang Pelaporan | Presentation Currency | PSAK 10 |
| Kebijakan Akuntansi | Accounting Policies | PSAK 1 |
| Estimasi Akuntansi | Accounting Estimates | PSAK 8 |
| Perubahan Kebijakan Akuntansi | Changes in Accounting Policies | PSAK 8 |
| Koreksi Kesalahan | Correction of Errors | PSAK 8 |
| Peristiwa Setelah Periode Pelaporan | Events After the Reporting Period | PSAK 8 (IAS 10) |
| Nilai Wajar | Fair Value | PSAK 68 (IFRS 13) |
| Biaya Perolehan | Cost / Acquisition Cost | Direct |
| Nilai Tercatat | Carrying Amount | Direct |
| Jumlah Tercatat | Carrying Amount | Alternate term |
| Nilai Sisa | Residual Value | Depreciation |
| Masa Manfaat | Useful Life | Depreciation |
| Tarif Penyusutan | Depreciation Rate | Direct |
| Metode Garis Lurus | Straight-Line Method | PSAK 16 |
| Metode Saldo Menurun | Declining Balance Method | PSAK 16 |
| Metode Unit Produksi | Units of Production Method | PSAK 16 |
| Amortisasi | Amortization | Intangible assets |
| Penurunan Nilai / Impairment | Impairment | PSAK 48 (IAS 36) |
| Pemulihan Rugi Penurunan Nilai | Reversal of Impairment Loss | PSAK 48 |
| Revaluasi | Revaluation | PSAK 16 (IAS 16) |
| Pengakuan Pendapatan | Revenue Recognition | PSAK 72 |
| Biaya Pinjaman | Borrowing Costs | PSAK 26 (IAS 23) |
| Sewa | Leases | PSAK 73 (IFRS 16) |
| Pajak Penghasilan | Income Taxes | PSAK 46 (IAS 12) |
| Imbalan Kerja | Employee Benefits | PSAK 24 (IAS 19) |
| Provisi, Liabilitas Kontinjensi, dan Aset Kontinjensi | Provisions, Contingent Liabilities, and Contingent Assets | PSAK 57 (IAS 37) |
| Transaksi dengan Pihak Berelasi | Related Party Transactions | PSAK 7 (IAS 24) |
| Kombinasi Bisnis | Business Combinations | PSAK 22 (IFRS 3) |
| Konsolidasi | Consolidation | PSAK 4 |
| Instrumen Keuangan | Financial Instruments | PSAK 71, 60, 55 (IFRS 9) |
| Penjabaran Mata Uang Asing | Foreign Currency Translation | PSAK 10 (IAS 21) |

### Table 8: Audit and Assurance Terminology

| Indonesian | English Translation | Notes |
|---|---|---|
| Audit | Audit | Direct |
| Laporan Auditor Independen | Independent Auditor's Report | Standard |
| Opini Audit | Audit Opinion | Direct |
| Wajar Tanpa Pengecualian (WTP) | Unqualified Opinion | Best opinion |
| Wajar Dengan Pengecualian (WDP) | Qualified Opinion | With exceptions |
| Tidak Wajar | Adverse Opinion | Direct |
| Tidak Memberikan Pendapat | Disclaimer of Opinion | Direct |
| Laporan Keuangan Diaudit | Audited Financial Statements | Direct |
| Entitas Audit | Audited Entity | Direct |
| Audit Umum | General Audit | Full scope |
| Audit Khusus | Special Audit | Limited scope |
| KAP (Kantor Akuntan Publik) | Public Accounting Firm | CPA Firm |
| Akuntan Publik (AP) | Public Accountant | Certified |
| Akuntan Publik Terdaftar | Registered Public Accountant | OJK registration |
| Standar Audit (SA) | Auditing Standards | Adoption of ISA |
| Kode Etik Akuntan | Code of Ethics for Accountants | IAI Kode Etik |
| Pengendalian Mutu | Quality Control | SA 220 (ISQC 1) |
| Risiko Audit | Audit Risk | Direct |
| Materialitas | Materiality | Direct |
| Pengujian Pengendalian | Test of Controls | Direct |
| Pengujian Substantif | Substantive Testing | Direct |
| Sampling Audit | Audit Sampling | Direct |
| Bukti Audit | Audit Evidence | Direct |
| Kertas Kerja Audit (KKA) | Audit Working Papers | Direct |
| Komite Audit | Audit Committee | Board-level |
| Auditor Internal | Internal Auditor | Direct |
| Satuan Pengawasan Intern (SPI) | Internal Audit Unit | Government entities |
| BPK (Badan Pemeriksa Keuangan) | Audit Board of Indonesia | State audit body |
| BPKP (Badan Pengawasan Keuangan dan Pembangunan) | Financial and Development Supervisory Board | Government internal audit |

### Table 9: Tax Accounting and Reporting Terms

| Indonesian | English Translation | Notes |
|---|---|---|
| Pajak Penghasilan (PPh) | Income Tax | Direct |
| Pajak Pertambahan Nilai (PPN) | Value Added Tax (VAT) | Currently 11% |
| Pajak Penjualan atas Barang Mewah (PPnBM) | Luxury Goods Sales Tax | Direct |
| Surat Pemberitahuan Tahunan (SPT) | Annual Tax Return | Direct |
| SPT Tahunan PPh Badan | Annual Corporate Income Tax Return | Direct |
| Surat Ketetapan Pajak (SKP) | Tax Assessment Letter | Direct |
| Surat Tagihan Pajak (STP) | Tax Collection Letter | Direct |
| Surat Keputusan Keberatan | Objection Decision Letter | Tax objection |
| Pemeriksaan Pajak | Tax Audit | Direct |
| Koreksi Fiskal | Fiscal Reconciliation | Book-to-tax adjustment |
| Laba/(Rugi) Fiskal | Taxable Profit/(Loss) | Fiscal result |
| Kompensasi Kerugian Fiskal | Tax Loss Carryforward | Direct |
| Pajak Kini | Current Tax | Tax payable for current period |
| Pajak Tangguhan | Deferred Tax | PSAK 46 |
| Aset Pajak Tangguhan | Deferred Tax Assets | Direct |
| Liabilitas Pajak Tangguhan | Deferred Tax Liabilities | Direct |
| Beban Pajak Kini | Current Tax Expense | Direct |
| Manfaat Pajak | Tax Benefit | Direct |
| Tarif Efektif Pajak | Effective Tax Rate | Direct |
| Angsuran PPh Pasal 25 | Monthly Income Tax Installment (PPh 25) | Direct |
| PPh Final | Final Income Tax | Various final-rate regimes |
| Dasar Pengenaan Pajak (DPP) | Tax Base | Direct |
| Faktur Pajak | Tax Invoice | PPN instrument |
| Pengkreditan Pajak Masukan | Input Tax Credit | PPN recovery |
| Pajak Keluaran | Output Tax | PPN on sales |
| Pengusaha Kena Pajak (PKP) | Registered VAT Entrepreneur | Direct |
| Norma Penghitungan Penghasilan Neto (NPPN) | Net Income Calculation Norms | Simplified tax for SMEs |

### Table 10: Banking and Capital Market Terminology

| Indonesian | English Translation | Notes |
|---|---|---|
| OJK (Otoritas Jasa Keuangan) | Financial Services Authority | Integrated financial regulator |
| Bank Indonesia (BI) | Bank Indonesia | Central bank |
| Lembaga Penjamin Simpanan (LPS) | Deposit Insurance Corporation | Direct |
| Bursa Efek Indonesia (BEI) | Indonesia Stock Exchange (IDX) | Direct |
| Indeks Harga Saham Gabungan (IHSG) | Composite Stock Price Index (JCI) | Direct |
| Laporan Keuangan Publikasi | Published Financial Statements | OJK filing |
| Laporan Tahunan | Annual Report | Direct |
| Prospektus | Prospectus | Direct |
| Pernyataan Pendaftaran | Registration Statement | IPO process |
| Penawaran Umum Perdana (IPO) | Initial Public Offering (IPO) | Direct |
| Penawaran Umum Terbatas (PUT) | Rights Issue | Direct |
| Obligasi | Bond | Direct |
| Sukuk | Sukuk (Islamic Bond) | Sharia finance |
| Reksa Dana | Mutual Fund | Direct |
| Dana Pensiun | Pension Fund | Direct |
| Asuransi | Insurance | Direct |
| Perusahaan Pembiayaan | Financing Company | Multi-finance |
| Kredit | Loan / Credit | Direct |
| Kredit Macet | Non-Performing Loan (NPL) | Direct |
| Rasio Kredit Bermasalah (NPL Ratio) | Non-Performing Loan Ratio | Direct |
| Agunan / Jaminan | Collateral | Direct |
| BI Rate / BI 7-Day Reverse Repo Rate | BI Rate | Policy rate |
| Sertifikat Bank Indonesia (SBI) | Bank Indonesia Certificates | Monetary instrument |
| Suku Bunga Dasar Kredit (SBDK) | Prime Lending Rate | Base lending rate |

### Table 11: Financial Document Abbreviations

| Abbreviation | Indonesian Full | English Translation |
|---|---|---|
| PSAK | Pernyataan Standar Akuntansi Keuangan | Statement of Financial Accounting Standards |
| SAK | Standar Akuntansi Keuangan | Financial Accounting Standards |
| SAK-ETAP | SAK untuk Entitas Tanpa Akuntabilitas Publik | SAK for Entities without Public Accountability |
| ISAK | Interpretasi Standar Akuntansi Keuangan | Interpretation of Financial Accounting Standards |
| PPSAK | Pencabutan PSAK | Revocation of PSAK |
| DSAK | Dewan Standar Akuntansi Keuangan | Financial Accounting Standards Board (IAI) |
| KAP | Kantor Akuntan Publik | Public Accounting Firm |
| LK | Laporan Keuangan | Financial Statements |
| LKK | Laporan Keuangan Konsolidasian | Consolidated Financial Statements |
| LKTT | Laporan Keuangan Tersendiri | Separate Financial Statements |
| LK Publikasi | Laporan Keuangan Publikasi | Published Financial Statements |
| CaLK | Catatan atas Laporan Keuangan | Notes to Financial Statements |
| LPS | Laba per Saham | Earnings Per Share (EPS) |
| ROA | Return on Assets (kept) | Return on Assets |
| ROE | Return on Equity (kept) | Return on Equity |
| NPL | Non-Performing Loan (kept) | Non-Performing Loan |
| CAR | Capital Adequacy Ratio (kept) | Capital Adequacy Ratio |
| BI | Bank Indonesia | Bank Indonesia |
| OJK | Otoritas Jasa Keuangan | Financial Services Authority |
| DJP | Direktorat Jenderal Pajak | Directorate General of Taxes |
| IAI | Ikatan Akuntan Indonesia | Indonesian Institute of Accountants |

### Table 12: Financial Report Boilerplate Phrases

| Indonesian | English Translation | Notes |
|---|---|---|
| Laporan keuangan terlampir | The accompanying financial statements | Standard cross-reference |
| Merupakan bagian yang tidak terpisahkan | Are an integral part of | Boilerplate |
| Disusun dan disajikan sesuai dengan | Prepared and presented in accordance with | Compliance statement |
| Manajemen bertanggung jawab atas | Management is responsible for | Responsibility statement |
| Menurut pendapat kami | In our opinion | Audit report |
| Menyajikan secara wajar, dalam semua hal yang material | Present fairly, in all material respects | True and fair view (audit) |
| Sesuai dengan Standar Akuntansi Keuangan di Indonesia | In accordance with Indonesian Financial Accounting Standards | Compliance |
| Tidak terdapat ketidakpastian material | No material uncertainty | Going concern |
| Setelah mempertimbangkan | Having considered | Board deliberation |
| Dengan mempertimbangkan risiko dan manfaat | Considering the risks and benefits | Judgment note |
| Dalam skenario yang mungkin terjadi | In reasonably possible scenarios | Sensitivity |
| Estimasi terbaik manajemen | Management's best estimate | Uncertainty |
| Tidak terdapat perubahan yang signifikan | No significant changes | Continuity statement |
| Informasi keuangan disajikan berdasarkan | Financial information is presented based on | Basis note |
| Angka-angka sebelumnya telah direklasifikasi | Prior year figures have been reclassified | Reclassification note |

### Table 13: Sharia (Islamic) Finance Terminology

| Indonesian | English Translation | Notes |
|---|---|---|
| Perbankan Syariah | Islamic Banking | UU No. 21/2008 |
| Akad | Contract / Agreement | Specific to sharia |
| Murabahah | Cost-plus Sale (Murabahah) | Keep + gloss |
| Mudharabah | Profit-Sharing (Mudharabah) | Keep + gloss |
| Musyarakah | Joint Venture (Musyarakah) | Keep + gloss |
| Ijarah | Lease (Ijarah) | Keep + gloss |
| Wakalah | Agency (Wakalah) | Keep + gloss |
| Kafalah | Guarantee (Kafalah) | Keep + gloss |
| Rahn | Pledge (Rahn) | Keep + gloss |
| Qardh | Benevolent Loan (Qardh) | Keep + gloss |
| Salam | Forward Sale (Salam) | Keep + gloss |
| Istishna | Manufacturing Contract (Istishna) | Keep + gloss |
| Sukuk | Islamic Bond (Sukuk) | Keep |
| Dewan Syariah Nasional (DSN) | National Sharia Board | MUI body |
| Fatwa DSN | DSN Fatwa / Sharia Ruling | Regulatory |
| Prinsip Syariah | Sharia Principles | Core concept |
| Bagi Hasil | Profit Sharing | Core mechanism |
| Nisbah | Profit Sharing Ratio | Contract term |
| Margin | Margin | For murabahah |
| Ujrah | Fee / Service Charge | For ijarah |
| Denda (Ta'zir) | Penalty (Ta'zir) | Late penalty (charitable) |
| Denda (Gharamah) | Penalty (Gharamah) | Late penalty (income) |
| BI Rate Syariah / SBIS | Sharia BI Certificate Rate | Monetary tool |

---

## 3. Standards

### 3.1 PSAK — Accounting Standards Framework

The Indonesian accounting standards are issued by **IAI (Ikatan Akuntan Indonesia)** through its **DSAK (Dewan Standar Akuntansi Keuangan)**.

**Three-tier framework:**
| Tier | Applies To | Standard |
|---|---|---|
| Tier 1 | Publicly accountable entities | PSAK (IFRS-based) |
| Tier 2 | Entities without public accountability | SAK-ETAP |
| Tier 3 | Micro, small, and medium entities | SAK-EMKM (SAK for MSMEs) |

**Transition from Dutch GAAP to IFRS:**
- Indonesia fully converged with IFRS through a phased approach (2008-2015)
- PSAK now substantially aligned with IFRS as issued by IASB
- Some modifications remain for local regulatory context
- Effective dates: IAI issues effective date in PSAK, typically 1 January of a given year

### 3.2 Regulatory Bodies

| Body | Role | English |
|---|---|---|
| OJK | Regulates financial services (banking, capital market, insurance) | Financial Services Authority |
| BI | Central bank: monetary policy, payment systems | Bank Indonesia |
| IAI | Professional body: accounting standards setting | Indonesian Institute of Accountants |
| DJP | Tax collection and administration | Directorate General of Taxes |
| Bapepam-LK (historical) | Former capital market regulator (merged into OJK 2013) | Capital Market and Financial Institution Supervisory Agency |

### 3.3 Reporting Currency and Format

- **Standard presentation currency:** Rupiah (IDR)
- **Rounding:** Typically presented in full Rupiah, thousands, or millions of Rupiah
  - "Disajikan dalam Rupiah penuh" → "Expressed in full Rupiah"
  - "Dalam ribuan Rupiah" → "In thousands of Rupiah" (most common for corporate)
  - "Dalam jutaan Rupiah" → "In millions of Rupiah"
- **Decimal/thousand separators:** ID conventions require comma as decimal, period as thousand separator
  - Translation: Swap to target language conventions

### 3.4 Audit Standards

- **SA (Standar Audit):** Indonesian audit standards, converged with ISA (International Standards on Auditing)
- **SPAP (Standar Profesional Akuntan Publik):** Professional standards for public accountants
- **Quality control:** SPM (Sistem Pengendalian Mutu) — converged with ISQC 1

### 3.5 Key Lexical Reference

| Indonesian | English | Notes |
|---|---|---|
| penyisihan | allowance / provision | For impairment, e.g., "penyisihan piutang" |
| cadangan | reserve | Equity reserve |
| provisi | provision | Liability of uncertain timing |
| estimasi | estimate | Accounting estimate |
| realisasi | realization | Actual outcome |
| pengakuan | recognition | Recognition of income/expense |
| pengukuran | measurement | Measurement of assets/liabilities |
| penghentian pengakuan | derecognition | Removal from financial statements |
| pengungkapan | disclosure | Notes disclosure |
| penyajian kembali | restatement | Restatement of comparatives |
| reklasifikasi | reclassification | Reclassification of items |
| penyesuaian | adjustment | Various adjustments |
| rekonsiliasi | reconciliation | Account reconciliation |
| konfirmasi | confirmation | Confirmation of balances |
| saldo | balance | Account balance |
| mutasi | movement | Movement in account |
| daftar | schedule / listing | Supporting schedule |
| rincian | breakdown / details | Detailed breakdown |
| ikhtisar | summary / overview | Summary schedule |
| sisa hasil usaha (SHU) | remaining income / surplus | Cooperative term |

### 3.6 Verification Checklist for Financial Translation

| Check | Description |
|---|---|
| Currency symbol/format | Rp → IDR — decimal/thousand separator swap verified |
| Rounding notation | "ribuan Rupiah" → "thousands of Rupiah" — consistent throughout |
| PSAK references | PSAK X (revised YYYY) → preserved with English gloss |
| Accounting equation | Assets = Liabilities + Equity — verify sub-totals and totals |
| Comparative columns | Current year / Prior year — preserve column alignment |
| Audit opinion type | WTP/WDP/Tidak Wajar/Tidak Memberikan Pendapat — correct mapping |
| Tax terms | Correct understanding of PPh, PPN, faktur pajak context |
| Acronym consistency | First-use expansion for ID-specific terms (PSAK, SAK, etc.) |
| Boilerplate consistency | Standard phrases translated uniformly across entire document |
| Number integrity | All financial figures double-checked (digit-for-digit match with source) |
| Footnotes/inline notes | Preserved and placed correctly |

---

**Revision History:** Initial domain knowledge base for Indonesian Financial translation.
