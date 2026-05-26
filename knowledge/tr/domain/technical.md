---
id: tr/domain/technical
type: domain
target_lang: tr
name: Türkçe Teknik Belge Çeviri Alan Bilgisi
description: Turkish Technical domain terminology and translation rules
---

# Türkçe Teknik Belge Çeviri Alan Bilgisi

## Okuyucu Modeli (Reader Model)

### Hedef Okuyucu Profili
- **Birincil Okuyucu**: Türk mühendisler, teknik uzmanlar, Ar-Ge personeli, kalite kontrol sorumluları
- **İkincil Okuyucu**: TSE denetçileri, sanayi ve teknoloji bakanlığı uzmanları, akreditasyon kuruluşları
- **Üçüncül Okuyucu**: Teknik ürün satın alma komiteleri, proje yöneticileri, teknik tercümanlar

### Okuyucu Beklentileri
1. **Kesinlik ve Doğruluk**: Teknik terimlerde standart karşılıklar beklenir, yabancı terimlerin birebir çevirisinden kaçınılmalıdır
2. **TSE Uyumluluğu**: Türk Standardları Enstitüsü tarafından belirlenen terminolojiye sadakat beklenir
3. **Ölçü Birimleri**: Metrik sistem (SI) kullanımı, yaygın olmayan birimler dönüştürülmeli
4. **Pasif Yapı Kullanımı**: Türkçe teknik metinlerde edilgen yapı tercih edilir ("yapılır", "belirlenir", "ölçülür")
5. **Netlik ve Kısalık**: Gereksiz sıfatlardan kaçınılmalı, doğrudan anlatım benimsenmeli

### Okuyucu Beklenti Matrisi

| Beklenti | Önem Derecesi | Karşılanmazsa Sonuç |
|----------|--------------|---------------------|
| Terminoloji tutarlılığı | Kritik | Teknik yanlış anlaşılma, güvenlik riski |
| TSE standart referansları | Yüksek | Belgenin reddi, uyumsuzluk cezası |
| SI birim sistemi | Yüksek | Ölçüm hataları, üretim hatası |
| Edilgen yapı | Orta | Doğal olmayan metin, güven kaybı |
| Şekil ve tablo etiketleme | Orta | Referans karışıklığı |

---

## Karar Çerçevesi (Decision Framework)

### Tablo T1: Teknik Terim Çeviri Stratejileri

| Kaynak Terim Türü | Çeviri Stratejisi | Örnek Kaynak | Örnek Çeviri | İstisna |
|-------------------|-------------------|-------------|-------------|---------|
| Uluslararası standart terim | Aynen koru | ISO 9001 | ISO 9001 | TSE karşılığı varsa kullan |
| Mühendislik terimi | Yerleşik Türkçe karşılık | Torque | Tork | "Moment" ile karıştırma |
| Bileşik teknik terim | Açımlama + kısaltma | Heat transfer coefficient | Isı transfer katsayısı (h) | İlk geçişte açıkla |
| Patent terimi | Orijinal + açıklama | Claim 1 | Talep 1 (Claim 1) | Hukuki bağlamda koru |
| Jenerik marka adı | TSE karşılığı | PVC pipe | PVC boru | Tescilli markaysa koru |
| Yeni teknoloji terimi | İngilizce + Türkçe açıklama | Machine learning | Makine öğrenmesi (machine learning) | TDK karşılığını izle |
| Kimyasal terim | IUPAC + Türkçe | Sodium hydroxide | Sodyum hidroksit (NaOH) | Yaygın adı varsa parantezde ver |
| Elektrik/elektronik terim | TSE/TS EN standardı | Ground | Toprak (Şase) | Bağlama göre seç |
| Yazılım terimi | Türkçeleştirilmiş | User interface | Kullanıcı arayüzü | Yerleşik İngilizce terim korunabilir |
| Otomotiv terimi | TSE 303 standardı | Brake system | Fren sistemi | Fren mi frenaj mi? → Fren |

### Tablo T2: TSE Standartlarına Referans Stili

