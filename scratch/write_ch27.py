import re
import os

paras_trans = [
"""---
title: Chương 27: Trang 27
---""",
"""Tối hôm qua về sau Phó Vân Xuyên đã nói những gì, cậu hoàn toàn không còn chút ấn tượng nào.""",
"""Cậu trước tiên trở về ký túc xá của đội tuyển tỉnh để thu dọn hành lý, lúc rời đi huấn luyện viên thông báo cho cậu biết sau này mỗi thứ Bảy đều phải quay lại đây tập huấn, dưới sự đưa đón của bác tài xế, cậu sau hơn một tháng xa cách lại lần nữa trở về trang viên của Phó Vân Xuyên.""",
"""Mẹ Giang nhìn thấy cậu trở về thì vui mừng khôn xiết, khi biết tin con trai đoạt cúp vô địch thì cười không khép được miệng, bảo rằng phải báo ngay tin vui này cho ông ngoại.""",
"""Ông ngoại của Giang Minh Lãng trong thời gian cậu tập huấn đã được chuyển tới bệnh viện tốt nhất ở thành phố A, ca phẫu thuật diễn ra rất thuận lợi, mẹ Giang định tuần sau khi ông cụ rời phòng ICU sẽ dẫn cậu vào viện thăm ông.""",
"""Đúng lúc này, cậu lại nhận được tin nhắn của Phó Vân Xuyên.""",
"""Phó Vân Xuyên: Về đến nơi thì lên thư phòng của tôi.""",
"""-""",
"""Bên trong thư phòng rộng lớn, Phó Vân Xuyên đứng lặng bên khung cửa sổ sát đất, trên gương mặt trắng bợt bệnh tật, chỉ có quầng thâm dưới mắt là đượm màu nồng đậm.""",
"""Anh chứng kiến cảnh Giang Minh Lãng bước xuống xe, vẫy tay chào dì Vương, cuối cùng biến mất khỏi tầm mắt của anh.""",
"""Tầm mắt dời đi, rơi trên cuốn lịch treo cách đó không xa, anh chậm rãi bước tới, đầu ngón tay lần lượt điểm qua vài con số, nhưng sự chú ý thì sớm đã không còn nằm ở đó nữa.""",
"""“Cốc cốc——” Cửa thư phòng vang lên tiếng gõ.""",
"""“Vào đi.”""",
"""Giang Minh Lãng hít sâu một hơi, lại chỉnh đốn lại mái tóc của mình, rồi mới đẩy cửa bước vào: “Phó tiên sinh, anh tìm tôi sao?”""",
"""Phó Vân Xuyên liếc nhìn cậu một cái, rồi ngồi lại vào chiếc ghế da.""",
"""“Sáng hôm nay, tại sao anh...” Giang Minh Lãng ngập ngừng do dự, muốn hỏi vì sao sáng nay Phó Vân Xuyên lại đi trước, nhưng lời mới nói được một nửa đã bị Phó Vân Xuyên cắt ngang.""",
"""“Bản hợp đồng trên bàn này cậu cầm lấy mà xem.” Phó Vân Xuyên tiện tay đẩy tập tài liệu trước mặt sang, sau đó rút ra một điếu thuốc lá mảnh, châm lửa rồi đưa lên giữa bờ môi: “Nếu cảm thấy hài lòng thì ký tên vào.”""",
"""“Khụ khụ!” Giang Minh Lãng không kịp phòng bị bị mùi khói thuốc làm cho sặc sụa, cậu bước tới cầm tập tài liệu trên bàn lên nhìn qua một lượt, ngay sau đó kinh ngạc ngẩng đầu lên: “Hợp đồng bao nuôi?”""",
"""Một làn khói mỏng phả ra từ bờ môi Phó Vân Xuyên, trong làn khói mờ ảo ánh mắt anh u tối khó lường, chất nicotine hun cho giọng nói của anh khàn đặc trầm thấp: “Cậu thỏa mãn các nhu cầu của tôi, ở bên cạnh tôi, tôi sẽ cho cậu tất cả những thứ cậu muốn.”""",
"""Giang Minh Lãng không thể tin nổi nhìn Phó Vân Xuyên: “Bao nuôi?” Trong đầu cậu nhớ lại ý nghĩa mà Phó Vân Xuyên đã dạy cho cậu trên xe hôm nọ.""",
"""“Là ý nghĩa như trước đây anh từng nói sao?” Cậu hỏi.""",
"""Giang Minh Lãng thậm chí còn đang nghĩ liệu bao nuôi có phải cũng là một phương thức yêu đương của con người hay không.""",
"""Phó Vân Xuyên ngắt lời cậu: “Đừng diễn nữa, đây chẳng phải là thứ cậu muốn sao? Bản hợp đồng này hiện tại tạm thời chưa có ngày kết thúc, trước khi tôi đề nghị chấm dứt, cậu phải ngoan ngoãn ở bên cạnh tôi.”""",
"""Nói xong, anh vừa cười vừa dùng ngữ điệu như đang đùa cợt cất lời: “Mọi thứ của cậu đều sẽ thuộc về tôi, nhưng cậu cứ yên tâm, đến thời điểm tôi muốn thả cậu đi rồi, trong thế giới của cậu sẽ vĩnh viễn không còn người tên Phó Vân Xuyên này nữa.”""",
"""Nói đến đây, biểu cảm của Phó Vân Xuyên thoáng hiện lên vẻ lạnh lùng chết lặng trong chốc lát.""",
"""“Vốn dĩ chỉ muốn chơi đùa với cậu vài ngày mà thôi.”""",
"""“Hết cách rồi, ai bảo tôi quá thích cậu cơ chứ.”""",
"""“Anh thích tôi?” Giang Minh Lãng chỉ nghe thấy điều mà cậu muốn nghe, cậu kiềm chế khóe môi đang muốn nhếch lên vì vui sướng, lấy hết dũng khí hỏi: “Vậy Phó tiên sinh, bây giờ chúng ta sắp yêu nhau đúng không?”""",
"""“Yêu đương?” Phó Vân Xuyên cười khẩy một tiếng, anh lắc đầu: “Không, chỉ là giao dịch.”""",
"""Làm sao anh có thể tin vào thứ quan hệ hư vô mờ mịt đó, chỉ có giao dịch mới vĩnh viễn đảm bảo Giang Minh Lãng thuộc về anh.""",
"""“Chỉ là... giao dịch?”""",
"""Một giây trước Giang Minh Lãng còn ôm trọn mong chờ, khoảnh khắc này, cậu như rơi xuống hầm băng lạnh giá.""",
"""Tất cả những thắc mắc của cậu đều đã tìm được lời giải đáp sau khi Phó Vân Xuyên dứt lời.""",
"""Hóa ra từ đầu chí cuối, Phó Vân Xuyên chưa từng có ý định cầu hoan với cậu, từ đầu đến cuối, anh chỉ muốn cùng cậu làm một cuộc giao dịch.""",
"""“Hóa ra, anh vẫn luôn coi tôi như một món hàng sao?” Nụ cười gượng gạo cứng đờ trên gương mặt, Giang Minh Lãng siết chặt bản hợp đồng trong tay, nhìn trừng trừng vào Phó Vân Xuyên hỏi từng câu từng chữ.""",
"""Cậu có thể không hiểu hàm nghĩa thực sự của việc bao nuôi, nhưng cậu hiểu rõ ý nghĩa của hai chữ giao dịch.""",
"""Cậu bắt đầu hồi tưởng lại từng khoảnh khắc mình đã hiểu lầm: “Cho nên thực ra bấy lâu nay anh đều đang nói cho tôi biết, chúng ta là quan hệ bao nuôi?”""",
"""Nghĩ đến những phản ứng ngốc nghếch bấy lâu nay của mình, cậu bàng hoàng lẩm bẩm: “Kết quả là tôi như một thằng ngốc, hoàn toàn không hiểu nổi ý của anh.”""",
"""Bàn tay kẹp điếu thuốc của Phó Vân Xuyên khựng lại giữa không trung.""",
"""“Tôi cứ tưởng anh đối tốt với tôi là vì thích tôi, cho nên tôi cũng thích anh,” Giang Minh Lãng ngước mắt nhìn thẳng vào mắt Phó Vân Xuyên, trong đôi mắt màu nâu rực lên ngọn lửa giận dữ ngút ngàn, đan xen cùng nỗi thất vọng cùng cực đang lan tràn: “Ít nhất tôi từng nghĩ chúng ta là bạn bè tốt của nhau.”""",
"""Lại một lần nữa nghe thấy hai chữ thích thốt ra từ miệng Giang Minh Lãng, lớp mặt nạ của Phó Vân Xuyên xuất hiện một vết nứt vỡ, khóe môi anh bỗng chốc hạ sụp xuống: “Lời nói dối cậu không nên nói nhất, chính là thích tôi.”""",
"""“Bốp——”""",
"""Tập hợp đồng dày cộp bị Giang Minh Lãng ném mạnh xuống dưới chân Phó Vân Xuyên, Giang Minh Lãng đỏ hoe mắt, gầm lên một tiếng gầm gừ uy hiếp đầy chấn động về phía Phó Vân Xuyên: “Tôi đúng là đồ ngu xuẩn, mới nghĩ rằng anh là người đầu tiên đối xử tốt với tôi như thế!”""",
"""Nét mặt Phó Vân Xuyên cứng đờ lại, nhìn Giang Minh Lãng không thèm quay đầu lại sải bước đi ra ngoài, giận dữ quát: “Cậu đứng lại đó cho tôi!”""",
"""【Xin chú ý, giá trị hắc hóa của phản diện đã tăng lên, hiện tại giá trị hắc hóa là: 86】""",
"""Giang Minh Lãng làm như không nghe thấy cắm đầu đi một mạch xuống lầu, không hề nghe thấy âm thanh đổ vỡ kinh hoàng vang lên từ trong thư phòng.""",
"""Cậu trở về phòng ngủ, bắt đầu thu dọn hành lý mình vừa mới mang về sắp xếp xong.""",
"""“Tiểu Lãng, con làm sao thế này?” Mẹ Giang bàng hoàng nhìn con trai mình.""",
"""Giang Minh Lãng im lặng không nói, một lúc sau mới đè thấp giọng nói với mẹ Giang: “Mẹ, con muốn đến trường ở.”""",
"""Mẹ Giang sững sờ: “Được, được rồi, con muốn làm gì mẹ đều đồng ý, nhưng chuyện này phải đợi mẹ xin phép Phó tiên sinh đã rồi mới——”""",
"""“Con sẽ không hỏi anh ta.” Giang Minh Lãng lần đầu tiên trong đời cãi lời mẹ Giang, cậu nhanh chóng thu dọn xong hành lý, quyết định trở lại ký túc xá của đội tuyển tỉnh ở tạm vài ngày.""",
"""Quả bóng rổ quý giá kia bị cậu nhẫn tâm lấy ra khỏi túi đồ.""",
"""Khi cậu kéo hành lý bước đến bên cạnh hồ nước, cậu nhận được cuộc gọi từ Phó Vân Xuyên.""",
"""“Quay lại,” Trước khung cửa kính sát đất ở tầng hai, Phó Vân Xuyên giơ điện thoại, gắt gao nhìn chằm chằm vào Giang Minh Lãng dưới lầu: “Ngay lập tức.”""",
"""Giang Minh Lãng đột ngột quay đầu lại, từ dưới ngước mắt nhìn lên hướng của anh: “Phó tiên sinh, cảm ơn anh suốt thời gian qua đã chăm sóc, sau này tôi sẽ không gặp lại anh nữa.”""",
"""Giang Minh Lãng không thể nhìn thấy biểu cảm của Phó Vân Xuyên lúc này đáng sợ đến mức nào, cậu nói xong liền quay người, tiếp tục sải bước đi ra ngoài cổng trang viên.""",
"""“Ha ha,” Đầu dây bên kia truyền đến tiếng cười rợn người của Phó Vân Xuyên: “Giang Minh Lãng, cậu có thể đi, nhưng chỉ cần cậu bước chân rời khỏi đây, tôi có thể cắt đứt toàn bộ chi phí điều trị cho ông ngoại cậu bất cứ lúc nào.”""",
"""Bàn chân vừa bước ra của Giang Minh Lãng khựng lại, cậu bỗng ngoắt người quay lại, một lần nữa nhìn về hướng Phó Vân Xuyên.""",
"""“Tôi trước giờ chưa bao giờ là người tốt cả, điều này, cậu nhớ cho kỹ.” Phó Vân Xuyên nói với tốc độ chậm rãi, nơi đáy mắt cuộn trào dục vọng chiếm đoạt ngập trời.""",
"""-""",
"""Đêm khuya, Giang Minh Lãng tránh mặt mẹ Giang, một mình bước vào phòng ngủ của Phó Vân Xuyên.""",
"""“Cởi quần áo, tắm rửa, lên giường.” Phó Vân Xuyên quay lưng về phía cậu, lạnh lùng ra lệnh: “Sau này mỗi một buổi tối cậu đều phải nằm trên giường của tôi đúng giờ.”""",
"""“Sau này mọi lịch trình của cậu đều phải báo cáo với tôi, thời gian ngoài lịch trình, cậu đều phải ngoan ngoãn ở lại trong trang viên này.”""",
"""“Bản hợp đồng tôi sẽ để mãi ở đầu giường phía bên cậu, bây giờ cậu không ký cũng được, tôi có thừa kiên nhẫn.”""",
"""Nói xong, Phó Vân Xuyên hơi nghiêng đầu, hỏi ngược lại: “Đã hiểu chưa.”""",
"""Giang Minh Lãng không thèm nhìn anh, chẳng nói nửa lời bước thẳng vào phòng tắm, chẳng mấy chốc tiếng nước chảy đã vang lên róc rách.""",
"""Lên giường, nằm xuống, quay lưng lại, nhắm mắt, một chuỗi động tác của Giang Minh Lãng liền mạch dứt khoát, không thèm bố thí một ánh mắt thừa thãi nào cho Phó Vân Xuyên bên cạnh.""",
"""Vốn tưởng Phó Vân Xuyên lại dùng cái dáng vẻ dọa chết người kia để uy hiếp cậu, nhưng chẳng bao lâu sau, cậu liền nghe thấy bên cạnh truyền đến tiếng thở mệt mỏi và đều đặn của Phó Vân Xuyên.""",
"""Giang Minh Lãng bất mãn trở mình, cố ý gây ra tiếng động thật lớn, nhưng vẫn không làm Phó Vân Xuyên thức giấc, về sau chính cậu cũng không chống đỡ nổi nữa, mí mắt trĩu nặng rồi thiếp đi.""",
"""Sáng hôm sau khi tỉnh dậy thì Phó Vân Xuyên lại biến mất tăm.""",
"""Hôm nay là Chủ nhật, Giang Minh Lãng chẳng cần đi đâu cả, chiểu theo lời của Phó Vân Xuyên thì cả ngày cậu đều phải ở lỳ trong trang viên.""",
"""Giang Minh Lãng nằm dang tay dang chân hình chữ Đại trên giường, lặng lẽ nhìn trần nhà, im lìm tự chữa lành vết thương lòng đầu tiên trong suốt cả cuộc đời làm cún của mình.""",
"""Cuối cùng cậu cũng hiểu vì sao con Golden đực ở lớp bên cạnh lúc nào cũng vì một câu nói bâng quơ của cô cún Bichon cái mà ủ rũ rầu rĩ cả ngày.""",
"""Cái mùi vị này đúng là chẳng dễ chịu chút nào.""",
"""【Diễn biến cốt truyện này quá nằm ngoài dự liệu của bản cầu rồi.】 Hệ thống lúc này nhảy tót ra, chậc chậc cảm thán.""",
"""Thấy Giang Minh Lãng không thèm đoái hoài gì đến mình, nó đành cụt hứng tàng hình trở lại.""",
"""Giang Minh Lãng suy nghĩ cả buổi sáng vẫn không tài nào hiểu nổi, Phó Vân Xuyên bao nuôi cậu rốt cuộc là vì cái gì chứ?""",
"""Rốt cuộc là mắt xích nào đã xảy ra sai sót mới dẫn đến cục diện như hiện tại? Đã không thích cậu, vậy tại sao nhất định phải trói chặt cậu ở bên cạnh mình?""",
"""Buổi trưa xuống lầu ăn bữa cơm, sau đó lại quay về phòng tiếp tục suy ngẫm về kiếp chó, mắt thấy mặt trời ngoài cửa sổ sắp lặn xuống núi, Giang Minh Lãng cảm thấy một luồng bực bội xao động mãnh liệt đang chạy loạn khắp cơ thể.""",
"""Mỗi ngày cậu đều cần phải vận động giải tỏa thể lực với cường độ cao, thế nhưng cả ngày hôm nay cậu chỉ nằm lì trên giường.""",
"""Cậu ngồi bật dậy trên giường, toàn bộ cơ bắp trên người ngứa ngáy khó chịu.""",
"""Phải làm chút gì đó thôi.""",
"""Cậu nghĩ.""",
"""Đúng lúc này, ánh mắt cậu vô tình lướt qua chiếc ghế sofa bọc da thật cách đó không xa, một xung động nguyên thủy liền xâm chiếm lý trí cậu.""",
"""Cậu đã rất lâu rồi không được mài răng.""",
"""Là Phó Vân Xuyên ép cậu đấy nhé.""",
"""“Gâu!——”"""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_027\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_027\translation.md'

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

print("Saved ch_027 successfully!")
