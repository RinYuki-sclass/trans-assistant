import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_048\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_048\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 103, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 1: Thẩm Từ -> anh
p[1] = "Thẩm Từ vô thức mím môi, trong giọng điệu ngày càng mập mờ của chàng trai, anh trở tay nắm chặt cổ tay đối phương rồi ấn mạnh lên cánh cửa."

# Para 24: Sở Tư Thừa -> cậu
p[24] = "Trong giọng điệu ngày càng lạnh nhạt của Thẩm Từ, đôi tai Sở Tư Thừa khẽ động, đôi mắt hạnh tròn trịa hơi nhướng lên, tựa như một chú mèo đang chằm chằm nhìn vào con mồi, ngay khi con mồi sắp sửa chạy thoát, cậu trực tiếp vươn tay, túm lấy cái đuôi mà đối phương đang muốn giấu đi."

# Para 25: Sở Tư Thừa -> cậu
p[25] = "Đầu ngón tay quấn từng vòng quanh chiếc cà vạt đen, càng làm tôn lên làn da trắng tuyết đến chói mắt, cậu giữ chặt người đàn ông đang định rời đi, ngay sau đó, trước khi đối phương kịp hủy bỏ thỏa thuận, cậu lên tiếng:"

# Para 31: chim sơn ca -> chim hoàng yến
p[31] = "“Tôi không có hứng thú với một con chim hoàng yến cũ.”"

# Para 44: Thẩm Từ -> anh
p[44] = "Chỉ là lần này, trước khi Thẩm Từ kịp tỉnh táo hơn nữa, một bàn tay khô ráo đột ngột nắm lấy cằm anh, sau đó dùng lực nhẹ, ngay khoảnh khắc Thẩm Từ bị ép phải ngửa đầu lên, trên đôi môi suýt chút nữa đã rách da kia liền xuất hiện một vệt hương cam quýt mang theo hơi thở ấm áp."

# Para 47: Thẩm Từ -> anh
p[47] = "Sở Tư Thừa khẽ đưa đầu lưỡi ra, thay Thẩm Từ liếm qua vết răng sâu hoắm kia, đồng thời cũng xoa dịu sự bất an trong lòng anh."

# Para 55: Thẩm Từ -> anh
p[55] = "Thế nhưng Thẩm Từ lại có cảm giác khó hiểu rằng, một khi anh bước chân ra khỏi căn phòng này, đừng nói đến chuyện giảm giá, ngay cả cơ hội tiếp cận chàng trai lần nữa cũng chẳng còn."

# Para 59: Sở Tư Thừa -> cậu
p[59] = "Đèn bên cạnh lối vào được bật lên ngay khoảnh khắc chàng trai tựa lưng vào công tắc, ánh sáng trắng ấm áp đổ xuống người cậu, tôn lên vẻ ngoài của cậu chẳng khác nào nhân vật chính trên sân khấu kịch."

# Para 62: Thẩm Từ thoại với Sở Tư Thừa
p[62] = "“Tốt nhất là cậu đừng lừa tôi!” Anh nói."

# Para 65: Sở Tư Thừa -> cậu
p[65] = "Cảm giác ẩm ướt nóng bỏng cùng với lời nói như giận dỗi in lên môi Sở Tư Thừa, người đàn ông với sự chiếm hữu cực mạnh ôm chặt lấy eo cậu."

# Para 78: Lệ Yến Trạch -> hắn
p[78] = "Dù sao sau khi hắn gặp tai nạn xe cộ, có quá nhiều kẻ thấy gió chiều nào che chiều nấy, biến mất khỏi bên cạnh hắn."

# Para 80: Lệ Yến Trạch -> hắn
p[80] = "Huống hồ hiện tại hắn còn có Chu Lạc Lạc, cho nên sự tồn tại của Tống Lạc An hay không, đối với hắn mà nói chẳng có chút ảnh hưởng nào."

# Para 86: Lệ Yến Trạch -> hắn
p[86] = "Trong quan niệm của Lệ Yến Trạch, chỉ có phần hắn vứt bỏ Tống Lạc An, tuyệt đối không có giả thiết Tống Lạc An dám quay ngược lại vứt bỏ mình."

# Para 87: Lệ Yến Trạch -> hắn
p[87] = "Từ đầu đến cuối hắn đều cho rằng trong mối quan hệ của hai người, hắn là kẻ ở vị trí chủ đạo, thế nên mới phẫn nộ đến vậy khi biết tin chàng trai kia phản bội mình."

# Para 88: Lệ Yến Trạch -> hắn
p[88] = "Không chỉ vì đoạn tình cảm mơ hồ hắn dành cho Tống Lạc An, mà còn vì lòng tự trọng không cho phép bất kỳ ai trái ý mình."

# Para 90: Lệ Yến Trạch -> Hắn
p[90] = "Hắn theo bản năng muốn chất vấn Tống Lạc An, chỉ là sau khi ngón tay nhấn vào số điện thoại, chưa đợi tiếng \"tút\" đầu tiên vang lên, hắn đã trực tiếp cúp máy."

# Para 91: Lệ Yến Trạch -> hắn
p[91] = "Một phần là vì hắn đột nhiên nhớ lại thái độ lạnh lùng của Tống Lạc An trong hai cuộc điện thoại trước đó, phần khác là vì tâm lý muốn trốn tránh theo bản năng của Lệ Yến Trạch."

# Para 92: Lệ Yến Trạch -> hắn
p[92] = "Giống như năm đó khi vừa mới gặp tai nạn xe cộ, hắn đã trốn tránh thông báo rằng mình có lẽ sẽ vĩnh viễn không thể đứng dậy được nữa, Lệ Yến Trạch không sẵn lòng chấp nhận, cũng không muốn trực tiếp đối mặt với sự thật rằng Tống Lạc An lại có thể hủy bỏ hợp đồng giữa hai người như thế, rồi không đợi được nữa mà lao vào vòng tay của một kim chủ tiếp theo."

# Para 94: Lệ Yến Trạch -> hắn
p[94] = "Lệ Yến Trạch khẽ rũ mắt, trước mặt hắn, màn hình điện thoại vì lâu không được chạm vào mà tắt ngóm."

# Para 97: Lệ Yến Trạch -> hắn
p[97] = "Nơi lồng ngực hắn giống như có thêm một ngọn núi lửa đang dần thức tỉnh, nham thạch không thể kìm nén được mà muốn phun trào từ bên trong ra ngoài."

# Para 98: Lệ Yến Trạch -> Hắn
p[98] = "Hắn cảm thấy cả người mình như đang bị một bàn tay vô hình xâu xé."

# Para 99: Lệ Yến Trạch -> hắn
p[99] = "Lý trí nói với hắn rằng, vì một món đồ chơi mà tức giận đến thế là không đáng, càng không đáng vì cậu ta mà triệt để trở mặt với nhà họ Thẩm, khiến cả giới phải xem trò cười."

# Para 100: Lệ Yến Trạch -> hắn
p[100] = "Nhưng cơ thể hắn lại không khống chế được mà muốn lập tức lao đến trước mặt Tống Lạc An, chất vấn đối phương tại sao lại rẻ mạt như thế, vẫn còn ở bên cạnh hắn mà đã nghĩ đến chuyện tìm người tiếp theo rồi?!"

# Para 102: Lệ Yến Trạch -> hắn
p[102] = "Dù sao thì thời gian qua, hắn cũng thừa nhận bản thân quả thực vì chuyện của Lạc Lạc mà đã lạnh nhạt với cậu một thời gian dài."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_048 updated successfully. Total paragraphs:", len(p))