| Referans Türü | Yazım Kuralı | Örnek | Açıklama |
|--------------|-------------|-------|----------|
| TS (Türk Standardı) | TS + numara + yıl | TS 500/2000 | Betonarme yapılar standardı |
| TS EN | TS EN + numara + yıl | TS EN 206:2014 | Beton standardı |
| TS ISO | TS ISO + numara + yıl | TS ISO 14001:2015 | Çevre yönetimi |
| TS EN ISO | TS EN ISO + numara + yıl | TS EN ISO 9001:2015 | Kalite yönetimi |
| TSE K | TSE K + numara | TSE K 101 | Uygunluk belgesi |
| TSE Hizmet | TSE Hizmet + numara | TSE Hizmet Yeri 123 | Hizmet yeri yeterlilik |
| Kabul edilmiş standart | Orijinal kod korunur | ASTM E84 | TSE karşılığı yoksa kullan |
| Yürürlükten kalkan | Eski numara + yeni numara | TS 500 (yerini TS EN 206 almıştır) | Güncelleme notu ekle |

### Tablo T3: SI Birim Sistemi Dönüşüm ve Kullanım Kuralları

| Birim | Türkçe Kullanım | Dönüşüm | Uyarı |
|-------|----------------|---------|-------|
| mm (milimetre) | mm veya milimetre | 1 mm = 0.001 m | "mil" ile karıştırma |
| cm (santimetre) | cm veya santimetre | 1 cm = 0.01 m | Teknik çizimde mm tercih edilir |
| m (metre) | m veya metre | - | Parsaj ifadesinde korunur |
| km (kilometre) | km veya kilometre | 1 km = 1000 m | Yol uzunluklarında |
| kg (kilogram) | kg veya kilogram | - | "kilo" kullanımından kaçın |
| g (gram) | g veya gram | 1 kg = 1000 g | İlaç/kimya dozajında |
| t (ton) | t veya ton | 1 t = 1000 kg | Taşımacılık/yük |
| N (Newton) | N | 1 N = 1 kg·m/s² | Kuvvet birimi |
| Pa (Paskal) | Pa veya Pascal | 1 Pa = 1 N/m² | Basınç birimi, bar=10⁵ Pa |
| MPa | MPa | 1 MPa = 10⁶ Pa | Yapı/çelik dayanımı |
| °C (santigrat) | °C | T(K) = T(°C) + 273,15 | Kelvin tercih edilmez |
| kW (kilovat) | kW | 1 kW = 1000 W | Güç birimi |
| kWh | kWh | - | Enerji tüketimi |
| L (litre) | L veya litre | 1 L = 0,001 m³ | "lt" kullanımından kaçın |
| dev/dak | dev/dak veya rpm | - | "rpm" korunabilir |

### Tablo T4: Güvenlik Seviyesi ve Uyarı Etiketi Çevirisi

| Kaynak İfade | Türkçe Karşılık | Kullanım Bağlamı | Görsel/Format |
|-------------|-----------------|------------------|--------------|
| DANGER | TEHLİKE | Ölüm veya ciddi yaralanma riski | Kırmızı zemin, beyaz yazı |
| WARNING | UYARI | Olası ölüm veya ciddi yaralanma | Turuncu zemin, siyah yazı |
| CAUTION | DİKKAT | Küçük/orta yaralanma riski | Sarı zemin, siyah yazı |
| NOTICE | NOT | Mala zarar riski, ekipman uyarısı | Mavi zemin, beyaz yazı |
| IMPORTANT | ÖNEMLİ | Kritik bilgi | Kalın yazı tipi |
| NOTE | NOT | Ek bilgi, açıklama | Normal yazı tipi |
| HAZARDOUS | TEHLİKELİ | Kimyasal/fiziksel tehlike | Standart uyarı sembolü |
| FLAMMABLE | YANICI | Yangın riski | Alev sembolü |
| TOXIC | ZEHİRLİ / TOKSİK | Sağlık tehlikesi | Kafatası sembolü |
| CORROSIVE | AŞINDIRICI / KOROZİF | Kimyasal yanık riski | Aşındırma sembolü |
| EXPLOSIVE | PATLAYICI | Patlama riski | Patlama sembolü |
| HOT SURFACE | SICAK YÜZEY | Yanma riski | Sıcak yüzey sembolü |
| ELECTRICAL SHOCK | ELEKTRİK ÇARPMASI | Elektrik tehlikesi | Şimşek sembolü |
| WEAR PPE | KKD GİYİN | Kişisel koruyucu donanım zorunluluğu | Koruyucu ekipman sembolü |

