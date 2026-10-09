import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_051/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P1
paras[1] = paras[1].replace('Lệ Yến Trạch cũng không để anh quay lại trường học.', 'Lệ Yến Trạch cũng không để cậu quay lại trường học.')

# P24
paras[24] = paras[24].replace('Anh còn vô cùng chu đáo giúp Lệ Yến Trạch', 'Cậu còn vô cùng chu đáo giúp Lệ Yến Trạch')

# P53
paras[53] = paras[53].replace('anh chẳng cần đoán cũng biết Thẩm Từ', 'cậu chẳng cần đoán cũng biết Thẩm Từ')

# P62
paras[62] = '“Cho dù cậu ấy ở bên tôi vì tiền thì đã sao? Tôi có tiền, cậu ấy cần tiền, chẳng phải điều đó chứng minh hai chúng tôi rất xứng đôi sao.”'

# P66
paras[66] = paras[66].replace('Ánh mắt hắn thực chất chẳng gợn chút sóng gió nào', 'Ánh mắt anh thực chất chẳng gợn chút sóng gió nào')

# P74
paras[74] = paras[74].replace('giống như anh ta ở phía sau.', 'giống như cậu ở phía sau.')

# P76
paras[76] = paras[76].replace('khoảnh khắc nhìn thấy Lệ Yến Trạch, hắn đã lập tức nhận ra', 'khoảnh khắc nhìn thấy Lệ Yến Trạch, cậu đã lập tức nhận ra')

# P77
paras[77] = paras[77].replace('hắn cũng đã ít nhiều nắm được một vài thông tin về vị "ông Tống" ở phòng 3601.', 'cậu cũng đã ít nhiều nắm được một vài thông tin về vị “cậu Tống” ở phòng 3601.')

# P81
paras[81] = paras[81].replace('anh ta siết chặt túi mua sắm trong tay', 'cậu siết chặt túi mua sắm trong tay')
paras[81] = paras[81].replace('tập đoàn Shen nghiên cứu', 'Thẩm thị nghiên cứu')
paras[81] = paras[81].replace('anh ta vừa không quên tăng âm lượng:', 'cậu vừa không quên cất cao giọng:')

# P82
paras[82] = paras[82].replace('"Tổng giám đốc Shen!', '“Thẩm tổng!')
paras[82] = paras[82].replace('mua cho ông Tống,', 'mua cho cậu Tống,')
paras[82] = paras[82].replace('mong ông Tống tạm thời dùng đỡ."', 'mong cậu Tống tạm thời dùng đỡ.”')

# P84
paras[84] = paras[84].replace('Anh ta đã tìm hiểu', 'Cậu đã tìm hiểu')
paras[84] = paras[84].replace('mẹ của Tống chữa bệnh', 'mẹ Tống chữa bệnh')

# P87
paras[87] = paras[87].replace('ông chủ của anh ta,', 'ông chủ của cậu,')

# P98
paras[98] = paras[98].replace('đưa cậu ta vượt qua mấy tầng lớp giai cấp', 'đưa cậu vượt qua mấy tầng lớp giai cấp')

# P102
paras[102] = paras[102].replace('tương lai, cậu ta cũng sẽ', 'tương lai, cậu ấy cũng sẽ')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_051 successfully!')
