---
name: manhwa-qc-refiner
description: >-
  Use this skill to audit, review, and refine manhwa translation scripts. It ensures accurate
  visual/contextual speaker attribution, eliminates unwanted AI artifact notes, SFX spam, and hallucination loops,
  recovers fragmented raw text into clean Single Line format, enforces project glossary terms, and binds character pronouns strictly.
---

# Manhwa QC & Dialogue Refiner

## Mục Đích
Subagent & Skill chuyên trách hậu kiểm, làm sạch và chuẩn hóa toàn diện file kịch bản dịch truyện tranh manhwa (`script.txt`), khắc phục triệt để các vấn đề thường gặp từ khâu OCR Vision sơ bộ:
1. **Nhận diện đúng nhân vật nói (Visual & Contextual Speaker Grounding)**.
2. **Xóa sạch text rác, SFX vụn vặt và ghi chú do AI tự sinh**.
3. **Bổ sung và phục hồi raw thiếu, hợp nhất câu vụn (Single Line Rule)**.
4. **Đảm bảo 100% chuẩn Glossary**.
5. **Đảm bảo đúng quy chuẩn Xưng hô & Dấu câu**.

---

## 🎯 5 Nhiệm Vụ Trọng Tâm (5 Core Directives)

### 1. Nhận diện đúng nhân vật nói (Speaker Attribution)
- Nhìn hướng đuôi bóng thoại và đối chiếu ngoại hình / văn phong của từng nhân vật:
  - **`[Han Yoojin]`**: Nhân vật chính. Xưng "tôi" - gọi "anh / Sung Hyunjae-ssi", gọi Yoohyun là "em / Yoohyun-ah", gọi Yerim là "nhóc / Yerim-ah".
  - **`[Han Yoohyun]`**: Em trai Yoojin, Hội trưởng Haeyeon. Gọi Yoojin là **`Hyung`** (BẮT BUỘC giữ `Hyung`, không dịch "anh"), xưng "em".
  - **`[Sung Hyunjae]`**: Hội trưởng Sesung. Tóc vàng, mắt hổ phách. Xưng "tôi" - gọi Yoojin là "cậu / Han Yoojin-gun". Văn phong điềm đạm, quý tộc (`~하네`, `~하게`, `~할까`, `~군`).
  - **`[Park Yerim]`**: Thợ săn cấp S Haeyeon (nước/băng). **Tự xưng "tôi"** (hoặc "bọn mình"), **TUYỆT ĐỐI KHÔNG dùng "em" hay "cháu"** với Yoojin. Gọi Yoojin là **"chú" hoặc "Ahjussi"** (chỉ khi raw có `아저씨`). **Bỏ hoàn toàn chữ "ạ"** khi nói chuyện với Yoojin.
  - **`[Iwahata Gakuto]`**: Kiếm sĩ cấp S Nhật Bản (Hội Amaterasu).
  - **`[Noah Rugir]`**: Thợ săn cấp S mang dòng máu rồng, tóc vàng nhạt, rụt rè.
  - **`[Yoo Myungwoo]`**: Thợ rèn cấp SS, bạn thân cùng tuổi Yoojin.
  - **`[Phát thanh viên]` / `[MC]`**: Người bình luận giải đấu/trận đấu.
  - **`[Narrator]` / `[Han Yoojin - Độc thoại]`**: Lời dẫn chuyện / suy nghĩ nội tâm.

### 2. Xóa các text không cần thiết & Note AI tự sinh (Clean AI Artifacts)
- **Xóa bỏ các ghi chú AI rác:**
  - *"Không có văn bản nào trong hình ảnh này."*
  - *"No Korean text detected in the image."*
  - Tiền tố thừa: `VI: `, `KR: ` thừa lặp lại, dấu ngoặc nhọn `<...>`.
- **Triệt tiêu vòng lặp Hallucination:** Loại bỏ các chuỗi lặp vô tận (ví dụ hàng trăm/nghìn dòng lặp `[Người nói/narrator] KR: 으음… <Ưm…>`).
- **Xóa văn bản bịa đặt:** Xóa các đoạn trần thuật giả tưởng không có trong ảnh gốc.
- **Lược bỏ SFX vụn:** Chỉ giữ lại SFX lớn có ý nghĩa cốt truyện (nổ, sấm sét, đổ vỡ).

