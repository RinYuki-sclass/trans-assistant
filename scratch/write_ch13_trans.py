# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_013"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 13: Em nhớ anh
---""",

    # 1: separator
    "================",

    # 2: “你說什麽？！——要死的不是我們這群人？”
    "“Anh nói cái gì cơ?!—— Người phải chết không phải là đám người chúng ta?”",

    # 3: 倍良雙手握拳狠狠砸在桌上...
    "Bội Lương hai tay nắm chặt thành đấm nện mạnh xuống bàn, gân xanh căng phồng để lộ ra sự không thể tin nổi của gã.",

    # 4: 他的表情扭曲，試圖理解婁安明荒唐的話語。
    "Biểu cảm của gã vặn vẹo, cố gắng lý giải những lời nói hoang đường của Lâu An Minh.",

    # 5: “所謂M星的末日，其實是即將從地底滲透出來的一種毒氣。”
    "“Cái gọi là mạt thế của hành tinh M, thực chất là một loại khí độc sắp sửa thẩm thấu ra từ dưới lòng đất.”",

    # 6: “雖然滲透時間只有短短一個小時...”
    "“Tuy rằng thời gian thẩm thấu chỉ ngắn ngủi trong vòng một tiếng đồng hồ, nhưng nguyên tố phóng xạ nồng độ cực cao trong khí độc có thể khiến sinh vật bị phong tỏa bên trong tuyệt chủng trong vòng một ngày...”",

    # 7: 婁安明從終端中劃出M星網上關於“毒氣”的資料...
    "Lâu An Minh từ thiết bị đầu cuối kéo ra tư liệu về “khí độc” trên mạng hành tinh M, ra hiệu cho bọn họ xem qua.",

    # 8: 他指著資料上的一行字...
    "Ông chỉ vào một dòng chữ trên tư liệu: “Nhưng may mắn là, hành tinh M có thể chia đơn giản thành ba tầng khí quyển, mật độ của mỗi tầng khí quyển giảm dần theo thứ tự. Tầng khí quyển Lyon thứ hai có mật độ nhỏ hơn khí độc, như vậy khí độc sẽ bị phong tỏa lại, không thoát ra ngoài được.”",

    # 9: “我知道原理，蔣卓航在媒體前解釋過無數次...”
    "“Tôi biết nguyên lý này, Tưởng Trác Hàng đã giải thích trước truyền thông vô số lần rồi. Phạm vi thẩm thấu của khí độc nằm trong tầng khí quyển thứ hai, tức là trên mặt đất, cho nên những người ở lại trên mặt đất của hành tinh M chắc chắn phải chết không nghi ngờ gì.” Bội Lương lướt nhanh qua một lượt, khẳng định chắc nịch.",

    # 10: “是，但那只是蔣卓航想讓你們知道的。”
    "“Đúng vậy, nhưng đó chỉ là những gì Tưởng Trác Hàng muốn cho các cậu biết mà thôi.”",

    # 11: 婁安明停頓了一下...
    "Lâu An Minh dừng lại một chút, khóe môi nhếch lên một nụ cười đầy vẻ mỉa mai: “Có phải hắn ta còn nói rằng, vì sức chứa của Paradise có hạn, cho nên chỉ có thể thông qua phương thức mua giấy chứng nhận cư trú để chọn ra những cư dân hành tinh M có thể sống sót? Hắn ta cảm thấy rất hổ thẹn, vì để chuộc tội lỗi của mình, vào thời khắc tận thế giáng lâm, hắn sẽ ở lại mặt đất, cùng đối mặt với cái chết cùng hành tinh M.”",

    # 12: 被戳到心裡的想法...
    "Bị nói trúng suy nghĩ trong lòng, Bội Lương ngẩn ra một thoáng, buột miệng nói: “Đúng thế, Tưởng Trác Hàng dù có nham hiểm đến đâu thì cũng coi như là một trang nam tử hán.”",

    # 13: “不，”婁安明閉上眼睛...
    "“Không,” Lâu An Minh nhắm mắt lại, thanh âm đột ngột hạ thấp xuống, “Cậu đã bao giờ nghĩ tới—— mật độ của khí độc có lẽ không hề lớn hơn tầng khí quyển thứ hai, mà là nhỏ hơn nó rất nhiều, đến lúc đó nó sẽ bay lên trên chứ không phải lắng xuống dưới hay chưa?”",

    # 14: 倍良被婁安明的話給釘在了原地...
    "Bội Lương bị những lời của Lâu An Minh đóng đinh tại chỗ. Cả người gã cứng đờ, hai cánh môi mất khống chế hé mở, phát ra những tiếng nghi vấn vô nghĩa.",

    # 15: 身後哐當一聲，是拐杖砸落到地面的聲響。
    "Phía sau vang lên một tiếng “choang” chói tai, là âm thanh cây gậy chống rơi đập xuống mặt sàn.",

    # 16: 紅發老頭顫著手，連胡須也細微地晃動了起來。
    "Lão già tóc đỏ run rẩy đôi bàn tay, ngay cả chòm râu cũng khẽ rung lên bần bật.",

    # 17: 他們都明白了這句提問裡的意思...
    "Bọn họ đều đã hiểu được ý tứ trong câu hỏi này: không gian bị khí độc phong tỏa, vừa vặn lại chính là nơi tọa lạc của Paradise.",

    # 18: 所以說，面臨死亡的不是他們這些遺留在地面的窮光蛋...
    "Nói cách khác, những kẻ phải đối mặt với cái chết không phải là đám nghèo kiết xác bị bỏ lại trên mặt đất như bọn họ, mà là những kẻ hào nhoáng rực rỡ nắm giữ tiền tài và quyền lực trong tay.",

    # 19: “…為什麽？”倍良啊啊了半天，最終憋出了幾個字。
    "“... Tại sao?” Bội Lương ú ớ nửa ngày trời, cuối cùng mới rặn ra được mấy chữ.",

    # 20: “因為他是瘋子，你們知道，他心裡有恨。”
    "“Bởi vì hắn ta là kẻ điên, các cậu biết đấy, trong lòng hắn có hận thù.” Lâu An Minh nhớ lại điều gì đó, trong mắt đong đầy thêm vài phần cảm xúc phức tạp.",

    # 21: 房間內陷入了漫長的沉默。
    "Bên trong căn phòng rơi vào một khoảng trầm mặc dài đằng đẵng.",

    # 22: “你是怎麽知道的？”...
    "“Làm sao anh biết được chuyện này?” Lời nói bất thình lình phá vỡ bầu không khí im lặng. Lão già tóc đỏ móc cây gậy chống lên, từng bước từng bước đi về phía Lâu An Minh.",

    # 23: “這個毒氣在十幾年前就有征兆了...”
    "“Loại khí độc này từ mười mấy năm trước đã có dấu hiệu rồi, mà người đầu tiên phát hiện ra nó chính là mẹ của Tiểu Dương.” Ánh mắt Lâu An Minh chuyển động, hướng tầm nhìn về phía Lâu Hỉ Dương đang ở trong góc.",

    # 24: 不同於瞠目結舌的其余二人...
    "Khác hẳn với hai người còn lại đang há hốc mồm kinh ngạc, Lâu Hỉ Dương từ đầu đến cuối đều bình thản dựa vào vách tường, cúi đầu nhìn thiết bị đầu cuối, trông như đang xuất thần mất tập trung.",

    # 25: 剛剛易緣突然給他打來了視頻通訊，但他沒接。
    "Vừa nãy Dịch Duyên đột nhiên gọi cuộc gọi video tới cho anh, nhưng anh không bắt máy.",

    # 26: 感覺到幾人的焦點移到了他的身上...
    "Cảm nhận được tiêu điểm của mấy người dời sang người mình, anh ngẩng đầu lên, hồi tưởng lại những lời Lâu An Minh vừa nói.",

    # 27: 適宜的，他疑惑地抬起了眉，“母親？”
    "Vô cùng thích hợp, anh nghi hoặc nhướng mày: “Mẹ ư?”",

    # 28: 他的母親是M星唯一一個獲得聯邦五星徽章的科學家...
    "Mẹ của anh là nhà khoa học duy nhất trên hành tinh M nhận được Huy chương Năm Sao của Liên bang, chuyện này ngoại trừ đám người Liên bang ra thì chẳng ai hay biết.",

    # 29: 而她早就在生下他後不見了蹤影...
    "Mà bà đã sớm mất tích không dấu vết sau khi sinh ra anh, Lâu An Minh cũng cố ý giấu giếm. Nếu Lâu Hỉ Dương không phải người trọng sinh thì đến tận bây giờ anh cũng sẽ không biết bà đã đi đâu.",

    # 30: 婁安明見他這副模樣，走過來拍了拍他的肩...
    "Lâu An Minh thấy bộ dạng này của anh, bước tới vỗ vỗ vai anh: “Trên người bà ấy nắm giữ chân tướng của khí độc, Tưởng Trác Hàng đang bí mật khống chế bà ấy.”",

    # 31: “小陽，明天，跟爸爸一起混進paradise找她，好嗎？”
    "“Tiểu Dương, ngày mai cùng ba trà trộn vào Paradise tìm bà ấy, được không?”",

    # 32: 感覺到肩膀處傳來的迫壓...
    "Cảm nhận được áp lực truyền tới từ bả vai, Lâu Hỉ Dương nâng mí mắt lên, yết hầu chuyển động, khẽ “ừm” một tiếng.",

    # 33: *
    "*",

    # 34: 婁禧陽回到自己的單人間，砰的一聲把門關上了。
    "Lâu Hỉ Dương quay về phòng đơn của mình, “rầm” một tiếng đóng sập cửa lại.",

    # 35: 打開終端，入眼就是易緣那條被掛斷的通訊記錄。
    "Mở thiết bị đầu cuối ra, đập vào mắt chính là bản ghi cuộc gọi bị cúp máy kia của Dịch Duyên.",

    # 36: 易緣走後，婁禧陽沒有發任何消息過去，甚至沒有問一句他去了哪裡。
    "Sau khi Dịch Duyên rời đi, Lâu Hỉ Dương không hề gửi bất kỳ tin nhắn nào qua đó, thậm chí chưa từng hỏi một câu cậu đã đi đâu.",

    # 37: 他承認他是有幾分刻意，誰叫這小兔崽子一聲不吭地就離家出走。
    "Anh thừa nhận bản thân có vài phần cố ý, ai bảo cái tên ranh con này chẳng nói chẳng rằng một tiếng liền bỏ nhà ra đi cơ chứ.",

    # 38: 【宿主，你想打就打過去嘛，一直盯著看眼睛不酸嘛～～】
    "【Ký chủ, ngài muốn gọi thì cứ gọi qua đó đi mà, cứ nhìn chằm chằm mãi thế mắt không mỏi sao ~~】",

    # 39: 小鐵錘壓低錘頭...
    "Búa sắt nhỏ hạ thấp đầu búa, đẩy đẩy mu bàn tay Lâu Hỉ Dương định giúp anh ấn nút gọi đi, lại bị một luồng khí lạnh thấu xương dọa cho sợ đến mức không dám nhúc nhích.",

    # 40: 幸好，在它以為自己要被眼刀子刮死時，易緣的視頻又打過來了。
    "May mắn thay, ngay lúc nó tưởng rằng mình sắp bị ánh mắt sắc như dao cạo cho chết thì cuộc gọi video của Dịch Duyên lại gọi tới.",

    # 41: 然後它就看見宿主冒著冷氣的臉一下子就變了...
    "Thế rồi nó nhìn thấy gương mặt đang tỏa ra khí lạnh của ký chủ bỗng chốc biến đổi, bất động thanh sắc chờ mười giây mới bình tĩnh nhận cuộc gọi.",

    # 42: 【哼！別以為我沒看見你嘴角彎了！】
    "【Hừ! Đừng tưởng tôi không nhìn thấy khóe môi ngài đã cong lên rồi nhé!】",

    # 43: “喂？”
    "“Alo?”",

    # 44: 婁禧陽靠在床頭，抬起眼皮看著眼前投影裡的人。
    "Lâu Hỉ Dương dựa vào đầu giường, nâng mí mắt nhìn người trong hình ảnh chiếu ảo trước mặt.",

    # 45: 易緣那邊的環境很暗，幾乎除了他的人什麽也看不清楚，不過大概能看出一張床的輪廓。
    "Không gian bên phía Dịch Duyên rất tối, gần như ngoại trừ người cậu ra thì chẳng nhìn rõ thứ gì khác, nhưng đại khái vẫn có thể nhìn ra đường nét của một chiếc giường.",

    # 46: “陽哥？”對面的人似乎有些緊張，連忙調整了一下鏡頭，將它對準了臉。
    "“Dương ca?” Người đối diện dường như có chút căng thẳng, vội vàng điều chỉnh lại ống kính một chút, nhắm thẳng vào khuôn mặt mình.",

    # 47: 易緣像是洗了澡...
    "Dịch Duyên dường như vừa mới tắm xong, đôi mắt xinh đẹp phủ lên một tầng sương nước, những lọn tóc mềm mại trước trán hơi ẩm ướt, trên chóp mũi cao thẳng còn đọng lại một giọt nước.",

    # 48: “我…我現在在一個朋友的家裡，等我在這裡玩幾天，就…就回去。”
    "“Em... Em hiện tại đang ở nhà một người bạn, đợi em chơi ở đây mấy ngày thì... thì sẽ về.” Dịch Duyên vô thức cắn chặt môi mình, cắn đến mức cánh môi mềm mại ướt át kia trắng bệch ra.",

    # 49: “嗯。”婁禧陽盯著那張唇，語氣聽起來毫無波動。
    "“Ừ.” Lâu Hỉ Dương nhìn chằm chằm cánh môi kia, ngữ khí nghe chẳng chút gợn sóng.",

    # 50: 朋友？太蹩腳的謊言，從小到大，易緣從來沒有過任何朋友。
    "Bạn bè ư? Một lời nói dối quá đỗi vụng về, từ nhỏ đến lớn, Dịch Duyên chưa từng có bất kỳ người bạn nào cả.",

    # 51: 易緣當然知道自己的話有多離譜...
    "Dịch Duyên đương nhiên biết lời nói của mình phi lý đến mức nào. Chính vì vậy, cậu bị sự hờ hững lạnh nhạt của Lâu Hỉ Dương đâm chọc sâu sắc, có phải anh căn bản chẳng hề lo lắng cho cậu, cho nên ngay cả điều này cũng không phát hiện ra?",

    # 52: 瞳孔微縮，易緣的眼睛逐漸染上了一圈紅暈...
    "Đồng tử co rút nhẹ, đôi mắt Dịch Duyên dần nhuộm lên một vòng ửng đỏ. Cậu nhìn Lâu Hỉ Dương, đè nén thanh âm chua xót, giả vờ thoải mái nói: “Dương ca, bốn ngày rồi, anh cũng chẳng hề hỏi em đi đâu, sao anh có thể như vậy chứ.”",

    # 53: 說不清緣由，在那一瞬間，婁禧陽清晰地捕捉到了心裡的酸脹感。
    "Chẳng rõ nguyên do, trong khoảnh khắc đó, Lâu Hỉ Dương bắt trọn được cảm giác cay cay xót xa dâng trào trong lòng.",

    # 54: 突然的一下冒出來，然後密密麻麻地延伸到指尖。
    "Nó bất thình lình nhú lên, rồi sau đó râm ran lan tỏa dày đặc tới tận đầu ngón tay.",

    # 55: “小緣，”握緊指尖，婁禧陽終是松了口，他直起腰，認真地對上易緣的眼睛，語速輕緩，
    "“Tiểu Duyên,” siết chặt đầu ngón tay, Lâu Hỉ Dương rốt cuộc cũng chịu nhượng bộ. Anh thẳng lưng dậy, nghiêm túc nhìn thẳng vào mắt Dịch Duyên, tốc độ nói nhẹ nhàng chậm rãi:",

    # 56: “我很擔心你，但我尊重你的選擇。”
    "“Anh rất lo lắng cho em, nhưng anh tôn trọng lựa chọn của em.”",

    # 57: 日思夜想的臉突然放大...
    "Gương mặt ngày nhớ đêm mong đột ngột phóng to trước mắt. Dịch Duyên ngẩn ngơ một lúc, sau khi hiểu được ý tứ của Lâu Hỉ Dương, trên gương mặt trắng nõn dần dần lan ra hai rặng mây đỏ.",

    # 58: “擔心我…是想我的意思嗎？”他的眼神飄忽不定，看上去竟有些羞澀。
    "“Lo lắng cho em... là có ý nhớ em đúng không?” Ánh mắt cậu phiêu hốt bất định, trông vậy mà lại có chút ngượng ngùng e ấp.",

    # 59: “我好想你呀，哥哥。”他極其小聲地補了一句...
    "“Em nhớ anh lắm đó, ca ca.” Cậu cực kỳ nhỏ giọng bồi thêm một câu, cúi đầu không dám nhìn Lâu Hỉ Dương. Vòng xoáy tóc ngoan ngoãn che trước ống kính, đung đưa làm tâm can Lâu Hỉ Dương ngứa ngáy từng hồi.",

    # 60: “嗯，我也想你。”
    "“Ừ, anh cũng nhớ em.”",

    # 61: 被鬼迷了心竅，婁禧陽竟隨著心裡想的說了出來。
    "Như bị ma xui quỷ khiến, Lâu Hỉ Dương lại nói ra đúng những gì trong lòng mình suy nghĩ.",

    # 62: 等他反應過來時，隻覺得頭皮發麻。
    "Đến khi anh phản ứng lại thì chỉ cảm thấy da đầu tê rần.",

    # 63: 不知道他這句話給了易緣多大的鼓舞...
    "Chẳng biết câu nói này đã đem lại nguồn khích lệ to lớn dường nào cho Dịch Duyên, cậu đột ngột ngẩng phắt đầu lên, nụ cười rạng rỡ ngoác tận mang tai. Khác hẳn với một Lâu Hỉ Dương đang ngượng ngùng khó xử, cậu nhảy cẫng lên khỏi giường.",

    # 64: “陽哥，我有個東西想給你看。”
    "“Dương ca, em có một thứ này muốn cho anh xem.”",

    # 65: 易緣的聲音聽起來很是興奮，稍稍讓婁禧陽從奇怪的氛圍裡走了出來。
    "Giọng nói của Dịch Duyên nghe có vẻ vô cùng phấn khích, thoáng chốc kéo Lâu Hỉ Dương thoát ra khỏi bầu không khí kỳ quặc ban nãy.",

    # 66: 但很快他就更加不自在了。
    "Thế nhưng rất nhanh sau đó anh lại càng thêm không tự nhiên.",

    # 67: 因為他看見易緣在脫衣服。
    "Bởi vì anh nhìn thấy Dịch Duyên đang cởi quần áo.",

    # 68: 婁禧陽這種鋼鐵直男真的很不擅長肉麻啊哈哈哈哈
    "Một gã trai thẳng như thép nguội cỡ Lâu Hỉ Dương quả thực là cực kỳ không thạo mấy chuyện sến sẩm này đâu ha ha ha ha"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_013 translation written: {len(paragraphs)} paragraphs.")