### Tablo T5: Teknik Doküman Bölümleri Çeviri Sözlüğü

| İngilizce | Türkçe | Alternatif Kullanım | Açıklama |
|-----------|--------|---------------------|----------|
| Abstract | Öz | Kısa özet | Bilimsel yayınlarda |
| Introduction | Giriş | - | Bölüm 1 |
| Scope | Kapsam | Uygulama alanı | Standardın/ürünün kapsamı |
| Normative References | Atıf Yapılan Standartlar | Normatif referanslar | Standart belgelerde |
| Terms and Definitions | Terimler ve Tanımlar | - | Sözlük bölümü |
| Specifications | Özellikler | Teknik özellikler | Performans kriterleri |
| Requirements | Gereklilikler | Şartlar | Zorunlu koşullar |
| Test Method | Deney Yöntemi | Test metodu | Laboratuvar prosedürü |
| Apparatus | Deney Düzeneği | Cihazlar | Kullanılan ekipman |
| Procedure | Yöntem | İşlem basamakları | Adım adım talimat |
| Calculation | Hesaplama | - | Formül ve hesaplamalar |
| Results | Sonuçlar | Test sonuçları | Veri ve bulgular |
| Annex | Ek | - | Zorunlu ekler |
| Appendix | Ek | İlave | Bilgi amaçlı ekler |
| Bibliography | Kaynakça | Referanslar | - |

### Tablo T6: Yaygın Teknik Kısaltmalar ve Türkçe Karşılıkları

| Kısaltma | Açılım | Türkçe Kullanım | Not |
|----------|--------|-----------------|-----|
| max. | maksimum | Maks. | Nokta ile kullanılır |
| min. | minimum | Min. | Nokta ile kullanılır |
| ort. | ortalama | Ort. | İstatistik |
| ref. | referans | Ref. | Dipnotlarda |
| yakl. | yaklaşık | Yakl. | Tahmini değerler |
| std. | standart | Std. | - |
| t. | ton | t | Birim olarak |
| dev. | devir | Dev. | Devir/dakika |
| mm | milimetre | mm | SI birim |
| °C | santigrat derece | °C | Sıcaklık |
| AC | Alternatif Akım | AA | Elektrik |
| DC | Doğru Akım | DA | Elektrik |
| kW | kilovat | kW | Güç |
| pH | pH | pH | Asitlik |
| RH | Bağıl Nem | BN | Nem ölçümü |
| KKD | Kişisel Koruyucu Donanım | KKD | İş güvenliği |

### Tablo T7: Teknik Çizim ve Şema Etiketleme Kuralları

| Öğe | Türkçe Etiket | Format Kuralı | Örnek |
|-----|--------------|--------------|-------|
| Şekil | Şekil | "Şekil X - Açıklama" | Şekil 1 - Kesit görünüşü |
| Tablo | Tablo | "Tablo X: Açıklama" | Tablo 1: Mekanik özellikler |
| Çizim | Çizim | "Çizim X: Açıklama" | Çizim 1: Montaj şeması |
| Grafik | Grafik | "Grafik X - Açıklama" | Grafik 1 - Yük-deformasyon |
| Diyagram | Diyagram | "Diyagram X: Açıklama" | Diyagram 1: Akış şeması |
| Denklem | Denklem | "Denklem X" | Denklem 1: F = m × a |
| Fotoğraf | Fotoğraf | "Fotoğraf X - Açıklama" | Fotoğraf 1 - Test düzeneği |
| Kesit | Kesit | "X-X Kesiti" | A-A Kesiti |
| Görünüş | Görünüş | "X Görünüşü" | Ön görünüş, yan görünüş |
| Detay | Detay | "Detay X" | Detay A |
| Parça no | Parça No. | "Parça No. X" | Parça No. 1 |
| Ölçü | (sayısal) | mm cinsinden | 250 ± 0,5 |

