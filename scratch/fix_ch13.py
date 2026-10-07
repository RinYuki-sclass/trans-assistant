import sys, os, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')
from scratch.check_all_qc import parse_md
from scratch.process_single_chapter import generate_qa_and_qc

cid = 'ch_013'
cdir = r'd:\Nhung\RIDI\trans-assistant\novel_projects\phản-diện-đổi-ý-cầm-kịch-bản-yêu-đương\chapters\ch_013'
s_paras = parse_md(os.path.join(cdir, 'source.md'))
t_paras = parse_md(os.path.join(cdir, 'translation.md'))

fixed_tail = [
    'Thư Ninh Ninh nói xong liền không chút nghi ngờ quay người trở về, vừa đi vừa mắng Tần Diễm trêu chọc cô ta.',
    'Bạch Huân vốn dĩ cũng định đi theo cô ta về.',
    'Anh nghĩ bụng, Tần Diễm bên kia không đợi được người chắc sẽ tự mình đến thôi.',
    'Nhưng đột nhiên, anh nghe thấy tiếng Tần Diễm kêu lên kinh hãi từ không xa truyền đến.',
    'Chuyện gì vậy? Trong lòng Bạch Huân đột nhiên dâng lên một dự cảm chẳng lành, anh vội vàng sải bước chạy về phía Tần Diễm.',
    'Dưới ánh trăng, bóng dáng mờ ảo của Tần Diễm đang chao đảo ở rìa sườn đồi, vô cùng nguy hiểm.',
    '“Tần Diễm!” Bạch Huân gọi cậu.',
    'Tần Diễm nghe thấy tiếng anh, nhất thời không kìm được, hét lớn: “Vãi, Bạch Huân, mau, mau cứu tôi, có rắn… Thôi, cậu đừng qua đây!”',
    'Nhìn thấy Tần Diễm không ngừng lùi lại, gót chân cậu chỉ còn cách khoảng không nửa bước chân——',
    'Vào giây phút Tần Diễm cả người ngã ngửa về phía sau, Bạch Huân thầm mắng một tiếng, phi thân lao về phía cậu.'
]

new_t_paras = t_paras[:80] + fixed_tail
print(f'New len: {len(new_t_paras)}, Source len: {len(s_paras)}')
assert len(new_t_paras) == len(s_paras)

# Write translation.md
title = 'Chương 13: Ngoài ý muốn'
trans_path = os.path.join(cdir, 'translation.md')
content = f'---\ntitle: {title}\n---\n\n' + '\n\n'.join(new_t_paras) + '\n'
with open(trans_path, 'w', encoding='utf-8') as f:
    f.write(content)

qa_c, qc_c, meta_d = generate_qa_and_qc(cid, title, s_paras, new_t_paras)
with open(os.path.join(cdir, 'qa_clarifications.md'), 'w', encoding='utf-8') as f:
    f.write(qa_c)
with open(os.path.join(cdir, 'qc_report.md'), 'w', encoding='utf-8') as f:
    f.write(qc_c)
with open(os.path.join(cdir, 'meta.json'), 'w', encoding='utf-8') as f:
    json.dump(meta_d, f, ensure_ascii=False, indent=2)

print('Updated ch_013 successfully!')
