import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_045\translation.md'
src_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_045\source.md'

with open(ch_path, 'r', encoding='utf-8') as f:
    t_text = f.read().strip()
with open(src_path, 'r', encoding='utf-8') as f:
    s_text = f.read().strip()

t_paras = [p.strip() for p in t_text.split('\n\n') if p.strip()]
s_paras = [p.strip() for p in s_text.split('\n\n') if p.strip()]

assert len(t_paras) == len(s_paras) == 105, f"Length mismatch: t={len(t_paras)}, s={len(s_paras)}"

p = t_paras[:]

# Para 2: anh -> cậu
p[2] = "Chỉ mới có mấy ngày, mà cậu đã không nhận ra giọng nói của hắn rồi sao?!"

# Para 24: chim yến tước -> chim hoàng yến
p[24] = "Một con chim hoàng yến."

# Para 49: chim sẻ vàng -> chim hoàng yến
p[49] = p[49].replace("chim sẻ vàng", "chim hoàng yến")

# Para 50: chim sẻ vàng -> chim hoàng yến
p[50] = "Một con chim hoàng yến chỉ biết ngửa tay xin tiền, có tư cách gì mà tự mở lồng bay ra ngoài?!"

# Para 91: Cậu muốn anh tự đoán, hoặc là chính miệng thừa nhận.
p[91] = "Cậu muốn anh tự đoán, hoặc là chính miệng thừa nhận."

# Para 94: Thẩm Từ -> anh
p[94] = "Người tốt bụng Thẩm Từ khẽ động ngón tay, ký tên mình lên tập tài liệu vừa mở ra, mực đen thấm vào giấy trắng, rồi trong mắt anh từ từ lan ra."

# Para 97: anh ta -> anh ấy
p[97] = "“Chủ yếu là tôi không biết người mà tôi nghĩ đến có muốn tôi đặt chuyện tốt đẹp này lên đầu anh ấy hay không.”"

# Para 99: từ chối -> phủ nhận, anh ta -> anh ấy
p[99] = "“Dù sao… anh ấy đã từng phủ nhận tôi một lần rồi.”"

# Para 100: từ chối -> phủ nhận, anh ta -> anh ấy
p[100] = "“Anh nói xem, anh ấy có phủ nhận tôi lần thứ hai không?”"

# Para 102: Thẩm Từ -> anh
p[102] = "Trong suốt hơn hai mươi năm cuộc đời, những người Thẩm Từ từng gặp, không một ai dám nói chuyện với anh như vậy, họ chỉ mong ngay khi anh vừa mở lời đã dâng câu trả lời cho anh."

# Para 103: Thẩm Từ -> anh
p[103] = "Không cần anh tốn tâm tư, thậm chí không cần động não."

# Para 104: Thẩm Từ -> anh
p[104] = "Mọi người xung quanh anh đều sẽ không có hành động mập mờ về câu hỏi, thậm chí còn đẩy câu hỏi lại cho anh như chàng trai này, bởi vì trong thương trường, điều đó tương đương với việc tự tay đưa mình lên đoạn đầu đài."

new_content = '\n\n'.join(p) + '\n'
with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("ch_045 updated successfully. Total paragraphs:", len(p))
