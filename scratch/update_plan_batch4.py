# -*- coding: utf-8 -*-
plan_path = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\plan.md'

with open(plan_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Batch 4 table and status
old_b4 = """### 🔹 BATCH 4: Đột Nhập Cứu Người & Tỏ Tình Xác Định Tình Cảm (7 chương: `ch_024` $\\rightarrow$ `ch_030`)
* **Mục tiêu:** Xâm nhập khu vực tuyệt mật; đối đầu với Tưởng Trác Hàng; Dịch Duyên bộc phát tính điên vì sợ mất Lâu Hỉ Dương; cả hai chính thức tỏ tình.

| Chapter ID | Tên chương | Số đoạn 1:1 | Trạng thái QC | Tiến độ | Tóm tắt sự kiện chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| [`ch_024`](chapters/ch_024) | Chương 24: Nhóc đáng thương | 84 | ⏳ PENDING | 0% | Quét toàn cảnh hành lang ngầm; Dịch Duyên đẩy Lâu Hỉ Dương lên giường đè người chúc ngủ ngon đầy tính chiếm hữu |
| [`ch_025`](chapters/ch_025) | Chương 25: Ca ca, đẹp trai quá | 90 | ⏳ PENDING | 0% | Buổi sáng thức dậy trong lòng nhau; Dịch Duyên si mê ngắm nhìn gương mặt anh; Tưởng Trác Hàng xuất hiện dưới ánh đèn |
| [`ch_026`](chapters/ch_026) | Chương 26: Đưa tôi về, Tưởng tiên sinh | 77 | ⏳ PENDING | 0% | Tưởng Trác Hàng giăng bẫy; Dịch Duyên phát điên bóp cổ Trần Liễm đoạt lại manh mối cứu Lâu Hỉ Dương |
| [`ch_027`](chapters/ch_027) | Chương 27: Ký chủ trong sạch khó giữ | 80 | ⏳ PENDING | 0% | Lâu Hỉ Dương rơi vào tình thế hiểm nghèo; Hệ Thống kêu gào cảnh báo mất đi trong trắng; Dịch Duyên kịp thời xông tới |
| [`ch_028`](chapters/ch_028) | Chương 28: Em cũng thích anh | 87 | ⏳ PENDING | 0% | Dịch Duyên trong cơn mê sảng thốt lên lời yêu; Lâu Hỉ Dương cúi đầu hôn lên môi cậu đáp lại: "Ừ, anh cũng thích em" |
| [`ch_029`](chapters/ch_029) | Chương 29: Em ngoan lắm mà | 79 | ⏳ PENDING | 0% | Hệ Thống Thiết Chùy thức tỉnh cập nhật tiến độ trả nợ lên 82%; Dịch Duyên nũng nịu đòi anh khẳng định sự ngoan ngoãn |
| [`ch_030`](chapters/ch_030) | Chương 30: Đừng khóc nữa | 78 | ⏳ PENDING | 0% | Chuẩn bị trước thềm Lễ rơi tuyết; tháo gỡ thiết bị cấy sau gáy của Dịch Duyên; Lâu Hỉ Dương xót xa ôm lấy cậu dỗ dành |"""

new_b4 = """### 🔹 BATCH 4: Đột Nhập Cứu Người & Tỏ Tình Xác Định Tình Cảm (7 chương: `ch_024` $\\rightarrow$ `ch_030`) — [HOÀN THÀNH ✅]
* **Mục tiêu:** Xâm nhập khu vực tuyệt mật; đối đầu với Tưởng Trác Hàng; Dịch Duyên bộc phát tính điên vì sợ mất Lâu Hỉ Dương; cả hai chính thức tỏ tình.

| Chapter ID | Tên chương | Số đoạn 1:1 | Trạng thái QC | Tiến độ | Tóm tắt sự kiện chính |
| :---: | :--- | :---: | :---: | :---: | :--- |
| [`ch_024`](chapters/ch_024) | Chương 24: Nhóc đáng thương | 85 | ✅ QC_PASSED | 100% | Đột nhập căn phòng tròn gặp mẹ; viết giấy hẹn nửa tháng sau cứu bà; Dịch Duyên hôn cằm an ủi "Đồ nhóc đáng thương" |
| [`ch_025`](chapters/ch_025) | Chương 25: Ca ca, đẹp trai quá | 91 | ✅ QC_PASSED | 100% | Dịch Duyên mặc âu phục lộ rõ dung mạo sắc sảo kinh diễm; Trương Sâm Trạch khiêu khích; Tưởng Trác Hàng xuất hiện tại bữa tiệc |
| [`ch_026`](chapters/ch_026) | Chương 26: Đưa tôi về, Tưởng tiên sinh | 78 | ✅ QC_PASSED | 100% | Lâu An Minh cải trang; Lâu Hỉ Dương nhận theo Tưởng Trác Hàng để cứu cha; Dịch Duyên phát điên bóp cổ Trần Liễm đòi súng |
| [`ch_027`](chapters/ch_027) | Chương 27: Ký chủ trong sạch khó giữ | 81 | ✅ QC_PASSED | 100% | Tiết lộ quá khứ đen tối của Tưởng Trác Hàng; bị tiêm thuốc kích dục; Tưởng Trác Hàng quay video sờ cơ bụng gửi cho Lâu An Minh và Dịch Duyên |
| [`ch_028`](chapters/ch_028) | Chương 28: Anh cũng thích em | 88 | ✅ QC_PASSED | 100% | Hệ thống truyền tống khẩn cấp; Dịch Duyên bắn kẻ chạm vào anh rồi bế bổng Lâu Hỉ Dương về phòng; cả hai có quan hệ thân mật và chính thức tỏ tình |
| [`ch_029`](chapters/ch_029) | Chương 29: Em ngoan lắm mà | 80 | ✅ QC_PASSED | 100% | Tiến độ trả nợ vọt lên 82%; Lâu Hỉ Dương thổ lộ thật lòng; Trần Liễm công khai là cậu ruột Dịch Duyên và đồng ý bẻ khóa thiết bị |
| [`ch_030`](chapters/ch_030) | Chương 30: Đừng khóc nữa | 79 | ✅ QC_PASSED | 100% | Tháo gỡ thành công thiết bị sau gáy cho Dịch Duyên; Lâu Hỉ Dương bộc bạch tâm can giãi bày mọi nỗi niềm; ôm dỗ Dịch Duyên khóc ướt gối |"""

assert old_b4 in content, "Batch 4 section not matched in plan.md"
content = content.replace(old_b4, new_b4)

with open(plan_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated plan.md successfully.")
