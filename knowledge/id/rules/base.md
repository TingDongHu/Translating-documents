---
id: id/rules/base
type: rules
target_lang: id
name: Pedoman Dasar Terjemahan Bahasa Indonesia
description: Indonesian base translation rules
---

# Pedoman Dasar Terjemahan Bahasa Indonesia

> Dokumen ini merupakan acuan utama untuk seluruh proyek terjemahan ke dalam bahasa Indonesia. Setiap penerjemah dan pengulas wajib memahami dan menerapkan pedoman di bawah ini secara konsisten.

---

## 1. Format Angka (Number Format)

### 1.1. Desimal

- **Tanda desimal adalah koma (`,`), BUKAN titik (`.`).**
- Contoh: `3,14` (bukan `3.14`), `0,05` (bukan `0.05`), `2,71828`.
- Pengecualian: data mentah atau kutipan langsung dari sumber berbahasa asing yang explicitly mempertahankan format aslinya.

### 1.2. Ribuan

- **Pemisah ribuan adalah titik (`.`), BUKAN koma.**
- Contoh: `1.000` (seribu), `25.000.000` (dua puluh lima juta), `3.141.592`.
- Untuk angka empat digit (1000--9999), titik boleh digunakan: `1.000` atau `1000`.

### 1.3. Bilangan Negatif

- Tanda minus ditulis sebagai `−` (tanda minus Unicode U+2212) atau `-` (tanda hubung) secara konsisten.
- Contoh: `−5`, `-12,75`.

### 1.4. Persentase

- Ditulis dengan angka diikuti tanda `%` tanpa spasi.
- Contoh: `5%`, `12,5%`, `100%`.
- Dalam teks formal, dieja: *lima persen*, *dua belas koma lima persen*.

### 1.5. Bilangan dalam Teks

- Angka satu sampai sepuluh dieja (*satu*, *dua*, *tiga*... *sepuluh*) kecuali dalam konteks teknis/tabel.
- Angka sebelas ke atas ditulis dengan angka: `11`, `25`, `100`.
- Bilangan besar di awal kalimat tetap dieja meskipun >10, atau susun ulang kalimat.

### 1.6. Pecahan

- Ditulis dengan garis miring: `1/2`, `3/4`, atau dieja: *setengah*, *tiga perempat*.
- Desimal lebih diutamakan daripada pecahan dalam konteks data.

---

## 2. Mata Uang (Currency)

### 2.1. Rupiah

- **Simbol `Rp` ditempatkan di depan angka, tanpa spasi.**
- Contoh: `Rp100.000`, `Rp5.500`, `Rp1.000.000.000`.
- Nilai desimal: `Rp1.500,50`.

### 2.2. Mata Uang Asing — Simbol

- Dolar AS: `USD` atau `US$` (konsisten per dokumen).
- Contoh: `US$1.000`, `USD 100,00`.
- Euro: `€`, ditempatkan **setelah** angka dengan spasi: `100,00 €`, atau `EUR 100,00`.
- Yen: `JP¥` atau `JPY`, ditempatkan sebelum angka: `JP¥10.000`.

### 2.3. Kode ISO

- Gunakan kode ISO 4217 (IDR, USD, EUR, JPY, GBP, CNY) untuk konteks formal, tabel, atau ketika simbol tidak tersedia.
- IDR ditulis `IDR` bukan `Rp` dalam tabel keuangan internasional.
- Contoh: `IDR 150.000`, `USD 2.500`.

### 2.4. Format Campuran

- Jika dokumen sumber menyebut mata uang asing, pertahankan kode/simbol asal dan beri padanan IDR dalam kurung jika relevan.
- Contoh: *Biaya tersebut sebesar USD 2.500 (setara Rp40.000.000).*

---

## 3. Tanggal dan Waktu (Date and Time)

### 3.1. Format Tanggal

- **Format baku: DD/MM/YYYY**
- Contoh: `25/12/2024`, `01/01/2025`.
- **JANGAN gunakan format MM/DD/YYYY** (gaya Amerika).
- Format panjang: *25 Desember 2024* (tanpa "tanggal" di awal).

### 3.2. Nama Bulan

