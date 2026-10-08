# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_012"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 12: Hắn điên rồi
---""",

    # 1: separator
    "================",

    # 2: 家裡一下子空了，也沒人需要婁禧陽照顧。
    "Trong nhà bỗng chốc trống vắng, cũng chẳng còn ai cần Lâu Hỉ Dương chăm sóc nữa.",

    # 3: 既然如此，他就沒必要每天花七.八個小時在兩個地方來回折騰。
    "Đã như vậy, anh cũng không cần thiết mỗi ngày phải bỏ ra bảy tám tiếng đồng hồ đi đi lại lại giữa hai nơi.",

    # 4: 思及至此，他乾脆裝了點衣服和洗漱用品，第二天一早就去鐵廠住下了。
    "Nghĩ tới đây, anh dứt khoát thu dọn một ít quần áo và đồ dùng vệ sinh cá nhân, sáng sớm ngày hôm sau liền tới xưởng sắt ở lại.",

    # 5: 但婁禧陽明顯忽略了一個問題...
    "Thế nhưng Lâu Hỉ Dương rõ ràng đã lơ là một vấn đề, đó là anh đã sớm trở thành tiêu điểm của hơn một ngàn người bang Lloyd, nhất cử nhất động đều bị bọn họ mang ra săm soi nghiền ngẫm hết lần này đến lần khác.",

    # 6: 於是乎，萊德的一群人看他獨自提著行李住進了空蕩的單人間...
    "Thế là, một đám người của Lloyd nhìn thấy anh xách hành lý một mình dọn vào căn phòng đơn trống trải, tiếng huýt sáo và tiếng hò reo trêu chọc thi nhau vang lên không dứt.",

    # 7: 緊接著，各種話題就在廠內上下傳了個遍...
    "Ngay sau đó, đủ loại chủ đề liền lan truyền khắp trên dưới trong xưởng, từng bước từng bước trật bánh theo chiều hướng kỳ quái——",

    # 8: #婁禧陽一個人搬過來了#
    "# Lâu Hỉ Dương một mình dọn qua đây #",

    # 9: #婁禧陽慘被甩#
    "# Lâu Hỉ Dương thảm hại bị đá #",

    # 10: 事情到這還不算離譜，不知道倍良又搞出了什麽么蛾子，話題進一步發酵——
    "Chuyện tới nước này vẫn chưa tính là thái quá, chẳng biết Bội Lương lại giở trò quỷ quái gì mà chủ đề tiến thêm một bước lên men——",

    # 11: #！婁禧陽因為被老婆發現是個變態後被趕出來了！#
    "#! Lâu Hỉ Dương vì bị vợ phát hiện là kẻ biến thái nên đã bị tống cổ ra khỏi nhà! #",

    # 12: 到最後傳到婁禧陽耳裡的最終結果變成了——
    "Tới cuối cùng truyền vào tai Lâu Hỉ Dương kết quả đã biến thành——",

    # 13: #乾！婁禧陽是變態！#
    "# Đệt! Lâu Hỉ Dương là kẻ biến thái! #",

    # 14: 婁禧陽整頓好自己的東西後...
    "Lâu Hỉ Dương sau khi thu dọn xong đồ đạc của mình, lại dành ra một hai tiếng đồng hồ chải chuốt lại toàn bộ ký ức một lượt, phân tích sâu những nút thắt đã phát sinh biến động, bỗng giật mình nhận ra kiếp này chuyện gì nên xảy ra thì vẫn cứ xảy ra. Cho dù chi tiết có đôi chút biến chuyển, nhưng cuối cùng vẫn quay trở về đúng quỹ đạo cũ.",

    # 15: 那麽就意味著，盡管他再來一次，也不能順風順水地完成計劃。
    "Điều đó có nghĩa là, cho dù anh làm lại một lần nữa thì cũng không thể nào thuận buồm xuôi gió hoàn thành kế hoạch.",

    # 16: 他有些掉以輕心了。
    "Anh đã có chút khinh suất rồi.",

    # 17: 就憑易天的那封信，這一次就比上輩子複雜了許多。
    "Chỉ bằng bức thư kia của Dịch Thiên, lần này đã phức tạp hơn kiếp trước rất nhiều.",

    # 18: 想到這裡，婁禧陽的眸色深了些許。
    "Nghĩ đến đây, sắc mắt Lâu Hỉ Dương trầm xuống đôi phần.",

    # 19: 耳邊突然響起了震動聲...
    "Bên tai đột nhiên vang lên tiếng rung, anh khẽ nâng mí mắt, theo bản năng hướng ánh mắt vào thiết bị đầu cuối, lại phát hiện trên đó chẳng hề có động tĩnh gì.",

    # 20: 不是易緣。
    "Không phải Dịch Duyên.",

    # 21: 他抿了抿唇，眸色又沉了一分，心緒複雜。
    "Anh mím mím môi, sắc mắt lại trầm xuống một phân, tâm tư rối bời.",

    # 22: 他又轉而打開了震動的萊德通訊戒。
    "Anh liền chuyển sang mở chiếc nhẫn liên lạc bang Lloyd đang rung lên.",

    # 23: 看著萊德內網上就#婁禧陽倒底是不是變態#的話題聊的水深火熱的一群人...
    "Nhìn một đám người trên mạng nội bộ bang Lloyd đang bàn tán sôi nổi như nước sôi lửa bỏng về chủ đề #Rốt cuộc Lâu Hỉ Dương có phải biến thái hay không#, Lâu Hỉ Dương chậm rãi híp mắt lại.",

    # 24: 看來是他給的buff太多，導致這群人完全沒有即將要進攻的危機意識，在這閑得蛋疼。
    "Xem ra là do anh buff cho quá nhiều, dẫn đến đám người này hoàn toàn không có chút ý thức nguy cơ nào về cuộc tấn công sắp tới, rảnh rỗi quá hóa rỗi hơi ở đây.",

    # 25: 前幾天按照圖紙做出的第一台雛形機甲出來後，萊德的人就炸了。
    "Mấy ngày trước sau khi mô hình cơ giáp đầu tiên được làm ra theo bản vẽ thiết kế, người của bang Lloyd liền bùng nổ.",

    # 26: 任何一個男人都會在絕對的武力面前熱血沸騰。
    "Bất kỳ người đàn ông nào cũng đều sẽ sôi trào nhiệt huyết trước vũ lực tuyệt đối.",

    # 27: 送死？不，這分明就是去砸場子的！
    "Đi tìm cái chết? Không, cái này rõ ràng là đi đập nát địa bàn của người ta!",

    # 28: 機甲兵團全團一掃以往的頹廢萎靡...
    "Toàn thể binh đoàn cơ giáp quét sạch vẻ sa sút ủ rũ ngày trước, từng người từng người đều như được tiêm máu gà. Tuy nói là sĩ khí giang hồ được cổ vũ phấn chấn, nhưng tình trạng như vậy cũng khiến bọn họ lơ là biếng nhác đi không ít.",

    # 29: 是該好好整治整治...
    "Quả đúng là nên chấn chỉnh lại cho ra trò. Lâu Hỉ Dương lướt sơ qua hàng loạt tin nhắn xin lỗi dồn dập của Bội Lương rồi tắt nhẫn liên lạc đi.",

    # 30: 深夜，在一群匪徒舒舒服服躺在床上準備入睡時...
    "Đêm khuya, lúc một đám thổ phỉ đang thoải mái nằm trên giường chuẩn bị đi ngủ, khuôn mặt anh tuấn không chút cảm xúc của Lâu Hỉ Dương liền chiếu ra từ chiếc nhẫn của bọn họ.",

    # 31: “五分鍾，下來訓練，遲到的人加訓兩小時。”
    "“Năm phút, xuống sân huấn luyện, người đến muộn phạt huấn luyện thêm hai tiếng.”",

    # 32: 畫面裡的婁禧陽像是才洗了頭...
    "Lâu Hỉ Dương trong hình dường như vừa mới gội đầu xong, tóc mái được anh tùy ý vuốt ngược ra sau tai, để lộ vầng trán sáng sủa.",

    # 33: 他頭頂上的暗紅色燈光在他身上鍍了一層紅霧...
    "Ánh đèn đỏ thẫm trên đỉnh đầu phủ lên người anh một tầng sương đỏ, mày mắt sâu thẳm ẩn giấu trong bóng tối, tựa như ác ma đang ung dung giương nanh múa vuốt về phía bọn họ.",

    # 34: 簡直比變態還像個變態。
    "Quả thực còn giống biến thái hơn cả kẻ biến thái.",

    # 35: 萊德眾匪徒：…其實以上言論我們都可以撤回，真的！
    "Chúng thổ phỉ Lloyd: ... Thực ra những lời bình luận bên trên chúng tôi đều có thể thu hồi lại mà, thật đấy!",

    # 36: *
    "*",

    # 37: 由於沒有事物再能讓婁禧陽分心...
    "Vì không còn điều gì khiến Lâu Hỉ Dương phải phân tâm nữa, anh dồn toàn bộ tinh lực vào việc thao luyện binh sĩ cơ giáp.",

    # 38: 在未來的四天時間裡...
    "Trong khoảng thời gian bốn ngày tiếp theo, Lâu Hỉ Dương mở ra chế độ huấn luyện địa ngục tàn khốc vô nhân đạo. Trên dưới hàng ngàn người của Lloyd kêu khổ thấu trời, nhưng cũng dần dần nhìn nhận nghiêm túc về trận chiến sắp phải đối mặt.",

    # 39: 在正式進攻的前兩天...
    "Vào hai ngày trước trận tiến công chính thức, toàn bộ cơ giáp của bang Lloyd đã hoàn thành cải tạo. Khi ánh mắt của toàn thể thổ phỉ Lloyd tập trung vào năm mươi cỗ cơ giáp đồ sộ hùng dũng, trong tròng mắt đục ngầu quanh năm đã bùng lên những tia lửa rực sáng.",

    # 40: 婁禧陽給了他們兩天的時間和機甲磨合...
    "Lâu Hỉ Dương cho bọn họ thời gian hai ngày để làm quen cọ xát với cơ giáp. Rạng sáng ngày thứ ba, anh thổi vang hồi còi xuất trận.",

    # 41: 留了兩百人給紅發老頭留守艾斯特區...
    "Để lại hai trăm người cho lão già tóc đỏ canh giữ khu Est, tám trăm người còn lại leo lên mô tô chiến đấu và cơ giáp bay thẳng về hướng Tây Lăng Sơn.",

    # 42: 轟隆隆的馬達聲在空中炸開...
    "Tiếng động cơ gầm rú ầm ầm nổ vang giữa không trung, phá vỡ sự tĩnh mịch hoang vu kể từ ngày tuyên bố mạt thế đến nay.",

    # 43: 由機甲兵團打頭陣...
    "Do binh đoàn cơ giáp đi tiên phong, bang phái Lloyd dừng lại ở bên ngoài ranh giới kích hoạt cơ chế phòng vệ của viện nghiên cứu Tây Lăng Sơn, chờ đợi hiệu lệnh của Lâu Hỉ Dương.",

    # 44: 很顯然這邊的動靜已經傳到了研究所裡...
    "Rất rõ ràng động tĩnh bên này đã truyền tới bên trong viện nghiên cứu. Lâu Hỉ Dương ngồi trong khoang điều khiển cơ giáp, nhìn những ánh đèn cảnh báo nối tiếp nhau sáng lên ở phía đối diện, cuối cùng khóa chặt tầm mắt vào góc đông nam của viện nghiên cứu.",

    # 45: 穿過電.網，從這個門闖進去...
    "Xuyên qua lưới điện, xông vào từ cánh cửa này, đi thẳng tới cuối đường rồi rẽ trái là có thể nhìn thấy phòng thí nghiệm giam giữ Lâu An Minh.",

    # 46: 婁禧陽快速計算著路徑...
    "Lâu Hỉ Dương nhanh chóng tính toán lộ trình. Ngay khoảnh khắc chuông báo động trên tháp canh của viện nghiên cứu vang lên, anh kề sát vào chiếc nhẫn liên lạc——",

    # 47: “機甲兵團跟我走，其余人按兵不動，跟隨倍良守在外圍等候指令。”
    "“Binh đoàn cơ giáp đi theo tôi, những người còn lại án binh bất động, theo Bội Lương trấn thủ ở vòng ngoài chờ đợi chỉ lệnh.”",

    # 48: 話音剛落，對面的四處大門就緩緩開了縫隙...
    "Lời vừa dứt, bốn cánh cổng lớn đối diện liền từ từ hé mở, hai mươi cỗ cơ giáp quân dụng cấp B nối đuôi nhau tràn ra ngoài, xếp thành một hàng chỉnh tề.",

    # 49: “此處是聯邦三星級研究所，機要重地，無關人員請迅速撤離，否則生死不論！”
    "“Nơi này là viện nghiên cứu ba sao của Liên bang, địa bàn cơ mật trọng yếu, người không phận sự mau chóng rút lui, bằng không sống chết mặc bay!”",

    # 50: 領頭的朝他們亮起了警示燈...
    "Kẻ dẫn đầu bật đèn cảnh báo về phía bọn họ, lời nói ra lại thong thả ung dung, dường như chẳng hề coi bọn họ ra gì.",

    # 51: 尤其是看到了他們的標志。
    "Đặc biệt là khi nhìn thấy huy hiệu của bọn họ.",

    # 52: 萊德？那個由一群老弱病殘湊在一起組成的破敗幫派...
    "Lloyd? Cái bang phái tàn tạ tập hợp bởi một lũ già yếu ốm đau bệnh tật kia, thực sự là không đáng để bọn họ phải huy động lực lượng lớn, phái ra hai mươi cỗ cơ giáp quân dụng cấp B này đã là nể mặt bọn chúng lắm rồi.",

    # 53: “喂，勸你們趕緊走...”
    "“Này, khuyên bọn mày mau cút đi, nhìn thấy mấy cỗ cơ giáp này chưa? Một phát pháo bắn qua là trên người bọn mày đến một mẩu vụn cũng không còn đâu, muốn gây chuyện thì ra ngoài đường lớn mà gây.”",

    # 54: 領頭的朝他們揮了揮手。
    "Tên cầm đầu phất phất tay về phía bọn họ.",

    # 55: 然而手還沒來得及放下，他的耳邊就炸開了一道摧天裂地的氣波。
    "Thế nhưng tay còn chưa kịp hạ xuống, bên tai gã đã nổ tung một luồng khí ba hủy thiên diệt địa.",

    # 56: 氣波波及到的四台機甲被無形的力推到半空中旋轉了多次後重重地砸落在身後的電.網上。
    "Bốn cỗ cơ giáp bị luồng khí ba quét trúng bị một lực vô hình hất tung lên giữa không trung xoay tròn mấy vòng, sau đó đập mạnh xuống lưới điện phía sau.",

    # 57: “換台s級再來。”婁禧陽收回手，語氣聽不出什麽波瀾。
    "“Đổi cỗ cấp S tới đây rồi hẵng nói chuyện.” Lâu Hỉ Dương thu tay về, ngữ khí chẳng nghe ra chút gợn sóng nào.",

    # 58: “我靠，拽！”
    "“Vãi chưởng, ngầu đét!”",

    # 59: “老子好久沒體會這種捏死螞蟻的感覺了。”
    "“Ông đây đã lâu lắm rồi chưa được nếm thử cảm giác bóp chết kiến thế này.”",

    # 60: ……
    "……",

    # 61: “走了，趁現在增援還沒出，你們掩護我去東南門。”
    "“Đi thôi, nhân lúc chi viện của chúng còn chưa ra, các người yểm trợ tôi tới cửa đông nam.”",

    # 62: 婁禧陽壓低嗓音，打斷正興奮不已的一群人。
    "Lâu Hỉ Dương hạ thấp giọng, cắt ngang đám người đang hưng phấn không thôi.",

    # 63: “是！”
    "“Rõ!”",

    # 64: 由張溝帶頭，五十台機甲緊隨婁禧陽身後...
    "Do Trương Câu dẫn đầu, năm mươi cỗ cơ giáp bám sát ngay sau lưng Lâu Hỉ Dương. Lại thêm hai tiếng nổ vang lên, chỉ cần giơ tay một cái, đối diện liền trống hoác một mảng.",

    # 65: 婁禧陽飛速地朝東南門跑著...
    "Lâu Hỉ Dương phi thân lao nhanh về phía cửa đông nam. Chỉ trong vỏn vẹn vài phút ngắn ngủi, bên trong viện nghiên cứu lại lao ra mười cỗ cơ giáp quân dụng cấp S cùng ba mươi cỗ cấp A. Đến đây, tiếng pháo nổ liên hồi không dứt, hai bên chính thức mở màn trận chiến.",

    # 66: 婁禧陽一腳踹飛了一個砸過來的鐵皮...
    "Lâu Hỉ Dương một cước đá bay một mảnh sắt vụn đập tới, nhắm thẳng cánh cửa bắn dữ dội một phát pháo. Cửa đông nam ầm ầm sụp đổ, anh không chút do dự nhảy xuống khỏi cơ giáp, lao như bay về phía mục tiêu.",

    # 67: 只要他動作夠快...
    "Chỉ cần động tác của anh đủ nhanh, nói không chừng còn chưa đợi bọn chúng khởi động cơ chế phòng vệ thì bọn họ đã có thể quay đầu rút lui rồi. Như vậy, thương vong của bang Lloyd có thể khống chế dưới mười người, thậm chí không có ai phải bỏ mạng.",

    # 68: 由於研究所的武裝機制都集中在所外...
    "Do cơ chế vũ trang của viện nghiên cứu đều tập trung ở bên ngoài, bên trong viện phần lớn đều là một đám nhân viên nghiên cứu chân yếu tay mềm. Mọi chuyện đều thuận lợi y như trong ký ức của anh, anh đánh ngất các thành viên viện nghiên cứu đi ngang qua một cách êm thấm, chỉ mất đúng hai phút là chạy tới trước phòng thí nghiệm giam giữ Lâu An Minh.",

    # 69: 按照記憶輸入密碼...
    "Dựa theo ký ức nhập mật mã vào, cánh cửa từ từ mở ra, một gương mặt có ba phần tương tự với anh nhìn thẳng vào tầm mắt anh.",

    # 70: 他已經接近十多年沒再見過這張臉了。
    "Anh đã gần mười mấy năm rồi chưa nhìn thấy lại khuôn mặt này.",

    # 71: “小陽，走，快走。”婁安明的眼裡亮了一瞬...
    "“Tiểu Dương, đi, mau đi thôi.” Trong mắt Lâu An Minh sáng lên trong khoảnh khắc, liền nhanh chóng bình tĩnh trở lại, “Đi theo ba, nhân lúc cơ chế phòng vệ còn chưa mở, chúng ta có cơ hội ra ngoài.”",

    # 72: 婁安明有條不紊地推了推鼻梁上的金絲眼鏡...
    "Lâu An Minh bình tĩnh đâu ra đấy đẩy gọng kính viền vàng trên sống mũi, nghiêng người bước ra khỏi cửa, sải bước nhanh chóng ra ngoài, mọi thứ đều như nằm trong kế hoạch của ông, chẳng có nửa điểm chật vật chạy trốn.",

    # 73: 婁禧陽抬起眼皮掠了一眼男人的背影，一言不發地跟在他身後。
    "Lâu Hỉ Dương nâng mí mắt liếc nhìn bóng lưng người đàn ông, không nói một lời bám sát theo sau ông.",

    # 74: 這條路是婁安明計劃好的，沒有什麽人，但是會路過所長辦公室。
    "Con đường này là do Lâu An Minh đã lên kế hoạch từ trước, không có mấy người, nhưng sẽ đi ngang qua văn phòng Viện trưởng.",

    # 75: 在他們拐角時，聽見了一陣激烈的爭執聲——
    "Khi bọn họ rẽ qua góc cua, liền nghe thấy một tràng tranh cãi kịch liệt vang lên——",

    # 76: “什麽叫做防衛機制開不了？你知道這裡面關的是什麽人嗎！啊！”
    "“Cái gì gọi là không mở được cơ chế phòng vệ hả? Cậu có biết người bị nhốt ở trong này là ai không hả! Hả!”",

    # 77: “劉所，我們已經在全力激活了，但是剛剛有人入侵了西菱山系統，我們……”
    "“Lưu viện trưởng, chúng tôi đã đang dốc toàn lực kích hoạt rồi, nhưng vừa nãy có người xâm nhập vào hệ thống Tây Lăng Sơn, chúng tôi……”",

    # 78: “別愣著，快走。”婁安明見婁禧陽突然停住了腳步，眉心一蹙，低聲催促他。
    "“Đừng ngây ra đó, mau đi thôi.” Lâu An Minh thấy Lâu Hỉ Dương đột nhiên khựng bước, chân mày cau lại, trầm giọng giục anh.",

    # 79: 婁禧陽晃了一下神，回頭看了眼身後，斂下眼底翻湧的疑雲，快步與婁安明並肩而行。
    "Lâu Hỉ Dương thất thần trong thoáng chốc, ngoái đầu nhìn phía sau một cái, thu lại mối nghi ngờ đang cuộn trào nơi đáy mắt, rảo bước đi song song cùng Lâu An Minh.",

    # 80: 沒有防衛機制的西菱山研究所已然成了一架脆皮...
    "Viện nghiên cứu Tây Lăng Sơn không có cơ chế phòng vệ đã hoàn toàn trở thành một món đồ giòn rụm dễ vỡ. Lúc bọn họ bước ra ngoài, cỗ cơ giáp cấp S cuối cùng vừa lúc đổ gục ngay trước mặt bọn họ.",

    # 81: 婁安明詫異地望著眼前的場景，顯然沒有料到會是全然相反的結果。
    "Lâu An Minh kinh ngạc nhìn khung cảnh trước mắt, rõ ràng là không ngờ tới sẽ có một kết quả hoàn toàn trái ngược thế này.",

    # 82: 婁禧陽將他推上機甲，隨後自己跳了上去，帶領萊德機甲兵返回，與倍良他們匯合。
    "Lâu Hỉ Dương đẩy ông lên cơ giáp, sau đó bản thân cũng nhảy lên, dẫn dắt cơ giáp binh của bang Lloyd quay về, hội quân cùng nhóm Bội Lương.",

    # 83: 八百匪徒，一個不少的起駕回程...
    "Tám trăm thổ phỉ, không thiếu một người nào cùng khởi hành trở về. Suốt dọc đường trở về rộn rã tiếng nói cười, hoàn toàn chưa dứt khỏi cảm giác sảng khoái vừa rồi.",

    # 84: “婁、安、明”倍良死死盯著眼前這個斯文敗類...
    "“LÂU, AN, MINH.” Bội Lương trừng trừng nhìn gã bại hoại nhã nhặn trước mặt, nghiến răng nghiến lợi rặn ra từng chữ, “Cái đồ mặt dày không biết xấu hổ nhà anh mà cũng dám xuất hiện trước mặt tôi à.”",

    # 85: 婁安明抽回手臂，理了理被倍良抓皺的白襯衫，淡淡道：“阿良，我沒功夫跟你鬧。”
    "Lâu An Minh rút tay về, vuốt phẳng lại chiếc áo sơ mi trắng bị Bội Lương túm nhăn nhúm, nhàn nhạt nói: “A Lương, tôi không rảnh gây sự với cậu.”",

    # 86: “你——”
    "“Anh——”",

    # 87: 婁禧陽靜靜地坐在一旁，旁觀著這一場鬧劇。
    "Lâu Hỉ Dương lặng lẽ ngồi một bên, khoanh tay bàng quan theo dõi màn kịch hề này.",

    # 88: 順勢低頭看了眼終端，發現和易緣的通訊界面仍停留在他走的那天。
    "Anh thuận thế cúi đầu liếc nhìn thiết bị đầu cuối, phát hiện giao diện trò chuyện với Dịch Duyên vẫn dừng lại ở đúng ngày cậu rời đi.",

    # 89: 余光中瞥見了一抹紅，果不其然，紅發老頭聞詢趕來了。
    "Nơi khóe mắt chợt thoáng qua một mảng màu đỏ, quả nhiên không ngoài dự đoán, lão già tóc đỏ nghe ngóng được tin tức liền vội vã chạy tới.",

    # 90: “你個臭小子！”
    "“Cái thằng ranh con này!”",

    # 91: 紅發老頭抄起拐杖就要朝婁安明身上掄，婁安明也沒躲，結結實實地受了這一拐。
    "Lão già tóc đỏ vung cây gậy chống toan quất thẳng vào người Lâu An Minh, Lâu An Minh cũng không né tránh, lãnh trọn một gậy này vào người.",

    # 92: “叔，阿良，你們要怎麽打我以後再說，我有一件很重要的事要說。”
    "“Chú, A Lương, mọi người muốn đánh tôi thế nào thì để sau hẵng nói, tôi có một chuyện vô cùng quan trọng cần nói.”",

    # 93: 婁安明將亂了的眼鏡摘下...
    "Lâu An Minh tháo chiếc kính mắt bị xô lệch xuống, để lộ ra đôi mắt mệt mỏi rã rời. Ông xoa xoa sống mũi, chậm rãi cất lời:",

    # 94: “蔣卓航，他瘋了。”
    "“Tưởng Trác Hàng, hắn ta điên rồi.”",

    # 95: *
    "*",

    # 96: 易緣正低頭看著終端，上面是陳斂發給他的一段錄像。
    "Dịch Duyên đang cúi đầu nhìn vào thiết bị đầu cuối, bên trên là một đoạn video do Trần Liễm gửi cho cậu.",

    # 97: 視頻裡，婁禧陽正跟在一個男人身後快步在西菱山研究所內穿梭。
    "Trong video, Lâu Hỉ Dương đang rảo bước đi theo sau một người đàn ông thoăn thoắt di chuyển bên trong viện nghiên cứu Tây Lăng Sơn.",

    # 98: 點了一下暫停，易緣將那一幀畫面放大再放大，直到婁禧陽清晰的臉佔滿整個屏幕。
    "Bấm nút tạm dừng một cái, Dịch Duyên phóng to khung hình đó lên hết cỡ, cho tới khi gương mặt rõ nét của Lâu Hỉ Dương chiếm trọn toàn bộ màn hình.",

    # 99: 陽哥，我好想你。
    "Dương ca, em nhớ anh quá.",

    # 100: 易緣將臉慢慢湊近，直到側臉貼在婁禧陽的投影上。
    "Dịch Duyên từ từ ghé mặt lại gần, cho đến khi một bên má áp sát vào hình ảnh chiếu ảo của Lâu Hỉ Dương.",

    # 101: “你可真像個瘋子。”
    "“Cháu trông thực sự giống hệt một kẻ điên.”",

    # 102: 陳斂冷不丁地對他說。
    "Trần Liễm bất thình lình nói với cậu một câu.",

    # 103: “別忘了約定易緣...”
    "“Đừng quên ước hẹn của chúng ta, Dịch Duyên. Từ nay về sau thời gian tự do mỗi ngày của cháu chỉ có ba tiếng đồng hồ thôi, những thời gian còn lại cháu không được bước ra khỏi viện điều trị này nửa bước.”",

    # 104: 陳斂使了個眼色，兩個穿著特質白大褂的人就走到了易緣身側。
    "Trần Liễm liếc mắt ra hiệu một cái, hai người mặc áo blouse trắng đặc chế liền bước tới bên cạnh Dịch Duyên.",

    # 105: 易緣順從地亮出了自己的後頸，讓他們將東西嵌進去。
    "Dịch Duyên ngoan ngoãn để lộ phần sau gáy của mình, để bọn họ khảm vật đó vào bên trong.",

    # 106: “過程會很痛苦，但是沒有辦法，不然你就沒命了。”陳斂眼底閃過一絲不忍，撤開了視線。
    "“Quá trình sẽ rất đau đớn, nhưng không còn cách nào khác, bằng không cháu sẽ mất mạng.” Đáy mắt Trần Liễm xẹt qua một tia không nỡ, dời tầm mắt đi chỗ khác.",

    # 107: 易緣伸出指尖抹掉鼻尖上的冷汗，低頭看回終端，心裡想的是，今天終於可以和陽哥發消息了。
    "Dịch Duyên đưa đầu ngón tay lau đi giọt mồ hôi lạnh trên chóp mũi, cúi đầu nhìn lại thiết bị đầu cuối, trong lòng thầm nghĩ: hôm nay rốt cuộc cũng có thể nhắn tin cho Dương ca rồi.",

    # 108: 感謝澆灌營養液的小天使，親親～
    "Cảm ơn thiên sứ nhỏ đã tưới dung dịch dinh dưỡng, hôn hôn ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_012 translation written: {len(paragraphs)} paragraphs.")
