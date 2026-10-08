# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_023"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 23: Sờ sờ
---""",

    # 1: “你認真的？”
    "“Ông nghiêm túc đấy chứ?”",

    # 2: 婁禧陽當然不信陳斂的鬼話...
    "Lâu Hỉ Dương đương nhiên không tin những lời quỷ quái của Trần Liễm. Không một ai hiểu rõ hơn anh người bị giam giữ ở đó là ai, đó chính là mẹ ruột của anh. Nếu như Tưởng Trác Hàng thực sự có ý đồ xằng bậy gì với mẹ anh thì kiếp trước đã không tự tay bắn nát đầu bà.",

    # 3: 陳斂見他不信...
    "Trần Liễm thấy anh không tin liền bất đắc dĩ thở dài: “Cậu không tin thì cũng chịu thôi. Thực ra hồi đầu lúc hắn ta nói với tôi thì tôi cũng chẳng tin, nhưng mà hồi Tưởng Trác Hàng giấu tình nhân bé nhỏ ở chỗ tôi thì nghiêm túc cẩn thận hết chỗ nói, quý giá như bảo bối không cho người ngoài nhìn thấy lấy một lần, mỗi tuần đều phải tới thăm mấy lượt, tôi chưa từng thấy hắn ta để tâm săn sóc ai đến mức này bao giờ.”",

    # 4: 可不嘛，他媽知道蔣卓航所有的陰謀...
    "Chẳng phải sao, mẹ anh biết rõ toàn bộ âm mưu của Tưởng Trác Hàng, đương nhiên là phải trông chừng chặt chẽ rồi, Lâu Hỉ Dương thầm nghĩ.",

    # 5: 不過為什麽蔣卓航不乾脆殺了她媽滅口...
    "Thế nhưng tại sao Tưởng Trác Hàng không dứt khoát giết mẹ anh để diệt khẩu, mà lại phải tốn bao tâm tư giấu người đi, Lâu Hỉ Dương đến nay vẫn chưa tìm ra đáp án.",

    # 6: “不過我得提醒你一句，千萬別自個兒找死...”
    "“Có điều tôi phải nhắc nhở cậu một câu, ngàn vạn lần đừng tự mình tìm tới cái chết, phòng bị ở nơi đó nghiêm ngặt hơn chỗ tôi nhiều lắm, mười cái mạng cũng không đủ cho cậu phung phí đâu.” Trần Liễm nghiền ngẫm dụng ý của Lâu Hỉ Dương, nét mặt trở nên nghiêm túc, “Tương tự, cắt đứt liên lạc với cha cậu và thằng con trai út nhà họ Trương kia đi, đừng để bọn họ chạy tới đây.”",

    # 7: 婁禧陽要是選擇留在易緣身邊...
    "Nếu Lâu Hỉ Dương đã chọn ở lại bên cạnh Dịch Duyên thì bắt buộc phải nói rõ ràng với bọn họ, bằng không đến lúc đó sẽ gây ra những rắc rối không cần thiết.",

    # 8: 陳斂說完就走...
    "Trần Liễm nói xong liền rời đi. Trước khi đi chợt nhớ ra điều gì, ông ta móc từ trong ngực ra một thứ ném lên giường. Lâu Hỉ Dương cầm lên xem, phát hiện là một chiếc mặt nạ che đi hơn nửa khuôn mặt.",

    # 9: “把它帶上，從今天起你就是我陳斂養子的保鏢，別露餡，別給我添麻煩。”
    "“Đeo nó vào, kể từ hôm nay cậu chính là vệ sĩ cho con nuôi của Trần Liễm tôi, đừng để lộ tẩy, đừng gây thêm phiền phức cho tôi.”",

    # 10: 門一關，陳斂的腳步聲就遠了...
    "Cửa vừa đóng lại, tiếng bước chân của Trần Liễm liền đi xa dần. Lâu Hỉ Dương sờ sờ chiếc mặt nạ, thuận tay đặt nó ở đầu giường, ngay sau đó túm lấy cổ áo Dịch Duyên xách cậu lên, hệt như xách gáy một chú mèo con: “Nói xem nào, giấu anh bao nhiêu chuyện rồi hả?”",

    # 11: 易緣的眼睛滴溜溜地在他臉上打量...
    "Đôi mắt Dịch Duyên đảo quanh đánh giá trên mặt anh, thấy anh không có vẻ giận dữ liền đáng thương bĩu bĩu môi, giọng nói nhỏ như muỗi kêu: “Anh ơi, đau……”",

    # 12: 婁禧陽看了眼自己的手...
    "Lâu Hỉ Dương liếc nhìn tay mình, xác định hoàn toàn không chạm vào sau gáy cậu, nhưng vẫn buông lỏng lực đạo, để Dịch Duyên chống người vào lồng ngực mình ngồi thẳng dậy.",

    # 13: “我不想看你發愁。”...
    "“Em không muốn nhìn anh phải buồn phiền.” Dịch Duyên rủ mắt xuống, ngón tay lướt nhẹ trên vùng bụng anh, “Anh muốn làm cái gì, em đều muốn giúp anh hoàn thành, em có thể làm được mà.”",

    # 14: 婁禧陽抓住易緣勾火的手...
    "Lâu Hỉ Dương bắt lấy bàn tay đang châm lửa khơi mào của Dịch Duyên, lực đạo khiến Dịch Duyên có chút đau. Cậu nâng mắt lên, mới ngẩn ngơ nhận ra Lâu Hỉ Dương đang nhìn mình, mà sâu trong đôi mắt ấy lại là sự áy náy... Và hối hận chưa từng có trước đây.",

    # 15: 驚呼還未來得及出口...
    "Tiếng thốt kinh ngạc còn chưa kịp bật ra khỏi miệng, cậu đã bị Lâu Hỉ Dương trở mình một cái ép chặt vào đầu giường, ngay sau đó liền bị một đôi môi ấm áp chặn đứng lại. Lâu Hỉ Dương trước tiên cuồng loạn cắn nhẹ lên cánh môi cậu, đợi đến khi cậu bị cảm giác nhói đau và tê dại làm cho mê muội mất phương hướng thì lại men theo kẽ hở đưa đầu lưỡi vào trong miệng cậu, quấn lấy cậu vừa nhẹ nhàng vừa tinh tế liếm mút, tựa như đang dùng phương thức này để vỗ về an ủi cậu.",

    # 16: “對不起小緣，對不起。”...
    "“Xin lỗi Tiểu Duyên, xin lỗi em.” Lâu Hỉ Dương ghé sát bên tai cậu, trầm giọng lặp đi lặp lại.",

    # 17: 他把臉深深地埋在易緣的頸間，感受著真切的體溫。
    "Anh vùi sâu khuôn mặt vào hõm cổ Dịch Duyên, cảm nhận nhiệt độ cơ thể chân thực rõ ràng.",

    # 18: 原來從一開始，易緣做的一切都是為了他...
    "Hóa ra ngay từ lúc bắt đầu, tất cả những gì Dịch Duyên làm đều là vì anh: chẳng nói chẳng rằng rời đi là vì anh, trở thành con nuôi của Trần Liễm giả vờ không quen biết cũng là vì anh. Giờ đây anh có niềm tin mãnh liệt để tin rằng trong đêm tuyết rơi năm xưa, Dịch Duyên cũng là vạn bất đắc dĩ.",

    # 19: 他上輩子是怎麽誤會他的呢？...
    "Kiếp trước anh đã hiểu lầm cậu như thế nào cơ chứ? Anh nhớ khi đó hành tung của mình cứ liên tục bị bại lộ, sau đó Dịch Duyên bỗng dưng biến mất không rõ nguyên do. Tại buổi yến tiệc, lúc biết được Dịch Duyên trở thành con nuôi của Trần Liễm anh mới bừng tỉnh đại ngộ, cứ ngỡ Dịch Duyên lấy chuyện đó ra giao dịch với Trần Liễm.",

    # 20: 在那場宴會上，他潛入易緣的房間...
    "Trong bữa tiệc đó, anh lẻn vào phòng Dịch Duyên chất vấn cậu tại sao. Dịch Duyên trong ký ức khoác lên mình bộ âu phục cao quý kiêu sa, cà vạt buông lơi, bên trên còn vương những vệt rượu vang đỏ văng trúng do giằng co ẩu đả với anh.",

    # 21: 他一直盯著他後方的紅點...
    "Cậu cứ nhìn chằm chằm vào chấm đỏ phía sau lưng anh, cười một cách lạnh lùng nhưng sắc mặt lại trắng bệch, tựa như đang nhẫn nhịn chịu đựng nỗi đau đớn nào đó. Cậu cầm khẩu súng xoay tròn trong đầu ngón tay, họng súng đen ngòm vẽ ra một đường cong nguy hiểm giữa không trung.",

    # 22: 他說：“什麽為什麽？你…我得活下去啊，滾吧。”
    "Cậu nói: “Tại sao cái gì chứ? Anh... Tôi phải sống tiếp chứ, cút đi.”",

    # 23: 隨著一聲槍響...
    "Theo một tiếng súng vang lên, vô số lính đánh thuê ùa vào như ong vỡ tổ, Lâu Hỉ Dương bất đắc dĩ đành phải nhảy cửa sổ rời đi. Kể từ đó anh không còn gặp lại Dịch Duyên nữa, cho tới khi anh và Lâu An Minh tìm được nơi ẩn náu của mẹ mình, ngay trước cổng viện điều trị, giữa những bông hoa tuyết trắng muốt như nhung và họng súng đen ngòm dày đặc, anh mới nhìn thấy lại gương mặt diễm lệ lạnh lùng kia, mà bên cạnh cậu vừa vặn đang có một Tưởng Trác Hàng mặt cười nhưng lòng không cười đứng đó.",

    # 24: “陽哥，你怎麽啦？”...
    "“Dương ca, anh bị làm sao thế?” Câu hỏi có chút ngượng ngùng của Dịch Duyên kéo dòng suy nghĩ của Lâu Hỉ Dương quay trở lại thực tại.",

    # 25: 婁禧陽這才反應過來自己快要把易緣勒死了，連忙松下了手。
    "Lâu Hỉ Dương lúc này mới nhận ra mình sắp siết chết Dịch Duyên tới nơi rồi, vội vàng nới lỏng tay ra.",

    # 26: “這是男朋友的福利嗎？”...
    "“Đây là phúc lợi của bạn trai sao?” Dịch Duyên co chân vòng qua thắt lưng đang rời đi của Lâu Hỉ Dương, kéo người trở lại một lần nữa, “Thế thì em thích lắm đấy.”",

    # 27: 如果是真的，他就更喜歡了。易緣這樣想道。
    "Nếu như là thật thì cậu lại càng thích hơn nữa. Dịch Duyên thầm nghĩ như vậy.",

    # 28: 婁禧陽看著身下這張因為害羞而紅撲撲的臉...
    "Lâu Hỉ Dương nhìn khuôn mặt đỏ ửng vì thẹn thùng dưới thân mình, bất giác đem gương mặt trong đêm tuyết năm xưa ra so sánh đối chiếu. Kiếp này, anh vẫn chưa từng nhìn thấy một mặt đó của Dịch Duyên, một mặt Dịch Duyên tựa như đóa hồng đen tua tủa gai nhọn.",

    # 29: “易緣，我不會再讓你難受了。”婁禧陽一臉認真。
    "“Dịch Duyên, anh sẽ không để em phải chịu khổ sở nữa đâu.” Lâu Hỉ Dương vẻ mặt đầy nghiêm túc.",

    # 30: 然而底下的易緣哪裡能放過這個機會...
    "Thế nhưng Dịch Duyên ở bên dưới làm sao chịu bỏ qua cơ hội này: “Thật không ạ? Thế thì Dương ca... Chỗ này của em khó chịu lắm.”",

    # 31: 說著，不管婁禧陽突然僵住的身體...
    "Vừa nói, mặc kệ cơ thể Lâu Hỉ Dương bỗng nhiên cứng đờ, cậu nắm lấy tay Lâu Hỉ Dương, làm nũng nói: “Anh giúp em sờ sờ một chút được không?”",

    # 32: ……
    "……",

    # 33: 婁禧陽花了幾分鍾的時間給張森澤發了幾條消息...
    "Lâu Hỉ Dương dành ra vài phút gửi mấy tin nhắn cho Trương Sâm Trạch, đại ý là anh hiện tại rất bận, trong khoảng thời gian này trước khi anh chủ động liên lạc thì đừng tìm anh, và xe của gã đã nát bét rồi, bảo gã nhớ tới cục giao thông mà nhận lại.",

    # 34: 而後他又給婁安明報了個信...
    "Sau đó anh lại báo tin cho Lâu An Minh, sao chép dán nguyên văn lời lẽ tương tự. Chỉ tiếc là Lâu An Minh không giống Trương Sâm Trạch, xối xả mắng anh một trận vuốt mặt không kịp, bày tỏ rằng ông thất vọng về anh đến nhường nào vân vân mây mây.",

    # 35: 婁禧陽一臉平淡地關上了終端，繼續低頭研究摘除裝置。
    "Lâu Hỉ Dương vẻ mặt thản nhiên tắt thiết bị đầu cuối, tiếp tục cúi đầu nghiên cứu thiết bị bóc tách.",

    # 36: 他不信他有兩輩子的機械改造造詣，破不開這個狗屁裝置。
    "Anh không tin với trình độ cải tạo cơ khí tích lũy qua hai kiếp của mình mà lại không phá giải nổi cái thiết bị chó má này.",

    # 37: 每當易緣為它而疼的時候...
    "Mỗi khi Dịch Duyên vì nó mà đau đớn, đó chính là lúc anh vò đầu bứt tai hận không thể lập tức phá bỏ nó ra ngay, cũng là lúc anh sốt ruột như lửa đốt mông nhất.",

    # 38: 因為易緣找到了抑製疼痛的另一途徑——對他上下其手，並且強迫他對他上下其手。
    "Bởi vì Dịch Duyên đã tìm ra một phương thức khác để ức chế cơn đau—— tay chân táy máy sờ soạng trên dưới người anh, đồng thời ép buộc anh cũng phải táy máy sờ soạng trên dưới người cậu.",

    # 39: 天知道那天他鬼使神差地幫易緣摸了一把後...
    "Trời mới biết ngày hôm đó ma xui quỷ khiến anh giúp Dịch Duyên sờ một cái xong, Dịch Duyên liền nếm được mùi ngon say mê thích thú, ngày nào cũng nhìn chằm chằm vào chỗ đó của anh như có điều suy nghĩ, nhìn đến mức da đầu Lâu Hỉ Dương tê rần.",

    # 40: 他也抽空在終端上查了一些關於兩個男人談戀愛的資料...
    "Anh cũng tranh thủ thời gian rảnh tra cứu trên thiết bị đầu cuối một số tài liệu về việc hai người đàn ông yêu đương với nhau. Chỉ là một loạt những khung hình kích thích làm Lâu Hỉ Dương ngồi không yên đứng chẳng vững, trên đó căn bản chẳng có quy trình cụ thể nào cả, vừa vào là đã thế này thế nọ luôn rồi!",

    # 41: 回想起易緣的各種暗示...
    "Hồi tưởng lại đủ loại ám hiệu của Dịch Duyên, Lâu Hỉ Dương bày tỏ vô cùng hoang mang hoảng loạn. Dịch Duyên lần nào cũng muốn anh chạm vào chỗ đó của cậu, chắc là muốn làm bên dưới rên rỉ đúng không? Khoan đã, ngộ nhỡ Dịch Duyên muốn anh làm người rên rỉ ở bên dưới thì phải làm sao đây...!",

    # 42: 婁禧陽一個激靈...
    "Lâu Hỉ Dương rùng mình một cái, chợt nhớ ra hiện tại mình chỉ là bạn trai giả của Dịch Duyên thôi, chắc là không cần làm tới bước đó đâu, nhưng rồi sẽ có một ngày đồ giả cũng biến thành đồ thật.",

    # 43: 那就從現在開始做些心裡建設吧...
    "Vậy thì cứ bắt đầu xây dựng tâm lý từ bây giờ đi, Lâu Hỉ Dương lấy đó làm kết luận, không nghĩ ngợi lung tung về những thứ này nữa, chuyên tâm dốc lòng nghiên cứu thiết bị.",

    # 44: 但他仍然沒放棄去第二樓找他媽。
    "Thế nhưng anh vẫn không hề từ bỏ ý định lên tầng hai tìm mẹ mình.",

    # 45: 他在等一個最佳的時機。
    "Anh đang chờ đợi một thời cơ tốt nhất.",

    # 46: 這些天他將他能去的地方都視察了一遍...
    "Mấy ngày nay anh đã đi khảo sát tất cả những nơi mình có thể tới một lượt, tìm kiếm chiếc thang máy bí mật kia. Thang máy cần có thẻ từ mở khóa tương ứng, Lâu Hỉ Dương quét thẻ từ trên mặt nạ của mình lên, phát hiện thang máy tới chỉ có duy nhất một nút bấm của tầng này.",

    # 47: 這一層實驗室的人全部都只有這一個按鍵...
    "Toàn bộ người ở tầng phòng thí nghiệm này đều chỉ có một nút bấm này, điều này chứng minh hai người mặc áo blouse trắng bị anh đánh ngất lần trước vừa khéo lại chính là người của tầng hai. Chỉ có thể nói là vận may của anh không tốt, xác suất năm mươi phần trăm mà cũng bỏ lỡ được.",

    # 48: 但婁禧陽並不是走投無路，因為他找到了連接兩層樓的空氣管道。
    "Nhưng Lâu Hỉ Dương không phải là đã hết đường đi, bởi vì anh đã tìm ra đường ống thông khí nối liền giữa hai tầng lầu.",

    # 49: 空氣管道所處的位置極其隱蔽...
    "Vị trí đặt ống thông khí cực kỳ kín đáo, nhưng Lâu Hỉ Dương đã thấy quá nhiều thủ đoạn kiểu này rồi. Trong một lần sờ soạng âu yếm cùng Dịch Duyên trong phòng tắm, anh tình cờ nhìn lên trần nhà tắm, ngay sau đó liền bắt trọn được manh mối—— anh nhanh tay chế tạo một chiếc máy dò mini bay theo đường ống lên trên, phát hiện đầu bên kia là một nhà vệ sinh công cộng.",

    # 50: 他不知道蔣卓航什麽時候會來...
    "Anh không biết khi nào Tưởng Trác Hàng sẽ tới, ngay cả Trần Liễm cũng không nắm rõ quy luật của hắn. Để tránh đụng độ trực diện, Lâu Hỉ Dương cố ý lựa chọn ngày hôm nay.",

    # 51: 明天就是蔣卓航的生日宴會...
    "Ngày mai chính là tiệc sinh nhật của Tưởng Trác Hàng, hắn ta khả năng cực lớn sẽ bận rộn xử lý các sự vụ của bữa tiệc, vậy thì ngày hôm nay chính là thời cơ tốt nhất.",

    # 52: 婁禧陽等到凌晨，躍上了浴室的天花板。
    "Lâu Hỉ Dương đợi tới rạng sáng, nhảy phắt lên trần nhà tắm.",

    # 53: “陽哥，你小心一點。”...
    "“Dương ca, anh cẩn thận một chút đấy.” Dịch Duyên ở bên dưới ngước nhìn lên, hàng mày thanh tú nhăn tít lại, “Thôi, hay là em đi cùng anh nhé.” Cậu vừa nói vừa giẫm lên bồn cầu, làm động tác toan đu người lên theo.",

    # 54: “別，你下去...”
    "“Đừng, em xuống đi, hai người càng khó ẩn nấp hơn, anh cần em ở bên dưới canh chừng giúp anh.” Lâu Hỉ Dương lắc đầu, hạ thấp giọng nói: “Ngoan ngoãn một chút đi.”",

    # 55: 易緣果真停在了原地，沒再吵著一起。
    "Dịch Duyên quả nhiên dừng lại tại chỗ, không còn nằng nặc đòi đi cùng nữa.",

    # 56: 婁禧陽囑咐了幾句...
    "Lâu Hỉ Dương dặn dò thêm vài câu, đeo mặt nạ lên mặt, đạp vào vách trong của đường ống dăm ba bước liền trèo lên phía trên.",

    # 57: 將隔板緩慢且輕地移開...
    "Chậm rãi và khẽ khàng dịch chuyển tấm vách ngăn ra, anh nhìn thấy toàn cảnh ở đầu bên kia. Từ trần nhà đáp đất không một tiếng động, Lâu Hỉ Dương đang ở trong một buồng vệ sinh ngồi xổm. Anh lắng tai nghe vài phút xác định bên trong không có ai mới từ từ đẩy cánh cửa buồng ra.",

    # 58: 這是一間男廁所...
    "Đây là một nhà vệ sinh nam, bên trong sạch sẽ đến mức khó tin, xem chừng không có mấy người sử dụng. Anh ngẩng đầu quét mắt một lượt cũng không thấy có camera. Tuy rằng không lắp camera trong nhà vệ sinh là thường thức cơ bản, nhưng Lâu Hỉ Dương lại không chắc cái nơi biến thái này có làm chuyện biến thái hay không.",

    # 59: 他側身靠在正門口...
    "Anh né người tựa vào cửa chính, cẩn thận lắng nghe một lúc, không nghe thấy tiếng bước chân cũng chẳng có tiếng thở, liền từ từ hé mở một khe nhỏ. Nhìn qua khe cửa, anh phát hiện bên ngoài là một dãy hành lang màu xanh lam sẫm.",

    # 60: 走廊上沒有人，兩側也沒有門，全是牆。
    "Trên hành lang không có một bóng người, hai bên cũng chẳng có cánh cửa nào, toàn bộ đều là vách tường.",

    # 61: 確認了情況後...
    "Sau khi xác nhận tình hình, Lâu Hỉ Dương từ khe cửa thả ba con ruồi điện tử ra ngoài. Đây là thứ anh chế tạo ra hồi còn nuôi nấng bé Dịch Duyên, có thể tạm thời vô hiệu hóa camera an ninh trong mười phút.",

    # 62: 等了一會兒，終端上的紅點顯示全黑了之後，婁禧陽推門而出。
    "Đợi một lát, sau khi các chấm đỏ trên thiết bị đầu cuối hiển thị tối đen hoàn toàn, Lâu Hỉ Dương đẩy cửa bước ra ngoài."
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_023 translation written: {len(paragraphs)} paragraphs.")
