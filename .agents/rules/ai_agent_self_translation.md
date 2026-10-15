---
description: QUY TẮC TỐI THƯỢNG TOÀN SOURCE - AI Code Agent tuyệt đối không dùng Google API Key, tự thân thực thi trực tiếp mọi tác vụ
globs: ["**/*"]
alwaysApply: true
---

# ⛔ QUY TẮC TỐI THƯỢNG TOÀN SOURCE: CODING AGENT KHÔNG DÙNG GOOGLE API KEY (UNIVERSAL ZERO GOOGLE API KEY POLICY)

> 🚨 **PHẠM VI ÁP DỤNG:**  
> Áp dụng cho **TOÀN BỘ SOURCE** của workspace `trans-assistant` (mọi thư mục, mọi dự án tiểu thuyết `novel_projects/**`, manhwa/webtoon `input/`, `output/`, `memory/`, `scripts/`, `pages/`, v.v.).

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Coding Agent Tự Thân Thực Thi Trực Tiếp (100% In-Context Direct Execution):**
   - Khi nhận bất kỳ mệnh lệnh nào từ người dùng (dịch thuật, OCR truyện tranh, tiền quét QA/pre-scan, kiểm duyệt QC, cập nhật timeline/lorekeeper, định dạng xuất bản, phân tích mã nguồn, v.v.), **AI Code Agent (Coding Agent trong Antigravity IDE) BẮT BUỘC PHẢI tự mình thực thi trực tiếp** bằng trí tuệ, ngữ cảnh sâu và các công cụ sẵn có của Agent (`view_file`, `write_to_file`, `replace_file_content`, v.v.).
   - Agent tự đọc nội dung thô (raw text, file markdown, hình ảnh), tự suy luận chuyển ngữ, tự định dạng văn bản chuẩn xác và tự lưu file kết quả.

2. **TUYỆT ĐỐI CẤM SỬ DỤNG GOOGLE API KEY DƯỚI MỌI HÌNH THỨC:**
   - ❌ **CẤM:** Coding agent tuyệt đối **KHÔNG ĐƯỢC CHẠY** bất kỳ file script, tool, CLI command, hoặc batch job nào gọi ra bên ngoài sử dụng Google API Key (`GEMINI_API_KEY`, `GOOGLE_API_KEY`, `google.genai`, `google-generativeai`, Google Cloud Vertex AI, Google Cloud Translation, v.v.).
   - ❌ **CẤM:** Không viết thêm hoặc thực thi các script trung gian tiêu tốn quota API key của người dùng.
   - ❌ **LÝ DO KỸ THUẬT & TRẢI NGHIỆM:**
     - Tránh triệt để mã lỗi **429 Too Many Requests / Resource Exhausted** do cạn hạn mức RPM/TPM của Google API.
     - Tránh mã lỗi **503 Service Unavailable / High Demand** làm sập quy trình tự động.
     - Bảo vệ 100% tài nguyên, chi phí và hạn mức cá nhân của người dùng trên Google AI Studio.
     - Năng lực suy luận và cửa sổ ngữ cảnh cực lớn của AI Code Agent trong Antigravity IDE vượt trội và ổn định hơn rất nhiều so với việc gọi script API đơn lẻ.

---

## 2. QUY CHUẨN THỰC THI CHO TỪNG LUỒNG CÔNG VIỆC TRÊN TOÀN SOURCE

### A. Luồng Dịch Thuật Tiểu Thuyết (Novel Projects & Input/QC):
- Agent tự mở `chapters/ch_xxx/source.md` hoặc `input/*.md` bằng `view_file`.
- Tự đối chiếu bảng xưng hô, đại từ, glossary trong `AGENTS.md` và `memory/`.
- Tự dịch từng đoạn 1:1, bảo toàn đúng số đoạn, cách nhau đúng 1 dòng trống (`\n\n`), dấu thoại `“...”`.
- Tự ghi bản dịch vào `chapters/ch_xxx/translation.md` bằng `write_to_file`.
- Tự chạy QC audit, tạo `qc_report.md` và cập nhật `meta.json` (`status: "qc_approved"`), cập nhật `memory/timeline.json`.

### B. Luồng Manhwa / Webtoon / Comic:
- Khi nhận lệnh dịch manhwa hoặc trích xuất bong bóng thoại: Coding Agent tự đọc và phân tích ảnh bằng năng lực multimodal có sẵn, tự nhận diện người nói `[Người nói/narrator]` và xuất kết quả trực tiếp, **không chạy script Python gọi GenAI API**.

### C. Luồng Tiền Quét (Pre-scan) & Cập Nhật Tri Thức (Lorekeeper):
- Tự trích xuất danh từ riêng, nhân vật mới và lập bảng QA trực tiếp trên file, không dùng API key.

---

## 3. CHECKLIST TUÂN THỦ DÀNH CHO CODING AGENT
- [ ] Không import hoặc chạy code gọi `google.genai` / `os.getenv("GEMINI_API_KEY")`.
- [ ] Mọi bản dịch và xử lý dữ liệu đều do chính Coding Agent sinh ra trực tiếp.
- [ ] Giữ nguyên 100% hạn mức API key của user, đảm bảo quy trình thông suốt không gián đoạn.
