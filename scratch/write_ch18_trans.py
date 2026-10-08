# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_018"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 18: Tầng thượng
---""",

    # 1: separator
    "==============",

    # 2: 婁禧陽睡前又給易緣打了好幾個視頻通訊...
    "Trước khi ngủ, Lâu Hỉ Dương lại gọi thêm mấy cuộc gọi video cho Dịch Duyên, tương tự vẫn chẳng có ai bắt máy.",

    # 3: 兩人的聊天界面上已經有十幾個未被接通的記錄...
    "Trên giao diện trò chuyện của hai người đã có mười mấy bản ghi cuộc gọi nhỡ, những chấm đỏ chi chít khiến Lâu Hỉ Dương hoàn toàn chẳng còn chút buồn ngủ nào.",

    # 4: “系統，你能告訴我多少關於易緣的消息？”
    "“Hệ thống, ngươi có thể nói cho ta biết bao nhiêu tin tức về Dịch Duyên?”",

    # 5: 【抱歉宿主，現在還不能告訴你任何消息嚶嚶嚶】
    "【Xin lỗi ký chủ, hiện tại vẫn chưa thể nói cho ngài bất kỳ tin tức nào đâu oa oa oa】",

    # 6: “如果我偏要知道呢？”...
    "“Nếu như ta cứ nhất quyết muốn biết thì sao?” Ngữ khí của Lâu Hỉ Dương thoáng mang theo hơi lạnh, sự bất thường của Dịch Duyên khiến anh bồn chồn nôn nóng một cách khó hiểu, “Nếu ta không tìm thấy cậu ấy thì tiến độ cũng sẽ chẳng có chuyển biến gì, đến lúc đó nhiệm vụ thất bại cả ngươi và ta đều cùng đi tong.”",

    # 7: 他知道這是系統的致命點，也是他重生到這裡的初衷。
    "Anh biết đây chính là tử huyệt của hệ thống, cũng là mục đích ban đầu khi anh trọng sinh đến nơi này.",

    # 8: 其實他自始自終都沒有將這個任務放在第一位...
    "Thực ra anh từ đầu đến cuối chưa từng đặt nhiệm vụ này lên vị trí hàng đầu, anh sống hay chết cũng chẳng màng, đối với anh mà nói đều chẳng có gì khác biệt.",

    # 9: 如果說剛開始他僅僅是因為有趣才願意配合系統...
    "Nếu như nói lúc mới bắt đầu anh chỉ vì cảm thấy thú vị mới bằng lòng phối hợp cùng hệ thống, thì về sau khi ngày tận thế được tuyên bố, động cơ của anh đã thay đổi: một là anh muốn đưa hành tinh M ở thế giới này trở lại quỹ đạo bình thường, hai là anh muốn biết được vận mệnh của Dịch Duyên.",

    # 10: 但婁禧陽沒發現的是...
    "Thế nhưng điều Lâu Hỉ Dương chưa từng nhận ra là, cả hai động cơ này đều không đủ để khiến anh phải bất an lo lắng đến nhường này vì hoàn cảnh của Dịch Duyên.",

    # 11: 果不其然，小鐵錘全身猛然繃緊：
    "Quả nhiên không ngoài dự đoán, búa sắt nhỏ toàn thân chợt căng cứng lại:",

    # 12: 【！！！容我再申明一遍我們位面討債所的原則...】
    "【!!! Xin cho tôi nhắc lại một lần nữa nguyên tắc của Sở Đòi Nợ Vị Diện chúng tôi, tất cả các thế giới đều được thiết lập dựa theo yêu cầu của chủ nợ, chúng tôi không thể làm trái ý nguyện của chủ nợ được. Vì chủ nợ không muốn ký chủ biết được tung tích của cậu ấy, nên tôi không thể tiết lộ hành tung của cậu ấy được.】",

    # 13: 【同樣，我們也不能插手除了感情進展以外的事情...】
    "【Tương tự, chúng tôi cũng không thể can thiệp vào những chuyện ngoài tiến triển tình cảm. Nếu như hành vi của ký chủ phá vỡ khuôn khổ dự tính của chủ nợ, nhẹ thì quay trở về thế giới ban đầu, nặng thì trực tiếp xóa sổ tinh thần đó nha!】",

    # 14: “他不願意讓我知道？嘖，這小屁孩兒”...
    "“Cậu ấy không muốn cho ta biết ư? Chậc, cái thằng nhóc này...” Lâu Hỉ Dương bắt trọn điểm mấu chốt trong lời của hệ thống, trong lòng bỗng chốc càng thêm khó chịu bực bội.",

    # 15: 【宿主……你這不會是想他了吧？】...
    "【Ký chủ... Ngài đây không phải là nhớ cậu ấy rồi đấy chứ?】 Búa sắt nhỏ lượn quanh đầu Lâu Hỉ Dương mấy vòng, quét biểu cảm trên mặt anh vào kho dữ liệu cảm xúc nhân loại để đối chiếu so sánh. Nhìn kết quả hiển thị trên trang dữ liệu, nó nhất thời ngũ vị tạp trần lẫn lộn.",

    # 16: 為什麽每次宿主和債主有矛盾，遭殃的都是自己啊嗚嗚嗚。
    "Tại sao mỗi lần ký chủ và chủ nợ có mâu thuẫn thì người chịu nạn luôn là mình cơ chứ hu hu hu.",

    # 17: 婁禧陽面上一青...
    "Sắc mặt Lâu Hỉ Dương tái xanh, tựa như vừa nuốt phải một con ruồi vậy. Anh vươn cánh tay trái lành lặn chộp lấy đầu búa sắt nhỏ, thế nhưng còn chưa kịp làm gì thì búa sắt nhỏ đã vút một cái biến mất tăm giữa không trung.",

    # 18: 臨走前還不怕死地說了一句...
    "Trước khi chuồn đi nó còn không sợ chết mà bồi thêm một câu: “Ngài cứ việc mạnh miệng tiếp đi, hừ hừ, sau này hối hận muốn chết cho coi!”",

    # 19: *
    "*",

    # 20: 婁禧陽已經在床上躺了將近三天了...
    "Lâu Hỉ Dương đã nằm trên giường gần ba ngày trời. Trong thời gian này người hộ lý kia ngoại trừ buổi tối ra thì từng bước không rời canh chừng anh, khiến anh căn bản không tìm được cơ hội nào ra ngoài thăm dò.",

    # 21: 傷口安安靜靜愈合了三天...
    "Vết thương yên ả khép miệng suốt ba ngày, đã không còn hễ cứ khẽ động đậy là lại toác ra nữa.",

    # 22: 雖然他很佩服這位“護工”的敬業程度...
    "Tuy rằng anh rất khâm phục mức độ tận tụy với nghề của vị “hộ lý” này, nhưng anh thực sự muốn hỏi xem có phải cấp trên giao việc cho cậu ta quá nhàn rỗi hay không mà khiến cậu rảnh rang đến mức độ này.",

    # 23: 正當他快要忍不住時，機會就來了。
    "Ngay lúc anh sắp sửa không nhịn nổi nữa thì cơ hội đã tới.",

    # 24: 婁安明來看他了。
    "Lâu An Minh tới thăm anh.",

    # 25: 婁安明進來的時候他差點沒認出來...
    "Lúc Lâu An Minh bước vào anh suýt chút nữa không nhận ra, nhìn một lúc mới phát hiện ra hóa ra ông đã đeo mặt nạ da người mô phỏng.",

    # 26: 他又換上了西裝...
    "Ông lại thay bằng một bộ âu phục, đôi mắt sau cặp kính gọng bạc nhìn thẳng vào anh, tựa như tròng mắt của người máy, chẳng mang theo chút cảm xúc nào.",

    # 27: 他走到病床邊...
    "Ông bước tới bên giường bệnh, lật chăn trên người Lâu Hỉ Dương ra, kéo cạp quần anh xuống nhìn suốt nửa phút mới chậm rãi mở miệng: “Ba nhớ huấn luyện viên cận chiến ba thuê cho con trước giờ luôn hết lời khen ngợi con, con không đến mức ngay cả mấy tên du côn cũng đánh không lại.”",

    # 28: 婁禧陽提了提褲子，沒說話。
    "Lâu Hỉ Dương kéo lại quần, không lên tiếng.",

    # 29: 見他這種反應...
    "Thấy phản ứng này của anh, khuôn mặt bình lặng của Lâu An Minh rốt cuộc cũng có thêm một tia biến đổi. Ông khẽ nhíu mày: “Bội Lương đã kể cho ba nghe chuyện của con rồi. Tiểu Dương, ba xưa nay luôn tin tưởng vào năng lực của con, vốn dĩ từ những chuyện này ba cứ ngỡ con đã trưởng thành rồi, nhưng cách làm của con ngày hôm đó khiến ba có chút thất vọng.”",

    # 30: “現在是什麽時候？...”
    "“Bây giờ là thời điểm nào rồi? Việc chúng ta phải làm là nghĩ đủ mọi cách tìm ra tung tích của mẹ con, cứu bà ấy ra, để bà ấy vạch trần lời nói dối của Tưởng Trác Hàng trước toàn thể người dân hành tinh M. Nhưng con nhìn bộ dạng của con hiện tại xem, con có để tâm vào chuyện này không?”",

    # 31: “爸，你還記得我的導師在畢業時跟您說了什麽嗎？”...
    "“Ba, ba còn nhớ người hướng dẫn của con lúc tốt nghiệp đã nói gì với ba không?” Lâu Hỉ Dương ngước mắt lên, lạnh lùng cắt ngang lời ông.",

    # 32: 婁禧陽從聯邦第一機甲學院畢業的那年...
    "Năm Lâu Hỉ Dương tốt nghiệp Học viện Cơ giáp Số Một Liên bang, Lâu An Minh từng đến trường thị sát, không chỉ một giáo viên hướng dẫn trước mặt ông khen ngợi Lâu Hỉ Dương điềm tĩnh, vững vàng, có bóng dáng của ông.",

    # 33: 如果婁安明當時將那些話記在心裡...
    "Nếu như Lâu An Minh khi đó ghi nhớ những lời ấy trong lòng, hoặc là hiểu biết đôi chút về tính cách của anh thì đã rất dễ dàng nhận ra sự cố ý của anh ngày hôm đó. Nhưng đáng tiếc, ông chẳng biết một chút gì cả.",

    # 34: 婁安明沉默了一會兒...
    "Lâu An Minh trầm mặc một thoáng, rốt cuộc không đáp lại được. Ông dời ánh mắt sang chiếc thiết bị đầu cuối đang vang lên tiếng chuông, đốt ngón tay bắt đầu gõ nhẹ lên cổ tay.",

    # 35: 婁禧陽看出來，他這是想走了。
    "Lâu Hỉ Dương nhìn ra được, ông đây là muốn rời đi rồi.",

    # 36: “之前放出去的暗線有動靜了...”
    "“Đường dây ngầm thả ra trước đó có động tĩnh rồi, ba phải đi xem sao, xin lỗi Tiểu Dương.” Lâu An Minh do dự một chút rồi vẫn nói ra miệng.",

    # 37: “我希望你能好好養傷...”
    "“Ba hy vọng con có thể dưỡng thương cho tốt, quay về giúp ba. Hãy ghi nhớ bài học từ sự lỗ mãng lần này, sau này đừng tái phạm nữa.”",

    # 38: 婁安明一邊說著一邊站起了身，轉頭就朝門外走。
    "Lâu An Minh vừa nói vừa đứng dậy, quay đầu bước ra ngoài cửa.",

    # 39: 婁禧陽見狀從床上跳了下來，穿上鞋子就跟在了他身後。
    "Lâu Hỉ Dương thấy vậy liền nhảy xuống giường, xỏ giày bước theo sau ông.",

    # 40: “我陪您，順便出去透口氣。”
    "“Con tiễn ba, tiện thể ra ngoài hít thở chút không khí.”",

    # 41: 婁安明見狀也沒拒絕，任由婁禧陽開了門。
    "Lâu An Minh thấy thế cũng không từ chối, mặc cho Lâu Hỉ Dương mở cửa.",

    # 42: 門剛一打開...
    "Cửa vừa mở ra, một gương mặt bị mặt nạ phòng hộ che kín mít liền nhào tới.",

    # 43: 護工盡忠職守地守在門外...
    "Người hộ lý tận tụy canh giữ ngoài cửa, chặn Lâu Hỉ Dương lại: “Anh tốt nhất nên nằm trở lại giường.”",

    # 44: “我和朋友出去走走，不會有事。”...
    "“Tôi cùng bạn ra ngoài đi dạo một chút, không sao đâu.” Lâu Hỉ Dương lách người chui ra từ khe hở, đối diện với ánh mắt mang vẻ dò xét của Lâu An Minh.",

    # 45: 走了幾步他又轉頭對跟在身後的護工道...
    "Đi được vài bước anh lại quay đầu nói với người hộ lý đi theo sau: “Có người đi cùng tôi rồi, không cần cậu đi theo đâu, vất vả cho cậu rồi.”",

    # 46: 那護工看樣子還想辯駁幾句，但最終還是放棄了。
    "Người hộ lý kia nom dáng vẻ vẫn muốn biện bạch vài câu, nhưng cuối cùng vẫn từ bỏ.",

    # 47: 父子兩人走在治療所的過道上...
    "Hai cha con rảo bước trên hành lang viện điều trị, không gian trống trải chỉ có tiếng bước chân của hai người.",

    # 48: “我不認為這裡的護工會像剛才那位一樣。”...
    "“Ba không nghĩ hộ lý ở đây lại giống như người vừa rồi đâu.” Lâu An Minh liếc mắt nhìn qua mặt Lâu Hỉ Dương, nhắc nhở, “Cẩn thận một chút, Tưởng Trác Hàng đã bắt đầu lùng sục tìm ba rồi.”",

    # 49: 婁禧陽應了一聲，一邊走著一邊用余光打量著周圍。
    "Lâu Hỉ Dương đáp một tiếng, vừa đi vừa dùng khóe mắt quan sát xung quanh.",

    # 50: 他先是將婁安明送到了治療所門口...
    "Trước tiên anh tiễn Lâu An Minh tới cổng viện điều trị, sau đó giả vờ đi dạo bước vào khu vườn nhỏ đi kèm. Trong vườn rất ít người, ngoài nhân viên của viện điều trị ra thì chỉ có lác đác vài bệnh nhân.",

    # 51: 吸引他注意的是秋千後面那堵爬滿c藤的牆。
    "Thứ thu hút sự chú ý của anh chính là bức tường phủ đầy dây leo C đằng sau chiếc xích đu.",

    # 52: paradise旨在複刻M星的原始自然環境...
    "Paradise nhắm tới mục tiêu tái hiện lại môi trường tự nhiên nguyên sinh của hành tinh M, nhưng điều kiện sinh trưởng của dây leo C cực kỳ khắc nghiệt, Lâu Hỉ Dương không nghĩ đơn thuần chỉ vì trang trí mà lại dùng tới loại thực vật này.",

    # 53: c草最罕為人知的特征就是茂密到密不透風...
    "Đặc tính ít người biết nhất của cỏ C chính là rậm rạp tới mức gió thổi không lọt, ngay cả thiết bị nhìn xuyên thấu cũng không thể nhìn thấu sang mặt bên kia qua lớp lá của nó.",

    # 54: 他抬步朝那邊走去。
    "Anh nhấc chân sải bước về phía đó.",

    # 55: 沒有人注意到他的動作，畢竟秋千是最為平常的設備。
    "Không một ai chú ý tới hành động của anh, dẫu sao xích đu cũng là thiết bị bình thường nhất.",

    # 56: 婁禧陽一個利落地起跳，一眨眼就翻到了草牆的另外一面。
    "Lâu Hỉ Dương tung người bật nhảy dứt khoát, chớp mắt một cái đã nhảy tót sang mặt bên kia của bức tường cỏ.",

    # 57: 他發現他繞到了治療所的背面...
    "Anh phát hiện mình đã đi vòng ra phía sau lưng viện điều trị, nơi này không có lấy một bóng người, vắng vẻ lạnh lẽo vô cùng.",

    # 58: 在此處巡視了一圈婁禧陽也沒發現有什麽異常...
    "Tuần tra một vòng ở nơi này Lâu Hỉ Dương cũng không phát hiện ra điều gì bất thường, đang định rời đi thì đột nhiên anh nghe thấy tiếng động cơ gầm rú vang lên.",

    # 59: 他猛然朝聲音響起之處望去...
    "Anh chợt ngoái đầu nhìn về nơi phát ra âm thanh, phát hiện trước mặt là một bức tường, mà âm thanh lại truyền ra từ bên ngoài tường.",

    # 60: 這堵牆……有隱藏門。
    "Bức tường này... Có cửa bí mật.",

    # 61: 婁禧陽的目光在牆上來回掃量，很快就確定了心裡的猜想。
    "Ánh mắt Lâu Hỉ Dương quét qua quét lại trên bức tường, rất nhanh đã khẳng định phỏng đoán trong lòng.",

    # 62: 他飛快地側身躲到了西面的死角...
    "Anh nhanh chóng né người nấp vào góc chết phía tây, quả nhiên không ngoài dự liệu, bức tường kia biến mất sau mười mấy giây.",

    # 63: 從外面走進來了兩個穿著白大褂的男人...
    "Từ bên ngoài bước vào hai người đàn ông mặc áo blouse trắng, hai người dường như không phát hiện ra điều bất thường, trước sau rảo bước đi xa.",

    # 64: 婁禧陽等了好幾秒，才悄聲跟了上去。
    "Lâu Hỉ Dương đợi vài giây mới lặng lẽ bám theo sau.",

    # 65: 兩個男人帶著面罩，走得很快...
    "Hai người đàn ông đeo mặt nạ, bước đi rất nhanh, rõ ràng là quen thuộc như lòng bàn tay với lộ trình này. Lâu Hỉ Dương nhìn bọn họ đi tới một góc cực kỳ hẻo lánh, mà nơi đó vừa vặn là một bên sườn của tòa nhà viện điều trị.",

    # 66: 這分明就是個死胡同...
    "Nơi này rõ ràng là một ngõ cụt, thế nhưng hai người đàn ông kia lại như biết có đường đi, cách không rút thiết bị đầu cuối quét một cái về phía tòa nhà—— trên bức tường vốn trống trơn liền hiện ra cánh cửa thang máy.",

    # 67: 婁禧陽瞳孔微縮，無聲地握緊了拳。
    "Đồng tử Lâu Hỉ Dương co rút lại, lặng lẽ siết chặt nắm đấm.",

    # 68: 這就是隱藏的那架電梯。
    "Đây chính là chiếc thang máy bí mật kia.",

    # 69: 兩個男人等了幾秒，顯示屏上就顯示門要開了。
    "Hai người đàn ông đợi vài giây, trên màn hình hiển thị cửa sắp mở.",

    # 70: 婁禧陽猛地從死角朝二人撲了過去...
    "Lâu Hỉ Dương bất thình lình từ góc chết lao bổ về phía hai người, một nhát chém tay hạ ngất người đàn ông gần nhất, lại ngay lúc người kia sắp kêu lên liền dùng đầu gối thúc mạnh vào bụng gã.",

    # 71: 兩人悄無聲息地躺倒在地。
    "Hai người không một tiếng động ngã gục xuống sàn.",

    # 72: 婁禧陽快速扒下一人的衣物，將面罩戴在了臉上，走進了電梯。
    "Lâu Hỉ Dương nhanh tay lột áo của một người, đeo mặt nạ lên mặt rồi bước vào thang máy.",

    # 73: 電梯的按鍵只有一和二...
    "Bàn phím của thang máy chỉ có số 1 và số 2, hoàn toàn khớp với phỏng đoán trước đó của anh: trên đỉnh tòa nhà này có ít nhất hai tầng không gian chưa được mở.",

    # 74: 他遲疑了會兒，按下了1。
    "Anh ngập ngừng một thoáng rồi bấm nút số 1.",

    # 75: 他感覺到電梯廂在迅速地平移又上行...
    "Anh cảm nhận được khoang thang máy đang dịch chuyển ngang rất nhanh rồi đi lên trên. Anh ghi nhớ sự thay đổi phương hướng, nửa phút sau, thang máy “đinh” một tiếng, cửa mở ra.",

    # 76: 入目是片昏暗的大廳。
    "Đập vào mắt là một đại sảnh u tối mờ mịt.",

    # 77: 大廳呈深紫色...
    "Đại sảnh mang sắc tím sẫm, ở giữa chứa một hồ nước tuần hoàn rộng khoảng mười mét vuông. Tia sáng màu xanh lam nhạt trên đỉnh đầu chiếu xuống làn nước, phản chiếu lên bốn bức tường những vệt sáng chập chờn đung đưa.",

    # 78: 黑靴踏上地面，婁禧陽踩到了水波紋上。
    "Đôi ủng đen giẫm lên mặt sàn, Lâu Hỉ Dương bước lên những gợn sóng nước phản chiếu.",

    # 79: 他屏住呼吸，抬眼望向最深處的走廊——他看到了無數扇亮著燈的門窗。
    "Anh nín thở, ngước mắt nhìn về phía hành lang sâu nhất bên trong—— anh nhìn thấy vô số cánh cửa và khung cửa sổ đang sáng đèn.",

    # 80: “你是誰？”
    "“Cậu là ai?”",

    # 81: 隨著一聲低啞的威脅聲響起...
    "Kèm theo một giọng nói đe dọa khàn khàn vang lên, tầm mắt Lâu Hỉ Dương chao đảo một cái, nhìn thấy điểm ngắm laze đã rơi ngay trên lồng ngực mình.",

    # 82: 婁禧陽望向朝他走來的黑西裝男人，緩緩舉起了雙手。
    "Lâu Hỉ Dương nhìn người đàn ông mặc âu phục đen đang tiến về phía mình, từ từ giơ hai tay lên.",

    # 83: “你不是這裡的人，這裡的人沒有你這麽高的。”
    "“Cậu không phải người ở đây, người ở đây không có ai cao như cậu cả.” Người đàn ông bình tĩnh nhưng dứt khoát phủ quyết thân phận của anh.",

    # 84: 婁禧陽的心跳逐漸加重...
    "Nhịp tim Lâu Hỉ Dương dần đập nhanh hơn. Anh nhìn người đàn ông trông như lính gác trước mặt, tính toán xem làm sao mới có thể giật lấy khẩu súng laze từ tay gã.",

    # 85: 正當男人離他只有一米遠的間距時，後面突然傳來了動靜。
    "Ngay lúc người đàn ông chỉ còn cách anh cự ly một mét, phía sau đột nhiên truyền tới động tĩnh.",

    # 86: “放下，他是我帶來的。”
    "“Hạ súng xuống, anh ấy là do tôi dẫn tới.”",

    # 87: 婁禧陽的視線越過男人的肩頭...
    "Tầm mắt Lâu Hỉ Dương vượt qua vai người đàn ông, nhìn thấy một bóng hình quen thuộc nơi đại sảnh nối liền với hành lang.",

    # 88: 護工走到二人面前...
    "Người hộ lý bước tới trước mặt hai người, giơ thẻ công tác trong tay ra hiệu cho người đàn ông xem, bất động thanh sắc chắn ngay trước người Lâu Hỉ Dương.",

    # 89: 下章掉馬
    "Chương sau lộ tẩy thân phận"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_018 translation written: {len(paragraphs)} paragraphs.")