- Ditulis dalam bahasa Indonesia dengan huruf kapital di awal.
- Januari, Februari, Maret, April, Mei, Juni, Juli, Agustus, September, Oktober, November, Desember.
- Singkatan (tiga huruf, pakai titik): Jan., Feb., Mar., Apr., Mei, Jun., Jul., Agt., Sep., Okt., Nov., Des.
- *Mei* tidak disingkat.

### 3.3. Format Waktu

- **Format 24 jam**, gunakan titik sebagai pemisah jam dan menit.
- Contoh: `08.30` (bukan 8:30 AM), `13.45`, `23.59`.
- Tengah malam: `00.00` atau `24.00`.
- Detik: `08.30.15` (08:30:15).
- Zona waktu: `14.00 WIB`, `09.00 UTC+7`.

### 3.4. Hari

- Nama hari: Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu.
- Singkatan: Sen., Sel., Rab., Kam., Jum., Sab., Min.

### 3.5. Rentang Tanggal dan Waktu

- Gunakan tanda pisah (`--`) tanpa spasi: `12--15 Januari 2024`.
- Atau dengan preposisi: *dari tanggal 12 sampai 15 Januari 2024*.
- Rentang waktu: `08.00--12.00 WIB`.

### 3.6. Abad dan Dekade

- Abad ditulis dengan angka Romawi atau angka Arab secara konsisten: *abad XXI* atau *abad ke-21*.
- Dekade: *tahun 1990-an*, *dasawarsa 1990-an*.

---

## 4. Alamat (Addresses)

### 4.1. Struktur Baku Alamat Indonesia

Urutan penulisan alamat dari yang terkecil ke terbesar:

```none
Jl. [nama jalan] No. [nomor], RT [nomor] / RW [nomor]
Kelurahan [nama]
Kecamatan [nama]
Kota [nama]
Provinsi [nama]
Kode Pos [angka]
```

### 4.2. Singkatan Baku

| Istilah | Singkatan |
|---|---|
| Jalan | Jl. |
| Nomor | No. |
| Rukun Tetangga | RT |
| Rukun Warga | RW |
| Kelurahan | Kel. |
| Kecamatan | Kec. |
| Provinsi | Prov. |

### 4.3. Contoh Lengkap

```none
Jl. Merdeka No. 45, RT 002 / RW 005
Kel. Kebon Jeruk
Kec. Palmerah
Kota Jakarta Barat
Prov. Daerah Khusus Jakarta
Kode Pos 11530
```

### 4.4. Alamat dalam Paragraf

- Tulis dalam format run-in: *beralamat di Jl. Merdeka No. 45, RT 002/RW 005, Kel. Kebon Jeruk, Kec. Palmerah, Jakarta Barat 11530.*

### 4.5. Alamat Luar Negeri

- Pertahankan urutan alamat negara asal.
- Tambahkan nama negara dalam bahasa Indonesia di akhir.
- Contoh: *1600 Pennsylvania Ave NW, Washington, DC 20500, Amerika Serikat.*

### 4.6. Penulisan "Jalan" vs "Jl."

- Dalam teks formal, gunakan `Jl.` (disingkat).
- Dalam teks sangat formal atau dokumen hukum, boleh ditulis lengkap `Jalan`.
- Konsisten dalam satu dokumen.

---

## 5. Nama Diri dan Kata Serapan (Proper Nouns)

### 5.1. Nama Asing

- **Nama orang asing tetap dipertahankan dalam ejaan aslinya.**
- Contoh: *William Shakespeare* (bukan *William Sakespeare*), *Friedrich Nietzsche*.
- Kecuali untuk nama yang sudah memiliki bentuk lazim dalam bahasa Indonesia: *Yesus*, *Muhammad*, *Socrates*, *Plato*.

### 5.2. Nama Tokoh dan Publikasi

- Nama tokoh Indonesia/Tokoh asing yang sering muncul di media Indonesia: gunakan ejaan yang lazim di Indonesia.
- Nama perusahaan/organisasi: pertahankan ejaan asli. Contoh: *Microsoft*, *Google*, *World Health Organization*.
- Untuk organisasi dengan akronim terkenal, gunakan akronim dengan kepanjangan bahasa Indonesia pada penyebutan pertama: *World Health Organization (WHO)* atau *Organisasi Kesehatan Dunia (WHO)*.

