# AI Novel Translation Tool (Trans-Tool)

Công cụ hỗ trợ dịch thuật tiểu thuyết tự động sử dụng Google Gemini AI, tối ưu cho việc dịch từ tiếng Anh/Hàn sang tiếng Việt với hệ thống quản lý Thuật ngữ (Glossary) và Kiểm soát chất lượng (QC).

## 🚀 Tính năng chính
- **Dịch thuật 2 bước (Translate & Refine):** Dịch thô từ tiếng Anh, sau đó đối chiếu với bản gốc tiếng Hàn để tinh chỉnh câu từ.
- **Quản lý Glossary:** Đảm bảo nhất quán tên nhân vật và thuật ngữ.
- **Personal Notes:** Ưu tiên các điều chỉnh cá nhân (ví dụ: đổi tên nhân vật, cách xưng hô cụ thể).
- **Hệ thống QC Review:** Tự động phát hiện lỗi dịch thuật, sai thuật ngữ hoặc thiếu sót so với bản gốc.

---

## 🛠 Cấu hình hệ thống

### 1. Yêu cầu phần mềm
- Đã cài đặt [Python 3.9+](https://www.python.org/downloads/).
- Cài đặt thư viện cần thiết:
  ```bash
  pip install google-genai
  ```

### 2. Cấu hình API Key
Mở file `scripts/main.py` và `scripts/qc_review.py`, tìm dòng:
```python
local_key = "AIzaSy..." # Thay bằng API Key Gemini của bạn
```
*Lưu ý: Bạn nên sử dụng Environment Variable `GEMINI_API_KEY` để bảo mật tốt hơn.*

---

## 📖 Hướng dẫn sử dụng

### 1. Dịch thuật chương mới
1. Copy nội dung tiếng Anh vào: `input/trans/eng.txt`
2. Copy nội dung tiếng Hàn vào: `input/trans/kor.txt`
3. Cập nhật thuật ngữ mới (nếu có) vào: `glossary/glossary.md` hoặc `glossary/personal_notes.md`
4. Chạy file: **`CHAY_DICH_THUAT.bat`**
5. Kết quả sẽ xuất hiện tại: `output/vi_final.txt`

### 2. Kiểm tra chất lượng (QC)
1. Copy bản dịch tiếng Việt cần kiểm tra vào: `input/qc/vi_to_qc.txt`
2. Copy bản gốc tiếng Hàn vào: `input/qc/kor.txt`
3. (Tùy chọn) Copy bản tiếng Anh tham chiếu vào: `input/qc/eng.txt`
4. Chạy file: **`CHAY_KIEM_TRA_QC.bat`**
5. Xem báo cáo lỗi tại: `output/qc_report.txt`

---

## 📂 Cấu trúc thư mục quan trọng
- `/glossary`: Chứa file thuật ngữ (`glossary.md`) và ghi chú cá nhân (`personal_notes.md`).
- `/input`: Nơi chứa dữ liệu đầu vào cho Dịch (`/trans`) và QC (`/qc`).
- `/output`: Nơi chứa kết quả sau khi xử lý.
- `/scripts`: Chứa các mã nguồn Python xử lý logic.

---

## ⚠️ Lưu ý quan trọng về định dạng
- **Hậu tố tên nhân vật:** Hệ thống được cấu hình để GIỮ NGUYÊN các hậu tố như `-ie, -ah, -ya` chỉ khi bản gốc có. AI sẽ không tự ý thêm vào.
- **Hội thoại:** AI sẽ bám sát cấu trúc của tác giả, không tự động thêm các câu dẫn như "Park Yerim nói" trừ khi bản gốc có sẵn.