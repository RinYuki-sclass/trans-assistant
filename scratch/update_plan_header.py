# -*- coding: utf-8 -*-
plan_path = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\plan.md'

with open(plan_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_header = """| Chỉ số | Giá trị | Ghi chú |
| :--- | :---: | :--- |
| **Tổng số chương toàn bộ truyện** | **35** | `ch_001` $\\rightarrow$ `ch_035` (32 chính văn + 3 phiên ngoại) |
| **Đã hoàn thành (QC_PASSED)** | **23** | Đã hoàn tất Batch 0 (`ch_001`), Batch 1 (`ch_002` $\\rightarrow$ `ch_007`), Batch 2 (`ch_008` $\\rightarrow$ `ch_015`), Batch 3 (`ch_016` $\\rightarrow$ `ch_023`) |
| **Đang chờ xử lý** | **12** | `ch_024` $\\rightarrow$ `ch_035` (đã có sẵn raw 1:1) |
| **Tiến độ tổng thể** | **65.7%** | Đã thông qua kiểm toán 23/35 chương đạt 100% QC PASS |
| **Mục tiêu quy chuẩn** | **100% PASS** | Khóa chặt đại từ: Lâu Hỉ Dương = "anh", Dịch Duyên = "cậu", cách dòng `\\n\\n`, thoại `“...”` |"""

new_header = """| Chỉ số | Giá trị | Ghi chú |
| :--- | :---: | :--- |
| **Tổng số chương toàn bộ truyện** | **35** | `ch_001` $\\rightarrow$ `ch_035` (32 chính văn + 3 phiên ngoại) |
| **Đã hoàn thành (QC_PASSED)** | **35** | Hoàn tất 100% toàn bộ Batch 0, 1, 2, 3, 4, 5 (`ch_001` $\\rightarrow$ `ch_035`) |
| **Đang chờ xử lý** | **0** | Đã hoàn thành toàn bộ |
| **Tiến độ tổng thể** | **100%** | Đã thông qua kiểm toán 35/35 chương đạt 100% QC PASS (10/10) |
| **Mục tiêu quy chuẩn** | **100% PASS** | Khóa chặt đại từ: Lâu Hỉ Dương = "anh", Dịch Duyên = "cậu", cách dòng `\\n\\n`, thoại `“...”` |"""

content = content.replace(old_header, new_header)
content = content.replace(
    "> **Trạng thái dự án:** 🚀 **ĐÃ KHỞI TẠO CẤU TRÚC VÀ RAW HOÀN CHỈNH — SẴN SÀNG THỰC THI**",
    "> **Trạng thái dự án:** 🏆 **HOÀN THÀNH TRỌN BỘ 100% TÁC PHẨM (35/35 CHƯƠNG ĐẠT CHUẨN QC PASS 10/10)**"
)

with open(plan_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated plan.md header successfully.")
