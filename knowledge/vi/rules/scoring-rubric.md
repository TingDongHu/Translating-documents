---
id: vi/rules/scoring-rubric
type: rules
target_lang: vi
name: Thang điểm Đánh giá Chất lượng Dịch thuật Tiếng Việt (Vietnamese Translation Quality Scoring Rubric)
description: Vietnamese translation quality scoring rubric
---

# Thang điểm Đánh giá Chất lượng Dịch thuật Tiếng Việt (Vietnamese Translation Quality Scoring Rubric)

> Phiên bản: 1.0 | Ngày: 2026-05
> Áp dụng cho: Dịch thuật từ ngôn ngữ nguồn sang tiếng Việt

---

## Cấu trúc Thang điểm

| Thang điểm | Mô tả | Ý nghĩa |
|-----------|-------|---------|
| **100** | Xuất sắc (Excellent) | Bản dịch hoàn hảo, không lỗi, tự nhiên như bản ngữ |
| **90** | Tốt (Good) | Bản dịch chất lượng cao, lỗi nhỏ không ảnh hưởng ý nghĩa |
| **80** | Đạt yêu cầu (Adequate) | Bản dịch đúng, còn một số chỗ chưa tự nhiên |
| **70** | Cần cải thiện (Needs Improvement) | Bản dịch đúng cơ bản nhưng có lỗi đáng kể |
| **60** | Kém (Poor) | Bản dịch có nhiều lỗi, cần dịch lại đáng kể |
| **<50** | Không đạt (Unacceptable) | Bản dịch sai nghiêm trọng, cần dịch lại hoàn toàn |

---

## 1. Độ chính xác về Số liệu (Numerical Accuracy) — Trọng số: 30%

Tiêu chí lớn nhất. Số liệu sai làm thay đổi hoàn toàn ý nghĩa của tài liệu kỹ thuật, tài chính, pháp lý.

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Hoàn hảo | Tất cả số liệu chính xác tuyệt đối. Dấu thập phân (dấu phẩy), dấu phân cách nghìn (dấu chấm hoặc cách), định dạng ngày tháng (DD/MM/YYYY), tiền tệ (₫ sau số, $ trước số), tỷ lệ phần trăm đúng chuẩn VI. Không có bất kỳ sai sót nào về số. |
| **90** | Gần hoàn hảo | Tất cả số liệu chính xác. Một lỗi nhỏ về định dạng không gây hiểu nhầm (ví dụ: thiếu một khoảng trắng giữa số và ký hiệu %, hoặc dùng dấu chấm thay dấu phẩy ở vị trí không quan trọng). Không có sai lệch về giá trị số. |
| **80** | Đạt yêu cầu | Số liệu chính xác. Có 1-2 lỗi định dạng nhỏ: dùng dấu chấm thay dấu phẩy thập phân ở 1-2 vị trí, thiếu dấu phân cách nghìn, hoặc nhầm lẫn định dạng ngày-tháng không gây nhầm lẫn về ngày (ví dụ: 06/05 thay vì 05/06 khi tháng và ngày không gây nhập nhằng). |
| **70** | Có lỗi | Có 1-2 lỗi về giá trị số (sai số ảnh hưởng đến tính toán) hoặc 3-4 lỗi định dạng. Định dạng ngày tháng nhầm lẫn nhưng có thể suy luận được ý đúng. Sai ký hiệu tiền tệ nhưng đúng giá trị. |
| **60** | Nhiều lỗi | 3-4 lỗi về giá trị số, nhiều lỗi định dạng. Lỗi ngày tháng gây nhầm lẫn hoặc hiểu sai. Sử dụng sai dấu phân cách thập phân gây thay đổi giá trị. Lẫn lộn ký hiệu tiền tệ. |
| **<50** | Không đạt | Sai số nghiêm trọng, sai ngày tháng không thể hiểu được, mất hoặc thêm số 0 làm thay đổi giá trị hàng chục lần. Định dạng ngày MM/DD/YYYY dùng sai cho văn bản tiếng Việt. Số liệu hoàn toàn không đáng tin cậy. |

### Ví dụ đánh giá

