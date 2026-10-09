import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

trans_paras = [
    # 000
    "Hôm thứ Ba do Kỷ Cảnh bất cẩn ngủ dậy muộn, dẫn đến việc khi cậu vội vã chạy tới phòng học thì tiết học đã trôi qua được gần một nửa.",
    # 001
    "Cậu tiện tay vuốt lại mái tóc dài chưa kịp chải chuốt vì vội vàng, lặng lẽ bước vào từ cửa sau.",
    # 002
    "Cậu đâu hay biết cảnh tượng này đã lọt vào tầm mắt của biết bao nhiêu con người.",
    # 003
    "Thiếu nữ dáng người cao ráo ngược ánh nắng bước vào, làn da trắng phát sáng, mái tóc dài óng ả như suối thác luồn qua kẽ tay, dường như người xung quanh còn có thể ngửi thấy mùi hương thanh nhã thoang thoảng theo từng bước chân của cô.",
    # 004
    "Có Alpha không kìm được mà hít sâu một hơi kinh ngạc.",
    # 005
    "“Đẹp quá đi mất…”",
    # 006
    "Tiếng trầm trồ tán thán này đã đánh thức vô số người đang ngẩn ngơ chết trân.",
    # 007
    "“Sao lại là cô ta nữa thế, đây đã là tuần thứ ba liên tiếp tới học ké rồi đấy, chẳng biết là tới nghe giảng thật hay là tới để quyến rũ đàn ông nữa.”",
    # 008
    "Có một Omega nghe thấy vậy liền đảo mắt khinh bỉ, chua ngoa hạ giọng nói.",
    # 009
    "“Ai bảo không phải chứ, có ai giống cô ta chân cẳng toàn là vết thương bầm tím mà vẫn mặc váy ngắn phơi ra cho thiên hạ ngắm, sợ người ta không biết những vết thương trên chân là do bị người ta làm trò trên giường tạo ra chắc?”",
    # 010
    "“Đúng vậy, hơn nữa cậu có để ý không, hôm nay vết thương trên chân cô ta trông còn kinh khủng hơn, nhìn thôi đã thấy đau rồi, đêm qua chắc là bị giày vò thảm hại lắm đây.”",
    # 011
    "Lại có một nữ Beta phụ họa theo.",
    # 012
    "Mấy cậu Alpha ngồi gần đó nghe không lọt tai nữa, bèn nhịn không được mà phản bác lại: “Này, các cậu đặt điều bôi nhọ một Omega như thế không hay chút nào đâu nhé?”",
    # 013
    "“Ai bảo cô ta là Omega chứ? Tôi dám cá chắc chắn cô ta là một Beta, hơn nữa còn là một Beta nghèo kiết xác hám giàu muốn câu dẫn thiếu gia nhà giàu, chỉ có Beta mới cố tình đeo choker giả vờ mình có tuyến thể Omega để thả thính Alpha thôi, thực tế Omega bây giờ người ta bỏ đeo từ lâu rồi.” Cậu chàng Omega nọ cười khẩy mỉa mai.",
    # 014
    "Mấy người bọn họ nói chuyện không hề nhỏ tiếng, chẳng những bị Kỷ Cảnh nghe thấy trọn vẹn, mà Lục Tư Niên đứng trên bục giảng cũng dừng lại bài giảng của mình.",
    # 015
    "“Xin đừng thảo luận những việc không liên quan đến bài học, nếu không xin hãy tự giác ra ngoài.”",
    # 016
    "Lục Tư Niên lạnh lùng quét mắt qua khu vực hàng ghế giữa và sau của lớp học, ngón tay gõ nhẹ lên bảng điện tử nhắc nhở.",
    # 017
    "Nói xong ánh mắt anh lướt qua góc phòng học một cái, hàng chân mày khẽ nhíu lại một thoáng khó nhận ra, rồi tiếp tục giảng bài.",
    # 018
    "Mấy người vừa nói chuyện bị Lục Tư Niên dọa cho một phen khiếp vía, vội vàng ngậm miệng giả câm giả điếc, bọn họ biết Lục Tư Niên tuy nghiêm khắc, nhưng trước giờ chưa bao giờ thẳng thừng đuổi sinh viên ra khỏi phòng học, điều này chứng tỏ Lục Tư Niên thực sự đã nổi giận.",
    # 019
    "Kỷ Cảnh chứng kiến cảnh tượng này, chẳng thèm để tâm chút nào mà còn duỗi dài đôi chân ra, hận không thể để bọn họ nhìn cho rõ ràng hơn.",
    # 020
    "Quần áo cậu mặc đều là đồ mua sỉ giá rẻ trên Tinh Võng, bởi vì theo thiết lập nhân vật của mình, cậu tuyệt đối không thể mặc đồ của Kỷ Vân Hy được, phải biết rằng bất kỳ món đồ nào của Kỷ Vân Hy giá cả cũng đều đắt đến mức dọa chết người, một “đứa con gái riêng nhà họ Kỷ”, “con gái của cô lao công” như cậu chắc chắn không thể nào mua nổi.",
    # 021
    "Cậu cúi đầu liếc nhìn đôi chân của mình, ngắm nhìn những vết thương “thảm thiết” bên trên.",
    # 022
    "Thứ Hai hàng tuần đều là lúc cường độ huấn luyện thực chiến của Vương Bằng khắc nghiệt nhất, Alpha va chạm bầm dập gãy tay gãy chân là chuyện cơm bữa, cậu làm sao để ý tới mấy vết thương vặt vãnh này chứ? Mặc dù nhìn qua thì đúng là trông thê thảm hơn tuần trước thật.",
    # 023
    "Đến giờ giải lao giữa tiết, Kỷ Cảnh nhìn về phía Lục Tư Niên trên bục giảng, nhìn anh cầm chiếc bình giữ nhiệt không biết đã dùng bao nhiêu năm lên uống nước, yết hầu theo đó chuyển động trồi sụt.",
    # 024
    "Ánh mắt Kỷ Cảnh khẽ ngưng lại, cậu giơ thiết bị đầu cuối lên tách một tiếng chụp lấy một bức ảnh của Lục Tư Niên, sau đó mở khung trò chuyện với anh, gửi sang.",
    # 025
    "【Dịch Nam Nam Nam】: [Hình ảnh].",
    # 026
    "Mấy ngày không tới lớp này, hễ rảnh rỗi là Kỷ Cảnh lại nhắn tin cho Lục Tư Niên, nhưng phần lớn đều không nhận được hồi âm, ngoại trừ những câu hỏi học thuật mà cậu giả vờ đưa ra.",
    # 027
    "Đầu bên kia Lục Tư Niên khựng lại động tác uống nước một nhịp, dường như là đã nhìn thấy tin nhắn trên thiết bị đầu cuối.",
    # 028
    "Kỷ Cảnh ngước mắt lên, vừa vặn chạm phải ánh nhìn Lục Tư Niên phóng tới, khóe mắt cậu cong lên nở một nụ cười rạng rỡ.",
    # 029
    "Lục Tư Niên căng cứng mặt mày, cúi đầu gõ chữ.",
    # 030
    "【Lục Tư Niên】: ?",
    # 031
    "【Dịch Nam Nam Nam】: Chụp lén chú đấy.",
    # 032
    "Lục Tư Niên rõ ràng là chẳng biết nên nói gì, người đàn ông mặt không cảm xúc trên bục giảng kia lại bị Kỷ Cảnh nhìn ra vài phần lúng túng mất tự nhiên.",
    # 033
    "Mãi một lúc lâu sau, trước khi tiếng chuông vào lớp vang lên, Kỷ Cảnh mới nhận được tin nhắn Lục Tư Niên gửi tới:",
    # 034
    "【Lục Tư Niên】: Tan học tìm tôi một chút.",
    # 035
    "Kỷ Cảnh nhìn dòng tin nhắn này, ánh mắt bỗng trở nên sâu thẳm đầy ẩn ý.",
    # 036
    "Lúc tan học, Kỷ Cảnh đợi Lục Tư Niên bước ra khỏi lớp rồi mới từ cửa sau rảo bước bám theo.",
    # 037
    "“Đại thúc, chú tìm em có việc gì thế ạ?” Kỷ Cảnh vừa rảo bước đuổi kịp Lục Tư Niên, vừa ghé sát tai anh khẽ thì thầm.",
    # 038
    "“Ừm.” Lục Tư Niên bước dịch sang bên cạnh một bước, giữ khoảng cách với cô mà không để lộ dấu vết.",
    # 039
    "Kỷ Cảnh thầm bĩu môi吐槽 trong lòng, im lặng bám theo Lục Tư Niên rẽ vào một tòa nhà vắng vẻ.",
    # 040
    "Tòa nhà này là khu văn phòng làm việc của Học viện Quân sự Đế quốc.",
    # 041
    "Lục Tư Niên dẫn cậu đến văn phòng làm gì nhỉ?",
    # 042
    "Sau khi quét mống mắt thành công, hai người bước vào một phòng làm việc rộng rãi và ngăn nắp.",
    # 043
    "Lục Tư Niên thuần thục xếp gọn giáo án cất vào ngăn kéo bàn làm việc, lại lấy ra một tập tài liệu viết gì đó.",
    # 044
    "Kỷ Cảnh đưa mắt nhìn quanh văn phòng một lượt, phát hiện nơi này sạch sẽ đến mức đáng sợ, ngay cả chiếc gối tựa trên ghế sofa nhỏ cũng được xếp đặt cùng một góc độ như được lập trình sẵn, Lục Tư Niên chắc chắn là mắc chứng ám ảnh cưỡng chế, Kỷ Cảnh thầm rủa.",
    # 045
    "“Một ngày hai lần, thoa đều ra, nếu không bị va chạm thêm thì hai ngày là tan vết bầm.”",
    # 046
    "Giọng nói của Lục Tư Niên kéo suy nghĩ của Kỷ Cảnh quay trở lại, cậu quay đầu nhìn anh, phát hiện Lục Tư Niên chẳng biết từ lúc nào đã lấy ra một hộp thuốc mỡ từ trong ngăn kéo, những ngón tay thon dài rõ khớp đẩy hộp thuốc tới trước mặt cậu.",
    # 047
    "Kỷ Cảnh phản ứng mất một lúc, mới nhận ra Lục Tư Niên đang nói tới những vết thương trên chân mình.",
    # 048
    "Không nói rõ được là cảm giác gì, nhưng khoảnh khắc này lồng ngực cậu bỗng có chút nghẹn lại, cậu nhìn thẳng vào mắt Lục Tư Niên, thế nhưng Lục Tư Niên lại có phần gượng gạo tránh đi ánh mắt của cậu.",
    # 049
    "Kỷ Cảnh nhếch môi cười: “Không sao đâu đại thúc, chỉ là ngã thôi mà, nhanh khỏi lắm….”",
    # 050
    "“Vết thương này của em là do ẩu đả đánh nhau.” Lục Tư Niên đột ngột cắt ngang lời cậu.",
    # 051
    "Kỷ Cảnh giật mình, nhất thời chẳng biết phải phản bác ra sao, cậu biết giải thích thế nào về việc một nữ Beta yếu đuối trên người lại toàn là vết thương do ẩu đả chứ?",
    # 052
    "Cậu đâu biết rằng màn biểu cảm này rơi vào mắt Lục Tư Niên, lại chính là sự khó xử nghẹn ngào muốn nói lại thôi của thiếu nữ.",
    # 053
    "Bầu không khí giằng co một lúc, cuối cùng bị tiếng bụng réo ùng ục của Kỷ Cảnh phá vỡ.",
    # 054
    "Kỷ Cảnh khẽ thở phào nhẹ nhõm, dưới ánh mắt kinh ngạc của Lục Tư Niên đưa tay ôm lấy bụng mình: “Đại thúc, em đói quá rồi, chúng ta đi ăn cơm đi.”",
    # 055
    "Lục Tư Niên nghe vậy lại theo bản năng mím chặt đôi môi mỏng, lộ ra vẻ mặt nghiêm nghị.",
    # 056
    "“Em đến bữa sáng còn chưa được ăn nữa nè, đói lả cả người rồi, lần này để em mời chú ăn ở căng tin nhé, coi như cảm ơn chú lần trước đã cứu em, có được không ạ?” Kỷ Cảnh trực tiếp tiến lên nắm lấy tay Lục Tư Niên, cố tình dùng giọng điệu làm nũng khẩn cầu.",
    # 057
    "Lục Tư Niên phản ứng rất mạnh, giật tay ra khỏi tay Kỷ Cảnh, khuôn mặt càng thêm căng cứng.",
    # 058
    "Thiếu nữ trước mặt dường như có chút hụt hẫng, dùng ánh mắt vô tội nhìn anh.",
    # 059
    "Anh bỗng thấy có chút áy náy bực bội, nhưng lại chẳng rõ nguyên do vì đâu, cuối cùng như ma xui quỷ khiến mà thốt ra một chữ: “Được.”",
    # 060
    "Ở nơi góc tối không ai để ý, vành tai Lục Tư Niên bỗng ửng lên một vệt hồng nhạt.",
    # 061
    "Giáo sư của trường quân sự Đế quốc có nhà ăn chuyên dụng riêng cho cán bộ giảng viên, Lục Tư Niên liền dẫn Kỷ Cảnh tới nhà ăn giáo viên.",
    # 062
    "Kỷ Cảnh thực ra rất hiếm khi ăn ở căng tin trường, cơ bản toàn ra ngoài ăn sơn hào hải vị, nhưng Lục Tư Niên thì gần như cả ba bữa đều giải quyết tại trường học.",
    # 063
    "Nhìn vào thực đơn, Kỷ Cảnh khó hiểu nhìn Lục Tư Niên một cái.",
    # 064
    "“Đại thúc chú cứ gọi thoải mái đi, em có thẻ… à không, em có thẻ cơm của mẹ em.” Kỷ Cảnh hào phóng nói.",
    # 065
    "Lục Tư Niên không nói gì, chỉ đợi sau khi Kỷ Cảnh đắn đo gọi món xong thì chuyển thực đơn cho người máy phục vụ.",
    # 066
    "“Đại thúc, ngày nào chú cũng ăn cơm ở đây ạ?”",
    # 067
    "“Đại thúc, mỗi ngày ngoài giờ dạy học ra chú còn làm gì nữa không?”",
    # 068
    "“Đại… à không đúng, hình như em không nên gọi chú là đại thúc đâu nhỉ, chú trông rõ ràng trẻ trung thế này mà, chỉ là…”",
    # 069
    "…",
    # 070
    "Suốt bữa ăn, Lục Tư Niên như một quả hồ lô ngâm nước chẳng hé răng nửa lời, còn Kỷ Cảnh thì cứ líu lo tìm đủ mọi chuyện để bắt chuyện.",
    # 071
    "“Lúc ăn cơm không được nói chuyện.”",
    # 072
    "Lục Tư Niên tựa như không nhịn nổi nữa, nghiêm túc răn đe một câu.",
    # 073
    "Kỷ Cảnh nghẹn lời, đồng thời trong lòng cộng thêm cho độ cổ hủ của Lục Tư Niên thêm một ngôi sao.",
    # 074
    "“Dạ vâng ạ.” Cậu cố tình kéo dài giọng đáp.",
    # 075
    "Ăn không nói ngủ không ngáy, đây là cái quy củ từ mấy trăm năm trước rồi cơ chứ, thế mà vẫn có người tuân thủ thật đấy.",
    # 076
    "Sau khi Kỷ Cảnh im lặng, Lục Tư Niên cảm thấy thanh tịnh hơn hẳn, dây thần kinh đang căng như dây đàn cũng hơi buông lỏng đôi chút, chuyên tâm ăn cơm.",
    # 077
    "Anh trước giờ chưa từng ngồi ăn cơm đối diện riêng tư với bất kỳ ai, điều này khiến anh cảm thấy rất căng thẳng.",
    # 078
    "Vốn tưởng Kỷ Cảnh đã chịu an phận, nào ngờ chuyện khiến thái dương anh giật nảy liên hồi vẫn còn ở phía sau.",
    # 079
    "“Đại thúc, chú dính cơm lên mặt kìa.”",
    # 080
    "Chất giọng dịu dàng của thiếu nữ vang lên trước mặt anh, khi anh vừa ngẩng đầu lên, đầu ngón tay ấm áp của đối phương đã chạm vào khóe môi anh, tựa như sợi lông vũ khẽ quẹt nhẹ qua bờ môi anh một cái.",
    # 081
    "Đầu óc Lục Tư Niên trống rỗng hoàn toàn, theo bản năng lập tức nắm chặt lấy cổ tay Kỷ Cảnh.",
    # 082
    "Thiếu nữ trước mắt cười vô cùng rạng rỡ, nhưng Lục Tư Niên lại cảm thấy trong mắt cô phảng phất nét tinh quái khó nhận ra, tựa như… cố tình.",
    # 083
    "Biểu cảm này khiến Lục Tư Niên cảm thấy quen thuộc lạ thường, nhưng anh chẳng còn tâm trí đâu để nghĩ sâu thêm nữa.",
    # 084
    "“Tôi ăn xong rồi.”",
    # 085
    "Lục Tư Niên như bị điện giật vội buông cổ tay Kỷ Cảnh ra, rồi đứng bật dậy.",
    # 086
    "Kỷ Cảnh căn bản chẳng gọi bao nhiêu, sớm đã dừng đũa từ lâu, thấy vậy cũng đứng dậy theo.",
    # 087
    "Trước khi rời đi Kỷ Cảnh gọi giật Lục Tư Niên lại, bảo rằng bọn họ vẫn chưa quẹt thẻ thanh toán.",
    # 088
    "“Tôi quẹt rồi.” Lục Tư Niên nhàn nhạt đáp.",
    # 089
    "Kỷ Cảnh đuổi theo: “Đại thúc, sao chú lại như thế chứ, rõ ràng trước đó đã nói là em mời chú rồi mà.”",
    # 090
    "“Không cần.”",
    # 091
    "“Thế cũng không được, lần sau em mời chú ra ngoài trường ăn cơm nhé?”",
    # 092
    "“Không cần.”",
    # 093
    "…",
    # 094
    "Sau khi tách khỏi Lục Tư Niên, Kỷ Cảnh về nhà thay lại đồ nam, rồi vội vã tới trường học tiết buổi chiều.",
    # 095
    "Đợi sau khi cậu tắm rửa xong nằm vật ra giường thì đã lại là mười giờ đêm.",
    # 096
    "Nằm một lúc cậu bỗng nhớ ra điều gì, bèn rời giường đi lấy một món đồ mang về.",
    # 097
    "Kỷ Cảnh cẩn thận ngắm nghía tuýp thuốc mỡ trên tay, ký hiệu quân dụng in trên đỉnh tuýp thuốc chứng tỏ đây là loại thuốc bôi vết thương dùng nội bộ trong quân đội.",
    # 098
    "Thế nhưng Kỷ Cảnh chẳng định dùng tới nó, tận trong xương tủy cậu vẫn là một Alpha mình đồng da sắt, chút vết thương vặt này mà cũng phải bôi thuốc thì quá mức yếu đuối õng ẹo rồi.",
    # 099
    "Kỷ Cảnh mở khung trò chuyện với Lục Tư Niên, bắt đầu gõ chữ:",
    # 100
    "【Dịch Nam Nam Nam】: Đại thúc ơi, sau này em có thể ăn cơm cùng chú được không ạ.",
    # 101
    "Gõ xong lại thấy chưa đủ, cậu lại chọn ra một nhãn dán mèo con thò đầu làm nũng từ đống biểu cảm mà Kỷ Vân Hy từng gửi cho mình.",
    # 102
    "【Dịch Nam Nam Nam】: [Hình mèo con thò đầu.jpg]",
    # 103
    "Không phải Kỷ Cảnh tự luyến, đàn ông là người hiểu đàn ông nhất, cậu cảm thấy nếu có một mỹ nhân xinh đẹp như Dịch Nam ngày nào cũng tán tỉnh làm nũng với mình thì cậu căn bản không thể kiềm chế nổi quá hai ngày.",
    # 104
    "Nhưng Lục Tư Niên đúng thật không phải người bình thường.",
    # 105
    "Rất lâu sau, đối phương mới gửi tin nhắn lại:",
    # 106
    "【Lục Tư Niên】: Tại sao.",
    # 107
    "Rõ ràng là Lục Tư Niên nhiều khả năng đến tận bây giờ vẫn chẳng hiểu nổi vì sao Kỷ Cảnh lại ngày ngày bám lấy anh.",
    # 108
    "Kỷ Cảnh thấy mệt mỏi trong lòng, mấy giây sau đôi mắt lại sáng lên tia sáng ranh mãnh.",
    # 109
    "【Dịch Nam Nam Nam】: Haizz",
    # 110
    "【Dịch Nam Nam Nam】: [Hình mèo con thở dài.jpg]",
    # 111
    "【Dịch Nam Nam Nam】: Đại thúc, chú đừng nói là đến giờ vẫn chưa nhận ra em đang theo đuổi chú đấy nhé?",
    # 112
    "Kỷ Cảnh dám đảm bảo, Lục Tư Niên lúc này nhất định đang bị sốc đến mức cứng đờ từ đầu tới chân.",
    # 113
    "Cậu tiếp tục gõ chữ:",
    # 114
    "【Dịch Nam Nam Nam】: Em thực ra từ hôm chú cứu em ấy, đã nhất kiến chung tình với chú rồi.",
    # 115
    "【Dịch Nam Nam Nam】: Hôm biết được chú chính là Lục giáo sư em vui lắm, không ngờ vẫn còn cơ hội được gặp lại chú.",
    # 116
    "【Dịch Nam Nam Nam】: Theo em được biết, Lục giáo sư chú đâu có bạn gái đúng không ạ.",
    # 117
    "【Dịch Nam Nam Nam】: Vậy thì, chú có muốn thử yêu đương với em không?",
    # 118
    "Kỷ Cảnh đợi đến nửa đêm vẫn không thấy Lục Tư Niên trả lời, cuối cùng đợi mãi rồi ngủ thiếp đi lúc nào không hay.",
    # 119
    "Cũng vì thế mà cậu đã bỏ lỡ tin nhắn mà Lục Tư Niên gửi tới lúc hai giờ sáng:",
    # 120
    "【Lục Tư Niên】: Xin lỗi, hiện tại tôi không có dự định yêu đương."
]

print(f"Total paragraphs for ch_094: {len(trans_paras)}")

out_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_094"
header = "---\ntitle: Chương 94: Khám bệnh và lời tỏ tình\n---\n\n"
content = header + "\n\n".join(trans_paras) + "\n"

trans_path = os.path.join(out_dir, "translation.md")
with open(trans_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved {trans_path} successfully!")
