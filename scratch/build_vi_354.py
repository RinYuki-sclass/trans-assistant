# -*- coding: utf-8 -*-
import json

paragraphs_vi = [
    # 0 (P1)
    "Một Thợ săn Trung Quốc bẻ quặt hai tay tôi ra sau lưng rồi còng lại. Nhìn cái cách bọn họ đột nhiên làm vậy, người đàn ông trung niên kia có vẻ là một Phi thức tỉnh giả.",
    # 1 (P2)
    "“Đáng lý tôi nên nói rằng thật vui khi gặp được đồng hương ở nơi đất khách quê người, nhưng mà ông là ai thế nhỉ?”",
    # 2 (P3)
    "Khi tôi bước lại gần chiếc bàn, người đàn ông trung niên đứng dậy, khóe miệng nhếch lên vặn vẹo.",
    # 3 (P4)
    "“Tao từng giữ một vị trí trong Hiệp hội Thợ săn đấy. Cũng nhờ ơn mày cả-.”",
    # 4 (P5)
    "“A! Nhớ ra rồi! Ông là Wanyong-ssi. Họ Lee đúng không? Oa, tôi cứ thắc mắc sao người Trung Quốc lại hiểu rõ về tôi đến tận chân tơ kẽ tóc như vậy; hóa ra là do ông đã sống rất đúng với cái tên của mình[1].”",
    # 5 (P6)
    "Có rất nhiều người ở bệnh viện biết về kỹ năng Kháng Độc của tôi, chuyện đó thì thôi đi, nhưng kỹ năng Mầm non triển vọng là tối mật. Tôi chỉ mới thông báo cho phía Hiệp hội như một phần trong thỏa thuận đàm phán về Trung tâm thức tỉnh mà thôi.",
    # 6 (P7)
    "Trước lời lẽ của tôi, Lee Wanyong sa sầm mặt mày rồi túm chặt lấy cổ áo tôi.",
    # 7 (P8)
    "“Thằng ranh con, mày chỉ giỏi mồm mép thôi!”",
    # 8 (P9)
    "“Làm sao mồm mép của tôi bì kịp ông được chứ? Ông đã huênh hoang đến mức nào rồi hả? Hử? Sắc mặt hồng hào thế kia cơ mà, chắc là được đối đãi tử tế lắm nhỉ.”",
    # 9 (P10)
    "“Tao từng là Trưởng phòng Nhân sự của Hiệp hội Thợ săn đấy-!”",
    # 10 (P11)
    "“Vâng, Wanyong-ssi. Tôi đã bảo là tôi biết ông rồi mà.”",
    # 11 (P12)
    "Nhìn cái bản mặt nhăn nhúm méo mó của hắn, kiểu gì tôi cũng sắp bị ăn đòn cho xem.",
    # 12 (P13)
    "“Nếu đã bán nước để tìm cho mình một chỗ dung thân, sao ông không chịu an phận thủ thường mà hưởng thụ đi, còn mò đến gặp tôi làm gì? Rốt cuộc ông đã bán những thứ gì rồi? Nếu từng ở phòng nhân sự, chắc hẳn ông đã dâng sạch toàn bộ năng lực của các Thợ săn trực thuộc Hiệp hội rồi đúng không? May mà Cục trưởng Song-nim không nằm trong biên chế của Hiệp hội đấy nhỉ? Đâu có chuyện ông chỉ đơn giản bị tống cổ khỏi Hiệp hội; chắc chắn bọn họ phải bắt ông ký khế ước bịt miệng, nên tôi đoán là ông đã tìm cách vô hiệu hóa nó rồi chứ gì.”",
    # 13 (P14)
    "Để đề phòng, tôi đã tắt kỹ năng Kháng Nguyền đi một lúc. Bởi vì lỡ như Wanyong-ssi đột nhiên quay phắt lại ôm chầm lấy tôi thì lời nguyền sẽ bị giải trừ mất. Trước những lời của tôi, Wanyong-ssi tuôn ra hàng tràng chửi rủa. Lẽ nào lời nguyền trừng phạt vì phá vỡ khế ước của hắn vẫn chưa được giải? Trông cơ thể hắn chẳng có thương tổn gì, vậy rốt cuộc đó là lời nguyền kiểu gì chứ?",
    # 14 (P15)
    "“Tao đã phải cật lực cống hiến từ những ngày đầu thành lập Hiệp hội để gây dựng được vị thế của mình đấy!”",
    # 15 (P16)
    "“Chuyện đó tôi cũng có nghe qua rồi. Nghe đồn ông đóng vai trò chủ chốt trong việc hất cẳng các thành viên sáng lập ban đầu nhỉ? Thường thì mình đuổi người ta đi thì sau này mình cũng sẽ bị tống cổ thôi—ác giả ác báo mà, thấy chưa? Tự làm tự chịu cả thôi.”",
    # 16 (P17)
    "Hắn đến gặp tôi chỉ để xả cơn giận thôi ư? Tôi không nghĩ vậy. Tôi chưa từng nghĩ lũ khốn bị đuổi khỏi Hiệp hội mà thoát được án tù kia sẽ chịu sống yên phận, nhưng tôi cũng không ngờ chúng lại bán đứng thông tin nhanh đến mức này. Dù có biết trước đi nữa thì tôi cũng chẳng có cách nào thực sự ngăn chặn được bọn chúng.",
    # 17 (P18)
    "‘Chắc hẳn bên phía Hiệp hội đã lập một khế ước khá chặt chẽ rồi.’",
    # 18 (P19)
    "Nhưng Hiệp hội cũng phải lưu tâm đến vấn đề nhân quyền. Họ không thể dùng những thứ điều khoản đến mức nổ tung đầu nếu để lộ bí mật được. Đó là lý do vì sao khi đăng ký làm Thợ săn, kể cả khi phát hiện bạn che giấu kỹ năng hay năng lực, họ thường cũng chỉ nhắm mắt làm ngơ cho qua.",
    # 19 (P20)
    "“Thế ông có dắt theo đứa bạn nào nữa không? Hay là còn cả bên phía MKC cũ nữa? Tôi nghe nói bọn họ cũng bắt tay với Trung Quốc rồi. Ông đã tuồn ra cả đống thông tin về cơ sở nuôi dưỡng rồi đúng không? Còn Haeyeon thì sao?”",
    # 20 (P21)
    "Khi tôi nhắc tới Haeyeon, bàn tay đang túm cổ áo tôi càng siết chặt hơn. Wanyong-ssi giật mạnh, kéo nửa người tôi ghì lên mặt bàn. Cạnh bàn sắc nhọn cấn vào người khiến tôi thấy hơi đau.",
    # 21 (P22)
    "“Thằng anh hay thằng em, cả hai thằng chúng mày đều là một lũ khốn nạn như nhau…….”",
    # 22 (P23)
    "Thằng khốn nghiến răng kèn kẹt lẩm bẩm. Sao tự dưng lại lôi Yoohyun-ie vào đây thế này?",
    # 23 (P24)
    "“Mắc mớ gì mà mày lại đi bới móc em trai người khác hả?”",
    # 24 (P25)
    "“Mày không biết cái thằng ranh con ngông cuồng Han Yoohyun đã được Hiệp hội đưa về cưu mang ngay khi nó vừa mới Thức tỉnh à? Thế mà thằng khốn đó lại dám quậy phá tanh bành ở đó đấy.”",
    # 25 (P26)
    "…Tôi biết Hiệp hội từng tạm thời che chở cho thằng bé, nhưng mà—quậy phá tanh bành ư? Khi tôi vô thức cau mày, thằng khốn Wanyong lại bắt đầu lớn tiếng quát tháo. Đúng như tôi nghĩ, tài mồm mép của hắn phải gấp đôi tôi là ít.",
    # 26 (P27)
    "“Tao đã cố thuyết phục nó gia nhập Hiệp hội vì nó vừa là trẻ vị thành niên vừa là cấp S. Tao đã bảo với nó rằng nếu thiên hạ biết một đứa trẻ chẳng có gì trong tay lại là Thợ săn cấp S, thì ngay cả gia đình nó cũng đừng hòng được an toàn.”",
    # 27 (P28)
    "…Tôi nhớ lại hình ảnh Yoohyun-ie, đứa em bặt vô âm tín mấy ngày trời rồi xuất hiện và lạnh lùng quay lưng lại với tôi. Hóa ra chính lũ khốn ở Hiệp hội đã phun ra những lời rác rưởi đó sao? Dĩ nhiên, bọn chúng nói không hề sai. Nếu Yoohyun-ie và tôi cứ tiếp tục thân thiết với nhau, chắc chắn sẽ có kẻ bắt tôi làm con tin để tạo đòn bẩy uy hiếp Thợ săn cấp S không một chỗ dựa này.",
    # 28 (P29)
    "Nhưng dù vậy, đe dọa một đứa trẻ như thế ư? Đó có phải việc mà một người lớn nên làm không hả?",
    # 29 (P30)
    "“Như chính mồm mày vừa nói đấy, thằng khốn, nó chỉ là một đứa trẻ con thôi. Thế mà mày lại dám lôi gia đình ra để ép nó phải cúi đầu trước mày sao? Đúng là cái đồ súc sinh chó đẻ.”",
    # 30 (P31)
    "Nghĩ đến cảnh hắn nhắm vào điểm yếu hòng khiến một đứa trẻ phải chùn bước, tôi cảm thấy tởm lợm không sao tả xiết. Kể cả người lớn đem gia đình của người lớn khác ra làm con tin đã là đê tiện lắm rồi, đằng này lại nhắm vào một đứa trẻ vị thành niên? Máu trong người tôi sôi sục lên. Thằng chó chết đó vẫn tiếp tục buông lời khiêu khích.",
    # 31 (P32)
    "“Mày có biết thằng ranh ngu xuẩn đó đã phá tan tành khu lưu trú tạm thời dành cho Thức tỉnh giả cấp cao và thậm chí còn đánh gục toàn bộ Thợ săn trực thuộc Hiệp hội không hả? Bọn tao đã cố thuyết phục nó một cách tử tế nhất có thể rồi đấy. Mẹ kiếp, thế rồi thằng khốn đó tuyên bố nó sẽ tự lập hội riêng và dọa sẽ giết sạch bọn tao nếu dám cản đường nó-.”",
    # 32 (P33)
    "“Thế thì nó làm tốt lắm.”",
    # 33 (P34)
    "Yoohyun-ie nhà chúng tôi thông minh thật đấy. Trước khi nhận được sự giúp đỡ của Seok Simyung, tôi từng rất lo lắng không biết làm sao thằng bé có thể tự mình chuẩn bị để lập hội, thế mà thằng chó chết trước mặt tôi đây lại dám định giở thói bắt nạt nó. Thật mừng vì thằng bé đã không phải chịu đựng bất công từ hắn.",
    # 34 (P35)
    "“Mày thất bại trong việc đem gia đình ra làm con tin, và cuối cùng nó lại là một Thợ săn cấp S chẳng có lấy một điểm yếu, nên chắc lúc đó bọn mày hoảng loạn phát điên lên rồi nhỉ? Sơ sểnh một cái là cả lũ mất mạng, mà có trốn ra nước ngoài thì cũng chẳng ai thèm chào đón, nên muốn sống thì chỉ có nước ngoan ngoãn đi dọn bãi chiến trường cho em trai tao thôi. Thực sự cảm ơn vì chuyện đó nhé.”",
    # 35 (P36)
    "Kiểu đe dọa liều mạng đó sẽ không còn tác dụng một khi hội đã được thành lập vững chắc. Bởi vì nó có thể gây ảnh hưởng xấu tới hội bất cứ lúc nào. Nhưng trước thời điểm đó, ừ thì, thằng bé chẳng có gì để mất, dù bọn chúng có gào lên cho cả thế giới biết đi chăng nữa. Dù có khả năng điều đó sẽ bị xem là điểm yếu sau khi hội thành lập, nhưng chẳng phải Seok Simyung sẽ giải quyết ổn thỏa mấy chuyện như vậy sao?",
    # 36 (P37)
    "Wanyong vẫn không ngừng tuôn ra những lời nguyền rủa. Mắt tôi đảo quanh, quan sát kỹ khung cảnh xung quanh. Hai Thợ săn đang đứng gác trước cửa ra vào. Bên cạnh họ, Sở Hoa Vân trông có vẻ chán chường. Ngoài ra còn một người đứng cạnh bàn, nhưng không ở quá gần chúng tôi. Người đó trông cũng chẳng giống Thợ săn cấp cao cho lắm.",
    # 37 (P38)
    "“Thế này nhé, Wanyong-ssi, ông vẫn còn giữ liên lạc với bên Hàn Quốc chứ? Hiệp hội đã được thanh trừng rồi, nhưng chúng tôi vẫn chưa lật tung mọi ngóc ngách lên được, nên tôi thấy lo lắm đấy.”",
    # 38 (P39)
    "Chỉ mới xử lý được những bộ phận cốt cán mà thôi. Dù sau đó đã có những đợt dọn dẹp nội bộ, nhưng quét sạch mọi thứ là điều bất khả thi. Góc bàn bằng sắt. Liệu có hiệu quả không nhỉ? Đáng ra mình nên chăm chỉ rèn luyện thân thể hơn một chút.",
    # 39 (P40)
    "“Dù sao thì tôi cũng khó mà trốn thoát khỏi đây được, vậy nên làm ơn nói cho tôi nghe xem nội gián là ai đi nào. …À, tư thế này khó chịu quá đấy.”",
    # 40 (P41)
    "Miệng lẩm bẩm ‘buông cổ áo tôi ra’, tôi thuận thế ngồi bệt luôn lên mặt bàn.",
    # 41 (P42)
    "“Mày nghĩ tao sẽ nói cho mày biết chắc? Nhưng mà này Giám đốc Han, ít ra tao cũng có thể cho mày vài lời khuyên đấy.”",
    # 42 (P43)
    "Hừm, đây có phải là cái kiểu đó không nhỉ? Kiểu kẻ phản bội đổi phe trước rồi giở giọng ‘này, nếu muốn yên thân thì~’, đại loại thế. Đôi khi tôi cũng từng thấy cái màn làm bộ làm tịch thân thiện này rồi.",
    # 43 (P44)
    "Dù sao đi nữa, thằng khốn này chắc chắn sẽ tiếp tục ăn cắp thông tin từ Hàn Quốc, và hơn hết là hắn đã dám đe dọa đứa em trai bé bỏng của tôi.",
    # 44 (P45)
    "“Nói thật nhé, một người muốn cho lời khuyên mà lại đi gây sự thế à? Ông làm việc tệ hại thật đấy.”",
    # 45 (P46)
    "“Rõ ràng là mày gây sự trước đấy chứ! Bám đít lũ cấp S cho đẫy vào để rồi cuối cùng bị lôi đầu đến tận đây, tao chỉ muốn xem-.”",
    # 46 (P47)
    "Tôi ngả mạnh nửa thân trên ra sau. Lưng tôi vừa chạm mặt bàn, thằng chó chết đang túm cổ áo tôi liền lảo đảo mất đà. Cùng lúc đó, tôi đạp mạnh chân vào mép bàn, tung một cú đá bốc lên. Đầu gối co lại của tôi nện thẳng vào gáy thằng súc sinh, rồi cả người tôi lộn vòng như đang nhào lộn, đầu gối tôi—cùng với cần cổ của thằng khốn—dập mạnh vào góc bàn sắt.",
    # 47 (P48)
    "Rầm!",
    # 48 (P49)
    "Cùng với âm thanh đó, tôi nghe thấy tiếng xương cổ hắn gãy rắc. Một Thợ săn Trung Quốc lao vội tới tóm lấy tôi nhưng đã muộn. Thi thể của Wanyong-ssi trượt khỏi mặt bàn rồi gục ngã đổ sụp xuống.",
    # 49 (P50)
    "“Mau gọi trị liệ—Không, hắn chết ngay lập tức rồi!”",
    # 50 (P51)
    "Chỉ riêng một cú thúc gối thôi đã đủ nguy hiểm rồi. Lại thêm sự trợ lực từ chiếc bàn sắt, nếu tôi ra đòn chuẩn xác thì một Phi thức tỉnh giả khó lòng mà sống sót nổi. Sở Hoa Vân thong thả bước lại gần, lấy mũi chân hích nhẹ vào Wanyong-ssi đang nằm dưới đất. Sau đó, hắn chuyển ánh nhìn sang tôi. Tôi nở một nụ cười như muốn hỏi xem hắn có ý kiến gì với chuyện này không.",
    # 51 (P52)
    "“Ngươi tàn nhẫn hơn vẻ bề ngoài đấy.”",
    # 52 (P53)
    "“Có lý do gì để giữ mạng cho một thằng chó chết bán nước cầu vinh à? Chưa kể, hắn còn dám đụng đến em trai tôi nữa.”",
    # 53 (P54)
    "Nếu để hắn sống, biết đâu hắn lại nhúng tay vào các phương án tác chiến mà phía Hàn Quốc đang triển khai để giải cứu tôi. Tốt nhất là tôi nên trừ khử hắn ngay khi có cơ hội. Sở Hoa Vân vươn tay ra túm chặt lấy gáy tôi. Như thể đang xách một con chuột cống, hắn dễ dàng nhấc bổng tôi lên rồi quăng mạnh xuống đất.",
    # 54 (P55)
    "“A, mẹ kiếp.”",
    # 55 (P56)
    "Đau điếng người đấy chứ chẳng đùa. Cổ tay bị trói quặt ra sau lưng nên tôi chỉ có thể đập người xuống sàn trong tư thế hoàn toàn không chút phòng bị.",
    # 56 (P57)
    "“Một Thợ săn cấp F Thức tỉnh còn chưa đầy nửa năm, kẻ luôn được Hội trưởng Hội Haeyeon bảo bọc che chở từng chút một. Lại còn là hệ hỗ trợ đặc thù nữa chứ. Vậy mà ngươi lại giết người cứ như không vậy.”",
    # 57 (P58)
    "“Tôi Thức tỉnh chưa được bao lâu thật, nhưng những khó khăn gian khổ tôi từng nếm trải đâu chỉ có vài ba thứ. Trước đó tôi cũng từng sống một cuộc đời trầy trật lắm rồi. Kể cả về khoản bị bắt cóc thì tôi cũng thuộc hàng lão làng rồi đấy.”",
    # 58 (P59)
    "Nếu cộng thêm cả những lần trước khi hồi quy thì đếm hết mười ngón tay cũng chẳng đủ.",
    # 59 (P60)
    "“Và cho dù tôi có thể nhẫn nhịn mọi thứ khác đi chăng nữa, tôi cũng tuyệt đối không tha cho kẻ nào dám động vào em trai tôi—vào lũ trẻ nhà tôi.”",
    # 60 (P61)
    "Ánh mắt tôi chạm phải cái nhìn lạnh tanh đang dán chặt từ trên cao xuống.",
    # 61 (P62)
    "“Nếu dám đụng tới bọn trẻ nhà tôi, thì dù là cấp S hay là thứ gì đi nữa, các người cũng phải chết.”",
    # 62 (P63)
    "Sở Hoa Vân bật cười không thành tiếng, có lẽ hắn nghĩ tôi chỉ đang nói khoác. Nhưng tôi hoàn toàn nghiêm túc đấy. Rồi thằng khốn đó nhẹ nhàng đặt một bàn chân lên chân phải của tôi.",
    # 63 (P64)
    "“Có kẻ chết ngay dưới sự giám sát của ta, vậy nên ngươi phải trả giá.”",
    # 64 (P65)
    "“Nói xàm, anh có thèm bận tâm việc hắn sống hay chết đâu chứ.”",
    # 65 (P66)
    "Chúng tôi đứng cách nhau một đoạn và hắn thì nhìn đi chỗ khác, nhưng hắn mang danh hiệu cấp S cơ mà. Nếu hắn muốn ngăn tôi lại thì đâu phải không làm được, thế mà hắn lại lê bước chậm như rùa bò, đến một bên chân mày cũng chẳng buồn nhấc lên—giờ lại nói cái giọng gì thế không biết? Nhưng Sở Hoa Vân thậm chí còn chẳng buồn giả vờ lắng nghe tôi.",
    # 66 (P67)
    "“……!”",
    # 67 (P68)
    "Chân hắn bắt đầu dồn lực ép xuống. Trong tích tắc, khúc xương chân tôi gãy rắc. Thoáng chốc, tầm nhìn của tôi trắng xóa. Tôi nghiến chặt răng, rít lên một hơi buốt nhói khi hắn nhấn sâu xuống hơn nữa như muốn nghiền nát vụn khúc xương đã gãy.",
    # 68 (P69)
    "“Á, ự! Mẹ kiếp…….”",
    # 69 (P70)
    "Toàn thân tôi run rẩy dữ dội vì cơn đau đớn tột cùng. Không tự chủ được, các ngón tay tôi cào cấu loạn xạ xuống mặt sàn. Thằng khốn điên khùng này, ư…….",
    # 70 (P71)
    "Bàn chân đang đè nghiến lên chân tôi vừa dời ra, thì thằng khốn liền rút một lọ thuốc hồi phục ra. Khi nhìn thấy nó, một luồng khí lạnh chạy dọc sống lưng tôi.",
    # 71 (P72)
    "“K─ Khoan đã! Nếu giờ anh─ dùng thuốc hồi phục thì…….”",
    # 72 (P73)
    "Nếu dùng thuốc hồi phục dưới cấp cao cho một khúc xương không chỉ đơn thuần là bị gãy mà đã vỡ vụn thành từng mảnh, vết thương sẽ không thể lành lặn như cũ được. Bởi vì nó sẽ phục hồi trong tình trạng biến dạng méo mó, khiến việc chữa trị dứt điểm sau này càng trở nên khó khăn hơn gấp bội. …Đó là sự thật mà tôi đã đúc kết được từ chính kinh nghiệm xương máu của mình.",
    # 73 (P74)
    "Nhưng thằng khốn đó cứ thế dốc thẳng lọ thuốc hồi phục lên chân tôi. Cơn đau có dịu đi nhưng không biến mất hoàn toàn. Tôi gồng chân bị thương lên, cố thử cử động nó.",
    # 74 (P75)
    "“…Ư.”",
    # 75 (P76)
    "Cơn đau buốt nhói nhức nhối chạy dọc khắp người. Đúng là một thằng chó đẻ không hơn không kém.",
    # 76 (P77)
    "“Ta sẽ đưa ngươi đến nơi ngươi sẽ sống kể từ giờ. Đi theo ta.”",
    # 77 (P78)
    "Thằng khốn sải bước ngang qua tôi rồi tiến về phía cửa. Này, cái thằng chó đẻ kia!",
    # 78 (P79)
    "“Tôi còn chẳng đứng dậy nổi nữa là, anh có biết không hả?!”",
    # 79 (P80)
    "“Vậy thì bò đi.”",
    # 80 (P81)
    "Cái cách hắn nhìn xuống tôi khiến tôi cảm thấy tởm lợm kinh khủng. So với thằng khốn này thì Sigma còn tử tế chán. Mà đồ ăn bên đó cũng ngon hơn cái chỗ này nữa. Tôi thực sự nhớ Moon của chúng tôi quá chừng.",
    # 81 (P82)
    "“Người ta bảo suy bụng ta ra bụng người—anh tưởng tôi là chó chắc, chỉ vì bản thân anh là một con chó à? Bảo tôi bò á, nói nhảm cái đéo gì thế. Gâu gâu. Tao vừa mới chửi mày đấy. Mày nghe hiểu tao nói gì không?”",
    # 82 (P83)
    "Đôi mày của Sở Hoa Vân hơi nhíu lại.",
    # 83 (P84)
    "“Không hiểu à? Nếu không phải là thằng chó thì… meo meo? Meooo. Nếu không phải tiếng này thì là tiếng gì? Be eee?”",
    # 84 (P85)
    "“Đỡ nó dậy.”",
    # 85 (P86)
    "Một Thợ săn Trung Quốc đỡ tôi dậy theo lệnh của Sở Hoa Vân. Khi tôi vừa đặt bàn chân phải chạm đất, một cơn đau khủng khiếp liền ập tới. Sở Hoa Vân đã tiến lại gần cửa. Không, làm sao tôi đi đượ……",
    # 86 (P87)
    "Bàn tay của tên Thợ săn Trung Quốc đẩy mạnh vào lưng tôi, giục giã tôi bước tiếp. Theo phản xạ tôi bước lên một bước, và rồi—rầm một cái—cả người tôi ngã nhào về phía trước.",
    # 87 (P88)
    "“Tôi không đi nổ-.”",
    # 88 (P89)
    "“Đứng dậy.”",
    # 89 (P90)
    "Một mệnh lệnh lạnh như băng được ban ra. Cái gì chứ… ôi trời đất ơi. Kể cả trong số tất cả những thằng chó chết mà tôi từng gặp, cái thằng khốn này cũng phải xếp vào hàng top đầu. Hèn chi đến cả Park Hayool cũng phải cẩn trọng nhìn sắc mặt hắn; hắn ta đích thị không phải là một thằng điên tầm thường. Một lần nữa, tôi lại gượng dậy rồi nghiến răng bước tiếp một bước, để rồi ngã quỵ xuống khi còn chưa đi nổi hai bước chân.",
    # 90 (P91)
    "“Đứng dậy.”",
    # 91 (P92)
    "A, muốn về nhà quá đi mất.",
    # 92 (P93)
    "“Đặc khu Hồ Sào là nơi giam giữ những Thức tỉnh giả cần được giám sát và theo dõi đặc biệt.”",
    # 93 (P94)
    "Thằng khốn Sở Hoa Vân bất ngờ giới thiệu vòng quanh cho tôi một cách khá tử tế. Bỏ qua cái sự thật là hắn đang cưỡng ép lôi một người đi đứng khó khăn đi khắp nơi, thì thỉnh thoảng hắn cũng đề cập đến vài điều mà tôi cần phải dỏng tai lên mà nghe kỹ.",
    # 94 (P95)
    "“Đặc biệt, Cơ sở Quản lý Thức tỉnh giả Đặc biệt số 1 trên Đảo Mẫu Sơn[2] là nơi giam giữ những Thức tỉnh giả sở hữu các kỹ năng quý hiếm hoặc quan trọng.”",
    # 95 (P96)
    "Gì đây, hắn đang bảo tôi hãy cuỗm bọn họ đi đấy à? Nhưng công tác giám sát ở đây chắc chắn là vô cùng nghiêm ngặt. Chỉ riêng nơi này hiện đã có tới ba Thợ săn cấp S túc trực, bao gồm cả Sở Hoa Vân và người được gọi là Quan Nương Tử. Nghe nói bọn họ làm việc theo ca luân phiên, nhưng lúc nào cũng có từ ba người trở lên sẵn sàng nhận lệnh. Thêm vào đó, hắn còn nói rằng trong trường hợp khẩn cấp, họ có thể yêu cầu chi viện từ Thượng Hải.",
    # 96 (P97)
    "‘Thượng Hải là một thành phố cực kỳ rộng lớn, nên chắc chắn họ phải có ba đến bốn người cấp S.’",
    # 97 (P98)
    "Chỗ đó cách đây bao xa nhỉ? Tạm thời thì tôi phải tính đến trường hợp có từ bảy Thợ săn cấp S trở lên có thể tập hợp lại chỉ trong vòng vài giờ đồng hồ. Ngược lại, số Thợ săn cấp S từ phía phe chúng tôi tới đây… cùng lắm chỉ được năm người là cùng? Vì vẫn phải có vài người ở lại trông chừng Hàn Quốc nữa.",
    # 98 (P99)
    "“Đây là nhà hàng thứ hai.”",
    # 99 (P100)
    "“…Tôi không hứng thú.”",
    # 100 (P101)
    "Thả tao ra đi, thằng chó chết. Lưng tôi ướt đẫm mồ hôi lạnh. Sở Hoa Vân quay sang nhìn tôi rồi mỉm cười.",
    # 101 (P102)
    "“Nếu ngươi có thể điều chỉnh kỹ năng Kháng Độc của mình, ta sẽ cho ngươi thuốc giảm đau.”",
    # 102 (P103)
    "“Tôi không làm được. Hơn nữa, cớ sao tôi phải tin anh mà uống chứ? Anh thực sự nghĩ tôi là một con chó đấy à?”",
    # 103 (P104)
    "Không, kể cả chó cũng chẳng thèm ăn. Làm sao tôi biết được đó là thuốc giảm đau thật, hay lại là loại thuốc nói thật hoặc thứ dược phẩm đáng ngờ nào khác chứ? Làm sao tôi có thể dễ dàng nhận lấy được? Thằng khốn Sở Hoa Vân lại cất bước đi tiếp. Vừa quay người lại, tôi lại ngã nhào thêm lần nữa. Tôi chẳng nhớ nổi đây đã là lần thứ bao nhiêu rồi. Chẳng lẽ khắp người tôi lại không bầm dập hết cả rồi sao?",
    # 104 (P105)
    "‘Hắn đang muốn bẻ gãy ý chí của mình, thằng chó chết tiệt.’",
    # 105 (P106)
    "Nếu tôi chỉ cần khóc lóc van xin rằng mình đã sai rồi, có lẽ lúc này hắn sẽ tha cho tôi. Làm vậy thì dễ dàng hơn nhiều, nhưng mà─ mẹ kiếp. Hắn có mơ đi.",
    # 106 (P107)
    "Tôi bị lôi xềnh xệch từ bên trong tòa nhà ra cả bên ngoài. Mặt trời đã lặn tự lúc nào và những cơn gió lạnh từ mặt hồ thổi tạt qua cơ thể tôi. Cầu thang, mấy cái bậc cầu thang khốn kiếp này. Dẫu vậy, nếu thấy đầu tôi sắp va vào gờ bậc thang thì bọn họ vẫn đưa tay ra đỡ lấy. Tôi lê bước lên cầu thang, gần như là vừa ngã vừa lết lên, rồi đứng trên đài quan sát nhìn ra mặt hồ. Không, chính xác là tôi ngã quỵ xuống.",
    # 107 (P108)
    "Co ro tựa vào lan can, tôi trừng mắt lườm thằng chó điên đó.",
    # 108 (P109)
    "“Hóa ra anh có năng khiếu tra tấn người khác nhỉ?”",
    # 109 (P110)
    "Hắn không đơn thuần chỉ gây đau đớn cho tôi, mà còn khiến tôi kiệt sức hoàn toàn. Sở Hoa Vân tựa lưng vào lan can rồi lấy ra một thứ trông giống như điếu xì gà. Thuốc lá dành cho Thức tỉnh giả cấp cao đã xuất hiện ở Trung Quốc rồi sao? Hay hắn chỉ đang làm màu để tạo không khí thôi? Với những động tác thuần thục, hắn cắt đầu điếu, châm lửa rồi ngậm vào miệng.",
    # 110 (P111)
    "“Chúng ta sẽ còn phải nhìn mặt nhau dài dài, nên ta muốn đảm bảo rằng điều này sẽ khắc sâu vào tâm trí ngươi.”",
    # 111 (P112)
    "“Khắc sâu á? Anh làm tôi buồn cười quá đấy.”",
    # 112 (P113)
    "Tôi khịt mũi một cái. Hắn mơ mộng hão huyền thật đấy.",
    # 113 (P114)
    "“Khi tôi trở về nhà, tôi sẽ được chữa trị khỏi hoàn toàn và sống một cuộc sống êm ấm. Cứ thử thoải mái đi, nhưng ba cái trò này chẳng là cái thá gì đâu. Thực sự chẳng bõ dính răng đâu nhé.”",
    # 114 (P115)
    "Trên đời này chỉ có duy nhất một người có thể khiến trái tim tôi tổn thương sâu sắc đến mức không thể nào lành lại được mà thôi. So với chuyện đó, ba cái thứ này thực sự chẳng đáng là bao. Tôi nheo mắt, nhìn chằm chằm vào mặt nước đen kịt đang gợn sóng lăn tăn qua khe lan can. Ánh đèn từ chòi canh rọi sáng, quét dài ra xa rồi lướt đi.",
    # 115 (P116)
    "Không biết giờ này mọi người đang làm gì nhỉ.",
    # 116 (P117)
    "[1] Nhân vật hư cấu Lee Wanyong trùng tên với chính khách người Hàn Lee Wanyong (Lý Hoàn Dụng), người (cùng với bốn người khác, thường được gọi là Ất Tỵ Ngũ Tặc) đã ký Hiệp ước Sáp nhập Nhật - Triều cùng các hiệp ước tiếp theo đặt Triều Tiên dưới ách thống trị của thực dân Nhật Bản. Cái tên này gần như đồng nghĩa với từ \"kẻ phản bội/bán nước\".",
    # 117 (P118)
    "[2] Bản gốc viết là 노산도 (Nosan-do), tác giả Geunseo có lẽ đang ám chỉ hòn đảo có thật ngoài đời là Đảo Mẫu Sơn (姥山岛, Mǔshān-dǎo), một trong hai hòn đảo nằm trên Sào Hồ (巢湖, Cháo-hú). Tên đảo này nếu phiên âm chính xác hơn sang tiếng Hàn sẽ là 모산도 (Mosan-do), do sử dụng âm đọc Mǔ của chữ 姥 tương ứng với âm Mo trong tiếng Hàn. Âm No mà tác giả dùng bắt nguồn từ âm đọc khác của chữ 姥 là Lǎo, tương ứng với âm Ro trong tiếng Hàn rồi chuyển thành No khi đứng đầu từ."
]

with open('scratch/paragraphs_vi.json', 'w', encoding='utf-8') as f:
    json.dump(paragraphs_vi, f, ensure_ascii=False, indent=2)

with open('scratch/354-vi.md', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(paragraphs_vi))

print(f"Saved {len(paragraphs_vi)} paragraphs to scratch/354-vi.md")