### 5.3. Ejaan Yang Disempurnakan (EYD)

- Gunakan Pedoman Umum Ejaan Bahasa Indonesia (PUEBI/EYD) edisi terbaru.
- Contoh penerapan:
  - *aktivitas* (bukan *aktifitas*)
  - *analisis* (bukan *analysis*)
  - *kategori* (bukan *katagori*)
  - *objek* (bukan *obyek*)
  - *subjek* (bukan *subyek*)
  - *praktik* (bukan *praktek*)
  - *proyek* (bukan *project*)
  - *kualitas* (bukan *qualitas*)

### 5.4. Kata Serapan dari Bahasa Asing

- Ikuti pedoman pembentukan istilah: serap dengan penyesuaian ejaan.
- Akhiran *-tion* → *-si*: *information* → *informasi*, *evaluation* → *evaluasi*.
- Akhiran *-ic* → *-is*: *automatic* → *otomatis*, *economic* → *ekonomis*.
- Awalan *inter-* → *antar-*: *international* → *internasional* (tetap *inter-* jika sudah baku).
- Akhiran *-al* → *-al* (kadang dipertahankan): *national* → *nasional*, *structural* → *struktural*.

### 5.5. Bentuk Perusahaan

- Indonesia: PT (Perseroan Terbatas), CV (Commanditaire Vennootschap), PD (Perusahaan Daerah).
- Contoh: *PT Telekomunikasi Indonesia Tbk*, *CV Maju Jaya*.
- Asing: pertahankan bentuk asli: *Inc.*, *LLC*, *GmbH*, *Ltd.*, *Co.*, *Corp.*.

### 5.6. Nama Geografis

- Nama kota/provinsi dalam negeri: gunakan ejaan resmi.
- Nama negara: gunakan nama baku Indonesia: *Amerika Serikat* (bukan *United States*), *Jerman* (bukan *Germany*), *Tiongkok* (bukan *China*), *Britania Raya* (bukan *United Kingdom*).
- Nama kota dunia: *London*, *Paris*, *Tokyo*, *Beijing*, *New York* (tetap dalam ejaan asli).

### 5.7. Merek Dagang

- Pertahankan ejaan asli merek dagang.
- Contoh: *iPhone*, *Windows*, *Toyota*, *Starbucks*.
- Jangan menerjemahkan nama merek.

---

## 6. Tanda Baca (Punctuation)

### 6.1. Tanda Koma (,)

- Digunakan di antara unsur-unsur dalam suatu perincian.
- Contoh: *Saya membeli buku, pensil, dan penggaris.*
- Digunakan sebelum kata penghubung *tetapi*, *melainkan*, *sedangkan*.
- Digunakan untuk memisahkan anak kalimat dari induk kalimat jika anak kalimat mendahului induk kalimat.
- Contoh: *Karena hujan deras, acara dibatalkan.*
- **TIDAK digunakan sebelum klausa *bahwa***: *Saya tahu bahwa dia sudah datang.*

### 6.2. Tanda Titik Koma (;)

- Digunakan untuk memisahkan bagian-bagian kalimat yang setara.
- Digunakan sebagai pengganti kata penghubung untuk memisahkan kalimat setara dalam satu kalimat.
- Contoh: *Hari ini hujan; kami tetap berangkat.*

### 6.3. Tanda Titik (:)

- Digunakan pada akhir pernyataan lengkap yang diikuti perincian.
- Digunakan sesudah kata atau ungkapan yang memerlukan pemerian.
- Contoh: *Acara ini membutuhkan perlengkapan berikut: meja, kursi, dan panggung.*
- **Tidak digunakan** sebelum perincian yang merupakan pelengkap kalimat.

### 6.4. Tanda Titik (.)

- Digunakan pada akhir kalimat berita.
- Digunakan di belakang singkatan gelar, jabatan, sapaan: *Dr.*, *S.E.*, *S.H.*, *Ir.*, *Bpk.*, *Ibu.*.
- Digunakan pada singkatan nama orang: *A. S. Kurniawan*.
- TIDAK digunakan di belakang singkatan lambang kimia, satuan ukuran, takaran, timbangan, dan singkatan yang sudah lazim tanpa titik: *cm*, *kg*, *Rp*, *PT*.

