---
id: id/rules/scoring-rubric
type: rules
target_lang: id
name: Rubrik Penilaian Kualitas Terjemahan — Bahasa Indonesia
description: Indonesian translation quality scoring rubric
---

# Rubrik Penilaian Kualitas Terjemahan — Bahasa Indonesia

> Rubrik ini digunakan untuk menilai kualitas terjemahan dari bahasa sumber ke dalam bahasa Indonesia. Setiap dimensi dinilai pada skala 1--6 (band). Bobot setiap dimensi mencerminkan tingkat kepentingannya terhadap kualitas keseluruhan.

---

## Format Penilaian

Setiap dimensi diberi skor band 1--6 berdasarkan deskriptor di bawah ini. Skor akhir dihitung sebagai **rata-rata tertimbang** dari seluruh dimensi.

**Rumus:**

```
Skor Total = (NA × 30%) + (TK × 20%) + (SF × 25%) + (KF × 10%) + (KL × 10%) + (IO × 5%)
```

| Kode | Dimensi | Bobot |
|---|---|---|
| NA | Numerical Accuracy | 30% |
| TK | Terminology Consistency | 20% |
| SF | Semantic Fidelity | 25% |
| KF | Format Compliance | 10% |
| KL | Completeness | 10% |
| IO | Inference / OCR Quality | 5% |

### Konversi Skor ke Presentase

| Skor Total | Presentase Kualitas |
|---|---|
| 5,5 -- 6,0 | 91--100% (Sempurna) |
| 4,5 -- 5,4 | 76--90% (Baik) |
| 3,5 -- 4,4 | 61--75% (Cukup) |
| 2,5 -- 3,4 | 46--60% (Kurang) |
| 1,5 -- 2,4 | 31--45% (Buruk) |
| 1,0 -- 1,4 | 16--30% (Sangat Buruk) |

### Aturan Zero-Tolerance

Pelanggaran zero-tolerance berikut **secara otomatis** membatasi skor maksimum yang dapat dicapai:

1. **Kesalahan format desimal** (menggunakan titik sebagai pemisah desimal, misalnya `3.14` bukan `3,14`) → skor maksimum **60%** (band 4,0).
2. **Kesalahan format tanggal** (menggunakan MM/DD/YYYY alih-alih DD/MM/YYYY) → skor maksimum **60%** (band 4,0).
3. **Kesalahan register sapaan** (menggunakan "kamu" dalam dokumen formal atau "Anda" dalam dialog informal yang jelas) → skor maksimum **60%** (band 4,0).

**Catatan:**
- Pelanggaran zero-tolerance bersifat kumulatif. Dua pelanggaran berbeda menghasilkan pembatasan skor yang sama (tidak bertambah parah).
- Pelanggaran zero-tolerance yang sama yang terjadi berulang kali dianggap sebagai satu pelanggaran untuk aturan ini, tetapi dicatat sebagai pengulangan.
- Jika terjadi pelanggaran zero-tolerance, tim harus melakukan koreksi wajib sebelum dokumen dianggap selesai.

### Aturan Global: Kesalahan Kritis

Kesalahan kritis adalah kesalahan yang mengubah makna secara fundamental atau menghasilkan informasi yang salah. Contoh:

- Angka yang salah (misalnya 1.000 menjadi 100.000).
- Nama yang salah eja sehingga mengubah identitas.
- Tanggal yang salah sehingga mengubah kronologi.
- Istilah yang salah sehingga mengubah instruksi/prosedur.

**Jika terdapat satu atau lebih kesalahan kritis, skor maksimum yang dapat dicapai adalah 60% (band 4,0),** berapa pun skor pada dimensi lain.

---

## Dimensi 1: Numerical Accuracy (NA) — Bobot 30%

*Akurasi numerik: angka, mata uang, tanggal, persentase, dan data kuantitatif lainnya.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Semua angka, mata uang, tanggal, persentase, dan data kuantitatif diterjemahkan dengan tepat tanpa satu pun kesalahan. Format angka (desimal koma, ribuan titik) diterapkan secara konsisten dan benar. Tidak ada kesalahan konversi satuan. |
| 5 | 83% | Hampir semua akurat. Mungkin terdapat 1--2 kesalahan minor pada angka yang tidak mengubah makna (misalnya format ribuan tidak konsisten untuk angka kecil). Tidak ada kesalahan pada tanggal, mata uang, atau persentase. |
| 4 | 67% | Sebagian besar akurat dengan 3--5 kesalahan minor. Mungkin ada satu kesalahan pada konversi satuan atau format yang tidak konsisten. Tidak ada kesalahan yang mengubah data secara signifikan. |
| 3 | 50% | Terdapat lebih dari 5 kesalahan numerik. Beberapa angka mungkin salah format atau salah konversi, tetapi belum mengubah makna keseluruhan secara fundamental. |
| 2 | 33% | Banyak kesalahan numerik (6--10). Terdapat kesalahan yang mengubah sebagian data. Format tidak konsisten di seluruh dokumen. |
| 1 | 17% | Kesalahan numerik sangat banyak (>10) atau terdapat kesalahan fatal pada data utama. Data kuantitatif tidak dapat diandalkan. |

