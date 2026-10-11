import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

p = os.path.join('novel_projects', 'tra-nam-này-không-đáng-được-tẩy-trắng', 'chapters')

arcs_config = [
    (1, "ch_001", "ch_018", "这悲惨的娇贵公子", "Hào môn đô thị"),
    (2, "ch_019", "ch_030", "这悲惨的正派大侠", "Võ hiệp giang hồ"),
    (3, "ch_031", "ch_042", "这悲惨的Omega", "ABO tinh tế"),
    (4, "ch_043", "ch_057", "这悲惨的网游boss", "Toàn tức võng du"),
    (5, "ch_058", "ch_074", "这悲惨的小夫郎", "Cổ đại chủng điền ca nhi"),
    (6, "ch_075", "ch_088", "这悲惨的末世温柔小受", "Mạt thế dị năng"),
    (7, "ch_089", "ch_102", "这悲惨的富二代", "Đô thị hào môn / Giới giải trí"),
    (8, "ch_103", "ch_115", "这悲惨的真少爷", "Thật giả thiếu gia / Đô thị"),
    (9, "ch_116", "ch_127", "这悲惨的后爸", "Hiện đại hào môn dưỡng oa"),
    (10, "ch_128", "ch_142", "这悲惨的府尹公子", "Cổ đại quyền mưu triều đình"),
    (11, "ch_143", "ch_154", "这悲惨的影帝", "Giới giải trí hào môn"),
    (12, "ch_155", "ch_166", "这悲惨的修真天才", "Tu chân tiên hiệp"),
    (13, "ch_167", "ch_171", "余处幽篁兮", "Hệ thống U Hoàng phiên ngoại")
]

for num, s_ch, e_ch, arc_name, genre in arcs_config:
    # Read the first chapter of this arc
    sf = os.path.join(p, s_ch, 'source.md')
    with open(sf, 'r', encoding='utf-8') as f:
        text = f.read(5000)
    
    print(f"==================================================")
    print(f"ARC {num}: {arc_name} ({genre}) [{s_ch} -> {e_ch}]")
    print(f"==================================================")
    
    # Extract identity of original host
    m_body = re.search(r'这个身体的原身名为([^，。\n]+)', text) or re.search(r'原身名为([^，。\n]+)', text) or re.search(r'原身叫([^，。\n]+)', text)
    if m_body:
        print("  Nguyên thân:", m_body.group(1).strip())
    
    # Extract age or status if mentioned
    m_age = re.search(r'(\d+岁)', text)
    if m_age:
        print("  Tuổi tác đề cập:", m_age.group(1).strip())
        
    # Search for first appearance of characters
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for l in lines[:25]:
        if any(k in l for k in ['原剧情', '渣攻', '渣受', '老公', '老攻', '老翟', '翟致', '先生', '少爷']):
            print("  -", l[:100])
    print()