### Tablo T8: Malzeme Adlandırma ve Çevirisi

| İngilizce | Türkçe | TS Standardı | Açıklama |
|-----------|--------|-------------|----------|
| Steel | Çelik | TS 2162 | Genel terim |
| Stainless steel | Paslanmaz çelik | TS EN 10088 | - |
| Carbon steel | Karbon çeliği | TS 2348 | Yapı çeliği |
| Alloy steel | Alaşımlı çelik | TS EN 10020 | - |
| Cast iron | Dökme demir | TS 520 | - |
| Aluminum | Alüminyum | TS EN 573 | - |
| Copper | Bakır | TS EN 1172 | - |
| Brass | Pirinç | TS EN 12163 | Bakır-çinko alaşımı |
| Bronze | Bronz | TS 409 | Bakır-kalay alaşımı |
| Titanium | Titanyum | TS EN 2002 | - |
| Polymer | Polimer | TS EN ISO 472 | Genel terim |
| Plastic | Plastik | - | Günlük kullanımda |
| Rubber | Kauçuk | TS 859 | Doğal/sentetik |
| Ceramic | Seramik | TS EN 14471 | - |
| Composite | Kompozit | TS EN 13706 | - |
| Concrete | Beton | TS EN 206 | Yapı malzemesi |
| Wood | Ahşap | TS 647 | - |

### Tablo T9: İş Sağlığı ve Güvenliği (İSG) Terimleri

| İngilizce | Türkçe | Mevzuat Referansı | Alternatif |
|-----------|--------|-------------------|------------|
| Occupational safety | İş sağlığı ve güvenliği (İSG) | 6331 sayılı Kanun | - |
| Risk assessment | Risk değerlendirmesi | Yönetmelik | - |
| Hazard | Tehlike | - | Risk ile karıştırma |
| Personal protective equipment | Kişisel koruyucu donanım (KKD) | Yönetmelik | - |
| Emergency exit | Acil çıkış | Binaların Yangından Korunması | - |
| Fire extinguisher | Yangın söndürücü | Yönetmelik | - |
| First aid | İlk yardım | Yönetmelik | - |
| Occupational accident | İş kazası | 6331 sayılı Kanun | - |
| Occupational disease | Meslek hastalığı | 5510 sayılı Kanun | - |
| Safety sign | Güvenlik işareti | Yönetmelik | TS EN ISO 7010 |
| Warning sign | Uyarı işareti | Yönetmelik | - |
| Prohibition sign | Yasak işareti | Yönetmelik | - |
| Mandatory sign | Zorunluluk işareti | Yönetmelik | - |
| Emergency sign | Acil durum işareti | Yönetmelik | - |
| Work permit | İş izni | - | riskli işlerde |

### Tablo T10: Ölçü ve Tolerans İfadeleri

| İfade | Türkçe | Kısaltma | Kullanım |
|-------|--------|----------|----------|
| Tolerance | Tolerans | Tol. | ± değer |
| Deviation | Sapma | - | Nominalden fark |
| Upper deviation | Üst sapma | Εs/ES | Delik/mil |
| Lower deviation | Alt sapma | Ei/EI | Delik/mil |
| Fit | Geçme | - | Sıkı, geçiş, gevşek |
| Clearance | Boşluk | - | Hareketli geçme |
| Interference | Sıkılık | - | Sıkı geçme |
| Allowance | Alıkonma | - | Amaçlı fark |
| Nominal dimension | Nominal ölçü | - | Teorik ölçü |
| Actual dimension | Gerçek ölçü | - | Ölçülen değer |
| Limit dimensions | Limit ölçüler | - | Maks/min |
| Roughness | Pürüzlülük | Ra | Yüzey kalitesi |
| Flatness | Düzlük | - | Geometrik tolerans |
| Parallelism | Paralellik | // | Geometrik tolerans |
| Perpendicularity | Diklik | ⊥ | Geometrik tolerans |
| Concentricity | Eşmerkezlilik | ◎ | Geometrik tolerans |

