# BỘ QUY CHUẨN DỊCH THUẬT & QUY TẮC BẮT BUỘC (TRANSLATION RULES)
## DỰ ÁN: XUYÊN THÀNH PHÁO HÔI CÁN ĐIỆU PHẢN PHÁI, BẤT THỊ GIÁ CÁN PHÁP (穿成炮灰干掉反派，不是这干法！)

---

## ⛔ PHẦN 1: QUY TẮC TỐI THƯỢNG (UNIVERSAL ZERO GOOGLE API KEY MANDATE)

1. **Agent Tự Thân Dịch Thuật Trực Tiếp 100%:**
   - Toàn bộ các công đoạn xử lý văn bản, đọc `source.md`, chuyển ngữ sang tiếng Việt, kiểm duyệt lỗi QC, cập nhật cơ sở dữ liệu `memory/` và `chapters_index.json` đều do AI Code Agent tự thân thực hiện trực tiếp.
   - **Tuyệt đối không chạy script ngoài, batch file hay thư viện bên ngoài sử dụng `GOOGLE_API_KEY` / `GEMINI_API_KEY`.**
   - Đảm bảo 100% không phát sinh lỗi hạn ngạch 429 Resource Exhausted hay 503 High Demand, duy trì sự ổn định tối đa cho toàn bộ pipeline.

2. **Nguyên Tắc Tự Hành Liên Hoàn (Zero Conversational Pause):**
   - Khi chạy ở chế độ tự hành liên hoàn theo batch, Agent không dừng lại giữa chừng chỉ để hỏi han hay mời chào ("nhắn tiếp tục để dịch tiếp").
   - Agent chủ động xử lý hết số chương trong batch được yêu cầu hoặc khi chạm Circuit Breaker thực sự.

---

## 📖 PHẦN 2: BẢO TOÀN NGUYÊN TÁC & QUY CHUẨN ĐỊNH DẠNG (1:1 ALIGNMENT)

1. **Khớp Đoạn Tuyệt Đối 1:1 (Paragraph Alignment):**
   - Số lượng đoạn văn trong bản dịch `translation.md` phải bằng chính xác 100% số lượng đoạn trong `source.md`.
   - Cấm gộp nhiều đoạn ngắn thành một đoạn dài.
   - Cấm chẻ một đoạn gốc thành nhiều đoạn rời rạc.
   - Không bỏ sót bất kỳ câu chữ, tình tiết nào của nguyên tác.

2. **Quy Cách Khoảng Cách Đoạn Chuẩn `\n\n`:**
   - Tất cả các đoạn văn (cả trần thuật lẫn lời thoại) phải cách nhau đúng một dòng trống (`\n\n`).
   - Tuyệt đối không để dính dòng (`\n`).

3. **Dấu Thoại Chuẩn Ngoặc Kép Cong `“...”`:**
   - Tất cả lời thoại trực tiếp của nhân vật bắt buộc đặt trong cặp ngoặc kép cong tiếng Việt: `“` và `”`.
   - Tuyệt đối không dùng gạch ngang đầu dòng (`- `) hoặc ngoặc kép thẳng lập trình (`"..."`).

4. **Định Dạng Tag Hệ Thống & Trạng Thái Đặc Thù:**
   - Các bảng lựa chọn hoặc thông báo của hệ thống: Đặt trong ngoặc vuông chuẩn:
     - `[A. Cán điệu hắn / Giết chết hắn. (Xác suất thành công: Cực thấp)]`
     - `[B. Cảm hóa hắn. (Xác suất thành công: Cực cao, Lựa chọn mặc định)]`
     - `[C. Yêu hắn. (Lựa chọn ưu tiên của ký chủ, Hệ thống đề cử)]`
     - `[Hệ thống cảnh báo: ...]`

---

## 👥 PHẦN 3: BẢNG THIẾT LẬP NHÂN VẬT & MA TRẬN ĐẠI TỪ XƯNG HÔ

### 3.1. Thiết Lập Nhân Vật Cốt Lõi