**Sub-dimensi yang dinilai:**
- Angka bulat dan desimal
- Mata uang (simbol, posisi, kode ISO)
- Tanggal dan waktu (format DD/MM/YYYY, 24 jam)
- Persentase dan rasio
- Konversi satuan (jika relevan)
- Konsistensi format angka antar-bagian dokumen

---

## Dimensi 2: Terminology Consistency (TK) — Bobot 20%

*Konsistensi penggunaan istilah teknis dan kosakata khusus di seluruh dokumen.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Semua istilah diterjemahkan secara konsisten di seluruh dokumen. Penggunaan istilah sesuai dengan glosarium proyek atau standar industri. Tidak ada variasi yang membingungkan. Istilah baru diperkenalkan dengan definisi yang jelas. |
| 5 | 83% | Sangat konsisten. Mungkin terdapat 1--2 variasi istilah yang tidak mengganggu pemahaman. Glosarium diikuti dengan baik. |
| 4 | 67% | Cukup konsisten. Terdapat 3--5 inkonsistensi istilah, tetapi masih dapat dipahami dalam konteks. Beberapa istilah mungkin tidak konsisten dengan glosarium. |
| 3 | 50% | Kurang konsisten. Banyak istilah yang diterjemahkan secara berbeda di bagian berbeda dokumen. Membingungkan pembaca. Glosarium tidak diikuti secara memadai. |
| 2 | 33% | Tidak konsisten secara signifikan. Istilah kunci diterjemahkan secara berbeda di berbagai bagian. Sulit diikuti. |
| 1 | 17% | Sangat tidak konsisten. Istilah berubah-ubah tanpa pola. Glosarium diabaikan. Terjemahan istilah tampak acak. |

**Sub-dimensi yang dinilai:**
- Konsistensi istilah teknis intra-dokumen
- Kesesuaian dengan glosarium proyek (jika ada)
- Konsistensi ejaan (EYD)
- Konsistensi istilah antar-dokumen dalam satu proyek
- Penggunaan padanan baku vs serapan asing

---

## Dimensi 3: Semantic Fidelity (SF) — Bobot 25%

*Kesesuaian makna antara teks sumber dan teks sasaran.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Makna, nuansa, dan tone teks sumber tersampaikan sepenuhnya. Tidak ada informasi yang bertambah, berkurang, atau berubah. Terjemahan terdengar alami dalam bahasa Indonesia tanpa mengorbankan ketepatan. |
| 5 | 83% | Makna utama tersampaikan dengan sangat baik. Mungkin ada sedikit kehilangan nuansa minor yang tidak mengubah substansi. Tidak ada distorsi makna. |
| 4 | 67% | Makna utama tersampaikan dengan baik, tetapi terdapat 1--2 bagian di mana makna kurang tepat atau sedikit meleset dari sumber. Tidak ada kesalahan fatal. |
| 3 | 50% | Terdapat beberapa bagian di mana makna tidak tersampaikan dengan benar (3--5 kesalahan semantik). Beberapa kalimat mungkin ambigu atau berbeda dari sumber. |
| 2 | 33% | Banyak kesalahan semantik. Makna beberapa paragraf menyimpang dari sumber. Pembaca akan mendapatkan informasi yang berbeda secara signifikan. |
| 1 | 17% | Terjemahan tidak dapat diandalkan. Makna sangat berbeda dari sumber di banyak bagian. Terjemahan tampak asal-asalan atau menggunakan mesin tanpa diedit. |

**Sub-dimensi yang dinilai:**
- Ketepatan makna leksikal (kata per kata)
- Ketepatan makna frasa dan idiom
- Ketepatan tone dan register
- Kealamian bahasa Indonesia
- Penanganan ambiguitas
- Adaptasi budaya yang tepat

---

## Dimensi 4: Format Compliance (KF) — Bobot 10%

