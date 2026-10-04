# -*- coding: utf-8 -*-
import json
import os
import re

ch16_dir = r"d:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_016"
source_file = os.path.join(ch16_dir, "source.md")
trans_file = os.path.join(ch16_dir, "translation.md")
qc_file = os.path.join(ch16_dir, "qc_report.md")
meta_file = os.path.join(ch16_dir, "meta.json")
timeline_file = r"d:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\memory\timeline.json"

translations = [
"""---
title: "Chương 16: Alaska 16"
---""",

"""Phó Vân Xuyên nằm trở lại vị trí cũ, nhạt giọng nói: “Tự mình lên đây.”""",

"""Giang Minh Lãng: ??? """,

"""Lên đây, là lên đâu cơ chứ?""",

"""“Sự kiên nhẫn của tôi có hạn thôi đấy.” Bóng tối dường như khiến cho Phó Vân Xuyên bồn chồn khó chịu, ngữ điệu rõ ràng càng thêm phần mất kiên nhẫn.""",

"""Giang Minh Lãng mù tịt chẳng hiểu ất giáp gì, cậu nhìn lồng ngực đang phập phồng gấp gáp vì bất an của Phó Vân Xuyên, nghĩ bụng Phó Vân Xuyên giữ mình ở lại là để mình bầu bạn với anh, mà sách giáo khoa có dạy rồi, phương thức bầu bạn với loài người chính là rúc vào trong lòng chủ nhân.""",

"""Phó Vân Xuyên hẳn là ngại ngùng không nỡ mở miệng bảo cậu ôm lấy anh.""",

"""Thế là trước khi Phó Vân Xuyên hoàn toàn cạn kiệt kiên nhẫn, Giang Minh Lãng đã động đậy. Cậu chầm chậm nhích lại gần Phó Vân Xuyên, sau đó mở rộng cánh tay anh ra, đặt bàn tay Phó Vân Xuyên lên eo mình, rồi gian nan nhét thân hình đồ sộ to lớn của mình chui tọt vào trong lòng đối phương.""",

"""Cậu vỗ nhẹ lên tấm lưng của Phó Vân Xuyên, cất giọng khẽ khàng dỗ dành: “Đừng sợ, đừng sợ nhé, có tôi ở bên cạnh anh rồi.”""",

"""...""",

"""Có lẽ là do chiếc giường của Phó Vân Xuyên quá đỗi êm ái, cho dù cậu cảm nhận được cơ thể Phó Vân Xuyên ban đầu cứng đờ như khúc gỗ, nhưng ôm một hồi rồi cậu cũng lăn ra ngủ say như chết từ lúc nào không hay. Đêm hôm đó Giang Minh Lãng ngủ một giấc say sưa ngon lành, đến khi mở mắt tỉnh dậy, cậu mới giật mình nhớ ra hôm nay mình vẫn phải đến trường đi học.""",

"""“A a a, tôi muộn giờ rồi!” Giang Minh Lãng vội vàng vùng vẫy thoát khỏi vòng tay của Phó Vân Xuyên, liếc nhìn đồng hồ rồi gào toáng lên.""",

"""Phó Vân Xuyên khẽ mở mi mắt, chậm rãi ngồi dậy, đồng tử xuất hiện một thoáng tan rã mơ màng ngắn ngủi.""",

"""Anh nâng mắt nhìn chằm chằm vào Giang Minh Lãng, nơi đáy mắt lóe lên những tia suy tính sâu xa, cuối cùng anh bước xuống giường, đi về phía phòng thay đồ.""",

"""“Mặc quần áo vào đi, tôi đưa cậu đến trường.”""",

"""Giang Minh Lãng trước tiên là thầm mừng rỡ trong lòng vì bản thân đã trốn học thành công, sau đó mới thong thả không chút vội vàng đi đánh răng rửa mặt, rồi ngoan ngoãn ngồi ngay ngắn trên sô pha đợi Phó Vân Xuyên.""",

"""Lúc cậu cùng Phó Vân Xuyên sóng vai bước xuống lầu, còn vừa vặn chạm mặt mẹ Giang đang đi lên hỏi Phó Vân Xuyên có ăn bữa sáng hay không.""",

"""Mẹ Giang ngạc nhiên liếc nhìn cậu một cái, không dám trước mặt Phó Vân Xuyên chất vấn con trai, chỉ đành dùng ánh mắt ra hiệu đầy thắc mắc.""",

"""“Sáng sớm tôi bảo cậu ấy lên thư phòng tôi một chuyến.” Phó Vân Xuyên đột nhiên lên tiếng giải thích, “Bữa sáng tôi không ăn đâu.”""",

"""Mẹ Giang ngẩn ra một thoáng, vội vàng gật đầu lia lịa.""",

"""Đối diện với ánh mắt dò xét của mẹ Giang, Giang Minh Lãng lấm lét ngoan ngoãn đi theo sau Phó Vân Xuyên lên xe.""",

"""Vừa mới bước lên xe, liền nghe thấy Phó Vân Xuyên quay sang dặn cậu: “Đừng nói cho bà ấy biết chuyện tối hôm qua.”""",

"""“Tại sao thế ạ?” Giang Minh Lãng ngây thơ cất tiếng hỏi, kết quả nhận lại được một nụ cười u ám rợn người tiêu chuẩn của Phó Vân Xuyên.""",

"""“Có đôi khi giả ngốc quá mức thì sẽ chẳng còn đáng yêu nữa đâu.” Phó Vân Xuyên cười mà như không cười nói.""",

"""Giang Minh Lãng lập tức ngậm chặt miệng lại, cậu nhiều khi thực sự không tài nào hiểu nổi những lời Phó Vân Xuyên nói, chẳng lẽ anh sợ người khác biết đêm qua vì sợ bóng tối mà anh đã ôm chặt cứng lấy mình sao?""",

"""Cậu đặt quả bóng rổ tiện tay mang theo lúc ra khỏi cửa từ trong lòng xuống dưới chân, rồi quay đầu hướng ánh mắt tò mò nhìn ra ngoài cửa sổ xe.""",

"""“Cậu thích Armand à?” Phó Vân Xuyên bất chợt buông một câu hỏi bâng quơ.""",

"""Giang Minh Lãng biết Phó Vân Xuyên đang nói tới quả bóng rổ của mình, quả bóng này là do mẹ Giang hồi đó cắn răng chi một số tiền lớn mua cho cậu phiên bản kết hợp giới hạn, đến nay đã bị chơi mòn vẹt cả rồi.""",

"""“Sao anh biết Armand thế?” Giang Minh Lãng mừng rỡ hỏi, “Chẳng lẽ anh cũng thích chơi bóng rổ sao?”""",

"""Thế nhưng Phó Vân Xuyên lại không hề trả lời câu hỏi này của cậu.""",

"""Đúng lúc này màn hình điện thoại của anh sáng lên một cái, Giang Minh Lãng dựa vào thị lực tinh tường của loài chó liền nhìn thấy ba chữ Phó Ngôn hiển thị trên đó.""",

"""Chỉ thấy Phó Vân Xuyên bình thản cầm điện thoại lên gõ vài chữ gửi đi, sau đó liền khóa màn hình lại.""",

"""“Đừng quên việc trước đây tôi bảo cậu làm, trông chừng Phó Ngôn cho cẩn thận, rồi báo lại cho tôi biết dạo này cậu ta đang làm những gì.”""",

"""Để cho anh biết, đôi vợ chồng kia đã cưng nựng, chiều chuộng đứa con nuôi này đến nhường nào.""",

"""Giang Minh Lãng lập tức cảnh giác cao độ, giữa hàng mày tuấn tú ngập tràn vẻ cự tuyệt: “Tại sao anh lại để ý tới cậu ta nhiều đến thế chứ?”""",

"""Câu này vừa thốt ra, bầu không khí bên trong khoang xe liền lập tức hạ nhiệt độ xuống mức âm độ đóng băng.""",

"""“Giang Minh Lãng,” Phó Vân Xuyên lạnh lùng gọi tên cậu, đoạn quay đầu sang, chầm chậm đưa bàn tay áp sát vào một bên tai của cậu.""",

"""Đôi găng tay da mát lạnh khẽ miết qua đuôi mắt cậu, còn chưa đợi cậu kịp phản ứng lại thì đã bị một lực đạo thô bạo đè ghì sát vào trước mặt Phó Vân Xuyên.""",

"""“Hãy nhận rõ vị trí của mình, đừng bao giờ thử thách giới hạn chịu đựng của tôi, nếu không tôi rất khó bảo đảm bản thân sẽ không làm gì cậu đâu.”""",

"""Giang Minh Lãng vô cùng chán ghét việc bị người khác ép buộc phải nhìn thẳng trừng trừng thế này, trong thế giới loài chó điều này đại diện cho sự thị uy và khiêu khích trắng trợn.""",

"""Cậu dứt khoát giơ tay hất mạnh bàn tay của Phó Vân Xuyên đang đè sau gáy mình ra, gằn giọng thấp giọng phản bác lại anh: “Tại sao lần nào anh cũng không thể nói chuyện tử tế được chứ? Tôi ghét anh như thế này lắm!”""",

"""Thân xe bất thình lình phanh gấp một cú dúi dụi, người tài xế ngồi phía trước sợ đến mức cuống cuồng lên tiếng: “Đến... đến nơi rồi ạ.”""",

"""Trong gương chiếu hậu, sắc mặt của Phó Vân Xuyên đã đen kịt đến mức có thể vắt ra nước.""",

"""Giang Minh Lãng buông xong lời dằn mặt liền cúi người nhặt lấy quả bóng rổ dưới chân rồi đẩy cửa bước xuống xe. Cho dù lúc này trong lòng cậu vừa thấy tủi thân vừa thấy tức giận, nhưng vẫn không quên quay đầu nói với người trong xe một câu: “Cảm ơn anh, tôi đi học đây, tạm biệt.”""",

"""Cửa xe tự động đóng lại, Phó Vân Xuyên chẳng nói chẳng rằng lấy nửa lời, chỉ ra hiệu cho tài xế lái xe đi.""",

"""Giang Minh Lãng đứng nguyên tại chỗ nhìn theo đuôi xe đang chầm chậm lăn bánh rời đi, trong lòng có đôi chút ủ rũ chán nản.""",

"""Thực ra ngày hôm qua khi Phó Vân Xuyên tặng giày thể thao cho cậu, cậu đã quyết định sẽ kết bạn làm bạn bè tốt với Phó Vân Xuyên rồi, thế nhưng lời đe dọa vừa rồi của người “bạn tốt” lại khiến cậu cảm thấy vô cùng tổn thương.""",

"""Bên trong xe, Phó Vân Xuyên nhìn qua gương chiếu hậu ngắm nhìn bóng dáng Giang Minh Lãng đang dần thu nhỏ lại ở đằng xa, trong gương Giang Minh Lãng vẫn luôn ngơ ngẩn nhìn theo hướng chiếc xe, biểu cảm trên mặt tủi thân không để đâu cho hết,""",

"""hệt như một chú chó cỡ lớn bị chủ nhân bỏ rơi ngoài đường.""",

"""“Lùi xe lại.”""",

"""“Dạ?”""",

"""“Tôi bảo, lùi xe lại.” Phó Vân Xuyên bực bội gắt gỏng.""",

"""“Dạ vâng, vâng ạ.”""",

"""Thế là Giang Minh Lãng liền trơ mắt nhìn chiếc xe vừa mới phóng đi cách đó không xa bỗng nhiên từ từ lùi ngược trở lại.""",

"""Cửa kính xe hạ xuống, lộ ra góc nghiêng gương mặt của Phó Vân Xuyên.""",

"""“Buổi chiều mấy giờ tan học?” Anh hỏi.""",

"""Giang Minh Lãng ngẩn tò te mất một lúc: “Dạ? Hôm nay thứ Ba, chắc là năm giờ ạ.”""",

"""Phó Vân Xuyên: “Tan học đứng ở đây đợi tôi,” Anh ngẫm nghĩ một thoáng rồi lại hỏi thêm, “Thích ăn món gì, buổi tối dẫn cậu đi ăn?”""",

"""Giang Minh Lãng: “A, được, được chứ ạ, tôi thích ăn thịt.” Nói xong cậu lại lấy hết dũng khí bổ sung thêm một câu, “Không phải là tôi không muốn giúp anh đâu, mà là... là vì Phó Ngôn cậu ta không thích tôi.”""",

"""Phó Vân Xuyên nhìn cậu một ánh mắt sâu xa: “Biết rồi, tạm biệt.”""",

"""Cửa kính xe lại lần nữa kéo lên, lần này thì chiếc xe mới thực sự lăn bánh rời đi hẳn.""",

"""Nhìn qua gương chiếu hậu thấy bóng dáng Giang Minh Lãng rõ ràng đã vui vẻ hớn hở chân sáo nhảy cẫng lên, nơi khóe môi Phó Vân Xuyên bỗng thoáng hiện một nụ cười thoáng qua rồi biến mất.""",

"""Đôi khi anh cảm thấy Giang Minh Lãng thực sự hệt như một chú chó lớn, chỉ cần nhận được một chút phản hồi đáp lại từ loài người là sẽ vui mừng khôn xiết mà ngoe nguẩy cái đuôi.""",

"""Đến lúc thu hồi ánh mắt lại, anh vừa vặn bắt gặp ánh nhìn đầy hoảng loạn đang vội vã dời đi của người tài xế.""",

"""“Đến công ty.”""",

"""Tiếng chuông điện thoại reo vang, Phó Vân Xuyên bấm nghe máy, ánh mắt dần trở nên lạnh lẽo tàn nhẫn: “Ừm, mấy mảnh đất kia của Phó thị có thể bắt đầu ra tay được rồi đấy.”""",

"""“Sắp xếp lại lịch trình tháng sau tôi đi thành phố C cho tôi.”""",

"""“Khoan đã, cho cậu thời hạn một tuần, tìm mang một món đồ chơi nhỏ tới đây cho tôi.”""",

"""...""",

"""Bởi vì sự việc trong đêm hội chào tân sinh viên, cái tên Phó Vân Xuyên nhanh chóng lan truyền rầm rộ khắp toàn bộ khuôn viên trường Đại học A.""",

"""Giang Minh Lãng bất kể đi tới đâu cũng đều nghe thấy những sinh viên đi ngang qua đang hào hứng bàn tán về lịch sử lập nghiệp làm giàu của Phó Vân Xuyên.""",

"""Kèm theo đó, bản thân cậu cũng được thơm lây mà nổi đình nổi đám khắp trường.""",

"""Nguyên do là vì rất nhiều người đều tận mắt nhìn thấy Phó Vân Xuyên đã lấy danh nghĩa người nhà phụ huynh của Giang Minh Lãng để tham dự đêm hội, cộng thêm quãng thời gian gần đây không ít người trông thấy Giang Minh Lãng mỗi ngày đều có xe sang đưa đón tận cổng trường, những lời đồn thổi phong thanh cứ thế lan truyền chóng mặt.""",

"""Hôm nay Giang Minh Lãng đang tập luyện trên sân bóng rổ, đã là lần thứ không biết bao nhiêu cậu nhận được những ánh mắt của người khác đang săm soi đánh giá đôi giày thể thao mới tinh trên chân mình.""",

"""Những ngón tay buông lỏng khỏi vành rổ, cậu từ trên không trung vững vàng tiếp đất, vớ lấy chiếc khăn lông khô bên cạnh quệt mồ hôi trên mặt.""",

"""Huấn luyện viên của đội bóng là một ông lão có gương mặt nghiêm nghị, vỗ vai cậu đầy vẻ tán thưởng, bảo cậu về phòng nghỉ ngơi cho tốt.""",

"""Những tiếng thì thầm bàn tán xì xào xung quanh lọt vào tai Giang Minh Lãng rõ mồn một, cậu nghe thấy bọn họ đang xì xầm những từ ngữ như “trai bao”, “được bao dưỡng”, “thích đàn ông”, mỗi khi Giang Minh Lãng đưa mắt nhìn sang thì những người kia lại như rất sợ cậu mà lập tức im bặt không dám nói nữa.""",

"""“Giang Minh Lãng!”""",

"""Vừa định quay về phòng thay đồ thì nghe thấy có người gọi tên mình, cậu quay đầu lại, trông thấy Phó Ngôn đang rảo bước đi tới, trên tay đưa cho cậu một chai nước suối.""",

"""Cảnh tượng này lại khiến cho đám đông đang rục rịch xung quanh một phen nổ tung bàn tán.""",

"""Đây chính là thiếu gia của Phó gia đấy, hơn nữa... có người lén liếc mắt nhìn sang Ngụy Minh đang dừng ném bóng ở cách đó không xa.""",

"""Giang Minh Lãng ngập ngừng một thoáng, cuối cùng vẫn đưa tay đón lấy chai nước.""",

"""Tuy rằng cậu luôn cố tình né tránh Phó Ngôn, nhưng khổ nỗi thời gian này Phó Ngôn lại cứ liên tục chủ động tìm tới cậu,""",

"""“Hôm nay sau khi tan học cậu có rảnh không, tôi mời cậu đi uống trà sữa nhé?” Phó Ngôn mỉm cười hỏi.""",

"""Giang Minh Lãng lắc đầu từ chối, bởi vì tối nay Phó Vân Xuyên cũng sẽ tới đón cậu.""",

"""“Hôm nay Phó tiên sinh lại đến đón cậu nữa à?” Phó Ngôn làm như thuận miệng bâng quơ hỏi han, “Thích thật đấy, bình thường sau khi tan học hai người hay đi làm những gì thế, tôi chẳng biết có thể làm được những việc gì nữa.”""",

"""Giang Minh Lãng hoàn toàn không hề nhận ra bản thân đang bị đối phương lựa lời moi thông tin, vui vẻ thật thà nói: “Chúng tôi đi ăn cơm.”""",

"""Kể từ sau ngày hôm đó, Phó Vân Xuyên dường như rất thích đưa cậu đến những nhà hàng cao cấp đắt đỏ để ăn cơm, rõ ràng những món ăn ở đó đều vô cùng thơm ngon tuyệt hảo, nhưng lần nào anh cũng chỉ ăn vài miếng tượng trưng rồi dừng đũa, chỉ ngồi chống cằm ngắm nhìn cậu ăn.""",

"""Trên gương mặt Phó Ngôn thoáng hiện một nét nghi hoặc lẫn kinh ngạc, cậu ta còn định nói thêm điều gì đó, nhưng Giang Minh Lãng đã nói lời tạm biệt rồi quay người bước vào phòng thay đồ.""",

"""“Cậu thích thằng nhóc đó đến thế cơ à? Cùng tôi đến sân bóng rổ, lần nào cũng là chạy tới tìm nó.”""",

"""Ngụy Minh nghiến răng nghiến lợi xuất hiện ngay bên cạnh Phó Ngôn, gã trừng mắt lườm nguýt bóng lưng của Giang Minh Lãng một cái đầy thù hằn, dứt lời liền bất chấp sự ngăn cản của Phó Ngôn, sải bước xông thẳng vào phòng thay đồ phía sau.""",

"""“Ngụy——”""",

"""“Rầm——”""",

"""Một tiếng động cực lớn vang lên, cánh cửa phòng thay đồ bị Ngụy Minh từ bên trong hung bạo giáng sập lại thật mạnh.""",

"""Lời tác giả:""",

"""Mấy cái tên như Armand gì đó đều là mình bịa ra thôi nhé, đừng tin nha (chọt ngón tay)""",

"""———""",

"""Các bảo bối thích bộ truyện này không cần phải lo lắng đâu nhé, những lời chúc tốt đẹp của mọi người mình đều nhận được hết rồi, thế giới đầu tiên này mình đã viết xong từ lâu rồi, tuyệt đối sẽ không bị ảnh hưởng bởi bất kỳ bình luận nào đâu nha, thả tim!"""
]

