import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_050\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_050\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 95, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 21: Sở Tư Thừa -> cậu
p[21] = "Ngoại hình hiện tại của cậu vốn thuộc kiểu \"cún con\" ấm áp, đôi mắt tròn trịa, dù không cười, chỉ cần nhìn chằm chằm vào người khác với ánh mắt ướt át thôi cũng đủ khiến đối phương có cảm giác mình là cả thế giới của cậu."

# Para 22: Sở Tư Thừa -> cậu
p[22] = "Huống chi bây giờ cậu đang cười với Lệ Yến Trạch, đôi mắt cún con tròn xoe hơi cong lại, con ngươi đen láy sáng lấp lánh, trông như thể thật sự bị những lời của Chu Lạc Lạc làm cho cảm động."

# Para 26: Sở Tư Thừa -> cậu
p[26] = "Thế nhưng, điều khiến hắn không ngờ tới là, Sở Tư Thừa đúng là đã cười với hắn, nhưng những lời cậu thong thả thốt ra sau đó lại là,"

# Para 34: Chu Lạc Lạc -> Gã
p[34] = "Gã nghi ngờ \"Tống Lạc An\" uống nhầm thuốc rồi."

# Para 35: Chu Lạc Lạc -> gã
p[35] = "Bởi lẽ cho dù là kiếp trước, hay là Tống Lạc An mà gã nhìn thấy sau khi trọng sinh trở về, khi đối mặt với Lệ Yến Trạch đều là dáng vẻ cẩn trọng dè dặt, tự cho là mình che giấu rất tốt, nhưng thực chất sự ái mộ trong mắt đã đong đầy đến mức sắp tràn ra ngoài."

# Para 42: Tống Lạc An -> cậu
p[42] = "Trong dự tính của Lệ Yến Trạch, hôm nay hắn có thể dẫn theo Chu Lạc Lạc đến cúi đầu xin lỗi Tống Lạc An đã là nể mặt cậu lắm rồi, nếu đối phương biết điều thì nên ngoan ngoãn thuận theo bậc thang hắn đưa ra mà bước xuống."

# Para 50: Tống Lạc An -> cậu
p[50] = "Cho nên, trong khoảng thời gian mất tích này, cậu hoàn toàn không hề nhớ tới hắn."

# Para 63: Lệ Yến Trạch -> hắn
p[63] = "Dù sao thì con chim hoàng yến mà Thẩm Từ không cần, cuối cùng lại phải cầu xin để được quay về bên cạnh hắn, Lệ Yến Trạch."

# Para 65: Lệ Yến Trạch -> hắn
p[65] = "Nhưng đáng tiếc thay, kịch bản hắn đã viết xong xuôi, diễn viên trước mắt lại chẳng hề phối hợp, còn rất không biết điều mà đặt câu hỏi cho hắn."

# Para 69: Sở Tư Thừa -> cậu
p[69] = "Lệ Yến Trạch nghe vậy cứ ngỡ thái độ của cậu cuối cùng đã mềm mỏng, đôi mắt sáng rực lên, lập tức gật đầu: \"Làm gì cũng được!\""

# Para 71: Sở Tư Thừa -> cậu
p[71] = "Sở Tư Thừa mỉm cười, sau đó dưới ánh mắt đầy vẻ nắm chắc phần thắng của Lệ Yến Trạch, cậu khẽ nói:"

# Para 90: Sở Tư Thừa -> Cậu
p[90] = "Cậu nói: “Sao anh có thể cho được chứ, bởi vì tất cả những chuyện này, chẳng phải đều do một tay Lệ tổng anh gây ra sao?”"

# Para 91: Lệ Yến Trạch -> Hắn, Tống Lạc An -> cậu
p[91] = "Hắn gây áp lực lên trường học, đưa người cha nghiện rượu của cậu từ quê nhà đến, chỉ vì Tống Lạc An bắt đầu phản kháng, không nghe lời, nên hắn bắt đầu dùng những \"chuyện nhỏ\" mà hắn cho là vậy để trừng phạt cậu."

# Para 94: Tống Lạc An -> cậu
p[94] = "Cú sốc bị đuổi học, bị người cha tồi tệ ôm chân khóc lóc xin tiền giữa đường, sự ngột ngạt và tuyệt vọng khi bị người qua đường chỉ trỏ, những ký ức này sẽ không biến mất chỉ vì cậu quay về bên Lệ Yến Trạch."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_050 updated successfully. Total paragraphs:", len(p))
