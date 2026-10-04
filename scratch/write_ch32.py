import re
import os

paras_trans = [
"""---
title: Chương 32: Trang 32
---""",
"""“Giang Minh Lãng, cậu là người đầu tiên nói rằng tôi sẽ không giết người.”""",
"""Tiếng cười trầm khẽ tràn ra từ kẽ ngón tay, anh cười một lát rồi mới cất lời: “Nếu như cậu có thể xuất hiện sớm hơn một chút.”""",
"""【Giá trị hắc hóa của phản diện đã giảm xuống, hiện tại giá trị hắc hóa là: 85】""",
"""Phó Vân Xuyên nhắm mắt lại, im lặng hồi lâu mới mở lời, ngữ điệu hờ hững tựa như đang kể câu chuyện của một người xa lạ nào đó.""",
"""“Kẻ đã chết năm đó không phải là tên cướp.”""",
"""“Hôm đó trước giờ tan học Phó Vân Hi níu tôi lại, bảo có một gã đàn ông đã quấy rối anh ta suốt mấy tháng trời.”""",
"""Lúc đó tinh thần của Phó Vân Hi rất không bình thường, đưa cho anh xem vô số lá thư người đàn ông kia viết cho mình, từng câu từng chữ đều dơ bẩn chướng mắt khôn cùng.""",
"""Thế nhưng Phó Vân Hi không dám nói cho vợ chồng Phó gia biết, bởi vì nếu làm vậy, bọn họ sẽ phát hiện đứa con trai mà họ hằng tự hào bấy lâu lại là một kẻ biến thái thích đàn ông.""",
"""“Anh ta bảo tôi đi cùng anh ta về nhà, tôi đi theo anh ta bước vào con hẻm nhỏ đó, khi tôi tìm thấy anh ta thì con dao trong tay anh ta đã cắm ngập vào tim gã đàn ông kia rồi.”""",
"""“Anh ta túm chặt lấy tay tôi, van xin tôi cứu anh ta.”""",
"""Nghe đến đây, Giang Minh Lãng chấn động hồi lâu không sao hoàn hồn được, cậu nhìn trừng trừng vào Phó Vân Xuyên, gặng hỏi:""",
"""“Cho nên, anh đã đồng ý?”""",
"""“Không có.”""",
"""“Nhưng mà...” Nếu Phó Vân Xuyên không đồng ý, vậy tại sao cuối cùng người nhận tội lại là anh?""",
"""Giang Minh Lãng muốn hỏi tiếp, nhưng đã bị Phó Vân Xuyên cắt ngang.""",
"""Phó Vân Xuyên đột nhiên đứng dậy, chẳng biết từ lúc nào trên gương mặt anh đã khôi phục lại vẻ lạnh lùng thường ngày: “Ăn xong chưa, đi thôi.”""",
"""Thấy Phó Vân Xuyên cất bước đi ra ngoài, Giang Minh Lãng vội vàng đứng dậy đuổi theo, vừa đi vừa hỏi dồn dập: “Về sau thế nào? Về sau đã xảy ra chuyện gì, tại sao anh không nói sự thật cho bọn họ biết?”""",
"""Giang Minh Lãng không dám tưởng tượng, nếu chân tướng sự việc là như vậy, thì ngần ấy năm qua Phó Vân Xuyên đã phải chịu đựng biết bao nhiêu đau đớn thống khổ.""",
"""Bên ngoài nhà hàng, ánh đèn đường mới vừa bừng sáng, giữa làn gió đêm Phó Vân Xuyên đột nhiên quay đầu lại, kéo Giang Minh Lãng vào lòng, trực tiếp dùng nụ hôn chặn đứng cái miệng đang liến thoắng không ngừng của cậu.""",
"""“Đừng hỏi nữa.” Xác nhận Giang Minh Lãng đã yên tĩnh trở lại, Phó Vân Xuyên mới rời khỏi bờ môi cậu, nhìn trừng trừng vào cậu với giọng nói khàn khàn: “Nếu sau này cậu còn có ý định rời bỏ tôi.”""",
"""Giang Minh Lãng thở hổn hển từng nhịp, đôi mắt nâu tròn xoe ngơ ngác nhìn vào mắt Phó Vân Xuyên.""",
"""“Muốn đi dạo không?” Phó Vân Xuyên đột nhiên hỏi cậu.""",
"""Giang Minh Lãng khó hiểu nhướng mày.""",
"""“Có muốn biến về nguyên hình của cậu không,” Phó Vân Xuyên dùng ánh mắt phác họa từng đường nét ngũ quan anh tuấn bức người của Giang Minh Lãng, nói: “Alaska”. """,
"""Giang Minh Lãng không hiểu vì sao Phó Vân Xuyên lại đột ngột nhắc tới chuyện này, nhưng cậu hiểu Phó Vân Xuyên không muốn tiếp tục nói sâu hơn nữa.""",
"""Quả thực bản thân đã rất lâu rồi không biến về nguyên hình chạy ra ngoài tuần tra, Giang Minh Lãng nhận ra điều đó.""",
"""“Được thôi.” Thế là cậu gật đầu, thấy xung quanh không có ai đi ngang qua liền xoẹt một tiếng biến trở lại thành một chú cún Alaska.""",
"""“Gâu!” Đi thôi!""",
"""Giang Minh Lãng hướng về phía Phó Vân Xuyên đang ngẩn ngơ sủa một tiếng, sải bốn chiếc chân chó to khỏe bắt đầu lon ton chạy về phía trước.""",
"""Phó Vân Xuyên rõ ràng vì tận mắt chứng kiến cảnh tượng này mà hồi lâu vẫn chưa thể lấy lại tinh thần, anh cúi đầu nhìn chú chó béo khổng lồ cao tới tận bắp đùi mình, rồi cất bước đi theo.""",
"""Khi đi ngang qua một cửa hàng tiện lợi, Phó Vân Xuyên đột nhiên dừng bước.""",
"""Lúc từ bên trong bước ra, trên tay Phó Vân Xuyên đang cầm một sợi dây dắt chó.""",
"""Phát hiện Phó Vân Xuyên muốn tròng dây vào cổ mình, Giang Minh Lãng bất mãn sủa gâu một tiếng.""",
"""“Không tròng dây thì mày sẽ bị đội bắt chó tóm đem đi nấu lẩu đấy.” Phó Vân Xuyên dọa nạt cậu.""",
"""Giang Minh Lãng: Rén ngay trong một giây.""",
"""Thế là dưới sự uy hiếp của Phó Vân Xuyên, Giang Minh Lãng đành miễn cưỡng để anh đeo vòng cổ vào cho mình.""",
"""“Ngoan một chút, ngày mai tôi bảo người ta đặt làm riêng cho mày.” Phó Vân Xuyên vừa đeo xong vòng cổ cho Giang Minh Lãng vừa ngập ngừng vươn tay ra, xoa xoa cái đầu to xù đầy lông của chú Alaska.""",
"""“Gâu gâu!”""",
"""Alaska hú lên hai tiếng, rồi lao vút về phía trước.""",
"""Phó Vân Xuyên nắm chặt dây dắt, rảo bước đuổi theo.""",
"""Hai người một mạch từ khu trung tâm thương mại sầm uất nhất thành phố A đi bộ đến công viên, chú cún Alaska ở trong công viên chơi đùa vui vẻ hết nấc với một đàn chó khác.""",
"""Cuối cùng chơi đến mức đi không nổi nữa, phụng phịu không chịu đi bị Phó Vân Xuyên kéo lê từng bước.""",
"""“Mệt rồi à?” Phó Vân Xuyên từ trên cao nhìn xuống nó.""",
"""“Ẳo u...” Đầu chó Alaska gục xuống, bốn chân duỗi thẳng đơ ra đất, trực tiếp từ chối đi bộ, ra hiệu cho Phó Vân Xuyên nghỉ ngơi một lát.""",
"""“Lên đây.”""",
"""Giọng nói của Phó Vân Xuyên từ trên đỉnh đầu truyền xuống, Giang Minh Lãng ngẩng đầu lên, phát hiện Phó Vân Xuyên thế mà lại ngồi xổm xuống, tóm lấy hai chân trước của nó gác lên vai anh, giây tiếp theo, cả người nó đã được bế bổng lên không trung.""",
"""Kích thước của Alaska tuyệt đối được xếp vào hàng ngũ đồ sộ, đứng thẳng lên có thể cao tới tận cổ của Phó Vân Xuyên.""",
"""Khối thịt chó béo múp míp rung rinh theo từng bước chuyển động của Phó Vân Xuyên,""",
"""“Gâu gâu!” Alaska phấn khích sủa vang hai tiếng, bởi vì từ trước đến nay nó chưa từng được ai bế bổng lên như thế này bao giờ.""",
"""Thật kỳ lạ làm sao, cảm giác này.""",
"""Giang Minh Lãng gác hai chân trước lên bờ vai Phó Vân Xuyên, cảm thấy trái tim mình ngưa ngứa tê rần.""",
"""Trước đây nó từng ảo tưởng rằng có một ngày mình cũng sẽ giống như những chú cún nhỏ được chủ nhân ôm gọn vào lòng.""",
"""Mà hiện tại tựa như, tựa như chính nó cũng đã có chủ nhân vậy.""",
"""Không đúng.""",
"""Giang Minh Lãng vội vàng lắc lắc cái đầu chó, xua tan những suy nghĩ thiếu thực tế trong đầu đi.""",
"""Phó Vân Xuyên đâu có thích cậu, cũng sẽ không phải là chủ nhân của cậu.""",
"""Sau khi nhiệm vụ kết thúc, bất kể thành công hay thất bại, cậu đều phải rời đi rồi.""",
"""Lời tác giả:""",
"""Vô cùng cảm ơn mọi người đã ủng hộ, mình sẽ tiếp tục cố gắng!""",
"""Chương 25: Alaska 25""",
"""Kể từ ngày hôm đó, Giang Minh Lãng vô cùng nôn nóng muốn biết chân tướng vụ án năm xưa Phó Vân Xuyên phải ngồi tù.""",
"""Không chỉ đơn thuần vì đó có thể là điểm mấu chốt của nhiệm vụ, mà quan trọng hơn là cậu muốn hiểu rõ quá khứ của Phó Vân Xuyên, muốn biết nỗi đau đớn tột cùng của anh bắt nguồn từ đâu.""",
"""Thế nhưng dưới sự gặng hỏi nhiều lần của cậu, Phó Vân Xuyên chẳng hề hé lộ thêm nửa chữ.""",
"""Bên phía Phó Vân Xuyên không có kết quả, đành phải đi tìm người khác.""",
"""Giang Minh Lãng ngay lập tức nghĩ tới Phó Ngôn.""",
"""Thông qua Phó Ngôn, cậu có cơ hội dò la chân tướng từ vợ chồng Phó gia.""",
"""Thế là hầu như ngày nào sau giờ học cậu cũng đến phòng học của Phó Ngôn tìm cậu ta, học kỳ sắp sửa kết thúc rồi mà cậu chưa một lần đợi được Phó Ngôn xuất hiện.""",
"""Theo nguồn tin vỉa hè, những biến động dữ dội của Phó gia khiến Phó Thành Hồng tức giận công tâm, phải vào phòng cấp cứu suốt đêm, còn Phó Ngôn với tư cách là người thừa kế duy nhất đành phải tạm dừng việc học để ra mặt chủ trì đại cục.""",
"""Cùng lúc đó, những đòn công kích của Phó Minh nhằm vào Phó Vân Xuyên cũng càng lúc càng trở nên dữ dội, cục diện đối đầu giữa tập đoàn Vân Xuyên và tập đoàn tài phiệt Phó thị đã bước vào thời khắc ngàn cân treo sợi tóc.""",
"""Nếu chiểu theo cốt truyện gốc, Phó Vân Xuyên sắp sửa nghênh đón kết cục cuối cùng, mà kết cục của anh chính là bị cặp đôi công thụ chính đích thân tống vào viện tâm thần, còn tập đoàn Vân Xuyên sẽ bị hai nhà Phó – Ngụy thâu tóm toàn bộ.""",
"""Giang Minh Lãng thầm nghĩ, Phó Vân Xuyên tuyệt đối không thể rơi vào kết cục thảm khốc này được.""",
"""Hôm nay cậu lại đến đứng đợi trước cửa lớp học của Phó Ngôn từ sớm, rất nhiều người trong lớp đều đã quen mặt cậu, cất tiếng chào hỏi.""",
"""“Lại đến tìm Phó Ngôn à, cậu may mắn đấy nhé, hôm nay cậu ta có đến trường, nhưng là trực tiếp đến gặp cố vấn học tập nộp đơn xin bảo lưu, cậu mau qua tìm cậu ta đi, may ra vẫn còn kịp đấy.” Có người tốt bụng nhắc nhở.""",
"""Giang Minh Lãng nói một tiếng cảm ơn rồi vội vã phi như bay về phía tòa nhà hành chính, quả nhiên không ngoài dự đoán, cậu trông thấy Phó Ngôn đang cất bước đi ra ngoài.""",
"""“Phó Ngôn, có thời gian nói chuyện một lát không?” Giang Minh Lãng thở hổn hển chặn đường trước mặt Phó Ngôn.""",
"""Vệ sĩ bên cạnh gọi một tiếng thiếu gia nhưng bị Phó Ngôn giơ tay ngăn lại: “Được chứ.”""",
"""Sau khi hai người bước vào thư viện ngồi xuống, Giang Minh Lãng liền đi thẳng vào vấn đề.""",
"""“Tôi muốn nói với cậu một chuyện, cậu có biết thật ra Phó tiên sinh chưa từng giết người không?”""",
"""Vốn tưởng Phó Ngôn không hay biết, nào ngờ cậu ta lại khẽ gật đầu: “Biết.”""",
"""Giang Minh Lãng lập tức chết sững tại chỗ.""",
"""“Hóa ra ngay cả chuyện này mà anh ấy cũng kể cho cậu nghe,” Phó Ngôn nhìn sâu vào Giang Minh Lãng, nói: “Cậu bảo nếu lúc này tôi bắt cóc cậu, liệu anh ấy có vì cậu mà từ bỏ mọi kế hoạch trả thù không?”""",
"""Giang Minh Lãng nghe vậy liền cảnh giác đảo mắt nhìn quanh bốn phía.""",
"""“Đây là trường học, tôi không ngu đến mức ra tay ở chỗ này đâu.” Phó Ngôn lạnh lùng nói: “Nhưng về sau thì chưa chắc.”""",
"""Trên gương mặt Phó Ngôn là một biểu cảm hoàn toàn xa lạ đối với Giang Minh Lãng, lúc này Phó Ngôn dường như đã xé bỏ toàn bộ lớp vỏ ngụy trang ngoan ngoãn thánh thiện.""",
"""“Trả thù có nghĩa là sao?” Giang Minh Lãng nhìn Phó Ngôn, trầm giọng hỏi.""",
"""Phó Ngôn day day mi tâm mệt mỏi: “Nếu mọi chuyện đã đi đến bước đường ngày hôm nay rồi thì cũng chẳng có gì là không thể nói.”""",
"""“Tất cả những gì Phó Vân Xuyên đang làm bây giờ chẳng phải đều nhằm trả thù việc năm đó bố mẹ bắt anh ta đi gánh tội thay cho anh Vân Hi sao?”""",
"""“Cái gì?” Đồng tử Giang Minh Lãng bỗng co rút dữ dội: “Gánh tội thay?”""",
"""“Thực ra tôi không hiểu tại sao anh ấy lại hận đến thế, chẳng qua chỉ là năm năm trời thôi mà, anh Vân Hi từ lúc sinh ra đã vì bị anh ta cướp đoạt chất dinh dưỡng trong bụng mẹ mà thể trạng ốm yếu bẩm sinh, đây vốn là món nợ Phó Vân Xuyên thiếu anh ấy.”""",
"""Phó Ngôn lạnh lùng buông lời phán xét:""",
"""“Sức khỏe của anh Vân Hi yếu ớt như vậy làm sao chịu nổi năm năm ngồi tù mọt gông, vả lại, chính Phó Vân Xuyên đã tự mình đồng ý cơ mà, tại sao bây giờ lại nhẫn tâm hạ thủ độc ác với Phó gia như thế chứ?”""",
"""Giang Minh Lãng không thể tin nổi nhìn trừng trừng vào Phó Ngôn: “Người không phải do anh ấy giết, anh ấy lấy tư cách gì phải đi ngồi tù chứ?”""",
"""“Cậu không hiểu đâu, kiếp nạn năm đó anh Vân Hi gặp phải, khéo lại chính là do Phó Vân Xuyên mang tới.”""",
"""Phó Ngôn vừa nói vừa né tránh ánh mắt của Giang Minh Lãng.""",
"""“Phó gia từ khi khởi nghiệp đã vô cùng mê tín vào số mệnh, mỗi khi có đứa trẻ chào đời đều mời đạo sĩ trong đạo quán về gieo quẻ. Bất hạnh thay, đạo sĩ năm đó tính ra Phó Vân Xuyên mệnh mang sát khí, không chỉ làm tổn hại đến người anh em ruột thịt mà còn chặt đứt long mạch tài vận của Phó gia.”""",
"""“Bố mẹ tuy không nỡ nhưng vẫn phải gửi anh ta sang nhà chú, nếu không phải về sau anh Vân Hi cứ khăng khăng đòi bố mẹ đón anh ta về nhà, thì làm sao lại vì sự trở về của Phó Vân Xuyên mà gặp phải vận hạn xui xẻo lớn như thế? Dù xét về tình hay về lý, Phó Vân Xuyên cũng nên đồng ý gánh tội thay.”""",
"""Nghe đến đây, trong mắt Giang Minh Lãng chỉ còn lại sự khó hiểu tột cùng đối với thứ lý lẽ hoang đường bỉ ổi này: “Tôi không thể nào hiểu nổi cậu đang nói cái quái gì nữa.”"""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_032\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_032\translation.md'

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

print("Saved ch_032 successfully!")
