# -*- coding: utf-8 -*-
import json

path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\memory\timeline.json"

with open(path, "r", encoding="utf-8") as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter_id": "ch_016",
        "chapter_title": "Chương 16: Hắn cũng giống như em",
        "events": [
            "Bác sĩ ép Lâu Hỉ Dương nhận hộ lý che mặt chăm sóc vết thương bụng; Lâu Hỉ Dương nghi ngờ đối phương là tai mắt.",
            "Trương Sâm Trạch dẫn đàn em vào thăm nhưng bị hộ lý chặn ở cửa; hai bên suýt ẩu đả.",
            "Trương Sâm Trạch vào phòng cảnh báo Dịch Duyên rất nguy hiểm và thổ lộ 'cậu ta cũng giống tôi, đều thích cậu'.",
            "Lâu Hỉ Dương từ chối tình cảm của Trương Sâm Trạch; tranh thủ lúc hộ lý vắng mặt đi thám thính toàn bộ viện điều trị, phát hiện tầng thượng có khu vực bí mật.",
            "Về phòng gặp lại hộ lý, Lâu Hỉ Dương vào nhà vệ sinh thì hộ lý xông vào đòi giúp đỡ."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Trương Sâm Trạch thừa nhận thích Lâu Hỉ Dương nhưng bị cự tuyệt; Lâu Hỉ Dương bắt đầu để ý các cử chỉ quen thuộc của hộ lý."
    },
    {
        "chapter_id": "ch_017",
        "chapter_title": "Chương 17: Anh đã làm gì",
        "events": [
            "Lâu Hỉ Dương cởi quần áo đi vệ sinh làm lộ cơ bắp và vết thương bị toác; hộ lý xót xa mắng anh không biết giữ gìn sức khỏe.",
            "Lâu Hỉ Dương nhận ra khẩu khí hộ lý rất giống Dịch Duyên nhưng nghi ngờ vì chiều cao và giọng nói khác biệt.",
            "Hộ lý chu đáo đút từng thìa cháo trứng và ức gà cho Lâu Hỉ Dương.",
            "Dịch Duyên quay về phòng thí nghiệm tầng thượng, tháo mặt nạ và giày độn đế; Trần Liễm mắng cậu vì đánh Lý Bưu thừa sống thiếu chết.",
            "Hé lộ Dịch Duyên bị cấy thiết bị trích xuất chip sau gáy nối với hệ thống trung tâm, gây đau tim dữ dội; dữ liệu chứng minh ở cạnh Lâu Hỉ Dương giúp cảm xúc cậu ổn định nhất."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Dịch Duyên âm thầm gánh chịu nỗi đau thể xác vì Lâu Hỉ Dương; sự gắn kết tâm lý sâu sắc giữa hai người."
    },
    {
        "chapter_id": "ch_018",
        "chapter_title": "Chương 18: Tầng thượng",
        "events": [
            "Lâu Hỉ Dương gọi nhiều cuộc video cho Dịch Duyên không được, đe dọa hệ thống Thiết Chùy; hệ thống nhắc nhở không được làm trái ý nguyện của chủ nợ.",
            "Lâu An Minh đeo mặt nạ da người đến thăm, trách Lâu Hỉ Dương thiếu cẩn trọng để bị thương.",
            "Lâu Hỉ Dương tiễn cha rồi lén lút trèo qua tường cỏ C sau xích đu, phát hiện cửa bí mật phía sau viện điều trị.",
            "Lâu Hỉ Dương đánh ngất 2 nhân viên nghiên cứu mặc áo blouse trắng, cướp thẻ từ và quần áo đi thang máy bí mật lên tầng 1.",
            "Lên tới đại sảnh tím sẫm, Lâu Hỉ Dương bị lính canh gác chĩa súng laze tra hỏi; hộ lý kịp thời xuất hiện chìa thẻ cứu anh."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương xót ruột nhớ Dịch Duyên; bắt đầu thâm nhập vào khu vực bí mật tầng trên."
    },
    {
        "chapter_id": "ch_019",
        "chapter_title": "Chương 19: Đưa cậu ấy đi",
        "events": [
            "Hộ lý đưa Lâu Hỉ Dương về phòng bệnh; Lâu Hỉ Dương ép hộ lý vào cửa chất vấn và ép tháo mặt nạ.",
            "Hộ lý phản kháng quyết liệt nhưng ngất xỉu vì đau tim; Lâu Hỉ Dương tháo mặt nạ ra bàng hoàng nhận ra đó chính là Dịch Duyên.",
            "Dịch Duyên tủi thân ôm cổ anh xin lỗi; Lâu Hỉ Dương phát hiện khối thiết bị cấy ghép đau đớn sau gáy cậu.",
            "Biết Dịch Duyên chịu đau đớn để bóc tách con chip vì muốn cứu mình, Lâu Hỉ Dương phẫn nộ và tự trách tột cùng, tuyên bố 'Em quan trọng hơn'.",
            "Lâu Hỉ Dương quyết định không để Dịch Duyên ở lại chịu khổ nữa, gọi điện nhờ Trương Sâm Trạch điều xe đến giải cứu."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương nhận ra hộ lý là Dịch Duyên; cảm xúc vượt lên trên lý trí khi quyết định đưa cậu trốn viện."
    },
    {
        "chapter_id": "ch_020",
        "chapter_title": "Chương 20: Anh lại hôn em rồi",
        "events": [
            "Trương Sâm Trạch dẫn người đến làm thủ tục xuất viện; sững sờ khi thấy Lâu Hỉ Dương ôm Dịch Duyên ngủ trên giường.",
            "Lâu Hỉ Dương thay quần áo cho Dịch Duyên đang hôn mê, vô tình nhìn thấy hình xăm mặt trời đỏ ở xương cụt kéo dài vào sâu.",
            "Dịch Duyên tỉnh lại thì thào 'Em xăm anh lên người em, em là của anh'; hai người kích tình ôm hôn nồng cháy trên giường.",
            "Lâu Hỉ Dương trấn an Dịch Duyên và đưa cậu ra xe cùng Trương Sâm Trạch, quyết tâm cắt bỏ thiết bị định vị trong vòng 3 tiếng."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Nụ hôn nồng cháy xác nhận tình cảm; Lâu Hỉ Dương thừa nhận 'Em quan trọng hơn' và đưa Dịch Duyên chạy trốn."
    },
    {
        "chapter_id": "ch_021",
        "chapter_title": "Chương 21: Yêu đương",
        "events": [
            "Đến khu đèn đỏ sào huyệt của Trương Sâm Trạch, Dịch Duyên bắt đền Lâu Hỉ Dương phải chịu trách nhiệm vì đã hôn và cởi áo mình.",
            "Dịch Duyên đề nghị Lâu Hỉ Dương giả vờ làm bạn trai; Lâu Hỉ Dương đồng ý và bối rối học cách yêu đương.",
            "Dịch Duyên kéo tay Lâu Hỉ Dương chỉ dẫn cách yêu đương khiến Lâu Hỉ Dương đỏ mặt xấu hổ.",
            "Trần Liễm gọi điện đe dọa nếu quá 4 tiếng không về viện Dịch Duyên sẽ chết; thợ kỹ thuật của Trương Sâm Trạch bó tay không gỡ được thiết bị.",
            "Lâu Hỉ Dương vội vã lái xe đưa Dịch Duyên quay về viện điều trị; trên đường đi bất ngờ bị một chiếc xe tải thùng kín đâm mạnh từ phía sau."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương chính thức đồng ý làm 'bạn trai' của Dịch Duyên; nảy sinh nhiều tiếp xúc thân mật."
    },
    {
        "chapter_id": "ch_022",
        "chapter_title": "Chương 22: Nhốt người nào",
        "events": [
            "Tài xế xe tải giả vờ xin lỗi; trong thùng xe xa hoa thực chất là Thủ lĩnh Liên bang Tưởng Trác Hàng ngồi quan sát.",
            "Lâu Hỉ Dương cõng Dịch Duyên chạy nước rút như bay về viện điều trị trong 15 phút cuối cùng.",
            "Về tới nơi an toàn cho Dịch Duyên, Lâu Hỉ Dương đấm vỡ mũi Trần Liễm rồi kiệt sức ngất xỉu.",
            "Tỉnh lại trong phòng Dịch Duyên, Trần Liễm đề nghị hợp tác: cho phép Lâu Hỉ Dương làm vệ sĩ ở cạnh Dịch Duyên.",
            "Trần Liễm tiết lộ chính Dịch Duyên đã đổi điều kiện để ông ta phá hỏng hệ thống phòng vệ Tây Lăng Sơn cho Lâu Hỉ Dương cứu cha.",
            "Lâu Hỉ Dương hỏi tầng hai giam giữ ai; Trần Liễm tiết lộ đó là 'tiểu tình nhân bị Tưởng Trác Hàng cướp về' (mẹ Lâu Hỉ Dương)."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương biết được sự hy sinh âm thầm của Dịch Duyên vì mình; đồng ý ở lại làm vệ sĩ cạnh cậu."
    },
    {
        "chapter_id": "ch_023",
        "chapter_title": "Chương 23: Sờ sờ",
        "events": [
            "Trần Liễm đưa mặt nạ cho Lâu Hỉ Dương đóng vai vệ sĩ; Lâu Hỉ Dương ôm hôn Dịch Duyên đầy hối lỗi và nhận ra kiếp trước đã hiểu lầm cậu.",
            "Dịch Duyên đòi 'phúc lợi bạn trai' bắt Lâu Hỉ Dương sờ soạng xoa dịu cơn đau cho mình; Lâu Hỉ Dương đỏ mặt làm quen với việc yêu đương đồng giới.",
            "Lâu Hỉ Dương phát hiện đường ống thông khí từ phòng tắm nối thẳng lên nhà vệ sinh tầng hai.",
            "Rạng sáng trước ngày sinh nhật của Tưởng Trác Hàng, Lâu Hỉ Dương chui qua ống thông khí lên nhà vệ sinh tầng hai.",
            "Thả 3 con ruồi điện tử vô hiệu hóa camera an ninh trong 10 phút, Lâu Hỉ Dương đẩy cửa bước vào hành lang xanh lam tầng hai tìm mẹ."
        ],
        "debt_repayment_progress": "30%",
        "key_relationships": "Lâu Hỉ Dương rũ bỏ hoàn toàn hiểu lầm kiếp trước, hết lòng chiều chuộng và tiếp xúc thân mật cùng Dịch Duyên."
    }
]

timeline.extend(new_entries)

with open(path, "w", encoding="utf-8") as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print("Batch 3 timeline updated successfully!")
