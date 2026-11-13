# AGENTS.md - WORKSPACE CODING & TRANSLATION AGENT GUIDELINES

Tài liệu này xác định các quy tắc cốt lõi áp dụng cho AI Code Agent (Antigravity IDE) khi làm việc trong **TOÀN BỘ SOURCE** của workspace `trans-assistant`.

---

## ⛔ QUY TẮC TỐI THƯỢNG: TOÀN BỘ SOURCE KHÔNG DÙNG GOOGLE API KEY (UNIVERSAL ZERO GOOGLE API KEY MANDATE)

> 🚨 **QUY TẮC BẮT BUỘC ÁP DỤNG CHO TOÀN BỘ SOURCE:**  
> Mọi mệnh lệnh từ người dùng gửi tới Coding Agent (ví dụ: *"dịch"*, *"dịch tiếp"*, *"chạy đi"*, *"tiếp tục"*, *"liên hoàn"*, *"chạy batch"*, *"OCR manhwa"*, *"soát lỗi QC"*, *"pre-scan"*, v.v.):
> 
> 1. **AI Code Agent BẮT BUỘC PHẢI TỰ THÂN THỰC HIỆN TRỰC TIẾP:**
>    - Agent tự đọc nội dung thô (`source.md`, raw text, ảnh manhwa trong `slices/`, tài liệu dự án) bằng các công cụ đọc file (`view_file`).
>    - Agent tự phân tích ngữ cảnh, đối chiếu quy chuẩn nhân vật / xưng hô trong `AGENTS.md` của từng dự án hoặc `memory/`.
>    - Agent trực tiếp biên dịch, OCR, phân tích, sinh văn bản tiếng Việt chuẩn xác, mượt mà, văn phong sắc bén, bảo toàn 1:1 số đoạn và đúng khoảng cách `\n\n`.
>    - Agent trực tiếp lưu file kết quả (`translation.md`, `qc_report.md`, `meta.json`, `timeline.json`) bằng `write_to_file`.
> 
> 2. **TUYỆT ĐỐI CẤM GỌI TOOL / SCRIPT BÊN NGOÀI THÔNG QUA GOOGLE API KEY TRÊN TOÀN SOURCE:**
>    - ❌ **CẤM:** Tuyệt đối không chạy bất kỳ script Python, batch file hay công cụ nào gọi API ngoài qua `GEMINI_API_KEY`, `GOOGLE_API_KEY` (như thư viện `google.genai`, `google-generativeai`, Google Cloud vertex/translate).
>    - ❌ **LÝ DO:** Tránh triệt để phát sinh lỗi **429 Resource Exhausted** (hạn mức RPM/TPM), tránh lỗi **503 High Demand** làm gián đoạn công việc, và bảo toàn 100% quota/credit của người dùng.
>    - AI Agent sở hữu năng lực thấu hiểu ngữ cảnh lớn và văn phong tốt nhất, do đó Agent tự thực thi đem lại chất lượng tối ưu và ổn định tuyệt đối.

---

## 📖 CÁC QUY CHUẨN ĐỊNH DẠNG & VĂN PHONG TIỂU THUYẾT & MANHWA

1. **Khoảng cách đoạn văn chuẩn `\n\n`:**
   - Mọi đoạn văn trần thuật hoặc lời thoại bắt buộc phải có đúng 1 dòng trống (`\n\n`) ngăn cách.
   - Tuyệt đối không để dính dòng (`\n`).

2. **Dấu ngoặc kép chuẩn `“...”`:**
   - Lời thoại tiểu thuyết sử dụng ngoặc kép cong tiếng Việt `“...”`, không dùng gạch đầu dòng `-`.

3. **Bảo toàn 100% nguyên tác (1:1 Paragraph Alignment):**
   - Số đoạn văn tiếng Việt phải khớp chính xác 1:1 với số đoạn văn gốc. Không tự gộp hoặc chẻ đoạn.

