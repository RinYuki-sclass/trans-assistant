import os

ch_path = r'd:\Nhung\trans-tool\novel_projects\khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho\chapters\ch_043\translation.md'
with open(ch_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all Tống Nhạc Minh -> Tống Lạc Minh
text = text.replace('Tống Nhạc Minh', 'Tống Lạc Minh')

# Para 37: nghe anh nói -> nghe cậu nói
text = text.replace(
    'Có điều người ở đầu dây bên kia rõ ràng cũng chẳng có ý định nghe anh nói, sau khi chất vấn tại sao Sở Tư Thừa không nghe máy xong, liền lập tức dẫn dắt chủ đề sang chuyện của chính hắn.',
    'Có điều người ở đầu dây bên kia rõ ràng cũng chẳng có ý định nghe cậu nói, sau khi chất vấn tại sao Sở Tư Thừa không nghe máy xong, liền lập tức dẫn dắt chủ đề sang chuyện của chính gã.'
)

# Para 48: Anh cảm thấy túi tiền của mình có chút eo hẹp
text = text.replace(
    'Anh cảm thấy túi tiền của mình có chút eo hẹp, còn Tống Lạc Minh ở đầu dây bên kia vừa mở miệng đã đòi một vạn tệ lại càng thấy số tiền này quá ít.',
    'Cậu cảm thấy túi tiền của mình có chút eo hẹp, còn Tống Lạc Minh ở đầu dây bên kia vừa mở miệng đã đòi một vạn tệ lại càng thấy số tiền này quá ít.'
)

# Para 65, 66, 69: Sở Tư Thừa gọi Tống Lạc Minh là "mày"
text = text.replace(
    '“Tại sao tôi phải đưa tiền cho anh?”',
    '“Tại sao tôi phải đưa tiền cho mày?”'
)
text = text.replace(
    'Sở Tư Thừa cười khẩy: “Tôi chẳng phải cha anh, cũng chẳng phải mẹ anh, dựa vào cái gì mà phải đưa tiền cho anh chứ?”',
    'Sở Tư Thừa cười khẩy: “Tôi chẳng phải cha mày, cũng chẳng phải mẹ mày, dựa vào cái gì mà phải đưa tiền cho mày chứ?”'
)
text = text.replace(
    'Sở Tư Thừa chậm rãi nói: “Có phải trước đây tôi đưa tiền cho anh nhiều quá, nên mới khiến anh quên mất mình là ai rồi không?”',
    'Sở Tư Thừa chậm rãi nói: “Có phải trước đây tôi đưa tiền cho mày nhiều quá, nên mới khiến mày quên mất mình là ai rồi không?”'
)

with open(ch_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("ch_043 refined successfully.")
