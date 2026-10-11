import urllib.request
import re
import html
import time
import json
import os
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'xuyên-thư-xong-tôi-giả-gay-trong-truyện-bá-tổng')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
MEMORY_DIR = os.path.join(PROJECT_DIR, 'memory')

os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
}

START_PAGE = 2
END_PAGE = 222  # inclusive

def fetch_page(idx):
    url = f'https://www.52shuku.net/chongsheng/07_b/bjVPq_{idx}.html'
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
                html_str = content.decode('utf-8', errors='ignore')

            content_m = re.search(r'<article[^>]*>(.*?)</article>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+id="text"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+class="content"[^>]*>(.*?)</div>', html_str, re.DOTALL) or \
                        re.search(r'<div[^>]+class="article-content"[^>]*>(.*?)</div>', html_str, re.DOTALL)
            
            if not content_m:
                raise ValueError("Could not find content container in page")

            raw_body = content_m.group(1)
            raw_body = re.sub(r'<div class="pagination"[^>]*>.*?</div>', '', raw_body, flags=re.DOTALL)
            raw_body = re.sub(r'<div class="read_page"[^>]*>.*?</div>', '', raw_body, flags=re.DOTALL)

            paras = [p.strip() for p in re.split(r'<p>|<br\s*/?>', raw_body) if p.strip()]
            cleaned_paras = []
            for p in paras:
                p_clean = re.sub(r'<[^>]+>', '', p)
                p_clean = html.unescape(p_clean).strip()
                p_clean = re.sub(r'^[　\s]+', '', p_clean)
                if not p_clean:
                    continue
                if any(ad in p_clean for ad in ['52shuku', '52书库', '版权', '请收藏', '传送门：', '目录 上一页']):
                    continue
                cleaned_paras.append(p_clean)

            return {
                'page': idx,
                'url': url,
                'paragraphs': cleaned_paras,
                'error': None
            }
        except Exception as e:
            if attempt == 4:
                return {
                    'page': idx,
                    'url': url,
                    'paragraphs': [],
                    'error': str(e)
                }
            time.sleep(1 + attempt)

