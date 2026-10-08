# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_022"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 22: Nhốt người nào
---""",

    # 1: separator / line 1 in source
    "Lâu Hỉ Dương lắc lắc đầu, xua đi những tiếng ù ù ong ong trong đầu, đúng lúc này, anh nghe thấy có tiếng ai đó gõ lên cửa kính xe từ bên ngoài.",

    # 2: 婁禧陽晃了晃頭...
    "Lâu Hỉ Dương lắc lắc đầu, xua đi những tiếng ù ù ong ong trong đầu, đúng lúc này, anh nghe thấy có tiếng ai đó gõ lên cửa kính xe từ bên ngoài.",

    # 3: 窗外站著一個普通得不能再普通的中年男人...
    "Bên ngoài cửa sổ xe đang đứng một người đàn ông trung niên bình thường không thể bình thường hơn. Gã vẻ mặt đầy áy náy nhìn anh, cách đó không xa còn đỗ một chiếc xe tải thùng kín lái tay kiểu cũ thời đại trước.",

    # 4: 這條小路唯一能通往的只有治療所...
    "Con đường nhỏ này nơi duy nhất có thể thông tới chỉ có viện điều trị. Nhìn từ hướng xe chạy tới, chỉ có thể là chiếc xe đi ra từ viện điều trị, nom dáng vẻ là xe chở hàng tiếp tế cho viện điều trị.",

    # 5: “先生，實在是不好意思...”
    "“Thưa ngài, thật vô cùng xin lỗi, vừa rồi tôi sơ ý ngủ gật một chút... Ngài xem liệu có tiện để lại phương thức liên lạc không, tôi...” Bác tài xế xe tải quan sát chiếc siêu xe trước mặt, lại liếc nhìn Lâu Hỉ Dương từ trên xuống dưới, sắc mặt vừa đắng chát vừa khó coi.",

    # 6: 婁禧陽隻覺得頭疼的炸裂...
    "Lâu Hỉ Dương chỉ cảm thấy đầu đau như muốn nổ tung. Anh nghiến răng chống người dậy, lúc này lại phát hiện Dịch Duyên đã nằm bất động gục trên người anh, ngất lịm đi rồi.",

    # 7: 糟了，他猛地看了眼時間，還剩十五分鍾。
    "Hỏng rồi! Anh chợt nhìn thời gian, chỉ còn lại đúng mười lăm phút.",

    # 8: 眼前一陣又一陣的恍惚...
    "Trước mắt từng đợt từng đợt hoa lên choáng váng. Lâu Hỉ Dương nhanh chóng túm lấy hai tay Dịch Duyên vắt lên vai mình, cõng cậu lên lưng, rồi tung một cước đạp văng cửa xe, sải chân lao như điên về phía trước.",

    # 9: “唉，先生！先生——”...
    "“Ơ, thưa ngài! Thưa ngài——” Tiếng kêu kinh ngạc của người đàn ông bị anh bỏ lại tít đằng sau. Anh liều mạng chạy về phía trước, anh không biết nơi này còn cách viện điều trị bao xa, con đường dài vô tận khiến đầu óc anh choáng váng, tựa như có một bàn tay đang hờ hững bao trùm lấy trái tim anh, giây tiếp theo sẽ không chút lưu tình mà bóp nghẹt lại.",

    # 10: 這種感覺讓他想起了婁安明和他母親死的那一個雪夜...
    "Cảm giác này làm anh nhớ lại đêm tuyết rơi ngày mà Lâu An Minh cùng mẹ anh qua đời năm xưa, cũng nhớ lại buổi hoàng hôn khi Trần Liễm trao hũ tro cốt của Dịch Duyên vào tay anh.",

    # 11: 他很熟悉...
    "Anh quá đỗi quen thuộc với nó, bởi vì trong mỗi một ngày sau khi tất cả mọi chuyện đã kết thúc, anh đều bị cảm giác như thế này gặm nhấm, một mình ngồi trên tầng thượng tòa nhà Liên bang nhìn xuống ánh đèn rực rỡ bên dưới.",

    # 12: 那是一種心跳仍在跳動，但卻通體冰涼的感覺。
    "Đó là một cảm giác mà trái tim rõ ràng vẫn đang đập, nhưng toàn thân lại lạnh ngắt như băng.",

    # 13: 耳邊突然被熱氣包裹...
    "Bên tai đột nhiên được hơi nóng bao bọc, gương mặt Dịch Duyên tựa vào hõm vai anh, vô thức rên khẽ một tiếng.",

    # 14: 是熱的。
    "Là ấm nóng.",

    # 15: 婁禧陽的肌肉突然繃到了極致，眼前的景物以更快的速度飛了起來。
    "Cơ bắp của Lâu Hỉ Dương đột ngột căng cứng đến cực hạn, cảnh vật trước mắt bay vút qua với tốc độ càng nhanh hơn.",

    # 16: 自從他再次回到那一天，見到那張臉後，他一直都是熱的。
    "Kể từ khi anh một lần nữa quay trở lại ngày hôm đó, nhìn thấy khuôn mặt kia, người cậu trước giờ vẫn luôn ấm nóng.",

    # 17: “老爺，他跑了。”
    "“Thưa lão gia, cậu ta chạy rồi.”",

    # 18: 貨車司機上了車...
    "Bác tài xế bước lên xe tải, cung kính cúi gầm đầu nói với người bên trong thùng xe. Trên mặt gã chẳng còn chút dáng vẻ đắng cay đau khổ vừa rồi nữa, nửa rủ mi mắt, mặt không chút cảm xúc.",

    # 19: 這不是一輛尋常的貨車...
    "Đây không phải là một chiếc xe tải thông thường. Bên trong thùng xe trang hoàng lộng lẫy xa hoa tựa như một phòng khách sang trọng, nói là một chiếc xe nhà di động phiên bản cỡ đại cũng không hề quá chút nào.",

    # 20: 中間的皮質沙發上坐著一個長發男人...
    "Trên chiếc ghế sô pha bằng da ở chính giữa đang ngồi một người đàn ông tóc dài. Hàng chục người đàn ông mặc âu phục đen đứng canh gác xung quanh, đồng loạt cúi đầu không dám nhìn thẳng vào người đó.",

    # 21: 男人黑如綢緞的長發被他束在腦後...
    "Mái tóc dài đen óng ả như lụa là của người đàn ông được buộc gọn ra sau đầu, chỉ để lại hai lọn tóc mỏng rủ xuống bên gò má tinh xảo, điểm xuyết cho sắc môi đỏ thắm rực rỡ.",

    # 22: M星公認的美人...
    "Mỹ nhân được công nhận toàn hành tinh M, đồng thời cũng là người cầm lái nắm trọn toàn bộ Liên bang. Không một ai dám đàm tiếu rằng Thủ lĩnh Liên bang Tưởng Trác Hàng lại sở hữu một lớp da túi xinh đẹp khiến người ta phải trầm luân mê đắm đến nhường này, ngay cả năm tháng cũng chẳng để lại bao nhiêu dấu vết trên gương mặt hắn ta.",

    # 23: “往治療所去了？”殷紅的唇勾起了一個細微的弧度。
    "“Đi về hướng viện điều trị rồi sao?” Đôi môi đỏ thắm cong lên một độ cong tinh tế.",

    # 24: “是。”司機頷首...
    "“Vâng.” Tài xế gật đầu, nhìn thấy cảnh này liền vội vàng cúi gầm đầu xuống thấp hơn, “Lần sau lão gia đừng mạo hiểm như vậy nữa, ngộ nhỡ thuộc hạ không khống chế tốt tốc độ thì ngài sẽ bị thương mất.”",

    # 25: 鬼知道開著開著蔣卓航就讓他撞上去是為什麽。
    "Quỷ mới biết đang lái xe ngon lành thì Tưởng Trác Hàng lại bảo gã tông thẳng vào đó là vì cái gì.",

    # 26: “去查這輛車。”...
    "“Đi điều tra chiếc xe này.” Tưởng Trác Hàng quay đầu nói với người bên cạnh, sau đó phất phất tay. Tài xế hiểu ý quay người đi, một lát sau, chiếc xe tải lại khởi động như chưa hề có chuyện gì xảy ra.",

    # 27: 婁禧陽看到治療所的大樓時已經筋疲力盡了...
    "Lúc Lâu Hỉ Dương nhìn thấy tòa nhà viện điều trị thì đã kiệt sức hoàn toàn rồi. Cả một đám người đông nghịt đen ngòm chặn ngay trước mặt anh, tựa như đã sớm chờ đợi anh xuất hiện.",

    # 28: “讓開—”...
    "“Tránh ra——” Chưa tới viện điều trị, Lâu Hỉ Dương sốt ruột tung chân đá bay người chắn trước mặt, thế nhưng vì thể lực cạn kiệt nên bị cả vòng người tràn lên vây kín trở lại. Mất hết sức lực, anh khuỵu một bên đầu gối xuống đất, mồ hôi men theo gò má từng giọt từng giọt rơi ướt đẫm mặt sàn. Anh chật vật muốn đứng dậy nhưng chẳng còn chút sức lực nào để đứng lên nữa.",

    # 29: “別緊張，已經在范圍內了，他沒事。”...
    "“Đừng căng thẳng, đã nằm trong phạm vi rồi, thằng bé không sao đâu.” Giọng nói vang lên từ phía sau. Lâu Hỉ Dương quay đầu lại, nhìn Trần Liễm từng bước từng bước đi về phía mình.",

    # 30: 陳斂向身邊的兩個白大褂遞了個眼色...
    "Trần Liễm đưa mắt ra hiệu với hai người mặc áo blouse trắng bên cạnh. Hai người lập tức bước lên muốn đón lấy Dịch Duyên đang hôn mê, nhưng lại bị một ánh mắt của Lâu Hỉ Dương đóng đinh ngay tại chỗ.",

    # 31: “放開易緣，他現在需要躺在實驗室的床上。”...
    "“Buông Dịch Duyên ra, hiện tại thằng bé cần phải nằm trên giường phòng thí nghiệm.” Trần Liễm bước lại gần, nhíu nhíu mày, “Đã tới dưới mí mắt tôi rồi thì cậu đừng hòng mang thằng bé rời đi nữa, có điều...”",

    # 32: 婁禧陽還在原地喘著氣...
    "Lâu Hỉ Dương vẫn đang thở dốc tại chỗ, nghe vậy liền cười lạnh một tiếng. Hai người mặc áo blouse vội vàng khiêng Dịch Duyên lên xe.",

    # 33: “陳斂我說…”婁禧陽撐著地面，緩緩地站起了身，“你他媽真是欠揍！”
    "“Trần Liễm, tôi bảo này...” Lâu Hỉ Dương chống tay xuống đất, chậm rãi đứng thẳng người dậy, “Ông mẹ nó đúng là thèm đòn!”",

    # 34: 陳斂看著歪歪站直的婁禧陽...
    "Trần Liễm nhìn Lâu Hỉ Dương đang loạng choạng đứng thẳng dậy. Lâu Hỉ Dương cao hơn ông ta trọn vẹn một cái đầu, áp lực kéo theo bóng râm ập tới bao trùm lấy ông ta. Ông ta lùi lại một bước, nhưng vẫn không né kịp nắm đấm đang bay thẳng tới.",

    # 35: 陳斂被這一拳硬生生地打翻在地...
    "Trần Liễm bị cú đấm này nện ngã sóng soài xuống đất. Đầu óc ông ta choáng váng ôm lấy chiếc mũi đang chảy máu ròng ròng, những lời chưa kịp nói ban nãy mới chậm rãi thốt ra miệng: “... Có điều, tôi có thể cho cậu ở lại đây bầu bạn với Dịch Duyên.”",

    # 36: 然而他這句話婁禧陽是聽不見了...
    "Thế nhưng câu nói này Lâu Hỉ Dương đã không còn nghe thấy nữa rồi, bởi vì đám vệ sĩ bên cạnh Trần Liễm đã lao vào đánh nhau hỗn loạn một đoàn cùng anh.",

    # 37: 婁禧陽醒來的時候發現自己正在一間看起來像臥室的房間裡...
    "Lúc Lâu Hỉ Dương tỉnh lại, anh phát hiện mình đang ở trong một căn phòng trông giống như phòng ngủ. Sở dĩ nói là “giống” vì nơi này có giường cũng có bàn, chỉ có điều trần nhà là một màu xám trắng lạnh lẽo, trong phòng cũng chẳng có lấy một ô cửa sổ.",

    # 38: 但他在枕頭上聞到了易緣的味道。
    "Thế nhưng anh ngửi thấy mùi hương của Dịch Duyên trên chiếc gối.",

    # 39: 他動了動身子...
    "Anh cử động cơ thể, cảm giác đau nhức tê dại dữ dội làm anh nhớ lại ngọn ngành câu chuyện. Anh hình như trong lúc đang đánh nhau với đám người kia thì lăn ra ngất xỉu, bởi vì mẹ kiếp mệt quá rồi.",

    # 40: 艸，真tm丟人！
    "Đệt, thật mẹ nó mất mặt chết đi được!",

    # 41: 婁禧陽想著自己在陳斂面前累的昏倒...
    "Lâu Hỉ Dương nghĩ đến cảnh tượng mình mệt đến ngất xỉu trước mặt Trần Liễm, cả người tức tối bật dậy khỏi giường.",

    # 42: “陽哥！你醒啦！”...
    "“Dương ca! Anh tỉnh rồi à!” Cánh cửa phòng đột nhiên bị ai đó đẩy ra, Dịch Duyên hưng phấn nhảy chân sáo chạy vào, tung người nhào bổ lên người Lâu Hỉ Dương. Lâu Hỉ Dương bị đòn tập kích bất thình lình này làm cho cơ bắp toàn thân đau nhức gào thét từng hồi, hít sâu một ngụm khí lạnh.",

    # 43: 易緣聞聲連忙翻下身...
    "Dịch Duyên nghe thấy tiếng vội vàng trườn xuống, quỳ ngồi bên cạnh Lâu Hỉ Dương: “Em xin lỗi, em quên mất.”",

    # 44: “你快點躺下。”...
    "“Anh mau nằm xuống đi.” Dịch Duyên đẩy vai Lâu Hỉ Dương ấn xuống giường, vẻ mặt đầy hối lỗi nhìn thẳng vào mắt anh, “Có phải em nặng quá không ạ?”",

    # 45: 易緣好歹是個一米七以上的正常男性...
    "Dịch Duyên dẫu sao cũng là một người đàn ông bình thường cao hơn một mét bảy, cõng cậu chạy nước rút hết tốc lực mười mấy phút đồng hồ quả thực còn mệt hơn bất kỳ bài huấn luyện thể năng nào anh từng trải qua ở học viện.",

    # 46: 但婁禧陽見易緣這副神情...
    "Thế nhưng Lâu Hỉ Dương nhìn thấy biểu cảm này của Dịch Duyên, ngẫm nghĩ một chút, cái đầu vốn định gật bỗng ngoắt ngoéo đổi hướng: “Không nặng.”",

    # 47: 易緣的眼睛亮了一下...
    "Đôi mắt Dịch Duyên sáng bừng lên, cậu chống hai tay hai bên đầu Lâu Hỉ Dương, cúi người xuống thấp giọng nói: “Cảm ơn ca ca.”",

    # 48: 溫熱的吐息打在婁禧陽臉上...
    "Hơi thở ấm nóng phả lên mặt Lâu Hỉ Dương, anh nhìn chóp mũi sắp dán sát vào nhau của hai người, nghiêng đầu đi, nghe thế nào cũng thấy lời của Dịch Duyên gượng gạo kỳ quặc.",

    # 49: 就是明明是正常的話，被易緣講出來就參雜了情.色意味。
    "Chính là những câu nói rõ ràng rất bình thường, nhưng qua miệng Dịch Duyên nói ra lại pha lẫn phong vị tình sắc ám muội.",

    # 50: 易緣低下頭，在婁禧陽唇上親了一下後翻身躺在了他旁邊。
    "Dịch Duyên cúi đầu hôn nhẹ một cái lên môi Lâu Hỉ Dương rồi trở mình nằm xuống bên cạnh anh.",

    # 51: 婁禧陽後知後覺地抬起了眉...
    "Lâu Hỉ Dương chậm nửa nhịp nhướng mày, vừa định mở miệng thì liền nghe Dịch Duyên nói năng dõng dạc chính khí lẫm liệt: “Bạn trai thì phải cảm ơn như thế này chứ.”",

    # 52: 婁禧陽這才想起來，自己已經是易緣的假“男朋友”了。他薄唇微抿，上面有細微的癢意。
    "Lâu Hỉ Dương lúc này mới sực nhớ ra, bản thân đã là “bạn trai” giả của Dịch Duyên rồi. Môi mỏng của anh khẽ mím lại, bên trên còn vương cảm giác ngứa ngáy nhè nhẹ.",

    # 53: 敲門聲打斷了兩人的對話...
    "Tiếng gõ cửa cắt ngang cuộc đối thoại giữa hai người. Trần Liễm khoanh tay dựa vào cửa, trong hai lỗ mũi còn nhét hai cục bông gòn: “Dịch Duyên nói hai người gặp phải tai nạn xe cộ, là chuyện thế nào?”",

    # 54: 婁禧陽撐著要坐起來...
    "Lâu Hỉ Dương chống tay định ngồi dậy, lại bị Dịch Duyên một lần nữa đè trở lại. Lần này cậu dứt khoát lật người ôm chặt lấy anh, tựa vào ngực anh với tư thế nép vào lòng, gắt gao đè chặt anh trên giường.",

    # 55: 陳斂沉默無聲地將這番畫面看在眼裡...
    "Trần Liễm im lặng thu trọn khung cảnh này vào mắt, trong lòng thầm thở dài một hơi. Ông ta sải bước đi tới bên mép giường: “Hôm nay Tưởng Trác Hàng đã tới. Nếu như đoán không nhầm, chiếc xe tông vào các cậu là một chiếc xe tải thùng kín, bên trong đang chở Thủ lĩnh Liên bang. Cậu nên hiểu rằng, hiện tại cậu sắp bị nhắm tới rồi đấy.”",

    # 56: 婁禧陽抬眸盯著他：“和我說這些做什麽？”
    "Lâu Hỉ Dương nâng mắt nhìn chằm chằm ông ta: “Nói với tôi những điều này làm gì?”",

    # 57: 陳斂輕笑：“向你展現我的誠意...”
    "Trần Liễm khẽ cười: “Để thể hiện thành ý của tôi với cậu, nói cho cậu biết con chó do Tưởng Trác Hàng nuôi nấng hiện tại muốn cắn ngược lại hắn ta một phát, hơn nữa còn muốn hợp tác với một thằng nhóc không biết trời cao đất rộng như cậu.”",

    # 58: 婁禧陽目光幽深，看著他繼續說下去。
    "Ánh mắt Lâu Hỉ Dương sâu thẳm, nhìn ông ta tiếp tục nói.",

    # 59: “你也看到了，我現在需要易緣體內的芯片...”
    "“Cậu cũng thấy rồi đấy, hiện tại tôi cần con chip trong cơ thể Dịch Duyên, chứng cứ bên trong đủ để cứu vãn hàng vạn sinh mạng. Nhưng Dịch Duyên lại không nỡ rời xa cậu đến mức này, cậu chỉ ngoắc ngoắc ngón tay là thằng bé liền bị cậu bắt cóc đi mất. Để phòng ngừa tình huống ngày hôm nay lại tái diễn, cậu có thể ở lại bên cạnh thằng bé với thân phận vệ sĩ. À đúng rồi, bữa tiệc vào tuần tới Dịch Duyên sẽ tham dự với thân phận con nuôi của tôi.”",

    # 60: “呵”婁禧陽笑了...
    "“Hừ,” Lâu Hỉ Dương bật cười, “Xin hãy hiểu cho rõ, mục đích của tôi là tháo bỏ thiết bị trên người cậu ấy, ông giữ tôi ở lại đây chẳng phải là dẫn sói vào nhà hay sao?”",

    # 61: “你盡管取，能取下來算我有眼不識泰山...”
    "“Cậu cứ việc tháo, nếu tháo được thì coi như tôi có mắt không tròng nhận không ra Thái Sơn. Lâu Hỉ Dương, cậu đối với tôi căn bản chẳng có chút giá trị lợi dụng nào, tôi chỉ muốn để Dịch Duyên không phải chịu đựng khổ sở như vậy mà thôi.” Trần Liễm đá đá vào mép giường, châm chọc nói.",

    # 62: “我再給你一次坦白的機會。”婁禧陽沉聲道。
    "“Tôi cho ông thêm một cơ hội để nói thật đấy.” Lâu Hỉ Dương trầm giọng nói.",

    # 63: “好吧，我還看上了你的艾斯匪幫...”
    "“Được rồi, tôi còn nhắm trúng bang phái của cậu ở khu Est nữa. Sau khi lấy được chip ra tôi cần lực lượng vũ trang, ngộ nhỡ bị Tưởng Trác Hàng phát hiện thì còn có vốn liếng liều mạng một phen.” Trần Liễm nhún vai thừa nhận mục đích chính, chợt nhớ ra điều gì, giọng điệu ông ta liền biến đổi, nhìn chằm chằm gáy Dịch Duyên nói: “Cậu không thật sự nghĩ rằng khi cậu đi đánh viện nghiên cứu Tây Lăng Sơn là do vận may tốt gặp đúng lúc hệ thống trục trặc đấy chứ?”",

    # 64: 婁禧陽清晰地感受到身上的易緣一下子繃緊了身子，像受到驚嚇的貓。
    "Lâu Hỉ Dương cảm nhận rõ ràng người Dịch Duyên nằm trên người mình bỗng chốc căng cứng cả người, hệt như một chú mèo bị giật mình hoảng sợ.",

    # 65: 聯想到了當時路過所長辦公室時聽到的話...
    "Liên tưởng tới những lời nghe được lúc đi ngang qua văn phòng Viện trưởng khi đó, sắc mắt Lâu Hỉ Dương biến đổi, rủ mắt nhìn khuôn mặt Dịch Duyên, nhưng Dịch Duyên lại vùi đầu thật chặt, chỉ có thể nhìn thấy chiếc chóp mũi cao thẳng.",

    # 66: “那東西是我弄爛的...”
    "“Thứ đó là do tôi phá hỏng đấy, nếu không nhờ Dịch Duyên tìm tôi trao đổi điều kiện thì cậu làm sao có thể thong dong dạo một vòng là cứu được Lâu An Minh ra chứ? Haizz, cậu nói xem Dịch Duyên sao lại thích cậu đến mức——”",

    # 67: “陳叔！”易緣猛地轉過頭，兩隻眼睛跟小豹子似的瞪著陳斂。
    "“Chú Trần!” Dịch Duyên đột ngột quay phắt đầu lại, hai con mắt tựa như báo con trừng trừng nhìn Trần Liễm.",

    # 68: 陳斂攤著手，訕訕地把話收了回去。
    "Trần Liễm giơ hai tay ra, gượng gạo nuốt lời trở vào.",

    # 69: 婁禧陽挪了一眼目光到易緣身上，眼裡翻湧著看不清的情緒。
    "Lâu Hỉ Dương dời ánh mắt sang người Dịch Duyên, trong mắt cuộn trào những cảm xúc nhìn không thấu.",

    # 70: “我答應你。”他抬頭，“最後一個問題，這裡的第二層樓，關著什麽人？”
    "“Tôi đồng ý với ông.” Anh ngẩng đầu, “Câu hỏi cuối cùng: tầng thứ hai ở nơi này, đang giam giữ ai?”",

    # 71: 陳斂被他問的措不及防...
    "Trần Liễm bị anh hỏi cho bất ngờ trở tay không kịp, “a” cả buổi mới phản ứng lại. Ông ta gãi gãi đầu: “À... Chuyện này có thể nói được chứ nhỉ...”",

    # 72: 糾結了一會兒...
    "Đắn đo giằng xé một hồi, ông ta đột nhiên ghé mặt lại gần trước mặt Lâu Hỉ Dương, thần bí nói: “Cậu có biết tại sao Tưởng Trác Hàng lại tới đây không?”",

    # 73: “嗯？”婁禧陽挑眉。
    "“Hửm?” Lâu Hỉ Dương nhướng mày.",

    # 74: “這裡…關著他的小情人，卑鄙手段搶來的那種！”陳斂一掌拍向床。
    "“Ở đây... Đang giam giữ tình nhân bé nhỏ của hắn ta, cái loại dùng thủ đoạn đê hèn cướp đoạt về ấy!” Trần Liễm vỗ một chưởng thật mạnh xuống giường."
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_022 translation written: {len(paragraphs)} paragraphs.")
