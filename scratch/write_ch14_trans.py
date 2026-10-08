# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_014"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 14: Chỉ cho anh xem
---""",

    # 1: separator
    "==================",

    # 2: 易緣原本就隻攏了一件浴衣...
    "Dịch Duyên vốn dĩ chỉ khoác hờ một chiếc áo choàng tắm. Ngay khoảnh khắc Lâu Hỉ Dương lên tiếng ngăn cản cậu, cậu liền nhanh tay giật phăng sợi dây buộc ngang eo.",

    # 3: 浴衣沒了牽扯...
    "Áo choàng tắm không còn dây níu giữ liền buông rủ xuống trước bụng cậu, thấp thoáng để lộ vòng eo trắng ngần gầy gò bên trong, cùng với một mảng màu sắc chợt lướt qua trên đó.",

    # 4: 緊接著，他微微傾身...
    "Ngay sau đó, cậu hơi nghiêng người về phía trước, áo choàng tắm sắp sửa tuột khỏi đầu vai.",

    # 5: “易緣，別脫了。”
    "“Dịch Duyên, đừng cởi nữa.”",

    # 6: 在易緣的手指抓上浴衣...
    "Ngay lúc ngón tay Dịch Duyên tóm lấy áo choàng tắm định thực hiện động tác tiếp theo, Lâu Hỉ Dương nhẫn nhịn hết nổi, khàn giọng quát dừng cậu lại.",

    # 7: 聽出來婁禧陽是認真的...
    "Nghe ra Lâu Hỉ Dương là thật sự nghiêm túc, động tác của Dịch Duyên khựng lại tại chỗ.",

    # 8: 一雙透亮的眼睛朝畫面裡的他望過來...
    "Một đôi mắt trong veo nhìn qua khung hình về phía anh, có chút vô tội: “Sao thế Dương ca? Em chỉ muốn cho anh xem thôi mà.”",

    # 9: 那副姿態純情又委屈...
    "Dáng vẻ kia vừa thuần tình lại vừa tủi thân, chẳng hề có chút dấu vết ngụy trang nào.",

    # 10: 婁禧陽眉頭皺的快要夾死蒼蠅...
    "Chân mày Lâu Hỉ Dương nhăn tít lại tới mức có thể kẹp chết ruồi. Anh dời tầm mắt khỏi vùng eo của Dịch Duyên, cảm thấy bản thân mình quả đúng là gặp quỷ rồi: “Xem cái gì? Có chuyện gì không thể trực tiếp mở miệng nói mà lại phải cởi quần áo?”",

    # 11: “就算你是個男人，也不能隨隨便便就脫衣服給別人看。”
    "“Cho dù em là đàn ông đi chăng nữa, cũng không thể tùy tùy tiện tiện cởi quần áo cho người khác xem như thế được.”",

    # 12: “那你還經常脫給別人看呢。”易緣不甘心。
    "“Thế chẳng phải anh cũng thường xuyên cởi cho người khác xem đấy thôi.” Dịch Duyên không cam lòng.",

    # 13: “我什麽時候…”婁禧陽話音一頓...
    "“Anh khi nào...” Giọng Lâu Hỉ Dương khựng lại, nhớ ra quả thực có chuyện này, nhưng đó đều là một đám đàn ông to xác tắm rửa cùng nhau mà thôi, “Em thì khác.”",

    # 14: “怎麽不一樣，而且，我隻給你看。”易緣小聲反駁。
    "“Khác chỗ nào chứ, hơn nữa, em chỉ cho một mình anh xem thôi.” Dịch Duyên nhỏ giọng cãi lại.",

    # 15: 婁禧陽被問住了，但下一秒還是嚴厲拒絕：“不行。”
    "Lâu Hỉ Dương bị hỏi đến nghẹn lời, nhưng giây tiếp theo vẫn nghiêm khắc từ chối: “Không được.”",

    # 16: 於是，在婁禧陽責令的目光下...
    "Thế là, dưới ánh mắt nghiêm khắc yêu cầu của Lâu Hỉ Dương, Dịch Duyên ngoan ngoãn mặc lại quần áo theo chỉ dẫn của anh.",

    # 17: “為什麽你身上的水還沒乾？”婁禧陽注意到易緣的臉上仍留著水珠...
    "“Tại sao nước trên người em vẫn chưa khô?” Lâu Hỉ Dương chú ý thấy trên mặt Dịch Duyên vẫn còn đọng lại những giọt nước, ngay cả cổ cũng bốc lên hơi ẩm ướt.",

    # 18: 易緣聞言怔了一下，也沒回答，不留痕跡地轉移了話題。
    "Dịch Duyên nghe vậy ngẩn ra một thoáng, cũng không trả lời, không để lại dấu vết mà chuyển dời chủ đề.",

    # 19: “哥哥，我在尾椎那裡，紋了身。”他突然湊近鏡頭，軟黏地開了口。
    "“Ca ca, ở chỗ xương cụt, em đã xăm hình rồi.” Cậu đột nhiên ghé sát ống kính, giọng nói mềm nhũn dính dấp cất lên.",

    # 20: 柔軟的唇瓣在屏幕前張張合合...
    "Cánh môi mềm mại trước màn hình khép mở liên hồi, cưỡng ép Lâu Hỉ Dương nhớ lại nụ hôn đêm hôm đó.",

    # 21: “紋了什麽？”他冷靜道。
    "“Xăm hình gì?” Anh bình tĩnh hỏi.",

    # 22: “不想告訴你了。”易緣突然往後一退...
    "“Không muốn nói cho anh biết nữa.” Dịch Duyên đột nhiên lùi lại phía sau, gương mặt phi giới tính nở nụ cười câu người mê hoặc, “Ca ca tự mình tới xem đi.”",

    # 23: 紋身這事可大可小...
    "Chuyện xăm mình này nói lớn cũng lớn mà nói nhỏ cũng nhỏ. Phóng tầm mắt nhìn khắp hành tinh M, ít nhất chín mươi phần trăm người đều có hình xăm trên người, chỉ là khác với các hành tinh khác, hình xăm ở hành tinh M một khi đã lên người là theo trọn cả đời, không có cơ hội xóa đi.",

    # 24: 婁禧陽肩臂上紋有一朵紅心黑蓮...
    "Trên bả vai và cánh tay Lâu Hỉ Dương có xăm một đóa hoa sen đen nhụy đỏ, là đồ đằng truyền lại từ thời ông nội của Lâu Hỉ Dương.",

    # 25: 但易緣不一樣...
    "Thế nhưng Dịch Duyên thì khác, cậu từ nhỏ đã sợ đau, tiêm thuốc một cái là sẽ chui tọt vào lòng anh thút thít hờn dỗi, phải dỗ dành một lúc lâu mới được. Trước kia Dịch Thiên cũng từng muốn xăm lên người cậu một con báo giống như ông, thấy cậu khóc lóc thảm thiết quá nên cũng đành thôi, không ngờ bây giờ cậu lại đi xăm mình.",

    # 26: “紋了就是一輩子，你想好了。”
    "“Xăm rồi là theo cả đời đấy, em suy nghĩ kỹ chưa.” Lâu Hỉ Dương ngẫm nghĩ, ai mà chẳng có thời kỳ nổi loạn, anh nên thấu hiểu cho đứa nhỏ ở độ tuổi này.",

    # 27: 只不過為什麽要紋在尾椎那塊兒？
    "Chỉ có điều tại sao lại phải xăm ở chỗ xương cụt kia chứ? Hiếm có người đàn ông nào thích xăm ở vị trí đó, người ngoài không nhìn thấy đã đành, da thịt chỗ đó lại còn nhạy cảm, chỉ cần chạm nhẹ một cái là tê dại cả người.",

    # 28: “嗯，想好了。”易緣盯著婁禧陽的下巴，眼底晦暗難辨。
    "“Vâng, em nghĩ kỹ rồi.” Dịch Duyên nhìn chằm chằm chiếc cằm của Lâu Hỉ Dương, đáy mắt tối tăm khó lường.",

    # 29: 易緣又東拉西扯地跟婁禧陽說了好一會兒...
    "Dịch Duyên lại chuyện đông chuyện tây nói với Lâu Hỉ Dương hồi lâu, Lâu Hỉ Dương cũng lẳng lặng lắng nghe, thỉnh thoảng hùa theo chủ đề của cậu. Chẳng hay biết từ lúc nào hai người đã trò chuyện suốt hai tiếng đồng hồ.",

    # 30: 但婁禧陽也未曾覺得煩悶，只是奇怪易緣的臉看上去怎麽還是濕乎乎的。
    "Thế nhưng Lâu Hỉ Dương cũng không hề cảm thấy phiền chán, chỉ lấy làm lạ vì sao gương mặt Dịch Duyên trông vẫn cứ ẩm ướt như vậy.",

    # 31: 如若不是對面的易緣臉色愈發慘白...
    "Nếu không phải Dịch Duyên ở đối diện sắc mặt càng lúc càng trắng bệch, giọng nói cũng ngày một yếu ớt đi thì Lâu Hỉ Dương có lẽ vẫn chưa nhận ra mấu chốt bên trong.",

    # 32: 那哪裡是水，分明就是冷汗。
    "Đó đâu phải là nước, rõ ràng chính là mồ hôi lạnh.",

    # 33: 鏡頭裡的易緣像是忍受著極大的痛苦...
    "Dịch Duyên trong ống kính dường như đang phải chịu đựng nỗi đau đớn tột cùng, những giọt mồ hôi to như hạt đậu men theo hạt môi chìm vào trong môi. Trong cơn mơ màng nhìn thấy thần sắc đột ngột căng cứng của Lâu Hỉ Dương, thầm kêu không ổn, cậu vội vàng ngắt kết nối cuộc gọi video.",

    # 34: 繃緊的神經放松，他任隨愈加強烈的痛苦席卷全身，倒在床上蜷緊了身體。
    "Dây thần kinh căng như dây đàn thả lỏng ra, cậu mặc cho cơn đau đớn ngày một dữ dội càn quét khắp toàn thân, ngã gục trên giường cuộn chặt thân thể lại.",

    # 35: 眼前的屏幕突然一黑，婁禧陽察覺不對，又打了回去，全都石沉大海。
    "Màn hình trước mắt đột ngột tối đen, Lâu Hỉ Dương nhận thấy điều bất thường liền gọi lại, tất cả đều như đá chìm đáy biển.",

    # 36: “系統，他怎麽了？”
    "“Hệ thống, cậu ấy bị làm sao thế?”",

    # 37: 【暫無回答權限。】
    "【Tạm thời không có quyền hạn trả lời.】",

    # 38: 婁禧陽快速地回想著...
    "Lâu Hỉ Dương nhanh chóng hồi tưởng lại, nhưng không nhớ ra bất kỳ ký ức nào liên quan đến việc cơ thể Dịch Duyên mang bệnh tật.",

    # 39: 或許是吃壞東西了？
    "Có lẽ là ăn phải thứ gì hỏng bụng rồi?",

    # 40: 不，不是，倘若是這種情況...
    "Không, không phải, nếu như là tình huống này thì Dịch Duyên nhất định sẽ tủi thân làm nũng cầu xin anh dỗ dành, chứ không phải giấu giếm anh không muốn để anh phát giác.",

    # 41: 陳斂對他做了什麽？
    "Trần Liễm đã làm gì cậu?",

    # 42: 婁禧陽皺眉思索...
    "Lâu Hỉ Dương nhíu mày suy nghĩ, sắc mắt càng thêm trầm xuống. Ý nghĩ chờ Dịch Duyên tự mình xuất hiện trước đó lập tức bị lật đổ. Bất luận thế nào, anh không thể để Dịch Duyên nằm ngoài phạm vi khống chế của mình, bất kể là xuất phát từ nhiệm vụ hệ thống hay là xuất phát từ trách nhiệm trông nom Dịch Duyên của anh.",

    # 43: 現在他已經不能確定易緣安全與否了。
    "Hiện tại anh đã không thể chắc chắn Dịch Duyên an toàn hay không nữa rồi.",

    # 44: 他挪了一眼目光，換了個方式問道：“系統，陳斂現在是不是在paradise？”
    "Anh dời ánh mắt, đổi một phương thức khác để hỏi: “Hệ thống, Trần Liễm hiện tại có phải đang ở Paradise không?”",

    # 45: 【是。】
    "【Đúng vậy.】",

    # 46: 聽到答案，婁禧陽翻身下床，快步出了門。
    "Nghe được câu trả lời, Lâu Hỉ Dương xoay người xuống giường, rảo bước đi ra ngoài cửa.",

    # 47: “爸，不是說去paradise嗎？現在就走吧。”婁禧陽敲響婁安明的房門，盯著他的眼睛沉聲道。
    "“Ba, chẳng phải nói đi Paradise sao? Bây giờ đi luôn đi.” Lâu Hỉ Dương gõ cửa phòng Lâu An Minh, nhìn thẳng vào mắt ông trầm giọng nói.",

    # 48: *
    "*",

    # 49: 婁安明當然不會拒絕婁禧陽...
    "Lâu An Minh đương nhiên sẽ không từ chối Lâu Hỉ Dương. Ông chuẩn bị sẵn hai cuốn giấy chứng nhận cư trú làm bằng thân phận giả, rồi cùng Lâu Hỉ Dương trước sau leo lên mô tô bay đặc cấp.",

    # 50: 不知道婁安明給倍良他們說了什麽...
    "Không biết Lâu An Minh đã nói gì với nhóm người Bội Lương, trước khi đi Bội Lương trợn mắt lườm nguýt bọn họ, còn đặc biệt sán lại trước mặt Lâu Hỉ Dương nhấn mạnh:",

    # 51: “你現在才是萊德的頭兒，有事記得叫我們。”
    "“Cậu hiện tại mới là đại ca của bang Lloyd, có chuyện gì nhớ gọi chúng tôi đấy.”",

    # 52: 說完朝婁安明翻了個白眼就走了。
    "Nói xong liền liếc trắng mắt với Lâu An Minh một cái rồi bỏ đi.",

    # 53: 婁禧陽和婁安明對視一眼，不約而同地飛上了天。
    "Lâu Hỉ Dương cùng Lâu An Minh đưa mắt nhìn nhau một cái, không hẹn mà cùng bay vút lên bầu trời.",

    # 54: “小陽，我已經知道了，你很優秀，遠遠出乎了我的意料，爸爸為你驕傲。”
    "“Tiểu Dương, ba đã biết rồi, con rất ưu tú, vượt xa ngoài dự liệu của ba, ba tự hào về con.”",

    # 55: “這十年是我虧欠了你，以後我會盡我所能補償你的損失…”
    "“Mười năm nay là ba nợ con, sau này ba sẽ dốc hết khả năng bồi thường cho những tổn thất của con...”",

    # 56: 婁安明原本一絲不苟的發絲在空中飄蕩...
    "Mái tóc vốn dĩ cẩn thận tỉ mỉ của Lâu An Minh bay phấp phới giữa không trung, từng câu từng chữ giống hệt như vị quan chức thủ đô ung dung khéo léo trước truyền thông năm xưa.",

    # 57: 而婁禧陽也最不喜歡這樣的婁安明，生疏，深沉，一板一眼。
    "Mà Lâu Hỉ Dương cũng ghét nhất một Lâu An Minh như thế này: xa cách, thâm trầm, cứng nhắc khuôn mẫu.",

    # 58: 他也不回答，只是兀自加快了速度，和婁安明一前一後錯開。
    "Anh cũng không thèm trả lời, chỉ tự mình tăng tốc độ lên, giãn cách vị trí trước sau với Lâu An Minh.",

    # 59: 兩人沉默地開了六個小時，最後抵達了那個令所有M星人向往的地方。
    "Hai người lái xe trong im lặng suốt sáu tiếng đồng hồ, cuối cùng đã đến được nơi mà tất cả người dân trên hành tinh M đều hằng khao khát hướng về.",

    # 60: 婁安明給自己帶上了DNA阻隔器...
    "Lâu An Minh đeo thiết bị ngăn chặn ADN cho mình, lại đeo thêm mặt nạ, rồi mới cùng Lâu Hỉ Dương mặt không đổi sắc tiến vào Paradise. Viên quan kiểm tra đánh giá bọn họ từ trên xuống dưới mấy lượt mới phất tay cho bọn họ vào trong.",

    # 61: 原因無他，只因兩人皆是匪徒打扮...
    "Nguyên do không gì khác, chỉ vì hai người đều ăn mặc theo phong cách thổ phỉ: cao ráo vạm vỡ, mặc áo may ô bạc màu, quần rằn ri quân đội xỏ vào ủng đen, trên cánh tay là hình xăm bắt mắt, tất cả đều rất khó để liên hệ với những người sang trọng đài các bên trong.",

    # 62: 但也不排除是搶了錢去買居住證的街頭混混...
    "Nhưng cũng không loại trừ khả năng là đám du côn đầu đường xó chợ cướp tiền để mua giấy chứng nhận cư trú, bên trong cũng có không ít cặn bã tụ tập lại với nhau làm xằng làm bậy.",

    # 63: 迎著打探的目光...
    "Đón nhận những ánh mắt dò xét, Lâu An Minh nghiêng người thấp giọng nói với Lâu Hỉ Dương: “Trước tiên đi tìm R để ông ta sắp xếp chỗ ở cho chúng ta. Nơi này là nơi gần Tưởng Trác Hàng nhất, dưới chân đèn thường tối nhất, chúng ta tuyệt đối không thể phô trương lộ liễu.”",

    # 64: 婁禧陽點了點頭，虛著眼睛看向了前方朝他們走來的一群人。
    "Lâu Hỉ Dương gật gật đầu, híp mắt nhìn về phía một đám người đang đi về phía bọn họ ở đằng trước.",

    # 65: 不是他們不能招搖，而是不要有不識相的找上門來。
    "Không phải bọn họ không thể phô trương, mà là tốt nhất đừng có kẻ nào không biết điều tự tìm tới cửa.",

    # 66: 馬上就見面啦
    "Sắp được gặp mặt rồi nè",

    # 67: 嘿嘿（流口水）
    "Hì hì (chảy nước miếng)",

    # 68: 謝謝小天使的營養液～
    "Cảm ơn dung dịch dinh dưỡng của thiên sứ nhỏ ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_014 translation written: {len(paragraphs)} paragraphs.")
