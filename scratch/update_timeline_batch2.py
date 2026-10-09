# -*- coding: utf-8 -*-
import json

path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_chs = {item.get("chapter") for item in data}

batch2_events = [
    {
        "chapter": "ch_096",
        "arc": "arc_04",
        "title": "Chương 96: Nghi ngờ và thăm dò",
        "summary": "Kỷ Cảnh áp đảo các đối thủ trên sân tập thực chiến và trêu chọc Lục Tư Niên; Lục Tư Niên hỏi về em gái Kỷ Cảnh; Kỷ Cảnh giả gái Dịch Nam gửi ảnh tất đen/tất trắng và viện cớ bị ba dượng bạo hành để thăm dò Lục Tư Niên.",
        "key_events": [
            "Kỷ Cảnh thắng liên tiếp 7 trận cận chiến, Vương Bằng khen ngợi trước mặt Lục Tư Niên.",
            "Kỷ Cảnh đuổi theo Lục Tư Niên và tuyên bố: 'Lục Tư Niên, tôi muốn theo đuổi anh'.",
            "Lục Tư Niên hỏi Kỷ Cảnh có phải có một đứa em gái hay không.",
            "Kỷ Cảnh gửi ảnh chụp tất đen và váy hai dây, bịa chuyện bị ba dượng say xỉn đánh đập để kích thích Lục Tư Niên."
        ]
    },
    {
        "chapter": "ch_097",
        "arc": "arc_04",
        "title": "Chương 97: Nếu em đồng ý thì sao",
        "summary": "Kỷ Cảnh trong trang phục nữ cùng Lục Tư Niên đi chơi thủy cung vào ngày lễ tình nhân; Kỷ Cảnh hôn má Lục Tư Niên giữa đàn cá; Lục Tư Niên muốn thuê nhà riêng bảo vệ Dịch Nam và dạy chỉ huy quân sự.",
        "key_events": [
            "Kỷ Cảnh bịa chuyện bị Alpha quấy rối ngoài đường vào ngày Valentine để kéo Lục Tư Niên tới đón.",
            "Hai người cùng nhau đi tham quan thủy cung, Lục Tư Niên bộc bạch chưa từng được nhìn thấy biển lớn.",
            "Kỷ Cảnh bất ngờ hôn lên gò má Lục Tư Niên, khiến Lục Tư Niên đỏ ửng tai và ngửi thấy mùi rượu Tequila quen thuộc.",
            "Lục Tư Niên đề nghị thuê nhà riêng cho Dịch Nam ở gần trường và đích thân dạy học chỉ huy."
        ]
    },
    {
        "chapter": "ch_098",
        "arc": "arc_04",
        "title": "Chương 98: Sân đấu thực chiến rực lửa",
        "summary": "Kỷ Cảnh từ chối lời đề nghị thuê nhà vì tự ái; Hệ thống Mật Bảo trao thưởng nước phục hồi năng lượng; Giải đấu cận chiến toàn trường chào đón Quân đoàn Ba, Lục Tư Niên làm trọng tài; Kỷ Cảnh chuẩn bị đấu Lục Đảo Phong.",
        "key_events": [
            "Kỷ Cảnh từ chối sự giúp đỡ vì không muốn bị thương hại hay cảm giác như bị bao nuôi.",
            "Hệ thống Mật Bảo xuất hiện thưởng Nước phục hồi năng lượng khôi phục chỉ số thể chất Alpha của Kỷ Cảnh.",
            "Học viện Quân sự Đế quốc tổ chức giải đấu cận chiến chào đón Quân đoàn Ba, Lục Tư Niên ngồi ghế trọng tài.",
            "Vương Bằng cảnh báo Kỷ Cảnh về thủ đoạn hiểm độc của thái tử gia Lục gia - Lục Đảo Phong."
        ]
    },
    {
        "chapter": "ch_099",
        "arc": "arc_04",
        "title": "Chương 99: Cơn sốt tin tức tố bùng phát",
        "summary": "Trận chung kết cận chiến giữa Kỷ Cảnh và Lục Đảo Phong diễn ra ở bối cảnh bờ biển; Kỷ Cảnh áp đảo dìm đầu Lục Đảo Phong xuống nước trả thù cho quá khứ của Lục Tư Niên; Lục Tư Niên trên ghế trọng tài xúc động nghẹn ngào.",
        "key_events": [
            "Quân đoàn trưởng Trương Mạc và ban lãnh đạo Quân đoàn Ba trực tiếp theo dõi trận chung kết.",
            "Kỷ Cảnh áp đảo vòng phân bảng và chọn chế độ bờ biển trong trận đấu với Lục Đảo Phong.",
            "Kỷ Cảnh túm tóc dìm đầu Lục Đảo Phong xuống nước biển lặp đi lặp lại để trả đũa mối thù quá khứ cho Lục Tư Niên.",
            "Lục Tư Niên nhận ra Kỷ Cảnh đang bảo vệ mình, tim đập dữ dội và vội vàng rời khỏi ghế trọng tài."
        ]
    },
    {
        "chapter": "ch_100",
        "arc": "arc_04",
        "title": "Chương 100: Gõ cửa căn hộ áp mái",
        "summary": "Lục Tư Niên hạ gục Lâm Diên Sơn sau hậu trường rồi đè Kỷ Cảnh vào gốc cây ngửi pheromone trấn an; Lục Tư Niên phát sốt Omega phải nghỉ dạy; Kỷ Cảnh tìm tới căn hộ áp mái của Lục Tư Niên.",
        "key_events": [
            "Lục Tư Niên tung cước đá bay Lâm Diên Sơn hộc máu vì dám xúc phạm thân phận Omega.",
            "Lục Tư Niên đè Kỷ Cảnh vào thân cây ven đường để ngửi tin tức tố Tequila giúp trấn tĩnh.",
            "Kỷ Cảnh được cha là Kỷ Trình khen ngợi và bảo vệ, bất chấp việc bị tước huy chương vì đánh Lục Đảo Phong.",
            "Lục Tư Niên phát sốt xin nghỉ dạy, Kỷ Cảnh tìm ra địa chỉ nhà và đến gõ cửa căn hộ áp mái."
        ]
    },
    {
        "chapter": "ch_101",
        "arc": "arc_04",
        "title": "Chương 101: Tỉnh giấc chung giường",
        "summary": "Lục Tư Niên trong cơn phát tình mất kiểm soát hôn môi Kỷ Cảnh và ôm cậu; Kỷ Cảnh nấu canh gừng chăm sóc anh suốt mấy ngày; sáng ra Lục Tư Niên thức giấc thấy hai người chung giường bèn hoảng loạn bỏ trốn vào phòng tắm.",
        "key_events": [
            "Lục Tư Niên mở cửa trong tình trạng sốt cao, tin tức tố tuyết tùng lan tỏa nồng nặc và ôm chặt Kỷ Cảnh.",
            "Lục Tư Niên mất kiểm soát đè Kỷ Cảnh xuống giường hôn môi sâu, Kỷ Cảnh kiềm chế không đánh dấu tuyến thể.",
            "Kỷ Cảnh nấu canh gừng và ở lại chăm sóc Lục Tư Niên suốt mấy ngày sốt mê man.",
            "Sáng ra Lục Tư Niên phát hiện hai người chung giường, hoảng hốt bọc chăn cho Kỷ Cảnh rồi trốn vào nhà tắm trong sự dằn vặt tội lỗi."
        ]
    },
    {
        "chapter": "ch_102",
        "arc": "arc_04",
        "title": "Chương 102: Giúp chị gái xử lý hoa đào",
        "summary": "Lục Tư Niên áy náy muốn bù đắp chịu trách nhiệm nhưng Kỷ Cảnh giận dỗi bỏ về; Kỷ Cảnh phát hiện vỏ thuốc ức chế cấm của Lục Tư Niên từ Kỷ Vân Hy; Kỷ Vân Hy nhờ Kỷ Cảnh giả gái trị tên Alpha bám đuôi.",
        "key_events": [
            "Lục Tư Niên nấu cháo chu đáo và nói muốn bù đắp chịu trách nhiệm với Dịch Nam; Kỷ Cảnh tức giận mắng anh cổ hủ rồi bỏ về.",
            "Kỷ Cảnh mặc đồ nữ về nhà bị ba mẹ bắt gặp, mẹ Kỷ chuẩn bị sẵn thuốc ức chế Alpha cho con trai.",
            "Lục Tư Niên mất ngủ nhớ về những đêm thân mật, nhắn tin nhận tội và xin cơ hội bù đắp.",
            "Kỷ Vân Hy nhận ra ống tiêm rỗng là thuốc kháng chế Omega bất hợp pháp làm hỏng tuyến thể; Kỷ Vân Hy nhờ Kỷ Cảnh giả gái trị tên Alpha quấy rối."
        ]
    }
]

for ev in batch2_events:
    if ev["chapter"] not in existing_chs:
        data.append(ev)

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated memory/timeline.json successfully!")
