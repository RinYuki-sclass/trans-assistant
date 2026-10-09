import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_047\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_047\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 109, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 2: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[2] = "Trong vài giây ngắn ngủi khi nhấn vào tin nhắn, Thẩm Từ đã suy đoán rất nhiều điều mà cậu có thể sẽ gửi cho anh."

# Para 3: Thẩm Từ -> anh
p[3] = "Thế nhưng, anh vẫn đoán sai rồi."

# Para 4: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[4] = "Anh cứ ngỡ ít nhất cậu cũng sẽ hỏi một câu xem tối nay anh có qua đó hay không, kết quả là đối phương hoàn toàn không nhắc lại chuyện này nữa."

# Para 6: Sở Tư Thừa -> cậu
p[6] = "Đó là bức ảnh cậu đang cầm tuýp thuốc mỡ trong tay."

# Para 9: Sở Tư Thừa -> cậu
p[9] = "Làn da trắng sứ, những ngón tay thon dài, dưới ống kính mờ nhòe vẫn thấy được các khớp xương hơi ửng hồng, cùng với tuýp thuốc màu bạc đang bị đầu ngón tay của cậu siết chặt khiến người ta không thể ngó lơ."

# Para 12: Sở Tư Thừa -> cậu
p[12] = "Đúng lúc này, theo một tiếng \"đinh đông\", cậu lại gửi thêm một tin nhắn nữa."

# Para 13: Thẩm Từ -> anh
p[13] = "Vẫn không hề đề cập đến việc anh có qua đó hay không, dường như chỉ đơn thuần là đưa ra lời giải đáp cho tấm ảnh phía trên,"

# Para 18: Sở Tư Thừa -> Cậu
p[18] = "Cậu giống như đã quên mất chuyện mình từng táo bạo mời Thẩm Từ qua đây, hệt như một cậu sinh viên đơn thuần vô tri, tràn đầy sự tò mò mập mờ đối với tuýp thuốc mỡ trong tay."

# Para 20: Thẩm Từ -> anh
p[20] = "Trong những tin nhắn này, rõ ràng chàng trai kia không hề nhắc đến ý định sử dụng thuốc mỡ lấy một chữ, nhưng Thẩm Từ lại cảm thấy xúc cảm trơn trượt mang theo hương cam quýt ấy dường như đã rơi xuống đầu ngón tay anh..."

# Para 24: Thẩm Từ -> anh
p[24] = "Mà là một lời trần thuật vô cùng thẳng thắn, nói cho chàng trai biết một cách đơn giản và rõ ràng rằng, anh đã thấu rõ tâm tư nhỏ nhen ẩn giấu sau những dòng tin nhắn kia."

# Para 27: Sở Tư Thừa -> Cậu
p[27] = "Cậu trả lời: 【Vậy anh cắn câu chưa?】"

# Para 29: Thẩm Từ -> anh
p[29] = "Sở Tư Thừa còn thẳng thắn hơn cả anh."

# Para 30: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[30] = "Cách một màn hình, Thẩm Từ dường như nhìn thấy chàng trai đang đứng trước mặt mình, trên khuôn mặt xinh đẹp treo nụ cười rạng rỡ, bên trong che giấu đầy ý xấu trêu chọc, ngay cả chiếc đuôi ác quỷ phía sau cũng không thèm che giấu mà đung đưa, dường như chắc chắn rằng cho dù anh có nhìn thấy dáng vẻ xấu tính của cậu, cũng sẽ không lựa chọn rời đi."

# Para 39: Thẩm Từ -> anh
p[39] = "Chiếc xe màu đen lao nhanh trên đường, Thẩm Từ nghịch chiếc điện thoại không một chút động tĩnh, trong đôi mắt màu mực dần dâng lên một tia hứng thú vốn không mấy khi xuất hiện ở anh."

# Para 46: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[46] = "Liệu cậu còn cùng anh dây dưa mập mờ như hiện tại không?"

# Para 47: Thẩm Từ -> anh
p[47] = "Loại vấn đề hoàn toàn không thể xác định này đối với Thẩm Từ mà nói đã rất lâu rồi chưa từng gặp phải. Cuộc sống của anh quá đỗi thuận lợi, thậm chí thuận lợi đến mức có phần tẻ nhạt, thế nên khi chạm trán một biến số như Sở Tư Thừa, anh đã không tự chủ được mà bị đối phương thu hút."

# Para 50: Thẩm Từ -> anh
p[50] = "Sau đó, trong ánh mắt ngẩn ngơ của Thẩm Từ, chàng trai đang đợi ở cửa thang máy nở một nụ cười rạng rỡ vô cùng với anh."

# Para 51: Sở Tư Thừa -> cậu
p[51] = "Trên tay cậu không cầm bất kỳ tuýp thuốc mỡ nào, nhưng Thẩm Từ dường như vẫn ngửi thấy mùi hương cam quýt thoang thoảng ấy."