4. **Nguyên tắc Tự Hành Liên Hoàn - Cấm Bẫy Dừng Hội Thoại (Zero Conversational Pause):**
   - Khi chạy chế độ tự hành (auto pilot / continuous batch), Agent tuyệt đối **không tự tạo điểm dừng** giữa các chương bằng các câu chat như *"Bạn chỉ cần nhắn 'tiếp tục' hoặc 'dịch tiếp'..."* hay *"Kế hoạch batch tiếp theo... hãy nhắn để tiếp tục"*.
   - Agent phải chủ động gọi tool nạp chương kế tiếp và thực thi tiếp tục không gián đoạn cho đến khi hoàn thành toàn bộ batch được giao hoặc gặp Circuit Breaker.

5. **Quản lý Đại từ & Nhân vật (Pronoun Binding):**
   - Tuân thủ nghiêm ngặt ma trận đại từ của từng dự án trong `novel_projects/<slug>/AGENTS.md` và `.agents/rules/novel_pronoun_conventions.md`.

6. **Phân định tuyệt đối giữa Lời thoại trực tiếp vs Trần thuật / Độc thoại nội tâm & Cặp xưng hô hiện đại:**
   - **Lời thoại trực tiếp trong ngoặc kép `“...”`:** Tuân thủ ngữ cảnh cảm xúc của nhân vật (khi phẫn nộ, chửi bới có thể dùng `“mày - tao”`, `“ngươi - ta”` theo quy chuẩn từng dự án).
   - **Quy tắc cặp xưng hô "tao - mày" trong bối cảnh hiện đại:**
     - Trong bối cảnh hiện đại (đô thị, showbiz, vườn trường, hào môn...), khi nhân vật trong lời thoại đối thoại trực tiếp (`“...”`) tự xưng là **"tao"** (ngôi 1), thì **BẮT BUỘC CHỈ ĐƯỢC GỌI NGƯỜI NGHE LÀ "mày"** (ngôi 2: cặp xưng hô đồng bộ `tao - mày`).
     - **TUYỆT ĐỐI CẤM** hiện tượng lai tạp, đá ngôi: Xưng `tao` nhưng lại gọi người nghe là `anh`, `cậu`, `hắn`, `ngươi`, `ông`, `chú`, `cô`, v.v.
     - *Ví dụ sai:* `“Tao cảnh cáo anh/cậu...”`, `“Tao nói cho các người biết...”`, `“Tao tha cho anh lần này...”`.
     - *Ví dụ đúng:* `“Tao cảnh cáo mày...”`, `“Tao nói cho tụi mày biết...”`, `“Tao tha cho mày lần này...”`.
   - **Trần thuật / Độc thoại nội tâm không ngoặc kép:** **TUYỆT ĐỐI CẤM** đem đại từ đối thoại ngôi 2/ngôi 1 (`mày`, `tao`) vào câu trần thuật hoặc suy nghĩ nội tâm ngôi 3, tránh gây hiện tượng "đá ngôi" phi logic.
   - *Ví dụ sai:* `Mày dựa vào cái thớ gì mà dám ghét cậu chứ!` (lẫn lộn `mày` ngôi 2 và `cậu` ngôi 3).
   - *Ví dụ đúng chuẩn ngôi 3:* `Hắn dựa vào cái thớ gì mà dám ghét cậu chứ!`

7. **Định dạng thoại Manhwa:**
   - Tuân thủ cấu trúc `[Người nói/narrator]` kèm KR: và câu dịch VI theo đúng [.agents/rules/manhwa_translation.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/manhwa_translation.md).

8. **Kiến Trúc Subagent Song Song (Parallel Subagent Architecture):**
   - Khi chạy batch lớn, Orchestrator được phân luồng cho nhiều Worker Subagent (`self`) chạy song song độc lập từng chương (Phase 1-3).
   - Worker chỉ ghi vào thư mục riêng của chương (`chapters/ch_xxx/`), cấm ghi file dùng chung để chống Race Condition.
   - Main Orchestrator gom kết quả và đồng bộ hóa Phase 4 (`timeline.json`, `chapters_index.json`, `TOC.md`), sau đó tự động nạp đợt worker kế tiếp.
