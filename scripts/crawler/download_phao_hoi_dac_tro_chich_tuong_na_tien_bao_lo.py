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
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'phao-hoi-dac-tro-chich-tuong-na-tien-bao-lo')
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
    print("Bắt đầu tải 66 trang từ 52shuku...")
    for p in range(2, 67):
        url = f'https://www.52shuku.net/chongsheng/06_b/bkecr_{p}.html'
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
                art = soup.find('article', class_='article-content')
                if not art:
                    continue
                for tag in art.find_all('p'):
                    t = clean_para(tag.get_text())
                    for line in t.splitlines():
                        line = line.strip()
                        if line and not line.startswith('目录') and '52书库' not in line and '传送门' not in line and 'Tips：' not in line and '小贴士' not in line:
                            all_paras.append(line)
        except Exception as e:
            print(f"Lỗi trang {p}: {e}")
        time.sleep(0.05)
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
        "project": "Pháo Hôi Đặc Trợ Chích Tưởng Nã Tiền Bào Lộ",
        "slug": "phao-hoi-dac-tro-chich-tuong-na-tien-bao-lo",
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
        "# MỤC LỤC: PHÁO HÔI ĐẶC TRỢ CHÍCH TƯỞNG NÃ TIỀN BÀO LỘ (《炮灰特助只想拿钱跑路》)",
        "",
        f"- **Tổng số chương:** {len(chapters_data)} (Chính văn hoàn thành)",
        "- **Tác giả:** Trạch Dược (择药)",
        "- **Góc nhìn:** Chủ công (Tùy Ứng × Phó Dận An)",
        "- **Nguồn chính:** [JJWXC (10234828)](https://www.jjwxc.net/onebook.php?novelid=10234828) & [52shuku](https://www.52shuku.net/chongsheng/06_b/bkecr.html)",
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
        cfg['status'] = 'raw_ready'
        cfg['updated_at'] = datetime.now(GMT7).isoformat()
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
        print(f"Đã cập nhật {CONFIG_PATH}")

if __name__ == '__main__':
    paras = fetch_all_pages()
    process_chapters(paras)
