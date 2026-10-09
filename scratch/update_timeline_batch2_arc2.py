import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

timeline_file = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"
with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter": "ch_038",
        "title": "Chương 38: Sống chung một phòng",
        "summary": "Cố Xuyên xếp Sở Niên Niên ở chung phòng nghỉ riêng trong khu an toàn. Đêm đó Cố Xuyên phát sốt mê man vì độc tố tích tụ; Sở Niên Niên ở bên chăm sóc và bón nước cho anh. Trong cơn mê, Cố Xuyên nhìn nhầm Sở Niên Niên thành bạch nguyệt quang đã khuất. Hệ thống Mật Bảo kích hoạt kịch bản yêu đương, Sở Niên Niên bực bội cắn môi Cố Xuyên tuyên bố chủ quyền.",
        "key_events": [
            "Cố Xuyên xếp Sở Niên Niên ở chung phòng riêng trong khu căn cứ",
            "Cố Xuyên phát sốt mê man, Sở Niên Niên tận tình bón nước chăm sóc suốt đêm",
            "Cố Xuyên mê sảng nhìn nhầm Sở Niên Niên thành chị gái đã khuất",
            "Sở Niên Niên giận dỗi cắn môi Cố Xuyên tuyên bố chủ quyền"
        ]
    },
    {
        "chapter": "ch_039",
        "title": "Chương 39: Ngắm nhìn cơ bắp",
        "summary": "Cố Xuyên tỉnh dậy sau cơn sốt, cảm thấy môi đau nhức và nhận ra Sở Niên Niên đã chăm sóc mình cả đêm. Cố Xuyên cởi áo để lộ thân hình vạm vỡ, cơ bắp cuồn cuộn khiến Sở Niên Niên ngắm mê mẩn. Lục Thiên và Lý Viện Viện đến báo cáo tình hình. Cố Xuyên quyết định giữ Sở Niên Niên ở lại phòng mình để tiện giám sát và bảo bọc.",
        "key_events": [
            "Cố Xuyên hạ sốt tỉnh dậy, nhận ra Sở Niên Niên đã chăm sóc mình cả đêm",
            "Cố Xuyên cởi trần để lộ cơ bắp cuồn cuộn khiến Sở Niên Niên nhìn đăm đắm",
            "Lục Thiên và Lý Viện Viện đến báo cáo tình hình căn cứ",
            "Cố Xuyên giữ Sở Niên Niên ở lại phòng mình chăm sóc bảo bọc"
        ]
    },
    {
        "chapter": "ch_040",
        "title": "Chương 40: Ngủ chung một giường",
        "summary": "Đêm mạt thế nhiệt độ hạ thấp đột ngột, gió lạnh thấu xương. Hệ thống Mật Bảo giao nhiệm vụ bắt buộc: Sở Niên Niên phải ngủ chung một giường với Cố Xuyên. Sở Niên Niên ôm gối run rẩy trèo lên giường làm nũng đòi sưởi ấm. Cố Xuyên ngoài miệng lạnh lùng đe dọa nhưng cuối cùng vẫn kéo chăn đắp cho cậu và để cậu nép vào lòng.",
        "key_events": [
            "Đêm đông mạt thế nhiệt độ hạ thấp đột ngột",
            "Hệ thống Mật Bảo giao nhiệm vụ cưỡng chế ngủ chung giường với Cố Xuyên",
            "Sở Niên Niên ôm gối trèo lên giường làm nũng cầu sưởi ấm",
            "Cố Xuyên lạnh lùng cảnh cáo nhưng không nỡ đẩy ra, kéo chăn ôm cậu vào lòng"
        ]
    },
    {
        "chapter": "ch_041",
        "title": "Chương 41: Hơi ấm đêm đông",
        "summary": "Cố Xuyên ôm Sở Niên Niên trong lòng, nhiệt độ cơ thể ấm áp xua tan cái lạnh giá. Sở Niên Niên nhân cơ hội lén hôn nhẹ lên cằm và môi Cố Xuyên khiến Cố Xuyên tim đập loạn nhịp nín thở. Sáng hôm sau, Lục Thiên và chú Bụng Bia gõ cửa mang đồ ăn sáng đến, ngỡ ngàng thấy hai người ngủ chung giường.",
        "key_events": [
            "Cố Xuyên ôm Sở Niên Niên sưởi ấm đêm đông, tim đập thình thịch",
            "Sở Niên Niên lén hôn cằm và môi Cố Xuyên khiến anh bối rối",
            "Lục Thiên và chú Bụng Bia bắt gặp hai người ở chung phòng",
            "Chú Bụng Bia trêu chọc chuyện tình cảm khiến Cố Xuyên ngượng ngùng đuổi khéo"
        ]
    },
    {
        "chapter": "ch_042",
        "title": "Chương 42: Dạo quanh căn cứ",
        "summary": "Cố Xuyên dắt Sở Niên Niên đi dạo khảo sát tình hình các khu vực xung quanh căn cứ. Sở Niên Niên ngoan ngoãn đi bên cạnh Cố Xuyên, thu hút nhiều ánh mắt tò mò. Cố Xuyên đào được rất nhiều tinh thạch cao cấp và đưa hết cho Sở Niên Niên hấp thụ nâng cao thể chất. Sở Niên Niên ngủ say gối đầu lên đùi Cố Xuyên làm nũng.",
        "key_events": [
            "Cố Xuyên dắt Sở Niên Niên đi dạo quanh khu căn cứ",
            "Cố Xuyên đào nhiều tinh thạch cao cấp đưa hết cho Sở Niên Niên hấp thụ",
            "Mọi người nhận ra sự cưng chiều ngoại lệ của Cố Xuyên dành cho Sở Niên Niên",
            "Sở Niên Niên ngủ say gối đầu lên đùi Cố Xuyên, lẩm bẩm làm nũng"
        ]
    },
    {
        "chapter": "ch_043",
        "title": "Chương 43: Bữa ăn ấm cúng",
        "summary": "Bữa cơm tập thể ấm cúng diễn ra tại phòng ăn chung của nhóm tinh anh. Sở Niên Niên ân cần gắp thức ăn, dỗ dành Cố Xuyên ăn nhiều thịt để bồi bổ sức khỏe. Cố Xuyên gắp thức ăn đáp lại, ngầm thừa nhận mối quan hệ trước toàn đội. Đang lúc vui vẻ thì còi báo động căn cứ hú vang: đàn tang thi biến dị bất ngờ áp sát.",
        "key_events": [
            "Bữa cơm tập thể ấm cúng giữa Cố Xuyên, Sở Niên Niên và đồng đội",
            "Sở Niên Niên gắp thức ăn dỗ dành Cố Xuyên; Cố Xuyên gắp lại ngầm thừa nhận tình cảm",
            "Đồng đội ngưỡng mộ bầu không khí ngọt ngào giữa hai người",
            "Còi báo động hú vang báo hiệu đợt tang thi biến dị đột kích căn cứ"
        ]
    },
    {
        "chapter": "ch_044",
        "title": "Chương 44: Rung động",
        "summary": "Tang thi tràn vào khu vực cầu thang, Cố Xuyên chỉ huy đội ngũ nghênh chiến. Trong lúc hỗn loạn, Sở Niên Niên bị tách khỏi đoàn nhưng dùng năng lực đặc biệt áp chế tang thi xung quanh. Cố Xuyên điên cuồng tìm kiếm và lao tới ôm chầm lấy Sở Niên Niên, run rẩy kiểm tra vết thương. Cố Xuyên chính thức rung động mãnh liệt, nhận ra tầm quan trọng của Sở Niên Niên trong lòng mình.",
        "key_events": [
            "Bầy tang thi tràn vào khu nhà, tình thế ngàn cân treo sợi tóc",
            "Sở Niên Niên ngầm dùng dị năng áp chế bầy quái vật tự bảo vệ mình",
            "Cố Xuyên hoảng loạn tìm kiếm và ôm chặt lấy Sở Niên Niên vào lòng",
            "Cố Xuyên chính thức rung động sâu sắc, thề bảo vệ Sở Niên Niên trọn đời"
        ]
    }
]

existing_cids = {item['chapter'] for item in timeline}
for entry in new_entries:
    if entry['chapter'] not in existing_cids:
        timeline.append(entry)

with open(timeline_file, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print(f"Updated timeline.json! Total chapters in timeline: {len(timeline)}")
