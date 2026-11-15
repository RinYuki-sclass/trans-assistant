# AGENT RULES: NGHE NÓI VỢ TÔI LÀ ĐẠI LÃO PHẢN DIỆN (听说我老婆是反派大佬)

Tài liệu này xác định các quy chuẩn nhân vật, bối cảnh, ma trận đại từ, văn phong và quy trình dịch thuật áp dụng riêng cho dự án **Nghe Nói Vợ Tôi Là Đại Lão Phản Diện**.

---

## ⛔ 1. QUY TẮC CỐT LÕI (MANDATORY ZERO API KEY & INTEGRITY RULES)

1. **Agent Tự Thân Dịch Thuật (Zero Google API Key Mandate):**
   - Agent tự đọc nội dung file raw `source.md`, tự phân tích ngữ cảnh nhân vật, tự sinh bản dịch tiếng Việt chuẩn xác, mượt mà và lưu trực tiếp vào file `translation.md`.
   - **Tuyệt đối cấm:** Gọi bất kỳ script, tool hoặc API nào bên ngoài dùng `GOOGLE_API_KEY` hay `GEMINI_API_KEY`.
2. **Bảo Toàn 1:1 Đoạn Văn (1:1 Paragraph Alignment):**
   - Số đoạn tiếng Việt trong `translation.md` phải khớp tuyệt đối 1:1 với `source.md`. Không tự ý gộp đoạn, chẻ đoạn, không thêm bớt tình tiết.
3. **Quy Cách Ngắt Dòng Chuẩn `\n\n`:**
   - Mọi đoạn trần thuật và lời thoại bắt buộc phải có đúng 1 dòng trống (`\n\n`) ngăn cách. Tuyệt đối không để dính dòng (`\n`).
4. **Dấu Ngoặc Thoại:**
   - Sử dụng ngoặc kép cong tiếng Việt `“...”` cho toàn bộ lời thoại nhân vật. Không dùng gạch đầu dòng (`-`).

---

## 2. BẢNG NHÂN VẬT CHÍNH & MA TRẬN ĐẠI TỪ

| Tên nhân vật | Tên gốc | Đại từ ngôi 3 (Kể chuyện) | Vai trò / Thân phận | Quy chuẩn xưng hô & Ghi chú |
| :--- | :--- | :--- | :--- | :--- |
| **Cố Kiêu** | 顾骄 | **cậu** *(CẤM dùng "hắn")* | **Công chính (Chủ công)**: Mỹ công niên hạ, tân sinh viên Học viện Liên Bang, tinh thần lực cấp SSS. | Bề ngoài nhìn như khốc ca ngầu lòi, mắt rũ ngạo mạn, nhưng bên trong là chú cún con ngây thơ siêu sợ giao tiếp (xã khủng), mù đường nặng. Nhầm đại lão phản diện là vợ nhỏ dịu dàng cần nuôi. **Giai đoạn 1 (Chương 1-25):** Tự xưng cứng **"tôi"** *(CẤM xưng "em")*, gọi TNK là **"Ôn tiên sinh / ngài / Thẩm tiên sinh"**. **Giai đoạn 2+ (Chương 26-122):** Tự xưng cứng **"em"** *(CẤM xưng "tôi")*, gọi TNK là **"anh / vợ / Nguyệt Khanh"**. |
| **Thẩm Nguyệt Khanh** | 沈月卿 | **hắn** *(CẤM dùng "cậu" hoặc "anh")* | **Thụ chính (Ám Vực Lĩnh Chủ)**: Bạo quân vùng ô nhiễm, đại lão phản diện khét tiếng tinh tế, cường thụ. | Nhan sắc tuyệt mỹ, tâm cơ thâm trầm, khống chế dục cực cao, bị bạo loạn tinh thần lực SSS-grade. Trước mặt Cố Kiêu đóng giả làm vợ hiền "Ôn tiên sinh" ôn nhu nhu nhược. **Giai đoạn 1 (Chương 1-25):** Tự xưng cứng **"tôi"** *(CẤM xưng "ta/anh")*, gọi Cố Kiêu là **"cậu / Cố đồng học / tiểu bằng hữu"**. **Giai đoạn 2+ (Chương 26-122):** Tự xưng cứng **"anh"** *(CẤM xưng "ta/tôi")*, gọi Cố Kiêu là **"em / A Kiêu / cún ngốc"**. *(Chỉ xưng "ta" khi đối diện thuộc hạ Ám Vực hoặc kẻ thù)*. |
| **Tần Phong** | 秦封 | **anh ta / gã** | **Phó quan / Cận vệ thân tín của Thẩm Nguyệt Khanh** | Nghiêm túc, trung thành, chứng kiến đại lão phản diện dần trở thành "thê nô". |
| **Hà bác sĩ** | 何医生 | **ông ta** | **Bác sĩ sơ đạo tinh thần lực A-grade tại Ám Vực** | Bất lực trước bạo loạn tinh thần lực của thủ lĩnh, kinh ngạc trước thực lực của Cố Kiêu. |
| **Cố Niệm An** | 顾念安 | **cậu ấy / anh ấy** | **Thành viên gia đình Cố gia (Cổ Võ Tinh)** | Người nhà thân yêu của Cố Kiêu. |

---

## 3. THIẾT LẬP TINH TẾ & BỐI CẢNH ĐẶC THÙ

1. **Thiết lập Tinh Thần Lực & Sơ Đạo (Mental Strength & Guidance):**
   - Tinh thần lực chia các cấp: F -> SSS. Cả Cố Kiêu và Thẩm Nguyệt Khanh đều là **SSS-grade** vô địch tinh tế.
   - Bạo loạn tinh thần lực: Khiến người bệnh đau đớn, phát cuồng giết chóc. Cần người có tinh thần lực ngang hàng hoặc cao hơn tiến hành **sơ đạo (chữa lành)**.
