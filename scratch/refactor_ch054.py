import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_054/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P1
paras[1] = paras[1].replace('trên người Thẩm Từ, anh mới chợt nhận ra', 'trên người Thẩm Từ, cậu mới chợt nhận ra')

# P10
paras[10] = paras[10].replace('Vậy thì anh có lẽ cần phải', 'Vậy thì cậu có lẽ cần phải')

# P13, P14
paras[13] = paras[13].replace('chê anh chưa mở màn', 'chê cậu chưa mở màn')
paras[14] = paras[14].replace('trước đó của anh rồi?', 'trước đó của cậu rồi?')

# P16
paras[16] = paras[16].replace('phản diện anh ghét gặp phải nhất,', 'phản diện cậu ghét gặp phải nhất,')

# P18
paras[18] = paras[18].replace('lúc này đây, anh lại ngửi thấy', 'lúc này đây, cậu lại ngửi thấy')

# P20
paras[20] = paras[20].replace('Bởi vì trước khi anh kiểm tra', 'Bởi vì trước khi cậu kiểm tra')

# P33
paras[33] = paras[33].replace('cậu trúc mã thanh mai', 'người bạn trúc mã thanh mai')

# P53
paras[53] = paras[53].replace('hai anh em nhà họ Tống,', 'hai đứa em nhà họ Tống,')

# P55
paras[55] = paras[55].replace('của nhân vật chính, anh đột nhiên', 'của nhân vật chính, cậu đột nhiên')

# P59
paras[59] = paras[59].replace('Nhận tiền xong anh còn có thể', 'Nhận tiền xong cậu còn có thể')

# P61, P62
paras[61] = paras[61].replace('ngay khi anh vừa nhận lương xong,', 'ngay khi cậu vừa nhận lương xong,')
paras[62] = paras[62].replace('vang lên bên tai anh:', 'vang lên bên tai cậu:')

# P73
paras[73] = paras[73].replace('hình tượng của Tống tiên sinh không?', 'hình tượng của cậu Tống không?')

# P80, P81
paras[80] = paras[80].replace('của chính mẹ Tống, anh cũng đều', 'của chính mẹ Tống, cậu cũng đều')
paras[81] = paras[81].replace('Anh đã quen sống một mình quanh năm suốt tháng, đối với tình thân vốn dĩ chẳng có mấy khái niệm, huống chi kẻ trước mắt đang cố dùng tình thân để trói buộc bắt cóc anh lại là một ông bố họ Tống mà ngay cả Tống Lạc An trong nguyên tác cũng đã quyết định từ bỏ.', 'Cậu đã quen sống một mình quanh năm suốt tháng, đối với tình thân vốn dĩ chẳng có mấy khái niệm, huống chi kẻ trước mắt đang cố dùng tình thân để trói buộc bắt cóc cậu lại là một ông bố họ Tống mà ngay cả Tống Lạc An trong nguyên tác cũng đã quyết định từ bỏ.')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_054 successfully!')
