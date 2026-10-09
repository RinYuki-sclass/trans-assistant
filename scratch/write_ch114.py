# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_114\translation.md"

paras = [
    # 000
    "Tập đoàn mà Kỷ Vân Hy đang công tác là con rồng đầu ngành thiết kế hàng đầu toàn đế quốc, đối tượng phục vụ trên thì chạm tới quan chức quý tộc dưới thì trải rộng đến các minh tinh cự phách, quân trang của các quân đoàn đế quốc về cơ bản đều bắt nguồn từ nơi đây.",
    # 001
    "Kỷ Cảnh ngay từ khi mới nhập đoàn đã nghe ngóng được tin tức Đệ tam quân đoàn chuẩn bị may đo lại quân trang mới, mỗi khi quân đoàn thay đổi một vị quân đoàn trưởng thì sẽ tiến hành cải cách kiểu dáng quân phục.",
    # 002
    "Mới nghe thì có vẻ khó tin, nhưng ngẫm nghĩ kỹ lại thì quả thực vô cùng hợp tình hợp lý.",
    # 003
    "Không ngờ đi nhập ngũ rồi mà vẫn có thể gặp lại chị gái ruột trong quân đoàn.",
    # 004
    "Kỷ Cảnh tranh thủ giờ nghỉ trưa lén lút đứng đợi ở một góc khuất kín đáo dưới tòa nhà chính vụ thầm nghĩ như vậy.",
    # 005
    "Tòa nhà chính vụ quản lý vô cùng nghiêm ngặt, từ trong ra ngoài đều thiết lập cơ chế phòng ngự bằng tia hồng ngoại, Kỷ Cảnh vốn dĩ là lén lút trốn ra ngoài, chê trời nắng nóng muốn lẻn vào bên trong chờ, nhưng nghĩ đi nghĩ lại vẫn không dám lấy tính mạng ra đánh cược, đành thò đầu qua mép tường nhìn ra bên ngoài.",
    # 006
    "Chẳng mấy chốc, cậu nghe thấy một tràng tiếng bước chân đều tăm tắp, tiếp đó năm sáu bóng người mặc quân phục nghiêm trang từ bên trong tòa nhà chính vụ sải bước đi ra, Kỷ Cảnh chỉ liếc mắt một cái là nhìn thấy ngay Lục Tư Niên đang đi ở vị trí dẫn đầu.",
    # 007
    "【Kỷ Vân Hy】: Tao tới rồi đấy.",
    # 008
    "Thiết bị đầu cuối vang lên tiếng chuông báo tin nhắn, ngay giây tiếp theo Kỷ Cảnh liền nhìn thấy trước cổng lớn xuất hiện một chiếc xe thương vụ khiêm tốn, Kỷ Vân Hy đi theo sau vài vị Alpha lớn tuổi bước xuống xe.",
    # 009
    "【Kỷ Vân Hy】: Mày đang ở xó xỉnh nào đấy!",
    # 010
    "【Kỷ Vân Hy】: Tao cảm giác ban nãy Lục Tư Niên liếc nhìn tao thêm hai lần đấy.",
    # 011
    "Phía bên kia mọi người đã bắt đầu lần lượt bắt tay chào hỏi theo lễ nghi, Kỷ Vân Hy ngó nghiêng nhìn dáo dác xung quanh.",
    # 012
    "【Anh Cảnh của mày】: Tao đang trốn ở góc tường này, ngay bên tay phải mày nhìn thẳng về phía trước, mày đừng có làm ầm lên đấy, tình cảnh thế này tao làm sao mà nhảy ra được?",
    # 013
    "Cơ thể Kỷ Vân Hy nhanh hơn não, theo bản năng liền nhìn sang hướng Kỷ Cảnh vừa nói, đâu biết rằng những người đứng trước mặt cô đều là một lũ quân nhân Alpha có năng lực quan sát cực kỳ nhạy bén, gần như lập tức phát hiện ra điểm bất thường.",
    # 014
    "“Ai ở đằng kia, bước ra mau.”",
    # 015
    "Sắc mặt Lục Tư Niên chợt lạnh tanh, tính công kích bùng phát trong nháy mắt khiến Kỷ Vân Hy theo bản năng lùi lại phía sau mấy bước.",
    # 016
    "Tình thế rơi vào giằng co, mấy vị tiền bối của Kỷ Vân Hy từng trải qua sóng gió nhiều rồi, chỉ mỉm cười trấn tĩnh đứng nguyên tại chỗ.",
    # 017
    "Đội lấy áp lực khổng lồ, Kỷ Cảnh biết lần này không thể đánh cược việc Lục Tư Niên không phát hiện ra mình nữa, đành phải cắn răng kiên trì chui ra khỏi góc tường.",
    # 018
    "Kỷ Vân Hy biết mình đã gây họa, cũng đành gượng gạo cười trừ hai tiếng, quay sang giải thích với mấy vị tiền bối: “Haha, thật ngại quá các thầy ạ, đây là Kỷ Cảnh, em trai ruột của em, nó thuộc Đệ tam quân đoàn, biết em tới nên muốn qua gặp em một lát.”",
    # 019
    "Mấy vị tiền bối đều rất coi trọng Kỷ Vân Hy, đây cũng chẳng phải lỗi lầm gì mang tính nguyên tắc, nên liền cười xòa cho qua chuyện.",
    # 020
    "Chỉ có thái độ của Lục Tư Niên là khiến cả đám người có chút không tài nào đoán nổi.",
    # 021
    "“Nếu cậu muốn gặp người nhà, có thể làm đơn xin phép từ trước.”",
    # 022
    "Kỷ Cảnh cảm nhận được ánh mắt của Lục Tư Niên, đầu lưỡi chống vào gò má nói: “Xin phép ai cơ, ngài sao?”",
    # 023
    "“Kỷ Cảnh, chú ý quy củ, đoàn trưởng là để cậu gọi như thế đấy à.” Chu Độ thấy thế vội vàng quát ngăn Kỷ Cảnh lại, bình thường chỉ có gã và Kỷ Cảnh hai người thì gọi bừa bãi thế nào cũng được, nhưng hiện tại còn có khách quý đang có mặt.",
    # 024
    "“Cậu có thể làm đơn xin phép tôi.”",
    # 025
    "Lục Tư Niên dường như chẳng hề bận tâm đến cách xưng hô của Kỷ Cảnh, bình tĩnh trả lời.",
    # 026
    "“Ồ, vậy thì thôi đi, phiền phức lắm, một tuần lễ cũng chẳng thấy mặt mũi Lục đoàn trưởng đâu một lần.” Kỷ Cảnh không nhìn vào mắt Lục Tư Niên nữa, cố tình nhấn mạnh ba chữ Lục đoàn trưởng.",
    # 027
    "Kể từ lần trước Lục Tư Niên xuất hiện giúp cậu cài lại thắt lưng xong, Kỷ Cảnh chưa từng gặp lại Lục Tư Niên thêm một lần nào nữa.",
    # 028
    "Vào lúc này chỉ cần Lục Tư Niên có chút EQ thôi là sẽ nhận ra điểm mấu chốt trong câu nói này, đưa ra câu trả lời rằng tuần này mình rất bận rộn, đồng thời nhạy bén phát hiện ra đối phương đang vô cùng chú ý đến chi tiết này của mình.",
    # 029
    "Thế nhưng Lục Tư Niên lại không như vậy, anh im lặng mím chặt đôi môi mỏng, không nói một lời nào.",
    # 030
    "“Nếu đã như vậy, hay là Lục đoàn trưởng cho phép cậu thanh niên này trò chuyện với Vân Hy nhà chúng tôi một lát, chúng ta vào trong trao đổi trước nhé?” Mấy vị tiền bối đều là cáo già lõi đời, sau khi ngửi ra mối quan hệ mập mờ ám muội giữa hai người liền thuận thế đưa ra một bậc thang hòa giải.",
    # 031
    "Chu Độ và một nữ Alpha dáng người cao ráo vội vàng mỉm cười dẫn mọi người đi về phía tòa nhà chính vụ.",
    # 032
    "Rất nhanh tại chỗ chỉ còn sót lại hai chị em Kỷ Vân Hy và Kỷ Cảnh.",
    # 033
    "“Tao bị mày hại chết rồi đấy.”",
    # 034
    "Tâm trạng Kỷ Cảnh không được tốt cho lắm, hoàn toàn trái ngược với thái độ nồng nặc mùi thuốc súng gai góc lúc nói chuyện với Lục Tư Niên, cậu ủ rũ cúi đầu oán trách.",
    # 035
    "Kỷ Vân Hy thì lại đang nghiền ngẫm ánh mắt của Lục Tư Niên nhìn Kỷ Cảnh trước lúc rời đi: “Không phải chứ, mày với Lục Tư Niên sao vẫn chưa làm lành lại với nhau à? Chẳng phải tao đã khuyên mày phải nói chuyện tử tế với anh ta rồi sao.”",
    # 036
    "“Làm lành cái gì?” Kỷ Cảnh nhướng mày, dùng vẻ mặt như thể cô đang nói đùa nhìn Kỷ Vân Hy, “Tao có thể nói chuyện gì với anh ta được chứ, trừ phi tao thật sự đi chuyển giới, biến trở lại thành Dịch Nam.”",
    # 037
    "“Tại sao phải biến trở lại thành Dịch Nam, Lục Tư Niên rõ ràng thích mày mà, mày không nhận ra ánh mắt anh ta nhìn mày sến sẩm đến mức nào à?” Không chỉ sến sẩm, mà còn chất chứa đắng cay chua xót nữa, Kỷ Vân Hy vừa nghĩ vừa xoa xoa hai cánh tay.",
    # 038
    "Kỷ Vân Hy bóc tách từng biểu cảm vi mô của Lục Tư Niên mà cô vừa quan sát được ra phân tích cặn kẽ cho Kỷ Cảnh nghe, cũng chẳng biết Kỷ Cảnh lọt tai được bao nhiêu, nhưng rõ ràng lúc rời đi trông cậu đã không còn bực bội như trước nữa.",
    # 039
    "Nhìn theo bóng lưng của Kỷ Cảnh, Kỷ Vân Hy bất đắc dĩ thở dài một hơi thật dài, dựa vào mức độ hiểu biết của cô về Kỷ Cảnh, cô biết hiện tại Kỷ Cảnh để tâm đến Lục Tư Niên nhiều tới nhường nào.",
    # 040
    "Cô cũng biết với tính cách kiêu ngạo của Kỷ Cảnh, cậu tuyệt đối không thể nào chủ động mở lời giãi bày với Lục Tư Niên trước được.",
    # 041
    "Nhưng cô không hề muốn nhìn thấy Kỷ Cảnh vì chuyện tình cảm mà phiền muộn âu sầu, cô muốn nhìn thấy một Kỷ Cảnh vô lo vô nghĩ thực sự của ngày xưa hơn.",
    # 042
    "Bởi vậy chuyến đi đến Đệ tam quân đoàn lần này, cô còn mang theo một mục đích khác.",
    # 043
    "Theo địa điểm tiền bối gửi tới, Kỷ Vân Hy bước vào tòa nhà hành chính đi tới phòng họp, cùng với các vị tiền bối chốt lại bản thiết kế quân trang cuối cùng của Đệ tam quân đoàn.",
    # 044
    "Lúc tan họp, Kỷ Vân Hy chặn đường Lục Tư Niên lại.",
    # 045
    "“Lục đoàn trưởng, có thể nói chuyện riêng một lát được không, về chuyện của Kỷ Cảnh.”",
    # 046
    "...",
    # 047
    "Chuyện Kỷ Cảnh trưa nay tự ý trốn khỏi doanh trinh sát bị bại lộ, cậu bị phạt nhốt vào khoang rèn luyện sức bền suốt ba tiếng đồng hồ.",
    # 048
    "Lúc bước ra ngoài, đội trưởng nhìn thành tích hiển thị trên màn hình quang học im lặng một hồi lâu, không nói thêm lời nào, chỉ bảo tối nay cậu không cần tập luyện nữa, cứ về ký túc xá nghỉ ngơi đi.",
    # 049
    "Kỷ Cảnh chỉ mong có thế, trở về ký túc xá liền tắm rửa gột sạch toàn bộ mồ hôi nhễ nhại trên người, bên hông quấn một chiếc khăn tắm bước ra ngoài.",
    # 050
    "【Kỷ Vân Hy】: Tao về rồi đấy nhé.",
    # 051
    "【Kỷ Vân Hy】: Để lại cho mày một bất ngờ đấy, đến lúc đó nhớ bao tao một bữa ra trò đấy nhé.",
    # 052
    "Kỷ Cảnh vừa bật thiết bị đầu cuối lên liền nhảy ra tin nhắn của Kỷ Vân Hy, lại còn là tin nhắn gửi từ ba tiếng trước.",
    # 053
    "Cậu tựa vào đầu giường, mất tập trung suy nghĩ về những lời Kỷ Vân Hy đã nói.",
    # 054
    "Lục Tư Niên thích cậu sao?",
    # 055
    "Thật ư? Nhưng người Lục Tư Niên thích chẳng phải là Dịch Nam sao, rõ ràng đã thích đến mức cầu hôn Dịch Nam rồi cơ mà... Nhưng tại sao Lục Tư Niên lại tự nguyện để cậu đánh dấu trọn đời? Lại còn cố ý gạt cậu ra khỏi vụ việc của Lâm Diên Sơn, trước đó còn giúp cậu thắt thắt lưng, sáng nay lại dùng ánh mắt giống như Kỷ Vân Hy miêu tả nhìn cậu.",
    # 056
    "Khoan đã,",
    # 057
    "Trong đầu Kỷ Cảnh đột nhiên trào dâng một phỏng đoán hoang đường —— mẹ nó chứ, chẳng lẽ Lục Tư Niên xem cậu thành thế thân của Dịch Nam rồi đấy chứ??!",
    # 058
    "Người phụ nữ mình yêu là giả mạo, nhưng lại không buông bỏ được, đành phải vương vấn nhớ nhung không dứt với chính kẻ lừa đảo.",
    # 059
    "Phỏng đoán này vừa thành hình, Kỷ Cảnh càng nghĩ càng thấy hợp lý, vừa bàng hoàng vừa tức giận sôi máu.",
    # 060
    "Đang chuẩn bị nổi trận lôi đình thì trên thiết bị đầu cuối đột nhiên xuất hiện một yêu cầu kết bạn.",
    # 061
    "Kỷ Cảnh vừa nhìn ảnh đại diện quen thuộc kia liền nhận ra ngay là Lục Tư Niên, bên trên hiển thị là do Chu Độ giới thiệu qua.",
    # 062
    "Kỷ Cảnh chầm chậm bình tĩnh lại, bộ não vận hành với tốc độ cao, sau đó nhấn đồng ý.",
    # 063
    "Rất nhanh, Lục Tư Niên liền gửi tới một dòng tin nhắn.",
    # 064
    "【Lục Tư Niên】: Kỷ Cảnh, chúng ta có thể nói chuyện một chút được không.",
    # 065
    "Kỷ Cảnh hít sâu một hơi.",
    # 066
    "【Anh Cảnh của mày】: Nói chuyện gì?",
    # 067
    "【Lục Tư Niên】: Mở cửa.",
    # 068
    "...",
    # 069
    "Lục Tư Niên đứng giữa hành lang ký túc xá vắng lặng, bóng lưng cao lớn nổi bật giữa dãy hành lang tĩnh mịch trông có vẻ cô quạnh khác thường.",
    # 070
    "Anh lặng lẽ nhìn số phòng ký túc xá trước mặt, bên trên hiện tại chỉ hiển thị duy nhất tên của một mình Kỷ Cảnh.",
    # 071
    "Những lời Kỷ Vân Hy nói vào giờ phút này vẫn không ngừng lởn vởn bên tai anh, đi kèm với nhịp tim đang đập dồn dập trong lồng ngực.",
    # 072
    "“Lục Tư Niên, Kỷ Cảnh rất thích anh, tuy rằng trước đây tôi từng nghi ngờ nó theo đuổi anh là xuất phát từ tâm lý trả thù, nhưng sau đó tôi phát hiện ra nó thực sự thích anh.”",
    # 073
    "“Tôi đã hỏi ba tôi rồi, Kỷ Cảnh đem năm năm tương lai của nó đổi lấy lá phiếu thuận của ba, anh phải biết rằng từ nhỏ nó đã vô cùng bài xích việc tiếp quản gia tộc, sau này khi tin tức anh là Omega được công bố tôi mới nhận ra nó bỏ phiếu là vì anh.”",
    # 074
    "“Từ rất lâu trước đây Kỷ Cảnh đã từng nói với tôi, nó biết người anh thích là Dịch Nam, một khi biết được chân tướng thì hai người nhất định sẽ chia tay, ngày hôm đó nó về nhà bảo với tôi nó đã chia tay với anh rồi, tôi nhận ra nó vô cùng đau lòng, khoảng thời gian đó ngày nào cũng mất hồn mất vía, quầng thâm mắt to đùng. Ngay cả lần này đến Đệ tam quân đoàn, nó cũng thừa nhận với tôi là vì anh mà tới.”",
    # 075
    "“Tôi nhận ra anh cũng thích nó có đúng không? Vậy rốt cuộc anh thích Dịch Nam hay là thích nó, đây là điều mà Kỷ Cảnh vẫn luôn bận tâm, nó cảm thấy anh chỉ thích Dịch Nam chứ không thích nó, nếu như người anh thích là nó, vậy thì tôi hy vọng anh có thể chủ động nói cho nó biết, với tính cách của Kỷ Cảnh thì anh rất khó có thể khiến nó chủ động mở lời trước.”",
    # 076
    "...",
    # 077
    "Một tiếng “cạch” vang lên, cánh cửa mở ra, cách một khe cửa không lớn cũng không nhỏ, ánh mắt của hai người cứ thế giao nhau giữa không trung.",
    # 078
    "Yết hầu Lục Tư Niên khẽ trượt lên xuống, bước nhanh một bước tiến vào trong phòng ký túc xá, rồi khép cửa phòng lại.",
    # 079
    "“Anh muốn nói gì với tôi.” Kỷ Cảnh hiếm hoi cảm thấy không tự nhiên, trên người Lục Tư Niên vẫn đang mặc bộ quân phục sĩ quan chỉnh tề nghiêm trang, còn cậu thì chỉ quấn độc một chiếc khăn tắm bên hông, nhìn thế nào cũng thấy kỳ quặc.",
    # 080
    "“Kỷ Cảnh,” Lục Tư Niên không hề có nửa điểm do dự, đi thẳng vào vấn đề chính, “Tôi không hề không thích em.”",
    # 081
    "Hai mắt Kỷ Cảnh xoẹt một cái trợn tròn xoe: “Cái... cái gì.”",
    # 082
    "“Tôi không hề không thích em,” Lục Tư Niên sải bước tiến lên, áp sát lại gần Kỷ Cảnh, lặp lại từng chữ, “Người tôi thích từ trước đến nay luôn là em, không phải Dịch Nam.”",
    # 083
    "Khoảnh khắc này Kỷ Cảnh cái gì cũng đã nghĩ thông suốt rồi, cậu không lùi bước nữa, mặc cho Lục Tư Niên áp sát về phía mình, cậu nhìn thẳng vào mắt Lục Tư Niên, bình tĩnh lại:",
    # 084
    "“Thế sao, tại sao lại nói như vậy.”",
    # 085
    "Hơi thở của Lục Tư Niên ở ngay trong gang tấc, gần đến mức Kỷ Cảnh vẫn có thể ngửi thấy mùi tin tức tố của Lục Tư Niên.",
    # 086
    "Chẳng hiểu vì sao, cậu cảm thấy tin tức tố của Lục Tư Niên lại càng thêm quyến rũ mê người.",
    # 087
    "Anh nói: “Bởi vì tôi ngay từ đầu đã nghi ngờ em là Kỷ Cảnh, sau này tôi đã xác định chắc chắn Dịch Nam nhất định là em, tôi thừa nhận lúc ban đầu tôi từng do dự đắn đo, nhưng tôi xác định người tôi thích chính là em trong bộ dạng Dịch Nam.”",
    # 088
    "Kỷ Cảnh nắm chặt nắm đấm, ánh mắt bởi vì tin tức tố trong phút chốc trở nên tối sầm mông lung, cậu mấp máy môi hỏi: “Nghi ngờ tôi từ lúc nào?”",
    # 089
    "“Ngày hôm đó bước ra khỏi phòng đấu vật, tôi đã ngửi thấy tin tức tố của em, có lẽ em không biết tin tức tố của mình mang mùi vị gì, nhưng tôi biết đó là mùi rượu Tequila, giống hệt mùi hương trên người em lúc này.”",
    # 090
    "Lục Tư Niên ngửi mùi tin tức tố rượu Tequila đang thoang thoảng quẩn quanh nơi đầu mũi, hai mắt không tài nào khống chế nổi bị hun đỏ lên, giọng nói chẳng biết tự lúc nào đã nhuốm màu dục vọng, chóp mũi bất giác muốn hướng về phía sau gáy Kỷ Cảnh thăm dò.",
    # 091
    "Hai người tuy rằng đều đã tiêm thuốc kháng mẫn, nhưng sức hút tin tức tố từ dấu ấn trọn đời là sự ràng buộc bất khả kháng chỉ thuộc về riêng hai người bọn họ.",
    # 092
    "“Tôi vẫn luôn cố tình không vạch trần em, là vì tôi tưởng rằng em tiếp cận để trêu đùa trả thù tôi, một khi tôi vạch trần, chúng ta sẽ chấm dứt tại đó.”",
    # 093
    "Giọng nói trầm thấp của Lục Tư Niên rung lên từ lồng ngực, Kỷ Cảnh lúc này mới nhận ra lồng ngực của hai người sớm đã dán sát vào nhau.",
    # 094
    "“Kỷ Cảnh,” Lục Tư Niên kìm nén hỏi, “Em có thích tôi không.”",
    # 095
    "Em chỉ cần nói thích là được rồi, chỉ cần em thích tôi, tôi có thể không để tâm đến bất cứ điều gì, không để tâm chuyện năm xưa vì sao em lại lăng mạ mẹ tôi, không để tâm vì sao em lại cố ý giả dạng thành phụ nữ để tiếp cận tôi.",
    # 096
    "Kỷ Cảnh hít sâu một hơi, khoang mũi bị mùi tin tức tố thuộc về riêng một mình Lục Tư Niên chiếm trọn, cậu nghiến chặt răng hàm sau, vừa giận Lục Tư Niên không tin bản thân thích anh, lại vừa giận chính mình tại sao lại ngu ngốc hiểu lầm lâu đến thế, hung dữ nói: “Anh có thể bớt khúc gỗ đi một chút được không, anh tự nói xem tôi có thích anh hay không hả?”",
    # 097
    "Dứt lời Lục Tư Niên liền không còn cách nào khắc chế nổi nữa, giữ chặt lấy sau gáy cậu rồi áp môi hôn lên môi cậu.",
    # 098
    "Thế tấn công của Lục Tư Niên vô cùng mạnh mẽ, Kỷ Cảnh cũng không chịu yếu thế, hai người hôn nhau hệt như đang đánh trận, ngay giây tiếp theo cả hai liền ngã nhào xuống chiếc giường nhỏ của Kỷ Cảnh, hôn đến long trời lở đất không dứt ra nổi, tựa như đang phát tiết hết mọi cảm xúc kìm nén bấy lâu nay.",
    # 099
    "“Anh nghe cho kỹ đây, tôi thích anh.” Kỷ Cảnh xé toạc cổ áo Lục Tư Niên, vùi đầu ghé sát vào tuyến thể sau gáy anh.",
    # 100
    "“Lục Tư Niên, anh đã bị tôi đánh dấu trọn đời rồi.” Cậu nghiến răng, cọ xát vào tuyến thể của Lục Tư Niên, sau đó thuận theo sự cám dỗ của tin tức tố, cắn phập một cái thật mạnh làm rách nốt gồ ấy.",
    # 101
    "Lục Tư Niên nhẫn nhịn thốt lên một tiếng “Ừm”, nếu Kỷ Cảnh phân biệt kỹ càng thì có thể nhận ra trong tiếng ừm này mang theo một tia ý cười rất khẽ.",
    # 102
    "“Cho dù anh bị tôi đánh dấu trọn đời rồi cũng không xong đâu.” Kỷ Cảnh ngồi bật dậy khỏi giường, gạt phăng cánh tay Lục Tư Niên đang siết chặt lấy eo mình ra, cắn xong liền vô tình tuyên bố.",
    # 103
    "“Trước đây tôi theo đuổi anh lâu như vậy, còn vì anh mà đuổi tới tận nơi này, kết quả cả một tuần trời anh cũng không thèm đến thăm tôi một lần, lần này phải đổi lại đến lượt anh rồi, anh thấy sao hả?”",
    # 104
    "Kỷ Cảnh khoanh hai tay trước ngực, nhướng mày nhìn Lục Tư Niên.",
    # 105
    "Lời tác giả:",
    # 106
    "Phía sau đôi chim cu chơi trò đuổi bắt tỏ tình, đại khái còn khoảng hai ba bốn chương nữa.",
    # 107
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-06-14 22:57:02~2023-06-17 22:34:36 nhé~",
    # 108
    "Cảm ơn thiên thần nhỏ ném lựu đạn: Đạt Lạp Đạt Lạp Y 1 cái;",
    # 109
    "Cảm ơn các thiên thần nhỏ ném địa lôi: Bảo Tử YYDS, Đạt Lạp Đạt Lạp Y 1 cái;",
    # 110
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Ôn Địch, Ân Nỉ Ân Nỉ Ân Nỉ 10 bình; Lam Phong Tuyết Ảnh, Duy Chỉ, Đạt Lạp Đạt Lạp Y 5 bình; Quyện Từ, Nhuyễn Manh Đích Anh Hủ, Cố Phong Tranh 1 bình;",
    # 111
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 114: Thăm dò và ghen tuông\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
