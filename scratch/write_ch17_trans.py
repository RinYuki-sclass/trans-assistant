# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_017"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 17: Anh đã làm gì
---""",

    # 1: separator
    "====================",

    # 2: 護工抓著他的手緊了又緊...
    "Người hộ lý nắm chặt lấy tay anh siết chặt từng hồi, nom bộ dạng có vẻ khá căng thẳng.",

    # 3: 婁禧陽低頭看他...
    "Lâu Hỉ Dương cúi đầu nhìn cậu, nhận ra người hộ lý này là nghiêm túc thật sự, chẳng nghĩ ra lý do gì để từ chối, bèn dứt khoát thuận theo sức kéo của cậu mà bước vào nhà vệ sinh.",

    # 4: 轉向牆壁...
    "Quay mặt vào tường, Lâu Hỉ Dương cử động cánh tay đang bị cậu nắm lấy: “Làm phiền cậu rồi.”",

    # 5: 他忽然出聲...
    "Anh đột ngột lên tiếng khiến người hộ lý giật nảy mình một cái, vội vàng rụt tay lại, thế nhưng vẫn đứng im tại chỗ không hề nhúc nhích.",

    # 6: 都是男的，婁禧陽也不介意什麽...
    "Đều là đàn ông cả, Lâu Hỉ Dương cũng chẳng để tâm điều gì. Một tay anh vén góc áo bệnh nhân lên, một tay kéo cạp quần xuống, để lộ trọn vẹn vết thương nơi bụng dưới cùng những vết bầm tím do đòn quyền cước để lại xung quanh.",

    # 7: 男人微弓著腰...
    "Người đàn ông hơi khom lưng, dải băng gạc quấn quanh đường nhân ngư cơ bắp ngày một rõ nét, hoóc-môn nam tính phả thẳng vào mặt khiến ánh mắt người hộ lý bên cạnh hoang mang tan rã.",

    # 8: 但是他很快就變了臉色。
    "Thế nhưng cậu rất nhanh đã biến đổi sắc mặt.",

    # 9: 因為婁禧陽的傷口裂開了。
    "Bởi vì vết thương của Lâu Hỉ Dương đã bị rách ra.",

    # 10: 由於婁禧陽一點也不顧及傷口...
    "Do Lâu Hỉ Dương một chút cũng không đoái hoài kiêng dè vết thương, trên bề mặt lớp băng gạc quấn quanh bụng dưới đã rỉ ra một vệt máu đỏ tươi.",

    # 11: “你為什麽不好好躺在床上。”
    "“Tại sao anh không chịu ngoan ngoãn nằm yên trên giường hả?” Người hộ lý bên cạnh bất thình lình thốt lên một câu, ánh mắt sắc như dao găm lập tức phóng thẳng lên mặt Lâu Hỉ Dương.",

    # 12: “明明受了傷，還到處亂跑...”
    "“Rõ ràng đang bị thương mà lại chạy loạn khắp nơi, ngay cả kim truyền dịch cũng bị anh giật ra, bây giờ vết thương lại toác ra rồi, lát nữa mà nhiễm trùng thì phải làm sao đây?”",

    # 13: 護工突然伸出手...
    "Người hộ lý đột ngột vươn tay ra, đầu ngón tay chạm nhẹ lên mép băng gạc, nhẹ như lông vũ, cọ vào khiến anh thấy ngứa ngáy từng hồi.",

    # 14: 婁禧陽被他這番舉動搞得一愣一愣的...
    "Lâu Hỉ Dương bị chuỗi hành động này của cậu làm cho ngây người ra. Anh nhìn ngón tay cẩn thận từng li từng tí của người hộ lý, một cảm giác tê rần khó tả như có luồng điện chạy qua truyền thẳng từ nơi cậu chạm vào lên tận não bộ.",

    # 15: “我沒事。”婁禧陽後退一步，躲開了他的手。
    "“Tôi không sao.” Lâu Hỉ Dương lùi lại một bước, né tránh bàn tay của cậu.",

    # 16: 他真不覺得有什麽大不了。
    "Anh thực sự không thấy có gì to tát.",

    # 17: 這種傷他兩輩子受得夠多了...
    "Vết thương kiểu này hai kiếp anh đã nếm trải quá đủ rồi. Dựa theo kinh nghiệm của anh, chưa đầy nửa tháng là có thể khỏi hẳn. Hiện tại toác ra chứng tỏ lành càng chậm hơn, đối với anh mà nói lại là một chuyện tốt, như vậy anh mới có thể tiếp tục ở lại nơi này để tìm kiếm tung tích của mẹ mình.",

    # 18: 只是這個假護工著什麽急？
    "Chỉ có điều cái tên hộ lý giả mạo này cuống cuồng cái gì chứ?",

    # 19: 等等，這些話聽著怎麽那麽耳熟？好像跟易緣的口吻差不多。
    "Khoan đã, mấy lời này nghe sao mà quen tai thế nhỉ? Hình như chẳng khác gì khẩu khí của Dịch Duyên.",

    # 20: 可是這不可能...
    "Thế nhưng điều này là không thể nào. Dịch Duyên hiện tại đang ở trong tay Trần Liễm, tuyệt đối không thể xuất hiện tại nơi mẫn cảm nhất đối với Tưởng Trác Hàng như thế này, lại còn biến thành một hộ lý hành vi quái đản.",

    # 21: 而且兩個人聲音也不一樣...
    "Hơn nữa giọng nói của hai người cũng chẳng giống nhau, người hộ lý này cao hơn Dịch Duyên năm sáu phân, chạm tới tận cằm anh rồi.",

    # 22: 婁禧陽剛才注意過其它病房...
    "Lâu Hỉ Dương ban nãy đã để ý các phòng bệnh khác, quả thực có vài phòng được bố trí hộ lý, mà hộ lý này chắc chắn là một trong những tai mắt được cố ý cài cắm vào, chỉ là vừa vặn phân công trúng anh mà thôi.",

    # 23: 所以，他這是太入戲了嗎？
    "Cho nên, cậu ta đây là diễn quá nhập tâm rồi sao?",

    # 24: 想到這裡，婁禧陽欲言又止地看了他一眼...
    "Nghĩ đến đây, Lâu Hỉ Dương muốn nói lại thôi liếc nhìn cậu một cái: “... Hiện tại tôi muốn đi tiểu, cậu có thể đừng chắn ngay trước mặt tôi thế này không?”",

    # 25: 而且就算兩個男人沒什麽，但他這種一動不動盯著他那看的真得很奇怪。
    "Hơn nữa cho dù hai người đàn ông chẳng có gì đi nữa, nhưng cái kiểu đứng bất động nhìn chằm chằm vào chỗ đó của anh thực sự là kỳ quặc hết sức.",

    # 26: 護工聞言立刻閃到了他身後...
    "Người hộ lý nghe vậy lập tức né sang phía sau lưng anh, cúi gằm đầu xuống thật sâu, dường như có chút ngượng ngùng xấu hổ.",

    # 27: 連婁禧陽放完水轉過身來都沒發現。
    "Đến mức Lâu Hỉ Dương giải quyết xong quay người lại lúc nào cũng không hay biết.",

    # 28: 然後婁禧陽就看見了他防護服下面的衣領上，沾著鮮紅的血，看上去還是不久前沾上的。
    "Thế rồi Lâu Hỉ Dương liền nhìn thấy trên cổ áo bên dưới bộ đồ bảo hộ của cậu dính những vệt máu đỏ tươi, trông như vừa mới dính phải cách đây không lâu.",

    # 29: 看來在剛才他消失的那段時間裡，去做了見不得人的事。
    "Xem ra trong khoảng thời gian biến mất ban nãy, cậu ta đã đi làm chuyện gì đó mờ ám không thể cho ai biết.",

    # 30: 婁禧陽在這一刻確定了這人絕對不是簡單的護工...
    "Lâu Hỉ Dương ngay khoảnh khắc này đã khẳng định chắc nịch người này tuyệt đối không phải hộ lý đơn thuần. Anh bất động thanh sắc thu hồi ánh mắt, lướt qua vai người hộ lý tới bồn rửa tay, rồi lại được hộ lý dìu đỡ nằm trở lại giường bệnh.",

    # 31: 後來護工叫來了主治醫生...
    "Về sau người hộ lý gọi bác sĩ điều trị chính tới xử lý lại miệng vết thương, tay phải của anh lại một lần nữa bị trói buộc bởi dây truyền nước muối.",

    # 32: 不得不說，這個護工真適合去演戲...
    "Phải công nhận rằng, người hộ lý này quả thực rất thích hợp đi đóng kịch, vừa nhập vai là không dừng lại nổi, mọi phương diện đều chăm sóc anh chu đáo đến từng chân tơ kẽ tóc, trường phái trải nghiệm nhập vai sâu sắc không ai khác ngoài cậu ta.",

    # 33: “吃飯。”
    "“Ăn cơm.”",

    # 34: 護工端著一個鐵盤，將杓子喂到了他的嘴前。
    "Người hộ lý bưng một chiếc khay sắt, đưa thìa đút tới tận khóe miệng anh.",

    # 35: 婁禧陽將唇抿得老緊，垂眼掃了一遍鐵盤裡的東西。
    "Lâu Hỉ Dương mím chặt môi, rủ mắt quét nhìn một lượt những món ăn trên khay sắt.",

    # 36: 雞蛋，米粥，還有清水煮雞胸肉。
    "Trứng gà, cháo hoa, cùng với ức gà luộc nước trong.",

    # 37: 這些都是宣告末日前M星最普遍的食物...
    "Đây đều là những món ăn phổ biến nhất trên hành tinh M trước ngày tuyên bố mạt thế, thế mà đặt vào hiện tại lại là món xa xỉ phẩm mà người bên ngoài ngay cả mơ cũng không dám mơ tới.",

    # 38: 他們甚至可以為了一塊壓縮餅乾拚命...
    "Bọn họ thậm chí có thể liều mạng vì một mẩu bánh quy nén, cho dù bánh quy nén nuốt vào nhạt như nhai sáp, nhưng chỉ một miếng thôi cũng đủ duy trì sự sống cho họ suốt cả ngày trời.",

    # 39: 婁禧陽突然想起那個瘦的雙加凹陷的小女孩...
    "Lâu Hỉ Dương đột nhiên nhớ tới bé gái gầy gò má hóp sâu hoắm kia. Anh nhớ khi mình đặt gói bánh quy nén vào tay cô bé, đôi mắt em đã sáng rực lên, đó là ngọn lửa của sự sống được thắp sáng trở lại.",

    # 40: 如果沒有這所謂的末日，一切的一切都不會發生。
    "Nếu như không có cái gọi là tận thế này, tất cả mọi chuyện đều sẽ không xảy ra.",

    # 41: 婁禧陽半闔著眼，思緒遊離。
    "Lâu Hỉ Dương khép hờ mắt, dòng suy nghĩ phiêu du.",

    # 42: “paradise裡的人，吃得都很好。”...
    "“Người ở trong Paradise đều ăn uống rất ngon.” Chẳng rõ vì nguyên cớ gì, người hộ lý đột nhiên thốt lên một câu: “Ăn mau đi, đừng lãng phí, vào thời buổi này lãng phí rồi là không còn nữa đâu.”",

    # 43: 察覺到護工像是在安慰他...
    "Nhận thấy người hộ lý dường như đang an ủi mình, Lâu Hỉ Dương dời ánh mắt lên chiếc mặt nạ phòng hộ trên mặt cậu, một lát sau mới nói: “Cậu để ở đây đi, tôi có thể dùng tay trái để ăn.”",

    # 44: “不行，”護工動作頓了一秒...
    "“Không được,” động tác người hộ lý khựng lại một giây, dùng giọng điệu cứng rắn bổ sung thêm, “Đây là công việc của tôi, xin anh hãy tôn trọng tôi.”",

    # 45: 婁禧陽沉默地和他對視，最終啟唇將眼前的米粥咽了下去。
    "Lâu Hỉ Dương im lặng nhìn thẳng vào mắt cậu, cuối cùng hé môi nuốt thìa cháo trước mặt xuống.",

    # 46: 護工的動作很小心...
    "Động tác của người hộ lý rất cẩn thận, cậu dường như rất thấu hiểu anh đang nghĩ gì: nóng thì chờ một chút rồi mới đút tiếp, khát thì canh liền được đưa tới miệng ngay.",

    # 47: 除了易緣，婁禧陽沒有被任何人這樣照顧過。
    "Ngoại trừ Dịch Duyên ra, Lâu Hỉ Dương chưa từng được bất kỳ ai chăm sóc chu đáo như vậy.",

    # 48: 婁禧陽從小就很獨立...
    "Lâu Hỉ Dương từ nhỏ đã rất tự lập, Lâu An Minh quanh năm suốt tháng chẳng mấy ngày ở nhà, anh cũng không thích bảo mẫu chăm sóc, trước giờ luôn sống một mình, cho dù có ốm đau bệnh tật cũng chỉ tự mình uống chút thuốc là xong chuyện.",

    # 49: 所以在搬到易緣對面之前，他不知道被人關心照顧是什麽感覺。
    "Cho nên trước khi dọn đến sống đối diện nhà Dịch Duyên, anh chưa từng biết cảm giác được người khác quan tâm chăm sóc là như thế nào.",

    # 50: 他到現在還記得他第一次替易天辦事受傷，易緣替他上藥時的情景。
    "Anh đến tận bây giờ vẫn còn nhớ rõ cảnh tượng lần đầu tiên anh làm việc giúp Dịch Thiên bị thương, Dịch Duyên bôi thuốc cho anh.",

    # 51: 那個時候小孩緊張兮兮的不停地往他腦門上吹氣...
    "Khi ấy đứa nhỏ lo lắng căng thẳng không ngừng thổi hơi phù phù lên trán anh, giọng sữa ngọt ngào dính dấp liên tục hỏi anh có đau không.",

    # 52: 也是在那個時候，他決定把易緣當成他的家人，要把他當做自己的親弟弟一樣照顧。
    "Cũng chính vào lúc đó, anh đã quyết định xem Dịch Duyên như người nhà của mình, muốn chăm sóc cậu như em trai ruột thịt.",

    # 53: 思緒被拉到從前...
    "Ký ức bị kéo về quá khứ, Lâu Hỉ Dương có chút thất thần, đương nhiên không hề nhận ra đôi bàn tay đang đút thức ăn cho mình đang run lên mất kiểm soát.",

    # 54: 兩人簡單機械的重複著這個動作，很快婁禧陽就吃完了。
    "Hai người lặp đi lặp lại động tác đơn giản máy móc này, rất nhanh Lâu Hỉ Dương đã ăn xong.",

    # 55: 他躺在床上，聽見護工關門出去的聲音，緩緩閉上了眼睛。
    "Anh nằm trên giường, nghe thấy tiếng người hộ lý đóng cửa bước ra ngoài, chậm rãi nhắm mắt lại.",

    # 56: *
    "*",

    # 57: 易緣端著餐盤出了病房...
    "Dịch Duyên bưng khay cơm bước ra khỏi phòng bệnh, bước chân thoăn thoắt đem khay trả về xe đẩy thức ăn, đi vòng vèo rẽ trái rẽ phải đi thang máy bí mật trở về tầng thượng của viện điều trị.",

    # 58: 取下防護面罩的那一刻，他感受到了空氣流通的快意。
    "Khoảnh khắc tháo mặt nạ phòng hộ xuống, cậu cảm nhận được khoái cảm khi không khí được lưu thông dễ chịu.",

    # 59: 面罩在他的臉上留下了深深的紅印...
    "Chiếc mặt nạ để lại những vết hằn đỏ sâu hoắm trên khuôn mặt cậu, nhưng cũng không che giấu được gương mặt đang trắng bệch đến dọa người.",

    # 60: 他忍受著鋪天蓋地的眩暈感，靠著牆壁往實驗室裡走。
    "Cậu cắn răng chịu đựng cảm giác choáng váng đầu óc ngợp trời ngợp đất, men theo vách tường bước về phía phòng thí nghiệm.",

    # 61: 視線裡突然出現了一雙皮鞋...
    "Trong tầm mắt đột nhiên xuất hiện một đôi giày da, đôi giày được chế tác tinh xảo, vừa nhìn đã biết giá trị không hề tầm thường.",

    # 62: “易緣，你今天出去做了什麽。”
    "“Dịch Duyên, hôm nay cháu ra ngoài làm cái gì.”",

    # 63: 雖然是問句...
    "Tuy rằng là một câu hỏi, nhưng ngữ khí giận dữ của người đàn ông đã để lộ ra rằng ông ta đều biết hết tất cả, và vô cùng bất mãn với hành vi của cậu.",

    # 64: “你把李彪搞了個半死不活，現在他爸發了瘋地在找你你知不知道？！”
    "“Cháu đánh Lý Bưu ra nông nỗi nửa sống nửa chết, hiện tại cha nó đang phát điên lên lùng sục tìm cháu, cháu có biết không hả?!”",

    # 65: “他不知道我是誰。”易緣冷聲嗆道。
    "“Hắn ta không biết cháu là ai.” Dịch Duyên lạnh giọng cãi lại.",

    # 66: 他抬起臉，滿臉的冷汗讓陳斂將後面的話吞回了肚子裡。
    "Cậu ngẩng mặt lên, khuôn mặt đầm đìa mồ hôi lạnh khiến Trần Liễm phải nuốt những lời định mắng tiếp theo trở vào bụng.",

    # 67: 陳斂歎了口氣...
    "Trần Liễm thở dài một hơi, bước lên một tay đỡ lấy cậu vào phòng thí nghiệm, đẩy cậu vào khoang thí nghiệm.",

    # 68: “怪我，不應該把他的消息告訴你，還放縱你去找他。”...
    "“Trách chú, không nên nói tin tức của cậu ta cho cháu biết, lại còn dung túng cho cháu đi tìm cậu ta.” Trần Liễm vạch cổ áo sau gáy cậu ra, xác nhận tiến trình bóc tách con chip không có sai sót mới yên tâm thở phào.",

    # 69: 易緣蹬掉藏了內增高的鞋...
    "Dịch Duyên đạp phăng đôi giày có độn đế giấu chiều cao bên trong ra, ngón tay ấn lên sau gáy, nơi đó chính là nguồn cơn của mọi đau đớn trên người cậu.",

    # 70: 他的後頸裡有一塊芯片，是他媽留下的，裡面是她收集的末日真相。
    "Sau gáy cậu có một con chip do mẹ cậu để lại, bên trong chứa đựng toàn bộ chân tướng ngày tận thế mà bà thu thập được.",

    # 71: 後頸嵌入的芯片提取器連接著這個治療所的中心系統...
    "Thiết bị trích xuất chip được khảm sau gáy kết nối trực tiếp với hệ thống trung tâm của viện điều trị này, hai bên không thể ngắt kết nối trong thời gian dài, vì vậy cậu bắt buộc mỗi ngày phải có hai mươi tiếng đồng hồ không được rời khỏi tòa nhà này nửa bước.",

    # 72: 除了不能出去外...
    "Ngoài việc không thể ra ngoài, nỗi đau đớn lớn nhất chính là nó gây ra những cơn co thắt tim, ngắt quãng đứt đoạn nhưng lại kéo dài liên miên bất tận, tựa như vô số lưỡi dao mềm mặc sức đâm chọc giày vò trên người cậu.",

    # 73: “你說了，我的要求你都會滿足。”...
    "“Chú đã nói rồi, yêu cầu của cháu chú đều sẽ thỏa mãn.” Dịch Duyên hít sâu một hơi, cảm nhận cơn đau đớn đang dần dần thoái trào.",

    # 74: 或許是陳斂覺得虧欠他，對他還算有求必應。
    "Có lẽ là Trần Liễm cảm thấy nợ cậu, nên đối với cậu vẫn coi như cầu được ước thấy.",

    # 75: 當他從陳斂口中得知婁禧陽進了paradise...
    "Khi cậu nghe Trần Liễm nói Lâu Hỉ Dương đã vào Paradise, thậm chí chỉ cách cậu vài tầng lầu, cậu đã hưng phấn đến mức toàn thân nóng rực lên.",

    # 76: 這是天意，老天都不讓婁禧陽離開他，婁禧陽隻屬於他。
    "Đây chính là ý trời, ông trời cũng không cho phép Lâu Hỉ Dương rời xa cậu, Lâu Hỉ Dương chỉ thuộc về một mình cậu.",

    # 77: 想到這裡，易緣的眼底漫上了一層黑霧...
    "Nghĩ đến đây, đáy mắt Dịch Duyên phủ lên một tầng sương đen: “Cháu muốn chú đi trùm bao tải đánh cho Trương Sâm Trạch một trận tơi bời, chú chịu hay không chịu?”",

    # 78: “絕對不行。”陳斂皺緊了眉，毫不猶豫地拒絕了他。
    "“Tuyệt đối không được.” Trần Liễm nhíu chặt mày, không chút do dự từ chối cậu.",

    # 79: “你的報復心也太強了...”
    "“Lòng trả thù của cháu quá mạnh mẽ rồi. Chú biết cháu trước giờ luôn ngụy trang trước mặt cái tên Lâu Hỉ Dương kia. Cháu đừng có không thích nghe, với tính cách của cậu ta thì tuyệt đối sẽ không bao giờ thích một con người thật sự của cháu đâu. Đến lúc đó chắc chắn cậu ta sẽ bôi dầu vào chân chạy mất dạng, nói không chừng còn quay đầu mắng cháu một câu biến thái, bảo cháu cút xéo……”",

    # 80: “你知道什麽！——”易緣突然拔高音量叫了一聲...
    "“Chú thì biết cái gì chứ!——” Dịch Duyên đột ngột cao giọng hét lên một tiếng, đôi mắt trở nên đỏ ngầu, “Anh ấy sẽ thích cháu, anh ấy chỉ có thể thích một mình cháu thôi!”",

    # 81: “他如果要離開我，我就只有把他鎖在我身邊了...”
    "“Nếu như anh ấy muốn rời xa cháu, cháu chỉ còn cách xích anh ấy lại bên cạnh mình. Không sao cả, cháu sẽ từ từ đợi anh ấy thích cháu……”",

    # 82: 易緣的聲音越來越弱，後面變成了自言自語的呢喃。
    "Giọng nói của Dịch Duyên càng lúc càng yếu ớt đi, về sau biến thành những lời nỉ non tự lẩm bẩm một mình.",

    # 83: 沒想到能把易緣刺激成這樣...
    "Không ngờ lại kích động Dịch Duyên tới mức này, Trần Liễm bị dọa cho giật mình một cái, cũng chẳng dám nói thêm câu nào nữa. Ông ta sắc mặt khó coi gọi một nhóm người tới làm công tác xoa dịu tâm lý cho cậu, đợi cậu bình ổn lại mới gọi tổ trưởng tới hỏi han cho rõ ràng.",

    # 84: “電流或許會造成他情緒波動走向極端。”...
    "“Dòng điện có lẽ gây ra dao động cảm xúc khiến cậu ấy đi tới cực đoan.” Vị tổ trưởng nghiêm túc phân tích các hạng mục số liệu, đẩy biểu đồ tới trước mặt Trần Liễm, “Số liệu biểu thị trong khoảng thời gian này cảm xúc của cậu ấy là ổn định nhất, có thể đẩy nhanh tốc độ lấy con chip ra.”",

    # 85: 陳斂看著上面的時間，恰好是易緣待在婁禧陽病房裡的時間段。
    "Trần Liễm nhìn mốc thời gian trên đó, vừa vặn chính là khoảng thời gian Dịch Duyên ở trong phòng bệnh của Lâu Hỉ Dương.",

    # 86: 他長吐了口氣，愁緒上湧。
    "Ông ta thở dài một hơi thật sâu, nỗi ưu sầu dâng trào.",

    # 87: 他只希望在這段時間裡婁禧陽不要出什麽岔子...
    "Ông ta chỉ hy vọng trong khoảng thời gian này Lâu Hỉ Dương đừng xảy ra chuyện gì trắc trở, bằng không Dịch Duyên có thể sẽ phát điên thật sự, đến lúc đó ông ta chết rồi biết ăn nói thế nào với mẹ cậu đây?",

    # 88: 愁啊。他搖了搖頭。
    "Sầu não quá đi thôi. Ông ta lắc lắc đầu.",

    # 89: 謝謝小天使的營養液～
    "Cảm ơn dung dịch dinh dưỡng của thiên sứ nhỏ ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_017 translation written: {len(paragraphs)} paragraphs.")