### 6.5. Tanda Petik (" " dan ' ')

- **Tanda petik ganda** (" ") untuk kutipan langsung.
- Contoh: *Dia berkata, "Saya akan datang besok."*
- **Tanda petik tunggal** (' ') untuk kutipan di dalam kutipan.
- Contoh: *Dia bertanya, "Apa maksudmu 'segera'?"*
- Tanda petik digunakan untuk judul artikel, puisi, bab buku.
- Tanda petik BUKAN untuk penekanan (gunakan huruf miring atau cetak tebal).

### 6.6. Tanda Pisah (—)

- Tanda pisah panjang (em dash) digunakan untuk menyisipkan keterangan atau penjelasan.
- Contoh: *Kemerdekaan bangsa itu—menurut pendapat para ahli—harus diperjuangkan.*
- Jarang digunakan dalam teks populer; lebih sering digantikan koma atau kurung.
- Dalam rentang angka: gunakan tanda pisah pendek (en dash, `--`): *tahun 2020--2024*.

### 6.7. Tanda Kurung (( ))

- Untuk keterangan tambahan: *Pendaftaran dibuka (sampai 31 Januari).*
- Untuk singkatan: *Organisasi Kesehatan Dunia (WHO).*
- Dalam konteks OCR: `[dipulihkan: keterangan]` (lihat Bagian 10).

### 6.8. Tanda Hubung (-)

- Digunakan untuk kata ulang: *anak-anak*, *buku-buku*, *berjalan-jalan*.
- Digunakan untuk merangkai kata dengan awalan *ber-* dan kata berulang: *ber-main-main*.
- Digunakan untuk merangkai unsur bahasa Indonesia dengan unsur bahasa asing: *di-backup*, *di-launching* (sebaiknya dihindari; gunakan padanan: *dicadangkan*, *diluncurkan*).

### 6.9. Tanda Tanya (?) dan Seru (!)

- Tanda tanya di akhir kalimat tanya.
- Tanda seru untuk seruan atau perintah tegas.
- Jangan menumpuk: `??` atau `!!!` tidak sesuai kaidah formal.

### 6.10. Tanda Elipsis (...)

- Digunakan untuk menunjukkan bagian kalimat yang dihilangkan dalam kutipan.
- Tiga titik, dengan spasi sebelum dan sesudah: *... demikianlah laporan ini ...*
- Empat titik jika akhir kalimat dihilangkan (titik akhir termasuk).

---

## 7. Format dan Tata Letak (Formatting)

### 7.1. Judul dan Subjudul

- **Huruf kapital di awal setiap kata** (title case) untuk judul utama — *BUKAN* semua kapital.
- Contoh: *Pedoman Terjemahan Bahasa Indonesia* (bukan *PEDOMAN TERJEMAHAN BAHASA INDONESIA*).
- Subjudul: huruf kapital hanya di awal frasa (sentence case): *Aturan penulisan angka*.
- Konsisten dengan format heading dalam dokumen target.

### 7.2. Huruf Miring (Italic)

- Digunakan untuk kata atau istilah asing yang belum diserap: *foreign policy*, *software*, *background*.
- Digunakan untuk judul buku, film, album: *Laskar Pelangi*, *Tenggelamnya Kapal van der Wijck*.
- Digunakan untuk penekanan (dengan bijaksana).
- Jangan menggunakan tanda petik sebagai pengganti huruf miring.

### 7.3. Huruf Tebal (Bold)

- Digunakan untuk istilah atau konsep kunci pada kemunculan pertama: **subjek** adalah pelaku dalam kalimat.
- Digunakan untuk judul tabel dan gambar.
- Jangan berlebihan.

### 7.4. Daftar (Lists)

