import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_042\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_042\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 104, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 1: Lệ Án Trạch -> Lệ Yến Trạch
p[1] = "Chu Lạc Lạc, người trước đó nói ra những lời kia chỉ nhằm khiến Lệ Yến Trạch thêm phần giận dữ: \"???\""

# Para 2: Cậu ta -> Gã
p[2] = "Gã chỉ tùy tiện nói thế thôi, ai ngờ đám người này lại tin là thật cơ chứ!"

# Para 3: Lệ Án Trạch -> Lệ Yến Trạch
p[3] = "Thấy ngón tay đang bám trên xe lăn của Lệ Yến Trạch hơi nới lỏng, Chu Lạc Lạc vội vàng lên tiếng cứu vãn:"

# Para 10: Lệ Án Trạch -> Lệ Yến Trạch
p[10] = "Ánh mắt Thẩm Từ tối sầm lại, Chu Lạc Lạc đang tự tán thưởng sự thông minh của chính mình khẽ nhếch môi, còn Lệ Yến Trạch thì nhìn chằm chằm vào căn phòng phía sau Thẩm Từ."

# Para 18: Chu Lạc Lạc -> gã
p[18] = "Đồng tử của Chu Lạc Lạc run rẩy vì không thể tin nổi, chân phải gã theo bản năng bước lên phía trước, muốn xông vào phòng để lôi chàng trai mà chính mắt gã đã thấy uống thuốc kia ra ngoài."

# Para 19: Chu Lạc Lạc -> gã
p[19] = "Thế nhưng gã lại bị một ánh mắt của Thẩm Từ đang chắn trước cửa đóng đinh tại chỗ."

# Para 46: Sở Tư Thừa thoại với Thẩm Từ: "Anh cũng thấy..."
p[46] = "“Anh cũng thấy bọn họ khá ngốc đúng không.”"

# Para 49: Sở Tư Thừa -> cậu
p[49] = "Chàng trai cười càng rạng rỡ hơn, chiếc điện thoại màu bạc trắng bị cậu xem như món đồ chơi bình thường, tung lên rồi lại thả xuống."

# Para 50: Thẩm Từ lặng lẽ nhìn cậu
p[50] = "Thẩm Từ lặng lẽ nhìn cậu."

# Para 62: Sở Tư Thừa -> cậu
p[62] = "Sở Tư Thừa thừa nhận vô cùng sảng khoái, nhưng sau khi thừa nhận, cậu lại mỉm cười nhẹ với Thẩm Từ,"

# Para 65: Sở Tư Thừa -> cậu
p[65] = "Sở Tư Thừa nhìn Thẩm Từ đang từng bước tiến đến trước mặt mình, lạnh lùng bóp chặt cổ cậu, cậu khẽ cúi đầu, trong mắt không hề thấy một tia hoảng loạn vì thiếu dưỡng khí, ngược lại nụ cười còn thêm phần trương dương và tùy ý."

# Para 66: Sở Tư Thừa -> cậu
p[66] = "Cậu nói: “Nể tình tôi... chúng ta vừa rồi chơi đùa vui vẻ, tôi có thể giảm giá cho anh...”"

# Para 68: Sở Tư Thừa -> cậu
p[68] = "Điều cậu thực sự muốn nói là chính cậu đã chơi đùa rất vui vẻ..."

# Para 70: Sở Tư Thừa -> cậu
p[70] = "Một lời tự tiến cử gần như trần trụi, tựa hồ không có chút tự trọng nào, nhưng thần thái của cậu lại đầy vẻ nghiền ngẫm, đến mức lời nói “giảm giá” như bán rẻ kia lọt vào tai người khác lại giống như một câu bố thí cao cao tại thượng."

