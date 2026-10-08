# -*- coding: utf-8 -*-
import os

# Fix ch_024
f24 = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_024\translation.md'
with open(f24, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('hình chữ “Hồi” (回)', 'hình chữ “Hồi”')
with open(f24, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix ch_028
f28 = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_028\translation.md'
with open(f28, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('từ việc莫名kỳ diệu bị đổi địa điểm', 'từ việc không hiểu sao kỳ lạ bị đổi địa điểm')
with open(f28, 'w', encoding='utf-8') as f:
    f.write(text)

# Fix ch_029
f29 = r'd:\Nhung\RIDI\trans-assistant\novel_projects\đấng-cứu-thế-trả-nợ-tình\chapters\ch_029\translation.md'
with open(f29, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('hình chữ Xuyên (川)', 'hình chữ Xuyên')
with open(f29, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated translations successfully.')
