# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_111\translation.md"

paras = [
    # 000
    "Kỷ Cảnh một mạch sải bước ra khỏi phòng ngủ của Lục Tư Niên, căn nhà của Lục Tư Niên có thể nói là một mớ hỗn độn ngổn ngang, chiếc áo sơ mi bị xé toạc cùng chiếc cà vạt rối bời bị vứt bừa bãi trên sàn nhà, mỗi một cái liếc nhìn đều khiến những hình ảnh trong ký ức càng thêm rõ mồn một.",
    # 001
    "Cậu tìm lại bộ quần áo nhăn nhúm của mình rồi tròng qua đầu, bước nhanh rời khỏi nhà Lục Tư Niên.",
    # 002
    "Thiết bị đầu cuối vừa được bật lên, hàng loạt tin nhắn chưa đọc liền ùn ùn ùa vào tầm mắt của Kỷ Cảnh.",
    # 003
    "Đa phần đều là từ phía nhà trường gửi đến, hỏi cậu tại sao lại liên tục mấy ngày liền không có lý do chính đáng mà không đến lớp, trong đó còn xen lẫn không ít cuộc gọi nhỡ từ ba mẹ và Kỷ Vân Hy.",
    # 004
    "【Kỷ Vân Hy】: Sao mày lại trốn học nữa rồi",
    # 005
    "【Kỷ Vân Hy】: Lại không nghe máy? Đừng bảo là lại ở nhà Lục Tư Niên đấy nhé!",
    # 006
    "【Kỷ Vân Hy】: Phía ba mẹ tao giữ chân giúp mày rồi đấy, liệu mà nhanh cái chân lên!",
    # 007
    "...",
    # 008
    "Kỷ Cảnh ngồi trên xe trở về nhà, lúc này mới muộn màng cảm thấy hai bên thái dương đau nhức nhối.",
    # 009
    "Ngoài thái dương ra, tuyến thể Alpha nơi sau gáy cậu cũng nhức mỏi căng trướng, cậu tiện tay sờ thử một cái, mới phát hiện bên trên vẫn còn những vết răng gồ ghề không bằng phẳng...",
    # 010
    "Là do Lục Tư Niên cắn.",
    # 011
    "Tại sao lại cắn chứ, là tức giận, hay là lúc tình cảm nồng nàn đã xem cậu thành Dịch Nam rồi.",
    # 012
    "Chậc.",
    # 013
    "Kỷ Cảnh vô cùng phiền lòng, đặc biệt là khi nghĩ đến mọi chuyện vừa mới xảy ra.",
    # 014
    "Cứ vậy đi, dứt khoát thì dứt khoát, dù sao Lục Tư Niên cũng hận chết cậu rồi, cậu bực bội thầm nghĩ.",
    # 015
    "Dựa theo mức độ hiểu biết của Kỷ Cảnh về Lục Tư Niên, cậu cho rằng khi ấy Lục Tư Niên ở lại có lẽ là vì trong lòng cảm thấy áy náy khi cậu đỡ giúp anh mũi tiêm kia.",
    # 016
    "Với tinh thần trách nhiệm kỳ quặc của Lục Tư Niên, nếu vứt bỏ cậu lại mà chạy lấy người thì mới là chuyện bất thường.",
    # 017
    "Còn về sau đó... chắc là Lục Tư Niên không thể kháng cự nổi tin tức tố Alpha của cậu, nên mới mơ mơ màng màng mà lên giường cùng cậu.",
    # 018
    "Kỷ Cảnh đưa ra một lời giải thích lạnh lùng tàn nhẫn cho hành vi của Lục Tư Niên.",
    # 019
    "Thực ra cậu ngay từ khoảnh khắc bước chân ra ngoài đã hối hận rồi, hối hận vì những lời vừa rồi đã nói với Lục Tư Niên.",
    # 020
    "Kỷ Cảnh từ nhỏ đã là một người vô cùng hiếu thắng, cậu không thể chịu đựng nổi bất kỳ ai chỉ trích mình, cũng không chấp nhận nổi bất cứ sự thất bại nào.",
    # 021
    "Bởi vậy năm xưa sau khi bị Omega mà mình theo đuổi từ chối, cậu mới thẹn quá hóa giận đối với Lục Tư Niên, để cho linh hồn cốt truyện thừa cơ chen chân vào.",
    # 022
    "Bởi vậy khi bị Lục Tư Niên vạch trần, nhận ra lớp ngụy trang của mình đã thất bại, hoặc là thân phận chân thật về mặt tình cảm không được Lục Tư Niên thừa nhận, cậu mới không thể khống chế nổi cảm xúc của chính mình.",
    # 023
    "Thực ra cuối cùng cậu có rất nhiều điều muốn nói, nhưng khi nhìn thấy những tia máu đỏ ngầu trong hốc mắt Lục Tư Niên, tất cả chỉ có thể hóa thành một câu xin lỗi.",
    # 024
    "Độ rung của thiết bị đầu cuối cắt ngang dòng suy nghĩ của Kỷ Cảnh, là tin nhắn do Vương Bằng gửi tới.",
    # 025
    "【Vương Bằng】: Thằng ranh con mày lại chơi trò mất tích với tao đấy à!",
    # 026
    "【Vương Bằng】: Hôm nay thứ Sáu rồi, năm giờ chiều nay đợt tuyển quân của Đệ tam quân đoàn kết thúc rồi đấy, mày rốt cuộc có đến hay không hả.",
    # 027
    "【Vương Bằng】: Nếu muốn đến thì bây giờ chạy qua vẫn còn kịp, cơ hội ngàn năm có một đấy Kỷ Cảnh à.",
    # 028
    "Hôm nay đã là thứ Sáu, đồng nghĩa với việc cậu đã ở lì trong nhà Lục Tư Niên tròn ba ngày.",
    # 029
    "Kỷ Cảnh cụp mắt chăm chú nhìn dòng tin nhắn này, như có điều suy nghĩ, vừa định gõ phím trả lời, nhưng ngay khoảnh khắc ngón tay khẽ cử động cậu lại khẽ bật cười thành tiếng.",
    # 030
    "Cậu vậy mà vào lúc này vẫn đang nghĩ về Lục Tư Niên, nghĩ rằng nếu như mình không đi báo danh đợt này, có phải cậu và Lục Tư Niên sẽ hoàn toàn đường ai nấy đi, mấy trăm năm nữa cũng chẳng gặp lại nhau hay không.",
    # 031
    "Cho dù có đến cùng một quân đoàn thì đã sao chứ?",
    # 032
    "Lục Tư Niên căn bản chẳng hề muốn nhìn thấy cậu nữa đâu.",
    # 033
    "Thế là Kỷ Cảnh phẳng lặng khóe môi, trả lời lại",
    # 034
    "【Kỷ Cảnh】: Không đi.",
    # 035
    "Xe dừng lại trước cổng trang viên Kỷ gia, Kỷ Cảnh xuống xe, cất bước đi thẳng vào trong nhà.",
    # 036
    "Giờ này ba mẹ Kỷ đều không có ở nhà, nhưng Kỷ Vân Hy lại hệt như một người gác cổng, ngay khi cậu vừa về đến nhà đã chặn đứng cậu ngay tại trận.",
    # 037
    "“Khai thật mau, mấy ngày nay mày lại đi đâu làm gì, có phải lại ở bên cạnh Lục Tư Niên không hả!”",
    # 038
    "Kỷ Vân Hy chống nạnh, chỉ trỏ trách móc, nháy mắt ra hiệu: “Gì thế hả, chẳng phải bảo là muốn chia tay với anh ta rồi sao, thế quái nào mà ngày nào cũng dính lấy nhau thế hả...”",
    # 039
    "“Chia rồi.”",
    # 040
    "Kỷ Cảnh không chút biểu cảm ngắt lời giọng điệu hóng hớt của Kỷ Vân Hy.",
    # 041
    "“... Hả?”",
    # 042
    "Kỷ Cảnh chẳng buồn để ý đến Kỷ Vân Hy đang ngơ ngác hóa đá tại chỗ, sải bước đi lên lầu.",
    # 043
    "Thế nhưng lúc này Kỷ Vân Hy ở phía sau cậu đột nhiên kinh hãi thốt lên một tiếng: “Trời đất ơi! Kỷ Cảnh, chỗ tuyến thể của mày bị làm sao thế kia!”",
    # 044
    "Kỷ Cảnh dừng bước, theo bản năng đưa tay sờ sờ sau gáy, ngập ngừng một hồi lâu rồi giấu giếm bảo: “Không có gì.”",
    # 045
    "Tình hình hiện tại vẫn chưa cho phép cậu kể hết toàn bộ sự việc ra, nhưng lời nói tiếp theo của Kỷ Vân Hy lại khiến cậu chợt nhớ tới một chuyện.",
    # 046
    "“Tao nhìn bộ dạng tuyến thể của mày sao giống như lúc Alpha bước vào kỳ mẫn cảm thế, mày cẩn thận chút đấy, lỡ như mày đột nhiên phát tác kỳ mẫn cảm thì làm sao bây giờ, vết bên trên kia không phải là do Lục Tư Niên cắn đấy chứ, phù, may mà anh ta chỉ là một Beta, bằng không thì...”",
    # 047
    "“Đánh dấu của Alpha đối với Omega mất bao lâu thì tiêu tan?”",
    # 048
    "Kỷ Cảnh đột nhiên cất tiếng hỏi.",
    # 049
    "Kỷ Vân Hy ngẩn ra: “Đánh dấu bình thường thì nhanh lắm, nhiều nhất là một tháng là biến mất sạch rồi, sao thế?”",
    # 050
    "“Không có gì.”",
    # 051
    "Thế thì Lục Tư Niên cùng lắm chỉ một tháng nữa là hoàn toàn chẳng còn dính dáng gì đến cậu nữa rồi.",
    # 052
    "...",
    # 053
    "【Vương Bằng】: Lục tổng chỉ huy, Kỷ Cảnh không đến báo danh đợt tuyển quân của Đệ tam quân đoàn rồi.",
    # 054
    "【Vương Bằng】: Cậu có thể nói với Chu Độ một tiếng được không, thật sự không thể trách tôi đâu đấy, tôi khuyên đến rát cả cổ họng rồi, thằng nhóc này không chịu thì tôi cũng hết cách.",
    # 055
    "Lục Tư Niên đứng giữa căn phòng khách trống trải, nhìn thấy tin nhắn do Vương Bằng gửi đến.",
    # 056
    "Anh đã dành ra vài ngày để hoàn tất thủ tục từ chức ở Học viện Quân sự Đế quốc, mọi thủ tục cần thiết trước khi trở lại quân đoàn, cũng như đơn xin kế nhiệm vị trí quân đoàn trưởng.",
    # 057
    "Hành lý của anh rất ít, ít đến mức chỉ mất vỏn vẹn một tiếng đồng hồ là đã thu dọn xong xuôi mọi thứ trong cả căn nhà.",
    # 058
    "Bên chân đặt một chiếc túi hành lý quân dụng đơn giản, sáng sớm ngày kia chỉ cần xách lên một cái là có thể rời khỏi căn nhà này, không để lại bất kỳ dấu vết tồn tại nào.",
    # 059
    "【Lục Tư Niên】: Được rồi, tôi biết rồi.",
    # 060
    "Lục Tư Niên không hề cảm thấy bất ngờ trước kết quả này.",
    # 061
    "Mấy ngày nay anh thậm chí từng nghĩ, nếu như lúc ấy anh giả vờ như không nghe thấy Kỷ Cảnh dùng giọng nữ, liệu rằng Kỷ Cảnh có không bỏ chạy hay không.",
    # 062
    "【Lục Tư Niên】: Năm tiếp theo làm phiền cậu chỉ dẫn kèm cặp tốt Kỷ——",
    # 063
    "Còn chưa kịp gửi đi, cuộc gọi của Trương Mạc đã gọi tới.",
    # 064
    "“Thư tố cáo của cậu đã chuyển đến chỗ tôi rồi, chuyện của Lâm Diên Sơn cậu chắc chắn muốn khởi tố chứ?”",
    # 065
    "“Chắc chắn.”",
    # 066
    "“Cậu phải nghĩ cho kỹ đấy, nếu khởi tố, thân phận Omega của cậu bắt buộc phải phơi bày trước toàn thể đế quốc đấy.”",
    # 067
    "“Tôi chấp nhận.” Lục Tư Niên bình thản đáp.",
    # 068
    "“Haizz.” Trương Mạc thở dài một hơi nặng nề, “Thôi được rồi, nhưng tôi phải nói trước, cậu chấp nhận được không có nghĩa là đám Alpha của Đệ tam quân đoàn có thể chấp nhận đâu. Thêm nữa, trong đó có một điểm không đúng lắm, cậu nói cậu bị Lâm Diên Sơn tiêm thuốc kích mẫn, vậy sau đó cậu giải quyết bằng cách nào?”",
    # 069
    "“Chuyện đó không quan trọng, Lâm Diên Sơn hắn ta sẽ tự nhận tội.”",
    # 070
    "Trong đôi mắt đen trầm tịch của Lục Tư Niên lóe lên một tia sáng lạnh buốt.",
    # 071
    "“Lục Tư Niên, tao thật không ngờ mày lại vì tao mà cam tâm tình nguyện phơi bày thân phận Omega của mày, tại sao lại bắt tao giấu giếm chuyện của Kỷ thái tử, chuyện đó có lợi lộc gì cho mày chứ?” Trong ký ức, Lâm Diên Sơn thoi thóp cười lạnh ngông cuồng.",
    # 072
    "“Ngươi chỉ cần hiểu rằng, nếu để Kỷ gia biết được ngươi đã ra tay với Kỷ Cảnh, ngươi sẽ còn chết thảm hơn thế này nhiều.” Lục Tư Niên giẫm lên ngực hắn, trầm giọng nói.",
    # 073
    "Sắc mặt Lâm Diên Sơn khi ấy lúc xanh lúc trắng, cuối cùng đột nhiên cười đầy vẻ châm chọc: “Thôi đi, mày tưởng tao thật sự không biết mày chính là muốn báo thù cho nó sao, bằng không một kẻ giỏi nhẫn nhịn như mày, làm sao có thể làm đến bước này chứ, Lục Tư Niên, thật không ngờ mày lại vì một tên Alpha...”",
    # 074
    "...",
    # 075
    "Sau khi cúp điện thoại, Lục Tư Niên không kìm được mà bấm mở một khung trò chuyện.",
    # 076
    "Ảnh đại diện của đối phương đã biến thành màu xám tro, thứ còn sót lại chỉ là một mảnh tĩnh lặng như chết.",
    # 077
    "Không biết đã nhìn chăm chú bao lâu, Lục Tư Niên mới chầm chậm gập thiết bị đầu cuối lại.",
    # 078
    "...",
    # 079
    "“Kỷ Cảnh.”",
    # 080
    "Tiếng ngón tay gõ nhịp xuống mặt bàn bất thình lình kéo dòng tâm tư cuộn trào của Kỷ Cảnh trở về.",
    # 081
    "“Mấy ngày nay con bị làm sao thế hả, ba mẹ nói chuyện với con mà con cứ mất hồn mất vía mãi thế.”",
    # 082
    "Trên bàn ăn, ba Kỷ nghiêm nghị nhìn cậu nói.",
    # 083
    "Kỷ Vân Hy thấy vậy liền vội vàng giảng hòa xoa dịu bầu không khí: “Ôi dào, chắc chắn là do tin tức Lục Tư Niên là Omega mà ba vừa kể làm nó giật nảy mình đấy thôi, Kỷ Cảnh mày nói có phải không?”",
    # 084
    "Kỷ Vân Hy vừa nói, vừa dùng khuỷu tay thúc mạnh vào người Kỷ Cảnh.",
    # 085
    "Lúc ăn bữa sáng hôm nay, ba Kỷ theo thói quen bật bản tin buổi sáng lên xem, vừa xem vừa kể về chuyện Lục Tư Niên khởi tố tổng chỉ huy đương nhiệm của Đệ tam quân đoàn là Lâm Diên Sơn, còn mở thiết bị đầu cuối cho bọn họ xem tin tức.",
    # 086
    "“À, vâng.” Kỷ Cảnh thẫn thờ đáp lời, cậu vẫn còn chưa thể bình tâm lại sau chuyện này.",
    # 087
    "Lục Tư Niên tự bộc lộ mình là Omega để làm cái giá khởi tố Lâm Diên Sơn, anh điên rồi sao?",
    # 088
    "Tại sao lại làm như vậy, chẳng phải anh là người để tâm nhất đến việc mình biến thành Omega sao?",
    # 089
    "Kỷ Cảnh biết điều cấm kỵ nhất của Lục Tư Niên chính là thân phận Omega, thế nên từ sau khi trở về cậu chưa từng nhắc đến việc mình bị tiêm thuốc kích mẫn dẫn đến phát tác kỳ mẫn cảm đầu tiên, bởi vì một khi nói cho ba mẹ Kỷ biết, chuyện Lục Tư Niên là Omega sẽ vì Lâm Diên Sơn mà bị ép phải phơi bày ra ánh sáng.",
    # 090
    "Hơn nữa vì sao chuyện này từ đầu chí cuối lại không hề nhắc tới một lời nào về cậu.",
    # 091
    "Kỷ Cảnh đột nhiên nghĩ tới một phỏng đoán không tưởng —— chẳng lẽ Lục Tư Niên là vì không muốn kéo cậu vào vòng xoáy này.",
    # 092
    "“Lục Tư Niên không nên nói ra điều đó, quân đoàn trước nay không bắt buộc quân nhân phải công khai giới tính, nó đã tiếp nhận chức vị quân đoàn trưởng của Đệ tam quân đoàn, bất luận là các Alpha trong quân đoàn hay Alpha trên toàn đế quốc, đều sẽ không phục trước thân phận Omega của nó đâu.”",
    # 093
    "Ba Kỷ thuận miệng nhận xét.",
    # 094
    "Kỷ Cảnh vẫn còn đang bàng hoàng thừ người ra thì tin nhắn của Vương Bằng lại gửi tới.",
    # 095
    "【Vương Bằng】: Có người nhờ tôi chuyển lời cho cậu, bảo cậu nhớ đi bệnh viện kiểm tra đấy.",
    # 096
    "Một dòng tin nhắn vô cùng khó hiểu, nhưng Kỷ Cảnh lập tức hiểu ngay người đó là ai.",
    # 097
    "Là Lục Tư Niên, Lục Tư Niên bảo cậu đi bệnh viện.",
    # 098
    "Kỷ Cảnh nghiến chặt quai hàm, đưa tay ra sau sờ nắn tuyến thể vẫn còn hơi sưng tấy, không nói một lời nào, cậu quả thực nên đến bệnh viện kiểm tra một chuyến.",
    # 099
    "Ăn sáng xong, Kỷ Cảnh liền ra ngoài đi tới bệnh viện.",
    # 100
    "Kỳ mẫn cảm đầu tiên có thể nói là giai đoạn quan trọng bậc nhất của một Alpha, chỉ cần sơ sẩy một chút là sẽ tàn phế cả đời, Kỷ Cảnh bao nhiêu ngày qua không thèm để tâm đến, ông lão bác sĩ Alpha ở bệnh viện nhìn cậu cứ như nhìn một thằng ngốc.",
    # 101
    "Đặc biệt là khi nghe Kỷ Cảnh nói mình bị thuốc kích thích tin tức tố dẫn đến bùng phát kỳ mẫn cảm đầu tiên, ông lão sợ tới mức tờ phiếu xét nghiệm trên tay cũng run lẩy bẩy.",
    # 102
    "“Ta bảo sao chỉ số hormone của cậu lại quái dị đến mức này chứ.” Ông lão nhìn vào bảng chỉ số trên tay, cố tỏ ra bình tĩnh hớp một ngụm trà.",
    # 103
    "“Nhưng cũng may đấy, Omega nhà cậu xử lý kịp thời, bằng không thì cậu đã tàn phế cả đời rồi, hiện tại nhìn qua thì tin tức tố Alpha của cậu vẫn tính là bình thường.”",
    # 104
    "Kỷ Cảnh nhận lại phiếu khám, đợi ông lão kê đơn thuốc.",
    # 105
    "“Hay là lát nữa cậu ghé qua quầy thuốc lấy thêm một thang thuốc dưỡng thai đi, giai đoạn đầu Omega là dễ sảy thai nhất đấy...”",
    # 106
    "Ông lão kê đơn xong, vừa dặn dò vừa cầm chén trà lên uống một hớp.",
    # 107
    "“Cái gì, ai dưỡng thai cơ? Cháu là Alpha mà.” Kỷ Cảnh ngẩn người, quay đầu nhìn ông.",
    # 108
    "“Ta đương nhiên biết cậu là Alpha, thuốc là để cho Omega của cậu uống.” Ông lão nghiêm túc nói, “Sau khi đánh dấu trọn đời thì khả năng thụ thai của Omega lên tới 90% đấy, hai đứa các cậu phải luôn luôn để ý.”",
    # 109
    "“Đánh dấu trọn đời cái gì cơ?” Đầu óc Kỷ Cảnh quay cuồng chao đảo, rồi hai mắt từ từ trợn tròn kinh ngạc.",
    # 110
    "Ông lão dường như nhận ra sự việc không hề đơn giản, liền đặt chén trà xuống, nghiêm giọng nói: “Nhóc con, cậu là do thuốc kích thích tin tức tố dẫn đến bùng phát kỳ mẫn cảm đầu tiên, cách duy nhất giúp cậu vượt qua kỳ mẫn cảm chỉ có thể là đánh dấu trọn đời một Omega, nói cách khác, Omega của cậu đã bị cậu đánh dấu trọn đời rồi, cậu đã hiểu chưa?”",
    # 111
    "Mãi cho đến khi bước chân ra khỏi bệnh viện, Kỷ Cảnh vẫn như một kẻ mất hồn.",
    # 112
    "Đánh dấu trọn đời.",
    # 113
    "Ông lão kia nói cậu đã đánh dấu trọn đời Lục Tư Niên.",
    # 114
    "Ông lão nói muốn đánh dấu trọn đời thì bắt buộc phải tiến vào khoang sinh sản mới có thể hoàn thành, dựa theo những kiến thức sinh lý AO mà cậu từng biết, cậu đột nhiên nhớ lại Lục Tư Niên từng chủ động...",
    # 115
    "Nghĩ đến đây, Kỷ Cảnh muộn màng nhận thức được rằng, Lục Tư Niên hóa ra sớm đã bị cậu đánh dấu trọn đời rồi.",
    # 116
    "Lời tác giả:",
    # 117
    "Hai người họ một người thì bốc đồng trẻ con, một người thì câm như hến, nảy sinh hiểu lầm là chuyện tất nhiên rồi.",
    # 118
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-26 20:08:45~2023-06-02 22:58:16 nhé~",
    # 119
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Hôm nay trăng đã tròn chưa 34 bình; Đồ Họa Ấn Hoa 10 bình; Tửu Khốn Tư Trà, Y 5 bình; Tích Điểm Vận Khí, Nhàn de Diêm 3 bình; Liêu Nhũ, Đề Đăng Nguyện Thanh Hoan 2 bình; Vũ, Lai Nhật Phương Trường 1 bình;",
    # 120
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 111: Rời đi sau cơn mẫn cảm\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
