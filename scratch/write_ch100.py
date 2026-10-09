# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_100\translation.md"

paras = [
    # 000
    "Bên kia hệ thống vang lên tiếng còi báo động tạm dừng trận đấu, bên này Lục Tư Niên xoay người, bước xuống khỏi hàng ghế trọng tài, rẽ vào bên trong sảnh chính.",
    # 001
    "So với sự ồn ào náo nhiệt bên ngoài, bên trong sảnh vô cùng yên tĩnh, trong đại sảnh thênh thang chỉ còn lại tiếng thở dốc hỗn loạn của Lục Tư Niên.",
    # 002
    "Anh ngửa đầu dựa vào tường, một số ký ức tựa như dòng nước lũ mất kiểm soát ùa về trong tâm trí.",
    # 003
    "Khoảng thời gian Lục Tư Niên mới được đón về nhà họ Lục, anh nhận ra từ trên xuống dưới cả nhà họ Lục chẳng có lấy một ai coi trọng anh, bao gồm cả người cha cùng huyết thống với anh, ngay cả ánh mắt ông ta nhìn anh cũng như đang nhìn một con chó hoang không ai thèm nhận.",
    # 004
    "Khi đó Lục Đảo Phong tuy tuổi đời còn nhỏ, nhưng bên cạnh đã có vài đứa con em dòng thứ bám gót a dua nịnh hót.",
    # 005
    "Biết được Lục Tư Niên là con ngoài giá thú của cha mình, Lục Đảo Phong liền câu kết với đám Alpha đó cô lập và ức hiếp Lục Tư Niên.",
    # 006
    "Thời điểm ấy Lục Tư Niên biết mình còn một tháng nữa là sẽ được nhà họ Lục đưa vào Học viện Cao cấp Đế quốc, để có thể thuận lợi bước chân vào đó, anh đã cắn răng nhẫn nhịn suốt một tháng ròng.",
    # 007
    "Anh biết muốn trả thù nhà họ Lục, bản thân buộc phải leo lên đỉnh kim tự tháp, thế là anh liều mạng chiến đấu, liên tục nhảy lớp, thi đỗ vào Quân đoàn Ba đầy vinh quang của Đế quốc, ngồi lên chiếc ghế Tổng chỉ huy.",
    # 008
    "Nhưng anh vẫn không thể lay chuyển được nhà họ Lục, thậm chí ngay cả Lục Đảo Phong anh cũng không động tới được.",
    # 009
    "Bởi vì anh hai bàn tay trắng, tất cả mọi thứ đều là do anh liều mạng đánh đổi mới có được, điều anh phải kiêng dè quá nhiều, chẳng hạn như nếu anh đụng vào Lục Đảo Phong, anh sẽ bị trục xuất khỏi Quân đoàn Ba, mọi nỗ lực của anh sẽ tan thành mây khói tro bụi.",
    # 010
    "Trước những gia tộc quyền thế hiển hách, vị trí Tổng chỉ huy của anh đáng là cái thá gì chứ.",
    # 011
    "Mẹ của Lục Tư Niên trước khi qua đời luôn miệng dặn dò, mong Lục Tư Niên trở thành một người quân tử khoáng đạt rộng lượng, không bị ân oán thế tục quấn thân, nhưng Lục Tư Niên chưa từng muốn làm một người quân tử gì hết.",
    # 012
    "Hành động ngày hôm nay của Kỷ Cảnh, không thể nghi ngờ gì nữa, đã thể hiện rõ ràng việc cậu biết tường tận sự chật vật nhếch nhác và tủi nhục năm xưa của Lục Tư Niên.",
    # 013
    "Lục Tư Niên khẽ cười một tiếng, giơ tay che khuất đôi mắt.",
    # 014
    "Tiếng bước chân từ cách đó không xa thong thả tiến lại gần, trong tầm mắt anh xuất hiện một đôi ủng da quân dụng.",
    # 015
    "“Lục chỉ huy, hàng ghế trọng tài tốt như thế không ngồi, trốn đến đây làm cái gì?”",
    # 016
    "Một giọng nam với âm điệu kỳ quặc truyền đến từ phía trước, Lục Tư Niên hạ tay xuống, nhìn thấy Lâm Diên Sơn với nụ cười nửa miệng trước mặt.",
    # 017
    "Lâm Diên Sơn, lớn hơn Lục Tư Niên hai khóa, nhưng trong các kỳ đánh giá sát hạch của quân đoàn luôn bị Lục Tư Niên áp đảo hoàn toàn, kẻ xếp thứ hai vạn năm.",
    # 018
    "Sau khi Lục Tư Niên giải ngũ, Lâm Diên Sơn mới từ vị trí Phó chỉ huy được thăng lên làm Tổng chỉ huy.",
    # 019
    "Lâm Diên Sơn dù là một Alpha nhưng lại thấp hơn Lục Tư Niên nửa cái đầu.",
    # 020
    "Lục Tư Niên đứng thẳng người, từ trên cao liếc xéo hắn ta một cái, quay người cất bước bỏ đi.",
    # 021
    "“Này, Lục Tư Niên, tao biết vì sao mày lại giải ngũ rồi đấy.”",
    # 022
    "Biểu cảm của Lâm Diên Sơn lập tức cứng đờ, sau đó lại nở một nụ cười rách toạc, vô cùng giễu cợt nhìn bóng lưng khựng lại của Lục Tư Niên.",
    # 023
    "Hắn ta chậm rãi bước tới, hạ thấp giọng nói: “Là một Omega, việc chém chém giết giết trong quân đội không thích hợp với mày đâu, mày thích hợp để bị Alpha đè dưới thân hơn đấy... Á——”",
    # 024
    "Cú đá bay bất thình lình của Lục Tư Niên đá văng cả người Lâm Diên Sơn bay ra ngoài, tên Alpha đập mạnh vào cây cột trụ tròn, phì một tiếng phun ra một ngụm bọt máu.",
    # 025
    "“Mày làm sao mà...” Lâm Diên Sơn không thể tin nổi nhìn anh.",
    # 026
    "Lục Tư Niên thu chân về: “Sao tao lại không bị tin tức tố của mày ảnh hưởng, Lâm Diên Sơn, mày muốn nói câu này chứ gì?”",
    # 027
    "Lúc Lâm Diên Sơn tiến lại gần, Lục Tư Niên đã ngửi thấy mùi tin tức tố Alpha cuồn cuộn ập tới như thủy triều, “Lâm Diên Sơn, theo cách nói của mày, mày đánh không lại một Omega, chẳng lẽ mày không càng thích hợp để bị người ta đè dưới thân hơn sao——”",
    # 028
    "Lục Tư Niên khựng lại vài giây, vẫn không thốt ra được cái từ thô tục kia, cuối cùng đành từ bỏ, dùng ánh mắt lạnh như băng liếc hắn ta một cái, đút hai tay vào túi quần quay người bước đi.",
    # 029
    "Cũng chính vào khoảnh khắc này, Lục Tư Niên sững sờ chết trân tại chỗ.",
    # 030
    "Kỷ Cảnh đang đứng cách đó không xa, dựa vào cột trụ với ánh mắt thâm trầm khó hiểu nhìn anh chăm chú.",
    # 031
    "“Tôi không làm phiền chuyện tốt của Lục giáo sư đấy chứ.” Kỷ Cảnh đứng thẳng người dậy, kéo dài giọng điệu nói.",
    # 032
    "Lục Tư Niên không hé răng nửa lời, bước chân anh cứng đờ mất vài giây, sau đó liền mạch sải bước đi ra ngoài cửa.",
    # 033
    "Khi đi ngang qua Kỷ Cảnh, anh hơi do dự dừng bước lại một chút, trầm giọng nói: “Không phải như cậu nghĩ đâu.”",
    # 034
    "Kỷ Cảnh nghe vậy nhướng mày, Lục Tư Niên... đây là đang giải thích với cậu sao?",
    # 035
    "“Cảm ơn.” Lục Tư Niên lại nói thêm một lời cảm ơn đầy ẩn ý khó hiểu, rồi cất bước rời đi.",
    # 036
    "Kỷ Cảnh cong cong khóe môi, cất bước đi theo sau.",
    # 037
    "Mới ra khỏi sảnh chưa được mấy bước, sống lưng Lục Tư Niên đột nhiên căng thẳng, dừng phắt lại.",
    # 038
    "Còn chưa đợi Kỷ Cảnh kịp phản ứng, cảnh tượng trước mắt bỗng nhiên quay cuồng chao đảo, cậu bị một luồng sức mạnh đè nghiến vào thân cây bên đường.",
    # 039
    "Cậu hoàn hồn lại, phát hiện Lục Tư Niên đang áp sát đè lên người mình, cúi gằm đầu thở dốc bên tai cậu, vành tai hơi ửng đỏ.",
    # 040
    "Tin tức tố vừa rồi không phải là hoàn toàn không có ảnh hưởng gì.",
    # 041
    "“Lục Tư Niên, anh đang phi lễ tôi đấy à——” Kỷ Cảnh nghiêng nghiêng đầu, cười trêu chọc.",
    # 042
    "“Đừng động đậy,” Lục Tư Niên dùng chất giọng khàn đặc gằn lên, “Để tôi ngửi một lát.”",
    # 043
    "Ngửi, ngửi cái gì?",
    # 044
    "Alpha không thể ngửi thấy mùi tin tức tố của chính mình, họ chỉ có thể ngửi thấy mùi của những Alpha và Omega khác.",
    # 045
    "Cậu biết trên người Lục Tư Niên thoang thoảng mùi gỗ tuyết tùng lành lạnh, cấm dục y hệt như con người anh vậy.",
    # 046
    "Một lúc lâu sau, rặng mây đỏ bên vành tai Lục Tư Niên mới dần dần rút đi, anh chậm rãi kéo giãn khoảng cách với Kỷ Cảnh.",
    # 047
    "“Kỷ Cảnh, người nhà họ Kỷ các cậu ai cũng có mùi giống nhau à.” Anh đột nhiên nhìn thẳng vào mắt Kỷ Cảnh hỏi một câu.",
    # 048
    "“Gì cơ?” Kỷ Cảnh nghe không hiểu.",
    # 049
    "Nhưng Lục Tư Niên không nói thêm gì nữa, anh thu hồi ánh mắt của mình, một mình khuất bóng nơi ngã rẽ góc đường.",
    # 050
    "...",
    # 051
    "Kỷ Cảnh do vi phạm quy tắc thi đấu nên đã bị tước huy chương vàng quán quân, đồng thời bị phía ban giám hiệu Học viện Quân sự Đế quốc phê bình nghiêm khắc một trận, nhưng nể sợ thân phận của Kỷ Cảnh nên không đưa ra bất kỳ hình thức kỷ luật nào.",
    # 052
    "Kỷ Cảnh chẳng hề để tâm, thứ cậu không thiếu nhất chính là lời tán dương và chỗ dựa vững chắc, chút vinh dự cỏn con này đối với cậu chẳng đáng một xu.",
    # 053
    "Đoạn video ghi hình phát sóng trực tiếp cảnh cậu đập nhừ tử Lục Đảo Phong lan truyền chóng mặt trên Mạng Tinh Vân Đế quốc, chỉ trong vòng một giờ ngắn ngủi lượt xem đã phá mốc một trăm nghìn.",
    # 054
    "Chủ đề hot search #Con trai độc nhất nhà họ Kỷ - Kỷ Cảnh đập nhừ tử thái tử gia nhà họ Lục# bùng nổ khắp cõi mạng.",
    # 055
    "Cùng lúc đó, tin tức về việc thiên phú của Kỷ Cảnh hồi sinh cũng được lan truyền rộng rãi trong giới thượng lưu trung tâm Đế quốc.",
    # 056
    "Gần như vừa về đến nhà, cậu đã bị Kỷ Vân Hy chặn đứng ngay cửa.",
    # 057
    "“Em trai à, mày gặp chuyện lớn rồi đấy.” Kỷ Vân Hy hả hê trên nỗi đau của người khác, “Ba đang đợi mày trong thư phòng kìa, mau vào đó đi.”",
    # 058
    "Việc Kỷ Cảnh đánh Lục Đảo Phong không đơn thuần chỉ là chuyện xích mích giữa hai người bọn họ, chuyện này còn liên quan đến mối ân oán phân tranh nhiều năm giữa hai đại gia tộc Kỷ gia và Lục gia.",
    # 059
    "Thế nhưng đúng như Kỷ Cảnh dự đoán, Kỷ Trình căn bản không có ý định mắng mỏ cậu, ngược lại còn với tâm trạng vô cùng sảng khoái vỗ vỗ vai cậu, hỏi han xem cơ thể cậu đã khỏi hẳn chưa, có cần đến bệnh viện kiểm tra lại lần nữa hay không.",
    # 060
    "“Con trai của ba đúng là xuất chúng, cái nhà họ Lục đó tính là cái thá gì chứ, ba cứ ngồi đó cho bọn họ phát điên cắn càn, bọn họ cũng chẳng dám đụng tới một cọng lông chân của nhà họ Kỷ ta đâu.”",
    # 061
    "Kỷ gia và Lục gia tuy trên danh nghĩa đều là một trong tứ đại gia tộc của Đế quốc, nhưng nếu luận về bề dày nội tình gia tộc thì Lục gia còn lâu mới đuổi kịp Kỷ gia.",
    # 062
    "Tầng lớp đỉnh chóp của Đế quốc ai nấy đều thấu hiểu trong lòng rằng hai nhà vốn không cùng một đẳng cấp.",
    # 063
    "“Trương Mạc vừa mới gọi điện cho ba, khen ba nuôi dạy con trai tốt lắm, bảo là Chu Độ bên Quân đoàn Ba đã chấm trúng con rồi, bảo con cứ ở trường thêm một năm nữa rồi sang chỗ cậu ta báo danh.”",
    # 064
    "Kỷ Trình nhấp một ngụm trà, ung dung nói: “Nhưng mà tại sao con lại đột nhiên kết oán với thằng Lục Đảo Phong thế?”",
    # 065
    "Kỷ Cảnh gãi gãi đầu, cười ha hả lấp liếm cho qua chuyện.",
    # 066
    "Còn về Quân đoàn Ba, cậu cũng không tha thiết muốn đi cho lắm, bởi vì cậu không thích cảm giác bị quy củ trói buộc, cậu cho rằng cái chốn quân đoàn ấy thích hợp hơn với một kẻ cổ hủ tuân thủ quy củ như Lục Tư Niên.",
    # 067
    "Huống chi Lục Tư Niên cũng chẳng còn ở đó nữa, đến đó lại càng chẳng có gì thú vị.",
    # 068
    "Kỷ Cảnh từ thư phòng của Kỷ Trình đi ra liền quay trở về phòng ngủ của mình.",
    # 069
    "Tắm rửa xong liếc nhìn đồng hồ, cậu mới phát hiện đã gần mười một giờ đêm rồi.",
    # 070
    "Nghĩ bụng chắc Lục Tư Niên vẫn chưa ngủ, cậu lại mở khung chat với Lục Tư Niên ra, gửi một tin nhắn sang.",
    # 071
    "【Dịch Nam Nam Nam】: Hôm nay làm trọng tài cuộc thi có thuận lợi không anh",
    # 072
    "【Dịch Nam Nam Nam】: [Mèo con xoay vòng tròn.jpg]",
    # 073
    "【Dịch Nam Nam Nam】: Dự báo thời tiết nói ngày mai trời đổ mưa to đấy, nhớ mang theo ô nhé.",
    # 074
    "...",
    # 075
    "Theo lẽ thường thì Lục Tư Niên hẳn phải trả lời từ sớm rồi, nhưng Kỷ Cảnh đợi mãi cho đến trước khi chìm vào giấc ngủ vẫn không nhận được hồi âm từ phía bên kia.",
    # 076
    "Một tia cảm giác khác lạ vừa nảy sinh trong lòng liền bị cơn buồn ngủ ập tới cuốn phăng đi, cậu nhắm nghiền hai mắt, ngủ say sưa một mạch.",
    # 077
    "Sáng hôm sau Kỷ Cảnh tinh thần sảng khoái thức dậy, nhìn qua một lượt phát hiện Lục Tư Niên vẫn bặt vô âm tín, thế là thu dọn đồ đạc định bụng đến trường hỏi thẳng mặt Lục Tư Niên xem sao.",
    # 078
    "Hôm nay quả nhiên trời đổ mưa lớn, bầu trời âm u xám xịt, tựa như đang ấp ủ một cơn mưa rào như trút nước.",
    # 079
    "Kỷ Cảnh mang theo một chiếc ô, rảo bước đi về phía phòng học của Lục Tư Niên.",
    # 080
    "Cậu đến đúng vào giờ điểm danh, theo lệ thường lúc này Lục Tư Niên đã đứng trên bục giảng chuẩn bị giáo án rồi, anh luôn có tính tự giác đến mức đúng giờ chuẩn chỉ bước vào lớp, thế nhưng hôm nay khi cậu bước vào phòng học, trên bục giảng lại trống không chẳng có một bóng người.",
    # 081
    "Không chỉ riêng Kỷ Cảnh, các học viên của Lục Tư Niên cũng phát hiện ra điểm bất thường, trên chỗ ngồi bắt đầu xì xào bàn tán to nhỏ.",
    # 082
    "Bởi vì hôm qua Quân đoàn trưởng Trương Mạc của Quân đoàn Ba đối xử rất khách khí với Lục Tư Niên, nên số lượng học viên đến lớp hôm nay đông gấp đôi so với trước kia, lúc ồn ào lên thì vô cùng huyên náo.",
    # 083
    "Kỷ Cảnh khẽ nhíu mày, ngồi xuống chỗ của mình rồi lại gửi tin nhắn cho Lục Tư Niên.",
    # 084
    "【Dịch Nam Nam Nam】: Lục giáo sư, có phải anh đến muộn rồi không.",
    # 085
    "Tin nhắn vẫn như đá chìm đáy biển, mãi cho đến khi tiết học trôi qua gần nửa tiếng đồng hồ, thiết bị đầu cuối mới khẽ rung lên.",
    # 086
    "【Lục Tư Niên】: Xin lỗi, hôm nay tôi phải xin nghỉ phép rồi.",
    # 087
    "Kỷ Cảnh vừa đọc tin nhắn chưa được bao lâu, ngoài cửa lớp đột nhiên có một vị lãnh đạo nhà trường lớn tuổi bước vào, vị lãnh đạo bước lên bục giảng, nghiêm túc thông báo: “Lục giáo sư cơ thể không khỏe nên đã xin nghỉ phép, khoảng thời gian này sẽ do tôi tạm thời dạy thay.”",
    # 088
    "Vị lãnh đạo vừa dứt lời, dưới lớp liền vang lên những tiếng than vãn rầu rĩ.",
    # 089
    "Kỷ Cảnh liếc nhìn bục giảng một cái, sau đó lén lút chuồn ra khỏi lớp bằng cửa sau.",
    # 090
    "Tại sao Lục Tư Niên lại xin nghỉ phép, bị ốm rồi sao? Nhưng hôm qua trông vẫn khỏe mạnh bình thường mà.",
    # 091
    "Kỷ Cảnh vừa sải bước dọc theo hành lang, vừa mở thiết bị đầu cuối, tìm một cái tên trong danh bạ rồi gọi điện sang.",
    # 092
    "“A lô, tôi đây, Kỷ Cảnh, cậu điều tra giúp tôi xem Lục Tư Niên sống ở đâu,” Kỷ Cảnh bước ra khỏi tòa nhà giảng đường, liếc nhìn bầu trời âm u, nói, “Đúng vậy, cần ngay lập tức, nhanh lên đấy.”",
    # 093
    "Tin tức bên kia gửi tới rất nhanh, Kỷ Cảnh liếc nhìn địa chỉ trên thiết bị đầu cuối, ra cổng trường bắt một chiếc xe rồi rời đi.",
    # 094
    "Lục Tư Niên sống trong một khu chung cư cách trường học không xa.",
    # 095
    "Đây là một khu nhà ở rất giản dị đơn sơ, ít nhất là xét theo thân phận của Lục Tư Niên thì được coi là vô cùng giản dị.",
    # 096
    "Kỷ Cảnh vừa thầm phàn nàn trong lòng rằng Lục Tư Niên là một tên tu sĩ khổ hạnh chẳng hiểu chút phong tình thi vị cuộc sống nào, vừa theo địa chỉ bước vào thang máy đi lên tầng cao nhất.",
    # 097
    "Trong thang máy còn có mấy bà cụ, thấy cậu bấm nút tầng cao nhất liền dùng ánh mắt tò mò hóng hớt đánh giá cậu.",
    # 098
    "“Cháu gái à, cháu là bạn gái của Lục giáo sư ở tầng thượng đó hả?”",
    # 099
    "Kỷ Cảnh nhất thời không biết nên trả lời thế nào, đành phải bảo mình là học trò của Lục Tư Niên.",
    # 100
    "Câu nói này vừa lọt vào tai bà cụ liền hỏng bét: “Nữ sinh viên sao?! Cái cậu Lục giáo sư đó trông vẻ ngoài thì đàng hoàng đứng đắn, lần trước tôi còn tính giới thiệu cháu gái tôi cho cậu ta cơ đấy, may mà cậu ta từ chối rồi, cái loại đàn ông này không thể lấy được, không thể lấy được đâu!”",
    # 101
    "Đoán chừng bà cụ đã hiểu lầm chuyện gì đó, Kỷ Cảnh vừa cười xấu xa, vừa gật đầu lia lịa ra chiều đồng tình.",
    # 102
    "Nhìn địa chỉ nơi ở, Lục Tư Niên hẳn là đã mua đứt toàn bộ tầng thượng này rồi.",
    # 103
    "Kỷ Cảnh bước ra khỏi thang máy, đối diện với cánh cửa lớn duy nhất, bấm vang chuông cửa."
]

header = "---\ntitle: Chương 100: Gõ cửa căn hộ áp mái\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written ch_100 translation successfully.")
