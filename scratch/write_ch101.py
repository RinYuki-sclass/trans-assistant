# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_101\translation.md"

paras = [
    # 000
    "Kỷ Cảnh bấm chuông cửa rất lâu, nhưng vẫn không đợi được người bên trong mở cửa.",
    # 001
    "Thế là cậu đổi từ bấm chuông sang đập cửa, hạ quyết tâm nhất định phải đánh thức Lục Tư Niên dậy bằng được.",
    # 002
    "Rất nhanh sau đó, cậu nghe thấy tiếng sột soạt động đậy truyền ra từ bên trong cánh cửa.",
    # 003
    "Cửa lớn bị người bên trong đẩy mở ra một khe hở, cùng lúc đó, một luồng khí tức gỗ tuyết tùng nồng đậm từ khe cửa cuồn cuộn ùa ra.",
    # 004
    "“Dịch... Nam?”",
    # 005
    "Lục Tư Niên khàn giọng gọi một tiếng.",
    # 006
    "Kỷ Cảnh sau khi nghe thấy tiếng gọi này của Lục Tư Niên thì trở nên có chút không tự nhiên, bởi vì cậu cảm thấy hai tiếng “Dịch Nam” kia pha lẫn một mùi vị khó tả thành lời.",
    # 007
    "Cậu hơi thất thần, ngước mắt nhìn về phía Lục Tư Niên, lúc này mới để ý thấy Lục Tư Niên vẫn còn mặc một bộ đồ ngủ kiểu dáng cũ kỹ, cổ áo ngủ xộc xệch mở toang, vùng da lộ ra ngoài lan tỏa từng mảng ửng hồng, cặp kính đã không cánh mà bay, thần sắc vô cùng chật vật.",
    # 008
    "Lục Tư Niên dường như rất nóng, trên trán rịn ra những giọt mồ hôi li ti dày đặc, ngay cả vùng cổ cũng ướt đẫm một mảng.",
    # 009
    "“Lục, Lục Tư Niên, em chỉ đến thăm anh thôi.” Kỷ Cảnh hiếm hoi lắm mới lắp bắp một lần.",
    # 010
    "Lục Tư Niên như thể bị đóng đinh tại chỗ, thần sắc đờ đẫn nhìn chằm chằm vào cậu, Kỷ Cảnh men theo khe cửa mở rộng bước vào nhà anh, vừa thuận tay đóng cửa lại liền phát hiện do Lục Tư Niên đứng bất động nên cả người cậu bị giam chặt hoàn toàn giữa cánh tay anh và cánh cửa.",
    # 011
    "Mùi tuyết tùng nồng nặc hòa lẫn với nhiệt độ cơ thể khác thường của Lục Tư Niên, không chừa một kẽ hở nào bao bọc lấy cậu.",
    # 012
    "Bởi vì hiện tại đứng quá gần, Kỷ Cảnh lúc này mới nghe thấy nhịp thở dồn dập bất thường của Lục Tư Niên.",
    # 013
    "Lục Tư Niên duy trì tư thế mang tính xâm phạm ngột ngạt như vậy, đột nhiên không kìm lòng được mà thốt lên một câu,",
    # 014
    "“Dịch Nam, em thơm quá.”",
    # 015
    "Tiếng thở dốc của anh dường như càng thêm mất kiểm soát vì sự tiếp cận gần gũi của Kỷ Cảnh.",
    # 016
    "Cậu phát hiện Lục Tư Niên đang không thể khống chế nổi mà áp sát đè lên người mình, toàn thân toát ra khí tức đầy tính xâm lược áp đảo.",
    # 017
    "Kỷ Cảnh cũng bị luồng tin tức tố nồng đậm này hun đỏ cả vành tai, đồng tử dần dần tan rã, dường như có một sức mạnh vô hình nào đó đang thôi thúc cậu áp sát lại gần người Lục Tư Niên.",
    # 018
    "Đột nhiên, những ngón tay thon dài rõ khớp xương của Lục Tư Niên vén lọn tóc dài trước trán cậu lên, nhẹ nhàng cài ra sau vành tai.",
    # 019
    "Trong tầm nhìn, gương mặt Lục Tư Niên càng lúc càng phóng đại, hơi thở ấm áp phả vào bên môi Kỷ Cảnh... Kỷ Cảnh nghe thấy tiếng tim mình đập thình thịch...",
    # 020
    "“Này, Lục Tư Niên, anh muốn làm cái gì đấy.”",
    # 021
    "Kỷ Cảnh nhìn chằm chằm vào đôi mắt tối tăm sâu thẳm của Lục Tư Niên, đột nhiên tỉnh táo lại, lớn tiếng quát lên để che giấu sự bối rối.",
    # 022
    "Lục Tư Niên như bừng tỉnh khỏi cơn mê muội, như bị điện giật vội vàng buông lỏng Kỷ Cảnh ra, lùi lại phía sau mấy bước.",
    # 023
    "“Xin lỗi, tôi vào phòng vệ sinh một lát.”",
    # 024
    "Lục Tư Niên cứng đờ quay người, Kỷ Cảnh nhìn anh chật vật bước tới bên bàn trà, từ trong ngăn kéo lôi ra một chiếc ống tiêm, sau đó vội vã bước nhanh vào phòng vệ sinh.",
    # 025
    "Sau khi Lục Tư Niên đi xa, mùi hương khó chịu kia đã nhạt đi không ít, nhưng khắp căn phòng vẫn tràn ngập luồng khí tức ấy, Kỷ Cảnh cảm thấy cơ thể mình có chút khô nóng bồn chồn.",
    # 026
    "Cảm giác khô nóng này khiến cậu thấy vô cùng xa lạ.",
    # 027
    "Cậu bắt đầu đi quanh nhà Lục Tư Niên nhìn ngó tứ phía, quyết định để bản thân bình tĩnh lại một chút.",
    # 028
    "Nhà của Lục Tư Niên y hệt như con người anh, toát lên vẻ cứng nhắc và cấm dục.",
    # 029
    "Đồ đạc nội thất ít ỏi thưa thớt, mặt sàn sạch bóng không một hạt bụi.",
    # 030
    "Tông màu xám đậm đồng điệu, trong nhà ngoại trừ bó hoa hồng cắm trên bàn trà ra thì không còn bất kỳ màu sắc nào khác.",
    # 031
    "Kỷ Cảnh nhớ ra bó hoa hồng kia hình như là do chính mình tặng.",
    # 032
    "Cậu đẩy cánh cửa phòng ngủ của Lục Tư Niên ra, bị sàn nhà bừa bộn bên trong làm cho giật mình.",
    # 033
    "Dưới sàn vương vãi cà vạt, áo sơ mi và quần âu, đồng thời còn có vài vỏ ống tiêm rỗng lăn lóc trong góc phòng.",
    # 034
    "Quần áo dưới đất rất quen mắt, hẳn là đồ Lục Tư Niên mặc ngày hôm qua, Kỷ Cảnh suy đoán hôm qua Lục Tư Niên rất có thể trong trạng thái thần trí mơ màng đã thay vội đồ ngủ rồi nằm vật ra giường ngủ thiếp đi, nên mới không trả lời tin nhắn của cậu.",
    # 035
    "Vậy rốt cuộc Lục Tư Niên bị làm sao, bị sốt à?",
    # 036
    "Cậu bước tới, cúi người nhặt một vỏ ống tiêm rỗng lên, trên thân ống tiêm in những ký tự mà cậu đọc không hiểu.",
    # 037
    "“Dịch Nam.”",
    # 038
    "Giọng nói của Lục Tư Niên bất thình lình vang lên sau lưng, Kỷ Cảnh theo bản năng nhét vội ống tiêm vào túi áo khoác, quay người lại,",
    # 039
    "“Anh đỡ hơn chưa?”",
    # 040
    "“Ừ.” Vệt đỏ trên mặt Lục Tư Niên đã tan biến, trở lại trạng thái nghiêm nghị ít cười thường ngày, nhưng thấy Dịch Nam đang đứng trong phòng ngủ của mình, nét mặt anh lại có chút mất tự nhiên, cuối cùng, anh dùng khẩu khí không cho phép từ chối nói: “Dịch Nam, em về trước đi.”",
    # 041
    "Tối qua sau khi Lục Tư Niên về nhà liền phát hiện cơ thể trở nên vô cùng kỳ lạ.",
    # 042
    "Đặc biệt là tuyến thể sau gáy, vừa tê vừa ngứa, như thể đang khát khao mãnh liệt muốn được thứ gì đó sắc nhọn cắn rách.",
    # 043
    "Anh giống như trước đây tiêm thuốc ức chế Omega, vốn tưởng ngủ một giấc là sẽ ổn, không ngờ sau khi thức dậy vào ngày hôm sau sự khó chịu lại ập đến dữ dội hơn.",
    # 044
    "Anh không ngờ Dịch Nam vào lúc này lại tìm đến tận nhà anh, vừa nãy suýt chút nữa... bản thân anh đã mất khống chế.",
    # 045
    "Bất luận thế nào, Dịch Nam vào thời điểm này đều không thích hợp để ở chung một phòng với anh.",
    # 046
    "Kỷ Cảnh không vui, làm gì có ai người ta vừa tới đã đuổi người đi thế này chứ.",
    # 047
    "“Tại sao, em không về đâu, em đặc biệt đến thăm anh mà, có phải anh thấy trong người không khỏe không?”",
    # 048
    "Kỷ Cảnh ngồi phịch xuống giường của Lục Tư Niên, đôi chân trần đung đưa loạn xạ giữa không trung, bày ra một bộ dạng ăn vạ rõ rệt.",
    # 049
    "Hôm nay Kỷ Cảnh vẫn mặc một chiếc váy hai dây màu trắng, lúc bước vào đã cởi giày tất ra rồi.",
    # 050
    "Lục Tư Niên nhắm nghiền hai mắt lại.",
    # 051
    "“Dịch Nam, chúng ta... nam nữ khác biệt, em không nên vào phòng ngủ của tôi.” Anh day day sống mũi, trầm giọng nói.",
    # 052
    "“Lục Tư Niên, anh đừng có cổ hủ như thế chứ, bây giờ là thời đại nào rồi cơ chứ.”",
    # 053
    "Kỷ Cảnh đứng dậy, sau đó kéo cánh tay Lục Tư Niên dắt anh về phía mép giường, rồi nhân lúc cơ thể Lục Tư Niên còn đang cứng đờ, mạnh mẽ ấn anh ngồi xuống giường.",
    # 054
    "Ngọn tóc mềm mại khẽ lướt qua gò má Lục Tư Niên, Kỷ Cảnh từ trên cao nhìn xuống anh, ra lệnh: “Anh nằm trên giường nghỉ ngơi cho khỏe đi, hôm nay em sẽ chăm sóc anh thật chu đáo.”",
    # 055
    "Nói xong liền buông Lục Tư Niên ra, quay người bước ra khỏi phòng ngủ của anh, còn chu đáo khép cửa lại.",
    # 056
    "Đầu óc Lục Tư Niên vốn đã mê man nặng trĩu, đầu vừa chạm vào gối liền không kìm chế được mà chìm vào giấc ngủ mê mệt.",
    # 057
    "Kỷ Cảnh lên Mạng Tinh Vân tra cứu xem bị sốt thì làm thế nào để hạ sốt, trên mạng hướng dẫn cậu có thể nấu một nồi canh gừng.",
    # 058
    "Kỷ Cảnh nửa hiểu nửa không, may mà trong tủ lạnh của Lục Tư Niên rau củ khá đầy đủ, Kỷ Cảnh loay hoay suốt một tiếng đồng hồ, nấu ra được một nồi canh gừng với mùi hăng nồng sực mũi.",
    # 059
    "Cậu còn gửi tin nhắn cho Kỷ Vân Hy.",
    # 060
    "【Anh Cảnh Của Mày】: Người bị sốt uống canh gừng có khỏi được không? [Hình ảnh.jpg]",
    # 061
    "【Kỷ Vân Hy】: Mày hỏi tao á? Làm sao tao biết được?",
    # 062
    "【Kỷ Vân Hy】: Chờ đã, cái này là do mày nấu đấy à?! [Kinh hãi!]",
    # 063
    "【Kỷ Vân Hy】: Mẹ kiếp, mày không phải đang ở nhà Omega nào đấy chứ?",
    # 064
    "...",
    # 065
    "Kỷ Cảnh không thèm trả lời, múc một bát rồi đẩy cửa phòng ngủ của Lục Tư Niên bước vào.",
    # 066
    "Bởi vì trong phòng ngủ quá tối, Kỷ Cảnh kéo hé rèm cửa ra một chút, phát hiện bên ngoài trời đã bắt đầu lất phất đổ mưa nhỏ.",
    # 067
    "Cậu đặt chiếc bát lên đầu giường, gọi một tiếng Lục Tư Niên, nhưng không nhận được lời đáp lại.",
    # 068
    "Thế là cậu nửa quỳ bò lên giường, định bụng sẽ gọi Lục Tư Niên dậy.",
    # 069
    "Lục Tư Niên đang bị cảm giác nóng rát cuộn trào nơi tuyến thể sau gáy xâm chiếm, trong cơn mơ anh liên tục mơ thấy một gương mặt hoàn mỹ tựa như tượng tạc, cùng một đôi mắt đen sâu thẳm ánh lên tia giảo hoạt xấu xa.",
    # 070
    "Một giọng nữ dịu dàng đang khẽ gọi tên anh.",
    # 071
    "Bàn tay ấm áp còn sờ lên trán anh.",
    # 072
    "Nhẹ nhàng êm ái, như đang vỗ về sự nôn nóng và bất an trong lòng anh.",
    # 073
    "Anh từ từ mở mắt, nhìn thấy Dịch Nam đang chống hai tay hai bên tai mình, cúi đầu gọi anh.",
    # 074
    "Ngọn tóc buông rủ khẽ quét qua gò má anh, Lục Tư Niên cảm thấy cổ họng ngứa ngáy cồn cào.",
    # 075
    "Thấy anh tỉnh lại, Kỷ Cảnh định đổi tư thế ngồi dậy, nhưng không ngờ vừa định rút tay về liền bị Lục Tư Niên nắm chặt lấy cổ tay, cậu mất trọng tâm, ngã nhào vào lòng Lục Tư Niên.",
    # 076
    "Kỷ Cảnh đè lên người Lục Tư Niên, ngẩn người ra một thoáng, ngẩng cằm lên muốn ngồi dậy, vừa ngẩng đầu liền đối diện thẳng với đôi mắt đen kịt sâu thẳm của Lục Tư Niên.",
    # 077
    "“Khát nước...” Giọng nói của Lục Tư Niên như bị đá sỏi mài qua, nhưng Kỷ Cảnh lại nghe ra được trong đó mang theo ý vị làm nũng kín đáo.",
    # 078
    "Kỷ Cảnh vừa định bảo trên bàn có canh gừng, Lục Tư Niên rốt cuộc không thể nhịn nổi nữa, ấn gáy cậu xuống, dùng môi chặn kín cánh môi cậu.",
    # 079
    "Trong khoảnh khắc, tiếng gào thét bị đè nén nơi sâu thẳm nhất trong cơ thể điên cuồng phá tan gông cùm xiềng xích, chiếm trọn toàn bộ lý trí của Lục Tư Niên.",
    # 080
    "Tầm nhìn đảo lộn đất trời, đợi đến khi Kỷ Cảnh ý thức được điều gì thì bản thân đã bị Lục Tư Niên đè nghiến dưới thân.",
    # 081
    "Lục Tư Niên căn bản không biết hôn môi, anh chỉ vụng về không ngừng mút cánh môi Kỷ Cảnh, hôn một cái rồi buông ra, sau đó lại tiếp tục hôn.",
    # 082
    "Kỷ Cảnh đã bị luồng tin tức tố mùi tuyết tùng nồng nặc đột ngột ập tới bao trùm đến mức không thể thở nổi, đại não cũng sắp sửa ngừng hoạt động.",
    # 083
    "Xung động bên trong cơ thể thôi thúc cậu làm điều gì đó với Lục Tư Niên.",
    # 084
    "Chẳng hạn như lật người đè ngược lại, rồi một ngụm cắn rách tuyến thể sau gáy của Lục Tư Niên.",
    # 085
    "Đánh dấu Lục Tư Niên, để trên người anh vĩnh viễn khắc sâu cái tên Kỷ Cảnh của cậu.",
    # 086
    "Chân răng cậu vừa tê vừa ngứa.",
    # 087
    "Nhưng lý trí mách bảo cậu rằng hiện tại vẫn chưa thể làm như vậy.",
    # 088
    "“Lục Tư Niên...” Tranh thủ khoảng trống giữa nụ hôn, cậu khàn giọng ra lệnh, “Mở miệng ra.”",
    # 089
    "Lục Tư Niên khựng lại một thoáng, sau đó khẽ hé mở cánh môi, ngay khoảnh khắc tiếp theo, đầu lưỡi Kỷ Cảnh đã cạy mở hàm răng anh.",
    # 090
    "Ngoài cửa sổ đột nhiên nổ ra một tiếng sấm vang trời, trong nháy mắt, mưa rào trút xuống xối xả.",
    # 091
    "Trong mắt Lục Tư Niên xuất hiện một thoáng ngơ ngác chết lặng.",
    # 092
    "(Không có bất kỳ miêu tả thân mật nào dưới cổ)",
    # 093
    "“Lục Tư Niên.”",
    # 094
    "Cậu gắng gượng duy trì sự tỉnh táo, khàn giọng dừng nụ hôn này lại.",
    # 095
    "“Em ra ngoài đây.” Kỷ Cảnh đè giữ Lục Tư Niên, sau khi bình tĩnh lại đôi chút liền nói.",
    # 096
    "Kỷ Cảnh nhìn vẻ mặt ngơ ngác của Lục Tư Niên đang nằm trên giường, đột nhiên như nghĩ thông suốt điều gì đó.",
    # 097
    "“Mẹ kiếp anh... chẳng lẽ chưa từng...?”",
    # 098
    "Trong giọng điệu của cậu thêm vài phần không thể tin nổi.",
    # 099
    "Cậu cảm thấy Lục Tư Niên đúng là một kỳ tích.",
    # 100
    "Thấy đôi mắt đỏ hoe của Lục Tư Niên nhìn chăm chú vào mình, trong lòng Kỷ Cảnh ngổn ngang đủ loại cảm xúc lẫn lộn, cuối cùng thở dài thườn thượt một hơi.",
    # 101
    "“Thôi bỏ đi, coi như tôi chịu thua anh rồi.”",
    # 102
    "Cậu lẩm bẩm, cam chịu quay trở lại giường.",
    # 103
    "“Tốt nhất là anh cứ ngoan ngoãn cho tôi.”",
    # 104
    "Cậu hung dữ nói.",
    # 105
    "...",
    # 106
    "Kỷ Cảnh chăm sóc Lục Tư Niên suốt mấy ngày liền, cuối cùng nằm bên cạnh anh ngủ thiếp đi.",
    # 107
    "Ngày hôm sau Lục Tư Niên từ từ mở mí mắt nặng trĩu ra, anh nhìn trần nhà ngẩn người gần một phút đồng hồ, mới nhận ra trong lồng ngực mình đang ôm một người.",
    # 108
    "Tóc của Dịch Nam rất dài, vài lọn tóc rối quấn quanh cổ Lục Tư Niên, hàng mi khẽ run rẩy, ngủ rất say.",
    # 109
    "Bầu trời sau mấy ngày mưa tầm tã liên tiếp rốt cuộc đã hé lộ ánh nắng ấm áp dịu dàng.",
    # 110
    "Ánh nắng ban mai màu vàng nhạt từ ngoài cửa sổ rọi thẳng lên người Dịch Nam, ngay cả từng sợi tóc cũng như đang phát sáng.",
    # 111
    "Trên người Dịch Nam tùy tiện khoác một chiếc áo ngủ của Lục Tư Niên, trên cổ vẫn đeo dải ruy băng buộc cổ.",
    # 112
    "Từ một người sống biến thành một bức tượng điêu khắc cần bao nhiêu thời gian?",
    # 113
    "Lục Tư Niên sẽ nói cho bạn biết rằng chỉ cần đúng ba giây.",
    # 114
    "Lục Tư Niên bỗng bật dậy, chăn trượt khỏi người anh, lúc này anh mới phát hiện chiếc áo ngủ của mình đã không cánh mà bay từ bao giờ.",
    # 115
    "Vô số mảnh vỡ ký ức thức tỉnh trong tâm trí, ký ức rất mờ mịt hỗn độn, Lục Tư Niên càng không dám nhớ lại những chi tiết trong đó, chỉ mơ hồ nhớ được cảm giác hơi thở quấn quýt triền miên.",
    # 116
    "Lục Tư Niên gần như hoảng loạn chạy trối chết.",
    # 117
    "Anh đờ đẫn rời giường mặc quần áo chỉnh tề, lặng lẽ không một tiếng động bước ra khỏi phòng ngủ.",
    # 118
    "Trước khi đi anh còn nhắm nghiền mắt dùng chăn bọc kín mít cả người Kỷ Cảnh lại.",
    # 119
    "Lục Tư Niên trốn vào trong phòng tắm, hai tay chống lên bồn rửa mặt, nhìn chính mình trong gương, trong lòng trào dâng một cảm giác tội lỗi vô cùng mãnh liệt."
]

header = "---\ntitle: Chương 101: Tỉnh giấc chung giường\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written ch_101 translation successfully.")
