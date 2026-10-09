import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_041\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_041\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 92, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 3: Lệ Yến Trạch -> hắn
p[3] = "Vốn dĩ, trong khoảng thời gian Lệ Yến Trạch gặp tai nạn xe cộ, nhờ sự chăm sóc tỉ mỉ không quản ngày đêm của Tống Lạc An, hắn đã dần quên đi bản hợp đồng kia. Trong những lần chung đụng thường ngày, hắn cũng thực sự ngỡ rằng mình và Tống Lạc An chỉ là một cặp tình nhân bình thường, đôi khi thậm chí còn vì một cử chỉ dịu dàng vô ý của Tống Lạc An mà rung động."

# Para 13: Lệ Yến Trạch -> hắn
p[13] = "Lệ Yến Trạch ngước mắt, ánh nhìn độc địa như loài rắn độc rơi trên cánh cửa đã bắt đầu lung lay trước mặt, sau đó hắn cười lạnh một tiếng, đáy mắt tràn ngập sự châm biếm dành cho Tống Lạc An và cả chính bản thân ngu ngốc của mình trong khoảng thời gian qua."

# Para 15: Lệ Yến Trạch -> Hắn
p[15] = "Hắn ngược lại muốn xem thử, kẻ có thể khiến Tống Lạc An thà phản bội mình để bám lấy rốt cuộc là ai!"

# Para 16: Chu Lạc Lạc -> gã
p[16] = "Chu Lạc Lạc nhếch mép cười khi Lệ Yến Trạch không nhìn thấy, nhưng trong lòng, gã vẫn giả vờ tỏ ra rất lo lắng cho Lệ Yến Trạch."

# Para 17: Chu Lạc Lạc -> gã
p[17] = "Bây giờ chỉ cần đám bảo vệ phá cửa xông vào, để Lệ Yến Trạch tận mắt nhìn thấy Tống Lạc An quấn lấy người đàn ông kia, kế hoạch chia rẽ của gã hôm nay coi như đã hoàn thành mỹ mãn."

# Para 21: Chu Lạc Lạc -> gã
p[21] = "Đến lúc đó, chú rể còn lại trong đám cưới thế kỷ của nhà họ Lệ, chắc chắn sẽ không ai khác ngoài gã, Chu Lạc Lạc!"

# Para 22: Chu Lạc Lạc -> gã
p[22] = "Gã sẽ không còn bị đám người nhà họ Chu khinh thường nữa, ngược lại, đám người kia còn phải quay sang nịnh bợ, xu nịnh gã, cầu xin gã cho họ một miếng cơm ăn!"

# Para 26: Chu Lạc Lạc -> gã
p[26] = "Để Tống Lạc An hoàn toàn biến mất khỏi cuộc đời Lệ Yến Trạch, nhường chỗ cho gã!"

# Para 28: Chu Lạc Lạc -> gã
p[28] = "Tuy nhiên, ngay khi gã còn đang đau đầu suy nghĩ xem nên mặc bộ quần áo nào để đi \"lật mặt\" đám người nhà họ Chu, thì cánh cửa trước mặt, vốn dĩ theo dự đoán của gã sẽ bị đám bảo vệ Lệ Yến Trạch mang tới đá tung ra, lại đột nhiên bị mở từ bên trong."

# Para 42: Thẩm Từ -> anh
p[42] = "Bánh xe vừa bắt đầu quay đã bị người đàn ông một cước đạp dừng lại, còn tên vệ sĩ đang nằm trên đất ôm lấy \"anh em\" mà co giật cũng bị anh túm lấy cổ áo, tiện tay ném ra ngoài cửa như vứt rác."

# Para 50: Thẩm Từ -> anh
p[50] = "Giọng điệu của anh thực sự rất bình thản, nhưng kết hợp với vẻ mặt cao cao tại thượng, cùng với lời nói nghe không lọt tai chút nào, vô thức khiến người ta có cảm giác đang bị anh chế giễu, hơn nữa còn là sự chế giễu đến cực điểm."

# Para 53: Chu Lạc Lạc thoại
p[53] = "“Anh dựa vào đâu mà nói Trạch ca như vậy?! Nếu không phải anh và Tống Lạc An ở đây làm những chuyện mờ ám không dám để ai thấy, anh nghĩ chúng tôi thèm nhìn thấy anh sao?!”"

# Para 54: Chu Lạc Lạc
p[54] = "Chưa đợi Lệ Yến Trạch mở miệng, Chu Lạc Lạc đã nhanh chóng nhảy ra lấy lòng."

# Para 55: Chu Lạc Lạc -> gã
p[55] = "Một tay gã chống nạnh, tay kia chỉ vào Thẩm Từ đang dựa vào khung cửa, má đỏ bừng, vẻ mặt đầy vẻ chính nghĩa, như thể đã đứng trên đỉnh cao đạo đức vậy."

# Para 56: Chu Lạc Lạc thoại
p[56] = "“Nếu anh không làm chuyện gì trái lương tâm, tại sao lại sợ chúng tôi gõ cửa?! Còn nói năng khó nghe như vậy, là do chột dạ nên nói năng lung tung rồi chứ gì!”"

# Para 57: Chu Lạc Lạc
p[57] = "Miệng Chu Lạc Lạc líu lo một tràng dài, lời lẽ như thể đã tận mắt nhìn thấy cảnh Thẩm Từ và Tống Lạc An vụng trộm, nên giờ phải đóng đinh họ lên cột sỉ nhục, bắt họ phải xấu hổ vì hành vi của mình!"

# Para 58: Chu Lạc Lạc -> gã
p[58] = "Thế nhưng, Thẩm Từ, người đang bị gã phán xét chính nghĩa, nghe vậy chỉ nhàn nhạt liếc nhìn gã một cái, rồi nói:"

# Para 63: Thẩm Từ -> Anh
p[63] = "Anh rũ mắt nhìn Lệ Yến Trạch, giọng điệu cũng lạnh lùng hẳn đi."

# Para 69: Thẩm Từ -> anh
p[69] = "Lệ Yến Trạch ngẩng đầu nhìn Thẩm Từ, ánh mắt sắc lẹm lướt từ đôi môi anh dần xuống phía dưới từng chút một."

# Para 87: Thẩm Từ -> anh
p[87] = "Hắn chẳng còn chút ý định nào muốn dây dưa với Thẩm Từ nữa, ánh mắt trực tiếp lướt qua anh, rơi vào căn phòng phía sau,"

# Para 91: tiên sinh Chu / tiên sinh Tống -> cậu Chu / cậu Tống
p[91] = "“Trong camera giám sát chỉ là một bóng lưng mờ ảo, ngộ nhỡ đúng như lời cậu Chu nói, chỉ là một nhân viên phục vụ có vóc dáng tương tự cậu Tống thì sao?”"

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_041 updated successfully. Total paragraphs:", len(p))
