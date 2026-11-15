import os
import sys
import re
import json
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'novel_projects', 'long-ngao-thien-canh-thi-luyen-ai-nao')
CHAPTERS_DIR = os.path.join(PROJECT_DIR, 'chapters')
TOC_PATH = os.path.join(PROJECT_DIR, 'TOC.md')
INDEX_PATH = os.path.join(PROJECT_DIR, 'chapters_index.json')
CONFIG_PATH = os.path.join(PROJECT_DIR, 'config.json')

os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_DIR, 'memory'), exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 1. Fetch TOC from JJWXC
toc_url = 'http://www.jjwxc.net/onebook.php?novelid=9882856'
req = urllib.request.Request(toc_url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=15) as resp:
    html = resp.read().decode('gb18030', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
ch_meta = []
for tr in soup.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) >= 2 and tds[0].get_text().strip().isdigit():
        ch_num = int(tds[0].get_text().strip())
        ch_title = tds[1].get_text().strip()
        ch_meta.append((ch_num, ch_title))

print(f"Tổng số chương trên JJWXC: {len(ch_meta)}")

chapters_index = []
raw_full = []
toc_lines = [
    "# MỤC LỤC: Long Ngạo Thiên Cánh Thị Luyến Ái Não?! (龙傲天竟是恋爱脑？！)",
    "",
    "- **Tác giả:** Hoang Bất Mậu (荒不谬)",
    "- **Slug:** `long-ngao-thien-canh-thi-luyen-ai-nao`",
    "- **Thể loại:** Đam mỹ, Chủ công, Xuyên thư, Dị năng, Sảng văn, Cường cường, Mỹ công x Khởi Điểm Long Ngạo Thiên thụ, Luyến ái não / Nghiện da thịt, 1v1, HE.",
    f"- **Tổng số chương:** {len(ch_meta)} chương",
    "",
    "---",
    "",
    "### Danh sách chương:",
    ""
]

for ch_num, ch_title in ch_meta:
    ch_id = f"ch_{ch_num:03d}"
    ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
    os.makedirs(ch_dir, exist_ok=True)

    url = f'http://www.jjwxc.net/onebook.php?novelid=9882856&chapterid={ch_num}'
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as resp:
        ch_html = resp.read().decode('gb18030', errors='ignore')

    ch_soup = BeautifulSoup(ch_html, 'html.parser')
    p_div = ch_soup.find('div', id='paragraph_comment_content')

    if not p_div:
        # fallback
        noveltext = ch_soup.find('div', class_='noveltext')
        p_div = noveltext

    for br in p_div.find_all('br'):
        br.replace_with('\n')

    raw = p_div.get_text()
    paras = []
    for l in raw.splitlines():
        clean_l = re.sub(r'^[　\s]+', '', l.strip())
        if clean_l and not clean_l.startswith('插入书签') and not clean_l.startswith('作者有话要说'):
            paras.append(clean_l)

    # Check author note
    author_note_div = ch_soup.find('div', class_='readsmall')
    if author_note_div:
        for br in author_note_div.find_all('br'):
            br.replace_with('\n')
        an_lines = [re.sub(r'^[　\s]+', '', l.strip()) for l in author_note_div.get_text().splitlines() if l.strip()]
        if an_lines:
            paras.append("【作者有话说】")
            paras.extend(an_lines)

    heading = f"第{ch_num}章 {ch_title}"
    full_ch_text = f"{heading}\n\n" + "\n\n".join(paras)

    source_path = os.path.join(ch_dir, 'source.md')
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(full_ch_text + "\n")

    raw_full.append(full_ch_text)

    chapters_index.append({
        'chapter_id': ch_id,
        'chapter_number': ch_num,
        'title': ch_title,
        'paragraphs_count': len(paras),
        'has_source': True,
        'has_translation': False,
        'status': 'raw_ready'
    })

    toc_lines.append(f"- **Chương {ch_num}:** {ch_title} | *{len(paras)} đoạn*")
    print(f"-> Đã tải Chương {ch_num}: {ch_title} ({len(paras)} đoạn)")

# Write files
with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    json.dump(chapters_index, f, ensure_ascii=False, indent=2)

with open(TOC_PATH, 'w', encoding='utf-8') as f:
    f.write("\n".join(toc_lines) + "\n")

with open(os.path.join(PROJECT_DIR, 'raw_full.md'), 'w', encoding='utf-8') as f:
    f.write("\n\n---\n\n".join(raw_full) + "\n")

