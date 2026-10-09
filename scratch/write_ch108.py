# -*- coding: utf-8 -*-
import os

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_108\translation.md"

paras = [
    # 000
    "Kỷ Cảnh đăng nhập vào tài khoản của Dịch Nam, đối diện với khung chat của người liên hệ duy nhất là Lục Tư Niên mà ngẩn người xuất thần một lúc lâu.",
    # 001
    "Dòng tin nhắn cuối cùng trên đó vẫn là câu “Tôi say rồi” do Lục Tư Niên gửi tới.",
    # 002
    "Đầu ngón tay khẽ cử động, cậu bắt đầu gõ tin nhắn trả lời:",
    # 003
    "【Dịch Nam Nam Nam】: Vậy bây giờ anh đã về nhà chưa?",
    # 004
    "Khoảng cách thời gian giữa hai tin nhắn cách nhau quá lâu, người tinh mắt chỉ cần liếc qua là có thể nhận ra sự qua loa chiếu lệ trong đó.",
    # 005
    "Kỷ Cảnh trước nay luôn làm theo ý mình, lúc yêu đương cũng chưa từng để tâm đến cảm xúc của Omega, những cuộc tình trước đây đối với cậu chẳng qua chỉ là trò giải trí tiêu khiển.",
    # 006
    "Thế nhưng cậu lại không kìm lòng được mà đặt mình vào vị trí của Lục Tư Niên, những lời say rượu cùng ánh mắt cô độc mệt mỏi của Lục Tư Niên ngày hôm nay cứ liên tục tái hiện trong tâm trí cậu.",
    # 007
    "Phải rồi, cái tên ngốc Lục Tư Niên đó chưa từng yêu đương bao giờ, mọi chuyện đều một mình ôm giữ nén chặt trong lòng, vô duyên vô cớ bị người ta đơn phương chiến tranh lạnh, hèn chi hôm nay lại uống nhiều rượu đến thế.",
    # 008
    "Nghĩ đến đây, Kỷ Cảnh lại không tự chủ được mà gửi thêm vài tin nhắn nữa:",
    # 009
    "【Dịch Nam Nam Nam】: Xin lỗi anh, mấy ngày nay tâm trạng em không được tốt lắm, nên mới không muốn trả lời tin nhắn của anh.",
    # 010
    "【Dịch Nam Nam Nam】: Sau này em sẽ không như vậy nữa đâu.",
    # 011
    "【Dịch Nam Nam Nam】: [Mèo con cọ chân.jpg]",
    # 012
    "Phía đối diện vô cùng yên ắng, Kỷ Cảnh đoán chừng phần lớn là Lục Tư Niên vẫn chưa tỉnh rượu.",
    # 013
    "Liệu anh có nằm vật ra sàn nhà suốt cả đêm không? Ngày mai thức dậy liệu anh còn nhớ được bao nhiêu phần?",
    # 014
    "Kỷ Cảnh ý thức được bản thân lại bắt đầu nghĩ về Lục Tư Niên, bực bội “chậc” một tiếng, rồi quay người đi rửa mặt súc miệng.",
    # 015
    "Ngày hôm sau lúc Kỷ Cảnh thức dậy liền nhìn thấy câu trả lời của Lục Tư Niên:",
    # 016
    "【Lục Tư Niên】: Ừ, không sao đâu.",
    # 017
    "【Lục Tư Niên】: Tôi về nhà rồi.",
    # 018
    "Kỷ Cảnh ngẫm nghĩ một lát, nhắn sang:",
    # 019
    "【Dịch Nam Nam Nam】: Tối qua có ai đưa anh về nhà không?",
    # 020
    "Phía Lục Tư Niên phải mất vài phút sau mới trả lời:",
    # 021
    "【Lục Tư Niên】: Nhớ không rõ lắm.",
    # 022
    "Kỷ Cảnh thở phào nhẹ nhõm một hơi, nhưng đồng thời trong lòng lại thầm nghĩ Lục Tư Niên dựa vào cái gì mà không nhớ chứ.",
    # 023
    "Tóm lại hai người dường như đã làm lành với nhau, Kỷ Cảnh vẫn theo giờ cũ đến lớp nghe giảng của Lục Tư Niên, mỗi ngày cố định trò chuyện với Lục Tư Niên một lúc, tựa như việc điểm danh theo quy trình được lập trình sẵn.",
    # 024
    "Cậu và Lục Tư Niên ở trong trường học thời gian dài, khó tránh khỏi bị không ít học viên của Học viện Quân sự Đế quốc phát hiện ra điều mờ ám.",
    # 025
    "Chẳng mấy chốc tin đồn về chuyện tình cảm của Lục Tư Niên đã bắt đầu lan truyền trong phạm vi hẹp trên diễn đàn Học viện Quân sự Đế quốc, nhưng phần lớn mọi người đều không tin Lục Tư Niên lại có thể yêu đương.",
    # 026
    "Mọi thứ nhìn bề ngoài có vẻ rất bình thường, nhưng Kỷ Cảnh lại có thể cảm nhận được sự thay đổi giữa cậu và Lục Tư Niên.",
    # 027
    "Trước kia mối quan hệ giữa cậu và Lục Tư Niên hoàn toàn dựa vào việc cậu chủ động bước lên trước một bước, thế nhưng lần này Kỷ Cảnh lại không thể bước tiếp được nữa.",
    # 028
    "Nói đúng hơn là không thể bước, chi bằng nói là bản thân cậu không muốn bước tiếp.",
    # 029
    "Cho dù trong lòng cậu biết rất rõ thời điểm này bản thân nên rèn sắt khi còn nóng, nhanh chóng nâng thanh tiến độ lên mốc 80%, sau đó ngả bài thẳng thắn dứt khoát với Lục Tư Niên.",
    # 030
    "Thế nhưng cậu lại không tài nào ra tay được, trong lòng dường như có một giọng nói đang vang lên hỏi rằng cậu có chắc chắn không, cậu thật sự muốn ngả bài với Lục Tư Niên sao, đến lúc đó Lục Tư Niên sẽ có phản ứng gì, đau khổ, phẫn nộ hay coi chuyện này như vết nhơ nhục nhã trong cuộc đời mình, rồi đến chết cũng không thèm qua lại với nhau nữa?",
    # 031
    "Mà Lục Tư Niên khoảng thời gian này lại mang thái độ không nóng không lạnh.",
    # 032
    "Trước kia Lục Tư Niên tuy bảo thủ, nhưng mỗi khi Kỷ Cảnh chủ động nắm tay anh thì anh đều sẽ đáp lại, cũng sẽ trong lúc tình cảm mập mờ nảy nở mà không kìm lòng được chủ động hôn cậu.",
    # 033
    "Thế nhưng Lục Tư Niên trong khoảng thời gian này lại không còn chủ động phát sinh bất kỳ hành vi thân mật nào nữa, bề ngoài anh không có gì thay đổi, anh vẫn sẽ siết chặt tay khi Kỷ Cảnh đưa tay sang, nhưng lại tuyệt nhiên không bao giờ chủ động nắm lấy tay cậu nữa.",
    # 034
    "Kỷ Cảnh thu trọn sự thay đổi của Lục Tư Niên vào đáy mắt, nhưng lại không muốn nghĩ sâu xa về nguyên nhân trong đó.",
    # 035
    "Bên kia một đám Alpha trong giờ nghỉ giải lao giữa tiết ngồi la liệt trên sân tập rên rỉ than vãn vì mệt mỏi, duy chỉ có một mình Kỷ Cảnh là không biết mệt mỏi đấm vào bao cát bia ngắm, gắt gao nhìn chằm chằm vào các chỉ số số liệu đang tăng vọt trên màn hình huỳnh quang.",
    # 036
    "“Được rồi, nghỉ ngơi một chút đi.”",
    # 037
    "Vương Bằng bước tới, giơ tay ấn nút dừng lại.",
    # 038
    "Anh ta ném một chai nước vào lồng ngực Kỷ Cảnh, thuận miệng hỏi: “Sao thế, tâm trạng không tốt à?”",
    # 039
    "Kỷ Cảnh tìm một khoảng đất trống ngồi bệt xuống một cách tùy ý, thản nhiên đáp: “Cũng tạm thôi.”",
    # 040
    "Vương Bằng cũng ngồi xuống bên cạnh cậu, đột nhiên hỏi: “Cậu với Lục giáo sư thân nhau lắm à?”",
    # 041
    "Động tác uống nước của Kỷ Cảnh khựng lại, liếc nhìn anh ta một cái.",
    # 042
    "Vương Bằng định nói gì đó, nhưng rồi lại ngậm miệng lại.",
    # 043
    "Anh ta thực ra muốn hỏi Kỷ Cảnh và Lục Tư Niên rốt cuộc có quan hệ thế nào, thân hay không thân, nếu không thân thì tại sao dạo gần đây Lục Tư Niên cứ liên tục tìm anh ta hỏi thăm chuyện của Kỷ Cảnh, còn nếu thân thì cớ sao không hỏi thẳng Kỷ Cảnh luôn cho rồi?",
    # 044
    "Nghĩ bụng chuyện mờ ám bên trong không thích hợp để mình xen vào hỏi han, anh ta bèn bất thình lình đổi đề tài:",
    # 045
    "“Bắt đầu từ học kỳ sau Đệ tam quân đoàn sẽ mở đợt tuyển quân cho sinh viên năm thứ tư đấy, tuy nói là năm thứ tư, nhưng trước đây cũng không phải chưa từng có tiền lệ học viên khóa dưới được đặc cách tuyển chọn,” Vương Bằng ân cần thấm thía nói với Kỷ Cảnh.",
    # 046
    "Thực chất là hôm đó Tổng trinh sát Chu Độ đã tìm anh ta, nhờ anh ta tìm cách kéo Kỷ Cảnh sang bên đó.",
    # 047
    "Thế là Vương Bằng ra sức vụng về khuyên nhủ: “Năng lực của cậu chắc chắn thừa sức đạt chuẩn, hay là cậu cũng đi thi thử xem sao?”",
    # 048
    "“Để sau rồi tính.” Kỷ Cảnh cũng không phải có chấp niệm gì quá lớn với Đệ tam quân đoàn.",
    # 049
    "“Để sau rồi tính á?!” Vương Bằng sốt ruột, anh ta không hiểu nổi Đệ tam quân đoàn mà các Alpha toàn Đế quốc đổ xô tranh giành nhau thì ở chỗ Kỷ Cảnh sao lại hệt như đi dạo chợ rau thế này, “Quy hoạch cuộc đời tương lai của cậu là gì hả? Các Alpha đến Học viện Quân sự Đế quốc ai nấy đều có mục tiêu vào quân đoàn làm sĩ quan, sao cậu lại chẳng giống họ chút nào thế.”",
    # 050
    "Học viện Quân sự Đế quốc đối với người bình thường là cánh cửa rồng để làm rạng danh tổ tông, đối với con em thế gia là công cụ để củng cố địa vị gia tộc.",
    # 051
    "Đối với Kỷ Cảnh mà nói thực ra chẳng là cái gì cả, bởi vì cậu cái gì cũng có rồi, cái gì cũng không thiếu.",
    # 052
    "Trước kia cậu vào Học viện Quân sự Đế quốc là để trả thù Lục Tư Niên, hiện tại thì cùng lắm là cậu khá thích thú tận hưởng chế độ huấn luyện của trường này mà thôi.",
    # 053
    "Kỷ Cảnh không thích bị trói buộc, cậu chưa từng đặt ra mục tiêu cho tương lai của mình, nếu nhất quyết phải nói ra một kế hoạch, hồi nhỏ cậu từng muốn đi du hành khắp dải ngân hà, làm một tên cướp biển không gian cũng không tồi.",
    # 054
    "Việc gia nhập Đệ tam quân đoàn cũng nằm trong phạm vi cân nhắc của cậu, bởi vì cậu cũng khá muốn trải nghiệm bầu không khí chiến đấu thực thụ.",
    # 055
    "“Chẳng có quy hoạch gì cả, thích làm gì thì làm nấy thôi.” Kỷ Cảnh dốc cạn cả chai nước vào miệng.",
    # 056
    "Vương Bằng thở ngắn than dài liên tục, biết hiện tại nói chuyện này không ăn thua, liền đổi chủ đề khác: “Cậu có biết không, hai ngày trước Đế quốc đã mở đợt bỏ phiếu về quyền tham gia quân đội của Omega đấy.”",
    # 057
    "Kỷ Cảnh bóp chai nước kêu lách tách giòn giã, đột nhiên tay buông lỏng ra, hỏi: “Gì cơ?”",
    # 058
    "“Haizz, thực ra tôi cảm thấy quân đoàn cũng không nhất thiết phải cấm tiệt Omega gia nhập, dù sao công nghệ hiện nay đã rất hoàn thiện phát triển rồi, chỉ cần Omega trước khi nhập ngũ tự nguyện tiêm một mũi thuốc kháng mẫn cảm tin tức tố dùng trong quân đội, thì căn bản sẽ không xảy ra chuyện Omega phát tình làm ảnh hưởng đến toàn bộ quân đoàn, hơn nữa giới tính là do bẩm sinh trời định, nhưng con người thì thiên biến vạn hóa đa dạng, dựa vào đâu mà lại cấm đoán quyền lựa chọn của Omega chứ... Alpha không phải cứ vào quân đoàn mới là vinh quang, Omega cũng chẳng phải sinh ra là bắt buộc phải ở trong nhà kính...”",
    # 059
    "Kỷ Cảnh từ trước đến nay đều nhận thấy Vương Bằng không giống với đại đa số Alpha khác, suy nghĩ của anh ta tinh tế và mềm mỏng hơn nhiều.",
    # 060
    "“Thế nhưng tôi nhìn số phiếu hiện tại, đề xuất này phần lớn khả năng cuối cùng sẽ thất bại, các Alpha xung quanh tôi đa số đều không tán thành.”",
    # 061
    "Đại đa số Alpha trong xương tủy đều khắc sâu tư tưởng cường quyền, họ thích quyền lực, thích chinh phục và thao túng, mà Omega lại thường là đối tượng để các Alpha chinh phục thao túng, họ theo bản năng bài xích việc Omega ngồi ngang hàng với mình, càng không chịu nổi việc đồng loại có gen thấp hơn lại vượt mặt chính mình.",
    # 062
    "Bi kịch của Lục Tư Niên trong nguyên tác chính là vì anh mạnh mẽ vượt trội hơn quá nhiều Alpha.",
    # 063
    "Vương Bằng ở bên cạnh cậu nói chuyện đầy phẫn nộ bất bình, còn trong đầu Kỷ Cảnh thì ngập tràn suy nghĩ: Nếu đề xuất này được thông qua, liệu Lục Tư Niên có thể quay trở lại quân đoàn hay không.",
    # 064
    "Cậu đột nhiên nhớ lại ngày hôm đó trong phòng giác đấu, tiếng gầm gừ trầm đục bên bờ vực sụp đổ của Lục Tư Niên.",
    # 065
    "Không một ai khao khát, và thích hợp để ở lại trong quân đoàn hơn Lục Tư Niên cả.",
    # 066
    "Lục Tư Niên có biết chuyện này không?",
    # 067
    "Anh đang nghĩ gì?",
    # 068
    "Mang theo suy nghĩ này, Kỷ Cảnh tự động chặn đứng mọi âm thanh ồn ào bên ngoài, vẻ mặt thâm trầm, học xong tiết học cuối cùng liền trở về nhà.",
    # 069
    "Lúc đi ngang qua thư phòng trên lầu, cậu nghe thấy giọng nói của Kỷ Trình truyền ra từ khe cửa khép hờ.",
    # 070
    "“Anh bảo nhà họ Lục đã bỏ phiếu chống sao? Bình thường thôi, nhà họ Lục những kẻ có chút quyền hành toàn bộ đều là Alpha, theo cái tính toán hẹp hòi của nhà họ Lục, làm sao có thể nhượng bộ đặc quyền của Alpha được chứ.”",
    # 071
    "“Chuyện này không phải chuyện nhỏ, liên quan đến quá nhiều lợi ích và quyền lực, xem ra lần này sắp có đợt xáo trộn bài lớn rồi.”",
    # 072
    "“Bên tôi vẫn chưa bỏ phiếu, chuyện này vẫn phải để tôi suy nghĩ thêm đã.”",
    # 073
    "...",
    # 074
    "Quyền quyết sách của Đế quốc chủ yếu nằm trong tay giới quân đội và tứ đại gia tộc, kết quả bỏ phiếu của bất kỳ bên nào cũng sẽ tạo ra ảnh hưởng chấn động to lớn.",
    # 075
    "Bởi vì mẹ Kỷ không muốn hai đứa con tiếp xúc với lợi ích gia tộc quá sớm trước khi trưởng thành, nên ba mẹ Kỷ chưa bao giờ nhắc tới những chuyện này trước mặt Kỷ Cảnh và Kỷ Vân Hy.",
    # 076
    "Chuyện này Kỷ Trình không nói cho cậu biết, cũng là điều hợp tình hợp lý.",
    # 077
    "Trong thư phòng Kỷ Trình đã cúp máy, Kỷ Cảnh định thần lại, lặng lẽ không một tiếng động lẻn về phòng mình, sau đó mở thiết bị đầu cuối, tìm kiếm cục diện bỏ phiếu hiện tại.",
    # 078
    "Hiện tại đã có nhà họ Lục và hai phần ba quân đội Đế quốc công bố kết quả bỏ phiếu, trong đó nhà họ Lục và một phần ba quân đội đều bỏ phiếu chống.",
    # 079
    "Còn có một phần ba quân đội Đế quốc bỏ phiếu thuận.",
    # 080
    "Mặc dù hiện tại vẫn còn hơn một nửa số người chưa bỏ phiếu, nhưng kết quả đã rõ ràng nghiêng hẳn về một phía.",
    # 081
    "Kỷ Cảnh gập thiết bị đầu cuối lại, day day ấn ấn giữa hai hàng lông mày.",
    # 082
    "Bất kể là vì lòng trắc ẩn thương cảm hay tâm lý bù đắp, hay là do thứ tình cảm mà ngay cả chính bản thân cậu cũng nhìn không thấu đang quấy phá, Kỷ Cảnh trong lòng đã âm thầm đưa ra một câu trả lời.",
    # 083
    "Một tiếng đồng hồ sau, cậu đứng trước cửa thư phòng, gõ vang cánh cửa.",
    # 084
    "“Vào đi.” Kỷ Trình nói.",
    # 085
    "“Ba.” Kỷ Cảnh bước vào thư phòng, cất tiếng gọi.",
    # 086
    "Kỷ Trình đặt tập tài liệu trong tay xuống, thong thả nói: “Có việc tìm ba à?”",
    # 087
    "Kỷ Cảnh mím chặt môi, đối diện với ánh mắt của Kỷ Trình, cậu nhắm mắt lại: “Ba, con có một chuyện muốn cầu xin ba.”",
    # 088
    "...",
    # 089
    "Từ thư phòng bước ra, Kỷ Cảnh thở phào nhẹ nhõm một hơi, sau đó ngửa người dựa vào tường.",
    # 090
    "Cậu thầm nghĩ, nhìn xem, Lục Tư Niên, tuy rằng tôi đã lừa dối anh, nhưng tôi đã bù đắp cho anh rồi đấy.",
    # 091
    "...",
    # 092
    "Mười ngày sau,",
    # 093
    "Trong căn phòng vắng vẻ quạnh quẽ, đối lập với ánh đèn rực rỡ muôn màu muôn vẻ ngoài cửa sổ sát đất, tông màu đen trắng xám đơn điệu bên trong phòng lại càng toát lên vẻ cô độc quạnh hiu.",
    # 094
    "Lục Tư Niên mặc một bộ đồ ngủ màu đen tuyền, đôi mắt sau tròng kính vô định nhìn ngắm ánh đèn hoa lệ ngoài cửa sổ.",
    # 095
    "“Lục Tư Niên, nhà họ Lục cộng thêm nhà họ Trần, cùng một bộ phận quân đội đều đã bỏ phiếu chống, còn về phía nhà họ Kỷ, ước chừng cũng chẳng có lý do gì để bỏ phiếu thuận cả, chuyện này, e là hỏng rồi.”",
    # 096
    "“Cậu đừng quá cố chấp với lần này, tương lai cậu còn rất nhiều năm, kiểu gì cũng sẽ có cơ hội thôi.”",
    # 097
    "Mấy ngày trước, Trương Mạc dùng giọng điệu nặng nề báo cho anh biết kết quả.",
    # 098
    "Lục Tư Niên vốn tưởng mình sẽ thất vọng, sẽ tuyệt vọng, nhưng vào thời điểm đó lại chẳng thể nảy sinh nửa phần cảm xúc nào, như thể đã hoàn toàn tê liệt chai sạn.",
    # 099
    "Không biết từ lúc nào, anh đã dần dần chấp nhận sự thật bản thân biến thành một Omega.",
    # 100
    "Cả cuộc đời này anh không có bất kỳ dục vọng mưu cầu nào, thứ duy nhất chống đỡ để anh tiếp tục sống chính là trả thù.",
    # 101
    "Ban đầu anh phát điên phủ nhận kết quả này, sau đó anh học được cách đè nén, trầm mặc làm một giáo sư trường quân sự; sau này nữa, anh gặp được Dịch Nam, trong mấy ngày ngỡ rằng mình đã... Kỷ Cảnh, anh dần dần chấp nhận hiện thực, anh phát hiện bản thân nảy sinh dục vọng mới, trên vai anh gánh vác trách nhiệm, anh phải chịu trách nhiệm với Kỷ Cảnh.",
    # 102
    "Ý thức trách nhiệm này trở thành động lực sống mới của anh, anh nghĩ rằng sau này cùng đối phương yên ổn bình lặng đi hết nửa đời sau có lẽ cũng không tồi.",
    # 103
    "Thế nhưng sau đó lại được thông báo rằng chẳng có chuyện gì xảy ra cả, mà Kỷ Cảnh dùng thân phận Dịch Nam tiếp cận anh có lẽ cũng chỉ là để trả thù anh mà thôi.",
    # 104
    "Anh không dám đối chất trực tiếp với Kỷ Cảnh, anh theo tiềm thức cảm thấy rằng, một khi anh vạch trần lớp ngụy trang của Kỷ Cảnh, Kỷ Cảnh đạt được mục đích trả thù, thì cậu và anh sẽ hoàn toàn cắt đứt không còn liên can gì nữa.",
    # 105
    "Lục Tư Niên lần đầu tiên trong đời nảy sinh cảm giác mờ mịt lạc lõng, anh không biết những năm tháng tiếp theo của cuộc đời mình nên trôi qua như thế nào, trả thù anh làm không được, cưới vợ sinh con anh cũng không làm được, trên cõi đời này chẳng có lấy một ai gắn kết dây dưa với anh, anh chỉ như một cánh bèo trôi dạt vô định.",
    # 106
    "Khi Trương Mạc nói với anh rằng anh có khả năng quay trở lại quân đoàn, anh thậm chí đã có một thoáng ngẩn ngơ thất thần.",
    # 107
    "Cho nên khi kết quả là thất bại, anh cũng không nảy sinh sự hụt hẫng cảm xúc quá lớn.",
    # 108
    "Thiết bị đầu cuối đột nhiên rung lên, yêu cầu cuộc gọi của Trương Mạc nhấp nháy nhảy múa trên màn hình quang học.",
    # 109
    "Lục Tư Niên ấn nút nghe máy.",
    # 110
    "“Lục Tư Niên, thành công rồi!!” Trương Mạc phấn khích gào thét.",
    # 111
    "“Nhà họ Kỷ không hiểu vì sao lại dẫn đầu bỏ phiếu thuận, sau đó nhà họ Vương có quan hệ thân thiết với nhà họ Kỷ cũng bám sát theo sau bỏ phiếu thuận, cuối cùng, cậu biết không, chính Nguyên soái đã bỏ phiếu thuận, một phần ba quân đội còn lại cũng theo Nguyên soái bỏ phiếu thuận!”",
    # 112
    "“May mắn vãi chưởng, đúng là vận may từ trên trời rơi xuống, rốt cuộc nhà họ Kỷ vì sao lại bỏ phiếu thuận chứ.”",
    # 113
    "“Lục Tư Niên, chuẩn bị thu xếp đồ đạc nhanh chóng quay về đi, vị trí Đoàn trưởng của tôi sẽ truyền lại cho cậu.”",
    # 114
    "...",
    # 115
    "Lục Tư Niên ngơ ngác nhìn kết quả bỏ phiếu hiển thị trên thiết bị đầu cuối, trong chốc lát ngay cả hô hấp cũng quên bẵng mất.",
    # 116
    "Trương Mạc nói nhà họ Kỷ dẫn đầu bỏ phiếu thuận, vậy thì nhà họ Vương tất nhiên là bỏ phiếu theo nhà họ Kỷ rồi.",
    # 117
    "Còn về Nguyên soái..., anh biết Nguyên soái qua lại rất thân thiết với nhà họ Kỷ.",
    # 118
    "Cho nên, tất cả mọi chuyện đều là vì nhà họ Kỷ.",
    # 119
    "Nhà họ Kỷ có lý do gì để bỏ phiếu thuận chứ?",
    # 120
    "Lục Tư Niên không nghĩ ra được bất kỳ nguyên nhân nào.",
    # 121
    "Chỉ có một khả năng duy nhất lóe lên trong tâm trí anh ——",
    # 122
    "Là Kỷ Cảnh sao.",
    # 123
    "Lời tác giả muốn nói:",
    # 124
    "Cảm ơn các thiên thần nhỏ đã ném vé bá vương hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-05-21 22:27:28~2023-05-22 22:13:17 nha~",
    # 125
    "Cảm ơn thiên thần nhỏ đã ném địa lôi: 31260994 1 quả;",
    # 126
    "Cảm ơn các thiên thần nhỏ đã tưới dung dịch dinh dưỡng: Túc Phong Niên, Nhàn Chi 10 bình; Noãn Noãn. 5 bình; Triều Ca, Lam Lam Lam Lam 2 bình; Triều Ca Dạ Huyền 1 bình;",
    # 127
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

header = "---\ntitle: Chương 108: Quyết định trở lại quân đoàn\n---\n\n"
content = header + "\n\n".join(paras) + "\n"

with open(target_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Written ch_108 translation successfully.")
