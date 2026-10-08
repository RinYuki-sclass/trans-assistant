# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_015"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 15: Nam hộ lý
---""",

    # 1: separator
    "================",

    # 2: “喲，新來的？”...
    "“Uầy, người mới tới à?” Gã đầu trọc cầm đầu cợt nhả huýt sáo một tiếng, đôi mắt hí ti hí xếch lên đánh giá hai người Lâu Hỉ Dương.",

    # 3: 一群人個個虎背熊腰...
    "Một đám người ai nấy đều lưng hùm vai gấu, nghiêng nghiêng bả vai sán lại trước mặt Lâu Hỉ Dương, mấy ánh mắt bắn phá quét tới quét lui trên người anh, cuối cùng dừng lại ở cổ tay anh.",

    # 4: 他們所在的地方正好是paradise一個熱鬧的街區...
    "Nơi bọn họ đang đứng vừa vặn là một khu phố náo nhiệt của Paradise. Khác với sự hoang vu lạnh lẽo ngoài thế giới bên ngoài, nơi đây khắp nơi đều là những cửa hàng sầm uất và người đi đường qua lại nườm nượp. Bọn họ ăn mặc sang trọng chỉn chu, cử chỉ giơ tay nhấc chân đều để lộ vẻ thản nhiên ung dung khác biệt hẳn so với bên ngoài.",

    # 5: 察覺到這裡的動靜...
    "Nhận thấy động tĩnh bên này, bọn họ đều ngầm hiểu ý nhau mà tản ra xung quanh, lại dừng chân ở đầu con phố cách bọn họ không xa, kín đáo dõi mắt nhìn vào trong.",

    # 6: 又是李彪他們這群人。
    "Lại là đám người Lý Bưu.",

    # 7: 成天挑釁滋事...
    "Suốt ngày gây sự kiếm chuyện, giống hệt như một bầy khổng tước lòe loẹt khoe mẽ. Nếu là trước kia, loại người này bọn họ cả đời cũng chẳng gặp nổi mấy tên.",

    # 8: 上一個新來的沒叫李彪一聲哥...
    "Người mới tới lần trước chỉ vì không gọi Lý Bưu một tiếng “anh” mà bị đám người này đánh cho phải nhập viện điều trị.",

    # 9: 據說李彪的老子是個暴發戶...
    "Nghe nói cha của Lý Bưu là một kẻ nhà giàu mới nổi, từ nhỏ gã đã hoang dã quen thói trong đoàn lính đánh thuê của gia đình, chiến trường chưa từng đặt chân lên lần nào nhưng lại tự cho là mình ghê gớm lắm. Đến ngày tận thế lại không có ai áp chế gã, cuồng vọng ngang ngược hết chỗ nói, thu nhận mấy tên đàn em du côn cướp tiền vào đây, dương oai diễu võ khắp nơi ở Paradise.",

    # 10: 新來的如果是不起眼的普通人倒還好...
    "Người mới đến nếu là kẻ bình thường không bắt mắt thì còn đỡ, nhưng nếu đụng phải hai kẻ xem chừng chẳng dễ chọc vào như ngày hôm nay thì chắc chắn sẽ đại náo long trời lở đất.",

    # 11: 他們在心裡默默歎氣...
    "Bọn họ thầm thở dài trong lòng nhưng chẳng một ai bước lên can ngăn. Ngay cả cảnh sát tinh tế đồn trú ở Paradise còn mặc kệ không quản, bọn họ thì làm được cái gì cơ chứ. Sống sót cho tốt mới là điều cấp bách nhất hiện giờ, đợi sau khi Paradise hoàn thiện thì tất cả sẽ quay trở lại quỹ đạo bình thường.",

    # 12: “老子問你們話呢，啞巴了？”
    "“Ông đây đang hỏi chuyện bọn mày đấy, câm rồi à?” Tên đầu trọc Lý Bưu thấy hai người mãi không đáp lại, bực bội xoa xoa cái đầu trọc lốc bóng lưỡng.",

    # 13: 婁禧陽抬起頭，“有事嗎？”
    "Lâu Hỉ Dương ngẩng đầu lên: “Có việc gì sao?”",

    # 14: “艸…當然有事了...”
    "“Mẹ kiếp... Đương nhiên là có việc rồi, mày còn dám nhìn ông đây kiểu đó nữa xem.” Lý Bưu vừa bị Lâu Hỉ Dương nhìn một cái, sống lưng tức khắc căng cứng. Gã hung dữ trừng trừng Lâu Hỉ Dương, không hiểu vì sao lồng ngực mình lại bắt đầu đập thình thịch dữ dội.",

    # 15: 像是預測到威脅的本能反應。
    "Tựa như phản xạ bản năng dự cảm thấy mối đe dọa.",

    # 16: 李彪身後的幾個小弟連忙拉住他...
    "Mấy tên đàn em phía sau Lý Bưu vội vàng kéo gã lại, sắc mặt chẳng mấy dễ coi.",

    # 17: 李彪沒見過什麽世面，他們卻見過...
    "Lý Bưu chưa từng va vấp sự đời mấy, nhưng bọn chúng thì từng trải rồi. Chỉ có thổ phỉ mới quấn băng vải đen trên cổ tay, đó chính là những kẻ liều mạng giết người không chớp mắt hàng thật giá thật, hoàn toàn không giống mấy kẻ cứng đầu ưa sĩ diện trước kia.",

    # 18: “拉老子幹嘛，滾！...”
    "“Kéo ông đây làm cái gì, cút! Hôm nay ông đây cũng không làm khó bọn mày, ngoan ngoãn gọi một tiếng anh thì ông đây thả cho bọn mày đi, còn nếu biết điều làm đàn em của ông thì sau này ở Paradise ông đây bảo bọc bọn mày tới cùng.” Lý Bưu gạt phăng bàn tay ngăn cản ra, từng bước áp sát về phía Lâu Hỉ Dương.",

    # 19: 李彪個頭不矮...
    "Lý Bưu vóc dáng không hề thấp, nhưng đến trước mặt Lâu Hỉ Dương lại chỉ có thể hơi ngước đầu lên, điều này khiến gã vô cùng khó chịu bực bội.",

    # 20: 婁禧陽向下睨了他一眼，懶懶道：“不好意思，以前有大師給我算過，說我命硬，克兄。”
    "Lâu Hỉ Dương liếc xéo gã từ trên xuống dưới, lười biếng nói: “Ngại quá, trước kia có đại sư từng xem bói cho tôi, nói số mệnh tôi cứng, khắc anh trai.”",

    # 21: 他話音剛落，就被身旁的婁安明壓住了手腕...
    "Anh vừa dứt lời liền bị Lâu An Minh bên cạnh đè chặt cổ tay. Lâu An Minh chỉnh lại mặt nạ cho vừa khít hơn, nén giọng khuyên anh: “Đừng phô trương.”",

    # 22: 婁禧陽不做聲，只是掠了他一眼。
    "Lâu Hỉ Dương không lên tiếng, chỉ liếc nhìn ông một cái.",

    # 23: 面前的李彪立刻就被婁禧陽的話激怒了...
    "Lý Bưu trước mặt lập tức bị câu nói của Lâu Hỉ Dương chọc giận. Lưỡi dao từ cánh tay cơ khí thò dài ra, chỉ cách yết hầu Lâu Hỉ Dương đúng một centimet.",

    # 24: 這讓後面的幾個小弟嚇得心臟都快要跳出嗓子眼兒了...
    "Cảnh tượng này làm mấy tên đàn em phía sau sợ đến mức tim muốn nhảy vọt ra ngoài cuống họng. Bọn chúng vội nhào lên ngăn cản: “Anh, anh ơi, không được đâu anh, anh quên lần trước làm ầm ĩ đến mức cảnh sát tinh tế cũng tới rồi sao, nếu không nhờ ba anh bỏ tiền chuộc anh về thì...”",

    # 25: “好了，給老子閉嘴！”...
    "“Đủ rồi, câm hết miệng lại cho ông!” Lý Bưu nhíu mày quát lớn, quay đầu trừng mắt nhìn Lâu Hỉ Dương một cái, dùng cằm hất hất về phía sau, thu lại đầu dao: “Ở đây đông người, ra con hẻm đằng kia, đừng hòng chạy thoát.”",

    # 26: 婁禧陽聳了聳肩，表示無所謂。
    "Lâu Hỉ Dương nhún vai, tỏ vẻ không sao cả.",

    # 27: 婁安明一聲不吭地將他的反應收入眼底...
    "Lâu An Minh im lặng thu trọn phản ứng của anh vào mắt, đáy mắt tràn ngập vẻ không tán thành, ông thấp giọng ra lệnh cho Lâu Hỉ Dương: “Nhân lúc này chạy mau đi.”",

    # 28: “怕什麽？我今天就是不叫，你怕就趕緊走。”
    "“Sợ cái gì? Hôm nay tôi nhất quyết không gọi đấy, ông sợ thì mau cút đi.” Lâu Hỉ Dương liếc nhìn ông một cái, đột ngột cao giọng lên khiến người xung quanh đều nghe thấy rõ mồn một.",

    # 29: 果不其然，人群中開始有動靜了。
    "Quả nhiên, trong đám đông bắt đầu có sự xao động.",

    # 30: 李彪回頭看了眼婁安明，沒想管他。
    "Lý Bưu quay đầu liếc nhìn Lâu An Minh, cũng chẳng thèm để ý tới ông.",

    # 31: 婁安明走後，婁禧陽跟著一群人進了昏暗的小巷...
    "Sau khi Lâu An Minh rời đi, Lâu Hỉ Dương đi theo đám người vào con ngõ u tối. Thấy xung quanh không còn ai, Lý Bưu nghiêng người một cái liền ép chặt Lâu Hỉ Dương lên tường: “Hỏi mày lần cuối cùng, gọi hay không gọi?”",

    # 32: “不叫。”婁禧陽放鬆了身子...
    "“Không gọi.” Lâu Hỉ Dương thả lỏng cơ thể, tựa người vào tường mượn lực: “Đánh đi.”",

    # 33: 李彪聞言一怔，隨即面容扭曲地瞪著他，像是吞了個蒼蠅似的。
    "Lý Bưu nghe vậy ngẩn ra, ngay sau đó khuôn mặt vặn vẹo trừng trừng nhìn anh, giống hệt như vừa nuốt phải một con ruồi vậy.",

    # 34: 他還沒見過上門找打的奇葩。
    "Gã chưa từng thấy kẻ kỳ dị nào tự mình tìm đến cửa đòi ăn đòn như thế này.",

    # 35: “挑釁老子？很好，你不知道連雇傭.兵都打不過老子？”
    "“Khiêu khích ông đây à? Tốt lắm, mày không biết ngay cả lính đánh thuê cũng đánh không lại ông sao?” Đáy mắt Lý Bưu lạnh tanh, siết chặt nắm đấm bên phải nện thẳng vào gò má Lâu Hỉ Dương.",

    # 36: 見婁禧陽只是偏了頭...
    "Thấy Lâu Hỉ Dương chỉ nghiêng đầu né đi, không hề có ý phản kháng, khóe môi lại như có như không nhếch lên, trong lòng Lý Bưu càng thêm nghẹn hỏa, vung nắm đấm lại giáng mạnh lên người anh.",

    # 37: 密密麻麻的拳腳打在婁禧陽身上...
    "Từng đòn quyền cước giáng dày đặc lên người Lâu Hỉ Dương. Anh nhắm nghiền mắt lại, cảm nhận nỗi đau da thịt truyền đến, tìm kiếm một đòn chí mạng vừa đúng thời cơ.",

    # 38: “噗呲——”是刀刃刺穿皮肉的聲音。
    "“Phập——” Là âm thanh lưỡi dao đâm xuyên qua da thịt.",

    # 39: 婁禧陽睜開眼...
    "Lâu Hỉ Dương mở mắt ra, nhìn thấy mũi dao nhọn trên cánh tay cơ khí của Lý Bưu từ từ rút ra khỏi bụng dưới của mình, kéo theo một vệt máu đỏ tươi.",

    # 40: 饒是不怕疼，婁禧陽還是嘶了一聲。
    "Dù cho không sợ đau, Lâu Hỉ Dương vẫn khẽ xuýt xoa một tiếng.",

    # 41: 李彪滿意地看著婁禧陽變了臉色...
    "Lý Bưu hài lòng nhìn sắc mặt Lâu Hỉ Dương biến đổi, giơ lưỡi dao dính máu quơ quơ trước mắt anh: “Hỏi mày lại lần nữa, gọi hay không?”",

    # 42: 婁禧陽虛眼看著刀尖，轉而對上了李彪發紅的雙眼，挑了一下眉
    "Lâu Hỉ Dương híp mắt nhìn mũi dao, rồi chuyển hướng nhìn thẳng vào đôi mắt đỏ ngầu của Lý Bưu, khẽ nhướng mày:",

    # 43: “到我了？”
    "“Tới lượt tôi chưa?”",

    # 44: “什——”
    "“Cái g—”",

    # 45: 李彪還沒反應過來婁禧陽的意思，就被一擊猛烈的頂撞摜到了另一側牆上。
    "Lý Bưu còn chưa kịp hiểu ý của Lâu Hỉ Dương là gì thì đã bị một đòn húc mạnh như búa bổ quật ngã sang bức tường bên kia.",

    # 46: “怎麽可能…？”怎麽可能連他出手的動作都沒看到，不可能。
    "“Làm sao có thể...?” Làm sao có thể ngay cả động tác ra tay của đối phương cũng không nhìn thấy, không thể nào.",

    # 47: 婁禧陽收回腳，向他逼近。
    "Lâu Hỉ Dương thu chân về, từng bước áp sát gã.",

    # 48: 周圍旁觀的幾個小弟已經看懵了...
    "Mấy tên đàn em đứng xem xung quanh đã đơ người ra. Bọn chúng không thể tin nổi nhìn chằm chằm Lâu Hỉ Dương, trố mắt nhìn anh một tay ôm bụng dưới máu chảy ròng ròng, một tay quăng quật tên Lý Bưu kiêu ngạo hống hách qua lại giữa hai bức tường chẳng khác nào đập một quả bóng da.",

    # 49: 意識到他們得做些什麽...
    "Ý thức được mình cần phải làm gì đó, mấy tên du côn đưa mắt nhìn nhau, nuốt nước bọt một cái rồi lao tới tập kích sau lưng Lâu Hỉ Dương——— và rồi, trong con ngõ nhỏ vang lên tiếng đập của sáu bảy quả bóng da.",

    # 50: …
    "……",

    # 51: 見情況差不多了，婁禧陽收了手...
    "Thấy tình hình hòm hòm rồi, Lâu Hỉ Dương thu tay lại. Anh quét mắt nhìn một vòng đám người nằm la liệt dưới đất, xoay người bước ra ngoài phố.",

    # 52: 他換上了一張慘白又虛弱的臉...
    "Anh thay bằng một gương mặt trắng bệch yếu ớt, bước chân lảo đảo bám vào tường đi ra ngoài phố lớn.",

    # 53: “救我……”他對圍觀的路人道。
    "“Cứu tôi……” Anh nói với người đi đường đang vây xem.",

    # 54: *
    "*",

    # 55: 婁禧陽住進了paradise唯一的重症治療所。
    "Lâu Hỉ Dương đã vào ở trong viện điều trị trọng bệnh duy nhất của Paradise.",

    # 56: paradise有兩個治療所...
    "Paradise có hai viện điều trị, một viện chỉ phụ trách chữa trị các bệnh vặt hàng ngày như cảm sốt đau đầu, viện còn lại chỉ phụ trách bệnh nặng, trang thiết bị y tế đầy đủ kèm theo khu nội trú, chỉ là điều kiện nhập viện vô cùng khắt khe để tránh lãng phí tài nguyên y tế thời mạt thế.",

    # 57: 婁禧陽成功的達到了住院要求，舒舒服服躺在了柔軟的醫床上。
    "Lâu Hỉ Dương đã thành công đạt chuẩn yêu cầu nhập viện, thoải mái nằm trên chiếc giường bệnh êm ái.",

    # 58: 這一間治療所，就是上輩子他母親被蔣卓航藏匿的地方。
    "Viện điều trị này chính là nơi kiếp trước mẹ anh bị Tưởng Trác Hàng giấu kín.",

    # 59: 一刀換一個入住資格，倒也不虧。
    "Một nhát dao đổi lấy tư cách nằm viện, tính ra cũng chẳng lỗ.",

    # 60: 婁禧陽往下躺了一躺，腹部的刀口扯了他一身冷汗。
    "Lâu Hỉ Dương nằm xuôi xuống một chút, vết dao chém ở bụng làm anh đau toát cả mồ hôi lạnh toàn thân.",

    # 61: 就是這個樣子有點太不方便。
    "Chỉ có điều bộ dạng này có chút quá đỗi bất tiện.",

    # 62: 他頭落在枕頭上...
    "Đầu anh tựa trên gối, nghiêng đầu nhìn cánh cửa phòng đóng chặt, nghĩ xem tối nay làm sao ra ngoài, lại nghĩ làm thế nào mới có thể tìm được Trần Liễm để đón Dịch Duyên trở về từ tay ông ta.",

    # 63: 望著望著，他有些晃神...
    "Nhìn mãi nhìn mãi, anh có chút xuất thần. Trong lúc ánh mắt anh còn đang lơ đãng tan rã thì cánh cửa phòng kia đột nhiên bị ai đó đẩy ra từ bên ngoài.",

    # 64: 婁禧陽抬眼看去...
    "Lâu Hỉ Dương ngước mắt nhìn sang, phát hiện là bác sĩ đi kiểm tra phòng, cùng với một người đi theo sau bịt kín mít cả khuôn mặt, nhìn dáng vẻ giống như một nam hộ lý.",

    # 65: “1121床，鑒於晚上你沒有親屬照看，治療所給你配了個護工，有事可以叫他。”
    "“Giường 1121, xét thấy buổi tối cậu không có người nhà chăm sóc, viện điều trị phân công cho cậu một hộ lý, có việc gì có thể gọi cậu ta.” Vị bác sĩ kia kiểm tra qua vết thương của Lâu Hỉ Dương một lượt, ngữ khí tùy ý gọi người phía sau bước lên.",

    # 66: 那人盯著他的腰腹移不開眼，眉眼晦暗。
    "Người nọ nhìn chằm chằm vào vùng bụng của anh không rời mắt nổi, ánh mắt tối tăm u ám.",

    # 67: 婁禧陽奇怪地看了他一眼，發現他在抬眼和他對上視線時匆忙躲開了。
    "Lâu Hỉ Dương kỳ quái liếc nhìn người nọ một cái, phát hiện người nọ khi ngước mắt chạm phải ánh nhìn của anh liền vội vã lảng tránh đi."
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_015 translation written: {len(paragraphs)} paragraphs.")
