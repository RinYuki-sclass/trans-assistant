# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_020"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 20: Anh lại hôn em rồi
---""",

    # 1: separator
    "====================",

    # 2: 治療所進來難出去倒是輕松的很...
    "Viện điều trị vào thì khó chứ ra thì lại nhẹ nhàng vô cùng. Động tác của Trương Sâm Trạch rất nhanh, chưa đầy nửa tiếng đã hùng hổ dẫn theo một đám người xông vào phòng bệnh của Lâu Hỉ Dương.",

    # 3: 婁禧陽說的急...
    "Lâu Hỉ Dương nói gấp gáp như vậy, gã vốn tưởng xảy ra chuyện gì to tát, nào ngờ vừa bước vào liền nhìn thấy một khung cảnh năm tháng tĩnh lặng đẹp đẽ.",

    # 4: 婁禧陽靠著床頭淺眠...
    "Lâu Hỉ Dương tựa vào đầu giường chợp mắt, ánh sáng len qua khe hở của tấm rèm cửa dày cộp chiếu sáng nửa bên mặt anh. Xuôi xuống dưới, trên eo anh gác một cánh tay trắng ngần, phía trong eo lộ ra một cái đầu tròn lông xù xù.",

    # 5: 床上躺著第二個人。
    "Trên giường đang nằm người thứ hai.",

    # 6: 婁禧陽正摟著他。
    "Lâu Hỉ Dương đang ôm lấy người đó.",

    # 7: 張森澤一時僵在了原地...
    "Trương Sâm Trạch nhất thời chết trân tại chỗ, gã ngơ ngác nhìn cánh tay kia, nửa ngày trời không làm ra phản ứng gì.",

    # 8: 婁禧陽已經換下了病服...
    "Lâu Hỉ Dương đã thay quần áo bệnh nhân ra, nghe thấy tiếng ồn ào liền có chút khó chịu, làm khẩu hình bảo bọn họ yên lặng một chút.",

    # 9: “手續辦好了？”...
    "“Thủ tục làm xong rồi chứ?” Lâu Hỉ Dương đè thấp giọng hỏi Trương Sâm Trạch vẫn còn đang ngẩn người.",

    # 10: 張森澤一個晃神，點了點頭。
    "Trương Sâm Trạch hoàn hồn lại, gật gật đầu.",

    # 11: 易緣被剛才的動靜吵到...
    "Dịch Duyên bị động tĩnh vừa rồi làm phiền, nửa tỉnh nửa mơ hừ hừ một tiếng. Cảm nhận được hơi thở quen thuộc vững chãi, cậu mới cọ cọ má vào làn da bên cạnh, dần dần yên tĩnh trở lại.",

    # 12: 張森澤被這人這樣小貓撒嬌般的舉動驚到了...
    "Trương Sâm Trạch bị hành động làm nũng như mèo con này của người nọ làm cho kinh ngạc. Gã vội vàng nhìn sang Lâu Hỉ Dương, chẳng những không thấy vẻ kháng cự của anh, ngược lại còn thấy anh nuông chiều xoa xoa đầu người nọ.",

    # 13: 他從來沒在婁禧陽臉上看到那樣的表情。
    "Gã chưa bao giờ nhìn thấy biểu cảm như vậy trên mặt Lâu Hỉ Dương.",

    # 14: 婁禧陽翻身下了床...
    "Lâu Hỉ Dương xoay người xuống giường. Anh rủ mắt nhìn người trên giường, khựng lại một lúc rồi quay người chỉ vào một tên đàn em nói: “Cởi áo của cậu ra, phiền các cậu ra ngoài trước một lát, tôi giúp cậu ấy thay đồ.”",

    # 15: 那人聞言一愣，連忙將衣服脫了下來。
    "Người nọ nghe vậy ngẩn ra, vội vàng cởi áo ra đưa tới.",

    # 16: 婁禧陽接過衣服...
    "Lâu Hỉ Dương đón lấy chiếc áo, đẩy Trương Sâm Trạch ra ngoài phòng bệnh, sau đó “cạch” một tiếng khóa trái cửa lại.",

    # 17: 原本他是想叫醒易緣讓他自己換一下...
    "Vốn dĩ anh định gọi Dịch Duyên dậy để cậu tự thay, dẫu sao đường đường chính chính dẫn một người mặc đồ hộ lý đi ra ngoài chắc chắn sẽ khiến người ta cảnh giác nghi ngờ. Nhưng Dịch Duyên đầm đìa mồ hôi lạnh, gọi thế nào cũng không tỉnh.",

    # 18: 無奈之下婁禧陽決定自己來幫他換。
    "Bất đắc dĩ, Lâu Hỉ Dương đành quyết định tự mình giúp cậu thay quần áo.",

    # 19: 可他的手剛解下易緣胸前的兩顆扣子後就再也下不去手了。
    "Thế nhưng tay anh vừa mới cởi được hai chiếc cúc trước ngực Dịch Duyên thì liền không tài nào tiếp tục xuống tay nổi nữa.",

    # 20: 操了，明明都是大老爺們兒，他這麽別扭幹什麽？
    "Mẹ kiếp, rõ ràng đều là đàn ông con trai với nhau cả, anh ngượng ngùng cái nỗi gì chứ?",

    # 21: 婁禧陽暗罵了自己一聲...
    "Lâu Hỉ Dương thầm mắng bản thân một câu, hạ quyết tâm, hít sâu một hơi rồi tự nhắc nhở mình không được phân tâm mà hoàn thành chuỗi động tác tiếp theo. Anh chẳng thèm nhìn sang nơi khác lấy một cái, ngón tay thoăn thoắt cởi hết toàn bộ hàng cúc áo.",

    # 22: 布料沒了束縛...
    "Tấm vải không còn trói buộc, tùy ý buông lơi tản mát sang hai bên, thấp thoáng để lộ làn da mịn màng không tì vết bên dưới lớp áo.",

    # 23: 或許是突然感受到了涼意...
    "Có lẽ là bất chợt cảm nhận được hơi lạnh, Dịch Duyên đột ngột nghiêng người, khẽ cuộn tròn thân thể lại.",

    # 24: 這下該看的不該看的全讓婁禧陽看光了。
    "Thế là phen này, chỗ nên nhìn hay không nên nhìn đều bị Lâu Hỉ Dương nhìn thấy sạch sành sanh.",

    # 25: 一個男的是怎麽做到腰這麽細還這麽白的？...
    "Một người đàn ông làm thế nào mà eo lại thon thả và trắng ngần đến mức này cơ chứ? Lâu Hỉ Dương trăm mối không thể hiểu nổi. Trong quan niệm của anh, đàn ông con trai thì phải giống như anh mới đúng, nói một câu công bằng, thế này thực sự là có chút ẻo lả quá đỗi.",

    # 26: 但一想到是易緣...
    "Thế nhưng vừa nghĩ tới đó là Dịch Duyên, anh chẳng những không cảm thấy ẻo lả, mà lại thấy hết sức đương nhiên, thậm chí anh còn lờ mờ cảm nhận được chút cảm giác không tự nhiên đang cuộn trào trong tim.",

    # 27: 他趕緊把不該有的想法丟掉...
    "Anh vội vàng vứt bỏ những suy nghĩ không nên có đi, lột áo trên của Dịch Duyên xuống rồi mặc chiếc áo sơ mi của vệ sĩ vào cho cậu.",

    # 28: 上衣換好後婁禧陽就開始解易緣的剩下的衣服...
    "Mặc xong áo trên, Lâu Hỉ Dương bắt đầu cởi nốt phần trang phục còn lại của Dịch Duyên. Vừa mới nắm lấy toan kéo xuống thì Dịch Duyên đột ngột vươn tay che lại, không cho anh động vào.",

    # 29: “不能脫。”易緣囈語。
    "“Không được cởi.” Dịch Duyên nói mớ.",

    # 30: “聽話，放手。”婁禧陽拍了拍他的手背，“我是你陽哥。”
    "“Ngoan, buông tay ra.” Lâu Hỉ Dương vỗ vỗ mu bàn tay cậu, “Anh là Dương ca của em đây.”",

    # 31: 不知是不是這句話的緣故...
    "Chẳng biết có phải nhờ câu nói này hay không mà Dịch Duyên thực sự ngoan ngoãn buông tay ra. Cậu còn lật người nằm sấp trên giường, phối hợp theo động tác của anh để anh cởi ra thuận lợi hơn.",

    # 32: 這下反而換作婁禧陽不利索了...
    "Phen này ngược lại đổi thành Lâu Hỉ Dương trở nên lúng túng luống cuống, bởi vì tay anh vừa vặn đặt ở vị trí vô cùng khó xử, tư thế hiện tại của hai người rất dễ khiến người ta liên tưởng miên man.",

    # 33: 秉著兄弟嘛，沒什麽大不了的心思...
    "Ôm tâm lý anh em với nhau thôi mà có gì to tát đâu, Lâu Hỉ Dương cắn răng, từ từ kéo lớp vải xuống.",

    # 34: 他的視野裡除了一片流暢的線條外...
    "Trong tầm mắt anh ngoại trừ những đường nét nuột nà mượt mà ra, còn dần dần hiện lên một hình xăm tinh xảo, xăm ở vị trí ngay phía dưới thắt lưng một chút, là một vầng thái dương đỏ rực, phần đuôi kéo dài mãi vào tận nơi sâu kín.",

    # 35: “我紋了一個紋身，在尾椎的位置。”
    "“Em đã xăm một hình xăm, ở chỗ xương cụt.”",

    # 36: “不告訴你，哥哥自己來看吧…”
    "“Không nói cho anh biết đâu, ca ca tự mình tới xem đi...”",

    # 37: 易緣的話從腦子裡冒了出來。
    "Những lời Dịch Duyên từng nói bỗng hiện lên trong đầu anh.",

    # 38: 婁禧陽怔愣地看著那個圖案...
    "Lâu Hỉ Dương ngơ ngác nhìn đồ án kia, đầu óc có một thoáng trống rỗng, ngay cả nhịp tim cũng bất giác đập dồn dập.",

    # 39: 太陽，是他的名字嗎？為什麽要把他紋在這裡？他不知道這個東西一輩子都洗不掉嗎？
    "Thái dương, mặt trời, là tên của anh sao? Tại sao lại xăm anh ở nơi này? Cậu không biết thứ này cả đời cũng không xóa đi được hay sao?",

    # 40: 荒唐的念頭佔據了他的腦海...
    "Ý nghĩ hoang đường chiếm trọn tâm trí anh. Như bị ma xui quỷ khiến, anh giơ tay lên, dùng phần thịt ngón tay cái vuốt ve lên hình xăm mặt trời, khẽ khàng xoa xoa vài cái.",

    # 41: “……”易緣突然繃緊了腰背...
    "“……” Dịch Duyên đột ngột căng cứng sống lưng, cậu uốn éo chỗ ngứa ngáy, cố gắng xua tan cảm giác nhột nhạt truyền tới từ xương cụt.",

    # 42: 婁禧陽像是觸電了般...
    "Lâu Hỉ Dương như bị điện giật, nhanh chóng rụt tay lại, thế nhưng tay mới rút được nửa đường thì đã bị một bàn tay khác chộp lấy.",

    # 43: 易緣不知道什麽時候醒了過來...
    "Dịch Duyên chẳng biết đã tỉnh dậy từ lúc nào, cậu trở tay nắm chặt lấy tay anh, đôi mắt ướt đẫm nước còn vương rặng mây đỏ.",

    # 44: “你看到了嗎？”他說，“哥哥，我把你紋到了我身上，我是你的。”
    "“Anh nhìn thấy rồi sao?” Cậu nói, “Ca ca, em đã xăm anh lên người em rồi, em là của anh.”",

    # 45: 婁禧陽喉結滾動著...
    "Yết hầu Lâu Hỉ Dương lăn chuyển, một câu cũng không thốt nên lời. Không một ai biết được câu nói này mang lại sự chấn động to lớn nhường nào cho anh, anh dùng lực siết chặt lấy tay Dịch Duyên, hơi thở dồn dập ngắn ngủi.",

    # 46: 下一秒，易緣從床上撲了上來。
    "Giây tiếp theo, Dịch Duyên từ trên giường nhào bổ lên người anh.",

    # 47: 他噙住婁禧陽的唇，細膩又繾倦地吻了起來。
    "Cậu ngậm lấy môi Lâu Hỉ Dương, tinh tế triền miên hôn lấy anh.",

    # 48: 像是火星子濺入了汽油裡...
    "Tựa như đốm lửa bắn vào trong thùng xăng, trong khoảnh khắc, ngọn lửa ngập trời thiêu rụi toàn bộ lý trí của Lâu Hỉ Dương.",

    # 49: 他扣住易緣的腦袋，一個翻身將他壓倒在床上，攻勢十足地表達著他的態度。
    "Anh giữ chặt lấy đầu Dịch Duyên, trở mình một cái đè nghiến cậu xuống giường, bày tỏ thái độ của mình bằng thế công mãnh liệt mười phần.",

    # 50: 曖昧的氣息在昏暗的病房裡持續了許久...
    "Bầu không khí mờ ám duy trì thật lâu trong căn phòng bệnh u tối. Lâu Hỉ Dương ngẩng đầu lên khỏi hõm cổ Dịch Duyên, kịp thời dừng lại những hành động không nên có.",

    # 51: “唔…”易緣喘著氣...
    "“Ưm...” Dịch Duyên thở dốc từng cơn, đôi mắt long lanh ngấn nước. Cậu nhìn chăm chú Lâu Hỉ Dương, càng dùng sức ôm chặt lấy anh hơn, sợ anh lại giống như lần trước vừa hôn xong liền trở mặt.",

    # 52: “你又親我了，不能走。”他執拗地抬起頭，又在婁禧陽嘴上啄了一口。
    "“Anh lại hôn em rồi, không được đi đâu đấy.” Cậu cố chấp ngẩng đầu lên, lại mổ thêm một cái lên môi Lâu Hỉ Dương.",

    # 53: “不走，乖，把衣服換好，我帶你離開這裡。”
    "“Không đi, ngoan, thay quần áo cho xong đi, anh đưa em rời khỏi nơi này.”",

    # 54: 婁禧陽聲音低啞...
    "Giọng Lâu Hỉ Dương khàn đục. Anh ngồi dậy khỏi người Dịch Duyên, nhanh chóng kéo chăn che lại. Nếu nhìn kỹ sẽ phát hiện vành tai anh đã đỏ rực như máu.",

    # 55: 易緣也坐了起來...
    "Dịch Duyên cũng ngồi dậy. Chiếc áo sơ mi ban nãy được Lâu Hỉ Dương cài nút ngay ngắn lúc này đã bị giật đứt hai chiếc cúc, thấp thoáng qua khe hở có thể nhìn thấy những vết hồng ngân mờ ám.",

    # 56: “陽哥，你什麽意思？”...
    "“Dương ca, anh có ý gì thế?” Cậu không kiềm chế nổi ngữ điệu phấn khích, nắm lấy Lâu Hỉ Dương gặng hỏi.",

    # 57: “快換上，之後再說。”...
    "“Mau mặc vào đi, chuyện đó nói sau.” Lâu Hỉ Dương điều hòa nhịp thở một lúc, sau khi bình tĩnh lại liền đưa quần cho cậu.",

    # 58: 易緣接過褲子...
    "Dịch Duyên nhận lấy quần, cũng chẳng hề kiêng dè Lâu Hỉ Dương, loáng một cái đã mặc xong xuôi.",

    # 59: 但他剛下床，就遲疑在了原地...
    "Thế nhưng vừa bước xuống giường, cậu liền ngập ngừng khựng lại tại chỗ: “Dương ca... Em không thể rời đi cùng anh được.”",

    # 60: “為什麽？”婁禧陽拽著他上前。
    "“Tại sao?” Lâu Hỉ Dương kéo cậu bước lên.",

    # 61: “我要是走了，芯片的摘除就徹底失敗了...”
    "“Nếu em bỏ đi, việc trích xuất con chip sẽ hoàn toàn thất bại. Chú ấy từng nói, nếu thất bại thì một nửa người dân trên hành tinh M đều sẽ chết, em muốn anh được sống sót bình an.” Vẻ mặt Dịch Duyên trở nên vô cùng nghiêm nghị.",

    # 62: 婁禧陽沉默了一會兒...
    "Lâu Hỉ Dương trầm mặc một lát, giữ thẳng mặt cậu lại, trịnh trọng đàng hoàng nói với cậu: “Nghe này Dịch Duyên, chuyện này rất phức tạp, Trần Liễm chưa chắc đã đáng tin. Hiện tại một chốc một lát không thể giải thích rõ ràng được, nhưng anh muốn em biết rằng anh đang hành động vì chân tướng, và anh nhất định sẽ thành công.”",

    # 63: 易緣似懂非懂地點點頭...
    "Dịch Duyên hiểu nửa vời gật gật đầu: “Nhưng trong người em có chứng cứ mà, lấy nó ra thì anh sẽ không cần...”",

    # 64: “我有其他的辦法，不需要你去犧牲...”
    "“Anh có cách khác, không cần em phải hy sinh,” Lâu Hỉ Dương nghiêm giọng dứt khoát cắt ngang lời cậu, “Dịch Duyên, bóc tách con chip rất đau đớn, anh không muốn nhìn thấy em giống như ngày hôm nay.”",

    # 65: “可芯片很重要，我可以熬過去。”易緣堅持道
    "“Nhưng con chip rất quan trọng, em có thể cắn răng chịu đựng được.” Dịch Duyên kiên trì nói.",

    # 66: “不行，你更重要。”...
    "“Không được, em quan trọng hơn.” Lâu Hỉ Dương nói xong mới nhận ra câu này mang hàm ý quá sâu xa, khẽ ho một tiếng, “Đi theo anh, anh sẽ tìm người tháo thiết bị sau gáy em xuống.”",

    # 67: 拽著易緣的手...
    "Nắm chặt lấy tay Dịch Duyên, anh dứt khoát kéo người vẫn còn đang ngẩn ngơ bước ra khỏi phòng bệnh.",

    # 68: 屋外的張森澤被突然打開的房門嚇了一跳...
    "Trương Sâm Trạch ở ngoài phòng bị cánh cửa đột ngột mở toang làm cho giật mình. Gã ngước mắt nhìn hai người trước sau bước ra, tầm mắt trước tiên dừng trên mặt Dịch Duyên nửa giây, sau đó lướt sang đôi môi đỏ ửng bất thường của Lâu Hỉ Dương.",

    # 69: “他…是你的鄰居弟弟？”...
    "“Cậu ta... Là cậu em trai hàng xóm của cậu à?” Môi Trương Sâm Trạch mấp máy liên hồi, chỉ rặn ra được đúng một câu này.",

    # 70: “嗯。”...
    "“Ừ.” Lâu Hỉ Dương mím mím môi, chuyển sang nói với người đàn ông đang thay đồ hộ lý trong phòng: “Làm phiền anh rồi, năm tiếng sau anh tìm cơ hội ra ngoài là được.”",

    # 71: 五個小時足夠他把易緣藏在一個相對安全的地方。
    "Năm tiếng đồng hồ là đủ để anh giấu Dịch Duyên ở một nơi tương đối an toàn.",

    # 72: 說完他拉過易緣...
    "Nói xong anh kéo Dịch Duyên qua, cố ý hay vô tình chắn đi ánh mắt của Trương Sâm Trạch, rảo bước nhanh chóng rời đi.",

    # 73: 張森澤的全自動無人超跑就停在治療所外...
    "Chiếc siêu xe không người lái hoàn toàn tự động của Trương Sâm Trạch đỗ ngay bên ngoài viện điều trị. Sau khi ba người lên xe liền rơi vào sự im lặng bất tận.",

    # 74: “陽哥，我身上的裝置有定位追蹤...”
    "“Dương ca, thiết bị trên người em có định vị theo dõi, hơn nữa nếu vượt khỏi phạm vi viện điều trị ba tiếng, người bên đó sẽ nhận được cảnh báo tới tìm em.” Dịch Duyên đột nhiên nhớ ra chuyện này, nắm chặt lấy tay Lâu Hỉ Dương.",

    # 75: “嗯，沒事。”
    "“Ừ, không sao.”",

    # 76: 婁禧陽早就考慮到了這一點...
    "Lâu Hỉ Dương đã sớm tính tới điểm này rồi. Chỉ cần anh có thể tháo bỏ hệ thống định vị theo dõi trong thiết bị trong vòng ba tiếng đồng hồ là được. Đối với toàn bộ thiết bị thì anh chưa chắc chắn, nhưng việc cắt đứt một bộ định vị thì vẫn có thể làm được dễ như trở bàn tay.",

    # 77: “哼。”...
    "“Hừ.” Trương Sâm Trạch ở hàng ghế trước đột nhiên quái gở kêu lên một tiếng: “Tiểu Dương, đừng trách tôi không nói trước với cậu nhé, cái thiết bị quỷ quái đó phức tạp lắm đấy, đám người kia chưa chắc đã xử lý được đâu.”",

    # 78: “慢慢來，到地方我先剪掉上面的定位，之後叫他們來。”...
    "“Cứ từ từ, tới nơi tôi sẽ cắt định vị bên trên trước, sau đó hẵng gọi bọn họ tới.” Lâu Hỉ Dương cúi đầu nhìn thời gian, đâu ra đấy lên kế hoạch cho các hành động tiếp theo.",

    # 79: “要是，他還是找到我了怎麽辦？”...
    "“Nếu như, chú ấy vẫn tìm được em thì phải làm sao?” Dịch Duyên đột ngột quay đầu lại, nhìn chằm chằm Lâu Hỉ Dương hỏi.",

    # 80: “那我就帶你逃出去。”...
    "“Vậy thì anh sẽ đưa em trốn ra ngoài.” Lâu Hỉ Dương nghiêng đầu nhìn lại. Nhận thấy ánh mắt Dịch Duyên ngày càng nóng rực thiêu đốt, anh bất động thanh sắc thu hồi ánh mắt.",

    # 81: 張森澤望著後視鏡裡的情景，拳頭越握越緊。
    "Trương Sâm Trạch nhìn cảnh tượng trong gương chiếu hậu, nắm đấm siết càng lúc càng chặt."
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_020 translation written: {len(paragraphs)} paragraphs.")
