# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_113\translation.md"

paras = [
    # 000
    "Mới có mấy ngày sau khi kết quả tuyển quân đợt hai được công bố, cái tên Alpha mặt trắng như thư sinh trước mắt này đã chạy tới đây rồi.",
    # 001
    "Người lính gác trước cổng trại dùng ánh mắt kỳ quặc đánh giá Kỷ Cảnh từ trên xuống dưới vài lần, sau đó dùng thiết bị đầu cuối báo cáo lên cho đội trưởng.",
    # 002
    "“Cậu đứng đây đợi đi, lát nữa sẽ có người của doanh trinh sát ra đón cậu.” Người lính gác khẽ nhướng mí mắt liếc nhìn bộ quần áo của cậu, dường như đối với cách ăn mặc đậm chất công tử bột này của cậu cảm thấy khịt mũi coi thường.",
    # 003
    "Hắn không hiểu tại sao cái loại mặt trắng nhỏ như thế này cũng có thể vào được doanh trinh sát, trong khi một trang nam nhi thiết huyết cứng rắn như hắn lại chỉ có thể đứng đây gác cổng.",
    # 004
    "Tâm tư của Kỷ Cảnh căn bản chẳng đặt vào chuyện này, cũng lười so đo, biếng nhác co một bên chân dài tựa lưng vào mép tường.",
    # 005
    "“Cái gì, Kỷ Cảnh tới báo danh rồi á, nhanh thế cơ à?”",
    # 006
    "Chu Độ lúc này vừa từ phòng đoàn trưởng của Lục Tư Niên bước ra, cửa còn chưa kịp khép lại thì người bên dưới đã gọi điện thoại lên.",
    # 007
    "Không ngờ Kỷ Cảnh lại đến nhanh như vậy, Chu Độ nhất thời không để ý đến âm lượng, rống lên một tiếng rồi cúi đầu liếc nhìn ngày tháng.",
    # 008
    "“Được rồi, lát nữa tôi đích thân xuống đưa nó về doanh trinh sát, chậc, tôi bảo tôi đích thân đưa đi, nghe không hiểu à?”",
    # 009
    "Chu Độ mải mê nói chuyện với đầu dây bên kia, hoàn toàn không để ý thấy cái giọng oang oang của mình đã bị Lục Tư Niên ở trong phòng đoàn trưởng nghe thấy rành rành.",
    # 010
    "Gã cúp điện thoại, đang định cất bước rời đi thì lại phát hiện không biết từ lúc nào Lục Tư Niên đã lặng lẽ không một tiếng động xuất hiện ngay sau lưng gã.",
    # 011
    "Chu Độ giật thót mình: “Lục... à không, đoàn trưởng ngài làm cái gì đấy?”",
    # 012
    "“Tôi xuống phòng hậu cần đối chiếu quân phục mới.” Giọng điệu Lục Tư Niên bình thản nói.",
    # 013
    "Đối chiếu quân phục á? Chẳng phải gửi qua thiết bị đầu cuối là xong rồi sao, việc gì phải đích thân đi.",
    # 014
    "Chu Độ khó hiểu liếc nhìn Lục Tư Niên một cái, Lục Tư Niên cao hơn gã, trông thì nhã nhặn, nhưng từ góc độ này nhìn Lục Tư Niên lại rất dễ khiến gã nhớ lại những lần trước đây bản thân từng bị Lục Tư Niên đè ra tẩn cho tơi bời trong các trận đối kháng. Gã bất giác thẳng lưng lên, đội lấy áp lực vô hình cùng Lục Tư Niên đi xuống lầu.",
    # 015
    "Ngoài cổng lớn Kỷ Cảnh vẫn đang tựa vào tường thất thần, liền bất thình lình nghe thấy giọng nói của người lính gác ban nãy đột ngột vút cao lên, ngữ điệu căng thẳng hệt như một kẻ ngốc vừa nhìn thấy tổng thống.",
    # 016
    "“Tổng tổng tổng trinh...” Người lính gác sợ tới mức líu cả lưỡi, đặc biệt là khi nhìn thấy bóng người đứng sau lưng Chu Độ, hắn hai mắt trợn ngược suýt nữa thì ngất xỉu tại chỗ.",
    # 017
    "Tầm mắt Kỷ Cảnh men theo hướng đó nhìn sang, vừa vặn nhìn thấy Chu Độ đang ra hiệu bảo cậu đi qua.",
    # 018
    "Cùng với...",
    # 019
    "Lục Tư Niên đang đứng cách Chu Độ không xa phía sau.",
    # 020
    "Hơi thở Kỷ Cảnh khựng lại, sải bước dài đi tới.",
    # 021
    "“Kỷ Cảnh, tôi là Chu Độ, cậu đi theo tôi đến doanh trinh sát báo danh.”",
    # 022
    "Chu Độ tùy ý đánh giá Kỷ Cảnh một lượt, quay người định dẫn Kỷ Cảnh đi, vừa cất bước liền phát giác ra điều gì đó bèn khựng lại một nhịp.",
    # 023
    "Cảm giác hiện diện từ ánh mắt của Lục Tư Niên quá mức mãnh liệt, Kỷ Cảnh không nhịn được liếc sang bên phải một cái, ngay khoảnh khắc chạm mắt với Lục Tư Niên, Kỷ Cảnh liền nhanh chóng giật phắt tầm mắt về, không chút biểu cảm nhìn thẳng về phía trước.",
    # 024
    "Rất nhanh cậu liền nhận thấy Lục Tư Niên không còn nhìn mình nữa, tiếng ủng quân dụng giẫm trên nền đất vang lên lách cách xa dần, cậu dời mắt lại, nhìn thấy bóng lưng Lục Tư Niên đang sải bước rời đi.",
    # 025
    "Cứ như thể Lục Tư Niên chưa từng dừng lại, ánh mắt ban nãy chỉ là ảo giác của một mình Kỷ Cảnh mà thôi.",
    # 026
    "“Kỳ lạ thật đấy, cậu ta chẳng phải bảo đi xuống phòng hậu cần sao, thế nào lại quay về phòng đoàn trưởng rồi.”",
    # 027
    "Chu Độ nhìn theo bóng lưng Lục Tư Niên đầy khó hiểu, luôn cảm thấy có chỗ nào đó sai sai.",
    # 028
    "Kỷ Cảnh nghe vậy không nói gì, nhưng tâm trí trong lòng thì chẳng biết đã bay bổng tận phương trời nào.",
    # 029
    "Cách biệt bao nhiêu ngày lại một lần nữa gặp lại Lục Tư Niên, tâm trạng vốn đang sục sôi như lửa của Kỷ Cảnh hệt như bị dội một gáo nước lạnh, đột ngột tụt thẳng về điểm xuất phát.",
    # 030
    "Cậu bắt đầu quay trở lại với lý trí, bình tĩnh suy xét xem tại sao mình lại đến cái nơi quỷ quái này, nói cách khác, cho dù cậu có đến Đệ tam quân đoàn thì đã làm sao chứ.",
    # 031
    "Cậu căn bản không dám chắc Lục Tư Niên rốt cuộc xuất phát từ nguyên do gì mà chủ động để cậu đánh dấu trọn đời, cậu chỉ là bị chuyện Lục Tư Niên đã bị cậu đánh dấu trọn đời làm cho mụ mẫm đầu óc, trong lòng có một giọng nói thôi thúc bảo cậu hãy đến Đệ tam quân đoàn, thế là cậu liền ma xui quỷ khiến mà chạy tới.",
    # 032
    "Kỷ Cảnh cứ thế cắm đầu cắm cổ bước đi, cuối cùng bị tiếng quát trầm thấp của Chu Độ kéo dòng suy nghĩ trở lại.",
    # 033
    "“Nghĩ cái gì đấy, lát nữa cậu vào trong tiêm một mũi thuốc giảm mẫn cảm tin tức tố, sau đó tôi sẽ đưa cậu về doanh trại thu dọn đồ đạc.”",
    # 034
    "Thôi kệ đi, quan tâm làm gì nữa, đến cũng đã đến rồi, cứ để mọi chuyện thuận theo tự nhiên đi.",
    # 035
    "Kỷ Cảnh từ bỏ việc suy nghĩ những điều vô ích, gật đầu bước vào trong tiêm thuốc.",
    # 036
    "Sau khi Omega được phép tòng quân, quân đội đế quốc đã đưa ra những điều chỉnh chính sách tương ứng, quy định vốn dĩ để quân nhân tự quyết định có tiêm thuốc giảm mẫn cảm tin tức tố hay không đã đổi thành bất kể quân nhân thuộc giới tính nào cũng bắt buộc phải tiêm, như vậy mới có thể tránh được tai họa hỗn loạn tin tức tố ngay từ tận gốc rễ.",
    # 037
    "Omega, Alpha và Beta đều có quyền lựa chọn giấu kín giới tính của mình, tuy nhiên hiện tại trên toàn bộ các quân đoàn của đế quốc chỉ có duy nhất một mình Lục Tư Niên thừa nhận giới tính Omega.",
    # 038
    "Sau khi hoàn tất mọi thủ tục nhập đoàn, Kỷ Cảnh trước tiên được Chu Độ đưa về ký túc xá làm thủ tục nhận phòng, sau đó lại được dẫn đi tham quan Đệ tam quân đoàn.",
    # 039
    "Đệ tam quân đoàn bao gồm rất nhiều binh chủng, trong đó lính trinh sát và lính chỉ huy là những binh chủng át chủ bài, Đệ tam quân đoàn chú trọng vào chiến trường tinh tế, đa phần các binh chủng đều được bồi dưỡng huấn luyện phục vụ cho chiến tranh giữa các vì sao.",
    # 040
    "“Vãi chưởng, kia là tổng trinh sát Chu Độ đấy à? Cái thằng nhóc đi bên cạnh gã là ai thế?!” “Không mặc quân phục, chắc là công tử thế gia có bối cảnh lớn nào đó đến Đệ tam quân đoàn tham quan rồi.” “Sao có thể chứ, mày từng thấy Chu Độ hòa nhã ôn tồn với con em thế gia bao giờ chưa.”",
    # 041
    "“Tao biết cậu ta là ai đấy, cậu ta tên là Kỷ Cảnh, là lính trinh sát đỗ đợt tuyển quân thứ hai lần này, anh em của tao hôm nay tiếp nhận cậu ta, lai lịch khủng khiếp lắm đấy.” Một Alpha lên tiếng.",
    # 042
    "Lời vừa dứt, toàn bộ các lính trinh sát đang nghỉ ngơi đều đồng loạt nhìn sang: “Lai lịch thế nào?”",
    # 043
    "Tên Alpha thận trọng nhìn ngó xung quanh, ghé sát lại hạ thấp giọng: “Đến cả Lục Tư Niên cũng đích thân xuống lầu ra đón đấy, bọn mày tự đoán xem lai lịch lớn cỡ nào.”",
    # 044
    "“Đệt! Thật hay đùa đấy!”",
    # 045
    "...",
    # 046
    "Sau khi Kỷ Cảnh dạo quanh một vòng từ trong ra ngoài doanh trinh sát, Chu Độ mới thả cho cậu về ký túc xá nghỉ ngơi, dặn dò cậu sáng mai phải đúng giờ cùng các cựu binh tham gia buổi tập huấn buổi sáng.",
    # 047
    "Cậu ôm một bộ quân phục mới tinh trở về phòng ký túc xá, phòng ký túc xá là phòng bốn người, nhưng vì cậu là tân binh đầu tiên đến báo danh nên hiện tại trong phòng chỉ có một mình cậu.",
    # 048
    "Do liên tục ngồi tinh hạm hai ngày trời, còn chưa kịp nghĩ ngợi đến chuyện của Lục Tư Niên, sau khi tắm rửa xong đầu vừa chạm vào gối là cậu đã ngủ thiếp đi mê mệt.",
    # 049
    "Cậu căn bản không hề hay biết những lời đồn đại liên quan đến cậu chỉ trong một đêm đã lan truyền khắp toàn bộ doanh trinh sát.",
    # 050
    "Sáng hôm sau khi trời còn chưa rạng sáng, Kỷ Cảnh đã bị tiếng chuông báo thức đinh tai nhức óc trong ký túc xá đánh thức.",
    # 051
    "Kỷ Cảnh từ nhỏ đến lớn chưa từng dậy đúng giờ bao giờ, nhưng trong lòng cậu vẫn nhận thức rõ ràng rằng đã bước chân vào quân đoàn thì phải tuân thủ kỷ luật.",
    # 052
    "Sau khi bị ép phải bứt đầu mình ra khỏi gối, cậu bắt đầu hối hận vì đã đến cái nơi tra tấn người quỷ quái này.",
    # 053
    "Vội vã thay bộ quân phục thống nhất của Đệ tam quân đoàn, cậu vừa vặn chạm mốc giây cuối cùng của tiếng còi tập hợp chạy đến thao trường huấn luyện.",
    # 054
    "Khi Kỷ Cảnh chạy tới nơi, toàn bộ lính trinh sát đã chỉnh tề xếp thành hàng ngũ ngay ngắn, hai Alpha vóc dáng cao lớn vạm vỡ đang đứng trên bục huấn luyện, một người trong số đó lạnh lùng nhìn về phía cậu.",
    # 055
    "“Tên gì, thuộc đội nào?”",
    # 056
    "Kỷ Cảnh giơ tay vuốt lại mái tóc rối bù: “Kỷ Cảnh, tôi không biết, hôm qua tôi mới tới.”",
    # 057
    "Một Alpha khác trên bục đột nhiên ghé tai nói điều gì đó với người nọ, sắc mặt người nọ liền sa sầm xuống, cuối cùng liếc cũng chẳng thèm liếc cậu một cái, lạnh lùng quát: “Kỷ Cảnh, Alpha lớp trinh sát năm nhất Học viện Quân sự Đế quốc, đội trưởng Đội Một bước ra nhận người.”",
    # 058
    "“Rõ!”",
    # 059
    "Dưới bục vang lên một tiếng hô dõng dạc, không lâu sau liền có một Alpha bước ra dẫn Kỷ Cảnh đi về phía phương trận hàng đầu tiên.",
    # 060
    "Nội dung huấn luyện buổi sáng của Đệ tam quân đoàn cũng tương tự như ở trường quân sự đế quốc, chỉ có điều cường độ huấn luyện mạnh hơn gấp mấy lần.",
    # 061
    "Kỷ Cảnh theo Đội Một thở hồng hộc hoàn thành xong bài huấn luyện, liền chạy lại dưới bóng một gốc cây ngồi bệt xuống.",
    # 062
    "Bầu không khí của Đệ tam quân đoàn nghiêm túc hơn trường quân sự rất nhiều, lúc huấn luyện yên tĩnh đến mức chỉ nghe thấy tiếng thở dốc nặng nề của đám Alpha, mãi cho đến khi tiếng còi nghỉ ngơi vang lên mới lục tục có các Alpha bắt đầu trò chuyện.",
    # 063
    "“Này nhìn thằng nhóc kia xem, quả nhiên, ngày đầu tiên tới đã vào thẳng Đội Một, lại còn chỉ là sinh viên năm nhất trường quân sự, chỗ dựa không biết phải khủng đến mức nào.”",
    # 064
    "“Chắc chắn rồi, cứ nhìn thái độ của hai vị trên bục hôm nay đối với việc nó đi trễ là thấy ngay, đổi lại là Alpha khác thì chẳng phải bị lột hai tầng da rồi sao.”",
    # 065
    "“Mẹ kiếp, dựa vào cái gì chứ, chỉ dựa vào việc nó có ba mẹ tốt thôi à?!”",
    # 066
    "...",
    # 067
    "Kỷ Cảnh ngửa đầu tu ừng ực chai nước, đám Alpha kia không hề hạ thấp giọng, ngược lại như cố tình nói cho cậu nghe.",
    # 068
    "Cậu vốn dĩ chẳng muốn để tâm tới, nhưng xui xẻo thay lại có mấy tên Alpha không có mắt tự tìm tới cửa.",
    # 069
    "Đệ tam quân đoàn lấy kẻ mạnh làm tôn kính, tự do quyết đấu nội bộ là quy củ ngầm mặc định, bất kỳ ai dù là quân đoàn trưởng đi chăng nữa nếu cậu thấy ngứa mắt đều có thể trực tiếp khiêu chiến.",
    # 070
    "Mấy tên Alpha tìm tới cửa Kỷ Cảnh nhìn khá quen mặt, là người của Đội Một, từ lúc huấn luyện đã liên tục liếc nhìn cậu.",
    # 071
    "“Người mới, đấu với tao một trận không?”",
    # 072
    "Tên đầu đinh dẫn đầu từ trên cao nhìn xuống cậu.",
    # 073
    "Lời tên đầu đinh vừa dứt, âm thanh xung quanh liền càng thêm náo nhiệt xôn xao.",
    # 074
    "“Đại Vĩ, mày thôi đi, lần trước mày bị Lục đoàn trưởng tẩn cho còn chưa đủ à, mông còn đau không đấy? Cái cổ mày mà gãy thêm lần nữa thì gay go to đấy nhé!”",
    # 075
    "Có kẻ thêm dầu vào lửa trêu chọc.",
    # 076
    "Tên đầu đinh nghe vậy liền phát hỏa, vô cùng xấu hổ tức tối: “Rõ ràng bọn mày đều không phục việc Lục Tư Niên một Omega làm quân đoàn trưởng của chúng ta, chỉ có tao với mấy thằng đàn ông dám trực diện tìm anh ta đánh, thua thì đã sao, bọn mày có thằng nào đánh thắng nổi tên biến thái Lục Tư Niên đó không! Thằng nhóc kia, rốt cuộc mày có đánh hay không hả?!”",
    # 077
    "“Không đánh.”",
    # 078
    "Kỷ Cảnh ngẩng đầu liếc nhìn tên đầu đinh một cái, hờ hững buông lời.",
    # 079
    "Lát nữa còn phải tiếp tục tập luyện, cậu việc gì phải lãng phí sức lực lên người tên ngốc này.",
    # 080
    "“Mẹ kiếp, cái đồ hèn nhát nhà mày, mày——”",
    # 081
    "“Đang làm cái gì đấy.”",
    # 082
    "Một giọng nói trầm thấp uy nghiêm lạnh lùng cắt ngang câu chửi thề sắp sửa thốt ra của tên đầu đinh, âm thanh này vừa cất lên, tất cả mọi người đều lập tức im bặt như ve sầu mùa đông.",
    # 083
    "Giọng nói này quá đỗi quen thuộc, Kỷ Cảnh đột ngột ngẩng phắt đầu nhìn qua —— Lục Tư Niên đang đứng sừng sững ngay sau lưng tên đầu đinh, bên cạnh còn có Chu Độ đi cùng.",
    # 084
    "Tên đầu đinh nhìn rõ người tới là ai liền lập tức rén ngang, rụt cổ lùi sang một bên, xung quanh một vòng các Alpha đang nằm ngồi ngả ngớn cũng đồng loạt bật dậy, đứng nghiêm trang chỉnh tề.",
    # 085
    "Lục Tư Niên ngày thường thường xuyên đi tuần tra, nhưng chưa từng có lần nào chủ động mở miệng chất vấn thế này.",
    # 086
    "Kỷ Cảnh vẫn giữ nguyên tư thế ngồi dưới đất, thấy tất cả mọi người đều đứng dậy rồi, mới uể oải chậm rãi đứng lên.",
    # 087
    "Cậu cảm thấy hình như Lục Tư Niên vẫn luôn nhìn mình, nhưng cậu không dám nhìn Lục Tư Niên, nên không biết đó có phải là ảo giác của mình hay không.",
    # 088
    "“Quân phục, mặc cho chỉnh tề.”",
    # 089
    "Giọng nói nghiêm khắc của Lục Tư Niên vang lên.",
    # 090
    "Phải mất vài giây Kỷ Cảnh mới phản ứng lại được là Lục Tư Niên đang nói chuyện với mình.",
    # 091
    "Cậu theo bản năng cụp mắt nhìn lại bản thân, mới phát hiện bộ đồ huấn luyện của mình mặc xộc xệch lỏng lẻo, thắt lưng đeo trễ nải buông thõng bên hông.",
    # 092
    "Thiết kế thắt lưng của quân phục không giống đồ bình thường, Kỷ Cảnh loay hoay một hồi thế nào cũng không chỉnh được, lại nghĩ đến việc Lục Tư Niên cứ nhìn chằm chằm mình, cơn bực dâng lên liền phiền muộn buông tay ra: “Không biết chỉnh.”",
    # 093
    "Xung quanh vang lên những tiếng hít sâu từng đợt, như thể kinh hãi trước thái độ này của cậu đối với Lục Tư Niên.",
    # 094
    "Bầu không khí đột ngột đông cứng lại, Kỷ Cảnh đợi nửa ngày cũng không thấy Lục Tư Niên đáp lời, cuối cùng là Chu Độ phá vỡ cục diện bế tắc này.",
    # 095
    "“Ha, cũng hài hước đấy chứ, sao nào, muốn tôi qua thắt giúp cậu à?” Chu Độ cười nói.",
    # 096
    "“Anh thắt giúp tôi một lần thì tôi sẽ biết làm ngay.” Kỷ Cảnh cũng chẳng thèm khách sáo.",
    # 097
    "“Được thôi.” Chu Độ cũng cảm thấy thú vị, bước lên một bước định túm lấy thắt lưng của Kỷ Cảnh.",
    # 098
    "“Chu Độ.” Lục Tư Niên đột nhiên quát khẽ một tiếng, dọa Chu Độ sững người đứng chôn chân tại chỗ, “Để cậu ta tự thắt.”",
    # 099
    "Cơn giận này của Lục Tư Niên phát ra quá mức vô cớ, Chu Độ nhất thời không biết bước tiếp theo nên làm cái gì.",
    # 100
    "“Đoàn trưởng, tôi không biết thắt thì phải làm sao bây giờ, ngài không cho tổng trinh sát dạy tôi, chẳng lẽ ngài tự mình tới dạy à?”",
    # 101
    "Kỷ Cảnh trong lòng cũng nghẹn một cục tức, lời nói còn chưa kịp suy nghĩ đã buột miệng thốt ra.",
    # 102
    "Bầu không khí càng thêm ngưng trệ nghẹt thở, Kỷ Cảnh nhìn cơ mặt lập tức căng cứng của Lục Tư Niên, khiêu khích nói.",
    # 103
    "Khoảnh khắc tiếp theo, cậu cảm nhận được một luồng sức mạnh bá đạo túm lấy thắt lưng của cậu giật mạnh về phía trước, Kỷ Cảnh đâm sầm thẳng vào lồng ngực vững chãi của Lục Tư Niên, ngay sau đó, bên hông vang lên một tiếng khóa cài lách cách giòn giã.",
    # 104
    "“Chỉ dạy một lần này thôi.”",
    # 105
    "Lục Tư Niên buông cậu ra, chẳng thèm để ý đến đám Alpha đang hóa đá xung quanh, gọi một tiếng Chu Độ đang có ánh mắt ngơ ngác, hai người quay lưng rời khỏi thao trường huấn luyện.",
    # 106
    "Kỷ Cảnh ngẩn ngơ cúi đầu nhìn chiếc thắt lưng ngay ngắn chỉnh tề, ngẩng đầu nhìn về hướng Lục Tư Niên rời đi, ánh mắt phức tạp không rõ ý vị.",
    # 107
    "...",
    # 108
    "Kỷ Cảnh mất gần một tuần lễ để làm quen đại khái với Đệ tam quân đoàn, các bài huấn luyện và khóa học dày đặc khiến cậu gần như không thể bứt ra chút thời gian nào để gọi một cuộc điện thoại về nhà.",
    # 109
    "Đến cuối tuần cậu mới sực nhớ ra ba mẹ, liền gọi một cuộc điện thoại về.",
    # 110
    "Nói chuyện với ba mẹ Kỷ một hồi xong, Kỷ Vân Hy đột nhiên thần thần bí bí thò đầu vào màn hình.",
    # 111
    "“Kỷ Cảnh, tuần sau tao sẽ đến Đệ tam quân đoàn nộp bản đề xuất thiết kế quân phục mới cho quân đoàn tụi mày đấy, mày liệu mà chuẩn bị chu đáo để đón tiếp bổn tiểu thư đi!”",
    # 112
    "Kỷ Vân Hy trong khung hình cười đầy vẻ bí hiểm.",
    # 113
    "Lời tác giả:",
    # 114
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-06-09 08:48:08~2023-06-14 22:57:02 nhé~",
    # 115
    "Cảm ơn thiên thần nhỏ ném địa lôi: Ly Viên 1 cái;",
    # 116
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Cột Dương 10 bình; Nhàn de Diêm 3 bình; Trì Tiệm 2 bình; Trấn Khuê, Triêu Ca, Đề Đăng Nguyện Thanh Hoan, Ly Viên, Mao Tuyến Đoàn 1 bình;",
    # 117
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 113: Tân binh gia nhập Đệ tam quân đoàn\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
