# -*- coding: utf-8 -*-
import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

timeline_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\memory\timeline.json"

with open(timeline_path, 'r', encoding='utf-8') as f:
    timeline = json.load(f)

new_entries = [
    {
        "chapter": "ch_111",
        "arc": "arc_04",
        "title": "Chương 111: Rời đi sau cơn mẫn cảm",
        "summary": "Kỷ Cảnh đau đầu rời khỏi nhà Lục Tư Niên sau khi cãi vã, từ chối nhập ngũ Đệ tam quân đoàn; Lục Tư Niên âm thầm dọn dẹp, tự phơi bày thân phận Omega trước toàn đế quốc để khởi kiện Lâm Diên Sơn nhằm bảo vệ Kỷ Cảnh; Kỷ Cảnh đi bệnh viện và bàng hoàng phát hiện Lục Tư Niên đã chủ động hiến dâng thân thể để cậu hoàn thành đánh dấu trọn đời.",
        "key_events": [
            "Kỷ Cảnh rời khỏi căn hộ của Lục Tư Niên, bực bội từ chối báo danh Đệ tam quân đoàn.",
            "Lục Tư Niên đơn độc thu dọn hành lý, công khai mình là Omega và nộp đơn khởi kiện Lâm Diên Sơn để bảo vệ Kỷ Cảnh.",
            "Lục Tư Niên nhắn Vương Bằng giục Kỷ Cảnh đi bệnh viện khám tuyến thể.",
            "Bác sĩ bệnh viện thông báo chỉ có đánh dấu trọn đời một Omega mới giải trừ được mũi tiêm kích mẫn; Kỷ Cảnh bàng hoàng nhận ra Lục Tư Niên đã chủ động hiến dâng để cậu đánh dấu trọn đời mình."
        ]
    },
    {
        "chapter": "ch_112",
        "arc": "arc_04",
        "title": "Chương 112: Cơ hội tuyển quân đợt hai",
        "summary": "Kỷ Cảnh nhận thức được sự độc chiếm trọn đời đối với Lục Tư Niên; không muốn xa cách nên đã nhờ Vương Bằng hỏi đợt tuyển quân; Lục Tư Niên bất ngờ hạ lệnh mở tuyển quân đợt hai toàn đế quốc; Kỷ Cảnh dốc toàn lực thi đỗ thủ khoa; Kỷ Cảnh từ biệt gia đình bay 2 ngày đến hoang tinh gia nhập Đệ tam quân đoàn.",
        "key_events": [
            "Kỷ Cảnh nhận thức được sự chiếm hữu trọn đời với Lục Tư Niên; không nỡ xa cách nên nhờ Vương Bằng hỏi cơ hội tuyển quân.",
            "Lục Tư Niên bất ngờ ban hành lệnh tuyển quân đợt hai trên toàn đế quốc, nâng cao tiêu chuẩn 20%.",
            "Kỷ Cảnh hừng hực khí thế thi đỗ thủ khoa; gia đình ngỡ ngàng, Kỷ Vân Hy nhìn thấu tâm can em trai.",
            "Kỷ Cảnh ngồi tinh hạm 2 ngày đến hoang tinh gia nhập Đệ tam quân đoàn."
        ]
    },
    {
        "chapter": "ch_113",
        "arc": "arc_04",
        "title": "Chương 113: Tân binh gia nhập Đệ tam quân đoàn",
        "summary": "Kỷ Cảnh đến Đệ tam quân đoàn báo danh; Lục Tư Niên giả vờ đi kiểm tra quân phục để xuống nhìn Kỷ Cảnh; Kỷ Cảnh vào Đội Một trinh sát; tên Alpha Đại Vĩ gạ đấu; Lục Tư Niên xuất hiện can thiệp, thẳng tay chỉnh thắt lưng cho Kỷ Cảnh: 'Chỉ dạy một lần này thôi'; Kỷ Vân Hy báo tin sắp tới quân đoàn bàn giao quân phục mới.",
        "key_events": [
            "Kỷ Cảnh báo danh Đệ tam quân đoàn; Lục Tư Niên vờ đi kiểm tra quân phục để xuống nhìn Kỷ Cảnh.",
            "Kỷ Cảnh gia nhập Đội Một trinh sát; tên Alpha Đại Vĩ gạ đấu; Lục Tư Niên xuất hiện ngăn chặn.",
            "Lục Tư Niên giật mạnh Kỷ Cảnh vào lòng cài lại thắt lưng quân phục: 'Chỉ dạy một lần này thôi'.",
            "Kỷ Vân Hy gọi điện báo sắp đến Đệ tam quân đoàn nộp bản thiết kế quân phục mới."
        ]
    },
    {
        "chapter": "ch_114",
        "arc": "arc_04",
        "title": "Chương 114: Thăm dò và ghen tuông",
        "summary": "Kỷ Vân Hy đến Đệ tam quân đoàn, Kỷ Cảnh trốn ra gặp bị Lục Tư Niên bắt gặp; Kỷ Vân Hy nói chuyện riêng khuyên Lục Tư Niên chủ động giải thích tình cảm với Kỷ Cảnh; Kỷ Cảnh bị phạt nhốt khoang thể lực; tối về Lục Tư Niên chủ động đến phòng ký túc xá thổ lộ rằng người anh luôn thích từ đầu đến cuối là em; hai người hôn nhau nồng cháy ngã xuống giường, Kỷ Cảnh cắn tuyến thể Lục Tư Niên và yêu cầu anh theo đuổi mình.",
        "key_events": [
            "Kỷ Vân Hy đến Đệ tam quân đoàn, Kỷ Cảnh lén gặp bị Lục Tư Niên bắt quả tang.",
            "Kỷ Vân Hy nói chuyện riêng khuyên Lục Tư Niên chủ động tháo gỡ hiểu lầm với Kỷ Cảnh.",
            "Lục Tư Niên đến phòng ký túc xá thổ lộ: 'Người tôi luôn thích từ đầu đến cuối là em, không phải Dịch Nam'.",
            "Hai người hôn nhau cuồng nhiệt ngã xuống giường; Kỷ Cảnh cắn tuyến thể Lục Tư Niên và bắt anh phải theo đuổi mình."
        ]
    },
    {
        "chapter": "ch_115",
        "arc": "arc_04",
        "title": "Chương 115: Gián cách ngàn dặm và hoa hồng",
        "summary": "Tiến độ nhiệm vụ hệ thống đạt 91%; Kỷ Cảnh tham gia huấn luyện bắn súng laser mô phỏng, được Lục Tư Niên từ sau lưng cầm tay chỉ dẫn bắn trúng hồng tâm 10 điểm tuyệt đối; bữa trưa Lục Tư Niên chủ động đi lấy cơm cho Kỷ Cảnh; Lục Tư Niên tặng bó hoa hồng to tướng; buổi tối Lục Tư Niên ngượng ngùng gửi ảnh cơ bụng cho Kỷ Cảnh theo yêu cầu.",
        "key_events": [
            "Tiến độ nhiệm vụ hệ thống đạt 91%.",
            "Huấn luyện súng laser mô phỏng, Lục Tư Niên từ sau lưng cầm tay Kỷ Cảnh chỉ dẫn bắn trúng hồng tâm 10 điểm tuyệt đối.",
            "Bữa trưa Lục Tư Niên lấy cơm cho Kỷ Cảnh; Lục Tư Niên tặng bó hoa hồng đỏ to tướng.",
            "Buổi tối Lục Tư Niên ngượng ngùng chụp ảnh ngậm vạt áo ngủ khoe cơ bụng 8 múi gửi cho Kỷ Cảnh."
        ]
    },
    {
        "chapter": "ch_116",
        "arc": "arc_04",
        "title": "Chương 116: Khắc ghi dấu ấn trọn đời",
        "summary": "Kỷ Cảnh bùng nổ sức mạnh trong kỳ kiểm tra cách đấu đạt 9.364.719 điểm, phá kỷ lục của Lục Tư Niên trở thành No.1 đế quốc; Kỷ Cảnh bí mật xăm tên Lục Tư Niên bằng chữ Lam Tinh cổ vào gốc đùi; Lục Tư Niên mặc tây trang mang hoa hồng hẹn Kỷ Cảnh ngắm dải ngân hà ở biên giới, giãi bày tâm tư sâu kín không thể sống thiếu Kỷ Cảnh; Lục Tư Niên cài hoa hồng lên tai Kỷ Cảnh và thổ lộ 'Tôi yêu em'.",
        "key_events": [
            "Kỷ Cảnh bùng nổ sức mạnh trong kỳ kiểm tra cách đấu đạt 9.364.719 điểm, phá kỷ lục của Lục Tư Niên trở thành No.1 đế quốc.",
            "Kỷ Cảnh xăm tên Lục Tư Niên bằng chữ Lam Tinh cổ vào gốc đùi để khắc ghi dấu ấn trọn đời.",
            "Lục Tư Niên mặc tây trang mang hoa hồng hẹn Kỷ Cảnh ngắm dải ngân hà ở biên giới, giãi bày tâm tư không thể sống thiếu Kỷ Cảnh.",
            "Lục Tư Niên cài hoa hồng lên tai Kỷ Cảnh và thổ lộ: 'Tôi yêu em, Kỷ Cảnh'."
        ]
    },
    {
        "chapter": "ch_117",
        "arc": "arc_04",
        "title": "Chương 117: Lời cầu hôn và chiếc nhẫn kim cương",
        "summary": "Lục Tư Niên trao chiếc vòng ngọc gia truyền của mẹ cho Kỷ Cảnh; Kỷ Cảnh ghen khi thấy nữ Alpha Thư Nghiên đi cùng Lục Tư Niên; Kỷ Cảnh mặc váy trắng tóc dài ngồi co ro trước cửa phòng Lục Tư Niên gọi 'Ông xã, anh đã về rồi sao', khiến Thư Nghiên rớt cằm; Kỷ Cảnh khoe hình xăm tên anh ở gốc đùi; hai người ân ái nồng nhiệt; sáng hôm sau Lục Tư Niên quỳ bên giường đeo nhẫn kim cương cầu hôn Kỷ Cảnh.",
        "key_events": [
            "Lục Tư Niên trao chiếc vòng ngọc gia truyền của mẹ cho Kỷ Cảnh; Kỷ Cảnh giãi bày sự thật chân thành.",
            "Kỷ Cảnh ghen khi thấy nữ Alpha Thư Nghiên đi cùng Lục Tư Niên.",
            "Kỷ Cảnh mặc váy trắng tóc dài ngồi trước cửa phòng Lục Tư Niên gọi 'Ông xã, anh đã về rồi sao', khiến Thư Nghiên rớt cằm.",
            "Kỷ Cảnh khoe hình xăm tên anh ở gốc đùi; hai người ân ái nồng nhiệt.",
            "Sáng hôm sau Lục Tư Niên quỳ bên giường đeo nhẫn kim cương cầu hôn Kỷ Cảnh; Kỷ Cảnh mỉm cười đồng ý."
        ]
    },
    {
        "chapter": "ch_118",
        "arc": "arc_04",
        "title": "Chương 118: Đồng phục thỏ nữ lang và Đại kết cục",
        "summary": "Hệ thống thông báo hoàn thành 100% nhiệm vụ toàn văn; Kỷ Cảnh và Lục Tư Niên đăng ký kết hôn, tiệc đính hôn có cả Nguyên soái tham dự; hai người lật đổ hoàn toàn Lục gia; Kỷ Cảnh tiếp quản Kỷ gia, Lục Tư Niên trở thành tân Nguyên soái đế quốc; khám vô sinh do thuốc ức chế cũ; Mật Bảo trao viên thuốc sinh con đặc biệt; Kỷ Cảnh mặc đồng phục thỏ nữ lang trêu ghẹo; đêm ngọt ngào mặn nồng; ĐẠI KẾT CỤC HOÀN TOÀN VIÊN MÃN (HE).",
        "key_events": [
            "Hệ thống thông báo hoàn thành 100% nhiệm vụ toàn văn; Mật Bảo tạm biệt về học giai đoạn hai.",
            "Kỷ Cảnh và Lục Tư Niên đăng ký kết hôn, tiệc đính hôn chấn động đế quốc có cả Nguyên soái chúc phúc; Lục gia sụp đổ hoàn toàn.",
            "Kỷ Cảnh tiếp quản Kỷ gia, Lục Tư Niên trở thành tân Nguyên soái đế quốc; bố mẹ giục sinh con nhưng phát hiện Lục Tư Niên vô sinh do thuốc ức chế cũ.",
            "Mật Bảo trở lại trao viên thuốc sinh con đặc biệt.",
            "Kỷ Cảnh mặc đồng phục thỏ nữ lang quyến rũ Lục Tư Niên; đêm ngọt ngào mặn nồng; ĐẠI KẾT CỤC HOÀN TOÀN VIÊN MÃN (HE)."
        ]
    }
]

# Avoid duplicates
existing_ch_ids = {item.get('chapter') for item in timeline}
for entry in new_entries:
    if entry['chapter'] not in existing_ch_ids:
        timeline.append(entry)
        print(f"Appended {entry['chapter']} to timeline.")
    else:
        print(f"{entry['chapter']} already in timeline, skipping.")

with open(timeline_path, 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

print("Updated timeline.json successfully!")