### Tablo T11: Kalite Kontrol ve Test Terimleri

| İngilizce | Türkçe | Açıklama | Standart |
|-----------|--------|----------|----------|
| Quality control | Kalite kontrol (KK) | Süreç kontrolü | TS EN ISO 9001 |
| Quality assurance | Kalite güvencesi | Sistem güvencesi | TS EN ISO 9001 |
| Inspection | Muayene | Gözle/yöntemle kontrol | TS EN ISO 2859 |
| Testing | Test / Deney | Ölçüm ve test | - |
| Non-destructive testing | Tahribatsız muayene (NDT) | Malzemeye zarar vermeyen | TS EN ISO 9712 |
| Destructive testing | Tahribatlı muayene | Örnek parça kullanılır | - |
| Sample | Numune | Test edilen parça | - |
| Lot | Parti | Üretim grubu | - |
| Batch | Parti | Üretim partisi | "Lot" ile eşdeğer |
| Defect | Kusur / Hata | Uygunsuzluk | - |
| Non-conformity | Uygunsuzluk | Standarda aykırılık | - |
| Corrective action | Düzeltici faaliyet | Sorun giderme | TS EN ISO 9001 |
| Preventive action | Önleyici faaliyet | Proaktif önlem | TS EN ISO 9001 |
| Calibration | Kalibrasyon | Cihaz ayarı/doğrulama | TS EN ISO 17025 |
| Verification | Doğrulama | Şartların sağlandığının teyidi | - |
| Validation | Geçerleme / Validasyon | Yöntem geçerliliği | - |
| Traceability | İzlenebilirlik | Belge/kayıt takibi | - |

### Tablo T12: Yazım ve Noktalama Kuralları (Teknik Metinlerde)

| Kural | Açıklama | Doğru Kullanım | Yanlış Kullanım |
|------|----------|---------------|-----------------|
| Ondalık ayracı | Türkçede virgül kullanılır | 3,14 mm | 3.14 mm |
| Binlik ayracı | Nokta veya boşluk | 1.250 veya 1 250 | 1,250 |
| Birim-ön ek arası | Boşluk bırakılmaz | 25mm | 25 mm |
| Sayı-birim | Boşluk bırakılır | 25 mm | 25mm (bazı kaynaklarda- Standarda göre değişir) |
| Kısaltma sonu | Nokta konur | Maks. | Maks |
| Tablo başlığı | Büyük harfle başlar | **Tablo 1:** Değerler | Tablo 1: değerler |
| Şekil başlığı | Büyük harfle başlar | **Şekil 1** - Montaj | Şekil 1 - montaj |
| Denklem numarası | Parantez içinde sağa yaslı | (1) | - |
| Birim sembolleri | Dik yazılır, büyük/küçük kuralı | N (Newton), mm | N, MM |
| Kısaltma açılımı | İlk geçişte parantez içinde | (TS EN ISO 9001) | - |
| Kimyasal formül | Alt indis doğru kullanılır | H₂O | H2O |
| Matematik işlem | × (çarpı), / (bölü) | 2 × 3 | 2x3 |

---

## Standartlar (Standards)

### TSE Standartları Referans Sistemi

1. **TS (Türk Standardı)**: Ulusal standart, ön ek TS
   - *Örnek*: TS 500 - Betonarme Yapıların Hesap ve Yapım Kuralları
   - *Örnek*: TS 181 - Emniyet Başlıkları

2. **TS EN (Avrupa Standardı)**: CEN/CENELEC'ten alınan standart
   - *Örnek*: TS EN 206 - Beton Özellikleri
   - *Örnek*: TS EN 10025 - Sıcak Haddelenmiş Yapı Çelikleri