# config.json
config_data = {
    "title": "Long Ngạo Thiên Cánh Thị Luyến Ái Não?!",
    "chinese_title": "【主攻】龙傲天竟是恋爱脑？！",
    "author": "Hoang Bất Mậu (荒不谬)",
    "description": "Tiểu thuyết chủ công, xuyên thư, dị năng, sảng văn, hài hước, cường cường, 1v1, HE. Dư Hạc Nhàn (mỹ công) xuyên vào tiểu thuyết sảng văn nam tần làm bạch nguyệt quang/người qua đường, đụng độ nam chính Khởi Điểm Sở Vân Hứa (thụ - Long Ngạo Thiên ngầu lòi, thiết huyết thẳng nam). Sau khi tiếp xúc, Long Ngạo Thiên mắc chứng nghiện da thịt/mùi hương của công, biến thành luyến ái não phát cuồng vì công, ban ngày hung dữ sát phạt ban đêm quấn quýt làm nũng.",
    "slug": "long-ngao-thien-canh-thi-luyen-ai-nao",
    "source_lang": "Chinese",
    "target_lang": "Vietnamese",
    "genre": ["Đam mỹ", "Chủ công", "Xuyên thư", "Dị năng", "Sảng văn", "Cường cường", "Mỹ công", "Long Ngạo Thiên thụ", "Luyến ái não", "1v1", "HE"],
    "raw_links": {
        "jjwxc": "http://www.jjwxc.net/onebook.php?novelid=9882856"
    },
    "style_guide": "Đam mỹ, chủ công, hiện đại dị năng, mỹ công x Khởi Điểm Long Ngạo Thiên thụ nghiện da thịt.\n\nQUY TẮC BẮT BUỘC:\n1. Định dạng đoạn văn: Bắt buộc cách nhau đúng 1 dòng trống (\\n\\n) giữa các đoạn và lời thoại. Tuyệt đối không dính dòng (\\n).\n2. Dấu ngoặc thoại: Lời thoại dùng ngoặc kép cong tiếng Việt “...”.\n3. Ngôi 3 trần thuật (Tự sự):\n   - Dư Hạc Nhàn (Công): Luôn dùng 'anh' (hoặc 'Dư Hạc Nhàn').\n   - Sở Vân Hứa (Thụ - Long Ngạo Thiên): Luôn dùng 'hắn' (hoặc 'cậu' tùy ngữ cảnh thân mật, ưu tiên 'hắn' khi thể hiện khí chất nam chính Khởi Điểm).\n4. Đối thoại Dư Hạc Nhàn ↔ Sở Vân Hứa:\n   - Ban đầu: Xưng 'tôi - cậu/anh'.\n   - Sau khi thân mật / nghiện da thịt: Sở Vân Hứa xưng 'tôi/em', gọi Dư Hạc Nhàn là 'anh/Hạc Nhàn', quấn quýt làm nũng; Dư Hạc Nhàn xưng 'tôi/anh', gọi 'cậu/A Hứa'.",
    "confidence_threshold": 0.8,
    "chunk_size": 20,
    "created_at": datetime.now().isoformat(),
    "chapters_count": len(ch_meta),
    "is_completed": True,
    "is_dropped": False,
    "drop_reason": ""
}

with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
    json.dump(config_data, f, ensure_ascii=False, indent=2)

# memory/
chars = {
    "project": "long-ngao-thien-canh-thi-luyen-ai-nao",
    "characters": [
        {
            "id": "char_1",
            "name": "Dư Hạc Nhàn",
            "chinese_name": "余鹤闲",
            "role": "Công chính (Mỹ công, xuyên thư, lười nhác, IQ cao)",
            "narrative_pronoun": "anh",
            "description": "Nhan sắc nghịch thiên, lười biếng nhưng thâm tàng bất lộ, người duy nhất chế ngự được Long Ngạo Thiên"
        },
        {
            "id": "char_2",
            "name": "Sở Vân Hứa",
            "chinese_name": "楚云许",
            "role": "Thụ chính (Long Ngạo Thiên nam chính Khởi Điểm)",
            "narrative_pronoun": "hắn",
            "description": "Chiến lực bạo biểu, phong cách thẳng nam thiết huyết, nhưng khi ở cạnh công thì luyến ái não, nghiện da thịt và hơi ấm của công"
        }
    ]
}
with open(os.path.join(PROJECT_DIR, 'memory', 'characters.json'), 'w', encoding='utf-8') as f:
    json.dump(chars, f, ensure_ascii=False, indent=2)

