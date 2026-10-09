# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_102\translation.md"

paras = [
    # 000
    "Kỷ Cảnh ngủ một giấc đẫy đà đến khi tự nhiên tỉnh lại, mơ màng quờ tay sang bên cạnh, lại phát hiện bên cạnh trống trơn.",
    # 001
    "Cậu giật mình ngồi dậy khỏi giường, liếc nhìn sang bên cạnh, nhận ra Lục Tư Niên đã không còn ở đó nữa.",
    # 002
    "Vò vò mái tóc dài hơi rối bời, cậu chậm chạp bước xuống giường, chân trần dẫm lên mặt sàn.",
    # 003
    "Bên chân đột nhiên đá trúng thứ gì đó, cậu ngẩn người, phát hiện đó là chiếc váy bị chính mình tiện tay vứt đi từ lúc nào chẳng hay.",
    # 004
    "Nó đã bị Lục Tư Niên làm bẩn, Kỷ Cảnh có chút bệnh sạch sẽ, lúc đó liền tiện tay chọn một bộ đồ ngủ trong tủ quần áo của Lục Tư Niên thay vào.",
    # 005
    "Cách một cánh cửa, cậu nghe thấy tiếng bát đũa va vào nhau lách cách truyền đến từ phòng khách.",
    # 006
    "Kỷ Cảnh đẩy cửa, cất bước đi ra ngoài.",
    # 007
    "Lục Tư Niên vừa lúc từ trong bếp đi ra, chạm mặt trực diện với Kỷ Cảnh, cả người liền cứng đờ lại.",
    # 008
    "“Rửa mặt súc miệng xong thì ra ăn sáng đi.”",
    # 009
    "Anh né tránh ánh mắt của Kỷ Cảnh, đặt bát cháo trắng bốc khói nghi ngút lên bàn ăn.",
    # 010
    "Kỷ Cảnh vừa ngủ dậy, đầu óc quay chậm chạp, vẫn chưa phát hiện ra có điểm gì không đúng, khẽ “ồ” một tiếng rồi đi về phía phòng vệ sinh.",
    # 011
    "“Chờ đã,”",
    # 012
    "Lục Tư Niên gọi giật cậu lại, cầm một đôi dép lê cúi người đặt bên chân cậu.",
    # 013
    "“Xỏ dép vào đi, sàn nhà lạnh.”",
    # 014
    "Kỷ Cảnh ngơ ngác xỏ dép vào, chẳng hiểu sao lại cảm thấy Lục Tư Niên dường như có chỗ nào đó đã khác đi rồi.",
    # 015
    "Rửa mặt xong Kỷ Cảnh tỉnh táo hơn rất nhiều, cậu ngồi bên bàn ăn, bưng bát cháo trắng húp một cách khoan khoái dễ chịu.",
    # 016
    "Còn Lục Tư Niên thì ngồi đối diện cậu, một lời không nói cắm cúi húp cháo.",
    # 017
    "Kỷ Cảnh chậm chạp nhận ra bầu không khí có chút kỳ quặc.",
    # 018
    "Cậu vừa húp cháo vừa khẽ nâng mí mắt đánh giá Lục Tư Niên.",
    # 019
    "Cậu suy đoán Lục Tư Niên chắc chắn là bị chuyện mấy ngày nay dọa cho ngốc luôn rồi, bằng không cả người sao trông lại vừa ngơ ngác vừa đờ đẫn thế kia.",
    # 020
    "Trên mặt Kỷ Cảnh lướt qua một tia vui vẻ.",
    # 021
    "Cậu cảm thấy tiến độ nhiệm vụ của mình chắc chắn đã tiến thêm một bước dài, bằng không sao xứng với sự nỗ lực không quản ngày đêm mấy ngày qua của cậu chứ.",
    # 022
    "“Dịch Nam.” Lục Tư Niên đột nhiên gọi tên cậu.",
    # 023
    "Kỷ Cảnh cong khóe môi, vui vẻ đáp: “Sao thế?”",
    # 024
    "“Xin lỗi em.”",
    # 025
    "Lục Tư Niên đặt bát đũa xuống, giọng nói trầm thấp vô cùng.",
    # 026
    "Khóe môi đang cong lên của Kỷ Cảnh từ từ hạ xuống: “Anh xin lỗi tôi cái gì?”",
    # 027
    "Ngay sau đó cậu nghe thấy Lục Tư Niên thở ra một hơi nặng nề.",
    # 028
    "“Chuyện mấy ngày nay, tôi sẽ bù đắp cho em,”",
    # 029
    "Lục Tư Niên trịnh trọng vô cùng, như thể đang đưa ra một lời hứa hẹn trọng đại nào đó,",
    # 030
    "“Tôi sẽ dùng tất cả mọi thứ để bù đắp cho em.”",
    # 031
    "Bàn tay đang bưng bát của Kỷ Cảnh khựng lại giữa không trung, sau đó đặt xuống mặt bàn.",
    # 032
    "Cậu từ từ ngước mắt lên, đối diện với đôi mắt phức tạp của Lục Tư Niên, bật cười: “Bù đắp cho tôi?”",
    # 033
    "Kỷ Cảnh sao lại không hiểu hai chữ “bù đắp” này có ý nghĩa gì chứ.",
    # 034
    "Trong con ngươi đen như đá hắc diệu thạch bùng lên ngọn lửa giận ngấm ngầm, nhưng ngoài mặt Kỷ Cảnh lại không lộ chút biểu cảm nào, như thể đang nói về một chuyện cỏn con chẳng đáng nhắc tới,",
    # 035
    "“Tôi hiểu ý của anh rồi Lục giáo sư.” Kỷ Cảnh đẩy ghế đứng phắt dậy, “Anh không cần phải bù đắp gì cho tôi cả, chuyện to tát gì đâu.”",
    # 036
    "“Chuyện to tát gì đâu?”",
    # 037
    "Lục Tư Niên cũng đứng bật dậy, ngữ điệu trở nên cứng ngắc, còn pha lẫn chút tức giận khó phát hiện: “Dịch Nam, chuyện này đối với em không quan trọng sao?”",
    # 038
    "Kỷ Cảnh vốn dĩ đã đang tức giận, câu chất vấn này của Lục Tư Niên hoàn toàn như đổ thêm dầu vào lửa,",
    # 039
    "“Lục Tư Niên, không phải ai cũng sống ở thế kỷ trước như anh đâu, tôi thấy anh thú vị nên chơi bời với anh một chút thôi, hôm nay chơi với anh, ngày mai tôi cũng có thể chơi với người khác.”",
    # 040
    "Gương mặt vạn năm không đổi sắc của Lục Tư Niên xuất hiện một thoáng đờ đẫn ngắn ngủi.",
    # 041
    "“Em đang chơi bời với tôi? Vậy em với những người khác cũng...”",
    # 042
    "Kỷ Cảnh không muốn nói nhiều thêm, quay người bước vào phòng ngủ của Lục Tư Niên, ba chân bốn cẳng thay lại quần áo của mình, rảo bước nhanh về phía cửa chính.",
    # 043
    "“Em muốn đi đâu.”",
    # 044
    "Lục Tư Niên sải bước đuổi theo, nắm lấy tay cậu.",
    # 045
    "“Về nhà.”",
    # 046
    "Kỷ Cảnh giật mạnh tay ra.",
    # 047
    "“Tôi đưa em về.”",
    # 048
    "Giọng nói của Lục Tư Niên dồn dập ngắn ngủi.",
    # 049
    "“Không cần, tôi tự đi.”",
    # 050
    "Kỷ Cảnh đẩy cửa lớn ra, bấm nút gọi thang máy.",
    # 051
    "Lục Tư Niên đứng chôn chân tại chỗ vài giây, sau đó xỏ vội giày rồi cùng cậu bước vào thang máy.",
    # 052
    "Trong buồng thang máy chật hẹp, không khí ngột ngạt như sắp sửa đông cứng lại, đúng lúc này cửa thang máy mở ra, một bà cụ quen mắt bước vào.",
    # 053
    "Bà cụ ngẩn người một thoáng, ánh mắt không ngừng đảo qua đảo lại giữa hai người, đặc biệt là nhìn chằm chằm vài lần vào những vệt đỏ trên cổ Kỷ Cảnh.",
    # 054
    "“Tội lỗi quá...” Bà vừa lẩm bẩm vừa lắc đầu ngán ngẩm.",
    # 055
    "Cửa thang máy vừa mở ra là Kỷ Cảnh liền rảo bước rời đi thật nhanh, mặc cho Lục Tư Niên đi theo sau lưng cũng không hề dừng lại.",
    # 056
    "Cuối cùng cậu vẫy một chiếc xe, ngồi lên xe chỉ vài giây sau đã biến mất khỏi tầm mắt của Lục Tư Niên.",
    # 057
    "Lục Tư Niên đứng bên lề đường, bóng lưng cao lớn sừng sững toát lên vẻ cô độc quạnh quẽ.",
    # 058
    "Lúc này, bà cụ vừa bước ra không nhịn được bèn hỏi một câu: “Lục giáo sư, cậu chọc giận cô nữ sinh... bạn gái cậu rồi hả?”",
    # 059
    "Lục Tư Niên lặng lẽ nhìn bà cụ một cái, cứng nhắc gật đầu: “Chắc là vậy ạ.”",
    # 060
    "“Đôi trẻ cãi nhau, đầu giường cãi cuối giường hòa thôi mà, cậu bỏ thêm vài ngày tâm tư dỗ dành cô bé là được rồi,” bà cụ đấm đấm bắp chân, dò hỏi, “Đúng rồi, cô bé đó là bạn gái cậu thật đấy à?”",
    # 061
    "Lục Tư Niên nghe vậy, ánh mắt dao động, khẽ lắc đầu.",
    # 062
    "Bà cụ lập tức vỗ đùi kêu to: “Thế sao mà được cơ chứ, cậu không thể làm kẻ phụ bạc vô trách nhiệm được đâu đấy nhé!”",
    # 063
    "Lục Tư Niên lại rơi vào trầm mặc, anh xoa xoa sống mũi, cũng không biết là đang nói với ai: “Cháu muốn chịu trách nhiệm, nhưng em ấy lại không muốn.”",
    # 064
    "Bà cụ nghe thấy lời này, đột nhiên im bặt, ánh mắt nhìn Lục Tư Niên cũng chuyển sang thương cảm xót xa,",
    # 065
    "“Haiz, người trẻ các cậu chơi bời thoáng quá, tôi già rồi cũng chẳng hiểu nổi, cô bé đó nhìn đúng là... Lục giáo sư à, thiên hạ đâu thiếu cỏ thơm, hay là hôm nào tôi giới thiệu cháu gái tôi cho cậu nhé...”",
    # 066
    "Lục Tư Niên xua xua tay, quay người bước trở về.",
    # 067
    "...",
    # 068
    "Kỷ Cảnh về đến nhà mới phát hiện thái độ của ba mẹ cùng Kỷ Vân Hy vô cùng bất thường.",
    # 069
    "Đặc biệt là cậu vẫn đang mặc nguyên một thân đồ con gái, vừa bước vào cửa đã đụng mặt trực diện với ba mẹ mình.",
    # 070
    "Kỷ Vân Hy với ánh mắt phức tạp đánh giá cậu từ trên xuống dưới, làm khẩu hình miệng: “Mày tiêu đời rồi.”",
    # 071
    "“Tiểu Cảnh, con mặc thành ra thế này là đi làm gì về thế hả!” Mẹ Kỷ khẽ thốt lên kinh ngạc, nhìn thấy những vết ban đỏ trên cổ Kỷ Cảnh.",
    # 072
    "“Kỷ Cảnh, giáo viên chủ nhiệm của con gọi điện cho ba, bảo con cả ngày thứ Sáu lẫn hôm nay đều không đến lớp, cũng không xin phép, thiết bị đầu cuối cũng không liên lạc được.”",
    # 073
    "Ánh mắt nghiêm khắc của ba Kỷ liếc nhìn Kỷ Cảnh, lông mày khẽ chau lại.",
    # 074
    "Kỷ Cảnh liếc nhìn ngày tháng, hóa ra hôm nay đã là thứ Ba rồi.",
    # 075
    "Cậu mặt không đổi sắc nói: “Con biết rồi thưa ba, lát nữa con sẽ tự mình giải thích với trường học.”",
    # 076
    "Ba Kỷ ừ một tiếng, cũng không nhiều lời thêm.",
    # 077
    "Cách giáo dục của ba Kỷ và mẹ Kỷ rất cởi mở phóng khoáng, họ luôn dành cho Kỷ Cảnh và Kỷ Vân Hy đủ không gian riêng tư, chỉ cần không chạm tới giới hạn nguyên tắc thì sẽ không hỏi han quá nhiều.",
    # 078
    "Trước khi Kỷ Cảnh lên lầu, liền nghe thấy mẹ Kỷ dặn dò: “Tiểu Cảnh, yêu đương rồi thì đừng giấu giếm ba mẹ nhé.”",
    # 079
    "Bước chân Kỷ Cảnh loạng choạng, suýt chút nữa vồ ếch ngã nhào.",
    # 080
    "“Tiểu Cảnh, kỳ nhạy cảm của con vẫn chưa từng tới, nếu đã yêu đương rồi thì tốt nhất nên chuẩn bị sẵn thuốc ức chế, thuốc ức chế của Alpha mẹ đã để sẵn trong tủ quần áo của con rồi, nhất định phải để tâm đấy, đừng sơ ý làm tổn thương Omega nhà người ta.”",
    # 081
    "Mẹ Kỷ ân cần thấm thía nói.",
    # 082
    "Kỷ Cảnh quả thực vẫn chưa từng trải qua kỳ nhạy cảm, đại đa số Alpha trước khi trưởng thành đều sẽ đón nhận kỳ nhạy cảm, vậy mà Kỷ Cảnh mãi vẫn chẳng thấy động tĩnh gì.",
    # 083
    "Cậu luôn cảm thấy đây là một sự sỉ nhục đối với thân phận Alpha của mình, vì thế từ trước đến nay đều cố tình né tránh vấn đề này.",
    # 084
    "Gương mặt cậu lúc xanh lúc đỏ quay trở về phòng của mình.",
    # 085
    "Buổi chiều cậu liền đến trường đi học, và trong mấy ngày tiếp theo cũng không hề tới dự tiết của Lục Tư Niên, càng không nhắn tin cho Lục Tư Niên.",
    # 086
    "Trong khoảng thời gian đó Lục Tư Niên có gửi cho cậu vài tin nhắn, đều ngắn gọn súc tích hỏi cậu có đi học hay không.",
    # 087
    "Về sau thấy Kỷ Cảnh không trả lời, anh cũng không hỏi nữa.",
    # 088
    "Lục Tư Niên lần thứ không đếm xuể nhìn vào giao diện trò chuyện trống trơn, những đốt ngón tay thon dài day day ấn ấn hàng chân mày đang nhíu chặt.",
    # 089
    "Dưới cặp kính nửa viền đen, lờ mờ có thể thấy được quầng thâm nhạt dưới mắt.",
    # 090
    "Mấy ngày nay, cứ hễ nhắm mắt lại là trong đầu anh lại hiện lên những chuyện đã làm với Kỷ Cảnh trong mấy ngày đó.",
    # 091
    "Ký ức của anh rất mờ mịt, anh chỉ nhớ được sự mập mờ ám muội khi môi lưỡi quấn quýt, cùng những hơi thở đan xen dồn dập.",
    # 092
    "Lúc Lục Tư Niên tỉnh lại khắp người đều không có gì bất thường, chứng tỏ là chính anh đã đem đối phương...",
    # 093
    "“Tư Niên, nhất định phải nhớ kỹ, con là một Beta nam, mẹ không cho phép con làm tổn thương bất kỳ người phụ nữ nào, nếu một ngày nào đó con tước đoạt sự trong trắng của ai, nhất định phải chịu trách nhiệm với người ta đến cùng.”",
    # 094
    "Người mẹ trong ký ức từng hướng về gương mặt của tên Alpha họ Lục trên bản tin thời sự, vô cùng trịnh trọng răn dạy anh.",
    # 095
    "Cuối cùng, Lục Tư Niên thở dài một hơi thật sâu, gửi tin nhắn đi:",
    # 096
    "【Lục Tư Niên】: Dịch Nam, chúng ta nói chuyện đi.",
    # 097
    "【Lục Tư Niên】: Có lẽ đối với em, những việc tôi làm với em không tính là gì, nhưng đối với tôi thì điều đó đã tương đương với phạm tội.",
    # 098
    "【Lục Tư Niên】: Tôi không thể thản nhiên chấp nhận tội lỗi mà mình đã gây ra cho em được, vậy nên mong em có thể cho tôi một cơ hội để bù đắp, có được không?",
    # 099
    "Thời điểm đó Kỷ Cảnh đang ở trên sân tập giao đấu với máy móc.",
    # 100
    "Các Alpha trong lớp đã không còn ai thích hợp để luyện tập đối kháng với cậu nữa, Vương Bằng đành phải tìm riêng cho cậu một người máy cấp cao.",
    # 101
    "Cậu mở thiết bị đầu cuối, ngồi sang một bên nghỉ giữa hiệp.",
    # 102
    "Nhìn thấy mấy tin nhắn Lục Tư Niên gửi tới, tâm trạng vốn đã bực bội của Kỷ Cảnh lại càng thêm khó khống chế.",
    # 103
    "Cái tên Lục Tư Niên này rốt cuộc đang làm cái trò quỷ gì thế không biết?",
    # 104
    "Chẳng phải mẹ nó chỉ là giúp anh ta nhiều lần như vậy thôi sao, có thể giữa chừng lúc mơ màng có dùng đến... một chút, nhưng có cần thiết phải bám riết lấy cậu đòi bù đắp thế không?",
    # 105
    "Có bản lĩnh thì xác nhận quan hệ với mình đi chứ.",
    # 106
    "Cậu thiếu chút bù đắp cỏn con đó của anh chắc?",
    # 107
    "Kỷ Cảnh cạch một tiếng đóng thiết bị đầu cuối lại, vung một cú đấm nện thẳng vào con robot vô tội.",
    # 108
    "Vương Bằng hài lòng nhìn Kỷ Cảnh, tựa như đang ngắm nhìn một con sói con do chính tay mình nuôi lớn, sau đó không kìm được chụp một bức ảnh, gửi vào nhóm chat của Quân đoàn Ba.",
    # 109
    "【Đại Bằng Tung Cánh】: Xuất sắc quá đi mất [Ngón tay cái]. Quả không hổ danh là thiên tài Alpha do đích thân tôi dẫn dắt.",
    # 110
    "Sau đó anh ta lại nhắn tin riêng cho Lục Tư Niên:",
    # 111
    "【Đại Bằng Tung Cánh】: Lục giáo sư, có phải anh quen biết Kỷ Cảnh không, thằng nhóc này lần trước còn hỏi tôi xem có biết chuyện giữa anh và nó không đấy.",
    # 112
    "Vương Bằng đã chuẩn bị sẵn tâm lý Lục Tư Niên sẽ không thèm đếm xỉa tới mình, bởi vì trước kia ở trong quân đoàn, Lục Tư Niên cũng chưa bao giờ trả lời bất kỳ chuyện gì không liên quan đến công việc.",
    # 113
    "Không ngờ lần này Lục Tư Niên lại trả lời rất nhanh chóng:",
    # 114
    "【Lục Tư Niên】: Quen biết.",
    # 115
    "Một lúc sau, anh lại nhắn tiếp:",
    # 116
    "【Lục Tư Niên】: Thứ Sáu tuần trước và thứ Hai tuần này cậu ấy đều không đến lớp đúng không.",
    # 117
    "【Đại Bằng Tung Cánh】: Chuyện này mà ngài cũng biết luôn á? Đúng vậy, cũng không rõ nguyên nhân vì sao, chính mồm nó bảo là nó bị ốm.",
    # 118
    "【Lục Tư Niên】: Được rồi, tôi biết rồi.",
    # 119
    "...",
    # 120
    "Kỷ Cảnh thu dọn quần áo định mang cho dì giúp việc giặt, mới sực nhớ ra trong chiếc áo khoác hôm nọ mặc đến nhà Lục Tư Niên vẫn còn cất đồ.",
    # 121
    "Cậu móc ống tiêm trong túi áo ra, cầm nó ngắm nghía qua lại một lượt.",
    # 122
    "Sau đó cầm nó bước vào phòng ngủ của Kỷ Vân Hy.",
    # 123
    "“Chị, chị xem giúp em cái này là thứ gì với, em nhìn không ra.”",
    # 124
    "Kỷ Cảnh đưa ống tiêm đến trước mắt Kỷ Vân Hy.",
    # 125
    "Kỷ Vân Hy là một Omega, Lục Tư Niên cũng là một Omega, cho nên Kỷ Vân Hy hẳn là ít nhiều cũng biết đôi chút.",
    # 126
    "Ai ngờ Kỷ Vân Hy cầm ống tiêm nhìn hồi lâu, đột nhiên như gặp phải ma quỷ vội vứt phắt ống tiêm trong tay đi.",
    # 127
    "“Vãi chưởng, thằng nhóc mày lấy thứ này ở đâu ra đấy?!” Sắc mặt Kỷ Vân Hy xám ngoét, nhào tới véo má cậu, “Mày có biết đây là thuốc cấm của Đế quốc không hả, bị ba mẹ biết được là mày chết chắc đấy!”",
    # 128
    "“Thuốc gì cơ?”",
    # 129
    "Kỷ Cảnh khẽ nhíu mày, nghiêm túc hỏi.",
    # 130
    "“Đây là thuốc ức chế đề kháng tin tức tố Omega,” Kỷ Vân Hy buông cậu ra, “Dùng nhiều thì tuyến thể Omega sẽ bị phế bỏ hoàn toàn, tương đương với tàn phế chức năng sinh lý, thể chất cũng sẽ bị tổn hại nghiêm trọng, thế nên mới bị cấm sử dụng.”",
    # 131
    "“Thế nên là, rốt cuộc mày đang yêu một Omega, hay là một Alpha nam hả?” Kỷ Vân Hy hiếm khi nhạy bén hỏi ngược lại cậu, “Cái này là của đối tượng mày đúng không, người ta thích mày mặc đồ con gái à?”",
    # 132
    "Kỷ Cảnh không lên tiếng, cậu vẫn đang mải suy nghĩ về chuyện ống thuốc kia.",
    # 133
    "“Đúng rồi, ngày mai giúp tao một việc đi.”",
    # 134
    "Kỷ Vân Hy chuyển chủ đề, tội nghiệp nhìn cậu.",
    # 135
    "Huyệt thái dương Kỷ Cảnh giật giật, tức tối hỏi: “Làm gì?”",
    # 136
    "“Có một tên Alpha nam cứ bám riết lấy tao mãi, bà đây đã bảo thẳng với hắn là tao không thích cái loại như hắn rồi, vậy mà cả ngày lẫn đêm cứ dính lấy tao không buông, làm cho người trong công ty tao ai cũng biết hết cả rồi.” Kỷ Vân Hy phẫn nộ nói.",
    # 137
    "Kỷ Cảnh nghe xong những lời này liền đoán ra Kỷ Vân Hy muốn cậu làm gì rồi.",
    # 138
    "“Ngày mai tao hẹn hắn ta ra ngoài, mày giả trang thành tao, làm cho hắn hết hy vọng, tiện thể dạy cho hắn một bài học luôn!” Kỷ Vân Hy siết chặt nắm đấm, sau đó nắm lấy tay Kỷ Cảnh làm nũng, “Được không hả, em trai ngoan của chị?”",
    # 139
    "Kỷ Cảnh rùng mình ớn lạnh một trận, hất tay cô ra: “Biết rồi, đợi đấy.”"
]

header = "---\ntitle: Chương 102: Giúp chị gái xử lý hoa đào\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written ch_102 translation successfully.")