3. **TS ISO (Uluslararası Standart)**: ISO'dan alınan standart
   - *Örnek*: TS ISO 14001 - Çevre Yönetim Sistemi

4. **TS EN ISO (Ortak Standart)**: ISO ve CEN ortak standardı
   - *Örnek*: TS EN ISO 9001 - Kalite Yönetim Sistemleri
   - *Örnek*: TS EN ISO 9712 - Tahribatsız Muayene Personel Sertifikasyonu

5. **TSE Uygunluk Belgesi**: TSE K markası
   - *Örnek*: TSE K 101 - Çimento

### Teknik Mevzuat Referansları

- **4703 sayılı Kanun**: Ürünlere İlişkin Teknik Mevzuatın Hazırlanması ve Uygulanması
- **CE İşareti**: AB uygunluk işareti, Türkiye'de de tanınır
- **ATEX**: Patlayıcı ortam ekipmanları (TS EN 60079 serisi)
- **Makine Emniyeti Yönetmeliği**: 2006/42/AT uyumlu (TS EN 12100)
- **Basınçlı Ekipmanlar Yönetmeliği (PED)**: TS EN 13445 serisi
- **Elektromanyetik Uyumluluk (EMC)**: TS EN 55011, TS EN 61000 serisi
- **Alçak Gerilim Direktifi (LVD)**: 2014/35/AB, TS EN 60335 serisi
- **Yapı Malzemeleri Yönetmeliği**: 305/2011/AB, TS EN 206, TS EN 771

### Teknik Çeviride Sık Yapılan Hatalar

1. **"Respectively" Çevirisi**: "Sırasıyla" olarak çevrilir, "saygıyla" değil.
   - *Yanlış*: A, B ve C saygıyla 1, 2 ve 3'tür.
   - *Doğru*: A, B ve C sırasıyla 1, 2 ve 3'tür.

2. **"Shall" Kullanımı**: Teknik metinlerde "zorunluluk" belirtir.
   - "The device shall be grounded" -> "Cihaz **topraklanmalıdır**" veya "Cihazın topraklanması **zorunludur**"
   - *Yanlış*: Cihaz topraklanacak (yetersiz)

3. **"May" / "Should" Ayrımı**:
   - May = -ebilir (izin): "Cihaz isteğe bağlı olarak kalibre edilebilir"
   - Should = -malıdır (tavsiye): "Cihaz düzenli olarak kalibre edilmelidir"

4. **"Check" vs "Verify" vs "Ensure"**:
   - Check = Kontrol edin (gözlem)
   - Verify = Doğrulayın (belgeli teyit)
   - Ensure = Sağlayın (garanti)

5. **Ön Eklerin Yazımı**:
   - "ön-ısıtma" değil, "ön ısıtma" (Türkçede ayrı yazılır)
   - "ön yükleme", "ön germe", "art işlem"

6. **Birim Boşluğu**:
   - Sayı ile birim arasında boşluk: 25 °C, 10 mm, 5 kg
   - Yüzde: %25 (boşluksuz), 25% (boşluksuz)

### Teknik Rapor Yazım Şablonu (Türkçe)

1. **Kapak Sayfası**: Proje/ürün adı, belge no, revizyon, tarih
2. **İçindekiler**: Bölüm ve alt bölümler
3. **Giriş ve Kapsam**: Belgenin amacı
4. **Atıf Yapılan Standartlar ve/veya Mevzuat**: Normatif referanslar
5. **Terimler ve Tarifler**: Kullanılan teknik terimler
6. **Genel Şartlar**: Tasarım/malzeme/üretim şartları
7. **Deney Yöntemleri**: Test prosedürleri
8. **Hesaplamalar**: Mühendislik hesaplamaları
9. **Muayene ve Deney**: Kalite kontrol aşamaları
10. **Ambalajlama, Taşıma ve Depolama**: Lojistik hükümler
11. **Ekler**: Teknik çizimler, şemalar, hesaplar
12. **Revizyon Takip Tablosu**: Değişiklik kaydı
