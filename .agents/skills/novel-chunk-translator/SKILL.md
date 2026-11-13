---
name: novel-chunk-translator
description: >-
  Use this skill to translate raw novel chapters with strict 1:1 paragraph alignment, zero addition,
  zero omission, exact pronoun binding, and mandatory '\n\n' paragraph spacing according to project AGENTS.md.
---

# Novel Chunk Translator Subagent

## Purpose
Translates raw novel content (`chapters/ch_xxx/source.md`) into fluent, faithful Vietnamese while strictly obeying project-specific `AGENTS.md` guidelines, verified glossary/pronoun decisions, and **Phrase-by-Phrase Scene Pronoun Locking** in **Continuous Execution Mode (Dịch liên hoàn toàn bộ Phrase trong chương không dừng hỏi)**.

---

## ⚡ CƠ CHẾ DỊCH THEO PHRASE / SCENE-CHUNK LIÊN HOÀN (CONTINUOUS PHASE 2)

Khi dịch một chương dài (60 – 180+ đoạn), để ngăn chặn triệt để hiện tượng **Mỏi Ngữ Cảnh (Context Fatigue)** và **Trôi Đại Từ (Pronoun Drift)**:

1. **Phân đoạn theo Phrase (25 – 40 đoạn/lượt):**
   - Không nạp nguyên một chương quá dài vào dịch dồn 1 lần.
   - Bẻ chương thành các Phrase theo phân cảnh tự nhiên (Scene Chunk) dựa trên `phrase_scene_map.json` hoặc bóc tách ngữ cảnh.
   - Mỗi Phrase có tập hợp nhân vật xuất hiện cụ thể (Active Cast).

2. **Khóa Cặp Xưng Hô Phân Cảnh (Scene Pronoun Locking):**
   - Trước khi dịch mỗi Phrase, Agent kích hoạt **Chỉ thị khóa đại từ** cho phân cảnh đó.
   - Ví dụ trong cảnh Công gặp Thụ: cặp xưng hô đã chọn là gì thì 100% các câu thoại trong cảnh đó phải khóa chặt cặp đó, cấm nhảy xưng hô giữa chừng.

3. **Nguyên tắc Tự Hành Liên Hoàn (Zero-Wait Autonomous Rule):**
   - Agent tự động dịch tuần tự Phrase 1 -> Phrase 2 -> Phrase 3 -> Phrase N trong cùng một tiến trình.
   - **TUYỆT ĐỐI CẤM** dừng lại sau Phrase 1 để hỏi *"Có muốn dịch tiếp phrase 2 không?"*.
   - Ráp nối toàn bộ các Phrase thành bản dịch 1:1 hoàn chỉnh và ghi thẳng vào `chapters/ch_xxx/translation.md`.

---

## 🛡️ NGUYÊN TẮC PHÒNG NGỪA CHARACTER & PRONOUN DRIFT

Khi dịch các bộ truyện thuộc `novel_projects/**`, dịch giả AI phải tuân thủ nghiêm ngặt bảng ma trận đại từ trong `AGENTS.md` của từng dự án và rules:

### 1. Quy tắc Ngôi Kể Thứ 3 Trần Thuật (Narrative):
* Tuân thủ hướng dẫn đại từ (`anh`, `cậu`, `y`, `hắn`, `gã`) theo bối cảnh truyện.
* **Chủ công:** POV Anchor thường dùng `"anh"` (hoặc `"hắn"` trong tiên hiệp); Thụ dùng `"cậu"` (thiếu niên, giả ngoan), hoặc `"hắn"` (Cường Thụ u ám, tướng quân), hoặc `"y"` (cổ đại/tiên hiệp).
* **Niên hạ:** Khi Thụ lớn tuổi hơn Công: bắt buộc Công là `"cậu"`, Thụ là `"anh"`.
* **Phản diện / Tra nam:** Dùng `"hắn"`, `"cậu ta"`, `"gã"`, `"gã ta"`. CẤM dùng `"anh"`, `"cậu"`.
* **Nhân vật phụ lớn tuổi:** Luôn dùng `"ông"`, `"bà"`, `"bác"`.

