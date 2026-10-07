import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

timeline_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"

with open(timeline_path, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

# Keep only ch_001 to ch_007 first
timeline = [x for x in timeline if int(x['chapter'].replace('ch_', '')) <= 7]

batch2_events = [
    {
        "chapter": "ch_008",
        "title": "Chương 8: Cho cậu đấy",
        "summary": "Bạch Huân say mê xe cộ; Tần Diễm ngoài mặt khó chịu nhưng chủ động đưa thẻ/chìa khóa và chia sẻ đồ uống với Bạch Huân. Tương tác mập mờ giữa hai người ở giảng đường khiến bạn học chú ý.",
        "key_events": [
            "Bạch Huân lộ sở thích đam mê xe cộ cuồng nhiệt",
            "Tần Diễm đưa chìa khóa xe cho Bạch Huân",
            "Tần Diễm bực bội đổi ly cà phê nhưng liên tục chú ý đến Bạch Huân"
        ]
    },
    {
        "chapter": "ch_009",
        "title": "Chương 9: Cậu ta muốn tỏ tình",
        "summary": "Bạch Huân cùng Tần Diễm vào phòng thay đồ thử áo sơ mi. Bạch Huân biết được kế hoạch Tần Diễm chuẩn bị tỏ tình trong chuyến dã ngoại; Hệ thống phát cảnh báo nhiệm vụ ngăn chặn.",
        "key_events": [
            "Tần Diễm cho Bạch Huân mượn áo sơ mi đen trong phòng thay đồ",
            "Bạch Huân nghe được kế hoạch dã ngoại leo núi để tỏ tình của Tần Diễm",
            "Hệ thống Yêu Đương phát cảnh báo nhiệm vụ can thiệp kịch bản"
        ]
    },
    {
        "chapter": "ch_010",
        "title": "Chương 10: Đã sống chung rồi",
        "summary": "Cả lớp tham gia chuyến dã ngoại leo núi cuối tuần. Trên chuyến xe chở đoàn, Tần Diễm ngủ say và vô thức tựa đầu vào vai Bạch Huân suốt chặng đường, bị bạn bè bắt gặp.",
        "key_events": [
            "Khởi hành chuyến dã ngoại ngoại khóa leo núi",
            "Tần Diễm ngủ gật và gục đầu tựa sát vai Bạch Huân",
            "Hội bạn thân Chu Táp, Lý Nhĩ kinh ngạc trước cảnh tượng thân mật của hai người"
        ]
    },
    {
        "chapter": "ch_011",
        "title": "Chương 11: Tiểu thuyết ngôn tình Mary Sue",
        "summary": "Tần Diễm thức giấc ngượng ngùng khi thấy mình tựa vào cổ Bạch Huân. Khi leo núi xảy ra sự cố nguy hiểm, Bạch Huân nhanh nhẹn giải cứu mọi người; Nụ cười dịu dàng của anh khiến tim Tần Diễm đập thình thịch.",
        "key_events": [
            "Tần Diễm bối rối xấu hổ sau khi thức giấc trên vai Bạch Huân",
            "Sự cố trượt chân nguy hiểm trên vách núi dốc",
            "Bạch Huân kịp thời ra tay cứu nguy, nụ cười làm Tần Diễm rung động mãnh liệt"
        ]
    },
    {
        "chapter": "ch_012",
        "title": "Chương 12: Tôi đến từ vùng núi",
        "summary": "Đoàn cắm trại dựng lều trên đỉnh núi. Bạch Huân thể hiện kỹ năng sinh tồn và tháo vát phi thường nhờ xuất thân vùng núi, khiến đại thiếu gia Tần Diễm tâm phục khẩu phục khen ngợi.",
        "key_events": [
            "Hoạt động dựng lều và sinh tồn ngoài trời trên núi",
            "Bạch Huân thành thạo giải quyết mọi khó khăn nhờ kinh nghiệm lớn lên từ vùng núi",
            "Tần Diễm chân thành khen ngợi: 'Bạch Huân, cậu rất giỏi'"
        ]
    },
    {
        "chapter": "ch_013",
        "title": "Chương 13: Ngoài ý muốn",
        "summary": "Buổi tối trên núi, Tần Diễm tách đoàn và bất ngờ chạm trán rắn độc bên rìa vách núi dốc. Trong lúc hoảng loạn lùi bước, Tần Diễm trượt chân ngã xuống vực sâu; Bạch Huân không màng nguy hiểm lao mình ra cứu.",
        "key_events": [
            "Tần Diễm hoảng hốt đối mặt với rắn độc trong đêm tối",
            "Tần Diễm trượt chân rơi khỏi mép vực sâu nguy hiểm",
            "Bạch Huân liều mình phi thân lao theo để bắt lấy Tần Diễm"
        ]
    },
    {
        "chapter": "ch_014",
        "title": "Chương 14: Cậu thật kỳ lạ",
        "summary": "Hai người lăn xuống sườn dốc và tìm thấy một hang đá trú ẩn trong đêm mưa lạnh. Bạch Huân cởi áo ướt sưởi ấm, chăm sóc và băng bó cho Tần Diễm. Tần Diễm bối rối tột độ trước sự ân cần của Bạch Huân.",
        "key_events": [
            "Hai người sống sót rơi vào sườn dốc và lánh nạn trong hang đá",
            "Bạch Huân cởi áo sưởi ấm bên đống lửa và chăm sóc vết thương cho Tần Diễm",
            "Bầu không khí mập mờ, tim Tần Diễm hoàn toàn bị thao túng"
        ]
    },
    {
        "chapter": "ch_015",
        "title": "Chương 15: Chơi thật đấy à",
        "summary": "Sáng hôm sau hai người được đội cứu hộ tìm thấy an toàn. Chu Táp lỡ tay vứt mất chiếc kính gọng vàng bị vỡ của Bạch Huân; Tần Diễm cảm kích và xót xa bèn âm thầm đặt mua đền chiếc kính hàng hiệu cao cấp cho anh.",
        "key_events": [
            "Đội cứu hộ tìm thấy Bạch Huân và Tần Diễm an toàn rời khỏi núi",
            "Chu Táp vứt mất chiếc kính gọng vàng vỡ tròng của Bạch Huân",
            "Tần Diễm âm thầm chi tiền đặt mua cặp kính gọng vàng mới đắt giá tặng Bạch Huân"
        ]
    }
]

timeline.extend(batch2_events)

with open(timeline_path, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print(f"Updated timeline.json successfully with {len(timeline)} chapters!")
