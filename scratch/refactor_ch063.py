import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_063/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P2, P3
paras[2] = paras[2].replace('muốn giữ anh ở lại, anh chỉ hít thở', 'muốn giữ cậu ở lại, cậu chỉ hít thở')
paras[3] = paras[3].replace('giục anh mau cút đi, anh trái lại', 'giục cậu mau cút đi, cậu trái lại')

# P13, P14
paras[13] = paras[13].replace('vì sao anh lại làm như vậy!', 'vì sao cậu lại làm như vậy!')
paras[14] = paras[14].replace('anh dựa vào cái gì mà đối xử với hắn', 'cậu dựa vào cái gì mà đối xử với hắn')

# P16
paras[16] = paras[16].replace('ban nãy của anh.', 'ban nãy của cậu.')

# P18, P20
paras[18] = paras[18].replace('Đương nhiên, hắn không phải là', 'Đương nhiên, anh không phải là')
paras[20] = paras[20].replace('Chỉ là hắn không thể ngờ', 'Chỉ là anh không thể ngờ')

# P30, P31, P36
paras[30] = paras[30].replace('đã khiến hắn có chút mệt mỏi', 'đã khiến anh có chút mệt mỏi')
paras[31] = paras[31].replace('thời điểm này hắn vẫn chưa', 'thời điểm này anh vẫn chưa')
paras[36] = paras[36].replace('đã khiến hắn liên tiếp phá vỡ hàng loạt quy tắc của bản thân, nếu hắn thật sự từng gặp đối phương ở một nơi nào đó, thì hắn tuyệt đối không thể nào chẳng có chút ấn tượng nào.', 'đã khiến anh liên tiếp phá vỡ hàng loạt quy tắc của bản thân, nếu anh thật sự từng gặp đối phương ở một nơi nào đó, thì anh tuyệt đối không thể nào chẳng có chút ấn tượng nào.')

# P46, P48, P51, P52
paras[46] = paras[46].replace('mỗi khi hắn đang suy nghĩ', 'mỗi khi anh đang suy nghĩ')
paras[48] = paras[48].replace('nhỏ hơn hắn vài tuổi,', 'nhỏ hơn anh vài tuổi,')
paras[51] = paras[51].replace('hắn đột nhiên cảm thấy,', 'anh đột nhiên cảm thấy,')
paras[52] = paras[52].replace('ngay cả chính hắn cũng không', 'ngay cả chính anh cũng không')

# P55, P56
paras[55] = paras[55].replace('lông mày của anh sau khi hắn nói xong', 'lông mày của cậu sau khi anh nói xong')
paras[56] = paras[56].replace('ban nãy của hắn nghe qua', 'ban nãy của anh nghe qua')

# P63, P64
paras[63] = paras[63].replace('suốt ba năm qua hắn và Lệ Yến Trạch', 'suốt ba năm qua anh và Lệ Yến Trạch')
paras[64] = paras[64].replace('cậu và hắn tuyệt đối không thể nào', 'cậu và anh tuyệt đối không thể nào')

# P70
paras[70] = paras[70].replace('quá gần với hắn, gần đến mức hắn có thể', 'quá gần với anh, gần đến mức anh có thể')

# P80, P81
paras[80] = paras[80].replace('bên cạnh gò má hắn.', 'bên cạnh gò má anh.')
paras[81] = paras[81].replace('Đầu ngón tay anh có chút lành lạnh,', 'Đầu ngón tay cậu có chút lành lạnh,')

# P84, P85, P87
paras[84] = paras[84].replace('hắn của ngày hôm nay lại đặc biệt', 'anh của ngày hôm nay lại đặc biệt')
paras[85] = paras[85].replace('Hắn nghe thấy chàng trai', 'Anh nghe thấy chàng trai')
paras[85] = paras[85].replace('trên da thịt của hắn,', 'trên da thịt của anh,')
paras[87] = paras[87].replace('Là đang sợ anh sao?', 'Là đang sợ cậu sao?')

# P90, P91, P94, P95, P96, P98, P100
paras[90] = paras[90].replace('đại não của hắn lại vẫn', 'đại não của anh lại vẫn')
paras[91] = paras[91].replace('Hắn hiểu rất rõ bản thân không phải đang sợ hãi chàng trai, cũng không phải đang sợ hãi những chuyện tiếp theo, hắn chỉ là có chút sợ hãi——', 'Anh hiểu rất rõ bản thân không phải đang sợ hãi chàng trai, cũng không phải đang sợ hãi những chuyện tiếp theo, anh chỉ là có chút sợ hãi——')
paras[94] = paras[94].replace('Hắn vẫn luôn sống trong', 'Anh vẫn luôn sống trong')
paras[95] = paras[95].replace('Hắn đã mất kiểm soát', 'Anh đã mất kiểm soát')
paras[96] = paras[96].replace('hắn căn bản không biết', 'anh căn bản không biết')
paras[98] = paras[98].replace('Cơ thể hắn sẽ theo', 'Cơ thể anh sẽ theo')
paras[100] = paras[100].replace('hắn không biết bản thân có nên tiếp tục', 'anh không biết bản thân có nên tiếp tục')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_063 successfully!')
