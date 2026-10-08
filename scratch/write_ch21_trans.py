# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_021"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 21: Yêu đương
---""",

    # 1: separator
    "================",

    # 2: 車穿行在狹窄昏暗的小巷...
    "Chiếc xe luồn lách qua những con hẻm nhỏ hẹp u ám, những tấm biển hiệu đèn neon giăng dọc đường để lộ bầu không khí mờ ám của nơi này.",

    # 3: paradise裡的紅燈區...
    "Khu đèn đỏ bên trong Paradise, người của Trương Sâm Trạch đang ở trong cửa tiệm nằm tận sâu cùng.",

    # 4: 易緣在車上的時候又開始發作了...
    "Dịch Duyên khi ở trên xe lại bắt đầu phát tác. Cậu co ro hai đầu gối, rúc vào lòng Lâu Hỉ Dương bên cạnh. Phần thịt ngón tay Lâu Hỉ Dương miết nhẹ sau gáy cậu, liên tục giục Trương Sâm Trạch tăng tốc độ xe lên.",

    # 5: “急什麽，到了。”...
    "“Vội cái gì, tới nơi rồi.” Trương Sâm Trạch đáp một tiếng, ánh mắt sâu thẳm. Sau khi chiếc xe hoàn toàn hạ cánh xuống đất, gã một tay đẩy cửa xe ra, khoanh tay đứng đợi với toàn thân đầy vẻ lệ khí.",

    # 6: 婁禧陽看了眼易緣...
    "Lâu Hỉ Dương liếc nhìn Dịch Duyên, cúi người bế ngang người lên, đón nhận ánh mắt nhìn chăm chú của Trương Sâm Trạch, rảo bước nhanh chóng tiến vào cửa tiệm bình thường không mấy bắt mắt trước mặt.",

    # 7: “工具材料都在這裡了，那些人正在趕來的路上。”
    "“Công cụ vật liệu đều ở đây cả rồi, những người đó đang trên đường chạy tới.” Trương Sâm Trạch quay lưng về phía bọn họ, đầu cũng không thèm ngoảnh lại nói.",

    # 8: “謝謝，麻煩你了，盡量讓他們快點。”婁禧陽腳步一頓。
    "“Cảm ơn, làm phiền cậu rồi, cố gắng bảo họ nhanh lên một chút.” Bước chân Lâu Hỉ Dương khựng lại.",

    # 9: “謝什麽？...”
    "“Cảm ơn cái gì? Trước kia cậu đã giúp tôi bao nhiêu lần rồi, giúp cậu vài lần thì tính là cái gì?” Trương Sâm Trạch mất kiên nhẫn cắt ngang lời anh, đối với sự khách sáo của Lâu Hỉ Dương cảm thấy vô cùng phiền lòng. Gã sải bước chân rời khỏi nơi này.",

    # 10: 婁禧陽把易緣放到簡陋的單人床上...
    "Lâu Hỉ Dương đặt Dịch Duyên xuống chiếc giường đơn sơ sài, quay người liền bắt đầu tìm kiếm dụng cụ để phá hủy hệ thống theo dõi trên người cậu.",

    # 11: “嗚…陽哥，”...
    "“Ưm... Dương ca,” Dịch Duyên mở mắt ra, cảm nhận được xúc cảm nơi sau gáy, vươn tay túm chặt lấy vạt áo Lâu Hỉ Dương, tựa như nhất định phải chạm vào người Lâu Hỉ Dương thì mới có thể tiếp tục nhẫn nhịn chịu đựng.",

    # 12: 婁禧陽垂眸睨了一眼，繼續手上的動作“乖乖躺好，別動。”
    "Lâu Hỉ Dương rủ mắt liếc nhìn một cái, tiếp tục động tác trên tay: “Ngoan ngoãn nằm yên đi, đừng lộn xộn.”",

    # 13: “哦。”易緣很乖地把臉放回了枕頭上，但手卻半點沒松開。
    "“Dạ.” Dịch Duyên rất ngoan ngoãn úp mặt trở lại gối, nhưng bàn tay lại chẳng hề nới lỏng nửa phần.",

    # 14: 他剛剛其實沒那麽痛...
    "Cậu vừa nãy thực ra không đau đến mức đó, chỉ là muốn làm cho Lâu Hỉ Dương căng thẳng một chút mà thôi. Đương nhiên, chủ yếu nhất là để cho cái tên Trương Sâm Trạch kia mở to mắt ra mà nhìn, đừng có nhòm ngó đồ của cậu.",

    # 15: “哥，你又親了我一次。”安靜了片刻，易緣冷不丁地出了聲。
    "“Ca ca, anh lại hôn em thêm một lần nữa rồi.” Yên ắng một lát, Dịch Duyên bất thình lình cất tiếng.",

    # 16: “嗯，抱歉。”...
    "“Ừ, xin lỗi.” Ngữ khí của Lâu Hỉ Dương vô cùng bình thản, như thể đang nói về một chuyện nhỏ nhặt không đáng kể, điều này làm Dịch Duyên nhất thời không biết phải tiếp lời thế nào.",

    # 17: 他趴在床上，看不到此時婁禧陽的表情，用臊的慌來形容都不為過。
    "Cậu nằm sấp trên giường nên không nhìn thấy biểu cảm của Lâu Hỉ Dương lúc này, dùng từ xấu hổ đến đỏ mặt tía tai để hình dung cũng không hề quá chút nào.",

    # 18: 是誰在那天晚上信誓旦旦地向易緣保證自己絕不會再做越界的事？？
    "Là ai vào đêm hôm đó đã thề thốt son sắt bảo đảm với Dịch Duyên rằng bản thân tuyệt đối sẽ không bao giờ làm chuyện vượt ranh giới nữa cơ chứ??",

    # 19: 嘶——臉很疼。
    "Xuýt—— Rát mặt thật đấy.",

    # 20: 易緣皺了皺眉，手指鑽進衣擺...
    "Dịch Duyên nhíu mày, ngón tay luồn vào trong gấu áo, dùng lực nhéo mạnh một cái vào bên hông cứng ngắc của Lâu Hỉ Dương, hoàn toàn chẳng màng việc chính mình là người nhào tới hôn trước, bẻ cong sự thật nói: “Anh vừa hôn vừa cắn em, lại còn cởi quần áo của em... Làm thế này thế nọ với em, anh phải chịu trách nhiệm với em.”",

    # 21: 痛感混合著說不清道不明的酥麻在腰間彌漫...
    "Cảm giác đau đớn hòa lẫn với sự tê dại khó tả lan tỏa nơi thắt lưng, tim Lâu Hỉ Dương nảy thót một cái, có chút giấu đầu hở đuôi: “Em đường đường là đàn ông con trai mà ăn nói bậy bạ cái gì thế, anh giúp em thay đồ chẳng phải vì em không cử động được sao?”",

    # 22: 想了想自己先前的一番行為...
    "Nghĩ lại chuỗi hành động trước đó của mình, anh quả thực đã hôn, cũng đã cắn, thậm chí còn bị mê hoặc bởi cơ thể chẳng khác gì mình kia...",

    # 23: 他根本不明白自己在做些什麽...
    "Anh căn bản không hiểu nổi bản thân đang làm cái gì, chỉ là sau khi Dịch Duyên thốt ra câu nói kia thì anh liền hoàn toàn đánh mất lý trí, trong cơ thể bị một lực vô hình thúc đẩy, cám dỗ anh tiếp tục làm tới cùng.",

    # 24: 婁禧陽的臉是健康的小麥色...
    "Khuôn mặt Lâu Hỉ Dương là màu lúa mì khỏe khoắn, nhưng giờ khắc này đã ngượng đến mức chuyển sang màu hồng nhạt. Anh gồng cứng cánh tay, thành khẩn nhận lỗi: “... Xin lỗi Dịch Duyên, em muốn anh bồi thường cho em thế nào?”",

    # 25: 易緣扇著睫毛...
    "Hàng mi Dịch Duyên khẽ chớp, dường như đang suy nghĩ điều gì, cuối cùng ánh mắt cậu rơi vào vạt áo bên dưới, lí nhí nói: “Em muốn yêu đương cùng anh.”",

    # 26: “什麽？”婁禧陽沒聽清。
    "“Cái gì?” Lâu Hỉ Dương nghe không rõ.",

    # 27: “我說，我想你假裝當我的女朋友，和我談戀愛。”
    "“Em nói là, em muốn anh giả vờ làm bạn gái của em, yêu đương cùng em.” Ngón tay Dịch Duyên siết chặt lại, lớn tiếng nói.",

    # 28: 婁禧陽的動作停了下來...
    "Động tác của Lâu Hỉ Dương dừng lại, một lúc sau mới tiếp tục ra tay hoàn thành phần kết thúc. Anh mím môi, thu lại vẻ sâu thẳm nơi đáy mắt, lặp lại: “Bạn gái, giả vờ? Xác định chứ?”",

    # 29: “嗯，假裝。”易緣閉上眼，確定道。
    "“Vâng, giả vờ.” Dịch Duyên nhắm mắt lại, khẳng định chắc nịch.",

    # 30: 還不是時候，不要把婁禧陽嚇跑...
    "Vẫn chưa tới thời điểm thích hợp, không được dọa cho Lâu Hỉ Dương sợ chạy mất. Cậu ở trong lòng hết lần này đến lần khác tự khuyên nhủ bản thân, chỉ là thế nào cũng không thể thỏa mãn với điều này.",

    # 31: 婁禧陽將取下的零件往垃圾桶裡一扔，仰身倒在座椅的靠背上。
    "Lâu Hỉ Dương ném linh kiện vừa tháo được vào thùng rác, ngả người tựa vào lưng ghế.",

    # 32: “我答應你易緣。”
    "“Anh đồng ý với em, Dịch Duyên.”",

    # 33: 易緣似乎有些激動...
    "Dịch Duyên dường như có chút kích động, cậu thoắt cái ngồi bật dậy khỏi giường, mặt đối mặt đón lấy ánh mắt của Lâu Hỉ Dương.",

    # 34: “不過我是男的，不是女朋友。”...
    "“Có điều anh là đàn ông, không phải bạn gái.” Lâu Hỉ Dương nhấn mạnh, rồi sau đó lại nghi hoặc nhíu mày, “Yêu đương, thì phải làm như thế nào?”",

    # 35: 易緣沒有吱聲...
    "Dịch Duyên không lên tiếng, cậu đè nén nhịp tim đang đập quá nhanh của mình, quỳ gối nhích lại gần Lâu Hỉ Dương, chống người ngồi lên đùi Lâu Hỉ Dương.",

    # 36: 婁禧陽見狀扶了一下他的腰...
    "Lâu Hỉ Dương thấy vậy liền đỡ lấy eo cậu vì sợ cậu ngã xuống, tay còn chưa kịp rút về thì Dịch Duyên đã ôm chầm lấy anh.",

    # 37: “談戀愛就是，...”
    "“Yêu đương chính là,” Dịch Duyên đặt tay lên mu bàn tay anh, từ từ chuyển từ ngồi sang quỳ, dựa nửa thân trên vào người anh, “Tất cả những việc hôm nay Dương ca làm với em đều có thể làm, hơn nữa còn...”",

    # 38: 婁禧陽感覺到自己的手指縫正被易緣的手緩慢摩擦，然後扣緊。
    "Lâu Hỉ Dương cảm nhận được kẽ ngón tay mình đang được bàn tay Dịch Duyên chậm rãi mơn trớn, rồi sau đó đan chặt mười ngón tay vào nhau.",

    # 39: 他湊近他的左耳，低聲說了些什麽。
    "Cậu ghé sát tai trái anh, thấp giọng thì thầm điều gì đó.",

    # 40: 婁禧陽的腦子空白了兩三秒...
    "Đầu óc Lâu Hỉ Dương trống rỗng suốt hai ba giây, ngay sau đó bàn tay như bị kim châm, nhanh chóng rút ra khỏi nơi đó.",

    # 41: 他繃著臉，將易緣抱回了床上...
    "Anh căng cứng mặt, bế Dịch Duyên đặt trở lại giường: “Anh thấy như vậy không đúng, vẫn là đợi anh tìm hiểu trước đã.”",

    # 42: 易緣無辜地抬頭看他...
    "Dịch Duyên ngây thơ ngẩng đầu nhìn anh. Cậu nhớ các cặp đôi trong những bộ phim cậu từng xem đều như vậy cả, trước tiên hôn hôn, rồi sờ sờ, tiếp theo là lăn lộn cùng một chỗ.",

    # 43: 正欲說些什麽時，外面傳來了一陣腳步聲。
    "Đang định nói gì đó thì bên ngoài truyền đến một tràng tiếng bước chân.",

    # 44: “陽陽，他們到了。”...
    "“Dương Dương, bọn họ tới rồi.” Trương Sâm Trạch dẫn theo mấy người đàn ông bước vào, phá vỡ bầu không khí mờ ám như có như không trong phòng.",

    # 45: 他眯著眼，在易緣身上打量。
    "Gã híp mắt, đánh giá trên người Dịch Duyên.",

    # 46: 婁禧陽站起身，將幾個人迎進門...
    "Lâu Hỉ Dương đứng dậy đón mấy người vào cửa: “Làm phiền các anh rồi, thiết bị trên người cậu ấy, hy vọng các anh có thể tận hết sức lực tháo gỡ ra, sau khi xong việc nhất định sẽ có hậu tạ.”",

    # 47: 領頭的眼鏡男掃了一眼易緣的後頸...
    "Gã đeo kính dẫn đầu quét mắt nhìn sau gáy Dịch Duyên một cái, có chút khó xử: “Tiên sinh, với năng lực của chúng tôi, e rằng chỉ có thể dốc hết sức mà thôi.”",

    # 48: 婁禧陽聞言拍了拍他的肩膀...
    "Lâu Hỉ Dương nghe vậy vỗ vỗ vai gã, trao cho Dịch Duyên một ánh mắt trấn an rồi quay người bước ra ngoài.",

    # 49: 他靠在商鋪外的牆上...
    "Anh tựa vào bức tường bên ngoài cửa tiệm, nhìn biển hiệu nhấp nháy phía trước mà chìm vào trầm tư.",

    # 50: 易緣說他離開治療所超過四小時，摘除芯片就徹底失敗了。
    "Dịch Duyên nói cậu rời khỏi viện điều trị quá bốn tiếng thì việc trích xuất chip sẽ hoàn toàn thất bại.",

    # 51: 垂眸看向終端，這個時候，已經離他們離開過了三個小時。
    "Rủ mắt nhìn thiết bị đầu cuối, lúc này đã trôi qua ba tiếng kể từ khi bọn họ rời khỏi đó.",

    # 52: 他不在意芯片...
    "Anh không quan tâm đến con chip, cho nên anh chẳng để tâm đến một tiếng đồng hồ ít ỏi còn lại, nhưng anh bận tâm lời của gã đeo kính kia. Trông cậy vào bọn họ tháo thiết bị ra ít nhất cũng phải mười ngày nửa tháng, điều đó đồng nghĩa với việc Dịch Duyên phải chịu đựng hàng trăm cơn đau đớn hành hạ.",

    # 53: 很煩。
    "Phiền phức chết đi được.",

    # 54: 他頂了頂腮幫，快速思考著更快的方案。
    "Anh đưa lưỡi chống nhẹ lên má, nhanh chóng suy tính phương án nhanh hơn.",

    # 55: 就在這個時候，他的終端亮了起來...
    "Đúng vào lúc này, thiết bị đầu cuối của anh sáng lên, bên trên hiển thị một chuỗi mã ký tự lộn xộn. Anh nhận ra loại mã này, thường là nguồn tin được mã hóa qua nhiều tầng lớp.",

    # 56: 等待了片刻，他接通了電話。
    "Đợi một lát, anh bắt máy.",

    # 57: “喂。”
    "“Alo.”",

    # 58: “你把易緣帶去了哪裡？！——”...
    "“Cậu đã đưa Dịch Duyên đi đâu rồi hả?!——” Đầu dây bên kia vang lên một tiếng rống giận dữ, âm thanh bị biến đổi qua dữ liệu trở nên the thé chói tai, thể hiện rõ sự nôn nóng và thịnh nộ của người nói.",

    # 59: “與你無關。”婁禧陽站直了身子，語氣發沉。
    "“Không liên quan tới ông.” Lâu Hỉ Dương đứng thẳng người dậy, ngữ khí trầm xuống.",

    # 60: “還有一個小時，馬上帶他回治療所，這不是小事，你別害了所有人！”
    "“Còn đúng một tiếng nữa, lập tức đưa thằng bé quay về viện điều trị, đây không phải chuyện đùa đâu, cậu đừng có hại chết tất cả mọi người!”",

    # 61: “陳斂。”婁禧陽喊出聲...
    "“Trần Liễm.” Lâu Hỉ Dương gọi thẳng tên ra, đầu bên kia yên ắng một thoáng. “Ông muốn làm gì, tưởng tôi không biết sao? Tưởng Trác Hàng chắc chắn không biết những việc ông đang làm đâu nhỉ.”",

    # 62: 蔣卓航的目的是毀掉M星...
    "Mục đích của Tưởng Trác Hàng là hủy diệt hành tinh M, vậy thì hắn ta hoàn toàn không cần thiết phải tốn bao công sức lấy chân tướng trong cơ thể Dịch Duyên ra làm gì, cứ để nó vĩnh viễn chìm vào bóng tối chưa được biết tới là xong.",

    # 63: 所以他在賭，賭陳斂所做的一切，都是背著蔣卓航的視線。
    "Cho nên anh đang đánh cược, cược rằng tất cả những gì Trần Liễm làm đều là giấu giếm sau lưng tầm mắt của Tưởng Trác Hàng.",

    # 64: 他暫且不明白他的動機...
    "Anh tạm thời chưa hiểu động cơ của ông ta, nhưng anh chán ghét Trần Liễm một cách rõ ràng, chán ghét tất cả những gì ông ta đã làm với Dịch Duyên.",

    # 65: 陳斂吐了一口長氣...
    "Trần Liễm thở dài một hơi dài, bình tĩnh lại: “Lâu Hỉ Dương, xuất phát điểm của tôi là vì hành tinh M. Hiện tại chân tướng sắp sửa bị chính tay cậu hủy hoại rồi, tính mạng của hàng vạn con người, cậu đền nổi không?”",

    # 66: “你以為我會相信當年親手殺害了一整個麥克家族的人嗎？”...
    "“Ông nghĩ tôi sẽ tin tưởng một kẻ năm xưa từng tự tay sát hại cả gia tộc Michael sao?” Lâu Hỉ Dương cười nhạo một tiếng, anh không cho rằng con người này lại có tấm lòng nhân từ giải cứu chúng sinh, “Còn nữa, tôi không quan tâm đến con chip này.”",

    # 67: “婁禧陽！”對面咬牙切齒地叫住了他...
    "“Lâu Hỉ Dương!” Đầu bên kia nghiến răng nghiến lợi gọi giật anh lại, “Cậu là người thế nào tôi đã điều tra bao nhiêu năm nay rất rõ ràng, người mong muốn hành tinh M trở lại quỹ đạo nhất chính là cậu, tại sao lại làm như vậy!”",

    # 68: “易緣有多痛苦你看不見是嗎？”...
    "“Dịch Duyên đau đớn thế nào ông bị mù không nhìn thấy đúng không?” Ngữ khí của Lâu Hỉ Dương lạnh lẽo tựa như lưỡi dao đóng băng, “Tốt nhất đừng để tôi gặp lại ông, bằng không tôi sẽ khiến ông phải đích thân nếm thử mùi vị đó đấy.”",

    # 69: 話說完，婁禧陽抬手，欲要掛斷。
    "Nói dứt lời, Lâu Hỉ Dương giơ tay toan cúp máy.",

    # 70: “等等——婁禧陽，一個小時他要是不會到治療所，他就會死！”
    "“Chờ đã—— Lâu Hỉ Dương, một tiếng nữa nếu thằng bé không về tới viện điều trị thì nó sẽ chết đấy!” Giọng Trần Liễm cuống quýt tới mức vỡ cả tiếng.",

    # 71: “你說什麽？”...
    "“Ông nói cái gì?” Lâu Hỉ Dương khựng lại, rồi sau đó chậm rãi và nguy hiểm ghé sát thiết bị đầu cuối, “Mẹ nó ông muốn chết à.”",

    # 72: 陳斂冷靜下來...
    "Trần Liễm bình tĩnh lại: “Thiết bị đó cậu không tháo được đâu, hiện tại còn năm mươi phút nữa, nếu cậu dám lấy mạng nó ra đánh cược thì tôi cũng tiếp chiêu tới cùng.”",

    # 73: 耳邊是滴滴滴的忙音...
    "Bên tai là những tiếng tút tút bận máy. Bàn tay buông thõng bên chân từng chút từng chút siết chặt lại, những đường gân xanh chằng chịt từ mu bàn tay bò lan lên tận cánh tay.",

    # 74: 艸。
    "Mẹ kiếp.",

    # 75: 指節狠狠地砸向牆面，老舊的牆面上瞬間多出了裂痕。
    "Đốt ngón tay nện dữ dội vào bức tường, trên mảng tường cũ kỹ tức khắc nứt toác ra những đường rạn vỡ.",

    # 76: 婁禧陽用拳頭撐著牆，翻湧的戾氣壓都壓不住。
    "Lâu Hỉ Dương dùng nắm đấm chống vào tường, lệ khí cuộn trào đè thế nào cũng không đè xuống nổi.",

    # 77: 像是在應證陳斂的話...
    "Như để minh chứng cho lời của Trần Liễm, gã đeo kính từ trong phòng bước ra ngoài, vẻ mặt tiếc nuối lắc đầu với anh: “Thật ngại quá tiên sinh, khối thiết bị đó đã bị người ta cải tạo lại rồi, chúng tôi không tháo được.”",

    # 78: 眼鏡男說著說著就沒了聲音，因為他被眼前的這雙眼睛嚇愣了。
    "Gã đeo kính vừa nói vừa tắt ngấm tiếng, bởi vì gã đã bị đôi mắt trước mặt dọa cho chết trân.",

    # 79: 婁禧陽放下拳，低頭看了眼時間。
    "Lâu Hỉ Dương hạ nắm đấm xuống, cúi đầu liếc nhìn thời gian.",

    # 80: 四十五分鍾。
    "Bốn mươi lăm phút.",

    # 81: 開車趕過去是四十分鍾。
    "Lái xe chạy tới đó mất bốn mươi phút.",

    # 82: 他快步衝進屋內...
    "Anh rảo bước lao vút vào trong phòng, gạt phăng mấy gã đàn ông chắn trước mặt ra, bế bổng Dịch Duyên lên.",

    # 83: 易緣沒反應過來他這番舉動...
    "Dịch Duyên chưa kịp phản ứng trước hành động này của anh, theo bản năng ôm chặt lấy cổ anh: “Dương ca, anh định làm gì thế?”",

    # 84: 婁禧陽沒說話...
    "Lâu Hỉ Dương không nói lời nào, thuận tay cầm lấy chìa khóa xe của Trương Sâm Trạch rồi sải bước không ngừng nghỉ đi ra ngoài, ôm Dịch Duyên lên xe.",

    # 85: 隨著車門關上，窗外的景色被遠遠甩在了後面。
    "Theo cánh cửa xe đóng lại, cảnh sắc ngoài cửa sổ bị bỏ lại tít đằng sau.",

    # 86: 易緣安靜地坐在角落...
    "Dịch Duyên im lặng ngồi trong góc, nhìn con đường vừa mới đi qua cách đây không lâu: “Anh muốn đưa em quay về sao?”",

    # 87: 婁禧陽伸手握住了他的手腕“要是離開那裡四個小時，你會死。”
    "Lâu Hỉ Dương vươn tay nắm chặt lấy cổ tay cậu: “Nếu như rời khỏi nơi đó quá bốn tiếng, em sẽ chết.”",

    # 88: 易緣悻悻地點了點頭...
    "Dịch Duyên buồn bã gật gật đầu, chuyển mắt nhìn ra ngoài cửa sổ, một lúc sau mới cất lời: “Em cứ ngỡ mình thực sự có thể rời khỏi nơi đó, ở bên cạnh anh.”",

    # 89: “會的小緣，等等我。”...
    "“Sẽ làm được thôi Tiểu Duyên, chờ anh.” Đợi anh tìm ra cách phá giải nó. Lâu Hỉ Dương nhìn thời gian trước mắt, nếu không có gì bất trắc thì có thể đưa Dịch Duyên trở về đúng giờ.",

    # 90: 易緣罕見的沒有跟他黏黏糊糊，只是沉默地埋著頭，看上去很沮喪。
    "Dịch Duyên hiếm hoi không bám riết lấy anh nhõng nhẽo nữa, chỉ im lặng cúi gằm đầu, trông vô cùng ủ rũ chán chường.",

    # 91: paradise的建設還處於開發階段，去往治療所的路線基本上見不著一個人影。
    "Công trình xây dựng Paradise vẫn đang trong giai đoạn khai phá, lộ trình đi tới viện điều trị căn bản chẳng thấy lấy một bóng người.",

    # 92: “哐啷——”...
    "“RẦM——” Tiếng vỏ sắt bị va chạm dữ dội vỡ vụn vang lên, lực xung kích ập tới từ phía sau lưng Lâu Hỉ Dương, kéo anh ngã nhào về phía trước.",

    # 93: 他迅速接過跌過來的易緣，讓他撞到他的懷裡。
    "Anh nhanh tay đón lấy Dịch Duyên đang ngã nhào tới, để cậu va trúng vào lòng mình.",

    # 94: 怎麽回事？
    "Chuyện gì xảy ra thế này?",

    # 95: sorry，存稿發完了加上最近很忙……
    "Xin lỗi mọi người, bản thảo dự trữ đã đăng hết cộng thêm dạo này rất bận……",

    # 96: 放心，會寫完的！謝謝寶貝們的營養液！
    "Yên tâm nhé, nhất định sẽ viết xong! Cảm ơn các bảo bối đã tưới dung dịch dinh dưỡng!"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_021 translation written: {len(paragraphs)} paragraphs.")
