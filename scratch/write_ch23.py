import re
import os

paras_trans = [
"""---
title: Chương 23: Trang 23
---""",
"""Đường trượt tuyết uốn lượn ngoằn ngoèo, Phó Vân Xuyên lộn nhào một vòng trên không rồi tiếp đất thật mạnh xuống một sườn dốc tuyết mới.""",
"""Lần này, khung cảnh biến thành căn gác xép của Phó gia.""",
"""Anh ngồi dưới đất, bực bội rít thuốc lá, cách đó không xa là tiếng tranh cãi của vợ chồng Phó gia về việc có nên đón anh về hay không. Đúng lúc này, một thiếu niên sạch sẽ thanh tú bước đến trước mặt anh, dắt lấy tay anh và nói: anh trai dẫn em đi chơi.""",
"""Sườn dốc tuyết lại lần nữa đổi thay, ván trượt tuyết để lại những đường cong sâu hoắm trên mặt tuyết.""",
"""“Vân Xuyên, em cứu anh với.” Thiếu niên trong ký ức mặt mũi đầy máu, vẻ mặt kinh hoàng nắm chặt lấy tay anh, toàn thân run rẩy kịch liệt.""",
"""Trong nhà tù nặng nề chết chóc, chính anh đang mang xiềng xích đi lại giữa những hàng rào lưới điện.""",
"""Hết lần này đến lần khác ẩu đả, hết lần này đến lần khác nhìn thấy ánh đèn xanh của phòng biệt giam.""",
"""Những túm lông dính máu đầm đìa, đống thịt nát chẳng còn rõ hình thù, thiếu niên gầy trơ như xương xẩu trong bức ảnh, cùng đôi nhãn cầu lồi ra đầy kinh hãi trước khi chết...""",
"""Vô số hình ảnh đan xen hiện ra trong tầm mắt trắng xóa mịt mùng, hơi thở của Phó Vân Xuyên bắt đầu trở nên hỗn loạn.""",
"""Anh vẫn đang lao xuống với tốc độ chóng mặt, nhưng cơ thể dường như sắp mất kiểm soát.""",
"""Vút một tiếng, một tiếng huýt sáo bất chợt lọt vào màng nhĩ của anh.""",
"""Giữa tiếng hò reo cổ vũ của đám huấn luyện viên, một giọng nam thanh niên nằm giữa ranh giới non nớt và trưởng thành đang cao giọng gào to: “Phó tiên sinh, anh đỉnh quá!”""",
"""Phó Vân Xuyên bỗng hoàn hồn, chỉ thấy trong tầm nhìn, Giang Minh Lãng đang đứng ở chân dốc ra sức vẫy cánh tay về phía anh, làn da màu nâu sẫm của cậu nổi bật lạ thường giữa nền tuyết trắng xóa.""",
"""Bóng dáng Giang Minh Lãng từ kích thước bằng hạt đậu dần trở nên rõ ràng trong tầm mắt, mà anh thì chỉ còn lại sườn dốc thoai thoải cuối cùng.""",
"""Anh cúi người chạm tay xuống đất, lướt ván trượt xuống dốc với tốc độ đã giảm rõ rệt, cuối cùng dừng lại đều đặn ngay trước mặt Giang Minh Lãng.""",
"""“Hóa ra anh lợi hại thế này, chắc hẳn anh hay chơi lắm nhỉ.” Giang Minh Lãng chạy vội tới, thật lòng cất lời.""",
"""Phó Vân Xuyên khó khăn lắm mới lấy lại bình tĩnh, anh cúi đầu liếc nhìn tấm ván trượt đã biến mất dưới chân Giang Minh Lãng, hỏi: “Ván trượt của cậu đâu rồi.”""",
"""Giang Minh Lãng gãi gãi sau gáy, thành thật khai báo: “Tôi phát hiện mình không thích chơi trượt tuyết cho lắm nên tháo ra rồi, nhưng trợ lý Trần có vẻ rất thích đấy.” Cậu chỉ tay về phía người trợ lý ở cách đó không xa.""",
"""“Vậy cậu muốn chơi cái gì.” Phó Vân Xuyên hỏi.""",
"""“Tôi muốn chơi tuyết cơ.” Giang Minh Lãng hớn hở đáp.""",
"""Không đợi Phó Vân Xuyên nói thêm câu nào, Giang Minh Lãng đã nhào một cú thật mạnh, ném cả người vào lớp tuyết dày cộm.""",
"""Chóp mũi cao thẳng vùi sâu vào trong tuyết, tò mò húc húc ngửi ngửi khắp xung quanh, cậu cực kỳ yêu thích mùi hương tự nhiên mát lạnh thấu xương ẩn chứa trong tuyết.""",
"""Cổ áo sau lưng bị người ta tóm lấy không chút nương tay, Giang Minh Lãng nhọc nhằn ngoái đầu lại, trông thấy Phó Vân Xuyên đang sa sầm mặt mày mắng cậu: “Bị tật gì đấy.”""",
"""Giang Minh Lãng giãy giụa vài cái không có kết quả, thế là cậu chìa tay ra, vốc một nắm tuyết đưa tới trước mặt Phó Vân Xuyên: “Phó tiên sinh, anh có thể chơi cái này với tôi một lát không?”""",
"""Dưới sự ép buộc của Phó Vân Xuyên, Giang Minh Lãng mới chịu từ trong tuyết đứng dậy, nắm tuyết trong lòng bàn tay cậu vì quá lâu không có người nhận lấy nên đã trượt rơi mất hơn nửa.""",
"""“Nếu anh không muốn chơi thì cũng chẳng sao đâu,” Thấy ánh mắt Phó Vân Xuyên nhìn mình kỳ lạ quá đỗi, cậu liền nói: “Tôi có thể tự qua bụi cây nhỏ bên kia chơi một lát.”""",
"""Nói xong, cậu buông tay xuống, bước thấp bước cao quay người đi về hướng lùm cây nhỏ cách đó không xa.""",
"""“Bốp”""",
"""Lưng cậu bị một vật mềm xốp đập trúng, cậu quay người lại thì phát hiện trong tay Phó Vân Xuyên đang nắm một vốc tuyết.""",
"""Bông tuyết lại một lần nữa phóng ra từ bàn tay Phó Vân Xuyên, lần này Giang Minh Lãng cười rộ lên đầy phấn khích, nhào tới dùng thân mình đỡ lấy bụm tuyết kia.""",
"""Hết nắm tuyết này đến nắm tuyết khác được Phó Vân Xuyên vốc lên ném tới, bột tuyết văng tung tóe vẽ nên từng mảng từng mảng sương mù trắng xóa giữa không trung.""",
"""Ở một bên khác, trợ lý Trần đang luyện tập tư thế đứng cơ bản ngơ ngác nhìn cảnh tượng trước mắt.""",
"""“Sao có cảm giác như đang trêu chó nhà tôi thế nhỉ.” Một huấn luyện viên cười đùa trêu chọc.""",
"""“Đúng vậy,” Ánh mắt trợ lý dán chặt vào khóe môi vô tình nhếch lên của Phó Vân Xuyên, lẩm bẩm: “Mắc tật gì không biết.”""",
"""...""",
"""Về sau, vì Giang Minh Lãng bắt đầu vốc tuyết đánh trả, hai người ném qua ném lại trong bãi tuyết càng lúc càng xa.""",
"""Phó Vân Xuyên chỉ sơ sẩy một cái đã không thấy bóng dáng Giang Minh Lãng đâu nữa.""",
"""Ngẩng mắt nhìn lại, bốn phía xung quanh chỉ còn lại một mình anh.""",
"""Cảm giác cô độc ập đến bất ngờ khiến tay chân anh lạnh buốt.""",
"""“Giang Minh Lãng!” Anh nghiến chặt răng, giận dữ gọi lớn.""",
"""Gọi liền mấy tiếng nhưng không có ai đáp lời.""",
"""Tuyết trong tay rơi tuột xuống đất, hơi thở của Phó Vân Xuyên càng lúc càng nặng nề.""",
"""Đột nhiên, một bóng đen to lớn từ phía sau xông thẳng tới trước mặt anh.""",
"""Tầm nhìn xoay tròn chóng mặt, Phó Vân Xuyên bị một thân hình cao lớn nặng nề đè sầm xuống lớp tuyết dày xốp.""",
"""“Gâu! Gâu!”""",
"""Giang Minh Lãng hưng phấn tột độ vùi mặt vào hõm cổ anh, phát ra hai tiếng chó sủa sống động như thật.""",
"""Phó Vân Xuyên ngửa mặt nhìn trời, đồng tử tan rã trong vài giây, sau đó ôm lấy người đang nằm trên mình, không kìm được mà giơ lòng bàn tay lên xoa xoa đầu Giang Minh Lãng.""",
"""Nhịp tim bất an dần trở về vẻ tĩnh lặng.""",
"""Cảm nhận được Phó Vân Xuyên đang xoa đầu mình, Giang Minh Lãng khựng lại rõ rệt, rồi ngẩng đầu lên.""",
"""Đây là lần đầu tiên Alaska được một nhân loại ngoài sĩ quan chấp hành xoa đầu, cậu trố mắt nhìn Phó Vân Xuyên, ngoác miệng cười toe toét.""",
"""Ánh nắng trên đỉnh đầu có chút chói chang, Phó Vân Xuyên nhìn thấy trên gò má ngăm đen của Giang Minh Lãng còn ửng lên rặng hồng vì bị lạnh cóng.""",
"""Giang Minh Lãng vì vận động kịch liệt mà đang thở dốc từng cơn, chất giọng trầm khàn mang theo hormone độc nhất vô nhị của thiếu niên.""",
"""Theo tầm mắt dời dần xuống dưới, đáy mắt anh càng lúc càng trở nên thâm sâu.""",
"""Bàn tay đang vuốt ve đỉnh đầu Giang Minh Lãng thuận đà trượt xuống, chậm rãi dừng lại ở sau gáy ram ráp tóc ngắn.""",
"""Gần như chẳng hề có điềm báo trước, sau gáy bị ấn mạnh xuống, dưới ánh mắt kinh ngạc của Giang Minh Lãng, Phó Vân Xuyên hơi nghiêng đầu, hôn lên cánh môi cậu.""",
"""Lần này không giống như lần trước cắn xé như trút giận, mà là từng chút từng chút một, dịu dàng cọ xát đôi môi cậu.""",
"""Giống như bị một quả cầu tuyết ném chuẩn xác trúng tim, Giang Minh Lãng ngơ ngác nhìn vào mắt Phó Vân Xuyên, hàng mi khẽ run rẩy.""",
"""“Mở miệng.”""",
"""Cậu nghe thấy Phó Vân Xuyên dùng chất giọng dịu dàng chưa từng có nói với mình.""",
"""Giang Minh Lãng như bị mê hoặc, nhắm mắt lại, khuỷu tay chống bên tai Phó Vân Xuyên, chủ động đè xuống...""",
"""Cả ba người ở lại sân tuyết đến tận giữa trưa mới đi ra, lúc bước ra mặt mũi Giang Minh Lãng đỏ bừng lựng cả lên, như thể sợ người khác không biết cậu và Phó Vân Xuyên đã làm gì vậy.""",
"""Trợ lý mắt nhìn mũi mũi nhìn tim, báo với Phó Vân Xuyên rằng máy bay đã đậu ở sân bay trực thăng của khách sạn, thế là cả ba lái xe xuống núi, xuất phát trở về thành phố A.""",
"""Suốt dọc đường đi Giang Minh Lãng đều lúng túng mất tự nhiên khác thường, một mặt cậu theo thói quen nép sát vào Phó Vân Xuyên để tìm kiếm cảm giác an toàn khi ở trên cao, mặt khác lại không hiểu sao hễ đến gần Phó Vân Xuyên là lại nhớ đến xúc cảm liếm lưỡi lẫn nhau, trái tim đập thình thịch thình thịch không ngừng nghỉ.""",
"""Cậu không hiểu vì sao Phó Vân Xuyên lại phải liếm lưỡi với mình, cậu cảm nhận theo trực giác rằng đây là một hành vi biểu đạt sự thân mật, nhưng nói chung trong giới loài chó không hề có hành vi này, cho dù có thân thiết lắm thì cũng chỉ dùng lưỡi liếm mõm đối phương mà thôi, vả lại còn phải là ở dạng chó nữa.""",
"""Giống như cậu chưa bao giờ liếm lưỡi lẫn nhau với Maltese vậy.""",
"""Vì ôm nặng tâm sự nên suốt cả quá trình trên máy bay đều im ắng khác thường.""",
"""Vừa xuống máy bay, Giang Minh Lãng đã trông thấy mẹ Giang đứng đợi sẵn ở sân sau từ sớm, ánh mắt bà nhìn cậu vừa có cưng chiều vừa có trách móc, nhưng nhiều hơn cả là nỗi ưu sầu nồng đậm.""",
"""Mẹ Giang trước tiên thu xếp ổn thỏa mọi việc cho Phó Vân Xuyên, sau đó kéo cậu lại bảo cậu phải cảm ơn Phó Vân Xuyên: “Mau cảm ơn Phó tiên sinh đi, toàn thêm phiền phức cho ngài ấy.”""",
"""Cảm nhận được Phó Vân Xuyên đang nhìn mình, cậu đành cắn răng, lúng búng ngượng ngùng nói một câu: “Cảm ơn Phó tiên sinh.”""",
"""“Không có gì.” Phó Vân Xuyên nói với mẹ Giang, sau đó nhìn sâu vào Giang Minh Lãng một cái rồi xoay người lên lầu.""",
"""Giang Minh Lãng nhìn bóng lưng rời đi của Phó Vân Xuyên mà khẽ xuất thần, đúng lúc này, cậu nghe mẹ Giang bảo: “Minh Lãng, cùng mẹ về phòng, mẹ có chuyện này muốn nói với con.”""",
"""Giọng điệu của mẹ Giang quá đỗi nặng nề, Giang Minh Lãng lập tức nhận ra chuyện bà sắp nói có lẽ là một việc rất lớn.""",
"""Sau khi về đến phòng cậu, mẹ Giang ngồi xuống.""",
"""“Có chuyện gì vậy mẹ?” Giang Minh Lãng căng thẳng hỏi.""",
"""Mẹ Giang muốn nói lại thôi, viền mắt đỏ hoe với tốc độ có thể thấy bằng mắt thường: “Minh Lãng, ông ngoại con...”""",
"""“Ông ngoại làm sao ạ?” Giang Minh Lãng buột miệng hỏi.""",
"""Mẹ Giang ôm trán cay đắng nói: “Phổi của ông ngoại con trước giờ vốn không tốt, hở một chút là ho, tuần trước ông cụ đi trên phố thì ho ra máu ngay tại chỗ, bị người ta phát hiện kéo đến bệnh viện kiểm tra, kết quả là...”""",
"""Mẹ Giang không kìm được nghẹn ngào bật khóc: “Kết quả kiểm tra ra ông bị ung thư phổi giai đoạn cuối, nếu không nhờ thím Vương gọi điện báo cho mẹ biết thì ông cụ vẫn muốn giấu giếm mãi.”""",
"""“Ung thư phổi giai đoạn cuối?” Giang Minh Lãng thảng thốt nói, ánh mắt dại đi.""",
"""Ung thư giai đoạn cuối, thường thức nghiên cứu về nhân loại chỉ ra rằng, một khi con người mắc phải ung thư, thứ phải đối mặt chính là cái chết tất yếu.""",
"""“Bác sĩ khuyên ông nên đến bệnh viện tốt nhất ở thành phố A phẫu thuật, phẫu thuật thành công thì có xác suất sống lâu hơn một chút, hiện tại tiền phẫu thuật cần một triệu tệ.” Giọng điệu mẹ Giang nặng trĩu.""",
"""Giang Minh Lãng hiểu rõ, một triệu tệ đối với gia đình bọn họ chính là một con số trên trời.""",
"""“Minh Lãng, con đã trưởng thành rồi, mẹ nghĩ con có quyền được biết tình cảnh gia đình chúng ta,” Bà nói: “Bây giờ món nợ mà bố đẻ con để lại chúng ta vẫn còn thiếu hai mươi vạn, mẹ nghĩ cách trì hoãn bọn họ, có lẽ... có lẽ đi vay mượn họ hàng thêm một chút cũng gom góp được...”""",
"""Càng nói, mẹ Giang càng suy sụp khóc nấc lên.""",
"""Giang Minh Lãng biết mẹ Giang đang tự lừa mình dối người, bà dù có làm cách nào cũng không thể gom đủ một triệu này.""",
"""Cậu đỏ hoe mắt bước tới, ôm lấy mẹ Giang vào lòng, nói: “Mẹ, con sẽ cùng mẹ nghĩ cách.”""",
"""Lời tác giả:""",
"""Chương 21: Alaska 21""",
"""Sáng hôm sau, Giang Minh Lãng nhận được điện thoại của Phó Vân Xuyên bảo cậu xuống lầu, nói là chở cậu đến trường.""",
"""Thế là cậu nhân lúc mẹ Giang đang bận bịu, lén lén lút lút leo lên xe của Phó Vân Xuyên."""
]

src_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_023\source.md'
out_path = r'd:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_023\translation.md'

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

print("Saved ch_023 successfully!")
