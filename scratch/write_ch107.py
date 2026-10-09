# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_107\translation.md"

paras = [
    # 000
    "“Tao, tao, Kỷ Cảnh mày... Lục Tư Niên...”",
    # 001
    "Kỷ Vân Hy ngôn ngữ hỗn loạn, tay chân múa may loạn xạ, chỉ trỏ vào Lục Tư Niên, một bộ dạng như vừa nhìn thấy ma quỷ ban ngày.",
    # 002
    "Cô vừa nhìn thấy cái gì thế này?",
    # 003
    "Kỷ Cảnh đang hôn môi với Lục Tư Niên sao?!",
    # 004
    "Bị Kỷ Vân Hy cắt ngang như vậy, Kỷ Cảnh từ trong cơn tức giận vừa rồi dần dần bình tĩnh trở lại, cậu hít sâu hai hơi, kéo cà vạt của Lục Tư Niên ôm tên sâu rượu vào lòng.",
    # 005
    "“Về nhà rồi tao nói cho mày sau.”",
    # 006
    "Kỷ Cảnh nửa ôm nửa đỡ Lục Tư Niên, dắt người bước về phía trước.",
    # 007
    "Kỷ Vân Hy vẫn còn đang đờ đẫn tại chỗ, ánh mắt ngơ ngác nhìn theo hướng Kỷ Cảnh đi.",
    # 008
    "Lúc đi ngang qua mặt Kỷ Vân Hy, cô mới hoàn hồn lại, nói: “Ba mẹ bảo tao đi tìm mày, tối nay ba mẹ ở lại đây nghỉ qua đêm, hỏi hai đứa mình có muốn về nhà không.”",
    # 009
    "“Mày tùy ý đi, tao về muộn một chút.”",
    # 010
    "Kỷ Cảnh đỡ Lục Tư Niên đi ra ngoài.",
    # 011
    "Dù sao Lục Tư Niên cũng cao lớn vạm vỡ như một Alpha, khá là nặng, may mà lúc say rượu anh cũng hệt như ngày thường, trầm mặc ít lời, mặt vùi vào vai Kỷ Cảnh, vô cùng phối hợp.",
    # 012
    "Kỷ Vân Hy nhìn chằm chằm vào đôi môi của Lục Tư Niên sắp chạm vào cổ Kỷ Cảnh, hít sâu một hơi, vội vàng rảo bước đuổi theo vài bước:",
    # 013
    "“Thế bây giờ mày định đi đâu đấy?”",
    # 014
    "“Đưa anh ta về nhà anh ta.”",
    # 015
    "Kỷ Cảnh liếc nhìn Lục Tư Niên đang tựa trên vai mình, ra hiệu.",
    # 016
    "Kỷ Vân Hy bừng tỉnh đại ngộ: “Về nhà anh ta? Ngay cả nhà anh ta ở đâu mày cũng biết, không đúng, chẳng lẽ lần trước mày nấu canh gừng chính là ở nhà anh ta sao...”",
    # 017
    "Kỷ Cảnh không thèm đếm xỉa tới cô, coi như ngầm thừa nhận.",
    # 018
    "May mắn là lúc này buổi tiệc mới diễn ra được một nửa, phần lớn mọi người đều tụ tập trong đại sảnh chính, nên hành động của Kỷ Cảnh và Lục Tư Niên không thu hút sự chú ý của ai.",
    # 019
    "Kỷ Vân Hy giúp Kỷ Cảnh gọi một chiếc xe, sau đó nhìn Kỷ Cảnh đỡ Lục Tư Niên lên xe.",
    # 020
    "“Tối nay mày nhất định phải về nhà đấy nhé.” Kỷ Vân Hy ân cần dặn dò, vẻ mặt tựa như người mẹ đang khuyên nhủ cô con gái sắp sửa qua đêm ở nhà bạn trai vậy.",
    # 021
    "Kỷ Cảnh ậm ừ qua loa một tiếng, rồi đọc địa chỉ nhà của Lục Tư Niên.",
    # 022
    "Đợi đến khi cậu vác được Lục Tư Niên về đến nhà anh thì đã gần mười giờ đêm rồi.",
    # 023
    "Ném Lục Tư Niên lên ghế sofa, Kỷ Cảnh cũng thuận thế dựa vào sofa nghỉ ngơi một lát.",
    # 024
    "Cậu tiện tay giật chiếc cà vạt âu phục của mình ra, cởi hai chiếc cúc áo trên cùng cho thoáng khí.",
    # 025
    "Sau đó cậu liếc nhìn Lục Tư Niên, đại phát từ bi cởi giày giúp anh.",
    # 026
    "“Này, Lục Tư Niên, tôi về đây nhé.”",
    # 027
    "Cậu cúi người, vỗ vỗ lên mặt Lục Tư Niên, còn thuận tay sờ thử trán anh một cái.",
    # 028
    "Người ta thường nói cồn có thể giải phóng những dục vọng chôn giấu tận đáy lòng con người, kẻ ngụy quân tử sẽ để lộ bản chất tà ác bên trong, kẻ giả vờ vui vẻ sẽ ôm đầu khóc nức nở, vậy thì đối với Lục Tư Niên mà nói, ranh giới đạo đức mà ngày thường anh tự đặt ra cho mình đã hoàn toàn tan biến dưới sự ăn mòn của men rượu.",
    # 029
    "Tiềm thức của anh khiến cảnh tượng này trùng khớp với buổi tối cách đây không lâu.",
    # 030
    "Khi ấy Dịch Nam quỳ gối trên giường, lòng bàn tay cũng dịu dàng áp lên trán anh như thế này, hệt như cái vuốt ve ấm áp của người mẹ hồi nhỏ.",
    # 031
    "Sau đó anh kéo Dịch Nam xuống, đè lên giường hôn ngấu nghiến.",
    # 032
    "Rồi sau đó nữa...",
    # 033
    "Đôi mắt mơ màng của Lục Tư Niên bỗng nhiên mở to, nơi đáy mắt in bóng gương mặt của Kỷ Cảnh.",
    # 034
    "Chiếc cà vạt của Kỷ Cảnh bị Lục Tư Niên dùng sức kéo mạnh xuống, cậu mất thăng bằng ngã nhào xuống dưới, vào giây cuối cùng kịp dùng khuỷu tay chống lên mặt sofa.",
    # 035
    "Đúng lúc này, Lục Tư Niên ngửa đầu lên, dùng môi chặn kín đôi môi của Kỷ Cảnh.",
    # 036
    "Nụ hôn của Lục Tư Niên ập đến đầy khí thế hung hãn mãnh liệt, thứ tình cảm ngày thường bị kìm nén gông cùm nay điên cuồng phá xiềng xích tràn ra, anh siết chặt lấy eo Kỷ Cảnh, dùng sức lật người đè cậu dưới thân.",
    # 037
    "Bản năng Alpha khiến Kỷ Cảnh vô cớ nổi giận, cảm giác bị người khác cưỡng ép áp chế hoàn toàn đi ngược lại thiên tính của Alpha,",
    # 038
    "Ngày thường cậu khoác lên lớp vỏ Dịch Nam thì nhẫn nhịn cho qua, nhưng hiện tại cậu căn bản không có lý do gì phải nhường nhịn Lục Tư Niên.",
    # 039
    "Cậu dùng đầu gối thúc mạnh vào bụng Lục Tư Niên, Lục Tư Niên rên khẽ một tiếng, động tác chậm lại.",
    # 040
    "Kỷ Cảnh thuận thế lật người lên trên, hai người ôm chặt lấy nhau lăn lông lốc từ trên sofa rơi xuống sàn nhà.",
    # 041
    "Lục Tư Niên cũng bị sự phản kháng của Kỷ Cảnh khơi dậy ham muốn chinh phục, anh nắm chặt cổ tay Kỷ Cảnh muốn đè lên đỉnh đầu, lại bị Kỷ Cảnh tung một cú thúc khuỷu tay làm suy giảm lực đạo.",
    # 042
    "Hai người hệt như đang đánh nhau trên sàn nhà lặng lẽ vật lộn qua lại, thế công của Lục Tư Niên rất mãnh liệt, đánh một hồi khiến Kỷ Cảnh tức giận nghẹn ứ nơi lồng ngực, mắt híp lại, hướng về phía Lục Tư Niên phóng thích tin tức tố Alpha.",
    # 043
    "Lục Tư Niên dường như không ngờ Kỷ Cảnh lại chơi xấu, thoạt đầu anh trừng mắt nhìn Kỷ Cảnh, sau đó toàn thân bỗng mềm nhũn ra, buông lỏng cổ tay Kỷ Cảnh.",
    # 044
    "Vành tai vốn đang đỏ ửng vì men rượu nay lại càng thêm đỏ rực, đỏ đến mức sắp nhỏ máu ra ngoài.",
    # 045
    "“Lục Tư Niên, không phải ai cũng nói lý lẽ với anh đâu.”",
    # 046
    "Kỷ Cảnh nhếch môi cười, trong chớp mắt đã hoán đổi lại vị trí của hai người.",
    # 047
    "Cậu cúi đầu, một ngụm cắn rách môi dưới của Lục Tư Niên, nhìn giọt máu đỏ tươi đọng lại nơi khóe môi anh.",
    # 048
    "“Anh nhìn cho rõ, tôi không phải Dịch Nam.”",
    # 049
    "Kỷ Cảnh bóp chặt cằm Lục Tư Niên, ép anh phải nhìn thẳng vào gương mặt của mình.",
    # 050
    "“Nói cho tôi biết, anh thích ai.”",
    # 051
    "Còn Lục Tư Niên nhìn chằm chằm gương mặt cậu, dần dần rơi vào thất thần.",
    # 052
    "“Thích em.” Anh khàn giọng nói.",
    # 053
    "Nói xong tựa như không nghe thấy gì ngẩng đầu lên, một lần nữa hôn lên môi Kỷ Cảnh.",
    # 054
    "Kỷ Cảnh tức đến mức sắp nổ tung lồng ngực.",
    # 055
    "Lục Tư Niên hệt như một quả bầu rỗng ngơ ngác, cậu mẹ nó đã nói bao nhiêu lần rằng cậu không phải Dịch Nam không phải Dịch Nam rồi, sao cái tên ngốc này cứ không chịu hiểu chứ.",
    # 056
    "Ánh mắt này không phải đang nhìn Dịch Nam thì là đang nhìn ai cơ chứ?",
    # 057
    "【Ting tong, kịch bản yêu đương phản diện đang cập nhật, xin vui lòng đợi giây lát.】",
    # 058
    "【Oa! Thật sự là quá đáng lắm luôn á, sao anh ta có thể coi người như một người phụ nữ được chứ?! Người chính là Alpha A nhất toàn Đế quốc cơ mà, chẳng lẽ một người xuất chúng như người trong lòng anh ta còn không bằng một nữ Beta do người bịa đặt ra sao?! Người tức giận tột cùng, người nhất định phải cho anh ta biết người là ai, phải cho anh ta hiểu hậu quả của việc nhìn nhầm người! Người lật người đè anh ta dưới thân... hướng về phía tuyến thể sau gáy kia, hung hăng cắn mạnh xuống...】",
    # 059
    "【Ký chủ, xin hãy diễn xuất theo đại cương cốt truyện này nha~】",
    # 060
    "Âm thanh thông báo của hệ thống vang lên bên tai Kỷ Cảnh.",
    # 061
    "Kỷ Cảnh đang trong trạng thái thịnh nộ tột cùng, chửi thầm trong lòng: “Cốt truyện quỷ quái gì thế này, thế này chẳng phải bảo tao đánh dấu anh ta sao!”",
    # 062
    "Mật Bảo rụt rè nép vào góc, yếu ớt bảo đây là nhiệm vụ bắt buộc phải hoàn thành.",
    # 063
    "Kỷ Cảnh hít sâu một hơi, kéo giật đôi môi đang bám riết không buông của Lục Tư Niên ra,",
    # 064
    "“Lục Tư Niên, tại sao lại thích Dịch Nam?”",
    # 065
    "Cậu gắng gượng duy trì sự bình tĩnh, cất tiếng hỏi.",
    # 066
    "Trên môi Lục Tư Niên vẫn còn vương một vệt máu đỏ tươi, con ngươi sâu thẳm nhìn chăm chú vào Kỷ Cảnh, hồi lâu sau anh mới nói: “Em đối với tôi, rất khác biệt.”",
    # 067
    "Đại từ nhân xưng Lục Tư Niên dùng vẫn là “em”, anh vẫn coi cậu là Dịch Nam.",
    # 068
    "Kỷ Cảnh bật ra một tiếng cười lạnh nơi cuống họng, ngay khoảnh khắc tiếp theo, ánh mắt cậu lạnh như băng, túm lấy Lục Tư Niên lật người anh lại, rồi cúi người đè nghiến lên lưng anh.",
    # 069
    "“Được thôi, anh thích, tôi ngược lại muốn xem xem anh thích cô ta đến mức nào.”",
    # 070
    "Cậu thì thầm bên tai Lục Tư Niên.",
    # 071
    "“Lục Tư Niên, anh là một Omega.” Cậu dùng giọng điệu trần thuật lạnh lùng thốt lên.",
    # 072
    "Lục Tư Niên giãy giụa một lát, nghe vậy đột nhiên từ bỏ, như thể ngầm thừa nhận lời cậu nói.",
    # 073
    "Kỷ Cảnh rũ mi mắt, sau đó thô bạo kéo tụt cổ áo sơ mi phía sau của anh xuống, không khí lạnh lẽo phả vào, gáy của Lục Tư Niên cứ thế bại lộ hoàn toàn trước mắt cậu.",
    # 074
    "Lục Tư Niên như ý thức được điều gì, trở tay nắm chặt lấy cổ tay Kỷ Cảnh, gân xanh nổi cộm cuồn cuộn.",
    # 075
    "“Chẳng phải anh thích em sao,” Kỷ Cảnh đột nhiên chuyển sang giọng nữ, khẽ thì thầm bên tai anh.",
    # 076
    "“Lục Tư Niên, để em cắn tuyến thể của anh nhé, có được không? Chỉ một cái thôi.”",
    # 077
    "Kỷ Cảnh dùng giọng điệu thường ngày của Dịch Nam, bình thản nói hết câu này.",
    # 078
    "Cậu nhìn chằm chằm vào sau gáy Lục Tư Niên, nơi đó có một khối phồng nhô lên không quá rõ ràng, cậu đột nhiên cảm thấy khô họng khát nước, cậu cảm thấy khối phồng này sau khi bị cắn rách sẽ trào ra dòng nước ngọt ngào thơm mát.",
    # 079
    "“Chỉ cắn một miếng thôi mà, sao thế, hôm đó em bị anh hành hạ như vậy, để em cắn một miếng cũng không được sao?”",
    # 080
    "Kỷ Cảnh vừa dụ dỗ anh, vừa kiên nhẫn chờ đợi phản ứng của Lục Tư Niên.",
    # 081
    "Cậu biết đây là vùng cấm kỵ bất khả xâm phạm của Lục Tư Niên.",
    # 082
    "Cậu nhìn thấy trên mu bàn tay Lục Tư Niên đang nắm chặt tay cậu nổi đầy gân xanh chằng chịt, từng đường gân đều gào thét sự cự tuyệt kháng cự của anh.",
    # 083
    "Thế nhưng Kỷ Cảnh chẳng hiểu vì sao, không những không thất vọng mà còn có vài phần may mắn nhẹ nhõm.",
    # 084
    "“Thôi bỏ đi, xem ra sự thích của anh cũng...” Cậu sảng khoái nói, vốn định buông tay, lại phát hiện Lục Tư Niên đột nhiên buông xuôi sức lực, áp trán xuống sàn nhà, sau gáy cứ thế ngoan ngoãn phơi bày trước mắt Kỷ Cảnh.",
    # 085
    "Kỷ Cảnh sững sờ chết trân.",
    # 086
    "Tuyến thể của Lục Tư Niên cách môi cậu chỉ vỏn vẹn một centimet, chỉ cần cậu khẽ cúi đầu xuống là có thể tùy ý cắn rách, cắn nát nó một cách dễ dàng.",
    # 087
    "Yết hầu chậm chạp nuốt ực một ngụm.",
    # 088
    "Kỷ Cảnh đột nhiên nở nụ cười đầy ẩn ý khó hiểu, sau đó rời khỏi người Lục Tư Niên đứng dậy.",
    # 089
    "“Xem ra, anh thật sự rất thích Dịch Nam.”",
    # 090
    "Cậu nói.",
    # 091
    "“Cứ thế đi, tôi đi đây.”",
    # 092
    "Một tay cậu vơ lấy chiếc áo khoác âu phục trên sofa, lạnh nhạt buông lại một câu “Tôi đi đây”, rồi cất bước rời khỏi nhà của Lục Tư Niên.",
    # 093
    "...",
    # 094
    "“Nói đi, phần này tao không diễn thì có hình phạt gì không.”",
    # 095
    "Kỷ Cảnh vừa sải bước trên đường về nhà vừa cất tiếng hỏi hệ thống.",
    # 096
    "【Hức... thực ra, thực ra không có hình phạt gì đâu á】",
    # 097
    "Con bướm bảy sắc cầu vồng thấp thỏm chọt chọt ngón tay vào nhau.",
    # 098
    "【Hệ thống bọn tui đều là hệ thống vô cùng nhân đạo, tuyệt đối sẽ không làm tổn thương bất kỳ ký chủ nào đâu, trước đây không nói cho ký chủ là sợ ký chủ biết rồi sẽ không chịu làm nhiệm vụ nữa...】",
    # 099
    "Như vậy thì chỉ tiêu KPI của nó sẽ gặp vấn đề lớn mất.",
    # 100
    "Mật Bảo âm thầm rơi nước mắt.",
    # 101
    "【Vừa nãy sao ký chủ không cắn đi, cắn một cái là người hoàn thành nhiệm vụ rồi mà】",
    # 102
    "Mật Bảo thực sự không nghĩ thông được nguyên nhân trong đó, tình cảm của con người đối với nó quả thực quá đỗi phức tạp.",
    # 103
    "Kỷ Cảnh không trả lời nó, mà hỏi ngược lại: “Hiện tại tiến độ đến đâu rồi?”",
    # 104
    "【Báo cáo ký chủ, hiện tại tiến độ đã đạt mốc 70% rồi nha!】",
    # 105
    "Lúc Kỷ Cảnh về đến nhà thì đèn trong nhà vẫn sáng trưng, mở cửa bước vào, quả nhiên không ngoài dự đoán, Kỷ Vân Hy đang khoanh tay đứng ở huyền quan với tư thế của một bậc phụ huynh chuẩn bị hỏi tội.",
    # 106
    "“Nói đi, mày với Lục Tư Niên rốt cuộc là có chuyện gì thế hả.”",
    # 107
    "Kỷ Cảnh từ nhỏ đến lớn vốn chẳng giấu giếm Kỷ Vân Hy điều gì, Kỷ Vân Hy cũng vậy, cho nên cậu không cần thiết phải giấu diếm cô.",
    # 108
    "Cậu lược bỏ đi sự tồn tại của hệ thống, chỉ bảo rằng mình thích Lục Tư Niên, nên cố tình bịa ra thân phận nữ Beta để theo đuổi Lục Tư Niên.",
    # 109
    "Kỷ Vân Hy sau khi nghe hết đầu đuôi câu chuyện, mặt nạ dưỡng da trên mặt rớt luôn xuống đất:",
    # 110
    "“Cái gì cơ?! Mày lừa anh ta mày là con gái, lại còn là con gái riêng của nhà họ Kỷ á?!”",
    # 111
    "Kỷ Vân Hy hét toáng lên: “Ba của chúng ta là một người đàn ông thật thà chất phác như thế mà bị mày bôi đen thành ra cái dạng gì thế này hả!”",
    # 112
    "Cô cuối cùng cũng hiểu vì sao Kỷ Cảnh chốc chốc lại giả trang thành con gái, lại còn luôn hỏi cô mấy câu hỏi kỳ quặc chẳng hiểu ra sao.",
    # 113
    "Khá lắm, em trai cô tiền đồ quá rồi, không những lừa được con cưng của trời Lục Tư Niên, mà còn khiến đối phương một lòng một dạ say đắm yêu cậu.",
    # 114
    "Đó là Lục Tư Niên đấy!",
    # 115
    "Kỷ Cảnh day day giữa hai hàng lông mày, cậu cũng biết chuỗi hành vi của mình kinh thế hãi tục đến mức nào.",
    # 116
    "“Mày đừng có ở đây gào toáng lên nữa, qua một khoảng thời gian nữa tao sẽ chia tay với Lục Tư Niên.”",
    # 117
    "Kỷ Cảnh bình thản nói.",
    # 118
    "Đợi cậu hoàn thành xong tiến độ, chỉ còn lại 10% nữa thôi, chẳng bao lâu nữa đâu.",
    # 119
    "Nào ngờ điều này lại khiến giọng Kỷ Vân Hy càng gào to hơn: “Hả? Mày muốn chia tay với anh ta?”",
    # 120
    "Kỷ Vân Hy nghẹn họng tựa như vừa nuốt phải thứ gì đó khó nuốt không nói nên lời: “Em trai à, mày có thấy Lục Tư Niên trong cả chuyện này vô cùng vô tội không, hơn nữa, còn rất đáng thương nữa... Đương nhiên tao không bảo là mày không thể chia tay với anh ta, tao chỉ có chút... được rồi, tao đồng cảm thương xót anh ta...”",
    # 121
    "Bất kỳ ai bị đem ra đùa giỡn tình cảm như vậy cũng không chịu nổi, huống chi lời nói dối này lại hoang đường đến tột cùng.",
    # 122
    "Kỷ Cảnh không phải không hiểu ý của Kỷ Vân Hy,",
    # 123
    "“Cho dù tao không chia tay với anh ta, anh ta cũng không thể chấp nhận nổi sự thật, rốt cuộc thì cũng sẽ chia tay với tao thôi.” Kỷ Cảnh rũ mi mắt, Kỷ Vân Hy không nhìn thấy nỗi ảm đạm nơi đáy mắt cậu.",
    # 124
    "“Lỡ như anh ta có thể chấp nhận thì sao?” Kỷ Vân Hy buột miệng thốt ra, sau đó cũng biết ý nghĩ này quá mức hoang đường, thiếu tự tin nuốt ngược lời vào trong.",
    # 125
    "“Không thể nào đâu.” Kỷ Cảnh nói.",
    # 126
    "Lục Tư Niên thích “Dịch Nam”, mà Kỷ Cảnh hiểu rõ, Dịch Nam này là được may đo riêng cho Lục Tư Niên, hoàn toàn không có bất kỳ quan hệ nào với chính bản thân cậu cả.",
    # 127
    "Lời tác giả muốn nói:",
    # 128
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-20 23:12:09~2023-05-21 22:27:28 nha~",
    # 129
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: Sơn Mộc Liệt 3 bình; 60031160, Y, Triều Ca 1 bình;",
    # 130
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 107: Mềm lòng và làm lành\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_107 translation successfully.")