| Tình huống | Lỗi | Điểm |
|-------------|------|-------|
| Dịch 3.14 (EN) → 3,14 (VI đúng) | Không lỗi | 100 |
| Dịch 3.14 (EN) → 3.14 (VI: giữ nguyên dấu chấm) | Lỗi nhỏ | 90 |
| Dịch 05/06/2026 (EN: May 6) → 05/06/2026 (VI: đúng, vì DD/MM trùng) | Không lỗi | 100 |
| Dịch 06/05/2026 (EN: June 5) → 05/06/2026 (lẽ ra là June 5 = 05/06) | Lỗi nặng | <50 |
| Dịch 1,000.50 (EN) → 1.000,50 (VI đúng) | Không lỗi | 100 |
| Dịch 1,000.50 (EN) → 1,000.50 (giữ nguyên) | Sai định dạng | 80 |
| Dịch $50 → 50$ (Mỹ) thay vì 50 USD | Nhẹ | 90 |
| Dịch 1.500.000 (VN tiền) → 150.000 (thiếu một số 0) | Nghiêm trọng | <50 |

---

## 2. Nhất quán Thuật ngữ (Terminology Consistency) — Trọng số: 20%

Đánh giá việc sử dụng thuật ngữ chuyên ngành, từ Hán-Việt vs thuần Việt, và tính nhất quán trong toàn bộ bản dịch.

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Xuất sắc | Thuật ngữ đồng nhất tuyệt đối xuyên suốt văn bản. Cân bằng lý tưởng giữa từ Hán-Việt và thuần Việt phù hợp với thể loại văn bản. Từ viết tắt được chú thích lần đầu. Tên riêng đồng nhất. Quyết định dịch thuật (giữ nguyên/phiên âm/dịch nghĩa) nhất quán. |
| **90** | Tốt | Thuật ngữ đồng nhất gần như tuyệt đối. 1-2 chỗ không đồng nhất về thuật ngữ không gây nhầm lẫn. Lựa chọn Hán-Việt/thuần Việt hợp lý cho thể loại. Có thể có 1 trường hợp ngoại lệ không gây ảnh hưởng. |
| **80** | Đạt | Thuật ngữ tương đối đồng nhất. Có 2-3 chỗ không đồng nhất (ví dụ: lúc dùng "bệnh nhân", lúc dùng "người bệnh" không có lý do). Từ Hán-Việt sử dụng hơi quá mức hoặc hơi thiếu so với tiêu chuẩn thể loại. 1-2 tên riêng không đồng nhất cách dịch. |
| **70** | Cần cải thiện | 4-5 chỗ không đồng nhất thuật ngữ. Mức độ Hán-Việt không phù hợp với thể loại văn bản (quá nhiều Hán-Việt trong văn bản phổ thông, hoặc quá ít trong văn bản pháp lý). Tên riêng dịch không đồng nhất (lúc phiên âm, lúc giữ nguyên). Thiếu chú thích từ viết tắt. |
| **60** | Kém | Nhiều chỗ không đồng nhất (6+). Thuật ngữ quan trọng bị dịch khác nhau trong cùng văn bản. Mức độ Hán-Việt hoàn toàn không phù hợp. Nhiều tên riêng sai cách xử lý. Gây khó hiểu cho người đọc. |
| **<50** | Không đạt | Thuật ngữ hỗn loạn, không có nhất quán. Cùng một khái niệm được dịch bằng 3-4 cách khác nhau. Từ Hán-Việt sử dụng bừa bãi. Tên riêng sai nguyên tắc. Bản dịch không chuyên nghiệp. |

### Ví dụ đánh giá

| Tình huống | Điểm |
|-------------|------|
| "patient" luôn được dịch là "bệnh nhân" xuyên suốt văn bản y khoa | 100 |
| "patient" lúc dịch "bệnh nhân", lúc dịch "người bệnh" trong cùng văn bản | 80 |
| "AI" xuất hiện lần đầu không chú thích "Trí tuệ nhân tạo" | 90 |
| Văn bản pháp luật dùng quá nhiều từ thuần Việt, thiếu chính xác | 70 |
| "bệnh nhân" → "patient", "người bệnh" → "sick person", "BN" → viết tắt không giải thích | <50 |
| Dùng "tử vong" trong văn bản cho trẻ em thay vì "chết" hoặc "mất" | 60 |
| Dùng "sử dụng" (formal) và "dùng" (informal) xen kẽ không có lý do trong văn bản kỹ thuật | 80 |