*Kesesuaian format, tata letak, dan gaya dengan dokumen sumber dan pedoman.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Format dokumen identik dengan sumber. Heading, daftar, tabel, spasi, font, dan elemen visual dipertahankan sempurna. Markup terstruktur dengan benar. |
| 5 | 83% | Format sangat baik. Mungkin ada 1--2 perbedaan minor dalam tata letak yang tidak mengganggu. Heading dan daftar konsisten. |
| 4 | 67% | Format cukup baik. Terdapat 3--5 ketidaksesuaian format (misalnya heading level salah, daftar tidak rapi, tabel sedikit berbeda). Masih dapat digunakan. |
| 3 | 50% | Format kurang baik. Beberapa elemen format tidak sesuai (heading, tabel, spasi). Dokumen terlihat tidak rapi. |
| 2 | 33% | Format buruk. Banyak elemen format yang hilang atau salah. Heading tidak konsisten, tabel berantakan, daftar tidak terstruktur. |
| 1 | 17% | Format sangat buruk. Hampir tidak ada format yang dipertahankan. Dokumen tidak dapat digunakan tanpa perbaikan format besar-besaran. |

**Sub-dimensi yang dinilai:**
- Heading dan subheading
- Daftar (numbered dan bulleted)
- Tabel (struktur, alignment)
- Paragraf dan spasi
- Nomor halaman
- Elemen visual (gambar, diagram)
- Markup dan tag pemformatan

---

## Dimensi 5: Completeness (KL) — Bobot 10%

*Kelengkapan terjemahan: semua segmen, bagian, dan elemen telah diterjemahkan.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Semua segmen, kalimat, paragraf, catatan kaki, header, footer, dan elemen lain telah diterjemahkan seluruhnya. Tidak ada yang terlewat. |
| 5 | 83% | Hampir lengkap. Mungkin ada 1--2 segmen kecil yang terlewat (misalnya satu catatan kaki atau keterangan gambar). Tidak mengganggu pemahaman. |
| 4 | 67% | Cukup lengkap. Terdapat 3--5 segmen yang tidak diterjemahkan, termasuk beberapa kalimat penting. Pembaca mungkin kehilangan sebagian informasi. |
| 3 | 50% | Kurang lengkap. Terdapat 6--10 segmen tidak diterjemahkan. Beberapa paragraf atau bagian penting hilang. |
| 2 | 33% | Tidak lengkap. Banyak bagian yang tidak diterjemahkan (>10 segmen). Dokumen tidak dapat digunakan tanpa pelengkapan signifikan. |
| 1 | 17% | Sangat tidak lengkap. Lebih dari 25% konten tidak diterjemahkan. Tidak memenuhi syarat sebagai terjemahan. |

**Sub-dimensi yang dinilai:**
- Seluruh teks utama
- Catatan kaki dan catatan akhir
- Header dan footer
- Keterangan tabel dan gambar
- Daftar isi dan indeks (jika ada)
- Lampiran dan suplemen
- Teks dalam elemen visual
- Tag `[dipulihkan: ...]` sudah ditangani (jika ada)

---

## Dimensi 6: Inference / OCR Quality (IO) — Bobot 5%

*Kualitas pemulihan teks dari artefak OCR dan kemampuan menerjemahkan teks yang tidak sempurna.*

| Band | Skor | Deskriptor |
|---|---|---|
| 6 | 100% | Semua teks hasil OCR dipulihkan dengan benar. Tidak ada teks yang dibiarkan tidak terbaca tanpa penanganan. Pemulihan dilakukan dengan tepat dan akurat. Format `[dipulihkan: ...]` digunakan secara konsisten dan tepat. |
| 5 | 83% | Pemulihan sangat baik. Mungkin ada 1--2 bagian di mana pemulihan kurang optimal, tetapi tidak mengubah makna. Penanganan teks rusak sangat baik. |
| 4 | 67% | Cukup baik. Terdapat 3--5 bagian yang pemulihannya kurang tepat atau tidak konsisten dalam penggunaan format. Beberapa teks rusak mungkin tidak ditandai. |
| 3 | 50% | Kurang baik. Beberapa teks hasil OCR tidak dipulihkan atau dipulihkan dengan salah. Format penandaan tidak konsisten. |
| 2 | 33% | Buruk. Banyak teks hasil OCR tidak tertangani. Pemulihan sering salah. Format `[dipulihkan: ...]` jarang digunakan. |
| 1 | 17% | Sangat buruk. Hampir tidak ada upaya pemulihan teks OCR. Teks rusak dibiarkan begitu saja atau diterjemahkan secara salah tanpa verifikasi. |

**Sub-dimensi yang dinilai:**
- Ketepatan pemulihan teks yang tidak terbaca
- Penggunaan format `[dipulihkan: ...]` yang tepat
- Penanganan teks yang sebagian rusak
- Verifikasi pemulihan dengan konteks
- Dokumentasi pemulihan untuk verifikasi akhir
- Ketepatan penerjemahan teks yang dipulihkan

