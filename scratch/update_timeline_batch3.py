# -*- coding: utf-8 -*-
import json

path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_chs = {item.get("chapter") for item in data}

batch3_events = [
    {
        "chapter": "ch_103",
        "arc": "arc_04",
        "title": "Chương 103: Trừng trị Alpha theo đuổi",
        "summary": "Kỷ Cảnh giả gái Dịch Nam đi gặp tên Alpha bám đuôi Minh Vũ để giúp Kỷ Vân Hy; Lục Tư Niên ghen tuông chạy tới đánh bay Minh Vũ, kéo Kỷ Cảnh ra xe hôn sâu và mang 4 sổ đỏ cùng bản thỏa thuận tiền hôn nhân ra cầu hôn Dịch Nam.",
        "key_events": [
            "Kỷ Cảnh cải trang thành Dịch Nam giúp chị gái Kỷ Vân Hy dạy dỗ tên Alpha Minh Vũ tại hộp đêm.",
            "Lục Tư Niên phát hiện story định vị, ghen tuông lao tới quật ngã Minh Vũ.",
            "Kỷ Cảnh ép Minh Vũ uống trọn ly rượu bị hạ thuốc.",
            "Lục Tư Niên kéo Kỷ Cảnh ra xe hôn cuồng nhiệt, trưng ra tài sản và thỏa thuận tiền hôn nhân để cầu hôn Dịch Nam."
        ]
    },
    {
        "chapter": "ch_104",
        "arc": "arc_04",
        "title": "Chương 104: Lịch sử phân hóa và lời thổ lộ",
        "summary": "Lục Tư Niên kể lại bi kịch của mẹ mình và nỗi dằn vặt muốn chịu trách nhiệm sau khi ngỡ rằng đã ngủ với Dịch Nam; Kỷ Cảnh giải thích chỉ dùng tay/đùi giúp đỡ; hai người xác nhận quan hệ hẹn hò; Kỷ Cảnh băn khoăn về lời nói dối.",
        "key_events": [
            "Lục Tư Niên bộc bạch về mẹ là một Beta hiền từ bị Alpha nhà họ Lục ruồng bỏ và qua đời trong oan ức.",
            "Lục Tư Niên xấu hổ thú nhận tưởng đã ngủ với Dịch Nam; Kỷ Cảnh bật cười giải thích chưa đến bước cuối cùng.",
            "Hai người chính thức xác nhận quan hệ hẹn hò: 'Tạm biệt nhé, bạn trai'.",
            "Tiến độ nhiệm vụ tăng lên 63%; Kỷ Cảnh trăn trở vì lừa dối người thực lòng yêu mình."
        ]
    },
    {
        "chapter": "ch_105",
        "arc": "arc_04",
        "title": "Chương 105: Bữa tiệc nguyên soái và ghen tuông",
        "summary": "Kỷ Cảnh ghen tị với chính thân phận Dịch Nam của mình; cả nhà Kỷ Cảnh dự tiệc sinh nhật Nguyên soái; Kỷ Cảnh đe dọa ném Lục Đảo Phong vào thùng rác trả thù cho Lục Tư Niên; Trương Mạc báo tin sắp có dự luật bỏ phiếu cho Omega tòng quân.",
        "key_events": [
            "Kỷ Cảnh ghen tị với thân phận Dịch Nam khi Lục Tư Niên khẳng định chỉ thích Dịch Nam.",
            "Gia đình Kỷ Cảnh dự đại thọ 50 tuổi của Nguyên soái; Nguyên soái khen ngợi chỉ coi trọng Kỷ Cảnh và Lục Tư Niên.",
            "Kỷ Cảnh đè bẹp sự khiêu khích của đám Alpha và đe dọa Lục Đảo Phong trả thù cho Lục Tư Niên.",
            "Trương Mạc báo cho Lục Tư Niên biết về dự luật bỏ phiếu khôi phục quyền tòng quân cho Omega."
        ]
    },
    {
        "chapter": "ch_106",
        "arc": "arc_04",
        "title": "Chương 106: Phòng nghỉ say rượu",
        "summary": "Lục Tư Niên say rượu nhắn tin cho Dịch Nam; Kỷ Cảnh ra hoa viên gặp anh; Lục Tư Niên bộc bạch ngưỡng mộ Kỷ Cảnh ngày xưa nhưng xin đừng lừa dối mình; Kỷ Cảnh bực bội vì bị gọi là Dịch Nam bèn hôn môi Lục Tư Niên và bị Kỷ Vân Hy bắt quả tang.",
        "key_events": [
            "Lục Đảo Phong xỏ xiên tại bàn tiệc bị Nguyên soái quát nạt răn đe.",
            "Lục Tư Niên uống say nhắn tin: 'Hình như tôi say rồi'; Kỷ Cảnh đi theo ra hoa viên.",
            "Lục Tư Niên say mèm kể lại sự việc 6 năm trước và tha thiết xin đối phương đừng lừa dối mình.",
            "Kỷ Cảnh hỏi 'Tôi là ai?', Lục Tư Niên đáp 'Dịch Nam'; Kỷ Cảnh tức giận hôn môi anh và bị Kỷ Vân Hy bắt gặp."
        ]
    },
    {
        "chapter": "ch_107",
        "arc": "arc_04",
        "title": "Chương 107: Mềm lòng và làm lành",
        "summary": "Kỷ Cảnh đưa Lục Tư Niên về căn hộ; Lục Tư Niên say rượu ôm hôn vật lộn; Kỷ Cảnh ép Lục Tư Niên dâng hiến tuyến thể nhưng dừng lại kịp thời; Kỷ Cảnh thú nhận sự thật giả gái với Kỷ Vân Hy.",
        "key_events": [
            "Kỷ Cảnh dìu Lục Tư Niên về căn hộ áp mái; hai người vật lộn lăn xuống sàn nhà.",
            "Kỷ Cảnh phóng tin tức tố Alpha áp chế và đòi cắn tuyến thể; Lục Tư Niên ngoan ngoãn dán trán xuống sàn để lộ tuyến thể cho cậu cắn.",
            "Kỷ Cảnh bàng hoàng nhận ra tình cảm của Lục Tư Niên nên dừng lại không cắn.",
            "Kỷ Cảnh về nhà thú nhận sự thật giả gái Dịch Nam với chị gái Kỷ Vân Hy."
        ]
    },
    {
        "chapter": "ch_108",
        "arc": "arc_04",
        "title": "Chương 108: Quyết định trở lại quân đoàn",
        "summary": "Khoảng cách giữa hai người thay đổi vì sự dằn vặt; Kỷ Cảnh cầu xin cha Kỷ bỏ phiếu thuận cho đề xuất Omega tòng quân; Kỷ gia dẫn đầu bỏ phiếu thuận giúp đề xuất thông qua ngoạn mục; Lục Tư Niên nhận ra Kỷ Cảnh đứng sau giúp đỡ.",
        "key_events": [
            "Kỷ Cảnh nhắn tin làm lành với Lục Tư Niên; hai người tiếp tục duy trì tương tác tại trường.",
            "Kỷ Cảnh biết tin về cuộc bỏ phiếu quyền tòng quân của Omega đang có nguy cơ thất bại.",
            "Kỷ Cảnh vào thư phòng cầu xin cha là Kỷ Trình bỏ phiếu thuận để giúp Lục Tư Niên.",
            "Kỷ gia dẫn đầu bỏ phiếu thuận, kéo theo Vương gia và Nguyên soái, giúp đề xuất thông qua thành công; Lục Tư Niên xúc động đoán ra Kỷ Cảnh đứng sau giúp mình."
        ]
    },
    {
        "chapter": "ch_109",
        "arc": "arc_04",
        "title": "Chương 109: Kỳ nhạy cảm bùng phát",
        "summary": "Kỷ Cảnh chấp nhận điều kiện thừa kế Kỷ gia sau 5 năm; tiến độ đạt 80% giải trói buộc hệ thống; Kỷ Cảnh nhắn tin chia tay và xóa tài khoản Dịch Nam; Lâm Diên Sơn phát điên tới ám hại Lục Tư Niên, Kỷ Cảnh xông tới đỡ đòn và bị tiêm thuốc kích thích bùng phát kỳ nhạy cảm.",
        "key_events": [
            "Tiến độ nhiệm vụ đột ngột cán mốc 80%, giải trói buộc hệ thống thành công.",
            "Kỷ Cảnh quyết định dứt áo ra đi, gửi tin nhắn chia tay tàn nhẫn và xóa sổ tài khoản Dịch Nam.",
            "Lâm Diên Sơn phát điên tìm tới nhà Lục Tư Niên định cưỡng ép nhục mạ anh trước khi anh trở lại quân đoàn.",
            "Kỷ Cảnh đạp cửa xông vào ứng cứu, lao mình đỡ mũi tiêm thuốc tăng mẫn cảm tin tức tố cho Lục Tư Niên."
        ]
    },
    {
        "chapter": "ch_110",
        "arc": "arc_04",
        "title": "Chương 110: Lần đánh dấu đầu tiên",
        "summary": "Kỳ nhạy cảm đầu tiên của Kỷ Cảnh bùng phát cuồng bạo; Lục Tư Niên chấp nhận dâng hiến tuyến thể để cứu Kỷ Cảnh khỏi nguy cơ phế bỏ; sáng hôm sau Kỷ Cảnh vô thức kẹp giọng nữ khiến thân phận Dịch Nam bại lộ hoàn toàn; hai người xảy ra cãi vã đau lòng.",
        "key_events": [
            "Kỳ nhạy cảm đầu tiên của Kỷ Cảnh bùng phát mất kiểm soát, hương rượu Tequila áp đảo hoàn toàn.",
            "Lục Tư Niên gọi điện hỏi bác sĩ Nguyễn Uyên và chấp nhận để Kỷ Cảnh cắn ngập răng nanh đánh dấu tuyến thể.",
            "Sáng hôm sau tỉnh dậy, Kỷ Cảnh vô thức dùng giọng nữ của Dịch Nam khiến thân phận giả bị vạch trần tại trận.",
            "Kỷ Cảnh hoảng sợ buông lời tàn nhẫn tự vệ, Lục Tư Niên quát ngăn lại; Kỷ Cảnh nói xin lỗi rồi bỏ chạy."
        ]
    }
]

for ev in batch3_events:
    if ev["chapter"] not in existing_chs:
        data.append(ev)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated memory/timeline.json successfully with Batch 3 events!")
