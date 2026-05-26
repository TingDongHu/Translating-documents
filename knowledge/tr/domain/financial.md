---
id: tr/domain/financial
type: domain
target_lang: tr
name: Türkçe Finansal Belge Çeviri Alan Bilgisi
description: Turkish Financial domain terminology and translation rules
---

# Türkçe Finansal Belge Çeviri Alan Bilgisi

## Okuyucu Modeli (Reader Model)

### Hedef Okuyucu Profili
- **Birincil Okuyucu**: Türk mali müşavirler (SMMM), yeminli mali müşavirler (YMM), bağımsız denetçiler
- **İkincil Okuyucu**: Şirket finans müdürleri, hazine uzmanları, iç denetçiler, risk yöneticileri
- **Üçüncül Okuyucu**: KGK (Kamu Gözetimi Kurumu) denetçileri, BDDK uzmanları, SPK analistleri, bankalar

### Okuyucu Beklentileri
1. **TMS/TFRS Uyumu**: Türkiye Muhasebe Standartları (TMS) ve Türkiye Finansal Raporlama Standartları (TFRS) terminolojisi kullanılmalıdır
2. **Muhasebe Hesap Planı**: Tek Düzen Hesap Planı (TDHP) kodlarına sadık kalınmalıdır
3. **Mali Tablo Formatı**: Bilanço, gelir tablosu, nakit akış tablosu KGK formatında sunulmalıdır
4. **Vergi Mevzuatı Terimleri**: Vergi Usul Kanunu (VUK) ve Kurumlar Vergisi Kanunu (KVK) terimleri kullanılmalıdır
5. **Finansal Oran ve Göstergeler**: Türkiye'de yaygın kullanılan finansal oran terminolojisi

### Okuyucu Beklenti Matrisi

| Beklenti | Önem Derecesi | Karşılanmazsa Sonuç |
|----------|--------------|---------------------|
| TMS/TFRS terminoloji uyumu | Kritik | Denetim görüşü olumsuz, KGK cezası |
| Hesap planı kod doğruluğu | Yüksek | Mali tablo tutarsızlığı |
| Vergi mevzuatı terim doğruluğu | Yüksek | Vergi cezası, faiz |
| Para birimi formatı | Yüksek | Rapor reddi, değerleme hatası |
| KGK format standardı | Yüksek | Bağımsız denetimde sorun |

---

## Karar Çerçevesi (Decision Framework)

### Tablo F1: Temel Finansal Tablo Terimleri (Bilanço)

| İngilizce | Türkçe (TMS/TFRS) | VUK Karşılığı | Hesap Kodu (TDHP) |
|-----------|--------------------|---------------|-------------------|
| Balance sheet | Bilanço | Bilanço | - |
| Assets | Varlıklar | Aktif | 1 |
| Current assets | Dönen varlıklar | Dönen varlıklar | 10-18 |
| Cash and cash equivalents | Nakit ve nakit benzerleri | Kasa/Banka | 10 |
| Trade receivables | Ticari alacaklar | Alacaklar | 12 |
| Inventories | Stoklar | Stoklar | 15 |
| Prepaid expenses | Peşin ödenmiş giderler | Gelecek aylara ait giderler | 18 |
| Non-current assets | Duran varlıklar | Duran varlıklar | 22-29 |
| Property, plant and equipment | Maddi duran varlıklar | Demirbaşlar | 25 |
| Intangible assets | Maddi olmayan duran varlıklar | Haklar/Şerefiye | 26 |
| Liabilities | Kaynaklar | Pasif | 3 |
| Current liabilities | Kısa vadeli yükümlülükler | Kısa vadeli borçlar | 30-38 |
| Trade payables | Ticari borçlar | Satıcılar | 32 |
| Non-current liabilities | Uzun vadeli yükümlülükler | Uzun vadeli borçlar | 40-48 |
| Equity | Özkaynaklar | Öz sermaye | 5 |
| Share capital | Ödenmiş sermaye | Sermaye | 50 |
| Retained earnings | Geçmiş yıl kârları | Geçmiş yıl kârları | 57 |
| Reserves | Yedekler | Yedek akçeler | 54 |
| Net income/(loss) | Dönem net kârı/(zararı) | Dönem kârı/zararı | 59 |

### Tablo F2: Gelir Tablosu Terimleri

