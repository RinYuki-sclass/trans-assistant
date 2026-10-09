# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_105\translation.md"

paras = [
    # 000
    "Kỷ Cảnh và Lục Tư Niên dường như đã bước vào giai đoạn yêu đương nồng nhiệt.",
    # 001
    "Cậu vẫn như trước đây mỗi tuần ba ngày đến dự tiết của Lục Tư Niên, rồi cùng anh ăn cơm, cuối cùng tìm một cái cớ rời đi để quay trở lại làm Kỷ Cảnh đi học những tiết học mà cậu vốn nên học.",
    # 002
    "Cậu hệt như nàng Lọ Lem Cinderella trong truyện cổ tích, mỗi tuần chỉ có vài khoảng thời gian ngắn ngủi được dùng thân phận Dịch Nam ở bên cạnh Lục Tư Niên.",
    # 003
    "Điểm khác biệt là, Lục Tư Niên của hiện tại trong giờ học sẽ theo bản năng nhìn chăm chú vào cậu, trên đường đi sẽ để mặc cho cậu nắm tay anh, thậm chí còn đưa cậu về văn phòng của anh để hôn cậu.",
    # 004
    "Có đôi khi anh còn chủ động gửi tin nhắn cho cậu, mặc dù những dòng chữ gửi sang vô cùng cứng nhắc và khô khan.",
    # 005
    "Thế nhưng Kỷ Cảnh lại chẳng hề cảm thấy tự nhiên và ung dung tự tại như cậu từng dự liệu.",
    # 006
    "Mỗi lần nhìn thấy gương mặt cứng đờ lạnh như băng kia của Lục Tư Niên vì “chính mình” mà xuất hiện những cảm xúc dịu dàng mềm mỏng, sự bực bội phiền muộn trong lòng Kỷ Cảnh lại tăng thêm một phần.",
    # 007
    "Cậu đầy ác ý nghĩ thầm, Lục Tư Niên cớ sao lại dễ công lược đến thế, nhanh như vậy đã yêu cái thân phận giả này của cậu rồi, bộ thiếu thốn tình yêu đến mức đó sao.",
    # 008
    "Nào ngờ ban đầu chính cậu là người chê bai Lục Tư Niên khó theo đuổi, tựa như một tảng đá vô cảm không có chút cảm xúc nào.",
    # 009
    "Thế là cậu bắt đầu vô thức né tránh Lục Tư Niên, tin nhắn cũng ít gửi hơn hẳn, lúc ở bên Lục Tư Niên chốc chốc lại thất thần lơ đãng.",
    # 010
    "Cậu sẽ dùng thân phận Dịch Nam cố ý để lộ ra một vài bản tính xấu xa tồi tệ của mình, muốn xem xem Lục Tư Niên sẽ phản ứng ra sao, thế nhưng Lục Tư Niên từ đầu đến cuối đều ngơ ngác đờ đẫn đến phát bực, như thể chẳng nhận ra chút điểm nào không đúng.",
    # 011
    "Thứ Sáu Kỷ Cảnh tan học về nhà, nằm vật ra giường trừng mắt nhìn trần nhà, ngay sau đó liền rút thiết bị đầu cuối ra.",
    # 012
    "Tin nhắn cuối cùng trong khung chat là do Lục Tư Niên gửi tới vào buổi sáng, anh bảo anh đã tan tiết rồi.",
    # 013
    "Nhưng Kỷ Cảnh không trả lời, cũng không có ý định trả lời, trực tiếp nhắn thẳng:",
    # 014
    "【Dịch Nam Nam Nam】: Lục Tư Niên, anh cảm thấy em và Kỷ Cảnh có giống nhau không.",
    # 015
    "Lục Tư Niên trả lời rất nhanh chóng:",
    # 016
    "【Lục Tư Niên】: Giống.",
    # 017
    "【Dịch Nam Nam Nam】: Giống đến mức nào?",
    # 018
    "【Lục Tư Niên】: Lần đầu tiên nhìn thấy em, tôi đã ngỡ là cậu ấy.",
    # 019
    "Kỷ Cảnh bực bội “chậc” một tiếng, bật dậy khỏi giường:",
    # 020
    "【Dịch Nam Nam Nam】: Anh thích em đúng không?",
    # 021
    "【Dịch Nam Nam Nam】: [Mèo con liếm lông.jpg]",
    # 022
    "【Lục Tư Niên】: Ừ.",
    # 023
    "Sau khi nhận được câu trả lời khẳng định, chân mày Kỷ Cảnh hơi giãn ra một chút, liền ướm hỏi:",
    # 024
    "【Dịch Nam Nam Nam】: Vậy Kỷ Cảnh trông giống em như thế, có phải anh cũng sẽ thích cậu ta không?",
    # 025
    "Lần này tốc độ trả lời của Lục Tư Niên rõ ràng chậm hơn rất nhiều, như thể đang do dự cân nhắc kỹ lưỡng:",
    # 026
    "【Lục Tư Niên】: Tôi thích em.",
    # 027
    "Nhìn dòng tin nhắn Lục Tư Niên gửi tới, ngọn lửa giận trong lòng Kỷ Cảnh bốc lên ngùn ngụt, cậu mạnh tay gập thiết bị đầu cuối lại.",
    # 028
    "Ý gì đây chứ? Ý là anh ta không thích Kỷ Cảnh mà chỉ thích mỗi Dịch Nam thôi chứ gì.",
    # 029
    "Ai thèm quan tâm anh ta có thích Kỷ Cảnh hay không chứ? Đợi cậu dùng thân phận Dịch Nam hoàn thành xong nhiệm vụ là sẽ hoàn toàn biến mất không dấu vết.",
    # 030
    "Nói thì nói như vậy, nhưng Kỷ Cảnh từ sau tin nhắn đó liền không thèm đếm xỉa đến Lục Tư Niên nữa, nghe thấy mẹ Kỷ ở dưới lầu gọi tên mình, cậu xỏ dép lê bước xuống lầu ăn cơm.",
    # 031
    "Trên bàn ăn, ba Kỷ vừa lướt xem thiết bị đầu cuối vừa thông báo: “Chủ nhật tuần này cả nhà chúng ta phải tham dự tiệc mừng thọ năm mươi tuổi của Nguyên soái, cả nhà đều phải đi đông đủ, sắp xếp thời gian cho cẩn thận.”",
    # 032
    "“Sinh nhật của Nguyên soái sao?”",
    # 033
    "Kỷ Vân Hy khẽ thốt lên kinh ngạc.",
    # 034
    "“Vậy chẳng phải ngài ấy chỉ còn mười năm nữa là sẽ chính thức thoái vị nghỉ hưu rồi à.”",
    # 035
    "Các đời Nguyên soái của Đế quốc đều chính thức thoái vị ở tuổi sáu mươi tròn, Kỷ Cảnh nhớ lại cốt truyện mà hệ thống đưa cho cậu, Lục Tư Niên chính là người tiếp quản vị trí của vị Nguyên soái đương nhiệm này.",
    # 036
    "Nhà họ Kỷ qua lại rất thân thiết với Nguyên soái, Kỷ Vân Hy và Kỷ Cảnh hồi nhỏ cũng thường xuyên được Nguyên soái bế ẵm chơi đùa.",
    # 037
    "Khác với những buổi yến tiệc thông thường khác, tiệc sinh nhật của Nguyên soái Đế quốc tất cả các thế gia môn phiệt đều bắt buộc phải nể mặt mà đối đãi long trọng.",
    # 038
    "Kỷ Cảnh gắp một miếng cơm, làm bộ như vô tình hỏi han: “Vậy tất cả người nhà họ Lục đều sẽ đến ạ?”",
    # 039
    "Kể từ sau vụ việc của Kỷ Cảnh, nhà họ Lục đã trở thành chủ đề cấm kỵ mà cả nhà đều chủ động tránh né nhắc tới.",
    # 040
    "Mẹ Kỷ ngẩn người một thoáng, liếc nhìn Kỷ Cảnh: “Chắc chắn là phải đến rồi, còn về phần Lục Tư Niên, dù không tham dự với tư cách con cháu nhà họ Lục thì cũng sẽ được mời với tư cách cựu Tổng chỉ huy.”",
    # 041
    "Nói xong, bà lại có ý thăm dò dò hỏi:",
    # 042
    "“Tiểu Cảnh à, nghe nói cậu ấy hiện đang làm giáo sư ở Học viện Quân sự Đế quốc? Con đã gặp cậu ấy chưa, đứa trẻ đó mẹ cũng từng gặp rồi, là một đứa trẻ rất tốt, có một số ân oán thì...”",
    # 043
    "“Mẹ, con no rồi.”",
    # 044
    "Kỷ Cảnh đoán được mẹ Kỷ định nói gì, vội vàng buông đũa chạy biến.",
    # 045
    "Cậu sợ nếu còn nói tiếp thì bản thân sẽ lộ tẩy mất, cậu biết phải nói thế nào với mẹ mình rằng cậu không những đã gặp anh ta, mà còn đang yêu đương với anh ta cơ chứ.",
    # 046
    "Sau đó Lục Tư Niên lại gửi cho cậu vài tin nhắn, Kỷ Cảnh trước sau đều không thèm trả lời, về sau Lục Tư Niên dù có chậm chạp đến đâu cũng nhận ra điểm bất thường của Kỷ Cảnh, gửi một câu “Dịch Nam, em sao thế?” rồi không nói thêm gì nữa.",
    # 047
    "Sáng sớm Chủ nhật, cả gia đình bốn người nhà họ Kỷ ngồi lên chiếc phi thuyền hướng về trang viên của Nguyên soái.",
    # 048
    "Đại thọ năm mươi tuổi của Nguyên soái nhận được sự chú ý của toàn thể Đế quốc, xe còn chưa tiến vào cổng lớn của trang viên đã bị giới truyền thông báo chí chen chúc bao vây chật như nêm cối.",
    # 049
    "Theo quy củ, tứ đại gia tộc sẽ đến địa điểm tổ chức tiệc sớm hơn nửa tiếng đồng hồ, vì vậy khi gia đình Kỷ Cảnh xuống xe, trong trang viên vẫn chưa có mấy người.",
    # 050
    "Kỷ Cảnh và Kỷ Vân Hy đi sau lưng ba mẹ Kỷ bước vào trong trang viên, dọc đường đi nhận được vô số ánh mắt quan sát dò xét.",
    # 051
    "Nguyên soái là một Alpha cao lớn vạm vỡ, hai bên thái dương đã điểm vài sợi tóc hoa râm, sau khi hàn huyên thăm hỏi vài câu với Kỷ Trình liền chuyển ánh mắt sang hai chị em Kỷ Cảnh.",
    # 052
    "“Đã nhiều năm không gặp, Tiểu Hy và Tiểu Cảnh đều đã lớn thế này rồi.”",
    # 053
    "Nguyên soái cười hiền từ, trong mắt hiện lên sự cảm thán trước sự trôi đi của năm tháng.",
    # 054
    "“Sức khỏe Tiểu Cảnh đã khá hơn chưa? Đoạn video thi đấu lần trước ta cũng có xem qua rồi, xem chừng đã hồi phục rất tốt.” Ông vỗ vỗ vai Kỷ Cảnh, “Thế hệ của các cháu ta chỉ coi trọng hai người, một là Tiểu Cảnh, người kia là cựu Tổng chỉ huy của Quân đoàn Ba Lục Tư Niên.”",
    # 055
    "Kỷ Trình đột nhiên lên tiếng: “Nguyên soái, Lục Tư Niên đã giải ngũ rồi, Tổng chỉ huy hiện tại là Lâm Diên Sơn.”",
    # 056
    "“Giải ngũ rồi sao?” Biểu cảm của Nguyên soái trông có vẻ rất đỗi ngạc nhiên, dường như hoàn toàn chưa hay biết gì: “Hồ đồ quá, đang yên đang lành tự dưng giải ngũ làm gì chứ, thế chẳng phải uổng phí tài năng sao.”",
    # 057
    "...",
    # 058
    "Bên kia ba Kỷ mẹ Kỷ đã đi xa, Kỷ Cảnh và Kỷ Vân Hy bắt đầu tản bộ vu vơ không mục đích trong trang viên, rất nhanh sau đó bọn họ lần lượt nhìn thấy xe của mấy gia tộc lớn khác lái vào.",
    # 059
    "Khoảng chừng vài chục phút sau, cánh cổng trang viên được người hầu mở toang, giới truyền thông vây kín bên ngoài lũ lượt ùa vào như đàn ong vỡ tổ.",
    # 060
    "Kỷ Cảnh liếc nhìn thời gian, lại nhìn những chiếc xe liên tiếp chạy vào trang viên, tựa như đang ngóng chờ ai đó đến.",
    # 061
    "Kỷ Cảnh và Kỷ Vân Hy quá đỗi nổi bật, hai gương mặt mang lại sức công kích thị giác cực đại đứng cạnh nhau, lập tức thu hút ánh nhìn của vô số ống kính truyền thông.",
    # 062
    "“Kỷ thái tử, xin hỏi vì sao trong trận đấu cận chiến ngài lại dùng bạo lực tàn nhẫn đối với thái tử nhà họ Lục như vậy, giữa hai người có thù oán gì sâu đậm chăng?”",
    # 063
    "“Kỷ thái tử, xin hỏi trước đây vì sao ngài lại phải tạm nghỉ học hai năm vì lý do sức khỏe, có phải ngài mắc chứng bệnh gì không, hiện tại đã bình phục hẳn chưa?”",
    # 064
    "“Nghe nói ngài từng là Alpha thiên tài xuất chúng nhất của thế hệ này, nhưng sau đó lại bị Beta Lục Tư Niên vượt mặt áp đảo hoàn toàn, xin hỏi ngài có cách nhìn nhận thế nào về Lục Tư Niên?”",
    # 065
    "...",
    # 066
    "Đối diện với những câu hỏi dồn dập hùng hổ ép người của giới truyền thông, Kỷ Cảnh kéo tay Kỷ Vân Hy với bộ mặt đen như đít nồi chuồn mất.",
    # 067
    "May mắn là đám phóng viên kia đã tìm thấy mục tiêu mới nên không đuổi theo truy hỏi nữa.",
    # 068
    "“Nhìn kìa, đó là phi thuyền của Quân đoàn Ba!”",
    # 069
    "“Khoan đã, đó là Lục Tư Niên phải không? Tại sao anh ta lại cùng đến dự tiệc với Đoàn trưởng của Quân đoàn Ba chứ, chẳng phải anh ta đã giải ngũ rồi sao?”",
    # 070
    "...",
    # 071
    "Kỷ Cảnh nghe vậy dừng bước chân lại, quay đầu nhìn sang phía cách đó không xa.",
    # 072
    "Lục Tư Niên đang đứng bên cạnh Trương Mạc, mặc một bộ âu phục đơn giản, dưới mắt mang theo chút mệt mỏi, đối diện với những lời truy hỏi của truyền thông vẫn một mực im lặng không hé răng.",
    # 073
    "Dường như nhận thấy tầm mắt của Kỷ Cảnh, anh khẽ nâng mí mắt, nhìn về phía Kỷ Cảnh.",
    # 074
    "Kỷ Cảnh thoắt cái thu hồi ánh mắt, kéo Kỷ Vân Hy cất bước rời đi.",
    # 075
    "“Em trai à, không ngờ mày nổi tiếng đến thế đấy.” Kỷ Vân Hy vừa đi vừa cố ý trêu chọc cậu,",
    # 076
    "“Lục Tư Niên người thật nhìn còn đẹp trai hơn trong ảnh nhiều, mày bảo xem một Beta như anh ta sao lại có thể cao đến thế chứ, gần như cao ngang ngửa mày rồi, hèn chi lại được lòng các Omega đến vậy.”",
    # 077
    "Kỷ Vân Hy có chút mê trai nổi lên.",
    # 078
    "“Thế tao với anh ta ai đẹp trai hơn?” Kỷ Cảnh bất mãn hỏi vặn lại.",
    # 079
    "Kỷ Vân Hy thực sự nghiêm túc suy nghĩ một hồi: “Ừm... nếu mặc âu phục thì anh ta đẹp trai hơn, còn nếu mặc áo khoác da thì mày đẹp trai hơn, tóm lại hai người bọn mày không phải cùng một kiểu đẹp trai...”",
    # 080
    "Hai người vừa đi dạo trong hoa viên vừa trò chuyện, đi chưa được mấy bước liền đụng mặt trực diện với Lục Đảo Phong đang đi lang thang.",
    # 081
    "Chân Lục Đảo Phong vẫn còn khập khiễng, đi đứng trông vô cùng buồn cười tức cười, đặc biệt là khoảnh khắc hắn ta nhìn thấy Kỷ Cảnh, đồng tử hoảng sợ co rút lại kịch liệt, đôi chân thọt lảo đảo lùi lại phía sau mấy bước liền.",
    # 082
    "“Mẹ kiếp, lại là cái thằng điên mày...!”",
    # 083
    "Bên cạnh Lục Đảo Phong còn có vài người con em dòng thứ bám theo, toàn bộ đều là Alpha, thấy vậy liền đồng loạt nhìn về phía Kỷ Cảnh.",
    # 084
    "Đoạn video Kỷ Cảnh đập nhừ tử Lục Đảo Phong đã được bọn họ chuyền tay nhau xem khắp nội bộ, người ngoài nhìn vào không hiểu mấy câu Kỷ Cảnh nói với Lục Đảo Phong mang ý nghĩa gì, nhưng bọn họ thì trong lòng hiểu rõ như lòng bàn tay.",
    # 085
    "Kỷ Cảnh là đang tới báo thù giúp Lục Tư Niên.",
    # 086
    "Một đám Alpha cắn răng tiến lên chắn trước mặt Lục Đảo Phong, hướng về phía Kỷ Cảnh phóng thích tin tức tố Alpha để áp chế.",
    # 087
    "Bên cạnh Kỷ Cảnh còn có Kỷ Vân Hy, Omega không chịu nổi mùi vị này, chân bắt đầu hơi run rẩy bủn rủn.",
    # 088
    "Kỷ Cảnh một tay ôm lấy eo Kỷ Vân Hy, nheo mắt đe dọa: “Các người muốn tìm cái chết à?”",
    # 089
    "Sắc mặt đám Alpha trắng bệch, lập tức thu hồi tin tức tố lại.",
    # 090
    "“Kỷ Cảnh, lần trước mày dùng thủ đoạn bẩn thỉu hèn hạ hại ông đây mất hết thể diện trước toàn thể Đế quốc, ông đây chết cũng không tha cho mày đâu!”",
    # 091
    "Lục Đảo Phong đứng giữa đám Alpha, khàn giọng gào thét.",
    # 092
    "“Lục Đảo Phong, lo lắng cho chính bản thân mày trước đi đã.”",
    # 093
    "Kỷ Cảnh đột nhiên bật cười, nụ cười vô cùng xấu xa, hàn ý lạnh lẽo từ độ cong khóe môi cậu tràn ra ngoài, cậu ngước mắt lần lượt quét qua từng tên Alpha trước mặt, nói:",
    # 094
    "“Có những chuyện các người đã quên, nhưng tao thì chưa quên đâu.”",
    # 095
    "Đám Alpha trong lòng dâng lên một cơn ớn lạnh rợn tóc gáy,",
    # 096
    "“Lục Đảo Phong, hẹn gặp lại ở giải cận chiến lần sau nhé,” Kỷ Cảnh liếc nhìn thời khóa biểu, “Còn lần này thì, ném mày vào thùng rác ngủ một đêm thấy thế nào?”",
    # 097
    "Cả người Lục Đảo Phong bắt đầu run rẩy với tốc độ mắt thường có thể nhìn thấy, hắn không thể tin nổi nói: “Kỷ Cảnh, mày quả nhiên là đang giúp anh ta báo thù đúng không... Tại sao, chẳng phải mày từng bị anh ta đánh cho mắc chướng ngại tâm lý sao, mày đáng ra phải hận anh ta đến tận xương tủy chứ, mày với anh ta rốt cuộc có quan hệ gì...”",
    # 098
    "Anh ta là ai?",
    # 099
    "Lục Tư Niên sao?",
    # 100
    "Đầu óc vốn đang mơ màng của Kỷ Vân Hy đột nhiên trở nên sáng rõ thông suốt, cô trố mắt nhìn chằm chằm Kỷ Cảnh, hai mắt trợn tròn xoe.",
    # 101
    "Sự kiên nhẫn của Kỷ Cảnh đã cạn kiệt, cậu liếc mắt nhìn Lục Đảo Phong lần cuối, để lại một câu “Liệu hồn mà đợi đấy” rồi đỡ Kỷ Vân Hy cất bước rời đi.",
    # 102
    "...",
    # 103
    "“Tư Niên, cậu đứng đực mặt ra đây làm cái gì thế?”",
    # 104
    "Trương Mạc đi ngang qua hoa viên, nhìn thấy Lục Tư Niên quay lưng về phía mình đứng bên một gốc cây không nói một lời, cũng chẳng rõ đã đứng ở đó bao lâu rồi.",
    # 105
    "Ông nhìn về phía trước, vừa vặn trông thấy đám người Lục Đảo Phong đang hùng hổ chửi rủa, cùng bóng lưng rời đi của Kỷ Cảnh và Kỷ Vân Hy.",
    # 106
    "“Vừa rồi bọn họ làm gì thế?” Trương Mạc tò mò hỏi.",
    # 107
    "Thế nhưng Lục Tư Niên mãi vẫn không đáp lại.",
    # 108
    "Ông nghiêng đầu nhìn anh, mới phát hiện ánh mắt Lục Tư Niên đang dán chặt vào bóng lưng của Kỷ Cảnh.",
    # 109
    "“Nghe người trong quân đoàn đồn cậu có bạn gái rồi hả...” Trương Mạc đột nhiên nhớ tới bức ảnh được lan truyền rộng rãi trong nhóm chat, “Ủa này, cậu có thấy gương mặt cô bé đó trông rất giống thằng nhóc nhà họ Kỷ kia không...”",
    # 110
    "“Ngài tìm tôi có chuyện gì thế ạ.” Lục Tư Niên cắt ngang lời ông.",
    # 111
    "Trương Mạc không hiểu ra sao, nhưng ông sực nhớ lại lý do mình đến tìm Lục Tư Niên:",
    # 112
    "“Không có gì bất ngờ thì tôi sắp được điều chuyển công tác rồi, gần đây tranh cãi về quyền bình đẳng của Omega đang diễn ra rất gay gắt, không có gì bất ngờ thì dự luật khôi phục quyền tòng quân của Omega bên phía Đế quốc sẽ được đưa ra bỏ phiếu trong tháng này...”",
    # 113
    "Trương Mạc thở dài một tiếng, vỗ vỗ vai Lục Tư Niên: “Chỉ cần số phiếu quá bán, cậu liền có thể quay trở lại rồi.”",
    # 114
    "Lời tác giả muốn nói:",
    # 115
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-18 21:10:30~2023-05-19 21:42:08 nha~",
    # 116
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: 60031160 5 bình; Tích Chút May Mắn 2 bình; Triều Ca 1 bình;",
    # 117
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 105: Bữa tiệc nguyên soái và ghen tuông\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_105 translation successfully.")
