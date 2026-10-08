# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_008"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 8: Quái vật gì thế
---""",

    # 1: separator
    "==================",

    # 2: 一場鬧劇在倍良的怒罵聲響起後結束...
    "Một màn trò hề kết thúc sau khi tiếng chửi mắng giận dữ của Bội Lương vang lên. Nhân lúc này, Lâu Hỉ Dương dẫn nhóc con không nghe lời nhà mình quay về bục sắt để dạy dỗ, đương nhiên đã bỏ lỡ những tiếng thán phục tầng tầng lớp lớp ngày một lớn hơn trên sân huấn luyện.",

    # 3: “這姓婁的小子什麽來頭啊...”
    "“Thằng nhóc họ Lâu này lai lịch thế nào vậy chứ, chỉ dựa vào mấy chiêu vừa rồi thì ai mà đánh lại được nó?”",

    # 4: “艸，還好老子沒有聽張溝的去挑釁他...”
    "“Mẹ kiếp, may mà ông đây không nghe lời Trương Câu đi khiêu khích nó, bằng không đầu cũng bị nó đánh văng mất!”",

    # 5: ……
    "……",

    # 6: 意猶未盡的幾個人在瞥到倍良難看的臉色後都息了聲...
    "Mấy gã vẫn còn chưa hết thòm thèm sau khi liếc thấy sắc mặt khó coi của Bội Lương đều nín bặt. Bọn họ dùng ngón chân cũng đoán được nguyên do Bội Lương nổi giận, chẳng qua là vì cả đám đàn ông to xác được huấn luyện nhiều năm trời lại chẳng đánh thắng nổi một đứa nhóc con.",

    # 7: 而面前的倍良火的不僅僅是這個...
    "Thế nhưng Bội Lương trước mặt nổi trận lôi đình không chỉ vì chuyện này, mà còn vì phương án huấn luyện cùng quy chế kỷ luật binh sĩ cơ giáp do Lâu Hỉ Dương gửi tới ba giây trước, phía sau bảng biểu có đính kèm một câu của Lâu Hỉ Dương:",

    # 8: [這些人欠訓，一周時間...]
    "[Đám người này còn thiếu huấn luyện, thời hạn một tuần, cứ theo quy trình trên mà làm, vừa rồi đứa nhỏ không hiểu chuyện, xin lỗi.]",

    # 9: 很不要命的練法，但一定有效。
    "Một cách luyện tập vô cùng liều mạng, nhưng nhất định sẽ có hiệu quả.",

    # 10: 倍良幾乎一眼就看出了這是一份獨創的s級訓練方案...
    "Bội Lương gần như chỉ liếc mắt một cái liền nhận ra đây là một bản phương án huấn luyện cấp S độc nhất vô nhị. Nếu như công khai nó ra ngoài, tuyệt đối sẽ dấy lên một cơn cuồng phong giữa các băng phái trên hành tinh M, thậm chí là trong quân đội Liên bang. Vậy thì, tại sao Lâu Hỉ Dương lại có thứ này?",

    # 11: 倍良頂了頂腮幫...
    "Bội Lương đưa lưỡi chống nhẹ lên má, giữa mày phủ lên một tầng u ám. Nhớ lại mấy chiêu Lâu Hỉ Dương vừa để lộ ra, gã nhận định ngay cả bản thân mình cũng chưa chắc đã đánh thắng được anh.",

    # 12: 壓下心中翻湧的疑慮...
    "Đè xuống nỗi nghi hoặc đang cuộn trào trong lòng, Bội Lương thu hồi dòng suy nghĩ, yết hầu chuyển động: “Tất cả mọi người, nghe khẩu lệnh của tôi——”",

    # 13: *
    "*",

    # 14: “哥哥，我錯了。”
    "“Ca ca, em sai rồi.”",

    # 15: “我只是想知道你這幾天都在外面做什麽...”
    "“Em chỉ muốn biết mấy ngày nay anh ở bên ngoài làm những gì thôi, em thề, chỉ có lần này là không kiềm chế được, lần sau nhất định sẽ không thế nữa.”",

    # 16: “別不理我好不好。”
    "“Đừng lơ em mà, có được không?”",

    # 17: 易緣寸步不離地跟在婁禧陽身後...
    "Dịch Duyên theo sát không rời bước sau lưng Lâu Hỉ Dương, vươn tay muốn nắm lấy tay anh nhưng lần nào cũng chỉ chậm một bước chân.",

    # 18: 婁禧陽抿著唇，也不理他...
    "Lâu Hỉ Dương mím môi, cũng không thèm để ý đến cậu, sắc mặt chẳng tính là ôn hòa. Bởi vì hiện tại sau khi đã bình tĩnh lại, anh nhận ra hai điều: một là bản tính Dịch Duyên vốn máu lạnh tàn bạo, hai là mẹ kiếp anh lại bị theo dõi rồi!",

    # 19: 三層樓高的台階總算讓他開了口...
    "Những bậc thang cao ba tầng lầu rốt cuộc cũng khiến anh mở miệng: “Xin lỗi, em sai rồi, đừng lơ em... Dịch Duyên, mỗi lần phạm lỗi em đều chỉ biết nói mấy câu này, rồi sau đó lại tiếp tục phạm phải.”",

    # 20: 坐回自己的那張破爛沙發...
    "Ngồi lại trên chiếc sô pha rách nát của mình, Lâu Hỉ Dương bình tĩnh nói với người trước mặt: “Lần trước anh đã nói với em rồi, em muốn biết cái gì thì cứ việc hỏi thẳng anh. Nếu anh bằng lòng nói cho em biết thì tự khắc sẽ nói, còn nếu anh không nói cho em biết tức là anh không muốn để em biết. Em theo dõi anh chỉ khiến anh tức giận mà thôi.”",

    # 21: 易緣似乎有些無措...
    "Dịch Duyên dường như có chút luống cuống, hai bàn tay vô thức vò vò vạt áo mình, đốt ngón tay trắng nõn bị cọ xát đến ửng đỏ: “Nhưng... nhưng em thực sự muốn biết anh đang làm gì, thế mà anh lại chẳng chịu nói cho em...”",

    # 22: 他的聲音還帶著剛才哭泣後的嗚咽...
    "Giọng nói của cậu vẫn còn vương tiếng nức nở sau trận khóc vừa rồi, đẩy vẻ đáng thương lên một tầm cao mới.",

    # 23: 婁禧陽的目光落在了那掛著淚珠的睫毛上...
    "Ánh mắt Lâu Hỉ Dương rơi vào hàng mi còn vương giọt lệ kia. Anh thở dài một hơi thật sâu, dứt khoát kéo Dịch Duyên ngồi xuống bên cạnh, sau đó mở màn hình quang học ra. Trên màn hình đang chiếu đoạn tin nhắn video của cha anh.",

    # 24: “我爸被關在西菱山研究所裡...”
    "“Ba anh bị giam ở viện nghiên cứu Tây Lăng Sơn, anh phải nghĩ cách cứu ông ấy ra, hiểu chưa?” Sau khi màn hình quang học tắt đi vài giây, Lâu Hỉ Dương mới cất lời.",

    # 25: 其實他本來並不打算告訴易緣...
    "Thật ra ban đầu anh vốn không định nói cho Dịch Duyên biết vì chẳng có gì cần thiết, nhưng tính khí Dịch Duyên quá bướng bỉnh cố chấp, nếu lần này không nói cho cậu biết thì e rằng sẽ còn có lần sau.",

    # 26: “嗯…對不起。”
    "“Vâng... Em xin lỗi.” Hiểu được chuyện này lớn đến mức nào, Dịch Duyên lập tức hối hận. Cậu thăm dò đánh giá sắc mặt Lâu Hỉ Dương, khẽ giọng nhận lỗi.",

    # 27: 下次他絕對不會再這樣了...
    "Lần sau cậu tuyệt đối sẽ không như vậy nữa, Lâu Hỉ Dương không nên phải nhẫn nhịn tính khí tùy hứng của cậu trong tình cảnh này.",

    # 28: 但婁禧陽這樣的事也願意跟他說...
    "Thế nhưng chuyện như vậy mà Lâu Hỉ Dương cũng chịu nói cho cậu biết, có phải đối với anh thì cậu là một sự tồn tại khác biệt hay không?",

    # 29: 想到這裡易緣起身跪在沙發上...
    "Nghĩ đến đây, Dịch Duyên đứng dậy quỳ trên sô pha, vòng tay ôm lấy cổ Lâu Hỉ Dương, một bàn tay nhẹ nhàng vuốt ve sau gáy anh, giọng mềm nhũn nói: “Em xin lỗi ca ca, những ngày qua anh nhất định mệt lắm rồi, Tiểu Duyên sau này sẽ không gây thêm phiền phức cho anh nữa đâu.”",

    # 30: 婁禧陽被易緣這個動作弄得渾身不自在...
    "Lâu Hỉ Dương bị động tác này của Dịch Duyên làm cho toàn thân không được tự nhiên, nhưng còn chưa kịp nghĩ thông cảm giác kỳ lạ này là gì thì đã bị một tiếng huýt sáo mang điệu bộ kỳ quặc cắt ngang.",

    # 31: 倍良靠在牆邊...
    "Bội Lương dựa vào mép tường, ánh mắt qua lại quét tới quét lui trên người hai người: “Tôi nói này, hai người vừa vừa phải phải thôi chứ, trong xưởng toàn một lũ đàn ông to xác hừng hực huyết khí, để người ta nhìn thấy thì hay ho gì.”",

    # 32: 婁禧陽將易緣扯下來...
    "Lâu Hỉ Dương kéo Dịch Duyên xuống, nhìn Bội Lương bước tới trước mặt anh.",

    # 33: 而易緣也是一頓...
    "Còn Dịch Duyên cũng khựng lại, bởi vì cậu ngửi thấy mùi nước hoa cổ long nồng nặc trên người kẻ này. Cậu cảnh giác liếc nhìn gã một cái, vừa vặn chạm phải đôi mắt như cười như không của Bội Lương.",

    # 34: 倍良倒也沒多說話的意思...
    "Bội Lương cũng chẳng có ý định nói nhiều, ngồi xuống liền tự mình tiếp tục làm công việc vừa bị gián đoạn ban nãy.",

    # 35: 婁禧陽丟了個機甲模型給易緣後也開始畫起了圖紙。
    "Lâu Hỉ Dương ném cho Dịch Duyên một mô hình cơ giáp rồi cũng bắt đầu vẽ bản vẽ thiết kế.",

    # 36: 三人逐漸形成了一個安靜的平衡狀態...
    "Ba người dần dần hình thành một trạng thái cân bằng yên tĩnh, cho đến khi chiếc nhẫn truyền tin chuyên dụng của Lloyd trên tay Bội Lương nhận được một tin nhắn, trên đó thông báo bọn họ sẽ tấn công viện nghiên cứu Tây Lăng Sơn vào một tuần sau.",

    # 37: 很顯然消息的發送者是誰...
    "Rất rõ ràng người gửi tin nhắn là ai. Bội Lương ngẩng đầu nhìn về phía Lâu Hỉ Dương, hai hàng lông mày nhăn tít lại.",

    # 38: “西陵山研究所的防衛機制接近頂級...”
    "“Cơ chế phòng vệ của viện nghiên cứu Tây Lăng Sơn gần như thuộc hàng đỉnh cấp, nếu chúng ta không phá vỡ được CPU phòng ngự của nó, chỉ dựa vào cơ giáp và một ngàn người này xông thẳng vào, cho dù may mắn cứu được người ra thì chúng ta nhiều nhất cũng chỉ còn lại một trăm người sống sót...”",

    # 39: “你說一周後進攻，沒覺得我們就是在送死嗎？”
    "“Cậu nói một tuần sau tấn công, không cảm thấy chúng ta căn bản là đang đi tìm cái chết hay sao?”",

    # 40: 聽到死這個字後易緣猛地抬起了頭...
    "Nghe thấy chữ “chết” này, Dịch Duyên chợt mạnh mẽ ngẩng đầu lên. Cậu theo bản năng nhìn về phía Lâu Hỉ Dương, đột nhiên ý thức được Lâu Hỉ Dương đang làm một việc liều mạng đến mức nào.",

    # 41: 婁禧陽波瀾不驚地按下了發送...
    "Lâu Hỉ Dương chẳng chút gợn sóng nhấn nút gửi đi, ngay sau đó Bội Lương lại nhận được một tập tài liệu. “Anh xem bản vẽ này trước đi, trong vòng năm ngày, cải tiến và nâng cấp toàn bộ cơ giáp. Thời gian hôm nay cũng hòm hòm rồi, ngày mai tôi lại đến.”",

    # 42: 他站起身，轉頭看向還坐在沙發上發呆的易緣...
    "Anh đứng dậy, quay đầu nhìn Dịch Duyên vẫn còn đang ngồi ngây người trên sô pha, vươn tay kéo cậu đứng lên: “Đi thôi, về nhà.”",

    # 43: 兩人一前一後下了樓...
    "Hai người trước sau bước xuống lầu, chỉ để lại Bội Lương nhìn bản vẽ trên màn hình quang học mà kích động đến mức mí mắt cũng run rẩy.",

    # 44: md，婁禧陽到底是什麽怪物……
    "Mẹ nó, Lâu Hỉ Dương rốt cuộc là loại quái vật gì vậy chứ……",

    # 45: *
    "*",

    # 46: 工廠的地板很粘膩...
    "Sàn nhà xưởng vô cùng dính nhớp, bên trên phủ một lớp xăng dầu đã khô. Dịch Duyên mỗi bước đi đều cảm giác như có một bàn tay đang túm lấy gót chân mình, trong đầu cậu không ngừng nghĩ tới những lời Bội Lương nói. Sau khi liên tưởng đến một khả năng nào đó, trái tim cậu bị siết chặt dữ dội.",

    # 47: 一個鐵管“咚”的一聲巨響，砸在了兩人的腳邊——
    "Một đoạn ống sắt vang lên tiếng “keng” chói tai, nện mạnh ngay bên chân hai người——",

    # 48: “婁禧陽，你憑什麽要我們一千多個兄弟為了你父親去送死？我們的命不算命，就你他媽的高貴是吧！”
    "“Lâu Hỉ Dương, mày dựa vào cái gì mà bắt hơn một ngàn anh em chúng tao phải vì cha mày mà đi tìm cái chết? Mạng của chúng tao không phải là mạng, chỉ có mày mẹ nó mới là cao quý thôi đúng không!”",

    # 49: 階梯下，不久前被易緣打得鼻青臉腫的張溝惡狠狠地望著他...
    "Dưới bậc thang, Trương Câu vừa bị Dịch Duyên đánh cho mặt mũi bầm dập cách đây không lâu đang hung tợn trừng mắt nhìn anh, cái cổ thô kệch căng phồng đỏ bừng.",

    # 50: 顯然是收到了進攻的消息...
    "Rõ ràng là đã nhận được tin tức tấn công, lối cầu thang vốn dĩ ồn ào lúc này tĩnh lặng như tờ, chỉ có tiếng thở dốc dồn dập của Trương Câu vang vọng giữa không trung.",

    # 51: 婁禧陽腳步一頓，易緣也跟著撞在了他的後背。
    "Bước chân Lâu Hỉ Dương khựng lại, Dịch Duyên đi phía sau cũng va vào lưng anh.",

    # 52: “對不起，但是必須去。”
    "“Xin lỗi, nhưng bắt buộc phải đi.” Lâu Hỉ Dương ngước mắt quét nhìn một vòng xung quanh, bình tĩnh nói.",

    # 53: 不把婁安明救出來...
    "Không cứu được Lâu An Minh ra, bọn họ sẽ không thể biết được chân tướng của ngày tận thế, những việc phía sau cũng không thể triển khai, cuối cùng người phải chết sẽ là hàng vạn sinh mạng.",

    # 54: 但是在這些人裡...
    "Thế nhưng trong số những người này, cũng sẽ có người bỏ mạng khi tấn công Tây Lăng Sơn, cái chết của họ là vì anh.",

    # 55: 易緣的余光瞥見婁禧陽的下巴緊繃...
    "Khóe mắt Dịch Duyên liếc thấy chiếc cằm Lâu Hỉ Dương căng cứng, ánh mắt rủ xuống, trong thoáng chốc thất thần.",

    # 56: 外人看婁禧陽這樣的神情或許是冷漠平淡...
    "Người ngoài nhìn vào thần sắc này của Lâu Hỉ Dương có lẽ sẽ thấy lạnh lùng hờ hững, nhưng Dịch Duyên so với bất kỳ ai đều hiểu rõ hơn, mỗi khi Lâu Hỉ Dương tự trách mình thì luôn mang bộ dạng này.",

    # 57: 他咬了咬舌尖，開口打破了長久的寂靜...
    "Cậu cắn nhẹ đầu lưỡi, mở miệng phá vỡ sự im lặng kéo dài: “Dương ca, không phải chúng ta muốn về nhà sao? Mau đi thôi.”",

    # 58: 婁禧陽嗯了一聲。
    "Lâu Hỉ Dương khẽ “ừm” một tiếng.",

    # 59: “回去？那我們呢。”
    "“Về? Thế còn chúng tao thì sao.” Trương Câu ánh mắt rực lửa trừng trừng nhìn Lâu Hỉ Dương, làm ra bộ dạng thề không chịu bỏ qua.",

    # 60: “你別以為你有個戒指就真能成我們老大了...”
    "“Mày đừng tưởng mày có một chiếc nhẫn thì thực sự có thể làm đại ca của bọn tao. Trương Câu tao cả đời này chỉ cống hiến mạng sống cho lão đại đích thực thôi. Còn cái vị lão đại này ấy à, mày hỏi thử anh em xung quanh xem, xem bọn họ nói thế nào?” Trương Câu quay đầu lại, trông thấy mọi người ai nấy đều cúi đầu im lặng, ngữ khí càng thêm lạnh lẽo.",

    # 61: “看見了沒？你婁禧陽沒資格取我們的命。”
    "“Thấy rồi chứ? Lâu Hỉ Dương mày không có tư cách lấy mạng của chúng tao.”",

    # 62: 煩死了。易緣眯著眼，用舌頭頂了頂上顎。
    "Phiền chết đi được. Dịch Duyên híp mắt, dùng đầu lưỡi chống lên vòm họng.",

    # 63: “如果你們因為我而死，在一切結束後我會為我的行為贖罪。”
    "“Nếu như các người vì tôi mà chết, sau khi tất cả mọi chuyện kết thúc, tôi sẽ vì hành vi của mình mà chuộc tội.” Giọng nói của Lâu Hỉ Dương vang lên từ bên cạnh, từng câu từng chữ rõ ràng truyền vào tai mọi người, bao gồm cả Dịch Duyên. Cậu như bị đóng đinh tại chỗ, như mất hồn mà bị Lâu Hỉ Dương kéo đi.",

    # 64: “上來。”婁禧陽開動機車...
    "“Lên đi.” Lâu Hỉ Dương khởi động mô tô bay, vỗ vỗ phía sau, ra hiệu cho Dịch Duyên đang nặng trĩu tâm sự mau lên xe. Chẳng cần Lâu Hỉ Dương nhắc bảo cậu ôm chặt lấy mình, Dịch Duyên vừa lên xe đã vô cùng tự giác vòng tay ôm lấy eo anh, áp chặt mặt vào lưng anh.",

    # 65: 機車在空中呼嘯...
    "Mô tô gầm rú giữa không trung, luồng khí lưu lao nhanh tạo thành một bức bình phong vô hình. Dịch Duyên mở hệ thống liên lạc trong mũ bảo hiểm ra, dọc đường câu được câu chăng nói chuyện với Lâu Hỉ Dương.",

    # 66: “陽哥，離末日還有十個月，我不準你現在死。”
    "“Dương ca, cách mạt thế còn mười tháng nữa, em không cho phép anh chết vào lúc này.”",

    # 67: “嗯。”
    "“Ừ.”",

    # 68: “你父親對你來說很重要嗎？”
    "“Cha của anh quan trọng với anh lắm sao?”",

    # 69: “或許吧。”
    "“Có lẽ vậy.”",

    # 70: “為什麽一定要救他？這麽多年來我從沒有聽你說過你父親找過你...”
    "“Tại sao nhất định phải cứu ông ấy? Bao nhiêu năm nay em chưa từng nghe anh nói cha anh tìm anh, hiện tại có chuyện mới nhớ tới tìm anh, cũng chẳng thấy ông ấy quan tâm xem mấy năm nay anh sống thế nào, cũng chẳng nghĩ xem một mình anh làm sao cứu ra được...”",

    # 71: “事關M星球人的生死存亡。”
    "“Liên quan đến sự sống còn của toàn bộ con người trên hành tinh M.”",

    # 72: “這很重要嗎？比你自己重要？”
    "“Chuyện đó quan trọng lắm sao? Quan trọng hơn cả bản thân anh à?”",

    # 73: 聽著易緣機關槍似的突突不停...
    "Nghe Dịch Duyên nói liên thanh như súng máy không ngừng nghỉ, Lâu Hỉ Dương bỗng nhếch khóe môi. Cảm giác được người khác quan tâm để ý quả thực rất không tệ.",

    # 74: “你怎麽不問為什麽比我自己重要？你不是什麽都得知道嗎”
    "“Sao em không hỏi tại sao lại quan trọng hơn bản thân anh? Chẳng phải chuyện gì em cũng muốn biết cho bằng được à?”",

    # 75: “我就不問！”
    "“Em không thèm hỏi đấy!” Dịch Duyên nghe xong lời nói đầy ẩn ý của Lâu Hỉ Dương, bực bội nhéo một cái vào bụng Lâu Hỉ Dương, chỉ phát hiện ngoại trừ cơ bắp cứng ngắc ra thì chẳng véo được cái gì.",

    # 76: 過了一會兒，易緣支支吾吾的哼道...
    "Một lúc sau, Dịch Duyên ấp úng hừ một tiếng: “Em đã sớm biết tại sao rồi, anh chính là một kẻ tốt bụng đến mức ngốc nghếch thiếu suy nghĩ, trước giờ luôn luôn là vậy.”",

    # 77: 婁禧陽輕笑一聲，沒回答他...
    "Lâu Hỉ Dương khẽ cười một tiếng, không trả lời cậu. Gương mặt Dịch Duyên có thể cảm nhận được lồng ngực anh đang chấn động, cánh tay ôm lấy anh càng siết chặt hơn nữa.",

    # 78: 他不會讓婁禧陽有任何危險。
    "Cậu sẽ không để Lâu Hỉ Dương gặp phải bất kỳ nguy hiểm nào.",

    # 79: 晚上，易緣看了眼熟睡的婁禧陽...
    "Buổi tối, Dịch Duyên nhìn Lâu Hỉ Dương đã ngủ say, cẩn thận từng li từng tí bước xuống giường, tự nhốt mình trong nhà vệ sinh.",

    # 80: 還沒等他打過去，陳斂的消息就來了。
    "Còn chưa đợi cậu gọi sang, tin nhắn của Trần Liễm đã gửi tới.",

    # 81: 此時，被易緣扒得一乾二淨的勞埃德：嘶…冷死我了，沒有人記得我嗎？
    "Lúc này, Lloyd bị Dịch Duyên lột sạch sành sanh: Xuýt... Lạnh chết tôi rồi, không ai còn nhớ đến tôi sao?"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_008 translation written: {len(paragraphs)} paragraphs.")
