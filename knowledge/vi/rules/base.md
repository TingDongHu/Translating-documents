# Quy tắc Dịch thuật Tiếng Việt (Vietnamese Translation Rules)

> Tài liệu tham khảo toàn diện cho dịch thuật từ ngôn ngữ nguồn sang tiếng Việt.
> Phiên bản: 1.0 | Ngày: 2026-05

---

## Mục lục

1. [Định dạng Số (Number Format)](#1-định-dạng-số-number-format)
2. [Tiền tệ (Currency)](#2-tiền-tệ-currency)
3. [Ngày và Giờ (Date and Time)](#3-ngày-và-giờ-date-and-time)
4. [Địa chỉ (Addresses)](#4-địa-chỉ-addresses)
5. [Danh từ Riêng (Proper Nouns)](#5-danh-từ-riêng-proper-nouns)
6. [Dấu câu (Punctuation)](#6-dấu-câu-punctuation)
7. [Định dạng Văn bản (Formatting)](#7-định-dạng-văn-bản-formatting)
8. [Ngữ pháp (Grammar)](#8-ngữ-pháp-grammar)
9. [Nghi thức Xã giao (Formality)](#9-nghi-thức-xã-giao-formality)
10. [Hiện vật OCR (OCR Artifacts)](#10-hiện-vật-ocr-ocr-artifacts)
11. [Triết lý Dịch thuật (Translation Philosophy)](#11-triết-lý-dịch-thuật-translation-philosophy)

---

## 1. Định dạng Số (Number Format)

### 1.1 Dấu thập phân (Decimal Separator)

Tiếng Việt sử dụng **dấu phẩy (`,`)** làm dấu phân cách thập phân, chịu ảnh hưởng từ tiếng Pháp. **Không** sử dụng dấu chấm (`.`) làm dấu thập phân.

| Đúng (VI) | Sai | Giá trị |
|-----------|-----|---------|
| 3,14 | 3.14 | Số pi |
| 0,5 | 0.5 | Một nửa |
| 99,99 | 99.99 | Giá tiền |
| 1.234,56 | 1,234.56 | Số lớn có thập phân |
| 10.000,00 | 10,000.00 | Số tròn có thập phân |
| 0,001 | 0.001 | Phần nghìn |
| 3.141.592,653 | 3,141,592.653 | Số pi mở rộng |

**Quy tắc:**
- Luôn dùng dấu phẩy `,` cho phần thập phân.
- Dấu chấm `.` làm dấu thập phân là lỗi nghiêm trọng.

### 1.2 Dấu phân cách nhóm số (Thousands Separator)

Tiếng Việt sử dụng **dấu chấm (`.`)** hoặc **dấu cách (khoảng trắng)** làm dấu phân cách hàng nghìn.

| Đúng (VI) | Cách viết khác | Ý nghĩa |
|-----------|----------------|---------|
| 1.000 | 1 000 | Một nghìn |
| 10.000 | 10 000 | Mười nghìn |
| 100.000 | 100 000 | Một trăm nghìn |
| 1.000.000 | 1 000 000 | Một triệu |
| 1.000.000.000 | 1 000 000 000 | Một tỷ |
| 2.500 | 2 500 | Hai nghìn năm trăm |
| 150.000 | 150 000 | Một trăm năm mươi nghìn |

**Quy tắc:**
- Dấu chấm `.` là dấu phân cách nhóm số phổ biến nhất.
- Khoảng trắng cũng được chấp nhận nhưng ít phổ biến hơn trong văn bản chính quy.
- Không dùng dấu phẩy `,` làm dấu phân cách nhóm số (dấu phẩy là dấu thập phân).

### 1.3 Số âm (Negative Numbers)

Số âm được biểu diễn bằng dấu trừ `-` đặt trước số, hoặc trong ngoặc đơn `( )` trong văn bản tài chính.

| Định dạng | Ví dụ |
|-----------|-------|
| Dấu trừ | -5,25 |
| Ngoặc đơn (tài chính) | (5,25) |
| Dấu trừ số lớn | -1.234,56 |
| Ngoặc đơn số lớn | (1.234,56) |

### 1.4 Tỷ lệ phần trăm (Percentages)

Dấu phần trăm `%` đặt **sau số** với một khoảng trắng hoặc không.

| Ví dụ | Ghi chú |
|-------|---------|
| 45,6% | Phổ biến nhất |
| 45,6 % | Cũng được chấp nhận |
| 100% | Không cách khi số tròn |
| Tăng 12,5% | Trong câu |
| Giảm 0,5% | Tỷ lệ nhỏ |
| Lãi suất 8,25%/năm | Trong hợp đồng |
| 50% ± 2% | Sai số |

**Ví dụ trong câu:**
> Tỷ lệ lạm phát năm 2025 là 3,5%, thấp hơn mức dự báo 4,2%.
> Có 99,9% khả năng hoàn thành đúng hạn.
> Giá cổ phiếu giảm 12,75% so với quý trước.

### 1.5 Phân số (Fractions)

| Ví dụ | Định dạng |
|-------|-----------|
| 1/2 | Một phần hai |
| 3/4 | Ba phần tư |
| 2 1/2 | Hai một phần hai |
| 7/10 | Bảy phần mười |

### 1.6 Số thứ tự (Ordinal Numbers)

| VI | English |
|----|---------|
| thứ nhất | 1st |
| thứ hai | 2nd |
| thứ ba | 3rd |
| thứ tư | 4th |
| thứ năm | 5th |
| lần thứ nhất/đầu tiên | first time |
| lần thứ hai | second time |

**Quy tắc:** Số thứ tự tiếng Việt dùng "thứ" + số đếm. Không dùng hậu tố như tiếng Anh (st, nd, rd, th).

### 1.7 Khoa học và Kỹ thuật

| Ký hiệu | VI Đúng | Ghi chú |
|---------|---------|---------|
| 1.000 m | Một nghìn mét | Khoảng cách giữa số và đơn vị |
| 25,4 mm | 25,4 mm | Dấu phẩy thập phân |
| 1.500 km² | 1.500 km² | Dấu chấm phân cách nghìn |
| 0,05 mg | 0,05 mg | Liều lượng nhỏ |
| 9,8 m/s² | 9,8 m/s² | Gia tốc trọng trường |
| 1.000.000 tấn | 1.000.000 tấn | Sản lượng |

---

## 2. Tiền tệ (Currency)

### 2.1 Đồng Việt Nam (VND)

Đơn vị tiền tệ chính thức của Việt Nam là **Đồng** (VND), ký hiệu **₫**.

| Định dạng | Ví dụ | Ghi chú |
|-----------|-------|---------|
| Số + ₫ | 50.000 ₫ | Phổ biến nhất |
| Số + đồng | 50.000 đồng | Trong văn bản chính quy |
| Số + VND | 50.000 VND | ISO code trong giao dịch quốc tế |
| Số tròn | 100.000 ₫ | Không có phần thập phân |
| Có thập phân | 25.500,50 ₫ | Khi cần độ chính xác |
| Dạng viết tắt | 50k | Không chính quy |

**Vị trí ký hiệu:** Ký hiệu `₫` luôn đặt **sau số tiền**, cách một khoảng trắng.

- **Đúng:** 150.000 ₫
- **Sai:** ₫150.000
- **Đúng:** 10.000.000 đồng
- **Sai:** đồng 10.000.000

### 2.2 Đô la Mỹ (USD)

| Định dạng | Ví dụ | Ghi chú |
|-----------|-------|---------|
| $ + số | $100 | Ký hiệu trước số |
| số + USD | 100 USD | ISO code |
| số + $ Mỹ | 100 $ Mỹ | Phân biệt với các loại đô la khác |
| Có thập phân | $99,99 | Dấu phẩy thập phân VI |
| Số lớn | $1.500,00 | Phân cách nghìn |

**Quy tắc:** Ký hiệu `$` đặt **trước** số (theo thông lệ quốc tế), nhưng phần thập phân theo định dạng VI.

- **Đúng:** Tổng số tiền là $1.250,50.
- **Sai:** Tổng số tiền là $1,250.50.
- **Đúng:** Giá niêm yết: 500 USD.
- **Sai:** Giá niêm yết: 500 $.

### 2.3 Euro (EUR)

| Định dạng | Ví dụ |
|-----------|-------|
| số + € | 100 € |
| số + EUR | 100 EUR |
| Có thập phân | 250,75 € |
| Số lớn | 1.500,00 € |

**Quy tắc:** Ký hiệu `€` đặt **sau số** (theo chuẩn VI và châu Âu).

### 2.4 Các loại tiền tệ khác

| ISO | Đơn vị | Định dạng VI |
|-----|--------|-------------|
| GBP | Bảng Anh | 100 £ hoặc 100 GBP |
| JPY | Yên Nhật | 10.000 ¥ hoặc 10.000 JPY |
| CNY | Nhân dân tệ | 100 ¥ (CNY) hoặc 100 CNY |
| KRW | Won Hàn Quốc | 50.000 ₩ hoặc 50.000 KRW |
| THB | Baht Thái | 1.000 ฿ hoặc 1.000 THB |
| SGD | Đô la Singapore | 100 SGD hoặc 100 $ Singapore |

### 2.5 Chuyển đổi và quy ước

**Quy tắc trong dịch thuật:**
- Giữ nguyên số tiền gốc, kèm theo ISO code.
- Chỉ chuyển đổi sang VND nếu có yêu cầu cụ thể.
- Ghi chú tỷ giá nếu thực hiện chuyển đổi.

**Ví dụ:**
> Ngân sách dự án là 50.000 USD (khoảng 1.250.000.000 ₫ theo tỷ giá 25.000 ₫/USD).
> Chi phí vận chuyển: 2.500 EUR (tương đương 70.000.000 ₫).
> Giá phòng: 1.500.000 ₫/đêm (khoảng 60 USD).

### 2.6 Cách viết số tiền trong văn bản pháp lý

> Số tiền: **Một tỷ, hai trăm năm mươi triệu đồng** (1.250.000.000 ₫).
> Bằng chữ: **Năm trăm nghìn đồng** (500.000 ₫).
> Tổng cộng: **Mười lăm triệu, ba trăm nghìn đồng** (15.300.000 ₫).

---

## 3. Ngày và Giờ (Date and Time)

### 3.1 Định dạng Ngày

Tiếng Việt sử dụng định dạng **DD/MM/YYYY** (chịu ảnh hưởng từ tiếng Pháp).

| Định dạng | Ví dụ | Ghi chú |
|-----------|-------|---------|
| DD/MM/YYYY | 25/05/2026 | Chuẩn phổ biến nhất |
| DD-MM-YYYY | 25-05-2026 | Dùng trong tên file |
| DD.MM.YYYY | 25.05.2026 | Ít phổ biến |
| Ngày DD tháng MM năm YYYY | Ngày 25 tháng 05 năm 2026 | Dạng đầy đủ trong văn bản |
| Tháng MM năm YYYY | Tháng 05 năm 2026 | Chỉ tháng và năm |

**Quy tắc quan trọng:**
- **Không bao giờ** dùng MM/DD/YYYY (định dạng Mỹ) — đây là lỗi nghiêm trọng.
- Ưu tiên DD/MM/YYYY với dấu gạch chéo `/`.

**So sánh:**
> **VI đúng:** 05/06/2026 = Ngày 5 tháng 6 năm 2026
> **EN (US) sai:** 05/06/2026 = Ngày 6 tháng 5 năm 2026
> **VI đúng:** 31/12/2025 = Ngày 31 tháng 12 năm 2025

### 3.2 Tên tháng trong tiếng Việt (Vietnamese Month Names)

| Số | Tháng VI | English | Ghi chú |
|----|----------|---------|---------|
| 1 | Tháng một (Tháng giêng) | January | "Tháng giêng" dùng trong văn cảnh dân gian/lịch âm |
| 2 | Tháng hai | February | |
| 3 | Tháng ba | March | |
| 4 | Tháng tư | April | |
| 5 | Tháng năm | May | |
| 6 | Tháng sáu | June | |
| 7 | Tháng bảy | July | |
| 8 | Tháng tám | August | |
| 9 | Tháng chín | September | |
| 10 | Tháng mười | October | |
| 11 | Tháng mười một | November | |
| 12 | Tháng mười hai (Tháng chạp) | December | "Tháng chạp" dùng trong văn cảnh dân gian/lịch âm |

**Quy tắc:**
- Dùng "tháng một" (không phải "tháng 1") trong văn bản chính quy.
- "Tháng giêng" (tháng 1 âm lịch) và "tháng chạp" (tháng 12 âm lịch) chỉ dùng khi nói về lịch âm.
- Tên tháng không viết hoa trừ đầu câu.

### 3.3 Thứ trong tuần (Days of the Week)

| VI | English | Ghi chú |
|----|---------|---------|
| Thứ hai | Monday | Không phải "Thứ 2" trong văn bản chính quy |
| Thứ ba | Tuesday | |
| Thứ tư | Wednesday | |
| Thứ năm | Thursday | |
| Thứ sáu | Friday | |
| Thứ bảy | Saturday | |
| Chủ nhật | Sunday | Không phải "Thứ chủ nhật" |

**Ví dụ:**
> Thứ hai, ngày 25 tháng 5 năm 2026
> Thứ bảy, ngày 30 tháng 5 năm 2026
> Chủ nhật, ngày 31 tháng 5 năm 2026

### 3.4 Định dạng Giờ (Time Format)

Tiếng Việt sử dụng **hệ 24 giờ**.

| Định dạng | Ví dụ | Ghi chú |
|-----------|-------|---------|
| HH:MM | 14:30 | Chuẩn phổ biến nhất |
| HH:MM:SS | 09:05:30 | Có giây |
| HHhMM | 14h30 | Dùng trong văn bản thông thường |
| HH giờ MM phút | 14 giờ 30 phút | Dạng đầy đủ |

**Quy tắc:**
- Luôn dùng hệ 24 giờ trong văn bản chính quy.
- Chuyển đổi AM/PM sang hệ 24 giờ:
  - 8:00 AM → 08:00
  - 12:00 PM → 12:00 (trưa)
  - 3:30 PM → 15:30
  - 11:59 PM → 23:59
  - 12:00 AM → 00:00 (nửa đêm)

**Ví dụ đúng/sai:**
> **Đúng:** Cuộc họp bắt đầu lúc 14:30.
> **Sai:** Cuộc họp bắt đầu lúc 2:30 PM.
> **Đúng:** Giờ làm việc: 08:00 - 17:30.
> **Đúng:** Chuyến bay khởi hành lúc 23:55.

### 3.5 Kết hợp Ngày và Giờ

> 14:30, ngày 25/05/2026
> 08:00 - 17:00, thứ hai đến thứ sáu
> 09:30 sáng ngày 01/01/2026
> 23:59:59, ngày 31/12/2025

### 3.6 Lịch Âm (Lunar Calendar)

Lịch âm vẫn được sử dụng rộng rãi trong đời sống và văn hóa Việt Nam.

**Các ngày lễ âm lịch quan trọng:**
| Lễ | Âm lịch | Ghi chú |
|----|---------|---------|
| Tết Nguyên Đán | Mùng 1 tháng Giêng | Tết cổ truyền, thường cuối tháng 1 - đầu tháng 2 DL |
| Tết Nguyên tiêu | Rằm tháng Giêng | 15/1 AL |
| Giỗ Tổ Hùng Vương | Mùng 10 tháng 3 | 10/3 AL |
| Lễ Phật Đản | Rằm tháng 4 | 15/4 AL (Phật giáo Bắc tông) |
| Tết Đoan Ngọ | Mùng 5 tháng 5 | 5/5 AL |
| Rằm tháng Bảy | 15/7 AL | Lễ Vu Lan (Xá tội vong nhân) |
| Tết Trung Thu | Rằm tháng 8 | 15/8 AL |
| Tết Hàn Thực | Mùng 3 tháng 3 | 3/3 AL |
| Tết Trùng Cửu | Mùng 9 tháng 9 | 9/9 AL |
| Tết Trùng Thập | Mùng 10 tháng 10 | 10/10 AL |
| Tết Hạ Nguyên | Rằm tháng 10 | 15/10 AL |
| Tết Ông Táo | 23 tháng Chạp | 23/12 AL |

**Quy tắc dịch:**
- Khi đề cập ngày âm lịch, ghi rõ "(âm lịch)" hoặc "AL".
- Có thể ghi kèm ngày dương lịch tương ứng trong ngoặc.
- Tên tháng âm lịch: tháng Giêng (1), tháng Chạp (12).

**Ví dụ:**
> Tết Nguyên Đán năm 2026 rơi vào ngày 17/02/2026 (mùng 1 tháng Giêng năm Bính Ngọ).
> Rằm tháng Tám (Trung Thu) là ngày 15/8 âm lịch hàng năm.
> Lễ Vu Lan diễn ra vào rằm tháng Bảy âm lịch.

### 3.7 Năm và Thế kỷ

| VI | English |
|----|---------|
| năm 2026 | 2026 |
| thế kỷ XXI | 21st century |
| thập niên 2020 | 2020s |
| những năm 1990 | the 1990s |
| trước Công nguyên (TCN) | BC |
| sau Công nguyên (SCN) | AD |
| thập kỷ 80 | the 80s |

**Quy tắc:**
- Năm viết đầy đủ 4 chữ số (không viết '26 thay cho 2026).
- Thế kỷ dùng số La Mã (XXI) hoặc số Ả Rập (thế kỷ 21).

### 3.8 Múi giờ (Time Zones)

> Giờ Việt Nam (GMT+7) — ICT (Indochina Time).
> Chênh lệch: sớm hơn UTC 7 tiếng.
> Không có giờ mùa hè (DST) ở Việt Nam.

**Ví dụ:**
> 09:00 (GMT+7) / 02:00 (UTC)
> 14:30 giờ Việt Nam (tương ứng 07:30 GMT)
> Hạn chót: 23:59 (giờ Việt Nam)

---

## 4. Địa chỉ (Addresses)

### 4.1 Cấu trúc địa chỉ Việt Nam

Thứ tự địa chỉ Việt Nam đi từ **nhỏ đến lớn** (ngược với phương Tây):

```
Số nhà → Ngõ/Hẻm → Đường/Phố → Phường/Xã → Quận/Huyện → Tỉnh/Thành phố
```

| Thành phần | Tiếng Việt | English Equivalent |
|------------|------------|-------------------|
| Số nhà | Số 12 | No. 12 |
| Ngõ/Hẻm | Ngõ 34 | Alley 34 |
| Ngách | Ngách 5 | Sub-alley 5 |
| Đường/Phố | Đường Láng Hạ / Phố Huế | Street |
| Tổ dân phố/Khu phố | Tổ 7 | Residential cluster |
| Phường | Phường Kim Mã | Ward |
| Xã | Xã Dương Xá | Commune |
| Quận | Quận Đống Đa | District |
| Huyện | Huyện Gia Lâm | Rural District |
| Thị xã | Thị xã Sơn Tây | Town |
| Thành phố trực thuộc tỉnh | Thành phố Bắc Ninh | Provincial City |
| Thành phố trực thuộc trung ương | Thành phố Hồ Chí Minh | Municipality |
| Tỉnh | Tỉnh Thừa Thiên Huế | Province |

### 4.2 Ví dụ địa chỉ đầy đủ

**Ví dụ 1 — Nội thành Hà Nội:**
```
Số 12, Ngõ 34, Phố Huế,
Phường Phố Huế, Quận Hai Bà Trưng,
Thành phố Hà Nội
```

**Ví dụ 2 — Ngoại thành:**
```
Số 5, Đường Ỷ Lan,
Xã Dương Xá, Huyện Gia Lâm,
Thành phố Hà Nội
```

**Ví dụ 3 — Thành phố Hồ Chí Minh:**
```
Số 123, Đường Lê Lợi,
Phường Bến Nghé, Quận 1,
Thành phố Hồ Chí Minh
```

**Ví dụ 4 — Tỉnh lẻ:**
```
Số 45, Đường Trần Hưng Đạo,
Xã Ninh Phong, Thành phố Ninh Bình,
Tỉnh Ninh Bình
```

### 4.3 Dạng viết gọn địa chỉ

**Ví dụ:**
> 12 Ngõ 34 Phố Huế, Hai Bà Trưng, Hà Nội
> 123 Lê Lợi, P. Bến Nghé, Q.1, TP.HCM
> 45 Trần Hưng Đạo, Ninh Bình

**Viết tắt phổ biến:**
| Đầy đủ | Viết tắt |
|--------|----------|
| Phường | P. |
| Quận | Q. |
| Thành phố | TP. |
| Thành phố Hồ Chí Minh | TP.HCM |
| Hà Nội | HN |
| Đường | Đ. |

### 4.4 Dịch địa chỉ từ tiếng nước ngoài sang tiếng Việt

Khi dịch địa chỉ nước ngoài sang tiếng Việt, giữ nguyên thứ tự của ngôn ngữ nguồn nhưng dịch các thành phần địa chỉ.

**Ví dụ:**
> **EN:** 123 Main Street, Apt 4B, New York, NY 10001, USA
> **VI:** Số 123, Đường Main, Căn hộ 4B, New York, NY 10001, Hoa Kỳ

> **EN:** 10 Downing Street, London, SW1A 2AA, United Kingdom
> **VI:** Số 10, Phố Downing, Luân Đôn, SW1A 2AA, Vương quốc Anh

**Quy tắc:**
- Dịch tên loại đường/phố (Street → Đường/Phố).
- Giữ nguyên tên riêng (Main Street → Đường Main, không dịch thành "Đường Chính").
- Giữ nguyên mã bưu chính.
- Dịch tên quốc gia.

### 4.5 Bưu chính (Postal)

Mã bưu chính Việt Nam gồm 5-6 chữ số:
- Hà Nội: 10xxxx
- TP. Hồ Chí Minh: 70xxxx
- Đà Nẵng: 50xxxx

---

## 5. Danh từ Riêng (Proper Nouns)

### 5.1 Tên người Việt Nam

Thứ tự tên người Việt: **Họ + Tên đệm + Tên chính**

| Họ | Tên đệm | Tên chính |
|----|---------|-----------|
| Nguyễn | Văn | A |
| Trần | Thị | Bích |
| Lê | Quang | Minh |
| Phạm | | Hùng |
| Hoàng | Thị | Mai |
| Vũ | Đình | Long |
| Đặng | | Thu Thủy |
| Bùi | Xuân | Trường |

**Ví dụ đầy đủ:**
> Ông **Nguyễn Văn A** — Mr. Nguyen Van A
> Bà **Trần Thị Bích** — Mrs. Tran Thi Bich
> Anh **Lê Quang Minh** — Mr. Le Quang Minh
> Chị **Phạm Hùng** — Ms. Pham Hung

**Quy tắc viết hoa:**
- Viết hoa chữ cái đầu của mỗi thành phần tên.
- Giữ nguyên dấu thanh trong mọi ngữ cảnh.
- Không tách tên đệm ghép: "Thị", "Văn", "Đình" viết riêng.

**Dấu cách và tên đệm:**
- Tên đệm luôn cách biệt bằng khoảng trắng.
- Tên có thể gồm 2 âm tiết: "Thu Thủy", "Minh Anh", "Phương Linh".

### 5.2 Xưng hô và danh xưng

| Danh xưng | Sử dụng |
|-----------|---------|
| Ông | Nam, lớn tuổi, trang trọng |
| Bà | Nữ, lớn tuổi, trang trọng |
| Anh | Nam, ngang hàng hoặc lớn hơn một chút |
| Chị | Nữ, ngang hàng hoặc lớn hơn một chút |
| Em | Người nhỏ tuổi hơn |
| Cô | Nữ, trẻ hoặc trung niên (miền Nam) |
| Chú | Nam, trung niên (miền Nam) |
| Thầy | Thầy giáo, bác sĩ (miền Nam) |
| Bác | Người lớn tuổi hơn cha mẹ |

### 5.3 Tên nước ngoài phiên âm sang tiếng Việt

Quy tắc phiên âm: giữ nguyên âm gần nhất với âm gốc, thêm dấu thanh phù hợp.

**Tên người nước ngoài:**
| English | VI phiên âm | Ghi chú |
|---------|-------------|---------|
| John | John (không phiên âm) | Tên phổ biến giữ nguyên |
| Michael | Michael | Giữ nguyên |
| Elizabeth | Elizabeth | Giữ nguyên |
| Christopher | Christopher | Giữ nguyên |
| Donald Trump | Donald Trump | Giữ nguyên trong văn bản thông thường |
| Vladimir Putin | Vladimir Putin | Giữ nguyên |
| Paris | Pa-ri | Phiên âm khi nói về thành phố |
| London | Luân Đôn | Phiên âm lịch sử |
| New York | Niu Oóc (Niu Yoóc) | Phiên âm / giữ nguyên |
| Washington | Oa-sinh-tơn | Phiên âm |
| California | Ca-li-phoóc-ni-a | Phiên âm |
| Tokyo | Tô-ki-ô | Phiên âm |

**Quy tắc hiện đại:**
- Tên người nước ngoài trong văn bản thông thường: **giữ nguyên bản gốc**.
- Tên địa danh nước ngoài: ưu tiên phiên âm nếu có truyền thống.
- Tên tổ chức/công ty: giữ nguyên tên gốc.
- Dùng dấu gạch nối cho tên phiên âm đa âm tiết: Oa-sinh-tơn, Luân Đôn.

### 5.4 Tên tổ chức và công ty

| English | VI |
|---------|-----|
| United Nations | Liên Hợp Quốc (LHQ) |
| World Bank | Ngân hàng Thế giới (WB) |
| International Monetary Fund | Quỹ Tiền tệ Quốc tế (IMF) |
| World Health Organization | Tổ chức Y tế Thế giới (WHO) |
| Microsoft Corporation | Tập đoàn Microsoft |
| Apple Inc. | Công ty Apple |

**Quy tắc:**
- Tên tổ chức quốc tế có bản dịch chuẩn bằng tiếng Việt.
- Tên công ty: giữ nguyên tên gốc, dịch loại hình (Inc. → Công ty, Corporation → Tập đoàn).
- Có thể kèm tên gốc trong ngoặc đơn lần đầu xuất hiện.

### 5.5 Tên địa danh trong nước

**Viết hoa:**
- Tên tỉnh/thành phố: Thành phố Hồ Chí Minh, Hà Nội, Đà Nẵng
- Tên quận/huyện: Quận 1, Quận Đống Đa, Huyện Gia Lâm
- Tên phường/xã: Phường Bến Nghé, Xã Dương Xá
- Tên đường: Đường Láng Hạ, Phố Huế

**Địa danh ghép:**
> Hồ Chí Minh, Hà Nội, Đà Nẵng (mỗi âm tiết viết hoa)
> Buôn Ma Thuột, Nha Trang, Vũng Tàu
> Sapa, Tam Đảo, Cát Bà

### 5.6 Quy tắc chuyển ngữ đặc biệt

**Các trường hợp ngoại lệ:**
| Gốc | Phiên âm cũ | Phiên âm mới (khuyến nghị) |
|-----|-------------|---------------------------|
| Korea | Cao Ly → Hàn Quốc | Hàn Quốc (Nam), Triều Tiên (Bắc) |
| Taiwan | Đài Loan | Đài Loan |
| Japan | Nhật Bản | Nhật Bản |
| Thailand | Thái Lan | Thái Lan |
| France | Pháp | Pháp |
| Germany | Đức | Đức |
| Russia | Nga | Nga |
| China | Trung Quốc | Trung Quốc |
| England | Anh | Anh |
| United States | Mỹ | Mỹ / Hoa Kỳ |

**Quy tắc:** Sử dụng tên phiên âm Hán-Việt cho các quốc gia có truyền thống lịch sử. Giữ nguyên tên gốc cho các quốc gia hiện đại mới.

---

## 6. Dấu câu (Punctuation)

### 6.1 Dấu chấm (Period - .)

- Kết thúc câu trần thuật.
- Dùng trong viết tắt: v.v., vân vân, T.Ư (Trung ương), NXB (Nhà xuất bản).
- Dấu phân cách hàng nghìn trong số.

> Việt Nam là một quốc gia Đông Nam Á.
> Các nguyên liệu gồm: gạo, thịt, rau, v.v.
> Dân số: 100.000.000 người.

**Quy tắc:** Không dùng dấu chấm trước dấu ngoặc kép hoặc dấu ngoặc đơn đóng (trừ khi là câu riêng biệt).

### 6.2 Dấu phẩy (Comma - ,)

- Ngăn cách các thành phần trong liệt kê.
- Ngăn cách mệnh đề trong câu.
- **Không** dùng trước "và" trong liệt kê đơn giản (khác với tiếng Anh - Oxford comma).

| VI | EN |
|----|-----|
| Táo, cam, chuối và nho | Apples, oranges, bananas, and grapes |
| Học sinh, sinh viên và giáo viên | Students, teachers, and staff |

**Quy tắc:**
- Không dùng dấu phẩy trước "và" (tương tự tiếng Pháp, khác với tiếng Anh).
- Dùng dấu phẩy để ngăn cách mệnh đề dài.
- Dấu phẩy thập phân: 3,14 (không phải 3.14).

### 6.3 Dấu hai chấm (Colon - :)

- Giới thiệu danh sách, trích dẫn, giải thích.
- Trước danh sách: "Các mặt hàng bao gồm: ..."
- Trong tỷ lệ: "Tỷ lệ 3:1"

> Có ba nguyên tắc cơ bản: thứ nhất..., thứ hai..., thứ ba...

### 6.4 Dấu chấm phẩy (Semicolon - ;)

- Ngăn cách các mệnh đề độc lập có liên quan chặt chẽ.
- Ngăn cách các phần tử trong liệt kê phức tạp (có chứa dấu phẩy nội bộ).

> Hội thảo diễn ra tại Hà Nội; hội nghị tại Đà Nẵng; triển lãm tại TP. Hồ Chí Minh.
> Tham dự có: Nguyễn Văn A, Giám đốc; Trần Thị B, Phó giám đốc; và Lê Văn C, Trưởng phòng.

### 6.5 Dấu ngoặc kép (Quotation Marks)

Tiếng Việt sử dụng nhiều loại dấu ngoặc kép:

| Loại | Ký tự | Sử dụng |
|------|-------|---------|
| Ngoặc kép cong | " " | Phổ biến nhất |
| Ngoặc kép thẳng | " " | Văn bản kỹ thuật |
| Ngoặc nhọn (guillemets) | « » | Văn bản chính quy (ảnh hưởng Pháp) |
| Ngoặc đơn | ' ' | Trích dẫn trong trích dẫn |

**Quy tắc:**
- Dấu ngoặc kép đặt bên ngoài dấu câu (khác với tiếng Anh Mỹ).
- Dấu chấm/dấu phẩy đặt **bên ngoài** dấu ngoặc kép.

> **VI:** Ông ấy nói "Tôi sẽ đến", nhưng đã không xuất hiện.
> **EN (US):** He said, "I will come," but didn't show up.

> **VI:** Tác phẩm "Chiến tranh và Hòa bình" là một kiệt tác.
> **EN (US):** The novel "War and Peace" is a masterpiece.

> **VI:** Anh hỏi: "Em có hiểu không?"; tôi gật đầu.
> **VI (guillemet):** « Đây là văn bản chính quy », tác giả nhấn mạnh.

### 6.6 Dấu gạch ngang (Dash)

Có hai loại gạch ngang trong tiếng Việt:

| Loại | Độ dài | Công dụng |
|------|--------|-----------|
| Dấu gạch nối | - (ngắn) | Từ ghép, phiên âm |
| Dấu gạch ngang | — (dài) | Ngăn cách thành phần chú thích, liệt kê |

**Dấu gạch nối (Hyphen):**
> xe đạp, máy tính, đường sá (từ ghép — không gạch nối)
> Oa-sinh-tơn, Luân Đôn, Tô-ki-ô (phiên âm — có gạch nối)
> các mối quan hệ Việt Nam - Hoa Kỳ (quan hệ song phương)

**Dấu gạch ngang (Em dash):**
> Cô ấy — người phụ nữ tôi yêu thương nhất — đã ra đi.
> Các nội dung chính:
> — Báo cáo tài chính
> — Kế hoạch năm 2026
> — Đề xuất chiến lược

### 6.7 Dấu ngoặc đơn (Parentheses - ())

- Chứa thông tin bổ sung, chú thích.
- Chứa tên gốc khi dịch thuật.

> Việt Nam (tên chính thức: Cộng hòa Xã hội Chủ nghĩa Việt Nam) là một quốc gia ở Đông Nam Á.
> Tổ chức Y tế Thế giới (WHO) công bố báo cáo.

### 6.8 Dấu chấm lửng (Ellipsis - ...)

- Biểu thị sự ngập ngừng, bỏ lửng.
- Độ dài: 3 chấm, không tách rời.

> Anh ấy nói... rồi im lặng...
> Danh sách còn tiếp...

### 6.9 Dấu hỏi và dấu chấm than (? và !)

- Dấu hỏi kết thúc câu hỏi.
- Dấu chấm than kết thúc câu cảm thán, mệnh lệnh.
- Không dùng cả hai (!?) trong văn bản chính quy.

> Bạn có khỏe không?
> Hãy cẩn thận!
> Tuyệt vời!

### 6.10 Khoảng trắng (Spacing)

**Quy tắc:**
- Một khoảng trắng sau dấu câu (phẩy, chấm, hai chấm, chấm phẩy).
- Không khoảng trắng trước dấu phẩy hoặc dấu chấm.
- Một khoảng trắng trước và sau dấu gạch ngang (em dash).

> **Đúng:** Một, hai, ba. Xin chào, bạn khỏe không?
> **Sai:** Một,hai,ba .Xin chào,bạn khỏe không?
> **Đúng:** Hà Nội — thủ đô của Việt Nam — là thành phố sôi động.

---

## 7. Định dạng Văn bản (Formatting)

### 7.1 Viết hoa tiêu đề (Title Case)

Tiếng Việt chủ yếu dùng **viết hoa kiểu câu (sentence case)** cho tiêu đề. **Không** viết hoa mọi từ như tiếng Anh.

| VI đúng (sentence case) | EN (title case) |
|--------------------------|----------------|
| Báo cáo tài chính năm 2026 | 2026 Financial Report |
| Quy trình xử lý đơn hàng | Order Processing Procedure |
| Phân tích thị trường bất động sản | Real Estate Market Analysis |
| Hướng dẫn sử dụng phần mềm | Software User Guide |

**Quy tắc viết hoa:**
- Viết hoa chữ **đầu tiên** của tiêu đề và danh từ riêng.
- Các từ còn lại viết thường (trừ tên riêng, tên tổ chức).

**Ngoại lệ:** Tên sách, tên phim, tên báo có thể viết hoa mọi từ chính (nhưng không bắt buộc).

> **Hoặc:** Chiến Tranh Và Hòa Bình / Chiến tranh và Hòa bình
> **Hoặc:** Số Đỏ / Số đỏ

### 7.2 Phân cấp tiêu đề (Heading Hierarchy)

```
# CHƯƠNG 1 (cấp 1 — Viết hoa toàn bộ cho chương, mục lớn)
## 1.1 Tên mục (cấp 2 — Sentence case)
### 1.1.1 Tên tiểu mục (cấp 3 — Sentence case)
#### (cấp 4 — Sentence case)
```

**Quy tắc:**
- Cấp 1 (tên chương, phần lớn): VIẾT HOA TOÀN BỘ.
- Cấp 2-4: Sentence case (chữ đầu viết hoa).
- Không dùng dấu chấm cuối tiêu đề.

### 7.3 Danh sách (Lists)

**Danh sách có thứ tự (Ordered):**
> 1. Bước thứ nhất
> 2. Bước thứ hai
> 3. Bước thứ ba

**Danh sách không thứ tự (Unordered):**
> - Mục A
> - Mục B
> - Mục C

**Danh sách phức tạp:**
> 1. Chuẩn bị nguyên liệu:
>    - Gạo: 500 gram
>    - Thịt: 200 gram
> 2. Nấu:
>    a) Đun nước sôi
>    b) Cho gạo vào

**Quy tắc dấu câu trong danh sách:**
- Mỗi mục trong danh sách bắt đầu bằng chữ thường (trừ khi là tên riêng).
- Danh sách đơn giản: không dùng dấu chấm phẩy hoặc dấu phẩy cuối mục.
- Dấu chấm chỉ dùng khi mỗi mục là một câu hoàn chỉnh.

### 7.4 Định dạng số trang và mục lục

> Trang 1-100
> Mục A.1, A.2, B.1
> Phụ lục 1, Phụ lục 2
> Chương I, Chương II

### 7.5 Khoảng cách dòng (Line Spacing)

- Văn bản chính quy: giãn dòng 1.5.
- Đoạn văn cách nhau bởi một dòng trống.
- Không thụt đầu dòng trong văn bản kỹ thuật (có thụt trong văn học).

### 7.6 In đậm và in nghiêng (Bold and Italic)

- **In đậm:** nhấn mạnh thuật ngữ lần đầu xuất hiện.
- *In nghiêng:* tên tác phẩm, từ mượn, nhấn mạnh nhẹ.
- Gạch chân: tránh dùng (dễ nhầm với siêu liên kết).

---

## 8. Ngữ pháp (Grammar)

### 8.1 Trật tự từ (Word Order)

Tiếng Việt tuân theo cấu trúc **SVO** (Chủ ngữ - Động từ - Tân ngữ), tương tự tiếng Anh.

> **VI:** Tôi ăn cơm. (S-V-O)
> **EN:** I eat rice. (S-V-O)
> **VI:** Cô ấy đọc sách.
> **EN:** She reads a book.

**Khác biệt quan trọng:**
> **VI:** Tôi cho anh ấy một cuốn sách. (S-V-O1-O2)
> **EN:** I give him a book. (S-V-O1-O2)
> **VI:** Tôi đã ăn cơm rồi.
> **EN:** I have already eaten rice.

### 8.2 Hệ thống Phân loại từ (Classifier System)

Tiếng Việt có hệ thống từ phân loại phong phú. Danh từ cần có từ phân loại khi đếm.

**Bảng từ phân loại chính:**

| Từ | Loại | Ví dụ | English |
|----|------|-------|---------|
| **cái** | Vật thể vô tri (trừu tượng, vật dụng) | cái bàn, cái ghế, cái nhà | (general object classifier) |
| **con** | Động vật, người (nghĩa bóng), đồ vật có hình dạng con vật | con chó, con mèo, con người, con tàu, con đường, con dao | (animal/elongated object classifier) |
| **chiếc** | Vật dụng nhỏ, phương tiện, đồ dùng cá nhân | chiếc xe, chiếc áo, chiếc bút, chiếc nhẫn, chiếc thuyền | (vehicle/small item classifier) |
| **quyển/cuốn** | Sách, vở, tài liệu đóng quyển | quyển sách, cuốn vở, quyển từ điển | (book/volume classifier) |
| **tờ** | Giấy tờ, tài liệu mỏng | tờ báo, tờ giấy, tờ đơn | (sheet/paper classifier) |
| **bức** | Tranh, ảnh, thư từ | bức tranh, bức ảnh, bức thư | (picture/letter classifier) |
| **ngôi** | Nhà, sao | ngôi nhà, ngôi sao | (building/star classifier) |
| **cây** | Thực vật, vật thể hình cột | cây bút (miền Nam), cây đàn, cây cột | (plant/upright classifier) |
| **tòa** | Cao ốc, tòa án | tòa nhà, tòa soạn | (building complex classifier) |
| **viên** | Viên nhỏ (thuốc, đá quý) | viên thuốc, viên kim cương | (small round classifier) |
| **sợi** | Sợi dài, mảnh | sợi dây, sợi tóc | (thread-like classifier) |
| **hạt** | Hạt nhỏ | hạt gạo, hạt cát, hạt đậu | (grain classifier) |
| **miếng** | Mảnh nhỏ | miếng bánh, miếng thịt | (piece classifier) |
| **tấm** | Tấm phẳng | tấm ảnh, tấm bản đồ, tấm lòng | (flat object classifier) |
| **lá** | Lá cây, vật thể hình lá | lá cờ, lá thư, lá bài | (leaf classifier) |
| **quả / trái** | Quả, vật hình cầu | quả bóng, trái cam | (fruit/round classifier) |

**Ví dụ đầy đủ:**
> **Đúng:** Một **cái** bàn, hai **con** chó, ba **chiếc** xe.
> **Sai:** Một bàn, hai chó, ba xe.
> **Đúng:** Tôi mua **một quyển** sách và **hai chiếc** bút.
> **Sai:** Tôi mua một sách và hai bút.

**Biến thể vùng miền:**
> **Miền Bắc:** quả cam, quả bóng
> **Miền Nam:** trái cam, trái bóng
> **Miền Bắc:** cái bút, cốc nước
> **Miền Nam:** cây bút, ly nước

### 8.3 Hệ thống Đại từ (Pronoun System)

Tiếng Việt có hệ thống đại từ phức tạp dựa trên tuổi tác, địa vị và mức độ thân mật.

**Đại từ nhân xưng chính:**

| Ngôi | Formal | Informal | Ghi chú |
|------|--------|----------|---------|
| Tôi (I) | Tôi | Tớ, mình | "Tôi" trung tính, "Tớ" thân mật |
| Bạn (you-sg) | Quý ông / Quý bà | Bạn, cậu | "Quý ông/bà" rất trang trọng |
| Anh ấy (he) | Ông ấy | Anh ấy, cậu ấy | |
| Cô ấy (she) | Bà ấy | Cô ấy | |
| Chúng tôi (we, exclusive) | Chúng tôi | Tụi tớ, bọn mình | "Chúng tôi" trừ người nghe |
| Chúng ta (we, inclusive) | Chúng ta | Tụi mình, bọn mình | Bao gồm người nghe |
| Các bạn (you-pl) | Quý vị | Các bạn, mọi người | |
| Họ (they) | Quý vị ấy | Họ, tụi nó | |

**Bảng tham chiếu đầy đủ:**

| Người nói → Người nghe | Đại từ | Ví dụ |
|------------------------|--------|-------|
| Trẻ → Lớn tuổi hơn | Cháu → Ông/Bà/Cô/Chú | Cháu chào bác ạ! |
| Lớn → Trẻ hơn | Anh/Chị → Em | Em đi đâu đấy? |
| Ngang hàng, thân | Tớ → Cậu | Cậu khỏe không? |
| Ngang hàng, xa | Tôi → Anh/Chị | Anh làm ơn giúp tôi. |
| Cấp dưới → Cấp trên | Tôi/Em → Anh/Chị | Em báo cáo anh... |
| Rất trang trọng | Tôi → Quý ông/Quý bà | Thưa quý ông... |

### 8.4 Không có biến tố (No Conjugation)

Tiếng Việt không có biến tố (không chia động từ theo thì, ngôi, số). Thì được biểu thị bằng từ chỉ thời gian và trợ từ.

> **EN:** I eat / He eats / I ate / I have eaten / I will eat
> **VI:** Tôi ăn / Anh ấy ăn (giống nhau)
> **VI quá khứ:** Tôi **đã** ăn
> **VI hiện tại:** Tôi **đang** ăn
> **VI tương lai:** Tôi **sẽ** ăn
> **VI hoàn thành:** Tôi **đã** ăn **rồi**

**Trợ từ thời gian:**
| Trợ từ | Chức năng | Ví dụ |
|--------|-----------|-------|
| đã | Quá khứ | Tôi đã đến. (I arrived.) |
| đang | Hiện tại tiếp diễn | Tôi đang học. (I am studying.) |
| sẽ | Tương lai | Tôi sẽ đi. (I will go.) |
| rồi | Hoàn thành | Tôi làm rồi. (I have done it.) |
| chưa | Phủ định / Chưa hoàn thành | Tôi chưa ăn. (I haven't eaten yet.) |
| từng | Từng trải | Tôi từng sống ở đó. (I have lived there before.) |
| sắp | Sắp xảy ra | Tôi sắp đi. (I am about to go.) |

### 8.5 Hệ thống Thanh điệu (Tone System)

Tiếng Việt có **6 thanh điệu** (ở phương ngữ Bắc Bộ):

| # | Tên thanh | Ký hiệu | Âm điệu | Ví dụ | Ý nghĩa |
|---|-----------|---------|---------|-------|---------|
| 1 | Ngang | (không dấu) | Cao, đều | ma | ma (ghost) |
| 2 | Huyền | \` | Thấp, giáng | mà | mà (but/that) |
| 3 | Sắc | ´ | Cao, lên | má | má (mother/cheek) |
| 4 | Hỏi | ̉ | Xuống-lên | mả | mả (grave/tomb) |
| 5 | Ngã | ˜ | Lên gãy | mã | mã (code/horse) |
| 6 | Nặng | ˀ | Thấp, nặng | mạ | mạ (rice seedling) |

**Các cặp từ dễ nhầm lẫn do sai dấu:**
> **bán** (sell) vs **bàn** (table/desk) vs **bản** (version) vs **bạn** (friend) vs **ban** (committee)
> **cà** (eggplant) vs **cả** (all/big) vs **cá** (fish) vs **cạ** (side)
> **má** (mother) vs **mà** (that) vs **mả** (grave) vs **mã** (code)
> **cơm** (rice) vs **cốm** (young rice) vs **cỏm** (money, slang)
> **học** (study) vs **hóc** (stuck) vs **hò** (chant) vs **hồ** (pond/paste)
> **tử** (death/Confucian scholar) vs **tứ** (four) vs **tư** (thought/private)

**Quy tắc:**
- Sai dấu thanh làm thay đổi hoàn toàn nghĩa của từ — **lỗi nghiêm trọng**.
- Luôn kiểm tra dấu thanh khi dịch.
- Các công cụ kiểm tra chính tả tiếng Việt phải được bật.

### 8.6 Từ láy (Reduplication)

Tiếng Việt sử dụng phổ biến từ láy để nhấn mạnh hoặc tạo sắc thái.

| Từ láy | Loại | Nghĩa |
|--------|------|-------|
| xanh xanh | Giảm nhẹ | Hơi xanh |
| đỏ đỏ | Giảm nhẹ | Hơi đỏ |
| sạch sành sanh | Nhấn mạnh | Rất sạch |
| đo đỏ | Giảm nhẹ | Hơi đỏ |
| linh tinh | Từ láy vần | Linh tinh |
| lung linh | Từ láy âm | Lung linh |
| nhỏ nhắn | Từ láy vần | Nhỏ nhắn, xinh xắn |

### 8.7 Câu phủ định (Negation)

> **VI:** Tôi **không** đi. (I am not going.)
> **VI:** Anh ấy **chưa** đến. (He hasn't arrived yet.)
> **VI:** Đừng làm việc đó! (Don't do that!)
> **VI:** Chẳng có gì. (There's nothing.)

| Từ phủ định | Mức độ | Ví dụ |
|-------------|--------|-------|
| không | Trung tính | Tôi không biết. |
| chưa | Chưa xảy ra | Tôi chưa ăn. |
| chẳng | Nhấn mạnh | Tôi chẳng muốn. |
| đừng | Cấm đoán | Đừng đi! |
| chớ | Cấm đoán (nhẹ) | Chớ lo. |

### 8.8 Câu hỏi (Questions)

> **VI:** Bạn có khỏe không? (Are you well?)
> **VI:** Anh ấy đã đến chưa? (Has he arrived?)
> **VI:** Ai đã làm việc này? (Who did this?)
> **VI:** Cái gì đây? (What is this?)
> **VI:** Tại sao? (Why?)
> **VI:** Ở đâu? (Where?)
> **VI:** Khi nào? (When?)
> **VI:** Bao nhiêu? (How much/many?)

**Cấu trúc câu hỏi có/không:**
> S + có + V + không?
> Bạn có thích không? (Do you like it?)
> Anh có đi không? (Are you going?)

### 8.9 Lượng từ (Quantifiers)

| Từ | Cách dùng | Ví dụ |
|----|-----------|-------|
| những | Số nhiều xác định | Những người bạn |
| các | Số nhiều tổng quát | Các học sinh |
| mọi | Tất cả (mỗi) | Mọi người |
| mỗi | Từng cái một | Mỗi ngày |
| từng | Từng cái riêng lẻ | Từng người một |
| vài | Một vài | Vài hôm nữa |
| nhiều | Số lượng lớn | Nhiều người |
| ít | Số lượng nhỏ | Ít khi |

---

## 9. Nghi thức Xã giao (Formality)

### 9.1 Hệ thống kính ngữ (Honorifics)

Tiếng Việt không có kính ngữ ngữ pháp như tiếng Nhật hay Hàn, nhưng có hệ thống xưng hô phức tạp phản ánh thứ bậc xã hội.

**Thang đo mức độ trang trọng:**

```
Thân mật (thấp) ←———→ Trang trọng (cao)
tớ/cậu → mày/tao → bạn → anh/chị → ông/bà → quý ông/quý bà → ngài
```

### 9.2 Đại từ trang trọng (Formal Pronouns)

| Hoàn cảnh | Đại từ | Ví dụ |
|-----------|--------|-------|
| Văn bản hành chính | Tôi → Quý ông/Bà | Tôi xin gửi đến Quý ông... |
| Hợp đồng | Bên A → Bên B | Bên A cam kết... |
| Thư từ ngoại giao | Ngài | Thưa Ngài Đại sứ... |
| Bài phát biểu | Thưa quý vị | Thưa quý vị đại biểu... |
| Khách hàng | Quý khách | Quý khách vui lòng... |
| Cấp trên | Tôi/Em → Anh/Chị | Em xin phép anh... |
| Hội nghị | Quý vị | Kính thưa quý vị... |

### 9.3 Kính ngữ trong văn bản chính quy

**Công văn, văn bản hành chính:**
> Kính gửi: Quý Ông/Bà
> Trân trọng kính mời...
> Kính chào Quý khách...
> Xin trân trọng cảm ơn...

**Thư từ thương mại:**
> Kính gửi Quý Công ty,
> Chúng tôi xin trân trọng thông báo...
> Rất mong nhận được sự phản hồi của Quý vị.
> Trân trọng,

**Biên bản, hợp đồng:**
> Các bên tham gia hợp đồng...
> Bên A có nghĩa vụ...
> Điều khoản này có hiệu lực kể từ ngày ký.

### 9.4 Từ ngữ trang trọng và thông tục

| Trang trọng (Formal) | Thông tục (Informal) | English |
|----------------------|----------------------|---------|
| tử vong | chết | die/death |
| phụ nữ có thai | bà bầu | pregnant woman |
| sử dụng | dùng | use |
| thực hiện | làm | do/perform |
| tiến hành | làm | conduct |
| cung cấp | cho | provide |
| hỗ trợ | giúp | support/help |
| thông báo | báo | notify |
| triển khai | làm | deploy/implement |
| giải trình | giải thích | explain |
| đề xuất | đề nghị | propose |
| Ủy ban Nhân dân | UBND | People's Committee |
| Hội đồng Nhân dân | HĐND | People's Council |

### 9.5 Văn phong theo thể loại (Register by Genre)

**Văn bản pháp luật:**
> **Điều 1.** Phạm vi điều chỉnh...
> Căn cứ Luật... ngày... tháng... năm...
> ...có hiệu lực thi hành kể từ ngày...

**Báo chí:**
> Theo thông tin từ... ngày... cho biết...
> Được biết,...
> Theo ghi nhận của phóng viên,...

**Học thuật:**
> Bài báo này phân tích...
> Kết quả nghiên cứu cho thấy...
> Có thể thấy rằng...
> Tác giả cho rằng...

**Thương mại / Quảng cáo:**
> Khám phá bộ sưu tập mới...
> Giải pháp toàn diện cho...
> Chất lượng hàng đầu...

### 9.6 Các biểu thức lịch sự (Polite Expressions)

| VI | English Context |
|----|-----------------|
| Làm ơn... | Please (general) |
| Vui lòng... | Please (formal) |
| Xin mời... | Please (invitation) |
| Cảm ơn | Thank you |
| Cảm ơn trước | Thank you in advance |
| Xin lỗi | Sorry / Excuse me |
| Xin phép | May I... |
| Kính thưa | Dear (very formal) |
| Trân trọng | Respectfully / Sincerely |
| Kính chúc | Respectfully wish |
| Thưa | Sir/Madam (beginning address) |
| Dạ vâng | Yes (respectful) |
| Dạ không | No (respectful) |

**Ví dụ:**
> Làm ơn cho tôi hỏi... (May I ask...)
> Vui lòng ký vào đây. (Please sign here.)
> Xin mời ông vào. (Please come in, sir.)
> Kính chúc quý vị sức khỏe. (Wishing you good health.)

### 9.7 Quy tắc "Dạ" và "Thưa" trong văn nói và viết

- "Dạ" và "Thưa" thường xuất hiện trong văn nói trang trọng hoặc thư từ.
- Trong văn bản viết chính quy, hạn chế "dạ", "thưa" trừ các trường hợp:
  - Thư từ cá nhân trang trọng.
  - Lời chúc, lời mời.
  - Văn bản hành chính có yếu tố cá nhân.

---

## 10. Hiện vật OCR (OCR Artifacts)

### 10.1 Các lỗi OCR thường gặp trong tiếng Việt

Do dấu thanh và ký tự đặc biệt, OCR tiếng Việt thường mắc các lỗi sau:

| Sai (OCR) | Đúng | Loại lỗi |
|-----------|------|----------|
| da | đã | Mất dấu |
| co | có | Mất dấu sắc |
| phu | phụ | Mất dấu nặng |
| ca | cả | Mất dấu hỏi |
| d8 | đã | Ký tự lỗi |
| 1.234,56 | 1.234,56 | Số bị lẫn |
| diroc | được | Lỗi ký tự |
| trong | trong | (đúng) |
| trien khai | triển khai | Mất dấu |
| cai | cái/cải/cạy | Nhập nhằng dấu |
| ntn | như thế nào | Viết tắt |
| & | và | Ký hiệu |

### 10.2 Quy trình phục hồi

Khi phát hiện lỗi OCR, sử dụng định dạng `[đã phục hồi: ...]` để ghi lại bản sửa.

| Lỗi OCR | Phục hồi | Giải thích |
|---------|-----------|------------|
| da co ket qua | đã [đã phục hồi: có] kết quả | Mất dấu sắc |
| duoc xac nhan | [đã phục hồi: được] xác nhận | Mất dấu nặng |
| tong so la 1000 | tổng số là [đã phục hồi: 1.000] | Thiếu dấu phân cách nghìn |
| ngay 1/1/2026 | ngày [đã phục hồi: 01/01/2026] | Chuẩn hóa định dạng ngày |
| ho ten: nguyen van a | họ tên: [đã phục hồi: Nguyễn Văn A] | Viết hoa và dấu |
| gia: 12.5 usd | giá: [đã phục hồi: 12,5 USD] | Dấu thập phân và ISO |
| 3.141592 | [đã phục hồi: 3,141592] | Sai dấu thập phân |
| 2:30 PM | [đã phục hồi: 14:30] | Đổi sang 24h |

### 10.3 Các trường hợp giới hạn

**Không phục hồi nếu không chắc chắn:**
> [!NOTE]
> Chỉ áp dụng `[đã phục hồi: ...]` khi có độ chắc chắn cao.
> Nếu nghi ngờ, để nguyên và ghi chú `[cần kiểm tra]`.

**Ví dụ về ghi chú kiểm tra:**
> Số tiền là 1.500.000 [cần kiểm tra: không rõ đơn vị tiền tệ].
> Ngày tháng: [cần kiểm tra: không đọc được].

### 10.4 Định dạng chuẩn của ghi chú phục hồi

```
[đã phục hồi: <giá trị đã sửa>]
```

- **Luôn dùng dấu ngoặc vuông** `[]`.
- **Luôn bắt đầu bằng** `đã phục hồi:` (chữ thường, không dấu cách đầu).
- **Luôn kết thúc bằng dấu đóng ngoặc** `]`.
- Nội dung bên trong viết đúng chính tả và dấu câu.

### 10.5 Tích lũy lỗi OCR phổ biến

| Ký tự gốc | Lỗi OCR phổ biến |
|-----------|------------------|
| đ | d, d8, cl |
| ơ | o, o7 |
| ư | u, u7 |
| â | a, aa |
| ê | e, ee |
| ô | o, oo |
| á | a, a' |
| à | a, a\` |
| ả | a, a? |
| ã | a, a~ |
| ạ | a, a. |
| dấu cách | bị mất trong scan |

### 10.6 Kiểm tra sau OCR

Checklist:
- [ ] Tất cả dấu thanh đã được khôi phục.
- [ ] Ký tự `đ` và `Đ` đã được kiểm tra.
- [ ] Ngày tháng đã chuyển sang định dạng DD/MM/YYYY.
- [ ] Số thập phân đã dùng dấu phẩy.
- [ ] Tên riêng đã viết hoa và đánh dấu đúng.
- [ ] Dấu câu đã được chuẩn hóa.

---

## 11. Triết lý Dịch thuật (Translation Philosophy)

### 11.1 Nguyên tắc cốt lõi

**1. Trung thành với ý nghĩa, tự nhiên trong diễn đạt**
> Dịch ý, không dịch từ. Câu văn tiếng Việt phải nghe tự nhiên.

**2. Ưu tiên sự rõ ràng, tránh mơ hồ**
> Văn phong khoa học, chính xác, không tối nghĩa.

**3. Tôn trọng phong cách ngôn ngữ nguồn**
> Giữ giọng điệu (trang trọng/thân mật/kỹ thuật/sáng tạo) của văn bản gốc.

### 11.2 Tránh Chữ Nôm (Avoid Chữ Nôm)

Chữ Nôm (Hán-Nôm) không được khuyến khích trong văn bản tiếng Việt hiện đại.

**Không dùng:**
> Các từ Hán-Nôm xa lạ, cổ xưa.
> Các biểu tượng chữ Nôm (𠊚, 𡗶, v.v.).

**Thay thế bằng:**
> Tiếng Việt thuần (pure Vietnamese) hoặc từ Hán-Việt thông dụng.

**Ví dụ:**
> **Tránh:** Thiền sư thuyết pháp về "vô thường" và "nhân quả" (quá nhiều từ Hán-Việt khó).
> **Nên:** Thiền sư giảng về sự vô thường và luật nhân quả (dùng từ phổ thông).

### 11.3 Từ Hán-Việt vs. Tiếng Việt thuần (Sino-Vietnamese vs. Pure Vietnamese)

**Nguyên tắc chung:**
- Sử dụng từ Hán-Việt khi cần độ chính xác kỹ thuật/pháp lý.
- Sử dụng tiếng Việt thuần khi muốn gần gũi, dễ hiểu.
- Cân bằng hai yếu tố tùy theo đối tượng và thể loại.

**Bảng so sánh:**

| Từ Hán-Việt | Tiếng Việt thuần | Ngữ cảnh sử dụng |
|-------------|-------------------|------------------|
| bệnh nhân | người bệnh | H-V: y khoa; Thuần: thân thiện |
| khảo sát | điều tra, xem xét | H-V: nghiên cứu; Thuần: đời thường |
| chẩn đoán | đoán bệnh | H-V: y khoa |
| điều trị | chữa bệnh | H-V: chuyên môn; Thuần: thông thường |
| thẩm mỹ | đẹp, làm đẹp | H-V: chuyên ngành; Thuần: đời thường |
| trí tuệ nhân tạo | thông minh nhân tạo (ít dùng) | H-V: tiêu chuẩn |
| khuyến mãi | giảm giá, tặng kèm | H-V: thương mại; Thuần: thông thường |
| hội nhập | nhập chung, hòa nhập | H-V: tiêu chuẩn |
| phát triển bền vững | phát triển lâu dài | H-V: tiêu chuẩn quốc tế |
| đại biểu | người thay mặt | H-V: hành chính; Thuần: dễ hiểu |
| hạ tầng | cơ sở vật chất | H-V: kỹ thuật |
| giải pháp | cách giải quyết | H-V: phổ biến; Thuần: giải thích |
| tiêu chuẩn | chuẩn mực | H-V: kỹ thuật; Thuần: đời thường |
| hợp tác | cùng làm | H-V: trang trọng; Thuần: thân mật |

**Ví dụ áp dụng:**

> **Văn bản kỹ thuật (ưu tiên Hán-Việt):**
> Hệ thống trí tuệ nhân tạo được triển khai để tối ưu hóa quy trình sản xuất, giảm thiểu chi phí vận hành và nâng cao năng suất lao động.

> **Văn bản phổ thông (ưu tiên thuần Việt):**
> Máy móc thông minh được đưa vào dùng để làm cho việc sản xuất nhanh hơn, tốn ít chi phí hơn và làm ra nhiều sản phẩm hơn.

> **Cân bằng (khuyến nghị):**
> Hệ thống trí tuệ nhân tạo giúp sản xuất nhanh hơn, giảm chi phí và tăng năng suất.

### 11.4 Cân bằng từ Hán-Việt (Managing Sino-Vietnamese Vocabulary)

**Khi nào ưu tiên Hán-Việt:**
- Thuật ngữ pháp lý, hợp đồng: "hợp đồng", "nghĩa vụ", "quyền lợi", "điều khoản"
- Thuật ngữ khoa học, kỹ thuật: "phân tích", "đánh giá", "môi trường"
- Thuật ngữ y khoa: "chẩn đoán", "phẫu thuật", "bệnh lý"
- Tên tổ chức: "Bộ Y tế", "Ủy ban Nhân dân"
- Văn bản chính quy: "trân trọng kính mời", "công văn số..."

**Khi nào ưu tiên thuần Việt:**
- Giao tiếp hàng ngày, văn bản phổ thông.
- Nội dung cho trẻ em, học sinh.
- Quảng cáo, tiếp thị (gần gũi, dễ nhớ).
- Văn học, sáng tạo (cảm xúc tự nhiên).

**Mức độ Hán-Việt theo thể loại:**
| Thể loại | % Hán-Việt | % Thuần Việt |
|----------|-------------|---------------|
| Pháp luật/Hành chính | 60-70% | 30-40% |
| Khoa học/Kỹ thuật | 50-60% | 40-50% |
| Kinh tế/Tài chính | 45-55% | 45-55% |
| Báo chí | 40-50% | 50-60% |
| Văn học | 20-35% | 65-80% |
| Quảng cáo | 15-25% | 75-85% |
| Thiếu nhi | 10-20% | 80-90% |

### 11.5 Nguyên tắc dịch thuật cụ thể

**1. Dịch từ viết tắt:**
> WHO → WHO (giữ nguyên, chú thích: Tổ chức Y tế Thế giới lần đầu)
> GDP → GDP (Tổng sản phẩm quốc nội)
> ASEAN → ASEAN (Hiệp hội các quốc gia Đông Nam Á)

**2. Dịch thành ngữ, tục ngữ:**
> **EN:** "Kill two birds with one stone."
> **VI:** "Một mũi tên trúng hai đích" hoặc "Nhất cử lưỡng tiện"
> **EN:** "Better late than never."
> **VI:** "Thà muộn còn hơn không" hoặc "Muộn còn hơn chẳng"

**3. Dịch đơn vị đo lường:**
> Giữ nguyên đơn vị quốc tế (m, km, kg, lít, v.v.)
> Chuyển đổi nếu cần thiết: inches → cm (2,54 cm), feet → m (0,3048 m)

**4. Dịch Humor / Chơi chữ:**
> Cân nhắc giữ nguyên hoặc thay bằng cách chơi chữ tương đương.
> Nếu không thể dịch được, thêm chú thích [không thể dịch được: chơi chữ].

### 11.6 Tự nhiên hóa (Naturalization)

**Mục tiêu:** Câu văn tiếng Việt không bị "bê nguyên" cấu trúc tiếng Anh.

**Ví dụ:**
> **EN:** "There are many factors that need to be considered."
> **Dịch từng từ (tồi):** "Có nhiều yếu tố mà cần phải được xem xét."
> **Tự nhiên (tốt):** "Có nhiều yếu tố cần xem xét."

> **EN:** "It is important to note that the deadline is approaching."
> **Dịch từng từ (tồi):** "Nó là quan trọng để lưu ý rằng hạn chót đang đến gần."
> **Tự nhiên (tốt):** "Cần lưu ý rằng hạn chót đang đến gần."

> **EN:** "The purpose of this report is to provide an overview..."
> **Dịch từng từ (tồi):** "Mục đích của báo cáo này là để cung cấp một tổng quan..."
> **Tự nhiên (tốt):** "Báo cáo này nhằm cung cấp tổng quan..."

**Các lỗi thường gặp khi dịch từ tiếng Anh:**
| English | Sai | Đúng |
|---------|-----|------|
| Being a student... | Là một sinh viên | Là sinh viên (bỏ "một") |
| There is/are... | Có... (thêm chủ từ giả) | Có... (tự nhiên) |
| It is + adj + to... | Nó là...để... | Thật...khi... / Việc... |
| Passive voice | Bị/được (lạm dụng) | Chủ động hóa hoặc bỏ "bị/được" |
| For example,... | Ví dụ cho... | Ví dụ,... / Chẳng hạn,... |
| In order to... | Để mà... | Để... / Nhằm... |
| In addition,... | Thêm vào đó | Ngoài ra,... / Thêm nữa,... |

### 11.7 Kiểm tra chất lượng bản dịch

**Checklist cuối cùng:**
- [ ] Ngữ pháp tiếng Việt tự nhiên (SVO, classifier, không lạm dụng bị động).
- [ ] Dấu thanh chính xác (kiểm tra kỹ từ dễ nhầm).
- [ ] Dấu câu đúng chuẩn tiếng Việt.
- [ ] Số, ngày tháng, tiền tệ đúng định dạng VI.
- [ ] Tên riêng phiên âm/nhập đúng.
- [ ] Mức độ Hán-Việt phù hợp với thể loại.
- [ ] Không còn dấu vết của lỗi OCR (nếu có).
- [ ] Không có lỗi chính tả hoặc dấu thanh.
- [ ] Câu văn tự nhiên, không bị ảnh hưởng quá nhiều từ cấu trúc tiếng Anh.

---

> *Tài liệu này là một phần của bộ kiến thức dịch thuật tiếng Việt. Mọi cập nhật và bổ sung đều được hoan nghênh.*

---

**© 2026 | Vietnamese Translation Knowledge Base | Phiên bản 1.0**
