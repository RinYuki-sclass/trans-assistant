# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_116\translation.md"

paras = [
    # 000
    "Lúc bấy giờ Lục Tư Niên đang ngồi nghiêm trang ngay ngắn bên đầu giường, sau khi nhìn thấy tin nhắn Kỷ Cảnh gửi tới liền giật bắn mình đứng phắt dậy khỏi giường.",
    # 001
    "Rất nhanh sau đó, một rặng mây đỏ không rõ nguyên do liền men theo sườn cổ lan tràn lên tận vành tai anh.",
    # 002
    "Kỷ Cảnh, cậu ấy, quá...",
    # 003
    "【Khúc Gỗ Lục】: Kỷ Cảnh, như vậy không tốt đâu.",
    # 004
    "Kỷ Cảnh đợi nửa ngày trời mới đợi được một câu “như vậy không tốt”, phụt một tiếng không nhịn được mà bật cười thành tiếng, cậu hoàn toàn có thể tưởng tượng ra lúc này Lục Tư Niên đang mang vẻ mặt thế nào.",
    # 005
    "【Anh Cảnh của mày】: Chỗ nào không tốt, tại sao lại không tốt? Tôi chỉ bảo anh chụp một tấm ảnh cơ bụng của anh thôi mà.",
    # 006
    "【Anh Cảnh của mày】: Anh có biết trước đây lúc tôi theo đuổi anh, tôi phải chụp cho anh những bức ảnh tốn bao nhiêu công sức không hả, nào là căn chỉnh ánh sáng, tìm góc chụp rồi còn phải chọn quần áo, giờ chỉ bảo anh vén áo lên chụp một tấm ảnh cũng không được. Mèo con tủi thân jpg.",
    # 007
    "【Anh Cảnh của mày】: Thôi được rồi, tôi biết rồi, tôi không nên tham lam như thế...",
    # 008
    "Lục Tư Niên trả lời rất nhanh",
    # 009
    "【Khúc Gỗ Lục】: Xin lỗi, tôi không có ý đó.",
    # 010
    "【Khúc Gỗ Lục】: Đợi tôi một lát.",
    # 011
    "【Anh Cảnh của mày】: Được! [Mắt lấp lánh sao].",
    # 012
    "Kỷ Cảnh mưu kế thành công, hai tay ôm sau gáy nằm dài thượt huênh hoang, chờ đợi bức ảnh cơ bụng của mình.",
    # 013
    "Vóc dáng của Lục Tư Niên thuộc hàng đỉnh cao nhất, nếu xét theo tiêu chuẩn phán xét của một Alpha mà nói thì Lục Tư Niên chính là hình mẫu thể hình trong mơ của Alpha.",
    # 014
    "Bình thường mặc quần áo vào thì không nhìn ra được, nhưng một khi cởi áo ra thì chuẩn chỉnh tám múi cơ bụng, từng múi cơ đều đẹp đẽ chuẩn mực như bước ra từ sách giáo khoa, cơ ngực nở nang săn chắc, đường eo thon gọn hữu lực.",
    # 015
    "Nơi Kỷ Cảnh thích nhất chính là cơ ngực của Lục Tư Niên, trước đây khi cậu chưa hiểu sự đời thì thích kiểu mềm mại của Omega, sau này khi nhìn thấy Lục Tư Niên mới hiểu rõ rốt cuộc bản thân thích kiểu thế nào, lúc thả lỏng thì mềm mại đàn hồi, lúc dùng lực thì có thể cảm nhận rõ rệt sức mạnh bùng nổ của cơ bắp.",
    # 016
    "Cậu hồi tưởng lại cảm giác xúc giác của ngày hôm ấy, lòng bàn tay bất giác ngứa ngáy râm ran.",
    # 017
    "Lục Tư Niên chụp bức ảnh này mất gần nửa tiếng đồng hồ, ngay khoảnh khắc bức hình vừa được gửi tới, Kỷ Cảnh liền nhanh tay lẹ mắt bấm mở ra.",
    # 018
    "Đó là một bức ảnh chụp hoàn toàn không có bố cục nghệ thuật, chẳng khác nào một tấm hình chụp tùy tiện tiện tay —— một đoạn eo nghiêng săn chắc hữu lực, đại khái nghiêng chừng bốn mươi lăm độ, có thể nhìn thấy rõ mồn một từng thớ vân trên làn da vùng eo bụng, cùng với những đường nét cơ bắp sắc lẹm như dao gọt của từng múi bụng, đường nhân ngư kéo dài tít tắp vào bên trong cạp chun của chiếc quần ngủ...",
    # 019
    "Vạt áo của bộ đồ ngủ kiểu dáng cổ hủ bị kéo vén lên cao, nhưng trong ống kính có thể thấy rõ hai bàn tay của Lục Tư Niên đều đang cầm thiết bị đầu cuối —— chứng tỏ vạt áo là do chính miệng Lục Tư Niên đang cắn lấy.",
    # 020
    "【Khúc Gỗ Lục】: Thế này có được không?",
    # 021
    "Vù một cái, Kỷ Cảnh cảm thấy một ngọn lửa vô danh từ sâu trong cơ thể bùng cháy dữ dội xông thẳng lên.",
    # 022
    "Cậu đập bốp một tiếng gập thiết bị đầu cuối lại, bình tâm lại một lát mới gõ phím trả lời",
    # 023
    "【Anh Cảnh của mày】: Ừm",
    # 024
    "【Anh Cảnh của mày】: Tôi thích lắm.",
    # 025
    "...",
    # 026
    "Là một Alpha trẻ tuổi tràn đầy nhiệt huyết tinh lực, Kỷ Cảnh nghẹn một bụng hỏa suốt cả đêm không nơi phát tiết, cậu đang vô cùng cấp thiết cần một con đường để giải tỏa.",
    # 027
    "Đang lúc kìm nén một thân sức lực không biết xả vào đâu thì vừa vặn đụng ngay buổi kiểm tra cách đấu mỗi tháng một lần của doanh trinh sát vào ngày hôm sau.",
    # 028
    "Đệ tam quân đoàn mỗi tháng đều có đợt kiểm tra định kỳ tương ứng làm tiêu chuẩn đánh giá kết quả huấn luyện, bài kiểm tra cách đấu chính là từng người bước vào phòng cách đấu đánh đối kháng, hệ thống sẽ tính điểm xếp hạng.",
    # 029
    "Kỷ Cảnh chỉ cảm thấy ngày hôm đó tinh lực của mình dồi dào khác thường, bên trong cơ thể cũng có một luồng sức mạnh vô hình liên tục không ngừng thúc đẩy cực hạn của cậu, khi con số điểm số kia được cậu đánh tung ra, chính bản thân Kỷ Cảnh cũng phải giật mình chấn động.",
    # 030
    "“Trời đất quỷ thần ơi, tao có nhìn nhầm không thế này......”",
    # 031
    "Cả một đám Alpha đứng chờ ở khu vực chờ bên ngoài há hốc mồm trợn trừng mắt nhìn dữ liệu truyền tải theo thời gian thực trên màn hình lớn ở trung tâm.",
    # 032
    "“9.364.719 điểm??! Tao không đếm nhầm chữ số đấy chứ, tao nhớ điểm số cao nhất trong lịch sử cũng chỉ có 9.364.699 điểm thôi mà!”",
    # 033
    "“Mày không đếm nhầm đâu, mày nhìn bảng xếp hạng bên cạnh kìa, Kỷ Cảnh hiện tại xếp thứ nhất trong bảng thành tích lịch sử của hệ thống rồi, điểm của Lục Tư Niên bị nó vượt qua rồi.”",
    # 034
    "Kỷ Cảnh vừa bước chân ra ngoài liền nghe thấy câu nói này, cậu đột ngột ngẩng phắt đầu lên, quả nhiên nhìn thấy tên của mình đã thay thế Lục Tư Niên trở thành vị trí số một.",
    # 035
    "Hệ thống xếp hạng chiến tích phòng cách đấu được áp dụng chung cho toàn thể đế quốc, Kỷ Cảnh đã vượt qua Lục Tư Niên, trở thành tân No.1 của toàn thể đế quốc.",
    # 036
    "Bảng xếp hạng này vừa tung ra, ánh mắt của toàn bộ các Alpha trong doanh trinh sát nhìn Kỷ Cảnh đều hoàn toàn thay đổi, trước đây tất cả mọi người đều nghĩ rằng cậu dựa vào gia thế bối cảnh mà đi cửa sau trong quân đoàn, đến cả Lục Tư Niên và Chu Độ cũng thiên vị cậu, không ngờ Kỷ Cảnh lại thực sự là một thiên tài thứ thiệt!",
    # 037
    "Kỷ Cảnh vẫn còn đang đứng chôn chân tại chỗ ngơ ngác thì mấy tên Alpha của Đội Một bên kia đã đỏ bừng mặt kích động ùa tới vây quanh.",
    # 038
    "Trong chớp mắt người thì quạt gió người thì dâng nước tận tay.",
    # 039
    "Kỷ Cảnh hoàn toàn không ngờ có một ngày bản thân lại có thể phá vỡ được kỷ lục của Lục Tư Niên.",
    # 040
    "Cậu được mọi người vây quanh đưa tới một góc ngồi xuống, lúc này mới chậm nửa nhịp nhớ ra điều gì đó, rút thiết bị đầu cuối ra gửi tin nhắn cho Lục Tư Niên.",
    # 041
    "“Đỉnh quá Kỷ Cảnh ơi, không ngoài dự đoán thì cậu hoàn toàn chính là một Lục Tư Niên tiếp theo đấy!”",
    # 042
    "“Xì, Lục Tư Niên chỉ là một Omega thì tính là cái thá gì chứ... ặc”",
    # 043
    "Tên Alpha mở mồm châm chọc Lục Tư Niên liền bị một ánh mắt lạnh thấu xương của Kỷ Cảnh quét qua làm cho sợ hãi ngậm chặt miệng lại.",
    # 044
    "“Hê hê, nếu tao là mày thì hôm nay tao sẽ đến khoang xăm hình của doanh trại để xăm chiến tích này lên người ngay.” Một Alpha đầy vẻ ngưỡng mộ và khát khao để lộ cánh tay của mình ra, trên cánh tay phải của hắn xăm một đồ đằng biểu tượng của Đệ tam quân đoàn.",
    # 045
    "Rất nhiều Alpha của Đệ tam quân đoàn sau khi gia nhập đều sẽ tự giác xăm đồ đằng lên người, nếu lập được chiến công hiển hách gì cũng thích xăm, các Alpha trời sinh đều thích khắc ghi những hình xăm uy phong bá khí lên thân thể.",
    # 046
    "【Khúc Gỗ Lục】: Kỷ Cảnh, em rất giỏi, tôi trước giờ luôn biết điều đó.",
    # 047
    "Thiết bị đầu cuối rung lên, Kỷ Cảnh vừa mỉm cười nhìn dòng tin nhắn của Lục Tư Niên, vừa như có điều suy nghĩ.",
    # 048
    "Buổi trưa Lục Tư Niên lại đến tìm Kỷ Cảnh ăn cơm trưa cùng, trước đó còn đặc biệt nghiêm túc hỏi cậu sau này có thể mỗi ngày đều cùng cậu ăn cơm được không.",
    # 049
    "Ăn cơm xong Lục Tư Niên lại có cuộc họp phải tham gia, cậu buổi chiều cũng có bài huấn luyện, hai người liền dùng dằng lưu luyến tách nhau ra.",
    # 050
    "Kỷ Cảnh một mạch sải bước về phía ký túc xá, trong đầu không ngừng suy nghĩ về những lời đám Alpha kia đã nói.",
    # 051
    "Xăm hình sao...",
    # 052
    "Cậu trước giờ chưa từng xăm bất cứ thứ gì lên người.",
    # 053
    "Kỷ Cảnh trước đây chưa từng nghĩ tới chuyện xăm hình, với công nghệ xăm của đế quốc, một khi đã xăm lên là sẽ theo suốt cả cuộc đời, không thể sửa đổi cũng không thể tẩy xóa, Kỷ Cảnh luôn cảm thấy đám Alpha xăm trổ lộn xộn khắp người đều ngốc nghếch hết chỗ nói.",
    # 054
    "Thế nhưng cậu đột nhiên lại nghĩ tới Lục Tư Niên, Lục Tư Niên đã bị cậu đánh dấu trọn đời rồi.",
    # 055
    "Trọn đời.",
    # 056
    "Kỷ Cảnh chưa từng nghĩ rằng bản thân sẽ sở hữu một thứ thuộc về riêng mình suốt cả cuộc đời.",
    # 057
    "Vậy còn Lục Tư Niên thì sao, anh liệu có muốn sở hữu một dấu ấn thuộc về riêng anh suốt cả cuộc đời hay không?",
    # 058
    "Một ý nghĩ nảy sinh trong lòng Kỷ Cảnh, bước chân đang hướng về ký túc xá của cậu liền rẽ ngang, bước thẳng về phía máy xăm hình của doanh trại.",
    # 059
    "Tối đến Kỷ Cảnh phanh rộng áo choàng tắm ngồi trên giường ngắm nhìn gốc đùi trong của mình.",
    # 060
    "Hình xăm mới xăm ở chỗ này vốn dĩ đã có chút đau nhức, kết quả buổi chiều tập luyện quá mức cuồng nhiệt, mồ hôi thấm vào vết thương làm cho nơi đó có chút sưng đỏ ửng lên.",
    # 061
    "Kỷ Cảnh dang rộng hai chân ra thêm một chút, định bụng để trần phơi ra ngoài cho nó dịu bớt đi.",
    # 062
    "Đúng lúc này thiết bị đầu cuối đột ngột reo lên, cậu mở ra xem, phát hiện là Lục Tư Niên",
    # 063
    "【Khúc Gỗ Lục】: Hình ảnh.",
    # 064
    "【Khúc Gỗ Lục】: Kỷ Cảnh, em có tiện ra ngoài cùng tôi một lát không?",
    # 065
    "Bức ảnh Lục Tư Niên gửi tới là lối vào thao trường huấn luyện của doanh trinh sát, Kỷ Cảnh chỉ liếc mắt một cái là nhận ra ngay.",
    # 066
    "Cũng hiếm thấy thật đấy, Lục Tư Niên đây là muốn chơi trò hẹn hò đêm khuya với cậu đấy à?",
    # 067
    "Kỷ Cảnh nhanh chóng cởi phăng áo choàng tắm ra, thay vào một chiếc áo phông trắng cùng quần dài.",
    # 068
    "【Anh Cảnh của mày】: Tới đây.",
    # 069
    "Kỷ Cảnh nghĩ rằng Lục Tư Niên muốn cùng cậu hẹn hò, nhưng không ngờ Lục Tư Niên lại trang trọng đến mức này.",
    # 070
    "Từ đằng xa đã nhìn thấy Lục Tư Niên đứng ở lối vào thao trường, không hề mặc quân phục sĩ quan, mà lại mặc áo sơ mi phối quần tây, lại còn thắt cà vạt vô cùng chỉnh chu nghiêm túc.",
    # 071
    "Dưới ánh trăng, chiếc áo sơ mi trắng của Lục Tư Niên ánh lên tia sáng mờ ảo, càng tôn lên vẻ thanh tú nhã nhặn của Lục Tư Niên.",
    # 072
    "Đợi đến khi Kỷ Cảnh bước lại gần mới phát hiện trong tay Lục Tư Niên còn đang ôm một bó hoa hồng.",
    # 073
    "“Lục giáo sư.”",
    # 074
    "Giọng nói trong trẻo phá tan màn đêm tĩnh mịch, Lục Tư Niên nhìn theo hướng phát ra âm thanh, trong sát na dường như nhìn thấy bóng hình Dịch Nam đang mỉm cười nhìn anh, cuối cùng hòa làm một thể với Kỷ Cảnh.",
    # 075
    "“Trang trọng thế cơ à.” Kỷ Cảnh mỉm cười đón lấy bó hoa hồng từ tay Lục Tư Niên, nhướng mày nói.",
    # 076
    "“Tôi muốn,” yết hầu Lục Tư Niên khẽ trượt lên xuống, “Đưa em đến một nơi.”",
    # 077
    "“Được thôi, Lục giáo sư đi đâu thì tôi theo đó.” Kỷ Cảnh cố tình gọi ba chữ Lục giáo sư đầy vẻ mập mờ ám muội.",
    # 078
    "Lục giáo sư không nhìn cậu, tựa như có chút ngượng ngùng, Kỷ Cảnh cứ thế sải bước đi theo sau anh, Kỷ Cảnh không mấy quen thuộc với Đệ tam quân đoàn, nhưng Đệ tam quân đoàn thực sự rất rộng lớn, chiếm cứ một nửa diện tích đất đai của cả tinh cầu.",
    # 079
    "Lục Tư Niên lái xe đưa cậu dừng lại ở một nơi giống như vùng ranh giới biên giới.",
    # 080
    "Kỷ Cảnh vừa bước xuống xe liền bị cảnh sắc nơi đây làm cho choáng ngợp chấn động.",
    # 081
    "“Nơi này là năm đầu tiên tôi tới Đệ tam quân đoàn vô tình tìm thấy, tinh cầu này cách dải Ngân Hà rất gần, màn trời ở đây có thể nhìn thấy vô cùng rõ ràng.”",
    # 082
    "Lục Tư Niên đem cảnh sắc tuyệt mỹ này quy về một cách cụt lủn không chút thi vị là nhìn rất rõ ràng.",
    # 083
    "“Nơi này rất yên tĩnh, rất thích hợp với tôi.”",
    # 084
    "Kỷ Cảnh dựa lưng vào thân xe, hỏi anh: “Anh đến đây thường làm cái gì?”",
    # 085
    "“Giải khuây.” Lục Tư Niên nói, “Ở đây tôi có thể tạm thời thả lỏng một lát.”",
    # 086
    "Kỷ Cảnh ngẫm nghĩ, Lục Tư Niên sống ngần ấy năm trời, bên cạnh không có lấy một người thân cận, tâm sự gì cũng chỉ có thể nghẹn đắng giấu kín trong lòng, hèn chi lại cần tìm một nơi để giải tỏa.",
    # 087
    "“Vậy nên, hôm nay Lục giáo sư đưa tôi tới đây để hẹn hò đấy à?” Kỷ Cảnh hỏi.",
    # 088
    "Lục Tư Niên dời tầm mắt sang, ừm một tiếng: “Còn để chúc mừng em đã phá kỷ lục của tôi nữa.”",
    # 089
    "Kỷ Cảnh cụp mắt nhìn bó hoa hồng trong lòng mình: “Hoa hồng ở đây cũng đặt được sao?”",
    # 090
    "“Không đặt được, tôi đặt từ tinh cầu bên cạnh chuyển tới.” Lục Tư Niên trả lời, tinh cầu này là một hoang tinh cằn cỗi chẳng có gì, nhưng tinh cầu lân cận của nó lại vừa vặn là một tinh cầu ngàn hoa vô cùng nổi tiếng.",
    # 091
    "“Lục Tư Niên,” Kỷ Cảnh bất thình lình cất lời, “Thực ra tôi luôn muốn hỏi, tại sao anh lại thích tôi nhiều đến như vậy?”",
    # 092
    "Kỷ Cảnh không hề chậm chạp đần độn, khi mọi hiểu lầm đã được giải tỏa sáng tỏ, cậu mới từ trong những hành động mà Lục Tư Niên từng làm nếm trải ra tình cảm sâu nặng mà anh dành cho mình.",
    # 093
    "Thế nhưng cậu lại không cảm thấy bản thân từng đối xử tốt với Lục Tư Niên nhiều tới mức ấy.",
    # 094
    "“Tôi...” Lục Tư Niên khựng lại một nhịp, sau đó lắc đầu, “Không biết nữa.”",
    # 095
    "“Mới đầu khi quen biết Dịch Nam, tôi cảm thấy cô ấy rất xinh đẹp, sau này phát hiện ra là em thì lại càng thêm phức tạp hơn.”",
    # 096
    "“Cho nên anh cảm thấy khá thất vọng à?” Kỷ Cảnh cố tình chọc ngoáy anh.",
    # 097
    "“Không phải,” Lục Tư Niên đáp lời rất nhanh, có lẽ là ngay cả chính bản thân anh cũng không rõ ngọn nguồn lý do, lời nói thốt ra trở nên chẳng còn theo logic mạch lạc nào, “Trước khi gặp cô ấy, gặp em, chưa từng có ai chủ động tiếp cận tôi, tôi trước giờ luôn chỉ có một mình, không ai kiên trì trò chuyện, ăn cơm cùng tôi, tôi cũng chưa từng tiếp xúc qua phụ nữ, nắm tay, ôm ấp tất cả những lần đầu tiên đều là cùng với em.”",
    # 098
    "“Em an ủi tôi, tặng hoa cho tôi, đưa tôi đi thủy cung, thay tôi ra mặt báo thù, lúc tôi ốm đau thì chăm sóc tôi, giúp tôi trở lại Đệ tam quân đoàn... Chưa từng có bất kỳ ai làm những chuyện này cho tôi cả, có những điều thậm chí ngay cả mẹ tôi cũng chưa từng làm được.”",
    # 099
    "“Trước khi gặp được em, động lực duy nhất để tôi sống tiếp chỉ có báo thù, nhưng em đã cho tôi nhận ra rằng tôi cũng có thể nảy sinh mọi cung bậc cảm xúc, không còn là một cái xác không hồn biết đi nữa, cho nên tôi nghĩ tôi không thể nào đánh mất em được, mất đi em rồi tôi lại sẽ quay trở về bộ dạng của trước ki——”",
    # 100
    "Lời nói của Lục Tư Niên bị đôi môi của Kỷ Cảnh chặn đứng lại, Kỷ Cảnh dùng hai tay chống bên hông anh, đè anh lên nắp xe mà hôn say đắm.",
    # 101
    "“Tôi biết rồi, Lục Tư Niên, anh không thể rời xa tôi được đâu.”",
    # 102
    "Kỷ Cảnh ngẩng đầu lên, vừa khẽ thở dốc vừa nở nụ cười tươi tắn.",
    # 103
    "Ánh trăng vằng vặc mông lung rọi xuống gương mặt Kỷ Cảnh, nụ cười nhẹ nhàng này khiến Lục Tư Niên bất giác nhìn đến mê mẩn đắm say.",
    # 104
    "Anh lại nhớ về nụ cười làm rung động tâm can của thiếu nữ vào buổi chiều tà ngày hôm ấy khi hỏi anh cô ấy có xinh đẹp hay không.",
    # 105
    "Anh đột nhiên cảm thấy còn thiếu một điều gì đó, bàn tay vừa định cử động thì vô tình chạm vào bó hoa hồng đặt trước mui xe.",
    # 106
    "“Ừm.” Lục Tư Niên nhìn sâu vào mắt Kỷ Cảnh, nghiêm túc nói,",
    # 107
    "Một bông hoa hồng được Lục Tư Niên nhẹ nhàng ngắt xuống, cài lên trên vành tai của Kỷ Cảnh.",
    # 108
    "“Tôi yêu em, Kỷ Cảnh.”",
    # 109
    "Lời tác giả:",
    # 110
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-06-21 09:00:00~2023-06-23 20:24:14 nhé~",
    # 111
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Ôn Địch 10 bình; Tễ 7 bình; Quy Ảnh, Bất Ái Nãi Cái Ái Ba Ba, Cột Dương 5 bình; Tựu Ái Nhược Công Cường Thụ, Ngộ Tống., Hạ Mộng Vi Vũ 1 bình;",
    # 112
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 116: Khắc ghi dấu ấn trọn đời\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
