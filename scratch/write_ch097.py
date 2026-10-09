# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_097\translation.md"

paras = [
    # 000
    "Kỷ Cảnh cau mày lại, trong mắt đong đầy sự thâm trầm khó dò.",
    # 001
    "Lục Tư Niên đang nghi ngờ cậu sao?",
    # 002
    "Cậu cẩn thận hồi tưởng lại khoảng thời gian tiếp xúc vừa qua, nhưng không hề phát hiện ra mình đã để lộ sơ hở ở chỗ nào.",
    # 003
    "Buổi sáng Lục Tư Niên chẳng phải còn hỏi cậu có phải có một đứa em gái hay sao?",
    # 004
    "Kỷ Cảnh đặt mình vào góc độ của Lục Tư Niên để suy nghĩ, cảm thấy tuy đối phương chắc chắn sẽ sinh nghi, nhưng hẳn là sẽ không nghĩ đến chuyện chính cậu giả trang thành nữ Beta để theo đuổi anh.",
    # 005
    "Dù sao thì chuyện này cũng quá mức hoang đường.",
    # 006
    "Kỷ Cảnh nghiêng về khả năng Lục Tư Niên đang thăm dò mình hơn.",
    # 007
    "【Dịch Nam Nam Nam】: Đúng vậy, nếu xét theo quan hệ huyết thống thì là thế, nhưng em không hề muốn có cái thân phận này.",
    # 008
    "【Dịch Nam Nam Nam】: Anh có ý gì chứ, có phải là không tin em không?",
    # 009
    "【Dịch Nam Nam Nam】: Vậy anh cảm thấy em là ai, và tại sao em lại phải tiếp cận anh chứ?",
    # 010
    "【Lục Tư Niên】: Xin lỗi.",
    # 011
    "Kỷ Cảnh rũ mắt nhìn chăm chú vào màn hình quang học, sau đó tắt thiết bị đầu cuối, định bụng sẽ phớt lờ Lục Tư Niên một đêm.",
    # 012
    "Hôm sau Kỷ Cảnh ngủ đến khi tự nhiên tỉnh giấc, cậu theo thói quen mở thiết bị đầu cuối, phát hiện giao diện vẫn dừng lại ở tin nhắn cuối cùng do Lục Tư Niên gửi tới.",
    # 013
    "【Dịch Nam Nam Nam】: Em thức rồi.",
    # 014
    "Lục Tư Niên gần như trả lời ngay lập tức.",
    # 015
    "【Lục Tư Niên】: Ừ.",
    # 016
    "【Dịch Nam Nam Nam】: Anh vẫn chưa nói cho em biết, anh thích bộ đồ nào đâu đấy.",
    # 017
    "Mãi một lúc lâu sau,",
    # 018
    "【Lục Tư Niên】: Khoảng thời gian này trời sẽ trở lạnh.",
    # 019
    "Kỷ Cảnh nhìn dòng tin nhắn với vẻ mặt kỳ quặc một hồi lâu, mới dần dần nghiền ngẫm ra ý của Lục Tư Niên, ý anh là chê cậu mặc phong phanh quá sao?",
    # 020
    "Kỷ Cảnh cảm thấy không còn gì để nói.",
    # 021
    "Lục Tư Niên đúng thật là đồ ngốc, người ta ám chỉ đến nước này rồi mà vẫn ngơ ngác như khúc gỗ mục.",
    # 022
    "【Dịch Nam Nam Nam】: Vậy nên, hôm nay anh có ra ngoài không?",
    # 023
    "Kỷ Cảnh tiện tay gõ xong tin nhắn này rồi mới rời giường đi rửa mặt súc miệng.",
    # 024
    "Cậu đã bật chuông thông báo, tài khoản này chỉ kết bạn với duy nhất một mình Lục Tư Niên, căn phòng tĩnh mịch báo cho cậu biết Lục Tư Niên vẫn chưa hề trả lời.",
    # 025
    "Cậu sang phòng Kỷ Vân Hy chọn một chiếc váy dài màu trắng và áo khoác mỏng màu vàng nhạt, đội tóc giả chỉnh tề xong liền dưới ánh mắt đầy vẻ hồ nghi của Kỷ Vân Hy sải bước ra khỏi cửa nhà.",
    # 026
    "【Dịch Nam Nam Nam】: Nếu anh đã không muốn, vậy em tự đi ra ngoài một mình.",
    # 027
    "【Dịch Nam Nam Nam】: Em cứ mặc như bộ gửi cho anh hôm qua đấy.",
    # 028
    "【Lục Tư Niên】: Dịch Nam, tôi không thích hợp để bắt đầu một mối quan hệ tình cảm.",
    # 029
    "【Dịch Nam Nam Nam】: Ồ.",
    # 030
    "【Dịch Nam Nam Nam】: [Mèo con ủ rũ cụp đuôi.jpg]",
    # 031
    "【Dịch Nam Nam Nam】: Nhưng mà em thật sự rất thích anh mà.",
    # 032
    "Kỷ Cảnh chọn một thủy cung ở khu trung tâm Đế quốc, dựa theo những thông tin tìm hiểu trước đó, cậu cảm thấy Lục Tư Niên sẽ thích nơi này.",
    # 033
    "Bởi vì anh từng nói trong một bài phỏng vấn rằng bản thân hy vọng có cơ hội được tham gia chỉ huy tác chiến trên biển.",
    # 034
    "Xung quanh liên tục có đủ loại ánh mắt dò xét đổ dồn về phía Kỷ Cảnh, Kỷ Cảnh mở thiết bị đầu cuối, tiếp tục gửi tin nhắn.",
    # 035
    "【Dịch Nam Nam Nam】: Có một Alpha cứ đi theo em mãi.",
    # 036
    "【Dịch Nam Nam Nam】: Anh ta lại gần bắt chuyện với em rồi,",
    # 037
    "Lục Tư Niên trả lời quá nhanh, khiến cho câu tiếp theo của Kỷ Cảnh còn chưa kịp gõ xong.",
    # 038
    "【Lục Tư Niên】: Nói cái gì.",
    # 039
    "【Dịch Nam Nam Nam】: Anh ta xin phương thức liên lạc của em, bảo muốn cùng em đi dạo, còn hỏi em có bạn trai chưa nữa.",
    # 040
    "【Dịch Nam Nam Nam】: Lục Tư Niên, em nên trả lời thế nào đây?",
    # 041
    "Lục Tư Niên im lặng nhìn màn hình quang học, không biết nên đáp lời ra sao.",
    # 042
    "Anh biết, mình nên nói rằng: Dịch Nam, chuyện này phải xem em có bằng lòng tiếp xúc với anh ta hay không.",
    # 043
    "Thế nhưng cảm giác bực bội phiền muộn lại trào dâng nghẹn ứ nơi lồng ngực, khiến cho đầu óc vốn luôn tỉnh táo của anh trở nên rối bời.",
    # 044
    "【Dịch Nam Nam Nam】: Em bảo với anh ta là em có bạn trai rồi.",
    # 045
    "Lục Tư Niên thở phào nhẹ nhõm một cách khó hiểu.",
    # 046
    "【Dịch Nam Nam Nam】: Nhưng anh ta không tin, bảo nếu có bạn trai thì cớ sao ngày lễ tình nhân lại đi ra ngoài một mình.",
    # 047
    "Lục Tư Niên giật mình, mở lịch Đế quốc xem ngày hôm nay, trên đó rõ ràng hiển thị ba chữ “lễ tình nhân”.",
    # 048
    "Hóa ra hôm nay là ngày lễ tình nhân?",
    # 049
    "Lời mời hẹn bất ngờ từ ngày hôm qua của Dịch Nam dường như đã có được một lời giải thích hợp lý hơn.",
    # 050
    "【Dịch Nam Nam Nam】: Lục Tư Niên, anh ta túm lấy tay em không cho em đi!",
    # 051
    "Chiếc bút máy kiểu cũ trên tay rơi cạch một tiếng xuống mặt bàn.",
    # 052
    "Lục Tư Niên nhìn chiếc bút trên bàn, ngẩn người trong giây lát, sau đó đẩy ghế từ từ đứng dậy.",
    # 053
    "【Lục Tư Niên】: Ở đâu.",
    # 054
    "Kỷ Cảnh hài lòng cười híp mắt, gửi một định vị sang đó.",
    # 055
    "Kỷ Cảnh, người từ đầu đến cuối tự biên tự diễn thêu dệt nên một câu chuyện cho Lục Tư Niên, lúc này đang đứng giữa quảng trường, trở thành tâm điểm thị giác của cả khu vực.",
    # 056
    "Một số Alpha xung quanh, thậm chí cả vài nữ Omega đã để ý thấy mỹ nhân trước mắt này đứng ở đây được một lúc rồi, bắt đầu rục rịch muốn tiến lên bắt chuyện.",
    # 057
    "Vừa có một Alpha to gan chuẩn bị bước qua, liền phát hiện có một người đàn ông dáng người cao lớn mang vẻ vội vã sải bước chạy đến trước mặt mỹ nhân.",
    # 058
    "Lục Tư Niên đến rất nhanh, lúc chạy tới nơi mới nhận ra bên cạnh Kỷ Cảnh chẳng hề có gã đàn ông nào, cũng không hề ăn mặc như trong ảnh.",
    # 059
    "Chiếc áo mỏng màu vàng nhạt tôn lên làn da trắng nõn như ngọc mỡ cừu của thiếu nữ.",
    # 060
    "Thiếu nữ ngoái đầu nhìn anh mỉm cười.",
    # 061
    "Lục Tư Niên lại ngẩn người: “Người đâu rồi?”",
    # 062
    "“Đi rồi, thấy đông người quá nên chạy mất dép rồi.” Kỷ Cảnh chẳng thèm nghĩ ngợi liền nói dối trơn tru.",
    # 063
    "Ý xấu thoáng lướt qua trong mắt thiếu nữ khiến Lục Tư Niên thất thần.",
    # 064
    "“Cho anh này.”",
    # 065
    "Kỷ Cảnh lấy ra bó hoa hồng tiện tay vơ được ở nhà trước khi đi, đưa đến trước mặt Lục Tư Niên.",
    # 066
    "Xung quanh truyền đến những tiếng hít hà khe khẽ.",
    # 067
    "“Mẹ kiếp, đúng là bạn trai của em ấy thật rồi!”",
    # 068
    "“Nhìn cách ăn mặc thì gã đàn ông này tuổi tác không nhỏ đâu, mặc đồ như ông chú ba bốn mươi tuổi vậy, chẳng qua mặt mũi đẹp trai với người cao ráo hơn chút thôi.”",
    # 069
    "“Đúng đấy, nhìn vẻ ngoài cũng chẳng giống đại gia có tiền, rốt cuộc coi trúng điểm gì ở anh ta chứ?”",
    # 070
    "“Tôi bảo mấy người bớt ghen ăn tức ở đi, diện mạo với khí chất của người ta hoàn toàn không cùng đẳng cấp với các người đâu, áo sơ mi quần âu nho nhã đẹp trai thế kia cơ mà.”",
    # 071
    "...",
    # 072
    "Những lời bàn tán xôn xao xung quanh lọt vào tai hai người, Lục Tư Niên nhìn thiếu nữ trước mặt, bất động thanh sắc kéo giãn ra một khoảng cách nhỏ.",
    # 073
    "Kỷ Cảnh thấy anh không nhận, dứt khoát nhét thẳng bó hoa hồng vào lồng ngực anh.",
    # 074
    "“Em đã mua hai vé vào cổng rồi, nhân lúc chưa đông người lắm mau đi xếp hàng thôi.”",
    # 075
    "Kỷ Cảnh nói xong liền cười tươi, kéo Lục Tư Niên đi về phía lối vào.",
    # 076
    "Lục Tư Niên bị cậu kéo đi về phía trước, đột nhiên nhận ra Dịch Nam vừa rồi có lẽ đã lừa mình.",
    # 077
    "Ngày lễ tình nhân rất đông đúc, hàng người xếp hàng cũng rất dài, vì chật chội nên Lục Tư Niên bất đắc dĩ phải đứng rất sát bên cạnh Kỷ Cảnh.",
    # 078
    "Kỷ Cảnh rất cao, nếu đứng gần thêm chút nữa, Lục Tư Niên gần như có thể chạm vào chóp mũi đối phương.",
    # 079
    "Anh nhận ra chiều cao của Dịch Nam cũng tương đương với Kỷ Cảnh.",
    # 080
    "“Lục Tư Niên, có phải anh thích biển lớn không?” Hơi thở ấm áp của thiếu nữ phả vào bên tai Lục Tư Niên, nhuộm lên đó một tầng ửng hồng nhạt.",
    # 081
    "Lục Tư Niên cảm thấy tuyến thể sau gáy mình lại bắt đầu ngứa ngáy.",
    # 082
    "“Ừ,” anh đáp.",
    # 083
    "“Anh đoán xem vì sao em lại biết anh thích biển lớn nào?” Kỷ Cảnh hỏi ngược lại.",
    # 084
    "“Vì sao?” Lục Tư Niên là người khô khan tẻ nhạt, chỉ có thể như nghiên cứu một vấn đề học thuật mà hỏi rõ nguyên nhân.",
    # 085
    "Kỷ Cảnh nhìn thẳng vào mắt anh: “Bởi vì, em đã đặc biệt lên mạng tra cứu thông tin về anh đấy, anh từng nói trong phỏng vấn rằng anh muốn đi tác chiến trên biển, cho nên em đoán anh nhất định rất thích biển cả.”",
    # 086
    "Nói xong thì cũng sắp đến lượt bọn họ, Kỷ Cảnh liền quay người chuẩn bị quét vé, nào ngờ Lục Tư Niên ở phía sau đang ngơ ngẩn nhìn theo bóng lưng của cậu xuất thần.",
    # 087
    "Khu vực đầu tiên bước vào là nhà trưng bày sứa, người quá đông nên Kỷ Cảnh nắm lấy ống tay áo của Lục Tư Niên, Lục Tư Niên không hiểu sao cũng không hề phản đối.",
    # 088
    "“Lục Tư Niên, tại sao anh lại thích biển cả thế?”",
    # 089
    "Kỷ Cảnh hỏi.",
    # 090
    "Lục Tư Niên nhìn góc nghiêng gương mặt cậu, nói: “Bởi vì tôi chưa từng được nhìn thấy biển.”",
    # 091
    "Khoa học công nghệ hiện đại của Đế quốc cực kỳ phồn vinh phát triển, chỉ cần tùy tiện ngồi phi thuyền là có thể đi tới bất kỳ vùng biển nào.",
    # 092
    "Nếu Lục Tư Niên ngay cả biển lớn cũng chưa từng thấy, chứng tỏ cuộc sống bao năm qua của anh thực sự vô cùng phẳng lặng tẻ nhạt.",
    # 093
    "Kỷ Cảnh nhíu mày: “Vậy anh từng đến thủy cung chưa?”",
    # 094
    "“Chưa,” Lục Tư Niên nói, “Hôm nay, là lần đầu tiên của tôi.”",
    # 095
    "Kỷ Cảnh thực sự có chút chấn động.",
    # 096
    "“Tại sao?”",
    # 097
    "Lục Tư Niên ngước mắt nhìn về phía trước, thản nhiên nói: “Trước kia là vì không có tiền, sau này thì vì không có thời gian.”",
    # 098
    "Đi theo dòng người di chuyển về phía trước, không biết từ lúc nào họ đã bước tới khu vực biển sâu.",
    # 099
    "“Thế còn công viên giải trí, quán bar, đấu trường thú, tiệm chơi game...” Kỷ Cảnh đếm từng nơi một, “Mấy chỗ này anh đã từng đi chưa?”",
    # 100
    "“Chưa từng.”",
    # 101
    "Kỷ Cảnh mang ánh mắt phức tạp nhìn Lục Tư Niên một cái.",
    # 102
    "Cuối cùng cậu cũng hiểu vì sao Lục Tư Niên lại tẻ nhạt và trầm mặc ít nói đến vậy rồi.",
    # 103
    "Cậu sải bước lên một bước, đứng đối diện trước mặt Lục Tư Niên, nói: “Lục Tư Niên, sau này em dẫn anh đi.”",
    # 104
    "Ngăn cách sau cặp kính nửa gọng màu đen, đôi mắt đen sâu thẳm của Lục Tư Niên nhìn chăm chú vào cậu, nhưng không đưa ra lời đáp lại.",
    # 105
    "Đúng lúc này, trong đám đông đột nhiên vang lên một tràng kinh thán.",
    # 106
    "Hai người nhìn theo hướng âm thanh phát ra, mới nhận ra trên đỉnh đầu có một đàn cá rực rỡ sắc màu đang bơi qua, tựa như một đóa hoa đột ngột bung nở, từng bông từng bông điểm xuyết giữa lòng biển sâu xanh thẳm u tối.",
    # 107
    "Ánh mắt hai người vô tình chạm nhau.",
    # 108
    "Kỷ Cảnh nhìn Lục Tư Niên trước mắt, đột nhiên nói: “Lục Tư Niên, anh có biết hay không, bây giờ nhìn anh trông rất dễ hôn đấy.”",
    # 109
    "Xung quanh quá đỗi ồn ào, Lục Tư Niên dường như không nghe rõ, nhưng ánh mắt lại dính chặt vào đôi môi của Kỷ Cảnh.",
    # 110
    "Ánh mắt Kỷ Cảnh trầm xuống, sau đó đột ngột cúi người, hôn lên gò má của Lục Tư Niên.",
    # 111
    "“Lục Tư Niên, em bảo là nhìn anh trông rất dễ hôn.”",
    # 112
    "Đàn cá một lần nữa ùa về phía đường hầm bằng kính, khơi dậy thêm một tràng trầm trồ kinh ngạc.",
    # 113
    "Chạm vào liền tách ra.",
    # 114
    "Hơi thở Lục Tư Niên rối loạn, vành tai nối liền xuống sau gáy dần dần nhuốm lên một mảng đỏ rực.",
    # 115
    "Anh lại ngửi thấy mùi vị rượu Tequila nồng cay quen thuộc trên người đối phương.",
    # 116
    "Anh muốn nói điều gì đó, nhưng Kỷ Cảnh đã quay người bước về phía trước.",
    # 117
    "Thủy cung này rất lớn, khi hai người bước ra khỏi khu trưng bày cuối cùng thì trời đã tối sầm lại.",
    # 118
    "Đa số mọi người đều chen chúc bên lề đường đợi xe, Kỷ Cảnh tính toán thời gian, lên kế hoạch cho bước tiếp theo nên làm gì.",
    # 119
    "Kết quả nghĩ được một nửa thì bụng cậu réo lên ùng ục, bị Lục Tư Niên nghe thấy, anh liền hỏi Kỷ Cảnh muốn ăn gì, Kỷ Cảnh ngẫm nghĩ một lát, quyết định cùng anh đi ăn tối ở gần đó.",
    # 120
    "Bữa tối Lục Tư Niên cũng ăn rất yên tĩnh, trong lúc ăn tuyệt đối không tùy tiện nói chuyện, hơn nữa còn giống hệt như ở nhà ăn trường học, chẳng biết từ lúc nào đã đi trả tiền xong xuôi.",
    # 121
    "Lục Tư Niên lái xe tới, đối với Kỷ Cảnh thì chiếc xe này không tính là đắt tiền, nhưng xét theo quân hàm quan chức của Lục Tư Niên thì lại khá tương xứng.",
    # 122
    "“Tôi đưa em về nhà.” Lục Tư Niên nói với cậu.",
    # 123
    "Kỷ Cảnh nghe vậy lập tức tỉnh cả ngủ, cậu vẫn chưa bịa ra địa chỉ nhà của “Dịch Nam”, đột nhiên bị hỏi thăm căn bản không biết nên ứng phó ra sao.",
    # 124
    "Thế là cậu bảo với Lục Tư Niên rằng mình sống ở ngay gần đây thôi, có thể tự đi bộ về được.",
    # 125
    "Lục Tư Niên nhìn cậu rất lâu, ngay vào lúc Kỷ Cảnh nghĩ rằng Lục Tư Niên đã nhìn ra manh mối gì đó thì anh lại nói lời từ biệt với cậu.",
    # 126
    "Trước khi đi, Lục Tư Niên đột nhiên gọi với lại,",
    # 127
    "“Dịch Nam, ở gần trường có một căn hộ đang cho thuê, em có muốn chuyển đến đó ở không.”",
    # 128
    "“Gì cơ?”",
    # 129
    "Kỷ Cảnh một lần nữa bị Lục Tư Niên làm cho trở tay không kịp.",
    # 130
    "“Em nói ba dượng của em khi say rượu sẽ đánh em,” Lục Tư Niên nhìn cậu, “Em dọn ra ngoài ở một mình thì ông ta sẽ không làm tổn thương em được nữa, em gặp nguy hiểm cũng có thể tìm tôi.”",
    # 131
    "“Tìm anh?” Kỷ Cảnh cong môi, cậu hiểu ý của Lục Tư Niên rồi, “Nhưng mà...”",
    # 132
    "“Nếu em muốn ở, không cần phải lo lắng về vấn đề tiền bạc,” vẻ mặt Lục Tư Niên mang theo một tia nghiêm túc đứng đắn, “Nếu em thực sự có hứng thú với ngành chỉ huy, mỗi ngày em có thể cùng tôi vào trường, tôi sẽ dạy em, em rất có thiên phú.”",
    # 133
    "“Lục Tư Niên,” Kỷ Cảnh bất thình lình cắt ngang lời anh, “Tại sao lại phải làm như vậy?”",
    # 134
    "“Nếu em đồng ý, vậy thì anh với em tính là quan hệ gì?”"
]

header = "---\ntitle: Chương 97: Nếu em đồng ý thì sao\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written ch_097 translation successfully.")
