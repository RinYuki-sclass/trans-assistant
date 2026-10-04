import re
import os

paras_trans = [
"""---
title: Chương 24: Trang 24
---""",
"""Suốt cả quãng đường Giang Minh Lãng đều mất hồn mất vía, mãi cho đến khi xe dừng trước cổng trường được một lúc lâu rồi, cậu mới hớt hải cuống cuồng xuống xe, chào tạm biệt Phó Vân Xuyên.""",
"""Phó Vân Xuyên nhìn hình bóng Giang Minh Lãng thu nhỏ dần trong gương chiếu hậu, ánh mắt trầm xuống.""",
"""“Tiểu Cầu, tôi phải làm sao mới có thể gom đủ một triệu này?” Giang Minh Lãng gọi hệ thống ra, hy vọng nhận được sự giúp đỡ từ hệ thống.""",
"""Quả cầu ánh sáng chầm chậm hiện hình: 【Vấn đề này vượt quá phạm vi dữ liệu lưu trữ của bản hệ thống.】""",
"""Nó cũng chỉ là một quả cầu lần đầu tiên đến thế giới loài người làm nhiệm vụ mà thôi, nó cũng chẳng biết đâu.""",
"""Giang Minh Lãng ủ rũ gục đầu xuống bàn học.""",
"""Cậu quá đỗi đồng cảm với nguyên chủ Giang Minh Lãng, từng li từng tí ký ức sống cùng ông ngoại tựa như dòng nước chảy hiện rõ mồn một trong tâm trí. Ông ngoại là một ông lão vô cùng nóng tính, Giang Minh Lãng từ nhỏ đến lớn đều bị ông đánh đòn, nhưng ông ngoài miệng cay độc trong lòng mềm yếu, luôn luôn im hơi lặng tiếng đối tốt với cậu.""",
"""Giang Minh Lãng từ nhỏ đã thường xuyên đi làm thêm kiếm sinh hoạt phí, thế là cậu men theo ký ức của chính Giang Minh Lãng để tìm kiếm, tìm được một ứng dụng tuyển dụng việc làm, lại mất cả buổi trưa để đi hỏi han, phát hiện cho dù cậu có trốn học đi làm thuê thì suốt cả ngày nhiều nhất cũng chỉ kiếm được vài trăm tệ.""",
"""Một triệu tệ đối với cậu quả thực là một con số trên trời.""",
"""Chuyện này quấn chặt lấy tâm trí, khiến buổi chiều cậu chơi bóng rổ liên tục xảy ra sơ suất.""",
"""“Minh Lãng——”""",
"""Giọng nói của Phó Ngôn từ phía sau truyền đến, cậu ta bước tới trước mặt Giang Minh Lãng: “Có một chuyện tôi rất muốn hỏi thẳng mặt cậu, về chuyện đêm hôm đó... Tôi cảm thấy hình như cậu rất để bụng việc tôi tiếp cận Phó tiên sinh.”""",
"""Cảm nhận được ánh mắt của Ngụy Minh ở đằng trước nhìn mình hằn học như muốn ăn tươi nuốt sống, Giang Minh Lãng cũng chẳng muốn nói chuyện nhiều với Phó Ngôn.""",
"""Đang định tìm cớ rời đi thì trong đầu cậu bỗng lóe lên một ý nghĩ.""",
"""Cậu bỗng nhìn thẳng vào Phó Ngôn, hỏi: “Phó Ngôn, cậu có biết chỗ nào có thể kiếm tiền thật nhanh không? Kiểu có thể kiếm được rất nhiều tiền ấy.”""",
"""Trong tiểu thuyết, Phó Ngôn vì không muốn tiêu tiền của Phó gia nên vẫn luôn làm thêm ở ngoài kiếm tiền, Giang Minh Lãng nghĩ bụng có lẽ Phó Ngôn biết cách làm sao để kiếm được tiền.""",
"""Phó Ngôn không ngờ cậu lại hỏi câu này, sững sờ trong giây lát rồi gật đầu: “Biết thì có biết, bây giờ cậu đang thiếu tiền lắm à, nhưng...” Cậu ta muốn nói với mối quan hệ giữa Phó Vân Xuyên và cậu thì làm sao cậu có thể thiếu tiền được.""",
"""Dưới sự gặng hỏi dồn dập của Giang Minh Lãng, Phó Ngôn đưa cho cậu danh thiếp của một người.""",
"""Người này là quản lý của trang viên rượu Bán Nguyệt, Phó Ngôn bảo làm bartender ở bên đó một ngày có thể nhận được mức lương bốn con số.""",
"""“Tôi nói là trường hợp bình thường nhất thôi đấy,” Phó Ngôn ngập ngừng liếc nhìn cậu một cái, ám chỉ: “Nhưng tôi từng thấy có người sau khi tan làm thì đi ra ngoài cùng khách của tửu trang,” Cậu ta ghé sát tai Giang Minh Lãng, thì thầm: “Hôm sau đã ngồi xe sang đến xin từ chức rồi.”""",
"""Giang Minh Lãng chẳng hề hiểu được lời ám chỉ của Phó Ngôn, cậu hết sức cảm kích chào tạm biệt Phó Ngôn, rồi rời khỏi sân bóng để liên lạc với quản lý của trang viên rượu Bán Nguyệt.""",
"""Đâu ngờ rằng Phó Ngôn phía sau sau khi đưa mắt tiễn cậu rời đi liền rút điện thoại ra.""",
"""Do dự vài giây sau, tin nhắn được gửi đi.""",
"""Phó Ngôn: Phó tiên sinh, ngại quá lại làm phiền ngài rồi, nhưng tôi có một chuyện không biết có nên nói với ngài không, là về Minh Lãng...""",
"""Phó Ngôn: Tôi tin cậu ấy sẽ không lầm đường lạc lối, nhưng tôi vẫn muốn báo cho ngài biết chuyện này.""",
"""Phó Ngôn: À đúng rồi, chuyện lần trước là vấn đề của tôi, tôi không nên đến chất vấn ngài, tôi chỉ là lo lắng cho hai người thôi, không biết dạo này ngài có rảnh không, có thể ra ngoài uống tách cà phê được không?""",
"""...""",
"""Quản lý trang viên rượu Bán Nguyệt bảo Giang Minh Lãng chiều tan học thì tới tửu trang tìm ông ta, Giang Minh Lãng chân trước vừa đồng ý xong thì chân sau đã nhận được tin nhắn của Phó Vân Xuyên.""",
"""Phó Vân Xuyên hỏi hôm nay cậu mấy giờ tan học, anh đến đón.""",
"""Giang Minh Lãng hoàn toàn không muốn để Phó Vân Xuyên biết chuyện này, thế là gửi lại một câu ngại quá, nói với Phó Vân Xuyên rằng sau khi tan học cậu phải đi huấn luyện bóng, bảo Phó Vân Xuyên không cần tiện đường đón cậu về trang viên nữa.""",
"""Cậu hoàn toàn không hề hay biết ở đầu dây bên kia, sắc mặt Phó Vân Xuyên khi nhìn thấy dòng tin nhắn này u ám và đáng sợ đến nhường nào.""",
"""Sau khi tan học, Giang Minh Lãng bắt taxi đến trang viên rượu Bán Nguyệt, nhìn cánh cổng lớn của tửu trang, cậu bất giác nhớ lại lần đầu tiên gặp gỡ Phó Vân Xuyên.""",
"""“Được, tối nay cậu có thể đi làm luôn. Thông thường người ở chỗ chúng tôi đều phải trải qua đào tạo mới được nhận việc, nhưng,” Người quản lý đẩy gọng kính viền vàng trên sống mũi, đánh giá Giang Minh Lãng từ trên xuống dưới: “Điều kiện của cậu rất tốt, lương theo giờ có thể trả cho cậu một nghìn tệ.”""",
"""Giang Minh Lãng nghe vậy liền rút điện thoại ra dùng máy tính bấm bấm, nghiêng người cản người quản lý lại: “Xin chào, tôi đang cần tiền gấp, có thể trả cao hơn cho tôi một chút được không? Tôi việc gì cũng làm được hết, lau sàn, rửa ly, khiêng bàn...”""",
"""“Tôi nghĩ cậu chưa hiểu rõ định vị tệp khách hàng ở đây của chúng tôi rồi, cậu hoàn toàn không cần phải làm mấy công việc đó.” Người quản lý giật giật khóe miệng, ánh mắt một lần nữa lướt qua khuôn mặt và vóc dáng của Giang Minh Lãng, thỏa hiệp nói.""",
"""“Cùng lắm tăng thêm cho cậu năm trăm nữa, còn về những chuyện khác...” Người quản lý nói lấp lửng mập mờ: “Chuyện xảy ra ngoài chỗ này tôi không quản được đâu.”""",
"""Giang Minh Lãng vẫn không hiểu nổi những ẩn ý phức tạp của loài người, tuy rằng không thể gom ngay lập tức một triệu tệ, nhưng làm việc ở đây cũng là một nguồn thu nhập khổng lồ.""",
"""Sau khi báo cáo qua với mẹ Giang một tiếng, cậu liền được người quản lý dẫn đi thay quần áo. Quản lý dặn cậu buổi tối cứ đứng ở quầy bar sắp xếp ly rượu là được, những việc khác tạm thời chưa cần cậu làm.""",
"""Sau chín giờ tối, trang viên rượu bắt đầu giờ kinh doanh, khách khứa lục tục kéo đến khá đông.""",
"""Giang Minh Lãng bận rộn làm việc nên không nhìn thấy các cuộc gọi nhỡ và tin nhắn của Phó Vân Xuyên trên điện thoại.""",
"""“Chào cậu, cậu là người mới à?” Một gã đàn ông trẻ tuổi đột nhiên bước đến đứng đối diện Giang Minh Lãng, đẩy một tấm danh thiếp sang cho cậu: “Bố tôi là chủ tịch bất động sản Gia Minh.”""",
"""Ánh mắt người đàn ông trượt dài từ khuôn mặt cậu xuống dưới, thầm nghĩ cả mặt mũi lẫn thân hình đều trông hoang dã ra trò.""",
"""Giang Minh Lãng liếc nhìn tấm danh thiếp, khó hiểu nhíu mày.""",
"""Gã đàn ông dường như sợ cậu hiểu lầm, vội nói: “Đừng hiểu lầm nhé, tôi không thích đàn ông đâu, là chị tôi chấm cậu đấy,” Gã hất cằm về phía người phụ nữ cách đó không xa: “Tối nay rảnh không, tan làm ra ngoài uống vài ly với bọn tôi nhé?”""",
"""Giang Minh Lãng đang định bảo không được thì khóe mắt bỗng thoáng thấy một bóng người vô cùng quen thuộc đang đằng đằng sát khí sải bước đi về phía bên này.""",
"""Phó Vân Xuyên dường như chẳng bao giờ sợ nóng, chiếc áo măng tô đen khiến anh trông hệt như một ông trùm xã hội đen máu lạnh trong phim điện ảnh.""",
"""Thấy Giang Minh Lãng như ngốc ra chẳng hề đáp lời, gã đàn ông giục giã: “Đi hay không, cho một câu dứt khoát đi, nói trước là chị tôi ra tay hào phóng lắm đấy.”""",
"""“Cút.” Một giọng nam trầm thấp lạnh lẽo cắt ngang lời thúc giục của gã.""",
"""Người đàn ông dường như chưa từng bị ai bảo cút bao giờ, mặt mày xám ngoét quay đầu lại chửi: “Mày là thằng nào?”""",
"""Giang Minh Lãng tròn xoe mắt, không dám tin lại nhìn thấy Phó Vân Xuyên ở nơi này.""",
"""“Cút ra ngoài.” Phó Vân Xuyên đến một cái liếc mắt cũng chẳng buồn bố thí cho gã, anh nhìn trừng trừng vào mắt Giang Minh Lãng, ngọn lửa giận dữ cuộn trào nơi đáy mắt đã lộ rõ không cần che giấu.""",
"""“Mày có biết tao là ai không, có cần nhìn xem đây là chỗ nào không hả!” Gã thanh niên càng thêm tức giận, tiếng quát tháo thu hút sự chú ý của mọi người xung quanh.""",
"""Đúng lúc này, người quản lý rảo bước nhanh tới bên cạnh Phó Vân Xuyên, cung kính khúm núm cất tiếng: “Phó tiên sinh.”""",
"""Phó Vân Xuyên nói: “Hôm nay chỗ này tôi bao trọn, bảo bọn họ đi hết đi, toàn bộ hóa đơn tôi thanh toán.”""",
"""Gã thanh niên nghe thấy lời này thì sắc mặt lập tức biến đổi, ai mà chẳng biết mức tiêu xài ở Bán Nguyệt đắt đỏ đến mức nào.""",
"""Thế nhưng người quản lý lại chẳng hề do dự lấy nửa giây, lập tức phân phó nhân viên đi giải tán khách hàng.""",
"""Bên kia, dưới sự kiên nhẫn khuyên nhủ của đội ngũ phục vụ, khách khứa dần dần rời đi hết.""",
"""Giang Minh Lãng ngơ ngác nhìn xung quanh bốn bề vắng tanh không một bóng người: “Phó tiên sinh, sao anh lại ở đây?”""",
"""“Nhiều khi tôi thực sự không thể đoán nổi rốt cuộc cậu muốn làm cái gì,” Cách một quầy bar, Phó Vân Xuyên vươn tay ra, những ngón tay bọc trong găng da nắm chặt lấy chiếc cà vạt trên đồng phục của Giang Minh Lãng, khẽ miết.""",
"""“Nhưng cậu phải biết hậu quả của việc chọc giận tôi là gì.” Cùng với âm cuối của chữ rốt cuộc tan biến, Giang Minh Lãng cảm thấy sau gáy mình bị chiếc cà vạt siết chặt kéo mạnh về phía trước, cậu mất thăng bằng ngã nhào tới, may mà kịp dùng hai cánh tay chống đỡ, nếu không sống mũi suýt chút nữa đã va thẳng vào mặt Phó Vân Xuyên.""",
"""“Ai cho cậu cái lá gan dám tìm người khác ngay dưới mí mắt tôi,” Phó Vân Xuyên nheo mắt, nghiến răng nghiến lợi thốt ra từng câu từng chữ: “Cậu muốn cái gì mà tôi không cho được?”""",
"""Giang Minh Lãng ngơ ngác nhìn khuôn mặt Phó Vân Xuyên gần trong gang tấc, nhọc nhằn tiêu hóa những lời Phó Vân Xuyên vừa nói.""",
"""Ý của Phó Vân Xuyên là anh đã biết chuyện mình thiếu tiền, trách mình không nói cho anh biết, không tìm anh để đòi sao?""",
"""Sau một hồi suy đi tính lại, cậu bừng tỉnh đại ngộ, hóa ra Phó Vân Xuyên nổi giận là vì chuyện này.""",
"""“Hóa ra anh biết rồi à.” Cậu ngượng ngùng mím môi: “Anh đừng giận mà, chính vì đó là anh nên tôi mới không muốn vay tiền của anh đấy chứ.”""",
"""Sắc mặt Phó Vân Xuyên giãn ra một chút, nói: “Cái gì?”""",
"""Giang Minh Lãng vươn hai cánh tay ra, vỗ vỗ lên lưng sau của Phó Vân Xuyên: “Xin lỗi nhé, tôi biết chúng ta là bạn bè, tôi gặp khó khăn đáng lẽ phải tìm anh giúp đỡ đầu tiên, nhưng anh đối với tôi thì khác biệt lắm, tôi không muốn tìm anh.”""",
"""Hỏi vay tiền Phó Vân Xuyên khiến cậu cảm thấy khó mở lời. Chuyện này rất kỳ lạ, bởi vì cậu chưa bao giờ ngần ngại mượn đồ của Maltese cả.""",
"""“Tôi muốn tự mình nghĩ cách gom đủ một triệu tiền phẫu thuật này cho ông ngoại trước đã.” Cậu gác cằm lên vai Phó Vân Xuyên, buồn bã nói.""",
"""Cơ thể Phó Vân Xuyên cứng đờ rõ rệt, một lúc sau anh mới dùng lại ngữ điệu bình thường cất lời: “Thay quần áo đi, về nhà với tôi.”""",
"""Giang Minh Lãng hiểu hôm nay không thể làm việc được nữa rồi, sau khi thay đồ xong liền ngồi lên xe của Phó Vân Xuyên.""",
"""Phó Vân Xuyên chắc hẳn là vội vã chạy tới trong lúc gấp gáp, hôm nay chính anh tự mình lái xe.""",
"""“Sau này cấm không được đến nữa.” Phó Vân Xuyên vừa lái xe vừa nói: “Bên này sẽ không thuê cậu nữa đâu.”""",
"""“Tại sao chứ, tôi cần phải kiếm tiền mà.” Giang Minh Lãng hỏi.""",
"""Phó Vân Xuyên: “Cậu có tiền.”""",
"""Giang Minh Lãng: “Tôi làm gì có tiền đâu.”""",
"""Phó Vân Xuyên: “Tôi từng đưa thẻ cho cậu rồi.”""",
"""Giang Minh Lãng: “Hả?”""",
"""Cậu chợt nhớ ra rồi, rất lâu trước đây Phó Vân Xuyên từng tiện tay đưa cho cậu một chiếc thẻ ngân hàng, nhưng cậu không để trong lòng, tiện tay quẳng trong phòng ngủ.""",
"""Phó Vân Xuyên: “Dùng chiếc thẻ đó đi thanh toán tiền phẫu thuật cho ông ngoại cậu, còn cả các chi phí về sau nữa, xe cộ, nhà cửa, muốn mua gì thì tự mình mua.”"""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_024\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_024\translation.md'

with open(src_path, 'r', encoding='utf-8') as f:
    source_paras = [p.strip() for p in f.read().split('\n\n') if p.strip()]

print(f"Source count: {len(source_paras)}, Trans count: {len(paras_trans)}")
assert len(source_paras) == len(paras_trans)

full_text = '\n\n'.join(paras_trans) + '\n'
forbidden = re.findall(r'\b(hắn|y)\b', full_text, re.IGNORECASE)
print(f"Forbidden pronouns count: {len(forbidden)}, {forbidden}")
assert len(forbidden) == 0

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Saved ch_024 successfully!")
