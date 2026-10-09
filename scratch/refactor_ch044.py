import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_044\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_044\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 95, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 12: Sở Tư Thừa -> cậu
p[12] = "Mà lúc này ở phía bên kia, trong căn phòng khách sạn xa hoa rộng rãi, Sở Tư Thừa nhìn chiếc điện thoại đặt làm riêng màu bạc trắng vừa mới lắp thẻ sim trong tay, ánh mắt cậu khẽ động, sau đó lại ngẩng đầu xác nhận với quản gia khách sạn một lần nữa:"

# Para 28: anh ta -> cậu ấy
p[28] = "“Hơn nữa mấy ngày nay nghe quản gia khách sạn nói, vị tiên sinh ở bên trong vẫn luôn không ra khỏi cửa, ngoại trừ dịch vụ ăn uống cần thiết, các dịch vụ khác cậu ấy cũng hủy bỏ, cơ bản là không gặp ai.”"

# Para 32: chim sơn ca -> chim hoàng yến
p[32] = "Phải biết rằng, đó chính là chú chim hoàng yến nhỏ đầu tiên mà sếp của họ bao nuôi đấy!"

# Para 46: Tống Lạc An -> Cậu ấy
p[46] = "“Cậu ấy rất, rất thích Lệ Yến Trạch……”"

# Para 47: Tống Lạc An -> cậu ấy
p[47] = "Vì vậy, ngay cả khi người đàn ông gặp tai nạn xe cộ, cậu ấy cũng không rời đi."

# Para 49: Tống Lạc An -> cậu
p[49] = "Nhưng ngay cả như vậy, Tống Lạc An cũng không bỏ cuộc, sau đó vì Lệ Yến Trạch không thích người lạ chạm vào mình, cậu còn tranh thủ thời gian đi học mát-xa."

# Para 50: Thẩm Từ -> anh
p[50] = "Thế nhưng, một người dường như si tình đến cực điểm trong báo cáo lại chủ động mời anh bao nuôi vào tối hôm đó, thậm chí còn nói có thể giảm giá…"

# Para 55: Thẩm Từ -> anh
p[55] = "Thẩm Từ rất rõ, nếu người con trai anh gặp đêm đó chính là người trong báo cáo, thì ngay khi anh bước ra khỏi phòng, não bộ sẽ tự động xóa sạch mọi dấu vết về đối phương."

# Para 56: Thẩm Từ -> anh
p[56] = "Nhưng tiếc là, chàng trai anh gặp không phải."

# Para 57: Tống Lạc An -> cậu, Thẩm Từ -> anh
p[57] = "Báo cáo kẹp rất nhiều ảnh của Tống Lạc An, có lúc cậu đi học, lúc làm thêm, lúc cười, lúc buồn bã… từng tấm từng tấm, mỗi tấm một vẻ, mỗi tấm đều không phải là người anh muốn gặp…"

# Para 59: Thẩm Từ -> Anh
p[59] = "Anh thường không hút thuốc."

# Para 60: Thẩm Từ -> anh
p[60] = "Dù là họp ở công ty mình hay ra ngoài gặp đối tác, mùi thuốc lá bám trên người luôn khiến hình ảnh của anh bị giảm giá trị ngay lập tức."

# Para 62: Thẩm Từ -> anh
p[62] = "Cho nên, anh không nên chạm vào, cũng không thể chạm vào."

# Para 64: Thẩm Từ -> anh
p[64] = "Khói bám lên người anh, cũng làm mờ đi đôi mắt đen sâu thẳm ấy."

# Para 77: Thẩm Từ -> Anh
p[77] = "Anh vẫn không thích trò đào góc tường, Thẩm Từ nghĩ."

# Para 80: Sở Tư Thừa -> cậu, Tống Lạc Minh
p[80] = "Đây là cuộc gọi đầu tiên cậu bắt máy kể từ sau khi cúp điện thoại của Tống Lạc Minh."

# Para 91: Lệ Yến Trạch -> Hắn
p[91] = "Hắn nghĩ, nếu Tống Lạc An lúc này có thể cúi đầu nhận sai, thì nhìn vào việc đối phương đã từng chăm sóc mình, hắn vẫn có thể tha thứ cho cậu, tiền viện phí bên kia cũng có thể chuyển lại."

# Para 94: chàng trai
p[94] = "Chưa đợi Lệ Yến Trạch nói thêm lời nào, bên phía chàng trai đã trực tiếp cúp máy."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_044 updated successfully. Total paragraphs:", len(p))
