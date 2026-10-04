import re
import os

paras_trans = [
"""---
title: Chương 35: Trang 35
---""",
"""Lúc đó liên hệ tới kết cục của Phó Vân Xuyên trong tiểu thuyết, Giang Minh Lãng bỗng nảy sinh suy đoán có lẽ lọ thuốc này chính là cội nguồn của mọi chuyện, nhưng cậu vẫn luôn không tài nào tưởng tượng ra mối quan hệ nhân quả logic hợp lý.""",
"""Mãi cho đến vừa rồi.""",
"""“Tôi vẫn luôn không thể hiểu nổi, rốt cuộc là loại người nhà kiểu gì mà có thể làm ra được chuyện táng tận lương tâm đến mức này.”""",
"""Trong tiểu thuyết, một Phó Vân Xuyên lợi hại xuất chúng như vậy rốt cuộc lại dễ dàng thảm bại cay đắng, hóa ra toàn bộ đều bắt nguồn từ đây.""",
"""Bàn tay Giang Minh Lãng nắm chặt lọ thuốc nổi gân xanh chằng chịt, cậu căm phẫn nhìn hai vợ chồng trước mắt, rút điện thoại ra gửi tin nhắn đi.""",
"""“Mẹ tôi đã cầm số thuốc còn lại đi báo cảnh sát rồi.”""",
"""Cậu gằn từng câu từng chữ đanh thép.""",
"""Mặc kệ sắc mặt Phó Thành Hồng trắng bệch như xác chết, hơi thở dồn dập gấp gáp như sắp ngất lịm đi, Giang Minh Lãng xoay người, dắt tay Phó Vân Xuyên đang ngẩn ngơ thất thần bước ra ngoài: “Chúng ta đi thôi Phó tiên sinh.”""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 80】""",
"""“Vân Xuyên, Vân Xuyên con đừng đi mà, mẹ cầu xin con, cho bố con một con đường sống đi con ơi!”""",
"""Phía sau truyền đến tiếng gào khóc thảm thiết của Phó phu nhân.""",
"""Ngọn lửa giận dữ kìm nén bấy lâu trong lòng Giang Minh Lãng cuối cùng bùng nổ không còn chỗ giấu, cậu ngoắt người quay lại, gầm lên: “Hai người thật sự là cha mẹ của anh ấy sao?!”""",
"""“Loại cha mẹ kiểu gì mà đối với việc con trai ruột bị người ta ức hiếp ngược đãi ở nhà người khác lại chẳng hề hay biết nửa phần, ngược lại còn chỉ trích con trai lang tâm cẩu phế mưu hại gia đình mình?”""",
"""“Hai người đối với nỗi sợ hãi bóng tối và không gian hẹp kín của anh ấy thì thờ ơ không thèm đếm xỉa, quay lưng một cái liền nhốt anh ấy vào nhà kho tối tăm không thấy ánh mặt trời!”""",
"""“Hai người mở miệng ra là bảo không biết, là bất đắc dĩ, nhưng trên thực tế chính là máu lạnh ích kỷ, tàn nhẫn ngu muội!”""",
"""Giang Minh Lãng đem toàn bộ vốn liếng từ ngữ mắng chửi học được suốt cả cuộc đời làm cún trút sạch lên đầu bọn họ.""",
"""Nếu có thể, cậu thậm chí còn muốn xông lên gâu gâu hai tiếng, dùng tiếng chó để chửi bới cho bõ tức hơn.""",
"""Phó phu nhân bị một tràng mắng xối xả tát thẳng vào mặt làm cho chết sững, tiếng khóc cũng nghẹn ứ lại trong cổ họng.""",
"""Đúng lúc này, Phó Vân Xuyên – người nãy giờ ánh mắt luôn dính chặt trên người Giang Minh Lãng – đã lấy lại thần sắc thường ngày, anh bình thản cất lời: “Đi thôi.”""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 60】""",
"""Giang Minh Lãng cố nén cơn giận, rảo bước đi theo sau lưng anh.""",
"""“Ngày mai tôi sẽ giao nộp toàn bộ bằng chứng các người ép tôi nhận tội thay cho Phó Vân Hi lên đồn cảnh sát,” Phó Vân Xuyên không thèm ngoái đầu lại, vẻ mặt lạnh lùng chết lặng tuyên bố:""",
"""“Nếu không phải vì ngày hôm nay, tôi cũng chẳng nỡ đi đến bước đường này, những ngày tháng còn lại, tự lo lấy thân đi.”""",
"""Tiếng thét chói tai kinh hoàng của Phó phu nhân kéo theo sự hỗn loạn khắp nơi, Giang Minh Lãng nghe thấy cả căn biệt thự bắt đầu nhốn nháo hoảng loạn:""",
"""“Gọi xe cấp cứu mau lên, nhanh lên——”""",
"""Chiếc xe lăn bánh rời khỏi căn biệt thự gà bay chó sủa kia, không gian bên trong khoang xe yên tĩnh lạ thường, Phó Vân Xuyên cuối cùng cũng trút bỏ hết toàn bộ lớp vỏ ngụy trang gồng mình, anh nghiêng người vùi đầu vào lồng ngực Giang Minh Lãng.""",
"""“Cảm ơn cậu.”""",
"""Giang Minh Lãng ngẩn người, rồi hào sảng đưa tay vỗ vỗ lên bờ vai rộng lớn của Phó Vân Xuyên như anh em tốt.""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 50】""",
"""Do dự hồi lâu, Giang Minh Lãng vẫn quyết định nói những lời mình muốn nói cho Phó Vân Xuyên nghe:""",
"""“Thực ra tôi biết vì sao trước đây anh lại giả vờ mình học kém,” cậu nói.""",
"""Bác tài xế phía trước đột nhiên rảnh tay, rút ra một cặp nút bịt tai cách âm không đổi sắc mặt đeo vào tai mình.""",
"""“Tôi có một người bạn cũng giống như vậy, nó thực ra rất thông minh, nhưng vì muốn thu hút sự chú ý của người khác nên cứ cố tình quậy phá gây sự.”""",
"""“Ý tôi muốn nói là, chắc hẳn anh đã từng rất để tâm đến bố mẹ mình, anh muốn bọn họ yêu thích anh.”""",
"""Giang Minh Lãng đầu óc thẳng như ruột ngựa chẳng biết vòng vo, cũng không hiểu cách nói khéo léo để dỗ dành cảm xúc con người.""",
"""Quả nhiên không ngoài dự đoán, Phó Vân Xuyên có xu hướng nổi giận khi bị chọc trúng tâm tư thầm kín: “Câm miệng.”""",
"""Giang Minh Lãng gãi gãi đầu, đột nhiên ghé sát tai Phó Vân Xuyên, thì thào nói nhỏ: “Nói cho anh một bí mật nhé, thực ra tôi là một chú chó lang thang đấy.”""",
"""Thấy Phó Vân Xuyên ngẩng đầu lên, cậu tiếp tục nói: “Ở chỗ chúng tôi có rất nhiều bạn là chó lang thang, cũng có rất nhiều đứa không biết bố mẹ mình là ai, giống hệt như tôi vậy.”""",
"""“Hồi nhỏ tôi thường hay nghĩ, tại sao bọn họ lại vứt bỏ tôi chứ, có phải vì tôi không giống như những đứa trẻ khác biết làm cho bọn họ yêu quý hay không? Rồi tôi cảm thấy rất buồn bã tủi thân, nghĩ rằng bản thân mình nhất định có chỗ nào đó có vấn đề, đến cả bố mẹ còn chẳng thích tôi, thì làm sao có chú chó nào thích tôi được nữa.”""",
"""“Về sau ngài sĩ quan chấp hành nói cho tôi biết, mọi sinh mệnh khi sinh ra trên đời đều là những cá thể độc lập riêng biệt, mỗi người đều mang một số mệnh khác nhau, giống như những khúc xương khác nhau vậy, một con chó không thích không có nghĩa là tất cả loài chó đều không thích, quả nhiên về sau tôi đã kết bạn được với rất nhiều người bạn tốt.”""",
"""“Ngài sĩ quan chấp hành còn bảo tôi phải tìm kiếm ước mơ của riêng mình, đi khám phá cuộc đời làm cún của mình, phải khiến cho bản thân sống thật vui vẻ, chứ không phải cứ mãi đắm chìm trong quá khứ thiếu may mắn.”""",
"""“Cậu đã tìm thấy ước mơ của mình chưa?”""",
"""Phó Vân Xuyên đột nhiên cất tiếng hỏi.""",
"""Giang Minh Lãng nhìn anh, rồi gật đầu thật mạnh.""",
"""Ước mơ của cậu chính là có được một người chủ hết mực cưng chiều yêu thương cậu, tốt nhất là có một người chủ nam và một người chủ nữ, như vậy chủ nữ có thể ôm ấp dỗ dành cậu, còn chủ nam có thể bảo vệ cậu và dắt cậu đi chơi đùa.""",
"""“Phó tiên sinh, anh cũng phải tìm kiếm động lực khiến anh hạnh phúc vui vẻ nhé.” Giang Minh Lãng chân thành nói.""",
"""Thế nhưng Phó Vân Xuyên không trả lời cậu, chỉ nhìn sâu vào đôi mắt cậu, trong con ngươi đen nhánh kia phản chiếu trọn vẹn khuôn mặt của cậu.""",
"""Ngay sau đó, Phó Vân Xuyên cúi đầu hôn thật sâu lên môi cậu.""",
"""“Xin lỗi, tôi hối hận rồi...” Trong lúc hôn nhau, Phó Vân Xuyên thì thầm một câu đầy ẩn ý mơ hồ.""",
"""“Hối hận cái gì cơ?” Giang Minh Lãng ngơ ngác khó hiểu.""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 40】""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 30】""",
"""...""",
"""Sau khi giao nộp vật chứng lên đồn cảnh sát, Phó Vân Xuyên chính thức đệ đơn kiện vợ chồng Phó Thành Hồng với hai tội danh: Tội bao che tội phạm và Tội cố ý gây thương tích chưa thành.""",
"""Đồng thời, anh cũng đệ đơn kiện Phó Minh – kẻ vẫn đang ngông cuồng làm loạn trên các phương tiện truyền thông – về tội phỉ báng xúc phạm danh dự.""",
"""Chân tướng năm xưa lần lượt được đưa ra ánh sáng trên khắp các mặt báo lớn nhỏ, nửa đời đầu đầy đau thương trắc trở của chủ tịch tập đoàn Vân Xuyên là Phó Vân Xuyên càng được các cơ quan báo đài thêu dệt phân tích thành muôn vàn câu chuyện cảm động.""",
"""Gần như chỉ trong vòng vỏn vẹn một tuần lễ, thị trường chứng khoán của các sản nghiệp cốt lõi thuộc Phó gia sụp đổ hoàn toàn, dàn nhân sự cấp cao kẻ bỏ đi người giải tán, lần lượt bị thâu tóm hoặc tuyên bố phá sản, chỉ còn sót lại vài doanh nghiệp nhỏ vẫn đang thoi thóp dưới sự chèo chống gượng gạo của Phó Ngôn.""",
"""Ngụy gia vì muốn bảo toàn lợi ích bản thân đã vội vã tuyên bố chấm dứt toàn bộ quan hệ hợp tác với Phó thị.""",
"""Trong khi đó, cổ phiếu của tập đoàn Vân Xuyên lại một đường tăng vọt phi mã.""",
"""Cuộc thương chiến chưa từng có trong lịch sử cuối cùng đã khép lại với chiến thắng vang dội thuộc về tập đoàn Vân Xuyên.""",
"""Còn về phần mẹ Giang, Phó Vân Xuyên không hề truy cứu thêm điều gì, chỉ từ chối đơn xin nghỉ việc của bà.""",
"""Và Giang Minh Lãng cũng đã thuận lợi hoàn thành kỳ thi cuối kỳ, chính thức bước vào kỳ nghỉ đông.""",
"""Khoảng thời gian này, giá trị hắc hóa của Phó Vân Xuyên liên tục giảm đều đặn, cho đến tận ngày hôm trước, hệ thống đột nhiên thông báo cho Giang Minh Lãng biết: Cậu đã hoàn thành nhiệm vụ!""",
"""Hôm nay quả cầu hệ thống lại bay ra, giục giã cậu mau chóng rời đi.""",
"""【Chúc mừng ngươi Alaska, ngươi đã hoàn thành xuất sắc nhiệm vụ rồi!】""",
"""Quả cầu ánh sáng bay lượn vòng quanh người cậu ríu rít.""",
"""【Ta đã báo cáo lên ngài sĩ quan chấp hành rồi, bây giờ chúng ta có thể quay về rồi đấy!~~】""",
"""Thấy Giang Minh Lãng cứ ngẩn ngơ thẫn thờ, hệ thống thắc mắc:""",
"""【Sao thế, ngươi không vui à?】""",
"""“Không có,” Giang Minh Lãng lắc đầu, ngẫm nghĩ một lát mới hạ giọng nói: “Có thể đợi thêm vài ngày nữa mới đi được không?”""",
"""Cậu muốn chào tạm biệt rất nhiều người.""",
"""Và còn cả Phó Vân Xuyên nữa.""",
"""【Được chứ, nhưng bởi vì ngươi đã hoàn thành nhiệm vụ nên hệ thống đã tự động đóng lại, qua một khoảng thời gian nữa ta sẽ quay lại đón ngươi, khi nào ngươi muốn đi thì ta sẽ đưa ngươi về.】""",
"""Giang Minh Lãng khẽ gật đầu.""",
"""【À đúng rồi, Alaska!】 Trước khi rời đi, quả cầu ánh sáng bất ngờ quay ngoắt lại.""",
"""“Có chuyện gì thế?”""",
"""【Thực ra ta phát hiện, ngươi cũng thông minh ra phết đấy chứ.】 Quả cầu ánh sáng tán thưởng nói.""",
"""Nhờ có Giang Minh Lãng xoay chuyển càn khôn cứu nguy vào phút chót, nếu không nhiệm vụ đầu tiên trong sự nghiệp của nó đã kết thúc trong thất bại ê chề rồi.""",
"""“Thực ra...” Giang Minh Lãng ngập ngừng do dự, cuối cùng vẫn thành thật cất lời: “Tiểu Cầu à, sau khi trở về ngươi nhất định phải chăm chỉ học tập thêm nhé.”""",
"""【Ý gì đấy con chó béo kia, ngươi đang chê bản cầu ngốc nghếch đấy hả!】""",
"""Quả cầu ánh sáng lập tức xù lông nổ tung.""",
"""Đúng lúc này, tiếng Phó Vân Xuyên đi làm về vọng vào tai Giang Minh Lãng.""",
"""Vừa thấy nhân vật phản diện trở về, quả cầu ánh sáng sợ hãi vội vã lủi mất tăm mất tích.""",
"""Cửa phòng được đẩy ra, người đàn ông âu phục phẳng phiu sải bước bước vào.""",
"""Giang Minh Lãng nhào một cú như chú cún béo lao thẳng đến trước mặt Phó Vân Xuyên.""",
"""“Ngày mai không đi tập bóng à?” Phó Vân Xuyên hiểu ý đưa tay xoa xoa đầu cậu, hỏi.""",
"""Giang Minh Lãng lắc đầu: “Huấn luyện viên bảo qua Tết mới quay lại tập luyện.”""",
"""Phó Vân Xuyên thong thả cởi áo khoác ngoài, sau đó cầm một chiếc hộp quà bằng da bước đến trước mặt Giang Minh Lãng.""",
"""“Hôm trước tôi đặt làm riêng, hôm nay người ta vừa giao tới.”""",
"""Giang Minh Lãng khó hiểu nhìn chiếc hộp, mãi cho đến khi Phó Vân Xuyên mở nắp hộp ra, mới phát hiện bên trong là một chiếc vòng cổ bằng da màu đen tinh xảo.""",
"""Mặt ngoài chiếc vòng cổ có in ba chữ cái: fyc.""",
"""“Đeo nó vào đi.”""",
"""Phó Vân Xuyên nhấc chiếc vòng cổ lên, nói với cậu.""",
"""Lời tác giả:""",
"""Vô cùng cảm ơn mọi người đã ủng hộ, mình sẽ tiếp tục cố gắng!""",
"""Chương 27: Alaska 27""",
"""Phó Vân Xuyên khẽ nhướng mày, kiên nhẫn chờ đợi.""",
"""Giang Minh Lãng từ chối: “Không muốn đâu.”""",
"""Phó Vân Xuyên thế mà lại chẳng hề tức giận, ngược lại còn ôn tồn nói: “Mấy hộp pate hôm trước mua cho mày tôi vẫn chưa vứt đâu, nếu mày đeo nó vào thì tôi sẽ trả lại cho mày.”""",
"""Giang Minh Lãng lúc này mới sực nhớ ra lần đầu tiên tới đây, Phó Vân Xuyên quả thực đã mua cho cậu mười mấy bao tải thức ăn và đồ ăn vặt cho chó.""",
"""Mỗi một món đều là thứ cậu chưa từng được ăn bao giờ, mùi thơm nức mũi.""",
"""Thấy thái độ của Giang Minh Lãng đã có phần lung lay, khóe môi Phó Vân Xuyên khẽ nhếch lên: “Mày chỉ cần đeo vào cho tôi ngắm một lát thôi.”""",
"""Nói đến đây, Phó Vân Xuyên lại rút ra một chiếc vòng cổ khác, bên trên có khắc chữ cái viết tắt tên của Giang Minh Lãng:""",
"""“Mày nhìn xem, tôi cũng có một chiếc này.”""",
"""“Thôi được rồi.”""",
"""Giang Minh Lãng mất hết tiền đồ gật gật đầu.""",
"""Cậu đón lấy chiếc vòng cổ đang móc trên ngón tay Phó Vân Xuyên, vụng về định tròng vào cổ mình, nhưng thiết kế của chiếc vòng cổ quá đỗi phức tạp, loay hoay mãi chẳng đeo được, cuối cùng Phó Vân Xuyên đành đón lấy, đích thân tròng chiếc vòng cổ vào cổ cậu."""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_035\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_035\translation.md'

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

print("Saved ch_035 successfully!")
