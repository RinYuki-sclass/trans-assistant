# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_016"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 16: Hắn cũng giống như em
---""",

    # 1: separator
    "====================",

    # 2: “我不需要護工。”...
    "“Tôi không cần hộ lý.” Lâu Hỉ Dương chuyển hướng nhìn về phía bác sĩ kiểm tra phòng, lắc lắc đầu.",

    # 3: 他的余光沒有放過那護工眼裡閃過的一瞬緊張。
    "Khóe mắt anh không hề bỏ sót tia căng thẳng thoáng xẹt qua trong mắt người hộ lý kia.",

    # 4: 怎麽回事，難道是他被人盯上了？...
    "Chuyện gì thế này, chẳng lẽ anh bị người ta nhắm vào rồi sao? Không thể nào, anh rõ ràng đã vào viện điều trị bằng phương thức hợp lý nhất rồi mà.",

    # 5: 婁禧陽分析著幾種可能的情況...
    "Lâu Hỉ Dương phân tích vài tình huống khả dĩ, cố gắng tìm ra đầu mối xuất hiện sai sót, nhưng hoàn toàn chẳng có manh mối nào.",

    # 6: “不好意思1121床...”
    "“Thật ngại quá giường 1121, nhằm đảm bảo an toàn cho bệnh nhân trong thời gian nằm viện, chúng tôi bắt buộc phải phân công hộ lý cho cậu.” Bác sĩ kiểm tra phòng mặt không đổi sắc, dùng khẩu khí không cho phép từ chối gạt đi lời anh.",

    # 7: 緊接著，他朝身後的護工遞了個眼色...
    "Ngay sau đó, ông ta đưa mắt ra hiệu với người hộ lý phía sau. Người hộ lý hiểu ý, cúi gầm đầu bước tới bên giường Lâu Hỉ Dương, giúp anh chỉnh lại bình truyền dịch.",

    # 8: 醫生又囑咐了幾句...
    "Bác sĩ lại dặn dò thêm vài câu rồi quay người rời đi, để lại Lâu Hỉ Dương cùng người hộ lý quái dị kia mắt to trừng mắt nhỏ.",

    # 9: 那護工像是新來的...
    "Người hộ lý kia giống như nhân viên mới đến, một chuỗi quy trình làm việc vụng về vô cùng, điều chỉnh xong tốc độ truyền dịch liền ngồi sang một bên không nói một lời.",

    # 10: 婁禧陽覺得氣氛挺難受的...
    "Lâu Hỉ Dương cảm thấy bầu không khí khá ngột ngạt khó chịu, liền nghiêng đầu nhìn sang, phát hiện toàn bộ khuôn mặt của đối phương đều bị mặt nạ phòng hộ che chắn kín mít không lọt một khe hở.",

    # 11: “你這麽帶著不悶？...”
    "“Cậu đeo thế này không thấy bí bách sao? Tôi chỉ bị thương ngoài da thôi, không có bệnh truyền nhiễm đâu.” Môi trường viện điều trị ở Paradise rất tốt, bên trong còn bật lò sưởi, Lâu Hỉ Dương chỉ nghĩ thôi cũng thấy nóng nực.",

    # 12: 這個人肯定有問題。
    "Người này chắc chắn có vấn đề.",

    # 13: 他不動聲色地試探眼前的人...
    "Anh bất động thanh sắc thăm dò người trước mặt, người nọ nghe vậy chỉ khựng lại một thoáng, cũng không nói lời nào, lắc đầu lia lịa thật nhanh.",

    # 14: “難道你要一直坐在這盯著我？”...
    "“Chẳng lẽ cậu định ngồi đây nhìn chằm chằm tôi suốt sao?” Lâu Hỉ Dương khẽ nhíu mày, nhận ra tình hình hiện tại chẳng mấy khả quan.",

    # 15: 一直盯著他，他要怎麽去找他媽。
    "Cứ nhìn chằm chằm vào anh thế này thì anh làm sao đi tìm mẹ mình được.",

    # 16: 那人點點頭，又搖了搖頭...
    "Người nọ gật gật đầu, rồi lại lắc lắc đầu, cuối cùng trịnh trọng gật đầu hai cái, trông ngoan ngoãn một cách kỳ dị, khiến áp lực của Lâu Hỉ Dương tăng lên gấp bội.",

    # 17: 他吐了口氣，躺倒在枕頭上...
    "Anh thở hắt ra một hơi, nằm ngửa trên gối, nhìn lên trần nhà chẳng biết đang nghĩ ngợi điều gì.",

    # 18: 他打開終端...
    "Anh mở thiết bị đầu cuối ra, trước tiên gọi vài cuộc gọi video cho Dịch Duyên nhưng đều không có ai bắt máy, sau đó lại nhắn tin cho Lâu An Minh, đơn giản kể lại tình hình cho ông hay.",

    # 19: 婁安明此刻正和R一起整理埋在paradise的暗線...
    "Lâu An Minh lúc này đang cùng R chỉnh lý các đường dây ngầm cài cắm ở Paradise, gần như không dứt ra được thời gian để nói chuyện với anh. Thấy đối phương mãi không có động tĩnh gì, Lâu Hỉ Dương bèn tắt thiết bị đầu cuối, định bụng ngủ một giấc.",

    # 20: 昨晚他一整夜都沒合眼。
    "Đêm qua anh thức trắng cả đêm không hề chợp mắt.",

    # 21: 閉眼前他看了一眼護工...
    "Trước khi nhắm mắt anh liếc nhìn người hộ lý một cái, phát hiện đối phương đang chăm chú nhìn chằm chằm vào mình—— chính xác là vùng bụng eo của anh.",

    # 22: 不明白這人倒底是為了什麽，婁禧陽沒去深究，合眼睡了過去。
    "Không hiểu người này rốt cuộc là có mục đích gì, Lâu Hỉ Dương cũng không truy cứu sâu xa, khép mắt ngủ thiếp đi.",

    # 23: …
    "……",

    # 24: 他是被一陣激烈的爭吵聲吵醒的...
    "Anh bị đánh thức bởi một tràng cãi vã kịch liệt. Vừa mở mắt ra, đập vào mắt là cả một đám người đông nghịt đen ngòm.",

    # 25: 那群人被那護工堵在門口...
    "Đám người kia bị người hộ lý chặn lại ở cửa. Nhìn qua bờ vai của hộ lý, anh lờ mờ nhìn thấy một khuôn mặt quen thuộc.",

    # 26: “張森澤？”婁禧陽抬了抬眉，喊出了聲。
    "“Trương Sâm Trạch?” Lâu Hỉ Dương khẽ nhướng mày, cất tiếng gọi.",

    # 27: 護工聽他醒了，後背一僵，緩緩地轉過頭來看了他一眼。
    "Người hộ lý nghe thấy anh đã tỉnh, sống lưng cứng đờ, chậm rãi quay đầu lại nhìn anh một cái.",

    # 28: 不知道是不是婁禧陽的錯覺，他總覺得那一眼像是告狀的委屈。
    "Chẳng biết có phải là ảo giác của Lâu Hỉ Dương hay không, anh cứ cảm thấy ánh mắt kia tựa như đang tủi thân mách tội vậy.",

    # 29: “陽陽！”
    "“Dương Dương!”",

    # 30: 聽到婁禧陽叫他，張森澤那張邪肆的臉瞬間亮了起來，巴巴地朝他揮手。
    "Nghe thấy Lâu Hỉ Dương gọi mình, khuôn mặt tà mị ngông nghênh của Trương Sâm Trạch lập tức sáng bừng lên, tha thiết vẫy tay với anh.",

    # 31: “你這請的什麽傻子護工，說啥都不讓我進去，有病是不咯？”
    "“Cậu thuê cái tên hộ lý ngốc nghếch gì thế này, nói thế nào cũng không cho tôi vào, bị bệnh đấy à?”",

    # 32: 張森澤惡狠狠地瞪了眼護工...
    "Trương Sâm Trạch hung dữ lườm người hộ lý một cái, đẩy cậu ta ra định bước vào trong, chẳng ngờ lệ khí trên người hộ lý này lớn đến đáng kinh ngạc, lại dùng bả vai húc ngược gã trở lại.",

    # 33: “嘿你奶奶的，蹬鼻子上臉了？”...
    "“Mẹ kiếp nhà mày, được đằng chân lân đằng đầu đấy à?” Sắc mặt Trương Sâm Trạch đen sì, giơ tay toan vung thẳng vào mặt người hộ lý.",

    # 34: “別鬧了。”婁禧陽冷冷出聲...
    "“Đừng quậy nữa.” Lâu Hỉ Dương lạnh lùng lên tiếng, “Người của cậu đông quá, đừng làm ảnh hưởng đến người khác, một mình cậu vào đây thôi.”",

    # 35: 張森澤忿忿地收回手...
    "Trương Sâm Trạch bực bội thu tay về, giơ tay phất phất ra phía sau, lướt qua vai người hộ lý bước vào trong.",

    # 36: 護工則是毫不留情地把門關上了...
    "Người hộ lý thì không chút lưu tình đóng sập cửa lại, nhốt cả đám vệ sĩ ở bên ngoài, im lặng quay trở lại đầu giường của Lâu Hỉ Dương, ngồi xuống nhìn chằm chằm Trương Sâm Trạch với vẻ u ám.",

    # 37: 婁禧陽將他的舉動看在眼中...
    "Lâu Hỉ Dương thu trọn hành động của cậu vào mắt, thầm nghĩ người này rốt cuộc có mục đích gì, nếu chỉ phụ trách giám sát anh thì tại sao lại có ác ý lớn đến thế đối với Trương Sâm Trạch.",

    # 38: 清了清嗓子，他對護工道...
    "Hắng giọng một cái, anh nói với người hộ lý: “Xin lỗi, tôi và vị tiên sinh này có chút chuyện riêng cần nói, có thể phiền cậu ra ngoài một chút được không?”",

    # 39: 似乎是沒想到婁禧陽會讓他出去...
    "Dường như không ngờ Lâu Hỉ Dương lại bảo mình ra ngoài, trong mắt người hộ lý hiện lên một mảng mờ mịt. Cậu nhìn Lâu Hỉ Dương, lí nhí nói: “Anh đang ngủ, tôi mới không cho hắn vào.”",

    # 40: 這個聲音很別扭，沙沙的...
    "Giọng nói này rất gượng gạo, khàn khàn, tựa như bị lăn qua một lớp sỏi cát. Lâu Hỉ Dương theo bản năng nhận ra đối phương có thể đang đổi giọng ngụy tạo âm thanh, một lúc sau mới chậm chạp vỡ lẽ—— người này... là đang giải thích với anh sao?",

    # 41: “嗯，我知道，”婁禧陽意味深長地打量了他一眼...
    "“Ừ, tôi biết rồi,” Lâu Hỉ Dương đánh giá cậu một cái đầy ẩn ý, quay đầu đi, “Vẫn làm phiền cậu ra ngoài một lát nhé.”",

    # 42: 那護工猛地站起身來...
    "Người hộ lý nọ đột ngột đứng bật dậy, liếc xéo Trương Sâm Trạch một nhát sắc lẹm, rảo bước nhanh chóng ra khỏi phòng bệnh. Nhìn từ động tác có thể thấy tràn ngập vẻ bất mãn và bực bội.",

    # 43: “什麽人哇…”張森澤癟著嘴角，對著婁禧陽嘖嘖感歎。
    "“Cái loại người gì không biết...” Trương Sâm Trạch bĩu môi, hướng về phía Lâu Hỉ Dương chậc chậc cảm thán.",

    # 44: “我收到婁叔的消息...”
    "“Tôi nhận được tin của chú Lâu, biết cậu đang ở viện điều trị này. Cậu làm tôi tức chết đi được, rõ ràng trước kia tôi mời cậu mà cậu chẳng thèm ngó ngàng tới tôi.” Trương Sâm Trạch vỗ vỗ lên mặt giường, trút bỏ nỗi bất mãn trong lòng.",

    # 45: 張森澤的父親和婁安明關系匪淺...
    "Cha của Trương Sâm Trạch và Lâu An Minh quan hệ không hề tầm thường, chỉ bằng việc biết Lâu An Minh bị giam ở viện nghiên cứu Tây Lăng Sơn là có thể nhận ra đôi phần, cho nên Trương Sâm Trạch có được tin tức của anh cũng chẳng có gì lạ.",

    # 46: 婁禧陽自知理虧...
    "Lâu Hỉ Dương tự biết mình đuối lý, bèn mỉm cười với Trương Sâm Trạch. Trương Sâm Trạch ngẩn ngơ một thoáng, cơn giận lập tức tan biến sạch sành sanh.",

    # 47: “靠，你就會對我使這招...”
    "“Mẹ kiếp, cậu chỉ giỏi dùng chiêu này với tôi thôi, cậu có biết nụ cười của cậu đẹp đến mức nào không hả.”",

    # 48: 好看，想親，張森澤暗暗想到...
    "Đẹp, muốn hôn quá, Trương Sâm Trạch thầm nghĩ, nhưng giây tiếp theo liền đè nén cơn xao động vừa nhú lên xuống.",

    # 49: 他可沒忘記幾年前的那件事。
    "Gã không hề quên chuyện xảy ra mấy năm trước.",

    # 50: 那個時候他情竇初開...
    "Khi ấy gã mới biết rung động đầu đời, lúc Lâu Hỉ Dương cười với gã liền không kìm lòng được, nhào tới toan cưỡng hôn anh, kết quả bị anh đánh cho mặt mũi bầm dập tím tái, còn nhận được một lời cảnh cáo tuyệt giao, trực tiếp chiến tranh lạnh cho đến tận lần gặp mặt trước mới kết thúc.",

    # 51: 如果不想失去婁禧陽，他必須老老實實以發小的身份待在他身邊。
    "Nếu không muốn mất đi Lâu Hỉ Dương, gã bắt buộc phải an phận thủ thường ở bên cạnh anh với thân phận bạn nối khố.",

    # 52: 注意到婁禧陽腰腹上的傷...
    "Chú ý tới vết thương nơi bụng eo Lâu Hỉ Dương, sắc mặt Trương Sâm Trạch trầm xuống, tức giận nói: “Là kẻ đui mù nào đánh cậu ra nông nỗi này? Ông đây nhất định bắt nó phải quỳ xuống xin lỗi cậu!”",

    # 53: “沒有誰，你別去。”...
    "“Không có ai cả, cậu đừng đi.” Lâu Hỉ Dương có chút bất lực, “Tôi và ba tôi hiện tại là thân phận gì? Càng khiêm tốn kín tiếng càng tốt, đừng làm lớn chuyện ra.”",

    # 54: 張森澤也不是傻的...
    "Trương Sâm Trạch cũng không phải kẻ ngốc, lời nói lúc giận thì nói thế thôi. Gã hậm hực thở hắt ra một hơi, ngồi phịch xuống giường.",

    # 55: “問你件事。”婁禧陽隔著被子踹了他一腳...
    "“Hỏi cậu chuyện này.” Lâu Hỉ Dương cách lớp chăn đá gã một cái, “Cậu có tin tức gì về Trưởng quan Đoàn Tình báo Liên bang không?”",

    # 56: “情報團？那不是蔣卓航的親信嗎...”
    "“Đoàn Tình báo á? Đó chẳng phải tâm phúc của Tưởng Trác Hàng sao, tôi làm gì có, nhưng ông già nhà tôi đoán chừng biết được chút ít đấy, lát nữa tôi hỏi giúp cậu.” Trương Sâm Trạch ngẫm nghĩ rồi xua tay phủ nhận.",

    # 57: 聯邦情報團行事謹慎隱秘...
    "Đoàn Tình báo Liên bang hành sự cẩn trọng bí mật, xưa nay chỉ nghe lệnh một mình Tưởng Trác Hàng. Kể từ khi Tưởng Trác Hàng và Lâu An Minh chính thức trở mặt xé toạc quan hệ, thế lực hai bên liền như nước với lửa.",

    # 58: 想必對方對婁安明一方勢力多有防備...
    "Chắc hẳn đối phương rất đề phòng thế lực bên phía Lâu An Minh, khả năng Trương Sâm Trạch lấy được tin tức hữu ích là vô cùng nhỏ bé.",

    # 59: 只可惜上輩子他沒有多留意陳斂這個人。
    "Chỉ tiếc là kiếp trước anh không để ý nhiều đến nhân vật Trần Liễm này.",

    # 60: 婁禧陽按了按眉間，想著該從哪裡入手。
    "Lâu Hỉ Dương day day ấn đường, nghĩ ngợi nên bắt đầu ra tay từ đâu.",

    # 61: “嘿，陽陽，怎麽只有你一個人呢...”
    "“Này, Dương Dương, sao chỉ có một mình cậu thế, cậu em trai hàng xóm của cậu không tới thăm cậu à?” Trương Sâm Trạch chẳng biết đang nghĩ gì, đôi mắt đảo liên hồi.",

    # 62: “他…”婁禧陽怔愣了一瞬，一時間竟卡了殼。
    "“Cậu ấy...” Lâu Hỉ Dương ngẩn người trong thoáng chốc, nhất thời lại nghẹn lời.",

    # 63: 這被張森澤捕捉到了...
    "Điều này bị Trương Sâm Trạch bắt trọn, gã hướng ánh mắt về phía anh, tâm trạng trở nên vui vẻ hẳn lên: “Cậu ta không cùng cậu tới Paradise đúng không.”",

    # 64: “這很好，陽陽，他不應該待在你身邊。”
    "“Thế thì tốt quá, Dương Dương, cậu ta không nên ở bên cạnh cậu.”",

    # 65: 張森澤抬起手捋了捋過長的頭髮，發絲在他指尖流動。
    "Trương Sâm Trạch giơ tay vuốt lại mái tóc hơi dài, lọn tóc lướt qua đầu ngón tay gã.",

    # 66: 想起那天在過道上看到的那一幕，他的指節泛起了白，
    "Nhớ lại cảnh tượng nhìn thấy ở lối đi ngày hôm đó, đốt ngón tay gã trắng bệch ra:",

    # 67: “他很危險，而且，他和我一樣。”
    "“Cậu ta rất nguy hiểm, hơn nữa, cậu ta cũng giống như tôi.”",

    # 68: 一樣喜歡你。
    "Cũng thích cậu như tôi.",

    # 69: 張森澤沒有將後面的話說出來，但他知道婁禧陽明白他的意思。
    "Trương Sâm Trạch không nói vế sau ra miệng, nhưng gã biết Lâu Hỉ Dương hiểu ý gã.",

    # 70: 婁禧陽緩緩收斂起臉上的表情...
    "Lâu Hỉ Dương chậm rãi thu lại vẻ mặt, rút chân trong chăn về: “Trước kia đã nói với cậu rồi, tôi không thích đàn ông.”",

    # 71: “他現在出了點事...”
    "“Hiện tại cậu ấy gặp chút chuyện, nhưng sau này tôi vẫn sẽ mang cậu ấy theo bên mình. Cậu ấy là do một tay tôi nuôi lớn, tôi tự có chừng mực.”",

    # 72: “是嗎？”張森澤直勾勾地看著他...
    "“Thế sao?” Trương Sâm Trạch nhìn chằm chằm vào anh, như muốn đào bới điều gì từ trong mắt anh, “Cậu có biết không Dương Dương, vừa rồi cậu đã khựng lại, từ nhỏ đến lớn, cậu chỉ khi nói dối tôi mới như vậy thôi.”",

    # 73: 婁禧陽看著他，抿直了唇，“沒有，沒有騙你。”
    "Lâu Hỉ Dương nhìn gã, mím chặt môi: “Không có, không lừa cậu.”",

    # 74: 張森澤嘴邊浮出一絲苦澀，收回視線，轉頭望向了門外。
    "Khóe miệng Trương Sâm Trạch dâng lên một tia cay đắng, thu hồi tầm mắt, quay đầu nhìn ra ngoài cửa.",

    # 75: 良久，他站起身來向外走去...
    "Hồi lâu sau, gã đứng dậy bước ra ngoài, vừa đi vừa vẫy vẫy tay với anh: “Tôi đi đây, có việc thì gọi tôi.”",

    # 76: “嗯。”婁禧陽應了一聲...
    "“Ừ.” Lâu Hỉ Dương đáp một tiếng, nhìn gã đóng cửa lại, rồi lại nghe tiếng bước chân của cả đám người đi xa dần, cuối cùng biến mất hẳn.",

    # 77: 他等了一會兒，並沒有等到那個護工進來。
    "Anh đợi một lát, nhưng không thấy người hộ lý kia bước vào.",

    # 78: 又過去了半小時，還是沒有人進來。
    "Lại trôi qua nửa tiếng nữa, vẫn không có ai đi vào.",

    # 79: 婁禧陽若有所思地看了眼門外...
    "Lâu Hỉ Dương như có điều suy nghĩ liếc nhìn ra ngoài cửa, phát hiện đối phương cũng không phải lúc nào cũng nhìn chằm chằm anh cả ngày. Như vậy, anh có thể nhân khoảng trống này lẻn ra ngoài.",

    # 80: 想到這裡，婁禧陽一手拔掉針頭，穿上鞋走出了病房。
    "Nghĩ đến đây, Lâu Hỉ Dương một tay giật phăng kim truyền dịch, xỏ giày bước ra khỏi phòng bệnh.",

    # 81: *
    "*",

    # 82: 婁禧陽快速地將整個治療所走了一遍...
    "Lâu Hỉ Dương nhanh chóng đi dạo khắp toàn bộ viện điều trị một lượt. Viện điều trị có tổng cộng mười tầng lầu, nhưng Lâu Hỉ Dương ước lượng chiều cao của nó, nó không chỉ có mười tầng, ít nhất có từ hai tầng trở lên không được công khai.",

    # 83: 那麽最有可能藏東西的地方就是頂樓沒開放的那幾層。
    "Vậy thì nơi có khả năng giấu đồ nhất chính là mấy tầng trên cùng chưa được mở kia.",

    # 84: 婁禧陽猜想或許有一架隱藏的電梯可以通往樓頂，但他還沒找到。
    "Lâu Hỉ Dương đoán có lẽ có một thang máy bí mật dẫn lên tầng thượng, nhưng anh vẫn chưa tìm ra.",

    # 85: 回到病房的時候，護工已經坐在他的床頭了。
    "Lúc trở về phòng bệnh, người hộ lý đã ngồi ở đầu giường của anh rồi.",

    # 86: “你去了哪裡？”他站起身來...
    "“Anh đã đi đâu?” Cậu đứng dậy, trên tay vẫn còn nắm chặt chiếc kim tiêm bị giật ra, dùng giọng điệu chất vấn hỏi anh.",

    # 87: 這個眼線太業余...
    "Tai mắt này quá đỗi nghiệp dư, mọi cử chỉ hành động đều sơ hở trăm bề, nhưng Lâu Hỉ Dương vẫn phối hợp diễn kịch cùng cậu.",

    # 88: “去散散步，裡面太悶了。”...
    "“Đi dạo một chút, trong phòng ngột ngạt quá.” Anh ôm bụng dưới đi tới mép giường, ném áo khoác lên giường, “Tôi đi vệ sinh một lát.”",

    # 89: 說完他轉身朝病房裡配備的衛生間裡走去...
    "Nói xong anh xoay người đi về phía nhà vệ sinh trong phòng bệnh, còn chưa đi được mấy bước thì người hộ lý kia đã thoắt cái lao tới trước mặt anh, một tay bám lấy cánh tay anh.",

    # 90: “讓我來幫你，先生。”
    "“Để tôi giúp anh, thưa tiên sinh.”",

    # 91: 婁禧陽：我有分寸。
    "Lâu Hỉ Dương: Tôi tự có chừng mực.",

    # 92: 謝謝小天使的營養液～
    "Cảm ơn dung dịch dinh dưỡng của thiên sứ nhỏ ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_016 translation written: {len(paragraphs)} paragraphs.")
