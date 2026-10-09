# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_112\translation.md"

paras = [
    # 000
    "Lục Tư Niên là người chủ động ngồi lên, tuy rằng biểu cảm và cơ bụng khi ấy đều căng cứng đến cực điểm, nhưng giờ nghĩ lại, mọi hành vi của anh đều mang tính mục đích rõ ràng.",
    # 001
    "Vậy nên Lục Tư Niên sớm đã biết rõ, bắt buộc phải hoàn thành đánh dấu trọn đời thì mới có thể cứu được cậu sao.",
    # 002
    "Chỉ đơn thuần là vì cậu đã đỡ giúp anh một mũi tiêm?",
    # 003
    "Vì một tinh thần trách nhiệm viển vông hư ảo mà có thể làm đến bước này sao?",
    # 004
    "Kỷ Cảnh đột nhiên cảm thấy những phỏng đoán trước đây của mình trở nên chẳng còn mấy căn cứ xác đáng nữa.",
    # 005
    "Trên đường về nhà, bộ não hỗn loạn của Kỷ Cảnh vẫn chẳng thể nghĩ thông được mấu chốt bên trong, điều duy nhất rõ ràng chính là cậu đã đánh dấu trọn đời Lục Tư Niên, điều này đồng nghĩa với việc Lục Tư Niên cả đời này chỉ thuộc về một mình Kỷ Cảnh cậu.",
    # 006
    "Sẽ không còn bất kỳ một Alpha nào có thể đánh dấu anh được nữa, Omega và Beta cũng sẽ vì tuyến thể của anh đã khắc sâu dấu ấn trọn đời của cậu mà chủ động tránh xa.",
    # 007
    "Không một ai có thể chấp nhận người bạn đời của mình từng bị một Alpha khác đánh dấu trọn đời, Lục Tư Niên cả đời này không thể nào có thêm phối ngẫu nào khác.",
    # 008
    "Một luồng cảm giác sung sướng mãnh liệt đến mức khó lòng ngó lơ tràn ngập trong lồng ngực Kỷ Cảnh.",
    # 009
    "Thiết bị đầu cuối trên cổ tay bất chợt vang lên một tiếng bíp, Kỷ Cảnh tùy tiện liếc mắt nhìn qua, phát hiện đó là thông báo đẩy tin tức, vốn định dời tầm mắt đi thì bất chợt bắt gặp hình ảnh đính kèm của bản tin.",
    # 010
    "“Tân quân đoàn trưởng Đệ tam quân đoàn Lục Tư Niên chính thức trở lại đội ngũ sau chuỗi sóng gió.”",
    # 011
    "Dưới tiêu đề nổi bật rõ ràng là một bức ảnh, trong bức ảnh một người đàn ông vóc dáng cao lớn đang xách theo chiếc túi hành lý quân dụng đơn sơ, lặng lẽ đứng trước cổng lớn tòa nhà chính vụ của Đệ tam quân đoàn.",
    # 012
    "Kỷ Cảnh chỉ liếc mắt một cái là nhận ra ngay người đàn ông trong ảnh chính là Lục Tư Niên.",
    # 013
    "Lục Tư Niên khi không mặc âu phục đã cởi bỏ đi vẻ tao nhã dịu dàng trôi nổi ngoài bề mặt, một bộ đồ huấn luyện quân dụng màu đen bó sát phác họa rõ nét vòng eo rắn rỏi hữu lực, khí trường lãnh đạm nghiêm nghị toát ra khắp toàn thân khiến người ta khó lòng tin nổi anh lại là một Omega.",
    # 014
    "Kỷ Cảnh nhìn đến mức ngơ ngẩn xuất thần, tính toán lại thời gian, hôm nay vừa vặn là ngày Lục Tư Niên trở về quân đoàn.",
    # 015
    "Đệ tam quân đoàn không nằm ở thủ đô đế quốc, mà được thiết lập đóng quân trên một tinh cầu nhỏ cằn cỗi hoang vu giáp ranh biên giới đế quốc.",
    # 016
    "Mấy ngày trước Kỷ Cảnh ma xui quỷ khiến thế nào lại đi tra cứu thông tin tinh hạm đến Đệ tam quân đoàn, các chuyến đi ít ỏi đến đáng thương đã đành, một khi ngồi là phải mất trọn vẹn hai ngày trời.",
    # 017
    "Lục Tư Niên đã đi rồi, không còn ở thủ đô nữa, mà đang ở trên một tinh cầu cách xa cậu hàng ức năm ánh sáng.",
    # 018
    "Anh liệu có còn trở về không? Khi nào?",
    # 019
    "Cậu và Lục Tư Niên liệu có còn cơ hội gặp lại nhau nữa không.",
    # 020
    "Kỷ Cảnh nhìn chằm chằm vào người trong bức ảnh, nhận thức được rằng cậu và Lục Tư Niên thực sự đang ngày càng xa cách hệt như những gì cậu từng tưởng tượng trước đây.",
    # 021
    "Sự bốc đồng đã vượt lên trước lý trí chi phối toàn bộ cơ thể, đợi đến khi Kỷ Cảnh kịp phản ứng lại thì đã bấm gọi vào số máy của Vương Bằng rồi.",
    # 022
    "“A lô, Kỷ Cảnh à?”",
    # 023
    "“Vương huấn luyện viên, đợt tuyển quân Đệ tam quân đoàn mà trước đây thầy nói ấy...” Kỷ Cảnh hiếm hoi hạ mình gọi một tiếng Vương huấn luyện viên, nói đến chỗ then chốt vẫn có chút khó mở lời, “Bây giờ còn tuyển nữa không ạ?”",
    # 024
    "“Hả? Không phải đến nước này rồi mày mới nghĩ thông suốt là muốn đi đấy chứ?!” Vương Bằng ở đầu dây bên kia kích động nhảy dựng lên, “Kỷ Cảnh, tao thấy mày đúng là khắc tinh của tao mà, bảo mày đi sớm thì mày không đi, bây giờ đợt tuyển quân đã kết thúc từ lâu rồi, trừ phi mày có ô dù chống lưng cực khủng, bằng không muốn đi thì đợi sang năm đi nhé!”",
    # 025
    "Đế quốc coi trọng vũ trang, các quân đoàn đều có quyền tự chủ quản hạt, nhưng về cơ bản chế độ tuyển quân của mỗi quân đoàn đều vô cùng nghiêm ngặt khắt khe, trong đó Đệ tam quân đoàn là gắt gao nhất, chưa từng có ai có thể dựa vào cửa sau mà bước vào.",
    # 026
    "Kỷ Cảnh cũng biết chuyện này là bất khả thi, chỉ trách bản thân quá mức bốc đồng mà gọi cuộc điện thoại này.",
    # 027
    "Một năm, lần đầu tiên cậu cảm thấy khoảng thời gian một năm lại đằng đẵng dài đến thế.",
    # 028
    "“Không có gì đâu, em chỉ thuận miệng hỏi một câu thôi.” Cậu tỏ ra bình tĩnh, nhưng rồi lại không cam lòng mà bồi thêm một câu, “Chẳng lẽ Đệ tam quân đoàn không có chế độ tuyển quân đợt hai sao ạ?”",
    # 029
    "Cậu đã đặc biệt tra cứu qua, kỳ tuyển quân lần này căn bản chưa đạt đủ chỉ tiêu số lượng dự kiến.",
    # 030
    "“Không có, đừng có nằm mơ giữa ban ngày nữa,” Vương Bằng bực bội gắt gỏng, “Đệ tam quân đoàn từ trước đến nay chưa từng có chuyện tuyển quân đợt hai bao giờ, đợi sang năm đi.”",
    # 031
    "Vương Bằng tức đến nghiến răng nghiến lợi, thằng nhãi Kỷ Cảnh này căn bản không hề biết rằng chỉ vì một câu thuận miệng không đi của nó, ông đã bị tên Chu Độ kia tra tấn suốt nửa tháng trời, lại còn phải chịu đựng bộ mặt lạnh lùng không rõ nguyên do của Lục Tư Niên.",
    # 032
    "Tuy miệng thì bảo không được, nhưng sau khi cúp máy ông vẫn gọi một cuộc điện thoại cho Chu Độ.",
    # 033
    "Phía Chu Độ hình như đang bận rộn chuyện Lục Tư Niên tiếp nhận chức vụ đoàn trưởng, nghe thấy chuyện này liền khó xử nhíu mày: “Tuyển quân đợt hai á? Khó nói lắm, Đệ tam quân đoàn thành lập ngần ấy năm trời cũng chưa từng có tiền lệ tuyển quân đợt hai bao giờ, tuy rằng lần này người chiêu mộ được quả thực quá ít.”",
    # 034
    "Không phải là do số người báo danh quá ít, mà là người đạt tới ngưỡng tiêu chuẩn chỉ đếm trên đầu ngón tay, Đệ tam quân đoàn từ trước đến nay luôn cầu tinh chứ không cầu đa.",
    # 035
    "“Thế nhưng thằng nhóc Kỷ Cảnh đó quả thực là một thiên tài, không thu nhận thì quá mức đáng tiếc, vốn dĩ chuyện này biết đâu chừng còn có cơ hội xoay chuyển, Trương Mạc khá hài lòng về Kỷ Cảnh, chỉ cần ông ấy gật đầu là được, nhưng hiện tại đoàn trưởng là Lục Tư Niên, con người cậu ta cổ hủ quy củ thế nào chẳng lẽ cậu không biết...”",
    # 036
    "Chu Độ cũng cảm thấy tiếc nuối, nói đến đoạn sau tự mình cũng thấy phiền não: “Thôi được rồi, tôi thử nhắc với Lục Tư Niên xem sao, nhưng hy vọng không lớn đâu nhé.”",
    # 037
    "“Được.”",
    # 038
    "Vương Bằng gật đầu, ông cũng thừa hiểu đây không đơn thuần là vấn đề hy vọng không lớn, mà căn bản là chuyện không thể nào.",
    # 039
    "Bên kia Chu Độ cúp điện thoại, sau khi bận rộn xong công tác bàn giao ở chỗ mình, mới bình tâm lại quan sát Lục Tư Niên đang xử lý văn kiện cách đó không xa.",
    # 040
    "Đường nét góc nghiêng của Lục Tư Niên sắc bén lạnh lùng, trên sống mũi cao thẳng đeo chiếc kính gọng nửa màu đen bảo thủ, biểu cảm quanh năm căng thẳng nghiêm nghị, nhìn thế nào cũng toát lên vẻ cứng nhắc vô tình.",
    # 041
    "Chu Độ trước đây vốn không muốn đụng chạm đến vẻ uy nghiêm đáng sợ của Lục Tư Niên, nói chuyện với Lục Tư Niên một câu thôi là gã cũng phải đắn đo nửa ngày trời.",
    # 042
    "Thế nhưng cuối cùng dựa vào sự thèm muốn nhân tài đối với Kỷ Cảnh, gã vẫn mở lời.",
    # 043
    "Vốn dĩ gã cứ ngỡ Lục Tư Niên sẽ chẳng thèm suy nghĩ mà trực tiếp không chút biểu cảm, trầm giọng buông một câu “Tôi bận lắm”, hoặc giả là đặt bút xuống giống như một vị lãnh đạo ngoài năm mươi tuổi, dùng ánh mắt mang đầy tính áp bách nhìn chằm chằm gã, rồi buông thêm câu “Chu Độ, cần tôi nói cho cậu biết lý do tại sao không được không?”.",
    # 044
    "Dù sao trước đây khi Lục Tư Niên còn làm chỉ huy quan cũng đối xử với cấp dưới của mình như vậy.",
    # 045
    "Thế nhưng gã không ngờ rằng Lục Tư Niên lại có phản ứng này.",
    # 046
    "Cây bút máy trên tay anh sau khi gã dứt lời liền khựng lại trên mặt giấy, ngòi bút kiên cố lấy tốc độ mắt thường có thể thấy được mà cong vẹo đi, cuối cùng phát ra một tiếng tách gãy gập.",
    # 047
    "Tuy rằng khoảng thời gian ngắn đến mức gần như có thể bỏ qua, nhưng Chu Độ phát hiện Lục Tư Niên vừa rồi đã mất tập trung.",
    # 048
    "“Cậu nói, là do chính Kỷ Cảnh đề xuất muốn tuyển quân đợt hai.” Giọng nói Lục Tư Niên có chút khàn, lại có chút trầm thấp, khiến Chu Độ không tài nào đoán nổi thái độ của anh.",
    # 049
    "“Đúng vậy, do chính thằng nhóc đó tự đề xuất đấy, quỷ mới biết tại sao trước đó nó lại không chịu tham gia, nhưng quân đoàn chúng ta chẳng phải xưa nay luôn tuân thủ nguyên tắc không bỏ sót bất kỳ mầm non ưu tú nào sao, dù sao năm nay người chiêu mộ cũng quá ít...” Chu Độ chuyển đề tài, dốc hết sức muốn khuyên nhủ Lục Tư Niên, muốn nói rằng quy củ là chết còn con người là sống, nhưng trong lòng gã thực ra cũng không chắc chắn, Đệ tam quân đoàn chưa từng có tiền lệ tuyển quân đợt hai, đổi lại là Trương Mạc cũng sẽ do dự ngập ngừng, huống chi là một Lục Tư Niên răm rắp khuôn phép.",
    # 050
    "Lục Tư Niên cụp mắt chăm chú nhìn ngòi bút bị gãy, trong lòng rõ ràng biết mình không nên đồng ý, vậy mà vẫn không cách nào khống chế nổi việc phỏng đoán ý đồ của Kỷ Cảnh.",
    # 051
    "Tại sao lại muốn đến Đệ tam quân đoàn, có liên quan gì đến anh không, Lục Tư Niên không muốn tiếp tục tự mình đa tình nữa.",
    # 052
    "Nhưng xét trên bất kỳ phương diện nào, Kỷ Cảnh đều có đủ tư chất để gia nhập Đệ tam quân đoàn.",
    # 053
    "“Tuyển.”",
    # 054
    "Cuối cùng, Lục Tư Niên cất lời: “Đợt tuyển quân thứ hai hướng tới toàn thể đế quốc, tiêu chuẩn xét tuyển tăng thêm hai mươi phần trăm so với đợt tuyển quân đầu tiên.”",
    # 055
    "...",
    # 056
    "Thế nào là lên voi xuống chó chìm nổi thất thường, Kỷ Cảnh dùng trọn vẹn một ngày hôm nay của mình để trả lời.",
    # 057
    "Đầu tiên là bị chấn động bởi việc Lục Tư Niên công khai mình là Omega, kế đó lại bị chấn động bởi việc chính mình đã đánh dấu trọn đời Lục Tư Niên, cuối cùng là bị chấn động tột độ bởi thông báo tuyển quân đợt hai do Đệ tam quân đoàn ban hành!",
    # 058
    "Chuyện này là sao chứ! Chẳng phải bảo là tuyệt đối không thể nào có tuyển quân đợt hai sao!",
    # 059
    "Kỷ Cảnh gọi một cuộc điện thoại cho Vương Bằng, rồi mới hay tin đây là chỉ thị do chính Lục Tư Niên đích thân hạ đạt.",
    # 060
    "Kỷ Cảnh không dám chắc liệu Lục Tư Niên có phải vì mình hay không, nhưng cậu không thể nào khống chế nổi nhịp tim đang rộn ràng nhảy múa của mình.",
    # 061
    "Cậu gần như thức trắng cả đêm, dùng trọn vẹn một buổi tối để tìm hiểu quy trình tuyển quân của Đệ tam quân đoàn, sau đó chuẩn bị đầy đủ mọi thông tin tư liệu cần thiết của bản thân.",
    # 062
    "Rồi ngay ngày đầu tiên của đợt tuyển quân thứ hai liền xuất hiện tại địa điểm tuyển quân, đập bốp một cái tờ đơn đăng ký lên mặt bàn tiếp nhận.",
    # 063
    "Hệt như được tiêm máu gà, Kỷ Cảnh hừng hực khí thế hăng say, ra đòn còn mạnh mẽ gấp mấy lần so với bình thường.",
    # 064
    "Cuối cùng khi bước ra khỏi trường thi tuyển quân chật ních người, cậu chẳng hề nhận ra một đám Alpha đang nhìn chằm chằm vào thành tích chung cuộc trên màn hình lớn công bố mà rớt cả quai hàm.",
    # 065
    "Kỷ Cảnh chưa bao giờ nghi ngờ năng lực của bản thân, ngay trước khi kết quả được công bố, cậu đã tuyên bố quyết định đi gia nhập Đệ tam quân đoàn ngay trên bàn ăn gia đình.",
    # 066
    "Mẹ Kỷ kinh ngạc đánh rơi cả đũa, ba Kỷ bị rượu trắng sặc đến ho sù sụ, Kỷ Vân Hy sau giây phút ngơ ngác ngắn ngủi liền kích động trừng mắt nhìn Kỷ Cảnh.",
    # 067
    "Kỷ Vân Hy tỏ rõ biểu cảm rằng cô biết thừa lý do vì sao Kỷ Cảnh đột nhiên lại muốn đến Đệ tam quân đoàn rồi!",
    # 068
    "“Tiểu Cảnh, ba cứ tưởng con không có hứng thú với Đệ tam quân đoàn chứ.”",
    # 069
    "Ba Kỷ bình tĩnh uống thêm hai ngụm rượu, ông xưa nay không hề phản đối việc con trai mình đi nhập ngũ vài năm, một người thừa kế gia tộc ưu tú nhất định phải tôi luyện được phẩm chất của một người lính.",
    # 070
    "Mẹ Kỷ thì lại không nghĩ như vậy, bà lo lắng đặt đũa xuống, trong mắt ngấn lệ: “Đến quân đoàn vất vả biết bao nhiêu, chuyến này đi lại phải mất mấy năm trời, ba mẹ biết bao lâu mới được gặp lại con?”",
    # 071
    "“Bốn năm ạ.”",
    # 072
    "Thời hạn nghĩa vụ quân sự mặc định của quân đoàn đế quốc là bốn năm, sau bốn năm đi hay ở sẽ bàn tiếp.",
    # 073
    "“Tại sao đột nhiên lại muốn đến Đệ tam quân đoàn? Hiện tại quân đoàn trưởng của Đệ tam quân đoàn là Lục Tư Niên đúng không...”",
    # 074
    "Đối diện với câu hỏi của ba Kỷ, Kỷ Cảnh có chút chột dạ, nhưng Kỷ Vân Hy thì lại như đang nghẹn một bí mật kinh thiên động địa nào đó, hết lần này đến lần khác vỗ vỗ vào đùi Kỷ Cảnh.",
    # 075
    "Sau bữa tối, Kỷ Vân Hy đẩy cậu vào trong phòng.",
    # 076
    "“Khai thật mau, có phải mày vì Lục Tư Niên nên mới đến Đệ tam quân đoàn không hả!”",
    # 077
    "Kỷ Vân Hy nói xong bí mật kìm nén bấy lâu, sảng khoái thở phào một hơi.",
    # 078
    "Kỷ Cảnh cứng cổ, mạnh miệng chối: “Không phải, em chỉ muốn đi trải nghiệm cuộc sống quân đoàn thôi, đám Alpha trong trường học yếu ớt quá.”",
    # 079
    "“Ồ—— thế cơ à.” Kỷ Vân Hy cố tình kéo dài giọng, “Không biết đứa nào mấy ngày nay mặt mày thối hoắc như cái gì ấy nhỉ.”",
    # 080
    "Kỷ Cảnh chẳng buồn để ý đến cô nữa, quay người bắt đầu thu dọn hành lý của mình.",
    # 081
    "Kỷ Vân Hy nhìn cậu một hồi, cuối cùng thở dài một tiếng, thấm thía khuyên nhủ: “Tình cảm là phải nói chuyện, nói, mày có hiểu không hả? Cần đôi bên cùng thổ lộ tâm tình với nhau, có những chuyện chỉ khi mày nói ra rõ ràng rành mạch thì đối phương mới có thể thấu hiểu được, biết đâu chừng những gì Lục Tư Niên nghĩ căn bản không hề giống như những gì mày tưởng thì sao?”",
    # 082
    "“Nhưng mà tao làm thế nào cũng không thể ngờ nổi Lục Tư Niên vậy mà lại là một Omega, chuyện này mày có biết không, sáng nay tao đã định hỏi rồi, thời gian mà Lục Tư Niên khởi tố Lâm Diên Sơn khai báo vừa vặn trùng khớp với lúc mày không có mặt, rốt cuộc giữa mày và anh ta đã xảy ra chuyện gì hả?” Kỷ Vân Hy chỉnh lại thái độ nghiêm túc hỏi han.",
    # 083
    "Xảy ra chuyện gì sao? Đánh dấu trọn đời rồi có tính không.",
    # 084
    "Kỷ Cảnh thầm nghĩ trong lòng, cuối cùng ba tấc lưỡi qua loa đuổi khéo Kỷ Vân Hy ra ngoài.",
    # 085
    "Danh sách kết quả tuyển quân đợt hai có rất nhanh, lần này tổng cộng chỉ tuyển đúng năm người, đều là Alpha, cái tên Kỷ Cảnh không ngoài dự đoán chễm chệ đứng ở vị trí đầu bảng.",
    # 086
    "Sau khi nhận được giấy báo trúng tuyển, theo quy trình Kỷ Cảnh sẽ phải tự túc xuất phát đến tinh cầu nơi Đệ tam quân đoàn đóng quân, thời gian quy định là trong vòng nửa tháng.",
    # 087
    "Thế nhưng Kỷ Cảnh mọi thứ đều đã chuẩn bị sẵn sàng từ sớm, thủ tục tạm dừng việc học bên phía trường quân sự đế quốc cũng đã hoàn tất.",
    # 088
    "Theo quy chế, nhập ngũ có thể miễn trừ niên hạn đào tạo tại trường quân sự đế quốc, chỉ cần cậu hoàn thành thuận lợi bốn năm nghĩa vụ quân sự thì sẽ tự động tốt nghiệp Học viện Quân sự Đế quốc.",
    # 089
    "Bởi vậy sau khi nhận được kết quả, cậu liền đặt luôn vé tinh hạm hướng về tinh cầu hoang vu kia.",
    # 090
    "Ban đầu ba mẹ Kỷ đề nghị lái tinh hạm tư nhân đưa cậu đi, nhưng bị Kỷ Cảnh từ chối.",
    # 091
    "Hai ngày sau, Kỷ Cảnh đứng sừng sững trước cổng lớn tòa nhà chính vụ của Đệ tam quân đoàn.",
    # 092
    "“Xin chào, tôi là Kỷ Cảnh, tân binh Đệ tam quân đoàn.”",
    # 093
    "Lời tác giả:",
    # 094
    "Cảm ơn các thiên thần nhỏ đã ném lôi hoặc tưới dung dịch dinh dưỡng cho tôi trong khoảng thời gian 2023-06-02 22:58:16~2023-06-09 08:48:08 nhé~",
    # 095
    "Cảm ơn thiên thần nhỏ ném địa lôi: Tiểu Bắc 1 cái;",
    # 096
    "Cảm ơn các thiên thần nhỏ tưới dung dịch dinh dưỡng: Là Tư Uông Không Phải Tất Chân Nha, Nguyệt Cẩn, Miêu 10 bình; Bạch Nhật Mộng xy, Cột Dương 5 bình; Nhàn de Diêm 2 bình; Quyện Từ 1 bình;",
    # 097
    "Vô cùng cảm ơn sự ủng hộ của mọi người dành cho tôi, tôi sẽ tiếp tục cố gắng!"
]

content = "---\ntitle: Chương 112: Cơ hội tuyển quân đợt hai\n---\n\n" + "\n\n".join(paras) + "\n"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Wrote {target_path} with {len(paras)} paras.")
