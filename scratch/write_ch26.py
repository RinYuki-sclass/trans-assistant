import re
import os

paras_trans = [
"""---
title: Chương 26: Trang 26
---""",
"""Trong ký túc xá có đồng đội trêu chọc cậu: “Minh Lãng, mấy trận trước đâu thấy mày coi trọng dữ vậy, sao thế, ngày mai có bạn gái đến xem à?”""",
"""Giang Minh Lãng bị chọc trúng tâm sự, trèo tót lên giường trốn tránh sự gặng hỏi của đồng đội, rút điện thoại ra gửi tin nhắn cho Phó Vân Xuyên.""",
"""Cậu nhận ra mình đã rất lâu rồi không được gặp Phó Vân Xuyên, không ai biết cậu mong chờ ngày mai đến nhường nào.""",
"""Giang Minh Lãng: Phó tiên sinh, tôi mang áo số mười bốn, chơi ở vị trí tiền đạo phụ.""",
"""Sau khi tin nhắn được gửi đi, Phó Vân Xuyên vẫn không trả lời ngay như thường lệ, Giang Minh Lãng đợi mãi rồi thiếp đi lúc nào không hay.""",
"""Nhưng sáng hôm sau khi thức dậy, cậu vẫn chưa nhận được tin nhắn hồi đáp của Phó Vân Xuyên.""",
"""Giang Minh Lãng ôm tia hy vọng le lói nghĩ bụng, có lẽ chỉ là Phó Vân Xuyên quên trả lời tin nhắn thôi.""",
"""-""",
"""Tầng cao nhất của tập đoàn Vân Xuyên, phòng làm việc của chủ tịch""",
"""“Phó tổng, người phụ trách dự án bất động sản nước C mà tập đoàn ta theo đuổi bấy lâu tối nay đang ở thành phố A, muốn hẹn gặp ngài một lát.” Trợ lý Trần nhìn Phó Vân Xuyên đang nhắm mắt tựa vào ghế sofa nghỉ ngơi, cẩn thận từng li từng tí cất lời.""",
"""Dưới ánh sáng lờ mờ, quầng thâm dưới mắt Phó Vân Xuyên cũng khó lòng che giấu nổi, anh bật cười châm biếm: “Đàm phán đổ bể với kẻ khác rồi mới nhớ tới tôi.”""",
"""Anh đặt mu bàn tay lên trán, nói: “Bảo ông ta cút đi, tối nay hủy hết toàn bộ lịch trình.”""",
"""“Ngài chắc chắn chứ ạ?” Trợ lý ngập ngừng: “Dự án này ngài đã mất gần một năm trời để thương thảo, một khi ký kết thành công sẽ đem lại lợi nhuận khó lòng đong đếm cho tập đoàn.”""",
"""“Người phụ trách bên đó nói rồi, chỉ cần tối nay ngài nể mặt ông ta, ông ta tuyệt đối sẽ không để ngài thất vọng.” Trợ lý bổ sung thêm.""",
"""“Tặc.” Phó Vân Xuyên phát ra một tiếng thở dài bực dọc: “Bảo ông ta đổi sang hôm khác.”""",
"""“E là không được đâu ạ, sáng sớm mai ông ta phải lên đường bay về nước C rồi.” Trợ lý ngẫm nghĩ, dè dặt thăm dò: “Ông ta hẹn lúc sáu giờ tối, nếu nhanh thì ngài vẫn còn kịp đến xem trận đấu của Giang tiên sinh.”""",
"""Phó Vân Xuyên chậm rãi mở mắt, nhìn về phía trợ lý Trần: “Cậu đi sắp xếp đi.”""",
"""-""",
"""Một tiếng trước khi trận đấu bắt đầu, Giang Minh Lãng đã thay xong đồng phục thi đấu trong phòng thay đồ.""",
"""Trước khi đóng cửa tủ lại, cậu lại lấy điện thoại ra xem, Phó Vân Xuyên vẫn chưa trả lời tin nhắn của cậu.""",
"""Cậu ngẫm nghĩ, lại gửi thêm một tin nhắn qua: Phó tiên sinh, hôm nay anh có đến không?""",
"""“Giang Minh Lãng, huấn luyện viên gọi mày kìa, nhanh cái chân lên!”""",
"""Đồng đội ngoài cửa thúc giục, Giang Minh Lãng ném điện thoại vào tủ đồ rồi quay người chạy ra ngoài.""",
"""Thời gian từng phút từng giây trôi qua, Giang Minh Lãng đã khởi động xong xuôi đứng chờ ở khu vực chờ sân, đồng hồ trên sân thi đấu hiển thị chỉ còn một phút nữa là đến bảy giờ tối.""",
"""Nhà thi đấu thể dục thể thao của thành phố A là nơi lớn nhất cả nước, lúc này trên khán đài không còn một chỗ trống, phóng tầm mắt ra xa toàn là người với người chen chúc nhau đông nghịt.""",
"""Cậu nhìn về phía hàng ghế người nhà lần cuối, đúng như dự đoán, không thấy bóng dáng Phó Vân Xuyên đâu cả.""",
"""Lần này cậu chẳng còn cách nào để tự lừa dối bản thân nữa, cậu thầm nghĩ, nếu không đến được thì việc gì phải nhận lời cậu chứ.""",
"""Tiếng còi vang lên, trận đấu chính thức bắt đầu.""",
"""“Giang Minh Lãng, đừng có ngẩn ngơ nữa, đẩy trạng thái lên cao nhất cho thầy!” Huấn luyện viên gào to, vỗ tay bôm bốp: “Đi, ra sân!”""",
"""···""",
"""“Phó tiên sinh, bên kia bảo là tạm thời xảy ra chút sơ suất nhỏ, hiện tại đang lập tức chạy đến đây rồi, mười phút nữa là tới.”""",
"""Trợ lý Trần cầm điện thoại, mồ hôi hột từng giọt từng giọt lăn dài trên trán: “Chỉ là một trận đấu bóng thôi mà, Giang tiên sinh sẽ hiểu cho ngài thôi.”""",
"""Phó Vân Xuyên cụp mắt nhìn thời gian, vừa vặn đúng bảy giờ.""",
"""Kim đồng hồ trên cổ tay từng giây từng giây chuyển động, nét mặt mong chờ của Giang Minh Lãng hết lần này đến lần khác xẹt qua trong tâm trí anh.""",
"""Từ đây lái xe đến nhà thi đấu mất bốn mươi tám phút đi đường.""",
"""Một trận bóng rổ diễn ra trong bao lâu? Thật trùng hợp, cũng đúng bốn mươi tám phút.""",
"""Phó Vân Xuyên nhắm mắt lại: “Không cần đến nữa,” Anh đứng phắt dậy: “Bảo ông ta ôm cái dự án chó má của mình cút khỏi thành phố A.”""",
"""Trợ lý Trần ngơ ngác cầm ống nghe điện thoại vẫn chưa kịp cúp máy, trơ mắt nhìn Phó Vân Xuyên sải bước rời khỏi tầm mắt.""",
"""Lên xe, nổ máy, đạp ga, Phó Vân Xuyên không cho bản thân nửa giây để thở, chiếc xe lao vút như tên bắn trên đường lớn, phát ra những tiếng gầm rú trầm đục.""",
"""Quãng đường bốn mươi tám phút bị anh ép cụt ngủn chỉ còn hơn ba mươi phút, khi anh chạy vào nhà thi đấu bóng rổ, toàn sân im ắng đến mức chỉ còn lại tiếng thở dốc dồn dập của anh.""",
"""Anh nhìn xuống dưới sân, chỉ thấy Giang Minh Lãng đang mặc bộ đồng phục thi đấu số mười bốn đứng ngoài vạch ba điểm, đôi mắt nâu nhìn chằm chằm vào bảng rổ đối phương, mồ hôi từ trán lăn xuống nhỏ giọt bên chân, giây tiếp theo, gập gối, bật nhảy, quả bóng rổ vẽ nên một đường parabol hoàn mỹ thoát khỏi lòng bàn tay, bay lên giữa không trung, rơi chuẩn xác vào trong rổ.""",
"""Bóng lọt lưới, còi mãn cuộc vang lên, cú ném ba điểm đè còi hoàn hảo đến không tì vết.""",
"""Trong khoảnh khắc, tiếng hò reo vang dội long trời lở đất, Giang Minh Lãng bị các đồng đội ùa tới vây chặt lấy, một đám thanh niên phát ra những tiếng gầm rú kích động tột cùng.""",
"""Phó Vân Xuyên nhìn Giang Minh Lãng toét miệng cười ngây ngô để lộ hàm răng trắng bóng, khóe môi anh cũng bất giác khẽ nhếch lên.""",
"""Bất chợt, nụ cười của anh khựng lại, anh giơ tay lên đặt trước lồng ngực mình, ánh mắt nhìn Giang Minh Lãng bỗng chốc dâng trào những đợt sóng ngầm cuồn cuộn.""",
"""Còn tự lừa mình dối người cái gì nữa, anh lạnh lùng nghĩ bụng, có thể vì một lời hẹn ước ấu trĩ thế này mà từ bỏ một dự án trị giá hàng trăm triệu, đầu óc anh sớm đã bị chó gặm mất rồi.""",
"""Thật nực cười làm sao, loại người như anh mà cũng có thể nảy sinh thứ tình cảm này sao, thứ này gọi là gì, thích ư?""",
"""Trong tầm mắt, Giang Minh Lãng xuyên qua đám đông lại đưa mắt nhìn về phía hàng ghế người nhà lần nữa, nụ cười dần dần tắt lịm, nỗi thất vọng trên mặt chẳng cần nói cũng hiểu rõ.""",
"""Cảnh tượng này rơi trọn vào mắt Phó Vân Xuyên.""",
"""Đã thích, vậy thì chiếm đoạt.""",
"""Anh nhìn chằm chằm vào nét cô đơn hụt hẫng hiện rõ trên gương mặt Giang Minh Lãng, quay người, biến mất vào trong bóng tối.""",
"""Cú ném ba điểm cuối cùng của Giang Minh Lãng đã giúp đội tuyển tỉnh bọn họ lội ngược dòng đánh bại đội tuyển tỉnh bên cạnh vào giây cuối cùng, xoay chuyển tình thế ngoạn mục trở thành nhà vô địch của giải đấu năm nay. Giữa vòng vây của đồng đội, cậu ôm cúp vô địch, bị mọi người vừa xô vừa đẩy trở về phòng nghỉ.""",
"""“Giang Minh Lãng, mày đỉnh vãi chưởng, mẹ nó cú ba điểm cuối cùng ngầu đét!” “Mấy đứa có thấy bản mặt thằng béo bên kia ban nãy không, ha ha ha.” “Giang Minh Lãng, sao mày không nói câu nào thế?”""",
"""Có người nhận ra Giang Minh Lãng bỗng nhiên như ngốc ra, đứng khựng lại không đi tiếp nữa, ánh mắt nhìn thẳng tắp về phía trước.""",
"""Mọi người khó hiểu nhìn theo, phát hiện phía trước có một người đàn ông âu phục phẳng phiu đang lặng lẽ đứng ở đó.""",
"""Giây tiếp theo, Giang Minh Lãng bỗng lao vút ra ngoài, hệt như một chú chó lớn nhìn thấy chủ nhân, tông thật mạnh vào trong lòng ngực đối phương.""",
"""Phó Vân Xuyên ôm lấy Giang Minh Lãng lùi lại vài bước mới khó khăn lắm mới đứng vững được.""",
"""“Tôi cứ tưởng hôm nay anh không tới cơ.” Giọng Giang Minh Lãng nghèn nghẹn.""",
"""Phó Vân Xuyên giơ tay lên, xoa xoa đầu cậu: “Tôi vừa thấy cú ném ba điểm đè còi của cậu rồi.”""",
"""Cả đám người nhìn thấy cảnh tượng trước mắt đều ngây như phỗng: “Khoan đã, người đàn ông này... tao cảm thấy hình như gặp ở đâu rồi thì phải...”""",
"""Đúng lúc này, huấn luyện viên cũng từ phía đối diện bước tới, vẫy tay gọi bọn họ: “Qua đây hết một lát, vị này là chủ tịch tập đoàn Vân Xuyên, Phó Vân Xuyên, mau tới chào một tiếng đi.”""",
"""-""",
"""Dưới sự tài trợ của Phó Vân Xuyên, toàn bộ đội tuyển tỉnh sau trận đấu được đưa tới một khách sạn xa hoa bậc nhất thành phố A để tổ chức tiệc mừng công.""",
"""Giang Minh Lãng với tư cách là đại công thần trở thành nhân vật chính bị chuốc rượu suốt cả bữa tiệc.""",
"""Giang Minh Lãng trước giờ chưa từng uống rượu, vài ly vào bụng là bắt đầu mất hết tỉnh táo, về sau mọi người vì sợ chọc giận Phó Vân Xuyên nên cũng chẳng dám làm khó Giang Minh Lãng quá mức.""",
"""Sau khi tiệc mừng công kết thúc, Giang Minh Lãng đã say đến mức chẳng phân biệt nổi đông tây nam bắc, Phó Vân Xuyên ôm lấy cậu, mở một căn phòng tổng thống ngay trong khách sạn.""",
"""Giang Minh Lãng ngã gục vào vai Phó Vân Xuyên, hơi thở nóng rực phả vào vành tai anh.""",
"""“Phó tiên sinh, khoảng thời gian này tôi nhớ anh lắm.”""",
"""Cửa phòng được đẩy ra, ánh đèn lần lượt bật sáng từ lối vào huyền quan, Phó Vân Xuyên trở tay đóng sầm cửa lại, ép Giang Minh Lãng lên cánh cửa, trực tiếp cúi đầu hôn tới tấp.""",
"""Bị men rượu xâm chiếm lý trí, Giang Minh Lãng vô cùng kích động, cậu ra sức hôn trả lại, bản năng của giống đực chi phối khiến cậu muốn chinh phục Phó Vân Xuyên, nhưng lại bị Phó Vân Xuyên đè chặt áp chế.""",
"""Hai người càng hôn càng kịch liệt, vừa hôn vừa di chuyển vào sâu trong phòng.""",
"""Giang Minh Lãng bị đè ngã thật mạnh xuống giường.""",
"""Chỉ thấy Phó Vân Xuyên từ trên cao nhìn xuống cậu, đôi mắt đen nhánh cuồn cuộn những đợt sóng ngầm, dường như đang do dự điều gì.""",
"""Tầm mắt Giang Minh Lãng mờ mịt, nhọc nhằn tìm kiếm hình bóng của Phó Vân Xuyên, cậu bỗng kéo mạnh Phó Vân Xuyên xuống, xoay người đè anh dưới thân, sau đó chống hai cánh tay đứng bất động.""",
"""Giang Minh Lãng cụp mắt nhìn khuôn mặt Phó Vân Xuyên, nói: “Mấy ngày nay tôi đã nghĩ thông suốt rồi, tôi quyết định đồng ý với anh.”""",
"""“Đồng ý cái gì?” Ánh mắt Phó Vân Xuyên tỉnh táo lại không ít.""",
"""Dưới ánh đèn, trên khuôn mặt Giang Minh Lãng thoáng hiện lên một nét thẹn thùng, cậu gập khuỷu tay xuống, ghé sát môi vào tai Phó Vân Xuyên, khẽ thì thầm: “Phó tiên sinh, tôi thích anh.”""",
"""“Cái gì?” Đồng tử Phó Vân Xuyên khẽ chấn động.""",
"""“Chúng ta có thể yêu nhau rồi.” Giang Minh Lãng hớn hở nói, như thể đã trút được điều quan trọng nhất đè nặng trong lòng suốt một tháng qua, cậu tựa như chiếc máy tính bị sập nguồn, tay vừa buông lỏng một cái, cả người liền gục xuống đè lên thân Phó Vân Xuyên, ngủ say như chết.""",
"""Đâu hay biết rằng Phó Vân Xuyên ở dưới thân sau khi nghe thấy câu nói của cậu, toàn thân đã cứng đờ như hóa đá.""",
"""Mãi một hồi lâu sau, Phó Vân Xuyên mới từ nơi sâu thẳm trong lồng ngực phát ra một tiếng cười lạnh tự giễu:""",
"""“Thích tôi?”""",
"""“Yêu nhau?”""",
"""“Hừ, đùa cái gì thế không biết.”""",
"""Lời tác giả:""",
"""Phó Vân Xuyên tự ti (nói nhỏ)""",
"""Chương 23: Alaska 23""",
"""Giang Minh Lãng mơ mơ màng màng mở mí mắt ra, đập vào mắt là một không gian hoàn toàn xa lạ, cậu chống tay ngồi dậy trên giường, phát hiện cả căn phòng vắng tanh không một bóng người.""",
"""Cậu vận hành bộ não đang đình trệ, nhọc nhằn chắp vá lại ký ức đêm qua.""",
"""Cậu nhớ mình trong tiệc mừng công đã uống rất nhiều rượu, sau đó được Phó Vân Xuyên đưa đến đây, rồi tiếp theo... Từng chi tiết nhỏ hiện về rõ mồn một trong tâm trí, Giang Minh Lãng bỗng bật dậy khỏi giường, rơi vào trạng thái đờ đẫn hóa đá.""",
"""Đúng lúc này, điện thoại cậu rung lên một tiếng.""",
"""Phó Vân Xuyên: Tỉnh rồi thì gọi điện thoại cho tài xế, bảo ông ấy chở cậu về.""",
"""Giang Minh Lãng nhìn vào màn hình điện thoại, bên dưới là một dãy số điện thoại."""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_026\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_026\translation.md'

with open(src_path, 'r', encoding='utf-8') as f:
    source_paras = [p.strip() for p in f.read().split('\n\n') if p.strip()]

print(f"Source count: {len(source_paras)}, Trans count: {len(paras_trans)}")
assert len(source_paras) == len(paras_trans)

full_text = '\n\n'.join(paras_trans) + '\n'
forbidden = re.findall(r'\b(hắn)\b', full_text, re.IGNORECASE)
print(f"Forbidden pronouns count: {len(forbidden)}, {forbidden}")
assert len(forbidden) == 0

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Saved ch_026 successfully!")
