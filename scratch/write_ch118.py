# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_118\translation.md"

paras = [
    # 000
    "【Đinh đoong, chúc mừng ký chủ hoàn thành một trăm phần trăm tiến độ nhiệm vụ!】",
    # 001
    "【Phần thưởng nhiệm vụ đang được phát ra, xin ký chủ kiên nhẫn chờ đợi.】",
    # 002
    "【Em đã hoàn thành toàn bộ nhiệm vụ của giai đoạn này rồi, ba ba ma ma gọi em về để tiếp tục tu nghiệp giai đoạn hai, ký chủ ơi, hẹn gặp lại ngài sau nhé~】",
    # 003
    "...",
    # 004
    "Kỷ Cảnh và Lục Tư Niên đã đi đăng ký kết hôn.",
    # 005
    "Lúc Kỷ Cảnh nói chuyện này với ba mẹ Kỷ, hai vị phụ huynh suýt chút nữa thì bị nghẹn họng vì đồ ăn.",
    # 006
    "Không phải là vì phản đối, hai bậc phụ huynh đều vô cùng ưu ái xem trọng Lục Tư Niên, huống chi Lục Tư Niên còn là một Omega, chỉ là không thể tin nổi con trai mình vậy mà lại có thể kết hôn với Lục Tư Niên.",
    # 007
    "Trước khoảnh khắc hỷ sự kết hôn được công bố rộng rãi trước toàn thể đế quốc, mẹ cậu vẫn còn nắm chặt lấy tay cậu hết lần này đến lần khác gặng hỏi cậu người đó thật sự là Lục Tư Niên sao, chính là Lục Tư Niên đó ư?",
    # 008
    "Không chỉ riêng mẹ Kỷ, ngay cả Vương Bằng, Chu Độ, cùng tất cả những người quen biết cậu và Lục Tư Niên đều điên cuồng oanh tạc thiết bị đầu cuối của cậu và Lục Tư Niên——",
    # 009
    "Cái gì cơ? Lục Tư Niên và Kỷ Cảnh kết hôn với nhau rồi á?",
    # 010
    "Lục Tư Niên chẳng phải có một cô bạn gái rồi sao?",
    # 011
    "Cái gì, cô bạn gái đó chính là Kỷ Cảnh á?",
    # 012
    "Những câu hỏi tương tự như thế này nhiều vô số kể, đặc biệt là Vương Bằng và Chu Độ, khóc lóc om sòm tự kiểm điểm lại sự ngu ngốc của bản thân, giải thích đến cuối cùng Kỷ Cảnh đã thấy phiền phức quá rồi, dứt khoát tắt luôn thiết bị đầu cuối đi tìm Lục Tư Niên.",
    # 013
    "Ngày đính hôn, ngoại trừ người của Lục gia ra, về cơ bản toàn bộ giới quyền quý hiển hách đều có mặt đông đủ, thậm chí ngay cả Nguyên soái cũng đích thân tới dự, tươi cười gửi gắm lời chúc phúc cho hai hậu bối mà ông xem trọng nhất.",
    # 014
    "Cuộc hôn nhân của Lục Tư Niên và Kỷ Cảnh tạo nên sức ảnh hưởng nặng nề nhất chính là đối với Lục gia.",
    # 015
    "Điều này đồng nghĩa với việc các phe phái lập trường phải chia lại bài từ đầu, trước đây một mình Lục Tư Niên đối đầu với Lục gia hoàn toàn là châu chấu đá xe, mà giờ đây sau lưng Lục Tư Niên là cả một Kỷ gia hùng mạnh chống đỡ.",
    # 016
    "Thời gian thấm thoát thoi đưa, chớp mắt một cái Kỷ Cảnh đã cùng Lục Tư Niên tham gia hai chiến dịch tinh tế quy mô lớn, vinh dự nhận được chiến công quân sự đặc đẳng rồi lựa chọn xuất ngũ trong vinh quang, trong khi Lục Tư Niên dựa vào những chiến công quân sự hiển hách liên tiếp không ngừng thăng tiến, trở thành Trung tướng trẻ tuổi nhất đế quốc.",
    # 017
    "Kỷ Cảnh thực hiện đúng lời ước hẹn với ba Kỷ, bắt đầu tiếp quản cơ nghiệp của Kỷ gia, trong lúc cậu dần dần quen tay vững vàng, quán xuyến Kỷ gia đâu ra đấy đâu vào đấy, đồng thời cố tình chèn ép Lục gia khiến bọn họ nếm mùi thất bại tứ bề, thì Lục Tư Niên lại tiếp tục chinh chiến bên ngoài thêm vài năm nữa, cuối cùng được Nguyên soái đích thân bổ nhiệm làm người kế thừa, trở thành tân Nguyên soái tiếp theo của đế quốc.",
    # 018
    "Kể từ khoảnh khắc Lục Tư Niên được bổ nhiệm làm Nguyên soái đế quốc, cũng đồng nghĩa với việc Lục gia hoàn toàn sụp đổ bại vong.",
    # 019
    "Các thế gia vọng tộc và quân đội xưa nay luôn dựa dẫm nương tựa lẫn nhau, Lục gia dưới sự thao túng có chủ đích của Lục Tư Niên đã bị gạt phăng ra khỏi guồng quay, chỉ trong vòng một năm ngắn ngủi đã hoàn toàn tan rã tan hoang.",
    # 020
    "Ngày hôm đó Kỷ Cảnh cùng Lục Tư Niên trở về Lục gia, tận mắt chứng kiến Lục Tư Niên dùng từng nắm đấm trả lại sòng phẳng không thiếu một chút nào những nỗi sỉ nhục mà năm xưa bản thân từng phải chịu đựng.",
    # 021
    "Kỳ hạn ước định giữa Kỷ Cảnh và ba Kỷ cũng đã đến ngày đáo hạn, Lục Tư Niên hỏi cậu có muốn trở lại quân đoàn hay không, Kỷ Cảnh liền từ chối, cậu thực sự không ưa nổi những quy chế kỷ luật gò bó trong quân đoàn, cậu cảm thấy tình trạng hiện tại cũng khá ổn thỏa, định bụng trước mắt cứ quản lý Kỷ gia đã, sau này nếu thấy chán ngán thì sẽ đi làm một tên hải tặc không gian.",
    # 022
    "“Em làm hải tặc không gian, tôi không nỡ bắt em đâu.” Lục Tư Niên vô cùng nghiêm túc nói với cậu.",
    # 023
    "“Vậy thì em sẽ làm hải tặc không gian của riêng đế quốc, tới lúc đó anh ngứa mắt tinh cầu nào thì em sẽ đi cướp tinh cầu đó.” Kỷ Cảnh mỉm cười trêu chọc.",
    # 024
    "Thế nhưng người đầu tiên cản trở giấc mộng hải tặc không gian của Kỷ Cảnh lại chính là ba mẹ Kỷ, mẹ Kỷ ngày ngày túm lấy cậu hỏi tại sao cậu và Lục Tư Niên bao nhiêu năm nay vẫn chưa có con cái, bảo rằng nếu cậu có thể sinh ra một đứa bé, thì hai người họ sẽ tùy ý để mặc Kỷ Cảnh muốn quậy phá thế nào cũng được.",
    # 025
    "Thế là Kỷ Cảnh và Lục Tư Niên bất đắc dĩ bị ép phải đến bệnh viện làm kiểm tra tổng thể, phát hiện vấn đề xuất phát từ phía Lục Tư Niên.",
    # 026
    "Lục Tư Niên do thời kỳ đầu tiêm quá liều lượng thuốc ức chế cấm trong thời gian dài, dẫn đến tuyến thể Omega bị rối loạn chức năng sinh sản, cả đời này đều không thể thụ thai sinh nở được nữa.",
    # 027
    "“Hừ, hóa ra phần thưởng nhiệm vụ mà mày nói chính là cái thứ này đấy à.”",
    # 028
    "Kỷ Cảnh cầm viên thuốc trên tay, đưa lên trước ánh mặt trời cẩn thận ngắm nghía.",
    # 029
    "Mật Bảo sau khi hoàn thành tất cả nhiệm vụ vốn dĩ đã trở về thế giới của mình, bắt đầu theo học các khóa huấn luyện hệ thống giai đoạn hai, đang học dở giữa chừng thì bị ký chủ đánh thức.",
    # 030
    "【Đúng rồi ạ, phần thưởng nhiệm vụ tối hậu phải đến đúng thời điểm mới có thể mở khóa, viên thuốc này có thể giúp nhân vật chính mang thai em bé đấy nha~】",
    # 031
    "Mật Bảo đã nhiều năm rồi không trở lại thế giới nhiệm vụ, phấn khích quay mòng mòng tại chỗ.",
    # 032
    "“Để sau tính tiếp, có con hay không đối với tôi cũng chẳng quan trọng.” Kỷ Cảnh tiện tay nhét viên thuốc vào trong túi áo.",
    # 033
    "Về đến nhà vừa vặn lúc Lục Tư Niên từ quân đoàn trở về, trên bộ quân phục sĩ quan đeo kín các loại huân chương chiến công, bao năm chinh chiến nơi sa trường khiến khí chất của Lục Tư Niên càng thêm trầm ổn chững chạc, Kỷ Cảnh nhìn mà cảm thấy cổ họng có chút khô nóng rạo rực.",
    # 034
    "Kỷ Cảnh bước tới hôn anh một cái: “Chị gái em mang về cho em một bộ đồng phục thỏ nữ lang đấy, anh có thích không?”",
    # 035
    "Vành tai Lục Tư Niên khẽ ửng đỏ: “Ừm, em mặc thì tôi đều thích.”",
    # 036
    "Buổi tối Kỷ Cảnh liền thay bộ đồng phục thỏ nữ lang kia, lúc tình cảm sâu đậm triền miên, Lục Tư Niên vươn tay luồn những lọn tóc dài của cậu vào lòng bàn tay, khẽ khàng vuốt ve.",
    # 037
    "“Lục Tư Niên, anh có muốn có con không?”",
    # 038
    "Kỷ Cảnh đè người lên anh hỏi nhỏ.",
    # 039
    "“Tôi yêu em, Kỷ Cảnh.” Lục Tư Niên giữ chặt lấy sau gáy cậu mà hôn môi, giọng nói khàn đặc run rẩy, “Xin lỗi em, cho dù tôi không thể sinh con, tôi cũng không thể nào chấp nhận việc em rời xa tôi.”",
    # 040
    "“Nghĩ linh tinh cái gì thế hả Lục nguyên soái của em,” Kỷ Cảnh móc viên thuốc trong túi áo ra, một bàn tay vuốt ve một cái trên những múi cơ bụng săn chắc của Lục Tư Niên, tò mò chớp chớp mắt nói: “Uống cái này vào anh có thể sinh con đấy, có muốn thử một chút không?”",
    # 041
    "...",
    # 042
    "Lời tác giả:",
    # 043
    "Tác phẩm đến đây là chính thức hoàn kết rồi, cảm ơn các bảo bối đã ủng hộ suốt thời gian qua nhé!",
    # 044
    "Xin đánh giá tốt khi hoàn truyện nè he he (đầu chó ngậm hoa)"
]

content = "---\ntitle: Chương 118: Đồng phục thỏ nữ lang và Đại kết cục\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
