import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import crawl_chapter

base_dir = r"d:\Nhung\trans-tool\novel_projects\đại-ma-đầu-nhật-nhật-tưởng-sát-ngã\chapters"

targets = [
    ("ch_025", "Chương 25: 第25頁", "https://czbooks.net/n/sk4ei1pgock/sk2l0?chapterNumber=24"),
    ("ch_030", "Chương 30: 第30頁", "https://czbooks.net/n/sk4ei1pgock/sk2l3?chapterNumber=29")
]

for ch_id, title, url in targets:
    ch_dir = os.path.join(base_dir, ch_id)
    os.makedirs(ch_dir, exist_ok=True)
    os.makedirs(os.path.join(ch_dir, "chunks"), exist_ok=True)
    
    data = crawl_chapter(url)
    source_md = f"---\ntitle: {title}\n---\n\n" + data["full_text"]
    with open(os.path.join(ch_dir, "source.md"), "w", encoding="utf-8") as f:
        f.write(source_md)
        
    meta = {
        "chapter_id": ch_id,
        "title": title,
        "imported_at": "2026-09-26T21:56:00.000000+07:00",
        "n_paragraphs": len(data["paragraphs"]),
        "n_chunks": (len(data["paragraphs"]) + 19) // 20,
        "chunk_size": 20
    }
    with open(os.path.join(ch_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully created {ch_id} (source len: {len(data['full_text'])})")