- **Daftar tidak berurutan:** gunakan tanda hubung (`-`) atau asterisk (`*`).
- **Daftar berurutan:** gunakan angka (`1.`, `2.`, `3.`) atau huruf (`a.`, `b.`).
- Setiap butir dimulai dengan huruf kapital jika merupakan kalimat lengkap.
- Akhiri setiap butir dengan titik jika kalimat lengkap; gunakan koma/tanpa tanda baca jika frasa.
- Konsisten: jangan mencampurbutir kalimat lengkap dan frasa dalam satu daftar.

### 7.5. Tabel

- Judul tabel diletakkan di atas tabel, rata kiri.
- Gunakan tabel sederhana; hindari penggabungan sel (merge) yang kompleks jika tidak perlu.
- Perataan: teks rata kiri, angka rata kanan, mata uang rata kanan.
- Header tabel menggunakan huruf kapital di awal.
- Konsistensi format angka dalam kolom (jumlah desimal sama).

### 7.6. Nomor Halaman

- Gunakan format sesuai dokumen target: *Halaman 1 dari 10*, atau cukup angka.
- Kata pengantar/daftar isi: gunakan angka Romawi kecil (i, ii, iii).
- Isi: gunakan angka Arab.

### 7.7. Spasi dan Paragraf

- Satu spasi setelah tanda titik (bukan dua).
- Paragraf baru menjorok (indentasi) atau diberi spasi antarbaris, konsisten.
- Dalam dokumen digital: spasi antarbaris 1,5 spasi.

---

## 8. Tata Bahasa (Grammar)

### 8.1. Struktur Kalimat (SVO)

- Bahasa Indonesia berpola **Subjek--Predikat--Objek** (SVO).
- Contoh: *Saya membaca buku.* (Subjek: Saya, Predikat: membaca, Objek: buku).
- Urutan ini harus dipertahankan dari bahasa sumber jika memungkinkan.
- Perhatikan bahwa bahasa Jerman/Belanda memiliki struktur kalimat yang berbeda (verba di posisi kedua); perlu penyesuaian dalam terjemahan.

### 8.2. Tidak Ada Konjugasi

- Bahasa Indonesia **tidak mengenal konjugasi verba** berdasarkan persona, jumlah, atau kala (tense).
- Waktu ditunjukkan oleh konteks atau kata keterangan: *sudah*, *akan*, *sedang*, *telah*.
- Contoh:
  - *Saya makan* (I eat / I ate / I have eaten — tergantung konteks).
  - *Saya sudah makan* (I have eaten).
  - *Saya akan makan* (I will eat).
  - *Saya sedang makan* (I am eating).
- **Jangan menerjemahkan tense secara harfiah** — gunakan keterangan waktu kontekstual.

### 8.3. Tidak Ada Kala (Tenses)

- Tidak ada perubahan bentuk verba untuk menunjukkan waktu.
- Gunakan kata bantu dan konteks:
  - Lampau: *sudah*, *telah*, *dulu*, *kemarin*, *pada tahun lalu*.
  - Kini: *sedang*, *kini*, *sekarang*, *saat ini*.
  - Akan datang: *akan*, *nanti*, *besok*, *mendatang*.

### 8.4. Prefiks (Awalan)

| Prefiks | Fungsi | Contoh |
|---|---|---|
| `me-/men-/meng-/meny-/mem-` | Verba aktif transitif | *menulis*, *membaca*, *mengirim*, *menyapu* |
| `ber-` | Verba intransitif / memiliki | *berlari*, *bermain*, *berbaju* |
| `di-` | Verba pasif | *ditulis*, *dibaca*, *dikirim* |
| `ter-` | Keadaan tak sengaja / paling | *tertulis*, *terjatuh*, *terbaik* |
| `pe-/pen-/pem-/peng-` | Nomina pelaku | *penulis*, *pembaca*, *pengirim* |
| `per-` | Verba kausatif / nomina | *perbesar*, *perbaiki*, *persatuan* |

### 8.5. Kata Ulang (Reduplikasi)

- Digunakan untuk membentuk jamak atau makna tertentu.
- Contoh: *buku-buku* (jamak), *berlari-lari* (berulang kali), *mata-mata* (spy, bukan mata yang banyak).
- Dalam konteks formal, untuk jamak juga bisa didiamkan tanpa reduplikasi jika konteks sudah jelas.
- Hindari reduplikasi berlebihan dalam teks formal.

