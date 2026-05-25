# Arabic (ar) Translation Rules — قاعدة معايير الترجمة العربية

> Version 1.0 | Last updated: 2026-05-25
> Applies to: All Arabic (ar) document translations in the pipeline.
> These rules govern the transformation of source-language text into Modern Standard Arabic (الفصحى) for formal documentation. Dialectal variants (العامية) are prohibited unless explicitly requested.

---

## Table of Contents

1. [Number Format](#1-number-format-تنسيق-الأرقام)
2. [Currency](#2-currency-العملات)
3. [Date and Time](#3-date-and-time-التاريخ-والوقت)
4. [Addresses](#4-addresses-العناوين)
5. [Proper Nouns](#5-proper-nouns-الأسماء-العلم)
6. [Punctuation](#6-punctuation-علامات-الترقيم)
7. [Formatting](#7-formatting-التنسيق)
8. [Grammar](#8-grammar-القواعد)
9. [Formality](#9-formality-مستويات-اللغة)
10. [OCR Artifacts](#10-ocr-artifacts-مشكلات-التعرف-البصري)
11. [Translation Philosophy](#11-translation-philosophy-فلسفة-الترجمة)

---

## 1. Number Format (تنسيق الأرقام)

### 1.1 Digit Sets

Arabic uses **two distinct digit sets** depending on region. For translation, the choice must be consistent throughout a single document.

| Digit | Eastern Arabic (شرق عربي) — Mashreq | Western Arabic (غرب عربي) — Maghreb |
|-------|---------------------------------------|--------------------------------------|
| 0 | ٠ | 0 |
| 1 | ١ | 1 |
| 2 | ٢ | 2 |
| 3 | ٣ | 3 |
| 4 | ٤ | 4 |
| 5 | ٥ | 5 |
| 6 | ٦ | 6 |
| 7 | ٧ | 7 |
| 8 | ٨ | 8 |
| 9 | ٩ | 9 |

**Rule:** Choose one digit set per document. **Never mix Eastern and Western digits** in the same document. This is zero-tolerance.

- **Preferred for most formal MSA translations:** Eastern Arabic digits (٠–٩), especially when translating for audiences in the Arabian Peninsula, Iraq, the Levant, and Egypt.
- **Western digits (0–9)** are acceptable in technical documents, software UI strings, and when the source document uses Western digits consistently.

### 1.2 Decimal Separator

| Usage | Symbol | Unicode | Example |
|-------|--------|---------|---------|
| Standard Arabic decimal separator | ٫ | U+066B | ١٢٣٫٤٥ (123.45) |
| Western decimal separator (alternative) | . | U+002E | ١٢٣.٤٥ |
| **Wrong** — mixing separators | , | U+002C | ١٢٣,٤٥ (confusable with thousands) |

### 1.3 Thousands Separator

| Usage | Symbol | Unicode | Example |
|-------|--------|---------|---------|
| Arabic thousands separator | ٬ | U+066C | ١٬٢٣٤٬٥٦٧ |
| Thin space (recommended in modern docs) | (thin space) | U+2009 | ١ ٢٣٤ ٥٦٧ |
| Comma (Western) | , | U+002C | 1,234,567 (only with Western digits) |

### 1.4 Negative Numbers

- The minus sign is placed **before** the number: −١٢٣ or -١٢٣
- Prefer the proper minus sign − (U+2212) over the hyphen - (U+002D) for clarity.
- Parentheses for negatives are acceptable in finance: (١٢٣) = −١٢٣

### 1.5 Percentages

- The percent sign follows the number with a thin space: ٢٥ % or 25 %
- In Arabic text, the symbol % is placed **after** the number (same as Western).
- The Arabic word «في المئة» or «بالمئة» may be used instead of % in formal text.

### 1.6 Fractions

- Fractions use the same slash as Western: ½, ⅓, ¼ — but may also be written out: النصف، الثلث، الربع
- Mixed fractions: ١ ½ (one and a half)

### 1.7 Ordinal Numbers

| Masculine | Feminine | Meaning |
|-----------|----------|---------|
| الأول | الأولى | first |
| الثاني | الثانية | second |
| الثالث | الثالثة | third |
| الرابع | الرابعة | fourth |
| الخامس | الخامسة | fifth |

### 1.8 Number-Gender Agreement (Nuancing — التمييز)

In Arabic, numbers 3–10 take the **opposite gender** of the noun they count. Numbers 1–2 agree in gender. Numbers 11–99 have complex rules.

| Rule | Example | Translation |
|------|---------|-------------|
| 1–2: agree with noun | كتاب واحد / كتابان اثنان | one book / two books |
| 3–10: opposite gender | ثلاثة كتب (masc. noun) / ثلاث طالبات (fem. noun) | three books / three female students |
| 11–99: first part opposite, second part agrees | أحد عشر كتابًا | eleven books |
| 100+: noun stays singular genitive | مئة كتاب | one hundred books |

### 1.9 Examples (20+)

| Source | Correct AR | Wrong AR | Notes |
|--------|------------|----------|-------|
| 123.45 | ١٢٣٫٤٥ | 123.45 (mixed) | Use consistent digit set |
| 1,000,000 | ١٬٠٠٠٬٠٠٠ or ١ ٠٠٠ ٠٠٠ | 1000000 | Apply thousands separator |
| -5.5% | −٥٫٥٪ or -٥٫٥٪ | 5.5-% | Minus before number |
| 3rd edition | الطبعة الثالثة | الطبعة 3 | Ordinal, not cardinal |
| Page 42 | صفحة ٤٢ | الصفحة 42 | Consistent digits |
| Version 2.0 | الإصدار ٢٫٠ | الإصدار 2.0 | |
| 25% discount | خصم ٢٥٪ / خصم ٢٥ في المئة | خصم 25٪ (mixed) | |
| 99 bottles | ٩٩ زجاجة | ٩٩ زجاجات | Broken plural not needed after number |
| 0.5 mg | ٠٫٥ مغ | 0,5 مغ (wrong separator) | |
| 10th anniversary | الذكرى العاشرة | الذكرى 10 | Ordinal required |
| 7 days | ٧ أيام | ٧ يوم | Plural after 3–10 |
| 2 meters | متران | ٢ متر | Dual required for 2 |
| 100 years | ١٠٠ عام | ١٠٠ أعوام | Singular after 100+ |
| 12 months | ١٢ شهرًا | ١٢ أشهر | Singular after 11–99 |
| 3 women | ٣ نساء (or ثلاث نساء) | ٣ امرأة | Plural required |
| 1st quarter | الربع الأول | الأول ربع | Adjective follows noun |
| ≈ 50 | حوالي ٥٠ / قرابة ٥٠ | تقريبًا 50 (mixed) | |
| ≥ 18 | ≥ ١٨ / أكبر من أو يساوي ١٨ | => 18 | |
| +20°C | +٢٠°م / ٢٠ درجة مئوية | +20° | |
| 3:2 ratio | نسبة ٣:٢ | النسبة 3:2 (mixed) | |
| Half (0.5) | النصف / ٠٫٥ | ½ (acceptable but prefer decimal) | |

---

## 2. Currency (العملات)

### 2.1 Currency Symbol Placement

In Arabic, the currency symbol is typically placed **after** the amount, unlike English where it precedes.

| Currency | Arabic Symbol | ISO Code | Example |
|----------|---------------|----------|---------|
| Saudi Riyal | ﷼ or ر.س | SAR | ١٠٠ ﷼ or ١٠٠ ر.س |
| Egyptian Pound | ج.م or E£ | EGP | ٥٠ ج.م |
| US Dollar | $ | USD | ٢٥ $ |
| Euro | € | EUR | ٣٠ € |
| UK Pound | £ | GBP | ٢٠ £ |
| Kuwaiti Dinar | د.ك | KWD | ١٠ د.ك |
| UAE Dirham | د.إ | AED | ٥٠ د.إ |
| Qatari Riyal | ر.ق | QAR | ١٠٠ ر.ق |
| Jordanian Dinar | د.ا | JOD | ٢٠ د.ا |
| Iraqi Dinar | د.ع | IQD | ٢٥٠٠٠ د.ع |

### 2.2 ISO Code Usage

- ISO codes (SAR, USD, etc.) are written **after** the amount with a space: ١٠٠ USD
- Prefer native symbols (ر.س, ﷼, ج.م) in Arabic documents over ISO codes.
- Use ISO codes in tables for column consistency.
- Never translate ISO codes.

### 2.3 Subunit Names

| Currency | Main Unit | Subunit | Subunit Name |
|----------|-----------|---------|-------------|
| SAR | ريال | هللة (halala) | ١ ريال = ١٠٠ هللة |
| EGP | جنيه | قرش (piaster) | ١ جنيه = ١٠٠ قرش |
| USD | دولار | سنت (cent) | ١ دولار = ١٠٠ سنت |
| EUR | يورو | سنت (cent) | ١ يورو = ١٠٠ سنت |
| KWD | دينار | فلس (fils) | ١ دينار = ١٠٠٠ فلس |

### 2.4 Currency Translation Rules

- **Do not translate currency units**: "50 dollars" → ٥٠ دولارًا (not ٥٠ عملة خضراء or slang terms).
- Maintain the source currency — do not convert to local equivalent unless explicitly instructed.
- In financial documents, write the amount in words followed by digits in parentheses: `خمسون ألف ريال سعودي (٥٠٬٠٠٠ ﷼) فقط لا غير`.
- Use the expression «فقط لا غير» (only, no more) at the end of written-out amounts in legal documents.

### 2.5 Examples (10+)

| Source | Correct AR | Notes |
|--------|------------|-------|
| $100 | ١٠٠ دولار أمريكي or ١٠٠ $ | Symbol after number |
| SAR 50.75 | ٥٠٫٧٥ ﷼ or ٥٠ ر.س و٧٥ هللة | |
| EGP 1,200 | ١٬٢٠٠ ج.م | Thousands separator |
| €2.5 million | ٢٫٥ مليون يورو | Scale word before currency |
| GBP 99.99 | ٩٩٫٩٩ £ | |
| 10 KWD | ١٠ د.ك | |
| AED 500 | ٥٠٠ د.إ | |
| Price: $19.99 | السعر: ١٩٫٩٩ $ | |
| Budget: £5K | الميزانية: ٥٬٠٠٠ £ | Expand K to full number |
| 1 SAR = 0.27 USD | ١ ﷼ = ٠٫٢٧ USD | Space around = |

---

## 3. Date and Time (التاريخ والوقت)

### 3.1 Calendar Systems

Arabic documents use two calendar systems:

| Calendar | Abbreviation | Marker | Usage Context |
|----------|-------------|--------|---------------|
| Hijri (Islamic) | هـ | هجرية | Religious, Saudi government, Islamic history |
| Gregorian (Western) | م | ميلادية | International business, most Arab governments, science |

**Rules:**
- The calendar marker (هـ or م) follows the year: ١٤٤٦هـ, ٢٠٢٦م
- Both may appear together: ١٤٤٦هـ / ٢٠٢٦م
- The abbreviation before the year: ١٤٤٦ هـ (with a space)

### 3.2 Month Names

**Gregorian Months (الأشهر الميلادية):**

| # | Arabic Name (Standard) | Alternative |
|---|----------------------|-------------|
| 1 | يناير (Yanayir) | كانون الثاني (Levant) |
| 2 | فبراير (Fibrayir) | شباط (Levant) |
| 3 | مارس (Mars) | آذار (Levant) |
| 4 | أبريل (Abriil) | نيسان (Levant) |
| 5 | مايو (Mayu) | أيار (Levant) |
| 6 | يونيو (Yunyu) | حزيران (Levant) |
| 7 | يوليو (Yulyu) | تموز (Levant) |
| 8 | أغسطس (Aghustus) | آب (Levant) |
| 9 | سبتمبر (Sibtambar) | أيلول (Levant) |
| 10 | أكتوبر (Uktubar) | تشرين الأول (Levant) |
| 11 | نوفمبر (Nufambar) | تشرين الثاني (Levant) |
| 12 | ديسمبر (Disambar) | كانون الأول (Levant) |

**Hijri Months (الأشهر الهجرية):**

| # | Arabic Name | English |
|---|-------------|---------|
| 1 | محرم | Muharram |
| 2 | صفر | Safar |
| 3 | ربيع الأول | Rabi' al-Awwal |
| 4 | ربيع الآخر / ربيع الثاني | Rabi' al-Akhir / Rabi' al-Thani |
| 5 | جمادى الأولى | Jumada al-Ula |
| 6 | جمادى الآخرة | Jumada al-Akhirah |
| 7 | رجب | Rajab |
| 8 | شعبان | Sha'ban |
| 9 | رمضان | Ramadan |
| 10 | شوال | Shawwal |
| 11 | ذو القعدة | Dhu al-Qi'dah |
| 12 | ذو الحجة | Dhu al-Hijjah |

### 3.3 Date Formats

| Format | Example | Usage |
|--------|---------|-------|
| Day Month Year (Arabic order) | ١٥ يناير ٢٠٢٦م | Most common in MSA |
| DD/MM/YYYY | ١٥/٠١/٢٠٢٦ | Numeric dates |
| YYYY/MM/DD | ٢٠٢٦/٠١/١٥ | ISO standard, databases |
| Written out | الخامس عشر من يناير عام ٢٠٢٦ | Formal/legal |

**Order for Arabic addresses:** Day → Month → Year (same as UK format).

### 3.4 Days of the Week

| Arabic | English |
|--------|---------|
| الأحد | Sunday |
| الإثنين | Monday |
| الثلاثاء | Tuesday |
| الأربعاء | Wednesday |
| الخميس | Thursday |
| الجمعة | Friday |
| السبت | Saturday |

- The week starts on **Sunday** (الأحد) in most Arab countries.
- Friday (الجمعة) is the weekly holiday/rest day.

### 3.5 Time Formats

| Format | Example | Notes |
|--------|---------|-------|
| 24-hour (formal) | ١٤:٣٠ | Preferred in official/business documents |
| 12-hour (informal) | ٢:٣٠ مساءً | Common in everyday writing |
| Written out | الثانية والنصف مساءً | Formal text |

**Time markers:**
- صباحًا (AM, lit. "morningly")
- مساءً (PM, lit. "eveningly")
- ظهرًا (noon)
- منتصف الليل (midnight)
- منتصف النهار (midday)

### 3.6 Timestamp Formats

| Source | Correct AR |
|--------|------------|
| 2026-01-15 | ١٥ يناير ٢٠٢٦م or ٢٠٢٦-٠١-١٥ |
| 3:30 PM | ٣:٣٠ مساءً or ١٥:٣٠ |
| Jan 15, 2026 | ١٥ يناير ٢٠٢٦ |
| 01/15/2026 | ١٥/٠١/٢٠٢٦ |
| 2026/01/15 14:30:00 | ٢٠٢٦/٠١/١٥ ١٤:٣٠:٠٠ |
| Q1 2026 | الربع الأول ٢٠٢٦ |
| FY2025 | السنة المالية ٢٠٢٥ |
| 1446 AH | ١٤٤٦هـ |
| 2026 CE | ٢٠٢٦م |

### 3.7 Duration

| English | Arabic |
|---------|--------|
| 2 years | سنتان (dual) or عامان |
| 3 months | ٣ أشهر |
| 10 days | ١٠ أيام |
| 1 week | أسبوع واحد |
| Half an hour | نصف ساعة |
| 24 hours | ٢٤ ساعة |

---

## 4. Addresses (العناوين)

### 4.1 Address Order

Arabic addresses follow a **largest-to-smallest** hierarchy, the reverse of the Western smallest-to-largest order.

| Order | Arabic | English Equivalent |
|-------|--------|-------------------|
| 1 | الدولة (Al-Dawlah) | Country |
| 2 | المنطقة / المحافظة (Al-Mintaqah / Al-Muhafazah) | Region / Governorate |
| 3 | المدينة (Al-Madinah) | City |
| 4 | الحي (Al-Hayy) | District / Neighborhood |
| 5 | الشارع (Al-Shari') | Street |
| 6 | رقم المبنى (Raqm al-Mabna) | Building Number |
| 7 | رقم الشقة / الطابق (Raqm al-Shiqqah / al-Tabiq) | Apartment / Floor |

**Example:**
```
المملكة العربية السعودية، منطقة الرياض، مدينة الرياض، حي العليا، شارع الملك فهد، مبنى رقم ٢٣، الطابق الرابع
```
(Saudi Arabia, Riyadh Region, Riyadh City, Al-Olaya District, King Fahd Street, Building 23, 4th Floor)

### 4.2 Translation of Address Components

| English | Arabic |
|---------|--------|
| Street | شارع (abbr. ش) |
| Road | طريق (abbr. ط) |
| Avenue | جادة (abbr. ج) |
| Alley / Lane | زقاق / حارة |
| Building | مبنى / عمارة |
| Apartment | شقة |
| Floor | طابق / دور |
| Office | مكتب |
| PO Box | صندوق بريد (ص.ب) |
| Postal Code | الرمز البريدي |
| Kingdom of Saudi Arabia | المملكة العربية السعودية |
| United Arab Emirates | الإمارات العربية المتحدة |
| State of Kuwait | دولة الكويت |

### 4.3 Postal Code Formats

| Country | Format | Example |
|---------|--------|---------|
| Saudi Arabia | 5 digits | ١١٥٦٤ |
| UAE | 5 digits | ٠٠٠٠٠ (PO Box system) |
| Egypt | 5 digits | ١١٥١١ |
| Jordan | 5 digits | ١١١١٨ |

### 4.4 Examples (10+)

| Source | Correct AR |
|--------|------------|
| 123 Main St, NY, USA | الولايات المتحدة، نيويورك، شارع مين الرئيسي، رقم ١٢٣ |
| PO Box 1234, Riyadh | صندوق بريد ١٢٣٤، الرياض |
| Floor 5, Building 7 | المبنى رقم ٧، الطابق الخامس |
| Apt 3B | الشقة ٣ب |
| King Fahd Road | طريق الملك فهد |
| Sheikh Zayed Road | شارع الشيخ زايد |
| Corniche Street | شارع الكورنيش |
| Al-Madinah Al-Munawwarah | المدينة المنورة |
| District 5, Cairo | القاهرة، الحي الخامس |
| Jeddah, Saudi Arabia | المملكة العربية السعودية، جدة |

---

## 5. Proper Nouns (الأسماء العلم)

### 5.1 Definite Article (ال) Rules — Solar and Lunar Letters

The definite article الـ (Al-) behaves differently depending on the first letter of the noun.

**Solar Letters (الحروف الشمسية)** — The ل of ال is **assimilated** in pronunciation (geminated), but still written.

| Letter | Pronunciation | Example |
|--------|---------------|---------|
| ت | at-T... | التاج (at-taj) |
| ث | ath-Th... | الثورة (ath-thawrah) |
| د | ad-D... | الدين (ad-din) |
| ذ | adh-Dh... | الذهب (adh-dhahab) |
| ر | ar-R... | الرحمن (ar-rahman) |
| ز | az-Z... | الزيت (az-zayt) |
| س | as-S... | الشمس (ash-shams) |
| ش | ash-Sh... | الشارع (ash-shari') |
| ص | as-S... | الصبر (as-sabr) |
| ض | ad-D... | الضوء (ad-daw') |
| ط | at-T... | الطريق (at-tariq) |
| ظ | az-Z... | الظل (az-zill) |
| ل | al-L... | الليل (al-layl) — note: ل is also solar! |
| ن | an-N... | النور (an-nur) |

**Lunar Letters (الحروف القمرية)** — The ل of ال is **pronounced clearly**.

| Letter | Pronunciation | Example |
|--------|---------------|---------|
| ا | al-... | الأب (al-ab) |
| ب | al-B... | البيت (al-bayt) |
| ج | al-J... | الجبل (al-jabal) |
| ح | al-H... | الحق (al-haqq) |
| خ | al-Kh... | الخير (al-khayr) |
| ع | al-'... | العلم (al-'ilm) |
| غ | al-Gh... | الغروب (al-ghurub) |
| ف | al-F... | الفجر (al-fajr) |
| ق | al-Q... | القمر (al-qamar) |
| ك | al-K... | الكتاب (al-kitab) |
| م | al-M... | المطر (al-matar) |
| هـ | al-H... | الهلال (al-hilal) |
| و | al-W... | الوقت (al-waqt) |
| ي | al-Y... | اليمن (al-yaman) |

**Mnemonic:** Solar letters = ت ث د ذ ر ز س ش ص ض ط ظ ل ن (initials of "طب ثم دنا زائر شمس صف ضع طلب لن"). Lunar letters = the rest.

### 5.2 Transliteration of Foreign Names

| Source Name | Arabic Transliteration | Notes |
|-------------|----------------------|-------|
| John | جون | Phonetic approximation |
| Smith | سميث | |
| New York | نيويورك | Written as one word |
| Los Angeles | لوس أنجلوس | |
| Washington | واشنطن | |
| London | لندن | Well-established form |
| Paris | باريس | Well-established form |
| Berlin | برلين | |
| Tokyo | طوكيو | Uses ط for T |
| Beijing | بكين | |

**Principles:**
- Use well-established Arabic forms where they exist (e.g., لندن not لاندن).
- For new names, use phonetic approximation based on Arabic phonology.
- The definite article ال is not typically added to foreign place names (although اليمن, العراق, etc. are exceptions).
- Names starting with vowels often take a hamza: أندرو (Andrew), إيمي (Amy).

### 5.3 Honorifics and Titles

| English | Arabic | Abbreviation |
|---------|--------|-------------|
| Mr. | السيد | أ. or س. |
| Mrs. | السيدة | السيدة |
| Miss | الآنسة | الآنسة |
| Dr. | الدكتور | د. |
| Professor | الأستاذ / الأستاذة | أ.د. (professor) |
| Engineer | المهندس / المهندسة | م. |
| His Excellency | صاحب السعادة / معالي | سعادة / معالي |
| His Highness | صاحب السمو | سمو |
| His Majesty | صاحب الجلالة | جلالة |
| Sheikh | الشيخ | الشيخ |

**Rules:**
- Honorifics precede the name: السيد أحمد (not أحمد السيد).
- Multiple titles: الأستاذ الدكتور محمد (Professor Dr. Muhammad).
- In formal correspondence, use respectful forms: حضرة صاحب السعادة (His Excellency).

### 5.4 Place Names — Well-Known Arabic Forms

| English | Arabic | Notes |
|---------|--------|-------|
| Saudi Arabia | المملكة العربية السعودية | Full formal name |
| Egypt | مصر | Also: جمهورية مصر العربية |
| Iraq | العراق | Takes definite article |
| Jordan | الأردن | Takes definite article |
| Kuwait | الكويت | Takes definite article |
| UAE | الإمارات العربية المتحدة | |
| Oman | عُمان | No definite article |
| Qatar | قطر | No definite article |
| Bahrain | البحرين | Takes definite article |
| Yemen | اليمن | Takes definite article |
| Syria | سوريا | Also: سورية |
| Lebanon | لبنان | No definite article |
| Palestine | فلسطين | No definite article |
| Morocco | المغرب | Takes definite article |
| Algeria | الجزائر | Takes definite article |
| Tunisia | تونس | No definite article |
| Sudan | السودان | Takes definite article |
| Libya | ليبيا | No definite article |

### 5.5 Company and Organization Names

- Translate the generic part, keep the brand name: "Microsoft Corporation" → شركة مايكروسوفت
- "Apple Inc." → شركة آبل (or simply آبل)
- "United Nations" → الأمم المتحدة
- "World Health Organization" → منظمة الصحة العالمية
- "World Bank" → البنك الدولي
- Do NOT translate registered trademarks: iPhone → آيفون (transliterated) but keep iPhone in technical text.

---

## 6. Punctuation (علامات الترقيم)

### 6.1 Arabic-Specific Punctuation

| Name | Symbol | Unicode | Usage |
|------|--------|---------|-------|
| Arabic comma | ، | U+060C | Separates clauses and list items |
| Arabic semicolon | ؛ | U+061B | Stronger pause than comma |
| Arabic question mark | ؟ | U+061F | Ends an interrogative sentence |
| Arabic percentage sign | ٪ | U+066A | Alternative to % in some contexts |
| Arabic decimal separator | ٫ | U+066B | Separates integer from fractional part |
| Arabic thousands separator | ٬ | U+066C | Groups digits in large numbers |
| Tatweel / Kashida | ـ | U+0640 | Justification extension character |
| Arabic full stop (same as Western) | . | U+002E | End of sentence |

### 6.2 Quotation Marks

| Type | Opening | Closing | Example |
|------|---------|---------|---------|
| Curly double quotes | " | " | قال "مرحباً" |
| Guillemets (French-style) | « | » | قال «مرحباً» |
| Angle quotes (alternative) | ‹ | › | |

**Note on RTL and Quotation Marks:**
In RTL text, quotation marks may appear visually reversed depending on the renderer. The opening quotation mark should be at the **beginning of the quoted text** (which is the right side in RTL). Use Unicode directional marks (‎ U+200E / ‏ U+200F) if nesting or mixed-direction quotes cause rendering issues.

### 6.3 Comma Usage in Arabic

- The Arabic comma (،) is used more sparingly than in English.
- In lists, the Arabic comma separates items: التفاح، البرتقال، الموز
- Before conjunctions like و (and) and فـ (so), the comma is often omitted.
- In complex sentences, the comma clarifies clause boundaries.

### 6.4 Kashida / Tatweel (كشيدة / تطويل)

- The tatweel character ـ (U+0640) is used for **justification** in Arabic calligraphy and typesetting.
- **Do not add kashida in digital/plain text** unless reproducing a specific calligraphic style.
- Modern document layout uses character spacing and font features instead of kashida.
- Kashida artificially inserted in OCR output should be **removed** during post-processing.

### 6.5 Spacing Rules

- **No space** before comma, period, semicolon, or question mark (unlike French): كتبته، ثم قرأته؟ (correct)
- **Space after** punctuation marks (same as Western).
- **No space** between the definite article ال and its noun: الكتاب (not ال كتاب).
- **Space** around dashes: الرياض — العاصمة (em-dash with spaces).
- **No space** around parentheses when enclosing a word: (النص) (not ( النص )).

### 6.6 Parentheses and Brackets

- Standard parentheses ( ) are used in Arabic as in English.
- Square brackets [ ] are used for editorial insertions and restorations.
- Curly braces { } are used in specialized/technical content.

### 6.7 Ellipsis

- Arabic uses the same ellipsis as English: ...
- In Arabic, it may be used more liberally for dramatic pauses.
- No space before ellipsis in Arabic.

### 6.8 Punctuation Examples (10+)

| Source | Correct AR | Incorrect AR |
|--------|------------|--------------|
| Hello, how are you? | مرحباً، كيف حالك؟ | مرحبا, كيف حالك؟ (Western comma) |
| Is this correct? | هل هذا صحيح؟ | هل هذا صحيح? (Western question mark) |
| Buy: apples, oranges. | اشترِ: تفاحاً، برتقالاً. | اشتر: تفاحا، برتقالا. (missing diacritics) |
| He said: "Go there." | قال: «اذهب إلى هناك». | قال: "اذهب إلى هناك." (acceptable, but guillemets preferred) |
| The book; the pen; the desk | الكتاب؛ والقلم؛ والمكتب | ; used with spaces (incorrect) |
| Wait — don't go! | انتظر — لا تذهب! | انتظر-لا تذهب! (no spaces around dash) |
| 50% done | تم ٥٠٪ | 50% (mixed digits) |
| See page 5 (section 2) | انظر صفحة ٥ (القسم ٢) | انظر صفحة 5 (القسم 2) |
| 1, 2, 3... | ١، ٢، ٣... | 1,2,3... |
| Dear Sir, | سيدي الفاضل، | عزيزي السيد, (Western comma) |

---

## 7. Formatting (التنسيق)

### 7.1 Text Direction

- Arabic is a **right-to-left (RTL)** script.
- Numbers and embedded LTR text are **left-to-right** within RTL context (bidirectional text).
- The direction of the entire document should be set to RTL.
- Mixed LTR/RTL content requires explicit bidirectional markup.

### 7.2 Paragraph Alignment

- Arabic paragraphs should be **right-aligned**.
- **Left-aligned** Arabic text is incorrect and signals poor quality.
- Full justification is common in print documents (newspapers, books).
- Digit-alignment (numbers) in tables: right-aligned in RTL context.

### 7.3 Lists and Numbering

- Bullet lists in RTL: bullets appear on the **right** side.
- Numbered lists in RTL: numbers appear on the **right** side.
- Numbering flows **right-to-left**: ٣. ٢. ١. (not 1. 2. 3.)
- Nested lists: indent from the right.
- In bilingual documents, keep list direction consistent with the Arabic version.

### 7.4 Tables

- Table headers in Arabic RTL tables are typically on the **right** side (first column).
- Table content flows right-to-left.
- Column order in RTL tables is the reverse of LTR tables.
- Numeric columns: right-align numbers.

### 7.5 Mixed RTL/LTR Content

- Embedded English text within Arabic: use LRM (Left-to-Right Mark, U+200E) if needed.
- Embedded Arabic text within English: use RLM (Right-to-Left Mark, U+200F) if needed.
- Phone numbers, emails, URLs are LTR even in Arabic text.
- Code and technical strings remain LTR.

### 7.6 Page Layout

- Page numbering: Arabic documents may use Arabic numerals (١, ٢, ٣) or Western numerals.
- Section numbering: use Arabic numerals consistently.
- Headers and footers should be right-aligned or centered.
- Footnotes appear at the bottom of the page (same as Western).

### 7.7 Line Spacing and Indentation

- Standard line spacing: 1.15–1.5 for readability.
- First-line indent: 0.5–1 cm from the right.
- Paragraph spacing: 6–12 pt after each paragraph.

### 7.8 Formatting Examples (10+)

| Element | Correct AR | Incorrect AR |
|---------|------------|--------------|
| Bullet list | • النقطة الأولى | • First point (LTR orientation) |
| Numbered list | ١. بند ٢. بند ٣. بند | 1. بند 2. بند (LTR numbering) |
| Table direction | Header on right | Header on left (LTR table) |
| Right alignment | نص محاذى لليمين | نص محاذى لليسار |
| Mixed text | مرحباً John | John مرحباً (poor bidi) |
| URL in text | زورنا example.com | example.com زورنا (no space) |
| Email in text | راسلنا user@site.com | user@site.com راسلنا |
| Phone number: | الهاتف: +966 55 123 4567 | +966 55 123 4567:الهاتف |
| Page header | right-aligned | left-aligned |
| Footnote marker | النص^(١) | ^(1) النص |

---

## 8. Grammar (القواعد)

### 8.1 Word Order

| Type | Order | Example |
|------|-------|---------|
| Classical / Formal MSA | **VSO** (Verb-Subject-Object) | كتب الطالب الدرس (The student wrote the lesson) |
| Modern / Journalistic | **SVO** (Subject-Verb-Object) | الطالب كتب الدرس (The student wrote the lesson) |
| Interrogative | Verb often first | هل كتب الطالب الدرس؟ (Did the student write the lesson?) |

**Rule:** For formal document translation, prefer **VSO** for narrative passages and general statements. Use **SVO** for topic-comment structures and when emphasis is on the subject.

### 8.2 Gender (الجنس: مذكر ومؤنث)

Arabic has two genders: masculine (مذكر) and feminine (مؤنث).

**Feminine markers:**
- Words ending in ة (taa marbuta): مدرسة (school), جامعة (university)
- Words ending in ى (alif maqsurah): كبرى (greatest), ذكرى (memory)
- Certain body parts (eye, ear, hand, foot)
- Certain natural elements: شمس (sun), نار (fire), ريح (wind)
- Most countries and cities: مصر (Egypt), دمشق (Damascus)

**Gender agreement:**
| Component | Rule | Example |
|-----------|------|---------|
| Adjective | Follows noun gender | بيت كبير / سيارة كبيرة |
| Verb | Agrees with subject gender | كتب الطالب / كتبت الطالبة |
| Demonstrative | هذا (masc) / هذه (fem) | هذا الكتاب / هذه السيارة |
| Pronouns | هو (masc) / هي (fem) | |

### 8.3 Number (العدد: مفرد، مثنى، جمع)

**Three numbers:** singular (مفرد), dual (مثنى), and plural (جمع).

| Number | Marker | Example |
|--------|--------|---------|
| Singular (مفرد) | Base form | كتاب (book) |
| Dual (مثنى) | انِ (nominative) / ينِ (oblique) | كتابان / كتابين (two books) |
| Sound masculine plural | ونَ (nominative) / ينَ (oblique) | معلمون / معلمين (teachers) |
| Sound feminine plural | ات | معلمات (female teachers) |
| Broken plural | Internal vowel change | كتب (books), مدارس (schools) |

**Agreement rules:**
- Adjectives agree in number with the noun (except for non-human plurals which take feminine singular adjectives): كتب كثيرة (many books, lit. "books many" — feminine singular adjective)
- Dual subjects take dual verbs: الطالبان كتبا (the two students wrote)
- Plural subjects take plural verbs

### 8.4 Idafa Construct (الإضافة — Possessive / Genitive Construction)

The idafa is a two-noun construct where the first is possessed and the second is the possessor.

| Rule | Example | Translation |
|------|---------|-------------|
| First term: indefinite (no ال) | كتاب الطالب | the student's book |
| Second term: definite or indefinite | كتاب طالب | a student's book |
| First term: no nunation (تنوين) | كتابُ الطالب (nom.) | |
| Multiple possessors | كتاب الطالب المجتهد | the diligent student's book |
| Adjectives follow the construct | كتاب الطالب الجديد | the student's new book |

**Common errors to avoid:**
- ❌ الكتاب الطالب (inserting ال on the first term)
- ❌ كتابة الطالب (using attached pronoun incorrectly for general possession)
- ✅ كتاب الطالب (correct idafa)

### 8.5 Verb Conjugation Patterns

| Pronoun | Past (كتب) | Present (يكتب) | Meaning |
|---------|-----------|----------------|---------|
| أنا (I) | كتبتُ | أكتب | I wrote / I write |
| أنتَ (you m.) | كتبتَ | تكتب | You wrote |
| أنتِ (you f.) | كتبتِ | تكتبين | You wrote |
| هو (he) | كتب | يكتب | He wrote |
| هي (she) | كتبت | تكتب | She wrote |
| نحن (we) | كتبنا | نكتب | We wrote |
| أنتم (you pl.) | كتبتم | تكتبون | You (pl.) wrote |
| هم (they m.) | كتبوا | يكتبون | They wrote |
| هن (they f.) | كتبن | يكتبن | They (f.) wrote |

### 8.6 Prepositions (حروف الجر)

| Arabic | Meaning | Governs | Example |
|--------|---------|---------|---------|
| في | in, at | Genitive | في المنزل |
| على | on, upon | Genitive | على الطاولة |
| من | from, of | Genitive | من المدرسة |
| إلى | to, toward | Genitive | إلى المكتب |
| عن | about, from | Genitive | عن الموضوع |
| مع | with | Genitive | مع الأصدقاء |
| بـ | with, by | Genitive | بالقلم |
| لـ | for, belonging to | Genitive | للطلاب |

### 8.7 Relative Clauses

- Definite antecedent: use الذي/التي/الذين/اللواتي
- Indefinite antecedent: no relative pronoun

| Type | Example | Translation |
|------|---------|-------------|
| Definite masc. sing. | الطالب الذي كتب | The student who wrote |
| Definite fem. sing. | الطالبة التي كتبت | The student (f.) who wrote |
| Definite masc. pl. | الطلاب الذين كتبوا | The students who wrote |
| Indefinite antecedent | طالب كتب الدرس | A student who wrote the lesson |

### 8.8 Negation

| Tense | Negation Word | Example |
|-------|---------------|---------|
| Past | لم + jussive | لم يكتب (he did not write) |
| Past (emphatic) | ما + past | ما كتب (he did not write) |
| Present | لا + indicative | لا يكتب (he does not write) |
| Future | لن + subjunctive | لن يكتب (he will not write) |
| Imperative | لا + jussive | لا تكتب (don't write!) |
| Nominal sentence | ليس | ليس كبيرًا (it is not big) |

### 8.9 Grammar Examples (15+)

| Source | Correct AR | Notes |
|--------|------------|-------|
| The student wrote | كتب الطالب | VSO order |
| Two students wrote | كتب طالبان | Dual subject + dual verb |
| The female students wrote | كتبت الطالبات | Fem. plural verb form |
| A big house | بيت كبير | Adjective follows noun |
| The big house | البيت الكبير | Both definite |
| The teacher's book | كتاب المدرس | Idafa construct |
| New cars | سيارات جديدة | Non-human plural + fem. sing. adj. |
| I have a book | عندي كتاب | Prepositional phrase |
| The man who came | الرجل الذي جاء | Definite + relative pronoun |
| He did not come | لم يأتِ | Past negation with لم |
| She is a doctor | هي طبيبة | No article needed for profession |
| This is a pen | هذا قلم | Demonstrative + noun |
| In the house | في البيت | Preposition + genitive |
| The two teachers (m.) | المدرسان (nom.) / المدرسين (obl.) | Dual declension |
| From the school | من المدرسة | من + genitive |
| Write! (m. sing.) | اكتب | Imperative |
| Write! (f. sing.) | اكتبي | Fem. imperative |
| Write! (pl.) | اكتبوا | Plural imperative |

---

## 9. Formality (مستويات اللغة)

### 9.1 Diglossia: الفصحى vs العامية

Arabic is a diglossic language. The two registers are never mixed in formal writing.

| Register | Arabic Name | Usage | Characteristics |
|----------|-------------|-------|-----------------|
| Modern Standard Arabic | الفصحى (MSA) | **ALL formal documents** | Full case endings (الإعراب), formal vocabulary |
| Classical Arabic | الفصحى التراثية | Religious texts, legal | Quranic vocabulary, archaic structures |
| Dialectal Arabic | العامية | Quoted speech, informal | No case endings, region-specific vocabulary |

**Rule:** All translated documents use **MSA (الفصحى)** unless the source explicitly contains dialectal speech that must be preserved as such.

### 9.2 Levels of Formality in MSA

| Level | Description | When to Use |
|-------|-------------|-------------|
| رسمي جدًا (Very formal) | Elaborate greetings, honorifics, flowery prose | Royal decrees, diplomatic notes, legal contracts |
| رسمي (Formal) | Standard business language, respectful address | Business correspondence, official reports |
| شبه رسمي (Semi-formal) | Polite but direct, fewer honorifics | Internal memos, professional emails |
| غير رسمي (Informal) | Colloquial-leaning written Arabic | Personal notes, social media (avoid in translation) |

### 9.3 Pronouns and Address

| Context | Pronoun | Example |
|---------|---------|---------|
| Very formal / To superior | حضرتك / سيادتك / سعادتك | سيادتك، نرجو التكرم بـ... |
| Formal to a group | أنتم (plural) | نأمل منكم... |
| Standard (to individual) | أنت / أنتِ | نرجو منك... |
| Informal | أنت / أنتِ (with dialectal influence) | —

**Honorific address forms:**
- حضرة صاحب السعادة / معالي / سمو (for dignitaries)
- السيد / السيدة الفاضل / الفاضلة (for general formal correspondence)
- صاحب / صاحبة الفضيلة (for religious figures / judges)
- سعادة السفير (for ambassadors)

### 9.4 Letter Openings and Closings

| Context | Arabic Opening | Arabic Closing |
|---------|---------------|----------------|
| Formal business | تحية طيبة وبعد، | وتقبلوا فائق الاحترام، |
| Very formal | السلام عليكم ورحمة الله وبركاته، أما بعد: | والله الموفق، |
| To a company | إلى السادة / شركة... | مع خالص الشكر والتقدير، |
| Government | سعادة / معالي ... حفظه الله | وتفضلوا بقبول فائق الاحترام |
| Academic | حضرة الأستاذ الدكتور ... المحترم | مع جزيل الشكر والامتنان |

### 9.5 Formality Vocabulary Choices

| Formal (رسمي) | Neutral (محايد) | Informal (عامي) | English |
|---------------|------------------|-----------------|---------|
| يستلم / يتسلم | يأخذ | ياخد | receive |
| يُعلم / يُفيد | يقول | يقول | inform |
| يطلب | يريد | عايز | want/request |
| يتفضل | يفعل | يعمل | kindly do |
| الآنف الذكر | المذكور | المذكور | aforementioned |
| أدناه | التالي | الجاي | below |
| بناءً على | حسب | على حسب | based on |
| يسرنا أن | نحن سعداء بـ | مبسوطين | we are pleased to |

### 9.6 Passive Voice

| Context | Active | Passive (formal) |
|---------|--------|------------------|
| Formal | قامت الشركة بتوقيع العقد | تم توقيع العقد من قبل الشركة |
| Very formal | نرفق لكم | مرفق لكم / يُرفق طيه |
| Impersonal | نحتاج إلى | يُحتاج إلى |

Passive voice (المبني للمجهول) is **more common in formal Arabic** than in English. It is formed by changing the internal vowels of the verb: كَتَبَ (he wrote) → كُتِبَ (it was written).

### 9.7 Formality Examples (10+)

| Informal / Source | Formal AR | Very Formal AR |
|-------------------|-----------|----------------|
| Please send the file | نرجو إرسال الملف | نرجو التكرم بإرسال الملف |
| We got your email | تلقينا بريدكم الإلكتروني | تشرفنا باستلام خطابكم |
| He said that... | أفاد بأن... | صرح / ذكر بأن... |
| We need your reply | نأمل الحصول على ردكم | نأمل التفضل بالإفادة |
| Send us the contract | يرجى إرسال العقد | نرجو التفضل بإرسال العقد |
| The price is 100 | السعر ١٠٠ | قيمته ١٠٠ |
| I think that | أعتقد أن | أرى أن / من وجهة نظري |
| This is important | هذا مهم | يكتسب هذا الأمر أهمية بالغة |
| We are working on it | نحن بصدد العمل عليه | يعمل الفريق حاليًا على إنجازه |
| Thanks | شكرًا | مع خالص الشكر والتقدير |
| Yours sincerely | مع الاحترام | وتفضلوا بقبول فائق الاحترام |

---

## 10. OCR Artifacts (مشكلات التعرف البصري)

### 10.1 Common OCR Confusions in Arabic Script

Arabic OCR produces systematic errors due to the connected nature of the script.

| Correct | Common OCR Error | Cause |
|---------|-----------------|-------|
| س (seen) | ش (sheen) | Dot placement error |
| ب (ba) | ت (ta) / ث (tha) / ن (nun) | Dot count confusion |
| ح (ha) | ج (jim) / خ (kha) | Dot placement |
| ع ('ayn) | غ (ghayn) | Dot addition |
| ف (fa) | ق (qaf) | Dot count (one vs two) |
| د (dal) | ذ (dhal) | Dot addition |
| ر (ra) | ز (zay) | Dot addition |
| ص (sad) | ض (dad) | Dot addition |
| ط (ta) | ظ (dha) | Dot addition |
| ـة (taa marbuta) | ـه (ha) | Shape similarity |
| لا (lam-alif) | ل ا (separated) | Ligature handling |
| أ (alif with hamza) | إ / ا | Hamza direction |

### 10.2 Restoration Markers

When fixing OCR errors in translated/processed text, use the following markers:

| Artifact Type | Marker Format | Example |
|---------------|--------------|---------|
| Character correction | [تم الاستعادة: الحرف] | [تم الاستعادة: المكتبة] ← المكتية |
| Word restoration | [تم الاستعادة: ...] | قرأ [تم الاستعادة: الكتاب] ← قرأ لكتاب |
| Diacritic restoration | Add حركات in brackets | [تم استعادة التشكيل] |
| Missing word | [تمت الإضافة: ...] | |

### 10.3 Specific Restoration Rules

| Issue | Broken Text | Restored Text |
|-------|-------------|---------------|
| Missing hamza | هذا الاب | هذا الأب |
| Missing dots | سجرة (seen in place of sh + dots missing) | شجرة |
| Broken lam-alif | ل ا (separated) | لا |
| Taa marbuta → ha | مدرسة → مدرسه | مدرسة |
| Missing medial forms | ب ا ب (separated) | باب |
| Ghost kashida | كـــتاب | كتاب |
| Wrong ا direction | استلم → أستلم | استلم (first person vs. third) |
| Missing ی vs ى | علی → على | على |
| Alif maqsurah | سعی → سعى | سعى |
| Wrong glyph shape | اللہ (Urdu style) → الله | الله |

### 10.4 Pre-Processing Steps

1. **Remove kashida/tatweel**: Strip all U+0640 characters.
2. **Normalize alif**: Convert أ إ آ → ا (for search indexing; restore for display).
3. **Normalize taa marbuta**: Ensure ة vs ه correctness.
4. **Check lam-alif ligatures**: Ensure لا is one glyph.
5. **Fix spacing**: Remove extra spaces, especially around ال.
6. **Verify dots**: Confirm correct dot count on all letters.

### 10.5 OCR Artifact Examples (10+)

| OCR Output | Correct AR | Restoration Applied |
|------------|------------|-------------------|
| سملت الشركة | عملت الشركة | س→ع correction |
| المكتية العامة | المكتبة العامة | ب→ك correction |
| جامعة الدول العرية | جامعة الدول العربية | ب→ي correction |
| التقرير السبوعي | التقرير الأسبوعي | Missing alif |
| قراءة القـرآن | قراءة القرآن | Kashida removed |
| رداسة جديدة | دراسة جديدة | ر→د (placeholder shape) |
| الفلاحون يزرعون | الفلاحون يزرعون | Correct as-is (common false positive) |
| مؤسسة النقل | مؤسسة النقل | Check taa marbuta in مؤسسة |
| قال إنه ذاهب | قال إنه ذاهب | Ensure hamza on إن |
| هذا لامر مهم | هذا الأمر مهم | Broken lam-alif → ال |

---

## 11. Translation Philosophy (فلسفة الترجمة)

### 11.1 Register and Tone

**Rule:** All formal document translation into Arabic uses **Modern Standard Arabic (MSA / الفصحى)** with a register matching the source document's formality level.

| Source Register | Arabic Register | Characteristics |
|-----------------|-----------------|-----------------|
| Legal/Contract | رسمي جدًا (Very formal) | Full case endings, classical constructions, verbose openings |
| Business/Corporate | رسمي (Formal) | Standard MSA, polite forms, idiomatic business phrases |
| Technical/Manual | شبه رسمي (Semi-formal) | Clear MSA, direct, minimal ornamentation |
| Marketing/Creative | إبداعي (Creative MSA) | MSA with rhetorical devices, parallelism, rhythm |
| Academic/Scientific | أكاديمي (Academic) | Precisely structured, terminology-rich, passive voice |

### 11.2 Avoiding Ambiguity

Arabic allows for structural ambiguity (e.g., idafa chains, pronoun attachment). Follow these rules:

1. **Prefer explicit subjects**: Do not rely on verb inflection alone if context could be ambiguous.
   - ❌ كتبت الدرس (ambiguous: I/she wrote the lesson?)
   - ✅ أنا كتبت الدرس / هي كتبت الدرس

2. **Resolve pronoun reference**: Ensure that هو/هي/هم refer to clear antecedents.
   - ❌ رأيت الرجل وهو يقرأ كتابه (his book = the man's? someone else's?)
   - ✅ رأيت الرجل وهو يقرأ كتاب الرجل / كتابه هو

3. **Avoid long idafa chains**: Break with prepositions.
   - ❌ كتاب مدرس اللغة العربية الجديد (whose book? whose Arabic? which is new?)
   - ✅ كتاب المدرس الجديد للغة العربية

### 11.3 Natural Arabic Flow

| Principle | English | Arabic (literal) | Arabic (natural) |
|-----------|---------|------------------|------------------|
| Avoid passive overuse | The decision was made | تم اتخاذ القرار | اتُخذ القرار (or تقرر) |
| Use verbal sentences | The report contains... | التقرير يحتوي على... | يحتوي التقرير على... |
| Prefer definite subjects | A meeting was held | تم عقد اجتماع | عُقد اجتماع / انعقد اجتماع |
| Connector fluency | The product, which was launched... | المنتج الذي تم إطلاقه... | المنتج الذي أُطلق... |

### 11.4 Cultural Adaptation

| Concept | Western Source | Arabic Adaptation |
|---------|---------------|------------------|
| "Dear Sir/Madam" | Generic | السيد/السيدة الفاضل/ة |
| "John and Mary" | Given names | السيد جون والسيدة ماري (or simply transliterated) |
| "Best regards" | Short | مع خالص التحية والتقدير |
| "FYI" | Acronym | لعلمكم / للإحاطة |
| "Break a leg" | Idiom | بالتوفيق (equivalent, not literal) |
| "It's raining cats and dogs" | Idiom | السماء تمطر بغزارة (not literal) |
| "Time is money" | Metaphor | الوقت من ذهب (cultural equivalent) |
| "Piece of cake" | Idiom | سهل جدًا / أمر بسيط |

### 11.5 Terminology Consistency

- **Glossary required**: Maintain a project glossary of key terms with approved Arabic translations.
- **One term, one translation**: Do not translate the same source term differently in the same document.
- **Loanwords**: Use established Arabic loanwords over literal translation for technical terms.
  - ✓ الإنترنت (internet) not الشبكة العنكبوتية العالمية
  - ✓ الكمبيوتر or الحاسوب (choose one)
  - ✓ البريد الإلكتروني (email) not الإيميل (too informal)
- **Neologisms**: For new terms not in existing glossaries, derive using Arabic morphological patterns or use Arabicized loanwords.

### 11.6 Sentence Length and Structure

| Guideline | Arabic | English Comparison |
|-----------|--------|-------------------|
| Arabic sentences can be longer | يستخدم الفواصل والروابط أكثر | Use more periods |
| Use و (wa) coordination | ...قام الفريق بتحليل البيانات وأعد التقرير ورفعه | ...analyzed, prepared, and submitted |
| Avoid comma splices in translation | Break into separate sentences | Use semicolons/conjunctions |
| Use participial phrases | بعد الانتهاء من التحليل،... | After completing the analysis... |

### 11.7 Special Considerations for Numbers in Translation

- **Render numerical values in Arabic digits** (١٢٣) unless the document is for a Maghreb audience (0–9).
- **Spell out numbers** at the beginning of sentences (ثمانية وعشرون طالبًا... not ٢٨ طالبًا...).
- **Currency** in legal documents: write both in words and digits.

### 11.8 Quality Checklist

| Check | Description |
|-------|-------------|
| Digit consistency | All numbers use the same digit set |
| Calendar consistency | Single calendar system (or both clearly labeled) |
| RTL layout | All paragraphs right-aligned, lists right-justified |
| Definite article | Correct solar/lunar assimilation |
| Gender agreement | Verbs, adjectives agree with nouns |
| Formality | Consistent register throughout |
| Terminology | No conflicting translations for same term |
| Punctuation | Arabic-specific marks (، ؟ ؛) correctly used |
| OCR artifacts | All kashida removed, no residual OCR errors |
| Idafa | No incorrect definite article on first term |

---

> This document is part of the Arabic (ar) translation knowledge base. For scoring and evaluation criteria, see `scoring-rubric.md`.
