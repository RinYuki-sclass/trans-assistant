# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_019"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 19: Đưa cậu ấy đi
---""",

    # 1: separator
    "================",

    # 2: 婁禧陽沉默地跟在護工的身後。
    "Lâu Hỉ Dương im lặng đi theo sau lưng người hộ lý.",

    # 3: 護工拽著他的手臂，帶著他回到了自己的病房。
    "Người hộ lý kéo cánh tay anh, dẫn anh quay trở về phòng bệnh của mình.",

    # 4: 他腦子裡還想著剛才的情境...
    "Trong đầu anh vẫn còn nghĩ tới cảnh tượng ban nãy, anh không hiểu việc người hộ lý này xuất hiện ở nơi đó mang ý nghĩa gì.",

    # 5: “你到底是什麽人。”...
    "“Rốt cuộc cậu là ai.” Lâu Hỉ Dương một tay đóng sầm cửa lại, áp sát người ép chặt người hộ lý trước mặt lên cánh cửa.",

    # 6: 嚴密的防護面罩近在咫尺...
    "Chiếc mặt nạ phòng hộ kín mít ở ngay trước mắt, cách một lớp màng mỏng màu xanh lam, anh chỉ có thể nhìn thấy một đôi mắt với đường nét mơ hồ, đang bất động nhìn chằm chằm vào anh.",

    # 7: 護工的呼吸有些急促...
    "Hơi thở của người hộ lý có chút dồn dập, anh có thể cảm nhận rõ ràng lồng ngực phập phồng trước mặt.",

    # 8: “你呢，你又在做些什麽！？...”
    "“Còn anh thì sao, anh lại đang làm cái gì thế hả?!” Dùng chất giọng khàn khàn ngụy tạo âm thanh, người hộ lý gay gắt chất vấn ngược lại, “Anh có biết không, nếu lúc đó tôi không có ở đó thì anh đã chết rồi!”",

    # 9: 護工言語激動...
    "Người hộ lý lời lẽ kích động, muốn giãy giụa thoát khỏi cánh tay đang đè trên vai mình, lại bị Lâu Hỉ Dương dùng lực mạnh hơn ấn ngược trở lại.",

    # 10: “我再問你一次，回答我，你是什麽人。”...
    "“Tôi hỏi cậu một lần nữa, trả lời tôi, cậu là ai.” Lâu Hỉ Dương trầm giọng xuống, đột ngột rút ngắn khoảng cách giữa hai khuôn mặt, đôi mắt hơi híp lại ẩn chứa sát khí khiến người ta khiếp sợ, “Ai phái cậu tới? Giám sát tôi, đúng không?”",

    # 11: “不是…我不是…”...
    "“Không phải... Tôi không phải...” Người hộ lý bị khí thế của anh trấn áp, bàn tay đang xô đẩy bất giác mềm nhũn lực đạo, như có như không chống lên trước ngực Lâu Hỉ Dương.",

    # 12: “聽著，我不管你是蔣卓航還是他身邊那條狗派來的...”
    "“Nghe đây, tôi không cần biết cậu là do Tưởng Trác Hàng hay là con chó bên cạnh hắn phái tới, hiện tại cậu chỉ có hai lựa chọn,” Lâu Hỉ Dương siết chặt lực đạo dưới tay, “Phối hợp với tôi, hoặc là hôn mê nửa năm.”",

    # 13: “聯邦黑市流傳的禁藥...”
    "“Thuốc cấm lưu truyền trên chợ đen Liên bang, tôi chỉ cần một câu nói là lấy được. Cậu không cần lo lắng, tôi sẽ không để cậu chết, sau khi cậu hôn mê tôi sẽ đặt cậu vào khoang ngủ.”",

    # 14: 婁禧陽說著就抬起了手臂，欲要先將他劈暈過去。
    "Lâu Hỉ Dương vừa nói vừa giơ cánh tay lên, toan đánh ngất đối phương trước.",

    # 15: “等等！”護工連忙偏頭，下意識地——摟住了他的腰。
    "“Chờ đã!” Người hộ lý vội vàng nghiêng đầu, theo bản năng—— ôm chầm lấy eo anh.",

    # 16: “我配合你，你想知道什麽？”...
    "“Tôi phối hợp với anh, anh muốn biết cái gì?” Người hộ lý vùi đầu vào lòng anh, nghẹn ngào nói.",

    # 17: 婁禧陽低頭看他...
    "Lâu Hỉ Dương cúi đầu nhìn cậu, ngẩn người một thoáng mới nhớ ra phải kéo cậu ra: “Tại sao cậu lại ở nơi ban nãy, nơi đó cất giấu bí mật gì?”",

    # 18: “一個秘密實驗基地，我是…那裡的的人。”...
    "“Một căn cứ thí nghiệm bí mật, tôi là... Người của nơi đó.” Người hộ lý ngẩng đầu lên, chậm rãi nói.",

    # 19: 婁禧陽揣摩著護工話裡的真假...
    "Lâu Hỉ Dương nghiền ngẫm độ thật giả trong lời nói của người hộ lý, rõ ràng có rất nhiều mối nghi ngờ đối với câu trả lời đơn giản này.",

    # 20: “是不是關著一個女人？”他快速追問。
    "“Có phải giam giữ một người phụ nữ không?” Anh dồn dập truy hỏi.",

    # 21: 護工聞言一愣，隨即搖了搖頭“沒有。”
    "Người hộ lý nghe vậy ngẩn ra, ngay sau đó lắc lắc đầu: “Không có.”",

    # 22: 聽到回答，婁禧陽徹底失去了耐心...
    "Nghe được câu trả lời, Lâu Hỉ Dương hoàn toàn mất hết kiên nhẫn. Anh cười khẩy một tiếng, bàn tay to lớn siết lấy chiếc cổ thon dài của người nọ, ngón tay nguy hiểm miết lên động mạch cổ: “Được rồi, tôi không rảnh ở đây đóng kịch với cậu, đã không chịu phối hợp thì ngoan ngoãn ngủ một giấc đi.”",

    # 23: “我沒騙你，真的沒有什麽女人...”
    "“Tôi không lừa anh, thực sự không có người phụ nữ nào cả, tôi chưa từng nhìn thấy bao giờ!” Ngón tay người hộ lý bấu vào mu bàn tay anh, cố gắng giải thích với anh.",

    # 24: 婁禧陽思索了幾秒，緩緩放下了手。
    "Lâu Hỉ Dương ngẫm nghĩ vài giây, chậm rãi buông tay xuống.",

    # 25: “把你的防護面罩摘了。”...
    "“Tháo mặt nạ phòng hộ của cậu xuống.” Anh dùng giọng điệu không cho phép cự tuyệt ra lệnh, “Mặt cũng không lộ, làm sao tôi tin cậu được?”",

    # 26: 這分明是最簡單的要求...
    "Đây rõ ràng là yêu cầu đơn giản nhất, nhưng người trước mặt lại bỗng chốc căng cứng cả người, tựa như một chú mèo sắp sửa xù lông.",

    # 27: “不行，不能摘，真的不行！”...
    "“Không được, không thể tháo, thực sự không được!” Người hộ lý đột nhiên vùng vẫy kịch liệt trong sự kìm kẹp của anh, muốn chạy trốn ra ngoài.",

    # 28: 婁禧陽見狀力度不減反增，死死地將他控制在身下。
    "Lâu Hỉ Dương thấy vậy lực đạo chẳng những không giảm mà càng tăng thêm, gắt gao khống chế cậu dưới thân mình.",

    # 29: 這太反常了。
    "Chuyện này quá đỗi bất thường.",

    # 30: 他眼底一沉...
    "Ánh mắt anh trầm xuống, giơ tay toan chộp lấy khuôn mặt của người hộ lý, thế nhưng ngón tay anh còn chưa chạm vào mặt nạ thì đã bị người hộ lý “bốp” một tiếng đánh bật trở lại.",

    # 31: 很強的力道，沒有底子的人絕對做不到。
    "Lực đạo rất mạnh, người không có nền tảng tuyệt đối không thể làm được.",

    # 32: 護工像是被逼到了極點...
    "Người hộ lý dường như bị dồn tới bước đường cùng, không còn vẻ ngoan ngoãn bình lặng như ban nãy nữa. Cùi chỏ của cậu như cuồng phong thúc thẳng về phía đầu vai anh, đồng thời giơ đầu gối húc mạnh vào đùi trong của anh.",

    # 33: 面對突然爆發的攻擊...
    "Đối mặt với đòn tấn công bộc phát bất thình lình, Lâu Hỉ Dương cũng động chân thật. Anh nghiêng người né tránh đòn tập kích của hộ lý, ngay khoảnh khắc đối phương chớp lấy khe hở định thoát thân liền nhanh tay tóm chặt lấy cổ tay cậu, một cú quật qua vai quật ngã người xuống mặt đất, đè chặt người dưới thân.",

    # 34: 護工的呼吸更加紊亂了...
    "Hơi thở của người hộ lý càng thêm hỗn loạn, toàn thân cậu bắt đầu run rẩy bần bật. Ngón tay Lâu Hỉ Dương đang ấn trên cổ tay cậu dần phát hiện ra mạch đập của đối phương ngày một rối loạn bất thường.",

    # 35: “喂，你怎麽了？”婁禧陽皺起眉，拍了拍護工的臉。
    "“Này, cậu bị làm sao thế?” Lâu Hỉ Dương nhíu mày, vỗ vỗ lên mặt người hộ lý.",

    # 36: “痛…好痛啊…”護工軟著聲哼哼著。
    "“Đau... Đau quá...” Người hộ lý mềm nhũn giọng rên rỉ từng tiếng.",

    # 37: 見狀不對，婁禧陽從他身上撤了下來...
    "Thấy tình hình không đúng, Lâu Hỉ Dương vội rút người khỏi cậu, phát hiện giọng nói của người hộ lý yếu ớt vô cùng, tựa như sắp ngất đi tới nơi.",

    # 38: “痛？”他明明控制了力道的。
    "“Đau ư?” Anh rõ ràng đã khống chế lực đạo rồi mà.",

    # 39: 婁禧陽抄起他的腿彎，將人橫抱了起來，放在了病床上。
    "Lâu Hỉ Dương luồn tay qua khoeo chân cậu, bế ngang người lên, đặt nằm lên giường bệnh.",

    # 40: “哪裡痛？”...
    "“Đau ở đâu?” Lâu Hỉ Dương đau đầu hỏi cậu, nhưng chỉ nhận lại cái lắc đầu không ngừng của đối phương. “Để tôi xem nào.” Anh đỡ lưng người hộ lý lên, muốn kiểm tra tình hình, nhưng chiếc mặt nạ phòng hộ trên mặt cậu thực sự quá vướng víu cản trở.",

    # 41: 婁禧陽嘖了一聲...
    "Lâu Hỉ Dương chậc một tiếng, đưa tay ấn vào chốt cài bí mật trên mặt nạ: “Chỉ là lộ mặt thôi mà, đừng kích động.”",

    # 42: 護工的頭仍是僵硬著想阻止他，但此刻卻沒了反抗的力氣。
    "Đầu người hộ lý vẫn cứng đờ muốn ngăn cản anh, nhưng giờ phút này lại chẳng còn chút sức lực nào để phản kháng.",

    # 43: 婁禧陽使了點力氣，才將面罩一點點的摘了下來。
    "Lâu Hỉ Dương dùng chút lực mới từng chút từng chút tháo được chiếc mặt nạ xuống.",

    # 44: 隨著面罩的剝離...
    "Theo sự tách rời của chiếc mặt nạ, anh dần dần nhìn thấy một chiếc cằm nhỏ nhắn tinh xảo, bờ môi đỏ mọng, sống mũi cao thẳng... Cùng với đôi mắt khiến anh ngày nhớ đêm mong kia.",

    # 45: “易緣？”婁禧陽怔愣地看著那雙眼睛，連呼吸都停了好幾秒。
    "“Dịch Duyên?” Lâu Hỉ Dương ngơ ngác nhìn đôi mắt ấy, ngay cả hơi thở cũng ngừng lại suốt vài giây.",

    # 46: 他的臉上布滿了紅印和汗，都是被面罩捂出來的。
    "Trên gương mặt cậu phủ đầy những vết hằn đỏ và mồ hôi, đều do bị mặt nạ bịt kín mà thành.",

    # 47: 鴉羽似的睫毛眨了幾下，認命的閉上了眼：“陽哥，對不起，又騙你了。”
    "Hàng mi đen như lông quạ chớp chớp vài cái, cam chịu nhắm mắt lại: “Dương ca, em xin lỗi, lại lừa anh rồi.”",

    # 48: 護工是易緣。
    "Người hộ lý chính là Dịch Duyên.",

    # 49: 這個事實令婁禧陽腦子一片亂麻...
    "Sự thật này khiến đầu óc Lâu Hỉ Dương rối như tơ vò, nhưng gương mặt trong nháy mắt trắng bệch như tờ giấy của Dịch Duyên càng làm tim anh đập dồn dập như trống trận.",

    # 50: “告訴我你哪裡疼？我去叫醫生來…”...
    "“Nói cho anh biết em đau ở đâu? Anh đi gọi bác sĩ tới...” Anh hiếm khi luống cuống chân tay đến thế, đứng dậy toan bấm chuông gọi thì bị Dịch Duyên nắm chặt lấy tay.",

    # 51: “不要，不能叫醫生…很快就好了，哥哥你陪陪我。”...
    "“Đừng mà, không được gọi bác sĩ... Sẽ nhanh khỏi thôi, ca ca anh ở bên em đi.” Dịch Duyên thẳng lưng nhích lại gần anh, hơi thở nóng bỏng phả bên tai. Lâu Hỉ Dương lập tức ôm chặt lấy lưng cậu, lòng bàn tay vuốt dọc sống lưng, lặng lẽ vỗ về an ủi.",

    # 52: 他記得小時候易緣摔傷了之後，他都會這樣哄他。
    "Anh nhớ hồi nhỏ sau khi Dịch Duyên bị ngã đau, anh đều dỗ dành cậu như thế này.",

    # 53: 但易緣從來都沒有像現在一樣疼得渾身發顫。
    "Thế nhưng Dịch Duyên chưa bao giờ đau đớn đến mức toàn thân run lẩy bẩy như bây giờ.",

    # 54: 他說不出現在是什麽樣的滋味...
    "Anh không nói nên lời hiện tại là cảm giác thế nào, ngoại trừ tự trách bản thân, còn muốn lôi cái tên Trần Liễm kia ra đánh cho tàn phế, rồi bảo Dịch Duyên đánh cho mình một trận thật đau.",

    # 55: 他的手移到易緣後頸時，摸到了一塊凸出來的東西。
    "Khi tay anh di chuyển tới sau gáy Dịch Duyên, liền sờ phải một khối gồ lên.",

    # 56: 他能感覺到易緣在他懷裡抖了一下。
    "Anh có thể cảm nhận được Dịch Duyên run lên một cái trong lòng mình.",

    # 57: “別碰，疼。”易緣的唇蹭著他的肩，咬牙忍耐著。
    "“Đừng chạm vào, đau lắm.” Môi Dịch Duyên cọ vào vai anh, nghiến răng nhẫn nhịn chịu đựng.",

    # 58: 婁禧陽快速撤離，轉而揉了揉易緣的腦袋，“告訴我，那是什麽？”
    "Lâu Hỉ Dương nhanh chóng rút tay về, chuyển sang xoa xoa đầu Dịch Duyên: “Nói cho anh biết, đó là cái gì?”",

    # 59: “我後頸有塊芯片，需要把它取出來。”易緣輕聲道。
    "“Sau gáy em có một con chip, cần phải lấy nó ra.” Dịch Duyên khẽ giọng nói.",

    # 60: 這個回答婁禧陽並不意外。
    "Câu trả lời này Lâu Hỉ Dương không hề bất ngờ.",

    # 61: 他一眼就看出了這個裝置...
    "Anh liếc mắt một cái liền nhận ra thiết bị này, ở trường anh từng học qua cấu tạo của nó. Người nhân tạo trên hành tinh M không ít, nhân loại cải tạo bộ phận cơ thể nhiều vô số kể, nhưng kẻ thực sự cấy ghép chip vào trong cơ thể người thì chẳng có mấy ai.",

    # 62: 不說知道這個方法的少之又少...
    "Không nói tới việc người biết phương pháp này ít ỏi đến đáng thương, mà việc lấy chip ra cũng vô cùng khó khăn, cơ thể con người phải gánh chịu nỗi đau đớn tột cùng. Hành vi cấy chip ngoài việc che giấu bí mật ra thì chẳng có chút ý nghĩa nào.",

    # 63: “誰弄進去的，你爸媽？”...
    "“Ai cấy vào, cha mẹ em à?” Trong ngữ khí của Lâu Hỉ Dương có cơn giận dữ không thể kiềm chế nổi, cái tên khốn Dịch Thiên kia dám lấy con trai mình làm két sắt bảo hiểm, căn bản không xứng đáng làm cha của Dịch Duyên.",

    # 64: 易緣沉默了良久，才軟軟一笑...
    "Dịch Duyên trầm mặc thật lâu mới nở nụ cười mềm mại: “Em vui lắm Dương ca, chỉ có anh mới quan tâm em thôi, thích anh chết đi được.”",

    # 65: “馬上把它取下來，我帶你走。”婁禧陽聲音沉的嚇人。
    "“Lập tức tháo nó ra, anh đưa em đi.” Giọng nói Lâu Hỉ Dương trầm đến mức đáng sợ.",

    # 66: “不要，他跟我說了...”
    "“Không được, chú ấy nói với em rồi, chỉ cần lấy con chip ra thì chúng ta mới có thể sống sót, em muốn anh được sống.” Dịch Duyên cố chấp lắc đầu.",

    # 67: “他是陳斂？芯片裡面有什麽？”
    "“Chú ấy là Trần Liễm? Bên trong con chip có cái gì?”",

    # 68: 婁禧陽的手一緊...
    "Bàn tay Lâu Hỉ Dương siết chặt, đang định hỏi cho rõ ràng thì liền nghe thấy bên tai vang lên tiếng thở đều đều, Dịch Duyên đã ngủ thiếp đi rồi.",

    # 69: 他繃緊了手臂肌肉...
    "Anh gồng cứng cơ bắp cánh tay, một lúc sau mới chậm rãi và nhẹ nhàng đặt đầu Dịch Duyên trở lại trên gối.",

    # 70: 手指還被易緣緊緊地攥在手裡...
    "Ngón tay vẫn bị Dịch Duyên nắm chặt trong tay, anh tựa vào đầu giường, nhìn khuôn mặt Dịch Duyên mà chìm vào dòng hồi ức dài đằng đẵng.",

    # 71: 他記起來易天日記本上的內容...
    "Anh nhớ lại nội dung trong cuốn nhật ký của Dịch Thiên, rất dễ dàng biết được thứ giấu trong con chip trên người Dịch Duyên là gì, bên trong đó khả năng cực lớn chính là chân tướng về “khí độc”.",

    # 72: 所以說自始自終，除了他和婁安明這一派，還有人在為這件事暗相奔走。
    "Nói cách khác từ đầu đến cuối, ngoài phe phái của anh và Lâu An Minh ra, vẫn còn có người đang âm thầm bôn ba vì chuyện này.",

    # 73: 從現在來看易緣或許還不知道芯片裡真正的內容是什麽，他可能被陳斂騙了。
    "Nhìn từ hiện tại có lẽ Dịch Duyên vẫn chưa biết nội dung thực sự trong chip là gì, cậu có thể đã bị Trần Liễm lừa.",

    # 74: 最大的疑點在於陳斂這個人...
    "Điểm nghi vấn lớn nhất nằm ở nhân vật Trần Liễm này. Ông ta rõ ràng là thân tín của Tưởng Trác Hàng, nhưng lại có quan hệ sâu xa với mẹ Dịch Duyên, thậm chí sau khi hai vợ chồng gặp nạn đã phó thác tất cả cho ông ta, hy vọng mượn tay ông ta giải cứu hành tinh M.",

    # 75: 他暫且不確定陳斂的立場...
    "Anh tạm thời chưa xác định được lập trường của Trần Liễm, nhưng điều anh có thể khẳng định là kiếp trước cho đến tận phút cuối cùng anh chưa từng phát hiện Trần Liễm có hành động phản kháng Tưởng Trác Hàng nào, và Trần Liễm nhất định có thể thông qua Dịch Duyên phát hiện ra hành tung của anh.",

    # 76: 所以說現在他的一切蹤跡都被陳斂看在眼裡。
    "Có nghĩa là hiện tại mọi dấu vết của anh đều nằm gọn trong tầm mắt của Trần Liễm.",

    # 77: 無論陳斂是敵是友，他都必須快刀斬斷陳斂對他的控制。
    "Bất kể Trần Liễm là bạn hay thù, anh đều bắt buộc phải dùng đao nhanh chặt đứt sự khống chế của Trần Liễm đối với mình.",

    # 78: 思及至此，婁禧陽拿定了主意...
    "Nghĩ đến đây, Lâu Hỉ Dương đã hạ quyết tâm. Tầm mắt anh rơi trên gương mặt Dịch Duyên rồi thất thần suốt một lúc lâu.",

    # 79: 他發現自己心情非常矛盾...
    "Anh phát hiện tâm trạng mình vô cùng mâu thuẫn: anh vừa vui mừng vì Dịch Duyên có lẽ không hề muốn phản bội anh, lại vừa không đành lòng nhìn Dịch Duyên phải chịu thương tổn.",

    # 80: 如果他沒發現...
    "Nếu như anh không phát hiện ra, vậy thì Dịch Duyên sẽ giống hệt kiếp trước một mình chịu đựng nỗi đau đớn, cậu liệu có thấy rất cô đơn, có thấy rất khó chịu hay không...",

    # 81: 熟睡的易緣突然囈語了幾句...
    "Dịch Duyên đang ngủ say đột nhiên nói mớ vài câu, biểu cảm đau đớn. Trái tim Lâu Hỉ Dương thắt lại, những cảm xúc vượt khỏi lý trí ập tới ngợp trời ngợp đất.",

    # 82: md，他現在就要帶易緣走。
    "Mẹ kiếp, anh bây giờ phải mang Dịch Duyên đi ngay lập tức.",

    # 83: 其實最理智的方式是讓易緣忍耐幾天等他找到他媽再走...
    "Thực ra phương thức lý trí nhất là để Dịch Duyên nhẫn nhịn vài ngày chờ anh tìm được mẹ rồi hẵng đi, nhưng không hiểu vì sao, hễ nhìn thấy Dịch Duyên là lồng ngực anh lại chua xót nghẹn ngào, cơn nóng nảy cuồng bạo trong người đè thế nào cũng không đè xuống nổi.",

    # 84: 他從來都不對易緣以外的任何事失去理智...
    "Anh trước giờ chưa từng mất đi lý trí trước bất kỳ chuyện gì ngoài Dịch Duyên. Đúng như tất cả các giáo viên hướng dẫn từng nói, anh là bản sao của Lâu An Minh, anh cũng luôn nghĩ như vậy, nhưng khi đối diện với Dịch Duyên, anh đã dao động rồi.",

    # 85: 管他娘的，他現在隻想要把易緣身上這個鬼裝置拆掉。
    "Kệ mẹ nó đi, anh bây giờ chỉ muốn tháo cái thiết bị quỷ quái này trên người Dịch Duyên xuống.",

    # 86: 婁禧陽打開終端，撥通了張森澤的電話：“森澤，半小時把我從治療所帶出來，”
    "Lâu Hỉ Dương mở thiết bị đầu cuối, bấm gọi cho Trương Sâm Trạch: “Sâm Trạch, nửa tiếng nữa đưa tôi ra khỏi viện điều trị,”",

    # 87: 他頓了頓，繼續道：“還有，你這邊有人會拆芯片摘除裝置的嗎？”
    "Anh dừng lại một chút rồi nói tiếp: “Còn nữa, bên cậu có ai biết tháo thiết bị trích xuất chip không?”",

    # 88: 是時候讓攻“幡然悔悟”了！
    "Đã đến lúc để công “bừng tỉnh ngộ ra” rồi!",

    # 89: 謝謝小天使的營養液～
    "Cảm ơn dung dịch dinh dưỡng của thiên sứ nhỏ ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_019 translation written: {len(paragraphs)} paragraphs.")