def main():
    print(f"Starting crawl for {END_PAGE - START_PAGE + 1} pages (pages {START_PAGE} to {END_PAGE}) from 52shuku.net...")
    start_time = time.time()
    page_results = {}

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_idx = {executor.submit(fetch_page, i): i for i in range(START_PAGE, END_PAGE + 1)}
        completed = 0
        total = len(future_to_idx)
        for future in as_completed(future_to_idx):
            res = future.result()
            page_results[res['page']] = res
            completed += 1
            if completed % 25 == 0 or completed == total:
                print(f"Progress: {completed}/{total} pages downloaded...")

    failed = [idx for idx, r in page_results.items() if r['error']]
    if failed:
        print(f"Warning: {len(failed)} pages failed, retrying sequentially...")
        for f_idx in failed:
            print(f"Retrying page {f_idx}...")
            r = fetch_page(f_idx)
            page_results[f_idx] = r

    still_failed = [idx for idx, r in page_results.items() if r['error']]
    if still_failed:
        print(f"FATAL: Pages could not be fetched: {still_failed}")
        return

    print("All pages fetched successfully! Assembling full novel stream...")
    
    # Assemble ordered paragraphs
    all_paras = []
    for p in range(START_PAGE, END_PAGE + 1):
        all_paras.extend(page_results[p]['paragraphs'])

    print(f"Total raw paragraphs across all pages: {len(all_paras)}")

    # Detect chapter boundaries
    # Patterns for chapter title:
    # "第X章" or "第 X 章" or "第X章 番外" or "番外X"
    ch_regex = re.compile(r'^(第\s*\d+\s*章.*|番外.*)$')
    
    chapters = []
    curr_title = "Văn án & Mở đầu"
    curr_paras = []

    for para in all_paras:
        m = ch_regex.match(para)
        # Avoid false positive like "补充说明：攻每结束一个小世界，记忆会(因为剧情设定)回档到第一章 开头。"
        if m and len(para) <= 60 and not any(k in para for k in ['补充说明', '回到', '到第', '在第']):
            if curr_paras:
                chapters.append({
                    'title': curr_title,
                    'paragraphs': curr_paras
                })
            curr_title = para
            curr_paras = []
        else:
            curr_paras.append(para)

    if curr_paras:
        chapters.append({
            'title': curr_title,
            'paragraphs': curr_paras
        })

    print(f"Detected {len(chapters)} chapters/sections!")
    for idx, ch in enumerate(chapters[:10]):
        print(f"  [{idx}] {ch['title']} ({len(ch['paragraphs'])} paras)")

    # Save full raw file
    full_raw_path = os.path.join(PROJECT_DIR, f'full_raw_{len(chapters)}_chapters.txt')
    with open(full_raw_path, 'w', encoding='utf-8') as f:
        for ch in chapters:
            f.write(f"# {ch['title']}\n\n")
            for p in ch['paragraphs']:
                f.write(f"{p}\n\n")
    print(f"Full raw text saved to: {full_raw_path}")

    # Save into chapters/ch_XXX/
    now_iso = datetime.now(GMT7).isoformat()
    for idx, ch in enumerate(chapters):
        ch_dir_name = f"ch_{idx:03d}" if idx > 0 else "ch_000_intro"
        ch_folder = os.path.join(CHAPTERS_DIR, ch_dir_name)
        os.makedirs(ch_folder, exist_ok=True)

        source_md = os.path.join(ch_folder, 'source.md')
        with open(source_md, 'w', encoding='utf-8') as f:
            f.write(f"# {ch['title']}\n\n")
            for p in ch['paragraphs']:
                f.write(f"{p}\n\n")

        meta_json = os.path.join(ch_folder, 'meta.json')
        meta_data = {
            'chapter_id': ch_dir_name,
            'title': ch['title'],
            'imported_at': now_iso,
            'status': 'SOURCE_READY',
            'n_paragraphs': len(ch['paragraphs']),
            'source_url': 'https://www.52shuku.net/chongsheng/07_b/bjVPq.html'
        }
        with open(meta_json, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

    print(f"All {len(chapters)} chapter folders created under {CHAPTERS_DIR}!")

    # Write config.json
    config_path = os.path.join(PROJECT_DIR, 'config.json')
    config_data = {
        "title": "Xuyên Thư Xong Tôi Giả Gay Trong Truyện Bá Tổng [Khoái Xuyên]",
        "chinese_title": "装弯后霸总自我攻略了[快穿] / 在霸总文学里装弯[快穿]",
        "author": "半斤墨水 (Bán Cân Mặc Thủy)",
        "description": "Lận Duy nhận nhiệm vụ du hành vào các thế giới tiểu thuyết tổng tài cẩu huyết tam quan bất chính thời xưa để uốn nắn cốt truyện, ngăn cản các nam chính vì tình yêu mà làm chuyện điên cuồng vi phạm pháp luật. Kết quả vì hệ thống trục trặc tới trễ, hắn vừa mở mắt đã thành tình địch của nam chính. Để bảo toàn tính mạng làm nhiệm vụ, Lận Duy đành nói dối mình thích đàn ông. Nào ngờ nam chính bá tổng nghe xong lại tự động rơi vào bẫy tự công lược, quay ngược lại theo đuổi hắn.",
        "slug": "xuyên-thư-xong-tôi-giả-gay-trong-truyện-bá-tổng",
        "source_lang": "Chinese",
        "target_lang": "Vietnamese",
        "raw_links": {
            "jjwxc": "https://www.jjwxc.net/onebook.php?novelid=5618458",
            "52shuku": "https://www.52shuku.net/chongsheng/07_b/bjVPq.html",
            "dmxs": "https://www.dmxs.org/cycs/18490.html"
        },
        "style_guide": "Truyện đam mỹ chủ công, khoái xuyên, ngọt sủng hài hước, cường cường. Công phúc hắc ôn nhu bạch thiết hắc x Thụ bá đạo ngạo kiều tự não bổ tự công lược. Lời thoại bảo toàn ngoặc kép tiếng Việt “...”, bảo toàn 1:1, phân đoạn \\n\\n.",
        "confidence_threshold": 0.8,
        "chunk_size": 20,
        "created_at": now_iso,
        "chapters_count": len(chapters)
    }
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
    print(f"config.json written to: {config_path}")

    # Write initial memory files
    characters_data = {
        "protagonists": {
            "蔺唯": {
                "vietnamese": "Lận Duy",
                "role": "Nhân vật chính (Công)",
                "personality": "Bề ngoài dịu dàng, chính trực, đáng tin cậy; bên trong cơ trí, giảo hoạt, bạch thiết hắc, độc miệng",
                "perspective": "Chủ công"
            },
            "霍淇君": {
                "vietnamese": "Hoắc Kỳ Quân",
                "role": "Nhân vật chính (Thụ)",
                "personality": "Bá đạo tổng tài, bề ngoài cao lãnh thâm trầm nhưng thực chất ngạo kiều, sĩ diện, giỏi tự não bổ và tự công lược",
                "perspective": "Chủ thụ (các phân thân nam chính qua các thế giới)"
            }
        },
        "recurring_supporting": {
            "付小青": {
                "vietnamese": "Phó Tiểu Thanh",
                "role": "Nữ chính nguyên tác thế giới 1"
            }
        }
    }
    with open(os.path.join(MEMORY_DIR, 'characters.json'), 'w', encoding='utf-8') as f:
        json.dump(characters_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(MEMORY_DIR, 'glossary.json'), 'w', encoding='utf-8') as f:
        json.dump({
            "装弯": "giả gay / giả cong",
            "自我攻略": "tự công lược",
            "白切黑": "vỏ trắng ruột đen / bạch thiết hắc",
            "天凉王破": "trời lạnh vương thị phá sản",
            "快穿": "khoái xuyên / xuyên nhanh"
        }, f, ensure_ascii=False, indent=2)

    with open(os.path.join(MEMORY_DIR, 'relationships.json'), 'w', encoding='utf-8') as f:
        json.dump({
            "Lận Duy - Hoắc Kỳ Quân": "Ban đầu là 'tình địch', sau thành người yêu (Lận Duy công x Hoắc Kỳ Quân thụ)"
        }, f, ensure_ascii=False, indent=2)

    with open(os.path.join(MEMORY_DIR, 'timeline.json'), 'w', encoding='utf-8') as f:
        json.dump({
            "arc_1": "Thế giới 1: Bác sĩ nam phụ pháo hôi x Bá tổng Hoắc Kỳ Quân",
            "arc_2": "Thế giới 2: Bạn trai cũ phong lưu x Đại lão giới giải trí tàn tật",
            "arc_3": "Thế giới 3: Tiểu hoàng đế x Đại tướng quân",
            "arc_4": "Thế giới 4: Bạch nguyệt quang tiên quân x Ma tôn"
        }, f, ensure_ascii=False, indent=2)

    print("Project memory files initialized successfully!")
    print(f"Elapsed time: {time.time() - start_time:.2f}s")

if __name__ == '__main__':
    main()
