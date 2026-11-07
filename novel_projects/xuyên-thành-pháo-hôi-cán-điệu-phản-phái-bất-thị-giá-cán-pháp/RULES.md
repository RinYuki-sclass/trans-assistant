# WORKSPACE RULES & PIPELINE CONVENTIONS: XUYÊN-THÀNH-PHÁO-HÔI-CÁN-ĐIỆU-PHẢN-PHÁI-BẤT-THỊ-GIÁ-CÁN-PHÁP

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)
- **Universal Zero Google API Key Mandate:** Toàn bộ công việc dịch thuật, kiểm định QC, cập nhật timeline/memory đều do Agent tự thân thực thi. Tuyệt đối không gọi Google API ngoài.
- **1:1 Paragraph Alignment:** Bản dịch tiếng Việt phải tương ứng 1:1 với số đoạn văn gốc trong `source.md`.
- **Formatting `\n\n`:** Giữa các đoạn trần thuật và lời thoại phải cách nhau đúng một dòng trống.
- **Ngoặc kép cong `“...”`:** Dành cho tất cả các câu thoại trực tiếp.

## 2. QUY TRÌNH DỊCH TỪNG CHƯƠNG (4 PHA TIÊU CHUẨN)
- **Pha 1 (Pre-scan QA):** Quét các từ ngữ mới, tên riêng, kiểm tra ma trận đại từ, tạo `qa_clarifications.md`.
- **Pha 2 (Dịch thuật 1:1):** Dịch trung thực, mượt mà, văn phong đam mỹ chủ công song cường, lưu vào `translation.md`.
- **Pha 3 (Soát lỗi QC Multi-layer):** Kiểm tra 6 tiêu chí QC, tạo `qc_report.md` và `meta.json`.
- **Pha 4 (Cập nhật Memory & Tiến độ):** Cập nhật `timeline.json`, đồng bộ trạng thái trong `chapters_index.json` và `TOC.md`.
