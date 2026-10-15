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

4. **Quản lý Đại từ & Nhân vật (Pronoun Binding):**
   - Tuân thủ nghiêm ngặt ma trận đại từ của từng dự án trong `novel_projects/<slug>/AGENTS.md` và `.agents/rules/novel_pronoun_conventions.md`.

5. **Định dạng thoại Manhwa:**
   - Tuân thủ cấu trúc `[Người nói/narrator]` kèm KR: và câu dịch VI theo đúng [.agents/rules/manhwa_translation.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/manhwa_translation.md).
