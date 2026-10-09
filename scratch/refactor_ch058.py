import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_058/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P17
paras[17] = paras[17].replace('Cậu ta đúng là có tầm nhìn', 'Cậu đúng là có tầm nhìn')

# P21
paras[21] = paras[21].replace('Anh chẳng những không nghe lời hắn', 'Cậu chẳng những không nghe lời hắn')

# P32
paras[32] = paras[32].replace('cả người anh bốc ra mùi tiền', 'cả người cậu bốc ra mùi tiền')

# P46
paras[46] = paras[46].replace('bị anh vứt thẳng vào thùng rác từ lâu, kết quả bây giờ thời gian quay ngược trở lại, nó lại quay về túi áo anh.', 'bị cậu vứt thẳng vào thùng rác từ lâu, kết quả bây giờ thời gian quay ngược trở lại, nó lại quay về túi áo cậu.')

# P48
paras[48] = paras[48].replace('Thế nhưng anh cũng không phải bực bội', 'Thế nhưng cậu cũng không phải bực bội')

# P55
paras[55] = paras[55].replace('lúc hắn lên tầng thay quần áo, người trợ lý vô cùng chu đáo đã mang bản sơ yếu lý lịch của Sở Tư Thừa đến trước mặt hắn.', 'lúc anh lên tầng thay quần áo, người trợ lý vô cùng chu đáo đã mang bản sơ yếu lý lịch của Sở Tư Thừa đến trước mặt anh.')

# P56
paras[56] = paras[56].replace('cứ ngỡ cậu ta chỉ là', 'cứ ngỡ cậu ấy chỉ là')

# P63, P65, P67, P69, P71
paras[63] = paras[63].replace('cho hắn nghe giải khuây.', 'cho anh nghe giải khuây.')
paras[65] = paras[65].replace('trong đầu hắn chẳng biết', 'trong đầu anh chẳng biết')
paras[67] = paras[67].replace('Hắn thậm chí còn chẳng rõ', 'Anh thậm chí còn chẳng rõ')
paras[69] = paras[69].replace('Huống hồ…… hắn cũng không muốn rút lại.', 'Huống hồ…… anh cũng không muốn rút lại.')
paras[71] = paras[71].replace('“Lên không?” Hắn lại hỏi', '“Lên không?” Anh lại hỏi')

# P89, P90
paras[89] = paras[89].replace('cậu ta có cho thêm', 'cậu có cho thêm')
paras[89] = paras[89].replace('cậu ta còn chẳng dám', 'cậu còn chẳng dám')
paras[90] = paras[90].replace('Cậu ta muốn biết', 'Cậu muốn biết')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_058 successfully!')
