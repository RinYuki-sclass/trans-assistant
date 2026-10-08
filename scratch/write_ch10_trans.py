# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_010"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 10: Thế sao anh lại hôn em!
---""",

    # 1: separator
    "====================",

    # 2: 事情結束後婁禧陽才意識到自己做了什麽。
    "Sau khi mọi chuyện kết thúc, Lâu Hỉ Dương mới ý thức được bản thân vừa làm cái gì.",

    # 3: 他直起身，雙目逐漸清明。
    "Anh thẳng người dậy, hai mắt dần dần lấy lại vẻ tỉnh táo.",

    # 4: 易緣還沒有從其中脫離出來，手指還拽著婁禧陽的睡衣。
    "Dịch Duyên vẫn còn chưa thoát ra khỏi dư âm nồng nàn, đầu ngón tay vẫn nắm chặt lấy vạt áo ngủ của Lâu Hỉ Dương.",

    # 5: 婁禧陽沉默了一會兒...
    "Lâu Hỉ Dương trầm mặc một lát mới ngước mắt nhìn về phía Dịch Duyên, phát hiện ánh mắt cậu hoang mang tan rã, đuôi mắt ửng hồng, bờ môi ướt át vẫn duy trì trạng thái hơi hé mở, khẽ khàng thở dốc.",

    # 6: “陽，陽哥？”他的眼中浮著後知後覺的喜悅。
    "“Dương, Dương ca?” Trong mắt cậu dâng lên niềm vui sướng chậm nửa nhịp.",

    # 7: 婁禧陽沒有回應，他緩緩抿直了唇，起身去了屋外。
    "Lâu Hỉ Dương không đáp lại, anh chậm rãi mím chặt môi, đứng dậy bước ra ngoài phòng.",

    # 8: 易緣倒是紅著眼角想跟上來，被他毫不留情地關在了房內。
    "Dịch Duyên đỏ hoe khóe mắt muốn theo ra ngoài, lại bị anh không chút lưu tình nhốt lại trong phòng.",

    # 9: 婁禧陽靠在牆上，頭疼地閉上了眼睛。
    "Lâu Hỉ Dương dựa vào vách tường, đau đầu nhắm nghiền hai mắt lại.",

    # 10: 他覺得自己實在是昏了頭了。
    "Anh cảm thấy bản thân mình thực sự là hồ đồ mê muội rồi.",

    # 11: 他為什麽會回吻過去？從今以後他該怎麽面對易緣？
    "Tại sao anh lại hôn đáp lại cậu chứ? Từ nay về sau anh phải đối mặt với Dịch Duyên thế nào đây?",

    # 12: 這已經超出他的計劃范圍內了。
    "Chuyện này đã hoàn toàn vượt khỏi phạm vi kế hoạch của anh rồi.",

    # 13: 從發現易緣喜歡他開始...
    "Kể từ lúc phát hiện Dịch Duyên thích mình, anh đã xác định bản thân sẽ không đưa ra bất kỳ phản hồi nào cho Dịch Duyên. Anh trước giờ luôn xem Dịch Duyên như em trai ruột thịt, tuy rằng không có quan hệ máu mủ, nhưng cộng cả kiếp trước anh gần như đã nuôi nấng Dịch Duyên hơn hai mươi năm trời. Dịch Duyên là người bầu bạn bên cạnh anh lâu nhất, cho dù về sau có phản bội anh, anh cũng chưa từng nghĩ sẽ làm gì cậu.",

    # 14: 原本的設想中...
    "Trong dự tính ban đầu, anh sẽ thay đổi vận mệnh của Dịch Duyên, để cậu sống một cuộc đời hạnh phúc không lo không nghĩ. Còn tình cảm không nên có mà Dịch Duyên dành cho anh rồi cũng sẽ tiêu tan theo thời gian, có lẽ sau này cậu sẽ yêu một người thích hợp, đến lúc đó anh sẽ với tư cách là người nhà của Dịch Duyên mà gửi lời chúc phúc cho cậu.",

    # 15: 還債，就算沒有這還債系統，他都不希望易緣像上輩子一樣。
    "Trả nợ, cho dù không có cái hệ thống trả nợ này, anh cũng không mong Dịch Duyên lại giống như kiếp trước.",

    # 16: 這樣的認知早就刻在了他的心裡，不可能有所改變。
    "Nhận thức như vậy đã sớm khắc sâu trong tim anh, không thể nào thay đổi được.",

    # 17: 既然不可能喜歡易緣，那他剛才的行為是做什麽？誰會和自己的弟弟接吻？易緣不懂事拿想拿談戀愛忽悠他，難道他看不出來嗎？
    "Đã không thể nào thích Dịch Duyên, vậy thì hành động vừa rồi của anh là có ý gì? Ai lại đi hôn môi với em trai của mình chứ? Dịch Duyên không hiểu chuyện lấy cớ muốn yêu đương để lừa gạt anh, chẳng lẽ anh lại không nhìn ra sao?",

    # 18: 嘖，他到底在做什麽？
    "Chậc, rốt cuộc là anh đang làm cái gì vậy chứ?",

    # 19: 婁禧陽皺緊了雙眉，此刻他很想抽煙，只可惜早就已經沒有煙了。
    "Lâu Hỉ Dương nhăn tít hai hàng lông mày. Giờ khắc này anh rất muốn hút một điếu thuốc, chỉ tiếc là đã sớm không còn thuốc lá nữa rồi.",

    # 20: 一牆之隔的臥室內，易緣仍不停地敲著門，一聲一聲地叫著他的名字。
    "Cách một bức tường trong phòng ngủ, Dịch Duyên vẫn không ngừng gõ cửa, từng tiếng từng tiếng gọi tên anh.",

    # 21: “陽哥，你是不是不適應？沒關系，我們就是假裝成戀人接個吻而已，你別放在心上，我不會把它當真的……”
    "“Dương ca, có phải anh không quen không? Không sao đâu mà, chúng ta chỉ giả vờ làm người yêu hôn nhau một cái thôi, anh đừng để trong lòng, em sẽ không cho là thật đâu……”",

    # 22: 易緣垂著腦袋一下一下往門上撓...
    "Dịch Duyên cúi gằm đầu từng chút từng chút cào cào lên cánh cửa. Cậu vẫn còn chìm đắm trong niềm vui sướng khi Lâu Hỉ Dương chủ động hôn mình, đến mức cửa bị Lâu Hỉ Dương mở ra từ bên ngoài lúc nào cũng không phát hiện.",

    # 23: 不知道過了多久，感到手落了空...
    "Không biết qua bao lâu, cảm thấy tay mình hụt vào khoảng không, cậu mới ngẩng đầu lên, đối diện ngay với gương mặt có thể nói là nghiêm túc đến cực điểm của Lâu Hỉ Dương.",

    # 24: “易緣。”婁禧陽一本正經地看著他，“對不起，剛才是我腦子不清醒。”
    "“Dịch Duyên.” Lâu Hỉ Dương nghiêm trang đứng đắn nhìn cậu, “Xin lỗi, vừa rồi là đầu óc anh không tỉnh táo.”",

    # 25: “啊？”易緣的嘴角還掛著笑意...
    "“Dạ?” Khóe môi Dịch Duyên vẫn còn vương nét cười, tia sáng trong mắt còn chưa kịp tan biến thì đã nghe thấy Lâu Hỉ Dương dứt khoát tuyệt tình nói: “Từ nay về sau anh tuyệt đối sẽ không làm bất kỳ hành vi nào vượt quá giới hạn nữa. Em là em trai anh, anh không nên làm như vậy.”",

    # 26: “陽哥你是不是誤會了？我只是想…”易緣蹩腳地回應道。
    "“Dương ca, có phải anh hiểu lầm rồi không? Em chỉ là muốn...” Dịch Duyên vụng về đáp lại.",

    # 27: “如果你想嘗試戀愛，我可以幫你找一個對的人...”
    "“Nếu như em muốn thử cảm giác yêu đương, anh có thể giúp em tìm một người thích hợp, bất kể là con gái... hay là con trai. Anh là anh trai em, cha em phó thác em cho anh, anh không thể cùng em làm chuyện này.”",

    # 28: 婁禧陽一邊說著，一邊目睹了易緣表情僵硬的全過程。
    "Lâu Hỉ Dương vừa nói vừa tận mắt chứng kiến toàn bộ quá trình nét mặt Dịch Duyên dần trở nên cứng đờ.",

    # 29: 由於之前的舉動，易緣頭頂上的小狗耳朵凌亂地搭在他的額前，現在看上去可憐至極。
    "Do những động tác trước đó, đôi tai cún con trên đỉnh đầu Dịch Duyên lộn xộn rũ xuống trước trán cậu, giờ phút này trông đáng thương tới cực điểm.",

    # 30: 空氣突然安靜了，易緣緩緩地垂下了眼簾，盯著地上婁禧陽的影子不說話。
    "Không khí đột nhiên tĩnh lặng, Dịch Duyên chậm rãi rủ mi mắt xuống, nhìn chằm chằm bóng hình Lâu Hỉ Dương trên mặt đất không nói một lời.",

    # 31: 婁禧陽看著他鴉羽般的睫毛，心想他剛才的那番話不算重，那為什麽易緣看上去那麽難過？
    "Lâu Hỉ Dương nhìn hàng mi đen như lông quạ của cậu, thầm nghĩ những lời ban nãy của mình đâu có quá nặng nề, vậy tại sao Dịch Duyên trông lại đau lòng đến thế?",

    # 32: 或許是忘了偽裝，易緣的眼裡逐漸蓄滿了淚意，再抬眼時，淚珠已然從眼眶內湧了出來。
    "Có lẽ là quên cả ngụy trang, trong mắt Dịch Duyên dần đong đầy nước mắt. Đến khi ngước mắt lên lần nữa, những giọt lệ đã tuôn trào ra khỏi hốc mắt.",

    # 33: “那你幹嘛親我啊？！——”他朝婁禧陽吼了一聲，一把推開婁禧陽，把自己埋進了床裡。
    "“Thế thì anh mắc mớ gì phải hôn em chứ?!——” Cậu gào lên một tiếng với Lâu Hỉ Dương, đẩy mạnh Lâu Hỉ Dương ra rồi vùi cả người vào trong giường.",

    # 34: “我今天不要和你一起睡了！”易緣的聲音從被子裡悶了出來。
    "“Hôm nay em không thèm ngủ cùng anh nữa đâu!” Tiếng nói của Dịch Duyên nghẹn ngào nghẹt mũi truyền ra từ trong chăn.",

    # 35: 婁禧陽站在門口，一時間有點猝不及防，他還沒有被易緣“趕”過。
    "Lâu Hỉ Dương đứng ở cửa, trong thoáng chốc có chút trở tay không kịp, anh trước giờ chưa từng bị Dịch Duyên “đuổi” bao giờ.",

    # 36: 可他剛準備轉身，又聽見易緣凶巴巴地朝他吼：“今天算了，明天你再出去！”
    "Nhưng anh vừa mới chuẩn bị quay người thì lại nghe thấy Dịch Duyên hung dữ gào lên với anh: “Hôm nay bỏ qua, ngày mai anh mới được cút ra ngoài!”",

    # 37: *
    "*",

    # 38: 婁禧陽一整個晚上都是睜眼躺過去的...
    "Lâu Hỉ Dương mở trừng mắt nằm suốt cả một đêm. Đầu óc anh một mảng hỗn loạn, thế nhưng nghiền ngẫm cả đêm cũng không nghĩ thông được cảm giác kỳ lạ trong lòng mình rốt cuộc bắt nguồn từ đâu.",

    # 39: 為了避免早起尷尬...
    "Để tránh khó xử vào sáng sớm, hôm sau anh ra ngoài từ rất sớm. Vốn dĩ hôm nay anh chỉ cần đến khu Est nhìn qua tiến độ một cái là được, thế mà bị anh kéo dài cứng nhắc thành nửa ngày trời.",

    # 40: “喂，你今天挺怪啊。”倍良用肩膀毫不客氣地撞了下他...
    "“Này, hôm nay cậu lạ lắm đấy nhé.” Bội Lương dùng bả vai chẳng chút khách khí húc vào anh một cái. Gã vừa dẫn đội huấn luyện xong, trên người vẫn còn bốc hơi nóng hầm hập, trông mệt không chịu nổi.",

    # 41: 只是他的臉上卻掛著罕有的暢快意味...
    "Chỉ là trên mặt gã lại treo nụ cười sảng khoái hiếm thấy. Nhờ có bản vẽ và phương án của Lâu Hỉ Dương, gã đã nhìn thấy tương lai bang Lloyd trỗi dậy nhanh chóng. Nếu không có ngày tận thế, gã thậm chí còn cảm thấy việc Lloyd xưng bá toàn bộ hành tinh M cũng là điều hoàn toàn có thể.",

    # 42: 婁禧陽面不改色地轉過頭，上下打量了倍良一番。
    "Lâu Hỉ Dương mặt không đổi sắc quay đầu lại, đánh giá Bội Lương từ trên xuống dưới một lượt.",

    # 43: 上輩子他就見識過了倍良風流多情的本性，或許他可以解答他的疑慮。
    "Kiếp trước anh đã từng chứng kiến bản tính phong lưu đa tình của Bội Lương, có lẽ gã có thể giải đáp được mối băn khoăn của anh.",

    # 44: 而倍良卻被他這樣的目光看得渾身一顫，他僵硬地吞下嘴裡的水，“你幹嘛？”
    "Thế nhưng Bội Lương lại bị ánh mắt này của anh nhìn đến mức rùng mình một cái. Gã cứng đờ nuốt ngụm nước trong miệng xuống: “Cậu làm cái gì đấy?”",

    # 45: “我有個問題想問你。”婁禧陽平靜地收回了目光，“什麽情況下，你會有想吻別人的衝動？”
    "“Tôi có một câu hỏi muốn hỏi anh.” Lâu Hỉ Dương bình tĩnh thu hồi ánh mắt, “Trong tình huống nào thì anh sẽ có thôi thúc muốn hôn người khác?”",

    # 46: 對面的倍良聞言整張臉都酸得皺了起來...
    "Bội Lương đối diện nghe vậy cả khuôn mặt liền nhăn nhúm lại vì chua loét: “Vãi chưởng, cậu ở đây diễn vai thiếu nam ngây thơ với tôi đấy à? Đừng có làm trò này chứ, cậu đã có cái gì Dịch Duyên nhà cậu rồi, hỏi câu này làm cái quái gì?”",

    # 47: “你誤會了，他是我弟弟。”
    "“Anh hiểu lầm rồi, cậu ấy là em trai tôi.”",

    # 48: “親生的？”
    "“Ruột thịt à?”",

    # 49: “不是，是別人托給我帶的。”
    "“Không phải, là người khác phó thác cho tôi nuôi.”",

    # 50: “那說屁啊，不就是情弟弟嗎，你們那天可把我們這群大老爺們兒酸掉牙了。”
    "“Thế thì nói nhảm làm gì, chẳng phải là em trai tình nhân sao! Hôm đó hai người các cậu làm cho cả đám đàn ông to xác tụi tôi chua đến rụng cả răng rồi đấy.”",

    # 51: “我說了你誤會了。”
    "“Tôi đã nói là anh hiểu lầm rồi.”",

    # 52: ……
    "……",

    # 53: “你到底能不能回答？”婁禧陽被兩人間無意義地爭論搞得氣血上湧。
    "“Rốt cuộc anh có trả lời được không?” Lâu Hỉ Dương bị cuộc tranh cãi vô nghĩa giữa hai người chọc cho khí huyết sôi trào.",

    # 54: 倍良見他這副模樣當真是要發火了的樣子...
    "Bội Lương thấy bộ dạng này của anh quả thực như sắp nổi trận lôi đình tới nơi, trong thoáng chốc có chút ngạc nhiên hiếm thấy. Bao nhiêu ngày qua gã chưa từng thấy Lâu Hỉ Dương có bất kỳ bất mãn nào trước những lời châm chọc cố ý của mình, còn tưởng tính tình người này hiền lành lắm.",

    # 55: “好了，能為什麽，不就是想跟對方上.床嗎？”倍良輕浮地吹了聲口哨“反正我每次都是為了上.床才會想接吻。”
    "“Được rồi, còn vì cái gì nữa, chẳng phải là muốn lên giường với đối phương sao?” Bội Lương cợt nhả huýt sáo một tiếng, “Dù sao tôi lần nào cũng là vì muốn lên giường mới nảy sinh ý muốn hôn môi.”",

    # 56: 上.床？和易緣？
    "Lên giường? Cùng với Dịch Duyên?",

    # 57: 婁禧陽的臉越來越黑，一想到那個畫面他就覺得自己罪無可恕，他就不該信倍良能有什麽靠譜的回答。
    "Sắc mặt Lâu Hỉ Dương càng lúc càng đen xì. Vừa nghĩ đến khung cảnh đó anh liền cảm thấy bản thân tội không thể tha, anh đúng là không nên tin Bội Lương có thể cho ra câu trả lời đứng đắn nào.",

    # 58: “你想吻誰啊？”倍良突然面露精光地朝他靠近，“那個易緣小弟弟？”
    "“Cậu muốn hôn ai hả?” Bội Lương đột nhiên lộ vẻ tinh quái nhích lại gần anh, “Cái cậu em trai Dịch Duyên kia à?”",

    # 59: 被他問得想起來了昨天的事，婁禧陽心裡有些毛躁。
    "Bị gã hỏi dồn làm nhớ lại chuyện ngày hôm qua, trong lòng Lâu Hỉ Dương có chút bực dọc bồn chồn.",

    # 60: 倍良鍥而不舍地追問著，問得婁禧陽不耐煩地回了一句“我想吻狗。”
    "Bội Lương bám riết không tha truy hỏi dồn dập, hỏi đến mức Lâu Hỉ Dương mất kiên nhẫn bực bội ném lại một câu: “Tôi muốn hôn chó.”",

    # 61: 話音剛落，腦海裡就竄出來易緣帶著狗耳朵帽子和狗爪子手套衝他笑的畫面，在那一刻，婁禧陽突然明白了什麽。
    "Lời vừa dứt, trong đầu anh liền hiện lên hình ảnh Dịch Duyên đội chiếc mũ tai cún và đeo găng tay móng cún cười với mình. Ngay khoảnh khắc đó, Lâu Hỉ Dương đột nhiên hiểu ra điều gì.",

    # 62: “對，狗，我可能是看到狗才會有接吻的衝動。”婁禧陽恍然大悟，瞬間心裡的鬱結就通了。
    "“Đúng vậy, chó, tôi có lẽ là nhìn thấy chó mới có thôi thúc muốn hôn môi.” Lâu Hỉ Dương bừng tỉnh đại ngộ, u uất trong lòng tức khắc được đả thông thông suốt.",

    # 63: 搞明白異常後，他轉身就往樓下走。
    "Sau khi hiểu rõ được điều bất thường, anh quay người liền bước xuống lầu.",

    # 64: 而被忽視的倍良獨自僵在原地，整個人說是被五雷轟頂也不為過。
    "Mà Bội Lương bị ngó lơ đứng đơ ra một mình tại chỗ, cả người nói là bị sét đánh ngang tai cũng không hề quá chút nào.",

    # 65: 婁禧陽風風火火地回到了易緣家，他今天特意拿了兩個罕見的機甲模型，打算哄一哄易緣。
    "Lâu Hỉ Dương hớt hải vội vã quay về nhà Dịch Duyên. Hôm nay anh đặc biệt lấy hai mô hình cơ giáp hiếm thấy, định bụng dỗ dành Dịch Duyên một chút.",

    # 66: 然而當他推開家門時，卻沒看見易緣朝他撲來的身影。
    "Thế nhưng khi anh đẩy cửa bước vào nhà, lại không nhìn thấy bóng dáng Dịch Duyên nhào tới ôm chầm lấy mình.",

    # 67: 他皺了皺眉，懷疑可能是易緣還在生氣，故意沒來接他，便主動走進了臥室。
    "Anh nhíu nhíu mày, nghi ngờ có thể là Dịch Duyên vẫn còn đang giận dỗi nên cố ý không ra đón mình, bèn chủ động bước vào phòng ngủ.",

    # 68: 沒人。
    "Không có ai.",

    # 69: 被子整整齊齊地折在一起，整個房間看上去空曠了許多。
    "Chăn gối được gấp lại ngay ngắn chỉnh tề, cả căn phòng trông trống trải đi rất nhiều.",

    # 70: 突然意識到有什麽不對，婁禧陽眉頭皺的更緊了，他快步走到衣櫃前，打開櫃門，發現裡面易緣的衣服全部都不見了。
    "Đột nhiên ý thức được có điều gì không đúng, chân mày Lâu Hỉ Dương càng nhăn chặt hơn. Anh rảo bước tới trước tủ quần áo, mở cửa tủ ra, phát hiện quần áo bên trong của Dịch Duyên toàn bộ đều biến mất không còn một chiếc.",

    # 71: 他又將這間房子裡裡外外都找了個遍，仍是沒看到易緣的身影。
    "Anh lại tìm kiếm khắp trong ngoài căn nhà một lượt, vẫn không thấy bóng dáng Dịch Duyên đâu.",

    # 72: 讓自己冷靜下來後，婁禧陽將上輩子的記憶搜索了個遍，確定了上輩子易緣離開他的時間不是這一天，而是一個月後。
    "Sau khi ép bản thân phải bình tĩnh lại, Lâu Hỉ Dương lục lọi toàn bộ ký ức của kiếp trước, xác định thời điểm Dịch Duyên rời xa anh ở kiếp trước không phải là ngày hôm nay, mà là một tháng sau.",

    # 73: “系統，易緣呢？”他沉了沉眼皮，語氣微微發冷。
    "“Hệ thống, Dịch Duyên đâu rồi?” Anh trầm mí mắt xuống, ngữ khí hơi lạnh lẽo.",

    # 74: 倍良：媽媽呀，這裡有變態！！
    "Bội Lương: Mẹ ơi, ở đây có kẻ biến thái!!",

    # 75: 專欄預收——《假校霸他很甜》求收藏啦～
    "Dự thu chuyên mục—— 《Đại ca trường giả mạo cậu ấy rất ngọt ngào》 cầu cất chứa nha ~",

    # 76: 【看起來像校霸的傻白甜攻X武力值Max真校霸美人受】
    "【Bên ngoài trông như đại ca trường ngốc nghếch ngọt ngào Công X Lực chiến Max đại ca trường mỹ nhân thụ thụ】",

    # 77: 明高一班來了一個轉學生。
    "Lớp Một trường Minh Cao vừa tới một học sinh chuyển trường.",

    # 78: 轉學生身高直逼一米九，寸頭不說眉骨處還有一道疤，看人的眼神又冷又狂。
    "Học sinh chuyển trường chiều cao ngấp nghé một mét chín, đã đầu đinh húi cua rồi lại còn có một vết sẹo nơi xương lông mày, ánh mắt nhìn người vừa lạnh lùng vừa ngông cuồng.",

    # 79: 聽說他是從隔壁垃圾學校轉來的，眾所周知，那裡盛產校霸，內卷非常嚴重。
    "Nghe nói cậu ta chuyển tới từ trường học rác rưởi bên cạnh, ai cũng biết nơi đó nổi tiếng sản sinh ra trùm trường, mức độ ganh đua nội bộ vô cùng khốc liệt.",

    # 80: 這在表面平靜的明高扔下了一枚炸彈。
    "Điều này như ném một quả bom xuống ngôi trường Minh Cao vốn bề ngoài phẳng lặng.",

    # 81: 在手機第n次收到莫名其妙的挑釁短信後，轉學生孫乾哲爆發了
    "Sau khi điện thoại nhận được tin nhắn khiêu khích vô căn cứ lần thứ n, học sinh chuyển trường Tôn Càn Triết bùng nổ:",

    # 82: 都特麽的說了多少次，啊？
    "Đã mẹ nó nói bao nhiêu lần rồi hả?",

    # 83: 他是真的不會打架啊！
    "Cậu ấy thực sự là không biết đánh nhau mà!",

    # 84: “快看他表情…孫乾哲發飆了好嚇人嗚嗚嗚”“打起來打起來”
    "“Mau nhìn nét mặt cậu ta kìa... Tôn Càn Triết nổi điên lên đáng sợ quá hu hu hu” “Đánh nhau rồi đánh nhau rồi”",

    # 85: “我靠，他看過來了！”
    "“Vãi chưởng, cậu ta nhìn sang đây rồi!”",

    # 86: 眾人趕緊低頭，一瞬間，教室裡安靜如雞。
    "Mọi người vội vàng cúi gầm đầu, trong nháy mắt, phòng học im phăng phắc như thóc ngâm.",

    # 87: #到底怎樣才能讓新同學相信自己真的是個乖學生？#
    "# Rốt cuộc làm sao mới có thể khiến các bạn học mới tin rằng mình thực sự là một học sinh ngoan ngoãn? #",

    # 88: #總有人為我打架怎麽搞？#
    "# Cứ luôn có người vì tôi mà đánh nhau thì phải làm sao đây? #",

    # 89: *
    "*",

    # 90: 孫乾哲決定身體力行，證明自己是良好公民。
    "Tôn Càn Triết quyết định tự thân hành động, chứng minh bản thân là một công dân gương mẫu.",

    # 91: 當他看到小白兔同桌放學後走向陰暗的小巷，一個箭步衝過去，就將那些想要搶劫同桌的混混全都趕跑。
    "Khi cậu nhìn thấy bạn cùng bàn thỏ trắng nhỏ sau giờ học đi về phía con hẻm u ám, một bước lao nhanh tới, liền đuổi sạch đám côn đồ muốn cướp tiền bạn cùng bàn đi hết.",

    # 92: 果然，在一眾混混驚恐的眼神中，同桌抬頭感激看他。
    "Quả nhiên, giữa ánh mắt kinh hoàng của đám côn đồ, bạn cùng bàn ngẩng đầu cảm kích nhìn cậu.",

    # 93: 翌日，同桌在年級群裡發了一句：“他不是校霸。懂？”
    "Hôm sau, bạn cùng bàn nhắn một câu vào nhóm khối: “Cậu ấy không phải trùm trường. Hiểu chứ?”",

    # 94: 從此，再沒混混上來挑釁，也再沒人傳他是校霸，同學們都對他熱情萬分，孫乾哲很是滿意。
    "Từ đó về sau, không còn tên du côn nào tới gây sự, cũng không ai đồn đại cậu là trùm trường nữa, các bạn học đều đối xử với cậu nhiệt tình vô cùng, Tôn Càn Triết cảm thấy hết sức hài lòng.",

    # 95: *
    "*",

    # 96: 不是校霸也不是直男的孫乾哲最近得了失心瘋，他發現他的同桌越來越好看了。
    "Không phải trùm trường mà cũng chẳng phải trai thẳng, Tôn Càn Triết dạo gần đây như bị phát cuồng, cậu phát hiện bạn cùng bàn của mình càng ngày càng ưa nhìn.",

    # 97: 還很害羞，隨便逗逗耳根就泛紅，看的他心裡直癢癢。
    "Lại còn rất hay xấu hổ, tùy tiện trêu chọc một chút là vành tai liền ửng đỏ, nhìn đến mức trong lòng cậu cứ ngứa ngáy từng hồi.",

    # 98: 最重要的是他看起來很明顯對自己有意思嘛。
    "Quan trọng nhất chính là đối phương trông rõ ràng là có ý với cậu mà.",

    # 99: 幾個月後，孫乾哲深吸一口氣。
    "Mấy tháng sau, Tôn Càn Triết hít sâu một hơi.",

    # 100: 傻逼竟是我自己。
    "Kẻ ngốc ngếch hóa ra lại chính là bản thân mình.",

    # 101: “孫乾哲，再躲我就把你腿打斷，”真.美人校霸在他耳邊曖昧低語，眼底卻是一片溫柔，“你試試。”
    "“Tôn Càn Triết, còn dám trốn nữa tôi sẽ đánh gãy chân cậu,” Trùm trường mỹ nhân đích thực ghé vào tai cậu ám muội thì thào, nhưng đáy mắt lại chan chứa một mảnh dịu dàng, “Cậu thử xem.”",

    # 102: 【閱讀指南】
    "【Chỉ dẫn đọc truyện】",

    # 103: 互寵，he，甜
    "Hỗ sủng, HE, ngọt ngào"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_010 translation written: {len(paragraphs)} paragraphs.")