### 2. Quy tắc Xưng Hô Đối Thoại Trực Tiếp (Dialogue):
* **Cặp Công - Thụ:** Theo đúng quy định của từng bộ trong `AGENTS.md`. CẤM hiện tượng "anh - anh" giữa 2 người nam trong cùng phân cảnh.
* **Speaker Tracking chủ động:** Luôn xác định ai là người mở miệng nói trước khi chọn đại từ xưng hô trong câu thoại.
* **Khóa Xưng Hô Phân Cảnh (Scene Pronoun Locking):** Trong cùng một cảnh đối thoại giữa 2 nhân vật, cặp xưng hô phải nhất quán xuyên suốt. CẤM câu trước gọi `"cậu"`, câu sau bỗng đổi thành `"ngươi"`.
* **Đồng bộ cặp xưng hô "tao - mày" trong bối cảnh hiện đại:**
  - Trong lời thoại trực tiếp ở bối cảnh hiện đại, khi người nói tự xưng là **"tao"** (ngôi 1), thì **BẮT BUỘC CHỈ ĐƯỢC GỌI NGƯỜI NGHE LÀ "mày"** (ngôi 2: cặp `tao - mày` bất di bất dịch).
  - **TUYỆT ĐỐI CẤM** hiện tượng lai tạp đá ngôi: xưng `tao` nhưng lại gọi đối phương là `anh`, `cậu`, `hắn`, `ngươi`, `ông`, `chú`, v.v. (Ví dụ SAI: `“Tao cảnh cáo anh/cậu...”` ➔ Bắt buộc: `“Tao cảnh cáo mày...”`).
* **Cấm rò rỉ mày/tao vào trần thuật nội tâm (Dialogue-to-Narrative Bleeding):**
  - Khi nhân vật thoại giận dữ dùng `“mày - tao”` trong ngoặc kép `“...”`, các câu trần thuật hoặc suy nghĩ nội tâm liền kề (không có ngoặc kép) **TUYỆT ĐỐI KHÔNG ĐƯỢC** dịch thành `mày`, `tao`. Bắt buộc phải duy trì ngôi thứ 3 (`hắn`, `anh`, `y`, `cậu`).

---

## 📌 CÁC NGUYÊN TẮC BẢO TOÀN NGUYÊN TÁC 1:1

1. **Zero Omission & Zero Addition:**
   - Dịch toàn bộ từng câu thoại, hành động, biểu cảm, âm thanh.
   - Không bỏ sót câu thoại ngắn hoặc từ cảm thán. Không chêm bình phẩm, không phóng tác thêm bớt.
2. **Bảo toàn số đoạn 1:1 (Paragraph Alignment):**
   - Mỗi đoạn văn gốc phải ứng đúng với 1 đoạn văn tiếng Việt.
   - Không gộp nhiều đoạn ngắn thành một đoạn dài, không chẻ nhỏ một đoạn.
3. **Khoảng cách đoạn chuẩn (`\n\n`):**
   - Mọi đoạn văn trần thuật và lời thoại **bắt buộc phải cách nhau đúng 1 dòng trống (`\n\n`)**.
   - Tuyệt đối không để dính dòng (`\n`).
4. **Dấu ngoặc kép cong tiếng Việt:**
   - Sử dụng ngoặc kép cong `“...”` cho lời thoại, không dùng gạch đầu dòng `-`.

---

## ⛔ QUY TẮC TỐI THƯỢNG (UNIVERSAL ZERO GOOGLE API KEY MANDATE)
Subagent / AI Code Agent PHẢI tự dịch trực tiếp trong context. Tuyệt đối KHÔNG chạy script trung gian hay gọi bất kỳ tool nào sử dụng `GEMINI_API_KEY` hay Google API Key bên ngoài.