### 3. Bổ sung & phục hồi raw thiếu (Single Line Rule)
- Khắc phục tình trạng một câu nói bị OCR ngắt thành 5-10 dòng vụn. Ghép lại thành **1 dòng đơn duy nhất** ở cả dòng `KR:` và câu dịch tiếng Việt.
- Sửa lỗi nhận diện ký tự OCR:
  - `쥐 보게` $\rightarrow$ `이것 보게` (Xem này).
  - `참고` trong ngữ cảnh chịu đựng gian nan $\rightarrow$ Dịch là "chịu đựng / nhẫn nhịn", tuyệt đối không dịch là "tham khảo".

### 4. Đảm bảo đúng Glossary & Danh từ Đời sống (Natural Noun Mandate)
- **Thuật ngữ thế giới Hunter:**
  - `화염뿔사자` $\rightarrow$ **Độc Giác Hỏa Sư** (không dùng Hỏa Giác Sư).
  - `경기장` $\rightarrow$ **võ đài** (trong đấu trường giải đấu).
  - `던전` $\rightarrow$ **ngục tối**.
  - `게이트석` $\rightarrow$ **Môn thạch**.
  - `그림자 없는 낮` $\rightarrow$ **Vô Ảnh Nhật**.
  - `물의 지배자` $\rightarrow$ **Kẻ Trị Thủy**.
  - `수능` $\rightarrow$ **kỳ thi đại học** (không để CSAT thô).
  - Tên bang hội: **Haeyeon (해연)**, **Sesung (세성)**, **Amaterasu (아마테라스)**.
- **QC Lỗi Danh từ ghép ngô nghê / Dịch máy móc (Anti-Literal Compound Nouns):**
  - Tuyệt đối không dịch ghép từng chữ tạo ra danh từ không có trong tiếng Việt.
  - `가벽` (假壁) $\rightarrow$ BẮT BUỘC dùng **"vách ngăn"** hoặc **"bức vách"** (CẤM dùng *"tường ngăn"* hay *"tường giả"*).
  - `지지대` (trong ẩn dụ tâm lý nâng đỡ chống sụp đổ) $\rightarrow$ Dùng **"trụ đỡ"** hoặc **"điểm tựa vững chắc"** (không dùng *"chỗ dựa"* chung chung hay *"giá đỡ"*).
  - `옷 깃 방향` (Yukata/Kimono) $\rightarrow$ **"vạt áo bị cài ngược bên"** (CẤM dùng *"hướng vạt áo"*).
  - `허리끈` $\rightarrow$ **"đai lưng"** hoặc **"thắt lưng"** (CẤM dùng *"dây đai áo"*).
  - `길드 독점` $\rightarrow$ **"các hội lớn độc quyền"** (không dùng *"bang hội độc chiếm"*).
  - `던전을 걸고` $\rightarrow$ **"đặt cược các ngục tối"** (không dùng *"tiền cược là các ngục tối"*).
  - `심의` (kiểm duyệt độ tuổi/thuần phong mỹ tục) $\rightarrow$ BẮT BUỘC nhận diện đúng **"quy chuẩn kiểm duyệt"** (CẤM OCR nhầm thành `샘의` - *suối nguồn*).
  - `양복` $\rightarrow$ Ưu tiên **"bộ vest"** tự nhiên thay vì lạm dụng từ *"âu phục"*.

### 5. Đảm bảo đúng Xưng hô & Dấu câu
- Khớp 100% số lượng và vị trí dấu câu (`!`, `!!`, `?`, `?!`, `~`, `~!!`, `.`, `…`, `,`).
- Không để đại từ nhảy lung tung giữa các câu liên tiếp.
- **Khóa cứng Hậu tố Tên riêng:** BẮT BUỘC giữ nguyên dạng `-ah` / `-yah`. `유현아` **LUÔN CHỐT LÀ `Yoohyun-ah`** (TUYỆT ĐỐI CẤM dịch thành *"Yoohyun à"* hay *"Yoohyun ơi"*), `유진아` $\rightarrow$ `Yoojin-ah`, `예림아` $\rightarrow$ `Yerim-ah`.
- **Chống lặp từ `참다` (Đa dạng hóa vốn từ nhẫn nại / chịu đựng):** Tuyệt đối không dịch máy móc lặp từ *"chịu đựng"* nhiều lần trong cùng 1 phân cảnh. Phân hóa tinh tế sang: *“cam chịu thiệt thòi”*, *“nén lòng, cắn răng nuốt cay đắng”*, *“gồng mình nén nhịn”*, *“kiên nhẫn chờ đợi”*.

---

## 📐 Định Dạng Đầu Ra Chuẩn
```text
📄 ẢNH: <tên_file>

[Người nói/narrator]
KR: <Dòng tiếng Hàn chuẩn trên 1 dòng>
<Dòng tiếng Việt chuẩn trên 1 dòng>
```
