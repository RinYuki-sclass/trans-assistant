---
description: Quy chuẩn định dạng văn bản, hậu tố tiếng Hàn và kiểm duyệt (QC) cho toàn bộ novel workflow (novel_projects, input/qc, SVR)
globs: ["novel_projects/**", "input/qc/**", "output/qc/**", "memory/**", "WORKFLOW_NOVEL_TRANSLATION.md"]
alwaysApply: true
---

# RULES ĐỊNH DẠNG & QC CHO NOVEL WORKFLOW

Áp dụng cho mọi file dịch thuật và QC thuộc thư mục `novel_projects/**`, `input/qc/**`, `output/qc/**`, cũng như toàn bộ quy trình QC tiểu thuyết.

## 1. QUY TẮC ĐỊNH DẠNG ĐOẠN VĂN (PARAGRAPH FORMATTING) - TỐI THƯỢNG
- **Các đoạn phải cách nhau đúng 1 dòng:** Trong mọi file dịch (`translation.md`, chunks, v.v.), giữa hai đoạn văn trần thuật hoặc lời thoại của nhân vật **bắt buộc phải có đúng 1 dòng trống (`\n\n`)**.
- **Tuyệt đối không để dính dòng:** Không được để các câu/đoạn văn dính sát nhau trên các dòng liên tiếp mà thiếu dòng trống ngăn cách (`\n` thay vì `\n\n`).
- **Không để thừa dòng trống:** Tránh để từ 2 dòng trống liên tiếp trở lên (`\n\n\n`).
- **Bảo toàn số đoạn 1:1:** Khớp chính xác từng đoạn với nguyên tác, không tự ý gộp đoạn và không tự ý chẻ nhỏ đoạn.

## 2. CHECKLIST KIỂM DUYỆT (QC AUDIT CHECKLIST)
Khi thực hiện QC một chương trong bất kỳ dự án nào:
1. [ ] **Format đoạn văn:** Rà soát toàn bộ file xem các đoạn văn và lời thoại đã cách nhau đúng 1 dòng trống (`\n\n`) chưa.
2. [ ] **Frontmatter:** Đảm bảo phần đầu file có `--- title: ... ---` đúng chuẩn nếu có yêu cầu.
3. [ ] **Lời tác giả (Author's Note):** Nếu cuối chương có ghi chú hoặc lời tác giả, phải phân tách bằng đường kẻ ngang `---` và tiêu đề `### Lời tác giả` (hoặc `### Ghi chú`), các đoạn bên dưới cũng cách nhau 1 dòng trống.
4. [ ] **Glossary & Xưng hô:** Đối chiếu danh xưng, đại từ ngôi 3 và xưng hô đối thoại theo đúng file `AGENTS.md` / `characters.md` của dự án tương ứng (riêng với các bộ trong `novel_projects/**`, áp dụng quy chuẩn phân ngôi `anh`, `cậu`, `y`, `hắn` theo [novel_pronoun_conventions.md](file:///d:/Nhung/RIDI/trans-assistant/.agents/rules/novel_pronoun_conventions.md); các file ngoài `novel_projects` như `input/qc` tuân thủ glossary riêng).
5. [ ] **Bảo toàn hậu tố tiếng Hàn:** Tuân thủ tuyệt đối Quy tắc 3 bên dưới, không bắt lỗi lạm dụng hậu tố `-ie`, `-ah`.

## 3. QUY TẮC HẬU TỐ XƯNG HÔ TIẾNG HÀN KHI QC (-ie, -ah, -yah, ...)
- **TUYỆT ĐỐI KHÔNG BẮT LỖI LẠM DỤNG HẬU TỐ:**
  - Không bắt lỗi, không cảnh báo, không phàn nàn và không trừ điểm khi bản dịch giữ lại các hậu tố thân mật tiếng Hàn sau tên riêng như `-ie`, `-ah`, `-yah` (ví dụ: `Yoohyun-ie`, `Yerim-ie`, `Yoojin-ie`, `Peace-ie`, `Yoohyun-ah`, `Yerim-ah`, `Peace-ah`...).
  - **Hợp lệ ở cả thoại và văn trần thuật:**
    - Trong lời gọi / hội thoại: `Yoohyun-ah`, `Yerim-ah`, `Peace-ah`... là cách xưng hô thân mật tự nhiên theo chuẩn nguyên tác.
    - Trong văn kể / trần thuật ngôi thứ ba / suy nghĩ của nhân vật: `Yoohyun-ie`, `Yerim-ie`, `Peace-ie`... là phong cách dịch hợp lệ để giữ sắc thái gần gũi, gắn kết gia đình / tình cảm của nhân vật (như góc nhìn người anh/người nuôi dưỡng của Han Yoojin).
  - **Nghiêm cấm trong Báo cáo QC:**
    - Tuyệt đối **KHÔNG** gán nhãn việc xuất hiện `-ie`, `-ah`, `-yah` là "lỗi hành văn", "lạm dụng đuôi `-ie`", "thừa đuôi `-ie`", "lặp lại hậu tố", hay "thừa thãi".
    - Tuyệt đối **KHÔNG** đề xuất xóa bỏ các hậu tố này trong cột "Đề xuất sửa tối thiểu (Minimal Patch)" nếu câu dịch không có lỗi nào khác.
  - **Phạm vi kiểm duyệt thực sự:** Chỉ bắt lỗi xưng hô nếu dịch sai lệch so với `characters.md` (ví dụ: tự ý đổi đại từ sai vai vế, Yerim xưng "cháu" thay vì "tôi", gọi cấp trên bằng "cậu ấy" thay vì "Cục trưởng/anh ấy", dịch sai nghĩa gốc, dịch sót hoặc thêm thắt tình tiết).
