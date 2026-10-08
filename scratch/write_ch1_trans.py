import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

paras = [
    # [0] ==============================
    "==============================",
    
    # [1] “末日即將來臨，M星球地面將不再適宜人類居住，天梯計劃已步上正軌，人類試圖在高空搭建新世界的構想終將完成。”
    "“Ngày tận thế sắp ập đến, mặt đất hành tinh M sẽ không còn thích hợp cho con người cư trú, Kế hoạch Thang Trời đã đi đúng quỹ đạo, ý tưởng con người xây dựng một thế giới mới trên không trung cuối cùng cũng sẽ hoàn thành.”",
    
    # [2] “聯邦137年3月14日，天梯計劃順利實施，paradise的搭建已有初步模型，人類的存活比例明顯提升…憑借paradise居住印章可在聯邦管理局登記侯住，或是購買星船票轉移至其它星球…”
    "“Ngày 14 tháng 3 năm Liên bang 137, Kế hoạch Thang Trời được triển khai thuận lợi, mô hình sơ khởi của Paradise đã hoàn thiện, tỉ lệ sống sót của nhân loại tăng lên rõ rệt... Dựa vào con dấu cư trú Paradise có thể đăng ký chờ vào ở tại Cục Quản lý Liên bang, hoặc mua vé tinh thuyền để di chuyển sang các hành tinh khác...”",
    
    # [3] 巨大的模擬光屏投射在空蕩的大街上，斷斷續續的影像孜孜不倦地重放著一個月前的新聞，影像裡的女女主播面無表情，平靜地宣布了M星球末日的來臨。
    "Màn hình quang học mô phỏng khổng lồ chiếu rọi xuống con phố vắng tanh, những thước phim chập chờn không mệt mỏi phát đi phát lại bản tin từ một tháng trước. Nữ phát thanh viên trong màn hình mặt không cảm xúc, bình tĩnh tuyên bố ngày tận thế của hành tinh M giáng lâm.",
    
    # [4] 但已經沒有人再稀得上抬頭看它一眼了，迫不得已出門購買物資的路人步履匆匆，下意識分出了一道奇異的目光落在路中央那穿著黑帽背心衛衣的男人身上。
    "Thế nhưng chẳng còn ai buồn ngẩng đầu nhìn lên lấy một lần nữa. Những người đi đường vạn bất đắc dĩ phải ra ngoài mua sắm nhu yếu phẩm đều rảo bước vội vã, trong vô thức lại liếc ánh nhìn kỳ lạ về phía người đàn ông mặc chiếc áo hoodie ba lỗ có mũ trùm màu đen đang đứng giữa đường.",
    
    # [5] 男人身材高挑，裸露出來的臂膀上蟄伏著肌肉，上面紋著看不出來形狀的紋路，一直延伸到背心裡面，有些泛白的帽沿幾乎將他半張臉都遮住了，隱隱約約能看見那利刀雕刻般的下頜線。
    "Người đàn ông vóc dáng cao ráo, cơ bắp cuồn cuộn trên cánh tay để trần, bên trên xăm những đường nét hoa văn không rõ hình thù kéo dài tận vào trong áo ba lỗ. Vành mũ trùm hơi bạc màu gần như che khuất nửa khuôn mặt, chỉ lờ mờ thấy được đường viền hàm dưới sắc bén tựa dao khắc.",
    
    # [6] 他微微抬著頭，似乎在看半空中懸浮的光屏，他有著與生俱來的氣場，單單站在那裡，就吸引了來去路人的眼光。
    "Anh khẽ ngẩng đầu, dường như đang nhìn màn hình lơ lửng giữa không trung. Khí chất trời sinh toát ra từ anh khiến cho việc anh chỉ đứng yên ở đó thôi cũng đủ thu hút mọi ánh mắt của người qua đường.",
    
    # [7] “還看什麽啊？誰不知道那paradise是給富人住的，一千萬星幣才能買到一枚居住印章，星船票就更不用說了，一億一張，像我們這樣的還不只能等死，快走吧，要是被他盯上了就完蛋了！”路過的人扯了把自己的老婆，瞥了一眼那邊的男人催促道。
    "“Còn nhìn cái gì nữa? Ai mà chẳng biết cái Paradise đó là để cho người giàu ở, một ngàn vạn tinh tệ mới mua nổi một con dấu cư trú, vé tinh thuyền thì khỏi phải bàn, một ức một vé, loại như chúng ta chỉ có nước chờ chết thôi. Mau đi đi, bị hắn nhắm trúng là xong đời đấy!” Một người đi đường kéo tay vợ mình, liếc nhìn người đàn ông đằng kia giục giã.",
    
    # [8] 看這副打扮就知道這又是一個妄自菲薄的窮光蛋，看上去也不像是什麽正經人，萬一搶他們的東西就不好了。
    "Nhìn cách ăn mặc đó là biết lại thêm một kẻ bần cùng tự sa ngã, trông chẳng giống người đàng hoàng đứng đắn gì, ngộ nhỡ cướp đồ của họ thì khốn.",
    
    # [9] 男人訓斥了一聲還在回頭看的老婆，兩人很快就走得沒影了。
    "Gã đàn ông quát người vợ vẫn còn ngoái đầu nhìn lại một tiếng, hai người nhanh chóng đi khuất dạng.",
    
    # [10] 婁禧陽聽著聲音，緩緩地收回了目光，嘴角似有似無的嘲諷也隨之銷聲匿跡。
    "Lâu Hỉ Dương nghe thấy những âm thanh đó, chậm rãi thu hồi ánh mắt, nét cười giễu cợt như có như không nơi khóe môi cũng theo đó biến mất không còn dấu vết.",
    
    # [11] 末日？paradise？真的很可笑。
    "Tận thế? Paradise? Thật nực cười làm sao.",
    
    # [12] 婁禧陽環視了一圈周圍，才克制住把那群聯邦的瘋子揪出來打一頓的念頭。
    "Lâu Hỉ Dương đưa mắt nhìn quanh một vòng, mới kiềm chế được ý định tóm cổ đám điên ở Liên bang ra đập cho một trận.",
    
    # [13] 而注意到他驟然發冷的視線的人都微不可察地與他拉開了距離，像他這樣的人，不管是末日還是從前都不會讓人產生親近之感。
    "Những ai nhận thấy ánh mắt đột nhiên lạnh buốt của anh đều bất giác né xa ra một khoảng. Một người như anh, dù là trong thời tận thế hay trước kia, chưa từng mang lại cho người khác cảm giác dễ gần gũi.",
    
    # [14] 或許不會有人知道，他心裡有著過於泛濫的同情心，換句話來說，他就是個老好人，和每一個救世主一樣。
    "Có lẽ chẳng một ai hay biết, sâu thẳm trong lòng anh lại thừa mứa sự đồng cảm đến mức dư thừa, nói cách khác, anh là một kẻ tốt bụng đến mức bao đồng, hệt như mọi đấng cứu thế khác.",
    
    # [15] 算著日子，今天剛好是他重生的第十年。
    "Tính theo ngày tháng, hôm nay vừa vặn tròn mười năm kể từ khi anh trọng sinh.",
    
    # [16] 說起來估計沒人會信，上輩子他算是拯救了整個M星球，甚至即將全票通過成為聯邦管理人，只是在他回家的路上，一把金光閃閃的鐵錘突然從天而降，仿佛帶著正義之光，硬生生將他給砸暈了。
    "Nói ra chắc chẳng ai tin, kiếp trước anh xem như đã cứu vớt toàn bộ hành tinh M, thậm chí sắp sửa được toàn phiếu thông qua trở thành người quản lý Liên bang, chỉ là trên đường trở về nhà, một chiếc búa sắt vàng óng ánh bất ngờ từ trên trời giáng xuống, mang theo luồng hào quang chính nghĩa chói lọi, nện thẳng vào đầu làm anh bất tỉnh nhân sự.",
    
    # [17] 昏迷前，他隱約聽見了一道脆生生地怒喊：【呔！欠債不還，天理難容！】
    "Trước khi hôn mê, anh lờ mờ nghe thấy một tiếng quát the thé giận dữ: 【Ái chà! Thiếu nợ không trả, thiên lý khó dung!】",
    
    # [18] 欠債？他欠什麽債了？
    "Thiếu nợ? Anh thiếu nợ cái gì cơ chứ?",
    
    # [19] 婁禧陽兩眼發直，還沒機會問出來，就發現自己一睜眼回到了他最狼狽的十七歲。
    "Lâu Hỉ Dương mắt mở trừng trừng, còn chưa kịp hỏi thành lời thì đã thấy mình vừa mở mắt ra đã quay trở về năm mười bảy tuổi chật vật nhất cuộc đời.",
    
    # [20] 那時的他還是個矜貴的公子哥，正準備去往Y星球深造機甲，哪知變故臨頭砸下，他的首都長官父親因貪汙受賄被捕，一夜之間，他被學院強硬退學，資金被全面凍結，從天之驕子淪為令人恥笑的笑柄。
    "Khi đó anh vẫn còn là một công tử quý phái ngậm thìa vàng, đang chuẩn bị sang hành tinh Y tu nghiệp cơ giáp chuyên sâu, nào ngờ tai họa ập xuống đầu, người cha làm quan chức thủ đô của anh bị bắt vì tội tham ô nhận hối lộ. Chỉ trong một đêm, anh bị học viện cưỡng chế đuổi học, toàn bộ tài sản bị đóng băng, từ con cưng của trời trượt dài thành trò cười cho thiên hạ.",
    
    # [21] 剛重生的婁禧陽再一次見到聯邦那一批人，看著他們漫不經心地將他的競賽獎杯在地上踢來踢去，皮笑肉不笑地將他請出了家門，封條上門，他的人生也由此徹底改寫。
    "Lâu Hỉ Dương vừa trọng sinh lại một lần nữa chạm mặt đám người Liên bang năm ấy, nhìn bọn chúng thản nhiên đá qua đá lại những chiếc cúp thi đấu của anh dưới sàn nhà, mặt cười mà mắt không cười “mời” anh ra khỏi cửa, dán niêm phong lên cổng nhà. Cuộc đời anh cũng từ giây phút ấy mà bị viết lại hoàn toàn.",
    
    # [22] 只是重來一次，他再也不會像從前那般可憐巴巴地擺出一副喪家犬的姿態去求別人，被一次次地拒之門外。
    "Chỉ là làm lại một đời, anh sẽ không bao giờ như trước đây, bày ra bộ dạng tội nghiệp như chó mất chủ đi van xin người khác để rồi hết lần này tới lần khác bị xua đuổi ngoài cửa.",
    
    # [23] 【目前還債進度：0%，宿主請努力哦～】系統那像是開了變聲器的萌娃聲音在他腦子裡回蕩。
    "【Tiến độ trả nợ hiện tại: 0%, ký chủ hãy cố gắng lên nhé~】 Giọng nói của hệ thống tựa như một đứa bé bật máy đổi giọng vang vọng trong đầu anh.",
    
    # [24] 【在此世界中，宿主可自由選擇是否重走過去的人生，但禁止崩壞原有的進程，否則世界崩塌，宿主死亡，同樣，若債務未還完，也會被系統抹殺哦，當宿主還完債後，便可選擇回到原有世界啦！】
    "【Trong thế giới này, ký chủ có thể tự do lựa chọn đi lại cuộc đời quá khứ hay không, nhưng nghiêm cấm làm sụp đổ tiến trình vốn có, nếu không thế giới sẽ sụp đổ và ký chủ sẽ tử vong. Tương tự, nếu món nợ chưa trả xong, ký chủ cũng sẽ bị hệ thống xóa sổ đó nha. Đến khi ký chủ trả xong nợ rồi thì có thể chọn quay về thế giới ban đầu nè!】",
    
    # [25] “我倒底欠了什麽債？”意外重生的婁禧陽摸著隱隱作痛的腦門，心裡其實並沒什麽波瀾，自他拯救世界後，他的人生便陷入了白水一般的寡淡無味，什麽都提不起他的興趣，重來一次，似乎也有點意思？
    "“Rốt cuộc ta đã thiếu món nợ gì?” Lâu Hỉ Dương bất ngờ trọng sinh xoa trán vẫn còn âm ỉ đau, trong lòng kỳ thực chẳng hề có chút gợn sóng nào. Kể từ sau khi giải cứu thế giới, cuộc đời anh đã rơi vào cảnh tẻ nhạt vô vị như nước ốc, chẳng còn điều gì khơi dậy được hứng thú nơi anh. Được sống lại một lần, dường như cũng có chút thú vị đấy chứ?",
    
    # [26] 他拖著一隻行李箱，名貴的襯衫在一片破敗老舊的居名樓裡顯得格格不入，他憑借著上一世的記憶，故意惹上了那群混混，又在意料之中時被那個男人救下了。
    "Anh kéo lê một chiếc vali hành lý, chiếc áo sơ mi đắt tiền trông hoàn toàn lạc quẻ giữa khu tập thể cũ kỹ đổ nát. Dựa vào ký ức kiếp trước, anh cố tình trêu chọc đám côn đồ du côn, rồi đúng như dự liệu được người đàn ông kia cứu giúp.",
    
    # [27] 男人帶著他左拐右繞，終於到了一棟看起來就年代久遠的居民房，這裡逼仄，潮濕，樓的外牆都是脫落的瓷磚和望不到盡頭的藤蔓。
    "Người đàn ông dẫn anh rẽ trái quẹo phải, cuối cùng cũng tới một tòa nhà dân cư trông có vẻ đã có từ rất lâu đời. Nơi đây chật hẹp, ẩm thấp, tường ngoài tòa nhà tróc lở gạch men và phủ kín những dây leo chằng chịt không thấy điểm dừng.",
    
    # [28] 【是情債哦，宿主。】小鐵錘故作曖昧地在他耳邊悄聲道。
    "【Là nợ tình đấy nhé, ký chủ.】 Tiểu Thiết Chùy làm bộ mập mờ, thì thầm bên tai anh.",
    
    # [29] 易天擦了擦手上殘留下來的血漬，將紙隨意地扔進了發著酸臭味的垃圾桶裡，“喏，小子，你就在這住下吧，一個月收你一千。”
    "Dịch Thiên lau sạch vết máu còn vương trên tay, tùy tiện ném tờ giấy vào thùng rác đang bốc mùi chua loét: “Này, nhóc con, cậu cứ ở lại đây đi, mỗi tháng thu cậu một ngàn.”",
    
    # [30] 婁禧陽正琢磨著系統的話，應了一聲便等著易天把鑰匙給他。
    "Lâu Hỉ Dương đang mải nghiền ngẫm lời của hệ thống, chỉ ừ một tiếng rồi đứng chờ Dịch Thiên đưa chìa khóa cho mình.",
    
    # [31] “爸爸。”
    "“Ba.”",
    
    # [32] 狹小的樓道突然響起了一道奶乎乎的聲音，瞬間拉回了婁禧陽複雜的思緒。對面的門突然打開，身後的光線勾勒出一個瘦小的身影，小孩緩步走到男人身邊。
    "Trong hành lang nhỏ hẹp bỗng vang lên một giọng nói non nớt ngây thơ, lập tức kéo dòng suy nghĩ phức tạp của Lâu Hỉ Dương quay trở về. Cánh cửa đối diện đột ngột mở ra, ánh sáng phía sau phác họa nên một bóng hình nhỏ thó gầy gò, đứa trẻ bước từng bước chậm rãi tới cạnh người đàn ông.",
    
    # [33] 眼前的小孩留著齊肩的短發，頭髮被他卡在耳後，露出了精致的下顎線。小孩的嘴很紅，上唇有顆圓潤的唇珠，鼻子很翹，單看還有些俏皮。最迷人的是他的眼睛，上挑的眼尾泛著紅，讓他不自覺想起了自家花園裡種的桔梗花。
    "Đứa trẻ trước mắt để mái tóc ngắn ngang vai, tóc được vén gọn sau tai để lộ đường viền hàm tinh tế. Đôi môi đứa nhỏ đỏ hồng, môi trên có một hạt châu tròn trịa, sống mũi rất cao và thẳng, nhìn riêng còn phảng phất nét tinh nghịch. Quyến rũ nhất chính là đôi mắt của cậu, đuôi mắt xếch lên ửng hồng, bất giác khiến anh nhớ tới những bông hoa cát cánh trồng trong vườn nhà mình.",
    
    # [34] 很漂亮，像個洋娃娃。
    "Rất đẹp đẽ, hệt như một con búp bê Tây.",
    
    # [35] 時隔多年再次看到這張臉，婁禧陽沉寂的心還是沒忍住重重一跳。
    "Cách biệt bao năm lại được nhìn thấy gương mặt này, trái tim vốn đã phẳng lặng của Lâu Hỉ Dương vẫn không kìm được mà đập thịch một tiếng thật mạnh.",
    
    # [36] 易緣，曾經陪伴了他人生中最孤獨狼狽的十年的鄰居弟弟，也是當初背叛他的人。
    "Dịch Duyên, cậu em hàng xóm từng đồng hành cùng anh suốt mười năm cô độc và chật vật nhất cuộc đời, cũng là kẻ năm xưa đã phản bội anh.",
    
    # [37] “這是我兒子易緣，今天滿九歲。”男人有些尷尬，拍了拍小孩的頭“快叫哥哥”
    "“Đây là con trai tôi Dịch Duyên, hôm nay tròn chín tuổi.” Người đàn ông có chút ngượng ngùng, vỗ vỗ đầu đứa nhỏ: “Mau gọi anh đi.”",
    
    # [38] 婁禧陽舔了下嘴唇，看向小孩的時候發現他正面無表情地盯著自己，眼神死氣沉沉的。
    "Lâu Hỉ Dương liếm môi, khi nhìn về phía đứa trẻ thì nhận thấy cậu đang mặt không cảm xúc nhìn chằm chằm vào mình, ánh mắt tĩnh mịch đến chết chóc.",
    
    # [39] “你好，我叫婁禧陽”想起來什麽，婁禧陽蹲下身來，也摸了摸小孩的頭，微微勾起了唇，柔聲道，“祝你生日快樂。”
    "“Chào em, anh tên là Lâu Hỉ Dương.” Nhớ ra điều gì đó, Lâu Hỉ Dương ngồi xổm xuống, cũng xoa xoa đầu đứa nhỏ, khóe môi khẽ cong lên, dịu giọng nói: “Chúc em sinh nhật vui vẻ.”",
    
    # [40] 他沒看見在他笑的時候，易緣死寂的眸子裡發出了一束亮光。
    "Anh không nhìn thấy ngay khoảnh khắc anh mỉm cười, nơi đáy mắt u ám của Dịch Duyên bỗng lóe lên một tia sáng rực rỡ.",
    
    # [41] 【叮咚！您的債主易緣已上線，目前還債進度：1%】
    "【Đinh đoong! Chủ nợ Dịch Duyên của ngài đã online, tiến độ trả nợ hiện tại: 1%】",
    
    # [42] 系統略顯興奮的聲音似乎又在婁禧陽的腦海裡響起，他猛然從回憶裡醒來，發現自己已經在路中央站了許久。
    "Âm thanh có phần phấn khích của hệ thống dường như lại vang lên trong tâm trí Lâu Hỉ Dương, anh bừng tỉnh khỏi dòng hồi ức, mới phát hiện mình đã đứng ngẩn ngơ giữa đường một hồi lâu.",
    
    # [43] 動了動酸澀的脖頸，婁禧陽邁開腿，開始做今天的正事——購買物資，回去喂易緣。
    "Khẽ xoay chiếc cổ đang mỏi nhừ, Lâu Hỉ Dương sải bước chân, bắt đầu làm việc chính của ngày hôm nay——mua nhu yếu phẩm rồi về nhà cho Dịch Duyên ăn.",
    
    # [44] 自從兩年前易緣的父親易天因車禍去世，婁禧陽就全然背負起了照顧易緣的責任，盡管就算易天還活著也不會管易緣，說起來，易緣從沒爹疼沒娘愛的小豆芽，在婁禧陽的照料下竟不知不覺地成年了，長成了一個冒著黑水的小玫瑰。
    "Kể từ sau khi cha của Dịch Duyên là Dịch Thiên qua đời vì tai nạn xe cộ hai năm trước, Lâu Hỉ Dương đã gánh vác toàn bộ trách nhiệm chăm sóc cậu. Dẫu cho Dịch Thiên còn sống thì ông ta cũng chẳng đoái hoài gì tới Dịch Duyên. Nói đi cũng phải nói lại, Dịch Duyên từ một mầm giá đỗ không cha thương không mẹ yêu, dưới sự săn sóc của Lâu Hỉ Dương thế mà đã bất giác trưởng thành, trổ mã thành một đóa hoa hồng nhỏ tẩm đầy độc đen.",
    
    # [45] 沒錯，黑芯子的那種。
    "Đúng vậy, chính là loại lòng dạ đen ngòm ấy.",
    
    # [46] 上輩子他全然沒發現這孩子哪裡不對，直到最後被他擺了一道，才發現自己蠢得要命。
    "Kiếp trước anh hoàn toàn chẳng nhận ra đứa nhỏ này có điểm nào bất thường, mãi cho đến cuối cùng bị cậu đâm sau lưng một vố đau điếng, anh mới vỡ lẽ nhận ra mình ngu ngốc đến cỡ nào.",
    
    # [47] 系統說他欠了易緣的情債，什麽意思？他理解不了。
    "Hệ thống bảo anh nợ Dịch Duyên nợ tình, rốt cuộc là có ý gì? Anh không tài nào hiểu nổi.",
    
    # [48] 不然也不會十年過去了他的還債進度才到10%。
    "Bằng không mười năm trôi qua rồi tiến độ trả nợ của anh cũng chẳng lẹt đẹt ở mức 10%.",
    
    # [49] 【宿主。】小鐵錘幽幽地發出了一聲長長的顫音，似在感歎這流水般的時間，又像是在為自己的青春傷懷。
    "【Ký chủ ơi.】 Tiểu Thiết Chùy u sầu phát ra một tiếng ngân dài ngao ngán, tựa như đang than thở thời gian thấm thoắt thoi đưa, lại như đang tiếc thương cho tuổi thanh xuân của chính mình.",
    
    # [50] 【十年了，你就刷了10%的進度，這樣下去，你恐怕得活到117歲才行…要不你還是研究一個長生不老的項目好了，哦哦，除此之外你還得順手拯救個世界，不然肯定活不到。】
    "【Mười năm rồi mà ngài mới cày được có 10% tiến độ, cứ đà này chắc ngài phải sống tới 117 tuổi mới xong việc mất... Hay là ngài đi nghiên cứu đề tài trường sinh bất lão luôn đi cho rồi, à à, ngoài ra ngài còn phải tiện tay giải cứu thế giới nữa đấy nhé, không thì chắc chắn chẳng sống thọ nổi đến lúc đó đâu.】",
    
    # [51] “要是你肯告訴我怎麽才算還債，我也不至於這樣。”
    "“Nếu mi chịu nói cho ta biết làm thế nào mới tính là trả nợ thì ta cũng đâu đến mức này.”",
    
    # [52] 這，這還要它怎麽教！情債嘛，不就是這樣這樣，再翻過來那樣那樣！
    "Chuyện, chuyện này còn cần nó phải dạy nữa sao! Nợ tình mà, chẳng phải chính là thế này thế này, rồi lại lật qua thế kia thế kia ư!",
    
    # [53] 小鐵錘羞得整個錘子都亮著紅光，但它一句話都不敢說，這是機密，得靠宿主自己悟。
    "Tiểu Thiết Chùy thẹn thùng tới mức cả cái búa đỏ rực lên, thế nhưng nó chẳng dám hé răng nửa lời. Đây là cơ mật, phải trông cậy vào ký chủ tự mình giác ngộ thôi.",
    
    # [54] 感覺到周圍安靜下來，婁禧陽平靜地屏蔽掉小鐵錘一聲接著一聲的歎氣。
    "Cảm nhận được không gian xung quanh đã yên ắng trở lại, Lâu Hỉ Dương bình thản chặn đứng những tiếng thở dài thườn thượt hết hơi này đến hơi khác của Tiểu Thiết Chùy.",
    
    # [55] 早在末日來臨的消息宣布前幾個月，婁禧陽便開始著意收集物資，也虧得他存的糧食夠多，才讓他和易緣能足不出戶一個月。
    "Ngay từ vài tháng trước khi tin tức tận thế được chính thức công bố, Lâu Hỉ Dương đã bắt đầu có ý thức tích trữ nhu yếu phẩm. Cũng may số lương thực anh dự trữ đủ nhiều, mới giúp anh và Dịch Duyên có thể ở yên trong nhà suốt một tháng ròng.",
    
    # [56] 他去了區裡最大的售貨區，這個時候只有這種規模的售貨區還在繼續營業，是由聯邦提供物資，還安排了嚴密的管控措施。每個人有明確的購買限額，一個身份碼一天限買十包。由於物資緊缺，普通的特級壓縮餅乾一包已經漲到了一百星幣，窮點的人根本買不起，大街上隨時會有人把購物袋搶走。
    "Anh đi tới khu bách hóa lớn nhất trong khu vực, vào thời điểm này chỉ có những khu thương mại tầm cỡ thế này mới còn mở cửa hoạt động, do Liên bang trực tiếp cung cấp hàng hóa và bố trí các biện pháp kiểm soát nghiêm ngặt. Mỗi người đều có hạn mức mua sắm rõ ràng, một mã định danh mỗi ngày chỉ được mua tối đa mười gói. Do hàng hóa khan hiếm, một gói bánh quy nén đặc cấp thông thường đã đội giá lên tới một trăm tinh tệ, người nghèo căn bản chẳng thể mua nổi, ngoài đường cái thì lúc nào cũng rình rập kẻ cướp giật túi đồ.",
    
    # [57] 婁禧陽看了眼時間，他答應易緣在八點前回去，眼前浮現出易緣委屈時那雙泛紅的眼睛，婁禧陽心裡一緊。
    "Lâu Hỉ Dương liếc nhìn đồng hồ, anh đã hứa với Dịch Duyên sẽ về trước tám giờ. Trong đầu bỗng hiện lên đôi mắt hoe đỏ của Dịch Duyên mỗi khi thấy tủi thân, lòng Lâu Hỉ Dương khẽ thắt lại.",
    
    # [58] 嘖，真賤。
    "Tặc, đúng là tự tìm khổ mà.",
    
    # [59] 婁禧陽暗暗唾棄自己，手下的動作卻仍是不知不覺快了起來。
    "Lâu Hỉ Dương thầm phỉ nhổ chính mình, thế nhưng động tác trên tay vẫn bất giác nhanh hơn hẳn.",
    
    # [60] 他估摸了一下自己頗為拮據的錢包，大概是足夠他買下這一些了。
    "Anh áng chừng chiếc ví tiền có phần eo hẹp của mình, áng chừng cũng vừa đủ để anh thanh toán chỗ đồ này.",
    
    # [61] 他拿過袋子，邁著長腿朝家裡快步走去。
    "Anh cầm lấy túi đồ, sải đôi chân dài rảo bước nhanh về nhà.",
    
    # [62] 盡管他一路跑回來，還是比約定的時間晚了十分鍾，在路過一樓時，婁禧陽遲疑了一會兒，還是從袋子裡拿出了兩塊壓縮餅乾，塞進了王婆婆的門縫裡。
    "Dẫu cho anh đã chạy suốt cả quãng đường về, nhưng vẫn trễ hơn mười phút so với giờ hẹn. Lúc đi ngang qua tầng một, Lâu Hỉ Dương chần chừ giây lát, rồi vẫn rút hai phong bánh quy nén trong túi ra, nhét qua khe cửa nhà bà cụ Vương.",
    
    # [63] 王婆婆是撿垃圾的，無夫無子，婁禧陽親眼目睹著她從六十歲撿到了七十歲，如今末世的到來，幾乎是斬斷了她所有的生路。
    "Bà cụ Vương sống bằng nghề nhặt rác, không chồng không con, Lâu Hỉ Dương đã tận mắt chứng kiến bà nhặt ve chai từ năm sáu mươi tuổi cho tới tận năm bảy mươi tuổi. Giờ đây ngày tận thế ập đến, gần như đã chặt đứt toàn bộ đường sống của bà.",
    
    # [64] 他和易緣住在三樓，破舊的居民樓隔音效果幾乎為零，短短的幾層台階，婁禧陽就聽見各種各樣的尖叫聲、哭喊聲，大家好像都想在臨死前，享受一場狂歡。
    "Anh và Dịch Duyên sống ở tầng ba, tòa nhà tập thể cũ nát có khả năng cách âm gần như bằng không. Chỉ trong vài bậc cầu thang ngắn ngủi, Lâu Hỉ Dương đã nghe thấy đủ loại tiếng la hét, tiếng khóc than, mọi người dường như đều muốn hưởng thụ một bữa tiệc cuồng hoan trước khi đón nhận cái chết.",
    
    # [65] 這也是婁禧陽禁止易緣出門的主要原因，易緣他長的太招人了。
    "Đây cũng là nguyên nhân chủ yếu khiến Lâu Hỉ Dương cấm Dịch Duyên bước chân ra khỏi cửa, Dịch Duyên lớn lên có diện mạo quá đỗi trêu ngươi dụ người.",
    
    # [66] 婁禧陽抬頭，預想中那巴巴等在樓道口的身影卻並未出現。
    "Lâu Hỉ Dương ngước mắt nhìn lên, bóng hình tha thiết đứng ngóng trông ở đầu cầu thang như trong dự liệu lại chẳng hề xuất hiện.",
    
    # [67] “哐當——”一聲重物從不遠處的上方響起。
    "“Rầm——” Một tiếng va đập của vật nặng đột ngột vang lên từ phía trên cách đó không xa.",
    
    # [68] 一種強烈的危機感突然湧上婁禧陽的心頭，他三兩步躍上台階，朝易緣家衝去。
    "Một dự cảm nguy hiểm mãnh liệt bất thình lình ùa lên cõi lòng Lâu Hỉ Dương, anh nhảy thoăn thoắt ba bước gộp làm hai lên các bậc thang, lao như bay về phía nhà Dịch Duyên.",
    
    # [69] 只見那扇本該緊閉著的鐵門半開著，門內還隱約傳來破碎的嗚咽聲。
    "Chỉ thấy cánh cửa sắt vốn dĩ phải khóa chặt giờ đây đang mở hờ một nửa, bên trong phòng còn mơ hồ truyền ra những tiếng nấc nghẹn ngào vụn vỡ.",
    
    # [70] “小緣——！”婁禧陽衝進門內，目光所及之處便是一片狼藉，在一片玻璃渣子中，躺著一個渾身冒血的壯漢，正捂著自己扭曲的鼻梁痛苦低吟。
    "“Tiểu Duyên——!” Lâu Hỉ Dương xông thẳng vào trong nhà, nơi tầm mắt quét qua là một mớ hỗn độn tan hoang. Giữa đống mảnh thủy tinh vỡ nát la liệt dưới sàn, có một gã hộ pháp to con máu me be bét đang nằm vật ra, hai tay ôm chặt sống mũi biến dạng rên rỉ đau đớn.",
    
    # [71] 他抬起眼皮，只見沙發上還壓著兩個男人，透過兩人的肩膀，他看到了易緣那張慘白的臉，更看到了他被撕扯至肩頭的白色薄衫，鎖骨上還粘上了鮮紅的血，易緣直勾勾地望著他，顫著聲喚他，像是奄奄一息的小動物，“陽哥…”
    "Anh nhướng mí mắt, chỉ thấy trên ghế sô pha còn có hai gã đàn ông đang đè ép xuống. Xuyên qua bả vai của hai gã, anh nhìn thấy khuôn mặt trắng bệch của Dịch Duyên, càng nhìn thấy rõ manh áo mỏng màu trắng của cậu bị giật rách toạc tới tận đầu vai, trên xương quai xanh còn vương vệt máu tươi đỏ thẫm. Dịch Duyên nhìn trừng trừng vào anh, cất giọng run rẩy gọi anh, tựa như một con thú nhỏ đang thoi thóp hơi tàn: “Dương ca…”",
    
    # [72] 其實如果婁禧陽留一個心眼的話，就會發現地上那壯漢的神情有多恐懼，沙發上那兩男人有多無措，而易緣那雙眼睛裡完全不是害怕，而是……一種獵物上鉤的興奮。
    "Kỳ thực nếu Lâu Hỉ Dương để tâm lưu ý một chút, anh sẽ nhận ra vẻ mặt của gã to con dưới đất đang tràn ngập nỗi kinh hoàng tới mức nào, hai gã trên sô pha thì hoang mang luống cuống ra sao, còn trong đôi mắt kia của Dịch Duyên căn bản chẳng hề có chút sợ hãi nào, mà là…… một niềm hưng phấn tột cùng khi thấy con mồi đã cắn câu.",
    
    # [73] 但他的理智完全被一股難以言說的怒火衝刷了個乾淨。
    "Thế nhưng lý trí của anh đã bị một ngọn lửa giận không tài nào diễn tả bằng lời thiêu rụi sạch bách.",
    
    # [74] “不是，兄弟，你聽我說，我沒……”那兩男人驚慌失措地從沙發上彈起，眼睜睜地看著眼前這個男人的手臂暴起了青筋，皮膚上的紋身令人為之一顫。
    "“Không phải, người anh em, cậu nghe tôi giải thích đã, tôi không có...” Hai gã đàn ông hoảng hốt bắn người bật dậy khỏi ghế sô pha, trừng mắt nhìn những đường gân xanh cuồn cuộn nổi lên trên cánh tay người đàn ông trước mặt, những hình xăm trên da thịt anh khiến người ta không rét mà run.",
    
    # [75] 艾恩匪幫，一群十足十的亡命之徒。
    "Băng đảng Ian, một lũ liều mạng cùng hung cực ác.",
    
    # [76] 簡易的黑色皮靴碾上地上那人的手臂，“哢擦”一聲，那條手臂以一條極為詭異的弧度垂落在地，而那人卻是連聲音都沒喊出來，就面色慘白地暈死了過去。
    "Đôi ủng da màu đen giản dị nghiền nát lên cánh tay của kẻ nằm dưới đất, một tiếng “rắc” giòn tan vang lên, cánh tay kia rũ xuống sàn nhà theo một góc độ vặn vẹo quái dị, mà kẻ nọ thậm chí còn chưa kịp thét lên tiếng nào đã mặt cắt không còn giọt máu ngất lịm đi.",
    
    # [77] 皮靴踩著手臂一步步走向沙發，婁禧陽帽沿下的薄唇抿出了一個殘忍的弧度。
    "Đôi ủng da giẫm qua cánh tay từng bước tiến về phía ghế sô pha, đôi môi mỏng dưới vành mũ trùm của Lâu Hỉ Dương mím lại thành một đường cong tàn nhẫn.",
    
    # [78] “別——”男人的話被婁禧陽的一個肘擊打回了肚子裡。
    "“Đừng——” Lời của gã đàn ông bị một cú thúc cùi chỏ hiểm hóc của Lâu Hỉ Dương nện ngược lại vào bụng.",
    
    # [79] 兩個壯漢，一次反擊的機會也沒有，就被婁禧陽雙雙打翻在地，一道黑影閃過，兩個人就徹底沒了意識。
    "Hai gã to con, đến nửa cơ hội phản kháng cũng không có, đã bị Lâu Hỉ Dương đánh gục lăn lộn xuống sàn, một bóng đen xẹt qua, cả hai người lập tức bất tỉnh nhân sự.",
    
    # [80] 婁禧陽悶不做聲地將地上的三個昏迷的人拎出了易緣的家，打包捆起來扔到了樓下的垃圾場。
    "Lâu Hỉ Dương lẳng lặng không nói một lời túm lấy ba kẻ hôn mê dưới đất lôi ra khỏi nhà Dịch Duyên, trói gô lại rồi quẳng thẳng xuống bãi rác dưới chân tòa nhà.",
    
    # [81] 望著易緣家半開的門，他深吸了一口氣，意識到自己的情緒確實是失控了，距離上一次自己情緒上頭，恐怕已經過了他自己都數不過來的時日。
    "Nhìn cánh cửa nhà Dịch Duyên vẫn đang mở hờ, anh hít sâu một hơi, nhận thức được rằng cảm xúc của mình quả thực đã mất kiểm soát. Cách lần cuối cùng anh nổi trận lôi đình như thế này, e rằng đã trôi qua những tháng ngày dài đằng đẵng đến chính anh cũng chẳng đếm xuể.",
    
    # [82] 他穩定了下情緒，走了進去，順手關上了鐵門。
    "Anh ổn định lại tâm trạng, cất bước đi vào trong, tiện tay đóng chặt cánh cửa sắt lại.",
    
    # [83] 易緣還維持著原來的狀態，他蜷縮在破舊的沙發上，整個人脆弱地發著抖，鎖骨上的那抹紅讓婁禧陽剛壓下去的躁鬱感又有複態重萌的趨勢。
    "Dịch Duyên vẫn duy trì tư thế ban đầu, cậu co ro trên chiếc sô pha cũ kỹ, cả người run rẩy đầy vẻ yếu ớt mong manh. Vệt máu đỏ tươi trên xương quai xanh khiến cảm giác bực bội nóng nảy mà Lâu Hỉ Dương vừa đè nén xuống lại có dấu hiệu bùng phát trở lại.",
    
    # [84] 婁禧陽走到沙發邊上，緩緩地俯下身來，擋住了易緣頭頂上的亮光。
    "Lâu Hỉ Dương bước tới bên cạnh ghế sô pha, chậm rãi cúi người xuống, che khuất luồng ánh sáng trên đỉnh đầu Dịch Duyên.",
    
    # [85] “小緣，別怕，哥哥回來了。”
    "“Tiểu Duyên, đừng sợ, anh về rồi đây.”",
    
    # [86] 溫熱的掌心撫過易緣的頭頂，他微不可察地一頓，突然從沙發上一躍而起，摟住了婁禧陽的脖子。
    "Lòng bàn tay ấm áp khẽ vuốt ve đỉnh đầu Dịch Duyên, cậu hơi khựng lại một thoáng khó lòng nhận ra, rồi đột ngột bật dậy khỏi sô pha, ôm chầm lấy cổ Lâu Hỉ Dương.",
    
    # [87] 婁禧陽自然而然地抱住了他，就像抱小孩一樣讓他縮在了自己的懷裡。
    "Lâu Hỉ Dương đón lấy cậu theo bản năng tự nhiên, tựa như ôm một đứa trẻ con để cậu rúc trọn vào lòng mình.",
    
    # [88] “陽哥，我好怕。”易緣在婁禧陽的頸間輕輕地蹭著，像隻撒嬌的小狗。
    "“Dương ca, em sợ lắm.” Dịch Duyên khẽ cọ cọ vào hõm cổ Lâu Hỉ Dương, hệt như một chú cún con đang làm nũng.",
    
    # [89] 如果忽略他眼裡翻湧的欲念的話。
    "Nếu như bỏ qua ngọn lửa dục vọng đang cuồn cuộn dâng trào nơi đáy mắt cậu.",
    
    # [90] 架空星際科幻背景，全是我瞎虛構的，別考據。攻受只是鄰居關系哦～求收藏（星星眼）
    "Bối cảnh khoa học viễn tưởng tinh tế giá không, toàn bộ đều do tôi tự bịa ra thôi, xin đừng khảo chứng. Công thụ lúc này chỉ là quan hệ hàng xóm láng giềng thôi nha~ Cầu mong mọi người nhấn yêu thích (mắt long lanh).",
    
    # [91] （易緣的乖巧都是裝的，在病與不病間反覆橫跳。）
    "(Sự ngoan ngoãn của Dịch Duyên đều là giả vờ cả đấy, cậu ấy liên tục nhảy qua nhảy lại giữa trạng thái có bệnh và không bệnh.)",
    
    # [92] 專欄預收求收藏——《治愈系奶狗拯救帥強慘反派[快穿]》
    "Chuyên mục hố mới xin cầu lưu trữ——《Cún Sữa Chữa Lành Cứu Rỗi Soái Cường Thảm Phản Diện [Khoái Xuyên]》",
    
    # [93] 有這麽一些反派，他們帥的慘絕人寰，蘇的炸裂蒼穹，狠的毀天滅地。
    "Có những nhân vật phản diện, bọn họ đẹp trai đến mức tuyệt luân, cuốn hút đến nổ tung bầu trời, tàn nhẫn đến mức hủy thiên diệt địa.",
    
    # [94] 但結局通通是被一身正氣的主角斬於劍下。
    "Thế nhưng kết cục của tất cả đều là bị nhân vật chính tràn đầy vẻ chính nghĩa chém rơi dưới lưỡi kiếm.",
    
    # [95] 外人都紛紛惋惜，這麽帥的帥哥，可惜是個瘋批。
    "Người ngoài ai nấy đều tấm tắc tiếc nuối, một soái ca tuấn tú dường ấy, tiếc thay lại là một kẻ điên khùng.",
    
    # [96] 然而他們都不知道，這些看似人格缺失的反派們，經歷過多少令人心驚的苦難。
    "Thế nhưng bọn họ chẳng hề hay biết, những kẻ tưởng chừng như nhân cách khiếm khuyết kia, đã từng phải trải qua bao nhiêu nỗi thống khổ rợn người.",
    
    # [97] 【你們的任務，是拯救這些反派。】
    "【Nhiệm vụ của các ngươi, chính là cứu rỗi những phản diện này.】",
    
    # [98] 執行官指著眼前一群天真爛漫的小毛球，愁的滿頭花白。
    "Chấp hành quan chỉ tay vào một đám cục bông nhỏ ngây thơ hồn nhiên trước mắt, lo lắng đến bạc cả đầu.",
    
    # [99] *
    "*",
    
    # [100] 小薩摩：軟綿綿雄蟲皇子X反叛軍首領【蟲族】
    "Samoyed nhỏ: Hùng trùng hoàng tử mềm mại đáng yêu X Thủ lĩnh quân phản loạn 【Trùng tộc】",
    
    # [101] 戰場上，屍橫遍野，滿身血氣的反叛軍首領在角落發現了一個瑟瑟發抖的小雄蟲。
    "Trên chiến trường thây chất đầy đồng, vị thủ lĩnh quân phản loạn nồng nặc mùi máu tanh phát hiện ra một chú hùng trùng nhỏ đang run rẩy co ro trong góc khuất.",
    
    # [102] 尖利的羽翅逼近雄蟲脆弱的脖頸。
    "Đôi cánh lông sắc nhọn kề sát vào chiếc cổ mảnh khảnh yếu ớt của hùng trùng.",
    
    # [103] 小雄蟲軟軟地捏了捏他的羽翅，小聲問他：你好，你能帶我回家嗎？
    "Chú hùng trùng nhỏ dùng đôi tay mềm mại khẽ nhéo nhéo cánh của y, nhỏ giọng hỏi: Xin chào, chú có thể đưa cháu về nhà không ạ?",
    
    # [104] 小馬爾濟斯：臭美小助理X凶狠武打影帝【娛樂圈】
    "Maltese nhỏ: Trợ lý nhỏ điệu đà thích làm đẹp X Ảnh đế phim võ thuật hung dữ 【Giới giải trí】",
    
    # [105] 靠武打戲名揚世界的影帝成名前過得落魄不堪。
    "Vị ảnh đế lừng danh thế giới nhờ những pha võ thuật hành động trước khi thành danh từng có chuỗi ngày bần cùng sa sút khôn cùng.",
    
    # [106] 在他一天被打得渾身是傷，卻只能吃兩碗泡麵的時候，白淨的少年出現在他面前。
    "Vào một ngày khi y bị đánh đến thương tích đầy mình, trong bụng chỉ có hai bát mì gói lót dạ, thì một thiếu niên trắng trẻo sạch sẽ bỗng xuất hiện trước mặt y.",
    
    # [107] 他說：我給你當助理好不好呀，不要錢的，但是你以後一定要給我買漂亮衣服嗷！
    "Cậu nói: Em làm trợ lý cho anh có được không nè, không lấy tiền đâu, nhưng sau này anh nhất định phải mua quần áo đẹp cho em đó nha!",
    
    # [108] …
    "…",
    
    # [109] 小柴，小阿拉，小雞毛等等（待定）
    "Shiba nhỏ, Alaska nhỏ, Golden nhỏ, v.v. (đang cập nhật)",
    
    # [110] 【閱讀指南】
    "【Hướng dẫn đọc】",
    
    # [111] 單元文，反派受，攻的原型是小狗
    "Đơn nguyên văn, thụ là phản diện, nguyên hình của công là những chú cún cưng",
    
    # [112] he，甜，求個收藏麽麽噠～（2023.1.3）
    "HE, ngọt ngào, xin cầu một nút theo dõi moah moah nè~ (3/1/2023)"
]

print(f"Total translated paragraphs: {len(paras)}")

# Write translation.md
ch_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_001"
trans_path = os.path.join(ch_dir, "translation.md")

content = "---\ntitle: Chương 1: Đinh, chủ nợ của bạn đã online\n---\n\n" + "\n\n".join(paras) + "\n"

with open(trans_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully written {trans_path}")
