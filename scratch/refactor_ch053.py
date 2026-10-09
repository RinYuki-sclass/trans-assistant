import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_053/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P1
paras[1] = paras[1].replace('sau khi nghe câu này của anh,', 'sau khi nghe câu này của cậu,')

# P4, P5, P7
paras[4] = paras[4].replace('Cậu ta còn tưởng', 'Cậu còn tưởng')
paras[5] = paras[5].replace('bên cạnh cậu ta cũng', 'bên cạnh cậu cũng')
paras[7] = paras[7].replace('anh thấy cậu ta xin lỗi', 'anh thấy gã xin lỗi')

# P41
paras[41] = paras[41].replace('anh vẫn có chút tò mò:', 'cậu vẫn có chút tò mò:')

# P45
paras[45] = paras[45].replace('tiếng lòng của cậu ta nhiều lời quá.', 'tiếng lòng của gã nhiều lời quá.')

# P48
paras[48] = paras[48].replace('người hắn gặp qua thì nhiều vô kể.', 'người anh gặp qua thì nhiều vô kể.')
paras[48] = paras[48].replace('Chu Lạc Lạc hắn chỉ cần', 'Chu Lạc Lạc anh chỉ cần')

# P53
paras[53] = paras[53].replace('sau đó anh lại thong thả buông lời:', 'sau đó cậu lại thong thả buông lời:')

# P57
paras[57] = paras[57].replace('lời mời mọc mập mờ của anh,', 'lời mời mọc mập mờ của cậu,')
paras[57] = paras[57].replace('Trông hắn như thể sau khi tan làm', 'Trông anh như thể sau khi tan làm')

# P60
paras[60] = paras[60].replace('chưa đợi anh tiến hành', 'chưa đợi cậu tiến hành')

# P68
paras[68] = paras[68].replace('Anh bất giác tiến lại gần', 'Cậu bất giác tiến lại gần')
paras[68] = paras[68].replace('Thẩm Từ giải thích với anh,', 'Thẩm Từ giải thích với cậu,')
paras[68] = paras[68].replace('người bạn của hắn đã báo cáo', 'người bạn của anh đã báo cáo')

# P70, P71
paras[70] = paras[70].replace('là vì hắn nửa đường đã được', 'là vì anh nửa đường đã được')
paras[71] = paras[71].replace('Bằng không anh thật sự nghĩ không ra', 'Bằng không cậu thật sự nghĩ không ra')

# P78, P80
paras[78] = paras[78].replace('chính là bản thân anh.', 'chính là bản thân cậu.')
paras[80] = paras[80].replace('Nhiệm vụ của anh còn làm nữa hay thôi?', 'Nhiệm vụ của cậu còn làm nữa hay thôi?')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_053 successfully!')