| İngilizce | Türkçe (TMS/TFRS) | Açıklama |
|-----------|--------------------|----------|
| Income statement | Gelir tablosu | Kâr/zarar tablosu |
| Revenue | Hasılat | Satış gelirleri |
| Cost of sales | Satışların maliyeti (-) | Direkt maliyet |
| Gross profit/(loss) | Brüt kâr/(zarar) | Hasılat - maliyet |
| Operating expenses | Faaliyet giderleri (-) | Pazarlama, genel yönetim, Ar-Ge |
| Selling expenses | Pazarlama, satış ve dağıtım giderleri | - |
| General and administrative expenses | Genel yönetim giderleri | İdari giderler |
| Research and development expenses | Araştırma ve geliştirme giderleri | Ar-Ge |
| Operating profit/(loss) | Faaliyet kârı/(zararı) | FVÖK (EBIT) |
| Other income and expenses | Diğer faaliyet gelir/giderleri | - |
| Finance income | Finansman gelirleri | Faiz, kur farkı geliri |
| Finance expense | Finansman giderleri (-) | Faiz, kur farkı gideri |
| Profit/(loss) before tax | Vergi öncesi kâr/(zarar) | - |
| Tax income/(expense) | Vergi geliri/(gideri) | Kurumlar vergisi + ertelenmiş vergi |
| Net profit/(loss) for the period | Dönem net kârı/(zararı) | - |
| Earnings per share | Hisse başına kazanç | EPS |
| EBITDA | FAVÖK | Faiz, amortisman, vergi öncesi kâr |
| EBIT | FVÖK | Faiz ve vergi öncesi kâr |

### Tablo F3: Nakit Akış Tablosu Terimleri

| İngilizce | Türkçe (TMS 7) | Açıklama |
|-----------|----------------|----------|
| Statement of cash flows | Nakit akış tablosu | TMS 7 kapsamı |
| Cash flows from operating activities | İşletme faaliyetlerinden nakit akışları | Esas faaliyet |
| Cash flows from investing activities | Yatırım faaliyetlerinden nakit akışları | MDV alım/satım |
| Cash flows from financing activities | Finansman faaliyetlerinden nakit akışları | Borçlanma/sermaye |
| Net increase/(decrease) in cash | Nakit ve nakit benzerlerinde net artış/(azalış) | - |
| Cash at beginning of period | Dönem başı nakit ve nakit benzerleri | - |
| Cash at end of period | Dönem sonu nakit ve nakit benzerleri | - |
| Depreciation and amortization | Amortisman ve itfa payları | Maddi/maddi olmayan |
| Changes in working capital | İşletme sermayesindeki değişim | Alacak/borç/stok değişimi |
| Capital expenditure | Sermaye harcamaları | MDV alımı (CAPEX) |
| Free cash flow | Serbest nakit akışı | FCF |
| Operating cash flow | İşletme nakit akışı | OCF |
| Dividend paid | Ödenen temettü | Kâr dağıtımı |

### Tablo F4: Finansal Oran ve Göstergeler

| İngilizce | Türkçe | Formül | Açıklama |
|-----------|--------|--------|----------|
| Current ratio | Cari oran | Dönen varlıklar / KVYK | Likidite ölçüsü |
| Quick ratio | Asit-test oranı | (Dönen varlıklar - Stoklar) / KVYK | Hızlı likidite |
| Cash ratio | Nakit oranı | (Nakit + Banka) / KVYK | En katı likidite |
| Leverage ratio | Kaldıraç oranı | Toplam borç / Toplam aktif | Borçluluk |
| Debt-to-equity ratio | Borç/Özkaynak oranı | Toplam borç / Özkaynak | Finansal yapı |
| Return on equity (ROE) | Özkaynak kârlılığı | Net kâr / Özkaynak | Kârlılık |
| Return on assets (ROA) | Aktif kârlılığı | Net kâr / Toplam aktif | Verimlilik |
| Net profit margin | Net kâr marjı | Net kâr / Hasılat | Kârlılık oranı |
| Gross profit margin | Brüt kâr marjı | Brüt kâr / Hasılat | Maliyet yönetimi |
| EBITDA margin | FAVÖK marjı | FAVÖK / Hasılat | Operasyonel kârlılık |
| Asset turnover | Aktif devir hızı | Hasılat / Toplam aktif | Verimlilik |
| Inventory turnover | Stok devir hızı | Maliyet / Ortalama stok | Stok yönetimi |
| Receivables turnover | Alacak devir hızı | Hasılat / Ortalama ticari alacak | Tahsilat |
| Days sales outstanding | Alacak tahsil süresi | 365 / Alacak devir hızı | Gün |
| Interest coverage ratio | Faiz karşılama oranı | FVÖK / Faiz giderleri | Borç ödeme |
| Dividend yield | Temettü verimi | Hisse başına temettü / Hisse fiyatı | Yatırım getirisi |
| Price-to-earnings (P/E) | Fiyat/kazanç (F/K) | Hisse fiyatı / HBK | Değerleme |
| Market-to-book ratio | Piyasa değeri/defter değeri | PD / DD | Değerleme |