# Para 52: Thẩm Từ -> anh
p[52] = "Là ảo giác của anh sao?"

# Para 53: Thẩm Từ -> anh
p[53] = "Thẩm Từ nghĩ như vậy, nhưng ngay sau đó, suy đoán của anh lại một lần nữa bị chàng trai kia phá vỡ."

# Para 54: Thẩm Từ -> anh
p[54] = "Cà vạt trước ngực bị những ngón tay thon dài khẽ khàng kéo lấy, theo động tác của Sở Tư Thừa, Thẩm Từ không tự chủ được mà ngẩng đầu lên, để rồi giây tiếp theo, anh cảm nhận được một sự mềm mại chạm khẽ lên môi mình."

# Para 57: Sở Tư Thừa -> cậu
p[57] = "Thẩm Từ nghe thấy cậu nói: “Ông chủ, thích mùi vị này không?”"

# Para 59: Sở Tư Thừa -> Cậu
p[59] = "Cậu đứng bên ngoài thang máy, ánh đèn vàng cam trên đỉnh đầu rớt xuống những vụn sáng vàng kim giữa làn tóc đen, kết hợp cùng gương mặt xinh đẹp kia, rực rỡ tựa như một giấc mộng."

# Para 62: Sở Tư Thừa -> cậu
p[62] = "Sở Tư Thừa nhìn Thẩm Từ đang đứng lặng thinh trong thang máy, chỉ chăm chú nhìn chằm chằm vào mình, đầu lưỡi cậu khẽ đẩy ra, mang theo viên kẹo màu cam ở trên đó."

# Para 64: Sở Tư Thừa -> Cậu
p[64] = "Cậu nói: “Yên tâm đi, tôi không có sở thích ăn uống bậy bạ đâu.”"

# Para 65: Sở Tư Thừa -> cậu
p[65] = "Sở Tư Thừa tưởng rằng Thẩm Từ ngẩn người trong thang máy là do đối phương hiểu lầm mùi vị trong miệng cậu là từ thuốc mỡ, nên mới đặc biệt giải thích một câu."

# Para 68: Sở Tư Thừa -> cậu
p[68] = "Thế nhưng, ngay khi hai người vừa vào cửa, Sở Tư Thừa đi phía sau Thẩm Từ vừa đóng cửa lại, thì ngay giây tiếp theo, cậu đã bị Thẩm Từ ở phía trước túm lấy vai, ấn mạnh lên cánh cửa."

# Para 70: Thẩm Từ -> anh
p[70] = "Giọng nói của người đàn ông như được tôi qua băng giá, dễ dàng khiến người ta nhận ra sự bất mãn của anh lúc này."

# Para 71: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[71] = "Thực ra anh không hề quan tâm Sở Tư Thừa có ăn uống bậy bạ hay không, anh chỉ cảm thấy bất ngờ trước hành động hôn đầy nhiệt tình của chàng trai, và càng muốn biết, ngoài anh ra, liệu cậu có đối xử với người khác như vậy hay không!"

# Para 76: Sở Tư Thừa -> Cậu
p[76] = "Cậu hỏi: “Anh đang ghen sao?”"

# Para 82: Shen -> Thẩm
p[82] = p[82].replace("nhà họ Shen", "nhà họ Thẩm")

# Para 91: Thẩm Từ -> anh
p[91] = "Một chàng trai vừa mới quen biết chưa đầy một tuần, tại sao lại có thể gây ra ảnh hưởng lớn đến cảm xúc của anh như vậy?"

# Para 93: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[93] = "Nhiệt độ cơ thể từ người cậu truyền qua lớp áo mỏng manh đến tận đầu ngón tay Thẩm Từ, khiến anh bừng tỉnh, đồng thời cũng đột ngột thu lại bàn tay đang đặt trên vai Sở Tư Thừa."

# Para 98: Sở Tư Thừa -> cậu
p[98] = "Giọng điệu của cậu nghe có vẻ hơi bất lực, giống như chỉ đang phối hợp với một Thẩm Từ cứng miệng không chịu cúi đầu, khiến Thẩm Từ nghe mà thấy hơi bực mình."

# Para 99: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[99] = "Nhưng cậu cứ như thể có khả năng thấu thị nội tâm anh, không đợi ngọn lửa trong lòng Thẩm Từ bùng lên, Sở Tư Thừa đã nói tiếp:"

# Para 102: Sở Tư Thừa -> Cậu
p[102] = "Cậu vươn tay vuốt phẳng hàng lông mày đang khẽ nhíu lại của Thẩm Từ, sau đó nhếch khóe miệng với đối phương:"

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_047 updated successfully. Total paragraphs:", len(p))
