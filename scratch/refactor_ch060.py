import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_060/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P1, P4, P14
paras[1] = paras[1].replace('khi hắn nhìn thẳng', 'khi anh nhìn thẳng')
paras[4] = paras[4].replace('khỏi miệng hắn,', 'khỏi miệng anh,')
paras[4] = paras[4].replace('sau khi hắn gọi giật', 'sau khi anh gọi giật')
paras[14] = paras[14].replace('hắn nhìn thấy chàng trai', 'anh nhìn thấy chàng trai')

# P6
paras[6] = paras[6].replace('bằng không cậu ta thật sự', 'bằng không cậu thật sự')

# P20
paras[20] = paras[20].replace('phong thái rụt rè kiêu ngạo', 'phong thái kiêu kỳ thận trọng')

# P28
paras[28] = paras[28].replace('xem thử hắn có giống tôi', 'xem thử anh ấy có giống tôi')

# P32, P33, P36, P40, P42, P54
paras[32] = paras[32].replace('cuộc gặp gỡ lần trước anh cũng', 'cuộc gặp gỡ lần trước cậu cũng')
paras[33] = paras[33].replace('muốn cảm ơn này của anh vừa', 'muốn cảm ơn này của cậu vừa')
paras[36] = paras[36].replace('Lệ Yến Trạch, anh chỉ muốn biết', 'Lệ Yến Trạch, cậu chỉ muốn biết')
paras[40] = paras[40].replace('xoa bóp của anh đây mà.', 'xoa bóp của cậu đây mà.')
paras[42] = paras[42].replace('chiếc đầu của anh nữa.', 'chiếc đầu của cậu nữa.')
paras[54] = paras[54].replace('Suốt quá trình anh chẳng buồn', 'Suốt quá trình cậu chẳng buồn')

# P99
paras[99] = paras[99].replace('đến đây là để tìm anh gây sự', 'đến đây là để tìm hắn gây sự')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_060 successfully!')
