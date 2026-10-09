import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_043\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_043\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 97, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 11: chim sơn ca -> chim hoàng yến
p[11] = "Cậu trợ lý nhỏ hùng dũng oai vệ chỉnh lại cà vạt trước ngực, chỉ chờ \"chim hoàng yến\" nhỏ khen ngợi sự sắp xếp tỉ mỉ của mình với ông chủ, đón chờ tương lai tươi đẹp được thăng chức tăng lương."

# Para 12: Sở Tư Thừa -> cậu
p[12] = "Thế nhưng, sáng sớm hôm sau khi tỉnh dậy, Sở Tư Thừa nhìn xe đẩy đầy ắp táo đỏ, yến sào, kỷ tử, còn có một củ nhân sâm nghìn năm theo lời nhân viên phục vụ... Cậu chỉ cảm thấy mình còn chưa bắt đầu ăn mà mũi đã sắp chảy máu đến nơi rồi."

# Para 13: Sở Tư Thừa -> cậu
p[13] = "“Thế này là có ý gì?” Cậu đưa tay nhấc một tuýp thuốc mỡ nhỏ trong chiếc hộp ở tầng thứ hai của xe đẩy lên, sau khi nhìn rõ ba chữ lớn “Hộ Cúc Sảng” trên đó, bộ não vốn đang tràn ngập lời muốn thổ tào của cậu trong thoáng chốc chỉ còn lại sáu dấu chấm tròn."

# Para 14: phục vụ nói
p[14] = "“À! Đây là do ngài Thẩm đặc biệt chuẩn bị cho cậu đấy ạ,”"

# Para 18: nở rộ
p[18] = "Để cậu nở rộ?"

# Para 21: Sở Tư Thừa -> cậu
p[21] = "Sở Tư Thừa nhìn tuýp thuốc mỡ trong tay, bật cười một tiếng đầy ẩn ý, sau đó nhét nó vào chiếc túi nhỏ màu đen mà cậu định mang theo."

# Para 24: Sở Tư Thừa -> cậu
p[24] = "Cậu đưa tay xuống dưới gối mò ra chiếc điện thoại nát đang sạc đến nóng hổi, Sở Tư Thừa mở khóa màn hình, ngay giây tiếp theo, màn hình đã bị đơ đến mức không thể chạm vào bởi hàng loạt cuộc gọi lỡ và tin nhắn điên cuồng ùa tới."

# Para 26: chim sơn ca -> chim hoàng yến
p[26] = "Dẫu sao đối phương cũng là một tổng tài bá đạo, vẫn cần thể diện và lòng tự trọng, đối mặt với một \"chim hoàng yến\" cần hắn bao nuôi, hắn tuyệt đối không thể làm ra hành động hèn mọn đến cực điểm là điên cuồng gọi điện cho đến khi Sở Tư Thừa bắt máy mới thôi."

# Para 27: Sở Tư Thừa -> cậu
p[27] = "Sở Tư Thừa kiểm tra một chút, cộng thêm cuộc gọi tối qua để xác nhận xem cậu có ở trong phòng hay không, Lệ Yến Trạch tổng cộng đã gọi cho cậu ba cuộc điện thoại, gửi hai tin nhắn."

# Para 28: Sở Tư Thừa -> cậu
p[28] = "Còn những tin nhắn khác suýt chút nữa làm điện thoại cậu nổ tung là đến từ người cha nghiện rượu, đứa em đang đi học, và người mẹ đang mang bệnh mà nửa đêm vẫn không chịu đi ngủ của cậu."

# Para 40: Nhạc Mỹ -> Lạc Mỹ
p[40] = p[40].replace("Nhạc Mỹ", "Lạc Mỹ")

# Para 61: thoại của Sở Tư Thừa
p[61] = "“Đáng tiếc, tôi không có sở thích đàn gảy tai trâu, cho nên nếu mày đã nghe không hiểu thì đi chết đi cho rồi.”"

# Para 63: Tống Lạc Minh
p[63] = "Tống Lạc Minh sau khi phản ứng lại thì tức đến nổ phổi vì câu nói này của Sở Tư Thừa."

# Para 70: Sở Tư Thừa -> cậu
p[70] = "Trên chiếc giường lớn trắng muốt, cậu tựa lưng vào đầu giường mềm mại, mọi thứ xung quanh đều là những thứ đắt đỏ và hoa lệ, ngay cả chiếc gối cậu đang kê dưới thắt lưng lúc này cũng có giá từ năm chữ số trở lên."

# Para 71: Sở Tư Thừa -> cậu
p[71] = "Trong một căn phòng như thế này, thứ rẻ nhất có lẽ chính là đống quần áo trong máy giặt và cái điện thoại cùi bắp giá vài trăm tệ trên tay cậu."

# Para 75: Tống Lạc An -> cậu ta
p[75] = "Một tổng tài bá đạo, đối với chó thì hào phóng như vậy, đối với người tình dù có tệ bạc đến đâu cũng không đến mức để cậu ta sống như thể vừa bò ra từ khu ổ chuột."

# Para 79: nguyên chủ -> cậu ta
p[79] = "Cho nên, gia đình mà cậu ta thà bạc đãi bản thân cũng phải phụng dưỡng, rốt cuộc đã cho nguyên chủ được cái gì?"

# Para 85: Sở Tư Thừa -> cậu
p[85] = "Tống Lạc An là vế trước, gia đình cậu ta là vế sau, còn Sở Tư Thừa, cậu chẳng thuộc về bên nào cả."

# Para 86: Sở Tư Thừa -> cậu
p[86] = "Trong mắt cậu không có thứ gọi là tình thân, bản thân cậu lại càng chẳng có chút cảm giác đạo đức nào."

# Para 87: Tống Nhạc Minh -> Tống Lạc Minh, Sở Tư Thừa
p[87] = "Thế là, mặc cho Tống Lạc Minh có ở đầu dây bên kia nổi điên trong bất lực thế nào, Sở Tư Thừa cũng chỉ đáp lại đúng một câu:"

# Para 88: Thoại Sở Tư Thừa
p[88] = "“Vậy thì mày đi chết đi.”"

# Para 89: Sở Tư Thừa -> cậu
p[89] = "Lệ Yến Trạch định dùng gia đình để đe dọa cậu, ép cậu phải quỳ gối cúi đầu, đúng là quá đỗi ngây thơ."

# Para 90: Sở Tư Thừa -> cậu
p[90] = "Sở Tư Thừa cúp máy, sau đó trực tiếp tắt nguồn điện thoại, cắt đứt mọi liên lạc với thế giới bên ngoài. Cả ngày cậu chỉ ở trong khách sạn ăn uống chơi bời, hoàn toàn không màng đến những sóng gió ngoài kia."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_043 updated successfully. Total paragraphs:", len(p))
