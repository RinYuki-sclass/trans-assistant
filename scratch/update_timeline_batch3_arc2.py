import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

timeline_file = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"
with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter": "ch_045",
        "title": "Chương 45: Tang thi triều tập kích",
        "summary": "Còi báo động căn cứ hú vang rền rĩ: làn sóng tang thi quy mô lớn ập đến bao vây khu vực. Cố Xuyên chỉ huy tuyến đầu đối phó lũ quái vật; Sở Niên Niên âm thầm hỗ trợ bảo vệ đồng đội. Bầy quái vật biến dị hung hãn liên tục chọc thủng các công trình phòng thủ ngoài rìa căn cứ. Lục Thiên và các thành viên hoảng hốt khi tang thi cấp cao áp sát khu dân cư.",
        "key_events": [
            "Còi báo động căn cứ hú vang báo hiệu đợt triều tang thi quy mô khổng lồ",
            "Cố Xuyên chỉ huy tuyến đầu đối phó bầy quái vật",
            "Sở Niên Niên âm thầm dùng dị năng hỗ trợ giải cứu đồng đội",
            "Tang thi biến dị cấp cao xuất hiện phá tan phòng tuyến ngoài"
        ]
    },
    {
        "chapter": "ch_046",
        "title": "Chương 46: Phòng thủ tiền tuyến",
        "summary": "Cố Xuyên dốc toàn lực chiến đấu ở tiền tuyến ác liệt, cản đường bầy tang thi hung hãn. Sở Niên Niên lo lắng chờ đợi ở hậu phương, không chịu di tản mà ở lại tiếp tế. Hai người xảy ra tranh cãi nhỏ khi Cố Xuyên yêu cầu Sở Niên Niên lui về nơi an toàn. Sở Niên Niên giận dỗi không thèm nhìn mặt Cố Xuyên nhưng vẫn ngấm ngầm để ý đến anh.",
        "key_events": [
            "Cố Xuyên chiến đấu quyết liệt tại tiền tuyến khói lửa",
            "Sở Niên Niên kiên quyết ở lại hậu phương hỗ trợ, không chịu bỏ chạy",
            "Tranh cãi gay gắt giữa Cố Xuyên và Sở Niên Niên vì lo lắng cho sự an toàn của nhau",
            "Sở Niên Niên giận dỗi cố tình ngó lơ nhưng trong lòng vẫn bồn chồn lo sợ cho Cố Xuyên"
        ]
    },
    {
        "chapter": "ch_047",
        "title": "Chương 47: Hy sinh anh dũng",
        "summary": "Phòng tuyến bị quái vật biến dị chọc thủng dữ dội, tình thế ngàn cân treo sợi tóc. Chú Bụng Bia dũng cảm lao ra chắn đường tang thi biến dị cấp cao để cứu đồng đội và hy sinh. Lục Thiên và Lý Viện Viện khóc ngất trước sự ra đi đau đớn của người đồng đội trung niên. Sở Niên Niên trừng phạt kẻ khiêu khích và thể hiện sức mạnh áp đảo khiến Lục Thiên kinh ngạc.",
        "key_events": [
            "Phòng tuyến bị chọc thủng, quái vật tàn sát dữ dội",
            "Chú Bụng Bia hy sinh anh dũng để cứu lấy Lục Thiên và đồng đội",
            "Toàn đội chìm trong tang thương và nước mắt",
            "Sở Niên Niên bộc lộ năng lực áp chế khiến Lục Thiên sững sờ"
        ]
    },
    {
        "chapter": "ch_048",
        "title": "Chương 48: Nỗi đau và an ủi",
        "summary": "Cả đội tiến hành chôn cất chú Bụng Bia trong bầu không khí đau thương tột cùng. Cố Xuyên chìm trong dằn vặt và tự trách bản thân vì không bảo vệ được đồng đội. Sở Niên Niên lặng lẽ ôm chặt lấy Cố Xuyên, dùng hơi ấm và lời nói dịu dàng an ủi anh. Cố Xuyên ôm chặt Sở Niên Niên cầu xin cậu giúp đỡ và ở bên cạnh mình.",
        "key_events": [
            "Chôn cất chú Bụng Bia trong khu rừng hoang",
            "Cố Xuyên dằn vặt suy sụp vì sự mất mát của đồng đội thân cận",
            "Sở Niên Niên dịu dàng ôm chặt an ủi Cố Xuyên",
            "Cố Xuyên ôm chặt Sở Niên Niên cầu xin cậu ở lại bên cạnh mình"
        ]
    },
    {
        "chapter": "ch_049",
        "title": "Chương 49: Điểm yếu duy nhất",
        "summary": "Sở Niên Niên lau người và xoa bóp cho Cố Xuyên sau những ngày chiến đấu kiệt sức. Cố Xuyên lần đầu tiên bộc lộ góc khuất yếu đuối, đau thương trước mặt Sở Niên Niên. Cố Xuyên hỏi về chiếc bánh kem 11 năm trước; Sở Niên Niên giải thích lý do nhờ chị gái mang tặng. Cố Xuyên nhận ra tình cảm chân thành sâu nặng của Sở Niên Niên từ thuở niên thiếu.",
        "key_events": [
            "Sở Niên Niên ân cần chăm sóc lau người cho Cố Xuyên",
            "Cố Xuyên bộc lộ khía cạnh yếu đuối duy nhất trước mặt Sở Niên Niên",
            "Hóa giải hiểu lầm về chiếc bánh kem 11 năm trước thời trung học",
            "Cố Xuyên thấu hiểu và rung động trước tấm chân tình của Sở Niên Niên"
        ]
    },
    {
        "chapter": "ch_050",
        "title": "Chương 50: Quyết không chạy trốn",
        "summary": "Tang thi triều tổng lực quy mô lớn nhất bắt đầu đổ bộ bao vây căn cứ. Cố Xuyên sắp xếp cho đoàn người rút lui, bảo Lục Thiên dẫn Sở Niên Niên đi trước. Sở Niên Niên kiên quyết từ chối trốn chạy một mình, quyết tâm ở lại cùng Cố Xuyên chiến đấu. Sở Niên Niên thể hiện dũng khí bảo vệ Cố Xuyên khiến toàn bộ căn cứ chấn động.",
        "key_events": [
            "Đợt tổng tấn công lớn nhất của tang thi triều ập đến",
            "Cố Xuyên yêu cầu Lục Thiên đưa Sở Niên Niên di tản khẩn cấp",
            "Sở Niên Niên kiên quyết không bỏ chạy, ở lại sát cánh bên Cố Xuyên",
            "Quyết tâm sống chết có nhau giữa khói lửa mạt thế"
        ]
    },
    {
        "chapter": "ch_051",
        "title": "Chương 51: Nụ hôn giữa khói lửa",
        "summary": "Chiến sự tạm lắng trong khoảnh khắc yên bình hiếm hoi giữa bầu trời đêm lấp lánh ánh sao. Cố Xuyên và Sở Niên Niên đứng cạnh nhau giữa tàn tích khói lửa chiến trường. Cố Xuyên trao cho Sở Niên Niên nụ hôn nồng cháy sâu đậm đầu tiên, xác nhận tình yêu. Cố Xuyên thề bảo vệ Sở Niên Niên trọn đời, chuẩn bị cho trận quyết chiến cuối cùng.",
        "key_events": [
            "Khoảnh khắc tĩnh lặng hiếm hoi giữa chiến trường tan hoang",
            "Cố Xuyên và Sở Niên Niên ngắm bầu trời sao bên cạnh nhau",
            "Nụ hôn sâu đầu tiên nồng nàn giữa khói lửa chiến tranh",
            "Cố Xuyên thề nguyện bảo vệ Sở Niên Niên trọn đời trọn kiếp"
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
