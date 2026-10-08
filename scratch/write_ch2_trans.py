import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

paras_ch2 = [
    # [0] ====================
    "====================",
    
    # [1] 婁禧陽摟著易緣，看他樣子還真像是怕極了，細白的後頸以肉眼可見的弧度發著抖，這樣的反應或多或少讓婁禧陽感到自責，“抱歉，是我回來晚了。”
    "Lâu Hỉ Dương ôm lấy Dịch Duyên, nhìn bộ dạng của cậu quả thực hệt như sợ hãi đến tột cùng, chiếc gáy trắng ngần run rẩy theo biên độ có thể thấy rõ bằng mắt thường. Phản ứng như vậy ít nhiều khiến Lâu Hỉ Dương cảm thấy tự trách: “Xin lỗi, là anh về muộn.”",
    
    # [2] “嗯，就是你錯了。”易緣的聲音悶悶的。
    "“Vâng, chính là anh sai rồi.” Giọng nói của Dịch Duyên rầu rĩ nghẹn ngào.",
    
    # [3] 婁禧陽：……
    "Lâu Hỉ Dương: ……",
    
    # [4] 安靜了一會兒，突然意識到兩人的姿勢不太對，婁禧陽不動聲色地拉開了一點距離，安撫性地在易緣的背上拍了兩下。
    "Yên lặng một lúc, bỗng nhiên nhận ra tư thế của hai người có chút không đúng, Lâu Hỉ Dương bất động thanh sắc kéo dãn một chút khoảng cách, vỗ nhẹ hai cái lên lưng Dịch Duyên như để an ủi.",
    
    # [5] 因為沒人管，易緣從小就很依賴他，幾乎每天都準時準點地打開家門站在樓道口等他回家，婁禧陽起初並沒有放在心上，隻覺著這小孩怪貼心的。
    "Bởi vì không có ai chăm sóc, Dịch Duyên từ nhỏ đã vô cùng ỷ lại vào anh, hầu như ngày nào cũng mở cửa đúng giờ đúng khắc đứng ở đầu cầu thang đợi anh về nhà. Lâu Hỉ Dương ban đầu cũng không để trong lòng, chỉ cảm thấy đứa nhỏ này ngoan ngoãn săn sóc lạ thường.",
    
    # [6] 直到有一次他在為易天辦事時被人纏上，一不留神耽誤到深夜，一上樓就看見家門前縮著一團小小的人影。
    "Mãi cho đến một lần anh bị người ta quấn lấy khi làm việc cho Dịch Thiên, sơ sẩy một chút đã dây dưa tới tận đêm khuya, vừa bước lên lầu liền nhìn thấy trước cửa nhà đang co ro một bóng người bé nhỏ.",
    
    # [7] 燈一亮，他就徑直對上了易緣那雙泛著血絲的眼睛，他說，哥哥你是不是也不要我了。
    "Đèn vừa bật sáng, anh liền chạm thẳng vào đôi mắt vằn tia máu của Dịch Duyên, cậu nói, anh ơi có phải anh cũng không cần em nữa rồi không.",
    
    # [8] 至此他就再也無法忘記那雙眼睛，因為無論是上輩子還是這輩子，易緣都是唯一一個會等他回家的人，如果易緣沒有做那些事，最後也沒有以那樣的方式離開的話，他想他上輩子最後的那段日子自己的心裡或許也不會空空蕩蕩。
    "Kể từ đó anh không bao giờ có thể quên được đôi mắt ấy, bởi vì bất kể là kiếp trước hay kiếp này, Dịch Duyên luôn là người duy nhất chờ anh về nhà. Nếu như Dịch Duyên không làm những chuyện kia, cuối cùng cũng không rời đi theo cách thức ấy, anh nghĩ những tháng ngày cuối cùng ở kiếp trước lòng mình có lẽ đã không trống rỗng đến nhường này.",
    
    # [9] 今天應該是易緣見他遲遲沒有回家，開了門就在外面等他，沒想到被那幾個惡心人的東西給盯上了，要是他再晚回來一會兒......
    "Hôm nay chắc hẳn là do Dịch Duyên thấy anh mãi không về, mở cửa đứng đợi anh ở bên ngoài, không ngờ lại bị mấy thứ kinh tởm kia nhắm trúng. Nếu như anh về muộn thêm một chút nữa......",
    
    # [10] 想到這裡，婁禧陽的眉頭一蹙。
    "Nghĩ tới đây, chân mày Lâu Hỉ Dương khẽ nhíu lại.",
    
    # [11] 突然，他感覺到一股濕熱感從他的脖頸處傳來。
    "Đột nhiên, anh cảm nhận được một luồng hơi nóng ẩm ướt phả tới từ nơi hõm cổ.",
    
    # [12] “陽哥，以後搬過來和小緣一起住好不好？”易緣把頭埋在他的胸前，唇瓣似是不經意地觸碰他的喉結，“我不敢一個人住。”
    "“Dương ca, sau này chuyển qua ở cùng Tiểu Duyên có được không?” Dịch Duyên vùi đầu trước ngực anh, cánh môi như vô tình khẽ chạm vào yết hầu của anh, “Em không dám ở một mình đâu.”",
    
    # [13] 婁禧陽渾身一僵，扯著易緣的後頸就把他從身上拉了下來。
    "Lâu Hỉ Dương toàn thân cứng đờ, túm lấy gáy Dịch Duyên kéo cậu ra khỏi người mình.",
    
    # [14] 又來了，這種詭異的感覺。婁禧陽頭皮有些發麻。
    "Lại tới nữa rồi, cảm giác quái dị này. Da đầu Lâu Hỉ Dương khẽ tê rần.",
    
    # [15] 易緣好像還沒反應過來，投向他的目光還帶著委屈，抽噎了兩聲後又強調了一遍，“陽哥，我真的很害怕，萬一晚上有人——”
    "Dịch Duyên dường như vẫn chưa kịp phản ứng, ánh mắt nhìn về phía anh còn vương đầy nét tủi thân, thút thít hai tiếng rồi lại nhấn mạnh thêm lần nữa: “Dương ca, em sợ thật mà, ngộ nhỡ ban đêm có người——”",
    
    # [16] “好。”
    "“Được.”",
    
    # [17] 婁禧陽的目光在易緣的鎖骨上停留了一瞬，不等易緣有所反應，應聲後就轉身打掃起了地面。
    "Ánh mắt Lâu Hỉ Dương dừng lại trên xương quai xanh của Dịch Duyên một thoáng, chẳng đợi Dịch Duyên kịp có phản ứng gì, vừa đồng ý xong liền xoay người dọn dẹp sàn nhà.",
    
    # [18] 【叮咚，目前還債進度：11%】
    "【Đinh đoong, tiến độ trả nợ hiện tại: 11%】",
    
    # [19] 【哇！宿主，恭喜你可以少活一年啦！】
    "【Oa! Ký chủ, chúc mừng ngài có thể sống bớt đi một năm rồi nè!】",
    
    # [20] 婁禧陽的動作微頓。
    "Động tác của Lâu Hỉ Dương khẽ khựng lại.",
    
    # [21] 難道刷進度的關鍵在於順著易緣的想法走？
    "Chẳng lẽ bí quyết tăng tiến độ nằm ở chỗ thuận theo ý muốn của Dịch Duyên?",
    
    # [22] 沒料到婁禧陽這麽快就答應了，易緣有些開心，暈乎乎的，但又不敢讓他看出來，低著頭死死捏住了自己的衣角，指尖都泛起了白。
    "Không ngờ Lâu Hỉ Dương lại đồng ý nhanh đến thế, Dịch Duyên cảm thấy vui mừng lâng lâng, nhưng lại chẳng dám để anh nhận ra, bèn cúi gầm mặt siết chặt góc áo mình, các đầu ngón tay đều trắng bệch ra.",
    
    # [23] 他起身，快速地把自己關進了廁所裡。
    "Cậu đứng dậy, nhanh chóng tự nhốt mình vào trong nhà vệ sinh.",
    
    # [24] 被他擦得乾乾淨淨的鏡面清晰地照出了他那張雌雄莫辨的臉。
    "Mặt gương được cậu lau chùi sạch bong sáng bóng phản chiếu rõ mồn một gương mặt phi giới tính khó phân biệt nam nữ của cậu.",
    
    # [25] 他不喜歡這張臉，他們都說自己像他的交際花媽媽，那些人的目光讓他反胃。
    "Cậu không thích gương mặt này, bọn họ đều bảo cậu giống người mẹ giao tế hoa của mình, ánh mắt của những kẻ đó làm cậu buồn nôn.",
    
    # [26] 但他喜歡看見婁禧陽看他時那純粹的欣賞意味。
    "Nhưng cậu thích nhìn thấy sự thưởng thức thuần túy trong mắt Lâu Hỉ Dương mỗi khi nhìn cậu.",
    
    # [27] 他媽在他六歲就死了，酒鬼父親拉扯他長大，易天除了嘴賤和酗酒外倒也沒什麽，只是經常喝醉後迷蒙的盯著他的臉，也不知道在透著看誰。
    "Mẹ cậu qua đời từ năm cậu lên sáu, người cha nát rượu nuôi cậu lớn khôn. Dịch Thiên ngoại trừ cái miệng độc địa và thói nghiện rượu ra thì cũng chẳng có gì khác, chỉ là sau khi say mèm thường mơ màng nhìn chằm chằm gương mặt cậu, chẳng biết là đang nhìn thấu qua ai.",
    
    # [28] 往往在一頓寂靜後，他會嗤鼻一笑，罵道：“男娃長成這副賤模樣，以後可別出門了，丟老子臉。”
    "Thường sau một hồi im ắng, ông ta sẽ hừ mũi cười khẩy một tiếng, chửi mắng: “Thằng ranh con mà mọc ra cái bộ dạng đê tiện này, sau này đừng có vác mặt ra đường, mất mặt ông đây.”",
    
    # [29] 樓下的巷子流竄著跟他爹一樣的二流子，小時候易緣出門，他爹都會跟在他身後，把眉頭皺的老緊，一副凶神惡煞的模樣，機甲學院裡的小孩都怕他的很，說他是殺人犯的兒子，初中上完他就不去上學了，反正婁禧陽什麽都會教他。
    "Con ngõ dưới lầu lúc nào cũng tụ tập đám du côn lưu manh hệt như cha cậu. Thuở nhỏ mỗi khi Dịch Duyên ra ngoài, cha cậu đều đi theo sau lưng, nhíu chặt mày thành một khối, dáng vẻ hung thần ác sát. Lũ trẻ trong học viện cơ giáp đều sợ cậu một phép, bảo cậu là con trai của kẻ giết người. Học xong cấp hai cậu cũng chẳng thèm đi học nữa, dù sao Lâu Hỉ Dương chuyện gì cũng dạy cho cậu.",
    
    # [30] 只不過在兩年前，一輛豪車發生故障，脫離空中軌道直直衝下地面，老易因此喪命。車主隨手給了一筆數額不小的補償費後就不了了之。
    "Chỉ là vào hai năm trước, một chiếc xe sang trọng gặp sự cố kỹ thuật, chệch khỏi đường ray trên không lao thẳng xuống mặt đất, lão Dịch vì thế mà mất mạng. Chủ xe tùy tiện bồi thường một khoản tiền không nhỏ rồi chuyện cứ thế trôi vào quên lãng.",
    
    # [31] 後來跟在他身後的，就變成了婁禧陽。
    "Về sau, người luôn đi theo bảo bọc sau lưng cậu đổi thành Lâu Hỉ Dương.",
    
    # [32] 婁禧陽是他晦暗的生活裡唯一的溫暖。他和這裡的所有人都不一樣，他身上有光，令他癡迷，如同上癮了一般。
    "Lâu Hỉ Dương là tia ấm áp duy nhất trong chuỗi ngày u tối của cậu. Anh không giống bất kỳ ai ở nơi này, trên người anh có ánh sáng khiến cậu mê mẩn, tựa hồ như đã nghiện tới mức không thể dứt ra.",
    
    # [33] 如果沒有婁禧陽，他會在聯邦宣布末日即將在10個月後來臨的那天，從這棟破舊的居民樓頂一躍而下。
    "Nếu như không có Lâu Hỉ Dương, cậu đã gieo mình từ sân thượng tòa nhà tập thể rách nát này xuống vào cái ngày Liên bang tuyên bố ngày tận thế sẽ giáng lâm sau mười tháng nữa rồi.",
    
    # [34] 他沒什麽好留戀的，也沒什麽欲望要在臨死前滿足。
    "Cậu chẳng có gì đáng để lưu luyến, cũng chẳng có dục vọng nào cần phải thỏa mãn trước lúc chết.",
    
    # [35] 易緣慶幸著，如果不是易天救過婁禧陽，恐怕他也不會多看他一眼。
    "Dịch Duyên thầm thấy may mắn, nếu không nhờ Dịch Thiên từng cứu mạng Lâu Hỉ Dương, e rằng anh cũng chẳng buồn nhìn cậu lấy một cái.",
    
    # [36] 他勾了勾嘴角，用熱水將鎖骨上的血漬搓洗乾淨。
    "Cậu khẽ nhếch khóe môi, dùng nước nóng cọ rửa sạch sẽ vệt máu vương trên xương quai xanh.",
    
    # [37] 這個時候早就已經停止供電了，他家裡的熱水器是婁禧陽自己做的，和現在市場上的大多數熱水器相差無幾，能轉化風能，水能，太陽能，都不需要電來支撐運轉。
    "Vào lúc này hệ thống điện lưới sớm đã ngừng cung cấp, bình nước nóng trong nhà cậu là do chính tay Lâu Hỉ Dương tự chế, không khác mấy so với phần lớn các loại bình nước nóng trên thị trường hiện nay, có thể chuyển hóa phong năng, thủy năng, thái dương năng, hoàn toàn không cần điện năng để duy trì hoạt động.",
    
    # [38] 幸虧如此，他們還能在這個世道洗上熱水澡。
    "Cũng may là nhờ vậy, họ mới có thể tắm nước nóng trong cái thời buổi loạn lạc này.",
    
    # [39] 易緣不明白為什麽婁禧陽什麽都會，他還記得婁禧陽曾經跟他說過：“技多不壓身。”
    "Dịch Duyên không hiểu vì sao Lâu Hỉ Dương chuyện gì cũng tường tận, cậu vẫn nhớ Lâu Hỉ Dương từng bảo với cậu: “Nhiều tài nghệ thì chẳng sợ thiệt thân.”",
    
    # [40] 終端傳來的訊息打斷了他的思緒，他淡化了嘴角的笑意，眼底閃過一絲不悅。
    "Tin nhắn từ thiết bị đầu cuối cắt ngang dòng suy nghĩ của cậu, cậu thu lại nụ cười nơi khóe môi, đáy mắt xẹt qua một tia khó chịu.",
    
    # [41] [啊——完了陳哥，這個世道真的完蛋了！明明是他自己請我們進去喝茶的，上來就把我鼻子打斷了，後頭那男的根本不講道理，我他媽一個字都來不及說啊——]
    "[Á—— Tiêu rồi anh Trần ơi, cái đời này hỏng bét thật rồi! Rõ ràng là tự nó mời bọn em vào uống trà, vừa vào đã đánh gãy mũi em, cái thằng đàn ông phía sau căn bản không hề nói lý lẽ, mẹ kiếp em còn chưa kịp hé răng nửa lời mà——]",
    
    # [42] 畫面還沒來得及顯現出來，就聽見來一陣高亢的嚎哭。
    "Hình ảnh còn chưa kịp hiện lên thì đã nghe thấy một tràng gào khóc thảm thiết réo rắt.",
    
    # [43] 半空中懸浮著卡頓的畫面，那三個壯漢坐在地上鬼哭狼嚎，陳斂的表情黑的嚇人。
    "Khung hình chập chờn lơ lửng giữa không trung, ba gã to con ngồi bệt dưới đất khóc lóc om sòm, sắc mặt của Trần Liễm đen như đít nồi đáng sợ.",
    
    # [44] [唉我艸，你看看，這三個人都成什麽樣了？我現在上哪去給他們…你幹嘛，別過來，艸，你們現在這個臉真他媽嚇人！]
    "[Haizz đệt mợ, cậu xem đi, ba người này thành cái dạng gì rồi? Giờ tôi biết đi đâu tìm thuốc cho chúng nó... Mày làm cái gì đấy, đừng có lại gần, đệt, cái bản mặt bây giờ của chúng mày kinh bỏ mẹ ra!]",
    
    # [45] “沒辦法，不這麽做騙不到他。”易緣瞥了一眼終端，眼神停留在鏡子前，他在思考睡衣該怎麽穿才能吸引到婁禧陽的目光。
    "“Hết cách rồi, không làm thế thì không lừa được anh ấy.” Dịch Duyên liếc nhìn thiết bị đầu cuối một cái, ánh mắt dừng lại trước gương, cậu đang suy tính xem đồ ngủ phải mặc thế nào mới thu hút được ánh nhìn của Lâu Hỉ Dương.",
    
    # [46] 陳斂看他這副模樣恨得牙癢癢，他真得不明白好好一個小孩怎麽會成現在這個樣子。
    "Trần Liễm nhìn bộ dạng này của cậu mà tức đến nghiến răng nghiến lợi, gã thực sự không tài nào hiểu nổi một đứa nhỏ ngoan ngoãn sao lại biến thành cái bộ dạng này.",
    
    # [47] [自打上個月你從你爸日記本上聯系到我，我已經幫你做了很多事，我可以一直幫你監視婁禧陽，你跟我們走後不用擔心什麽。]
    "[Kể từ tháng trước khi cậu lần theo cuốn nhật ký của cha cậu liên lạc với tôi, tôi đã giúp cậu làm bao nhiêu chuyện rồi, tôi có thể tiếp tục giúp cậu giám sát Lâu Hỉ Dương, sau khi cậu đi theo bọn tôi thì không cần phải lo lắng điều gì nữa.]",
    
    # [48] “再等等。”
    "“Chờ thêm chút nữa.”",
    
    # [49] [嘖，我不管你要做什麽，最多再給你一個月，必須跟我走，你爸媽留在你身體裡的那個芯片對我們來說至關重要。]
    "[Chậc, tôi mặc kệ cậu muốn làm cái gì, nhiều nhất chỉ cho cậu thêm một tháng nữa thôi, bắt buộc phải đi cùng tôi, con chip cha mẹ cậu để lại trong cơ thể cậu có ý nghĩa sống còn đối với chúng tôi.]",
    
    # [50] “嗯，知道了。”
    "“Vâng, biết rồi.”",
    
    # [51] [您可別騙我，就算你不想活，也不能不讓你情哥哥活下去吧，M星球全人類的命可都在你手裡，你太冷血，和你媽媽一點都不像…]
    "[Cậu đừng có lừa tôi đấy nhé, dẫu cho cậu không thiết sống thì cũng không thể không để cho anh trai tình nhân của cậu sống tiếp chứ, mạng sống của toàn thể nhân loại hành tinh M đều nằm trong tay cậu đấy, cậu quá máu lạnh, chẳng giống mẹ cậu một chút nào...]",
    
    # [52] 易緣滿臉不耐，一把關掉了終端，陳斂苦口婆心的勸說消失得一乾二淨。
    "Dịch Duyên đầy vẻ mất kiên nhẫn, dứt khoát tắt phụt thiết bị đầu cuối, những lời khuyên can đắng cay khổ cực của Trần Liễm lập tức tan biến sạch bách.",
    
    # [53] 他對上鏡子裡那雙陰鬱的眼，冷笑了一聲。
    "Cậu đối diện với đôi mắt u ám trong gương, cười khẩy một tiếng.",
    
    # [54] 他才不需要別人喜歡他，他只要婁禧陽喜歡。
    "Cậu căn bản chẳng cần ai khác thích mình, cậu chỉ cần Lâu Hỉ Dương thích cậu là đủ.",
    
    # [55] 與此同時，客廳的婁禧陽收到了一條訊息。
    "Cùng lúc đó, Lâu Hỉ Dương đang ở phòng khách nhận được một tin nhắn.",
    
    # [56] [張森澤：明早九點龍淵城六號商鋪巷口，急事，關於婁叔的。]
    "[Trương Sâm Trạch: Chín giờ sáng mai ở đầu ngõ cửa hàng số sáu thành Long Uyên, việc gấp, liên quan đến chú Lâu.]",
    
    # [57] 婁禧陽翻看著記錄，距離上一次張森澤跟他聯系，已經是五年前了。
    "Lâu Hỉ Dương lần giở lại lịch sử tin nhắn, khoảng cách từ lần cuối cùng Trương Sâm Trạch liên lạc với anh đã là chuyện của năm năm trước.",
    
    # [58] 果然，一切都要開始了嗎？
    "Quả nhiên, mọi chuyện sắp sửa bắt đầu rồi sao?",
    
    # [59] 婁禧陽的指尖有些燥熱，壓製在心裡的某種衝動時隔十幾年又重新冒了出來，很久了，他已經很久沒有這樣……興奮了。
    "Đầu ngón tay Lâu Hỉ Dương có chút nóng ran, một loại xúc động bị đè nén sâu kín trong lòng sau hơn mười năm nay lại rục rịch trỗi dậy. Đã lâu lắm rồi, anh đã lâu lắm rồi không có cảm giác…… phấn khích như thế này.",
    
    # [60] 上輩子也是這個時候，他收到了張森澤的消息，至此，他走上了一條通往深淵的道路。
    "Kiếp trước cũng vào đúng thời điểm này, anh nhận được tin nhắn của Trương Sâm Trạch, từ đó bước lên một con đường dẫn thẳng xuống vực sâu.",
    
    # [61] “陽哥，我洗好了，你也快去洗吧。”易緣清亮的嗓音打斷了婁禧陽的思緒。
    "“Dương ca, em tắm xong rồi, anh cũng mau đi tắm đi.” Chất giọng trong trẻo của Dịch Duyên cắt ngang dòng suy nghĩ của Lâu Hỉ Dương.",
    
    # [62] 他尋聲看去，只見易緣穿著一件松松垮垮的條紋睡衣，沒穿褲子，睡衣下擺剛好遮住了臀部，兩條又長又直的腿朝他走來。
    "Anh theo tiếng nhìn qua, chỉ thấy Dịch Duyên đang mặc một chiếc áo ngủ kẻ sọc thùng thình, không mặc quần, vạt áo ngủ vừa vặn che kín mông, đôi chân vừa dài vừa thẳng đang bước về phía anh.",
    
    # [63] 領口處的兩個紐扣都沒扣，鎖骨若隱若現。
    "Hai chiếc cúc áo nơi cổ áo đều không cài, xương quai xanh thoắt ẩn thoắt hiện.",
    
    # [64] 見婁禧陽的目光果然鎖在了自己身上，易緣滿意地勾起了嘴角，看來剛才在浴室裡沒白折騰。
    "Thấy ánh mắt của Lâu Hỉ Dương quả nhiên khóa chặt lên người mình, Dịch Duyên hài lòng nhếch khóe môi, xem ra ban nãy trong phòng tắm không uổng công lăn lộn.",
    
    # [65] 他知道婁禧陽直的不能再直，只有想方設法地按照星網上的攻略一步步來，要乖要軟會撒嬌，還要適當地勾引。
    "Cậu biết tỏng Lâu Hỉ Dương là thẳng nam không thể thẳng hơn, chỉ đành trăm phương ngàn kế làm theo từng bước hướng dẫn trên Tinh võng, phải ngoan, phải mềm mỏng biết làm nũng, lại còn phải biết câu dẫn một cách chừng mực.",
    
    # [66] “陽哥我…”易緣軟著聲伸手扯了扯婁禧陽的手。
    "“Dương ca em...” Dịch Duyên nũng nịu vươn tay kéo kéo tay Lâu Hỉ Dương.",
    
    # [67] “啪”的一聲，白嫩的手背上被婁禧陽打出了一片紅暈。
    "“Bốp” một tiếng, trên mu bàn tay trắng nõn bị Lâu Hỉ Dương đánh đỏ ửng một mảng.",
    
    # [68] “把褲子穿上。”
    "“Mặc quần vào.”",
    
    # [69] 婁禧陽面無表情地抽回了手，將褲子蒙到了易緣的頭上。
    "Lâu Hỉ Dương mặt không cảm xúc rút tay về, chụp luôn chiếc quần lên đầu Dịch Duyên.",
    
    # [70] 易緣：……
    "Dịch Duyên: ……",
    
    # [71] 【叮咚……目前還債進度降為10%】系統有氣無力地伏在婁禧陽肩上，一顆錘頭看上去很喪。
    "【Đinh đoong... tiến độ trả nợ hiện tại giảm xuống còn 10%】 Hệ thống ủ rũ phủ phục trên vai Lâu Hỉ Dương, cái đầu búa trông vô cùng thảm hại chán chường.",
    
    # [72] 婁禧陽有些詫異地看了易緣一眼。
    "Lâu Hỉ Dương có chút ngạc nhiên liếc nhìn Dịch Duyên một cái.",
    
    # [73] 難道不順著這小屁孩的心意走就不行？怎麽那麽小氣？可是這樣睡覺確實很冷啊。
    "Chẳng lẽ không thuận theo ý của thằng nhóc này là không xong sao? Sao mà nhỏ nhen thế? Nhưng ngủ kiểu đó thì lạnh thật mà.",
    
    # [74] 只見易緣黑著臉穿上了褲子，眼裡湧上了幾絲惱怒，“今晚哥哥要和我一起睡。”
    "Chỉ thấy Dịch Duyên đen mặt mặc quần vào, trong mắt dâng lên vài tia bực bội: “Tối nay anh phải ngủ cùng em.”",
    
    # [75] “爸爸的房間不能進去。”生怕婁禧陽拒絕，易緣趕緊補上了一句。
    "“Phòng của ba không được vào đâu.” Sợ Lâu Hỉ Dương từ chối, Dịch Duyên vội vã bồi thêm một câu.",
    
    # [76] 他家裡可只有兩間房。
    "Nhà cậu tính ra chỉ có đúng hai gian phòng.",
    
    # [77] 婁禧陽思索了一番，覺得易緣說得很有道理，加上想試驗自己的猜想，就點了點頭，“嗯，好。”
    "Lâu Hỉ Dương suy nghĩ một lát, cảm thấy Dịch Duyên nói rất có lý, cộng thêm muốn kiểm chứng suy đoán của mình, liền gật đầu: “Ừ, được.”",
    
    # [78] 【叮咚，目前還債進度為12%！】
    "【Đinh đoong, tiến độ trả nợ hiện tại là 12%!】",
    
    # [79] 提示音果然響起，婁禧陽望著易緣莫名有些雀躍的發旋，若有所思地挑了挑眉。
    "Âm thanh nhắc nhở quả nhiên vang lên, Lâu Hỉ Dương nhìn xoáy tóc tự dưng có vẻ hớn hở của Dịch Duyên, như có điều suy nghĩ khẽ nhướng mày.",
    
    # [80] 從去年開始，天氣就變得極為混亂，並且混亂程度逐日遞增，到目前，今天可能熱到地面可以煎雞蛋，明天就可能冰雹滿天飛，沒有人可以知道明天會是什麽樣的。
    "Kể từ năm ngoái, thời tiết đã trở nên vô cùng hỗn loạn, và mức độ hỗn loạn cứ tăng dần theo từng ngày. Cho đến hiện tại, hôm nay có thể nóng đến mức rán được trứng trên mặt đất, ngày mai đã có thể mưa đá bay đầy trời, chẳng ai có thể biết trước ngày mai sẽ ra sao.",
    
    # [81] 但據說paradise已經完成了氣候調節系統的設計，如果能花上一千萬買一張居住證，那麽就不用為忽冷忽熱的氣溫擔憂。
    "Nhưng nghe đồn Paradise đã hoàn thiện thiết kế hệ thống điều hòa khí hậu, nếu như có thể bỏ ra một ngàn vạn mua một tấm giấy phép cư trú, thì sẽ chẳng phải bận lòng lo lắng về nhiệt độ nóng lạnh thất thường nữa.",
    
    # [82] 夜裡很冷，刺骨的寒順著被子的縫隙一縷縷地竄進來
    "Đêm khuya lạnh thấu xương, cái rét buốt giá theo từng kẽ hở của tấm chăn từng luồng từng luồng len lỏi vào.",
    
    # [83] 易緣偷偷拉開婁禧陽的手臂縮到了他的懷裡，又強製性地把那張炙熱的手放在自己的腰上。
    "Dịch Duyên lén lút kéo cánh tay Lâu Hỉ Dương ra rồi rúc sâu vào trong lòng anh, lại còn mang tính cưỡng chế đặt bàn tay nóng rực kia lên eo của mình.",
    
    # [84] 感受到溫熱的體溫，甚至還夾雜著婁禧陽身上和他一樣的味道，易緣愜意的眯起了雙眼，默默地笑了一聲。
    "Cảm nhận được hơi ấm nhiệt độ cơ thể, thậm chí còn phảng phất mùi hương trên người Lâu Hỉ Dương giống hệt như mùi trên người cậu, Dịch Duyên khoan khoái híp đôi mắt lại, âm thầm cười khẽ một tiếng.",
    
    # [85] 你會隻屬於我的，婁禧陽。
    "Anh sẽ chỉ thuộc về một mình em thôi, Lâu Hỉ Dương.",
    
    # [86] 半夢半醒的婁禧陽被冰得一抖，下意識地把懷裡的人抱緊了。
    "Lâu Hỉ Dương trong cơn nửa tỉnh nửa mơ bị hơi lạnh làm cho khẽ rùng mình, theo bản năng vô thức ôm chặt lấy người trong lòng."
]

print(f"Total paras ch_002: {len(paras_ch2)}")

ch_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_002"
trans_path = os.path.join(ch_dir, "translation.md")
content = "---\ntitle: Chương 2: Mặc quần vào\n---\n\n" + "\n\n".join(paras_ch2) + "\n"
with open(trans_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Written {trans_path}")