---

## 3. Độ trung thực Ngữ nghĩa (Semantic Fidelity) — Trọng số: 25%

Đánh giá mức độ truyền tải chính xác ý nghĩa, sắc thái, và ngữ cảnh của văn bản gốc.

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Xuất sắc | Ý nghĩa được truyền tải đầy đủ, chính xác 100%. Sắc thái, ngữ cảnh, giọng điệu được giữ nguyên. Câu văn tiếng Việt tự nhiên, không bị "bóng" tiếng nước ngoài. Không thêm/bớt/sửa ý. Dịch thành ngữ, ẩn dụ, chơi chữ phù hợp. |
| **90** | Tốt | Ý nghĩa chính xác trên 99%. 1-2 chỗ sắc thái nhẹ chưa được truyền tải hoàn hảo (ví dụ: dịch "significant" thành "quan trọng" thay vì "đáng kể" trong ngữ cảnh). Câu văn chủ yếu tự nhiên. Không có lỗi về ý. |
| **80** | Đạt | Ý nghĩa chính xác khoảng 95%. Một vài chỗ dịch hơi cứng hoặc thiếu sắc thái. Có thể có 1-2 lỗi nhỏ về ý không ảnh hưởng tổng thể. Đôi chỗ còn "bóng" tiếng Anh. |
| **70** | Cần cải thiện | Ý nghĩa chính xác khoảng 85-90%. Có 2-3 lỗi về ý nghĩa hoặc sắc thái. Bản dịch còn nhiều chỗ gượng ép, thiếu tự nhiên. Diễn đạt tiếng Việt chưa trôi chảy. Một số câu khó hiểu. |
| **60** | Kém | Ý nghĩa chính xác khoảng 70-84%. 4-5 lỗi về ý nghĩa đáng kể. Bản dịch vụng về, mắc lỗi ngữ pháp tiếng Việt cơ bản. Nhiều câu khó hiểu hoặc hiểu sai. |
| **<50** | Không đạt | Ý nghĩa chính xác dưới 70%. Sai lệch ý nghĩa nghiêm trọng. Nhiều câu dịch sai hoàn toàn. Người đọc không thể hiểu hoặc hiểu sai ý tác giả. Bản dịch không thể sử dụng được. |

### Các lỗi thường gặp về ngữ nghĩa

| Lỗi | Sai | Đúng | Mức độ |
|------|-----|------|--------|
| Sai dấu thanh đổi nghĩa | "Tôi có bán xe" (I sell car) | "Tôi có bạn xe" (??? Vô nghĩa) | Nghiêm trọng |
| Sai danh từ riêng | "Hà Nội" thành "Hạ Nội" | Hà Nội | Nghiêm trọng |
| Dịch sát từ | "It is raining cats and dogs" → "Trời mưa mèo và chó" | "Mưa như trút nước" | Nặng |
| Sai ngữ cảnh | Dịch formal thành informal | Tùy ngữ cảnh | Trung bình |
| Bỏ sót ý | Bỏ qua một mệnh đề phụ | Giữ đầy đủ | Tùy mức |
| Thêm ý | Thêm thông tin không có trong gốc | Trung thành với gốc | Tùy mức |

### Ví dụ cụ thể

> **Gốc (EN):** "The company's revenue grew substantially, reaching an all-time high of $2.5 million."
> **Dịch tốt (100):** "Doanh thu của công ty tăng trưởng đáng kể, đạt mức cao nhất mọi thời đại là 2,5 triệu USD."
> **Dịch trung bình (80):** "Doanh thu của công ty tăng trưởng mạnh, đạt mức cao nhất lịch sử là $2,5 triệu."
> **Dịch kém (60):** "Doanh thu của công ty đã phát triển tốt, đạt được $2.5 triệu."
> **Dịch không đạt (<50):** "Công ty phát triển doanh thu, đã có 2.5$."

---

## 4. Tuân thủ Định dạng (Format Compliance) — Trọng số: 10%