glossary = {
    "project": "long-ngao-thien-canh-thi-luyen-ai-nao",
    "terms": {
        "龙傲天": "Long Ngạo Thiên",
        "恋爱脑": "Luyến ái não (yêu mù quáng / cuồng yêu)",
        "起点男": "Nam chính Khởi Điểm",
        "异能": "Dị năng",
        "主攻": "Chủ công",
        "穿书": "Xuyên thư"
    }
}
with open(os.path.join(PROJECT_DIR, 'memory', 'glossary.json'), 'w', encoding='utf-8') as f:
    json.dump(glossary, f, ensure_ascii=False, indent=2)

relationships = {
    "project": "long-ngao-thien-canh-thi-luyen-ai-nao",
    "pairs": [
        {
            "character_1": "Dư Hạc Nhàn",
            "character_2": "Sở Vân Hứa",
            "type": "Công x Thụ",
            "status": "Oan gia -> Người yêu cuồng nhiệt"
        }
    ]
}
with open(os.path.join(PROJECT_DIR, 'memory', 'relationships.json'), 'w', encoding='utf-8') as f:
    json.dump(relationships, f, ensure_ascii=False, indent=2)

timeline = {
    "project": "long-ngao-thien-canh-thi-luyen-ai-nao",
    "events": [
        {
            "chapter": 0,
            "summary": "Khởi tạo dự án, cào toàn bộ 22 chương raw chuẩn xác từ JJWXC."
        }
    ]
}
with open(os.path.join(PROJECT_DIR, 'memory', 'timeline.json'), 'w', encoding='utf-8') as f:
    json.dump(timeline, f, ensure_ascii=False, indent=2)

# AGENTS.md
agents_md = f"""# AGENT RULES: LONG NGẠO THIÊN CÁNH THỊ LUYẾN ÁI NÃO?! (龙傲天竟是恋爱脑？！)

## 1. THÔNG TIN DỰ ÁN & BỐI CẢNH
- **Tên truyện:** Long Ngạo Thiên Cánh Thị Luyến Ái Não?! (【主攻】龙傲天竟是恋爱脑？！)
- **Tác giả:** Hoang Bất Mậu (荒不谬)
- **Slug dự án:** `long-ngao-thien-canh-thi-luyen-ai-nao`
- **Nguồn raw:** JJWXC (`novelid=9882856`)
- **Thể loại:** Đam mỹ, Chủ công, Xuyên thư, Dị năng, Sảng văn, Cường cường, Mỹ công x Khởi Điểm Long Ngạo Thiên thụ, Luyến ái não / Nghiện da thịt, 1v1, HE.
- **Quy mô:** {len(ch_meta)} chương hoàn thành.

---

## 2. QUY CHUẨN ĐỊNH DẠNG & VĂN PHONG (STRICT)
1. **Khoảng cách đoạn văn chuẩn `\\n\\n`:** Mọi đoạn trần thuật và lời thoại bắt buộc phải có đúng 1 dòng trống (`\\n\\n`) ngăn cách. Tuyệt đối không dính dòng (`\\n`).
2. **Dấu ngoặc kép chuẩn `“...”`:** Lời thoại dùng ngoặc kép cong tiếng Việt `“...”`, không dùng gạch đầu dòng.
3. **Bảo toàn 100% nguyên tác (1:1 Paragraph Alignment):** Số đoạn văn tiếng Việt phải khớp chính xác 1:1 với số đoạn văn gốc trong `source.md`.
4. **Ngôi 3 trần thuật:**
   - **Dư Hạc Nhàn (Công):** Dùng **anh** hoặc tên riêng.
   - **Sở Vân Hứa (Thụ - Long Ngạo Thiên):** Dùng **hắn** (hoặc **cậu** khi ở thế mềm mỏng, ưu tiên 'hắn' khi thể hiện khí chất cường hãn).
5. **Tuyệt đối phân định Trần thuật vs Đối thoại:**
   - Không đem đại từ xưng hô mày/tao vào câu trần thuật ngôi 3.
   - Đối thoại: Giữ nguyên văn phong hiện đại tự nhiên, hài hước, sắc sảo.
"""

with open(os.path.join(PROJECT_DIR, 'AGENTS.md'), 'w', encoding='utf-8') as f:
    f.write(agents_md.strip() + "\n")

print(f"HOÀN TẤT: Đã khởi tạo dự án và nạp {len(ch_meta)} chương raw vào {CHAPTERS_DIR}")
