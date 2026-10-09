import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

trans_paras = [
    # 000
    "Một chất giọng nam trầm thấp hoàn toàn lạc điệu bỗng cắt ngang tâm tư rục rịch muốn làm bậy của đám Alpha, đồng thời cũng cắt đứt luôn động tác vung quyền muốn đập nát đầu đối phương của Kỷ Cảnh.",
    # 001
    "Giọng nói này… sao nghe quen tai thế nhỉ?",
    # 002
    "“Thằng nào đấy?” Tên Alpha cầm đầu mất kiên nhẫn chậc một tiếng, nhìn ngõ cụt trước mặt rồi chợt hiểu ra, gã quay đầu về hướng của Lục Tư Niên, “Thằng ranh…” Cách xưng hô vốn sắp thốt ra khỏi miệng bỗng cứng đờ bẻ ngoặt lại sau khi nhìn rõ Lục Tư Niên, gã nghiến răng nói,",
    # 003
    "“Ông chú này, ông cố tình đến tìm chuyện gây sự đấy à?”",
    # 004
    "Hôm nay Lục Tư Niên không mặc sơ mi quần tây của trường học, nhưng vẫn là phong cách ăn mặc cổ hủ rập khuôn như cũ, toát lên khí chất của một người đàn ông trưởng thành ngoài ba mươi tuổi. Đám Alpha này trông bộ dạng đều là thiếu niên mới mười sáu mười bảy tuổi, vừa nhìn thấy Lục Tư Niên liền bất giác liên tưởng ngay tới chủ nhiệm giám sát kỷ luật, trong lòng không kìm được mà thấy chột dạ e sợ.",
    # 005
    "Dù rằng vị “chủ nhiệm giám sát” này sở hữu một khuôn mặt trẻ trung và vô cùng nho nhã tuấn tú.",
    # 006
    "“Ba giây, biến mất khỏi đây.”",
    # 007
    "Lục Tư Niên cúi nhìn đám du côn lùn hơn mình nửa cái đầu trước mặt, mặt không cảm xúc nói.",
    # 008
    "Đám Alpha đều đang ở độ tuổi huyết khí phương cương, trong lòng ai cũng nung nấu ý nghĩ tuyệt đối không thể chịu nhục nhận thua trước mặt mỹ nhân, vừa nghe thấy câu này liền lập tức nổi giận đùng đùng: “Dựa vào cái gì chứ? Bọn tao đang nói chuyện với em gái xinh đẹp này, liên quan cái rắm gì đến ông, chẳng lẽ ông là bạn trai của ẻm chắc?!”",
    # 009
    "Đám Alpha xoa tay bẻ khớp rôm rốp, trong lúc nói chuyện Lục Tư Niên cũng tiện mắt liếc nhìn thiếu nữ đang nép mình trong góc tường, khoảnh khắc chạm phải ánh mắt của thiếu nữ, hàng chân mày anh khẽ nhíu lại một thoáng không để lại dấu vết.",
    # 010
    "“Hành vi của các cậu đã cấu thành tội quấy rối tình dục.” Lục Tư Niên vừa bình thản trần thuật, vừa tháo cúc tay áo sơ mi rồi chậm rãi xắn lên, “Có chịu cút hay không?”",
    # 011
    "Một cảm giác nguy cơ mãnh liệt lập tức quét qua cơ thể đám Alpha, bọn chúng liếc mắt ra hiệu cho nhau, thầm nghĩ nhiều Alpha như thế này chẳng lẽ lại không đánh nổi một người đàn ông, bèn gầm gừ lao vào tấn công Lục Tư Niên.",
    # 012
    "Trong con hẻm nhỏ hẹp vang lên những tiếng gào thét thảm thiết đau đớn đến thấu xương của đám Alpha, Kỷ Cảnh dựa lưng vào bờ tường đứng xem, ánh mắt âm thầm di chuyển theo từng động tác của Lục Tư Niên.",
    # 013
    "Thảm thật đấy, cậu thầm nghĩ.",
    # 014
    "Cậu vẫn nhớ rõ năm xưa Lục Tư Niên ra tay đánh người tàn bạo đến mức nào.",
    # 015
    "Cậu khẽ liếm môi, ánh mắt dán chặt vào những đường gân xanh ẩn hiện nơi yết hầu của Lục Tư Niên vì cuộc giao tranh kịch liệt mà không rời đi nửa khắc.",
    # 016
    "Tên Alpha cuối cùng ôm lấy cánh tay gãy của mình hớt hải chạy trốn mất dạng ở đầu ngõ, mọi thứ lại chìm vào yên ắng.",
    # 017
    "Lục Tư Niên đứng thẳng người dậy, lồng ngực phập phồng theo từng nhịp thở dốc, chiếc túi kín màu đen cầm trên tay ban nãy đã bị rách, đang nằm lăn lóc cách chân Kỷ Cảnh không xa.",
    # 018
    "Kỷ Cảnh hoàn hồn, vội vàng quay trở lại bộ dạng điềm đạm đáng thương như ban đầu, co rúm người lại trong góc tường.",
    # 019
    "Lục Tư Niên liếc nhìn Kỷ Cảnh một cái, không nói một lời tiến lên nhặt chiếc túi kín lên rồi quay người định rời đi.",
    # 020
    "“Đại thúc, đồ trong túi của chú hình như bị vỡ rồi kìa.” Kỷ Cảnh nhìn bóng lưng Lục Tư Niên, cất tiếng gọi.",
    # 021
    "Bóng dáng Lục Tư Niên khựng lại, anh chậm rãi xoay người, đôi mắt sâu thẳm phẳng lặng như mặt hồ không chút gợn sóng chạm phải đôi mắt của Kỷ Cảnh.",
    # 022
    "Một lúc sau, anh cất giọng: “Kỷ Cảnh?”",
    # 023
    "Tim Kỷ Cảnh đập thót một cái, sau đó liền hoảng hốt cúi đầu, dùng chất giọng thiếu nữ nghẹn ngào như sắp khóc nói: “Chú… quen anh ấy sao, không phải đâu, em tên là Dịch Nam, Kỷ Cảnh… anh ấy là anh trai của em…”",
    # 024
    "“Anh trai?” Trong giọng nói của Lục Tư Niên hiếm hoi lắm mới gợn lên một chút cảm xúc ngạc nhiên.",
    # 025
    "Ai ai cũng biết, nhà họ Kỷ chỉ có hai đứa con, một Kỷ Cảnh và một Kỷ Vân Hy.",
    # 026
    "Thiếu nữ trước mắt này trông thật sự quá đỗi giống Kỷ Cảnh.",
    # 027
    "Kỷ Cảnh rặn ra hai giọt nước mắt, ngước mắt nhìn Lục Tư Niên, yếu ớt nói: “Đại thúc, em không muốn nhắc đến chuyện này nữa đâu.”",
    # 028
    "Lục Tư Niên ngờ vực quan sát Kỷ Cảnh một lượt, thiếu nữ dung mạo diễm lệ tuyệt trần, nơi khóe mắt còn đọng giọt lệ trong suốt, cánh môi đỏ hồng, chiếc cổ thon dài, xương quai xanh rõ nét… ăn mặc lại vô cùng mát mẻ.",
    # 029
    "Lục Tư Niên giật mình, kịp thời thu hồi tầm mắt trước khi ánh nhìn trượt xuống thấp hơn, anh mất tự nhiên mím mím môi, cũng chẳng buồn đáp lời mà nghiêng người định bước đi.",
    # 030
    "“Đại thúc, cảm ơn chú, đồ đạc của chú để em đền tiền cho nhé, coi như là lời cảm ơn.”",
    # 031
    "Kỷ Cảnh thầm mắng Lục Tư Niên EQ thấp, chẳng biết thương hoa tiếc ngọc gì cả, bèn vội vàng đứng dậy đuổi theo, giữ chặt lấy tay Lục Tư Niên.",
    # 032
    "“Không cần.”",
    # 033
    "Lục Tư Niên cau mày nhìn chằm chằm vào bàn tay của Kỷ Cảnh, tựa như đang nhìn thấy một cảnh tượng thương phong bại tục trái với thuần phong mỹ tục, anh cứng rắn giật tay mình ra, rồi rảo bước nhanh biến mất ở góc phố.",
    # 034
    "Thần thái Kỷ Cảnh lập tức biến đổi, tựa như biến thành một con người khác hẳn, cậu hừ lạnh một tiếng về hướng Lục Tư Niên vừa rời đi.",
    # 035
    "Cậu là một đại mỹ nhân sống sờ sờ chủ động chạm vào anh, thế mà anh lại mang cái thái độ tránh như tránh tà thế này, cứ ở vậy cô độc suốt đời đi đồ cổ họ Lục kia!",
    # 036
    "…",
    # 037
    "Kỷ Cảnh ban đầu vốn định ở nội trú trong trường, nhưng khoảng thời gian này cậu đều cần sự giúp đỡ của Kỷ Vân Hy nên thỉnh thoảng lại chạy về nhà.",
    # 038
    "Cậu lấy được thời khóa biểu của Lục Tư Niên từ tay cậu chàng Omega tên Tiêu Tiêu kia, tính toán giờ giấc lên lớp của anh, cơ bản là mỗi thứ Ba, thứ Tư, thứ Năm sau khi tan tiết cuối cùng cậu đều có thể kịp chạy về nhà thay đồ nữ.",
    # 039
    "Theo bước đầu tiên trong kế hoạch của cậu, chính là mặc đồ nữ đi học lớp của Lục Tư Niên để cọ sự hiện diện.",
    # 040
    "Thế nhưng chuyện đụng độ Lục Tư Niên vào hôm Chủ nhật là điều nằm ngoài dự tính của cậu.",
    # 041
    "Thế là cậu nhanh chóng chỉnh sửa kịch bản của mình, vào ngày thứ Ba liền diện đồ nữ bước đến phòng học của Lục Tư Niên.",
    # 042
    "Bởi vì ở trong trường nên Kỷ Cảnh không mặc áo hai dây nữa, cậu diện một chiếc áo nỉ tay dài phối cùng chân váy ngắn kẻ caro, đôi chân dài trắng nõn thon thả khiến đám Alpha trong lớp học liên tục liếc nhìn về phía cậu.",
    # 043
    "Lớp học của Lục Tư Niên hầu như buổi nào cũng có gương mặt mới, đều là vì hâm mộ danh tiếng của Lục Tư Niên mà tới, học sinh trong lớp cũng chẳng lấy làm lạ.",
    # 044
    "Chỉ là trong lòng bọn họ thầm cảm thán cô nàng Omega lần này tới dự thính quả thực quá đỗi xinh đẹp, sao bình thường chẳng thấy xuất hiện trên diễn đàn trường bao giờ, theo lý mà nói một nữ Omega xinh đẹp nhường này sớm đã gây bão mạng rồi mới phải.",
    # 045
    "Chỉ có điều… trông dáng vẻ thì gia cảnh có vẻ không được khá giả cho lắm, quần áo nhìn cứ như kiểu dáng từ nhiều năm trước, đôi giày thể thao trắng cũng chẳng nhìn ra nhãn hiệu gì.",
    # 046
    "Phòng học đang râm ran xao động nhanh chóng im bặt ngay sau khi Lục Tư Niên cầm bình giữ nhiệt bước vào.",
    # 047
    "Lục Tư Niên điểm danh từng người một như thường lệ, không bỏ sót bất kỳ học sinh nào trốn tiết hay đi muộn, những sinh viên dự thính không có tên trong danh sách lớp quá nhiều nên anh cũng không chủ ý để tâm.",
    # 048
    "Nếu không phải trong lúc giảng bài phát hiện mấy cậu học sinh Alpha bên dưới cứ chốc chốc lại nhìn về phía góc khuất nhất của lớp học, thì Lục Tư Niên cũng chẳng nhận ra thiếu nữ mình gặp hôm nọ đang ngồi ở đó.",
    # 049
    "Cổ tay cầm bút viết bảng của Lục Tư Niên khựng lại một giây, sau đó liền xem như không có chuyện gì mà tiếp tục giảng bài.",
    # 050
    "Kể từ sau cái liếc mắt đó, anh liền cảm nhận được ánh mắt mang cảm giác hiện diện vô cùng mãnh liệt đến từ góc phòng học.",
    # 051
    "Sau khi tiếng chuông tan học vang lên, đa số sinh viên đều chẳng nán lại thêm một khắc nào, ùa ra khỏi lớp như bầy ong vỡ tổ, chớp mắt trong phòng học chỉ còn lại mấy Omega đến dự thính cùng với thiếu nữ tên Dịch Nam kia.",
    # 052
    "Mấy Omega đỏ bừng mặt tụ tập lại bàn tán điều gì đó, thỉnh thoảng lại ngước mắt nhìn trộm Lục Tư Niên.",
    # 053
    "Lục Tư Niên ngăn nắp tắt màn hình quang học, thu dọn giáo án, nhàn nhạt quét mắt nhìn xuống bên dưới rồi cất tiếng: “Các bạn học rời đi sau cùng xin nhớ tắt đèn và đóng cửa giúp tôi.”",
    # 054
    "Nói dứt lời liền cầm lấy bình giữ nhiệt bước ra khỏi phòng học.",
    # 055
    "Kỷ Cảnh thấy vậy liền vội vàng đứng dậy bám theo ra ngoài.",
    # 056
    "Lục Tư Niên chân dài, bước đi rất nhanh, Kỷ Cảnh chân cũng dài, kiên trì bền bỉ bám sát phía sau anh.",
    # 057
    "Mãi cho đến khi cả hai đi tới một góc hành lang vắng lặng, Lục Tư Niên mới dừng bước lại.",
    # 058
    "Kỷ Cảnh không kịp phanh lại, suýt chút nữa đâm sầm vào lồng ngực Lục Tư Niên, Lục Tư Niên khẽ né người tránh đi không để lại dấu vết.",
    # 059
    "“Bạn học, có việc gì sao?”",
    # 060
    "Lục Tư Niên cau mày hỏi.",
    # 061
    "Kỷ Cảnh ngẩn người, ngước mắt nhìn Lục Tư Niên, nở một nụ cười thẹn thùng: “Đại thúc, không ngờ chú lại chính là Lục giáo sư đại danh đỉnh đỉnh đấy ạ.”",
    # 062
    "Tầm mắt Lục Tư Niên không kìm được mà đánh giá thiếu nữ trước mặt, anh luôn cảm thấy cô gái này có điểm gì đó kỳ lạ, đặc biệt là khuôn mặt phiên bản nữ của Kỷ Cảnh này.",
    # 063
    "Hơn nữa việc cô đột nhiên xuất hiện trong tiết học của anh thế này thật sự có phần quá mức trùng hợp.",
    # 064
    "Lục Tư Niên ngoài mặt không biểu lộ gì, giọng điệu việc công xử theo phép công: “Lớp nào, tên gì.”",
    # 065
    "Kỷ Cảnh khựng lại một chút, có tật giật mình né tránh ánh mắt anh, lí nhí đáp: “Em là Dịch Nam, lớp 4 phòng ngự ạ.”",
    # 066
    "Lục Tư Niên “ừm” một tiếng, xoay người định đi thì lại bị thiếu nữ gọi giật lại.",
    # 067
    "“Nếu hôm ấy không nhờ có Lục giáo sư cứu em thì có lẽ em đã… Thầy vì cứu em mà làm hỏng đồ đạc, trong lòng em thực sự áy náy không yên,” Kỷ Cảnh bước nhanh vài bước lên phía trước, một lần nữa rút ngắn khoảng cách giữa hai người, rồi giơ thiết bị đầu cuối của mình lại gần,",
    # 068
    "“Hay là Lục giáo sư thêm phương thức liên lạc của em đi ạ? Em chuyển tiền trả lại cho thầy.”",
    # 069
    "Đây mới chính là mục đích cuối cùng của Kỷ Cảnh, đi tán người ta mà lại không có phương thức liên lạc thì tán kiểu gì chứ?",
    # 070
    "“Không cần đâu.”",
    # 071
    "Lục Tư Niên mím môi từ chối thẳng thừng.",
    # 072
    "Nói xong liền chẳng đợi Kỷ Cảnh kịp dây dưa thêm, dứt khoát cất bước rời đi.",
    # 073
    "Đợi Lục Tư Niên đi xa rồi, Kỷ Cảnh mới không nhịn được mà chĩa ngón giữa về phía bóng lưng anh: “Đúng là khúc gỗ chết tiệt!”",
    # 074
    "Suốt hai ngày sau đó, tiết học nào Kỷ Cảnh cũng ngồi vững như bàn thạch ở góc phòng học.",
    # 075
    "Lục Tư Niên chỉ thỉnh thoảng mới liếc nhìn về phía cậu một cái mà không để lại dấu vết, rồi chẳng có thêm bất kỳ phản ứng dư thừa nào khác.",
    # 076
    "Sau giờ học Kỷ Cảnh viện đủ mọi lý do để xin phương thức liên lạc của Lục Tư Niên, nhưng đều bị Lục Tư Niên không nể tình mà gạt phăng đi.",
    # 077
    "Kỷ Cảnh cứ ngỡ là do Lục Tư Niên chê bai không vừa mắt mình nên mới từ chối, nhưng thực tế Lục Tư Niên căn bản chẳng nghĩ tới tầng lớp đó, anh chỉ cảm thấy hành vi nằng nặc đòi phương thức liên lạc của thiếu nữ này rất thiếu logic.",
    # 078
    "Khắp Đế quốc đều đồn đại Beta Lục Tư Niên nằm trong top mười bảng xếp hạng hình mẫu lý tưởng của Beta và Omega, nam thanh nữ tú tỏ ý muốn thân cận với Lục Tư Niên nhiều vô số kể, trên thực tế đại đa số đều chỉ hàm súc đưa mắt đưa tình, toàn bộ đều bị sự phớt lờ của Lục Tư Niên đánh bật trở về mà thảm bại quy hàng, chỉ có số ít người nói thẳng mục đích, rồi nhận về cái nhíu mày từ chối dứt khoát của anh.",
    # 079
    "Nói trắng ra, Lục Tư Niên chính là một tảng đá chưa bao giờ biết thông suốt chuyện tình cảm.",
    # 080
    "Thế nhưng anh không thể không thừa nhận Dịch Nam sở hữu một gương mặt cực kỳ khó quên, đó là một khuôn mặt khiến anh kinh diễm, khiến anh bất giác cứ nhìn về phía góc phòng học trong giờ giảng bài.",
    # 081
    "Tiết học ngày thứ Sáu, anh không còn nhìn thấy bóng dáng Dịch Nam nữa.",
    # 082
    "Lục Tư Niên thu hồi tầm mắt, tiếp tục giảng bài.",
    # 083
    "Tiết học ngày thứ Hai, Dịch Nam vẫn không tới.",
    # 084
    "Thế nhưng vào ngày thứ Ba, khoảnh khắc Lục Tư Niên vừa bước chân vào phòng học, anh liền nhìn thấy thiếu nữ đang ngồi ở góc quen thuộc.",
    # 085
    "Thân hình Lục Tư Niên khựng lại một thoáng, bước lên bục giảng bắt đầu tiết học hôm nay.",
    # 086
    "Thời khóa biểu ngày thứ Sáu và thứ Hai của Kỷ Cảnh trùng giờ nên không thể đến lớp của Lục Tư Niên, tiết thực chiến của Vương Bằng hôm thứ Sáu sau khi tan lớp, Vương Bằng còn cố tình giữ riêng một mình cậu lại để đối kháng với người máy cấp S, cậu bị đánh rất sướng mà đánh cũng rất đã tay.",
    # 087
    "Alpha trên người có va chạm trầy xước là chuyện khó tránh khỏi, thế nên cậu căn bản không để ý thấy trên đôi chân lộ ra của mình đang chằng chịt những vết bầm tím loang lổ, nổi bật trên làn da trắng nõn trông vô cùng rợn người.",
    # 088
    "Cảnh tượng này khiến mấy cậu học sinh Alpha liên tục ngoái đầu nhìn trộm, bị Lục Tư Niên đứng trên bục giảng thu trọn vào tầm mắt.",
    # 089
    "“Hàng thứ hai người thứ ba, cậu đứng dậy trả lời câu hỏi này cho tôi.” Lục Tư Niên gõ nhẹ lên bục giảng, cất tiếng.",
    # 090
    "Cậu học sinh Alpha bị bắt quả tang lúng túng đứng dậy, ấp úng chẳng nói nên lời.",
    # 091
    "Lục Tư Niên biết câu hỏi này đã vượt ngoài chương trình học, chẳng ai có thể trả lời được, đang định bảo Alpha kia ngồi xuống thì chợt thấy nơi góc phòng học có một cánh tay giơ lên.",
    # 092
    "“Bạn học giơ tay trả lời thử xem.”",
    # 093
    "Kỷ Cảnh nhìn chằm chằm Lục Tư Niên nhếch môi cười, đứng dậy đưa ra câu trả lời vô cùng trôi chảy mạch lạc.",
    # 094
    "Ánh mắt Lục Tư Niên dừng lại trên khuôn mặt thiếu nữ vài giây, gật đầu ra hiệu cho cô ngồi xuống: “Ừm, rất tốt.”",
    # 095
    "Anh đâu hay biết câu khen ngợi “rất tốt” này đã dấy lên làn sóng chấn động lớn đến nhường nào trong lòng các học sinh trong lớp.",
    # 096
    "Lục Tư Niên trước giờ chưa từng khen ngợi bất kỳ một học sinh nào.",
    # 097
    "Cả đám người âm thầm bàn tán xôn xao, mãi cho đến khi tiếng chuông tan học vang lên, bọn họ vẫn còn dùng ánh mắt đầy ẩn ý nhìn về phía Kỷ Cảnh.",
    # 098
    "Lục Tư Niên rời khỏi phòng học theo đúng quy trình, Kỷ Cảnh cũng theo đúng quy trình bám sát theo sau.",
    # 099
    "“Lục giáo sư, em có rất nhiều câu hỏi muốn thỉnh giáo thầy, thầy có thể cho em phương thức liên lạc được không ạ?” Kỷ Cảnh đi theo Lục Tư Niên trên hành lang vắng lặng, kiên trì không biết mệt mỏi hỏi.",
    # 100
    "Lục Tư Niên dừng bước, xoay người nhìn cậu, nói: “Nếu buổi nào em cũng chăm chỉ nghe giảng thì em sẽ chẳng có bất kỳ câu hỏi nào cả.”",
    # 101
    "Kỷ Cảnh nghe vậy liền nghẹn lời, nhất thời chẳng tìm ra câu gì để phản bác.",
    # 102
    "Thiếu nữ trước mặt bỗng nhiên ngập ngừng cúi đầu xuống, Lục Tư Niên thuận theo động tác của cô nhìn xuống dưới, đôi chân dài trắng nõn chằng chịt những vết thương bầm tím chói mắt liền đập thẳng vào tầm mắt anh.",
    # 103
    "Lục Tư Niên bỗng như bị điện giật mà vội vàng thu hồi tầm mắt, nhìn sang chỗ khác.",
    # 104
    "“Thế nhưng, em không thể buổi nào cũng đến nghe giảng được mà.” Kỷ Cảnh cúi đầu, nghẹn ngào cất giọng.",
    # 105
    "“Tại sao?” Lục Tư Niên hỏi thẳng thừng.",
    # 106
    "Kỷ Cảnh vừa ấp a ấp úng, vừa suy nghĩ xem làm sao để diễn xuất thiết lập nhân vật của mình trông đáng thương hơn một chút.",
    # 107
    "“Là vì em căn bản không phải là học sinh của Học viện quân sự Đế quốc, đúng không? Bạn học Dịch Nam.” Giọng nói trầm thấp của Lục Tư Niên vang lên bên tai.",
    # 108
    "Kỷ Cảnh ngẩn người ngước đầu lên, vừa khéo va thẳng vào một đôi mắt đen láy sâu thẳm khôn cùng."
]

print(f"Total paragraphs for ch_092: {len(trans_paras)}")

out_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_092"
header = "---\ntitle: Chương 92: Dịch Nam trà trộn\n---\n\n"
content = header + "\n\n".join(trans_paras) + "\n"

trans_path = os.path.join(out_dir, "translation.md")
with open(trans_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved {trans_path} successfully!")
