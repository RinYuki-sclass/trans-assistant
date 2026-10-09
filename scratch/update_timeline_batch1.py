import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

timeline_file = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"
with open(timeline_file, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter": "ch_032",
        "title": "Chương 32: Ôm đùi làm nũng",
        "summary": "Cố Xuyên sững sờ trước lời tỏ tình của Sở Niên Niên, lạnh lùng gạt đi và nghi ngờ cậu lại giở trò tâm cơ. Sở Niên Niên thi triển công phu trà xanh làm nũng, ôm đùi Cố Xuyên khóc lóc cầu xin. Cố Xuyên kiểm tra vết thương trên lưng Sở Niên Niên, thấy cậu không bị nhiễm độc tang thi bèn thở phào và dắt cậu về nhà kho.",
        "key_events": [
            "Cố Xuyên sốc trước câu tỏ tình của Sở Niên Niên và chất vấn cậu",
            "Sở Niên Niên nước mắt lưng tròng ôm đùi làm nũng, đòi theo Cố Xuyên bằng được",
            "Cố Xuyên kiểm tra vết thương sau lưng xác nhận Sở Niên Niên miễn nhiễm virus tang thi",
            "Cố Xuyên bất đắc dĩ kéo Sở Niên Niên đứng dậy đưa về nhà kho"
        ]
    },
    {
        "chapter": "ch_033",
        "title": "Chương 33: Dọn sạch tang thi",
        "summary": "Sở Niên Niên bước vào nhà kho khiến Lục Thiên và Lý Viện Viện cùng các đồng đội khác cảnh giác do tiền sử bất hảo. Cố Xuyên chủ động đưa bánh quy nén và nước cho Sở Niên Niên, đồng thời dặn dò đồng đội không được làm khó cậu. Cả đội bàn kế hoạch dọn dẹp tang thi và thu gom vật tư trước khi nghe thấy tiếng cầu cứu qua bộ đàm.",
        "key_events": [
            "Sở Niên Niên theo Cố Xuyên vào nhà kho, đối mặt với sự nghi ngại của Lục Thiên và Lý Viện Viện",
            "Cố Xuyên bảo vệ Sở Niên Niên, chia sẻ khẩu phần lương khô nước uống cho cậu",
            "Cả đội bàn kế hoạch thu gom vật tư và dọn sạch các đợt tang thi quanh thị trấn",
            "Nhận được tín hiệu cấp cứu khẩn cấp qua bộ đàm từ đoàn xe tiếp tế"
        ]
    },
    {
        "chapter": "ch_034",
        "title": "Chương 34: Lên xe đại lão",
        "summary": "Tín hiệu bộ đàm bị cắt đứt sau tiếng nổ lớn. Cố Xuyên chỉ huy nhóm lên xe xuất phát giải cứu người sống sót. Sở Niên Niên quấn quýt đòi đi theo, Cố Xuyên ngoài lạnh trong nóng cho cậu lên xe ngồi cạnh mình. Trên đường đi, Sở Niên Niên mệt mỏi ngủ thiếp đi và tựa đầu vào vai Cố Xuyên, khiến Cố Xuyên khẽ nín thở dung túng.",
        "key_events": [
            "Tín hiệu bộ đàm cầu cứu bị gián đoạn; Cố Xuyên hạ lệnh xuất phát chi viện",
            "Sở Niên Niên nũng nịu đòi đi cùng, Cố Xuyên đồng ý cho cậu lên xe riêng",
            "Sở Niên Niên tựa đầu ngủ ngon lành trên vai Cố Xuyên; Cố Xuyên ngoài mặt lạnh nhạt nhưng không nỡ đẩy ra",
            "Đến địa điểm tập kết, Cố Xuyên dặn Sở Niên Niên ở yên trên xe rồi xông ra tiêu diệt quái vật"
        ]
    },
    {
        "chapter": "ch_035",
        "title": "Chương 35: Cõng em",
        "summary": "Sau trận chiến quét sạch tang thi, Sở Niên Niên xuống xe tìm Cố Xuyên và than vãn chân bị trật khớp. Cố Xuyên dứt khoát cúi người cõng Sở Niên Niên trên lưng trước sự ngỡ ngàng của Lục Thiên và đồng đội. Sở Niên Niên ôm cổ Cố Xuyên, tận hưởng cảm giác an toàn quen thuộc như thời thơ ấu.",
        "key_events": [
            "Cố Xuyên cùng đội dị năng giải cứu thành công người sống sót",
            "Sở Niên Niên kêu đau chân làm nũng; Cố Xuyên bá đạo cúi người cõng cậu lên lưng",
            "Lục Thiên và Lý Viện Viện sững sờ trước sự cưng chiều khác thường của Cố Xuyên",
            "Thu gom tinh thạch dị năng và chuẩn bị lên đường hướng về căn cứ Long Thành"
        ]
    },
    {
        "chapter": "ch_036",
        "title": "Chương 36: Đột phá vòng vây",
        "summary": "Đoàn xe di chuyển trên đường cao tốc thì bị bầy tang thi biến dị bao vây tấn công. Cố Xuyên bộc phát dị năng sấm sét đỉnh cao dọn đường máu cho đoàn xe. Sở Niên Niên ngầm dùng năng lực khống chế quái vật giải vây lúc nguy cấp. Sau trận chiến, Cố Xuyên đưa tinh thạch cấp cao cho Sở Niên Niên giữ.",
        "key_events": [
            "Đoàn xe bị bầy tang thi biến dị phục kích trên đường cao tốc",
            "Cố Xuyên thi triển dị năng lôi điện kinh thiên mở đường máu cho cả đoàn",
            "Sở Niên Niên âm thầm hỗ trợ xua đuổi những đợt quái vật áp sát xe",
            "Cố Xuyên trao tinh thạch cấp cao cho Sở Niên Niên, mối quan hệ ngày càng khăng khít"
        ]
    },
    {
        "chapter": "ch_037",
        "title": "Chương 37: Làn sóng tang thi ập đến",
        "summary": "Đoàn xe tiến sát vành đai ngoài căn cứ Long Thành thì gặp làn sóng tang thi quy mô lớn tràn tới. Cố Xuyên bố trí phòng thủ nghiêm ngặt, giao Lục Thiên bảo vệ Sở Niên Niên. Sở Niên Niên nhất quyết không chịu rời đi trước mà kiên định ở lại hậu phương chờ đợi Cố Xuyên, thề đồng hành cùng anh đối mặt hiểm nguy.",
        "key_events": [
            "Đoàn xe đến gần căn cứ Long Thành thì đụng độ đợt triều tang thi quy mô khổng lồ",
            "Cố Xuyên chỉ huy phòng thủ tiền tuyến, yêu cầu Lục Thiên đưa Sở Niên Niên rút lui an toàn",
            "Sở Niên Niên từ chối bỏ chạy một mình, quyết tâm ở lại sát cánh bên Cố Xuyên",
            "Không khí căng thẳng tột độ báo hiệu cuộc đại chiến trước cổng căn cứ Long Thành"
        ]
    }
]

# Check existing
existing_cids = {item['chapter'] for item in timeline}
for entry in new_entries:
    if entry['chapter'] not in existing_cids:
        timeline.append(entry)

with open(timeline_file, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print(f"Updated timeline.json! Total chapters in timeline: {len(timeline)}")