| Tên Hán Việt | Tên Gốc | Ngôi 3 Trần Thuật | Vai Trò & Tính Cách | Thiết Lập Chi Tiết |
| :--- | :--- | :---: | :--- | :--- |
| **Tần Mục** | 秦穆 | **hắn** | **Công chính**<br>(Chủ công phong phê, giả hoàn khố) | Kiếp trước là đại ma đầu/phản diện dồn thế giới vào diệt vong. Xuyên thư thành pháo hôi liếm cẩu. Tính cách thong dong, sắc sảo, thích trêu chọc, ngông nghênh nhưng cực kỳ thâm trầm và chiếm hữu. |
| **Giản Vân Trầm** | 简云沉 | **cậu** | **Thụ chính**<br>(Mỹ cường thảm, phản diện nguyên tác) | Con riêng Khương gia, chịu nhiều uất ức, bề ngoài lạnh lùng gai góc như nhím nhưng bên trong khát khao hơi ấm. Từng căm thù Tần Mục xem mình là thế thân. |
| **Khương Vân Hàn** | 姜云寒 | **anh ta / gã** | **Nam chính nguyên tác** | Thiếu gia chính thống của Khương gia, đối tượng nguyên thân mê mệt, đối thủ tranh đoạt vị thế với Giản Vân Trầm. Ngạo mạn, đạo đức giả. |
| **Hệ thống** | 系统 | **hệ thống / nó** | **Hệ thống nhiệm vụ** | Trói định với Tần Mục, ép buộc làm nhiệm vụ pháo hôi nhưng hoàn toàn bất lực trước độ điên và sự áp đảo của Tần Mục. |
| **Khương gia chủ / Khương Đằng** | 姜腾 | **ông ta / lão** | Gia chủ Khương gia | Người cha tàn nhẫn, chỉ coi trọng lợi ích gia tộc, đối xử bạc bẽo với Giản Vân Trầm. |

---

### 3.2. Ma Trận Xưng Hô Đối Thoại Bắt Buộc

| Cặp Giao Tiếp | Người Nói | Xưng | Gọi Đối Phương | Sắc Thái & Giai Đoạn Áp Dụng |
| :--- | :--- | :---: | :---: | :--- |
| **Tần Mục ↔ Giản Vân Trầm** | Tần Mục | **tôi / anh** | **cậu / em / Giản Vân Trầm / nhóc con** | - Giai đoạn đầu (thăm dò, đùa cợt): xưng **"tôi - cậu"**.<br>- Giai đoạn xác định tình cảm / trêu chọc thân mật / yêu nhau: xưng **"anh - em"**.<br>- Biệt danh trêu đùa: **"nhóc con"** hoặc gọi cả họ lẫn tên khi nghiêm túc. |
| | Giản Vân Trầm | **tôi / em** | **anh / Tần Mục / Tần thiếu** | - Ban đầu (đề phòng, mỉa mai): xưng **"tôi - anh / Tần thiếu"**.<br>- Khi rung động, thân mật: xưng **"em - anh"**.<br>- Khi tức giận, quẫn bách: gọi thẳng tên **"Tần Mục"**. |
| **Tần Mục ↔ Khương Vân Hàn** | Tần Mục | **tôi** | **cậu Khương / anh** | Lạnh nhạt, thờ ơ, mỉa mai, dứt khoát xem như không khí. |
| | Khương Vân Hàn | **tôi** | **Tần Mục** | Bất ngờ, tức tối, không cam lòng khi mất đi một kẻ luôn bám đuôi. |
| **Tần Mục ↔ Hệ Thống** | Tần Mục | **ta / tôi** | **mi / hệ thống** | Tư thế kẻ bề trên, thong dong chế giễu, không sợ trừng phạt. |
| | Hệ Thống | **bản hệ thống / tôi** | **ký chủ** | Máy móc, hoảng loạn, bất lực trước sự chệch hướng cốt truyện. |
| **Giản Vân Trầm ↔ Khương Vân Hàn** | Giản Vân Trầm | **tôi** | **anh / Khương thiếu gia** | Thù hận, mỉa mai, không nhượng bộ dù chỉ nửa bước. |

---

## 🎭 PHẦN 4: PHÂN ĐỊNH TUYỆT ĐỐI GIỮA TRẦN THUẬT VÀ LỜI THOẠI

1. **Ngôi 3 Trần Thuật (Tự sự của người kể chuyện):**
   - Tần Mục: Bắt buộc dùng **"hắn"**.
   - Giản Vân Trầm: Bắt buộc dùng **"cậu"**.
   - Khương Vân Hàn: Dùng **"anh ta / gã"**.
   - Khương lão gia: Dùng **"ông ta / lão"**.
   - Tuyệt đối không để xảy ra hiện tượng lộn xộn giữa "hắn" và "cậu" trong cùng một đoạn văn miêu tả hai người tương tác.

