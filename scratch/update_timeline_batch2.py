# -*- coding: utf-8 -*-
import json

path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\memory\timeline.json"

with open(path, "r", encoding="utf-8") as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter_id": "ch_008",
        "chapter_title": "Chương 8: Quái vật gì thế",
        "events": [
            "Bội Lương chửi mắng chấm dứt trò hề; Lâu Hỉ Dương dẫn Dịch Duyên về bục sắt giáo huấn.",
            "Lâu Hỉ Dương đưa phương án huấn luyện cấp S độc quyền khiến Bội Lương và bang Lloyd thán phục kinh hãi.",
            "Dịch Duyên nhận lỗi vì đã theo dõi, Lâu Hỉ Dương giải thích đang tìm cách cứu cha khỏi viện nghiên cứu Tây Lăng Sơn.",
            "Lâu Hỉ Dương phát lệnh tấn công Tây Lăng Sơn sau một tuần, đưa bản vẽ nâng cấp 50 cơ giáp cho Bội Lương trong vòng 5 ngày.",
            "Trương Câu chặn đường chất vấn vì sao phải hy sinh anh em vì cha của Lâu Hỉ Dương; Lâu Hỉ Dương khẳng định sẽ chuộc tội nếu có người chết.",
            "Trên đường về, Dịch Duyên ôm chặt Lâu Hỉ Dương, thầm hạ quyết tâm sẽ không để anh gặp nguy hiểm; tối đến lén liên lạc với Trần Liễm."
        ],
        "debt_repayment_progress": "15%",
        "key_relationships": "Dịch Duyên thấu hiểu gánh nặng và sự tự trách của Lâu Hỉ Dương; quyết định bí mật giúp anh phá vỡ phòng ngự Tây Lăng Sơn."
    },
    {
        "chapter_id": "ch_009",
        "chapter_title": "Chương 9: Giống cún con",
        "events": [
            "Dịch Duyên ra điều kiện với Trần Liễm: đồng ý đi theo với điều kiện ông ta phải phá khóa hệ thống phòng vệ viện nghiên cứu Tây Lăng Sơn.",
            "Nhờ bản vẽ cấp S của Lâu Hỉ Dương, bang Lloyd vận hành hoàn hảo, tiến độ cứu cha rút ngắn còn nửa tháng.",
            "Lâu Hỉ Dương đi mua nhu yếu phẩm ở thành Long Uyên, giúp đỡ hai bà cháu và được tặng bộ mũ găng tay len hình cún con.",
            "Lâu Hỉ Dương mang về tặng Dịch Duyên; tối đến Dịch Duyên đội tai cún và đeo móng cún giả vờ sủa 'gâu' trêu chọc anh.",
            "Dịch Duyên xin Lâu Hỉ Dương làm bạn gái giả trước mạt thế, Lâu Hỉ Dương vô thức 'ừm' một tiếng và bị Dịch Duyên cưỡng hôn.",
            "Lâu Hỉ Dương không kiềm lòng được liền ôm gáy Dịch Duyên hôn đáp lại; tiến độ trả nợ tăng lên 30%."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Nụ hôn đáp lại đầu tiên của Lâu Hỉ Dương; tiến độ trả nợ nhảy vọt lên 30%."
    },
    {
        "chapter_id": "ch_010",
        "chapter_title": "Chương 10: Thế sao anh lại hôn em!",
        "events": [
            "Sau nụ hôn, Lâu Hỉ Dương tự trách bản thân mất tỉnh táo và tuyên bố từ nay sẽ giữ đúng ranh giới anh em.",
            "Dịch Duyên uất ức khóc hét 'Thế sao anh lại hôn em!' rồi tự giam mình trong phòng ngủ.",
            "Hôm sau Lâu Hỉ Dương hỏi Bội Lương lý do muốn hôn người khác, Bội Lương bảo 'muốn lên giường'; Lâu Hỉ Dương gạt phắt bảo 'muốn hôn chó' rồi tự suy luận là do thấy tai cún.",
            "Lâu Hỉ Dương mang mô hình cơ giáp về dỗ dành thì phát hiện toàn bộ quần áo của Dịch Duyên đã biến mất, cậu đã bỏ nhà ra đi sớm hơn kiếp trước 1 tháng."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương tự lừa mình dối người về ranh giới anh em; Dịch Duyên rời đi sớm hơn dự tính để thực hiện thỏa thuận với Trần Liễm."
    },
    {
        "chapter_id": "ch_011",
        "chapter_title": "Chương 11: Hãy mở nó ra",
        "events": [
            "Lâu Hỉ Dương tức giận khi thấy Dịch Duyên lại bỏ đi như kiếp trước; uy áp của Đấng Cứu Thế khiến Hệ Thống Thiết Chùy sợ hãi kích hoạt giải pháp.",
            "Hệ thống chỉ dẫn vào phòng Dịch Thiên, mở ngăn kéo bằng ADN của Dịch Duyên tìm thấy cuốn sổ tay da bò 15 năm trước.",
            "Cuốn sổ hé lộ mẹ Dịch Duyên là tình báo viên FC, phát hiện chân tướng mạt thế và bị Tưởng Trác Hàng hãm hại; cha Dịch Duyên dặn cậu nếu cùng đường hãy tìm Trần Liễm.",
            "Lâu Hỉ Dương nhận ra kiếp trước Dịch Duyên trở thành con nuôi của Trần Liễm là do lá thư này; anh quyết định chuẩn bị chiến dịch Tây Lăng Sơn."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương thấu hiểu nguyên do sâu xa dẫn đến hành động và thân thế của Dịch Duyên."
    },
    {
        "chapter_id": "ch_012",
        "chapter_title": "Chương 12: Hắn điên rồi",
        "events": [
            "Lâu Hỉ Dương dọn đến xưởng sắt ở, cả bang Lloyd đồn ầm tin 'Lâu Hỉ Dương là biến thái bị vợ đuổi'.",
            "Lâu Hỉ Dương mở chế độ huấn luyện địa ngục chấn chỉnh binh đoàn; 50 cơ giáp hoàn thành cải tiến.",
            "Rạng sáng ngày thứ 3, 800 người bang Lloyd cùng dàn cơ giáp tấn công viện nghiên cứu Tây Lăng Sơn.",
            "Lâu Hỉ Dương dùng một chưởng khí ba quét sạch dàn cơ giáp B phòng thủ; hệ thống phòng vệ của viện bất ngờ bị ai đó hack tê liệt hoàn toàn (do Dịch Duyên và Trần Liễm làm).",
            "Lâu Hỉ Dương giải cứu thành công Lâu An Minh không tốn một binh một tốt.",
            "Lâu An Minh gặp lại Bội Lương và lão tóc đỏ, thốt ra bí mật: 'Tưởng Trác Hàng, hắn ta điên rồi'.",
            "Tại viện điều trị bí mật, Dịch Duyên ngắm video của Lâu Hỉ Dương, ngoan ngoãn để các bác sĩ cấy thiết bị đau đớn vào sau gáy để có 3 giờ tự do mỗi ngày."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Dịch Duyên âm thầm hy sinh chịu đựng đau đớn để mở đường an toàn cho Lâu Hỉ Dương giải cứu cha."
    },
    {
        "chapter_id": "ch_013",
        "chapter_title": "Chương 13: Em nhớ anh",
        "events": [
            "Lâu An Minh vạch trần âm mưu của Tưởng Trác Hàng: khí độc mạt thế thực chất nhẹ hơn tầng khí thứ hai và sẽ bốc lên Paradise tiêu diệt tầng lớp thượng lưu cầm quyền.",
            "Mẹ của Lâu Hỉ Dương là nhà khoa học 5 sao phát hiện ra điều này và đang bị Tưởng Trác Hàng giam giữ ở Paradise; Lâu An Minh rủ anh cùng đi tìm.",
            "Dịch Duyên gọi video cho Lâu Hỉ Dương; Lâu Hỉ Dương thú nhận 'Anh rất lo lắng cho em... Anh cũng nhớ em'.",
            "Dịch Duyên vui sướng nhảy cẫng lên và bắt đầu cởi quần áo muốn khoe thứ gì đó."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương lần đầu thành thật thừa nhận nhớ Dịch Duyên; khoảng cách tình cảm được thu hẹp rõ rệt."
    },
    {
        "chapter_id": "ch_014",
        "chapter_title": "Chương 14: Chỉ cho anh xem",
        "events": [
            "Dịch Duyên khoe hình xăm ở xương cụt: 'Chỉ cho một mình anh xem'; Lâu Hỉ Dương bắt cậu mặc quần áo đàng hoàng.",
            "Hai người trò chuyện hơn 2 tiếng; Lâu Hỉ Dương phát hiện mồ hôi lạnh trên mặt Dịch Duyên trước khi cậu ngắt máy vì đau đớn do cấy ghép.",
            "Lâu Hỉ Dương lo lắng tột cùng, hỏi hệ thống xác nhận Trần Liễm đang ở Paradise.",
            "Lâu Hỉ Dương giục Lâu An Minh lên đường ngay đến Paradise; hai người đóng giả thổ phỉ trà trộn vào thành công."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương sốt ruột vì tình trạng sức khỏe của Dịch Duyên, lập tức lên đường đến Paradise tìm cậu."
    },
    {
        "chapter_id": "ch_015",
        "chapter_title": "Chương 15: Nam hộ lý",
        "events": [
            "Đến khu phố Paradise sầm uất, Lâu Hỉ Dương bị gã côn đồ nhà giàu Lý Bưu chặn đường bắt gọi 'anh'.",
            "Lâu Hỉ Dương mỉa mai 'mệnh cứng khắc anh trai', dụ cả bọn vào hẻm tối rồi cố tình để Lý Bưu đâm một nhát vào bụng dưới.",
            "Ngay sau đó, Lâu Hỉ Dương phản công đập tan nát cả bọn như đập bóng da, rồi giả vờ yếu ớt ra đường cầu cứu.",
            "Mục đích của anh: dùng vết thương để giành một suất nhập viện điều trị trọng bệnh nơi mẹ anh bị giam giữ.",
            "Buổi tối, bác sĩ đưa vào một nam hộ lý bịt kín mặt chăm sóc giường 1121; người hộ lý nhìn chằm chằm vào vết thương ở bụng anh với ánh mắt u ám (chính là Dịch Duyên)."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Dịch Duyên xuất hiện với thân phận nam hộ lý chăm sóc Lâu Hỉ Dương đang bị thương."
    }
]

timeline.extend(new_entries)

with open(path, "w", encoding="utf-8") as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print("Updated timeline.json with ch_008 -> ch_015 successfully!")