### Tablo F5: TMS/TFRS Standartları Referans Tablosu

| Standart Kodu | İngilizce Adı | Türkçe Adı | Kapsam |
|--------------|---------------|------------|--------|
| TMS 1 | Presentation of Financial Statements | Finansal Tabloların Sunuluşu | Mali tablo yapısı |
| TMS 2 | Inventories | Stoklar | Stok değerleme |
| TMS 7 | Statement of Cash Flows | Nakit Akış Tablosu | Nakit akış raporlaması |
| TMS 8 | Accounting Policies | Muhasebe Politikaları | Değişiklik ve hatalar |
| TMS 12 | Income Taxes | Gelir Vergileri | Ertelenmiş vergi |
| TMS 16 | Property, Plant and Equipment | Maddi Duran Varlıklar | MDV muhasebesi |
| TMS 17 | Leases | Kiralama İşlemleri | (TMS 17 yerini TFRS 16'ya bırakmıştır) |
| TMS 19 | Employee Benefits | Çalışanlara Sağlanan Faydalar | Kıdem tazminatı |
| TMS 21 | Effects of Changes in Foreign Exchange Rates | Kur Değişiminin Etkileri | Kur farkları |
| TMS 23 | Borrowing Costs | Borçlanma Maliyetleri | Faiz aktifleştirme |
| TMS 24 | Related Party Disclosures | İlişkili Taraf Açıklamaları | Transfer fiyatlandırması |
| TMS 27 | Separate Financial Statements | Bireysel Finansal Tablolar | Bağlı ortaklık |
| TMS 28 | Investments in Associates | İştiraklerdeki Yatırımlar | Özkaynak yöntemi |
| TMS 32 | Financial Instruments: Presentation | Finansal Araçlar: Sunum | Borç/sermaye ayrımı |
| TMS 33 | Earnings per Share | Hisse Başına Kazanç | EPS hesaplaması |
| TMS 34 | Interim Financial Reporting | Ara Dönem Finansal Raporlama | - |
| TMS 36 | Impairment of Assets | Varlıklarda Değer Düşüklüğü | Değerleme |
| TMS 37 | Provisions, Contingent Liabilities | Karşılıklar, Koşullu Borçlar | - |
| TMS 38 | Intangible Assets | Maddi Olmayan Duran Varlıklar | - |
| TMS 40 | Investment Property | Yatırım Amaçlı Gayrimenkuller | - |
| TFRS 1 | First-time Adoption | TFRS'nin İlk Uygulaması | - |
| TFRS 3 | Business Combinations | İşletme Birleşmeleri | Şerefiye |
| TFRS 7 | Financial Instruments: Disclosures | Finansal Araçlar: Açıklamalar | - |
| TFRS 8 | Operating Segments | Faaliyet Bölümleri | - |
| TFRS 9 | Financial Instruments | Finansal Araçlar | Sınıflandırma/değerleme |
| TFRS 10 | Consolidated Financial Statements | Konsolide Finansal Tablolar | Kontrol |
| TFRS 15 | Revenue from Contracts with Customers | Müşteri Sözleşmelerinden Hasılat | 5 aşamalı model |
| TFRS 16 | Leases | Kiralamalar | Kullanım hakkı varlığı |

### Tablo F6: TRY Format ve Para Birimi Kullanım Kuralları

| Kural | Açıklama | Doğru | Yanlış |
|-------|----------|-------|--------|
| TL sembolü | ₺ veya TL | 1.250,50 TL | 1,250.50 TL |
| Kuruş | İki ondalık | 125,50 ₺ | 125.5 TL |
| Binlik ayraç | Nokta | 1.250.000 TL | 1,250,000 TL |
| Ondalık ayraç | Virgül | 999,99 TL | 999.99 TL |
| Sıfır kuruş | ,00 yazılmaz | 1.250 TL | 1.250,00 TL |
| Milyar/Milyon | Açık yazım | 5 milyar TL | 5.000.000.000 TL |
| Sembol-sayı arası | Boşluk | 100 ₺ | 100₺ |
| USD/TL gösterimi | Çapraz | 1 USD = 30,50 TL | 1 USD = 30.50 TL |
| Negatif tutar | Parantez veya (-) | (1.250 TL) veya -1.250 TL | -1.250TL |
| Metin içinde tutar | Yazı + rakam | yirmi beş bin TL (25.000 TL) | - |
| Çek/senet tutarı | Yazı ile | ***Yirmi Beş Bin TL*** | - |

### Tablo F7: Vergi Terimleri (VUK + KVK + GVK)

| İngilizce | Türkçe | Kanun | Açıklama |
|-----------|--------|-------|----------|
| Corporate income tax | Kurumlar vergisi | KVK m.1 | Kurum kazançları |
| Withholding tax | Stopaj / Tevkifat | GVK m.94 | Kaynakta kesinti |
| Value added tax (VAT) | Katma değer vergisi (KDV) | KDVK | Mal/hizmet vergisi |
| Special consumption tax | Özel tüketim vergisi (ÖTV) | ÖTVK | Lüks/zararlı ürün |
| Stamp tax | Damga vergisi | 488 sayılı Kanun | Belge vergisi |
| Customs duty | Gümrük vergisi | GK | İthalat vergisi |
| Property tax | Emlak vergisi | 1319 sayılı Kanun | Gayrimenkul |
| Municipal tax | Belediye vergisi | 2464 sayılı Kanun | İlan/reklam, eğlence |
| Motor vehicle tax | Motorlu taşıtlar vergisi (MTV) | 197 sayılı Kanun | Araç |
| Inheritance and gift tax | Veraset ve intikal vergisi | 7338 sayılı Kanun | Miras/hibe |
| Banking and insurance transactions tax | Banka ve sigorta muameleleri vergisi (BSMV) | 6802 sayılı Kanun | Finansal işlem |
| Income tax | Gelir vergisi | GVK | Gerçek kişi |
| Tax base | Matrah | - | Verginin hesaplandığı tutar |
| Tax rate | Vergi oranı | - | %X |
| Tax return | Vergi beyannamesi | - | Yıllık/geçici |
| Tax declaration | Beyanname | - | - |
| Tax assessment | Tarhiyat | VUK | Vergi belirleme |
| Tax penalty | Vergi cezası | VUK | Usulsüzlük/kaçakçılık |
| Tax inspection | Vergi incelemesi | VUK | Denetim |
| Tax amnesty | Vergi affı / Yapılandırma | - | Kanunla düzenlenir |
| Advance tax | Geçici vergi | KVK m.32 | 3 ayda bir |
| Minimum tax | Asgari kurumlar vergisi | KVK (2024 düzenlemesi) | - |

### Tablo F8: Vergi Beyanname Türleri

| İngilizce | Türkçe | Dönem | Verilme Süresi |
|-----------|--------|-------|----------------|
| Corporate tax return | Kurumlar vergisi beyannamesi | Yıllık | Nisan ayının son günü |
| Income tax return | Gelir vergisi beyannamesi | Yıllık | Mart ayının son günü |
| VAT return | KDV beyannamesi | Aylık | İzleyen ayın 26. günü |
| Withholding tax return | Muhtasar ve prim hizmet beyannamesi | Aylık | İzleyen ayın 26. günü |
| Stamp tax return | Damga vergisi beyannamesi | Aylık | İzleyen ayın 26. günü |
| Corporate provisional tax return | Geçici vergi beyannamesi | 3 aylık | İzleyen ayın 17. günü |
| VAT withholding declaration | KDV tevkifat beyannamesi | Aylık | İzleyen ayın 26. günü |
| Special consumption tax return | ÖTV beyannamesi | Aylık | İzleyen ayın 15. günü |
| Social security premium | SGK prim bildirgesi | Aylık | İzleyen ayın 26. günü |
| Declaration of withholding | Muhtasar beyanname | Aylık | İzleyen ayın 26. günü |
| Final tax return | Kesin mizan | Yıllık | Denetim amaçlı |

### Tablo F9: Denetim ve Bağımsız Denetim Terimleri

| İngilizce | Türkçe | Düzenleme | Açıklama |
|-----------|--------|-----------|----------|
| Audit | Denetim / Bağımsız denetim | 660 sayılı KHK | - |
| Auditor | Denetçi | KGK lisansı | - |
| External audit | Bağımsız denetim | - | Dış denetçi |
| Internal audit | İç denetim | - | Kurum içi |
| Statutory audit | Yasal denetim | TTK m.397 | Zorunlu |
| Audit report | Denetim raporu | - | - |
| Unqualified opinion | Olumlu görüş | - | Temiz rapor |
| Qualified opinion | Şartlı olumlu görüş | - | Sınırlı sorun |
| Adverse opinion | Olumsuz görüş | - | Önemli yanlışlık |
| Disclaimer of opinion | Görüş bildirmekten kaçınma | - | Yeterli kanıt yok |
| Audit committee | Denetim komitesi | - | - |
| Audit evidence | Denetim kanıtı | - | - |
| Materiality | Önemlilik | - | Eşik değer |
| Risk assessment | Risk değerlendirmesi | - | - |
| Control environment | Kontrol ortamı | - | - |
| Internal control | İç kontrol | - | - |
| Compliance audit | Uyum denetimi | - | Mevzuata uygunluk |
| Performance audit | Performans denetimi | - | Verimlilik |
| Financial audit | Finansal denetim | - | Mali tablo |
| Forensic audit | Adli denetim | - | Dolandırıcılık |
| Audit opinion | Denetim görüşü | - | Nihai karar |
| Key audit matters | Kilit denetim konuları | BDS 701 | Önemli alanlar |
| Going concern | İşletmenin sürekliliği | TMS 1 | Varsayım |

### Tablo F10: Bilanço Dışı Kalemler ve Dipnot Terimleri

| İngilizce | Türkçe | Açıklama |
|-----------|--------|----------|
| Off-balance sheet items | Bilanço dışı kalemler | - |
| Contingent liabilities | Koşullu borçlar (Şarta bağlı borçlar) | TMS 37 |
| Contingent assets | Koşullu varlıklar (Şarta bağlı varlıklar) | TMS 37 |
| Guarantees | Garantiler / Teminatlar | - |
| Letters of guarantee | Teminat mektupları | Banka dışı |
| Pledged assets | Rehinli varlıklar | - |
| Collateral | Teminat | - |
| Commitments | Taahhütler | Satın alma taahhütleri |
| Operating lease | Faaliyet kiralaması | TFRS 16 öncesi |
| Derivative instruments | Türev araçlar | Forward, swap, opsiyon |
| Offsetting | Mahsup / Netleştirme | - |
| Notes to the financial statements | Finansal tablo dipnotları | TMS 1 |
| Accounting policies | Muhasebe politikaları | TMS 8 |
| Significant judgments | Önemli muhakemeler | - |
| Fair value measurement | Gerçeğe uygun değer | TFRS 13 |
| Related party transactions | İlişkili taraf işlemleri | TMS 24 |
| Subsequent events | Bilanço sonrası olaylar | TMS 10 |
| Segment reporting | Bölüm raporlaması | TFRS 8 |
| Earnings per share | Hisse başına kazanç | TMS 33 |

### Tablo F11: Değerleme ve Amortisman Terimleri

| İngilizce | Türkçe | TMS/TFRS | VUK |
|-----------|--------|----------|-----|
| Cost | Maliyet bedeli | TMS 16 | VUK m.262 |
| Fair value | Gerçeğe uygun değer | TFRS 13 | - |
| Net realizable value | Net gerçekleşebilir değer | TMS 2 | - |
| Present value | Bugünkü değer | - | - |
| Residual value | Kalıntı değer | TMS 16 | - |
| Useful life | Faydalı ömür | TMS 16 | - |
| Depreciation | Amortisman (maddi) | TMS 16 | VUK m.313 |
| Amortization | İtfa payı (maddi olmayan) | TMS 38 | VUK m.313 |
| Impairment | Değer düşüklüğü | TMS 36 | - |
| Revaluation | Yeniden değerleme | TMS 16 | VUK geçici m. |
| Straight-line method | Normal amortisman | Doğrusal | VUK m.315 |
| Accelerated method | Azalan bakiyeler yöntemi | - | VUK m.315 (2 kat) |
| Units of production | Üretim miktarı yöntemi | - | - |
| Useful life table | Faydalı ömür tablosu | - | VUK 333 Sıra No.lu Tebliğ |
| Impairment test | Değer düşüklüğü testi | TMS 36 | - |
| Capitalization | Aktifleştirme | - | VUK m.163 |
| Cost model | Maliyet modeli | TMS 16 | VUK |
| Revaluation model | Yeniden değerleme modeli | TMS 16 | Seçimlik |

### Tablo F12: Finansal Piyasa ve Yatırım Terimleri

| İngilizce | Türkçe | Açıklama / Mevzuat |
|-----------|--------|--------------------|
| Stock exchange | Borsa | BİST (Borsa İstanbul) |
| Equity / Share | Hisse senedi / Pay | - |
| Bond | Tahvil | Kamu/özel sektör |
| Government bond | Devlet tahvili | Hazine borçlanması |
| Treasury bill | Hazine bonosu | Kısa vadeli |
| Eurobond | Eurobond | Yabancı para tahvil |
| Sukuk | Sukuk / Kira sertifikası | Faizsiz enstrüman |
| Mutual fund | Yatırım fonu | - |
| ETF | Borsa yatırım fonu (BYF) | - |
| Derivative | Türev ürün | Forward, futures, swap, opsiyon |
| Forward | Forward | Tezgah üstü türev |
| Swap | Swap | Faiz/döviz takası |
| Option | Opsiyon | Alım (call) / satım (put) |
| Futures | Futures | Borsada işlem gören |
| Margin | Teminat | Türev işlemlerde |
| Leverage | Kaldıraç | Borçla yatırım |
| IPO | Halka arz | İlk halka arz |
| Secondary public offering | İkincil halka arz | - |
| Dividend | Temettü / Kâr payı | - |
| Rights issue | Bedelli sermaye artırımı | - |
| Bonus issue | Bedelsiz sermaye artırımı | - |
| Buyback | Geri alım | Pay geri alımı |
| Market capitalization | Piyasa değeri | PD |
| Price ceiling | Tavan fiyat | %10 sınırı |
| Price floor | Taban fiyat | %10 sınırı |
| Index | Endeks | BİST 100, BİST 30 |
| Credit rating | Kredi notu | Derecelendirme |
| Portfolio | Portföy | - |
| Asset allocation | Varlık dağılımı | - |
| Risk management | Risk yönetimi | - |

### Tablo F13: Finansal Kısaltmalar

| Kısaltma | Açılım | Türkçe |
|----------|--------|--------|
| KGK | Kamu Gözetimi Kurumu | - |
| TMS | Türkiye Muhasebe Standardı | - |
| TFRS | Türkiye Finansal Raporlama Standardı | - |
| BDS | Bağımsız Denetim Standardı | - |
| KDV | Katma Değer Vergisi | - |
| ÖTV | Özel Tüketim Vergisi | - |
| KVK | Kurumlar Vergisi Kanunu | 5520 sayılı |
| GVK | Gelir Vergisi Kanunu | 193 sayılı |
| VUK | Vergi Usul Kanunu | 213 sayılı |
| TTK | Türk Ticaret Kanunu | 6102 sayılı |
| SPK | Sermaye Piyasası Kurulu | - |
| BDDK | Bankacılık Düzenleme ve Denetleme Kurumu | - |
| BİST | Borsa İstanbul | - |
| MKK | Merkezi Kayıt Kuruluşu | - |
| TAKBİS | Takasbank | - |
| TCMB | Türkiye Cumhuriyet Merkez Bankası | - |
| HMB | Hazine ve Maliye Bakanlığı | - |
| SMMM | Serbest Muhasebeci Mali Müşavir | - |
| YMM | Yeminli Mali Müşavir | - |
| FAVÖK | Faiz, Amortisman ve Vergi Öncesi Kâr | EBITDA |
| FVÖK | Faiz ve Vergi Öncesi Kâr | EBIT |
| PD | Piyasa Değeri | - |
| DD | Defter Değeri | - |
| HBK | Hisse Başına Kâr | EPS |
| TDHP | Tek Düzen Hesap Planı | - |
| KAP | Kamuyu Aydınlatma Platformu | - |
| EKA | Elektronik Kamu Aydınlatma | - |
| GK | Gümrük Kanunu | 4458 sayılı |

### Tablo F14: Finansal Tablo Çevirisinde Dikkat Edilmesi Gereken Hususlar

| Husus | Açıklama | Doğru | Yanlış |
|-------|----------|-------|--------|
| "Revenue" çevirisi | TMS 18/TFRS 15'e göre "hasılat" | Hasılat | Gelir (çok genel) |
| "Cost" çevirisi | TMS 2'ye göre "maliyet" | Satışların maliyeti | Satışların gideri |
| "Property" çevirisi | TMS 16: "Maddi duran varlık" | Maddi duran varlıklar | Mallar/mülkler |
| "Equity" çevirisi | TMS 1: "Özkaynak" | Özkaynak | Öz sermaye (VUK) |
| "Provision" çevirisi | TMS 37: "Karşılık" | Karşılık | Rezerv (farklı) |
| "Allowance" çevirisi | Değer düşüklüğü karşılığı | Şüpheli alacak karşılığı | - |
| "Goodwill" çevirisi | TFRS 3: "Şerefiye" | Şerefiye | İyi niyet (yanlış) |
| "Inventory" çevirisi | TMS 2: "Stok" | Stoklar | Envanter (genel) |
| "Trade receivables" | "Ticari alacaklar" | Ticari alacaklar | Müşteri alacakları (biraz genel) |
| "Payable" | Borç | Ticari borçlar | - |
| "Deferred tax" | "Ertelenmiş vergi" | Ertelenmiş vergi varlığı/yükümlülüğü | - |
| "Disclosure" | "Açıklama / Dipnot" | Dipnot açıklamaları | - |
| "Interim" | "Ara dönem" | Ara dönem finansal tablolar | - |
| "Consolidated" | "Konsolide" | Konsolide finansal tablolar | Birleşik (farklı) |
| "Impairment loss" | "Değer düşüklüğü zararı" | Değer düşüklüğü zararı | - |
| "Treasury shares" | "Kendi hisse senetleri" | Kendi pay senetleri | - |
| "Non-controlling interest" | "Kontrol gücü olmayan pay" | Kontrol gücü olmayan pay | Azınlık payı (eski) |

### Tablo F15: Bankacılık Düzenleme Terimleri (BDDK)

| İngilizce | Türkçe | Düzenleme |
|-----------|--------|-----------|
| Capital adequacy ratio | Sermaye yeterlilik oranı (SYR) | BDDK düzenlemesi |
| Tier 1 capital | Ana sermaye | Basel III / BDYK |
| Tier 2 capital | Katkı sermaye | Basel III / BDYK |
| Common equity tier 1 | Çekirdek ana sermaye (ÇAS) | Basel III |
| Risk-weighted assets | Riske ağırlıklı varlıklar (RAV) | - |
| Non-performing loan (NPL) | Takipteki alacak | BDDK |
| Loan loss provision | Kredi risk karşılığı | - |
| Liquidity coverage ratio | Likidite karşılama oranı (LKO) | Basel III |
| Net stable funding ratio | Net istikrarlı fonlama oranı (NSFR) | Basel III |
| Leverage ratio | Kaldıraç oranı | Basel III |
| Credit risk | Kredi riski | - |
| Operational risk | Operasyonel risk | - |
| Market risk | Piyasa riski | - |
| Interest rate risk | Faiz oranı riski | - |
| Foreign exchange risk | Kur riski | - |
| Stress test | Stres testi | BDDK |
| Loan-to-deposit ratio | Kredi/mevduat oranı | - |
| Net interest margin | Net faiz marjı | - |
| Asset-liability management | Aktif-pasif yönetimi | - |
| Provision | Karşılık | TMS 37 + BDDK düzenlemesi |
| Write-off | Zarar yazma / Silme | - |
| Restructuring | Yapılandırma | - |
| Maturity mismatch | Vade uyumsuzluğu | - |

---

## Standartlar (Standards)

### Finansal Raporlama Çerçevesi

**Türkiye'de Finansal Raporlama Standartları Hiyerarşisi**
1. **TFRS/TMS**: KGK tarafından yayımlanan, IASB ile tam uyumlu standartlar
2. **VUK**: Vergi Usul Kanunu, vergi matrahı belirlemede kullanılır
3. **BDDK Düzenlemeleri**: Bankalar için ek düzenlemeler
4. **SPK Tebliğleri**: Halka açık şirketler için ek düzenlemeler
5. **KGK Yayınları**: Kavramsal çerçeve, rehberler, ilke kararları

**Mali Tabloların Seti (TMS 1)**
1. Bilanço (Finansal durum tablosu)
2. Gelir tablosu (Kâr veya zarar tablosu)
3. Diğer kapsamlı gelir tablosu (Özkaynak değişim tablosu)
4. Nakit akış tablosu
5. Dipnotlar (Önemli muhasebe politikaları ve diğer açıklayıcı notlar)
6. Geriye dönük düzeltme varsa karşılaştırmalı dönem bilgileri

### Hesap Planı Sistemi (Tek Düzen Hesap Planı - TDHP)

**1. Dönen Varlıklar** (10-18)
- 100 KASA, 102 BANKALAR, 120 ALICILAR, 153 TİCARİ MALLAR

**2. Duran Varlıklar** (22-29)
- 250 ARAZİ VE ARSALAR, 252 BİNALAR, 253 TESİS MAKİNA VE CİHAZLAR, 254 TAŞITLAR, 255 DEMİRBAŞLAR

**3. Kısa Vadeli Yükümlülükler** (30-38)
- 320 SATICILAR, 360 ÖDENECEK VERGİ VE FONLAR

**4. Uzun Vadeli Yükümlülükler** (40-48)
- 400 BANKA KREDİLERİ (Uzun Vadeli)

**5. Özkaynaklar** (50-59)
- 500 SERMAYE, 540 YASAL YEDEKLER, 570 GEÇMİŞ YILLAR KÂRLARI, 590 DÖNEM NET KÂRI

**6-8. Gelir ve Gider Hesapları**
- 600 YURT İÇİ SATIŞLAR, 601 YURT DIŞI SATIŞLAR, 620 SATIŞLARIN MALİYETİ, 760 PAZARLAMA GİDERLERİ, 770 GENEL YÖNETİM GİDERLERİ

**9. Nazım Hesaplar**
- 950-951 TEMİNAT MEKTUPLARI, 990-991 GARANTİLER

### Önemli Vergi Oranları (2026 itibarıyla)

| Vergi Türü | Oran | Açıklama |
|------------|------|----------|
| Kurumlar vergisi | %25 | %30 da olabilir (geçici düzenleme kontrol) |
| Gelir vergisi dilimleri | %15 - %40 | Artan oranlı |
| KDV (genel) | %20 | 2024'te %18'den %20'ye yükseldi |
| KDV (indirimli) | %10 | Temel gıda vb. |
| KDV (çok düşük) | %1 | Konut, gazete vb. |
| Stopaj (kurum) | %15 | Temettü stopajı |
| Stopaj (kira) | %20 | Gayrimenkul sermaye iradı |
| Stopaj (maaş) | Artan oranlı | SGK primi + Gelir vergisi |
| Damga vergisi (sözleşme) | Binde 9,48 | 2024 oranı |
| Motorlu taşıtlar vergisi | Araç değerine göre | Yıllık |
| ÖTV (otomobil) | %45 - %220 | Motor hacmine göre |

### Finansal Çeviride Kritik Noktalar

1. **TFRS Terimlerinde Güncellik**: Standartlar güncellenebilir, güncel KGK/TMS yayınları kontrol edilmelidir
2. **VUK-TFRS Farkları**: VUK ve TFRS farklı değerleme esaslarına sahiptir, çeviride bağlama dikkat edilmelidir
3. **Para Birimi**: Raporlama para birimi (functional currency) ve sunum para birimi ayrımı yapılmalıdır
4. **Dipnot Numaralandırma**: TFRS dipnot numaralandırması KGK örnek formatına uygun olmalıdır
5. **Karşılaştırmalı Bilgiler**: TMS 1 gereği en az bir önceki dönem karşılaştırmalı verilmelidir