2. **CẤM ĐÁ NGÔI (Tránh lẫn lộn góc nhìn):**
   - **Lời thoại trong ngoặc kép `“...”`:** Được phép dùng các đại từ đối thoại tùy theo cảm xúc (ví dụ: giận dữ mắng nhau có thể dùng `“mày - tao”`, `“ngươi - ta”`).
   - **Văn trần thuật bên ngoài ngoặc kép:** **TUYỆT ĐỐI CẤM** đem đại từ đối thoại (`mày`, `tao`, `ngươi`, `ta`) vào câu tự sự hoặc suy nghĩ nội tâm ngôi 3.
   - *Sai phạm:* `Mày dựa vào cái gì mà dám nhìn cậu như thế!`
   - *Chuẩn xác:* `Hắn dựa vào cái gì mà dám nhìn cậu như thế!` hoặc `Gã dựa vào cái gì mà dám nhìn cậu như thế!`

---

## 📚 PHẦN 5: BẢNG THUẬT NGỮ CHUẨN HÓA (GLOSSARY)

| Thuật Ngữ Gốc (CN) | Hán Việt / Nghĩa Chuẩn | Bản Dịch Tiếng Việt Chuẩn Xác | Ghi Chú Ngữ Cảnh |
| :--- | :--- | :--- | :--- |
| **穿书** | Xuyên thư | **xuyên thư / xuyên vào sách** | Giữ thể loại xuyên thư quen thuộc. |
| **炮灰** | Pháo hôi | **pháo hôi / kẻ lót đường** | Dùng từ "pháo hôi" khi nói về kịch bản/vai trò. |
| **反派** | Phản phái | **phản diện** | Đại phản diện, kẻ phản diện. |
| **干掉反派** | Cán điệu phản phái | **cán điệu phản diện / xử đẹp phản diện** | Chơi chữ kép giữa "tiêu diệt" và "đè/làm tình". |
| **白月光** | Bạch nguyệt quang | **bạch nguyệt quang / ánh trăng sáng** | Người tình trong mộng không chạm tới được. |
| **替身** | Thế thân | **kẻ thế thân / người đóng thế** | Giản Vân Trầm từng bị coi là thế thân của Khương Vân Hàn. |
| **私生子** | Tư sinh tử | **con riêng / con ngoài giá thú** | Thân phận nhạy cảm của Giản Vân Trầm tại Khương gia. |
| **疯批** | Phong phê | **điên cuồng / kẻ điên rồ** | Hình tượng nội tâm của Tần Mục. |
| **纨绔** | Hoàn khố | **công tử ăn chơi / kẻ ăn chơi trác táng** | Vỏ bọc bề ngoài của Tần Mục. |
| **强强** | Cường cường | **song cường** | Hai bên đều mạnh mẽ, thông minh, bản lĩnh. |
| **主攻** | Chủ công | **chủ công** | Góc nhìn và định hướng theo phía công (Tần Mục). |

---

## 🔍 PHẦN 6: BỘ TIÊU CHUẨN KIỂM ĐỊNH CHẤT LƯỢNG (QC 6 LỚP)

Tất cả các chương trước khi hoàn thành và đánh dấu `qc_approved` bắt buộc phải đạt đủ 6 tiêu chí:

1. **Lớp 1 - Paragraph Count Integrity:** Số đoạn văn của `translation.md` khớp tuyệt đối 1:1 với `source.md` (chênh lệch = 0).
2. **Lớp 2 - Spacing Consistency:** Đúng chuẩn 1 dòng trống (`\n\n`) giữa mọi đoạn văn, không tồn tại dòng nào dính liền `\n`.
3. **Lớp 3 - Dialogue Punctuation:** 100% lời thoại dùng ngoặc kép cong `“...”`.
4. **Lớp 4 - Pronoun & Perspective Consistency:** Ngôi 3 tự sự chuẩn (Tần Mục = "hắn", Giản Vân Trầm = "cậu"), xưng hô đối thoại đúng ma trận, không đá ngôi.
5. **Lớp 5 - Translation Completeness:** Không sót câu, không thêm chi tiết ngoài nguyên tác, câu chữ gọt giũa thuần Việt, giàu cảm xúc.
6. **Lớp 6 - Zero External API Compliance:** Toàn bộ quá trình do Agent tự thân thực thi, đảm bảo không vi phạm quy định bảo tồn hạn ngạch.
