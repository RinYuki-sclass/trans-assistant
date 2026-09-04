import os
import json

with open('scratch/paragraphs.json', 'r', encoding='utf-8') as f:
    kr_paras = json.load(f)

print(f"Total KR paragraphs: {len(kr_paras)}")

vi_paras = [
    # 1
    "‘Thợ săn cấp S sao.’",
    # 2
    "Nghe nói ở đây có từ ba Thợ săn cấp S trở lên thường trú. Một là thằng Sở Hoa Vân, một người khác là Quan Nương Tử vừa thoáng thấy ở sân bay, vậy thì ắt phải còn một người nữa. Tôi đoán người còn lại chính là gã đàn ông trước mắt này.",
    # 3
    "Dù đang ngồi xổm nhưng vóc dáng gã vẫn đồ sộ đến phát khiếp, chiều cao trông chừng phải tầm 2 mét hoặc hơn. Bảo là người châu Á thì lại có cảm giác hơi lai một chút. Màu tóc cũng ngả sang nâu. Bề ngoài trông có vẻ tính tình không đến nỗi tệ, thế nhưng...",
    # 4
    "Tôi bước tới mép bể bơi, vươn tay về phía gã đàn ông.",
    # 5
    "“Sao anh cứ đứng nhìn trơ ra thế?”",
    # 6
    "“Hử?”",
    # 7
    "“Ai đó đã bẻ gãy chân tôi nên tôi không tự trèo lên được đâu. Chẳng lẽ anh vẫn chưa nghe nói sao?”",
    # 8
    "Thật ra cũng không hẳn là bất khả thi, nhưng chắc chắn sẽ khá chật vật. Nếu là Sở Hoa Vân, hẳn hắn sẽ cấm tiệt đám binh lính giúp đỡ rồi đứng khoanh tay thưởng ngoạn cảnh tôi còng lưng chật vật trèo lên, nhưng người này thì sao đây? Khi tôi nhìn chằm chằm vào gã, gã bật cười khẩy một tiếng rồi túm lấy tôi, một hơi kéo bổng lên khỏi bể bơi.",
    # 9
    "“Cảm ơn anh.”",
    # 10
    "Tạm thời xem ra thuộc phe ôn hòa. Bước ra khỏi làn nước âm ấm khiến tôi thấy hơi lạnh. Tôi ngước nhìn gã đàn ông cao lớn hơn mình một cái đầu.",
    # 11
    "“Làm phiền anh lấy giúp tôi đôi nạng được không?”",
    # 12
    "Gã chẳng nói chẳng rằng, mang luôn cả đôi nạng tới cho tôi. Thật lòng cảm ơn vì đã đối xử với tôi như một con người.",
    # 13
    "“Mai tôi lại đến. Ở ngoan nhé nhóc.”",
    # 14
    "- Kyooc!",
    # 15
    "Sau khi chào Thủy Long, tôi quay lại nhìn gã đàn ông.",
    # 16
    "“Xin chào, tôi là Han Yoojin. Chắc hẳn anh cũng biết rồi.”",
    # 17
    "“Hoàng Lâm.”",
    # 18
    "Ánh mắt gã nhìn tôi có pha chút tò mò. Đó là vẻ mặt nhìn một đối tượng dễ xơi và vô hại, không mảy may có chút phòng bị nào. Mà chuyện đó cũng là lẽ đương nhiên thôi.",
    # 19
    "‘Khác với Sở Hoa Vân, người này xem ra còn nói chuyện được.’",
    # 20
    "Sở Hoa Vân là cái thằng mà dù tôi có nói gì đi chăng nữa, hắn cũng sẽ coi như chó sủa ngang tai rồi bỏ ngoài tai hết. Cứ nhìn việc bị chửi mà mặt hắn chẳng thèm biến sắc, thay vào đó lại giáng hình phạt xuống là đủ biết hắn tuyệt đối không xem tôi như một con người đồng đẳng. 'Con chó định cắn càn à, thế thì phải huấn luyện lại thôi'. Cảm giác chính là như vậy đấy.",
    # 21
    "Một đối tượng không thể giao tiếp. Về sức mạnh thì tôi không thể với tới gót chân hắn, nếu đến cả lời nói cũng không thông thì tôi hầu như chẳng thể làm được trò trống gì. Bởi vậy nên tôi mới cố tình tỏ ra ương bướng hơn. Nhằm mục đích khiến hắn phải để tâm đến sự hiện diện của tôi thêm một chút.",
    # 22
    "Dĩ nhiên, một phần cũng vì tôi thấy tởm lợm nếu phải cúi đầu khuất phục.",
    # 23
    "“Anh là Thợ săn cấp S à? Tôi nghe nói ở đây có ba người.”",
    # 24
    "“Đúng thế. Nghe bảo cậu bắt nạt đám lính hả?”",
    # 25
    "Đột nhiên nói cái thứ xàm xí gì vậy trời.",
    # 26
    "“Chẳng phải là ngược lại sao. Anh nhìn bộ dạng của tôi đi này.”",
    # 27
    "“Trông chẳng khác nào con trĩ non rơi xuống nước.”",
    # 28
    "Trĩ non cái nỗi gì. Hoàng Lâm vén vạt áo ướt sũng của tôi lên xem rồi tặc lưỡi chậc chậc.",
    # 29
    "“Ngã cầu thang hay sao thế này. Cần thuốc không?”",
    # 30
    "“Cái thân xác này của tôi không được tùy tiện dùng thuốc hay kỹ năng trị liệu đâu. Vậy nên phiền anh chuyển lời bảo tên họ Sở nương tay một chút.”",
    # 31
    "“Nó có thèm nghe lời tôi đâu.”",
    # 32
    "“Tính nết gì mà kỳ quặc thế không biết.”",
    # 33
    "“Vì là con trai một của nhà quyền quý đấy.”",
    # 34
    "Hoàng tử cơ đấy. Người ta gọi là 'tiểu hoàng đế' phải không nhỉ? Nhưng tôi đồ rằng trong số đó cũng phải sinh ra trong một gia đình giàu nứt đố đổ vách kèm theo cái tính nết bẩn thỉu trời sinh thì mới nặn ra nổi một thằng như thế.",
    # 35
    "“Cứ để thế này thì cảm lạnh mất, tôi thay quần áo trước được chứ?”",
    # 36
    "Tôi chống nạng cất bước, vừa cau mày nhìn đám binh lính đang đứng trơ như phỗng.",
    # 37
    "“Mấy người tới đây để quản lý tôi chẳng phải sao? Thuần hóa Thủy Long thì ít nhất cũng phải đoán được là sẽ bị nước bắn tung tóe chứ, cớ sao lại đi tay không thế hả? Đúng là cái đồ quân đội nhà Đường [1], à mà đây là Trung Quốc nên đúng là quân Đường thật. Nếu tôi ngã bệnh liệt giường làm tiến độ huấn luyện gặp trục trặc thì là trách nhiệm của các anh đấy. Rõ chưa?”",
    # 38
    "Nghe đến hai chữ 'trách nhiệm', đám binh lính liền luống cuống bảo rằng sẽ mang khăn tắm và quần áo khô đến cho cậu ngay.",
    # 39
    "“Bắt nạt người ta rõ ràng thế còn gì.”",
    # 40
    "Hoàng Lâm vỗ nhẹ vào vai tôi một cái rồi nói. Bảo là vỗ nhẹ chứ tôi suýt nữa thì ngã nhào. Tay gã to như cái nắp vung nồi vậy.",
    # 41
    "“Ai bảo các anh ấy không làm tròn bổn phận chứ.”",
    # 42
    "“Cậu thì mong đợi gì ở binh lính chứ. Thông thường cứ ra lệnh sao thì làm đúng ngần ấy thôi. Mà điều đó còn được khuyến khích nữa kìa. Tốt nhất là quân Tốt chỉ cần làm đúng những gì được bảo.”",
    # 43
    "Đúng là như vậy thật. Không phải nơi nào khác mà lại là quân đội, một người lính hay hành động bộc phát thì dù năng lực cá nhân có xuất chúng đến đâu, đối với chỉ huy cũng chỉ là cục nợ đau đầu mà thôi. Dù rằng nhân vật như thế lên phim làm nhân vật chính thì hợp lắm đấy.",
    # 44
    "“Cái ngữ mồm mép trơn tuột như cậu mà vào quân ngũ thì một là bị đá văng, hai là leo tót lên trên, chỉ có một trong hai đường đó thôi.”",
    # 45
    "“Dù vậy thì binh lính ở đây cũng là người thức tỉnh cả mà. Với lại tôi thấy dường như đều là cấp trung.”",
    # 46
    "“Vì là người thức tỉnh nên lại càng phải thắt chặt kỷ luật. Hơn nữa, những kẻ được điều đến tận đây thì cứ xem như linh kiện máy móc là được. Không nghĩ ngợi lan man, tuyệt đối trung thành với mệnh lệnh. Cho dù hôm nay bảo đào ao đổ đầy nước rồi ngày mai bảo lấp lại, chúng cũng sẽ tuân theo răm rắp không một lời dị nghị.”",
    # 47
    "Đúng chuẩn quân đội bình thường. Nói cách khác, cứ coi như từ Thợ săn cấp trung trở xuống toàn là những kẻ đầu óc cứng nhắc xơ cứng chứ gì.",
    # 48
    "Trong lúc đó, đám binh lính đã mang khăn và quần áo tới. Đúng chuẩn chỉ có ngần ấy thứ.",
    # 49
    "“…Không có nổi chút tinh tế mà đem theo một cái ghế à? Thấy người ta đang chống nạng thế này mà?”",
    # 50
    "Theo lẽ thường thì đứng thay quần khó lắm chứ bộ. Dù ngồi bệt xuống sàn cũng được đấy, nhưng ôi trời. Hoàng Lâm bảo 'Thấy chưa' rồi đỡ tôi thay đồ. Cũng tốt bụng gớm.",
    # 51
    "“Cứ thế này mà tôi nảy sinh tình cảm với anh là không ổn đâu đấy nhé. Tôi còn đang dự định vượt ngục cơ mà.”",
    # 52
    "“Tôi cũng tò mò không biết cậu định trốn thoát bằng cách nào đây.”",
    # 53
    "Hoàng Lâm vác tôi lên vai như một bao tải hàng. Thân hình to xác nên bờ vai cũng rộng thênh thang như Thái Bình Dương vậy. Gã sải những bước dài, leo cầu thang một lần hai ba bậc.",
    # 54
    "“Nói thật chứ bị đối xử tệ bạc thế này mà bảo tôi không bỏ trốn thì vô lý quá. Rốt cuộc tại sao lại làm vậy chứ? Nếu tôi bảo không nuôi được thú cưỡi rồi cứ thế chìa cổ ra thách giết thì tính sao đây? Rõ ràng đây đâu phải việc có thể cưỡng ép làm được.”",
    # 55
    "“Vì trên đời chẳng có ai là không bị khuất phục cả. Vả lại, bọn tôi còn có mục đích quan trọng hơn cả việc nuôi dưỡng thú cưỡi.”",
    # 56
    "Có mục đích khác sao?",
    # 57
    "“…Mục đích gì cơ? Chắc anh chẳng chịu nói cho tôi biết đâu nhỉ.”",
    # 58
    "“Bắt giết những Thợ săn Hàn Quốc đến cứu cậu.”",
    # 59
    "Trong khoảnh khắc, tôi nghẹn họng không thốt nên lời. Chính vì đó là lời thốt ra từ một kẻ từ nãy đến giờ luôn cư xử hòa nhã nên cảm giác như bị một vố trời giáng thẳng vào sau gáy càng thêm đau điếng.",
    # 60
    "“Đằng nào họ cũng sẽ đến cứu cậu thôi, chẳng phải sao?”",
    # 61
    "“Không, chuyện đó... cũng đâu có gì chắc chắn. Mà anh cứ thế bộc bạch hết ra như vậy có ổn không đấy?”",
    # 62
    "“Có gì mà phải bí mật. Đến con nít cũng đoán ra được. Họ đến thì sẽ đánh nhau, rồi một trong hai bên sẽ phải bỏ mạng thôi.”",
    # 63
    "Dù đúng là lời có lý thật, thế nhưng...",
    # 64
    "“Tự tin gớm nhỉ. Biết đâu họ có thể lén lút cướp riêng một mình tôi đi, hoặc là bên anh sẽ bị quét sạch thì sao.”",
    # 65
    "“Đừng lo. Bọn tôi sẽ cố gắng giữ em trai cậu sống sót để làm con tin. Mang toàn bộ thú cưỡi của hội Haeyeon sang đây, rồi cậu lại tiếp tục nuôi dưỡng để gia tăng chiến lực, sau khi dọn dẹp sạch sẽ Võ Lâm Minh thì sẽ nuốt trọn luôn cả Hàn Quốc vốn đã hao hụt Thợ săn cấp S, hình như kế hoạch là như thế đấy.”",
    # 66
    "Hóa ra là vì có một con tin hữu dụng nên việc tôi phản kháng hay bất mãn cũng chẳng thành vấn đề sao. Yoohyun thì đúng là rất thích hợp để làm con tin thật. Miễn là bắt sống được nó, vì là Thợ săn cấp S nên cũng không dễ chết... Khốn kiếp.",
    # 67
    "Tôi cố đè nén cơn cuộn trào ruột gan xuống. Làm sao có kẻ nào ở Trung Quốc đủ năng lực bắt sống được em trai tôi chứ. Vậy nên đó chỉ là ảo tưởng viển vông mà thôi.",
    # 68
    "“Hội trưởng hội Haeyeon chắc chắn sẽ đến, và nghe đâu khả năng cao là Sesung cũng sẽ tới, cậu nghĩ sao? Đứa bé hệ thủy của Haeyeon thì vì còn nhỏ nên hình như họ định dụ dỗ lôi kéo thử xem sao. Nó có đi cùng không nhỉ? Tôi thì chẳng hào hứng gì với việc đánh nhau với trẻ con đâu.”",
    # 69
    "“…Tôi không biết. Mà rốt cuộc lấy đâu ra cái sự tự tin đó vậy trời? Đâu phải cứ đông người hơn là nắm chắc phần thắng đâu chứ?”",
    # 70
    "“Thì có lợi thế hơn mà.”",
    # 71
    "…Ừ, nói cũng đúng. Thế nhưng tôi không hề nghĩ rằng Yoohyun hay Sung Hyunjae sẽ thua. Huống chi ở đây còn là hồ nước nữa chứ. Đây là môi trường mà ngay cả một mình Yerim cũng có thể cân nổi hai ba Thợ săn cấp S.",
    # 72
    "…Liệu ngoài ưu thế áp đảo về số lượng ra thì bọn họ còn có biện pháp đối phó nào khác chăng? Có thể là không có, nhưng lỡ có thì tính sao đây. Thế nhưng trước hồi quy, Trung Quốc đã tự sụp đổ vì nội chiến cắn xé lẫn nhau rồi mà. Vốn dĩ chẳng có gì ghê gớm cả. Đã từng không có, nhưng khả năng mọi chuyện bị thay đổi là hoàn toàn có thể xảy ra.",
    # 73
    "‘Ngục tối mà Noah-ssi và Liette tiến vào chẳng phải cũng thuộc về Trung Quốc sao.’",
    # 74
    "Biết đâu họ lại thu được những vật phẩm đặc thù hay danh hiệu từ loại ngục tối đặc biệt đáng lẽ chỉ xuất hiện ở một tương lai xa xôi nào đó. Người Mới hoàn toàn có thể lại mắc sai sót trong việc quản lý nữa mà. Dẫu vậy thì Yoohyun cũng đã mạnh hơn rất nhiều so với dòng thời gian gốc. Thằng bé có kỹ năng mới, và cấp bậc vũ khí cũng đã khác xưa.",
    # 75
    "“Này anh, đã trót làm phúc thì mở lòng nói tuốt tuột xem rốt cuộc các anh định bắt sống đứa em trai quý giá của người ta bằng cách nào đi chứ.”",
    # 76
    "“Không được đâu. Tôi cũng biết phân biệt lời nào nên nói, lời nào không nên nói mà.”",
    # 77
    "“Dù sao thì với sức lực của tôi thì làm được gì cơ chứ.”",
    # 78
    "“Cậu còn gọi điện thoại được cơ mà.”",
    # 79
    "“Tôi sẽ không gọi nữa đâu. Anh không cho phép thì tôi làm sao gọi được chứ.”",
    # 80
    "“Thế à.”",
    # 81
    "‘Chắc không phải đâu nhỉ’, Hoàng Lâm vừa cười vừa nhảy phắt lên tầng cầu thang cuối cùng. Rồi gã đặt tôi xuống và nói.",
    # 82
    "“Lát nữa tôi sẽ ra lệnh cho bọn họ không được phản ứng lại bất kỳ lời nào của cậu nữa.”",
    # 83
    "Hự.",
    # 84
    "“Kìa, anh cũng thấy rồi đấy thôi. Phải có tôi bảo thì chúng nó mới chịu làm việc đàng hoàng cơ mà.”",
    # 85
    "“Này.”",
    # 86
    "Hoàng Lâm chìa chiếc máy truyền tin ra trước mặt tôi.",
    # 87
    "“Cần thứ gì thật sự cần thiết thì cứ nói qua đây. Rồi tôi sẽ truyền đạt lại cho đám binh lính.”",
    # 88
    "Khốn kiếp, gã bịt luôn cả miệng tôi rồi. Thân hình to như gấu mà hóa ra lại là cáo già. Cái chiêu dọa dẫm 'Không nghe lời tôi mà lỡ tôi có mệnh hệ gì thì cấp trên của các người có để yên không hả~' vốn hiệu nghiệm là thế, vậy mà giờ bị bít mất đường dùng. Đương nhiên hễ còn mang tai thì bọn lính vẫn sẽ ít nhiều dao động, nhưng chắc chắn là chẳng dễ dàng gì.",
    # 89
    "Nếu đúng như lời Hoàng Lâm thì binh lính ở đây không giống như trên máy bay, hối lộ e rằng cũng chẳng ăn thua. Phiền phức thật rồi đây.",
    # 90
    "“Anh cũng gây ức chế hơn tôi tưởng đấy.”",
    # 91
    "Tôi giật lấy chiếc máy truyền tin rồi làu bàu, còn Hoàng Lâm thì nở một nụ cười trông có vẻ hiền từ.",
    # 92
    "“Với lại đừng có chọc giận thằng A Vân quá. Lúc tứ chi còn lành lặn thì phải biết giữ mình đi chứ.”",
    # 93
    "“…Trông tôi thế này mà anh bảo lành lặn đấy à?”",
    # 94
    "“Thì vẫn còn gắn trên người đấy thôi.”",
    # 95
    "Cái chốn này đúng là man rợ thật. Tôi thở dài thườn thượt rồi ngước nhìn Hoàng Lâm.",
    # 96
    "“Thường thì đạt đến tầm Thợ săn cấp S rồi chẳng ai muốn bị trói buộc vào những nơi như quân đội cả, anh không thấy bất mãn sao? Không nảy ra ý định tự lập hội riêng à? Hay là người nhà anh bị bắt làm con tin rồi?”",
    # 97
    "Sở Hoa Vân thì nghe bảo vốn cắm rễ trong quân ngũ từ đầu nên có thể hiểu được, nhưng gã đàn ông trước mắt tôi trông chẳng có vẻ gì là một người lính cả. Ngay cả bộ quần áo gã mặc cũng đâu phải quân phục.",
    # 98
    "“Tôi cũng ở trong quân ngũ từ trước khi thức tỉnh rồi.”",
    # 99
    "“…Thật á?”",
    # 100
    "“Vì tôi là con thứ trong một gia đình giàu có mà. Móc nối sẵn một chân trong quân đội thì làm gì cũng tiện. Cậu khích bác hay đấy, nhưng cuộc sống của tôi quá đỗi sung túc để mà nảy sinh bất mãn. Cái thân này từ lúc lọt lòng đã ngốn cả đống tiền của rồi.”",
    # 101
    "“À, vâng.”",
    # 102
    "Quả nhiên trông mặt mà chẳng bắt được hình dong. Hoàng Lâm bảo hẹn gặp lại sau rồi nghênh ngang rời đi. Dù vậy thì gã ta không giống Sở Hoa Vân, liệu có cơ hội để áp dụng từ khóa lên gã không nhỉ? Nếu sống trong nhung lụa ấm êm thì chắc cũng chẳng có ác cảm gì đặc biệt với người nuôi dưỡng đâu.",
    # 103
    "Còn Sở Hoa Vân thì e rằng đến cha mẹ ruột hắn cũng chẳng nương tay đâu. Linh cảm mách bảo tôi như vậy.",
    # 104
    "“Nếu còn định bắt làm việc tiếp thì ít ra cũng phải cho ăn cơm chứ. Da bụng sắp dán vào lưng rồi đây này.”",
    # 105
    "Nghe tôi nói, người lính lẳng lặng dẫn đường phía trước. Nơi tôi được dẫn đến là một nhà ăn. Không phải dành cho binh lính thông thường, mà là nhà ăn sĩ quan. Và ở nơi đó, thằng chó má đang ngồi chễm chệ.",
    # 106
    "“Ngồi xuống.”",
    # 107
    "“Ta ăn vào khéo lại nghẹn họng mất nên─”",
    # 108
    "“Ngươi thích sàn nhà hơn à.”",
    # 109
    "Phải rồi, thức ăn thì có tội tình gì đâu. Tôi bèn ngoan ngoãn đi lại ngồi vào chỗ theo lệnh hắn. Chẳng mấy chốc món ăn đã được dọn lên. Bên ngoài là trứng còn bên trong là cái thứ gì tôi cũng chịu, tóm lại chỉ vỏn vẹn đúng một miếng nằm chỏng chơ trên đĩa. Hương vị thì... cũng được đấy chứ. Rồi tiếp đó là bào ngư, hải sâm cùng một con cá hấp cỡ lớn, súp và các món khác lần lượt được bưng ra.",
    # 110
    "Nhìn chung hương vị tuy lạ lẫm và nồng đậm nhưng ăn cũng vừa miệng. Nói thật lòng thì khá là ngon.",
    # 111
    "“Ta ăn no nê rồi đấy, nhưng đột nhiên được tiếp đãi tử tế thế này khiến ta thấy nghi ngờ đấy.”",
    # 112
    "Dù tôi có hỏi xem rốt cuộc tâm tính hắn đổi khác thế nào đi nữa, thì ánh mắt Sở Hoa Vân hướng về phía tôi vẫn y như cũ. Hắn nhìn tôi thậm chí còn chẳng bằng một kẻ dưới trướng, mà chẳng khác nào đang nhìn một con thú hoang vừa mới bắt về cần phải thuần hóa. Biết thế lật bàn cho rồi.",
    # 113
    "“Con người thích nghi rất nhanh.”",
    # 114
    "Sở Hoa Vân đặt đôi đũa dài xuống rồi nói.",
    # 115
    "“Ngay cả với đau đớn, họ cũng thích nghi dễ dàng đến bất ngờ.”",
    # 116
    "“…Nghĩa là thân xác phải có lúc dễ chịu thì hành hạ mới càng thấy thống khổ hơn chứ gì, cái kiểu... Ôi trời, đúng là cái đồ chó má.”",
    # 117
    "Dù lời chửi thề buột miệng thốt ra, gã vẫn thản nhiên như không. Thay vào đó, một trong số những người lính đang túc trực liền tiến lại gần.",
    # 118
    "Bốp─!",
    # 119
    "Hắn giáng một cái tát nảy lửa vào má tôi. Hơi cáu rồi đấy nhé. Ngay cả trước hồi quy, vì sợ để lại dấu vết nên người ta cũng hiếm khi đánh vào mặt tôi cơ mà.",
    # 120
    "“Cảm ơn vì bữa ăn. Ta đi được chưa?”",
    # 121
    "Sở Hoa Vân gật đầu cho phép. Chốn này không thể ở lâu được, tuyệt đối không thể ở lâu. Lời Hoàng Lâm nói cũng khiến tôi canh cánh trong lòng. Trở về căn phòng được chỉ định cho mình, tôi cởi áo ngoài ra.",
    # 122
    "“Tôi vừa xuống bể bơi xong mới chỉ thay quần áo thôi nên muốn tắm rửa, mấy anh chuẩn bị giúp tôi được không?”",
    # 123
    "Tôi cất tiếng hỏi nhưng đám lính canh không buồn nhúc nhích lấy một sợi lông mày. Xem chừng mệnh lệnh của Hoàng Lâm đã được ban xuống rồi. Tôi cố tình thở dài thật lớn rồi dùng chiếc máy truyền tin Hoàng Lâm đưa để yêu cầu khăn tắm và đồ ngủ.",
    # 124
    "“Các anh cũng chẳng có ý định giúp tôi tắm rửa đâu nhỉ? Vâng, vâng.”",
    # 125
    "Bước vào phòng tắm, tôi khép hờ cửa lại rồi thò đầu ra nhìn đám lính canh.",
    # 126
    "“Đóng hẳn cửa nhé? Hay là cứ hé mở chừng này?”",
    # 127
    "“…….”",
    # 128
    "“A, rốt cuộc là sao chứ. Ít nhất cũng phải trả lời chừng này chứ.”",
    # 129
    "Thế mà chúng nó cũng phải cẩn thận hỏi lại cấp trên rồi mới bảo tôi cứ mở ra. Cửa phòng tắm dù hé mở đôi chút nhưng vị trí đó không nhìn thấy buồng tắm đứng được. Xem ra chúng cũng chẳng có ý định bước vào. Tôi vặn vòi hoa sen để tiếng nước chảy vang lên rồi đưa mắt dáo dác nhìn quanh.",
    # 130
    "‘Chắc là đã bám theo tới đây rồi.’",
    # 131
    "Tôi xé một mẩu giấy vệ sinh, rút bút ra viết chữ.",
    # 132
    "[Dokkaebi?]",
    # 133
    "Sau khi phe phẩy mẩu giấy vệ sinh một lát, từ góc buồng tắm đứng liền xuất hiện những bóng hình mờ ảo trăng trắng. Bọn chúng khẽ thì thào.",
    # 134
    "“Chào đại ca Kim!”",
    # 135
    "“Bọn tôi thấy rồi nhưng không mách đâu.”",
    # 136
    "“Tin được không?”",
    # 137
    "“Liệu có được không nhỉ?”",
    # 138
    "Bầy Dokkaebi cẩn trọng lên tiếng. Tôi cũng hạ giọng thật khẽ theo để tiếng nói chìm trong tiếng nước chảy, không lọt ra ngoài.",
    # 139
    "“Mấy đứa có biết Yoon Yoon không? Vua Dokkaebi ấy.”",
    # 140
    "Bầy Dokkaebi nhảy cẫng lên rồi làm động tác như thể lấy tay che miệng lại.",
    # 141
    "“Không được.”",
    # 142
    "“Không nói được đâu.”",
    # 143
    "“Không được đâu mà.”",
    # 144
    "Hóa ra là có biết. Nhưng tại sao lại không nói được chứ? Lẽ nào đã xảy ra chuyện gì với Yoon Yoon rồi sao?",
    # 145
    "“Tôi là bạn của Yoon Yoon đấy.”",
    # 146
    "“Thật không?”",
    # 147
    "“Con người ở đây nói dối giỏi lắm.”",
    # 148
    "“Đại ca Kim ở đây cũng nói dối rồi đấy thôi.”",
    # 149
    "“Tôi không nói dối đâu.”",
    # 150
    "Ít nhất thì với mấy đứa nhóc này tôi chưa từng nói dối. Còn Yoon Yoon thì... đúng là tôi có hơi lừa phỉnh một chút. Ừm. Hơn cả chuyện đó, xem ra bầy Dokkaebi đã gặp phải chuyện chẳng lành ở Trung Quốc rồi thì phải... Tôi nở một nụ cười tinh quái rồi thì thào với bọn chúng.",
    # 151
    "“Các cậu có muốn thử làm một trò thú vị không?”",
    # 152
    "“Trò thú vị á?”",
    # 153
    "“Gì thế?”",
    # 154
    "“Gì vậy?”",
    # 155
    "“Cũng chẳng có gì to tát đâu.”",
    # 156
    "Tôi lấy một quả bom từ kho đồ ra rồi lắc lắc trước mặt bọn chúng.",
    # 157
    "“Chỉ là trò đùa thổi bay hòn đảo này thôi mà~”"
]

print(f"Total VI paragraphs: {len(vi_paras)}")
assert len(kr_paras) == len(vi_paras), f"Mismatch: {len(kr_paras)} vs {len(vi_paras)}"

footer_note = """
---
[1] Quân đội nhà Đường (당나라 군대): Thành ngữ tiếng Hàn dùng để chỉ một đội quân hay tập thể vô kỷ luật, ô hợp và lỏng lẻo. Ở đây tác giả vừa dùng nghĩa bóng, vừa chơi chữ vì bối cảnh câu chuyện đang diễn ra ngay tại Trung Quốc."""

os.makedirs('output', exist_ok=True)
output_path = 'output/result_359-kr.txt'

lines_out = []
for kr, vi in zip(kr_paras, vi_paras):
    lines_out.append(f"KR: {kr}")
    lines_out.append(vi)
    lines_out.append("")  # Blank line between pairs

result_content = "\n".join(lines_out).rstrip() + "\n" + footer_note + "\n"

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result_content)

print(f"Successfully wrote {len(kr_paras)} pairs to {output_path}")
