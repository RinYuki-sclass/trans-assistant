---
description: Quy chuẩn định dạng văn bản và kiểm duyệt (QC) cho các dự án trong novel_projects
globs: novel_projects/**
alwaysApply: true
---

# RULES ĐỊNH DẠNG & QC CHO CÁC DỰ ÁN NOVEL_PROJECTS

Áp dụng cho mọi file dịch thuật và QC thuộc thư mục `novel_projects/**`.

## 1. QUY TẮC ĐỊNH DẠNG ĐOẠN VĂN (PARAGRAPH FORMATTING) - TỐI THƯỢNG
- **Các đoạn phải cách nhau đúng 1 dòng:** Trong mọi file dịch (`translation.md`, chunks, v.v.), giữa hai đoạn văn trần thuật hoặc lời thoại của nhân vật **bắt buộc phải có đúng 1 dòng trống (`\n\n`)**.
- **Tuyệt đối không để dính dòng:** Không được để các câu/đoạn văn dính sát nhau trên các dòng liên tiếp mà thiếu dòng trống ngăn cách (`\n` thay vì `\n\n`).
- **Không để thừa dòng trống:** Tránh để từ 2 dòng trống liên tiếp trở lên (`\n\n\n`).
- **Bảo toàn số đoạn 1:1:** Khớp chính xác từng đoạn với nguyên tác, không tự ý gộp đoạn và không tự ý chẻ nhỏ đoạn.

## 2. CHECKLIST KIỂM DUYỆT (QC AUDIT CHECKLIST)
Khi thực hiện QC một chương trong bất kỳ dự án nào thuộc `novel_projects`:
1. [ ] **Format đoạn văn:** Rà soát toàn bộ file xem các đoạn văn và lời thoại đã cách nhau đúng 1 dòng trống (`\n\n`) chưa.
2. [ ] **Frontmatter:** Đảm bảo phần đầu file có `--- title: ... ---` đúng chuẩn.
3. [ ] **Lời tác giả (Author's Note):** Nếu cuối chương có ghi chú hoặc lời tác giả, phải phân tách bằng đường kẻ ngang `---` và tiêu đề `### Lời tác giả` (hoặc `### Ghi chú`), các đoạn bên dưới cũng cách nhau 1 dòng trống.
4. [ ] **Glossary & Xưng hô:** Đối chiếu danh xưng, đại từ ngôi 3 và xưng hô đối thoại theo đúng file `AGENTS.md` của dự án tương ứng.