### 8.6. Tidak Ada Gender Gramatikal

- Bahasa Indonesia **tidak mengenal gender gramatikal**.
- Kata ganti tunggal: *dia* (untuk laki-laki dan perempuan).
- Kata ganti jamak: *mereka*.
- *Dia perempuan* (she), *Dia laki-laki* (he).
- Untuk penekanan gender: *ia* (netral), *beliau* (hormat), *ia perempuan* jika perlu diperjelas.
- **Jangan menerjemahkan he/she menjadi "dia" secara berulang** tanpa konteks yang jelas.

### 8.7. Kata Depan

- *di* (tempat): *di rumah*, *di Jakarta*, *di dalam*.
- *ke* (tujuan): *ke pasar*, *ke luar negeri*.
- *dari* (asal): *dari Bandung*, *dari pagi*.
- *di-* sebagai awalan (pasif) ditulis serangkai: *ditulis*, *dibuat*.
- *di* sebagai kata depan (tempat) ditulis terpisah: *di sini*, *di atas*.

### 8.8. Kata bilangan

- *Satu*, *dua*, *tiga*... + kata penggolong untuk benda: *sebuah buku*, *dua ekor kucing*, *tiga orang siswa*.
- Penggolong umum: *buah* (benda umum), *orang* (manusia), *ekor* (hewan), *batang* (benda panjang), *lembar* (kertas/dokumen), *butir* (benda kecil/bulat).

### 8.9. Kalimat Pasif

- Dua bentuk pasif:
  - *di-* + verba: *Buku itu dibaca oleh saya.* (formal)
  - Verba tanpa awalan dengan pelaku: *Buku itu saya baca.* (lebih alami untuk orang pertama).
- Dalam terjemahan, preferensi pasif *di-* lebih fleksibel; gunakan bentuk yang paling alami konteksnya.

---

## 9. Formalitas dan Sapaan (Formality)

### 9.1. "Anda" vs "Kamu"

- **Anda**: formal, sopan, untuk orang yang baru dikenal, atasan, klien, publik umum, dokumen resmi.
- **Kamu**: informal, akrab, untuk teman sebaya, orang yang lebih muda, suasana santai.
- **Kau-/-mu**: bentuk lebih akrab lagi, hindari dalam dokumen formal.
- **Dalam dokumen resmi/teknis, gunakan "Anda" secara konsisten.**
- Jangan mencampur penggunaan "Anda" dan "kamu" dalam satu dokumen.

### 9.2. Sapaan Formal

| Bentuk | Penggunaan |
|---|---|
| Yth. Bapak [nama] | Laki-laki, formal surat |
| Yth. Ibu [nama] | Perempuan, formal surat |
| Yth. Saudara/Saudari [nama] | Netral gender |
| Bapak/Ibu | Audiens umum, presentasi |
| Sdr. | Singkatan Saudara/Saudari |

### 9.3. Penutup Surat Formal

- *Hormat kami* (formal standar).
- *Demikian disampaikan, atas perhatiannya kami ucapkan terima kasih.* (sangat formal).
- *Salam hormat* (sedikit kurang formal).
- Hindari *Best Regards*, *Sincerely*, *Cheers* dalam surat berbahasa Indonesia.

### 9.4. Tingkat Tutur

- Bahasa Indonesia tidak memiliki tingkat tutur sebanyak bahasa Jawa atau Sunda, tetapi tetap ada nuansa formal/informal.
- **Formal (baku):** gunakan kata-kata baku, hindari singkatan tidak resmi, hindari partikel *-lah*, *-kah*, *-pun* secara berlebihan.
- **Semi-formal:** partikel bisa digunakan secukupnya untuk kealamian.
- **Informal:** hanya untuk dialog/percakapan dalam karya sastra atau konten khusus.

### 9.5. Kata Ganti Orang Ketiga Hormat

- *beliau*: untuk orang yang dihormati (guru, pejabat, tokoh).
- *-nya*: bentuk netral untuk kepemilikan (bukunya, rumahnya).
- Hindari penggunaan *ia* secara berlebihan; gunakan pengulangan nomina atau sinonimi jika perlu.

### 9.6. Imbauan dan Larangan

