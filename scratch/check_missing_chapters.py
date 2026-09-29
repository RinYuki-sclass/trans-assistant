import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import fetch_series_chapters

res = fetch_series_chapters('https://czbooks.net/n/sk4ei1pgock')
chapters = res['chapters']
print(f"Total CZBooks chapters: {len(chapters)}")

base_dir = r"d:\Nhung\trans-tool\novel_projects\đại-ma-đầu-nhật-nhật-tưởng-sát-ngã\chapters"

missing_chapters = []
for i, ch in enumerate(chapters, start=1):
    ch_id = f"ch_{i:03d}"
    ch_path = os.path.join(base_dir, ch_id)
    has_source = os.path.exists(os.path.join(ch_path, 'source.md'))
    has_trans = os.path.exists(os.path.join(ch_path, 'translation.md'))
    if not (has_source and has_trans):
        missing_chapters.append({
            'index': i,
            'id': ch_id,
            'title': ch.get('title', ''),
            'url': ch.get('url', ''),
            'has_source': has_source,
            'has_trans': has_trans
        })

print(f"Number of missing or incomplete chapters: {len(missing_chapters)}")
for mc in missing_chapters:
    print(f"- {mc['id']} (Trang {mc['index']}): {mc['title']} | source: {mc['has_source']} | trans: {mc['has_trans']} | URL: {mc['url']}")
