# -*- coding: utf-8 -*-
import json

timeline_file = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\memory\timeline.json'

with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

# Batch 5 chapters
batch5_events = [
    {
        "chapter_id": "ch_031",
        "chapter_title": "Chương 31: Tiết rơi tuyết năm 417",
        "events": [
            "Lâu Hỉ Dương gạt lệ hôn Dịch Duyên; tiến độ trả nợ nhảy vọt lên 90%; hứa hẹn cùng cậu ngắm tuyết.",
            "Trần Liễm mắng mỏ vì tháo thiết bị nhưng vẫn chấp hành kế hoạch phối hợp mở đường.",
            "Lễ rơi tuyết năm 417 của Liên bang: Tưởng Trác Hàng di chuyển mẹ Lâu Hỉ Dương khỏi viện điều trị.",
            "Lâu Hỉ Dương dùng hệ thống dịch chuyển và tàng hình 1 phút lẻn vào xe áp giải cứu mẹ, nhận được con chip vạch trần chân tướng khí độc mạt thế.",
            "Tưởng Trác Hàng đem quân chặn đường; Lâu Hỉ Dương hé lộ quân tiếp viện bang Ryder của Bội Lương đã bao vây phía sau nhờ sự trợ giúp của Trần Liễm.",
            "Lâu Hỉ Dương và Tưởng Trác Hàng giương súng đối đầu trực diện dưới làn tuyết rơi."
        ],
        "debt_repayment_progress": "90%",
        "key_relationships": "Lâu Hỉ Dương dốc toàn lực bảo vệ mẹ và tinh cầu M; tình cảm với Dịch Duyên ngày càng sâu đậm."
    },
    {
        "chapter_id": "ch_032",
        "chapter_title": "Chương 32: Chỉ có em [Hoàn]",
        "events": [
            "Tưởng Trác Hàng vạch trần bí mật năm xưa: ông ta và Lâu An Minh từng yêu nhau, bị quý tộc gia tộc Mike cưỡng ép chuốc thuốc Lâu An Minh với mẹ Lâu Hỉ Dương khiến bà mang thai.",
            "Tưởng Trác Hàng bắn chết mẹ Lâu Hỉ Dương; Dịch Duyên xông vào đá bay súng.",
            "Lâu Hỉ Dương kích hoạt con chip trên thiết bị đầu cuối phát trực tiếp chân tướng khí độc lên toàn bộ truyền hình M tinh và paradise thông qua mạng lưới xâm nhập của Trần Liễm.",
            "Lâu Hỉ Dương tha mạng cho Tưởng Trác Hàng nhưng Tưởng Trác Hàng tự sát bằng súng; Lâu An Minh đến ôm thi thể người yêu rời đi.",
            "Paradise bị nổ tung; Lâu Hỉ Dương và Dịch Duyên cùng ngắm tuyết thật rơi; Lâu Hỉ Dương hôn cậu: 'Anh chỉ còn lại một mình em thôi, Tiểu Duyên'.",
            "Nhiệm vụ trả nợ hoàn thành 100%; Hệ thống Thiết Chùy giải trừ trói buộc quay về sở đòi nợ."
        ],
        "debt_repayment_progress": "100%",
        "key_relationships": "Hoàn thành 100% nhiệm vụ trả nợ tình; Lâu Hỉ Dương và Dịch Duyên trọn đời bên nhau."
    },
    {
        "chapter_id": "ch_033",
        "chapter_title": "Phiên ngoại 1: Về kiếp trước",
        "events": [
            "Hồi tưởng kiếp trước: Lâu Hỉ Dương 17 tuổi, cha bị bắt vì vu oan tham ô hối lộ, nhà bị tịch thu niêm phong.",
            "Cầm 2000 tinh tệ đi thuê phòng, bị côn đồ gây sự và được Dịch Thiên cứu, cho thuê phòng đối diện với giá 1000 tinh tệ/tháng.",
            "Lần đầu tiên gặp Dịch Duyên 9 tuổi: bé trai xinh đẹp như búp bê tây, mắt đuôi hoa cát cánh; Lâu Hỉ Dương tưởng bé gái khen xinh và chúc mừng sinh nhật.",
            "Nụ cười của Lâu Hỉ Dương thắp sáng linh hồn tăm tối của Dịch Duyên.",
            "Lâu Hỉ Dương đi làm nhân viên quán trà sữa bị kẻ thù của cha tìm tới đánh đập; Dịch Duyên xót xa thổi vết thương đòi giết kẻ bắt nạt.",
            "Lâu Hỉ Dương hỏi: 'Em sẽ mãi mãi ở bên anh chứ?'; gieo mầm cố chấp cả đời của Dịch Duyên."
        ],
        "debt_repayment_progress": "100%",
        "key_relationships": "Khởi nguồn tình cảm và sự gắn kết định mệnh giữa Lâu Hỉ Dương và Dịch Duyên từ thuở thiếu thời."
    },
    {
        "chapter_id": "ch_034",
        "chapter_title": "Phiên ngoại 2: Về kiếp này",
        "events": [
            "Sau khi hệ thống rời đi, Lâu Hỉ Dương phát hiện Dịch Duyên bất an, né tránh và lo sợ bị ghét bỏ.",
            "Lâu Hỉ Dương gặng hỏi; Dịch Duyên thừa nhận phần thưởng của hệ thống đã giúp cậu nhớ lại toàn bộ ký ức kiếp trước.",
            "Tiết lộ sự thật kiếp trước: Dịch Duyên vượt quá 4 tiếng nên tháo chip thất bại; cậu tự sát để trích xuất chip cứu thế giới và thỏa mãn ước nguyện không xuất hiện trước mặt anh.",
            "Linh hồn Dịch Duyên lên sở đòi nợ thứ nguyên; ước nguyện kiếp sau 'muốn anh ấy yêu em' biến thành đơn đòi nợ của hệ thống.",
            "Lâu Hỉ Dương ôm hôn Dịch Duyên khẳng định yêu con người cậu của cả hai kiếp; hóa giải mọi khúc mắc và đau thương."
        ],
        "debt_repayment_progress": "100%",
        "key_relationships": "Giải mã trọn vẹn nguồn gốc hệ thống trả nợ tình; tình yêu hai kiếp thăng hoa hoàn mỹ."
    },
    {
        "chapter_id": "ch_035",
        "chapter_title": "Phiên ngoại 3: Về thời điểm Dịch Duyên tháo xuống mặt nạ ngoan ngoãn",
        "events": [
            "Tiệc mừng công: Trương Sâm Trạch ngồi đối diện nhìn Lâu Hỉ Dương cưng chiều đút thức ăn cho Dịch Duyên, ăn 'cơm chó' phát ngấy.",
            "Trần Liễm kéo Dịch Duyên ra khuyên đừng giả ngoan nữa, tiết lộ Lâu Hỉ Dương đã sớm biết bộ mặt thật của cậu từ lâu.",
            "Dịch Duyên lo lắng hỏi phản ứng của Lâu Hỉ Dương; Trần Liễm kể lại câu trả lời ê răng của anh: 'Ừ, khá đáng yêu'."
        ],
        "debt_repayment_progress": "100%",
        "key_relationships": "Dịch Duyên được cưng chiều vô hạn; Lâu Hỉ Dương bao dung và yêu thương trọn vẹn mọi mặt tính cách của cậu."
    }
]

# Update or append
existing_ch_ids = [item['chapter_id'] for item in timeline]
for event in batch5_events:
    if event['chapter_id'] in existing_ch_ids:
        idx = existing_ch_ids.index(event['chapter_id'])
        timeline[idx] = event
    else:
        timeline.append(event)

with open(timeline_file, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print("Updated timeline.json successfully with Batch 5 events.")