- **Larangan:** *Dilarang merokok*, *Tidak boleh masuk*.
- **Imbauan:** *Harap tenang*, *Mohon perhatikan*, *Silakan duduk*.
- **Formal:** *Dimohon untuk tidak...*, *Diharapkan agar...*.

---

## 10. Artefak OCR (OCR Artifacts)

### 10.1. Definisi

Artefak OCR adalah teks yang tidak dapat terbaca dengan jelas oleh perangkat lunak OCR (pengenalan karakter optis) dan memerlukan pemulihan manual oleh penerjemah atau pemeriksa.

### 10.2. Format Pemulihan

Gunakan format berikut untuk menandai teks yang dipulihkan:

```none
[dipulihkan: teks yang dipulihkan]
```

### 10.3. Contoh

| Sumber (OCR) | Hasil |
|---|---|
| Teks tidak terbaca | `[dipulihkan: paragraf ini rusak pada sumber]` |
| Karakter tidak jelas | `[dipulihkan: nama kota]` |
| Angka tidak terbaca | `[dipulihkan: 1.500]` |
| Kata hilang sebagian | `[dipulihkan: perusahaan]` |

### 10.4. Kapan Menggunakan

- Gunakan ketika teks sumber memang tidak terbaca dan tidak dapat dipulihkan dengan pasti.
- Jika Anda yakin dengan pemulihan, jangan gunakan tag — langsung tulis teks yang benar.
- Jika ragu, gunakan tag dan konsultasikan dengan pengulas.
- Jangan gunakan tag untuk teks yang sengaja dihapus atau disensor (gunakan `[redacted]` atau `[disunting]`).

### 10.5. Teks Rusak Partial

Untuk teks yang sebagian rusak:

```none
Kalimat ini [dipulihkan: mengandung] kata yang [dipulihkan: tidak terbaca] oleh OCR.
```

### 10.6. Gambar dan Diagram

Jika OCR tidak dapat mengekstrak teks dari gambar, diagram, atau bagan:

```none
[Gambar: deskripsi singkat tentang diagram]
[dipulihkan: teks dalam gambar tidak dapat diekstrak]
```

### 10.7. Dokumentasi

- Catat semua penggunaan tag `[dipulihkan: ...]` dalam lembar terpisah untuk verifikasi akhir.
- Pemeriksa kualitas harus memverifikasi ketepatan pemulihan.

---

## 11. Filosofi Penerjemahan (Translation Philosophy)

### 11.1. Prinsip Dasar

1. **Kealamian** — Terjemahan harus terdengar alami dalam bahasa Indonesia, seolah-olah teks itu memang ditulis dalam bahasa Indonesia.
2. **Ketepatan** — Makna dan nuansa sumber tetap terjaga tanpa distorsi.
3. **Konsistensi** — Istilah, gaya, dan format konsisten di seluruh dokumen.
4. **Keterbacaan** — Prioritas pada kemudahan pembaca memahami teks.

### 11.2. Formal Baku (Register)

- **Gunakan ragam baku (formal) sebagai default.**
- Ragam baku berarti: tata bahasa sesuai PUEBI, kosakata standar, struktur kalimat lengkap.
- Ragam non-baku hanya digunakan jika teks sumber memang informal (misalnya dialog, media sosial, pidato santai) dan sudah disepakati dengan pengguna jasa.

### 11.3. Menghindari Pinjaman Berlebihan

- **Jangan gunakan kata Belanda/Inggris jika ada padanan baku Indonesia yang lazim.**
- Contoh penggantian:

| Hindari | Gunakan |
|---|---|
| *accuren* | *terjadi* |
| *available* | *tersedia* |
| *background* | *latar belakang* |
| *consultation* | *konsultasi* (sudah baku) |
| *due date* | *batas waktu* |
| *feedback* | *masukan* |
| *issue* | *masalah* (jika konteks masalah); *isu* (jika konteks topik hangat) |
| *meeting* | *rapat*, *pertemuan* |
| *overview* | *gambaran umum* |
| *progress* | *kemajuan* |
| *review* | *tinjauan* / *ulasan* |
| *update* | *pembaruan* |
| *value* | *nilai* |

