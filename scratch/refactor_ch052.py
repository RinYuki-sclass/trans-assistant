import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_052/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P3, P4, P6
paras[3] = paras[3].replace('Tại sao hắn phải vì', 'Tại sao anh phải vì')
paras[4] = paras[4].replace('rời xa hắn.', 'rời xa anh.')
paras[6] = paras[6].replace('cậu ta chỉ là một tình nhân mà thôi, không muốn cung phụng cậu ta', 'cậu ấy chỉ là một tình nhân mà thôi, không muốn cung phụng cậu ấy')

# P15
paras[15] = paras[15].replace('ngay lúc cậu ta vừa khóc vừa cầu xin', 'ngay lúc gã vừa khóc vừa cầu xin')
paras[15] = paras[15].replace('giọng của cậu ta,', 'giọng của gã,')

# P25, P26
paras[25] = paras[25].replace('trách móc anh ta đã dồn ép', 'trách móc cậu đã dồn ép')
paras[26] = paras[26].replace('khiến cậu ta trở nên kiêu ngạo', 'khiến cậu trở nên kiêu ngạo')

# P30, P31
paras[30] = paras[30].replace('“Ngài Tống, theo tôi thấy, ngài nên tha thứ cho cậu Chu đi ạ,”', '“Cậu Tống, theo tôi thấy, cậu nên tha thứ cho thiếu gia Chu đi ạ,”')
paras[31] = paras[31].replace('“Cậu ấy cũng đâu có làm gì sai…”', '“Cậu Chu cũng đâu có làm gì sai…”')

# P33, P37, P38
paras[33] = paras[33].replace('cậu ta đã bảo mà', 'gã đã bảo mà')
paras[33] = paras[33].replace('tiếng lòng của cậu ta', 'tiếng lòng của gã')
paras[33] = paras[33].replace('về phía cậu ta cả.', 'về phía gã cả.')

paras[37] = paras[37].replace('tiếng lòng của cậu ta,', 'tiếng lòng của gã,')
paras[38] = paras[38].replace('Cậu ta muốn đối phương', 'Gã muốn đối phương')
paras[38] = paras[38].replace('cậu ta ở kiếp trước!', 'gã ở kiếp trước!')

# P40, P41
paras[40] = paras[40].replace('khiến cậu ta không ngờ tới là', 'khiến gã không ngờ tới là')
paras[40] = paras[40].replace('tiếng lòng của cậu ta,', 'tiếng lòng của gã,')
paras[41] = paras[41].replace('như cậu ta đã đinh ninh,', 'như gã đã đinh ninh,')

# P48
paras[48] = paras[48].replace('hành động không báo trước của anh', 'hành động không báo trước của cậu')

# P55, P56, P57, P58, P60, P61
paras[55] = paras[55].replace('trên mặt anh cũng không hề lộ ra vẻ hoảng loạn, thậm chí còn mỉm cười đầy khiêu khích với gã,', 'trên mặt cậu cũng không hề lộ ra vẻ hoảng loạn, thậm chí còn mỉm cười đầy khiêu khích với hắn,')
paras[56] = paras[56].replace('Chẳng phải cậu ta nói tôi hắt nước vào người cậu ta sao', 'Chẳng phải gã nói tôi hắt nước vào người gã sao')
paras[57] = paras[57].replace('hắt nước bẩn lên người anh, vậy thì anh đành', 'hắt nước bẩn lên người cậu, vậy thì cậu đành')
paras[58] = paras[58].replace('Anh như vậy gọi là điên sao?', 'Cậu như vậy gọi là điên sao?')
paras[60] = paras[60].replace('phía sau gã,', 'phía sau hắn,')
paras[61] = paras[61].replace('anh Chu,', 'cậu Chu,')

# P66, P68
paras[66] = paras[66].replace('cậu ta vốn chẳng hề bị bỏng', 'gã vốn chẳng hề bị bỏng')
paras[68] = paras[68].replace('"ánh trăng sáng"', '“ánh trăng sáng”')

# P73, P74, P75
paras[73] = paras[73].replace('tạt cậu ta,', 'tạt gã,')
paras[73] = paras[73].replace('tạt cậu ta lần thứ hai.', 'tạt gã lần thứ hai.')
paras[74] = paras[74].replace('cứ thấy cậu ta một lần là tạt một lần.', 'cứ thấy gã một lần là tạt một lần.')
paras[75] = paras[75].replace('của anh chỉ là một cách chào hỏi', 'của cậu chỉ là một cách chào hỏi')

# P77, P80, P82
paras[77] = paras[77].replace('“Ông Tống, nếu ông không muốn tha thứ cho thiếu gia nhà họ Chu, ông có thể nói thẳng, có cần thiết phải ra tay làm người khác bị thương không?!”', '“Cậu Tống, nếu cậu không muốn tha thứ cho thiếu gia Chu, cậu có thể nói thẳng, có cần thiết phải ra tay làm người khác bị thương không?!”')
paras[80] = paras[80].replace('Tống tấu ở đây chính là', 'Song tấu ở đây chính là')
paras[82] = paras[82].replace('vậy thì anh sẽ cụ thể hóa tình cảnh thảm hại của đối phương. Dù sao thì tai nghe không bằng mắt thấy, giờ đây chắc chắn mọi người đều tin anh chính là', 'vậy thì cậu sẽ cụ thể hóa tình cảnh thảm hại của đối phương. Dù sao thì tai nghe không bằng mắt thấy, giờ đây chắc chắn mọi người đều tin cậu chính là')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_052 successfully!')
