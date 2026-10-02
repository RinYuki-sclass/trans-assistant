---
name: novel-chunk-translator
description: >-
  Use this skill to translate raw novel chapters with strict 1:1 paragraph alignment, zero addition,
  zero omission, exact pronoun binding, and mandatory '\n\n' paragraph spacing according to project AGENTS.md.
---

# Novel Chunk Translator Subagent

## Purpose
Translates raw novel content (`chapters/ch_xxx/source.md`) into fluent, faithful Vietnamese while strictly obeying project-specific `AGENTS.md` guidelines and verified glossary/pronoun decisions.

---

## ⛔ NGUYÊN TẮC PHÒNG NGỪA CHARACTER & PRONOUN DRIFT NGAY TỪ KHÂU DỊCH

Khi dịch các bộ truyện thuộc `novel_projects/**`, để không bị bắt lỗi ở khâu QC, dịch giả AI phải tuân thủ nghiêm ngặt bảng ma trận đại từ trong `AGENTS.md` của từng dự án và [novel_pronoun_conventions.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/novel_pronoun_conventions.md) (các dự án ngoài `novel_projects` như SVR/Hunter dịch theo glossary riêng):

### 1. Quy tắc Ngôi Kể Thứ 3 Trần Thuật (Narrative):
* **Tra cứu ma trận thể loại:** Tuân thủ hướng dẫn đại từ (`anh`, `cậu`, `y`, `hắn`, `gã`) theo bối cảnh trong [novel_pronoun_conventions.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/novel_pronoun_conventions.md).
* **Quy tắc Tuổi Tác & Phân ngôi trong truyện Chủ công:**
  - **Mặc định (Công lớn tuổi hơn hoặc ngang hàng):** Công làm POV Anchor dùng đại từ `"anh"` (hoặc `"hắn"` trong tiên hiệp); Thụ dùng `"cậu"` (thiếu niên, giả ngoan), hoặc `"hắn"` (Cường Thụ u ám, tướng quân), hoặc `"y"` (cổ đại/tiên hiệp).
  - ⭐ **ĐẶC BIỆT KHI THỤ LỚN TUỔI HƠN CÔNG (Niên hạ công x Niên thượng thụ):** Bắt buộc tuân thủ quy tắc tuổi tác: **Công là `"cậu"`**, **Thụ là `"anh"`**.
* **Tra công / Phản diện nam (Lệ Yến Trạch, Friedrich):** Dùng `"hắn"` (tuyệt đối KHÔNG dùng `"anh"`).
* **Phản diện giả tạo / Trà xanh (Chu Lạc Lạc, Felo, Elio):** Dùng `"gã"`, `"gã ta"`, `"hắn"` (tuyệt đối KHÔNG dùng `"cậu"`, `"cậu ta"`).
* **Quy tắc Nhập Xác:** Khi Công đã nhập vào thân xác (dù tác giả ghi Ryan hay Tống Lạc An), toàn bộ hành động và tâm tư của nhân vật chính đều quy nhất về `"anh"`.

### 2. Quy tắc Xưng Hô Đối Thoại Trực Tiếp (Dialogue):
* **Cặp Công - Thụ:**
  * Công (Sở Tư Thừa): Xưng `"tôi"`, gọi Thụ là `"anh"` / tên riêng / danh xưng.
  * Thụ (Alex / Thẩm Từ): Xưng `"tôi"`, gọi Công là `"cậu"` (❌ **TUYỆT ĐỐI CẤM** Thụ gọi Công là `"anh"`).
  * ❌ **CẤM HIỆN TƯỢNG ANH - ANH:** Không để 2 người nam cùng gọi nhau là "anh - anh" trong cùng một phân cảnh đối thoại.
* **Speaker Tracking chủ động:** Luôn xác định ai là người mở miệng nói trước khi chọn đại từ xưng hô trong câu thoại.
* **Tiếng lòng vs Lời nói:** Phân tách rõ ràng giữa tiếng lòng đọc tâm trong ngoặc vuông `【...】` và lời nói phát ra ngoài miệng trong ngoặc kép `“...”`.
* **Khóa Xưng Hô Phân Cảnh (Scene Pronoun Locking):** Trong cùng một cảnh đối thoại giữa 2 nhân vật, cặp xưng hô phải nhất quán xuyên suốt. CẤM câu trước gọi `"cậu"`, câu sau bỗng đổi thành `"ngươi"`.
* **Kế thừa đại từ cho câu phán xét không ngoặc kép:** Khi đoạn văn trần thuật tiếp nối lời thoại chứa đại từ ngôi 2 (`你` / `너`) mang tính phán xét, chất vấn trực tiếp đối phương, BẮT BUỘC phải kế thừa đại từ của câu thoại liền trước (`cậu` đi với `cậu`, `ngươi` đi với `ngươi`).

---

## ⛔ CÁC NGUYÊN TẮC BẢO TOÀN NGUYÊN TÁC 1:1

1. **Zero Omission & Zero Addition**:
   - Dịch toàn bộ từng câu thoại, hành động, biểu cảm, âm thanh.
   - Không bỏ sót câu thoại ngắn hoặc từ cảm thán (ví dụ: `- Kyooc!`, `뀩!`, `“……”`).
   - Không chèn bình phẩm hay tự phóng tác thêm bớt.

2. **Bảo toàn số đoạn 1:1 (Paragraph Alignment)**:
   - Mỗi đoạn văn gốc phải ứng đúng với 1 đoạn văn tiếng Việt.
   - Không gộp nhiều đoạn ngắn thành một đoạn dài, không chẻ nhỏ một đoạn.

3. **Khoảng cách đoạn chuẩn (`\n\n`)**:
   - Mọi đoạn văn trần thuật và lời thoại **bắt buộc phải cách nhau đúng 1 dòng trống (`\n\n`)**.
   - Tuyệt đối không để các dòng dính liền kề nhau (`\n`).

4. **Tên phương Tây & Thuật ngữ**:
   - Tuyệt đối giữ nguyên tên tiếng Anh/phương Tây: `Alex`, `Ryan`, `Friedrich`, `Felo`, `Heideman`, `Sachsen`... CẤM phiên âm Hán-Việt.
   - Không dùng lượng từ sai (dùng `thư trùng`, `hùng trùng`, cấm dùng `con thư trùng`, `con hùng trùng`).
   - Giữ nguyên hậu tố thân mật tiếng Hàn nếu có (`-ie`, `-ah`, `-yah`).

---

## 🛠️ QUY TRÌNH THỰC HIỆN DỊCH

1. Đọc kỹ `AGENTS.md` của dự án và các cặp xưng hô đã được duyệt trong `qa_clarifications.md`.
2. Dịch từng chunk đoạn và kiểm tra số đoạn: `len(source_paragraphs) == len(trans_paragraphs)`.
3. Lưu kết quả vào `chapters/ch_xxx/translation.md`.