Đánh giá mức độ tuân thủ các quy tắc định dạng tiếng Việt (dấu câu, viết hoa, khoảng trắng, cấu trúc danh sách, v.v.).

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Hoàn hảo | Tất cả quy tắc định dạng tiếng Việt được tuân thủ. Dấu câu đúng vị trí. Viết hoa đúng (sentence case cho tiêu đề). Không có lỗi khoảng trắng. Cấu trúc danh sách và tiêu đề nhất quán. Dấu ngoặc kép đặt đúng vị trí so với dấu câu. |
| **90** | Tốt | Gần như hoàn hảo. 1-2 lỗi nhỏ về định dạng: dư/thừa khoảng trắng, lỗi viết hoa/thường không ảnh hưởng đọc hiểu. |
| **80** | Đạt | 3-4 lỗi định dạng nhỏ. Dấu câu đôi chỗ chưa đúng. Một số chỗ viết hoa sai quy tắc (ví dụ: viết hoa mọi từ trong tiêu đề kiểu tiếng Anh). |
| **70** | Cần cải thiện | 5-6 lỗi định dạng. Dấu câu sai nhiều chỗ (dấu phẩy trước "và", dấu chấm cuối tiêu đề, khoảng trắng sai). Viết hoa không nhất quán. |
| **60** | Kém | 7+ lỗi định dạng rõ rệt. Lỗi dấu câu hệ thống (ví dụ: luôn đặt dấu chấm trong ngoặc kép kiểu Mỹ). Nhiều chỗ viết hoa sai. Cấu trúc văn bản lộn xộn. |
| **<50** | Không đạt | Lỗi định dạng tràn lan. Không tuân thủ bất kỳ quy tắc định dạng tiếng Việt nào. Định dạng kiểu nước ngoài được giữ nguyên mà không điều chỉnh. Văn bản trông như chưa qua biên tập. |

### Kiểm tra cụ thể

**Checklist định dạng:**
- [ ] Dấu phẩy: không dùng Oxford comma (không có dấu phẩy trước "và").
- [ ] Dấu ngoặc kép: dấu câu nằm ngoài ngoặc kép.
- [ ] Dấu gạch ngang: có khoảng trắng trước và sau em dash.
- [ ] Viết hoa tiêu đề: sentence case.
- [ ] Khoảng trắng: một khoảng sau dấu câu, không khoảng trước dấu phẩy/chấm.
- [ ] Dấu phẩy động: dùng dấu phẩy (không phải dấu chấm).

---

## 5. Tính đầy đủ (Completeness) — Trọng số: 10%

Đánh giá mức độ đầy đủ của bản dịch so với văn bản gốc.

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Đầy đủ tuyệt đối | Toàn bộ văn bản gốc được dịch đầy đủ. Không thiếu đoạn, câu, từ, hoặc phần nào. Chú thích, phụ lục, ghi chú cuối trang đều được dịch. Tất cả nội dung trong bảng biểu, hình vẽ, chú thích đều được xử lý. |
| **90** | Gần đầy đủ | Thiếu 1-2 từ/cụm từ nhỏ không ảnh hưởng đến ý nghĩa tổng thể. Hoặc thiếu 1 ghi chú cuối trang không quan trọng. |
| **80** | Tương đối đầy đủ | Thiếu 1-2 câu hoặc 1 đoạn ngắn. Nội dung trong bảng biểu hoặc chú thích hình ảnh bị bỏ sót một phần. |
| **70** | Thiếu đáng kể | Thiếu 1 đoạn văn hoặc 3-4 câu rải rác. Một phần phụ lục hoặc ghi chú quan trọng không được dịch. Bảng biểu thiếu nội dung. |
| **60** | Thiếu nhiều | Thiếu nhiều đoạn (2-3 đoạn). Nhiều chú thích, ghi chú không được dịch. Nội dung quan trọng bị bỏ qua. |
| **<50** | Thiếu trầm trọng | Thiếu nguyên trang hoặc phần lớn nội dung (trên 10% văn bản gốc bị bỏ qua). Bản dịch không thể sử dụng do thiếu quá nhiều. |

### Ví dụ

| Tình huống | Điểm |
|-------------|------|
| Dịch đầy đủ 100% văn bản 10 trang, kể cả footnotes | 100 |
| Thiếu 1 tên riêng trong danh sách 100 mục | 90 |
| Thiếu 1 câu trong đoạn mở đầu | 90 |
| Thiếu 1 đoạn văn 3-4 dòng ở giữa tài liệu | 70 |
| Bỏ qua hoàn toàn phần Phụ lục (2 trang) | <50 |
| Bảng biểu chỉ dịch tiêu đề, không dịch nội dung | 60 |
| Thiếu chú thích cuối trang số 5 và 7 | 80 |

