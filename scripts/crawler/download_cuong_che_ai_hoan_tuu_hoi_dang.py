import os
import sys
import re
import json
import time
from datetime import datetime, timezone, timedelta
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

GMT7 = timezone(timedelta(hours=7))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'cường-chế-ái-hoàn-tựu-hồi-đáng-thiểm-cẩu-công-bị-đào-không-liễu')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config.json')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')
RAW_FULL_PATH = os.path.join(PROJECT_DIR, 'raw_full.md')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_para(text):
    text = text.replace('\xa0', ' ').replace('\u3000', ' ')
    text = re.split(r'目录\s+上一页', text)[0]
    text = re.split(r'哦豁[，,]小伙伴们', text)[0]
    text = re.split(r'传送门[：:]', text)[0]
    text = re.split(r'Tips[：:]', text)[0]
    text = re.split(r'小贴士[：:]', text)[0]
    return text.strip()

def fetch_all_pages():
    all_paras = []
    print("Bắt đầu tải các trang từ 52shuku (từ trang 2 đến trang 93)...")
    for p in range(2, 94):
        url = f'https://www.52shuku.net/chongsheng/20_b/bkfhk_{p}.html'
        for retry in range(3):
            try:
                req = urllib.request.Request(url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=15) as resp:
                    soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
                    art = soup.find('article', class_='article-content')
                    if not art:
                        print(f"Không tìm thấy article-content ở trang {p}")
                        break
                    for tag in art.find_all('p'):
                        t = clean_para(tag.get_text())
                        for line in t.splitlines():
                            line = line.strip()
                            if (line and not line.startswith('目录') and 
                                '52书库' not in line and '传送门' not in line and 
                                'Tips：' not in line and '小贴士' not in line and
                                not line.startswith('第1页第2页') and
                                not line.startswith('所属专题')):
                                all_paras.append(line)
                    break
            except Exception as e:
                print(f"Lỗi trang {p} (thử lần {retry+1}): {e}")
                time.sleep(1)
        time.sleep(0.05)
        if p % 15 == 0:
            print(f"Đã tải xong đến trang {p}/93...")
    return all_paras

def process_chapters(all_paras):
    full_text = '\n\n'.join(all_paras)
    
    # Save raw_full.md
    with open(RAW_FULL_PATH, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"Đã lưu file raw tổng: {RAW_FULL_PATH} ({len(full_text)} ký tự)")
    
    # Find all chapter boundaries
    pattern = re.compile(r'^(第\s*(\d+)\s*章[^\n]*)', re.M)
    matches = list(pattern.finditer(full_text))
    print(f"Phát hiện {len(matches)} tiêu đề chương.")
    
    chapters_data = []
    
    for i, m in enumerate(matches):
        ch_num = int(m.group(2))
        ch_title_raw = m.group(1).strip()
        start_idx = m.start()
        end_idx = matches[i + 1].start() if i + 1 < len(matches) else len(full_text)
        
        ch_content = full_text[start_idx:end_idx].strip()
        ch_paras = [p.strip() for p in ch_content.split('\n\n') if p.strip()]
        
        ch_folder_name = f"ch_{ch_num:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_folder_name)
        os.makedirs(ch_dir, exist_ok=True)
        
        source_path = os.path.join(ch_dir, 'source.md')
        
        source_md_content = f"""---
title: Chương {ch_num}: {ch_title_raw}
chapter_num: {ch_num}
original_title: {ch_title_raw}
paragraphs_count: {len(ch_paras)}
characters_count: {len(ch_content)}
---

{ch_content}
"""
        with open(source_path, 'w', encoding='utf-8') as sf:
            sf.write(source_md_content)
            
        chapters_data.append({
            "chapter_id": ch_folder_name,
            "chapter_num": ch_num,
            "title": f"Chương {ch_num}: {ch_title_raw}",
            "original_title": ch_title_raw,
            "paragraphs_count": len(ch_paras),
            "characters_count": len(ch_content),
            "status": "raw_ready",
            "source_path": f"chapters/{ch_folder_name}/source.md",
            "has_translation": False,
            "updated_at": datetime.now(GMT7).isoformat()
        })
    
    # Update chapters_index.json
    index_data = {
        "project": "Cường Chế Ái Hoàn Tựu Hồi Đáng, Thiểm Cẩu Công Bị Đào Không Liễu",
        "slug": "cường-chế-ái-hoàn-tựu-hồi-đáng-thiểm-cẩu-công-bị-đào-không-liễu",
        "total_chapters": len(chapters_data),
        "status": "raw_ready",
        "updated_at": datetime.now(GMT7).isoformat(),
        "chapters": chapters_data
    }
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print(f"Đã cập nhật {INDEX_PATH}")
    
    # Update TOC.md
    toc_lines = [
        "# MỤC LỤC: CƯỜNG CHẾ ÁI HOÀN TỰU HỒI ĐÁNG, THIỂM CẨU CÔNG BỊ ĐÀO KHÔNG LIỄU (《强制爱完就回档，舔狗攻被掏空了》)",
        "",
        f"- **Tổng số chương:** {len(chapters_data)} chương",
        "- **Tác giả:** Nãi Cà Đạt Nhân (奶咖达人)",
        "- **Góc nhìn & Thể loại:** Chủ công (Hoa Y Lâu × Thẩm Kinh Dạng), ABO, Niên hạ, Hồi đương, Thụ cưỡng chế công",
        "- **Nguồn:** [52shuku (bkfhk)](https://www.52shuku.net/chongsheng/20_b/bkfhk.html)",
        "",
        "---",
        "",
        "| STT | Mã chương | Tên chương | Số đoạn | Số ký tự | Trạng thái |",
        "| :---: | :---: | :--- | :---: | :---: | :---: |"
    ]
    for c in chapters_data:
        toc_lines.append(f"| {c['chapter_num']} | `{c['chapter_id']}` | [{c['title']}](chapters/{c['chapter_id']}/source.md) | {c['paragraphs_count']} | {c['characters_count']} | 📥 Raw Ready |")
        
    with open(TOC_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(toc_lines) + '\n')
    print(f"Đã cập nhật {TOC_PATH}")
    
    # Update config.json
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            cfg = json.load(f)
        cfg['total_chapters'] = len(chapters_data)
        cfg['chapters_count'] = len(chapters_data)
        cfg['status'] = 'raw_ready'
        cfg['source_urls'] = {
            "primary": "https://www.52shuku.net/chongsheng/20_b/bkfhk.html",
            "reference": "https://www.52shuku.net/chongsheng/20_b/bkfhk_2.html"
        }
        cfg['updated_at'] = datetime.now(GMT7).isoformat()
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        print(f"Đã cập nhật {CONFIG_PATH}")

if __name__ == '__main__':
    paras = fetch_all_pages()
    process_chapters(paras)
