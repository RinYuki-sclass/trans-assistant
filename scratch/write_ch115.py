# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_115\translation.md"

paras = [
    # 000
    "Kỷ Cảnh không trông mong Lục Tư Niên thực sự làm được điều gì to tát, cậu chỉ cảm thấy nếu như Lục Tư Niên cứ giữ cái tần suất một tuần không gặp nhau nổi một lần mà yêu đương, hai người sớm muộn gì cũng lại cãi vã to chuyện.",
    # 001
    "Cậu biết Lục Tư Niên mới tiếp quản Đệ tam quân đoàn không lâu, khoảng thời gian này nhất định vô cùng bận rộn, đưa ra yêu cầu này chủ yếu là muốn Lục Tư Niên luôn ghi nhớ trong lòng mà chủ động tìm tới cậu.",
    # 002
    "Dù sao cậu cũng quá đỗi hiểu rõ đàn ông rồi, một khi có được trong tay là không biết trân trọng, tuy rằng Lục Tư Niên khá thành thật chung thủy, nhưng Kỷ Cảnh chẳng hề chê việc Lục Tư Niên để tâm đến cậu nhiều hơn một chút.",
    # 003
    "Kỷ Cảnh lúc này rốt cuộc đã thấu hiểu tại sao trước đây những Omega từng yêu đương với cậu lại hay bám người và nhạy cảm đến vậy rồi.",
    # 004
    "Còn về việc Lục Tư Niên lĩnh hội được bao nhiêu thì Kỷ Cảnh chưa dám đảm bảo, ít nhất tần suất Lục Tư Niên đến thăm cậu trong tuần này đã khiến cậu vô cùng hài lòng.",
    # 005
    "Nghĩ đến vẻ mặt mờ mịt ngơ ngác của Lục Tư Niên sau khi nghe xong những lời của mình, Kỷ Cảnh không nhịn được khẽ bật cười thành tiếng.",
    # 006
    "【Đinh đoong, chúc mừng ký chủ, hiện tại tiến độ nhiệm vụ đã đạt 91%, ký chủ cố lên cố lên, đạt tới một trăm phần trăm sẽ phát phần thưởng thần bí!】",
    # 007
    "“Mày vẫn chưa đi à?” Kỷ Cảnh huýt sáo một tiếng.",
    # 008
    "【Chưa đi đâu ạ, em phải đợi đến khi ký chủ hoàn thành tiến độ cuối cùng cơ hì hì~】",
    # 009
    "“Phần thưởng thần bí là cái gì, mày nói trước cho tao biết đi, khéo tao vừa động lòng một cái là cày đầy luôn đấy.”",
    # 010
    "【Không được nói đâu ạ... Tóm lại, nhất định là thứ mà ký chủ hằng mong muốn.】",
    # 011
    "“Được rồi.” Kỷ Cảnh bất đắc dĩ nói.",
    # 012
    "Lúc này cậu đang rảo bước trên con đường dẫn đến trường bắn mô phỏng vũ khí, bất thình lình nghe thấy tiếng còi hiệu phía trước vang lên, liền lập tức lướt chân bôi dầu đuổi theo đám lính trinh sát đang phi như bay vào bên trong sân bãi.",
    # 013
    "Hôm nay là lần đầu tiên Kỷ Cảnh tham gia buổi huấn luyện súng ống mô phỏng kể từ khi gia nhập Đệ tam quân đoàn.",
    # 014
    "Đế quốc nghiêm cấm quần chúng bình thường mua bán hoặc sử dụng các loại súng máy khí tài, Kỷ Cảnh từ thời tiểu học đã theo học tại các học viện do quân bộ trực tiếp quản hạt, cơ hội tiếp xúc với các loại súng ống thông thường không hề ít, nhưng được chạm tay vào mẫu súng laser tối tân nhất của đế quốc như hôm nay lại là lần đầu tiên trong đời cậu.",
    # 015
    "Đội trưởng Đội Một đứng ở vị trí hàng đầu đối diện mọi người thao tác thị phạm, trên thực tế trong toàn đội chỉ có duy nhất một mình Kỷ Cảnh là chưa từng luyện qua, màn thị phạm này căn bản là dành riêng cho một mình cậu.",
    # 016
    "Ánh mắt Kỷ Cảnh bị cây súng trên tay đối phương thu hút chặt chẽ.",
    # 017
    "Không có một Alpha nào lại không mê đắm vũ khí, Kỷ Cảnh đương nhiên cũng không ngoại lệ.",
    # 018
    "Sau khi màn thị phạm kết thúc, các lính trinh sát có mặt tại hiện trường được chia thành mười nhóm lần lượt vào tập bắn, Kỷ Cảnh vô cùng bất hạnh bị xếp vào vị trí cuối cùng của nhóm.",
    # 019
    "“Vãi chưởng, khó vãi đái, laser nhanh hơn đạn thường nhiều quá, bắn ra nhẹ bẫng chẳng có chút cảm giác thực tế nào, tao toàn phải dựa vào cảm giác.”",
    # 020
    "“Thế thì cảm giác của mày nhạy bén ghê cơ, bắn bao nhiêu lần rồi mà phát nào cũng trượt bia.”",
    # 021
    "“Cút!”",
    # 022
    "...",
    # 023
    "Đám Alpha xung quanh bước xuống sân cãi cọ rôm rả tưng bừng, mãi mới đến lượt Kỷ Cảnh cầm lấy súng.",
    # 024
    "Đám Alpha phía trước nói không sai chút nào, súng laser cầm trên tay nhẹ bẫng không có trọng lượng thực tế, kiểu dáng cũng khác xa so với những khẩu súng mà Kỷ Cảnh từng cầm trước đây.",
    # 025
    "“Suỵt, im lặng chút coi, xem thằng nhóc kia bắn được bao nhiêu điểm.”",
    # 026
    "“Nó mới chạm vào lần đầu, không trượt bia đã được coi là thiên phú trác tuyệt rồi.”",
    # 027
    "Tên Alpha tên Đại Vĩ khịt mũi hừ lạnh khinh khỉnh.",
    # 028
    "Kỷ Cảnh hồi tưởng lại từng chi tiết trong màn thị phạm ban nãy, từ từ giơ cánh tay lên, bắp tay dần dần căng siết làm lộ ra những đường nét cơ bắp tuyệt đẹp.",
    # 029
    "Khẽ nhắm mắt trái, Kỷ Cảnh nín thở, đầu ngón tay khẽ động.",
    # 030
    "Gần như cùng lúc với khoảnh khắc đầu ngón tay nhấn xuống, trên tấm bia cách xa hàng trăm mét liền xuất hiện một lỗ thủng bị tia laser màu xanh lam thiêu đốt.",
    # 031
    "Kỷ Cảnh híp mắt nhìn qua, bất mãn khẽ nhíu mày.",
    # 032
    "“Vãi đạn! Bảy vòng, có nhầm không vậy, nó hack game đấy à?!”",
    # 033
    "“Sao lại nổ súng nữa rồi, lần này bao nhiêu, đệt mợ, tám vòng! Tao mà không nhớ nhầm thì người lần trước vừa tới đã bắn trúng tám vòng là Lục Tư Niên đúng không? Ơ kìa, mày làm cái gì đấy, đánh tao làm gì——”",
    # 034
    "Đám Alpha đứng xem phía sau thấy vậy đều lao xao bàn tán ầm ĩ, Kỷ Cảnh lại bắn thêm một phát nữa, phát hiện vẫn chỉ là tám vòng.",
    # 035
    "Đúng lúc cậu sắp sửa mất kiên nhẫn thì một giọng nói trầm thấp quen thuộc đột ngột vang lên bên tai,",
    # 036
    "“Thả lỏng.”",
    # 037
    "Mùi tin tức tố hương gỗ thông dễ chịu trên người Lục Tư Niên khiến Kỷ Cảnh bất giác thả lỏng dây thần kinh căng thẳng.",
    # 038
    "Tin tức tố nồng độ thấp có thể phát huy công hiệu vỗ về xoa dịu tốt nhất đối với phối ngẫu.",
    # 039
    "Khóe môi cậu vừa định nhếch lên mỉm cười thì đã bị Lục Tư Niên từ phía sau vươn tay giữ chặt lấy bàn tay.",
    # 040
    "“Hổ khẩu thả lỏng bớt một phần ba lực.”",
    # 041
    "Lòng bàn tay ấm áp dán chặt lên mu bàn tay Kỷ Cảnh, cậu từ từ buông bớt lực, ngay khoảnh khắc cậu vừa tìm được điểm ngắm chuẩn xác, Lục Tư Niên đã giúp cậu siết cò phát súng này.",
    # 042
    "Trúng ngay hồng tâm.",
    # 043
    "“Tự mình làm đi.”",
    # 044
    "Lục Tư Niên rút tay về, ánh mắt Kỷ Cảnh chợt sắc lạnh, không chút do dự bóp cò liên thanh bằng bằng bằng bảy phát súng liên tiếp.",
    # 045
    "Phát nào phát nấy đều mười vòng trúng hồng tâm.",
    # 046
    "“Hay lắm!”",
    # 047
    "Chu Độ hô to một tiếng dõng dạc, dẫn đầu vỗ tay tán thưởng.",
    # 048
    "Kỷ Cảnh hạ cánh tay xuống, lập tức quay người đối diện với Lục Tư Niên, Lục Tư Niên trông như vừa họp xong, trên tay vẫn cầm chiếc bình giữ nhiệt kiểu ông già từng dùng ở Học viện Quân sự Đế quốc.",
    # 049
    "Cậu đang định nhân góc khuất kín đáo lén làm chút chuyện mờ ám với Lục Tư Niên, bởi vì vừa rồi Lục Tư Niên thực sự có chút quá đỗi gợi cảm, thế nhưng Chu Độ đã sải một bước dài chen ngang vào giữa hai người bọn họ.",
    # 050
    "“Thằng nhóc khá lắm, không tệ, năm xưa cũng chỉ có Lục Tư... Lục đoàn trưởng mới đạt được cái trình độ này của cậu thôi!”",
    # 051
    "Chu Độ giơ tay vỗ mạnh một cái lên vai Kỷ Cảnh, sau đó quay người nghiêm khắc quát: “Dù sao các cậu cũng là đội mũi nhọn của doanh trinh sát tôi, ngay cả một tân binh Alpha mới tới cũng bắn phát nào trúng mười vòng phát nấy, tại sao các cậu lại không làm được? Bắt đầu từ hôm nay cường độ huấn luyện của Đội Một tăng thêm cho tôi!”",
    # 052
    "Cả đám Alpha xung quanh không ai dám bước lên tiếp lời, toàn bộ đều cúi gằm mặt nhìn mũi giày.",
    # 053
    "May mắn thay lời Chu Độ vừa dứt thì chuông giải tán đã vang lên, vừa vặn đúng giờ ăn trưa, Chu Độ dù có bực bội đến đâu cũng phải thả người đi ăn cơm.",
    # 054
    "“Buổi trưa,” Lục Tư Niên đột nhiên cất tiếng, đợi đến khi Kỷ Cảnh nhìn sang, anh bước tới gần vài bước, “Tôi có thể ăn cơm cùng em không.”",
    # 055
    "Kỷ Cảnh nghe vậy khẽ ngẩn người, sau đó lập tức hiểu ngay ý đồ của Lục Tư Niên.",
    # 056
    "“Lục đoàn trưởng chẳng phải trăm công nghìn việc bận rộn lắm sao?”",
    # 057
    "“Không có, có thể cùng em ăn cơm.” Lục Tư Niên răm rắp khuôn phép trả lời.",
    # 058
    "“Ồ——” Kỷ Cảnh cố tình kéo dài giọng điệu, “Thế thì được thôi, anh định đưa tôi đi đâu ăn đây?”",
    # 059
    "Lục Tư Niên nghe vậy có chút ngạc nhiên: “Ở đây chỉ có nhà ăn mới có cơm ăn thôi.”",
    # 060
    "Ý của tôi là anh có thể trực tiếp đưa tôi về phòng làm việc của anh ăn riêng cơ mà, nhà ăn đông người như thế thì làm việc gì có tiện không? Kỷ Cảnh mệt mỏi trong lòng.",
    # 061
    "Kỷ Cảnh hiện tại chưa muốn bại lộ mối quan hệ giữa mình và Lục Tư Niên, bản thân cậu chẳng bận tâm điều gì, nhưng Lục Tư Niên với tư cách là một Omega đảm nhận vị trí đoàn trưởng vốn dĩ đã có nhiều điều tiếng dị nghị, lúc này mà truyền ra tin tức anh yêu đương với một Alpha trong quân đoàn thì lại càng thêm rắc rối.",
    # 062
    "Đúng lúc này Chu Độ đột nhiên bước tới hỏi cậu: “Kỷ Cảnh, đi ăn cơm với tôi không?”",
    # 063
    "Chu Độ bồi dưỡng Kỷ Cảnh như người kế nhiệm, bình thường thỉnh thoảng sẽ rủ Kỷ Cảnh đi ăn cơm cùng, lần này cũng không nghĩ nhiều mà thuận miệng hỏi luôn.",
    # 064
    "“Kỷ Cảnh đi với tôi.”",
    # 065
    "Lục Tư Niên đột nhiên liếc nhìn Chu Độ một cái.",
    # 066
    "“Hả? Cái gì cơ?” Chu Độ như bị ảo giác ngoáy ngoáy lỗ tai.",
    # 067
    "“Cùng đi đi, đi thôi.” Kỷ Cảnh ngắt lời, vỗ bàn chốt hạ.",
    # 068
    "Suốt dọc đường Chu Độ hệt như gặp ma liên tục liếc trộm Lục Tư Niên, tần suất dày đặc đến mức ngay cả Kỷ Cảnh cũng thấy khó chịu.",
    # 069
    "“Tôi đi lấy cơm giúp em luôn.” Lục Tư Niên để lại câu nói này rồi quay người đi thẳng.",
    # 070
    "Chu Độ: “Không phải chứ, cậu với Lục đoàn trưởng rốt cuộc có quan hệ gì thế hả, tôi chưa từng thấy Lục Tư Niên ăn cơm cùng ai bao giờ, huống chi cậu ta lại còn đi lấy cơm hộ cậu nữa chứ.”",
    # 071
    "“Có lẽ là... Lục đoàn trưởng tán thưởng tôi chăng.” Kỷ Cảnh mở to mắt nói dối không chớp mắt.",
    # 072
    "Chu Độ nửa tin nửa ngờ tự mình đi lấy cơm, Đệ tam quân đoàn không có đặc quyền cấp bậc quân hàm, cho dù là Lục Tư Niên hay Chu Độ cũng đều phải tự xếp hàng lấy cơm cùng các Alpha khác.",
    # 073
    "Ba người ngồi ở chiếc bàn trong góc khuất, bầu không khí kỳ quặc vô cùng.",
    # 074
    "Chu Độ cảm nhận rõ ràng thái độ của Lục Tư Niên đối với gã không giống như trước, trước đây cùng lắm là không có thái độ gì, bây giờ lại mang theo chút địch ý thoang thoảng.",
    # 075
    "Gã cũng chưa từng nghĩ có một ngày bản thân lại cùng ngồi chung bàn ăn cơm với Lục Tư Niên, người mà gã luôn tránh xa ba bước.",
    # 076
    "Để xoa dịu bầu không khí ngột ngạt, gã bắt đầu vắt óc tìm đề tài nói chuyện, nhưng nghĩ nát óc cũng chỉ nhớ ra được chuyện hóng hớt duy nhất liên quan đến Lục Tư Niên, thế là gã nói:",
    # 077
    "“Lục đoàn trưởng, hoa hồng hôm nay cậu nhận được tôi nhìn thấy rồi đấy nhé, có phải do chị dâu mà mọi người trong nhóm nói gửi tặng không vậy.”",
    # 078
    "“Hoa hồng?”",
    # 079
    "Kỷ Cảnh đột ngột dừng đũa lại.",
    # 080
    "Lục Tư Niên bình thường lúc ăn cơm kiên quyết không mở miệng nói chuyện, lúc này thấy Kỷ Cảnh nhìn mình, không thể không ngắn gọn buông một chữ “Không phải”, sau đó không chút biểu cảm nhìn sang Chu Độ: “Ăn cơm không được nói chuyện.”",
    # 081
    "Chu Độ bẽn lẽn ngậm miệng lại.",
    # 082
    "“Hoa hồng gì cơ.” Kỷ Cảnh căn bản không có ý định bỏ qua chuyện này.",
    # 083
    "“Thì một bó to đùng ấy, đang đặt trong phòng đoàn trưởng kia kìa.” Chu Độ vô tư nói.",
    # 084
    "Sau đó gã liền phát hiện Kỷ Cảnh cũng đột nhiên im bặt không nói tiếng nào nữa.",
    # 085
    "Bữa cơm này Chu Độ ăn vô cùng nghẹn ứ bức bối, và vội vài miếng xong liền kiếm cớ chuồn mất dạng, Lục Tư Niên và Kỷ Cảnh còn lại ăn thêm một lúc cũng bước ra khỏi nhà ăn.",
    # 086
    "Lục Tư Niên bất chợt lên tiếng: “Hoa hồng, là do tôi đặt.”",
    # 087
    "Kỷ Cảnh dừng bước chân lại, bốn mắt nhìn nhau với Lục Tư Niên.",
    # 088
    "“Tặng cho em.”",
    # 089
    "Lục Tư Niên nghẹn ra bốn chữ cuối cùng.",
    # 090
    "Lục Tư Niên đối với chuyện tình cảm nửa hiểu nửa không, nhưng biết rõ hoa hồng mang ý nghĩa gì, cũng nhớ rõ lần đầu tiên khi cùng “Dịch Nam” ra ngoài hẹn hò, “Dịch Nam” từng tặng anh một cành hoa hồng.",
    # 091
    "Hôm đó Kỷ Cảnh đòi anh phải theo đuổi cậu, Lục Tư Niên lần đầu tiên cảm thấy khó giải quyết, đành phải tham khảo theo thủ đoạn theo đuổi của Dịch Nam.",
    # 092
    "“...” Kỷ Cảnh cạn lời không nói nên lời, “Khi nào thì tặng cho tôi?”",
    # 093
    "Lục Tư Niên cúi đầu liếc nhìn thời gian: “Bây giờ đến phòng đoàn trưởng lấy cũng được.”",
    # 094
    "Màn tặng hoa của Lục Tư Niên đơn thuần chỉ là đem hoa tặng ra ngoài mà thôi, Kỷ Cảnh từ phòng đoàn trưởng của Lục Tư Niên ôm về một bó hoa hồng đỏ rực to đùng.",
    # 095
    "Kỷ Cảnh vốn dĩ không trông mong Lục Tư Niên có thể hiểu được sự lãng mạn gì, nói thật việc anh có thể làm đến bước tặng hoa hồng cho mình này đã vượt xa kỳ vọng ban đầu của Kỷ Cảnh rồi.",
    # 096
    "Kỷ Cảnh làm theo hướng dẫn trên thiết bị đầu cuối, cắm bó hoa hồng vào chiếc cốc nước quân dụng được Đệ tam quân đoàn phát thống nhất, đặt ngay ngắn trước bậu cửa sổ.",
    # 097
    "Đồng thời chụp một bức ảnh gửi qua cho Kỷ Vân Hy.",
    # 098
    "Cậu hiện tại bắt đầu mong chờ xem Lục Tư Niên tiếp theo sẽ làm những trò gì nữa rồi.",
    # 099
    "Buổi chiều Lục Tư Niên không xuất hiện, cũng không gửi tin nhắn nào cho cậu, chắc là lại rất bận rộn.",
    # 100
    "Mãi đến tối khi tan hàng về ký túc xá, Kỷ Cảnh mới nhìn thấy tin nhắn Lục Tư Niên gửi tới cách đây không lâu.",
    # 101
    "【Khúc Gỗ Lục】: Xin lỗi, chiều nay bận quá.",
    # 102
    "【Anh Cảnh của mày】: Đang làm gì đấy?",
    # 103
    "【Khúc Gỗ Lục】: Đang trên đường về ký túc xá.",
    # 104
    "【Anh Cảnh của mày】: Gửi tấm ảnh cho tôi xem coi.",
    # 105
    "【Khúc Gỗ Lục】: [Hình ảnh].",
    # 106
    "【Anh Cảnh của mày】: Sau này báo cáo hành trình là phải kèm theo ảnh chụp, như vậy mới có độ tin cậy.",
    # 107
    "【Anh Cảnh của mày】: Mèo con xoay vòng jpg.",
    # 108
    "【Khúc Gỗ Lục】: Được.",
    # 109
    "...",
    # 110
    "Kỷ Cảnh tắm rửa xong lại mở thiết bị đầu cuối ra, xem Lục Tư Niên có nói thêm gì để mở ra đề tài mới hay không.",
    # 111
    "Kết quả chỉ thấy năm sáu tin tức quân sự do Lục Tư Niên chuyển tiếp qua.",
    # 112
    "【Anh Cảnh của mày】: ...",
    # 113
    "【Anh Cảnh của mày】: Gửi cái này cho tôi làm gì?",
    # 114
    "【Khúc Gỗ Lục】: Tôi muốn cùng em bàn luận về tin tức.",
    # 115
    "【Anh Cảnh của mày】: ...",
    # 116
    "【Anh Cảnh của mày】: Lục Tư Niên, có ai đi tán tỉnh người ta như anh không hả?",
    # 117
    "【Khúc Gỗ Lục】: Xin lỗi.",
    # 118
    "【Khúc Gỗ Lục】: Tôi sẽ cải thiện.",
    # 119
    "Kỷ Cảnh thở dài thườn thượt một hơi, thầm nghĩ cái tính cách này của Lục Tư Niên mà yêu đương được thì đúng là ăn may vớ bẫm.",
    # 120
    "Nói thì nói vậy, cậu vẫn mở từng bài báo mà Lục Tư Niên gửi tới ra xem, rồi phát hiện quả thực vô cùng tẻ nhạt.",
    # 121
    "Cậu đặt thiết bị đầu cuối xuống, định thay bộ đồ ngủ, ánh mắt đột nhiên liếc qua thân dưới của mình, trong nháy mắt, một tia sáng lóe lên trong đầu.",
    # 122
    "【Anh Cảnh của mày】: Lục Tư Niên, hay là để tôi dạy anh cách nói chuyện nhé?",
    # 123
    "【Khúc Gỗ Lục】: Được.",
    # 124
    "【Anh Cảnh của mày】: Bây giờ, gửi một bức ảnh cơ bụng của anh qua đây.",
    # 125
    "Lời tác giả:",
    # 126
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-06-17 22:34:36~2023-06-20 19:24:12 nhé~",
    # 127
    "Cảm ơn các thiên thần nhỏ ném địa lôi: Lai Nhật Phương Trường, Thủ)、Hậu ζ 1 cái;",
    # 128
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Lam Phong Tuyết Ảnh, 46377191, Lý Văn, Cột Dương 5 bình; Mỹ Nhân Làm 1 Thiên Kinh Địa Nghĩa, Nhàn de Diêm, Hạ Mộng Vi Vũ 2 bình; Quyện Từ, Ngộ Tống., Triêu Ca, Lâm Trí, Trấn Khuê 1 bình;",
    # 129
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 115: Gián cách ngàn dặm và hoa hồng\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
