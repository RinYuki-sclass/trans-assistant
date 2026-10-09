import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_056/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P8
paras[8] = paras[8].replace('tổng không thể rảnh rỗi không có việc gì làm', 'chẳng lẽ lại rảnh rỗi không có việc gì làm')

# P30
paras[30] = paras[30].replace('anh đột nhiên nghĩ đến việc Thẩm Từ cũng là vì muốn tốt cho anh nên mới đưa Chu Lạc Lạc đi', 'cậu đột nhiên nghĩ đến việc Thẩm Từ cũng là vì muốn tốt cho cậu nên mới đưa Chu Lạc Lạc đi')

# P33
paras[33] = paras[33].replace('ghép cho anh một cái', 'ghép cho cậu một cái')

# P45
paras[45] = paras[45].replace('quyến luyến không nỡ xa anh,', 'quyến luyến không nỡ xa cậu,')

# P54
paras[54] = paras[54].replace('đi tranh sủng vì anh ta chắc?', 'đi tranh sủng vì hắn chắc?')

# P57, P58
paras[57] = paras[57].replace('Kịch xem đã đủ lâu rồi, anh cũng nên', 'Kịch xem đã đủ lâu rồi, cậu cũng nên')
paras[58] = paras[58].replace('Chỉ là, anh muốn rời đi, nhưng diễn viên vẫn còn nấn ná trên sân khấu lại không cam tâm để anh đi như vậy.', 'Chỉ là, cậu muốn rời đi, nhưng diễn viên vẫn còn nấn ná trên sân khấu lại không cam tâm để cậu đi như vậy.')

# P60, P62
paras[60] = paras[60].replace('muốn nhảy xổ vào bóp cổ anh:', 'muốn nhảy xổ vào bóp cổ cậu:')
paras[62] = paras[62].replace('ngay khoảnh khắc đầu ngón tay sắp chạm vào anh,', 'ngay khoảnh khắc đầu ngón tay sắp chạm vào cậu,')

# P77
paras[77] = paras[77].replace('việc anh vẫn còn yêu hắn tha thiết.', 'việc cậu vẫn còn yêu hắn tha thiết.')

# P81
paras[81] = paras[81].replace('anh không những không bỏ chạy, mà thậm chí còn cất bước đi thẳng về phía người đàn ông.', 'cậu không những không bỏ chạy, mà thậm chí còn cất bước đi thẳng về phía hắn.')

# P84, P86, P87
paras[84] = paras[84].replace('anh bước tới trước mặt người đàn ông', 'cậu bước tới trước mặt người đàn ông')
paras[86] = paras[86].replace('thì anh cũng không tiện giải trình.', 'thì cậu cũng không tiện giải trình.')
paras[87] = paras[87].replace('Thế nhưng, anh nói:', 'Thế nhưng, cậu nói:')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_056 successfully!')
