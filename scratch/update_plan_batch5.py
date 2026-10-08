# -*- coding: utf-8 -*-
plan_path = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\plan.md'

with open(plan_path, 'r', encoding='utf-8') as f:
    content = f.read()

old_b5 = """### 🔹 BATCH 5: Quyết Chiến Tiết Rơi Tuyết & 3 Phiên Ngoại Hoàn Hảo (5 chương: `ch_031` $\\rightarrow$ `ch_035`)
* **Mục tiêu:** Trận chiến quyết định tại Lễ rơi tuyết năm 417; lật đổ âm mưu của Tưởng Trác Hàng; hoàn thành 100% nhiệm vụ trả nợ tình; giải mã bí mật kiếp trước và kiếp này qua 3 phiên ngoại.

| Chapter ID | Tên chương | Số đoạn 1:1 | Trạng thái QC | Tiến độ | Tóm tắt sự kiện chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| [`ch_031`](chapters/ch_031) | Chương 31: Tiết rơi tuyết năm 417 | 78 | ⏳ PENDING | 0% | Tiến độ trả nợ vọt lên 90%; trận tuyết đầu mùa năm 417; đối đầu trực diện bóc trần bộ mặt thật của Tưởng Trác Hàng |
| [`ch_032`](chapters/ch_032) | Chương 32: Chỉ có em [Hoàn] | 77 | ⏳ PENDING | 0% | Lâu Hỉ Dương và Dịch Duyên đồng tâm hiệp lực giành thắng lợi trọn vẹn; giải cứu thế giới; xác lập tương lai trọn đời bên nhau |
| [`ch_033`](chapters/ch_033) | Phiên ngoại 1: Về kiếp trước | 95 | ⏳ PENDING | 0% | Hé lộ góc nhìn kiếp trước: biến cố năm 17 tuổi của Lâu Hỉ Dương và mối duyên nghiệt ngã thầm kín của Dịch Duyên |
| [`ch_034`](chapters/ch_034) | Phiên ngoại 2: Về kiếp này | 51 | ⏳ PENDING | 0% | Cuộc sống sau khi nhiệm vụ hoàn thành và Hệ Thống rời đi; Lâu Hỉ Dương phát hiện sự thật Dịch Duyên đã sớm biết tất cả |
| [`ch_035`](chapters/ch_035) | Phiên ngoại 3: Về thời điểm Dịch Duyên tháo xuống mặt nạ ngoan ngoãn | 14 | ⏳ PENDING | 0% | Tiệc mừng công; Trương Sâm Trạch ăn "cơm chó" ngập mồm; phản ứng thú vị của Lâu Hỉ Dương khi biết Dịch Duyên giả ngoan: "Ừ, khá đáng yêu" |"""

new_b5 = """### 🔹 BATCH 5: Quyết Chiến Tiết Rơi Tuyết & 3 Phiên Ngoại Hoàn Hảo (5 chương: `ch_031` $\\rightarrow$ `ch_035`) — [HOÀN THÀNH ✅]
* **Mục tiêu:** Trận chiến quyết định tại Lễ rơi tuyết năm 417; lật đổ âm mưu của Tưởng Trác Hàng; hoàn thành 100% nhiệm vụ trả nợ tình; giải mã bí mật kiếp trước và kiếp này qua 3 phiên ngoại.

| Chapter ID | Tên chương | Số đoạn 1:1 | Trạng thái QC | Tiến độ | Tóm tắt sự kiện chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| [`ch_031`](chapters/ch_031) | Chương 31: Tiết rơi tuyết năm 417 | 79 | ✅ QC_PASSED | 100% | Tiến độ trả nợ vọt lên 90%; trận tuyết rơi năm 417; giải cứu mẹ nhận chip; đối đầu trực diện bóc trần bộ mặt thật của Tưởng Trác Hàng |
| [`ch_032`](chapters/ch_032) | Chương 32: Chỉ có em [Hoàn] | 78 | ✅ QC_PASSED | 100% | Vạch trần chân tướng khí độc lên toàn tinh cầu; Tưởng Trác Hàng tự sát; hoàn thành 100% nhiệm vụ trả nợ; Lâu Hỉ Dương và Dịch Duyên trọn đời bên nhau |
| [`ch_033`](chapters/ch_033) | Phiên ngoại 1: Về kiếp trước | 96 | ✅ QC_PASSED | 100% | Góc nhìn kiếp trước: biến cố năm 17 tuổi của Lâu Hỉ Dương gặp Dịch Duyên 9 tuổi xinh đẹp như búp bê tây; gieo mầm cố chấp cả đời |
| [`ch_034`](chapters/ch_034) | Phiên ngoại 2: Về kiếp này | 52 | ✅ QC_PASSED | 100% | Hệ thống rời đi; Dịch Duyên nhớ lại ký ức kiếp trước; giải mã bí mật tự sát kiếp trước và nguồn gốc đơn đòi nợ của hệ thống |
| [`ch_035`](chapters/ch_035) | Phiên ngoại 3: Về thời điểm Dịch Duyên tháo xuống mặt nạ ngoan ngoãn | 15 | ✅ QC_PASSED | 100% | Tiệc mừng công; Trương Sâm Trạch ăn "cơm chó" ngập mặt; phản ứng thú vị của Lâu Hỉ Dương khi biết Dịch Duyên giả ngoan: "Ừ, khá đáng yêu" |"""

assert old_b5 in content, "Batch 5 section not found in plan.md"
content = content.replace(old_b5, new_b5)

with open(plan_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated plan.md successfully with Batch 5.")