---

## 6. Chất lượng OCR / Suy luận (Inference & OCR Quality) — Trọng số: 5%

Đánh giá khả năng xử lý các hiện vật OCR (văn bản quét) và suy luận chính xác nội dung bị hỏng.

### Bảng điểm

| Điểm | Mô tả | Yêu cầu chi tiết |
|------|-------|-------------------|
| **100** | Xuất sắc | Tất cả lỗi OCR được phát hiện và phục hồi chính xác. Định dạng `[đã phục hồi: ...]` được sử dụng đúng quy tắc. Suy luận chính xác 100%. Không có can thiệp sai. |
| **90** | Tốt | Hầu hết lỗi OCR được xử lý. 1-2 chỗ phục hồi không tối ưu nhưng vẫn đúng. Suy luận chính xác. Ghi chú phục hồi đúng định dạng. |
| **80** | Đạt | Phát hiện và phục hồi phần lớn lỗi OCR. 1-2 lỗi OCR bị bỏ sót hoặc phục hồi sai nhẹ (không ảnh hưởng nghĩa). Định dạng ghi chú đôi chỗ chưa đúng. |
| **70** | Cần cải thiện | Nhiều lỗi OCR bị bỏ sót (3-4 lỗi). 1-2 suy luận sai dẫn đến hiểu sai nhẹ. Định dạng ghi chú phục hồi không nhất quán. Thiếu `[cần kiểm tra]` ở chỗ nghi ngờ. |
| **60** | Kém | Nhiều lỗi OCR không được phục hồi. 3-4 suy luận sai. Thiếu ghi chú kiểm tra ở những chỗ cần thiết. Định dạng ghi chú sai quy tắc. |
| **<50** | Không đạt | Hầu hết lỗi OCR không được phát hiện hoặc phục hồi sai. Suy luận sai nghiêm trọng làm thay đổi ý nghĩa văn bản. Không sử dụng ghi chú phục hồi. Bản dịch chứa nhiều lỗi OCR thô. |

### Các lỗi OCR thường gặp

| OCR gốc | Phục hồi đúng | Phục hồi sai | Điểm |
|---------|---------------|--------------|------|
| "da co ket qua" | "đã có kết quả" | "đa cô kết quả" | 100 vs <50 |
| "ngay 1/1/2026" | "ngày 01/01/2026" | "ngày 1/1/2026" (giữ nguyên) | 90 vs 80 |
| "ho ten: nguyen van a" | "họ tên: Nguyễn Văn A" | "họ tên: nguyen van a" | 90 vs 70 |
| "3.141592" | "3,141592" | "3.141592" (giữ nguyên) | 100 vs 80 |

---

## Nguyên tắc Không khoan nhượng (Zero-Tolerance Rules)

Các lỗi sau đây dẫn đến **điểm tối đa là 60** cho toàn bộ bản dịch, bất kể các tiêu chí khác.

### ZT-1: Sai dấu thanh gây thay đổi nghĩa nghiêm trọng

| Từ sai | Từ đúng | Hậu quả |
|--------|----------|----------|
| bán | bạn | "sell" → "friend" |
| cá | cả | "fish" → "all" |
| má | mà | "mother" → "that/but" |
| tử | tứ/tư | "death" → "four" / "thought" |
| hóa | hỏa | "chemistry" → "fire" |
| mỹ | mĩ (cũ) | Không phải lỗi (biến thể chính tả cho phép) |

**Lưu ý:** Một số biến thể chính tả được chấp nhận:
- "mỹ" / "mĩ" (cả hai đều đúng)
- "kỹ" / "kĩ" (cả hai đều đúng)
- "cá nhân" không thể viết "cá nhân" — đây là lỗi chính tả thông thường

**Ngoại lệ:** Các lỗi dấu thanh nhỏ không làm thay đổi nghĩa hoặc ngữ cảnh cho phép suy luận dễ dàng (ví dụ: "toi" → "tôi" trong ngữ cảnh rõ ràng) không bị coi là zero-tolerance.

### ZT-2: Sai định dạng ngày tháng

