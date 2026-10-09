import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_049\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_049\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 104, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 10: Chu Lạc Lạc thoại xưng em
p[10] = "“Hay là... để em đi xin lỗi cậu ấy nhé.”"

# Para 50: Thẩm Từ -> anh
p[50] = "Vị cam quýt trong khoang miệng mãi vẫn không tan đi, giống như cảm giác trơn trượt thỉnh thoảng lại xuất hiện trên gò má anh vậy, khiến người ta không kìm được muốn đưa tay chạm vào, để xác nhận xem những thứ đó rốt cuộc đã được mình rửa sạch hay chưa."

# Para 68: Thẩm Từ -> anh
p[68] = "Chỉ có điều lần này, trước khi anh kịp dùng lực, một ngón tay mang theo hơi nước đã nhanh hơn một bước chen vào giữa đôi môi anh."

# Para 70: Sở Tư Thừa -> cậu
p[70] = "Thẩm Từ nghe thấy cậu nói: “Đừng dày vò bản thân.”"

# Para 75: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[75] = "Thẩm Từ không nói gì, chỉ lẳng lặng cảm nhận ngón tay trong khoang miệng đang khều nhẹ đầu lưỡi mình như thế nào, khám phá từng ngóc ngách bên trong khuôn miệng anh, giống như cách cậu đã tỉ mỉ làm anh mềm nhũn ra trước đó."

# Para 77: Sở Tư Thừa -> Cậu
p[77] = "Cậu chậm rãi rút ngón tay mình về, đồng thời bàn tay còn lại cũng thoát khỏi sự kiềm chế của Thẩm Từ, tiếp tục di chuyển xuống dưới."

# Para 90: Thẩm Từ -> anh
p[90] = "Bốn mắt nhìn nhau, đôi mày anh không tự chủ được mà nhíu lại, “Ai thế?”"

# Para 94: Sở Tư Thừa -> cậu
p[94] = "Ban đầu cậu không định để ý đến người bên ngoài, chỉ là tiếng chuông cửa kia sau khi không nhận được hồi đáp thì không những không biết điều mà dừng lại, ngược lại còn vang lên ngày càng dồn dập hơn."

# Para 98: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[98] = "Chỉ là trước khi mở cửa phòng tắm, cậu lại đột ngột dừng lại, suy nghĩ vài giây rồi quay trở vào, vớt Thẩm Từ vẫn còn đang nhũn cả tứ chi ra khỏi nước, phủ một chiếc khăn lên đầu anh, sau đó cầm lấy chiếc áo choàng tắm bên cạnh quấn chặt lấy người anh."

# Para 99: Sở Tư Thừa -> cậu
p[99] = "Thẩm Từ nhìn hành động của cậu không nhịn được mà nhướng mày, “Chu đáo đến vậy sao?”"

# Para 100: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[100] = "Có thể nói, ngay khi Sở Tư Thừa quay lại bế anh ra khỏi bồn tắm, Thẩm Từ đã hiểu rõ ý định của cậu — chàng trai lo lắng người bên ngoài sẽ bất chấp xông vào, nên đã giúp anh chuẩn bị sẵn sàng trước."

# Para 101: Thẩm Từ -> anh
p[101] = "Như vậy dù cho có xảy ra chuyện ngoài ý muốn thật, anh cũng không đến mức hoàn toàn không có sự chuẩn bị nào."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_049 updated successfully. Total paragraphs:", len(p))
