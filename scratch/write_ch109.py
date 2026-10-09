# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_109\translation.md"

paras = [
    # 000
    "Tối hôm kết quả bỏ phiếu đề xuất được công bố chính thức, Kỷ Cảnh ngồi trong văn phòng của Kỷ Trình.",
    # 001
    "“Tiểu Cảnh, thứ con muốn thì ba đã cho con rồi,” Kỷ Trình ngồi trên chiếc ghế da, đầu ngón tay khẽ gõ lên mặt bàn, xoay một vòng, nghiêm túc nói, “Chuyện con đã hứa với ba, ba cũng hy vọng con có thể thực hiện được.”",
    # 002
    "Đối với Kỷ Trình mà nói, việc Omega khôi phục quyền tòng quân không thể nói là không có ảnh hưởng gì tới nhà họ Kỷ, sở dĩ ông đồng ý với thỉnh cầu của Kỷ Cảnh là bởi vì Kỷ Cảnh đã chịu nhượng bộ thỏa hiệp.",
    # 003
    "Kỷ Cảnh đã dùng sự lùi bước của bản thân để đem ra trao đổi.",
    # 004
    "“Con biết rồi thưa ba, sau khi tốt nghiệp con sẽ theo ba học cách tiếp quản nhà họ Kỷ.” Kỷ Cảnh nhìn kết quả, thở dài một hơi thật sâu, “Thế nhưng con cũng chỉ đồng ý trong thời hạn năm năm thôi đấy nhé.”",
    # 005
    "“Năm năm sau, nếu con vẫn không thích cái thân phận người thừa kế Kỷ gia này, con sẽ đi du lịch khắp các vì sao, đến lúc đó ba vẫn nên nghĩ cách giao lại cho chị gái đi, nếu chị ấy đồng ý.”",
    # 006
    "Kỷ Cảnh nhún nhún vai.",
    # 007
    "“Con...” Kỷ Trình tức đến mức không thốt nên lời, “Đều tại mẹ con nuông chiều các con quá mức hư đốn rồi.”",
    # 008
    "“Tiểu Cảnh, con vẫn chưa nói cho ba biết tại sao lại nhất quyết bắt ba bỏ phiếu thuận đấy...”",
    # 009
    "“Ba, con đi tắm đây!”",
    # 010
    "Kỷ Cảnh ngắt lời Kỷ Trình, nhanh như chớp chuồn mất khỏi thư phòng.",
    # 011
    "Dự luật đã được thông qua rồi, Lục Tư Niên ước chừng vui sướng phát điên lên rồi nhỉ?",
    # 012
    "Kỷ Cảnh vừa trở về phòng vừa thầm nghĩ.",
    # 013
    "Nếu không có gì bất ngờ xảy ra, anh hẳn là sẽ rất nhanh được trở lại Đệ tam quân đoàn thôi.",
    # 014
    "Như vậy cũng tốt, cậu nên nhân khoảng thời gian này mau chóng cày nốt cho xong thanh tiến độ, đến lúc đó... Lục Tư Niên đến quân đoàn, bản thân ở lại trường học, không gặp lại nhau nữa thì bọn họ cũng sẽ rất nhanh quên đi đối phương thôi.",
    # 015
    "Kỷ Cảnh rũ mi mắt xuống, không biết đang suy nghĩ điều gì.",
    # 016
    "Cậu mở thiết bị đầu cuối ra,",
    # 017
    "【Dịch Nam Nam Nam】: Lục Tư Niên, ngày mai là cuối tuần, chúng ta...",
    # 018
    "Mấy chữ 'ra ngoài hẹn hò có được không' còn chưa kịp gõ xong, Kỷ Cảnh đã bị âm thanh thông báo vang dội như sấm sét của hệ thống làm cho trở tay không kịp.",
    # 019
    "【Ting tong! Chúc mừng ký chủ đã hoàn thành xuất sắc nhiệm vụ chính: Tiến độ phản diện theo đuổi nhân vật chính đã chính thức đạt mốc 80%!】",
    # 020
    "【Ting tong, dữ liệu đang được tải lên máy chủ, đếm ngược giải trừ trói buộc hệ thống: 3 — 2 — 1】",
    # 021
    "【Ting tong, đã hoàn tất giải trừ trói buộc, chúc mừng ký chủ, từ nay về sau quyền chi phối ý thức thân thể hoàn toàn thuộc về riêng người, chúc người một tương lai xán lạn rực rỡ!】",
    # 022
    "Con bướm bảy sắc cầu vồng từ từ hiện hình, ngay sau đó một luồng ánh sáng dịu nhẹ bao bọc lấy Kỷ Cảnh đang ngơ ngác đờ đẫn.",
    # 023
    "Đầu óc Kỷ Cảnh hoàn toàn trống rỗng, còn chưa kịp phản ứng thì đã cảm thấy cảm giác trói buộc gông cùm trong cơ thể nháy mắt tan biến không còn dấu vết.",
    # 024
    "“Ý gì đây?”",
    # 025
    "Kỷ Cảnh định thần lại, giọng điệu bỗng chốc cất cao, chân mày hiện lên vẻ sốt ruột lo âu, “Ý là tao đã hoàn thành xong nhiệm vụ rồi? Chuyện này không thể nào, sao tự dưng lại vô duyên vô cớ nhảy vọt lên 80% thế được.”",
    # 026
    "Mật Bảo nhìn ký chủ có phần nôn nóng cuống quýt, âm thầm rụt rè nép vào trong góc:",
    # 027
    "【Hức... Hệ thống tuyệt đối không thể xảy ra sai sót được đâu á, hoàn thành xong nhiệm vụ chẳng phải rất tốt sao, sao ký chủ trông có vẻ không hài lòng thế nè.】",
    # 028
    "Như thể bị chạm đúng vào điểm yếu nhạy cảm, sắc mặt Kỷ Cảnh lập tức sa sầm xuống, cậu khẽ nghiến răng hàm sau, một lúc sau mới trầm giọng bình tĩnh nói:",
    # 029
    "“Không vui? Làm sao có thể, tao cầu còn chẳng được ấy chứ, tao đâu có sở thích bệnh hoạn làm phụ nữ đâu.”",
    # 030
    "【Có lẽ ký chủ có thể thử cày tiến độ lên mốc 100% nha, đến lúc đó sẽ có phần thưởng thần bí đó!】",
    # 031
    "Tầm mắt Kỷ Cảnh rơi vào dòng tin nhắn chưa kịp gửi đi mà chẳng có tiêu cự, hồi lâu sau, cậu nói:",
    # 032
    "“Thôi khỏi, cứ thế này đi.”",
    # 033
    "Lục Tư Niên không nên tiếp tục bị cậu lừa dối thêm nữa, mối quan hệ hoang đường nực cười giữa hai người cũng nên chấm dứt dấu chấm hết tại đây rồi.",
    # 034
    "Từng chữ từng chữ trong khung chat bị Kỷ Cảnh xóa sạch, rồi gõ lại những dòng mới:",
    # 035
    "【Dịch Nam Nam Nam】: Lục Tư Niên, khoảng thời gian này em đã suy nghĩ rất nhiều.",
    # 036
    "【Dịch Nam Nam Nam】: Có lẽ chúng ta căn bản không thích hợp để làm người yêu của nhau.",
    # 037
    "【Dịch Nam Nam Nam】: Em muốn chia tay rồi.",
    # 038
    "【Dịch Nam Nam Nam】: Chia tay đi Lục Tư Niên.",
    # 039
    "Sau khi gửi dòng tin nhắn cuối cùng đi, Kỷ Cảnh lập tức tắt phụt thiết bị đầu cuối, vớ lấy chiếc gối trên giường úp chặt lên mặt mình.",
    # 040
    "Cậu thầm nghĩ Lục Tư Niên anh không được phép hận tôi, tôi đã bù đắp cho anh rồi, cho nên anh không có quyền hận tôi.",
    # 041
    "Thời gian dường như ngưng đọng lại sau khi cậu gửi tin nhắn đi, cậu cảm thấy vạn vật xung quanh đều trở nên chậm chạp, ngoại trừ trái tim đang đập thình thịch điên cuồng vì bất an của chính mình.",
    # 042
    "Cậu cố tình phớt lờ việc thiết bị đầu cuối có tin nhắn gửi tới hay không, thế là cậu lao vào chơi vài ván game, nhưng càng chơi lại càng thấy phiền muộn bực bội, trận nào cũng thua tơi bời thảm hại.",
    # 043
    "Lục Tư Niên sẽ nói gì đây? Anh sẽ níu kéo mình sao, hay là sẽ thản nhiên chấp nhận? Một người đàn ông như Lục Tư Niên rất khó có những phản ứng mãnh liệt kích động nhỉ.",
    # 044
    "Kỷ Cảnh không thể khống chế nổi bản thân cứ mãi suy nghĩ về phản ứng của Lục Tư Niên, nghĩ tới nghĩ lui cuối cùng mới định thần lại, cậu bước tới bên mép giường, nhặt chiếc thiết bị đầu cuối bị ném sang một bên lên, mở ra.",
    # 045
    "Trong giao diện khung chat, Lục Tư Niên nửa tiếng trước đã gửi tới một tin nhắn thoại.",
    # 046
    "Chỉ có duy nhất một tin nhắn thoại.",
    # 047
    "Kỷ Cảnh bấm mở tin nhắn thoại,",
    # 048
    "“Dịch Nam, chúng ta gặp nhau một lần có được không, tôi nghĩ chúng ta cần phải nói chuyện tử tế một lần.”",
    # 049
    "Giọng nam trầm ấm thông qua luồng sóng âm vô hình truyền thẳng vào tai Kỷ Cảnh, nơi cổ họng Lục Tư Niên dường như có thứ gì đó nghẹn ứ chẹn ngang, khó chịu và đau nhói.",
    # 050
    "Kỷ Cảnh cảm thấy nơi lồng ngực một trận nghẹt thở ngột ngạt, cậu tựa như lại nhìn thấy bộ dạng của Lục Tư Niên lúc say rượu ngày hôm đó.",
    # 051
    "Mày còn đang xoắn xuýt do dự cái gì nữa chứ, đừng mẹ nó tiếp tục dây dưa dùng dằng với Lục Tư Niên nữa.",
    # 052
    "Nơi đáy mắt Kỷ Cảnh bùng lên một tầng lửa ngầm u ám.",
    # 053
    "【Dịch Nam Nam Nam】: Không muốn gặp, chẳng có lý do gì cả, không thích nữa chính là không thích.",
    # 054
    "【Dịch Nam Nam Nam】: Nếu nhất định phải nói lý do, thì là vì anh quá đỗi tẻ nhạt khô khan, chẳng có chút thú vị nào.",
    # 055
    "【Dịch Nam Nam Nam】: Chỉ là một mối tình mà thôi, kết thúc thì là kết thúc rồi, anh sẽ còn gặp được rất nhiều người phù hợp với anh.",
    # 056
    "【Dịch Nam Nam Nam】: Sẽ luôn có người yêu tất cả mọi thứ thuộc về anh, nhưng người đó tuyệt đối không phải là em.",
    # 057
    "【Dịch Nam Nam Nam】: Lục Tư Niên, đừng tìm em nữa.",
    # 058
    "Kỷ Cảnh tựa như vô cùng sợ hãi sẽ phải chờ đợi tin nhắn phản hồi của Lục Tư Niên, nhanh chóng thoát khỏi giao diện trò chuyện, trực tiếp xóa bỏ hủy luôn tài khoản này.",
    # 059
    "Nhìn tài khoản của “Dịch Nam” hoàn toàn xám xịt biến mất, chút cảm xúc nơi đáy mắt Kỷ Cảnh từng chút từng chút một rút đi.",
    # 060
    "Cậu trước sau vẫn không nói ra sự thật, cậu không rõ vì sao bản thân lại không dám nói, cậu cảm thấy làm như vậy đã đủ để Lục Tư Niên hết hy vọng rồi, có nói cho anh biết sự thật hay không cũng chẳng còn quan trọng nữa.",
    # 061
    "Kể từ khi “Dịch Nam” biến mất khỏi thế giới này, Kỷ Cảnh dường như đã quay trở lại trạng thái trước kia.",
    # 062
    "Cậu không còn phải vội vã thay đồ con gái chạy tới trường nữa, cũng không cần vắt óc tìm đủ mọi cách để ngụy trang thành Dịch Nam.",
    # 063
    "Cậu không biết mấy ngày nay Lục Tư Niên đang làm gì, chỉ là thỉnh thoảng ở bên ngoài sân tập lại vô tình thoáng thấy bóng dáng của Lục Tư Niên.",
    # 064
    "Không biết có phải ảo giác hay không, mỗi khi cậu đưa mắt nhìn sang thì Lục Tư Niên liền cất bước rời đi.",
    # 065
    "Con đường duy nhất có thể nghe được cái tên Lục Tư Niên chính là từ Vương Bằng.",
    # 066
    "“Thằng nhóc, chuyện tuyển quân của Đệ tam quân đoàn cậu đã cân nhắc đến đâu rồi?” Vương Bằng vừa huấn luyện học sinh xong, cả người đầy mồ hôi ngồi phịch xuống bên cạnh Kỷ Cảnh.",
    # 067
    "“Vẫn chưa cân nhắc.” Kỷ Cảnh nói.",
    # 068
    "Vương Bằng vỗ bốp một cái vào lưng Kỷ Cảnh: “Thằng nhóc cậu rốt cuộc đang do dự cái gì thế hả? Ngay cả Lục Tư Niên Lục tổng chỉ huy cũng sắp quay trở lại Đệ tam quân đoàn rồi kìa, có cậu ấy ở đó Đệ tam quân đoàn chỉ có ngày càng hùng mạnh hơn thôi.”",
    # 069
    "“Anh ấy sắp quay lại rồi sao...” Kỷ Cảnh khẽ lẩm bẩm một câu bằng giọng rất nhỏ.",
    # 070
    "“Ai cơ? Lục Tư Niên á, đúng vậy, trong tháng này coi như có thể hoàn tất xong thủ tục phục chức rồi.” Vương Bằng vô tư nói, “Chỉ là không biết sao tự dưng lại đùng đùng quay trở lại, chậc, cái tên Lâm Diên Sơn kia ước chừng sắp tức đến phát điên rồi.”",
    # 071
    "Kỷ Cảnh đã không còn nghe lọt tai những lời Vương Bằng nói sau đó nữa, sau khi chuông tan học vang lên, cậu đúng giờ đứng dậy, sải bước ra khỏi sân tập.",
    # 072
    "Trong trường học vẫn treo đầy thông báo tuyển quân của Đệ tam quân đoàn khắp nơi, Kỷ Cảnh ma xui quỷ khiến thế nào lại dừng bước trước một tấm áp phích thông báo, nhìn thấy trên đó ghi rõ thời gian là vào chiều thứ Sáu.",
    # 073
    "Bên cạnh còn có rất nhiều học viên của Học viện Quân sự Đế quốc đang đứng, Kỷ Cảnh khó tránh khỏi nghe thấy cuộc trò chuyện của họ:",
    # 074
    "“Hôm nay cậu có đi học tiết của Lục giáo sư không? Tớ nghe người ta đồn hình như thầy ấy sắp đi rồi, hôm nay tớ đặc biệt đến để ngắm thầy ấy đấy, kết quả là người ta căn bản không có ở đó luôn!”",
    # 075
    "“Tớ cũng đi nè! Đổi thành một giáo sư bụng bia rồi, bảo là Lục giáo sư từ hôm qua đã ngừng giảng dạy rồi, hu hu hu tớ biết thế đã đi từ hôm qua rồi, lần này biết bao giờ mới được gặp lại thầy ấy nữa đây.”",
    # 076
    "Một Omega nũng nịu than thở oán trách.",
    # 077
    "Lục Tư Niên không dạy học nữa rồi sao, nhanh đến thế ư?",
    # 078
    "Kỷ Cảnh nghe vậy ngẩn người ra một thoáng, đang định nghe xem đám Omega đằng kia nói gì tiếp thì mí mắt phải của cậu đột nhiên giật mạnh một cái thật mạnh.",
    # 079
    "Ngay sau đó, một cảm giác nguy cơ mãnh liệt ập thẳng vào lồng ngực.",
    # 080
    "Còn chưa đợi cậu kịp phản ứng xem rốt cuộc là có chuyện gì, bên tai bỗng nhiên vang lên từng hồi chuông báo động chói tai inh ỏi.",
    # 081
    "【Nguy hiểm! Nguy hiểm! Phát hiện đối tượng nhiệm vụ sắp sửa đối mặt với rủi ro trong cốt truyện gốc, xin ký chủ hãy nhanh chóng tới hiện trường để hóa giải nguy cơ.】",
    # 082
    "Hô hấp của Kỷ Cảnh nghẹn lại: “Rủi ro gì cơ?”",
    # 083
    "【Phát hiện một trong những phản diện của nguyên tác là Lâm Diên Sơn đang tiến hành hành động theo cốt truyện gốc, xin ký chủ hãy nhanh chóng tới đó!】",
    # 084
    "Cái tên Lâm Diên Sơn vừa thốt ra, Kỷ Cảnh liền lập tức nhớ lại cuốn tiểu thuyết nguyên tác mà cậu từng xem trước đây.",
    # 085
    "Vào giai đoạn giữa và cuối khi Lục Tư Niên bị Kỷ Cảnh giày vò tra tấn, tên phản diện Lâm Diên Sơn vì nhiều lần bị chèn ép thất bại trong quân đoàn nên sinh lòng oán hận, đã tra cứu trái phép địa chỉ nhà của Lục Tư Niên, và hung hãn xông tới định dùng tin tức tố Alpha làm nhục Lục Tư Niên để trút giận uất hận trong lòng.",
    # 086
    "“Lục Tư Niên sắp quay lại quân đoàn rồi, Lâm Diên Sơn ước chừng tức phát điên lên rồi.”",
    # 087
    "Câu nói bâng quơ của Vương Bằng cứ văng vẳng bên tai Kỷ Cảnh.",
    # 088
    "【Đã mở đường hầm không gian cho ký chủ.】 Mật Bảo chu đáo mở ra cánh cổng dịch chuyển cho Kỷ Cảnh.",
    # 089
    "“Mẹ kiếp...”",
    # 090
    "Trong đầu Kỷ Cảnh toàn bộ đều là Lâm Diên Sơn, hoàn toàn không có thời gian để suy nghĩ những thứ khác, cậu tung một cước đạp văng cánh cửa lao thẳng vào trong đường hầm.",
    # 091
    "Vừa đạp cửa xông ra ngoài, Kỷ Cảnh đã bị một mùi bạc hà nồng nặc sặc sụa hun đến đỏ hoe cả mắt.",
    # 092
    "Bên tai truyền đến một tiếng nổ lớn, tựa như tiếng chai thủy tinh bị đập nát vỡ vụn bắn tung tóe khắp mặt sàn.",
    # 093
    "“Lục Tư Niên, mày mẹ nó chỉ là một con Omega sinh ra để người ta đè dưới thân thì có tư cách gì mà quay lại quân đoàn, mày dựa vào cái gì mà tranh giành với tao, dựa vào cái gì mà Trương Mạc trong mắt chỉ có một mình mày, tao có chỗ nào thua kém mày chứ!”",
    # 094
    "Giọng nói của Lâm Diên Sơn tựa như một kẻ điên gào thét cuồng loạn, nghe những tiếng va chạm trầm đục có thể thấy hắn ta đang cận chiến vật lộn với Lục Tư Niên.",
    # 095
    "“Sao mày lại không có phản ứng gì với tin tức tố của tao, hả, mày tưởng tao không biết sao, mày tìm Nguyễn Uyên xin thuốc kháng chế Omega, không có thuốc kháng chế mày mẹ nó đã bị tao đánh chết từ lâu rồi... Á——”",
    # 096
    "“Đánh? Bây giờ thì sao, mày còn dám đánh với tao nữa không?” Giọng nói trầm khàn vì vật lộn của Lục Tư Niên truyền ra từ bên trong cánh cửa.",
    # 097
    "Kỷ Cảnh hung hãn đạp tung cánh cửa lớn, đập ngay vào mắt là cảnh tượng Lục Tư Niên đang đè nghiến Lâm Diên Sơn trên đống mảnh vỡ thủy tinh.",
    # 098
    "Lục Tư Niên rõ ràng không ngờ tới việc Kỷ Cảnh lại xuất hiện ở đây, ngay cả động tác cũng vì hành động phá cửa của Kỷ Cảnh mà khựng lại mất nửa giây.",
    # 099
    "Ánh mắt Lâm Diên Sơn lóe lên tia tàn độc, nhân cơ hội thoát khỏi sự kìm kẹp của Lục Tư Niên, liên tục lùi lại kéo giãn khoảng cách với Lục Tư Niên.",
    # 100
    "Lục Tư Niên liếc nhìn Kỷ Cảnh, đôi mắt hẹp dài dưới tròng kính khẽ lạnh đi, muốn giải quyết Lâm Diên Sơn trước.",
    # 101
    "“Mày tưởng mày tiêm thuốc kháng chế rồi thì không phải là một Omega nữa sao, hôm nay tao sẽ cho mày thấy Omega trước mặt Alpha phải có bộ dạng thế nào——”",
    # 102
    "Lâm Diên Sơn đột nhiên nở nụ cười điên loạn thần kinh, lướt người lao tới tấn công Lục Tư Niên.",
    # 103
    "Kỷ Cảnh nhìn thấy nơi tay phải của Lâm Diên Sơn lóe lên một vệt sáng lạnh lẽo, tim cậu thắt lại rung chuyển, sải bước lao vào chắn ngang giữa hai người, giơ tay ra chặn đòn của Lâm Diên Sơn.",
    # 104
    "Lâm Diên Sơn không ngờ Kỷ Cảnh lại xen vào can thiệp, bị thế công của Kỷ Cảnh đánh cho không còn chút sức lực chống đỡ nào, hắn hoảng sợ nhận ra bản thân ngay cả một Alpha tân sinh viên cũng đánh không lại.",
    # 105
    "Ngay khi Kỷ Cảnh chuẩn bị vặn ngược tay Lâm Diên Sơn ra sau lưng, Lâm Diên Sơn gầm lên một tiếng dữ dội, khoảnh khắc tiếp theo, Kỷ Cảnh cảm thấy cánh tay mình truyền đến một cơn đau nhói buốt nhức.",
    # 106
    "Lục Tư Niên tung một cú quét chân đá văng tay phải của Lâm Diên Sơn,",
    # 107
    "Ống tiêm rỗng rơi cạch xuống mặt sàn, Lục Tư Niên tinh mắt nhìn thấy chiếc ống tiêm dưới đất, bước lên một bước tóm cổ áo xách Lâm Diên Sơn dậy.",
    # 108
    "“Mày tiêm cái gì cho cậu ấy?!” Trên gương mặt Lục Tư Niên hiếm hoi lắm mới xuất hiện vẻ hoảng loạn tột cùng.",
    # 109
    "“Tiêm cái gì à? Ha ha, yên tâm đi, chỉ là thuốc tăng mẫn cảm tin tức tố thôi mà, thật tiếc quá, vốn dĩ là chuẩn bị để tiêm cho mày đấy...”",
    # 110
    "Mặt Lâm Diên Sơn đầy máu me, cười cuồng loạn ngạo nghễ.",
    # 111
    "“Nhưng mà không sao hết... Nó là một Alpha, một khi phát tình lên thì người bị giày vò chỉ có một mình mày thôi, ha ha, Lục Tư Niên, mày cứ đợi đấy——”",
    # 112
    "Lời tác giả muốn nói:",
    # 113
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-22 22:13:17~2023-05-23 22:03:02 nha~",
    # 114
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: Thủy Mặc, Y 5 bình; Lam Lam Lam Lam 2 bình; 60031160, Sơn Khê Mộc Hề 1 bình;",
    # 115
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 109: Kỳ nhạy cảm bùng phát\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_109 translation successfully.")
