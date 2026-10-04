import re
import os

paras_trans = [
"""---
title: Chương 37: Trang 37
---""",
"""Giang Minh Lãng sững sờ đứng chôn chân tại chỗ, nhất thời chẳng biết nên phản ứng ra sao.""",
"""Cậu rảo bước nhanh ra khỏi phòng, cầm điện thoại bấm gọi lại cho Phó Vân Xuyên, muốn hỏi anh vì sao đột nhiên lại làm như vậy, nhưng đầu dây bên kia liên tục báo máy bận tắt nguồn.""",
"""Một dự cảm chẳng lành dâng lên trong lòng, cậu tìm số điện thoại của trợ lý rồi bấm gọi qua.""",
"""“Xin chào, Giang tiên sinh.” Điện thoại được kết nối.""",
"""“Alo, trợ lý Trần, tôi muốn tìm Phó——” Giang Minh Lãng sốt ruột định hỏi xem Phó Vân Xuyên đang ở đâu thì bị đối phương cắt ngang.""",
"""“Ngại quá, ý của Phó tổng là cậu không cần tìm ngài ấy nữa đâu, có bất kỳ vấn đề gì cậu đều có thể trao đổi với tôi.”""",
"""“Cái gì cơ?” Vẻ mặt Giang Minh Lãng sững sờ thảng thốt.""",
"""“Đúng lúc tôi cũng cần liên hệ với cậu, theo ý của Phó tổng, chiếc thẻ ngân hàng đưa cho cậu trước đây cậu vẫn có thể tiếp tục sử dụng bình thường, số tiền quẹt không giới hạn. Ngoài ra ngài ấy có nhắc tới chuyện hợp đồng, bởi vì cậu chưa từng ký tên nên hợp đồng không có hiệu lực.”""",
"""“Tôi muốn nói chuyện với anh ấy.” Giang Minh Lãng bình tĩnh nói.""",
"""“Thành thật xin lỗi, Phó tổng đang bận.” Trợ lý im lặng trong giây lát.""",
"""“Tôi hiểu rồi, cảm ơn anh.” Giang Minh Lãng buông điện thoại xuống, cúp máy.""",
"""Giang Minh Lãng có ngốc đến đâu thì cũng không thể không hiểu được ý tứ của Phó Vân Xuyên.""",
"""Chuyện này rốt cuộc là sao chứ?""",
"""Cậu không hiểu nổi.""",
"""“Con về rồi đấy à? Mau lại đây giúp mẹ thu dọn đồ đạc một tay nào.” Mẹ Giang giữa lúc bận rộn ngẩng đầu nhìn Giang Minh Lãng vừa trở về phòng, cất tiếng gọi.""",
"""Giang Minh Lãng im thin thít bước tới bên cạnh mẹ Giang, giúp bà thu dọn quần áo.""",
"""Nhận ra sự bất thường, mẹ Giang dừng động tác trên tay lại, quay đầu nhìn đứa con trai đang mất hồn mất vía bên cạnh.""",
"""“Tiểu Lãng, tình cảm của người giàu có không thể tin là thật được đâu con.” Bà thở dài một tiếng, ngay từ đầu khi phát hiện ra manh nha giữa hai người, bà đã biết con trai mình cuối cùng sẽ phải chịu tổn thương, hệt như chính bản thân bà thời còn trẻ tuổi.""",
"""“Lại đây Tiểu Lãng, để mẹ ôm con một cái nào.” Mẹ Giang dang rộng hai cánh tay, nói với Giang Minh Lãng.""",
"""Giang Minh Lãng nhìn hành động xa lạ đầy ấm áp này đối với mình, sống mũi bỗng cay xè, cậu nhào tới ôm chầm lấy mẹ.""",
"""“Tiểu Lãng, đừng đau lòng, con phải nhớ rằng trên thế giới này mẹ và ông ngoại sẽ mãi mãi yêu thương con.” Mẹ Giang dịu dàng xoa đầu cậu, ân cần an ủi.""",
"""“Cảm ơn mẹ.” Giang Minh Lãng nghẹn ngào cất tiếng.""",
"""Hai mẹ con cuối cùng vào sáng sớm ngày hôm sau đã dọn dẹp hành lý rời khỏi tòa trang viên này.""",
"""Bởi vì ông ngoại của Giang Minh Lãng cần phải ở lại bệnh viện theo dõi thêm vài ngày nữa mới có thể làm thủ tục xuất viện, thế nên hai mẹ con đành phải ở tạm trong bệnh viện để chờ ông ngoại ra viện.""",
"""Chớp mắt một cái, kể từ ngày hệ thống thông báo cậu nên rời đi đến nay đã trôi qua tròn một tuần lễ.""",
"""Trong suốt khoảng thời gian này, Giang Minh Lãng đã nhiều lần bấm gọi vào số máy của Phó Vân Xuyên, nhưng lần nào cũng không có người bắt máy.""",
"""Ngồi trên ghế sofa trong phòng bệnh, Giang Minh Lãng mò quả cầu ánh sáng từ trong túi quần ra, ánh mắt có chút thất thần.""",
"""Có lẽ cậu thực sự nên rời đi rồi.""",
"""“Bố nhìn xem, Tiểu Lãng nhà mình đoạt cúp vô địch trong giải đấu này đấy.” Ở phía bên kia, mẹ Giang đang cầm điện thoại mở lại video trận chung kết bóng rổ cho ông ngoại xem.""",
"""Ông lão ngoài bảy mươi tuổi cười rạng rỡ với những nếp nhăn xô lại trên mặt, liên tục gật đầu tấm tắc khen: “Tốt, tốt lắm!”""",
"""Trong lúc thất thần, quả cầu ánh sáng trong tay vì bị cậu vô tình chạm phải vị trí nào đó mà bỗng nhiên phát sáng rực rỡ.""",
"""Rất nhanh sau đó, hệ thống đã hiện hình trong thần thức của cậu.""",
"""【Sắp đi rồi hả Alaska?】 Hệ thống ngáp dài một cái hỏi.""",
"""Giang Minh Lãng lúc này mới sực tỉnh nhận ra mình vừa bấm sáng quả cầu: “Hả? Tôi...”""",
"""【Ngươi rốt cuộc còn do dự cái gì nữa chứ, chẳng lẽ ngươi không muốn quay về Học viện Gâu Gâu nữa sao? Lúc mới đến ngươi từng nói với ta rằng ngươi nhất định phải hoàn thành nhiệm vụ để quay về tự mình chọn chủ nhân cơ mà.】 Hệ thống khó hiểu hỏi.""",
"""“...” Giang Minh Lãng chính bản thân cũng không hiểu nổi, chỉ là hễ nghĩ đến chuyện phải rời đi, gương mặt của Phó Vân Xuyên lại hiện rõ mồn một trong tâm trí cậu.""",
"""“Tôi có một câu hỏi, nếu tôi rời đi rồi thì thân phận Giang Minh Lãng này sẽ ra sao?” Cậu hỏi.""",
"""【Nhân vật Giang Minh Lãng này là do ngươi đến nên hệ thống mới cưỡng chế cài cắm vào, nếu ngươi rời đi, Giang Minh Lãng sẽ biến mất hoàn toàn, nói một cách đơn giản là cậu ta sẽ tan biến khỏi ký ức của tất cả mọi người.】""",
"""Giang Minh Lãng nghe vậy liền ngước mắt nhìn về phía người trên giường bệnh.""",
"""Hồi lâu sau, cuối cùng cậu cũng hạ quyết tâm: “Tiểu Cầu, tôi không muốn đi nữa.”""",
"""【Cái gì cơ?!】 Quả cầu ánh sáng nổ tung, sốt sắng lượn vòng quanh đầu Giang Minh Lãng: 【Ngươi nghiêm túc đấy chứ?】""",
"""“Ừm,” Giang Minh Lãng gật đầu: “Tôi ở nơi này, đã giao phối rồi.”""",
"""Trong nhận thức của Giang Minh Lãng, ý nghĩa của việc giao phối vô cùng trọng đại.""",
"""Điều quan trọng nhất là suốt mấy ngày qua cậu đã nghĩ thông suốt rồi, ở nơi này, cậu đã có được tất cả những thứ mà mình hằng mong ước.""",
"""Quả cầu ánh sáng trên không trung nổ tung thành một dấu chấm than: 【Ngươi... ngươi... ngươi thế mà lại cùng nhân vật phản diện...】""",
"""【Ngươi nghĩ kỹ rồi chứ, một khi đã quyết định ở lại thì sẽ không còn cơ hội hối hận đâu đấy.】""",
"""“Ừm, tôi nghĩ kỹ rồi.”""",
"""【Được rồi, ta sẽ về báo cáo lại với ngài sĩ quan chấp hành, ngài ấy chắc hẳn sẽ đến gặp ngươi lần cuối cùng.】""",
"""“Được, cảm ơn ngươi nhé Tiểu Cầu.” Giang Minh Lãng mỉm cười.""",
"""【Đã bảo đừng gọi bản hệ thống là Tiểu Cầu rồi cơ mà... Ta đi đây, nhiệm vụ bên này của ngươi đã kết thúc, ta phải đi nhận nhiệm vụ tiếp theo rồi.】""",
"""Quả cầu ánh sáng ngượng ngùng bay lượn một vòng, tựa như xấu hổ không muốn nói lời từ biệt, cuối cùng dưới lời chào tạm biệt nhiệt tình của Giang Minh Lãng liền biến mất khỏi thần thức.""",
"""Bác sĩ điều trị chính của ông ngoại thông báo ngày mai ông cụ đã có thể về nhà, thế là mẹ Giang đã mua xong vé xe về quê và hoàn tất mọi thủ tục xuất viện.""",
"""Ngày hôm sau, Giang Minh Lãng tay xách nách mang hành lý lớn nhỏ, mẹ Giang đẩy xe lăn chở ông ngoại, cả ba người đứng trên sân ga chờ tàu hỏa.""",
"""Thấy Giang Minh Lãng liên tục thẫn thờ mất hồn, mẹ Giang ôn tồn nói: “Tiểu Lãng à, chỉ là về quê một thời gian thôi mà, sang năm con vẫn còn phải lên đây đi học tiếp cơ mà.”""",
"""Giang Minh Lãng khẽ gật đầu, phía xa xa đoàn tàu hỏa đã từ từ tiến vào sân ga.""",
"""Đúng lúc cả ba người chuẩn bị bước lên tàu hỏa thì chuông điện thoại của Giang Minh Lãng bỗng reo vang.""",
"""Màn hình hiển thị cuộc gọi đến từ trợ lý Trần.""",
"""“Alo?”""",
"""“Alo, Giang tiên sinh, thật lòng xin lỗi vì đã làm phiền cậu, nhưng tôi thực sự hết cách rồi,” Đầu dây bên kia truyền đến giọng nói cuống cuồng lo lắng tột độ của trợ lý: “Sắp có một cuộc họp đa quốc gia quan trọng diễn ra, thế nhưng hiện tại Phó tổng đã mất tích rồi, điện thoại tắt máy, bên cạnh không mang theo bất kỳ ai cả.”""",
"""Giang Minh Lãng khựng lại bước chân: “Tôi cũng không biết anh ấy đang ở đâu, anh ấy chưa từng nghe điện thoại của tôi.”""",
"""“Cách đây không lâu Phó tổng từng giao cho tôi một bản di chúc, bảo tôi tìm luật sư xử lý, người thụ hưởng duy nhất trong bản di chúc đó chính là cậu,”""",
"""Trợ lý Trần dồn dập nói:""",
"""“Hôm qua ngài ấy còn đến tòa án gặp Phó phu nhân một lần.”""",
"""“Lúc đó tôi đã cảm thấy có điều bất thường nhưng không nghĩ sâu xa, hiện tại ngài ấy bặt vô âm tín, tôi lo lắng——”""",
"""Chiếc điện thoại rơi “choảng” một tiếng thật mạnh xuống nền đất, đầu óc Giang Minh Lãng ong lên một tiếng dữ dội, cậu vứt bỏ toàn bộ hành lý trong tay, quay người điên cuồng lao như bay.""",
"""Tiếng gọi với theo đầy hoảng hốt của mẹ Giang bị cậu bỏ lại xa tít tắp phía sau lưng, cậu bất chấp tất cả lao ra khỏi nhà ga, chặn ngay một chiếc taxi phóng thẳng về phía trang viên.""",
"""Cậu không biết Phó Vân Xuyên đang ở đâu, nhưng trực giác mách bảo cho cậu biết rằng Phó Vân Xuyên nhất định đang ở đó!""",
"""Bước xuống xe, Giang Minh Lãng chạy thục mạng vào trong trang viên, phát hiện bên trong vắng ngắt không một bóng người, thậm chí ngay cả phòng bảo vệ trông cổng cũng trống trơn, toàn bộ trang viên chìm trong sự tĩnh mịch chết chóc, không có lấy nửa phần sinh khí.""",
"""Cánh cửa lớn của tòa nhà chính đang mở toang, Giang Minh Lãng chạy một mạch thông suốt không gặp chút trở ngại nào, cậu trước tiên tìm phòng ngủ của Phó Vân Xuyên, rồi lại tìm thư phòng, cuối cùng gần như lùng sục khắp mọi căn phòng cũng không tìm thấy bóng dáng Phó Vân Xuyên đâu.""",
"""Một nỗi bất an kinh hoàng siết chặt lấy lồng ngực Giang Minh Lãng, cậu thở hổn hển từng ngụm lớn, khản cả giọng gọi từng tiếng từng tiếng tên của Phó Vân Xuyên.""",
"""Đúng lúc này, một tia ý nghĩ bỗng lóe lên trong đầu cậu.""",
"""Không kịp suy nghĩ nhiều, Giang Minh Lãng lao thẳng lên tầng cao nhất.""",
"""Vừa bước chân vào khu vực hồ bơi, làn hơi nước buốt lạnh lập tức xộc thẳng vào khoang mũi cậu.""",
"""Tông màu xám đậm u ám chết chóc đè nén khiến Giang Minh Lãng gần như nghẹt thở.""",
"""Cậu nhìn về phía làn nước cách đó không xa, mặt nước phẳng lặng tựa như một vũng nước tù đọng chết chóc.""",
"""“Phó Vân Xuyên! Phó Vân Xuyên——”""",
"""Giang Minh Lãng lao thục mạng tới mép hồ bơi, gào to tên của Phó Vân Xuyên.""",
"""Quả nhiên không ngoài dự đoán, dưới đáy làn nước sâu trong vắt, cậu nhìn thấy một người đàn ông đang chìm sâu dưới đáy nước.""",
"""Cậu nhớ lại lần trước, Phó Vân Xuyên cũng từng gục đầu lặn sâu vào trong nước như thế này, khi ấy cậu còn ngỡ rằng Phó Vân Xuyên đang tự sát.""",
"""“Phó Vân Xuyên!” Giang Minh Lãng đỏ hoe mắt gầm lên một tiếng, thế nhưng người dưới đáy nước không có lấy nửa phần phản ứng.""",
"""“Tõm——” Một cột nước khổng lồ nổ tung trên mặt nước phẳng lặng, Giang Minh Lãng lao thẳng đầu xuống nước, làn nước lạnh buốt thấu xương lập tức quấn chặt lấy người cậu kín kẽ không một kẽ hở.""",
"""Ôm chặt lấy eo Phó Vân Xuyên, Giang Minh Lãng dùng hết sức bình sinh đưa người trồi lên khỏi mặt nước.""",
"""“Phó tiên sinh, anh tỉnh lại đi!” Giang Minh Lãng liên tục vỗ vào mặt Phó Vân Xuyên, sốt ruột gào khóc gọi lớn.""",
"""Phó Vân Xuyên trên người vẫn mặc bộ âu phục cao cấp may đo riêng, ngay cả đôi găng tay da cũng được đeo ngay ngắn trên tay, nếu không phải khuôn mặt anh trắng bệch chỉ còn toàn tử khí, thì tất cả đều hệt như mọi ngày bình thường.""",
"""Giang Minh Lãng chiểu theo phương pháp đã học, không ngừng thực hiện các thao tác hô hấp nhân tạo cho Phó Vân Xuyên.""",
"""Cậu hết lần này đến lần khác gọi tên Phó Vân Xuyên, nhưng đáp lại cậu chỉ là sự im lặng chết chóc lạnh lẽo.""",
"""Tại sao Phó Vân Xuyên lại làm như vậy chứ?""",
"""Giang Minh Lãng nghĩ mãi chẳng thông, rõ ràng anh đã có thể tự do tận hưởng tương lai tươi sáng của mình rồi cơ mà?""",
"""Giang Minh Lãng nhìn khuôn mặt Phó Vân Xuyên, đau đớn xót xa nghĩ bụng.""",
"""Đúng lúc này, khóe mắt cậu thoáng thấy bàn tay của Phó Vân Xuyên.""",
"""Cậu đột ngột giật phăng đôi găng tay của Phó Vân Xuyên ra, sau đó siết chặt lấy bàn tay trần của đối phương.""",
"""“Phó tiên sinh, bây giờ anh đã chạm vào người tôi rồi đấy,” Giang Minh Lãng căng thẳng nhìn phản ứng của Phó Vân Xuyên: “Chẳng lẽ anh không muốn biết xem liệu tôi có giống như chú cún con kia và Phó Vân Hi hay không sao?”""",
"""Thời gian từng phút từng giây trôi qua, ngay khoảnh khắc Giang Minh Lãng sắp sửa rơi vào tuyệt vọng cùng cực thì ngón tay của Phó Vân Xuyên khẽ giật giật một cái.""",
"""Trông thấy mí mắt đang nhắm nghiền của Phó Vân Xuyên khẽ rung rinh, Giang Minh Lãng lập tức lay mạnh người anh.""",
"""Ánh mắt đầu tiên khi Phó Vân Xuyên mở mắt ra chính là khuôn mặt của Giang Minh Lãng: “Giang Minh Lãng?” Giọng anh khàn đặc thốt lên.""",
"""Nghe thấy Phó Vân Xuyên cất tiếng nói, Giang Minh Lãng không kìm nén nổi nữa, cậu nhào tới ôm chặt cứng lấy anh, bật khóc nức nở: “Dọa chết tôi rồi, tôi cứ tưởng anh đã chết rồi cơ chứ!”""",
"""Nhiệt độ cơ thể nóng rực trên người Giang Minh Lãng không ngừng truyền sang, Phó Vân Xuyên mới bàng hoàng ý thức được rằng cảnh tượng trước mắt là có thật.""",
"""“Không phải cậu... đã đi rồi sao?” Ý thức của anh vẫn còn mơ màng."""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_037\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_037\translation.md'

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

print("Saved ch_037 successfully!")
