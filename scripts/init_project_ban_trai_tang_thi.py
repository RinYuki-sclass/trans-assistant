import os
import sys
import json
import re
import time
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\trans-tool\novel_projects"

# -------------------------------------------------------------
# 1. BUILD PROJECT: ban-trai-tang-thi-cua-toi
# -------------------------------------------------------------
def build_ban_trai_tang_thi():
    p_slug = "ban-trai-tang-thi-cua-toi"
    p_dir = os.path.join(BASE_DIR, p_slug)
    chapters_dir = os.path.join(p_dir, "chapters")
    memory_dir = os.path.join(p_dir, "memory")
    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(memory_dir, exist_ok=True)
    
    print(f"=== KHỞI TẠO DỰ ÁN: {p_slug} ===")
    
    # 1.1 Config.json
    config = {
        "title": "Bạn Trai Tang Thi Của Tôi",
        "chinese_title": "我的丧尸男友",
        "author": "Ngã Ký Minh Nguyệt (我寄明月)",
        "slug": p_slug,
        "source_lang": "Chinese",
        "target_lang": "Vietnamese",
        "genre": [
            "Đam mỹ",
            "Chủ công",
            "Niên hạ",
            "Mạt thế tang thi",
            "Hài hước ngọt ngào",
            "Dị năng",
            "Tang thi cún con công x Nhân loại học trưởng thụ",
            "1v1",
            "HE"
        ],
        "description": "Tiểu thuyết đam mỹ mạt thế chủ công 1v1. Phương Thanh Trúc là đại biểu nhân loại cần cù nỗ lực sinh tồn trong ngày tận thế. Không ngờ cậu lại liên tục đụng độ cùng một con tang thi 'y phục tề chỉnh, mặt người dạ thú' theo đuổi cuồng nhiệt. Tần Duy tuy biến thành tang thi nhưng vẫn giữ chấp niệm một lòng một dạ theo đuổi học trưởng, bám dính như cún con, nãi hung nãi manh, đối ngoại tàn khốc đối nội ngoan ngoãn nghe lời.",
        "style_guide": "Chủ công, mạt thế hài hước ngọt ngào, cún con tang thi x học trưởng nhân loại.\n1. Định dạng \\n\\n giữa các đoạn văn.\n2. Lời thoại ngoặc kép “...”.\n3. Đại từ: Tần Duy xưng tôi/anh/em, Phương Thanh Trúc xưng tôi/cậu/anh.",
        "confidence_threshold": 0.8,
        "chunk_size": 20,
        "created_at": "2026-11-15T18:30:00",
        "chapters_count": 46,
        "is_completed": False,
        "is_dropped": False
    }
    with open(os.path.join(p_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    # 1.2 AGENTS.md
    agents_md = """# QUY CHUẨN DỊCH THUẬT: Bạn Trai Tang Thi Của Tôi (我的丧尸男友)

- **Tác phẩm:** Bạn Trai Tang Thi Của Tôi (我的丧尸男友)
- **Slug:** `ban-trai-tang-thi-cua-toi`
- **Tác giả:** Ngã Ký Minh Nguyệt (我寄明月)
- **Thể loại:** Đam mỹ, Chủ công, Niên hạ, Mạt thế tang thi, Hài hước ngọt ngào, Tang thi cún con công x Nhân loại học trưởng thụ, 1v1, HE.
- **Quy mô:** 46 chương (41 chương chính văn + 5 chương phiên ngoại).

---

### 1. Ma trận nhân vật & Quy chuẩn xưng hô
- **Công: Tần Duy (秦唯)**
  - Thân phận: Đàn em khóa dưới, sau mạt thế biến thành tang thi cao cấp/tinh anh. Tuy nhiên bản năng yêu thầm và chấp niệm với học trưởng Phương Thanh Trúc không hề mất đi, kiên trì theo đuổi, bám dính như cún con, nãi manh, làm nũng nhưng lúc chiến đấu bảo vệ thụ thì hung hãn tột cùng.
  - Ngôi thứ 3: "anh" hoặc "hắn".
  - Đối thoại: Xưng "tôi / anh / em", gọi thụ là "học trưởng / anh / Thanh Trúc / bảo bối / vợ".
  - Phong thái: Dính người, ngọt ngào, vô cùng sủng thụ, nghe lời thụ vô điều kiện.
- **Thụ: Phương Thanh Trúc (方青竹)**
  - Thân phận: Sinh viên đại học / học trưởng, người sống sót kiên cường trong mạt thế, sở hữu dị năng, thông minh, điềm đạm, lý trí. Ban đầu kinh ngạc vì bị tang thi theo đuổi, sau đó dần xiêu lòng và hết mực dung túng cho chú tang thi nhỏ của mình.
  - Ngôi thứ 3: "cậu" hoặc "hắn".
  - Đối thoại: Xưng "tôi", gọi công là "Tần Duy / cậu / em".
  - Phong thái: Thanh lãnh nhưng nội tâm dịu dàng, bao dung, làm chủ gia đình.
- **Nhân vật phụ:**
  - Đỗ Ngôn Mặc (杜言默)
  - Đào Thả Văn (陶且文)
  - Diệp Trạch Niên (叶择年) & Thẩm Nghị Luân (沈毅轮)

---

### 2. Quy chuẩn kỹ thuật & Định dạng
1. **Khoảng cách đoạn chuẩn `\\n\\n`:** Cách dòng đúng 1 dòng trống giữa mọi đoạn văn trần thuật và lời thoại.
2. **Dấu ngoặc kép chuẩn `“...”`:** Lời thoại nhân vật đặt trong dấu ngoặc kép cong tiếng Việt.
3. **Bảo toàn 100% nguyên tác (1:1 Paragraph Alignment):** Số đoạn bản dịch phải khớp chính xác với số đoạn trong `source.md`.
4. **Văn phong:** Hài hước, ngọt ngào, sinh động, toát lên sự đáng yêu của chú cún tang thi và sự bao dung của học trưởng loài người.
5. **CẤM DÙNG GOOGLE API KEY:** Tuyệt đối tuân thủ Universal Zero Google API Key Mandate theo AGENTS.md gốc.
"""
    with open(os.path.join(p_dir, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(agents_md)

    # 1.3 Memory files
    characters = {
        "characters": [
            {
                "id": "char_tan_duy",
                "name": "Tần Duy",
                "original_name": "秦唯",
                "role": "Công chính (Tang thi công, niên hạ, cún con bám người)",
                "aliases": ["Tiểu Tần", "Tần tang thi"],
                "gender": "Nam",
                "status": "Tang thi cao cấp / Thể tiến hóa",
                "first_appearance": "Chương 1",
                "description": "Đàn em khóa dưới si tình, biến dị thành tang thi nhưng giữ trọn ký ức và tình yêu với Phương Thanh Trúc."
            },
            {
                "id": "char_phuong_thanh_truc",
                "name": "Phương Thanh Trúc",
                "original_name": "方青竹",
                "role": "Thụ chính (Nhân loại thụ, học trưởng thanh lãnh)",
                "aliases": ["Học trưởng Phương", "Thanh Trúc"],
                "gender": "Nam",
                "status": "Nhân loại sống sót / Dị năng giả",
                "first_appearance": "Chương 1",
                "description": "Học trưởng trường đại học, thanh lãnh, lý trí, dịu dàng, chỗ dựa tinh thần cho Tần Duy."
            }
        ]
    }
    with open(os.path.join(memory_dir, "characters.json"), "w", encoding="utf-8") as f:
        json.dump(characters, f, ensure_ascii=False, indent=2)

    with open(os.path.join(memory_dir, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump({"glossary": []}, f, ensure_ascii=False, indent=2)

    relationships = {
        "relationships": [
            {
                "source": "Tần Duy",
                "target": "Phương Thanh Trúc",
                "type": "Người yêu / Nhất kiến chung tình",
                "description": "Tần Duy yêu thầm Phương Thanh Trúc từ trước mạt thế, sau khi thành tang thi liền dùng mọi cách để bám dính lấy học trưởng."
            }
        ]
    }
    with open(os.path.join(memory_dir, "relationships.json"), "w", encoding="utf-8") as f:
        json.dump(relationships, f, ensure_ascii=False, indent=2)

    timeline = {
        "timeline": [
            {
                "chapter": 1,
                "event": "Tần Duy biến thành tang thi tinh anh, gặp lại học trưởng Phương Thanh Trúc và triển khai theo đuổi cuồng nhiệt."
            }
        ]
    }
    with open(os.path.join(memory_dir, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

    # 1.4 Crawl available chapters from JJWXC
    print("Đang tải các chương khả dụng của 'Bạn Trai Tang Thi Của Tôi' từ JJWXC...")
    jj_url = "https://www.jjwxc.net/onebook.php?novelid=2883447"
    req = urllib.request.Request(jj_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req, timeout=10).read().decode('gb18030', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('tr', {'itemprop': 'chapter'})
    
    chapters_index = {}
    toc_lines = ["# MỤC LỤC: BẠN TRAI TANG THI CỦA TÔI (我的丧尸男友)\n\n"]
    raw_full_content = []

    for r in rows:
        tds = [td.get_text(strip=True) for td in r.find_all('td')]
        ch_num = int(tds[0])
        ch_title = tds[1]
        ch_slug = f"ch_{ch_num:03d}"
        ch_dir = os.path.join(chapters_dir, ch_slug)
        os.makedirs(ch_dir, exist_ok=True)
        
        link = r.find('a')
        href = link.get('href', '') if link else ''
        
        has_source = False
        ch_content = ""
        
        if href and ch_num <= 17:
            # fetch public chapter
            try:
                ch_req = urllib.request.Request(href, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                ch_raw = urllib.request.urlopen(ch_req, timeout=10).read().decode('gb18030', errors='ignore')
                ch_soup = BeautifulSoup(ch_raw, 'html.parser')
                div = ch_soup.find('div', class_='noveltext')
                if div:
                    children = [c for c in div.children if c.name == 'div']
                    main_div = None
                    for c in children:
                        if len(c.get_text(strip=True)) > 200:
                            main_div = c
                            break
                    if main_div:
                        for br in main_div.find_all('br'):
                            br.replace_with('\n')
                        text = main_div.get_text()
                        paras = [p.strip() for p in text.split('\n') if p.strip()]
                        ch_content = f"# Chương {ch_num}: {ch_title}\n\n" + '\n\n'.join(paras)
                        with open(os.path.join(ch_dir, "source.md"), "w", encoding="utf-8") as sf:
                            sf.write(ch_content)
                        has_source = True
                        print(f"  [Ch {ch_num:02d}] Tải thành công {len(paras)} đoạn: {ch_title}")
                        time.sleep(0.3)
            except Exception as e:
                print(f"  [Ch {ch_num:02d}] Lỗi tải: {e}")
                
        if has_source and ch_content:
            raw_full_content.append(ch_content)
            
        chapters_index[ch_slug] = {
            "chapter_number": ch_num,
            "title": ch_title,
            "status": "ready_to_translate" if has_source else "pending_source",
            "has_source": has_source,
            "has_translation": False
        }
        
        status_str = "✅ Đã nạp raw" if has_source else "⏳ Chờ cập nhật VIP"
        toc_lines.append(f"- [Chương {ch_num:02d}: {ch_title}](chapters/{ch_slug}/source.md) - {status_str}\n")
        
    with open(os.path.join(p_dir, "chapters_index.json"), "w", encoding="utf-8") as f:
        json.dump(chapters_index, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(p_dir, "TOC.md"), "w", encoding="utf-8") as f:
        f.writelines(toc_lines)
        
    with open(os.path.join(p_dir, "raw_full.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(raw_full_content))
        
    print(f"✅ Hoàn thành khởi tạo: {p_slug}\n")

build_ban_trai_tang_thi()
