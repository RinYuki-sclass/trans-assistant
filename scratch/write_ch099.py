# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_099\translation.md"

paras = [
    # 000
    "Các trận đấu dưới võ đài diễn ra vô cùng sôi nổi như lửa đổ thêm dầu, giữa không trung chốc chốc lại có một chiếc flycam phát sóng trực tiếp bay vút qua vo ve, tiếng reo hò cổ vũ, tiếng gầm gừ trầm đục hòa lẫn cùng tiếng động cơ tạo nên một khung cảnh huyên náo và cuồng nhiệt.",
    # 001
    "Trên hàng ghế trọng tài, mọi người vừa theo dõi vừa hạ giọng trao đổi với các quân nhân chính quy của Quân đoàn Ba xung quanh.",
    # 002
    "Lục Tư Niên đoan chính nghiêm túc quan sát tình hình dưới khán đài, trong khoảng thời gian này người của Quân đoàn Ba đều cố gắng bắt chuyện với anh, nhưng đều bị những câu “ừ”, “đúng vậy” không nóng không lạnh của anh chặn họng trở về.",
    # 003
    "Những người thuộc Quân đoàn Ba được phái tới làm trọng tài phần lớn đều quen biết Lục Tư Niên, thậm chí có vài người từng là cấp dưới của Lục Tư Niên, họ hiểu rõ tính khí của anh nên về sau cũng không tự tìm rắc rối bắt chuyện với anh nữa.",
    # 004
    "“Vừa nãy ở vòng tái đấu tôi phát hiện ra một hạt giống tốt đấy.” Một người bên Quân đoàn Ba vỗ vai đồng đội.",
    # 005
    "“Ai thế?”",
    # 006
    "“Kìa, người thứ hai từ ngoài cùng bên trái.” Người nọ hất cằm ra hiệu, “Tôi để ý rồi, bất kỳ Alpha nào bắt cặp đấu với cậu ta, chưa đầy mười phút là đã bị đánh cho nằm đo ván, chiêu thức còn khá giảo hoạt linh hoạt nữa.”",
    # 007
    "“Ồ, cậu nói cậu ta à, tôi đã chú ý từ vòng sơ loại rồi, Lý giáo sư, thầy có quen thằng nhóc đó không?”",
    # 008
    "Người đàn ông trung niên được gọi là Lý giáo sư trả lời bằng giọng kinh ngạc: “Cậu nói người thứ hai ngoài cùng bên trái à? Đó là tân sinh viên lớp trinh sát, Kỷ Cảnh.”",
    # 009
    "Nói xong sợ bọn họ không biết, ông còn đặc biệt nhấn mạnh bổ sung thêm một câu: “Kỷ Cảnh, con trai độc nhất của nhà họ Kỷ.”",
    # 010
    "“Uầy, hóa ra là thái tử gia à.”",
    # 011
    "Người nọ thở dài một tiếng, trong ngữ điệu pha lẫn chút thất vọng, sau đó liền không nhắc tới Kỷ Cảnh nữa.",
    # 012
    "Ai nấy đều hiểu rõ, trên một đấu trường như thế này, thứ đem ra so tài đâu chỉ có năng lực chiến đấu của bản thân, mà còn có cả nhân tình thế thái.",
    # 013
    "So với việc để thái tử gia bại trận dưới tay mình, phần lớn những người có mối quan hệ lợi ích gắn kết với gia tộc của thái tử đều sẽ chọn cách nương tay, nhường cho thái tử một chút thể diện.",
    # 014
    "Lục Tư Niên nghe vậy khẽ nâng mí mắt, tiếp tục giữ im lặng.",
    # 015
    "Vòng tái đấu hạ màn trong một hồi còi vang dội, sau một tiếng đồng hồ nghỉ ngơi ngắt quãng, danh sách thi đấu trận chung kết đã được công bố.",
    # 016
    "Trên bảng danh sách tổng cộng có mười hai người, Lục Tư Niên liếc mắt nhìn qua, không ngoài dự đoán nhìn thấy tên của Kỷ Cảnh.",
    # 017
    "Chẳng bao lâu sau các trọng tài xung quanh bắt đầu di chuyển, nhường lại ba vị trí ở chính giữa.",
    # 018
    "Khán giả bên dưới cũng dần dần yên tĩnh lại, dùng ánh mắt nhiệt thành hướng về phía bàn trọng tài.",
    # 019
    "Mọi người đều biết, Quân đoàn trưởng của Quân đoàn Ba hôm nay sẽ đích thân tham dự trận chung kết của giải đấu cận chiến.",
    # 020
    "Ngoài Quân đoàn trưởng Alpha Trương Mạc ra, còn có Tổng chỉ huy đương nhiệm Lâm Diên Sơn cùng Tổng trinh sát Chu Độ.",
    # 021
    "Ba người này đã đại diện cho đỉnh cao kim tự tháp quyền lực của Quân đoàn Ba.",
    # 022
    "Khoảnh khắc ba Alpha bước lên khán đài trọng tài, toàn bộ đấu trường cận chiến như bùng nổ sôi trào.",
    # 023
    "Đám Alpha bên dưới mặt đỏ tía tai, ánh mắt bừng sáng tia nhiệt huyết sùng bái và khao khát hướng về.",
    # 024
    "So với những lời chào hỏi vồn vã nồng nhiệt của các trọng tài khác, Lục Tư Niên sau khi làm lễ chào quân đội, vẫn một mình ngồi ở vị trí của mình, khẽ gật đầu chào Quân đoàn trưởng Trương Mạc.",
    # 025
    "Dưới sự chứng kiến của hàng ngàn hàng vạn con mắt, Trương Mạc lại mỉm cười với Lục Tư Niên: “Tư Niên, đã lâu không gặp.”",
    # 026
    "Lời chào hỏi này khiến tất cả mọi người có mặt đều sững sờ kinh ngạc, lúc này họ mới sực nhớ ra, Lục Tư Niên từng là Tổng chỉ huy của Quân đoàn Ba.",
    # 027
    "Tổng chỉ huy đương nhiệm Lâm Diên Sơn trước kia chẳng qua cũng chỉ là một Phó chỉ huy dưới quyền anh mà thôi.",
    # 028
    "Lục Tư Niên bình thản gật đầu: “Sắc mặt Quân đoàn trưởng tốt hơn trước rất nhiều.”",
    # 029
    "“Đúng vậy, bà xã ở nhà chăm sóc chu đáo mà.” Trương Mạc thở dài một hơi đầy khoan khoái, ngầm tự đắc nói.",
    # 030
    "Trong khi mọi người xung quanh đều ngơ ngác nhìn lên lễ đài, Kỷ Cảnh và Vương Bằng đang ngồi ở một góc.",
    # 031
    "“Mày nhìn Lâm Diên Sơn kìa, mặt đen như than củi ấy, nếu không phải Lục Tư Niên tự mình nộp đơn xin giải ngũ, hắn ta làm sao có cửa ngồi lên vị trí Tổng chỉ huy được chứ.” Vương Bằng khịt mũi khinh bỉ.",
    # 032
    "“Lâm Diên Sơn?” Kỷ Cảnh đột nhiên khẽ lẩm bẩm cái tên này.",
    # 033
    "Cậu nhớ rõ, trong nguyên tác mà hệ thống đưa cho cậu xem, Lâm Diên Sơn cũng là một trong những kẻ sau này làm nhục và chèn ép Lục Tư Niên, cuối cùng bị Lục Tư Niên hủy hoại tuyến thể Alpha.",
    # 034
    "“Thôi không nói đến hắn nữa, lát nữa mày nghe lời tao đấy nhé, tách khỏi Lục Đảo Phong ra, chọn bảng nào không có nó ấy.” Vương Bằng nghiêm túc dặn dò, “Bảng đó độ ẩm ướt giả tạo quá lớn, tao hy vọng mày có thể đạt được kết quả công bằng.”",
    # 035
    "Vương Bằng hoàn toàn không ý thức được rằng, bản thân mình lại theo thói quen bỏ qua thân phận thế gia của Kỷ Cảnh.",
    # 036
    "So với tác phong ngang ngược phô trương của Lục Đảo Phong, Kỷ Cảnh tỏ ra đặc biệt khiêm nhường.",
    # 037
    "Kỷ Cảnh dời tầm mắt, nhìn sang phía Lục Đảo Phong đang được một đám Alpha vây quanh xun xoe, khóe môi nhếch lên một nụ cười lạnh lẽo: “Tất nhiên rồi.”",
    # 038
    "Hồi còi chung kết vang lên, mười hai Alpha tự do chọn bảng, bảng đấu có Lục Đảo Phong rất nhanh đã kín chỗ, Kỷ Cảnh và năm người còn lại tự động gom thành một bảng.",
    # 039
    "Sau khi trận đấu bắt đầu, gương mặt Trương Mạc đã lấy lại vẻ uy nghiêm nghiêm cẩn, chăm chú quan sát các trận cận chiến dưới võ đài.",
    # 040
    "Ánh mắt của Lục Tư Niên không thể dời khỏi Kỷ Cảnh dưới khán đài, anh nhận ra so với Kỷ Cảnh mà anh nhìn thấy cách đây không lâu, tốc độ và lực đạo hiện tại của cậu rõ ràng đã tăng vọt lên mấy bậc.",
    # 041
    "Hệt như một con sư tử cuồng nộ vừa mới thức giấc.",
    # 042
    "Từng cú đấm trúng đích nện thẳng vào da thịt, căn bản không cho đối thủ bất kỳ khoảng trống nào để thở dốc.",
    # 043
    "“Người đang giữ đài ở bảng thứ hai là ai thế?”",
    # 044
    "Trương Mạc bên cạnh bất chợt mở miệng hỏi.",
    # 045
    "Một giáo sư nghe vậy lập tức trả lời: “Là tân sinh viên lớp trinh sát, con trai độc nhất của nhà họ Kỷ, Kỷ Cảnh.”",
    # 046
    "“Con trai của Kỷ Trình à?” Trương Mạc nhướng mày, ngạc nhiên nói, “Chẳng phải nghe bảo thằng nhóc đó mắc chứng rối loạn tâm lý gì đó, đã phế bỏ rồi sao, cớ sao...”",
    # 047
    "Ông vừa chăm chú nhìn Kỷ Cảnh dưới võ đài, vừa nuốt những lời còn lại vào trong bụng.",
    # 048
    "Vị giáo sư kia không dám tiếp lời, chỉ sững sờ nhìn khóe môi Trương Mạc cong lên đầy vẻ hài lòng.",
    # 049
    "“Chu Độ, cậu thấy thế nào?” Trương Mạc liếc nhìn Tổng trinh sát bên cạnh.",
    # 050
    "Chu Độ vóc dáng vạm vỡ, lực lưỡng như một con gấu đen, anh ta khẽ hất cằm: “Cũng khá.”",
    # 051
    "“Lục Tư Niên, cậu thấy sao.” Trương Mạc phớt lờ Lâm Diên Sơn bên cạnh, vượt qua khoảng trống nhìn sang Lục Tư Niên.",
    # 052
    "Lục Tư Niên không để ý đến sắc mặt u ám âm trầm của Lâm Diên Sơn, chỉ nghiêm túc gật đầu: “Rất tốt.”",
    # 053
    "“Chậc, hiếm khi nghe thấy cậu khen người khác đấy.” Trương Mạc cười nói.",
    # 054
    "Kết quả võ chủ của bảng thứ nhất rất nhanh đã hiển thị trên màn hình lớn.",
    # 055
    "Cái tên Lục Đảo Phong rõ ràng xuất hiện chình ình trên bảng.",
    # 056
    "“Hừ,” Trương Mạc nhìn kết quả cười lạnh một tiếng, “Đây là đang diễn trò cho chúng ta xem đấy à.”",
    # 057
    "Chu Độ thấy vậy, lạnh lùng chửi một câu “đồ ngu”.",
    # 058
    "So với bảng thứ nhất, tốc độ của bảng thứ hai rõ ràng chậm hơn rất nhiều.",
    # 059
    "Những học viên kiệt xuất của Học viện Quân sự Đế quốc nhiều không đếm xuể, trong đó còn có những Alpha lớn hơn Kỷ Cảnh mấy khóa, bọn họ đều liều mạng muốn thể hiện bản thân trước mắt Quân đoàn Ba, nhưng hết lần này đến lần khác đều bị Kỷ Cảnh áp chế triệt để, dù vậy vẫn kiên quyết không chịu nhận thua.",
    # 060
    "Khi Alpha cuối cùng với đôi mắt đỏ ngầu ngã gục xuống sàn bất tỉnh nhân sự, tên của Kỷ Cảnh rốt cuộc đã xuất hiện trên màn hình lớn.",
    # 061
    "“Đệt mợ, Kỷ Cảnh? Thật sự là Kỷ Cảnh à?!”",
    # 062
    "Một đám Alpha lớp 3 trinh sát phấn khích bật dậy khỏi ghế ngồi.",
    # 063
    "“Tao sai rồi, trước đây tao không nên nghi ngờ nó dùng hack gian lận, thế này thì mẹ nó biến thái quá thể, chẳng lẽ ban đầu nó cố tình giả vờ làm gà mờ yếu ớt à?”",
    # 064
    "“Cũng chưa chắc, lỡ như trong số đó có người kiêng dè thân phận của nó nên cố tình nương tay thì sao...”",
    # 065
    "“Mày đùa cái quái gì thế?! Mày nhìn ông anh vừa nãy đi, cơ bắp mạch máu trên người sắp nổ tung tới nơi rồi kìa, mày gọi cái đó là nương tay hả?!”",
    # 066
    "“Chậc, thôi được rồi, đúng là không giống nương tay thật, than ôi ông đây chẳng qua không dám tin Kỷ Cảnh lại thực sự đỉnh vãi chưởng như thế thôi, làm vậy trông bọn mình trước kia ngu ngốc vãi đạn.”",
    # 067
    "...",
    # 068
    "Kỷ Cảnh không ngừng thở dốc, mồ hôi từ đầu đến chân đã ướt đẫm cả người cậu, lồng ngực cậu phập phồng dữ dội vì bộc phát sức lực trong thời gian dài, cậu theo thói quen vén lọn tóc mái ướt đẫm mồ hôi ra sau tai, sau đó bước sang một bên, nhận lấy chai nước Vương Bằng đưa tới rồi ngửa cổ uống ừng ực.",
    # 069
    "“A a a, Kỷ Cảnh đẹp trai quá đi mất!”",
    # 070
    "Trên khán đài, các Omega bùng nổ từng tràng thét chói tai đầy kinh ngạc.",
    # 071
    "“Kỷ Cảnh của lớp 3 trinh sát đấy, còn là thái tử gia của nhà họ Kỷ nữa.”",
    # 072
    "“Nhà họ Kỷ? Là nhà họ Kỷ đó á? Thế chẳng phải gia thế cũng ngang ngửa Lục Đảo Phong sao, trời đất ơi, sao cậu ấy có thể kín tiếng đến thế chứ!”",
    # 073
    "Duy chỉ có Lục Tư Niên trên khán đài là đột nhiên chau mày lại, bởi vì anh phát hiện sau khi Kỷ Cảnh vén tóc mái lên, để lộ ra một đôi lông mày đã được cạo tỉa thanh mảnh.",
    # 074
    "Đúng lúc Lục Tư Niên nghi ngờ không biết có phải mình nhìn lầm hay không, Kỷ Cảnh lại đột nhiên nhớ ra điều gì, vội buông tóc mái xuống.",
    # 075
    "“Vậy là, sắp tới sẽ là màn đối đầu giữa thái tử nhà họ Kỷ và thái tử nhà họ Lục cho chúng ta xem rồi?” Một giáo sư đột nhiên cười đầy hứng thú, “Cảnh tượng này hiếm thấy lắm đây.”",
    # 076
    "Câu nói đùa này khiến cả nhóm người trên bàn trọng tài bật cười theo, ai nấy đều nóng lòng chờ đợi trận quyết đấu chung kết giữa Kỷ Cảnh và Lục Đảo Phong.",
    # 077
    "Trận chung kết cuối cùng tương đối đặc biệt, hai bên bắt buộc phải chọn một võ đài ảo để phân định thắng thua, mỗi môi trường sẽ được thiết lập những chướng ngại vật khác nhau.",
    # 078
    "“Mày đỉnh thật đấy, tao còn không ngờ mày giành được hạng nhất bảng, sao tao cảm giác mày đột nhiên mạnh lên trông thấy thế?” Vương Bằng bên cạnh giúp cậu khởi động làm nóng người, vừa cảm thán vừa thở ngắn than dài, “Lục Đảo Phong tuy tay chân không sạch sẽ, nhưng năng lực vẫn có đôi chút đấy, nó ẵm liền hai năm hạng nhất toàn khối rồi.”",
    # 079
    "“Thực ra bây giờ em chỉ muốn về nhà ngủ thôi, nhưng thầy có biết vì sao em lại đánh tới tận bây giờ không?” Kỷ Cảnh đột nhiên hỏi anh ta.",
    # 080
    "Vương Bằng ngớ người: “Vì sao?”",
    # 081
    "“Bởi vì, hôm nay em đến đây chính là để đập cho nó một trận.” Kỷ Cảnh lười biếng nâng mí mắt lên, sau đó vẫy vẫy tay, sải bước đi về phía khu vực chuẩn bị thi đấu.",
    # 082
    "Lục Đảo Phong cũng đồng thời từ phía đối diện bước lên võ đài.",
    # 083
    "Đây là lần đầu tiên sau nhiều năm Kỷ Cảnh chạm trán trực diện với Lục Đảo Phong, hồi nhỏ trong các buổi tiệc từng gặp vài lần, cậu vốn chẳng bao giờ thèm để đối phương vào mắt.",
    # 084
    "Lục Đảo Phong nửa cười nửa không nhìn chằm chằm Kỷ Cảnh, trong mắt tràn đầy sự khinh miệt coi thường.",
    # 085
    "Những người khác không biết, nhưng hắn ta thì quá rõ ràng, năm xưa Kỷ Cảnh đã bị Lục Tư Niên đánh cho thành một kẻ phế vật như thế nào.",
    # 086
    "Cái thứ rác rưởi hèn nhát như thế này, mà cũng xứng so tài với hắn sao?",
    # 087
    "“Kỷ Cảnh, nhiều năm không gặp.” Lục Đảo Phong khoanh hai tay trước ngực, nở nụ cười giả tạo.",
    # 088
    "Ánh mắt Kỷ Cảnh xuyên qua bờ vai Lục Đảo Phong, bắn thẳng về phía Lục Tư Niên trên bàn trọng tài.",
    # 089
    "“Thế à, chúng ta từng gặp nhau sao?” Cậu nhướng mày, “Có lẽ là tôi chưa từng chú ý đến cái loại người như anh thôi.”",
    # 090
    "“Mày ——” Lục Đảo Phong nghẹn họng tức tối.",
    # 091
    "Đúng lúc này, âm thanh thông báo của hệ thống vang lên, yêu cầu hai người chọn bối cảnh thi đấu cho võ đài ảo.",
    # 092
    "“Vậy để mày chọn trước đi, kẻo người ta lại bảo tao bắt nạt đàn em khóa dưới, tuy mày còn lớn tuổi hơn tao, ồ nhớ ra rồi, mày từng lưu ban hai năm đúng không?” Lục Đảo Phong cao giọng nói xỉa xói.",
    # 093
    "“Tôi chọn chế độ bờ biển.” Kỷ Cảnh không thèm đếm xỉa tới hắn ta, trực tiếp báo kết quả với hệ thống.",
    # 094
    "Âm thanh tải dữ liệu của hệ thống vang lên, ngay khoảnh khắc tiếp theo, toàn bộ võ đài đã được bao phủ bởi một màn ánh sáng ảo, trên màn hình lớn có thể thấy hai người đang đứng sừng sững bên bờ biển sóng cuộn trào dâng.",
    # 095
    "“Bắt đầu đi.”",
    # 096
    "Kỷ Cảnh căn bản không cho bất kỳ ai có thời gian thích ứng đệm lót, trực tiếp hạ lệnh với hệ thống.",
    # 097
    "“Này, Kỷ Cảnh, mày đã hỏi qua tao chưa hả?”",
    # 098
    "Lục Đảo Phong rốt cuộc không thể nhịn nổi nữa, lớn tiếng chửi rủa.",
    # 099
    "Kỷ Cảnh cất bước, từng bước từng bước áp sát về phía Lục Đảo Phong, tựa như một con dã thú đang khoan thai ung dung tiến lại gần con mồi.",
    # 100
    "Tiếng sóng biển gầm thét vỗ vào bờ đá đã làm suy giảm âm lượng của Kỷ Cảnh, nhưng từng người có mặt tại hiện trường đều nghe rõ mồn một lời Kỷ Cảnh nói.",
    # 101
    "“Hỏi mày làm cái gì? Tao tới đây là để đập mày mà.”",
    # 102
    "...",
    # 103
    "Tiếng va chạm thân thể kịch liệt từ loa phóng thanh trên đài vang vọng khắp toàn bộ đấu trường.",
    # 104
    "Toàn bộ khán đài im phăng phắc như tờ, mọi người đều ngơ ngác nhìn vào màn hình quang học, trong mắt viết đầy sự hoang mang ngỡ ngàng.",
    # 105
    "Chẳng phải là xem quyết đấu sao?",
    # 106
    "Sao lại biến thành màn bạo lực đẫm máu ẩu đả đơn phương thế này?",
    # 107
    "Mắt thấy Lục Đảo Phong trên võ đài bị từng cú đấm giáng xuống đến mức không còn một chút sức lực chống đỡ nào, trên hàng ghế trọng tài có vị giáo sư lên tiếng: “Chuyện này là thế nào?”",
    # 108
    "“Còn thế nào được nữa, thành tích của Lục Đảo Phong quá nhiều nước, múa rìu qua mắt thợ gặp phải cao thủ chân chính rồi chứ sao.” Một Alpha của Quân đoàn Ba lên tiếng châm chọc.",
    # 109
    "Những người khác có thể không nhìn ra, nhưng họ lại hiểu rất rõ những trận đấu trước đây của Lục Đảo Phong có vấn đề rất lớn.",
    # 110
    "“Dù sao Lục Đảo Phong cũng là đích tử của nhà họ Lục, hay là dừng trận đấu lại đi, nhà họ Lục mà truy cứu thì nhà trường cũng khó ăn nói.” Vị giáo sư ngập ngừng đề xuất.",
    # 111
    "Lời còn chưa dứt, trên khán đài đã truyền đến những tiếng xôn xao khác lạ.",
    # 112
    "Mọi người nhìn lên màn hình quang học, chỉ thấy Kỷ Cảnh đang túm lấy cổ áo sau của Lục Đảo Phong, từng bước từng bước lôi xềnh xệch hắn ta xuống biển.",
    # 113
    "“Cậu ta muốn làm gì?” Trương Mạc bỗng nhiên đầy hứng thú lên tiếng hỏi.",
    # 114
    "Trên võ đài,",
    # 115
    "“Kỷ Cảnh, mẹ nó buông tao ra, rốt cuộc mày muốn làm cái gì hả?!!”",
    # 116
    "Lục Đảo Phong vừa giãy giụa vừa gào thét khản đặc cả giọng, cả người hắn đầy máu me do bị Kỷ Cảnh đấm, đôi chân vô lực kéo lê trên cát tạo thành hai vệt dài ngoằng.",
    # 117
    "Ngay sau đó, hắn bị Kỷ Cảnh ném thẳng vào trong làn sóng biển cuộn trào.",
    # 118
    "Lục Đảo Phong bị nước biển sặc đầy khoang mũi, bắt đầu ho sặc sụa dữ dội.",
    # 119
    "Đúng lúc này, hắn bị Kỷ Cảnh túm tóc lôi ngược ra khỏi mặt nước biển.",
    # 120
    "“Lục Đảo Phong, có phải mày rất thích nhìn người khác giãy giụa chết đuối không?”",
    # 121
    "Giọng nói của Kỷ Cảnh vang lên tựa như tiếng thì thầm của ác ma nơi địa ngục.",
    # 122
    "“Cái... cái gì... ư...”",
    # 123
    "Lục Đảo Phong còn chưa kịp phản ứng thì đã bị ấn chặt đầu dìm sâu vào trong làn nước biển.",
    # 124
    "“Thế nào, dễ chịu không?”",
    # 125
    "Kỷ Cảnh túm hắn lên, mỉm cười hỏi.",
    # 126
    "“Mày đang nói nhảm cái gì, muốn chết... ư...”",
    # 127
    "Kỷ Cảnh một lần nữa đè đầu hắn ấn thẳng xuống làn nước biển sâu.",
    # 128
    "“Tao nhìn mày ngứa mắt lâu lắm rồi.”",
    # 129
    "Kỷ Cảnh lại lôi cổ áo hắn nhấc lên, sau đó căn bản không cho hắn bất kỳ cơ hội hít thở nào, thô bạo dằn mạnh xuống nước.",
    # 130
    "...",
    # 131
    "Trên hàng ghế trọng tài đã có giáo sư đập bàn đứng phắt dậy, nhấn chuông báo động yêu cầu hệ thống lập tức chấm dứt trận đấu.",
    # 132
    "“Hê, đừng nói nữa, thằng nhóc này đúng là thú vị thật đấy.”",
    # 133
    "Trương Mạc cong mắt nói với Chu Độ, nói xong lại quay sang nhìn Lục Tư Niên: “Tôi thấy cái nhuệ khí trên người cậu ta khá giống cậu đấy... Lục Tư Niên?”",
    # 134
    "Lưng Lục Tư Niên đã rời khỏi tựa lưng của chiếc ghế, anh gắt gao nhìn chằm chằm Kỷ Cảnh trên màn hình quang học, trong mắt ngập tràn vẻ bàng hoàng ngỡ ngàng.",
    # 135
    "Những lời Kỷ Cảnh vừa nói hệt như câu thần chú cứ lặp đi lặp lại vang vọng bên tai anh không dứt.",
    # 136
    "Tiếng gọi của Trương Mạc khiến anh giật mình hoàn hồn, sau đó anh nghe thấy tiếng trái tim mình đang đập rộn ràng điên cuồng kịch liệt.",
    # 137
    "Lục Tư Niên nới lỏng cà vạt, lặng lẽ thở hắt ra một hơi: “Xin lỗi, tôi ra ngoài một chút.”"
]

header = "---\ntitle: Chương 99: Cơn sốt tin tức tố bùng phát\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Written ch_099 translation successfully.")