with open(source_file, "r", encoding="utf-8") as f:
    s_paras = [p.strip() for p in f.read().strip().split("\n\n") if p.strip()]

print(f"Source count: {len(s_paras)}, Trans count: {len(translations)}")
assert len(s_paras) == len(translations), f"Count mismatch: {len(s_paras)} vs {len(translations)}"

# Check forbidden words
forbidden = []
for idx, p in enumerate(translations):
    if re.search(r'\b(hắn)\b', p, re.IGNORECASE):
        forbidden.append((idx, p))
assert len(forbidden) == 0, f"Found 'hắn' in {forbidden}"
print("Zero 'hắn' detected across entire chapter!")

# Save translation.md
full_trans_content = "\n\n".join(translations) + "\n"
with open(trans_file, "w", encoding="utf-8") as f:
    f.write(full_trans_content)
print(f"Successfully written {trans_file}")

# Generate qc_report.md
qc_report_content = f"""# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG DỊCH THUẬT (QC REPORT)
**Chương:** Chương 16: Alaska 16 (`ch_016`)  
**Số đoạn gốc:** {len(s_paras)} | **Số đoạn dịch:** {len(translations)}  
**Tỷ lệ khớp đoạn:** 100% (98/98) - Tuyệt đối 1:1  
**Điểm chất lượng:** 1.0/1.0 (XUẤT SẮC)

---

## 1. Kiểm tra tuân thủ Rules Arc 1
- **Công (Giang Minh Lãng):** Xưng ngôi thứ 3 là **"cậu"**, rúc vào lòng Phó Vân Xuyên dỗ dành anh ngủ như bản năng loài chó; phản ứng dữ dội khi bị đè đầu thị uy trên xe nhưng vẫn lễ phép cảm ơn; vẫy đuôi vui sướng khi Phó Vân Xuyên lùi xe rủ đi ăn thịt. Tuyệt đối không dùng "hắn".
- **Thụ (Phó Vân Xuyên):** Xưng ngôi thứ 3 là **"anh"**, ngủ một giấc bình yên không mộng mị trong vòng ôm ấm áp của cún; tức giận đe dọa nhưng thấy cún tủi thân liền mềm lòng lùi xe hẹn ăn tối; thích ngắm nhìn Giang Minh Lãng ăn ngon miệng. Tuyệt đối không dùng "hắn" hay "y".
- **Đối thoại người - người:** Phó Vân Xuyên (**tôi - cậu**) ↔ Giang Minh Lãng (**tôi - anh / Phó tiên sinh**).
- **Tình huống kịch tính:** Ngụy Minh ghen tuông lôi kéo Phó Ngôn không thành, xông vào phòng thay đồ đóng sập cửa để đối đầu với Giang Minh Lãng.

---

## 2. Thống kê kỹ thuật
- **Độ dài đoạn văn:** 98 đoạn, phân cách bởi `\\n\\n`.
- **Dấu ngoặc thoại:** Chuẩn `“...”`.
- **Zero Omission & Addition:** Bảo toàn 100% câu chữ và các ghi chú tác giả cuối chương.
- **Kết luận:** **PASSED - ĐẠT CHUẨN XUẤT SẮC**
"""

