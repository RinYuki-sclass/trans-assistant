import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_057/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P2
paras[2] = paras[2].replace('anh liền dứt khoát mở miệng:', 'cậu liền dứt khoát mở miệng:')

# P7
paras[7] = paras[7].replace('anh làm sao có thể', 'cậu làm sao có thể')

# P9
paras[9] = paras[9].replace('Anh thật sự muốn giết hắn.', 'Cậu thật sự muốn giết hắn.')

# P13
paras[13] = paras[13].replace('bản thân anh cũng không', 'bản thân cậu cũng không')

# P19
paras[19] = paras[19].replace('【Ký chủ! Anh nghĩ đến nhân vật phản diện đi! Anh vẫn còn chưa đi ăn cơm với hắn mà! Lẽ nào anh không muốn gặp lại hắn một lần nữa sao?!】', '【Ký chủ! Cậu nghĩ đến nhân vật phản diện đi! Cậu vẫn còn chưa đi ăn cơm với anh ấy mà! Lẽ nào cậu không muốn gặp lại anh ấy một lần nữa sao?!】')

# P34
paras[34] = paras[34].replace('anh chỉ rũ mắt', 'cậu chỉ rũ mắt')

# P41
paras[41] = paras[41].replace('bên tai anh lại vang lên', 'bên tai cậu lại vang lên')

# P44
paras[44] = paras[44].replace('đưa lưng về phía anh,', 'đưa lưng về phía cậu,')

# P56
paras[56] = paras[56].replace('chẳng thèm liếc nhìn hắn lấy một cái', 'chẳng thèm liếc nhìn gã lấy một cái')

# P67
paras[67] = paras[67].replace('Chính hắn đã tiếp thêm dũng khí', 'Chính anh đã tiếp thêm dũng khí')

# P90
paras[90] = paras[90].replace('Tống Lạc An cậu ta chẳng phải', 'Tống Lạc An chẳng phải')

# P99
paras[99] = paras[99].replace('bị anh lắng nghe', 'bị cậu lắng nghe')

# P102
paras[102] = paras[102].replace('anh cũng đánh giá cao', 'cậu cũng đánh giá cao')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_057 successfully!')
