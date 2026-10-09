import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

trans_paras = [
    # 000
    "Đầu óc Kỷ Cảnh trống rỗng trong chốc lát, rất nhanh sau đó cậu liền nhận ra Lục Tư Niên sớm đã nhìn thấu lời nói dối của mình.",
    # 001
    "Dưới tròng kính mỏng manh, đôi mắt sâu thẳm kia dường như muốn nhìn thấu tâm can cậu.",
    # 002
    "Thế nhưng,",
    # 003
    "Kỷ Cảnh lại cười thầm một tiếng trong lòng.",
    # 004
    "Cùng lúc đó, khóe mắt cậu bắt đầu ngập tràn hơi nước với tốc độ mắt thường cũng có thể nhìn thấy, hàng mi cong vút khẽ chớp động đầy vẻ yếu đuối, hàm răng ngọc cắn chặt lấy bờ môi phấn hồng, cậu hoảng loạn cúi gằm đầu xuống, tựa như không muốn để Lục Tư Niên nhìn thấy dáng vẻ chật vật đáng thương của mình.",
    # 005
    "“Em xin lỗi…” Kỷ Cảnh kìm nén tiếng nức nở lí nhí nói, “Em không cố ý lừa chú đâu.”",
    # 006
    "Kỷ Cảnh căn bản không hề phát hiện ra rằng, người đàn ông họ Lục trước mặt sớm đã cứng đờ như một tảng đá hình người ngay khoảnh khắc mắt cậu vừa hoe đỏ.",
    # 007
    "Lục Tư Niên căng cứng mặt mày, hồi lâu sau mới khẽ “ừm” một tiếng.",
    # 008
    "“Em không phải là sinh viên của trường quân đội Đế quốc, em chỉ là con gái của một cô lao công quét dọn trong trường thôi,” Hàng mi đang rủ xuống của Kỷ Cảnh bỗng khẽ run rẩy, sau đó cậu ngước mắt lên, cố nén giọt nước mắt chực trào mà nhìn Lục Tư Niên.",
    # 009
    "“Em là con gái riêng của Kỷ Trình – gia chủ đương nhiệm của nhà họ Kỷ, mẹ em không muốn dính líu gì tới ông ta, thế nên ban đầu em mới không muốn cho chú biết mối quan hệ giữa em và Kỷ Cảnh.” Kỷ Cảnh mở to mắt bắt đầu nói hươu nói vượn, đồng thời trong lòng thầm cúi đầu tạ lỗi với ông bố thật thà chính trực của mình.",
    # 010
    "Thân phận bối cảnh này chính là thứ cậu đặc biệt đo ni đóng giày riêng cho Lục Tư Niên, hoàn cảnh xuất thân gần như y hệt này đủ để khiến Lục Tư Niên nảy sinh thứ tình cảm khác biệt đối với cậu.",
    # 011
    "“Nếu không phải hôm thứ Ba em đi theo mẹ tới trường để phụ giúp mẹ, thì em cũng không tình cờ phát hiện ra đại thúc chính là Lục giáo sư đại danh đỉnh đỉnh,” Kỷ Cảnh tiếp tục diễn xuất,",
    # 012
    "“Em biết tiết học của thầy có thể vào dự thính nên em mới tới, nhưng em thực sự không muốn lừa dối thầy đâu, em chỉ là… chỉ là không muốn để thầy biết em chỉ là con gái của một cô lao công quét rác…” Một giọt nước mắt nóng hổi cuối cùng cũng không kìm được mà lăn dài trên khóe mắt thiếu nữ, sau khi ý thức được điều này, thiếu nữ liền dùng sức quệt mạnh khóe mắt, rồi xấu hổ cúi gằm mặt xuống.",
    # 013
    "“Thứ Hai và thứ Sáu mẹ đều không đi làm, thế nên em cũng không vào trường được… hu hu… em xin lỗi.”",
    # 014
    "Nhìn từ góc độ của Lục Tư Niên, anh vừa vặn có thể thấy rõ mồn một những giọt nước mắt không ngừng lăn dài trên chiếc cằm trắng nõn thanh tú của thiếu nữ.",
    # 015
    "Bốn phía quá đỗi tĩnh lặng, ngoài tiếng thút thít nhỏ nhẹ tựa mèo con của thiếu nữ ra, anh chỉ có thể nghe thấy nhịp tim bỗng chốc đập loạn một nhịp của chính mình.",
    # 016
    "“Đưa thiết bị đầu cuối cho tôi.”",
    # 017
    "Lục Tư Niên căng cứng quai hàm, cất lên một câu.",
    # 018
    "Thiếu nữ dường như chưa kịp phản ứng, ngơ ngác ngước đầu lên, trên gương mặt thanh tú diễm lệ vẫn còn vương vệt nước mắt chưa khô.",
    # 019
    "Đôi mắt Lục Tư Niên trầm xuống, đè nén cảm giác ngứa ngáy kỳ lạ trong lòng, anh trực tiếp giơ cổ tay để lộ ra thiết bị đầu cuối của mình, lặp lại một lần nữa: “Không phải em muốn xin phương thức liên lạc của tôi sao.”",
    # 020
    "Kỷ Cảnh nghe vậy theo bản năng nâng cổ tay lên chạm nhẹ vào thiết bị đầu cuối của Lục Tư Niên, độ rung truyền đến nơi cổ tay báo hiệu hai người đã kết bạn thành công.",
    # 021
    "“Có câu hỏi nào thì có thể hỏi tôi.”",
    # 022
    "Lục Tư Niên hạ cánh tay xuống, cất giọng lạnh lùng cứng nhắc.",
    # 023
    "Nói dứt lời liền dứt khoát quay người rời đi.",
    # 024
    "Kỷ Cảnh đến nước mắt cũng chưa kịp lau, ngơ ngác nhìn giao diện trên màn hình thiết bị đầu cuối.",
    # 025
    "Sao tự nhiên lại cho rồi?",
    # 026
    "…",
    # 027
    "Ảnh đại diện của Lục Tư Niên là bức ảnh thẻ chụp trong thời gian anh còn tại ngũ, mặc một bộ quân phục chỉ huy trưởng Đế quốc, nghiêm túc cứng nhắc nhìn thẳng vào ống kính.",
    # 028
    "Không phải Kỷ Cảnh chê bai, mà ngay cả ông bố Kỷ Trình của cậu giờ cũng chẳng thèm lấy ảnh thẻ chính diện làm ảnh đại diện nữa rồi, Lục Tư Niên đường đường là một thanh niên chưa tới ba mươi tuổi, mà sống chẳng khác nào một ông cụ già sáu bảy mươi tuổi nghiêm khắc.",
    # 029
    "Nếu không phải nhờ khuôn mặt kia quá mức tuấn tú chịu đòn tốt, thì cậu đến cả hứng thú nhắn tin tán tỉnh Lục Tư Niên cũng chẳng buồn có.",
    # 030
    "Kỷ Cảnh thong dong nằm dài trên giường, bấm mở vòng bạn bè của Lục Tư Niên.",
    # 031
    "Lục Tư Niên chắc hẳn là kẻ không bao giờ biết cài đặt phạm vi hiển thị hoa mỹ hay chữ ký cá nhân màu mè, tên hiển thị vẻn vẹn ba chữ Lục Tư Niên, hình nền đều là mặc định ban đầu, lướt hết toàn bộ vòng bạn bè cũng chưa đầy hai mươi bài đăng, trong đó toàn là thông báo tin tức của quân đoàn, bài đăng cuối cùng là vào một ngày trước khi Lục Tư Niên giải ngũ, sau đó liền không cập nhật thêm bất kỳ bài nào nữa.",
    # 032
    "Kỷ Cảnh vừa lướt vừa thở dài, cậu không hiểu nổi rõ ràng mình chỉ nhỏ hơn Lục Tư Niên có năm tuổi, sao cảm giác như cả hai chẳng sống cùng một thế kỷ vậy.",
    # 033
    "Sau khi lướt xong vòng bạn bè của Lục Tư Niên, Kỷ Cảnh lập tức bắt tay vào kế hoạch bước thứ hai: Tìm hiểu sở thích của Lục Tư Niên, bắt đầu từ những chủ đề chung để rút ngắn khoảng cách giữa hai người.",
    # 034
    "Kỷ Cảnh thoát khỏi vòng bạn bè của Lục Tư Niên, bấm mở khung trò chuyện với anh, bắt đầu gõ chữ:",
    # 035
    "【Dịch Nam Nam Nam】: Đại thúc ơi, chú đang làm gì đấy ạ.",
    # 036
    "【Dịch Nam Nam Nam】: [Hình mèo con vắt chân.jpg]",
    # 037
    "…",
    # 038
    "Mười mấy phút trôi qua, bặt vô âm tín.",
    # 039
    "Kỷ Cảnh nhìn đồng hồ, bây giờ đã là mười giờ đêm, cậu không tin giờ này mà Lục Tư Niên còn bận rộn chuyện gì.",
    # 040
    "Không tin tà, cậu lại nhắn liền mấy tin:",
    # 041
    "【Dịch Nam Nam Nam】: Ảnh đại diện là ảnh của chú thật ạ?",
    # 042
    "【Dịch Nam Nam Nam】: Đẹp trai quá đi! [Mắt lấp lánh]",
    # 043
    "Cậu không tin trên đời lại có người đàn ông nào từ chối được lời khen đẹp trai từ phụ nữ.",
    # 044
    "Thế nhưng, sự thật đã chứng minh Lục Tư Niên đúng là một người đàn ông không bình thường.",
    # 045
    "Nửa tiếng sau, Kỷ Cảnh nhìn chằm chằm vào cả màn hình toàn là tin nhắn độc thoại của mình, bật ra một tiếng cười lạnh.",
    # 046
    "Ngay sau đó, cậu dường như ngộ ra điều gì, lại gửi thêm một tin nhắn nữa sang.",
    # 047
    "Lần này không phải tán tỉnh bâng quơ nữa, mà là một câu hỏi học thuật vô cùng nghiêm cẩn.",
    # 048
    "Nếu như không có Lục Tư Niên, thì Kỷ Cảnh vốn là Alpha thiên tài số một của thế hệ này.",
    # 049
    "Thiên phú ngút trời cộng thêm nguồn tài nguyên bồi dưỡng đỉnh cấp của nhà họ Kỷ, nếu không phải giữa chừng bị linh hồn kia chiếm đoạt làm lỡ dở mất mấy năm, thì năng lực của Kỷ Cảnh thậm chí hoàn toàn có thể sánh ngang với Lục Tư Niên ở thời kỳ hoàng kim.",
    # 050
    "Thế nên căn bản không có chuyện cậu không hiểu, ngược lại cậu cố tình chọn ra một câu hỏi cực kỳ hóc búa để đi hỏi Lục Tư Niên.",
    # 051
    "Quả nhiên không ngoài dự đoán, chỉ chừng khoảng năm phút sau, Lục Tư Niên liền gửi tin nhắn lại.",
    # 052
    "【Lục Tư Niên】: [Hình ảnh].",
    # 053
    "【Lục Tư Niên】: Em xem qua đi.",
    # 054
    "Kỷ Cảnh tiện tay bấm mở bức ảnh ra, đó là một sơ đồ tư duy được viết tay toàn bộ.",
    # 055
    "Kỷ Cảnh: “…”",
    # 056
    "【Dịch Nam Nam Nam】: Sao lúc nãy chú không trả lời em thế ạ?",
    # 057
    "Mãi một lúc sau, Lục Tư Niên mới hồi đáp:",
    # 058
    "【Lục Tư Niên】: Tại sao phải trả lời.",
    # 059
    "Kỷ Cảnh cạn lời toàn tập, giờ thì cậu đã vô cùng thấu hiểu vì sao có nhiều Omega thích Lục Tư Niên đến thế mà anh vẫn ế chỏng chơ chưa từng yêu đương một lần nào.",
    # 060
    "Cậu nheo mắt nhìn màn hình quang học, khóe miệng khẽ nhếch lên một nụ cười đầy tà ý.",
    # 061
    "【Dịch Nam Nam Nam】: Dạ được rồi, là em làm phiền chú rồi ạ.",
    # 062
    "【Dịch Nam Nam Nam】: Em chỉ là rất muốn tìm chú để nói chuyện thôi mà.",
    # 063
    "Kỷ Cảnh vẫn chưa thỏa mãn, kiên nhẫn chờ đợi Lục Tư Niên hồi đáp, lần này đối phương cũng phải mất một lúc lâu mới nhắn lại.",
    # 064
    "【Lục Tư Niên】: Ừm.",
    # 065
    "Kỷ Cảnh nhìn mà bật cười, đồng thời trong lòng bùng lên ngọn lửa hiếu thắng không tên.",
    # 066
    "Cậu không tin mình lại không thể khiến cái tên Lục Tư Niên này nói thêm vài câu.",
    # 067
    "Cậu đặt thiết bị đầu cuối xuống, nhìn lên trần nhà suy nghĩ, đôi chân dài đang vắt chéo đu đưa qua lại.",
    # 068
    "Đột nhiên, khóe mắt cậu lướt qua những vết bầm tím chói mắt trên đôi chân mình.",
    # 069
    "Một ý nghĩ tà ác bỗng nảy mầm trong lòng cậu.",
    # 070
    "Cậu chỉnh lại ga giường một chút, sau đó cởi bỏ chiếc quần đùi rộng thùng thình của mình ra, kéo chiếc chăn lại che đi một nửa, rồi giơ thiết bị đầu cuối lên, tách một tiếng chụp lấy một bức ảnh.",
    # 071
    "【Dịch Nam Nam Nam】: Đau quá đi à.",
    # 072
    "【Dịch Nam Nam Nam】: [Hình ảnh].",
    # 073
    "Đây là một bức ảnh mang tính xung kích thị giác vô cùng mãnh liệt.",
    # 074
    "Giữa lớp chăn đệm màu xám đậm, đôi chân dài trắng nõn thon thả thoắt ẩn thoắt hiện, những vệt máu đỏ sẫm cùng những mảng bầm tím loang lổ đan xen chằng chịt vào nhau.",
    # 075
    "Tựa như một chùm hoa mai đỏ nở rộ giữa màn tuyết trắng đêm khuya.",
    # 076
    "Mang lại cho người ta vô vàn liên tưởng mê man.",
    # 077
    "Gần như ngay giây tiếp theo sau khi bấm mở bức ảnh, Lục Tư Niên đã chật vật tắt phụt thiết bị đầu cuối đi.",
    # 078
    "Máu huyết toàn thân anh dồn dập dâng trào lên não, lồng ngực anh phập phồng dữ dội, đôi chân kia cứ lởn vởn mãi trong tâm trí không cách nào xua đi được, cảm giác khô nóng bứt rứt khiến anh bất giác tháo tung chiếc cúc áo ngủ cài kín mít trên cùng ra.",
    # 079
    "Mấy phút trôi qua, cảm giác khô nóng kia chẳng những không giảm mà còn bùng lên dữ dội hơn, Lục Tư Niên cảm nhận được nơi sau gáy lại bắt đầu ngứa ngáy âm ỉ.",
    # 080
    "Anh trở mình rời giường, từ trong ngăn kéo lấy ra chiếc túi kín màu đen, rút ống thuốc tiêm bên trong ra, chẳng thèm nhìn lấy một cái mà trực tiếp đâm thẳng vào tuyến thể sau gáy.",
    # 081
    "Lục Tư Niên tựa lưng vào tường, yết hầu chuyển động theo từng nhịp thở dần bình ổn trở lại, dưới cổ áo mở rộng, những giọt mồ hôi men theo xương quai xanh chảy tràn vào lồng ngực săn chắc…",
    # 082
    "Sau khi từ phòng tắm bước ra, anh mở thiết bị đầu cuối lên, màn hình vẫn đang dừng lại ở giao diện bức ảnh mà Dịch Nam gửi tới.",
    # 083
    "【Lục Tư Niên】: Sau này đừng gửi loại ảnh này nữa.",
    # 084
    "Kỷ Cảnh gần như trả lời lại ngay tức khắc.",
    # 085
    "【Dịch Nam Nam Nam】: Tại sao chứ? Em chỉ muốn nói cho chú biết là em đau lắm thôi mà.",
    # 086
    "Lục Tư Niên nhìn câu nói đầy mập mờ dễ gây hiểu lầm mà đối phương gửi sang, nhất thời chẳng biết nên trả lời ra sao.",
    # 087
    "【Lục Tư Niên】: Làm sao mà bị thương như thế.",
    # 088
    "Kỷ Cảnh suy nghĩ một lúc,",
    # 089
    "【Dịch Nam Nam Nam】: Em bất cẩn bị ngã thôi ạ.",
    # 090
    "Thế nhưng Lục Tư Niên ở đầu bên kia khi nhìn thấy câu này thì lại cau chặt mày.",
    # 091
    "Lục Tư Niên hiểu rất rõ, loại vết thương kiểu này tuyệt đối không thể là do ngã mà thành, ngược lại giống như… bị người ta đánh đập dã man.",
    # 092
    "Chưa đợi Lục Tư Niên kịp suy nghĩ thêm, Kỷ Cảnh đã nhanh chóng chủ động kết thúc chủ đề.",
    # 093
    "【Dịch Nam Nam Nam】: Buồn ngủ quá rồi, em đi ngủ đây ạ, chúc chú ngủ ngon.",
    # 094
    "Lục Tư Niên nhìn chằm chằm vào hai chữ ngủ ngon, im lặng một lúc lâu, rồi tắt thiết bị đầu cuối đi.",
    # 095
    "Chỉ có điều trước khi chìm vào giấc ngủ, mỗi lần nhắm mắt mở mắt ra, trong đầu anh đều hiện lên đôi chân chằng chịt những vết thương kia.",
    # 096
    "…",
    # 097
    "Suốt hai ngày sau đó Kỷ Cảnh đều đến lớp của Lục Tư Niên đúng hẹn, nhưng cậu nhạy bén phát hiện Lục Tư Niên dường như đang cố tình phớt lờ mình, rõ ràng trong giờ giảng bài anh có thói quen đảo mắt nhìn quanh toàn bộ học sinh, thế nhưng trước sau lại chẳng thèm liếc nhìn về phía góc của cậu lấy một lần.",
    # 098
    "Sau khi tan lớp, cậu lại bám theo như trước kia, chỉ có điều không còn đòi phương thức liên lạc nữa, mà đề nghị mời Lục Tư Niên đi ăn cơm coi như lời cảm ơn anh đã cứu mình.",
    # 099
    "Sau đó cậu liền nhận ra thái độ của Lục Tư Niên còn lạnh lùng cứng nhắc hơn trước, không những từ chối cậu thẳng thừng mà đến liếc nhìn cậu một cái cũng không thèm, ánh mắt lảng tránh, cả người toát lên vẻ bài xích cự tuyệt.",
    # 100
    "Kỷ Cảnh thầm đoán có phải đêm hôm đó mình chơi đùa quá trớn rồi không, dù sao bức ảnh kia đối với một gã cổ hủ phong kiến như Lục Tư Niên mà nói thì đúng là quá mức kích thích.",
    # 101
    "Kiên trì được hai ngày, Kỷ Cảnh lại một lần nữa biến mất khỏi tiết học ngày thứ Sáu của Lục Tư Niên.",
    # 102
    "Lục Tư Niên liếc nhìn góc phòng học, khẽ thở phào nhẹ nhõm một hơi, sau đó thu dọn giáo án, bước ra khỏi phòng học đi về phía nhà ăn giáo viên.",
    # 103
    "Chiếu theo lịch học của trường quân sự Đế quốc, lúc này vẫn còn một bộ phận học sinh đang học tiết cuối cùng.",
    # 104
    "Khi đi ngang qua sân tập, Lục Tư Niên theo thói quen liếc nhìn vào trong sân một cái.",
    # 105
    "Anh nhớ Vương Bằng đang phụ trách dạy tiết thực chiến cho lớp trinh sát ở sân tập.",
    # 106
    "Vương Bằng trước đây từng làm bạn cùng phòng suốt ba năm với Lục Tư Niên, chỉ có điều Lục Tư Niên là bị bí mật cách chức chuyển về trường làm giáo sư, còn Vương Bằng là nhận lệnh xuống trường huấn luyện một năm, sau đó sẽ được triệu hồi trở lại Đệ tam quân đoàn.",
    # 107
    "“Kỷ Cảnh, đừng có đứng đó mà nhe răng cười cợt nhả!” Vương Bằng gầm lên một tiếng, thổi một hồi còi chói tai.",
    # 108
    "Ánh mắt Lục Tư Niên thuận theo tiếng quát nhìn về phía cách đó không xa, chỉ thấy Kỷ Cảnh đang đứng dưới khán đài, cười toe toét vô cùng ngứa mắt với Vương Bằng.",
    # 109
    "Lục Tư Niên nhạy bén phát hiện Kỷ Cảnh đã đổi một kiểu tóc mới.",
    # 110
    "Lần trước Kỷ Cảnh vẫn còn để lộ trán, lần này lại để tóc mái che khuất hàng lông mày, ngũ quan vốn mang tính công kích rất mạnh nhờ có phần tóc mái này mà trở nên ngoan ngoãn dịu đi đôi phần.",
    # 111
    "Ánh mắt Lục Tư Niên dừng lại trên gương mặt Kỷ Cảnh, ngay khoảnh khắc tiếp theo, trong đầu anh liền hiện lên khuôn mặt của Dịch Nam.",
    # 112
    "Con gái riêng.",
    # 113
    "Lục Tư Niên thầm lẩm bẩm trong lòng, nhìn Kỷ Cảnh một cái thật sâu, rồi cất bước biến mất ở cuối con đường."
]

print(f"Total paragraphs for ch_093: {len(trans_paras)}")

out_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_093"
header = "---\ntitle: Chương 93: Cảnh cáo và nghi ngờ\n---\n\n"
content = header + "\n\n".join(trans_paras) + "\n"

trans_path = os.path.join(out_dir, "translation.md")
with open(trans_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Saved {trans_path} successfully!")
