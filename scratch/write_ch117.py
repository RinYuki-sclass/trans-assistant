# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_117\translation.md"

paras = [
    # 000
    "Đầu ngón tay thô ráp ấm áp chầm chậm vuốt ve sau vành tai Kỷ Cảnh, hệt như đang vén lấy một lọn tóc dài vốn chẳng hề tồn tại.",
    # 001
    "Rặng mây đỏ như thủy triều cuồn cuộn ùa lên hai gò má Kỷ Cảnh, cậu vạn lần không ngờ có một ngày bản thân lại bị Lục Tư Niên trêu chọc đến mức đỏ bừng cả mặt.",
    # 002
    "“Anh... anh đang nghĩ cái gì đấy...”",
    # 003
    "Kỷ Cảnh lắp ba lắp bắp nói.",
    # 004
    "Lục Tư Niên hồi thần lại, khẽ lắc đầu: “Không có gì.”",
    # 005
    "“Có phải anh rất muốn tôi để tóc dài không?” Kỷ Cảnh dần dần bình tĩnh trở lại.",
    # 006
    "Lục Tư Niên không biết nói dối, Kỷ Cảnh nhìn thấy rành rành câu trả lời khẳng định từ trong đôi mắt anh.",
    # 007
    "“Cũng không phải là không thể để...” Cậu tha cho Lục Tư Niên, quay người ngồi trở lại nắp mui xe, thuận miệng buông một câu.",
    # 008
    "Lúc này Lục Tư Niên lại im bặt không tiếng động, Kỷ Cảnh lặng lẽ ngước nhìn dải Ngân Hà bao la vô tận, trong khóe mắt liếc thấy Lục Tư Niên quay trở lại trong xe, lấy ra một thứ gì đó.",
    # 009
    "Anh trở lại bên cạnh cậu: “Kỷ Cảnh...” Anh gọi, Kỷ Cảnh nghiêng đầu, thấy anh từ trong một chiếc hộp sắt có niên đại cổ xưa lấy ra một chiếc vòng ngọc trắng.",
    # 010
    "“Đây là di vật duy nhất mẹ tôi để lại.” Bà bảo tôi phải tặng cho người vợ tương lai của mình, đại diện cho lời chúc phúc và che chở của bà, những lời phía sau Lục Tư Niên không nói ra, anh nhìn Kỷ Cảnh, khẽ nói: “Tôi muốn tặng cho em.”",
    # 011
    "Kỷ Cảnh sững sờ ngơ ngác, đầu óc còn chưa kịp xoay chuyển thì chiếc vòng ngọc mát lạnh đã tròng vào cổ tay cậu.",
    # 012
    "Thứ này nhất định là để lại cho vợ của Lục Tư Niên rồi đúng không?",
    # 013
    "Kỷ Cảnh theo bản năng nghĩ thầm trong bụng.",
    # 014
    "Lục Tư Niên đây là có ý gì, chẳng lẽ là đang ngụ ý ám chỉ, muốn cầu hôn cậu sao?",
    # 015
    "Đợi nửa ngày trời không thấy Lục Tư Niên nói câu tiếp theo, Kỷ Cảnh không nhịn được: “Anh không có gì muốn nói nữa à?”",
    # 016
    "Lục Tư Niên nhìn cậu một lát, rồi lắc đầu.",
    # 017
    "Kỷ Cảnh có chút bực mình, ngoảnh mặt đi không thèm nói chuyện nữa.",
    # 018
    "Một lát sau, cậu bất thình lình mở miệng: “Lục Tư Niên, không biết anh có tin hay không, nhưng tôi muốn nói cho anh biết ban đầu tôi không phải cố ý lăng mạ mẹ anh đâu, nói cách khác, người mắng mẹ anh không phải là tôi, còn nữa, tôi phải thừa nhận, lúc mới bắt đầu giả dạng làm Dịch Nam tiếp cận anh là có mưu đồ khác, nhưng sau này tôi thực sự đã thích anh rồi, anh đừng giận nhé...”",
    # 019
    "“Tôi tin.” Lục Tư Niên ngắt lời cậu, “Em đã thay đổi rất nhiều, hôm đó Kỷ tiểu thư cũng từng nhắc tới với tôi, cô ấy cảm thấy em của hiện tại mới chính là em.”",
    # 020
    "“Em thích tôi, tôi rất vui lòng.”",
    # 021
    "“À, ồ, được thôi, hai người tin tôi là tốt rồi.”",
    # 022
    "Kỷ Cảnh thất thần chốc lát, cố ý né tránh ánh mắt của Lục Tư Niên, dùng mũi giày đá nhẹ vào bãi cát gồ ghề dưới chân.",
    # 023
    "Hóa ra Kỷ Vân Hy cũng không hề vô tâm vô phế đến mức đó.",
    # 024
    "Sau đó hai người lại ngắm bầu trời thêm một lúc, Lục Tư Niên nhìn thời gian rồi lái xe đưa Kỷ Cảnh trở về.",
    # 025
    "Mấy ngày sau đó ngày nào Kỷ Cảnh cũng nhận được một bó hoa tươi, cùng với những màn bày tỏ tình cảm vụng về của Lục Tư Niên.",
    # 026
    "Thế nhưng Kỷ Cảnh mãi vẫn chưa đợi được Lục Tư Niên nói ra điều mà cậu muốn nghe nhất.",
    # 027
    "Bước ngoặt của sự việc diễn ra vào thứ Bảy tuần này, theo quy chế của Đệ tam quân đoàn, nửa tháng sẽ được nghỉ một ngày, Chủ nhật vừa vặn chính là ngày đó.",
    # 028
    "Thứ Bảy Kỷ Cảnh đang cùng các Alpha của Đội Một tiến hành diễn tập thao tác chiến hạm, vừa đáp đất xuống, liền từ xa nhìn thấy bóng hình Lục Tư Niên đang sải bước đi tới.",
    # 029
    "Vấn đề nằm ở chỗ, lần này người đi bên cạnh Lục Tư Niên không phải là Chu Độ, mà là một người phụ nữ eo thon chân dài.",
    # 030
    "Gương mặt người phụ nữ kia treo nụ cười mang vài phần quyến rũ, khuôn mặt xinh đẹp khiến người ta rất khó lòng không chú ý tới cô ta.",
    # 031
    "Kỷ Cảnh nhớ rõ người phụ nữ này là ai, trước đây trốn trong phòng đoàn trưởng của Lục Tư Niên từng nhìn thấy vài lần, là tân tổng chỉ huy, một nữ Alpha tên là Thư Nghiên.",
    # 032
    "Lục Tư Niên rõ ràng chỉ là tình cờ đi ngang qua, không hề phát hiện ra Kỷ Cảnh đang huấn luyện ở phía này, còn về việc cụ thể hai người nói những gì thì do khoảng cách quá xa nên Kỷ Cảnh không nghe thấy được, nhưng từ xa nhìn thấy nữ Alpha kia định khoác vai bá cổ Lục Tư Niên, lại bị Lục Tư Niên né tránh ra.",
    # 033
    "Không chỉ riêng Kỷ Cảnh chú ý tới, mà bên cạnh còn có không ít Alpha cũng nhìn thấy cảnh tượng này.",
    # 034
    "Thế là khó tránh khỏi có kẻ không kìm nổi tính hóng hớt bàn tán xôn xao,",
    # 035
    "“Kia chẳng phải là Lục Tư Niên với Thư Nghiên sao, nói đi cũng phải nói lại, bóng lưng hai người trông xứng đôi phết nhỉ!”",
    # 036
    "“Hê, đúng thế thật đấy, trước đây lúc Lục Tư Niên còn làm tổng chỉ huy thì Thư Nghiên chính là do anh ta đích thân tuyển vào doanh chỉ huy, làm Lâm Diên Sơn tức đến nổ đom đóm mắt, khi đó tao đã thấy hai người có tia lửa rồi, chỉ tiếc là giới tính không hợp...”",
    # 037
    "“Giới tính không hợp cái gì, mày lại quên Lục Tư Niên là một Omega rồi à!”",
    # 038
    "“Thế chẳng phải chuẩn bài rồi sao! Một nam một nữ, một A một O, Thư Nghiên đánh đấm cũng đỉnh chóp, ơ kìa, Kỷ Cảnh mày không tập nữa à?”",
    # 039
    "...",
    # 040
    "Bài huấn luyện này vốn dĩ là nội dung cuối cùng của ngày hôm nay, Kỷ Cảnh tập xong liền cầm lấy chai nước bước vào một góc nghỉ ngơi, rõ ràng biết Lục Tư Niên không thể nào có gì với nữ Alpha kia, nhưng nghe đám ngốc kia gán ghép bừa bãi là trong lòng lại thấy tức anh ách buồn nôn.",
    # 041
    "Chậc, cái tên Lục Tư Niên này không biết đang giở trò quỷ gì nữa.",
    # 042
    "Cậu mở thiết bị đầu cuối ra",
    # 043
    "【Anh Cảnh của mày】: Đang làm gì đấy.",
    # 044
    "Lục Tư Niên mãi một hồi lâu sau mới trả lời",
    # 045
    "【Khúc Gỗ Lục】: Hình ảnh jpg.",
    # 046
    "【Khúc Gỗ Lục】: Đệ nhất quân đoàn có người tới, đang tiếp đón.",
    # 047
    "Kỷ Cảnh liếc nhìn một cái rồi không thèm gõ chữ nữa, ngồi im ở đó đợi đội trưởng thổi còi tan buổi tập.",
    # 048
    "Tập luyện xong Kỷ Cảnh trở về ký túc xá, mới sực nhớ ra hôm nay Lục Tư Niên vẫn chưa tặng hoa cho mình.",
    # 049
    "Kỷ Cảnh nắm thiết bị đầu cuối, tung lên không trung vẽ một đường cong tuyệt đẹp trong lòng bàn tay, thầm nghĩ:",
    # 050
    "Chẳng phải chỉ là một người phụ nữ thôi sao, có thể sánh bằng Kỷ Cảnh cậu chắc?",
    # 051
    "Thế là cậu đứng dậy, từ trên đỉnh tủ quần áo lôi xuống một chiếc vali hành lý, chiếc vali này là thứ cậu từng đắn đo nửa ngày trời cuối cùng quyết định mang theo cùng, không ngờ hôm nay lại thực sự có đất dụng võ.",
    # 052
    "...",
    # 053
    "Buổi tối, Lục Tư Niên từ phòng tiếp tân bước ra, tùy tiện ăn vài miếng lương khô quân dụng, quay lại phòng đoàn trưởng cầm lấy bó hoa rồi sải bước về phía ký túc xá.",
    # 054
    "Anh dự định về phòng thay một bộ quần áo khác rồi mới đi tìm Kỷ Cảnh.",
    # 055
    "Không ngờ Thư Nghiên lại cứ bám riết không tha đi theo sau lưng anh.",
    # 056
    "“Đoàn trưởng, nửa đêm nửa hôm ngài ôm bó hoa hồng to tướng thế này đi đâu đấy?” Thư Nghiên hoàn toàn chẳng biết nhìn sắc mặt, ton hót lon ton chạy theo sau lưng Lục Tư Niên gặng hỏi,",
    # 057
    "“Đệt mợ, không phải ngài giấu người đẹp trong phòng ký túc xá đấy chứ?!”",
    # 058
    "Nhìn Lục Tư Niên đi về hướng ký túc xá, Thư Nghiên kinh hãi thốt lên.",
    # 059
    "Phòng ký túc xá của Thư Nghiên cách phòng Lục Tư Niên không xa, thấy Lục Tư Niên không thèm để ý đến mình liền hạ quyết tâm bám theo Lục Tư Niên để tìm hiểu cho ra ngô ra khoai.",
    # 060
    "Lục Tư Niên đang bận gửi tin nhắn, không chú ý đến cô ta",
    # 061
    "【Lục Tư Niên】: Tôi về ký túc xá rồi, tối nay qua tặng hoa cho em.",
    # 062
    "Anh chàng giao hoa Lục Tư Niên đợi nửa ngày không thấy Kỷ Cảnh trả lời, chân mày khẽ nhíu lại, bước chân cũng nhanh hơn.",
    # 063
    "“Ấy, ngài đi chậm chút coi.”",
    # 064
    "Thư Nghiên chạy thục mạng đuổi theo, vừa đuổi vừa gọi, đột nhiên Lục Tư Niên phía trước khựng phắt bước chân lại, Thư Nghiên vội vàng phanh gấp, tránh được một màn va chạm thảm khốc.",
    # 065
    "“Sao thế?” Cô ta vừa hỏi, vừa nương theo ánh mắt của Lục Tư Niên nhìn qua.",
    # 066
    "Cô ta hít ngược một hơi khí lạnh——",
    # 067
    "Một cô gái mặc chiếc váy dài trắng tinh khôi đang điềm đạm đáng yêu ngồi trước cửa phòng ký túc xá của Lục Tư Niên, mái tóc đen dài chấm eo như dòng thác xõa tung trên nền đất, cô ôm đầu gối cuộn tròn lại, từ góc độ của bọn họ chỉ có thể nhìn thấy chiếc cằm thanh tú trắng nõn của cô gái, cùng đôi môi đỏ mọng tươi tắn, đen, trắng, đỏ, ba gam màu đan xen tạo nên một vẻ đẹp mong manh dễ vỡ.",
    # 068
    "Cô hệt như một chú cún con không nơi nương tựa, lặng lẽ rúc vào góc tường chờ đợi chủ nhân trở về nhà.",
    # 069
    "Tựa như nghe thấy tiếng bước chân ngay trong gang tấc, cô gái chầm chậm ngẩng đầu lên——",
    # 070
    "“Mẹ kiếp, thế này cũng quá đỗi xinh đẹp rồi đấy chứ...”",
    # 071
    "Thư Nghiên còn chưa kịp cảm thán xong, liền bị những lời tiếp theo của cô gái đánh cho cháy đen thui cả trong lẫn ngoài",
    # 072
    "“Ông xã, anh đã về rồi sao...”",
    # 073
    "Cô gái khẽ nắn giọng dịu dàng cất tiếng gọi, đôi mắt nhìn về phía Lục Tư Niên lấp lánh những ánh sáng lung linh vỡ vụn.",
    # 074
    "Ô ô... ô... ông xã??!",
    # 075
    "Thư Nghiên phóng ánh mắt hình viên đạn sang Lục Tư Niên bên cạnh, chỉ thấy Lục Tư Niên cũng đực mặt đứng sững tại chỗ, hai mắt gần như dính chặt lên người cô gái.",
    # 076
    "Lục Tư Niên cử động, anh sải bước tiến lên, bế bổng cô gái từ dưới đất lên, giọng nói có chút khàn đặc: “Tại sao... lại ăn mặc thế này tới tìm tôi.”",
    # 077
    "“Anh không thích sao?” Cô gái hỏi ngược lại.",
    # 078
    "“Ừm, thích.” Lục Tư Niên lại nói, phía sau bọn họ nói những gì Thư Nghiên đã không còn nghe thấy được nữa, chỉ thấy Lục Tư Niên mở cửa ký túc xá, ôm cô gái bước vào trong, cô gái vừa vào phòng liền đóng sầm cửa lại, bỏ mặc một mình Thư Nghiên đứng bên ngoài nhặt lại chiếc cằm vừa rớt của mình.",
    # 079
    "Kỷ Cảnh bị ôm chặt cứng kéo vào trong phòng, đèn còn chưa kịp bật thì những nụ hôn dày đặc của Lục Tư Niên đã rơi xuống tới tấp.",
    # 080
    "Kỷ Cảnh bị hôn đến mức không thở nổi, thầm nghĩ Lục Tư Niên quả nhiên thích nhất cái dáng vẻ này của cậu.",
    # 081
    "Cậu lần mò đập bốp một cái bật đèn sáng trưng, sau đó đẩy Lục Tư Niên ra.",
    # 082
    "“Người phụ nữ kia là ai?” Kỷ Cảnh đi thẳng vào vấn đề, chất vấn: “Hôm nay tôi nhìn thấy anh đi cùng cô ta.”",
    # 083
    "Lục Tư Niên thở dốc nặng nề, chiếc kính nửa gọng đen trên sống mũi bị anh giật phăng xuống, đôi mắt sâu thẳm nhìn trừng trừng vào Kỷ Cảnh trước mặt, như muốn nuốt trọn lấy cậu,",
    # 084
    "Anh hít sâu một hơi, bình tĩnh nói: “Tổng chỉ huy Thư Nghiên, một nữ Alpha.”",
    # 085
    "“Tôi và cô ta ai đẹp hơn?” Kỷ Cảnh lại hỏi.",
    # 086
    "“Em.” Lục Tư Niên có chút mờ mịt.",
    # 087
    "“Cô ta thích anh à?” Kỷ Cảnh nguy hiểm nhìn chằm chằm anh.",
    # 088
    "Lúc này Lục Tư Niên mới phản ứng lại được: “Không phải, cô ấy thích nữ Omega.”",
    # 089
    "Nhận được câu trả lời Kỷ Cảnh lập tức mất hết dũng khí hống hách, cậu mềm giọng lại, ghé sát vào tai Lục Tư Niên, dùng giọng nữ dịu dàng thầm thì: “Vậy sau này anh cũng phải cách xa những Alpha và phụ nữ khác ra một chút, dù sao thì—— anh cũng đã bị tôi đánh dấu trọn đời rồi, tôi đẹp hơn bọn họ nhiều, đúng không?”",
    # 090
    "“Ừm, được.” Lục Tư Niên khàn giọng đáp lời, tựa như không nhịn nổi nữa, nghiêng đầu dán môi lên môi Kỷ Cảnh.",
    # 091
    "Kỷ Cảnh lại cùng Lục Tư Niên hôn nhau thêm một lúc, mới sực nhớ ra một chuyện chính sự khác.",
    # 092
    "“Lục Tư Niên, tôi muốn cho anh xem một thứ.” Cậu bóp cằm Lục Tư Niên, đẩy người ra.",
    # 093
    "“Thứ gì.”",
    # 094
    "Chiếc váy hôm nay Kỷ Cảnh mặc xẻ tà rất cao, lúc này đã bị Lục Tư Niên vò cho rối tung rối mù.",
    # 095
    "Cậu vén vạt váy lên, chỉ thấy trên làn da trắng mịn như ngọc trai kia, có xăm một dãy chữ Lam Tinh cổ.",
    # 096
    "Kỷ Cảnh tuần trước đã dưỡng lành vết xăm rồi, mãi mà chưa tìm được cơ hội cho Lục Tư Niên xem.",
    # 097
    "“Xăm cái gì?” Hơi thở Lục Tư Niên khựng lại, mắt không dám nhìn thẳng lên trên.",
    # 098
    "“Tên của anh,” Kỷ Cảnh mỉm cười, “Chữ Lam Tinh cổ.”",
    # 099
    "Lục Tư Niên sững sờ chết lặng.",
    # 100
    "“Tôi là người rất công bằng, tôi đánh dấu trọn đời anh rồi, thì để tên của anh xăm lên người tôi, thế nào?” Kỷ Cảnh cười nói, “Này, anh bị làm sao thế, ngơ ngác đực mặt ra làm gì?”",
    # 101
    "“Kỷ Cảnh, hình xăm không rửa sạch được đâu.”",
    # 102
    "Lục Tư Niên chầm chậm thốt ra từng chữ, giọng nói vô cùng trầm đục, “Cả đời, cả đời này đều không xóa đi được.”",
    # 103
    "“Tại sao phải xóa đi?”",
    # 104
    "“Sau này, có thể em sẽ gặp được người mình thích hơn, với gia thế của em, tôi không xứng...”",
    # 105
    "“Lục Tư Niên, anh đừng có vào lúc này chọc giận tôi, anh có hiểu đánh dấu trọn đời mang ý nghĩa gì không hả? Tôi bằng lòng vì anh...” Kỷ Cảnh bóp cằm Lục Tư Niên, ép anh phải nhìn thẳng vào mắt mình.",
    # 106
    "Thế nhưng cậu vừa định mở miệng nói tiếp, cơn giận liền tan biến sạch sành sanh: “Này, Lục Tư Niên, mắt anh đỏ quá...”",
    # 107
    "Lục Tư Niên không cho cậu cơ hội nói tiếp nữa, nghiêng người chặn chặt lấy đôi môi cậu.",
    # 108
    "Hai người càng hôn càng động tình nồng cháy, Kỷ Cảnh bị Lục Tư Niên đè ngã nhào xuống chiếc giường của anh.",
    # 109
    "Kỷ Cảnh xoay người đè ngược lại lên người Lục Tư Niên, cúi đầu, đè thấp giọng nói: “Ông xã, em muốn làm anh.”",
    # 110
    "...",
    # 111
    "Một đêm triền miên phong tình.",
    # 112
    "Lục Tư Niên mở mí mắt ra, nhìn vào gáy người trong lòng, vẻ mặt ngơ ngẩn thẫn thờ.",
    # 113
    "Kỷ Cảnh bị cảm giác lành lạnh truyền tới từ ngón tay đánh thức, cậu mơ màng mở mắt, nhìn thấy Lục Tư Niên đang nửa quỳ bên đầu giường, nắm lấy tay cậu nhẹ nhàng đeo vào thứ gì đó.",
    # 114
    "Kỷ Cảnh mất nửa phút để tỉnh táo tinh thần, sau đó nhìn về phía bàn tay mình, phát hiện trên ngón áp út của bàn tay trái xuất hiện thêm một chiếc nhẫn.",
    # 115
    "Khoan đã, đây là cái gì, nhẫn kim cương sao?!",
    # 116
    "Kỷ Cảnh bật dậy khỏi giường.",
    # 117
    "Lúc này Lục Tư Niên vừa thu tay về, bị Kỷ Cảnh làm cho giật mình.",
    # 118
    "“Anh làm cái gì đấy?” Kỷ Cảnh hỏi anh.",
    # 119
    "“Đeo nhẫn cho em,” Lục Tư Niên bình tĩnh nói, “Chiếc nhẫn này là lúc trước mua để cầu hôn em, vốn định đợi em đồng ý, nếu em đồng ý thì sẽ tặng cho em.”",
    # 120
    "Kỷ Cảnh choáng váng đầu óc, cậu phát hiện bản thân có chút không theo kịp tư duy của Lục Tư Niên, chẳng lẽ Lục Tư Niên vừa rồi đã cầu hôn mình rồi, mà do mình ngủ quên mất?",
    # 121
    "“Anh không cầu hôn trước đã à?” Kỷ Cảnh hỏi anh.",
    # 122
    "Không ngờ Lục Tư Niên im lặng trước, một lát sau anh mới nói: “Tối hôm qua, em gọi tôi là ông xã.”",
    # 123
    "Kỷ Cảnh cũng im lặng theo một lúc, trong lòng tự nhủ bản thân không sao cả, là do Lục Tư Niên không hiểu cách phân biệt giữa tình thú và hiện thực mà thôi.",
    # 124
    "“Được rồi, thế thì tôi...”",
    # 125
    "“Kỷ Cảnh, em... có đồng ý gả cho tôi không?” Lục Tư Niên đột nhiên lĩnh ngộ ra, vẻ mặt đứng đắn nghiêm túc hỏi.",
    # 126
    "Kỷ Cảnh liếc nhìn bàn tay mình, mỉm cười: “Tôi đồng ý.”",
    # 127
    "..."
]

content = "---\ntitle: Chương 117: Lời cầu hôn và chiếc nhẫn kim cương\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