# Para 72: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[72] = "Thẩm Từ không nói một lời, chỉ im lặng xem xét chàng trai đột nhiên xuất hiện bên cạnh mình này, từ lớp da thịt cho đến linh hồn, anh cố gắng xuyên qua nụ cười đầy ẩn ý của chàng trai để dò xét ý đồ thực sự của đối phương, làm rõ xem rốt cuộc cậu muốn có được thứ gì từ trên người anh, giống như mỗi một kẻ từng tiếp cận anh trước đây."

# Para 73: Thẩm Từ -> anh
p[73] = "Nhưng đáng tiếc là, anh chẳng nhìn thấy gì cả."

# Para 74: Thẩm Từ -> anh
p[74] = "Trong đôi mắt của chàng trai đang hào phóng để mặc cho anh đánh giá kia không hề có một chút dục vọng trần tục nào, bất kể là tiền bạc, hay là tình dục..."

# Para 75: Sở Tư Thừa -> cậu, Thẩm Từ -> anh
p[75] = "Làn da của cậu vẫn nóng bỏng như cũ, yết hầu không ngừng trượt lên xuống cũng đang âm thầm nói lên sự khô nóng bên trong cơ thể cậu lúc này, nếu đổi lại là người khác, thậm chí là chính Thẩm Từ của nửa giờ trước, dưới dược hiệu mãnh liệt như vậy đều sẽ đánh mất lý trí."

# Para 77: Sở Tư Thừa -> cậu
p[77] = "Cậu thậm chí còn có thời gian để dự đoán hành vi của đám người Lệ Yến Trạch, mang điện thoại vào phòng tắm để chế độ im lặng từ trước."

# Para 80: Thẩm Từ -> anh
p[80] = "Nhưng vì chàng trai này đã từng giúp anh, hơn nữa còn rất tự giác không vượt quá giới hạn, nên Thẩm Từ không định truy cứu nguyên nhân đối phương xuất hiện ở nơi này."

# Para 85: Thẩm Từ -> anh, Sở Tư Thừa -> cậu
p[85] = "Anh trả lời câu hỏi trước đó của Sở Tư Thừa, ánh mắt cũng không thèm dừng lại trên người cậu thêm một phân nào nữa."

# Para 87: Sở Tư Thừa -> cậu
p[87] = "Cậu nhìn người đàn ông cúi đầu chỉnh lại dây thắt lưng áo tắm, sau đó xoay người đi về phía cửa."

# Para 89: Thẩm Từ -> anh
p[89] = "Nhưng sau một tuần, anh sẽ không quản chi phí của căn phòng này nữa, giống như chàng trai kia vậy, sẽ cùng căn phòng này bị gạch bỏ khỏi bảng kế hoạch của anh."

# Para 94: Thẩm Từ -> anh
p[94] = "Tối nay anh đã mất kiểm soát một lần rồi."

# Para 96: Thẩm Từ -> anh
p[96] = "Anh sẽ không cho phép bản thân mất kiểm soát thêm lần thứ hai."

# Para 97: Thẩm Từ -> anh
p[97] = "Chiếc cúc cuối cùng trên áo sơ mi trắng được cài lại, Thẩm Từ xoay người đi về phía huyền quan, khi mở cửa ra lần nữa, anh đã trở lại làm vị trưởng tử nhà họ Thẩm nghiêm nghị, luôn bình tĩnh và tự chủ."

# Para 98: Sửa lỗi Ngài Sachsen -> Thẩm tổng!
p[98] = "“Thẩm tổng!” Trợ lý đứng sau cửa cung kính nói."

# Para 100: Thẩm Từ -> anh
p[100] = "Thẩm Từ chỉnh lại đồng hồ đeo tay, như sực nhớ ra điều gì, anh bổ sung thêm một câu: \"Có điều căn phòng này không cần trả, lát nữa cậu tới quầy lễ tân một chuyến, chọn hết tất cả những dịch vụ mà trước đó tôi đã từ chối.\""

# Para 101: Sửa lỗi Ngài Sachsen -> Thẩm tổng!
p[101] = "“…… Vâng, thưa Thẩm tổng!”"

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_042 updated successfully. Total paragraphs:", len(p))
