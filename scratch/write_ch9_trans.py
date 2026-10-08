# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_009"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 9: Giống cún con
---""",

    # 1: separator
    "================",

    # 2: 陳斂的臉浮現在半空...
    "Gương mặt của Trần Liễm hiện lên giữa không trung, biểu cảm nghiêm nghị. Phía sau ông ta là một dãy hành lang giống như của viện điều trị, hiện lên một mảng màu xám trắng: “Dịch Duyên, chú cho cháu thêm ba ngày nữa, bất luận thế nào cháu cũng bắt buộc phải đi cùng chú. Nếu còn không bắt đầu hành động của chúng ta thì tất cả sẽ không còn kịp nữa đâu.”",

    # 3: “我知道你舍不得那個姓婁的...”
    "“Chú biết cháu không nỡ rời xa cái tên họ Lâu kia, nhưng cháu phải cân nhắc cho rõ ràng, đi cùng chúng ta thì cậu ta mới có cơ hội sống sót...”",

    # 4: “好，我答應你。”
    "“Được, cháu đồng ý với chú.”",

    # 5: 那邊陳斂嘴唇動著還在勸著什麽...
    "Đầu bên kia môi Trần Liễm vẫn mấp máy như đang khuyên nhủ điều gì đó, dường như còn chưa kịp phản ứng lại.",

    # 6: 易緣抬起眼皮...
    "Dịch Duyên nâng mí mắt, nhìn thẳng vào người đàn ông trong khung hình ảo, lặp lại một lần nữa: “Cháu có thể đi cùng chú, nhưng cháu có một điều kiện, giúp cháu phá vỡ hệ thống phòng vệ của viện nghiên cứu Tây Lăng Sơn.”",

    # 7: 陳斂的目光凝滯了一會兒...
    "Ánh mắt Trần Liễm ngưng trệ một thoáng, sau đó ông ta nhíu mày, ngữ điệu cao lên, mang theo vài phần khó hiểu và không thể tin nổi: “Dịch Duyên, cháu có biết cháu đang nói cái gì không?”",

    # 8: “我知道，我還知道你一定可以做到的...”
    "“Cháu biết, cháu còn biết chú nhất định có thể làm được. Chú Trần Liễm, với tư cách là Trưởng quan Đoàn Tình báo Liên bang, chuyện này đối với chú dễ như trở bàn tay mà đúng không?”",

    # 9: 對面的陳斂聽到這話表情一下子就僵硬了...
    "Trần Liễm ở đối diện nghe thấy lời này biểu cảm tức khắc cứng đờ. Ông ta không ngờ Dịch Duyên lại vạch trần thân phận của mình nhanh đến vậy.",

    # 10: 易緣依舊是那一副無所謂的模樣...
    "Dịch Duyên vẫn là dáng vẻ chẳng hề để tâm kia, vô cùng kiên nhẫn chờ đợi câu trả lời của ông ta.",

    # 11: “呵，”陳斂輕笑了一聲...
    "“Hừ,” Trần Liễm khẽ cười một tiếng, đổi lại thần sắc thường ngày, “Được, chú đồng ý với cháu. Dù sao thì cũng đều phải chết cả, thêm một tội danh này cũng chẳng là gì. Cháu bao giờ thì đi? Chú phái người tới đón cháu.”",

    # 12: “後天早上陽哥離開後吧，謝了，再見。”
    "“Sáng ngày mốt sau khi Dương ca rời đi nhé, cảm ơn, tạm biệt.” Nói xong hai chữ cuối cùng, Dịch Duyên chẳng chút lưu luyến dập tắt cuộc gọi. Cậu nhìn mình trong gương hồi lâu mới mở cửa, rón rén từng bước trở lại giường.",

    # 13: 每次和易緣睡一張床的時候...
    "Mỗi lần ngủ chung một giường với Dịch Duyên, Lâu Hỉ Dương đều ngủ rất say, cộng thêm việc bươn chải mệt mỏi mấy ngày nay, anh hoàn toàn không hề nhận ra sự rời đi của Dịch Duyên.",

    # 14: 易緣用手撐著床...
    "Dịch Duyên dùng tay chống giường, cúi người ngắm nhìn gương mặt Lâu Hỉ Dương hết lần này đến lần khác.",

    # 15: 婁禧陽的眉眼深邃...
    "Mày mắt Lâu Hỉ Dương sâu thẳm, đường nét góc cạnh rõ ràng, bình thường khi không có biểu cảm trông vừa lạnh lùng vừa vô tình, nhưng một khi đã cười, khóe môi anh sẽ cong lên một độ cong vô cùng đẹp mắt, lộ ra hàm răng trắng muốt, rực rỡ chói lòa tựa như vầng thái dương lúc băng tuyết tan biến, khiến toàn thân Dịch Duyên dâng trào hơi nóng.",

    # 16: 他永遠記得第一次在昏暗的樓道裡見到婁禧陽時...
    "Cậu vĩnh viễn nhớ rõ lần đầu tiên nhìn thấy Lâu Hỉ Dương ở góc cầu thang u tối, nụ cười Lâu Hỉ Dương nở với cậu khi ấy chính là niềm vui sướng chưa từng có trong đời cậu.",

    # 17: 他伸出手，指尖隔著毫米的距離...
    "Cậu vươn tay ra, đầu ngón tay cách một khoảng cách chỉ vài milimet lướt dọc theo sống mũi cao thẳng của Lâu Hỉ Dương, cuối cùng dừng lại trên đôi môi mỏng kia.",

    # 18: 指尖停頓了許久，終究沒有落下去。
    "Đầu ngón tay khựng lại thật lâu, rốt cuộc vẫn không chạm xuống.",

    # 19: 易緣收回手，躺回了被窩裡。
    "Dịch Duyên thu tay về, nằm trở lại vào trong chăn.",

    # 20: *
    "*",

    # 21: 得利於婁禧陽的機甲圖紙以及訓練方案...
    "Nhờ có bản vẽ cơ giáp cùng phương án huấn luyện của Lâu Hỉ Dương, toàn bộ trên dưới bang Lloyd đều đâu vào đấy ngăn nắp trật tự. Lão già tóc đỏ giám sát việc cải tạo cơ giáp, Bội Lương thao luyện tất cả các binh đoàn bao gồm cả cơ giáp binh, việc cần Lâu Hỉ Dương làm chẳng còn lại bao nhiêu.",

    # 22: 相比前幾天一下子輕松了不少...
    "So với mấy ngày trước thì bỗng chốc nhẹ nhõm hơn hẳn. Lâu Hỉ Dương áng chừng tiến độ, kiếp trước anh phải mất hai tháng cho việc giải cứu Lâu An Minh, mà lần này chỉ dùng nửa tháng. Cứ theo đà này, anh ít nhất có thể kết thúc trận mạt thế này sớm hơn ba tháng, đưa hành tinh M trở lại quỹ đạo bình thường.",

    # 23: 他今天只在艾斯特區待了兩三個小時就離開了...
    "Hôm nay anh chỉ ở khu vực Est hai ba tiếng đồng hồ rồi rời đi. Lúc về trời vẫn còn là buổi chiều, nghĩ đến số bánh quy nén ở nhà chẳng còn lại mấy gói, anh liền bẻ lái hướng về thành Long Uyên.",

    # 24: 距離他上一次來已經過去了一周的時間...
    "Cách lần trước anh đến đây đã trôi qua tròn một tuần. Một tuần lễ, đối với những người đang dần cạn kiệt lương thực, không mua nổi giấy chứng nhận cư trú trên hành tinh M mà nói, là khoảng thời gian dài đằng đẵng gần như tuyệt vọng.",

    # 25: 在售貨區外面，坐滿了一圈又一圈的人...
    "Bên ngoài khu bán hàng, từng vòng từng vòng người ngồi chật kín. Bọn họ đa phần quần áo rách rưới, má hóp sâu hoắm, nhìn chằm chằm vào số lương thực trên tay mỗi một người bước ra từ bên trong, trong ánh mắt phát ra vẻ điên cuồng khiến người ta sợ hãi rùng mình.",

    # 26: 婁禧陽被這樣的情景釘在了原地...
    "Lâu Hỉ Dương bị cảnh tượng này đóng đinh tại chỗ. Tương tự, đám người kia khi nghe thấy tiếng gầm rú đặc trưng của mô tô bay đặc cấp cũng đồng loạt nhìn sang.",

    # 27: 一輛特級飛摩可以賣到一千萬以上的星幣...
    "Một chiếc mô tô bay đặc cấp có thể bán được hơn mười triệu tinh tệ, nhưng gần như không thể cưỡng chế đổi chủ xe. Nghĩ đến đây, đám người kia lại ảm đạm thu hồi ánh mắt.",

    # 28: 婁禧陽鎖好車，將衛衣帽子帶上後走進了售貨區。
    "Lâu Hỉ Dương khóa xe cẩn thận, trùm mũ áo hoodie lên rồi bước vào khu bán hàng.",

    # 29: “那個人看上去很有錢，我們……”
    "“Người kia trông có vẻ rất nhiều tiền, chúng ta……” Một bà cụ lặng lẽ thăm dò người bên cạnh.",

    # 30: “別想了，他那樣子看上去就不好惹...”
    "“Đừng nghĩ nữa, bộ dạng cậu ta trông đã thấy chẳng dễ chọc vào đâu, coi chừng bị cậu ta đánh cho mẹ nhận không ra đấy, bỏ đi.” Một gã đàn ông giọng thô kệch cắt ngang lời bà cụ.",

    # 31: 婁禧陽聽著身後響起的議論...
    "Lâu Hỉ Dương lắng nghe những lời bàn tán vang lên sau lưng, bước chân khựng lại đôi chút rồi dần dần bước nhanh hơn.",

    # 32: “奶奶，我們回去吧，不會有人白送壓縮餅乾給我們的。”
    "“Bà ơi, chúng ta về đi thôi, không có ai cho không bánh quy nén cho chúng ta đâu.” Bé gái chui ra từ trong lòng bà cụ, thấy bà cụ vẫn kiên quyết không đi liền thở dài, cúi đầu xoa xoa cái bụng rỗng tuếch, đầu óc mê man bắt đầu mất tập trung.",

    # 33: 模糊間她好像聽見身邊的幾個伯伯激動地道著謝...
    "Trong cơn mơ màng, cô bé dường như nghe thấy mấy người bác bên cạnh kích động nói lời cảm ơn, ngay sau đó số người cảm ơn càng lúc càng nhiều. Còn chưa đợi cô bé hoàn hồn lại thì đã nghe thấy một giọng nói trầm thấp đầy từ tính vang lên ngay trên đỉnh đầu——",

    # 34: “抱歉，只能給你們兩包。”
    "“Xin lỗi, tôi chỉ có thể cho hai người hai gói thôi.”",

    # 35: 兩包壓縮餅乾突然出現在她眼前...
    "Hai gói bánh quy nén đột nhiên xuất hiện trước mắt cô bé. Cô bé ngẩng đầu lên, nhìn thấy một chiếc cằm với đường nét góc cạnh rõ ràng.",

    # 36: “謝謝！謝謝，謝謝你！你真是個好心的小夥子！”
    "“Cảm ơn! Cảm ơn, cảm ơn cậu! Cậu quả là một chàng trai tốt bụng!” Bà cụ kích động nhìn Lâu Hỉ Dương, miệng không ngừng nói lời cảm ơn.",

    # 37: 婁禧陽把壓縮餅乾放到小女孩兒的手上...
    "Lâu Hỉ Dương đặt bánh quy nén vào tay bé gái, nói một câu không cần khách sáo rồi quay người định rời đi.",

    # 38: “等等——小夥子，我這裡有些不值錢的小玩意兒可以送給你。”
    "“Chờ đã—— Chàng trai trẻ, bà ở đây có mấy món đồ nhỏ không đáng tiền có thể tặng cho cậu.” Bà cụ hốt hoảng muốn đứng dậy, nhưng vì cơ thể suy yếu suýt chút nữa đứng không vững.",

    # 39: 婁禧陽見狀扶了她一把...
    "Lâu Hỉ Dương thấy vậy liền đỡ bà một tay, ngay sau đó liền thấy bà cụ lấy từ dưới người ra một túi vải, bên trong đựng đầy mũ và găng tay đan bằng len.",

    # 40: 老婦將裡面的東西掏出來...
    "Bà cụ móc đồ bên trong ra, từng món một đưa cho Lâu Hỉ Dương xem: “Đây là đồ bà đan theo cách đan len của Trái Đất cổ được ghi chép trong sách, bây giờ chẳng đáng tiền nữa rồi, cậu cầm mấy cái về đi.”",

    # 41: 婁禧陽的目光落在了那頂白色毛茸茸的狗狗帽子上...
    "Ánh mắt Lâu Hỉ Dương rơi vào chiếc mũ hình chú cún màu trắng lông xù xù. Không hiểu vì sao, anh đột nhiên nhớ tới đôi mắt cười sáng lấp lánh của Dịch Duyên.",

    # 42: 易緣皮膚很白，頭髮又乖順，帶上去應該會很可愛。
    "Da Dịch Duyên rất trắng, tóc tai lại ngoan ngoãn mềm mượt, đội vào chắc hẳn sẽ rất đáng yêu.",

    # 43: 見婁禧陽有意...
    "Thấy Lâu Hỉ Dương có ý muốn lấy, bé gái nhanh tay lẹ mắt nhét chiếc mũ kia vào tay anh, còn móc thêm cả đôi găng tay hình vuốt cún đồng bộ, một mạch nhét hết vào lòng anh.",

    # 44: 就這樣，婁禧陽帶著一屁股債和狗狗套裝回到了家裡。
    "Cứ như vậy, Lâu Hỉ Dương mang theo một đống nợ cùng với bộ đồ cún con trở về nhà.",

    # 45: 他當然是沒有錢當大善人的...
    "Anh đương nhiên là không có tiền để làm đại thiện nhân rồi, vừa nãy anh phải tạm thời vay Trương Sâm Trạch một ít tinh tệ, sau này còn phải trả đủ cả vốn lẫn lãi cho người ta.",

    # 46: 在他開門的時候...
    "Lúc anh mở cửa, trong phòng vang lên một tràng âm thanh hốt hoảng vội vã, ngay sau đó liền nhìn thấy Dịch Duyên mừng rỡ như điên lao bổ về phía anh.",

    # 47: “陽哥，你今天怎麽這麽早就回來啦！”
    "“Dương ca, hôm nay sao anh về sớm thế ạ!” Dịch Duyên ôm chầm lấy anh, còn cọ cọ vào hõm cổ anh.",

    # 48: “嗯，這幾天都比較空閑。”
    "“Ừ, mấy ngày này tương đối rảnh rỗi.” Lâu Hỉ Dương xoa xoa đỉnh đầu mềm mại của cậu hai cái, nghiêng người bước vào trong nhà.",

    # 49: 易緣盯著他手裡的袋子，發現露出了一點毛茸茸的東西。
    "Dịch Duyên nhìn chằm chằm vào chiếc túi trên tay anh, phát hiện lộ ra một góc đồ lông xù xù.",

    # 50: “陽哥，袋子裡裝的是什麽？”
    "“Dương ca, trong túi đựng cái gì thế ạ?” Cậu kinh ngạc nghé mắt nhìn vào trong túi, lại phát hiện Lâu Hỉ Dương khẽ giấu ra sau lưng một chút.",

    # 51: 婁禧陽被自己下意識的舉動別扭住了...
    "Lâu Hỉ Dương bị hành động theo bản năng của chính mình làm cho ngượng ngùng, có cái gì phải trốn tránh chứ? Chẳng qua chỉ là một bộ đồ cún con lông trắng thôi mà? Chẳng qua chỉ là cảm thấy Dịch Duyên đội vào sẽ rất... có chút đáng yêu thôi mà? Anh đang chột dạ cái gì chứ?",

    # 52: 想到這裡，婁禧陽皺了下眉...
    "Nghĩ đến đây, Lâu Hỉ Dương nhíu mày một cái, ngược lại hào phóng đưa chiếc mũ cùng găng tay bên trong ra: “Người khác tặng, anh thấy rất hợp với em.”",

    # 53: 易緣從來沒有被婁禧陽送過除了資料以及機甲模型以外的禮物...
    "Dịch Duyên chưa bao giờ được Lâu Hỉ Dương tặng món quà nào khác ngoài tài liệu và mô hình cơ giáp. Cậu có chút ngây người, hai mắt ngơ ngác trừng tròn xoe, lâng lâng nhận lấy từ tay anh.",

    # 54: 感覺到氣氛有點古怪...
    "Cảm thấy bầu không khí có chút kỳ quặc, Lâu Hỉ Dương khẽ ho một tiếng, không cảm xúc mở thiết bị đầu cuối tiếp tục bàn bạc chuyện tiền lãi với Trương Sâm Trạch.",

    # 55: 原本他以為事情到這就已經結束了...
    "Vốn dĩ anh tưởng chuyện đến đây là kết thúc rồi, nhưng anh vạn vạn không ngờ tới lúc tắm xong quay về phòng ngủ, lại nhìn thấy Dịch Duyên đang đội đôi tai cún lông xù xù nằm cuộn trên giường xem thứ gì đó.",

    # 56: 那一下讓婁禧陽的腦子有點發鈍...
    "Khoảnh khắc đó khiến đầu óc Lâu Hỉ Dương có chút đình trệ. Anh ngượng ngùng dời tầm mắt đi, giả vờ trấn tĩnh bước về phía bên giường của mình.",

    # 57: 他剛坐下，床微微陷下去了一點...
    "Anh vừa ngồi xuống, giường hơi lún xuống một chút, liền bị Dịch Duyên đột ngột quay đầu lại làm cho giật mình một cái: “Dương ca, yêu đương là cảm giác thế nào ạ?”",

    # 58: 婁禧陽：？
    "Lâu Hỉ Dương: ?",

    # 59: “陽哥應該和每任女朋友都接過吻吧？”
    "“Dương ca chắc là từng hôn môi với mỗi một cô bạn gái rồi đúng không?”",

    # 60: 婁禧陽：…
    "Lâu Hỉ Dương: ...",

    # 61: 被易緣問得沉默了好半天...
    "Bị Dịch Duyên hỏi đến mức trầm mặc hồi lâu, Lâu Hỉ Dương mới khẽ ho một tiếng xua tan lúng túng, ngước mắt nhìn về phía Dịch Duyên, phát hiện ra cậu đang xem một cuốn tiểu thuyết tình cảm không biết kiếm ở đâu ra.",

    # 62: M星最新的小說功能...
    "Chức năng tiểu thuyết mới nhất của hành tinh M, mỗi khi độc giả lật một trang, sẽ tự động chiếu lên sách đoạn hình ảnh tương ứng. Mà lúc Dịch Duyên hỏi anh, màn hình đang vừa vặn phát đến phân cảnh nam nữ chính hôn nhau.",

    # 63: “嗯，就是像他們這樣...”
    "“Ừ, chính là giống như bọn họ thế này, sẽ hôn môi, nhịp tim sẽ đập nhanh hơn, trong đầu sẽ thường xuyên nhớ tới người đó...” Lâu Hỉ Dương bình tĩnh phân tích.",

    # 64: 當他看見易緣的眼神隨著他的話愈來愈炙熱時，他緩緩閉上了嘴。
    "Khi anh nhìn thấy ánh mắt Dịch Duyên theo từng lời nói của mình mà ngày càng trở nên nóng rực, anh liền chậm rãi ngậm miệng lại.",

    # 65: 他突然想起來易緣對他的感情不一般。
    "Anh đột nhiên nhớ ra tình cảm Dịch Duyên dành cho anh vốn không hề bình thường.",

    # 66: 這樣一想，奇怪的感覺瞬間密密麻麻地遍布了全身。
    "Vừa nghĩ như vậy, cảm giác kỳ lạ tức khắc râm ran lan tỏa dày đặc khắp toàn thân.",

    # 67: “陽哥，你看我這樣像不像一條小狗。”
    "“Dương ca, anh nhìn em thế này có giống một chú cún con không.” Dịch Duyên đột nhiên nhích về phía anh, ngồi sát rạt bên cạnh anh, giơ cổ tay lên hướng về phía anh, trên tay vừa vặn đang mang đôi găng tay vuốt cún lông xù kia.",

    # 68: “汪！”易緣湊近他的耳朵，壓下嗓子叫了一聲。
    "“Gâu!” Dịch Duyên ghé sát tai anh, đè thấp giọng sủa một tiếng.",

    # 69: 隨即一張炙熱的手掌就捂住了他的嘴...
    "Ngay sau đó một bàn tay nóng bỏng liền bịt chặt lấy miệng cậu. Chân mày Lâu Hỉ Dương nhăn tít lại, trông có vẻ rất dữ dằn, nhưng sau vành tai hơi ửng đỏ lại bán đứng anh.",

    # 70: “別亂叫，去給我睡覺。”婁禧陽低聲訓斥。
    "“Đừng có kêu bậy bạ, đi ngủ cho anh.” Lâu Hỉ Dương trầm giọng quở trách.",

    # 71: 易緣嘴角微微上揚...
    "Khóe môi Dịch Duyên khẽ nhếch lên. Trong lúc Lâu Hỉ Dương còn chưa kịp phản ứng, phong cách bỗng chốc quay ngoắt, lại quay trở về chủ đề ban nãy.",

    # 72: “我好想在末日前談一次戀愛，可是我找不到女朋友...”
    "“Em rất muốn trước mạt thế được yêu đương một lần, nhưng mà em không tìm được bạn gái,” Dịch Duyên ủ rũ rủ mi mắt xuống, đặt chiếc vuốt cún lên lòng bàn tay Lâu Hỉ Dương, “Dương ca, lần trước anh chưa trả lời câu hỏi của em, anh giả vờ làm bạn gái em trong mấy tháng cuối cùng này được không?”",

    # 73: 婁禧陽的大半注意力都被手上毛毛的觸感吸引去了...
    "Phần lớn sự chú ý của Lâu Hỉ Dương đều bị xúc cảm lông xù trên tay thu hút mất rồi, yết hầu lặng lẽ chuyển động, theo bản năng “ừm” một tiếng.",

    # 74: 在易緣撲過來的時候他才意識到剛才他回應的是什麽問題...
    "Đến lúc Dịch Duyên nhào tới anh mới ý thức được câu hỏi vừa rồi mình đồng ý là cái gì, nhưng tất cả đã không còn kịp nữa. Tầm nhìn của anh một mảng hỗn loạn, ngay sau đó trên môi liền in lên một đôi môi mềm mại ấm áp.",

    # 75: 這次和上一回完全不一樣...
    "Lần này hoàn toàn không giống lần trước, động tác của Dịch Duyên vừa nhẹ nhàng vừa cẩn thận từng li từng tí, cái liếm mút không đúng phương pháp tựa như động vật nhỏ lại khiến đầu óc Lâu Hỉ Dương trống rỗng.",

    # 76: 易緣的手搭在他的肩上...
    "Bàn tay Dịch Duyên đặt trên vai anh, xúc cảm từ chiếc găng tay truyền tới từ sau gáy, thiêu đốt đi lý trí của anh.",

    # 77: 他從來沒有過這樣的感覺...
    "Anh chưa bao giờ có cảm giác như thế này, giống như có một mầm non nào đó đang thò đầu nhú lên trong tim.",

    # 78: 終究是沒忍住心裡的癢意，他扣住易緣的後腦杓，回吻了過去。
    "Rốt cuộc không kìm nén được cảm giác ngứa ngáy trong lòng, anh giữ chặt gáy Dịch Duyên, hôn đáp lại.",

    # 79: 【叮咚，目前還債進度30%！請宿主再接再厲哦～】
    "【Đinh đong, tiến độ trả nợ hiện tại 30%! Ký chủ hãy tiếp tục cố gắng nhé ~】",

    # 80: 系統久違的提示音在婁禧陽耳邊響起，但他卻一個字也沒聽進去。
    "Tiếng thông báo đã lâu không xuất hiện của hệ thống vang lên bên tai Lâu Hỉ Dương, nhưng anh lại chẳng lọt tai lấy một chữ nào.",

    # 81: 婁禧陽：原來我還是個毛絨控？？
    "Lâu Hỉ Dương: Hóa ra mình còn là người cuồng lông xù xù nữa sao??",

    # 82: 易緣：早說嘛，我天天給你穿，穿一整個動物園都沒問題！
    "Dịch Duyên: Nói sớm đi chứ, ngày nào em cũng mặc cho anh xem, mặc cả một sở thú cũng không thành vấn đề!"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_009 translation written: {len(paragraphs)} paragraphs.")
