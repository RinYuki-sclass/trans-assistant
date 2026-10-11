---
name: manhwa-chunk-translator
description: >-
  Use this skill to perform multimodal OCR and high-precision translation of Manhwa/Webtoon/Comic images
  using Gemini Pro. It extracts text from speech bubbles, accurately identifies the speaker or narrator
  in the format [Người nói/narrator], binds pronouns based on visual context and project rules, matches punctuation,
  and outputs clean Vietnamese translation compatible with the project's web tools.
---

# Manhwa Chunk Translator (Gemini Pro)

## Purpose
Kỹ năng chuyên sâu sử dụng **Gemini Pro (Multimodal Vision & Deep Reasoning)** để đọc hình ảnh manhwa/webtoon/truyện tranh, trích xuất nguyên bản chữ Hàn từ bóng thoại (OCR cực kỳ chính xác) và dịch sang tiếng Việt tự nhiên, chuẩn sắc thái và ngữ cảnh nhân vật.

---

## 🎯 Model & Cấu Hình Subagent
Khi kích hoạt subagent thực hiện tác vụ này, **luôn chỉ định `Model: "pro"`**:
```python
invoke_subagent(
    Subagents=[{
        "TypeName": "self",
        "Role": "Manhwa Pro Translator",
        "Model": "pro",
        "Prompt": "Dịch ảnh manhwa trong thư mục slices/..."
    }]
)
```

---

## 📐 Định Dạng Đầu Ra Bắt Buộc (Strict Format)

Đầu ra cho mỗi file ảnh phải tuân thủ chính xác cấu trúc sau:

```text
📄 ẢNH: <tên_file_ảnh>

[Người nói/narrator]
KR: <Exact Korean transcription in a SINGLE line>
<Natural Vietnamese translation in a SINGLE line>

[Người nói/narrator]
KR: <Exact Korean transcription in a SINGLE line>
<Natural Vietnamese translation in a SINGLE line>
```

> [!IMPORTANT]
> **Quy Tắc Dòng Đơn (Single Line Rule)**:
> Nếu một bóng thoại chứa nhiều dòng chữ ngắt dòng, **bắt buộc gộp thành 1 dòng đơn duy nhất** (nối bằng dấu cách) ở cả dòng `KR:` và dòng dịch tiếng Việt. Tuyệt đối không giữ các dấu xuống dòng con bên trong cùng một hộp thoại.

---

## 👁️ Nhận Diện Người Nói Qua Thị Giác (Visual Speaker Attribution)

Tận dụng năng lực thị giác sâu sắc của Model Pro để gán nhãn `[Người nói/narrator]`:

1. **Nhìn hướng đuôi bóng thoại (Tail direction)**:
   - Đuôi bóng trỏ về nhân vật nào -> gán tên nhân vật đó: `[Han Yoojin]`, `[Han Yoohyun]`, `[Sung Hyunjae]`, `[Park Yerim]`, `[Song Taewon]`, `[Yoo Myungwoo]`.
2. **Khung chữ nhật dẫn chuyện / Hộp suy nghĩ nền**:
   - Gán `[Narrator]` hoặc `[Độc thoại]` (nếu là suy nghĩ nội tâm của nhân vật chính mà không mở miệng thì ghi rõ `[Yoojin - Độc thoại]`).
3. **Hiệu ứng âm thanh then chốt (Sound Effects)**:
   - Bỏ qua các chữ SFX nhỏ lặt vặt.
   - Nếu là âm thanh quan trọng cho diễn biến (tiếng sấm, đổ vỡ, kỹ năng nổ): gán `[SFX]`.
4. **Nhân vật phụ / Đám đông**:
   - Gán `[Dân chúng]`, `[Thợ săn]`, `[Bang chúng]` hoặc `[Người qua đường]`.
5. **Không xác định được người nói**:
   - Để `[Bóng thoại]`.

---

## ⚖️ Quy Tắc Dịch Thuật & Nhận Diện Bắt Buộc (Rules)

