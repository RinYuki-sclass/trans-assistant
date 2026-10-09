import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

timeline_file = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"

with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter": "ch_052",
        "arc": "arc_02",
        "title": "Chương 52: Khắc tinh tang thi",
        "summary": "Cố Xuyên bộc phát toàn bộ dị năng hệ sấm sét đỉnh phong, càn quét vòng vây bầy tang thi cấp cao. Sở Niên Niên thi triển năng lực khắc chế đặc thù, âm thầm vô hiệu hóa đòn tấn công của tang thi chúa, giúp phòng tuyến Long Thành đứng vững.",
        "key_events": [
            "Cố Xuyên phát huy toàn bộ dị năng sấm sét đỉnh cao đẩy lùi tang thi biến dị",
            "Sở Niên Niên âm thầm hỗ trợ làm chậm và vô hiệu hóa tang thi chúa",
            "Phòng tuyến căn cứ Long Thành giữ vững trong gang tấc"
        ]
    },
    {
        "chapter": "ch_053",
        "arc": "arc_02",
        "title": "Chương 53: Đổi mới Long Thành",
        "summary": "Đợt triều tang thi bị đẩy lùi hoàn toàn khỏi bờ cõi căn cứ Long Thành. Cố Xuyên chỉ huy dọn dẹp chiến trường, thu giữ lượng lớn tinh thạch cấp cao. Nội bộ lãnh đạo cũ của căn cứ Long Thành rung chuyển; Cố Xuyên bắt đầu thanh trừng phe phái mục nát.",
        "key_events": [
            "Đẩy lùi hoàn toàn đợt triều tang thi, dọn sạch chiến trường",
            "Thu hoạch khối lượng lớn tinh thạch cấp cao từ quái vật",
            "Nội bộ căn cứ Long Thành chấn động trước sức mạnh và uy quyền của Cố Xuyên"
        ]
    },
    {
        "chapter": "ch_054",
        "arc": "arc_02",
        "title": "Chương 54: Thủ lĩnh tối cao",
        "summary": "Cố Xuyên chính thức tiếp quản quyền lực tối cao, trở thành thủ lĩnh duy nhất của căn cứ Long Thành. Địa vị của Sở Niên Niên được nâng lên ngang hàng thủ lĩnh; mọi người trong căn cứ đều kính cẩn và tôn trọng cậu.",
        "key_events": [
            "Cố Xuyên chính thức trở thành thủ lĩnh tối cao căn cứ Long Thành",
            "Sở Niên Niên được toàn bộ căn cứ kính nể và thừa nhận địa vị ngang hàng",
            "Cố Xuyên trao toàn bộ đặc quyền và vật tư tốt nhất cho Sở Niên Niên"
        ]
    },
    {
        "chapter": "ch_055",
        "arc": "arc_02",
        "title": "Chương 55: Tái thiết căn cứ",
        "summary": "Căn cứ Long Thành bước vào giai đoạn tái thiết toàn diện, phổ cập vắc xin phòng ngừa virus. Đời sống cư dân dần đi vào nề nếp ổn định; Cố Xuyên ngày đêm quấn quýt bên Sở Niên Niên, tình cảm giữa hai người vô cùng thắm thiết.",
        "key_events": [
            "Tái thiết toàn diện cơ sở hạ tầng căn cứ Long Thành và phổ cập vắc xin",
            "Cuộc sống hòa bình và nụ cười trở lại với người dân trong mạt thế",
            "Cố Xuyên và Sở Niên Niên gắn bó keo sơn không rời nửa bước"
        ]
    },
    {
        "chapter": "ch_056",
        "arc": "arc_02",
        "title": "Chương 56: Kịch bản hoàn thành",
        "summary": "Hệ thống Mật Bảo vang lên thông báo: Độ hảo cảm của Cố Xuyên đạt 100%, nhiệm vụ kịch bản yêu đương hoàn thành xuất sắc. Sở Niên Niên nhận được quyền chọn rút lui sang thế giới kế tiếp, cậu bắt đầu do dự trước tình cảm sâu đậm của Cố Xuyên.",
        "key_events": [
            "Hệ thống thông báo độ hảo cảm đạt 100%, nhiệm vụ hoàn thành toàn diện",
            "Sở Niên Niên chuẩn bị thoát ly thế giới mạt thế",
            "Sở Niên Niên dằn vặt và quyến luyến trước tình yêu chân thành của Cố Xuyên"
        ]
    },
    {
        "chapter": "ch_057",
        "arc": "arc_02",
        "title": "Chương 57: Chạy trốn bất thành",
        "summary": "Sở Niên Niên toan lặng lẽ rời khỏi căn hộ giữa đêm khuya để thoát ly thế giới thì bị Cố Xuyên phát hiện kịp thời. Cố Xuyên chặn ngay cửa ra vào, ôm chặt lấy cậu từ phía sau, ánh mắt đỏ ngầu ghen tuông và tuyệt vọng cấm cậu rời xa mình.",
        "key_events": [
            "Sở Niên Niên lén lút thu dọn hành lý định chuồn đi giữa đêm",
            "Cố Xuyên chặn đường bắt quả tang, ôm chặt cậu từ phía sau",
            "Cố Xuyên bùng nổ chiếm hữu và van nài cậu ở lại bên anh trọn đời"
        ]
    },
    {
        "chapter": "ch_058",
        "arc": "arc_02",
        "title": "Chương 58: Ngoại truyện viên mãn - Kết thúc Thế giới 2",
        "summary": "Cố Xuyên bá đạo tuyên bố: 'Muốn chạy? Ai đào tinh thạch cho em, ai cho em ăn, ai ngủ cùng em cả đời?'. Sở Niên Niên đầu hàng trước sự dung túng yêu chiều vô điều kiện của đại lão, cam tâm tình nguyện ở lại. Kết thúc viên mãn Thế giới 2 và chuyển tiếp sang Thế giới 3 (Trùng tộc).",
        "key_events": [
            "Cố Xuyên bá đạo tuyên bố quyền sở hữu trọn đời đối với Sở Niên Niên",
            "Sở Niên Niên ngọt ngào đồng ý làm dây tơ hồng cả đời cho Cố Xuyên",
            "Đại kết cục viên mãn của Thế giới 2 (Mạt thế tang thi)",
            "Đoạn preview ngắn chuyển giao sang Thế giới 3 (Trùng tộc: Gavin x Eli)"
        ]
    }
]

existing_cids = {item['chapter'] for item in timeline}
for entry in new_entries:
    if entry['chapter'] not in existing_cids:
        timeline.append(entry)
    else:
        # Update existing
        for i, item in enumerate(timeline):
            if item['chapter'] == entry['chapter']:
                timeline[i] = entry

with open(timeline_file, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print(f"Updated timeline.json! Total chapters in timeline: {len(timeline)}")
