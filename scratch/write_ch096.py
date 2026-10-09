# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_096\translation.md"

paras = [
    # 000
    "Trên sân tập rộng lớn, từng hồi còi chói tai vang vọng khắp không gian.",
    # 001
    "Lại là một ngày thứ Sáu, lúc Lục Tư Niên đi ngang qua sân tập liền bắt gặp cảnh tượng trước mắt —— đám Alpha trẻ tuổi hiếu thắng quây thành một vòng tròn, ở giữa có hai Alpha đang cởi trần cận chiến tay đôi.",
    # 002
    "Một trong hai người sở hữu dung mạo quá đỗi hút mắt, đôi mắt đen như đá hắc diệu thạch tựa như loài báo săn đang rình mồi.",
    # 003
    "Alpha đối diện rõ ràng đã không chống đỡ nổi nữa, mặt mũi bầm tím ngã gục xuống mặt đất.",
    # 004
    "“Kỷ Cảnh ghi thêm một điểm, hiện tại đã được 7 điểm rồi, thắng liền bảy trận, còn ai muốn lên đấu với cậu ta nữa không?”",
    # 005
    "Vương Bằng thổi còi, cất giọng sang sảng hét lớn.",
    # 006
    "“Mẹ kiếp, có biến thái quá không vậy, giờ tao tin Kỷ Cảnh bị đoạt xá thật rồi đấy.”",
    # 007
    "“Tuần trước đánh giá tháng, tính cả mấy lớp chỉ huy, phòng ngự, pháo binh các kiểu, Kỷ Cảnh đứng nhất toàn khoá, hạng nhất đấy! Có thể thế được à, chỉ vỏn vẹn một tháng mà từ bét bảng nhảy vọt lên hạng nhất?!”",
    # 008
    "Đám Alpha bên dưới bất bình phẫn nộ, từng người một thi nhau đứng dậy muốn lên so tài với Kỷ Cảnh.",
    # 009
    "Vương Bằng cười huýt sáo một tiếng, sau đó đứng sang một bên xem trò vui, đột nhiên ánh mắt liếc qua, thấy Lục Tư Niên đang đứng cách đó không xa.",
    # 010
    "“Lục chỉ... à không đúng, Lục giáo sư, lâu lắm rồi không thấy anh.” Vương Bằng bước đến bên cạnh Lục Tư Niên ôn lại chuyện cũ.",
    # 011
    "“Ừ.” Lục Tư Niên gật đầu, nhưng ánh mắt vẫn không hề rời khỏi người Kỷ Cảnh.",
    # 012
    "Vương Bằng nhìn theo tầm mắt của anh, tiếp lời: “Thấy không, thằng nhóc đó đấy, Kỷ Cảnh, tân sinh viên lớp trinh sát, một hạt giống tốt, tuy từng bị lưu ban, nhưng tôi dám nói cậu ta là thiên tài trong mấy khóa gần đây cũng chẳng ngoa đâu.”",
    # 013
    "“Chậc, có điều người này tà môn thật sự, rõ ràng trước kia yếu như sên, đùng một cái biến thành con người khác, nếu không phải đích thân tôi quan sát cậu ta suốt một tháng trời, tôi còn nghi cậu ta dùng tà thuật gì ấy chứ.” Vương Bằng vừa nói vừa cảm thán, “Nhưng mà nhiều lúc cái nhuệ khí trên người cậu ta, nhìn rất giống anh hồi trước đấy.”",
    # 014
    "“Ừ, không tệ.” Lục Tư Niên quan sát một lát, gật đầu nói.",
    # 015
    "Lục Tư Niên vốn luôn biết rất rõ Kỷ Cảnh có thiên phú.",
    # 016
    "Vương Bằng cười cười, đột nhiên huých nhẹ vai anh: “Này, Lục giáo sư, dạo này có tin vui à? Chừng nào mới công khai chị dâu cho anh em biết đây?”",
    # 017
    "Lục Tư Niên khẽ chau mày: “Chị dâu nào?”",
    # 018
    "“Anh không xem nhóm chat à, có người chụp được ảnh anh hẹn hò với chị dâu trong trường kìa, phải công nhận là xinh đẹp tuyệt đỉnh luôn,” Vương Bằng trêu chọc, “Cơ mà, cứ thấy gương mặt đó quen quen ở đâu rồi ấy...”",
    # 019
    "“Không có chị dâu nào cả, đừng đồn bậy.” Lục Tư Niên nghiêm túc nói.",
    # 020
    "“Thật hay đùa thế, anh ngần này tuổi rồi mà còn chưa chịu ổn định à? Giờ đằng nào cũng giải ngũ rồi, đến lúc nên yêu đương đăng ký kết hôn rồi sinh con đẻ cái các thứ đi chứ...”",
    # 021
    "“Tôi không thích hợp.” Lục Tư Niên ngắt lời anh ta, vẫy tay rồi quay người rời đi.",
    # 022
    "Bên này Vương Bằng còn đang ngơ ngác, bên kia Kỷ Cảnh đã kết thúc trận đấu, ánh mắt cậu dõi theo hướng Lục Tư Niên đi, sau đó chẳng buồn chào hỏi ai mà cất bước đuổi theo.",
    # 023
    "“Này, Lục Tư Niên.”",
    # 024
    "Kỷ Cảnh đi theo Lục Tư Niên rẽ qua một khúc quanh, lên tiếng gọi giật lại.",
    # 025
    "Lục Tư Niên dừng bước, quay lưng về phía cậu lạnh lùng nói: “Kỷ Cảnh, tôi nghĩ cậu nên hiểu rõ tôi không có ý định truy cứu hành vi lần trước của cậu.”",
    # 026
    "“Làm gì căng thế, chẳng phải chỉ hôn anh một cái thôi sao, truy cứu thế nào, bắt tôi chịu trách nhiệm à?” Kỷ Cảnh nhìn anh, đầy ác ý kéo dài giọng điệu.",
    # 027
    "Cậu đương nhiên biết Lục Tư Niên sẽ không truy cứu, Lục Tư Niên hơn ai hết không hề muốn để người khác biết mình là Omega.",
    # 028
    "Lưng Lục Tư Niên căng cứng lại, Kỷ Cảnh ngửi thấy mùi nguy hiểm thoang thoảng trong không khí.",
    # 029
    "Một lúc sau, luồng khí tức kia bị cưỡng ép đè nén xuống, Lục Tư Niên đột nhiên xoay người đối diện với cậu, bình tĩnh hỏi: “Kỷ Cảnh, cậu có một người em gái?”",
    # 030
    "Kỷ Cảnh nghe vậy đầy ẩn ý nhướng mày, khóe môi cong lên: “Chuyện này mà cũng bị anh biết rồi cơ à?”",
    # 031
    "Ý tứ ngoài lời chính là cậu quả thực có một đứa em gái.",
    # 032
    "Nhận được câu trả lời, Lục Tư Niên nhìn sâu vào mắt cậu một cái, sau đó quay đầu bước đi, anh không muốn xảy ra xung đột với Kỷ Cảnh.",
    # 033
    "Kỷ Cảnh bỗng cảm thấy có chút thú vị, thầm nghĩ chi bằng làm cho cục diện càng thêm thú vị hơn một chút, bèn hướng về bóng lưng Lục Tư Niên thốt ra một câu: “Lục Tư Niên, tôi muốn theo đuổi anh.”",
    # 034
    "“Tôi không nói đùa đâu, bằng không lần trước đã chẳng hôn môi anh rồi.” Kỷ Cảnh tiếp tục gào toáng lên.",
    # 035
    "Nhìn thấy bàn tay xuôi bên hông của Lục Tư Niên siết chặt thành nắm đấm, bóng lưng càng lúc càng đi xa, cuối cùng biến mất khỏi tầm mắt.",
    # 036
    "Kỷ Cảnh bật cười, khàn giọng lẩm bẩm: “Xem ra, mình đã có tiến triển rồi đấy chứ.”",
    # 037
    "...",
    # 038
    "Kỷ Cảnh vác cả người đầy mồ hôi trở về nhà, vừa bước vào cửa chính liền phát hiện dọc hành lang bày kín hoa hồng.",
    # 039
    "“Uầy, lão Kỷ lại muốn cầu hôn nữa à?”",
    # 040
    "Cậu vừa kinh ngạc vừa buột miệng kêu lên.",
    # 041
    "Kỷ Vân Hy bên cạnh kéo lê đôi dép lê đi tới, vẻ mặt không còn tha thiết gì cuộc đời: “Mai là lễ tình nhân, hôm nay lão Kỷ lại đang khởi động làm nóng người ở đây đấy.”",
    # 042
    "Kỷ Trình là một người đàn ông nhìn bề ngoài có vẻ nghiêm túc cứng nhắc nhưng bên trong lại cực kỳ lãng mạn và mang trái tim thiếu nữ, năm nào vào ngày lễ tình nhân cũng vắt óc nghĩ đủ mọi cách để mang lại bất ngờ mới cho mẹ Kỷ.",
    # 043
    "Mẹ Kỷ thì năm nào cũng cười toe toét không khép được miệng, chỉ khổ cho Kỷ Vân Hy và Kỷ Cảnh, năm nào cũng phải chứng kiến bọn họ sến súa nhét cơm chó ngập họng, ngấy đến mức nổi hết cả da gà.",
    # 044
    "Có điều sau này Kỷ Cảnh bị nhập hồn trở thành thiếu niên u ám bất hảo, căn bản chẳng thèm để tâm đến ba mẹ Kỷ, khiến Kỷ Vân Hy phải một mình chịu đựng nỗi thống khổ này suốt bao nhiêu năm trời.",
    # 045
    "Ba Kỷ và mẹ Kỷ đang ngồi trong phòng khách, nghe thấy lời hai người nói liền quay đầu nhìn sang,",
    # 046
    "Ba Kỷ: “Về rồi thì mau đi dọn dẹp đi, xuống ăn cơm.”",
    # 047
    "Mẹ Kỷ lại nhìn Kỷ Cảnh thêm vài lần, sau đó bất thình lình đứng dậy, bước đến bên cạnh Kỷ Cảnh, giơ tay lau mồ hôi trên mặt cậu.",
    # 048
    "“Mẹ, mặt con toàn mồ hôi thôi.” Kỷ Cảnh né tránh.",
    # 049
    "Nào ngờ tiếng “mẹ” này khiến mẹ Kỷ sững sờ chết trân tại chỗ, vành mắt lập tức hoe đỏ.",
    # 050
    "“Tiểu Cảnh, dạo này ở trường con có vui không?”",
    # 051
    "Mẹ Kỷ đột nhiên hỏi.",
    # 052
    "Kỷ Cảnh gãi đầu: “Rất tốt ạ.”",
    # 053
    "Mẹ Kỷ nhìn chằm chằm cậu, rồi mỉm cười: “Tốt là được rồi, mẹ vẫn thích bộ dạng này của con hơn.”",
    # 054
    "Không khí bỗng chốc trở nên tĩnh lặng, ba Kỷ khẽ ho một tiếng, cắt ngang sự im ắng lúc này.",
    # 055
    "Kỷ Cảnh ôm lấy mẹ Kỷ một cái, sau đó lên lầu tắm rửa thay quần áo, rồi xuống lầu cùng cả nhà ăn một bữa cơm tối.",
    # 056
    "“Này, ngày mai mày có kế hoạch gì chưa?” Kỷ Vân Hy huých nhẹ Kỷ Cảnh, nhỏ giọng hỏi.",
    # 057
    "Kỷ Cảnh vốn dĩ chẳng có kế hoạch gì, vì cậu căn bản không nhớ ra ngày mai là lễ tình nhân.",
    # 058
    "“Làm gì?” Cậu liếc xéo Kỷ Vân Hy.",
    # 059
    "Kỷ Vân Hy cười nịnh nọt: “Tao biết mày chắc chắn rảnh rỗi không có việc gì làm, hay là đi xem phim với tao đi, tao...”",
    # 060
    "“Xin lỗi nhé, tao có hẹn rồi.”",
    # 061
    "Kỷ Cảnh nhướng mày, cắt ngang lời cô.",
    # 062
    "Kỷ Vân Hy giận dữ, cô trừng mắt nhìn Kỷ Cảnh: “Mày bốc phét, chẳng lẽ mày muốn bảo mày lén lút sau lưng tao có người yêu rồi à?!”",
    # 063
    "“Đúng thế.” Kỷ Cảnh thản nhiên gật đầu coi như chuyện hiển nhiên.",
    # 064
    "“Không thể nào! Tao không tin!” Kỷ Vân Hy như bị sét đánh ngang tai, cô đột nhiên nhận ra mấy hành vi bất thường mấy ngày nay của Kỷ Cảnh, rất có khả năng thật sự có tình hình rồi.",
    # 065
    "Cảm giác cô đơn ập đến khiến cô luống cuống tay chân, chất vấn: “Thế sao vừa nãy mày không nói?”",
    # 066
    "“Bởi vì tao quên mất ngày mai là lễ tình nhân.” Kỷ Cảnh đứng dậy, vỗ vai cô, thấm thía nói: “Cảm ơn bà chị già nhé, tao đi hẹn người ta ngày mai đi chơi đây.”",
    # 067
    "Kỷ Cảnh hài lòng nhìn bóng lưng bị đả kích nặng nề của Kỷ Vân Hy, lười biếng quay về phòng, mở khung chat với Lục Tư Niên ra.",
    # 068
    "【Dịch Nam Nam Nam】: Lục Tư Niên",
    # 069
    "【Dịch Nam Nam Nam】: Lục Tư Niên",
    # 070
    "【Dịch Nam Nam Nam】: Lục Tư Niên",
    # 071
    "...",
    # 072
    "Có lẽ do những tin nhắn dội bom liên tiếp đã tác động đến Lục Tư Niên, lần này không bao lâu sau Lục Tư Niên đã trả lời.",
    # 073
    "【Lục Tư Niên】: Sao thế?",
    # 074
    "Ngón tay Kỷ Cảnh lơ lửng trên màn hình.",
    # 075
    "【Dịch Nam Nam Nam】: Ngày mai là cuối tuần, cùng em ra ngoài đi dạo có được không?",
    # 076
    "【Dịch Nam Nam Nam】: [Mèo con làm nũng.jpg]",
    # 077
    "【Dịch Nam Nam Nam】: Được không mà!",
    # 078
    "【Dịch Nam Nam Nam】: Sao không trả lời em?",
    # 079
    "...",
    # 080
    "Lục Tư Niên nhìn những tin nhắn không ngừng nhảy ra từ phía đối diện, khóe môi mím chặt thành một đường thẳng tắp.",
    # 081
    "Nghi ngờ và mâu thuẫn lởn vởn trong lòng đang va chạm kịch liệt trong dòng suy nghĩ căng thẳng.",
    # 082
    "【Lục Tư Niên】: Xin lỗi, có lẽ tôi không có thời gian.",
    # 083
    "【Dịch Nam Nam Nam】: Ồ.",
    # 084
    "【Dịch Nam Nam Nam】: Vì sao lại không có thời gian?",
    # 085
    "...",
    # 086
    "Kỷ Cảnh đã tranh thủ khoảng thời gian trống chui vào khoang trò chơi đánh xong một ván game rồi, mà bên kia vẫn chưa có hồi âm.",
    # 087
    "Thế là cậu vừa trầm ngâm vừa đứng dậy, lượn sang phòng Kỷ Vân Hy lục lọi càn quét một vòng rồi mới trở về.",
    # 088
    "Cậu cầm đồ vật trong tay, đối diện với chính mình trong gương khẽ cong môi cười.",
    # 089
    "【Dịch Nam Nam Nam】: [Hình ảnh]",
    # 090
    "【Dịch Nam Nam Nam】: [Hình ảnh]",
    # 091
    "【Dịch Nam Nam Nam】: Anh thích bộ nào, ngày mai em mặc bộ đó ra gặp anh có được không?",
    # 092
    "...",
    # 093
    "Lục Tư Niên đã ngồi cứng đờ trước bàn làm việc gần nửa tiếng đồng hồ rồi, anh ngơ ngác nhìn dòng tin nhắn đối phương hỏi anh vì sao không có thời gian, anh không biết nói dối, càng không biết bịa chuyện để lấp liếm.",
    # 094
    "Vô số lý do trào dâng trong đầu, nhưng gõ vào rồi lại xóa đi, chẳng thể gửi đi được.",
    # 095
    "Lục Tư Niên nhận thức rất rõ rằng mình đang lãng phí thời gian, anh nên dứt khoát từ chối, sau đó chặt đứt sự dây dưa tình cảm không nên có này.",
    # 096
    "Thế nhưng anh lại không sao khống chế nổi bản thân cứ mãi suy nghĩ xem nên trả lời thế nào.",
    # 097
    "Tin nhắn mới đột ngột gửi đến khiến anh ngẩn người trong giây lát, theo bản năng bấm mở bức ảnh mới nhất.",
    # 098
    "Đó là một bức ảnh chụp trước gương.",
    # 099
    "Thiếu nữ mặc một chiếc áo hai dây màu đen dây mảnh, cổ áo hơi rộng nửa che nửa hở, nổi bật nhất chính là làn da trắng đến lóa mắt cùng đường xương quai xanh rõ nét.",
    # 100
    "Vạt áo hai dây rất ngắn, quỳ ngồi trên mặt đất cũng chỉ vừa vặn chạm sàn, đôi chân dài thon thẳng tắp mang tất đen, nghiêng một nửa về phía gương.",
    # 101
    "Lục Tư Niên chỉ vừa liếc qua một cái đã không dám nhìn tiếp nữa, anh hoảng loạn gạt sang bức ảnh tiếp theo.",
    # 102
    "Bức tiếp theo là váy ngắn đồng phục học sinh thanh thuần, vẫn cùng một tư thế, nhưng đôi tất đen đã được thay bằng tất trắng cổ ngắn tinh khôi, tạo nên sự tương phản màu sắc rõ rệt so với bức trước.",
    # 103
    "Lục Tư Niên nhìn chằm chằm bức ảnh, yết hầu khẽ lăn lên lộn xuống.",
    # 104
    "Không khí xung quanh bắt đầu trở nên nóng ran.",
    # 105
    "Anh không kìm chế được mà giơ tay lên, cởi chiếc cúc áo cài ở trên cùng cổ áo.",
    # 106
    "Cùng lúc đó, ánh mắt anh tập trung vào đôi chân của Kỷ Cảnh trong bức ảnh thứ hai, ánh mắt trầm xuống như mặt biển sâu thẳm đen kịt.",
    # 107
    "Trên đó chằng chịt những vết bầm tím loang lổ, so với lần trước còn nghiêm trọng hơn không biết bao nhiêu lần.",
    # 108
    "Kỷ Cảnh kiên nhẫn chờ đợi, cậu vốn là đàn ông, cậu hiểu rõ Lục Tư Niên đang nghĩ gì.",
    # 109
    "Người càng cấm dục thì dã thú bị giam giữ trong lòng lại càng điên cuồng bấy nhiêu.",
    # 110
    "Sau đó cậu nhận được câu trả lời của Lục Tư Niên,",
    # 111
    "【Lục Tư Niên】: Chân của em, tại sao lại thành ra thế này.",
    # 112
    "Kỷ Cảnh nhướng mày, bấm mở bức ảnh xem lại, lúc này mới chú ý tới những vết thương trên chân mình.",
    # 113
    "Chậc, cậu quên mất hôm qua vừa lên võ đài đấu tay đôi với người ta trong tiết của Vương Bằng.",
    # 114
    "Kỷ Cảnh nghĩ nửa ngày, vẫn không biết nên lấp liếm thế nào.",
    # 115
    "【Lục Tư Niên】: Có ai đánh em à?",
    # 116
    "Kỷ Cảnh nhìn mấy chữ cuối cùng, đột nhiên nảy ra một ý, cố ý để trôi qua rất lâu rồi mới chậm rì rì trả lời.",
    # 117
    "【Dịch Nam Nam Nam】: ...Vâng",
    # 118
    "Nhắn xong Kỷ Cảnh dứt khoát gửi một tin nhắn thoại, dùng giọng nữ dịu dàng đầy vẻ khó mở lời nói: “Ngại quá, không ngờ anh lại phát hiện ra, em... vốn không muốn nói đâu.”",
    # 119
    "Lục Tư Niên rất nhanh đã trả lời.",
    # 120
    "【Lục Tư Niên】: Là ai.",
    # 121
    "【Dịch Nam Nam Nam】: Ba dượng của em.",
    # 122
    "【Dịch Nam Nam Nam】: Mấy năm trước mẹ tái hôn với một Beta nam mở tiệm tạp hóa, người Beta đó thích uống rượu, nếu mẹ không có nhà, ông ta say rượu sẽ đánh em.",
    # 123
    "【Dịch Nam Nam Nam】: Anh đừng giận, em không cố ý lừa anh đâu.",
    # 124
    "...",
    # 125
    "Hai mươi phút sau,",
    # 126
    "【Lục Tư Niên】: Tôi biết rồi.",
    # 127
    "Năm phút sau,",
    # 128
    "【Lục Tư Niên】: Dịch Nam, em thực sự là em gái của Kỷ Cảnh sao."
]

content = "\n\n".join(paras) + "\n"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written {len(paras)} paras to {target_path}")
