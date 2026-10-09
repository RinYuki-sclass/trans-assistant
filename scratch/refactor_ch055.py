import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_055/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P2
paras[2] = paras[2].replace('Sắc mặt của anh vô cùng', 'Sắc mặt của cậu vô cùng')

# P7
paras[7] = paras[7].replace('anh không dám đảm bảo', 'cậu không dám đảm bảo')

# P11, P13
paras[11] = paras[11].replace('để dạy cho anh nhớ rõ', 'để dạy cho cậu nhớ rõ')
paras[13] = paras[13].replace('Anh cao hơn bố Tống', 'Cậu cao hơn bố Tống')

# P26, P27, P28, P29, P30
paras[26] = paras[26].replace('cậu ta đã liệu trước', 'cậu đã liệu trước')
paras[27] = paras[27].replace('công việc nên cậu ta không', 'công việc nên cậu không')
paras[28] = paras[28].replace('Anh ngay cả hai đứa em trai em gái họ Tống trước kia có thể tùy ý đòi hỏi yêu sách ở anh mà anh còn coi như không khí, thì ông già cặn bã này lấy đâu ra thể diện để cho rằng anh sẽ tiếp tục nhẫn nhục chịu đựng chứ?', 'Cậu ngay cả hai đứa em họ Tống trước kia có thể tùy ý đòi hỏi yêu sách ở cậu mà cậu còn coi như không khí, thì ông già cặn bã này lấy đâu ra thể diện để cho rằng cậu sẽ tiếp tục nhẫn nhục chịu đựng chứ?')
paras[29] = paras[29].replace('nhiều, cậu ta dứt khoát', 'nhiều, cậu dứt khoát')
paras[30] = paras[30].replace('nhìn thấy ánh mắt của cậu ta,', 'nhìn thấy ánh mắt của cậu,')

# P40
paras[40] = paras[40].replace('Càng không đáng để anh phải', 'Càng không đáng để cậu phải')

# P44, P45
paras[44] = paras[44].replace('vui vẻ theo anh.', 'vui vẻ theo cậu.')
paras[45] = paras[45].replace('ánh mắt anh nhìn hắn,', 'ánh mắt cậu nhìn hắn,')

# P54, P55, P57
paras[54] = paras[54].replace('chết ngay trước mặt anh vào lúc này, anh cũng sẽ', 'chết ngay trước mặt cậu vào lúc này, cậu cũng sẽ')
paras[55] = paras[55].replace('cuối cùng của anh rồi.', 'cuối cùng của cậu rồi.')
paras[57] = paras[57].replace('khá xa, anh phải xuất phát', 'khá xa, cậu phải xuất phát')

# P70
paras[70] = paras[70].replace('Nhưng còn anh thì sao?', 'Nhưng còn cậu thì sao?')

# P86
paras[86] = paras[86].replace('sau lưng anh.', 'sau lưng cậu.')

# P98
paras[98] = paras[98].replace('Tổng không phải thật sự là bố đẻ của hắn đấy chứ?', 'Chẳng lẽ lại là bố đẻ của hắn thật đấy chứ?')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_055 successfully!')