| Sai | Đúng | Lý do |
|-----|------|-------|
| MM/DD/YYYY (05/06/2026) | DD/MM/YYYY (06/05/2026) | Định dạng Mỹ bị cấm trong văn bản VI |
| Tháng 5/6/2026 | Ngày 6 tháng 5 năm 2026 | Viết tắt không rõ ràng |
| 2026/05/06 (ISO) | 06/05/2026 | ISO không phải chuẩn VI |

### Xử lý khi phát hiện ZT

- Nếu phát hiện bất kỳ lỗi zero-tolerance nào, điểm tổng thể **tối đa là 60**.
- Ghi rõ lỗi ZT trong báo cáo đánh giá.
- Bản dịch cần được sửa và đánh giá lại.

---

## Cách tính điểm Tổng thể (Overall Score Calculation)

Điểm tổng thể = (Điểm Numerical × 30%) + (Điểm Terminology × 20%) + (Điểm Semantic × 25%) + (Điểm Format × 10%) + (Điểm Completeness × 10%) + (Điểm OCR × 5%)

**Kiểm tra Zero-Tolerance trước khi tính điểm:**
1. Nếu có lỗi ZT-1 hoặc ZT-2 → Điểm tổng thể = min(điểm tính theo công thức, 60).

**Ví dụ tính điểm:**

| Tiêu chí | Trọng số | Điểm | Điểm có trọng số |
|-----------|----------|------|-------------------|
| Numerical Accuracy | 30% | 90 | 27,0 |
| Terminology Consistency | 20% | 80 | 16,0 |
| Semantic Fidelity | 25% | 85 | 21,25 |
| Format Compliance | 10% | 90 | 9,0 |
| Completeness | 10% | 100 | 10,0 |
| OCR Quality | 5% | 80 | 4,0 |
| **Tổng** | **100%** | | **87,25** |

→ Xếp loại: **Tốt (90-80)**

> **Lưu ý:** Nếu phát hiện lỗi zero-tolerance, điểm 87,25 sẽ bị giới hạn ở mức 60, xếp loại Kém.

---

## Thang xếp loại Tổng thể

| Khoảng điểm | Xếp loại | Hành động |
|-------------|----------|-----------|
| 93-100 | **Xuất sắc** | Chấp nhận, không cần chỉnh sửa |
| 85-92 | **Tốt** | Chấp nhận, có thể chỉnh sửa nhỏ |
| 75-84 | **Đạt yêu cầu** | Chấp nhận có điều kiện, cần chỉnh sửa một số chỗ |
| 65-74 | **Cần cải thiện** | Cần chỉnh sửa đáng kể trước khi chấp nhận |
| 50-64 | **Kém** | Cần dịch lại hoặc chỉnh sửa toàn diện |
| <50 | **Không đạt** | Dịch lại hoàn toàn |

---

## Mẫu báo cáo đánh giá

```
=== ĐÁNH GIÁ CHẤT LƯỢNG DỊCH THUẬT TIẾNG VIỆT ===

Tài liệu: [tên tài liệu]
Người đánh giá: [tên]
Ngày: [ngày]

1. Độ chính xác Số liệu (30%): __ /100
   - Nhận xét: ...
2. Nhất quán Thuật ngữ (20%): __ /100
   - Nhận xét: ...
3. Độ trung thực Ngữ nghĩa (25%): __ /100
   - Nhận xét: ...
4. Tuân thủ Định dạng (10%): __ /100
   - Nhận xét: ...
5. Tính đầy đủ (10%): __ /100
   - Nhận xét: ...
6. Chất lượng OCR (5%): __ /100
   - Nhận xét: ...

TỔNG ĐIỂM: __ /100
XẾP LOẠI: [Xuất sắc/Tốt/Đạt/Cần cải thiện/Kém/Không đạt]

Zero-Tolerance: [Có/Không]
Nếu có: Điểm giới hạn ở 60.

NHẬN XÉT CHUNG:
...

KHUYẾN NGHỊ:
...
```

---

> *Tài liệu này là một phần của bộ kiến thức dịch thuật tiếng Việt.*
> *Áp dụng cho quy trình đánh giá chất lượng bản dịch.*

---

**© 2026 | Vietnamese Translation Quality Scoring Rubric | Phiên bản 1.0**