2. **Địa danh & Thế lực:**
   - **Ám Vực (暗域):** Vùng đất hỗn loạn ngoài tầm kiểm soát của Liên Bang, nơi Thẩm Nguyệt Khanh thống trị.
   - **Khu ô nhiễm (污染区):** Vùng đất nguy hiểm bao bọc trang viên của Thẩm Nguyệt Khanh.
   - **Học viện Liên Bang (联邦学院):** Học viện quân sự danh giá số 1 tinh tế.
   - **Cổ Võ Tinh (古武星):** Quê nhà nghèo khó nhưng giàu truyền thống võ thuật của Cố Kiêu.
3. **Chi tiết hài hước sa điêu:**
   - Cố Kiêu nghèo đến mức không mua nổi quang não có chức năng định vị GPS, dẫn đến việc đi lạc vào động quỷ nhưng lại ngỡ vào nhầm nhà người bệnh hiền lành.

---

## 4. MA TRẬN XƯNG HÔ THEO GIAI ĐOẠN QUAN HỆ (QUY TẮC ĐƠN TÔN ĐỘC NHẤT)

> 🚨 **QUY TẮC CHỐT ĐƠN TÔN - CẤM ĐA LỰA CHỌN:**  
> Mỗi giai đoạn quan hệ chỉ có **DUY NHẤT 1 ĐẠI TỪ TỰ XƯNG CỐ ĐỊNH**. Tuyệt đối cấm dùng dạng liệt kê tùy nghi như "tôi / em" khiến cảnh trước xưng "em", cảnh sau lại xưng "tôi".

1. **Giai đoạn 1: Sơ đạo tinh thần lực & Hiểu lầm mỹ nhân (Chương 1 - 25)**
   - **Cố Kiêu:** Tự xưng duy nhất **“tôi”** *(CẤM xưng "em")*. Gọi Thẩm Nguyệt Khanh: thường ngày gọi **“Ôn tiên sinh”**, khách khí/tôn kính gọi **“ngài”**, khi biết họ Thẩm gọi **“Thẩm tiên sinh”**. Cặp chuẩn: `tôi - Ôn tiên sinh` hoặc `tôi - ngài`.
   - **Thẩm Nguyệt Khanh** *(khi đối diện Cố Kiêu)*: Tự xưng duy nhất **“tôi”** *(CẤM xưng "ta" hay "anh")*. Gọi Cố Kiêu: thường ngày gọi **“cậu”**, ngữ cảnh học đường gọi **“Cố đồng học”**, trêu chọc gọi **“tiểu bằng hữu”**. Cặp chuẩn: `tôi - cậu` hoặc `tôi - Cố đồng học`.
   - *(Ngoại lệ: Khi đối diện thuộc hạ Ám Vực hoặc kẻ thù, Thẩm Nguyệt Khanh xưng “ta”, gọi “các ngươi / anh”)*.

2. **Giai đoạn 2: Yêu đương ngọt ngào & Nuôi vợ nhỏ (Chương 26 - 65)**
   - **Cố Kiêu:** Tự xưng duy nhất **“em”** *(CẤM xưng "tôi" trong đối thoại thân mật)*. Gọi Thẩm Nguyệt Khanh: thường ngày gọi **“anh”**, ngọt ngào/sủng vợ gọi **“vợ”**, khi nghiêm túc gọi **“Nguyệt Khanh”**. Cặp chuẩn: `em - anh` hoặc `em - vợ`.
   - **Thẩm Nguyệt Khanh** *(khi đối diện Cố Kiêu)*: Tự xưng duy nhất **“anh”** *(CẤM xưng "ta" hay "tôi")*. Gọi Cố Kiêu: thường ngày gọi **“em”**, gọi tên âu yếm gọi **“A Kiêu”**, biệt danh trêu yêu gọi **“cún ngốc”**. Cặp chuẩn: `anh - em` hoặc `anh - A Kiêu`.

3. **Giai đoạn 3: Rớt áo giáp bạo quân & Đồng tâm hiệp lực (Chương 66 - 122)**
   - **Kế thừa 100% Giai đoạn 2:** Dù biết vợ mình là Đại lão phản diện tàn bạo nhất tinh tế, Cố Kiêu vẫn một lòng cưng chiều, khóa cứng tự xưng **“em”**, gọi **“anh / vợ / Nguyệt Khanh”**.
   - **Thẩm Nguyệt Khanh:** Trước mặt Cố Kiêu luôn xưng **“anh”**, gọi **“em / A Kiêu / cún ngốc”**. Chỉ khi bộc phát uy áp trước mặt kẻ thù/người ngoài mới xưng **“ta”**, gọi **“ngươi / các ngươi”**.

---

## 5. PHÂN BIỆT RÕ RÀNG GIỮA LỜI THOẠI VÀ TRẦN THUẬT

- **Lời thoại trong `“...”`:** Tự nhiên, phản ánh đúng tính cách: Cố Kiêu chân thành, ngơ ngác, ấm áp; Thẩm Nguyệt Khanh ôn nhu ngụy trang bên ngoài nhưng bên trong thâm độc, cố chấp bệnh kiều.
- **Văn trần thuật ngôi 3 ngoài ngoặc:**
  - Bắt buộc tuân thủ: Cố Kiêu = **“cậu”**, Thẩm Nguyệt Khanh = **“hắn”**.
  - **TUYỆT ĐỐI CẤM** đem đại từ đối thoại (`mày`, `tao`, `tôi`, `anh`) vào làm chủ ngữ câu trần thuật hoặc độc thoại nội tâm ngôi 3 (chống lỗi "đá ngôi").