---

## Panduan Penilaian Praktis

### Cara Menilai

1. **Baca dokumen terjemahan secara keseluruhan** untuk mendapatkan kesan umum.
2. **Periksa dimensi Numerical Accuracy (NA)** terlebih dahulu — ini memiliki bobot tertinggi dan kesalahan zero-tolerance termudah dideteksi.
3. **Bandingkan dengan sumber** untuk Semantic Fidelity dan Completeness.
4. **Periksa konsistensi istilah** menggunakan fitur cari.
5. **Periksa format** dengan membandingkan struktur dokumen sumber dan target.
6. **Periksa penanganan OCR** jika dokumen berasal dari pemindaian.
7. **Periksa pelanggaran zero-tolerance** — jika ada, batasi skor maksimum.

### Tabel Ringkasan Zero-Tolerance

| Pelanggaran | Batas Maksimum |
|---|---|
| Desimal menggunakan titik (mis. `3.14` bukan `3,14`) | 60% / band 4,0 |
| Tanggal menggunakan MM/DD/YYYY | 60% / band 4,0 |
| "Kamu" dalam dokumen formal / "Anda" dalam konteks informal jelas | 60% / band 4,0 |
| Kesalahan kritis (mengubah makna fundamental) | 60% / band 4,0 |

### Contoh Kasus

**Kasus A:** Terjemahan sempurna dalam semua dimensi, angka akurat, istilah konsisten.
- Skor: NA=6, TK=6, SF=6, KF=6, KL=6, IO=6
- Total: (6×30)+(6×20)+(6×25)+(6×10)+(6×10)+(6×5) / 100 = 600/100 = **6,0 (100%)**

**Kasus B:** Angka dan tanggal benar, beberapa inkonsistensi istilah minor, format cukup baik, makna baik.
- Skor: NA=6, TK=4, SF=5, KF=4, KL=6, IO=6
- Total: (6×30)+(4×20)+(5×25)+(4×10)+(6×10)+(6×5) / 100 = 505/100 = **5,05 (84%)**

**Kasus C:** Menggunakan titik sebagai pemisah desimal (zero-tolerance), istilah cukup, makna baik.
- Batas maksimum: 60% (band 4,0)
- Skor sebelum pembatasan: NA=3 (karena kesalahan format), TK=5, SF=5, KF=5, KL=5, IO=5
- Total sebelum batas: (3×30)+(5×20)+(5×25)+(5×10)+(5×10)+(5×5) / 100 = 440/100 = **4,4 (73%)**
- Karena zero-tolerance dilanggar, skor dibatasi menjadi **60% / 4,0**.
- Dokumen WAJIB diperbaiki.

**Kasus D:** Terdapat satu kesalahan kritis (angka 100.000 diterjemahkan menjadi 10.000).
- Batas maksimum: 60% (band 4,0)
- Skor sebelum pembatasan: NA=1 (kesalahan fatal), TK=6, SF=3, KF=6, KL=6, IO=6
- Total sebelum batas: (1×30)+(6×20)+(3×25)+(6×10)+(6×10)+(6×5) / 100 = 345/100 = **3,45 (58%)**
- Karena kesalahan kritis, skor dibatasi menjadi **60% / 4,0** (dalam kasus ini tidak berubah karena sudah di bawah 60%).
- Dokumen WAJIB diperbaiki.

---

## Catatan untuk Penilai

1. **Bersikap objektif.** Gunakan bukti dari teks, bukan perasaan.
2. **Berikan komentar spesifik** untuk setiap band yang diberikan, terutama jika band di bawah 4.
3. **Zero-tolerance bersifat mutlak.** Jika ragu apakah suatu format benar, periksa pedoman base.md.
4. **Kesalahan kritis harus dicatat** dengan kutipan langsung dari teks sumber dan terjemahan.
5. **Dokumen dengan skor < 70% (band < 4,0)** harus dikembalikan untuk revisi sebelum disetujui.
6. **Untuk dokumen dengan skor 4,0--4,4 (61--75%),** penilai dapat memutuskan apakah revisi diperlukan atau perbaikan minor sudah cukup.
7. **Simpan dokumentasi penilaian** untuk setiap proyek sebagai bagian dari rekam jejak mutu.

---

> Rubrik ini disusun berdasarkan praktik terbaik industri penerjemahan dan disesuaikan dengan kebutuhan spesifik proyek bahasa Indonesia. Pembaruan akan dilakukan secara berkala.
