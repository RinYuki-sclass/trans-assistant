# -*- coding: utf-8 -*-
import json

timeline_file = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\memory\timeline.json'

with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

# Batch 4 chapters
batch4_events = [
    {
        "chapter_id": "ch_024",
        "chapter_title": "Chương 24: Nhóc đáng thương",
        "events": [
            "Lâu Hỉ Dương khảo sát hành lang tầng 2 thiết kế hình chữ Hồi, phát hiện hệ thống bảo vệ laser bằng gương và đèn tròn cực kỳ nghiêm ngặt.",
            "Lâu Hỉ Dương gọi hệ thống Tiểu Thiết Chùy; Thiết Chùy mắng anh là đồ móng giò vô tình nhưng vẫn cấp kỹ năng 'Không khí môi chất hóa' 5 phút; thông báo tiến độ trả nợ hiện tại là 60%.",
            "Tàng hình đột nhập vào căn phòng hình cung trung tâm, Lâu Hỉ Dương gặp mẹ mình - một nhà khoa học gầy gò đang tuyệt vọng viết nhật ký.",
            "Lâu Hỉ Dương viết dòng chữ 'Nửa tháng sau, đợi con' vào sổ của mẹ; trước khi hết giờ anh ôm hụt bà rồi kịp thời trốn thoát về buồng vệ sinh.",
            "Lâu Hỉ Dương chui về phòng ôm Dịch Duyên tâm sự; Dịch Duyên nâng mặt anh gọi 'Đồ nhóc đáng thương' rồi hôn nhẹ lên cằm anh an ủi."
        ],
        "debt_repayment_progress": "60%",
        "key_relationships": "Lâu Hỉ Dương gắn kết huyết thống với mẹ; Dịch Duyên dịu dàng che chở và an ủi tổn thương tâm lý của Lâu Hỉ Dương."
    },
    {
        "chapter_id": "ch_025",
        "chapter_title": "Chương 25: Ca ca, đẹp trai quá",
        "events": [
            "Buổi sáng thức dậy, Lâu Hỉ Dương nhìn Dịch Duyên thay đồ rồi đỏ mặt mất kiểm soát dục vọng, vội vã nhắm mắt đè nén.",
            "Dịch Duyên chải tóc ra sau tai, mặc âu phục lộ rõ dung mạo sắc sảo kinh diễm; đòi Trần Liễm đưa súng laser mini cất vào hông.",
            "Dịch Duyên giúp Lâu Hỉ Dương sơ vin áo sơ mi và khen 'Anh, đẹp trai quá'; cả hai đeo mặt nạ cùng Trần Liễm đến tiệc sinh nhật Tưởng Trác Hàng ở paradise.",
            "Toàn trường trầm trồ trước vẻ đẹp của Dịch Duyên; Lâu Hỉ Dương lo lắng tìm kiếm Lâu An Minh và chú Q.",
            "Trương Sâm Trạch đến khiêu khích Dịch Duyên ('Cậu yêu Lâu Hỉ Dương đúng không?', 'Vụ đánh người là do cậu làm?'); Dịch Duyên lập tức giả vờ tủi thân núp sau Lâu Hỉ Dương.",
            "Tưởng Trác Hàng xuất hiện tại bữa tiệc."
        ],
        "debt_repayment_progress": "60%",
        "key_relationships": "Dịch Duyên khéo léo diễn xuất ngoan ngoãn để Lâu Hỉ Dương che chở trước mặt Trương Sâm Trạch."
    },
    {
        "chapter_id": "ch_026",
        "chapter_title": "Chương 26: Đưa tôi về, Tưởng tiên sinh",
        "events": [
            "Lâu Hỉ Dương phát hiện Lâu An Minh cải trang trà trộn vào hàng phóng viên; chạm mắt Tưởng Trác Hàng.",
            "Tưởng Trác Hàng tuyên bố 99 ngày nữa khí độc sẽ tràn vào M tinh; paradise sẽ đóng cửa sau 60 ngày và cất cánh sau 90 ngày.",
            "Tưởng Trác Hàng tiếp cận nhóm Trần Liễm, ép Dịch Duyên làm trợ lý riêng và đòi xin Lâu Hỉ Dương (vệ sĩ) về dinh thự.",
            "Thuộc hạ báo tin về hành động của Lâu An Minh; Tưởng Trác Hàng uy hiếp: hoặc đưa vệ sĩ này về, hoặc đi thanh trừng kẻ ngốc không biết điều.",
            "Để cứu cha, Lâu Hỉ Dương đóng giả vệ sĩ xưng 'thiếu gia', ôm Dịch Duyên xin lỗi rồi lén rút khẩu súng laser sau lưng cậu, đồng ý theo Tưởng Trác Hàng.",
            "Dịch Duyên phát hiện mất súng, cảm xúc bùng nổ mất kiểm soát, bóp cổ Trần Liễm đòi súng laser."
        ],
        "debt_repayment_progress": "60%",
        "key_relationships": "Lâu Hỉ Dương hy sinh thân mình bảo vệ cha và Dịch Duyên; Dịch Duyên nổi cơn điên cuồng vì bị tách rời khỏi Lâu Hỉ Dương."
    },
    {
        "chapter_id": "ch_027",
        "chapter_title": "Chương 27: Ký chủ trong sạch khó giữ",
        "events": [
            "Dịch Duyên bị thiết bị kích điện phát cuồng, bị Trần Liễm và vệ sĩ đánh ngất áp giải về viện điều trị.",
            "Tưởng Trác Hàng đưa Lâu Hỉ Dương về biệt thự, đuổi trợ lý Jason và dặn chừa lối hoa viên cho Lâu An Minh lẻn vào.",
            "Tưởng Trác Hàng tháo mặt nạ Lâu Hỉ Dương, nhìn gương mặt giống hệt Lâu An Minh mà bàng hoàng run rẩy; Tiểu Thiết Chùy cảnh báo 99% dâm dục.",
            "Tiết lộ quá khứ của Tưởng Trác Hàng: từng mang mã số nô lệ tình dục do gia tộc Mike nuôi dưỡng, mượn khí độc để chôn vùi đám quý tộc.",
            "Tưởng Trác Hàng tiêm thuốc kích dục cực mạnh vào người Lâu Hỉ Dương, quay video sờ cơ bụng gửi cho Lâu An Minh ép xuất hiện, đồng thời tiện tay gửi cho Dịch Duyên."
        ],
        "debt_repayment_progress": "60%",
        "key_relationships": "Vạch trần ân oán tình thù giữa Tưởng Trác Hàng và Lâu An Minh; Lâu Hỉ Dương rơi vào tình thế nguy cấp."
    },
    {
        "chapter_id": "ch_028",
        "chapter_title": "Chương 28: Anh cũng thích em",
        "events": [
            "Lâu Hỉ Dương trúng thuốc quằn quại; Tưởng Trác Hàng sai Jason đưa đàn ông vào giải tỏa giúp anh.",
            "Trong phòng ngủ, Lâu Hỉ Dương tự giải quyết nhưng trong đầu chỉ toàn hiện lên khuôn mặt và tiếng gọi 'ca ca' của Dịch Duyên.",
            "Hệ thống phát cảnh báo trinh tiết nguy cấp, kích hoạt truyền tống không gian đưa Lâu Hỉ Dương trở về đại sảnh viện điều trị.",
            "Dịch Duyên xem video phát điên, thiết bị sau gáy cảnh báo đỏ; nghe tin Lâu Hỉ Dương về liền xông ra bắn thủng tay tên thuộc hạ dám chạm vào anh.",
            "Dịch Duyên bế bổng Lâu Hỉ Dương về phòng; Lâu Hỉ Dương mất kiểm soát ôm hôn cắn xé Dịch Duyên; cả hai có quan hệ thân mật thực sự.",
            "Dịch Duyên mê man tỏ tình: 'Ca ca, em thích anh'; Lâu Hỉ Dương cúi đầu hôn đáp lại: 'Ừ, anh cũng thích em'."
        ],
        "debt_repayment_progress": "60%",
        "key_relationships": "Bước ngoặt quan hệ trọng đại: Lâu Hỉ Dương chấp nhận tình cảm của Dịch Duyên, cả hai chính thức thành người yêu và phát sinh quan hệ thân mật."
    },
    {
        "chapter_id": "ch_029",
        "chapter_title": "Chương 29: Em ngoan lắm mà",
        "events": [
            "Hệ thống Thiết Chùy tỉnh lại sau 24h, kinh ngạc thông báo tiến độ trả nợ tăng vọt lên 82% (tăng 30% sau đêm ân ái).",
            "Lâu Hỉ Dương bế Dịch Duyên vào bồn tắm; nghiêm túc thổ lộ 'Anh thực sự thích em rồi, chúng ta ở bên nhau'; Dịch Duyên ngập tràn hạnh phúc rơi nước mắt.",
            "Dịch Duyên giải thích chỉ muốn yêu anh, bảo 'Em ngoan lắm mà'; Lâu Hỉ Dương dỗ dành và cưng chiều cậu.",
            "Lâu Hỉ Dương sang gặp Trần Liễm; Trần Liễm công khai thẻ tình báo viên liên sao và kết quả ADN chứng minh ông ta là CẬU RUỘT của Dịch Duyên.",
            "Trần Liễm kể về cái chết của em gái (mẹ Dịch Duyên) do Tưởng Trác Hàng sát hại 10 năm trước và lý do ông ta nằm vùng.",
            "Lâu Hỉ Dương nhờ Trần Liễm chuẩn bị bẻ khóa hệ thống để tháo thiết bị trước Lễ rơi tuyết; Trần Liễm dặn nếu sau này không chịu nổi tính khí Dịch Duyên thì đừng đá cậu quá tàn nhẫn."
        ],
        "debt_repayment_progress": "82%",
        "key_relationships": "Tình yêu được xác lập vững chắc; làm sáng tỏ thân thế gia đình Dịch Duyên (Trần Liễm là cậu ruột)."
    },
    {
        "chapter_id": "ch_030",
        "chapter_title": "Chương 30: Đừng khóc nữa",
        "events": [
            "Còn 3 ngày trước Lễ rơi tuyết, Lâu Hỉ Dương tập trung bẻ khóa để tháo thiết bị sau gáy cho Dịch Duyên, cố tình né tránh thân mật vì sợ mất kiểm soát.",
            "Dịch Duyên tủi thân, ngửi thấy mùi thuốc lá liền cãi nhau với anh vì muốn giữ thiết bị lấy chip bằng chứng; Lâu Hỉ Dương lạnh giọng quát bảo quay về phòng ngủ.",
            "Dịch Duyên khóc chạy đi, tiến độ trả nợ tụt 10% (xuống 72%); Thiết Chùy nhắc nhở Lâu Hỉ Dương rằng Dịch Duyên thiếu cảm giác an toàn và sợ anh hối hận.",
            "Dịch Duyên ra ngoài đánh người giải tỏa bực tức; sáng hôm sau Lâu Hỉ Dương đến phòng tháo thành công thiết bị cho cậu.",
            "Lâu Hỉ Dương chân thành thổ lộ hết tâm can: anh đau lòng khi thấy cậu đau, anh né tránh vì tim đập loạn nhịp khi ở cạnh cậu.",
            "Phát hiện gối Dịch Duyên ướt đẫm nước mắt, Lâu Hỉ Dương vén chăn ôm lấy cậu dỗ dành: 'Dịch Duyên, đừng khóc nữa'."
        ],
        "debt_repayment_progress": "72%",
        "key_relationships": "Tháo gỡ thành công xiềng xích thiết bị sau gáy; hai người thẳng thắn giãi bày giải tỏa mọi bất an và rào cản tâm lý."
    }
]

# Update or append
existing_ch_ids = [item['chapter_id'] for item in timeline]
for event in batch4_events:
    if event['chapter_id'] in existing_ch_ids:
        idx = existing_ch_ids.index(event['chapter_id'])
        timeline[idx] = event
    else:
        timeline.append(event)

with open(timeline_file, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print("Updated timeline.json successfully with Batch 4 events.")
