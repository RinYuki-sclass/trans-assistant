import os
import sys

trans_paras = [
    "Sương đen đặc quánh bao phủ khắp các con phố hoang tàn đổ nát của tinh cầu A, phóng tầm mắt ra xa chỉ có thể miễn cưỡng phác họa được đường nét đại khái của những công trình kiến trúc xung quanh, thế nhưng bên tai lại có thể nghe thấy rõ ràng những tiếng gầm rú kỳ quái chói tai.",
    "Tiếng gầm rú dần dần áp sát, đó không chỉ là một tiếng đơn lẻ mà là cả một bầy hàng trăm con, phát ra âm thanh cực kỳ đinh tai nhức óc như muốn xé toạc màn sương đen ập tới.",
    "“Rầm——”",
    "Tòa nhà bên cạnh đột ngột sụp đổ, ngay sau đó, một chiếc xe màu đen tông vỡ bức tường, lao vút đi trong tiếng gầm rú.",
    "Phía sau chiếc xe này, vô số quái vật đang điên cuồng đuổi theo bám riết. Những “quái vật” này chỉ có thể miễn cưỡng nhìn ra chút hình dáng con người, nhưng đã hoàn toàn không còn thuộc về phạm trù nhân loại. Tứ chi của chúng vặn vẹo thành những tư thế kỳ quái quái đản, đôi con ngươi đen kịt như vật chết trừng trừng nhìn chằm chằm chiếc xe phía trước, như thể đó là món sơn hào hải vị tuyệt thế.",
    "Lúc này, bên trong chiếc xe màu đen có hai người đang ngồi. Hoàng Mao đang cầm lái căng thẳng đến mức hai hàm răng va vào nhau lập cập, hắn chốc chốc lại nhìn vào gương chiếu hậu, rồi lại liếc mắt nhìn người đàn ông tóc đen bên cạnh, cứ như vậy kéo dài suốt mấy phút đồng hồ, mới ngập ngừng do dự mở miệng hỏi cậu: “Sở Niên Niên, cậu chắc chắn chúng ta phải làm thế này chứ? Nếu dẫn cả đàn tang thi này về phía Cố Xuyên, bọn họ sẽ chẳng ai sống sót nổi đâu.”",
    "“Cẩn thận lái xe đi.”",
    "Giọng nói của người đàn ông được gọi là Sở Niên Niên vô cùng êm tai, thanh âm nũng nịu ngây ngô mang chất giọng sữa ngọt ngào, bất cứ ai nghe thấy cũng đều nghĩ rằng cậu đang làm nũng.",
    "Nhìn từ góc độ của Hoàng Mao, có thể thấy được góc nghiêng hoàn mỹ như tượng tạc của Sở Niên Niên. Hắn không kìm được nhìn đến ngây người, thầm nghĩ hèn chi trước mạt thế cậu lại là minh tinh. Ngay khi hắn còn đang si mê ngắm nhìn, một đôi mắt hồ ly u ám quỷ dị bỗng xộc thẳng vào tầm mắt hắn.",
    "“Anh Nghiêm, anh không nói gì, là hối hận rồi sao?” Sở Niên Niên chớp chớp mắt, nét mặt tàn nhẫn hiểm độc ban nãy thoắt cái đã biến mất không còn tăm hơi, thay vào đó là vẻ ngây thơ giả tạo. Cậu mang gương mặt vừa thuần khiết vừa quyến rũ chết người, dùng giọng điệu châm dầu vào lửa mà nói:",
    "“Nhưng anh đừng quên, Cố Xuyên đã nạy hết toàn bộ người của anh đi rồi. Nếu không có anh ta, sao anh lại rơi vào cảnh phải đơn độc sinh tồn thế này, đây chẳng phải là biến tướng muốn lấy mạng anh sao?”",
    "“Dẫn tang thi qua đó, đợi bọn họ chết hết rồi, chúng ta sẽ cướp sạch vật tư của bọn họ rồi chạy đến căn cứ khác. Như vậy ít nhất ba tháng tới chúng ta không phải lo cơm ăn áo mặc, cứ thế lái xe thẳng đến thành phố B.” Thấy Hoàng Mao vẫn còn đôi chút do dự, Sở Niên Niên tiếp tục dụ dỗ.",
    "Hoàng Mao vốn là một dị năng giả hệ Thổ cấp B. Giữa thời mạt thế tang thi giăng đầy này, người thức tỉnh dị năng vốn đã ít lại càng ít, huống chi hắn còn là dị năng giả cấp B cực kỳ hiếm có. Dựa vào dị năng của mình, từ một tên lưu manh chuyên lừa gạt trộm cắp, hắn một bước trở thành một trong những nhân vật dẫn đầu của căn cứ thành phố C, thu nạp mấy dị năng giả cấp thấp làm đàn em.",
    "Sở Niên Niên cũng là một thành viên trong đội của bọn họ, chỉ có điều cậu tương đối đặc biệt. Cậu chẳng có bất kỳ dị năng nào, cũng không cần phải ra ngoài tìm kiếm vật tư, chỉ dựa vào nhan sắc tuyệt mỹ đã khiến Hoàng Mao cam tâm tình nguyện giữ cậu lại bên cạnh.",
    "Mọi chuyện bắt nguồn từ nửa tháng trước, hôm ấy tiểu đội của bọn họ nhận nhiệm vụ ra ngoài thành tiếp nhận vật tư, thế nhưng giữa đường lại đụng độ phải đợt triều tang thi. Hoàng Mao thấy tình hình không ổn liền một mình lái xe chuồn trước, những người còn lại suýt chút nữa bỏ mạng toàn quân, may mắn thay đụng phải Cố Xuyên ra tay cứu giúp mới giữ được mạng sống.",
    "Các đội viên đưa Cố Xuyên trở về căn cứ, sau đó vạch trần bộ mặt thật của Hoàng Mao trước mặt mọi người. Hành vi của Hoàng Mao khiến quần chúng phẫn nộ, sau khi được mọi người bỏ phiếu, hắn đã bị trục xuất khỏi căn cứ. Trong khi đó, Cố Xuyên dựa vào cấp bậc dị năng thâm sâu khôn lường đã nhanh chóng trở thành nhân vật cốt cán của căn cứ trong một thời gian ngắn.",
    "Do hệ thống phòng thủ của căn cứ sắp sửa sụp đổ, mọi người cấp thiết cần một chỗ dừng chân mới, thế nên vài ngày trước, Cố Xuyên đã dẫn theo mấy người thuộc hạ cũ ra ngoài thành.",
    "Từ một đội trưởng cao cao tại thượng một sớm biến thành kẻ lang thang đầu đường xó chợ, thuộc hạ dưới trướng lại còn chạy theo người khác, Hoàng Mao vì thế mà mang lòng oán hận Cố Xuyên thấu xương, xoa tay nghiến răng muốn cho anh một bài học. Đúng lúc này lại bị Sở Niên Niên châm ngòi thổi gió, hai người vừa ăn khớp với nhau, lập tức quyết định bắt nhóm người Cố Xuyên phải trả giá đắt.",
    "Nghĩ đến ba tháng tới không cần phải đối mặt liều mạng với tang thi, Hoàng Mao rốt cuộc cũng hạ quyết tâm. Hắn nhấn mạnh chân ga, tăng tốc lao thẳng về phía trạm trung chuyển nơi nhóm người Cố Xuyên đang dừng chân.",
    "“Tôi còn một câu hỏi nữa,” Hoàng Mao nhìn về phía trước, hỏi: “Cậu với Cố Xuyên có thù oán gì, mà khiến cậu hận đến mức muốn giết chết anh ta thế?”",
    "Sở Niên Niên nghe vậy liền lập tức sa sầm mặt mày. Cậu cười như không cười nhìn tấm kính chắn gió phía trước, trong tầm mắt, bóng hình khiến cậu ngày đêm mong nhớ kia đang dần dần trở nên rõ nét.",
    "Cậu thì thầm bằng một thanh âm nhỏ đến mức không thể nghe thấy——",
    "“Bởi vì, em muốn anh ấy nhìn thấy em mà.”",
    "-",
    "Theo tiếng ầm ầm của đàn tang thi ập đến, nhóm người Cố Xuyên đã nhạy bén bắt được động tĩnh. Bọn họ đồng loạt nhìn qua những kẽ hở thủng lỗ chỗ của nhà kho ra bên ngoài, đôi mắt không kìm được trừng trừng đờ đẫn, ngay lập tức cất tiếng gọi lớn tên Cố Xuyên.",
    "“Cố Xuyên, nhìn mau!——”",
    "“Trời đất ơi, ở đâu ra mà lắm tang thi thế này.”",
    "“Hu hu hu oa, chết chắc rồi! Bọn chúng nhìn một cái là biết đang nhắm thẳng về phía chúng ta rồi, tôi mới hơn hai mươi tuổi thôi, tôi không muốn chết đâu!”",
    "Bầu không khí bên trong nhà kho kín mít chìm vào nỗi tuyệt vọng như chết chóc, trên gương mặt mỗi người đều tràn ngập vẻ sợ hãi và không cam lòng.",
    "Lúc này, trên nóc nhà kho có một người đàn ông mặc bộ đồ bảo hộ màu đen đang đứng. Đôi mắt đen hẹp dài của anh lặng lẽ nhìn về phía đàn tang thi đang cuồn cuộn tràn tới cách đó không xa. Đột nhiên, ánh mắt anh tối sầm lại, khóa chặt vào một chiếc xe màu đen kín đáo.",
    "“Không kịp nữa rồi. Lục Thiên dựng tường đất, Lý Viện Viện hỗ trợ, những dị năng giả hệ tấn công còn lại phân tán giữ vị trí.” Giọng nói của người đàn ông trầm thấp êm tai như rượu vang ủ lâu năm, rõ ràng đang ở vào tình thế ngàn cân treo sợi tóc nhưng vẫn điềm tĩnh như xưa, tựa như một con sói trưởng thành đang lặng lẽ lượn quanh chờ đợi thời cơ cắn trả.",
    "Sau khi nghe thấy lời của Cố Xuyên, mọi người đều không hẹn mà cùng bình tĩnh trở lại. Bọn họ nhanh chóng tuân theo mệnh lệnh của Cố Xuyên vây chặt lấy nhà kho. Vừa định hỏi Cố Xuyên bước tiếp theo phải làm gì thì đã thấy anh chẳng biết từ lúc nào đã một mình xông thẳng vào đàn tang thi đang ùa tới.",
    "“Điên rồi, điên thật rồi! Cố đội muốn làm gì vậy, không có anh ấy thì chúng ta biết phải làm sao bây giờ!?” Lý Viện Viện, người phụ nữ duy nhất trong đội, hai mắt đỏ hoe vì suy sụp.",
    "Cậu thiếu niên Lục Thiên bên cạnh lại như mất hồn, cậu nhìn chằm chằm vào bóng lưng của Cố Xuyên, lẩm bẩm: “Không, anh ấy không phải muốn bỏ rơi chúng ta, anh ấy muốn một mình dụ đàn tang thi đi chỗ khác.”",
    "Lý Viện Viện ngẩn người, đảo mắt nhìn sang, quả nhiên phần lớn đàn tang thi kia đều bị động tĩnh của Cố Xuyên dụ sang phía đối diện.",
    "Thân ảnh dẻo dai mạnh mẽ của Cố Xuyên luồn lách giữa bầy tang thi dày đặc. Bất cứ nơi nào anh đi qua, lôi hỏa kinh thiên đều nổ tung thành hình vòng cung giữa đám tang thi. Anh chưa từng dừng lại dù chỉ một khắc, đôi con ngươi đen kịt nhìn trừng trừng vào chiếc xe màu đen kia hệt như đang khóa chặt con mồi.",
    "Không ai có thể đo lường nổi rốt cuộc anh còn che giấu thực lực thâm sâu đến mức nào, anh bí ẩn tựa như một vùng biển sâu thăm thẳm và tịch mịch.",
    "Sấm sét với tốc độ càn quét quét sạch từng mảng tang thi, nổ tung khiến chúng văng tung tóe khắp nơi, rất nhanh chóng Hoàng Mao đã nhìn thấy Cố Xuyên đang lao thẳng về phía mình trong gương chiếu hậu.",
    "“Mẹ kiếp, Niên Niên, hắn phát hiện ra chúng ta rồi, làm sao bây giờ!” Hoàng Mao hoảng sợ nhìn sang Sở Niên Niên.",
    "“Ồ, vậy thì anh đi chết đi.”",
    "“Cậu nói cái gì?”",
    "Sở Niên Niên đột nhiên quay đầu lại nở nụ cười với hắn: “Tôi bảo, vậy thì anh đi chết đi cho rồi.”",
    "Nói dứt lời, không đợi Hoàng Mao kịp phản ứng, cậu bỗng nhiên mở toang cửa xe, nhảy phắt xuống khỏi chiếc xe đang chạy chầm chậm giữa bầy tang thi.",
    "Ngay sau đó, tiếng thét kinh hãi đầy đau đớn của Hoàng Mao truyền đến từ phía trước. Chỉ thấy một đám tang thi như thể bị ai đó điều khiển bỗng nhiên tăng tốc độ, từ cánh cửa xe đang mở toang mà bổ nhào vào trong xe——",
    "Cùng lúc đó, Sở Niên Niên cảm giác cổ mình bị một bàn tay to lớn đầy sức mạnh siết chặt lấy. Cậu thuận thế quay đầu lại, một gương mặt điển trai lạnh lùng góc cạnh đập ngay vào tầm mắt cậu.",
    "“Là cậu.” Đôi mắt Cố Xuyên xẹt qua một tia lạnh lẽo đầy thâm ý.",
    "Bàn tay trên cổ siết chặt thêm đôi chút, Sở Niên Niên cảm thấy cả người mình đã bị Cố Xuyên lôi đi rồi ném vào một cửa tiệm bỏ hoang.",
    "Do quán tính, Sở Niên Niên ngã nhào xuống đất, mặt đất thô ráp khiến lòng bàn tay trắng nõn của cậu rách toạc ra những vệt máu chói mắt. Cậu cũng không thèm đứng dậy, cứ thế ngước nhìn Cố Xuyên từ dưới lên.",
    "Cố Xuyên đứng ngược sáng, ngồi xổm xuống trước mặt cậu, sau đó túm chặt lấy cổ áo cậu xách bổng lên.",
    "“Tang thi bên ngoài là do cậu điều khiển.”",
    "Cố Xuyên không dùng câu nghi vấn, mà khẳng định chắc nịch tội trạng của Sở Niên Niên.",
    "Điểm này không hề khó nhận biết, hành động của đợt tang thi kia rõ ràng có mục đích, hành động vừa rồi khi chúng đồng loạt phớt lờ Sở Niên Niên mà lao vào cắn xé Hoàng Mao mang theo một sự ăn ý quỷ dị.",
    "Mà khi anh rời khỏi nhà kho, bầy tang thi vốn đang ùa về phía nhà kho lại không hẹn mà cùng đuổi theo anh, chứng tỏ——",
    "“Cậu muốn lấy mạng tôi.”",
    "Cố Xuyên túm chặt lấy Sở Niên Niên, từng tấc từng tấc áp sát lại gần cậu, hơi thở ấm nóng khi nói chuyện phả thẳng lên chóp mũi thanh tú của Sở Niên Niên.",
    "Sở Niên Niên chưa bao giờ ở cự ly gần Cố Xuyên đến thế này. Cậu kìm nén sự cố chấp nơi đáy mắt, chợt mếu máo, tủi thân nói: “Cố ca ca, anh làm em đau rồi.”",
    "Cố Xuyên nghe vậy, theo bản năng liền nới lỏng lực tay.",
    "Ngay trong khoảnh khắc ấy, Sở Niên Niên lập tức vùng ra khỏi sự kiềm tỏa của Cố Xuyên, lùi về sau một bước lớn. Liền sau đó, bên ngoài cánh cửa sắt đóng chặt phát ra tiếng vang ầm ầm long trời lở đất.",
    "Đó là tang thi đang tông cửa.",
    "Sắc mặt Cố Xuyên tối sầm lại, quay đầu nhìn về phía Sở Niên Niên, chỉ thấy Sở Niên Niên đang cười như không cười nhìn anh.",
    "“Nếu như ca ca vĩnh viễn không vừa mắt em, vậy thì hôm nay anh cứ——”",
    "Đi chết đi.",
    "Bờ môi Sở Niên Niên mấp máy, thế nhưng lại phát hiện ra hai chữ cuối cùng bất luận thế nào cũng không thể thốt ra khỏi miệng, tựa như bị một luồng sức mạnh vô hình nào đó chặn đứng lại. Mà mọi thứ xung quanh, bao gồm cả Cố Xuyên, đều dừng lại bất động.",
    "【Oa hô la hô, hê hê, Mật Bảo ta lại có ký chủ mới rồi nè!】",
    "Cùng với tiếng nhạc đệm quen thuộc, một chú bướm rực rỡ sắc màu tỏa ánh hào quang đột nhiên xuất hiện giữa không trung. Nó bay lượn quanh Sở Niên Niên mấy vòng, như thể đang bước đầu tìm hiểu ký chủ mới của mình.",
    "【Ý thức tự chủ của nhân vật phản diện đang thức tỉnh——】",
    "【Hồi tưởng cốt truyện—— Kịch bản yêu đương đang truyền tải, 3, 2, 1】",
    "Trước mắt Sở Niên Niên bỗng nhiên lóe lên một đạo bạch quang chói lòa, cậu thuận thế nhắm mắt lại, cảm thấy mình dường như đã bước vào một đường hầm thời không. Và ở bên trong đó, cậu đã hiểu rõ ngọn ngành mọi chuyện, hóa ra bản thân chỉ là một nhân vật phản diện độc ác trong cuốn tiểu thuyết đam mỹ mang tên 《Ngược Ái: Người Tình Thế Thân Của Đại Lão Mạt Thế》.",
    "《Ngược Ái: Người Tình Thế Thân Của Đại Lão Mạt Thế》 kể về câu chuyện trong thời mạt thế, một tiểu thụ kiên cường đáng yêu là Lục Thiên bất ngờ thức tỉnh dị năng hệ Thổ, trong một lần rơi vào hiểm cảnh đã được nhân vật chính công Cố Xuyên cứu mạng. Dưới sự an bài của số phận, cậu được Cố Xuyên lựa chọn, cùng anh ra khỏi thành phố để thăm dò địa điểm căn cứ mới. Qua từng lần đối mặt với hiểm nguy, Lục Thiên đã bị Cố Xuyên thu hút sâu sắc, đồng thời phát hiện Cố Xuyên dành cho mình sự thiên vị đặc biệt. Ngay khi hai người vừa nảy sinh tình cảm và chuẩn bị định ước cả đời, Lục Thiên lại bất ngờ phát hiện hóa ra mình chỉ là kẻ thế thân cho bạch nguyệt quang đã mất sớm của Cố Xuyên. Sự quan tâm chăm sóc mà Cố Xuyên dành cho cậu chỉ vì cậu có vài phần tương đồng với bạch nguyệt quang kia. Lục Thiên vì thế mà đau đớn tột cùng, quyết tâm dứt áo ra đi cắt đứt quan hệ với Cố Xuyên, và phía sau đó là cả một chuỗi quy trình truy thê hỏa táng tràng dài dằng dặc.",
    "Còn cậu, Sở Niên Niên, lại chính là nhân vật phản diện lớn nhất trong cuốn sách này. Là em trai ruột của bạch nguyệt quang của Cố Xuyên, từ thuở nhỏ lần đầu gặp gỡ Cố Xuyên, cậu đã nhen nhóm lòng sùng bái mãnh liệt đối với anh. Đó không phải là tình yêu theo định nghĩa truyền thống, mà là một thứ tình cảm khó lòng gọi tên. Cậu khao khát vô cùng được Cố Xuyên đoái hoài nhìn mình một lần, nhưng dưới những lần lạnh lùng cự tuyệt của Cố Xuyên, sự cố chấp tà ác trong lòng cậu đã sinh sôi nảy nở, quyết tâm bắt Cố Xuyên phải chết trong tay mình. Trải qua hết lần này đến lần khác mưu toan hãm hại, Cố Xuyên rốt cuộc không thể nhẫn nhịn thêm được nữa mà ra tay hạ sát, Sở Niên Niên cuối cùng cũng phải nhận lấy kết cục chết vô cùng thê thảm.",
    "Cố Xuyên xuất thân từ danh môn thế gia, vào năm học cấp ba vì một vài biến cố mà chuyển đến học tại thị trấn nhỏ nơi cậu và chị gái sinh sống, từ đó quen biết chị gái cậu cùng với cậu.",
    "Sở Niên Niên bị khí chất người anh trai độc nhất vô nhị trên người Cố Xuyên thu hút, thế nhưng trong mắt Cố Xuyên xưa nay chỉ nhìn thấy mỗi chị gái của cậu, thái độ đối với cậu luôn có cũng được mà không có cũng chẳng sao, thậm chí có thể nói là chán ghét cậu, đối với yêu cầu muốn làm đàn em đi theo anh của cậu thì anh xem như điếc không nghe thấy.",
    "Mãi cho đến khi Cố Xuyên tốt nghiệp trở về gia tộc tiếp quản sản nghiệp, chị gái vì bạo bệnh mà qua đời, cậu và Cố Xuyên cũng cắt đứt liên lạc từ dạo đó.",
    "Sở Niên Niên bỏ học cấp ba giữa chừng, dựa vào ngoại hình xuất chúng mà ký hợp đồng với một công ty giải trí, lăn lộn trở thành một minh tinh nhỏ chìm nổi nửa vời. Trong một buổi tiệc rượu tình cờ, cậu nhìn thấy tổng tài tập đoàn bên cạnh là Cố Xuyên. Chưa từ bỏ ý định, cậu nhiều lần sán lại gần gửi tín hiệu cầu bao nuôi tới đối phương, kết quả chẳng ngoài dự liệu, cậu hết lần này đến lần khác bị từ chối thẳng thừng không thương tiếc.",
    "Về sau mạt thế ập đến không một lời báo trước, thế giới chìm vào một mảnh hỗn độn u tối. Cậu tình cờ phát hiện bản thân hoàn toàn miễn nhiễm với virus tang thi, hơn nữa còn có thể điều khiển được tang thi. Cậu giấu kín bí mật này trà trộn sống qua ngày trong căn cứ, thế mà lại một lần nữa đụng độ Cố Xuyên.",
    "Và âm mưu hãm hại lần này, cũng bắt nguồn từ sự cự tuyệt của Cố Xuyên.",
    "Cố Xuyên lựa chọn người trong căn cứ để cùng anh ra ngoài tìm kiếm địa điểm căn cứ mới, Sở Niên Niên lấy hết can đảm xung phong đi cùng, nhưng lại một lần nữa bị Cố Xuyên lạnh lùng từ chối. Cậu đinh ninh rằng Cố Xuyên ghét bỏ cậu chỉ là một người bình thường, càng tin chắc rằng Cố Xuyên sẽ vĩnh viễn không bao giờ đoái hoài nhìn thấy mình.",
    "Cũng chính từ khoảnh khắc này, cậu đã mất đi quyền kiểm soát đối với cơ thể mình. Cốt truyện ép buộc cậu đưa ra quyết định bắt Cố Xuyên phải chết, cậu tìm đến Hoàng Mao, xúi giục gã hợp tác với mình.",
    "Còn về lý do tại sao lại tìm Hoàng Mao ấy à, chẳng qua chỉ là vì cậu không biết lái xe mà thôi.",
    "【Hồi tưởng cốt truyện hoàn tất, kịch bản yêu đương đã được tải lên, thỉnh ký chủ nghiêm túc hoàn thành nhiệm vụ, tiến độ đạt đến 80 là có thể lấy lại quyền tự chủ cơ thể.】",
    "Ý thức quay trở lại, đôi mắt hồ ly của Sở Niên Niên chậm rãi chớp động, đôi mắt vốn bị sương đen bao phủ đã lấy lại vẻ trong trẻo như thuở ban đầu. Thế giới tĩnh lặng xung quanh cũng bắt đầu chuyển động trở lại, cậu nhìn bầy tang thi sắp sửa phá vỡ cửa sắt, mí mắt bắt đầu run rẩy kịch liệt—— Cậu đang làm cái gì thế này, cậu lại muốn Cố Xuyên phải chết ư, làm sao cậu có thể nỡ để Cố Xuyên chết được cơ chứ!",
    "Đồng tử của Sở Niên Niên co thắt lại, cậu nghiêng người lao thẳng về phía Cố Xuyên. Móng vuốt tang thi vừa vặn từ bên ngoài cửa sắt đâm xuyên vào đã rạch lên lưng cậu năm vết thương rướm máu ghê người.",
    "Sở Niên Niên xòe năm ngón tay cách không vung mạnh về phía đàn tang thi đang lao tới, bầy tang thi này lập tức im bặt lại, vẻ mặt chết lặng xoay người, từ từ tản mác trôi dạt về hướng ngược lại.",
    "Cậu há miệng hít thở từng ngụm lớn, phía sau lưng truyền đến cảm giác đau rát nhói buốt không thể nào phớt lờ.",
    "Ngay sau đó, cậu bắt gặp ánh mắt thâm trầm khó dò của Cố Xuyên.",
    "Cố Xuyên mạnh bạo túm lấy cậu nhìn thoáng qua sau lưng, gầm nhẹ: “Sở Niên Niên cậu có bệnh à, tự tìm đường chết đấy à?”",
    "Sở Niên Niên bị anh quát đến ngơ ngác, nhìn vào đôi mắt của Cố Xuyên mới chậm chạp hoàn hồn lại, nhỏ giọng giải thích: “Không phải đâu, em miễn nhiễm với virus tang thi mà, anh đừng lo.”",
    "Cố Xuyên nửa tin nửa ngờ buông cậu ra, ánh mắt của một người lăn lộn thương trường bao năm như muốn nhìn thấu tâm can cậu. Cứ như vậy chờ đợi suốt gần mười phút đồng hồ, xác định Sở Niên Niên không hề có lấy nửa điểm dấu hiệu biến dị, anh mới thở phào một hơi, hỏi: “Rốt cuộc cậu muốn làm cái gì? Muốn lấy mạng tôi, hay là tự tìm đường chết?”",
    "“Em——”",
    "【Ký chủ xin chú ý, phân đoạn này có kịch bản cố định, thỉnh diễn theo đúng kịch bản yêu đương nha~】",
    "Sở Niên Niên xấu hổ khó mở lời nói: “Không, em không muốn lấy mạng anh, em chỉ... muốn người của ca ca thôi.”",
    "“Người?” Cố Xuyên vừa định mở miệng đã bị lời nói của cậu dọa cho sững sờ, anh nhíu mày: “Cậu có biết mình đang nói gì không đấy?”",
    "“Em biết chứ, em nói là em chỉ muốn ca ca thích em, có được không?”",
    "Sở Niên Niên ngượng ngùng đỏ bừng cả hai gò má, lấy hết dũng khí khẽ chạm nhẹ một cái lên môi Cố Xuyên.",
    "Ngay sau đó, cậu đã thu hoạch được một Cố Xuyên ca ca cả người cứng đờ như khúc gỗ."
]

cdir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_031"
src_file = os.path.join(cdir, "source.md")
with open(src_file, "r", encoding="utf-8") as f:
    src_content = f.read()

src_body = src_content.split("---\n\n", 1)[1] if "---\n\n" in src_content else src_content
src_paras = [p for p in src_body.split("\n\n") if p.strip()]

print(f"Source paras: {len(src_paras)}")
print(f"Trans paras: {len(trans_paras)}")

assert len(src_paras) == len(trans_paras), f"Mismatch: {len(src_paras)} != {len(trans_paras)}"

header = "---\ntitle: Chương 31: Tôi chỉ muốn người của anh\n---\n\n"
trans_file = os.path.join(cdir, "translation.md")
with open(trans_file, "w", encoding="utf-8") as f:
    f.write(header + "\n\n".join(trans_paras) + "\n")

print("Successfully wrote translation.md!")
