import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_061/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P4
paras[4] = paras[4].replace('Chẳng lẽ cậu ta đã sớm', 'Chẳng lẽ cậu đã sớm')

# P27
paras[27] = paras[27].replace('việc anh đã tuyên bố bản thỏa thuận giữa hai người vô hiệu từ lâu, thì cho dù là trước lúc anh tiếp nhận nhiệm vụ', 'việc cậu đã tuyên bố bản thỏa thuận giữa hai người vô hiệu từ lâu, thì cho dù là trước lúc cậu tiếp nhận nhiệm vụ')

# P58
paras[58] = paras[58].replace('Sở Tư Thừa bật cười, anh dùng đôi mắt', 'Sở Tư Thừa bật cười, cậu dùng đôi mắt')

# P87
paras[87] = paras[87].replace('của Lệ Yến Trạch, anh tiếp tục bồi', 'của Lệ Yến Trạch, cậu tiếp tục bồi')

# P89
paras[89] = paras[89].replace('ở ngoài cổng chờ anh đó sao.', 'ở ngoài cổng chờ cậu đó sao.')

# P103, P104, P105
paras[103] = paras[103].replace('ở bên cạnh hắn mãi mãi sao?', 'ở bên cạnh anh ta mãi mãi sao?')
paras[104] = paras[104].replace('tiếp cận hắn, quyến rũ thu hút hắn', 'tiếp cận anh ta, quyến rũ thu hút anh ta')
paras[105] = paras[105].replace('“Hắn chẳng qua chỉ là', '“Anh ta chẳng qua chỉ là')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_061 successfully!')