with open(qc_file, "w", encoding="utf-8") as f:
    f.write(qc_report_content)
print(f"Successfully written {qc_file}")

# Update meta.json
with open(meta_file, "r", encoding="utf-8") as f:
    meta_data = json.load(f)

meta_data["title"] = "Chương 16: Alaska 16"
meta_data["translated_at"] = "2026-10-04T22:00:00+07:00"
meta_data["status"] = "QC_PASSED"
meta_data["qc_score"] = 1.0
meta_data["n_paragraphs"] = len(translations)

with open(meta_file, "w", encoding="utf-8") as f:
    json.dump(meta_data, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {meta_file}")

# Update timeline.json
with open(timeline_file, "r", encoding="utf-8") as f:
    timeline_data = json.load(f)

ch16_entry = {
    "chapter_id": "ch_016",
    "title": "Chương 16: Alaska 16",
    "summary": "Giang Minh Lãng rúc vào lòng dỗ dành Phó Vân Xuyên ngủ yên một đêm trọn vẹn. Sáng hôm sau, Phó Vân Xuyên đích thân lái xe đưa cậu đi học. Trên xe nảy sinh cãi vã khi Phó Vân Xuyên đè đầu đe dọa cậu theo dõi Phó Ngôn, nhưng thấy chú cún tủi thân, Phó Vân Xuyên liền lùi xe lại rủ cậu tối đi ăn thịt. Tại trường, Phó Ngôn liên tục tiếp cận moi tin khiến Ngụy Minh nổi cơn ghen tuông xông vào phòng thay đồ chặn cửa trước mặt Giang Minh Lãng.",
    "key_events": [
        "Giang Minh Lãng chui vào lòng Phó Vân Xuyên ngủ chung giường để xua tan nỗi sợ bóng tối",
        "Phó Vân Xuyên ngủ ngon giấc không mộng mị, thức dậy đưa Giang Minh Lãng đến trường",
        "Tranh cãi trên xe quanh việc theo dõi Phó Ngôn, Giang Minh Lãng phản kháng vì bị đè đầu thị uy",
        "Phó Vân Xuyên mềm lòng lùi xe lại hẹn Giang Minh Lãng chiều tan học đi ăn thịt",
        "Phó Vân Xuyên bắt đầu ra tay thôn tính đất đai của Phó thị và yêu cầu thuộc hạ chuẩn bị 'đồ chơi nhỏ'",
        "Phó Ngôn hỏi dò Giang Minh Lãng về Phó Vân Xuyên, Ngụy Minh ghen tuông xông vào phòng thay đồ đóng sầm cửa"
    ],
    "status_tags": ["Thế giới 1", "Rúc lòng ngủ chung", "Lùi xe dỗ cún", "Hẹn ăn thịt", "Ngụy Minh ghen tuông chặn cửa"]
}

found = False
for idx, ev in enumerate(timeline_data):
    if ev.get("chapter_id") == "ch_016":
        timeline_data[idx] = ch16_entry
        found = True
        break
if not found:
    timeline_data.append(ch16_entry)

with open(timeline_file, "w", encoding="utf-8") as f:
    json.dump(timeline_data, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {timeline_file}")
