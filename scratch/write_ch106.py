# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_106\translation.md"

paras = [
    # 000
    "Omega quá dễ bị ảnh hưởng bởi tin tức tố của Alpha, dù chỉ là một chút thoang thoảng thôi cũng đủ khiến toàn thân Kỷ Vân Hy khó chịu không thôi.",
    # 001
    "Được Kỷ Cảnh ôm eo dìu đi một đoạn đường rất dài cô mới từ từ lấy lại được tinh thần.",
    # 002
    "“Omega thật sự không ngửi nổi một chút tin tức tố Alpha nào sao.” Kỷ Cảnh buông cô ra, bất thình lình cất tiếng hỏi.",
    # 003
    "“Tùy vào nồng độ nữa, khoảng cách giao tiếp bình thường thì không sao, nhưng nếu cố tình phóng thích tin tức tố như vừa nãy thì sẽ không chịu đựng nổi đâu.” Kỷ Vân Hy hít một hơi thật sâu không khí trong lành.",
    # 004
    "Vậy tại sao Lục Tư Niên lại không mấy chịu ảnh hưởng bởi tin tức tố của cậu, ngoại trừ lần đầu tiên ra?",
    # 005
    "Chẳng lẽ là vì loại thuốc ức chế đề kháng kia sao?",
    # 006
    "“Mày vẫn chưa tới kỳ nhạy cảm, tin tức tố chưa quá mức nhạy bén mãnh liệt, bằng không theo cái kiểu ôm vừa nãy của mày, Omega người ta đã sớm không chịu nổi rồi.”",
    # 007
    "Kỷ Vân Hy thở phào may mắn nói, cô cảm thấy Kỷ Cảnh vẫn chỉ là một cậu bé con chưa kịp lớn.",
    # 008
    "Bản thân cậu bé con này thì lại cảm thấy vô cùng xấu hổ ngượng ngùng.",
    # 009
    "Nếu để Lục Tư Niên biết bản thân mình đến tận bây giờ vẫn chưa từng trải qua kỳ nhạy cảm, liệu anh có cười nhạo cậu không nhỉ?",
    # 010
    "“Mày với Lục Tư Niên rốt cuộc có quan hệ gì thế, vừa nãy cái thằng ngu nhà họ Lục sao lại bảo mày đang thay anh ta báo thù?” Kỷ Vân Hy quay trở lại chủ đề chính.",
    # 011
    "Kỷ Cảnh chột dạ dời ánh mắt sang hướng khác: “Chẳng có quan hệ gì cả, tao chỉ đơn thuần nhìn Lục Đảo Phong ngứa mắt thôi.”",
    # 012
    "Kỷ Vân Hy lại mang ý tứ khó hiểu kéo dài giọng điệu: “Thế à......”",
    # 013
    "Lúc bọn họ bước vào đại sảnh chính, buổi yến tiệc đã bắt đầu được một khoảng thời gian.",
    # 014
    "Mẹ Kỷ đứng ở một góc vẫy vẫy tay với hai đứa con, ra hiệu cho hai đứa mau chóng bước qua đó.",
    # 015
    "Hai chị em Kỷ Cảnh chạy tới nơi, mới phát hiện con em thế hệ trẻ của mấy đại gia tộc cùng các quan chức cấp cao Đế quốc đều đang tụ tập ở đó.",
    # 016
    "Lục Đảo Phong sau khi nhìn thấy Kỷ Cảnh, còn sợ hãi thụt lùi trốn tịt vào trong đám đông.",
    # 017
    "“Mấy đứa nhỏ nhớ qua kính rượu Nguyên soái một ly nhé.”",
    # 018
    "Người Omega lên tiếng là Thẩm Lâm, bà ta nở nụ cười tươi tắn trên mặt, ngấm ngầm đẩy Lục Đảo Phong lên phía trước.",
    # 019
    "Thẩm Lâm trông có vẻ yếu đuối mỏng manh, nhưng Kỷ Cảnh lại có thể nhìn thấy sự độc địa nham hiểm trong đôi mắt của người phụ nữ này.",
    # 020
    "Lục Đảo Phong cắn răng bước tới, ấp úng ngập ngừng nói vài câu chúc tụng.",
    # 021
    "Trên mặt Nguyên soái chỉ treo nụ cười xã giao theo công thức, không đưa ra phản ứng gì quá nhiệt tình.",
    # 022
    "Đúng lúc này Kỷ Cảnh cũng cầm ly rượu bước lên, nụ cười trên mặt Nguyên soái lại sâu thêm vài phần.",
    # 023
    "“Ta nhớ hồi Tiểu Cảnh còn bé nghịch ngợm ghê lắm, còn thích giật tóc của ta nữa cơ.” Nguyên soái cười vô cùng hiền từ.",
    # 024
    "“Thằng bé hồi nhỏ chưa hiểu chuyện, để Nguyên soái chê cười rồi.” Mẹ Kỷ cười nói.",
    # 025
    "“Không sao, Alpha mà, nghịch ngợm một chút lúc nào cũng tốt, Tiểu Cảnh là một Alpha vô cùng xuất sắc.” Nguyên soái phản bác lại.",
    # 026
    "Ông lão đã qua nửa đời người vì bận rộn chinh chiến nơi sa trường nên không có con cái, lúc nào cũng thích tìm kiếm sự gửi gắm tình thân nơi những hậu bối xuất chúng.",
    # 027
    "Trong lúc hai người trò chuyện, không ai để ý thấy nụ cười trên gương mặt Thẩm Lâm đã cứng đờ đến cực điểm.",
    # 028
    "Đúng lúc này, Nguyên soái đột nhiên liếc mắt nhìn sang một chỗ, sau đó vẫy tay gọi lớn: “Lục Tư Niên, lại đây, qua bên này.”",
    # 029
    "Tiếng gọi vừa vang lên, tất cả mọi người có mặt tại hiện trường đều ngầm đưa mắt nhìn về phía Thẩm Lâm.",
    # 030
    "Những gì Lục Tư Niên phải trải qua ở nhà họ Lục, những người trong giới thượng lưu ít nhiều đều từng nghe phong phanh qua.",
    # 031
    "“Nguyên soái.” Lục Tư Niên cung kính cất tiếng chào.",
    # 032
    "Nguyên soái kéo Lục Tư Niên đứng sang bên cạnh mình, đối diện trực tiếp với Kỷ Cảnh.",
    # 033
    "Ông không biết mối duyên nợ giữa hai người, chỉ nghĩ muốn giới thiệu cho hai người làm quen với nhau: “Tư Niên là mầm non ưu tú ta phát hiện ra khi đi thị sát Đệ tam quân đoàn, còn Tiểu Cảnh là đứa trẻ ta nhìn từ nhỏ đến lớn, hai đứa làm quen kết giao với nhau một chút cũng tốt.”",
    # 034
    "Cả Lục Tư Niên và Kỷ Cảnh đều có chút gượng gạo, cuối cùng là Lục Tư Niên lên tiếng: “Nguyên soái, tôi và Kỷ Cảnh có quen biết nhau.”",
    # 035
    "“Quen biết nhau sao? Quen biết từ lúc nào thế.” Nguyên soái ngạc nhiên.",
    # 036
    "Ngay lúc này, Lục Đảo Phong bỗng xen ngang: “Trước khi vào Học viện Quân sự Đế quốc, bọn họ từng học chung một trường.”",
    # 037
    "Nguyên soái hơi có chút không hài lòng, nhưng vì tò mò nên vẫn để Lục Đảo Phong nói tiếp,",
    # 038
    "“Nguyên soái có lẽ chưa biết, khi đó Lục Tư Niên đã hại Kỷ Cảnh mắc phải chướng ngại tâm lý, tố chất thể lực sa sút không phanh đã đành, còn phải nghỉ học suốt hai năm trời.” Lục Đảo Phong sa sầm mặt mũi, căm phẫn nhìn chằm chằm Lục Tư Niên.",
    # 039
    "Lời này vừa thốt ra, bầu không khí lập tức tụt dốc xuống điểm đóng băng.",
    # 040
    "Kỷ Cảnh nhìn chăm chú không chớp mắt vào Lục Tư Niên, hồi lâu sau mới lên tiếng: “Không có đâu thưa Nguyên soái, giữa tôi và Lục Tư Niên không hề có mâu thuẫn gì cả.”",
    # 041
    "“Mày nói dối!” Lục Đảo Phong hét lớn, “Kỷ Cảnh, rõ ràng mày hận anh ta đến tận xương tủy, mày chắc chắn luôn tìm đủ mọi cách để trả thù anh ta, còn giả vờ thay anh ta báo thù làm cái gì...”",
    # 042
    "“Đủ rồi!” Nguyên soái quát lạnh một tiếng, uy áp quân đội khiến cả hội trường đều im bặt nín thở.",
    # 043
    "“Lục phu nhân về nhà nên quản giáo lại con cái của mình cho cẩn thận.”",
    # 044
    "Nguyên soái lạnh lùng nhìn Thẩm Lâm, không chút nể nang nói.",
    # 045
    "Sắc mặt Thẩm Lâm lúc đen lúc trắng, nói lời xin lỗi một tiếng rồi lôi Lục Đảo Phong rời đi.",
    # 046
    "Màn kính rượu kết thúc trong sự mất vui, Kỷ Cảnh bị mẹ Kỷ kéo đi chỗ khác, nhưng lại không nhìn thấy thần sắc bất thường của Lục Tư Niên.",
    # 047
    "Với tư cách là thái tử gia của nhà họ Kỷ, Kỷ Cảnh bị ba Kỷ kéo đi khắp nơi chúc rượu xã giao.",
    # 048
    "Nhà họ Kỷ trong việc lựa chọn người thừa kế vẫn giữ tư tưởng truyền thống, việc Kỷ Cảnh trở thành gia chủ đời tiếp theo của Kỷ gia là quy tắc thép không thể lay chuyển.",
    # 049
    "“Kỷ Cảnh quả thực là nhân tài kiệt xuất, Alpha ưu tú thế này đúng là chỉ có Kỷ gia chủ mới bồi dưỡng ra được.”",
    # 050
    "Những vị khách tới lui đều thi nhau khen ngợi chúc mừng.",
    # 051
    "“Không biết Kỷ Cảnh đã có Omega trong lòng chưa? Con gái nhà chúng tôi trạc tuổi cậu ấy, nếu có cơ hội...”",
    # 052
    "Người nọ chìa cành ô liu về phía Kỷ Trình.",
    # 053
    "Còn Kỷ Cảnh thì theo tiềm thức đưa mắt tìm kiếm trong đám đông, cuối cùng ở một góc yên tĩnh nhìn thấy bóng dáng cao lớn quen thuộc kia.",
    # 054
    "Tất cả mọi người có mặt đều đang mải mê giao lưu kết nối, duy chỉ có một mình Lục Tư Niên là lặng lẽ đứng ở góc rẽ cầu thang, tựa như cả thế giới này chỉ có một mình anh.",
    # 055
    "Cậu nhớ lại Lục Tư Niên hồi ở học viện cao cấp cũng như vậy, luôn đi sớm về muộn một mình, chưa từng nói chuyện dư thừa với bất kỳ ai.",
    # 056
    "Góc nhìn của Kỷ Cảnh hơi lệch một chút, cậu mơ hồ nhìn thấy trên tay Lục Tư Niên đang cầm một ly sâm panh, lọn tóc mái chưa được chải chuốt rủ xuống trước trán, trông có vẻ hơi tiều tụy chán chường.",
    # 057
    "Kỷ Trình bên cạnh nói: “Chuyện này vẫn phải xem ý tứ của Kỷ Cảnh đã, Kỷ Cảnh, con đang ngẩn người làm gì thế?”",
    # 058
    "Kỷ Cảnh hoàn hồn lại, sau đó xua xua tay, nói với Kỷ Trình rằng mình có việc phải rời đi một lát, rồi dán mắt vào hướng của Lục Tư Niên, luồn lách qua đám đông bước tới.",
    # 059
    "Bên kia Lục Tư Niên lại đứng thẳng người dậy, sải bước đi ra phía hoa viên bên ngoài.",
    # 060
    "Kỷ Cảnh lặng lẽ đi theo sau lưng anh, nhìn Lục Tư Niên bước tới một góc vắng vẻ, sau đó đứng tựa vào tường, cúi đầu, dùng đầu ngón tay xoa xoa sống mũi, như đang cố gắng giải rượu.",
    # 061
    "Gió đêm bên ngoài se se lạnh, tiếng người ồn ào trong buổi yến tiệc đều bị bỏ lại phía sau lưng.",
    # 062
    "Kỷ Cảnh lại nhìn thấy Lục Tư Niên mở thiết bị đầu cuối ra, gõ gõ thứ gì đó.",
    # 063
    "Ngay sau đó Kỷ Cảnh phát hiện thiết bị đầu cuối của mình sáng lên, trên đó hiện ra tin nhắn mới của Lục Tư Niên:",
    # 064
    "【Lục Tư Niên】: Hình như tôi say rồi.",
    # 065
    "Đầu óc Kỷ Cảnh ong ong một tiếng, ma xui quỷ khiến thế nào lại sải bước tiến lên phía trước, cất tiếng gọi: “Lục Tư Niên.”",
    # 066
    "Lục Tư Niên hẳn là thật sự say rồi, phản ứng vô cùng chậm chạp, đợi đến khi Kỷ Cảnh bước tới đứng trước mặt anh rồi mới ngơ ngác ngẩng đầu lên.",
    # 067
    "Nhờ ánh trăng sáng vằng vặc, Kỷ Cảnh nhìn rõ rặng mây đỏ bị men rượu hun lên trên gương mặt Lục Tư Niên.",
    # 068
    "Vệt đỏ ửng ấy lan tỏa từ tận vành tai xuống đến tận cổ, chìm sâu vào bên dưới chiếc cà vạt.",
    # 069
    "Ánh mắt Lục Tư Niên rất sâu thẳm, sắc môi lại rất nhạt, mùi rượu nồng đậm hòa lẫn với hương gỗ thông trên người anh, bao bọc lấy Kỷ Cảnh không chừa một kẽ hở.",
    # 070
    "Kỷ Cảnh buồn cười nhìn ánh mắt ngơ ngác đờ đẫn của Lục Tư Niên, nói: “Lục Tư Niên, anh say rồi à?”",
    # 071
    "Lục Tư Niên chậm chạp phản ứng lại, sau đó khẽ gật đầu.",
    # 072
    "“Chưa từng uống rượu.”",
    # 073
    "Kỷ Cảnh cũng không thấy lạ, Lục Tư Niên chưa từng đi xã giao, hơn nữa theo quan niệm đúng sai nghiêm ngặt của anh, cồn vốn thuộc về danh mục đồ cấm.",
    # 074
    "“Chưa từng uống mà cũng uống, uống bao nhiêu rồi?” Cậu bước lên một bước, đột nhiên chống một cánh tay bên tai Lục Tư Niên.",
    # 075
    "Khoảng cách nháy mắt bị kéo gần, mùi rượu trên người Lục Tư Niên càng thêm nồng nặc, hơi thở nóng bỏng theo từng lời anh nói phả thẳng vào chóp mũi Kỷ Cảnh,",
    # 076
    "Vẻ mặt Lục Tư Niên vô cùng nghiêm túc, như thể đang thực sự nghiêm túc hồi tưởng lại, cuối cùng anh nhắm mắt lại, lắc đầu:",
    # 077
    "“Đếm không xuể.”",
    # 078
    "Cổ họng bị men rượu hun đến khàn đặc.",
    # 079
    "Kỷ Cảnh phát hiện luồng hương gỗ thông trên người Lục Tư Niên đã trở nên nồng đậm hơn rất nhiều, ngửi đến mức khiến cậu có chút lâng lâng phiêu diêu, chân răng lại bắt đầu ngứa ngáy.",
    # 080
    "“Anh uống rượu làm cái gì.”",
    # 081
    "Câu hỏi này không nhận được câu trả lời từ Lục Tư Niên.",
    # 082
    "Kỷ Cảnh không cam lòng, cậu lại nhích lại gần thêm một chút, ghé sát vào tai Lục Tư Niên, nghiến nghiến răng, hạ giọng nói: “Này, anh có nhớ tôi từng nói, tôi muốn theo đuổi——”",
    # 083
    "“Sáu năm trước tôi đánh Kỷ Cảnh, là vì Kỷ Cảnh đã lăng mạ mẹ của tôi.”",
    # 084
    "Lục Tư Niên hẳn là đầu óc không còn tỉnh táo, căn bản không trả lời lời Kỷ Cảnh, ngược lại còn chẳng đầu chẳng đuôi lôi chuyện này ra nói.",
    # 085
    "Kỷ Cảnh nghe thấy chuyện này thoạt đầu lấy làm lạ vì đại từ nhân xưng Lục Tư Niên dùng, sau đó lại thấy mất hứng, buông anh ra, đứng thẳng người dậy.",
    # 086
    "“Thực ra tôi rất ngưỡng mộ Kỷ Cảnh,” Lục Tư Niên lại vô cớ nói thêm một câu, “Ngày đầu tiên chuyển trường, tôi nhìn thấy cậu ấy ở phòng đấu tập, đánh cho một Alpha sắp tốt nghiệp học viện cao cấp không còn chút sức lực chống cự nào,”",
    # 087
    "“Rõ ràng nhỏ tuổi như thế, nhưng thành tích môn nào cũng rất xuất sắc, có rất nhiều người yêu mến cậu ấy, vô ưu vô lo.”",
    # 088
    "Kỷ Cảnh lặng lẽ lắng nghe Lục Tư Niên khen ngợi mình, không hề ý thức được khóe môi mình đã nhếch lên thật cao.",
    # 089
    "Thật kỳ lạ, từ nhỏ đến lớn rõ ràng có biết bao nhiêu người từng khen ngợi cậu, nhưng những lời này thốt ra từ miệng Lục Tư Niên lại khiến cậu cảm thấy vô cùng thỏa mãn tự đắc.",
    # 090
    "“Thế nhưng,” giọng điệu Lục Tư Niên bỗng nhiên trầm hẳn xuống, “Cậu ấy lại trước mặt toàn trường, làm nhục mẹ của tôi.”",
    # 091
    "Khóe môi Kỷ Cảnh lập tức hạ sụp xuống.",
    # 092
    "“Tôi đã không khống chế được cảm xúc của mình, đợi đến khi Kỷ Cảnh được đưa vào bệnh viện rồi mới bình tĩnh lại.”",
    # 093
    "“Tôi không ngờ Kỷ Cảnh lại vì tôi mà mắc phải chướng ngại tâm lý, cuộc sống và tương lai đều bị ảnh hưởng, cho nên dù lần trước cậu ấy dùng tin tức tố khống chế tôi, tôi cũng không định truy cứu bất cứ điều gì nữa.”",
    # 094
    "Lục Tư Niên ngửa đầu ra sau, gáy tựa vào tường, chiếc cổ thon dài vì động tác này mà uốn thành một đường cong tuyệt đẹp, yết hầu với hình dáng hoàn mỹ khẽ lăn lên lộn xuống,",
    # 095
    "“Em có thể hận tôi, trả thù tôi,”",
    # 096
    "Anh bất thình lình lại đổi chủ ngữ, dùng ngôi thứ hai nói,",
    # 097
    "“Thế nhưng, xin em đừng lừa dối tôi.”",
    # 098
    "Tựa như một chiếc búa tạ từ trên trời giáng xuống, nện thẳng vào đầu Kỷ Cảnh khiến trước mắt cậu nổ đom đóm mắt.",
    # 099
    "Lời này của Lục Tư Niên có ý nghĩa gì chứ,",
    # 100
    "Lừa dối?",
    # 101
    "Anh đã biết được điều gì rồi sao?",
    # 102
    "Kỷ Cảnh trực tiếp túm lấy cà vạt của Lục Tư Niên kéo thẳng người anh dậy, trầm giọng nói: “Lừa dối cái gì, anh muốn nói cái gì hả.”",
    # 103
    "Thế nhưng Lục Tư Niên dường như đã hoàn toàn mất đi ý thức, cặp kính của anh vì động tác của Kỷ Cảnh mà rơi tuột xuống đất, để lộ ra đôi mắt đen vô thần bên dưới.",
    # 104
    "Lục Tư Niên ngã gục vào bờ vai Kỷ Cảnh, Kỷ Cảnh theo bản năng ôm chặt lấy anh.",
    # 105
    "Không biết đã trôi qua bao lâu, dòng suy nghĩ của Kỷ Cảnh cũng dần dần lắng dịu lại.",
    # 106
    "Kỷ Cảnh đỡ vững Lục Tư Niên, cúi người nhặt cặp kính của anh lên, định bụng kéo anh đi chỗ khác.",
    # 107
    "Nào ngờ Lục Tư Niên lại như xác chết đội mồ sống lại lẩm bẩm: “Từ năm giờ mười hai phút chiều thứ Sáu, em đã không trả lời tin nhắn của tôi nữa rồi, đây là lần thứ mười một kể từ sau khi chúng ta xác định mối quan hệ.”",
    # 108
    "“Tại sao không để ý đến tôi.”",
    # 109
    "Lục Tư Niên rầu rĩ hỏi.",
    # 110
    "Động tác của Kỷ Cảnh khựng lại, cậu suýt chút nữa tưởng tai mình bị ảo giác.",
    # 111
    "Ngay sau đó, một ý nghĩ hoang đường nảy sinh trong tâm trí cậu.",
    # 112
    "Cậu nhắm mắt lại, bật ra một tiếng cười lạnh lẽo.",
    # 113
    "Cậu túm lấy cổ áo sau của Lục Tư Niên lôi người anh dậy,",
    # 114
    "“Lục Tư Niên, nói cho tôi biết, tôi là ai.”",
    # 115
    "Lục Tư Niên bị ép phải nhìn cậu, hồi lâu sau, ánh mắt anh dao động chớp chớp, trả lời: “Dịch Nam.”",
    # 116
    "Dịch Nam.",
    # 117
    "Kỷ Cảnh lẩm nhẩm trong miệng, hóa ra từ đầu đến cuối vừa rồi, Lục Tư Niên đều coi cậu là Dịch Nam.",
    # 118
    "“Lục Tư Niên——”",
    # 119
    "Kỷ Cảnh bóp chặt cằm anh, ấn mạnh anh vào tường,",
    # 120
    "“Mẹ kiếp anh mở to mắt chó ra nhìn cho thật rõ ràng, tôi rốt cuộc là ai.”",
    # 121
    "Nói dứt lời, cậu đột ngột cúi người, nặng nề hôn siết lên đôi môi của Lục Tư Niên.",
    # 122
    "Lục Tư Niên vô cùng phối hợp, phối hợp đến mức thậm chí còn muốn dùng sức đè ngược Kỷ Cảnh lại.",
    # 123
    "Thế nhưng anh càng phối hợp thì trong lòng Kỷ Cảnh lại càng thêm nghẹn ứ bức bối.",
    # 124
    "Cậu giật mạnh đầu Lục Tư Niên ra, gầm nhẹ: “Anh mở mắt to ra nhìn cho rõ xem rốt cuộc là ai đang hôn anh!”",
    # 125
    "“Choang——”",
    # 126
    "Cách đó không xa truyền đến tiếng ly rượu rơi vỡ tan tành.",
    # 127
    "Kỷ Cảnh ngẩn người, nhìn theo hướng âm thanh phát ra.",
    # 128
    "Chỉ thấy Kỷ Vân Hy với gương mặt đờ đẫn sững sờ đứng chôn chân tại đó, cái miệng há hốc thành hình chữ O tròn xoe.",
    # 129
    "Lời tác giả muốn nói:",
    # 130
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-19 21:42:08~2023-05-20 23:12:09 nha~",
    # 131
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: Vũ, Cố Lai 1 bình;",
    # 132
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 106: Phòng nghỉ say rượu\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_106 translation successfully.")
