import os
import sys
import time
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))

def crawl_missing():
    czbooks_url = 'https://czbooks.net/n/sk4ei1pgock'
    slug = 'đại-ma-đầu-nhật-nhật-tưởng-sát-ngã'
    base_dir = rf"d:\Nhung\trans-tool\novel_projects\{slug}\chapters"
    chunk_sz = 20

    print("Fetching series chapters list from CZBooks...")
    res = fetch_series_chapters(czbooks_url)
    chapters = res['chapters']
    print(f"Total series chapters: {len(chapters)}")

    missing = []
    for i, ch in enumerate(chapters, start=1):
        ch_id = f"ch_{i:03d}"
        ch_path = os.path.join(base_dir, ch_id)
        source_path = os.path.join(ch_path, 'source.md')
        if not os.path.exists(source_path):
            missing.append({
                'index': i,
                'id': ch_id,
                'title': ch.get('title', f"第{i}頁"),
                'url': ch.get('url', ''),
                'path': ch_path
            })

    print(f"Found {len(missing)} missing chapters to crawl:")
    for m in missing:
        print(f"  - {m['id']}: {m['title']} -> {m['url']}")

    if not missing:
        print("No missing chapters found!")
        return

    success_cnt = 0
    for idx, item in enumerate(missing, 1):
        ch_id = item['id']
        ch_index = item['index']
        ch_url = item['url']
        ch_path = item['path']

        print(f"\n[{idx}/{len(missing)}] Crawling {ch_id} ({item['title']})...")
        try:
            c_res = crawl_chapter(ch_url)
            clean_title = c_res.get('title') or item['title']
            title_str = f"Chương {ch_index}: {clean_title}"
            raw_text = c_res.get('full_text', '')
            paras = [p.strip() for p in raw_text.split('\n') if p.strip()]

            if not paras:
                raise ValueError("No paragraphs extracted!")

            chunks_dir = os.path.join(ch_path, 'chunks')
            os.makedirs(chunks_dir, exist_ok=True)

            n_chunks = (len(paras) + chunk_sz - 1) // chunk_sz

            # 1. Write source.md
            source_md = f"---\ntitle: {title_str}\n---\n\n{raw_text}"
            with open(os.path.join(ch_path, 'source.md'), 'w', encoding='utf-8') as f:
                f.write(source_md)

            # 2. Write chunk files
            for ci in range(n_chunks):
                s, e = ci * chunk_sz, (ci + 1) * chunk_sz
                chunk_text = '\n'.join(paras[s:e])
                with open(os.path.join(chunks_dir, f"chunk_{ci+1:03d}.md"), 'w', encoding='utf-8') as f:
                    f.write(f"---\ntitle: {title_str} — Chunk {ci+1}/{n_chunks}\n---\n\n{chunk_text}")

            # 3. Write meta.json
            import json
            meta = {
                'chapter_id': ch_id,
                'title': title_str,
                'imported_at': now_gmt7().isoformat(),
                'n_paragraphs': len(paras),
                'n_chunks': n_chunks,
                'chunk_size': chunk_sz,
            }
            with open(os.path.join(ch_path, 'meta.json'), 'w', encoding='utf-8') as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)

            print(f"  -> Successfully saved {ch_id}: {len(paras)} paragraphs, {n_chunks} chunks.")
            success_cnt += 1
            # Brief pause to be respectful to the host
            time.sleep(1)

        except Exception as e:
            print(f"  -> ERROR crawling {ch_id}: {e}")

    print(f"\n==========================================")
    print(f"Finished crawling: {success_cnt}/{len(missing)} successfully imported.")

if __name__ == '__main__':
    crawl_missing()
