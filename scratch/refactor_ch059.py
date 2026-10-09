import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_059/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# Assistant references
for idx in [3, 5, 6, 11, 14, 21, 22, 37, 40, 45, 51, 58, 59]:
    paras[idx] = paras[idx].replace('cậu ta', 'cậu')

# Thẩm Từ being called "hắn"
paras[1] = paras[1].replace('khiến hắn có thể làm ra', 'khiến anh có thể làm ra')
paras[32] = paras[32].replace('nhìn thẳng vào hắn.', 'nhìn thẳng vào anh.')
paras[38] = paras[38].replace('lợi dụng hắn, huống chi là cái kiểu coi hắn như', 'lợi dụng anh, huống chi là cái kiểu coi anh như')
paras[66] = paras[66].replace('hắn căn bản không có ý định', 'anh căn bản không có ý định')
paras[67] = paras[67].replace('Mặc dù hắn quả thực', 'Mặc dù anh quả thực')
paras[72] = paras[72].replace('mắt, hắn lại đột nhiên mở miệng:', 'mắt, anh lại đột nhiên mở miệng:')
paras[81] = paras[81].replace('ảo, hắn nhìn thấy', 'ảo, anh nhìn thấy')
paras[90] = paras[90].replace('xung quanh hắn', 'xung quanh anh')
paras[92] = paras[92].replace('yêu cầu hắn phải giữ mình trong sạch, mặt khác lại là vì hắn căn bản chẳng hề hứng thú', 'yêu cầu anh phải giữ mình trong sạch, mặt khác lại là vì anh căn bản chẳng hề hứng thú')
paras[93] = paras[93].replace('lên người hắn lúc nãy, khi hắn nhìn về phía đối phương, bởi vì khoảng cách có hơi xa một chút, hắn thậm chí còn chẳng thấy rõ diện mạo', 'lên người anh lúc nãy, khi anh nhìn về phía đối phương, bởi vì khoảng cách có hơi xa một chút, anh thậm chí còn chẳng thấy rõ diện mạo')
paras[94] = paras[94].replace('cho đến khi hắn lướt qua vai đối phương rời đi, chuẩn bị vào phòng nghỉ thay quần áo, thì bỗng nhiên ma xui quỷ khiến thế nào, hắn mới quay đầu lại', 'cho đến khi anh lướt qua vai đối phương rời đi, chuẩn bị vào phòng nghỉ thay quần áo, thì bỗng nhiên ma xui quỷ khiến thế nào, anh mới quay đầu lại')
paras[95] = paras[95].replace('đã khiến hắn bất giác', 'đã khiến anh bất giác')

# Sở Tư Thừa being called "anh"
paras[8] = paras[8].replace('quần áo trên người anh có rẻ tiền đến đâu, chiếc ba lô trong lòng anh có cũ rách nát đến mức nào', 'quần áo trên người cậu có rẻ tiền đến đâu, chiếc ba lô trong lòng cậu có cũ rách nát đến mức nào')
paras[10] = paras[10].replace('Thế nhưng anh vẫn nhận ra', 'Thế nhưng cậu vẫn nhận ra')
paras[12] = paras[12].replace('Cho nên anh đã nhìn thẳng', 'Cho nên cậu đã nhìn thẳng')
paras[18] = paras[18].replace('từ trên người anh một cảm giác', 'từ trên người cậu một cảm giác')
paras[25] = paras[25].replace('từ lúc anh bước lên xe', 'từ lúc cậu bước lên xe')
paras[51] = paras[51].replace('từ nét mặt của anh', 'từ nét mặt của cậu')
paras[63] = paras[63].replace('trước mặt anh rồi, anh còn có lý do', 'trước mặt cậu rồi, cậu còn có lý do')
paras[65] = paras[65].replace('liếc mắt nhìn anh thêm hai cái.', 'liếc mắt nhìn cậu thêm hai cái.')
paras[82] = paras[82].replace('toàn bộ mày mắt anh,', 'toàn bộ mày mắt cậu,')
paras[86] = paras[86].replace('Là cảm thấy anh đáng thương,', 'Là cảm thấy cậu đáng thương,')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_059 successfully!')
