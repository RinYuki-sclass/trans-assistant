---
description: "Quy chuẩn quản lý, cấu trúc dữ liệu và đồng bộ Mục lục chương truyện (TOC / Chapter Index) cho toàn bộ novel_projects"
globs: "novel_projects/**"
alwaysApply: true
---

# RULES QUẢN LÝ MỤC LỤC CHƯƠNG TRUYỆN (NOVEL CHAPTER TOC & INDEX RULES)

> **Phạm vi áp dụng:** Toàn bộ các bộ tiểu thuyết thuộc thư mục `novel_projects/**` trong workspace `trans-tool`.  
> **Mục tiêu:** Thiết lập cấu trúc dữ liệu mục lục chuẩn hóa, phân định rõ ràng giữa mã trang/chương vật lý và tiêu đề văn học, cung cấp nguồn chân lý duy nhất (Single Source of Truth) cho cả AI Code Agent (tự động điều phối) và người dùng (tra cứu, đọc duyệt, xuất bản).

---

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Song hành Hai định dạng (Dual-Format SSoT):**
   - Mỗi dự án tiểu thuyết (`novel_projects/<slug>/`) bắt buộc sở hữu cặp file mục lục trung tâm:
     - `chapters_index.json`: Định dạng JSON máy đọc (Machine-readable) phục vụ cho Agent, Orchestrator, EPUB generator và Web Reader.
     - `TOC.md`: Định dạng Markdown trực quan (Human-readable) hiển thị cây mục lục, thanh tiến độ, huy hiệu trạng thái và liên kết trực tiếp tới file dịch.
2. **Tách biệt ID thư mục vật lý vs Số chương văn học:**
   - **`id` (Folder ID):** Tên thư mục thực tế trong `chapters/` (ví dụ: `p80`, `p81` hoặc `ch_001`). Tuyệt đối không thay đổi tùy tiện để tránh gãy liên kết nội bộ.
   - **`chapter_no`:** Số thứ tự chương nguyên tác theo logic nội dung (ví dụ: Chương 80, hoặc 80.1 nếu chương bị tách thành 2 trang web raw).
   - **`title_vi`:** Tiêu đề tiếng Việt chuẩn ngữ nghĩa văn học, loại bỏ toàn bộ tag rác web cào.
3. **Tuân thủ Tuyệt đối Zero Google API Key Mandate:**
   - Mọi tác vụ quét, khởi tạo, cập nhật trạng thái mục lục đều do AI Code Agent trực tiếp thực hiện hoặc sử dụng script cục bộ (`scripts/sync_novel_toc.py`). Tuyệt đối không gọi bất kỳ API bên ngoài nào.

---

## 2. CẤU TRÚC DỮ LIỆU CHUẨN: `chapters_index.json`

File `chapters_index.json` nằm tại thư mục gốc của từng project:

```json
{
  "project_slug": "kieu-khi-diem-cong-luon-bi-phan-dien-nham-vao",
  "title": "Kiều Khí Điềm Công Luôn Bị Phản Diện Nhắm Vào",
  "original_title": "娇气甜攻总被反派盯上[快穿]",
  "author": "Yên Tử Sơn Cố (烟紫山故)",
  "total_chapters": 144,
  "stats": {
    "pending": 0,
    "raw_ready": 49,
    "prescanned": 0,
    "translating": 0,
    "translated": 16,
    "qc_approved": 16,
    "published": 0
  },
  "arcs": [
    {
      "arc_id": 1,
      "arc_name": "Tu Chân Giới: Thanh Lãnh Kiếm Tôn Thụ",
      "folder_range": ["p1", "p79"]
    },
    {
      "arc_id": 2,
      "arc_name": "Tinh Tế ABO: Alpha Đỉnh Cấp Phân Hóa Lần Hai Omega",
      "folder_range": ["p80", "p144"]
    }
  ],
  "chapters": [
    {
      "id": "p80",
      "order": 80,
      "chapter_no": 80,
      "sub_index": null,
      "arc_id": 2,
      "arc_name": "ABO",
      "title_zh": "第80章 军校入驻",
      "title_vi": "Chương 80: Nhập học trường quân sự",
      "status": "qc_approved",
      "paragraph_count": 101,
      "word_count": 2840,
      "source_url": "https://www.dmxs.org/view/6-14206-80.html",
      "updated_at": "2026-10-27T22:00:00+07:00"
    }
  ]
}
```

---

## 3. ĐỊNH DẠNG TRỰC QUAN: `TOC.md`

File `TOC.md` được render tự động hoặc biên soạn với cấu trúc chuẩn:

```markdown
# 📖 MỤC LỤC: Kiều Khí Điềm Công Luôn Bị Phản Diện Nhắm Vào
> **Tác giả:** Yên Tử Sơn Cố | **Tiến độ:** 16 / 65 trang (24.6%) | **Cập nhật:** 27/10/2026  
> **Trạng thái:** 🟢 Đã duyệt QC (16) | 🔵 Đã dịch (0) | ⚪ Chưa dịch (49)

---

## 🌌 THẾ GIỚI 2: Tinh Tế ABO (Trang 80 - 144)

| STT | Mã mục | Tiêu đề tiếng Việt | Nguyên tác (Trung) | Số đoạn | Trạng thái |
| :---: | :---: | :--- | :--- | :---: | :---: |
| 1 | `p80` | [Chương 80: Nhập học trường quân sự](chapters/p80/translation.md) | 第80章 | 101 | 🟢 Đã duyệt QC |
| 2 | `p81` | [Chương 81: Huấn luyện bãi tập](chapters/p81/translation.md) | 第81章 | 98 | 🟢 Đã duyệt QC |
| ... | ... | ... | ... | ... | ... |
| 17 | `p96` | [Chương 96: Phụ đạo đặc biệt](chapters/p96/source.md) | 第96章 | 112 | ⚪ Chưa dịch |
```

---

## 4. MA TRẬN 6 TRẠNG THÁI CHƯƠNG (STATE LIFECYCLE)

| Mã trạng thái | Icon | Tên hiển thị | Điều kiện thỏa mãn |
| :--- | :---: | :--- | :--- |
| `pending` | 🔴 | Thiếu raw | Chưa tồn tại thư mục hoặc `source.md` trống. |
| `raw_ready` | ⚪ | Đã cào raw | Đã có `source.md` sạch, chưa pre-scan QA. |
| `prescanned` | 🟡 | Đã duyệt QA | Đã có `qa_clarifications.md` chốt xưng hô và glossary. |
| `translating` | 🟠 | Đang dịch | Đang dịch dở dang theo chunks. |
| `translated` | 🔵 | Đã dịch thô | Đã sinh `translation.md` khớp 1:1 paragraph alignment. |
| `qc_approved`| 🟢 | Đã duyệt QC | Đã chạy QC kiểm định, đạt chuẩn 1:1, không lệch đại từ. |
| `published`  | 🟣 | Đã xuất bản | Đã đóng gói meta/summary, sẵn sàng cho EPUB/Web. |

---

## 5. QUY CHUẨN ĐẶT TIÊU ĐỀ TIẾNG VIỆT (`title_vi`)

1. **Cú pháp Chương thông thường:**  
   `Chương [Số]: [Tên chương tiếng Việt]`  
   *Ví dụ:* `Chương 80: Viện trưởng Dạ Lâm Uyên`
2. **Khi nguyên tác không có tên chương phụ:**  
   Giữ nguyên: `Chương [Số]` (Không tự bịa thêm tên phụ nếu raw không có).
3. **Cú pháp Khoái xuyên / Vị diện (Arc-level):**  
   Tại cấp độ hiển thị tổng, ghi rõ tên Thế giới ở tiêu đề phân đoạn H2, các chương con chỉ cần giữ `Chương [Số]: [Tên]`.
4. **Cú pháp Phiên ngoại / Ngoại truyện:**  
   `Phiên ngoại [Số/Tên]: [Tên chương]` (Ví dụ: `Phiên ngoại 1: Kỷ niệm ngày thành hôn`).
5. **Cú pháp Chương bị chia nhiều trang web raw (Split Chapters):**  
   `Chương [Số] (Thượng)` / `Chương [Số] (Hạ)` hoặc `Chương [Số] (Phần 1)` / `Chương [Số] (Phần 2)`.

---

## 6. QUY TẮC ĐỒNG BỘ DÀNH CHO AI AGENT & SCRIPTS

1. Khi Agent hoàn thành dịch hoặc duyệt QC một chương:
   - Cập nhật trường `"status"` trong `chapters/<id>/meta.json`.
   - Cập nhật entry tương ứng trong `chapters_index.json`.
   - Render cập nhật dòng tương ứng trong `TOC.md`.
2. Khi khởi tạo dự án mới hoặc cào raw một Arc:
   - Tự động sinh `chapters_index.json` ban đầu với danh sách toàn bộ các chương/trang vừa cào ở trạng thái `raw_ready`.
   - Sinh file `TOC.md` làm bảng điều hướng trung tâm cho dự án.
3. Tích hợp trực tiếp với `scripts/inspect_chapter_state.py` và `scripts/epub_generator.py` để lấy danh sách chương từ `chapters_index.json` thay vì duyệt file ngẫu nhiên trên ổ đĩa.