Luôn nạp và tuân thủ chặt chẽ nội dung của 2 file rules:
1. [`.agents/rules/manhwa_translation.md`](file:///d:/Nhung/trans-tool/.agents/rules/manhwa_translation.md): Quy tắc dấu câu, kính ngữ, đại từ xưng hô cố định.
2. [`.agents/rules/manhwa_characters_visual.md`](file:///d:/Nhung/trans-tool/.agents/rules/manhwa_characters_visual.md): Hồ sơ nhận diện ngoại hình (màu tóc, trang phục, ma thú) và manh mối lời thoại quy chiếu cho từng nhân vật.

1. **Punctuation Matching (Tối Thượng)**:
   - Số lượng và vị trí các dấu câu (`!`, `!!`, `?`, `?!`, `~`, `~!!`, `.`, `…`, `….`, `,`, `' '`) ở câu tiếng Việt **phải khớp 100% với dòng KR**.
   - Nếu câu tiếng Hàn là câu lửng không có dấu chấm cuối câu thì câu tiếng Việt cũng **không đặt dấu chấm**.
2. **Từ `형` (Hyung)**:
   - Khi Han Yoohyun gọi Han Yoojin là `형`, **luôn giữ nguyên là `Hyung`**, không dịch thành "anh".
3. **Hậu Tố Xưng Hô Tên Riêng**:
   - `-아` / `-야` -> `-ah` / `-yah` (ví dụ: `유현아` -> `Yoohyun-ah`, `예림아` -> `Yerim-ah`, `유진아` -> `Yoojin-ah`).
   - `-씨` -> `-ssi` (ví dụ: `성현제 씨` -> `Sung Hyunjae-ssi`, `성모 씨` -> `Sungmo-ssi`, `한유진 씨` -> `Han Yoojin-ssi`).
   - `-군` -> `-gun` (ví dụ: `한유진 군` -> `Han Yoojin-gun`).
   - `-양` -> `-yang` (ví dụ: `리에트 양` -> `Liette-yang`).
4. **Kính Ngữ & Tính Lịch Sự**:
   - Đuôi `요`: Không lạm dụng chêm "ạ", dịch tự nhiên theo văn phong truyện tranh.
   - Đuôi `했습니까`, `하십니까`, `하십시오`, `드리다`: Thêm đầy đủ chủ-vị và dùng từ ngữ lịch thiệp thay vì chỉ thêm "ạ".
5. **Bảng Xưng Hô Cốt Lõi**:
   - **Han Yoojin ↔ Han Yoohyun**: Anh – Em (*Yoohyun-ah / em trai*) & Em – Hyung / Anh.
   - **Sung Hyunjae ↔ Han Yoojin**: Tôi – Cậu (*Han Yoojin-gun*) & Tôi – Anh (*Sung Hyunjae-ssi / Sungmo-ssi*).
   - **Park Yerim ↔ Han Yoojin**: Tôi/Bọn mình – Chú/Ahjussi.
   - **Park Yerim ↔ Han Yoohyun**: Tôi – Anh (*Hội trưởng*). Yoohyun gọi Yerim: Tôi – Cô (*Park Yerim*).
   - **Park Yerim ↔ Sung Hyunjae**: Cháu – Chú (*chú Hội trưởng*).
   - **Song Taewon ↔ Han Yoojin**: Tôi – Cậu (*Han Yoojin-ssi*) & Tôi – Anh.
   - **Yoo Myungwoo**: Tự xưng "Tôi".

---

## 🛠️ Prompt Mẫu Khi Gửi Lệnh Cho Model Pro

```text
You are an expert Manhwa/Webtoon translator and typesetter assistant using Gemini Pro Multimodal Vision.

CRITICAL EXHAUSTIVE EXTRACTION MANDATE:
- You MUST detect and extract 100% of all readable text in this image without skipping anything.
- Scan methodically panel-by-panel, from top to bottom, right to left.
- Do NOT skip small speech bubbles, whisper dialogues (dotted border), small handwritten side remarks/thoughts next to characters, rectangular narration/caption boxes, or system message/quest windows.
- If a single speech bubble contains multiple lines of text, join them into a SINGLE line separated by a space in both KR and VI.

TASK:
1. Examine this manhwa image carefully and perform panel-by-panel exhaustive OCR.
2. Transcribe Korean text with 100% precision (do not hallucinate, inspect every stroke).
3. Identify who is speaking [Speaker/narrator] using visual balloon tails, character appearance, and context.
4. Translate into natural Vietnamese adhering strictly to:
   - Punctuation Matching (SUPREME RULE)
   - Specific Name Suffixes (-ah, -ssi, -gun) & Hyung preservation
   - Pronoun rules from manhwa_translation.md and visual profiles from manhwa_characters_visual.md
5. Output in single-line per bubble format:

[Speaker/narrator]
KR: <Korean text on 1 line>
<Vietnamese text on 1 line>
```
