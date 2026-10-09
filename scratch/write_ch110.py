# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_110\translation.md"

paras = [
    # 000
    "Lời Lâm Diên Sơn vừa dứt, một luồng tin tức tố Alpha mùi rượu Tequila nồng đậm liền theo xu thế bùng nổ hung hãn cuồn cuộn tràn tới từng ngóc ngách.",
    # 001
    "Lục Tư Niên từng tiêm thuốc kháng chế, vốn dĩ sẽ không bị tin tức tố của Alpha bình thường ảnh hưởng quá nhiều, vậy mà lúc này lại bị mùi vị tràn đầy tính xâm lược này hun đến mức hoa mắt chóng mặt.",
    # 002
    "Quá mức nồng nặc dữ dội.",
    # 003
    "Cơ bắp toàn thân bắt đầu mỏi nhừ mềm nhũn, những giọt mồ hôi li ti từ nơi chân mày Lục Tư Niên trượt dài rơi xuống.",
    # 004
    "“Kỷ Cảnh——” Anh đè thấp cổ họng gọi lớn.",
    # 005
    "Kỷ Cảnh đứng nguyên tại chỗ, cúi gằm đầu bất động không nhúc nhích, nhưng từ góc độ của Lục Tư Niên nhìn qua, lại có thể nhìn thấy vệt đỏ ửng dị thường lan tỏa từ chóp tai xuống đến tận cổ của Kỷ Cảnh.",
    # 006
    "Nghe thấy tiếng gọi của Lục Tư Niên, Kỷ Cảnh từ từ ngẩng đầu lên.",
    # 007
    "“Lục Tư Niên, phải làm sao bây giờ, em khó chịu quá...”",
    # 008
    "Giọng nói của Kỷ Cảnh khàn đặc đến đáng sợ, khoảnh khắc chạm vào đôi mắt cậu, một luồng tin tức tố càng thêm mãnh liệt tựa như dã thú gầm thét lao thẳng về phía Lục Tư Niên.",
    # 009
    "Lục Tư Niên nhìn thấy một đôi mắt đỏ rực đến mức hóa đen, đôi mắt ấy đang nhìn chằm chằm vào anh không chớp, hệt như một con sư tử cuồng nộ đang đói khát vừa phát hiện ra nguồn thức ăn duy nhất của nó suốt cả tháng trời.",
    # 010
    "Thế nhưng cậu vẫn đứng chôn chân tại chỗ, tầm mắt lượn lờ trên người Lục Tư Niên, tựa như có một sợi dây vô hình đang trói buộc chút lý trí cuối cùng còn sót lại của cậu.",
    # 011
    "“Rầm——”",
    # 012
    "Một tiếng động vang dội vang lên bên cạnh, đầu gối Lâm Diên Sơn đập mạnh xuống mặt sàn, cả người run rẩy một cách bất thường, cơ bắp toàn thân căng cứng, đôi mắt nhìn Kỷ Cảnh cũng đỏ ngầu một mảng.",
    # 013
    "“Mẹ kiếp... không đúng, sao lại có thể nồng nặc đến mức này...”",
    # 014
    "Lâm Diên Sơn bất an nuốt nước bọt ừng ực, tin tức tố của Alpha đối với đồng giới là tín hiệu khiêu khích giao tranh bạo lực, mà nồng độ tin tức tố Alpha vượt xa mức bình thường này lại khiến bản năng gen thôi thúc Lâm Diên Sơn phải lập tức rút lui, bằng không sẽ bị coi là kẻ cạnh tranh giành giật bạn đời.",
    # 015
    "Ánh mắt Kỷ Cảnh đã từ từ dời sang người Lâm Diên Sơn, Lâm Diên Sơn nhìn thấy tín hiệu thị uy cảnh cáo trong đồng tử đang co rút lại của cậu.",
    # 016
    "Một ý nghĩ hoang đường nảy ra trong trạng thái thần kinh căng thẳng tột độ, Lâm Diên Sơn gần như buột miệng gào lên: “Mày đừng bảo là mày còn chưa từng trải qua kỳ nhạy cảm đấy nhé!——”",
    # 017
    "Nỗi sợ hãi trước nguy cơ ập đến bủa vây cõi lòng Lâm Diên Sơn, hắn theo bản năng lùi về phía sau, còn chưa đợi hắn kịp hành động, tiếng xé gió cực mạnh đã xé rách màng nhĩ hắn, hắn bị túm cổ áo nhấc bổng lên ném thẳng vào góc bàn, ngũ tạng lục phủ như bị chấn động đến mức lệch vị trí.",
    # 018
    "Từng đòn tấn công chí mạng tới tấp giáng xuống người Lâm Diên Sơn, hắn bất lực nhìn Lục Tư Niên đang trượt ngồi dưới đất cách đó không xa, tiếng kêu cứu bị nhấn chìm hoàn toàn trong tiếng gầm gừ mất khống chế của Kỷ Cảnh.",
    # 019
    "Dục vọng tàn bạo bạo ngược khắc sâu trong gen của Alpha vào khoảnh khắc này được giải phóng đến tột cùng, Kỷ Cảnh bị sự hưng phấn che mờ hai mắt, nhưng đúng lúc này lại ngửi thấy một sợi tin tức tố Omega mỏng manh yếu ớt.",
    # 020
    "Khoảnh khắc tiếp theo, nắm đấm của cậu bị một lòng bàn tay bao bọc lấy.",
    # 021
    "“Kỷ Cảnh, bình tĩnh lại, cậu sắp đánh chết hắn rồi.”",
    # 022
    "Lục Tư Niên cả người đầy mồ hôi chắn trước mặt Lâm Diên Sơn, bàn tay đang nắm chặt nắm đấm của Kỷ Cảnh không ngừng run rẩy mất kiểm soát.",
    # 023
    "“Lục Tư Niên, mau giải phóng tin tức tố của mày ra, bằng không mày không khống chế nổi nó đâu!”",
    # 024
    "Lâm Diên Sơn ở sau lưng anh gào thét.",
    # 025
    "Ngay sau đó, hương gỗ thông cuồn cuộn không dứt hòa vào trong luồng tin tức tố mùi rượu Tequila nồng nặc.",
    # 026
    "Lục Tư Niên cảm nhận được bàn tay của Kỷ Cảnh đang từ từ thả lỏng sức lực.",
    # 027
    "“Lục Tư Niên...” Sát khí nơi đáy mắt Kỷ Cảnh dần dần tan rã, ngơ ngác nhìn anh.",
    # 028
    "Lục Tư Niên dùng sức kéo Kỷ Cảnh vào lòng, ôm chặt lấy eo cậu.",
    # 029
    "“Bình tĩnh lại đi, Kỷ Cảnh.”",
    # 030
    "Rõ ràng bàn tay của chính mình vẫn còn đang run rẩy, nhưng lại từng cái từng cái trầm ổn vỗ về lên lưng Kỷ Cảnh.",
    # 031
    "“Ha ha, Lục Tư Niên mày đúng là đồ ngu xuẩn, lần này mày sẽ bị nó chơi chết cho xem, hy vọng mấy ngày nữa tao có thể đọc được tin tức mày bị thái tử nhà họ Kỷ chơi chết——”",
    # 032
    "Lâm Diên Sơn chẳng biết từ lúc nào đã bò trốn ra ngoài cửa, hắn nhổ một búng máu về phía Lục Tư Niên: “Nếu mày chạy trốn thì thằng nhóc này sẽ hoàn toàn biến thành phế nhân đấy ha ha ha!”",
    # 033
    "Cánh cửa lớn bị Lâm Diên Sơn đóng sập lại thật mạnh, tất cả mọi mùi hương đều bị cánh cửa đóng chặt và cửa sổ phong tỏa gắt gao bên trong phòng.",
    # 034
    "Cằm của Kỷ Cảnh tì mạnh lên bờ vai Lục Tư Niên, động tác này vô cùng nguy hiểm, chỉ cần lại gần thêm một chút nữa thôi, chóp mũi của cậu liền có thể chạm vào tuyến thể ẩn mật nơi sau gáy của Lục Tư Niên.",
    # 035
    "Tương tự như vậy, tư thế ôm ấp này khiến Lục Tư Niên bị tin tức tố Alpha kín không kẽ hở bao bọc lấy, không chốn dung thân, nồng nặc đến mức khiến anh gần như nghẹt thở ngạt thở, sắp sửa chết chìm bên trong, lồng ngực phập phồng dữ dội kịch liệt.",
    # 036
    "“Lục Tư Niên, em khó chịu quá.”",
    # 037
    "Kỷ Cảnh thở dốc thô ráp, chóp mũi không tự chủ được mà cọ xát trên làn da sau gáy Lục Tư Niên, hơi thở nóng rực cùng sự ma sát da thịt khiến toàn thân Lục Tư Niên run rẩy kịch liệt.",
    # 038
    "Sự dung hợp thu hút trong gen của Alpha và Omega khiến cả hai người đều không cách nào thoát khỏi bản năng.",
    # 039
    "“Kỷ Cảnh, ngoan một chút, tôi đang nghĩ cách đây.”",
    # 040
    "Lục Tư Niên dùng cánh tay ôm chặt cứng lấy eo Kỷ Cảnh, gắng gượng giữ vững giọng nói đang run rẩy dỗ dành, sau đó hít sâu một hơi, chật vật mở thiết bị đầu cuối, tìm số điện thoại của Nguyễn Uyên.",
    # 041
    "Thế nhưng Kỷ Cảnh lúc này đã hoàn toàn không nghe lọt tai bất kỳ lời nào Lục Tư Niên nói nữa, sự thôi thúc chưa từng có trong đời khiến cậu bất giác phá tan phòng tuyến cuối cùng.",
    # 042
    "Cảm giác nóng ẩm ướt át từ tuyến thể nhạy cảm nhất sau gáy Lục Tư Niên truyền thẳng vào dây thần kinh của anh, đồng tử Lục Tư Niên co rút dữ dội,",
    # 043
    "“Lục Tư Niên, em chỉ cọ cọ một chút thôi... khó chịu quá...”",
    # 044
    "“A lô? Lục Tư Niên?” Giọng nói ngạc nhiên ở đầu dây bên kia thiết bị đầu cuối át đi lời thỉnh cầu của Kỷ Cảnh.",
    # 045
    "Cánh tay Lục Tư Niên càng thêm dùng sức, anh giữ chặt gáy Kỷ Cảnh cố gắng giữ vững cậu: “Đừng cắn...” Giọng anh khàn đặc nói.",
    # 046
    "“Cắn cái gì mà cắn...” Nguyễn Uyên kỳ quặc hỏi.",
    # 047
    "Thiết bị đầu cuối kết nối với dây thần kinh cá nhân, ngoại trừ chính người nghe máy ra thì không ai có thể nghe thấy âm thanh xung quanh.",
    # 048
    "Vì thế Nguyễn Uyên không nghe thấy tiếng nỉ non rên khẽ của Kỷ Cảnh, mà Kỷ Cảnh cũng không nghe thấy giọng của Nguyễn Uyên.",
    # 049
    "“Alpha chưa từng trải qua kỳ nhạy cảm mà bị tiêm thuốc tăng mẫn cảm tin tức tố, thì phải làm thế nào.”",
    # 050
    "Bề ngoài Lục Tư Niên vô cùng bình tĩnh trấn định hỏi, nhưng cơ thể lại vì tuyến thể bị giày vò mà vô lực trượt xuống, chút sức lực cuối cùng bị rút cạn, hai người rơi phịch xuống mặt thảm lông.",
    # 051
    "“Giọng cậu sao lại thế này... Cậu không phải đang... Đệt mợ??!”",
    # 052
    "“Mau nói đi!” Lục Tư Niên gắt gao gầm nhẹ.",
    # 053
    "“Hết cách rồi, không đánh dấu một Omega thì người cậu ta sẽ phế bỏ hoàn toàn đấy.” Ý thức được tình hình nghiêm trọng, thái độ Nguyễn Uyên lập tức trở nên nghiêm túc đứng đắn, “Hơn nữa không thể là đánh dấu tạm thời được đâu, cậu hiểu ý tôi chứ Lục Tư Niên, phải làm đến bước cuối cùng, tức là đánh dấu trọn đời đấy.”",
    # 054
    "...",
    # 055
    "Răng nanh sắc nhọn, cắn rách tuyến thể đỏ ửng sưng tấy, Kỷ Cảnh rốt cuộc không thể cưỡng lại nổi sự cám dỗ, một ngụm cắn rách khối phồng bên môi.",
    # 056
    "Cậu cuối cùng cũng nếm được dòng nước mát lành thanh khiết bên trong khối phồng ấy, cậu thầm nghĩ.",
    # 057
    "Hương gỗ thông nồng nặc men theo khoang miệng cậu hòa vào khắp các mạch máu toàn thân, da đầu Kỷ Cảnh tê dại bừng tỉnh, răng càng thêm dùng sức vài phần, cắn sâu hơn nữa.",
    # 058
    "Cơn đau ập đến dữ dội cưỡng ép ngắt đứt dây thần kinh kết nối thiết bị đầu cuối của Lục Tư Niên.",
    # 059
    "Giọng của Nguyễn Uyên đột ngột ngưng bặt, thiết bị đầu cuối rơi bộp xuống sàn nhà, trong đầu Lục Tư Niên lóe lên một khoảng trắng xóa mịt mù.",
    # 060
    "Anh cảm nhận được một luồng tin tức tố Alpha cực kỳ hùng hậu đang men theo tuyến thể bị cắn rách sau gáy với thế công đầy tính xâm lược, bá đạo xông thẳng vào cơ thể anh.",
    # 061
    "“Kỷ Cảnh.”",
    # 062
    "Lục Tư Niên thất thần nhìn lên trần nhà, vô thức gọi khẽ một tiếng tên cậu, âm sắc vừa trầm đục vừa khàn đặc.",
    # 063
    "Cà vạt của anh từ lâu đã rối tung rối mù, cúc áo sơ mi cũng bị bung đứt vài chiếc.",
    # 064
    "Kỷ Cảnh dựa theo bản năng cắn rách tuyến thể hoàn thành đánh dấu xong, lý trí ngắn ngủi quay trở lại.",
    # 065
    "“Lục Tư Niên, xin lỗi, em... không kìm chế được...” Trong giọng nói của Kỷ Cảnh để lộ ra một phần mờ mịt và luống cuống, nhưng nhiều hơn cả vẫn là ý định xâm lược chưa hề lắng xuống.",
    # 066
    "Gần như không có Alpha nào có thể chống cự nổi sự mất khống chế khi kỳ nhạy cảm ập đến, huống chi kỳ nhạy cảm của Kỷ Cảnh hoàn toàn là do bị thuốc tăng mẫn cảm tin tức tố ép buộc bộc phát.",
    # 067
    "Rất nhanh sau đó Kỷ Cảnh lại một lần nữa bị tước đoạt ý thức, việc đánh dấu tuyến thể đơn thuần tựa như gãi ngứa ngoài giày, hoàn toàn không thể làm lắng dịu những đợt sóng biển cuộn trào mãnh liệt.",
    # 068
    "Bản năng đã thao túng cơ thể cậu.",
    # 069
    "“Lục Tư Niên, anh giúp em đi mà...”",
    # 070
    "Kỷ Cảnh ngẩng đầu, hôn lên môi Lục Tư Niên, nhỏ giọng làm nũng.",
    # 071
    "...",
    # 072
    "Lọn tóc mái trước trán Kỷ Cảnh được một bàn tay thon dài rõ đốt ngón tay vén lên, ngón tay cái của Lục Tư Niên dịu dàng vuốt ve qua hàng lông mày được cố ý cạo tỉa thanh mảnh của cậu.",
    # 073
    "...",
    # 074
    "Lúc Kỷ Cảnh tỉnh dậy thì đã là buổi chiều của một ngày nào đó mà cậu chẳng rõ.",
    # 075
    "Cậu mở đôi mắt mơ màng mờ mịt, trong tầm nhìn nhòe nhoẹt xuất hiện một góc nghiêng gương mặt với đường nét lạnh lùng sắc bén.",
    # 076
    "Lục Tư Niên đang nửa dựa vào đầu giường, cặp kính nửa viền đen đã được tháo ra đặt trên tủ đầu giường, không còn cặp kính che chở tu sức, vẻ nho nhã ấm áp trên người anh bị giảm bớt, để lộ ra nét sắc sảo vốn có nơi chân mày ánh mắt anh.",
    # 077
    "Anh tựa như đang thất thần lơ đãng, lại tựa như đang trầm tư suy nghĩ.",
    # 078
    "Dường như phát hiện ra động tĩnh của Kỷ Cảnh, Lục Tư Niên chậm rãi nghiêng đầu sang, mấp máy môi nói: “Tỉnh rồi à?”",
    # 079
    "“Ừm...” Kỷ Cảnh theo phản xạ có điều kiện gật gật đầu.",
    # 080
    "Cậu mất vài phút đồng hồ để chắp vá lại những mảnh ký ức vụn vỡ trong suốt kỳ nhạy cảm vừa qua.",
    # 081
    "Thế nhưng linh hồn của cậu vẫn chưa hoàn toàn về đúng vị trí.",
    # 082
    "“Lục Tư Niên, bụng em đói cồn cào rồi này——”",
    # 083
    "Một giọng nữ ngọt ngào nũng nịu bất thình lình từ cổ họng Kỷ Cảnh thốt ra.",
    # 084
    "Trong khoảnh khắc, Lục Tư Niên ngẩn người sững sờ,",
    # 085
    "Kỷ Cảnh cũng lập tức tỉnh cả ngủ, đồng tử đột ngột co rút phóng đại.",
    # 086
    "Kỷ Cảnh hoàn toàn không ngờ bản thân lại vô thức dùng giọng nữ của Dịch Nam, cậu tận mắt nhìn thấy trên mặt Lục Tư Niên từ từ xuất hiện sự mờ mịt bàng hoàng.",
    # 087
    "“Kỷ Cảnh...” Giọng của Lục Tư Niên khàn đặc như bị lưỡi dao cứa qua, anh nhìn thẳng vào mắt Kỷ Cảnh, từng chữ từng chữ nói, “Dịch Nam chính là cậu, đúng không.”",
    # 088
    "Kỷ Cảnh gắt gao nhìn chằm chằm vào đôi mắt Lục Tư Niên, cố gắng nhìn ra điều gì đó từ đáy mắt anh, lời nói dối bị vạch trần một cách trở tay không kịp, sự hoảng loạn đột ngột trỗi dậy trong lòng làm đảo lộn toàn bộ năng lực phán đoán của cậu.",
    # 089
    "Cậu bỗng dời tầm mắt đi, trốn tránh không thèm nhìn Lục Tư Niên,",
    # 090
    "“Đúng, là tôi đấy.” Cậu vờ tỏ ra bình tĩnh nói.",
    # 091
    "“Tại sao lại lừa dối tôi.” Giọng điệu của Lục Tư Niên rất bình thản, nhưng thái độ càng bình thản thì lại càng khiến Kỷ Cảnh thẹn quá hóa giận bùng nổ.",
    # 092
    "Cậu tựa như một đứa trẻ lén ăn trộm kẹo bị bắt quả tang trước mặt mọi người, cố tình giương nanh múa vuốt thị uy để vớt vát lại chút thể diện tự tôn cuối cùng.",
    # 093
    "“Tại sao cái gì chứ, trêu chọc anh cho vui thôi mà, bằng không tôi mưu cầu gì ở anh hả?” Kỷ Cảnh nghiến chặt răng hàm sau, từ kẽ môi rặn ra câu nói này.",
    # 094
    "“Cậu chỉ là đang trêu đùa tôi thôi sao?” Giọng điệu vốn dĩ bình thản của Lục Tư Niên đột ngột hạ xuống điểm đóng băng.",
    # 095
    "Khi nhìn thấy gương mặt Lục Tư Niên vì những lời mình nói mà nhuộm lên vẻ tức giận, dây thần kinh của Kỷ Cảnh đứt phựt, đột nhiên bật ra một tiếng cười lạnh lẽo.",
    # 096
    "“Sao thế, anh thất vọng lắm đúng không, người Dịch Nam mà anh thích hóa ra lại là tôi, cô gái lương thiện ngoan ngoãn mọi mặt thuận theo ý anh hóa ra lại là tên Alpha nam từng làm nhục mẹ anh, anh tức chết đi được đúng không? Có phải anh cảm thấy Dịch Nam là tôi thì vô cùng kinh tởm buồn nôn không, tôi——”",
    # 097
    "“Kỷ Cảnh, tôi...” Lục Tư Niên đột nhiên cắt ngang lời cậu.",
    # 098
    "Thế nhưng Kỷ Cảnh lại chẳng cho Lục Tư Niên bất kỳ cơ hội nào để nói tiếp, cậu trốn tránh không muốn nghe Lục Tư Niên nói tiếp, sợ hãi chính miệng Lục Tư Niên sẽ thốt ra những lời căm ghét tởm lợm cậu.",
    # 099
    "“Tôi thấy anh cũng chẳng yêu Dịch Nam đến thế đâu nhỉ, bằng không cớ sao anh lại để tôi đánh dấu anh? Anh rõ ràng có thể vứt bỏ mặc xác tôi mà, anh ở lại làm cái gì chứ? Hừ, thế nào, có phải đột nhiên cảm thấy tôi so với phụ nữ càng làm cho anh——”",
    # 100
    "“Kỷ Cảnh, đủ rồi đấy!”",
    # 101
    "Lục Tư Niên nghiêm giọng quát lớn cắt ngang lời Kỷ Cảnh.",
    # 102
    "Kỷ Cảnh ngẩn người một thoáng, ngay sau đó nhận ra Lục Tư Niên vừa rồi đã lớn tiếng quát mình.",
    # 103
    "Cậu hình như chưa từng thấy Lục Tư Niên thẳng mặt quát tháo ai bao giờ, cùng lắm chỉ là hạ giọng gằn giọng thị uy mà thôi.",
    # 104
    "Ngay cả hồi cậu bị Lục Tư Niên đập nhừ tử năm xưa, Lục Tư Niên cũng không tức giận phẫn nộ như lúc này.",
    # 105
    "Cảm xúc của Lục Tư Niên chưa bao giờ biểu lộ mãnh liệt rõ ràng ra ngoài mặt như thế, xem ra anh thật sự hận chết cậu rồi.",
    # 106
    "Nghĩ đến đây, Kỷ Cảnh đột nhiên chẳng còn muốn nói bất cứ điều gì nữa, cậu lặng lẽ nhìn Lục Tư Niên, nhìn những vết thương chằng chịt thảm hại trên cơ thể vạm vỡ của anh.",
    # 107
    "“Xin lỗi.”",
    # 108
    "Cậu khẽ thốt lên một câu bằng giọng rất nhỏ.",
    # 109
    "Nói xong cậu im lặng bước xuống giường, ba chân bốn cẳng mặc lại quần áo chỉnh tề, rồi không thèm ngoái đầu lại cất bước rời đi.",
    # 110
    "Cánh cửa phòng bị đóng sập lại thật mạnh, căn phòng quay trở lại sự tĩnh mịch chết chóc như cõi chết, chỉ còn trơ trọi lại tiếng thở dốc nặng nề của Lục Tư Niên.",
    # 111
    "Không biết đã trôi qua bao lâu, Lục Tư Niên mới khẽ cử động cánh tay cứng đờ của mình.",
    # 112
    "Anh giơ tay lên, day day chân mày, nơi khóe môi tràn ra một nụ cười đắng chát xót xa.",
    # 113
    "Lục Tư Niên à, mày còn ôm hy vọng may mắn chờ đợi điều gì nữa chứ?",
    # 114
    "Mày thật sự nghĩ rằng Kỷ Cảnh là vì thích mày thật lòng nên mới giả trang thành Dịch Nam để theo đuổi mày sao?",
    # 115
    "Rõ ràng đã sớm nhận ra rồi, cậu ấy là vì muốn trả thù, chẳng phải sao.",
    # 116
    "Thế nhưng những lời cậu ấy nói với Lục Đảo Phong, cùng với việc vận dụng quyền lực nhà họ Kỷ để bỏ phiếu giúp anh rốt cuộc là xuất phát từ điều gì chứ?",
    # 117
    "Lục Tư Niên từ từ dựa vào đầu giường, mệt mỏi nhắm nghiền hai mắt lại.",
    # 118
    "Lời tác giả muốn nói:",
    # 119
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-23 22:03:02~2023-05-26 20:08:45 nha~",
    # 120
    "Cảm ơn thiên thần nhỏ đã ném địa lôi: Một Con Ngốc Nghếch 1 quả;",
    # 121
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: Tịch Trừng Tử 70 bình; Hạp Dương, Tiên Sinh Sơn Dương, 64980271, Vô Ngôn Kính 10 bình; Y 6 bình; Trân Châu Và Bánh Mì 5 bình; Mộng Y Trác 3 bình; Triều Ca 2 bình;",
    # 122
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 110: Lần đánh dấu đầu tiên\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_110 translation successfully.")
