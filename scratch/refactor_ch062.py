import os

p_trans = r'novel_projects/khi-đại-lão-phản-diện-sắm-vai-nhân-vật-chính-kho/chapters/ch_062/translation.md'
with open(p_trans, 'r', encoding='utf-8') as f:
    paras = f.read().split('\n\n')

# P62, P65, P66, P69
paras[62] = paras[62].replace('làm nhiệm vụ anh cũng từng', 'làm nhiệm vụ cậu cũng từng')
paras[65] = paras[65].replace('thế nhưng anh tổng không thể vì', 'thế nhưng cậu chẳng lẽ lại vì')
paras[66] = paras[66].replace('cho dù sau khi anh đi thật sự bị tức giận đến ngã bệnh, thì người nên cảm thấy cắn rứt áy náy cũng tuyệt đối không phải là anh,', 'cho dù sau khi cậu đi thật sự bị tức giận đến ngã bệnh, thì người nên cảm thấy cắn rứt áy náy cũng tuyệt đối không phải là cậu,')
paras[69] = paras[69].replace('quan sát anh thấy vậy', 'quan sát cậu thấy vậy')

new_content = '\n\n'.join(paras)
with open(p_trans, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated ch_062 successfully!')
