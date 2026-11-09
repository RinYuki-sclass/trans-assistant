import json
import os
from datetime import datetime, timezone, timedelta

GMT7 = timezone(timedelta(hours=7))
P = 'd:/Nhung/trans-tool/novel_projects/cường-chế-ái-hoàn-tựu-hồi-đáng-thiểm-cẩu-công-bị-đào-không-liễu'
idx_path = os.path.join(P, 'chapters_index.json')
toc_path = os.path.join(P, 'TOC.md')
timeline_path = os.path.join(P, 'memory', 'timeline.json')

with open(idx_path, 'r', encoding='utf-8') as f:
    idx_data = json.load(f)

completed_ids = []
for ch in idx_data.get('chapters', []):
    cid = ch['chapter_id']
    meta_path = os.path.join(P, 'chapters', cid, 'meta.json')
    trans_path = os.path.join(P, 'chapters', cid, 'translation.md')
    if os.path.exists(meta_path) and os.path.exists(trans_path):
        with open(meta_path, 'r', encoding='utf-8') as mf:
            meta = json.load(mf)
        if meta.get('qc_approved'):
            ch['status'] = 'completed'
            ch['has_translation'] = True
            ch['qc_score'] = meta.get('score', 98)
            ch['updated_at'] = datetime.now(GMT7).isoformat()
            completed_ids.append(cid)

with open(idx_path, 'w', encoding='utf-8') as f:
    json.dump(idx_data, f, ensure_ascii=False, indent=2)

# Update TOC.md
with open(toc_path, 'r', encoding='utf-8') as f:
    toc_lines = f.readlines()

new_toc_lines = []
for line in toc_lines:
    for cid in completed_ids:
        if f"`{cid}`" in line and "📥 Raw Ready" in line:
            line = line.replace("📥 Raw Ready", "✅ Hoàn thành")
    new_toc_lines.append(line)

with open(toc_path, 'w', encoding='utf-8') as f:
    f.writelines(new_toc_lines)

# Update timeline.json
if os.path.exists(timeline_path):
    with open(timeline_path, 'r', encoding='utf-8') as f:
        timeline = json.load(f)
    
    existing_events = {e.get('chapter') for e in timeline}
    new_events = [
        {
            "event_id": "evt_ch001",
            "chapter": "ch_001",
            "title": "Hôn lễ 4A1O & Hoa Y Lâu bị chuốc mê",
            "summary": "Hoa Y Lâu mừng rỡ vì thoát vai liếm cẩu sau khi hôn lễ của Thời Gia Hy kết thúc, nhưng vừa ra ngoài đã bị Thẩm Kinh Dạng dùng tin tức tố Whisky và chuốc mê.",
            "timestamp": datetime.now(GMT7).isoformat()
        },
        {
            "event_id": "evt_ch002",
            "chapter": "ch_002",
            "title": "Lần hồi quy đầu tiên",
            "summary": "Hoa Y Lâu tỉnh dậy nhận ra thời gian quay ngược về 1 ngày trước đám cưới. Tưởng rằng chỉ cần tham dự lại là xong nhưng sau đám cưới lại tiếp tục bị bắt cóc.",
            "timestamp": datetime.now(GMT7).isoformat()
        },
        {
            "event_id": "evt_ch003",
            "chapter": "ch_003",
            "title": "Bắt quả tang tên biến thái",
            "summary": "Hoa Y Lâu kiên quyết không ngất, bắt quả tang Thẩm Kinh Dạng đang cầm đồ của mình hít hà say mê. Hai người giằng co nảy lửa.",
            "timestamp": datetime.now(GMT7).isoformat()
        }
    ]
    for ne in new_events:
        if ne['chapter'] not in existing_events:
            timeline.append(ne)
            
    with open(timeline_path, 'w', encoding='utf-8') as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

print(f"Synced {len(completed_ids)} completed chapters: {completed_ids}")
