import os
import sys
import json
import re
import time
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"d:\Nhung\trans-tool\novel_projects"

def build_than_ai_tang_tien_sinh():
    p_slug = "than-ai-tang-tien-sinh"
    p_dir = os.path.join(BASE_DIR, p_slug)
    chapters_dir = os.path.join(p_dir, "chapters")
    memory_dir = os.path.join(p_dir, "memory")
    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(memory_dir, exist_ok=True)
    
    print(f"=== KHỞI TẠO DỰ ÁN: {p_slug} ===")
    
    # 2.1 Config.json
    config = {
        "title": "Thân Ái Tang Tiên Sinh",
        "chinese_title": "亲爱的丧先生[末世]",
        "author": "Giáng Nguyệt Tinh (绛月星)",
        "slug": p_slug,
        "source_lang": "Chinese",
        "target_lang": "Vietnamese",
        "genre": [
            "Đam mỹ",
            "Trọng sinh",
            "Mạt thế phế thổ",
            "Xây dựng căn cứ",
            "Dị năng",
            "Cường cường",
            "Ngọt sủng",
            "Tang thi vương trung khuyển công x Cường thụ nhân loại",
            "1v1",
            "HE"
        ],
        "description": "Tiểu thuyết đam mỹ mạt thế trùng sinh 1v1. Kiếp trước Phàm Độ trải qua muôn vàn gian khổ nơi mạt thế, đến khi chết mới biết người đàn ông luôn âm thầm đứng ngoài cửa bảo vệ mình chính là Tần Trạm – người đã sớm biến thành nhiễm thể cao cấp (tang thi vương) và yêu thầm cậu đến chết. Trọng sinh về ngày đầu mạt thế, Phàm Độ mỉm cười mở rộng cửa 'nhận nuôi' con tang thi trung khuyển này, cùng nhau thu gom tài nguyên, xây dựng căn cứ, khai hoang làm giàu và thống trị mạt thế.",
        "style_guide": "Trọng sinh, mạt thế xây dựng căn cứ, tang thi niên hạ trung khuyển x cường thụ đại lão.\n1. Định dạng \\n\\n giữa các đoạn văn.\n2. Lời thoại ngoặc kép “...”.\n3. Đại từ: Tần Trạm xưng tôi/hắn/anh, Phàm Độ xưng tôi/cậu/y.",
        "confidence_threshold": 0.8,
        "chunk_size": 20,
        "created_at": "2026-11-15T18:30:00",
        "chapters_count": 111,
        "is_completed": False,
        "is_dropped": False
    }
    with open(os.path.join(p_dir, "config.json"), "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    # 2.2 AGENTS.md
    agents_md = """# QUY CHUẨN DỊCH THUẬT: Thân Ái Tang Tiên Sinh (亲爱的丧先生[末世])

- **Tác phẩm:** Thân Ái Tang Tiên Sinh (亲爱的丧先生[末世])
- **Slug:** `than-ai-tang-tien-sinh`
- **Tác giả:** Giáng Nguyệt Tinh (绛月星)
- **Thể loại:** Đam mỹ, Trọng sinh, Mạt thế phế thổ, Xây dựng căn cứ, Dị năng, Ngọt sủng, Tang thi vương trung khuyển công x Cường thụ nhân loại, 1v1, HE.
- **Quy mô:** 111 chương (Toàn văn chính văn + Phiên ngoại hoàn tất).

---

### 1. Ma trận nhân vật & Quy chuẩn xưng hô
- **Công: Tần Trạm (秦湛)**
  - Thân phận: Nhiễm thể cao cấp / Tang thi vương, niên hạ, bản năng chiến đấu siêu phàm nhưng trước mặt thụ thì cực kỳ ngoan ngoãn, trung khuyển, bệnh kiều si tình, một lòng bảo vệ và phục tùng Phàm Độ.
  - Ngôi thứ 3: "hắn" hoặc "anh".
  - Đối thoại: Xưng "tôi / anh", gọi thụ là "Phàm Độ / Độ Độ / cậu / anh".
  - Phong thái: Độc chiếm, trung thành vô điều kiện, sẵn sàng xé xác bất cứ ai đe dọa Phàm Độ.
- **Thụ: Phàm Độ (凡度)**
  - Thân phận: Nhân loại trọng sinh, cường thụ, đội trưởng / căn cứ trưởng, thâm trầm, phúc hắc, cơ trí, người duy nhất chế ngự và thuần hóa Tang Thi Vương Tần Trạm.
  - Ngôi thứ 3: "cậu" hoặc "hắn".
  - Đối thoại: Xưng "tôi", gọi công là "Tần Trạm / anh / đồ ngốc".
  - Phong thái: Bình tĩnh, quyết đoán, dung túng và hết mực cưng chiều tang thi trung khuyển của mình.
- **Nhân vật phụ:**
  - Ninh Phong (宁峰)
  - Lâm Tử Hiên (林子轩)

---

### 2. Quy chuẩn kỹ thuật & Định dạng
1. **Khoảng cách đoạn chuẩn `\\n\\n`:** Cách dòng đúng 1 dòng trống giữa mọi đoạn văn trần thuật và lời thoại.
2. **Dấu ngoặc kép chuẩn `“...”`:** Lời thoại nhân vật đặt trong dấu ngoặc kép cong tiếng Việt.
3. **Bảo toàn 100% nguyên tác (1:1 Paragraph Alignment):** Số đoạn bản dịch phải khớp chính xác với số đoạn trong `source.md`.
4. **Văn phong:** Sảng văn mạt thế, kiến thiết căn cứ chặt chẽ, tình cảm ngọt sủng ấm áp đan xen chiến đấu căng thẳng.
5. **CẤM DÙNG GOOGLE API KEY:** Tuyệt đối tuân thủ Universal Zero Google API Key Mandate theo AGENTS.md gốc.
"""
    with open(os.path.join(p_dir, "AGENTS.md"), "w", encoding="utf-8") as f:
        f.write(agents_md)

    # 2.3 Memory files
    characters = {
        "characters": [
            {
                "id": "char_tan_tram",
                "name": "Tần Trạm",
                "original_name": "秦湛",
                "role": "Công chính (Tang thi vương, niên hạ trung khuyển)",
                "aliases": ["Tiểu Trạm", "Tang tiên sinh"],
                "gender": "Nam",
                "status": "Nhiễm thể cao cấp / Tang thi vương",
                "first_appearance": "Chương 1",
                "description": "Nhiễm thể cao cấp có ý thức, yêu thầm Phàm Độ đến tận lúc chết ở kiếp trước, kiếp này được Phàm Độ nhận nuôi và hết mực trung thành bảo vệ cậu."
            },
            {
                "id": "char_pham_do",
                "name": "Phàm Độ",
                "original_name": "凡度",
                "role": "Thụ chính (Cường thụ trùng sinh, thủ lĩnh căn cứ)",
                "aliases": ["Độ ca", "Thủ lĩnh Phàm"],
                "gender": "Nam",
                "status": "Nhân loại trùng sinh / Thủ lĩnh liên minh sinh tồn",
                "first_appearance": "Chương 1",
                "description": "Nhân loại trọng sinh, thâm trầm phúc hắc, bản lĩnh cao cường, chủ động thuần dưỡng Tần Trạm và xây dựng căn cứ mạt thế thịnh vượng."
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
                "source": "Tần Trạm",
                "target": "Phàm Độ",
                "type": "Người yêu / Tuyệt đối trung thành",
                "description": "Tần Trạm yêu thầm Phàm Độ qua hai kiếp, nguyện làm tấm khiên và thanh kiếm sắc bén nhất bảo vệ Phàm Độ."
            }
        ]
    }
    with open(os.path.join(memory_dir, "relationships.json"), "w", encoding="utf-8") as f:
        json.dump(relationships, f, ensure_ascii=False, indent=2)

    timeline = {
        "timeline": [
            {
                "chapter": 1,
                "event": "Phàm Độ trọng sinh về 5h sáng ngày 12/6/2020 khi mạt thế bùng nổ, mở cửa đón nhận và nhận nuôi tang thi Tần Trạm."
            }
        ]
    }
    with open(os.path.join(memory_dir, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

    # 2.4 Crawl all 111 chapters from dmxs.org
    print("Đang cào toàn bộ 111 chương của 'Thân Ái Tang Tiên Sinh' từ dmxs.org...")
    chapters_index = {}
    toc_lines = ["# MỤC LỤC: THÂN ÁI TANG TIÊN SINH (亲爱的丧先生[末世])\n\n"]
    raw_full_content = []

    for num in range(1, 112):
        ch_slug = f"ch_{num:03d}"
        ch_dir = os.path.join(chapters_dir, ch_slug)
        os.makedirs(ch_dir, exist_ok=True)
        
        url = f"https://www.dmxs.org/view/6-6248-{num}.html"
        retries = 3
        ch_content = ""
        ch_title = f"第{num}章"
        has_source = False
        
        while retries > 0:
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
                raw = urllib.request.urlopen(req, timeout=12).read()
                html = raw.decode('gbk', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                
                h1 = soup.find('h1')
                if h1:
                    ch_title = re.sub(r'^亲爱的丧先生\s*', '', h1.get_text(strip=True)).strip()
                    
                div = soup.find('div', class_='read_chapterDetail')
                if div:
                    for s in div.find_all(['script', 'style']):
                        s.decompose()
                    for br in div.find_all('br'):
                        br.replace_with('\n')
                    for p in div.find_all('p'):
                        p.append('\n')
                    text = div.get_text()
                    lines = [line.strip() for line in text.split('\n') if line.strip()]
                    clean_lines = []
                    for line in lines:
                        if '耽美小说' in line and 'www.dmxs.org' in line:
                            continue
                        if '亲爱的丧先生最新章节' in line or '下一章' in line or '上一章' in line:
                            continue
                        clean_lines.append(line)
                        
                    ch_content = f"# Chương {num}: {ch_title}\n\n" + '\n\n'.join(clean_lines)
                    with open(os.path.join(ch_dir, "source.md"), "w", encoding="utf-8") as sf:
                        sf.write(ch_content)
                    has_source = True
                    raw_full_content.append(ch_content)
                    print(f"  [Ch {num:03d}/111] Cào thành công {len(clean_lines)} đoạn: {ch_title}")
                    time.sleep(0.15)
                    break
            except Exception as e:
                retries -= 1
                if retries == 0:
                    print(f"  [Ch {num:03d}/111] Thất bại: {e}")
                time.sleep(1)
                
        chapters_index[ch_slug] = {
            "chapter_number": num,
            "title": ch_title,
            "status": "ready_to_translate" if has_source else "pending_source",
            "has_source": has_source,
            "has_translation": False
        }
        status_str = "✅ Đã nạp raw" if has_source else "❌ Thiếu raw"
        toc_lines.append(f"- [Chương {num:03d}: {ch_title}](chapters/{ch_slug}/source.md) - {status_str}\n")

    with open(os.path.join(p_dir, "chapters_index.json"), "w", encoding="utf-8") as f:
        json.dump(chapters_index, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(p_dir, "TOC.md"), "w", encoding="utf-8") as f:
        f.writelines(toc_lines)
        
    with open(os.path.join(p_dir, "raw_full.md"), "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(raw_full_content))
        
    print(f"✅ Hoàn thành 100% khởi tạo: {p_slug}\n")

if __name__ == '__main__':
    build_than_ai_tang_tien_sinh()
