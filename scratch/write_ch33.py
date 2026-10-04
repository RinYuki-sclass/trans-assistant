import re
import os

paras_trans = [
"""---
title: Chương 33: Trang 33
---""",
"""Trong thế giới của cậu, chưa từng có khái niệm về đạo sĩ hay số mệnh.""",
"""Cậu không tài nào hiểu nổi tại sao cùng là con ruột, mà Phó Vân Xuyên lại vì cái lý do hoang đường nực cười đến thế mà không nhận được lấy nửa phần yêu thương thiên vị.""",
"""Thảo nào, thảo nào ngay cả chính bản thân Phó Vân Xuyên cũng hoài nghi mình là tai ương gieo rắc bất hạnh, việc anh luôn đeo găng tay chẳng phải đã nói lên nỗi sợ hãi sâu kín trong lòng anh hay sao?""",
"""Trong toàn bộ chuyện này, cậu chỉ nhìn thấy sự ác ý đầy hiển nhiên của tất cả mọi người bao gồm cả Phó Ngôn trút lên đầu Phó Vân Xuyên, chỉ vì một câu nói buột miệng của một gã đạo sĩ.""",
"""“Lần đầu tiên tôi biết chuyện này, tôi cũng từng nảy sinh lòng thương hại đối với Phó Vân Xuyên.” Phó Ngôn đột nhiên đổi giọng: “Tôi cũng hiểu, bố mẹ thực sự rất yêu thương anh Vân Hi, nhận nuôi tôi cũng là vì tôi trông rất giống anh Vân Hi.”""",
"""“Nhưng bọn họ quả thực đã trở thành cha mẹ của tôi, nuôi nấng tôi, yêu thương tôi, cho tôi một mái ấm gia đình, thế nên tôi sẵn sàng vì bọn họ mà làm bất cứ điều gì.”""",
"""“Sau khi biết Phó Vân Xuyên ngấm ngầm giám sát tôi, tôi đã cố ý điều tra tiếp cận anh ấy, thậm chí muốn lợi dụng tình cảm đặc biệt anh ấy dành cho tôi để hóa giải mối thù hận đối với Phó gia. Đáng tiếc thay,” Giọng Phó Ngôn ngừng lại một nhịp, nhìn đăm đăm vào Giang Minh Lãng: “Chính vì có cậu xuất hiện, kế hoạch của tôi đã thất bại.”""",
"""Giang Minh Lãng bỗng đập bàn đứng phắt dậy, lông tơ toàn thân dựng đứng cả lên: “Cho nên từ đầu chí cuối, cậu đều là cố ý?”""",
"""Trong cốt truyện gốc, Phó Ngôn ngay từ đầu đã bày tỏ sự lương thiện và ấm áp vô bờ bến với Phó Vân Xuyên, cậu ta trao cho Phó Vân Xuyên sự quan tâm săn sóc, mỗi lần đều xuất hiện đúng thời điểm để an ủi tâm hồn đầy thương tích của anh.""",
"""Thế nhưng tất cả những điều đó lại đều là toan tính có chủ đích, thứ tình thương và sự thừa nhận duy nhất mà Phó Vân Xuyên ngỡ rằng mình có được, hóa ra toàn bộ chỉ là dối trá!""",
"""“Các người xấu xa quá chừng!” Giang Minh Lãng chỉ tay vào mặt Phó Ngôn, giận dữ quát lớn.""",
"""“Xin lỗi nhé, da thịt tóc tai đều do cha mẹ ban cho, anh ấy không nên làm tổn thương bố mẹ.” Phó Ngôn nói bằng giọng điệu đầy vẻ lẽ phải danh chính ngôn thuận.""",
"""Giang Minh Lãng chẳng còn muốn nói thêm nửa lời nào với Phó Ngôn nữa, khoảnh khắc này cậu chỉ cảm thấy một ngọn lửa phẫn nộ ngùn ngụt bốc cháy trong lồng ngực, nhưng tay chân thì lạnh buốt thấu tận tâm can.""",
"""Cậu sải bước đi ra ngoài, không thèm quay đầu lại.""",
"""“Giang Minh Lãng,” Phó Ngôn gọi với theo sau lưng cậu: “Phiền cậu về nói với Phó Vân Xuyên một tiếng, bố hiện tại bệnh rất nặng rồi, bố mẹ đều muốn được gặp anh ấy lần cuối.”""",
"""Bước chân Giang Minh Lãng khựng lại trong giây lát, rồi nhanh chóng rời khỏi thư viện.""",
"""Cậu cúi gầm mặt bước đi trong khuôn viên trường học, bất giác xâu chuỗi lại toàn bộ quá khứ và kết cục của Phó Vân Xuyên trong tiểu thuyết lẫn ngoài đời thực.""",
"""Ngột ngạt, đau đớn, nghẹt thở đến cùng cực.""",
"""Đang đi, cậu bỗng sải bước chạy thục mạng, cậu chạy như điên xông ra khỏi cổng trường, lao thẳng đến vị trí xe của Phó Vân Xuyên đang chờ đón cậu.""",
"""Cậu mở toang cửa xe rồi nhào thẳng vào bên trong, ôm chầm lấy Phó Vân Xuyên đang ngồi đợi ở hàng ghế sau vào lòng.""",
"""Hơi thở nóng rực dồn dập phả vào một bên cổ Phó Vân Xuyên, anh nhíu mày nhìn tấm lưng Giang Minh Lãng, hỏi: “Cậu làm sao thế?”""",
"""“Anh rõ ràng đã nhận được giấy báo trúng tuyển rồi, có thể rời xa bọn họ rồi, tại sao lại phải đồng ý gánh tội thay cho Phó Vân Hi chứ?” Giang Minh Lãng nghẹn ngào hỏi với giọng mũi trầm đục.""",
"""Nếu như năm đó Phó Vân Xuyên không đồng ý, vậy thì cuộc đời của anh liệu có bước sang một ngã rẽ tràn ngập ánh sáng hay không?""",
"""“Sao cậu lại biết chuyện này?” Ánh mắt Phó Vân Xuyên bỗng chốc tối sầm lại, liếc mắt nhìn về phía ghế lái.""",
"""Bác tài xế ở hàng ghế trước hoảng hốt cuống cuồng xuống xe, tự giác đóng chặt cửa lại.""",
"""“Tôi xin lỗi, tôi đã đi hỏi Phó Ngôn.” Giang Minh Lãng thành thật thú nhận.""",
"""Phó Vân Xuyên im lặng hồi lâu không nói một lời, cả khoang xe chìm vào sự tĩnh lặng chết chóc kéo dài.""",
"""“Thực ra năm đó tôi không ngờ bọn họ lại hạ mình cầu xin tôi đi gánh tội thay cho anh ta,” Phó Vân Xuyên đột nhiên bật cười tự giễu, phá vỡ bầu không khí im lìm:""",
"""“Bọn họ không mở lời xin xỏ, khéo đến cuối cùng tôi cũng tự nguyện đi ngồi tù thay cho Phó Vân Hi.”""",
"""Trong căn gác xép u tối năm xưa, hình ảnh thiếu niên sạch sẽ ngược sáng vươn tay về phía anh đã trở thành một trong số những ký ức tươi đẹp hiếm hoi ít ỏi suốt cả cuộc đời Phó Vân Xuyên.""",
"""Khi ấy, anh chỉ từng nhận được hai lần thiện ý thuần khiết không toan tính: một lần đến từ chú cún con lang thang ngoài ngõ, và một lần đến từ Phó Vân Hi.""",
"""“Chẳng có gì to tát cả, coi như tôi trả lại ơn sinh thành cho bọn họ.”""",
"""Phó Vân Xuyên vừa nói dứt lời, ánh mắt lại dần dần lạnh lẽo như băng giá:""",
"""“Nhưng những gì bọn họ nợ tôi, tôi cũng sẽ đòi lại không thiếu một đồng một cắc.”""",
"""Nghe đến đây, cánh tay Giang Minh Lãng đang ôm lấy anh càng siết chặt hơn:""",
"""“Phó tiên sinh, tôi đau lòng quá.”""",
"""Phó Vân Xuyên thực chất không hề hay biết rằng những ác ý đổ lên người anh còn nhiều hơn gấp bội so với những gì anh tưởng tượng, mà tất cả những điều tàn nhẫn ấy đều bị Giang Minh Lãng nhìn thấu tận chân tơ kẽ tóc.""",
"""Nghĩ đến kết cục của Phó Vân Xuyên, trong lòng Giang Minh Lãng trào dâng một khát vọng mãnh liệt chưa từng có: Cậu muốn xoay chuyển nó, cậu muốn Phó Vân Xuyên có được một tương lai xán lạn rực rỡ ánh mặt trời.""",
"""Phó Vân Xuyên tuyệt đối không đáng phải nhận lấy cái kết cục bi thảm đó.""",
"""Bộ não Giang Minh Lãng vận hành hết công suất, cuối cùng đi đến một quyết định dứt khoát.""",
"""Nếu dự đoán và kế hoạch của cậu thất bại, cậu sẽ dắt Phó Vân Xuyên bỏ trốn, bất luận thế nào đi nữa, viện tâm thần tuyệt đối không thể là chốn dung thân cuối đời của Phó Vân Xuyên.""",
"""Cảm xúc xa lạ chi phối khả năng phán đoán của Phó Vân Xuyên, anh không tài nào hiểu nổi vì cớ gì Giang Minh Lãng lại nảy sinh cảm xúc đau buồn đau xót đến thế.""",
"""Chẳng lẽ là vì chính anh sao?""",
"""Thế nhưng tại sao cậu nhất định phải biết cho bằng được chân tướng, tại sao lại tỏ ra để tâm quan tâm đến anh như vậy?""",
"""“Tôi thích anh.” Những lời Giang Minh Lãng nói với anh cách đây không lâu lại văng vẳng bên tai.""",
"""Một giả thuyết vừa mới manh nha hình thành trong đầu liền bị anh lạnh lùng bóp nghẹt.""",
"""Làm sao có thể có người thực sự thích anh cho được?""",
"""Cả cuộc đời này anh vì cái thứ gọi là “thích” mà làm những chuyện ngu xuẩn đã quá nhiều rồi.""",
"""Bất kể là vì muốn thu hút sự chú ý của vợ chồng Phó gia mà cố tình đánh nhau gây chuyện, thi đứng bét bảng; hay là giấu giếm bọn họ nộp đơn thi vào trường kinh doanh hàng đầu, ôm mộng tưởng có thể đích thân đem giấy báo trúng tuyển về khiến họ phải nhìn anh bằng con mắt khác, chí ít cũng chịu san sẻ chút ánh nhìn lên người anh.""",
"""Mãi về sau khi ở trong tù, anh mới thấu hiểu một điều: Chỉ cần không hy vọng, thì sẽ không bao giờ phải rơi vào tuyệt vọng.""",
"""“Giang Minh Lãng, tôi thích cái dáng vẻ này của cậu.”""",
"""Phó Vân Xuyên bất thình lình lên tiếng, như một phần thưởng khẽ hôn lên vành tai Giang Minh Lãng.""",
"""Vành tai Giang Minh Lãng khẽ giật giật, đôi tai dưới làn da nâu sẫm lập tức nhuộm một lớp ửng hồng: “Cái gì cơ?”""",
"""Hình như cậu lúc nào cũng vì hai chữ thích thốt ra từ miệng Phó Vân Xuyên mà trở nên căng thẳng thẹn thùng.""",
"""Nhận ra Phó Vân Xuyên không phải đang nói thích con người mình, Giang Minh Lãng gạt bỏ nỗi hụt hẫng thoáng qua, lấy lại bình tĩnh rồi buông tay ra.""",
"""“Phó Ngôn nói, bọn họ muốn gặp anh lần cuối.” Cậu vẫn quyết định nói cho Phó Vân Xuyên biết.""",
"""“Vậy sao.” Phó Vân Xuyên vẻ mặt bình thản bấm hạ cửa kính xe, ra hiệu cho tài xế lái xe trở về nhà.""",
"""Không hiểu Phó Vân Xuyên có ý định gì, Giang Minh Lãng thẳng thắn hỏi: “Phó tiên sinh, anh có về không?”""",
"""“...” Khóe môi Phó Vân Xuyên khẽ nhếch: “Có lẽ vậy.” Vài giây sau, anh lại bồi thêm: “Tuần sau.”""",
"""Giang Minh Lãng: “Có thể dẫn tôi đi cùng được không?”""",
"""Phó Vân Xuyên nghe vậy liền liếc nhìn cậu một cái, một thoáng sau mới nói: “Được.”""",
"""Chiếc xe khuất dần dưới chân núi, giữa khoang xe tĩnh mịch, âm thanh thông báo của hệ thống khẽ vang lên.""",
"""【Ting tong, giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 75】""",
"""【Cảnh báo, điểm cốt truyện hắc hóa của phản diện đã mở ra, xin ký chủ hãy kịp thời ngăn chặn giá trị hắc hóa của phản diện tăng vọt trong giai đoạn này!】""",
"""...""",
"""Lời tác giả: Mỗi sáng 9 giờ ra chương mới, hôm nào đổi ngày ra sẽ báo trước moa moa.""",
"""Vô cùng cảm ơn mọi người đã ủng hộ, mình sẽ tiếp tục cố gắng!""",
"""Chương 26: Alaska 26""",
"""Giang Minh Lãng nhận được điện thoại của Phó Vân Xuyên vào một buổi chiều muộn Chủ nhật, lúc đó cậu đang cắm đầu nỗ lực ôn tập cho kỳ thi cuối kỳ sắp diễn ra.""",
"""Cậu như đối mặt với kẻ thù lớn, vội vã chạy xuống lầu, vừa vặn chạm mặt mẹ Giang.""",
"""Nhìn thấy Giang Minh Lãng né tránh mình rảo bước đi về phía xe của Phó Vân Xuyên, mẹ Giang muốn nói lại thôi, cuối cùng vẫn cất bước đi theo sau.""",
"""Trong xe, Phó Vân Xuyên hạ cửa kính xuống, trước lúc xe lăn bánh, mẹ Giang đột nhiên cúi gập người thật sâu trước mặt Phó Vân Xuyên:""",
"""“Phó tiên sinh, tôi xin lỗi ngài.”""",
"""Phó Vân Xuyên nhìn thấy cảnh này liền nhíu chặt mày.""",
"""Xe lăn bánh rời khỏi trang viên, anh quay sang nhìn Giang Minh Lãng bên cạnh: “Cậu có lời nào muốn giải thích không?”""",
"""Giang Minh Lãng ngập ngừng nói: “Nếu có thể, tôi hy vọng anh cho mẹ tôi một cơ hội sửa đổi sai lầm.”""",
"""Tâm trạng của Phó Vân Xuyên dường như càng thêm bực bội u ám, cảnh vật ngoài cửa sổ không ngừng lướt qua, chừng nửa tiếng sau, Giang Minh Lãng đã nhìn thấy cả một quần thể biệt thự xa hoa lộng lẫy hiện ra trước mắt.""",
"""“Không phải là đến bệnh viện sao?”""",
"""Giang Minh Lãng không ngờ bọn họ lại chọn gặp mặt Phó Vân Xuyên ngay tại nhà mình.""",
"""Phó Vân Xuyên nhắm nghiền mắt, giữa hai hàng lông mày toàn là sự bực dọc u uất.""",
"""【Giá trị hắc hóa của phản diện đã tăng lên, hiện tại là: 80】""",
"""“Phó tiên sinh, đến nơi rồi ạ.” Bác tài xế dừng xe lại: “Bên ngoài có người làm của gia đình này đang chờ đón ngài.”""",
"""Giang Minh Lãng nhìn ra ngoài cửa sổ, quả nhiên trông thấy mấy tên vệ sĩ và người giúp việc đang đứng túc trực.""",
"""Phó Vân Xuyên mở mắt, bước xuống xe.""",
"""Giang Minh Lãng bám sát theo sau, chỉ thấy một ông lão ăn vận theo phong cách quản gia tiến lên nghênh đón: “Nhị thiếu gia, tiểu thiếu gia đang đợi ngài ở sân trước.”""",
"""Chỉ thấy Phó Vân Xuyên dùng ánh mắt âm u lạnh lẽo liếc xéo lão quản gia: “Đừng gọi tôi là thiếu gia.”""",
"""Lão quản gia toàn thân lạnh toát, gượng gạo cười gật đầu vâng dạ.""",
"""“Phó tiên sinh, anh thấy trong người không khỏe sao?” Giang Minh Lãng đuổi kịp bước chân Phó Vân Xuyên, ân cần hỏi han.""",
"""Ngay từ lúc ở trên xe, sắc mặt Phó Vân Xuyên đã không bình thường chút nào rồi.""",
"""Thấy Phó Vân Xuyên không trả lời, Giang Minh Lãng đột nhiên cách một lớp găng tay da nắm chặt lấy bàn tay anh: “Đừng sợ, tôi ở bên cạnh anh mà.”""",
"""Phó Vân Xuyên ngẩn người, rũ mi mắt nhìn hai bàn tay đang đan chặt vào nhau, rồi trở tay siết chặt lấy bàn tay của Giang Minh Lãng.""",
"""“Đi sát theo tôi.”""",
"""Phó Vân Xuyên hiển nhiên vô cùng quen thuộc với nơi này, chẳng mấy chốc bọn họ đã nhìn thấy bóng dáng của Phó Ngôn.""",
"""Bên cạnh Phó Ngôn còn có một gã tóc xanh dương, chính là Ngụy Minh.""",
"""“Tôi biết ngài sẽ tới mà.” Phó Ngôn bước lên phía trước nói với Phó Vân Xuyên, dứt lời liền liếc nhìn hai bàn tay đang nắm chặt của hai người: “Bố mẹ đang đợi ngài ở trên lầu.”""",
"""Ngụy Minh bước tới, kéo Phó Ngôn bảo vệ sau lưng mình.""",
"""Phó Ngôn lại nói: “Ngài đã mất ngần ấy năm để bày bố cục diện hiện tại, chắc hẳn hiểu rõ hôm nay bọn họ gặp ngài là vì điều gì.”""",
"""Phó Vân Xuyên mỉm cười: “Vì điều gì, chẳng lẽ là vì muốn cầu xin tôi rủ lòng thương tha mạng, cầu xin tôi chừa cho Phó gia các người một con đường sống sao?”"""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_033\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_033\translation.md'

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

print("Saved ch_033 successfully!")
