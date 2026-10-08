# -*- coding: utf-8 -*-
import os

target_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_011"
target_file = os.path.join(target_dir, "translation.md")

paragraphs = [
    # 0: header
    """---
title: Chương 11: Hãy mở nó ra
---""",

    # 1: separator
    "====================",

    # 2: 空氣中彌漫著令人窒息的低氣壓...
    "Trong không khí tràn ngập luồng áp suất thấp đến mức khiến người ta nghẹt thở. Cây búa sắt nhỏ run rẩy lóe lên một tia kim quang, cuối cùng vì suy nghĩ cho an toàn của bản thân mà lựa chọn ẩn thân không hiện hình, âm thanh điện tử lượn lờ xung quanh nhỏ như tiếng muỗi kêu:",

    # 3: 【嗚嗚，宿主，系統檢測到易緣已經離開了哦...】
    "【Hu hu, ký chủ, hệ thống kiểm tra thấy Dịch Duyên đã rời đi rồi nha, thế nhưng ký chủ không cần lo lắng, cậu ấy tuyệt đối an toàn……】",

    # 4: “我知道，”他當然知道易緣已經走了...
    "“Tôi biết.” Anh đương nhiên biết Dịch Duyên đã rời đi, giống hệt kiếp trước, lặng lẽ không một tiếng động, không hề có bất kỳ dấu hiệu báo trước nào.",

    # 5: 緊接著，易緣會在不久之後再次出現...
    "Ngay sau đó, Dịch Duyên sẽ lại xuất hiện trong một khoảng thời gian ngắn nữa, biến thân trở thành con nuôi của tâm phúc dưới trướng Tưởng Trác Hàng. Vào ngày Tết Tuyết Rơi năm Liên bang 137, cậu sẽ áp chế anh sang một bên, lạnh lùng nhìn cha mẹ anh chết dưới tay Tưởng Trác Hàng.",

    # 6: 他永遠記得易緣迎著飛雪走到他面前的畫面...
    "Anh vĩnh viễn nhớ rõ hình ảnh Dịch Duyên đón những bông tuyết bay bước đến trước mặt anh. Ánh lửa chập chờn nhảy múa trong đôi mắt ngấn nước long lanh của cậu, cậu mỉm cười, nhưng lại giống hệt như một con ác khuyển bước ra từ địa ngục.",

    # 7: 他用指尖輕柔地抹去他臉上的血跡...
    "Cậu dùng đầu ngón tay dịu dàng lau đi vệt máu trên mặt anh, nói: “Dương ca, xin lỗi.”",

    # 8: 沒有人知道當時的他有多絕望...
    "Không một ai biết được khi đó anh tuyệt vọng đến nhường nào. Ngoại trừ cảm giác bất lực ập tới như sóng cuộn, còn có phần tình cảm chưa từng nhận ra đã lặng lẽ vỡ vụn trong tim.",

    # 9: 從那之後，易緣似乎回到了最開始的乖軟少年...
    "Kể từ sau đó, Dịch Duyên dường như đã quay trở lại thành thiếu niên ngoan ngoãn mềm mại lúc ban đầu, lúc nào cũng bám lấy anh, làm nũng với anh. Nhưng anh chưa từng nói với cậu thêm một câu nào nữa, thậm chí số lần nhìn thẳng vào cậu cũng chỉ đếm trên đầu ngón tay. Mỗi lần như vậy Dịch Duyên đều tủi thân đến đỏ hoe khóe mắt, làm như thể anh mới chính là kẻ vong ân bội nghĩa vậy.",

    # 10: 記憶中後來易緣就又消失了...
    "Trong ký ức về sau Dịch Duyên lại biến mất, biến mất một cách triệt để không còn tăm hơi. Cuối cùng Lâu Hỉ Dương nhận được một đoạn video giám sát mới biết được hóa ra cậu đã chết.",

    # 11: 他萬萬沒想到，一個背叛他的人，這輩子卻成了他的債主。
    "Anh vạn vạn không ngờ tới, một kẻ từng phản bội anh, kiếp này lại biến thành chủ nợ của anh.",

    # 12: 最開始，他花了幾年的時間慢慢去接受...
    "Ban đầu, anh đã phải mất vài năm trời để dần dần chấp nhận, trong những ngày tháng sinh hoạt cùng bé Dịch Duyên mà dần hóa giải cừu hận, đồng thời lựa chọn tin tưởng lời của hệ thống, tin rằng hành vi khi đó của Dịch Duyên là có nguyên do.",

    # 13: 易緣雖然性格有些缺陷...
    "Dịch Duyên tuy tính cách có đôi chút khiếm khuyết, nhưng chưa từng thực sự làm ra chuyện ác nào tội không thể tha.",

    # 14: 所以他教他養他...
    "Cho nên anh dạy dỗ cậu, nuôi nấng cậu, mong muốn Dịch Duyên có thể trở thành một người lương thiện trong sáng. Sau khi biết được Dịch Duyên thích mình, anh càng thêm khẳng định lúc trước Dịch Duyên có nỗi khổ tâm mới phản bội anh, khẳng định kiếp này Dịch Duyên sẽ không nỡ rời xa anh.",

    # 15: 但現在易緣還是走了...
    "Thế nhưng hiện tại Dịch Duyên vẫn rời đi, kết cục giống y hệt kiếp trước. Nói cách khác, tất cả những gì anh làm đều là công cốc nực cười.",

    # 16: 想到這裡，婁禧陽冷笑了一聲。
    "Nghĩ đến đây, Lâu Hỉ Dương cười lạnh một tiếng.",

    # 17: “我問的是，他去了哪裡。”
    "“Tôi hỏi là, cậu ấy đã đi đâu.” Xương hàm Lâu Hỉ Dương theo từng chữ thốt ra dần siết chặt lại, giọng nói trầm và chậm, để lộ cơn giận dữ mà chính bản thân anh cũng chưa từng phát giác.",

    # 18: 他的眉眼以肉眼可見的弧度變得冷戾...
    "Đôi mày của anh biến đổi theo độ cong có thể nhìn thấy bằng mắt thường trở nên lạnh lẽo tàn nhẫn, cảm giác áp bách nghiêng trời lệch đất ập tới, ép búa sắt nhỏ thở mạnh một hơi cũng không dám.",

    # 19: 來自於救世主的威壓...
    "Uy áp đến từ Đấng Cứu Thế, nó đã chân chân chính chính thể hội được rồi, cái này quả thực còn đáng sợ hơn cả búa sắt lớn lúc nổi giận nữa hu hu hu.",

    # 20: 可它就是個無辜可憐的打工錘，一切都與他無瓜！
    "Nhưng nó chỉ là một cây búa làm công vô tội đáng thương thôi mà, tất cả mọi chuyện chẳng liên quan gì tới nó hết á!",

    # 21: 【嗶嗶，檢測到宿主情緒波動過大...】
    "【Bíp bíp, phát hiện dao động cảm xúc của ký chủ quá lớn, tiến độ trả nợ bước vào giai đoạn trở ngại, kích hoạt chế độ dọn dẹp trở ngại】",

    # 22: 【叮咚，解決方案已合成。】
    "【Đinh đong, phương án giải quyết đã tổng hợp xong.】",

    # 23: 【滴滴，方案已啟動。】
    "【Tít tít, phương án đã được khởi động.】",

    # 24: ……
    "……",

    # 25: 一連串的系統提示音在空中響起...
    "Một tràng âm thanh thông báo của hệ thống vang lên giữa không trung, Lâu Hỉ Dương khẽ nhíu mày, ngước mắt nhìn hệ thống đang hiển hiện hình dáng giữa không trung.",

    # 26: 【宿主，請您進入易天臥室...】
    "【Ký chủ, xin ngài hãy bước vào phòng ngủ của Dịch Thiên, ở bên trái bàn chức năng có một khung ảnh bằng gỗ, xin hãy mở nó ra.】",

    # 27: 易天臥室？
    "Phòng ngủ của Dịch Thiên?",

    # 28: 婁禧陽側頭掃了眼左手邊緊閉的房門...
    "Lâu Hỉ Dương nghiêng đầu liếc nhìn cánh cửa đóng chặt bên tay trái, trầm giọng nói: “Tôi không có sở thích dòm ngó chuyện riêng tư của người khác.”",

    # 29: 【請您配合，這是您知道易緣去向的唯一線索。】
    "【Xin ngài hãy phối hợp, đây là manh mối duy nhất để ngài biết được tung tích của Dịch Duyên.】",

    # 30: 聞言，婁禧陽的表情松了一點...
    "Nghe vậy, vẻ mặt Lâu Hỉ Dương thoáng giãn ra một chút. Anh một lần nữa hướng tầm mắt về phía cánh cửa kia, sau khi suy ngẫm một hồi, cuối cùng nhấc chân bước vào trong.",

    # 31: “吱呀—”，滿天的灰塵在開門的一瞬間迫不及待的衝向門外。
    "“Két——”, bụi bay mù trời trong khoảnh khắc cánh cửa mở ra đã không kịp chờ đợi mà ùa ra ngoài cửa.",

    # 32: 房間裡的裝設很簡單...
    "Bày biện trong phòng rất đơn giản, một tấm chiếu tatami thô sơ nhất, mang theo chức năng an thần có cũng như không.",

    # 33: 婁禧陽掃了一眼...
    "Lâu Hỉ Dương quét mắt nhìn một vòng, đi thẳng tới chiếc bàn chức năng trước giường, liếc mắt liền nhìn thấy khung ảnh trong miệng hệ thống.",

    # 34: 相框沒什麽特別...
    "Khung ảnh chẳng có gì đặc biệt, chỉ là một bức ảnh chân dung của một người phụ nữ mang đậm dấu ấn thời đại. Nhìn kỹ, đôi mắt của người phụ nữ gần như giống hệt Dịch Duyên.",

    # 35: 他把相框打開，一張卡片晃晃悠悠的飄落在地上。
    "Anh mở khung ảnh ra, một tấm thẻ lảo đảo rơi lơ lửng xuống mặt đất.",

    # 36: 婁禧陽神情微頓...
    "Thần sắc Lâu Hỉ Dương khựng lại, anh nhặt tấm thẻ lên, phát hiện bên trên viết: “Tiểu Duyên, mở ngăn kéo dưới gầm giường ra, dùng ADN của con.”",

    # 37: 婁禧陽轉身去到易緣的房間...
    "Lâu Hỉ Dương quay người đi sang phòng của Dịch Duyên, tìm thấy sợi tóc rụng của cậu trên giường rồi quay trở lại chỗ cũ, nhắm chuẩn vào khu vực quét, rất nhanh đã mở được ngăn kéo ra.",

    # 38: 裡面是一個老舊的牛皮筆記本...
    "Bên trong là một cuốn sổ tay bìa da bò cũ kỹ, ngày tháng ở trang đầu tiên là năm Liên bang 125, tức là mười lăm năm trước.",

    # 39: 婁禧陽知道易天是個懷舊的人...
    "Lâu Hỉ Dương biết Dịch Thiên là một người hoài cổ, dùng phương thức thế này hoàn toàn nằm trong dự liệu của anh.",

    # 40: 上面像是他的情史——
    "Bên trên giống như lịch sử tình trường của ông ta——",

    # 41: “今天，老子遇到了一個女人...”
    "“Hôm nay, ông đây gặp được một người phụ nữ, cô ấy rất đẹp, là vưu vật quyến rũ mê người nhất mà ông đây từng thấy...”",

    # 42: “她叫老子滾遠點…”
    "“Cô ấy bảo ông đây cút xéo đi...”",

    # 43: “呵，原來她是個女.表.子...”
    "“Hừ, hóa ra cô ta là một con điếm, chỉ thích mấy lão già có tiền có quyền, ông đây không xứng.”",

    # 44: “她懷孕了，老子的。”
    "“Cô ấy mang thai rồi, là của ông đây.”",

    # 45: “孩子叫易緣，她走了。”
    "“Đứa bé tên Dịch Duyên, cô ấy bỏ đi rồi.”",

    # 46: …
    "…",

    # 47: “她死了。”
    "“Cô ấy chết rồi.”",

    # 48: 婁禧陽快速地瀏覽著...
    "Lâu Hỉ Dương lướt nhanh qua các trang, phát hiện Dịch Thiên sau khi viết tới đoạn này thì dừng bút, những trang phía sau đều để trống.",

    # 49: 但在本子的最後，又出現了兩頁的字...
    "Thế nhưng ở phần cuối cùng của cuốn sổ lại xuất hiện hai trang chữ, lần này không có ghi ngày tháng, đồng thời đối tượng người đọc đã đổi thành Dịch Duyên.",

    # 50: “小子，你看到它的時候老子估計已經死了...”
    "“Thằng nhóc, lúc con nhìn thấy cuốn sổ này thì ông đây đoán chừng đã chết rồi. Ông đây muốn nói cho con biết, mạt thế của hành tinh M sẽ giáng lâm sau sáu năm nữa, con có phải rất sợ hãi không? Muốn lập tức trốn tới hành tinh khác chứ gì? Hừ, đừng có mơ tưởng.",

    # 51: 你還記得你媽長什麽樣嗎...
    "Con còn nhớ mẹ con trông thế nào không, chính là bức ảnh lúc nãy đấy, là một đại mỹ nhân đúng không, cô ấy cái gì cũng tốt, chỉ có điều quá đỗi tuyệt tình.",

    # 52: 那時候老子少年氣盛...
    "Hồi đó ông đây tuổi trẻ khí thịnh, cứ muốn tới câu lạc bộ lớn nhất toàn Liên bang để tìm em gái……",

    # 53: ……
    "……",

    # 54: ……
    "……",

    # 55: 就不跟你講老子和她怎麽在一起的...
    "Không thèm kể cho con nghe chuyện ông đây với cô ấy đến với nhau thế nào nữa, tóm lại, sau khi cô ấy bất ngờ mang thai con, cô ấy buộc phải thẳng thắn thú nhận với ta rất nhiều điều——",

    # 56: 她是FC星際情報團的一員...
    "Cô ấy là một thành viên của Đoàn Tình báo Tinh tế FC, mỗi một vị khách hàng trong câu lạc bộ đều là nguồn tin tức của cô ấy.",

    # 57: 關於M星的末日...
    "Về ngày tận thế của hành tinh M, thực ra từ rất lâu trước đây đã có điềm báo rồi, đây là một ván cờ sinh tử khổng lồ và vô cùng khủng khiếp.",

    # 58: 你別怪她在你兩歲的時候離開...
    "Con đừng trách cô ấy rời đi lúc con hai tuổi, cô ấy không phải không cần con đâu, là ông đây lừa con đấy, là do ông đây quá ngu ngốc không nghĩ thông suốt.",

    # 59: 蔣卓航已經發覺了你媽的存在，所以她死了。
    "Tưởng Trác Hàng đã phát giác ra sự tồn tại của mẹ con, cho nên cô ấy đã chết.",

    # 60: 老子知道的太多，所以老子也快死了。
    "Ông đây biết quá nhiều, cho nên ông đây cũng sắp chết rồi.",

    # 61: 本來想讓你好好活下去...
    "Vốn dĩ muốn để con sống thật tốt, không muốn để con biết quá nhiều, đưa con tới hành tinh khác sống những ngày tháng vô ưu vô lo.",

    # 62: 但老子還是想了想...
    "Thế nhưng ông đây ngẫm lại, nếu như đi đến bước đường cuối cùng, hành tinh M nhất định phải đối mặt với bước đường cùng tuyệt cảnh, thì ông đây cùng mẹ con hy vọng con đi tìm người này, ông ta tên Trần Liễm. Mã thiết bị đầu cuối bên dưới chỉ dùng một lần, sau khi liên lạc được nhớ bảo ông ta cho con phương thức liên lạc khác.”",

    # 63: 所有的話語在此畫上了句點...
    "Tất cả lời lẽ dừng lại ở đây. Ánh mắt Lâu Hỉ Dương vẫn nán lại hồi lâu trên câu nói cuối cùng kia. Gương mặt trông có vẻ bình lặng, nhưng sâu trong đáy mắt lại cuộn trào sóng ngầm.",

    # 64: 兩件事，一是易緣的父母或許知道所謂M星末日的真相...
    "Hai chuyện: một là cha mẹ Dịch Duyên có lẽ biết được chân tướng về cái gọi là mạt thế hành tinh M, đây là điều anh chưa từng lường trước được, anh trước giờ vẫn nghĩ chỉ có anh và cha mẹ anh mới biết được nội tình bên trong.",

    # 65: 二是他認得這個陳斂...
    "Hai là anh nhận ra Trần Liễm này, ông ta chính là cha nuôi của Dịch Duyên ở kiếp trước, là tay sai đắc lực của Tưởng Trác Hàng. Cho nên, Dịch Duyên rất có thể là sau khi nhìn thấy thứ này đã liên lạc với Trần Liễm, rồi bị Trần Liễm dẫn đi.",

    # 66: 【嗶嗶，檢測到阻礙已消除，清掃模式已關閉。】
    "【Bíp bíp, phát hiện trở ngại đã được giải trừ, chế độ dọn dẹp đã tắt.】",

    # 67: “告訴我他現在在哪裡。”
    "“Nói cho tôi biết hiện tại cậu ấy đang ở đâu.” Lâu Hỉ Dương nhìn cây búa sắt nhỏ đã khôi phục lại vẻ hoạt bát, cất tiếng hỏi.",

    # 68: 【不能哦宿主～】
    "【Không được đâu nha ký chủ ~】",

    # 69: 回答在他預想之內...
    "Câu trả lời nằm trong dự liệu của anh. Lâu Hỉ Dương cúi đầu liếc nhìn cuốn sổ tay, đặt nó trở lại chỗ cũ.",

    # 70: “那就等他自己出來吧，反正也沒多久了。”
    "“Vậy thì đợi cậu ấy tự mình xuất hiện đi, dù sao cũng chẳng còn bao lâu nữa.”",

    # 71: 求收藏呀求收藏～
    "Cầu cất chứa nha cầu cất chứa ~"
]

os.makedirs(target_dir, exist_ok=True)
with open(target_file, "w", encoding="utf-8") as f:
    f.write("\n\n".join(paragraphs) + "\n")

print(f"ch_011 translation written: {len(paragraphs)} paragraphs.")
