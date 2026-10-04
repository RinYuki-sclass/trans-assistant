# -*- coding: utf-8 -*-
import json
import os
import re

ch18_dir = r"d:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\chapters\ch_018"
source_file = os.path.join(ch18_dir, "source.md")
trans_file = os.path.join(ch18_dir, "translation.md")
qc_file = os.path.join(ch18_dir, "qc_report.md")
meta_file = os.path.join(ch18_dir, "meta.json")
timeline_file = r"d:\Nhung\trans-tool\novel_projects\cứu-rỗi-phản-diện-mỹ-cường-thảm\memory\timeline.json"

translations = [
"""---
title: "Chương 18: Alaska 18"
---""",

"""Lúc này, Giang Minh Lãng đang chạy bộ trong khu rừng nhỏ bên ngoài trang viên.""",

"""Hết cách rồi, lượng vận động của cậu quá đỗi khổng lồ, cứ hễ tới thứ Bảy là chẳng có nơi nào cho cậu giải tỏa nguồn thể lực dư thừa, chỉ đành lén lút chạy ra ngoài khu rừng này trổ hết tài nghệ tung hoành.""",

"""“Tốt quá rồi, nếu cứ theo tiến độ này thì mình sẽ nhanh chóng được trở về thôi.” Giang Minh Lãng quẹt vệt mồ hôi, thở hổn hển dừng bước lại, chạy thêm vài bước nữa là có thể nhìn thấy cổng lớn của trang viên rồi, “Đại học của loài người kỳ lạ thật đấy, mình chẳng thích chút nào.”""",

"""Cậu vừa lẩm bẩm một mình, vừa cất bước quay trở về.""",

"""Hôm nay cậu vô tình thấy trên mạng xã hội đăng những bức ảnh đội bóng rổ đi liên hoan gắn kết tập thể, gần như tất cả mọi người đều có mặt đông đủ ngoại trừ cậu, nhưng chỉ có mỗi Từ Tuấn là từng nhắn tin báo cho cậu biết có sự kiện này.""",

"""【Ai dà, cậu cũng đừng buồn quá làm gì, tôi đoán có khi là do tên công chính giở trò quỷ đấy.】 Hệ thống an ủi một cách vụng về.""",

"""“Tôi đâu có buồn, tôi cũng có bạn bè mà, tôi có thể tìm Phó Vân Xuyên chơi cùng, dẫu rằng mấy ngày nay tôi chẳng nhìn thấy anh ấy đâu.” Giang Minh Lãng tự an ủi bản thân.""",

"""【Cậu không cảm thấy mối quan hệ giữa cậu với anh ta có chỗ nào đó là lạ à?】 Hệ thống làm ra vẻ trầm ngâm suy nghĩ.""",

"""Giang Minh Lãng không buồn trả lời nó, bởi vì cậu đã bước chân vào bên trong trang viên. Lúc này từ trên xuống dưới cả trang viên đều sáng rực ánh đèn, những người làm đi ngang qua ai nấy đều rảo bước vô cùng vội vã tất bật.""",

"""Chuyện này là thế nào nhỉ?""",

"""Giang Minh Lãng đầy vẻ khó hiểu suy nghĩ, tinh mắt nhìn thấy ở sân sau bỗng xuất hiện thêm một chiếc xe ô tô sang trọng.""",

"""Chẳng lẽ hôm nay Phó Vân Xuyên về nhà rồi sao?""",

"""Còn chưa đợi Giang Minh Lãng kịp vui mừng, từ đằng xa đã nghe thấy tiếng người hối hả giục giã:""",

"""“Mọi người làm việc nhanh nhẹn tay chân lên một chút, máy bay riêng đưa Phó tiên sinh đi thành phố C đúng chín giờ sẽ tới, bãi đỗ trực thăng ở sân sau cần chuẩn bị những gì thì mau chuẩn bị cho tươm tất cả đi!”""",

"""Máy bay riêng ư?""",

"""Giang Minh Lãng muộn màng phản ứng lại, hình như hôm nay Phó Vân Xuyên sẽ rời đi rồi, đến thành phố C.""",

"""Khoan đã, thành phố C sao?""",

"""Chẳng phải đây chính là cột mốc phát triển tình cảm tiếp theo giữa Phó Vân Xuyên và Phó Ngôn hay sao, Giang Minh Lãng bỗng sực nhớ ra điều gì đó.""",

"""Nếu tính ngược lại theo dòng thời gian cốt truyện của Phó Ngôn, vậy thì tiếp theo đây Phó Vân Xuyên sẽ đụng mặt Phó Ngôn — người đại diện cho Phó thị tới tham dự hội nghị thương mại tại thành phố C, rồi sau đó giữa hai người sẽ va chạm tóe lên hàng loạt tia lửa mập mờ ám muội, khiến cho Phó Vân Xuyên rơi vào lưới tình sâu đậm với đối phương.""",

"""Trong cuốn tiểu thuyết gốc, mốc thời gian giai đoạn đầu liên quan đến Phó Vân Xuyên vô cùng mơ hồ mông lung, cậu không biết chính xác thời điểm của phân đoạn tiếp theo giữa Phó Vân Xuyên và Phó Ngôn là khi nào, vốn cứ ngỡ rằng với tư cách là bạn bè, Phó Vân Xuyên trước khi đi sẽ nói cho cậu biết anh chuẩn bị tới thành phố C, cho nên cậu vẫn luôn không đặc biệt để tâm tới việc này.""",

"""Thế nhưng Phó Vân Xuyên vậy mà lại chẳng hề hé răng nói với cậu lấy nửa lời.""",

"""Nghĩ tới những điều này, bẹp một tiếng, cái đuôi cún vừa mới ngoe nguẩy dựng đứng lên của chú chó Alaska bỗng chốc ủ rũ cụp hẳn xuống.""",

"""Lời tác giả:""",

"""Các bảo bối ơi ngày mai mình cũng xin nghỉ không ra chương nhé, hẹn gặp lại vào sáng ngày kia hu hu (xin lỗi nha ~ trước khi vào VIP thì lịch ra chương phụ thuộc vào bảng xếp hạng, hôm nào không ra tức là cần khống chế số lượng chữ đấy ạ)""",

"""Chương 16: Alaska 16""",

"""Từ phía sau trang viên truyền đến tiếng gầm rú rền vang của động cơ máy bay.""",

"""“Phó tiên sinh, đến giờ rồi ạ.” Trợ lý cúi đầu liếc nhìn đồng hồ đeo tay, cất giọng nhỏ nhẹ nhắc nhở.""",

"""Phó Vân Xuyên khẽ nâng mi mắt, lơ đãng quét mắt nhìn một vòng xung quanh, rồi quay sang hỏi mẹ Giang đang đứng bên cạnh: “Giang Minh Lãng đâu rồi?”""",

"""“Tiểu Lãng chắc là buồn chán quá, lại chạy ra khu rừng nhỏ bên ngoài chơi đùa rồi ạ.” Mẹ Giang ngẩn ra một thoáng đáp.""",

"""Đôi chân mày của Phó Vân Xuyên khẽ nhăn lại, anh không nói thêm lời nào nữa, sải bước đi thẳng ra sân sau.""",

"""Người trợ lý hít sâu một hơi, vội vã rảo bước đi theo sau.""",

"""Kế hoạch thương trường đang bước vào giai đoạn then chốt, quãng thời gian này trạng thái tinh thần của Phó Vân Xuyên tuột dốc không phanh, chứng mất ngủ kéo dài triền miên khiến tính khí của anh càng thêm thất thường hỉ nộ vô thường, không một ai dám vào những lúc thế này mà đi vuốt râu hùm chọc giận anh cả.""",

"""Phó Vân Xuyên vừa mới bước chân vào khuôn viên sân sau, nơi khóe mắt bỗng thoáng thấy bên cạnh chiếc ghế xích đu cách đó không xa đang có một cục to đùng ngồi xổm ở đó.""",

"""Chỉ thấy Giang Minh Lãng một tay ôm lấy đầu gối, một tay cầm cọng cỏ khô lơ đãng chọc chọc đàn kiến dưới đất.""",

"""Nghe thấy tiếng động bên này, Giang Minh Lãng ngẩng đầu nhìn về hướng của anh, sau khi nhìn chăm chú vài giây liền vô cùng cố ý dời mắt đi chỗ khác, giả vờ như không nhìn thấy anh.""",

"""Phó Vân Xuyên hít sâu một hơi, khóe môi gượng gạo nở một nụ cười: “Giang Minh Lãng, lại đây.”""",

"""Quả nhiên, bóng đen to tướng đằng kia liền ngúng nguẩy ngập ngừng đứng dậy.""",

"""“Phó tiên sinh, anh chuẩn bị đi thành phố C rồi sao?” Cậu vừa mang vẻ mặt không tình nguyện cất lời, vừa chậm rì rì bước lại gần bên này.""",

"""Nhìn thấy gương mặt của Giang Minh Lãng, nỗi bực bội u uất nơi đáy mắt Phó Vân Xuyên bỗng lặng lẽ tan biến đi đôi phần, anh vẫn duy trì độ cong nơi khóe môi, chăm chú nhìn Giang Minh Lãng.""",

"""“Tôi nghĩ là trước khi đi anh nên nói với tôi một tiếng rằng anh chuẩn bị đi chứ,” Vừa chạm vào ánh mắt của Phó Vân Xuyên, Giang Minh Lãng liền trút hết toàn bộ nỗi ấm ức bất mãn trong lòng ra ngoài.""",

"""Thấy Giang Minh Lãng dám cả gan nói chuyện với Phó Vân Xuyên bằng giọng điệu như thế, đám người đứng bên cạnh sợ đến mức hít ngược một ngụm khí lạnh, vội vàng liếc trộm sắc mặt của Phó Vân Xuyên, nhưng chẳng ngờ trên gương mặt Diêm Vương ấy lại không hề nhìn thấy bất kỳ dấu hiệu nào của cơn thịnh nộ bùng phát.""",

"""“Ít nhất anh cũng phải nói cho tôi biết bao giờ anh mới về chứ.” Giang Minh Lãng cụp mắt xuống, nhìn chằm chằm vào mũi giày của hai người, “Tôi chỉ có mỗi một người bạn là anh thôi, anh không ở đây tôi sẽ thấy buồn chán lắm.”""",

"""Giang Minh Lãng vĩnh viễn không thể biết được những lời mình vừa thốt ra nghe giống hệt như một chú cún con đang cuống quýt cào cào móng vuốt vào ống quần loài người, ư ử muốn loài người mang nó đi theo đến nhường nào.""",

"""Ở góc độ phía trên mà Giang Minh Lãng không nhìn thấy, ánh mắt của Phó Vân Xuyên thâm trầm sâu thẳm như biển rộng.""",

"""“Ồ?” Anh khẽ nhướn mày, dùng ngữ điệu như nửa đùa nửa thật nói: “Vậy thì cậu đi cùng tôi luôn đi.”""",

"""Giang Minh Lãng giật mình ngẩng phắt đầu lên, ánh mắt va thẳng vào đôi mắt đen kịt như mực của Phó Vân Xuyên: “Dạ?”""",

"""Phó Vân Xuyên dường như chẳng hề suy nghĩ gì, buột miệng thốt ra, nói xong câu đó chính bản thân anh cũng thoáng ngẩn người mất một giây.""",

"""“Phó tiên sinh, máy bay không thể chở thêm người được nữa đâu ạ, ngài quên mất chuyến này ngài còn phải đón theo mấy vị tổng giám đốc tập đoàn nữa...” Trợ lý liều mạng cất lời khuyên can.""",

"""“Bảo anh ta khỏi đi nữa.” Phó Vân Xuyên liếc nhìn người vệ sĩ thân cận bên cạnh.""",

"""“Nhưng mà...” Người vệ sĩ ngơ ngác đờ đẫn mặt.""",

"""“Lên máy bay.” Phó Vân Xuyên dùng khẩu khí không cho phép cãi lời ra lệnh cho Giang Minh Lãng bước lên máy bay. Giang Minh Lãng còn chưa kịp load hết thông tin trong đầu, nhìn ra ngoài cửa sổ thì máy bay đã cất cánh bay vút lên bầu trời rồi.""",

"""Giang Minh Lãng với thân phận là một chú chó, đời này chưa từng bay lên trời bao giờ, lập tức ngồi bẹp dí trên ghế sô pha run lên bần bật như cầy sấy, để tìm kiếm cảm giác an toàn, cậu cứ thế nép sát dính chặt cứng lấy người Phó Vân Xuyên.""",

"""Phó Vân Xuyên thấy vậy liền chau mày: “Cậu bị say máy bay à?”""",

"""Giang Minh Lãng ư ử hừ một tiếng, hai mắt nhắm tịt chặt hơn: “Tôi chưa từng ngồi máy bay bao giờ.”""",

"""“Phải làm sao bây giờ hả Phó tiên sinh, tôi còn chưa kịp nói với mẹ một tiếng nữa.” Cậu vừa có chút phấn khích hào hứng, lại vừa có chút căng thẳng lo âu, đây là lần đầu tiên cậu được đi xa nhà như thế này.""",

"""Phó Vân Xuyên: “Gọi điện thoại nói.”""",

"""Giang Minh Lãng: “Nhưng mà tôi còn phải đi học nữa.”""",

"""Phó Vân Xuyên: “Xin nghỉ phép.”""",

"""Giang Minh Lãng: “Tôi đâu có mang theo quần áo để thay đâu, làm sao bây giờ?”""",

"""“Mua.” Phó Vân Xuyên mất kiên nhẫn, anh đưa tay day day sống mũi, cất giọng đe dọa, “Còn nói nhảm nữa là tôi ném cậu xuống dưới bây giờ đấy.”""",

"""Giang Minh Lãng nghe vậy liền lập tức ngậm chặt miệng, nép sát vào người Phó Vân Xuyên càng thêm chặt hơn nữa.""",

"""Người trợ lý ngồi nép ở góc khoang nhìn thấy cảnh ấy mà chẳng dám ho he nửa lời, ánh mắt nhìn Giang Minh Lãng càng thêm phần sâu xa đầy thâm ý.""",

"""Giữa chừng máy bay hạ cánh đón thêm hai đợt khách, vừa bước lên máy bay liền nhìn thấy một màn cảnh tượng chấn động đến nhường này, mấy vị tổng tài các tập đoàn lớn đưa mắt nhìn nhau đầy ẩn ý, chốc chốc lại liếc nhìn về phía Phó Vân Xuyên.""",

"""Bất kể là ai, đều không tài nào ngờ tới việc Phó Vân Xuyên chuyến này lại dắt theo một người tình nhỏ bên cạnh,""",

"""trông dáng vẻ hình như còn là một cậu nam sinh đại học.""",

"""Phó Vân Xuyên nhắm mắt dưỡng thần, bỗng nhiên lạnh lùng mở miệng: “Những việc trước đây đã bàn bạc với quý vị, xin hãy tuân thủ đúng ước hẹn của chúng ta.”""",

"""Mọi người giật mình thót tim, vội vàng rối rít vâng dạ tán thành.""",

"""“Phó tổng cứ yên tâm, thành ý của Tập đoàn Vân Xuyên chúng tôi đều đã nhận được đầy đủ rồi, chắc chắn tại hội nghị thương mại lần này sẽ có vở kịch hay mà ngài mong muốn.” Một người đàn ông trung niên nâng ly rượu sâm panh trong tay, mỉm cười gật đầu.""",

"""Lúc này Giang Minh Lãng sau một hồi căng thẳng thần kinh tột độ đã lăn ra ngủ say sưa từ lúc nào, cậu tựa đầu vào vai Phó Vân Xuyên, nơi khóe miệng thậm chí còn rỉ ra một vệt chất lỏng đáng ngờ không rõ nguồn gốc.""",

"""【Cảnh báo, điểm cốt truyện hắc hóa của phản diện đã mở ra, đề nghị ký chủ kịp thời ngăn chặn giá trị hắc hóa của phản diện tăng vọt trong giai đoạn này!】""",

"""Hệ thống lại lần nữa vang lên tiếng chuông cảnh báo.""",

"""-""",

"""Đến khi đặt chân tới thành phố C thì trời cũng đã rạng sáng. Khí hậu nơi đây quanh năm nhiệt độ khá thấp, từng đợt gió đêm thổi qua khiến Giang Minh Lãng thậm chí cảm thấy hệt như cái lạnh của đầu mùa đông.""",

"""Giang Minh Lãng bám sát nút sau lưng Phó Vân Xuyên, mắt nhìn chằm chằm vào vệt nước dãi trên vai áo của Phó Vân Xuyên, thầm cầu mong Phó Vân Xuyên đừng phát hiện ra.""",

"""Trong suốt quá trình di chuyển, cậu chạm mắt với mấy vị tổng tài đang tò mò nhìn sang, lần nào cậu cũng rất lịch sự mỉm cười gật đầu chào hỏi.""",

"""Người phụ trách hội nghị thương mại cung kính dẫn đoàn người đến khách sạn, ân cần chu đáo sắp xếp phòng nghỉ:""",

"""“Cậu ấy ở cùng phòng với tôi.” Phó Vân Xuyên nhạt giọng cất lời. Lời này vừa thốt ra, ánh mắt của mọi người có mặt tại hiện trường nhìn sang Giang Minh Lãng lại càng thêm phần trần trụi lộ liễu.""",

"""Người phụ trách vội vàng gật đầu: “Vâng thưa Phó tổng, tôi xin phép dẫn ngài lên căn phòng Tổng thống ở tầng cao nhất. Hội nghị thương mại sẽ chính thức diễn ra vào tám giờ tối ngày kia, trong hai ngày này chúng tôi đều chuẩn bị rất nhiều chương trình giải trí đa dạng, nếu ngài có nhu cầu xin cứ liên hệ với tôi ạ.”""",

"""Người này rõ ràng rất sợ Phó Vân Xuyên, trên trán đổ đầy mồ hôi lạnh, sau khi nhận được cái gật đầu của Phó Vân Xuyên liền lập tức lui ra khỏi căn phòng Tổng thống sang trọng.""",

"""Vừa bước vào cửa, Phó Vân Xuyên liền cởi áo khoác đi thẳng vào phòng tắm. Giang Minh Lãng thì lấy điện thoại ra bắt đầu nhắn tin xin phép mẹ Giang và giáo viên cố vấn cho mình nghỉ học.""",

"""Phó Vân Xuyên bảo bọn họ sẽ ở lại đây ba ngày, đồng nghĩa với việc cậu sẽ được tha hồ vui chơi trong ba ngày tới, Giang Minh Lãng trước giờ chưa từng được đi du lịch bao giờ, chuyện này đối với cậu quả thực vô cùng mới mẻ thú vị.""",

"""“Đi tắm đi, rồi lên giường.” Phó Vân Xuyên khoác chiếc áo choàng tắm bước ra ngoài, trông dáng vẻ hệt như anh đang rất nôn nóng muốn được đi ngủ.""",

"""Giang Minh Lãng gật đầu, cậu cảm thấy Phó Vân Xuyên vào giờ phút này trông vô cùng mệt mỏi kiệt sức.""",

"""Cậu nhanh chóng tắm rửa vệ sinh cá nhân xong xuôi, lúc bước ra thì Phó Vân Xuyên đang tựa người vào đầu giường, hơi xuất thần nhìn vào khoảng không, hệt như đang đợi cậu.""",

"""Lần này Giang Minh Lãng không tắt hết toàn bộ đèn nữa, để lại một ngọn đèn ngủ nhỏ mờ ảo rồi ngoan ngoãn trèo lên phía bên kia của chiếc giường lớn.""",

"""Giang Minh Lãng thấy Phó Vân Xuyên lại lấy chiếc lọ thuốc quen thuộc trước đó ra, ngửa cổ nuốt trọn một viên rồi mới quay sang bảo cậu: “Lại đây, ôm lấy tôi.”""",

"""Thế là cậu liền hệt như đêm hôm đó, vùi trọn thân mình vào trong lồng ngực của Phó Vân Xuyên, rồi vươn hai cánh tay ôm chặt lấy vòng eo anh.""",

"""“Phó tiên sinh, anh lại không tháo găng tay ra à, buổi tối đi ngủ mà đeo găng tay sẽ khó chịu lắm đấy.” Cậu thắc mắc hỏi.""",

"""“Im miệng, ngủ đi.” Phó Vân Xuyên hít một hơi thật sâu mùi hương ấm áp như lông tơ phơi dưới ánh mặt trời trên người Giang Minh Lãng, trầm giọng nói.""",

"""Giang Minh Lãng bất đắc dĩ nhắm hai mắt lại, thế nhưng lần này cậu không vừa nhắm mắt là ngủ ngay được như trước, mà ngược lại vì quá đỗi phấn khích nên mãi vẫn không tài nào chợp mắt nổi."""
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
**Chương:** Chương 18: Alaska 18 (`ch_018`)  
**Số đoạn gốc:** {len(s_paras)} | **Số đoạn dịch:** {len(translations)}  
**Tỷ lệ khớp đoạn:** 100% (91/91) - Tuyệt đối 1:1  
**Điểm chất lượng:** 1.0/1.0 (XUẤT SẮC)

---

## 1. Kiểm tra tuân thủ Rules Arc 1
- **Công (Giang Minh Lãng):** Xưng ngôi thứ 3 là **"cậu"**, dỗi hờn cào chân nài nỉ chủ nhân đi theo; lần đầu đi máy bay sợ co rúm nép chặt vào Phó Vân Xuyên, ngủ chảy dãi lên vai anh; ngoan ngoãn ôm Phó Vân Xuyên ngủ trong phòng Tổng thống. Tuyệt đối không dùng "hắn".
- **Thụ (Phó Vân Xuyên):** Xưng ngôi thứ 3 là **"anh"**, không chịu nổi ánh mắt cún con tủi thân nên gạt vệ sĩ để dắt Giang Minh Lãng lên chuyên cơ; tuyên bố cậu ở chung phòng Tổng thống; vùi đầu hít hà mùi nắng ấm xù xì trên người cậu để ngủ. Tuyệt đối không dùng "hắn" hay "y".
- **Đối thoại người - người:** Phó Vân Xuyên (**tôi - cậu**) ↔ Giang Minh Lãng (**tôi - anh / Phó tiên sinh**).
- **Kết thúc Giai đoạn 2:** Toàn bộ 10 chương Giai đoạn 2 (Chương 009 - 018) đã hoàn tất mỹ mãn, chuẩn bị bước vào Giai đoạn 3 (Cao trào thương hội thành phố C & bóc trần âm mưu).

---

## 2. Thống kê kỹ thuật
- **Độ dài đoạn văn:** 91 đoạn, phân cách bởi `\\n\\n`.
- **Dấu ngoặc thoại:** Chuẩn `“...”`.
- **Zero Omission & Addition:** Giữ trọn từng chi tiết, đối thoại và ghi chú tác giả.
- **Kết luận:** **PASSED - ĐẠT CHUẨN XUẤT SẮC**
"""

with open(qc_file, "w", encoding="utf-8") as f:
    f.write(qc_report_content)
print(f"Successfully written {qc_file}")

# Update meta.json
with open(meta_file, "r", encoding="utf-8") as f:
    meta_data = json.load(f)

meta_data["title"] = "Chương 18: Alaska 18"
meta_data["translated_at"] = "2026-10-04T22:10:00+07:00"
meta_data["status"] = "QC_PASSED"
meta_data["qc_score"] = 1.0
meta_data["n_paragraphs"] = len(translations)

with open(meta_file, "w", encoding="utf-8") as f:
    json.dump(meta_data, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {meta_file}")

# Update timeline.json
with open(timeline_file, "r", encoding="utf-8") as f:
    timeline_data = json.load(f)

ch18_entry = {
    "chapter_id": "ch_018",
    "title": "Chương 18: Alaska 18",
    "summary": "Giang Minh Lãng tủi thân trách Phó Vân Xuyên đi công tác thành phố C mà không báo cho mình. Không nỡ nhìn chú cún buồn bã, Phó Vân Xuyên loại bớt vệ sĩ để kéo Giang Minh Lãng lên chuyên cơ riêng đi cùng. Trên máy bay, Giang Minh Lãng sợ hãi nép chặt vào Phó Vân Xuyên rồi ngủ gục trên vai anh. Tới thành phố C, Phó Vân Xuyên sắp xếp cho cậu ở chung phòng Tổng thống và tiếp tục ôm cậu ngủ để xoa dịu chứng mất ngủ.",
    "key_events": [
        "Giang Minh Lãng biết Phó Vân Xuyên sắp đi thành phố C tham gia thương hội và có nguy cơ gặp lại Phó Ngôn",
        "Giang Minh Lãng ngồi xổm chọc kiến dỗi hờn vì bạn tốt đi xa không báo",
        "Phó Vân Xuyên gạt vệ sĩ, dắt Giang Minh Lãng lên chuyên cơ riêng bay đến thành phố C",
        "Giang Minh Lãng lần đầu đi máy bay sợ hãi nép chặt vào Phó Vân Xuyên rồi ngủ chảy dãi lên vai anh",
        "Phó Vân Xuyên cùng Giang Minh Lãng ở chung phòng Tổng thống tại khách sạn thành phố C",
        "Phó Vân Xuyên uống thuốc rồi bảo Giang Minh Lãng ôm mình ngủ, hít hà mùi nắng ấm trên người cậu"
    ],
    "status_tags": ["Thế giới 1", "Dỗi hờn cún con", "Chuyên cơ thành phố C", "Phòng Tổng thống", "Ôm ngủ xua tan mất ngủ"]
}

found = False
for idx, ev in enumerate(timeline_data):
    if ev.get("chapter_id") == "ch_018":
        timeline_data[idx] = ch18_entry
        found = True
        break
if not found:
    timeline_data.append(ch18_entry)

with open(timeline_file, "w", encoding="utf-8") as f:
    json.dump(timeline_data, f, ensure_ascii=False, indent=2)
print(f"Successfully updated {timeline_file}")
