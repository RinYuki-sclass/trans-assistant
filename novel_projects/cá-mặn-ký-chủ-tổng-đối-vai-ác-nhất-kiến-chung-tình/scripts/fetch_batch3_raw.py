import urllib.request
import re
import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"d:\Nhung\RIDI\trans-assistant\novel_projects\cá-mặn-ký-chủ-tổng-đối-vai-ác-nhất-kiến-chung-tình\chapters"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def clean_html(html_str):
    # Loại bỏ thẻ script trước tiên
    html_str = re.sub(r'<script[^>]*>.*?</script>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    
    content_match = re.search(r'<div[^>]*id=["\']content["\'][^>]*>(.*?)</div>', html_str, re.DOTALL | re.IGNORECASE)
    text = content_match.group(1) if content_match else html_str
    
    text = re.sub(r'<br\s*/?>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<p[^>]*>', '\n\n', text, flags=re.IGNORECASE)
    text = re.sub(r'</p>', '', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    
    text = text.replace('&nbsp;', ' ').replace('&ldquo;', '“').replace('&rdquo;', '”')
    text = text.replace('&lsquo;', '‘').replace('&rsquo;', '’').replace('&hellip;', '…')
    
    garbage_keywords = [
        "推荐阅读", "亡灵法师他会治疗", "换嫁小夫郎", "虐主文的NPC消极怠工了",
        "嫁给铁哥们", "两界种田大亨", "恋爱脑重生日常", "穿越之家有赘婿",
        "海岛求生：生活玩家种田囤货", "改嫁京圈太子爷后，竹马们气疯了", "寡夫郎家的小酒楼",
        "咸鱼攻救赎反派boss指南 第", "document.write", "耽美小说", "搜索",
        "近代现代古代架空", "高分榜单", "function", "navigator", "vipmember", "vipread",
        "需要VIP权限", "history.back()", "404.html", "isgood", "首页 > 穿越重生",
        "作者：梅子清汤", "标签:", "强强", "情有独钟", "系统", "甜文", "快穿", "爽文", "穿越重生"
    ]
    
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    cleaned = []
    for l in lines:
        if any(k in l for k in garbage_keywords):
            continue
        if re.match(r'^[{}();\s]*$', l):
            continue
        cleaned.append(l)
    return cleaned

full_lines = []
print("Bắt đầu tải các trang từ 17 đến 25...")
for p in range(17, 26):
    url = f"https://www.dmxs.org/view/6-18479-{p}.html"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw_html = resp.read().decode('gb18030', errors='ignore')
            lines = clean_html(raw_html)
            filtered = []
            for l in lines:
                if "dmxs.org" in l or "上一章" in l or "下一章" in l or "目录" in l or "加入书签" in l:
                    continue
                filtered.append(l)
            full_lines.extend(filtered)
            print(f"Trang {p}: {len(filtered)} dòng")
    except Exception as e:
        print(f"Lỗi tải trang {p}: {e}")

full_text = "\n\n".join(full_lines)

# Bắt tiêu đề chương nguyên tác
chapter_pattern = re.compile(r'(第0([23][0-9])章\s*([^\n\r]*))')
matches = list(chapter_pattern.finditer(full_text))

print(f"\nTìm thấy {len(matches)} tiêu đề chương nguyên tác:")
for m in matches:
    print(f" - {m.group(1)} (Chương {m.group(2)}, vị trí: {m.start()})")

chapters_content = {}
for i in range(len(matches)):
    c_title = matches[i].group(1).strip()
    c_num = int(matches[i].group(2))
    
    if c_num < 21 or c_num > 30:
        continue
        
    start_pos = matches[i].start()
    if i + 1 < len(matches):
        end_pos = matches[i+1].start()
        c_text = full_text[start_pos:end_pos].strip()
    else:
        c_text = full_text[start_pos:].strip()
        
    chapters_content[c_num] = {
        "title": c_title,
        "content": c_text
    }

for c_num in range(21, 31):
    if c_num in chapters_content:
        c_dir = os.path.join(base_dir, f"c{c_num}")
        os.makedirs(c_dir, exist_ok=True)
        
        c_text = chapters_content[c_num]["content"]
        paras = [p.strip() for p in re.split(r'\n\s*\n', c_text) if p.strip()]
        clean_text = "\n\n".join(paras)
        
        src_path = os.path.join(c_dir, "source.md")
        with open(src_path, "w", encoding="utf-8") as f:
            f.write(clean_text + "\n")
            
        meta_path = os.path.join(c_dir, "meta.json")
        meta_data = {
            "chapter": c_num,
            "title_raw": chapters_content[c_num]["title"],
            "title_vi": "",
            "paragraphs_count": len(paras),
            "status": "raw_fetched"
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)
            
        print(f"✅ c{c_num}: {chapters_content[c_num]['title']} -> {len(paras)} đoạn văn")
    else:
        print(f"❌ Không tìm thấy c{c_num}")