- **Catatan:** Beberapa kata asing sudah diserap secara resmi dan baku dalam KBBI; kata-kata tersebut boleh digunakan: *konsultasi*, *evaluasi*, *informasi*, *sistem*, *metode*, *teknologi*.
- Juga hindari struktur kalimat yang meniru bahasa asing (misalnya kalimat pasif berlebihan alih-alih aktif).

### 11.4. Prinsip Penerjemahan: Isi vs Bentuk

- Prioritaskan **isi** (makna) daripada **bentuk** (struktur harfiah).
- Contoh:
  - Inggris: *It is raining cats and dogs.*
  - Harfiah: *Hujan kucing dan anjing.* (salah)
  - Alami: *Hujan deras sekali.* (benar)
  - Atau pertahankan idiom jika padanan ada: *Hujan deras* / *Hujan lebat*.

### 11.5. Idiom dan Peribahasa

- Cari padanan dalam bahasa Indonesia jika ada.
- Jika tidak ada padanan, jelaskan maknanya secara lugas.
- Contoh:
  - *The ball is in your court.* → *Keputusan ada di tangan Anda.*
  - *Break the ice.* → *Mencairkan suasana.*
  - *A piece of cake.* → *Sangat mudah* / *Anak-anak juga bisa.*

### 11.6. Istilah Teknis

- Istilah teknis yang sudah memiliki padanan resmi di KBBI/Pusat Bahasa: **wajib** menggunakan padanan tersebut.
- Istilah teknis tanpa padanan resmi: pertahankan istilah asli dengan huruf miring, beri penjelasan pada kemunculan pertama.
- Contoh: *software* → *perangkat lunak*; *hardware* → *perangkat keras*; *firewall* → *firewall* (miring, belum ada padanan baku).

### 11.7. Penanganan Ambiguitas

- Jika kalimat sumber ambigu, pilih interpretasi yang paling masuk akal dalam konteks dan beri catatan kaki.
- Jangan menerjemahkan ambiguitas dengan kalimat yang juga ambigu dalam bahasa Indonesia jika bisa dihindari.

### 11.8. Adaptasi Budaya

- Contoh, satuan: konversi *feet* → *meter*, *miles* → *kilometer*, *Fahrenheit* → *Celsius*, jika konteks tidak memerlukan satuan asli.
- Mata uang: pertimbangkan apakah perlu dikonversi ke IDR atau dipertahankan dengan kode ISO (lihat Bagian 2).
- Tanggal: **selalu** konversi dari format sumber ke DD/MM/YYYY.

### 11.9. Kutipan Langsung

- Kutipan dari sumber berbahasa Indonesia: pertahankan apa adanya.
- Kutipan dari sumber berbahasa asing: **terjemahkan** ke bahasa Indonesia, kecuali:
  - Kutipan tersebut adalah istilah hukum/teknis yang bermakna spesifik dalam bahasa aslinya.
  - Kutipan puisi/sastra yang keindahannya hilang jika diterjemahkan.
  - Atas permintaan pengguna jasa.

### 11.10. Daftar Periksa Akhir (Final Checklist)

Setiap dokumen terjemahan harus diperiksa terhadap hal-hal berikut:

- [ ] Format angka (desimal koma, ribuan titik)
- [ ] Format mata uang (Rp di depan, tanpa spasi)
- [ ] Format tanggal (DD/MM/YYYY)
- [ ] Format waktu (24 jam)
- [ ] Ejaan sesuai PUEBI/EYD
- [ ] Konsistensi istilah (sesuai glosarium jika ada)
- [ ] Formalitas (Anda/kamu konsisten)
- [ ] Tanda baca sesuai kaidah Indonesia
- [ ] Nama diri asing dipertahankan
- [ ] Pinjaman asing diminimalkan
- [ ] Semua segmen sudah diterjemahkan (tidak ada segmen terlewat)
- [ ] Tag `[dipulihkan: ...]` sudah diverifikasi
- [ ] Terjemahan terdengar alami dalam bahasa Indonesia

---

> **Dokumen ini bersifat living document. Pembaruan dan penyempurnaan akan dilakukan secara berkala berdasarkan masukan dari tim penerjemah dan pengulas.**
