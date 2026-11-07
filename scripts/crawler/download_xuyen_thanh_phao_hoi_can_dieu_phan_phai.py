import sys
import re
import os
import json
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.request
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_SLUG = "xuyên-thành-pháo-hôi-cán-điệu-phản-phái-bất-thị-giá-cán-pháp"
PROJECT_DIR = os.path.join(BASE_DIR, "novel_projects", PROJECT_SLUG)
CHAPTERS_DIR = os.path.join(PROJECT_DIR, "chapters")
MEMORY_DIR = os.path.join(PROJECT_DIR, "memory")

sys.path.append(os.path.join(BASE_DIR, "scripts"))
try:
    from jjwxc_hanviet import to_hanviet
except ImportError:
    def to_hanviet(text, capitalize_words=True):
        return text

BASE_URL = 'https://www.52shuku.net/chongsheng/09_b/bkdLt_{}.html'
PAGES = list(range(2, 130))  # 2 to 129 (128 pages)

def fetch_page(p):
    url = BASE_URL.format(p)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode('utf-8', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                art = soup.find('article', class_='article-content')
                return p, art.get_text() if art else ''
        except Exception as e:
            time.sleep(1 + attempt)
    return p, ''

def is_noise_line(line):
    s = line.strip()
    if not s:
        return True
    noise_patterns = [
        r'52书库',
        r'www\.52shuku\.net',
        r'52shuku',
        r'小贴士:找看好看得小说',
        r'传送门：排行榜单',
        r'哦豁，小伙伴们如果觉得',
        r'目录\s*上一页',
        r'上一页\s*下一页',
        r'目录\s*下一页',
        r'开始阅读\s*\|\s*阅读记录',
        r'Tips:书荒了不要急',
        r'Tips：如果觉得52不错',
        r'小说简介：',
        r'所属专题：'
    ]
    for np in noise_patterns:
        if re.search(np, s):
            return True
    return False

def clean_paragraph(p):
    p = p.replace('\xa0', ' ').replace('\u3000', ' ').strip()
    p = re.sub(r' +', ' ', p)
    return p

def main():
    print("=" * 60)
    print("🚀 BẮT ĐẦU CÀO TOÀN BỘ RAW CHO DỰ ÁN NOVEL")
    print(f"📖 Tên dự án: {PROJECT_SLUG}")
    print("=" * 60)

    os.makedirs(CHAPTERS_DIR, exist_ok=True)
    os.makedirs(MEMORY_DIR, exist_ok=True)

    print(f"[*] Đang tải {len(PAGES)} trang từ 52shuku...")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_page, PAGES))

    results.sort(key=lambda x: x[0])
    print(f"[+] Hoàn tất tải {len(results)} trang trong {time.time() - start_time:.2f}s")

    all_lines = []
    for p, text in results:
        lines = text.split('\n')
        for l in lines:
            cleaned = clean_paragraph(l)
            if cleaned and not is_noise_line(cleaned):
                # Filter synopsis on page 2
                if p == 2 and any(k in cleaned for k in [
                    '《穿成炮灰干掉反派', '作者：凌晨赶稿', '文案：', '【主攻+双强', '假纨绔真风流',
                    '秦穆死后才知道', '再睁眼，他被系统', '遇到反派那天', '面前弹出三个选项',
                    '[A.干掉他', '[B.感化他', '[C.爱上他', '[任务失败惩罚', '秦穆看着反派',
                    '他慢条斯理地', '“我选A。”', '他掐住少年', '后来，对方将他', '“秦穆，睁开你的',
                    '简云沉有两个秘密', '一、他是姜家', '二、他恨透了', '后来的后来', '系统：说好没理智',
                    '“反派和反派在一起'
                ]):
                    continue
                all_lines.append(cleaned)

    # Save raw full
    raw_full_content = "\n\n".join(all_lines)
    raw_full_path = os.path.join(PROJECT_DIR, "raw_full.md")
    with open(raw_full_path, "w", encoding="utf-8") as f:
        f.write(raw_full_content + "\n")
    
    raw_full_txt_path = os.path.join(PROJECT_DIR, "raw_full.txt")
    with open(raw_full_txt_path, "w", encoding="utf-8") as f:
        f.write(raw_full_content + "\n")
    print(f"[+] Đã lưu toàn văn raw vào: {raw_full_path} ({len(all_lines)} dòng, {len(raw_full_content)} ký tự)")

    # Locate chapter headings
    ch_indices = []
    for idx, line in enumerate(all_lines):
        m = re.match(r'^(第\s*(\d+)\s*章.*|番外.*)$', line)
        if m:
            if m.group(2):
                ch_num = int(m.group(2))
                ch_title = m.group(1).strip()
            else:
                ch_num = len(ch_indices) + 1
                ch_title = line.strip()
            ch_indices.append((ch_num, ch_title, idx))

    print(f"[+] Tìm thấy {len(ch_indices)} tiêu đề chương.")

    # Split into chapters
    chapters = []
    for i in range(len(ch_indices)):
        num, title, start_idx = ch_indices[i]
        end_idx = ch_indices[i+1][2] if i + 1 < len(ch_indices) else len(all_lines)
        ch_paras = all_lines[start_idx:end_idx]
        chapters.append((num, title, ch_paras))

    print(f"[+] Đã chia thành {len(chapters)} chương.")

    chapters_list = []
    toc_lines = [
        f"# MỤC LỤC: XUYÊN THÀNH PHÁO HÔI CÁN ĐIỆU PHẢN PHÁI, BẤT THỊ GIÁ CÁN PHÁP",
        "",
        "> **Tác giả:** Lăng Thần Cản Cảo Linh Cảm Hảo (凌晨赶稿灵感好)  ",
        "> **Tổng số chương:** 173 chương (Chính văn + Phiên ngoại)  ",
        "> **Nguồn raw:** 52shuku / Fanqie Novel  ",
        "",
        "---",
        "",
        "| Chương | Tiêu Đề Gốc | Tiêu Đề Hán-Việt | Số Đoạn | Số Ký Tự | Trạng Thái |",
        "| :--- | :--- | :--- | :---: | :---: | :---: |"
    ]

    for num, title, paras in chapters:
        ch_id = f"ch_{num:03d}"
        ch_dir = os.path.join(CHAPTERS_DIR, ch_id)
        os.makedirs(ch_dir, exist_ok=True)

        source_path = os.path.join(ch_dir, "source.md")
        content = "\n\n".join(paras)
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(content + "\n")

        title_hv = to_hanviet(title).strip()
        word_count = sum(len(p) for p in paras)
        para_count = len(paras)
        is_extra = num >= 169

        ch_meta = {
            "id": ch_id,
            "order": num,
            "chapter_no": num,
            "sub_index": None,
            "arc_id": 2 if is_extra else 1,
            "arc_name": "Phiên Ngoại" if is_extra else "Chính Văn",
            "title_zh": title,
            "title_vi": title_hv,
            "title_hv": title_hv,
            "status": "pending",
            "paragraph_count": para_count,
            "word_count": word_count,
            "source_url": "",
            "updated_at": "2026-11-07T22:00:00"
        }
        chapters_list.append(ch_meta)
        toc_lines.append(f"| {ch_id} | {title} | {title_hv} | {para_count} | {word_count} | ⏳ Chờ dịch |")

    # Write chapters_index.json
    index_data = {
        "project_slug": PROJECT_SLUG,
        "title": "Xuyên Thành Pháo Hôi Cán Điệu Phản Phái, Bất Thị Giá Cán Pháp",
        "author": "Lăng Thần Cản Cảo Linh Cảm Hảo (凌晨赶稿灵感好)",
        "total_chapters": len(chapters),
        "stats": {
            "pending": len(chapters),
            "raw_ready": len(chapters),
            "prescanned": 0,
            "translating": 0,
            "translated": 0,
            "qc_approved": 0,
            "published": 0
        },
        "arcs": [
            {
                "arc_id": 1,
                "arc_name": "Chính Văn",
                "folder_range": ["ch_001", "ch_168"]
            },
            {
                "arc_id": 2,
                "arc_name": "Phiên Ngoại",
                "folder_range": ["ch_169", "ch_173"]
            }
        ],
        "chapters": chapters_list
    }
    index_path = os.path.join(PROJECT_DIR, "chapters_index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)
    print(f"[+] Đã tạo chapters_index.json ({len(chapters_list)} chương)")

    # Write TOC.md
    toc_path = os.path.join(PROJECT_DIR, "TOC.md")
    with open(toc_path, "w", encoding="utf-8") as f:
        f.write("\n".join(toc_lines) + "\n")
    print(f"[+] Đã tạo TOC.md")

    # Write config.json
    config_data = {
        "title": "Xuyên Thành Pháo Hôi Cán Điệu Phản Phái, Bất Thị Giá Cán Pháp",
        "chinese_title": "穿成炮灰干掉反派，不是这干法！",
        "author": "Lăng Thần Cản Cảo Linh Cảm Hảo (凌晨赶稿灵感好)",
        "description": "【Chủ công + Song cường + Cứu rỗi + 1v1 Song khiết + Ngọt ngào】\n\nGiả hoàn khố chân phong lưu phong phê công (Tần Mục) x Cố chấp âm uất mỹ cường thảm thụ (Giản Vân Trầm)\n\nTần Mục sau khi chết mới biết được, thế giới mà mình sống cả một đời thực chất là một cuốn tiểu thuyết, mà hắn chính là đại phản diện tột cùng từng dồn nhân vật chính đến đường cùng, ép thế giới phải tái khởi động vô số lần.\n\nMở mắt ra lần nữa, hắn bị trói định với một hệ thống, xuyên vào một cuốn sách khác, biến thành nam phụ pháo hôi si mê nhân vật chính cuồng dại.\n\nVào ngày chạm trán đại phản diện của cuốn sách này, hệ thống biến mất bấy lâu nay bỗng xuất hiện trở lại, bắn ra ba lựa chọn trước mặt:\n[A. Cán điệu hắn / Giết chết hắn. (Xác suất thành công: Cực thấp)]\n[B. Cảm hóa hắn. (Xác suất thành công: Cực cao, Lựa chọn mặc định)]\n[C. Yêu hắn. (Lựa chọn ưu tiên của ký chủ, Hệ thống đề cử)]\n[Hình phạt khi nhiệm vụ thất bại: Linh hồn bị xóa sổ hoàn toàn.]\n\nTần Mục nhìn ánh mắt âm trầm thoáng qua như loài rắn độc của thiếu niên phản diện, bỗng nhiên bật cười.\nHắn thong dong, chậm rãi đáp lời hệ thống:\n“Ta chọn A.”\nHắn bóp chặt chiếc cổ thon gầy của thiếu niên, nhưng ngay trong khoảnh khắc đối phương kề cận cái chết, hắn lại buông tay.\n\nVề sau, thiếu niên ấy chặn hắn trong gian phòng mờ tối, giọng nói lạnh băng chất vấn:\n“Tần Mục, mở to mắt ra nhìn cho kỹ, tôi rốt cuộc là ai.”\n\n-\nGiản Vân Trầm có hai bí mật:\nMột là, cậu là đứa con riêng không thể lộ ra ánh sáng của Khương gia, sớm muộn gì cũng sẽ đoạt lại tất cả những gì thuộc về mình.\nHai là, cậu căm ghét tột cùng gã đàn ông họ Tần luôn coi mình như kẻ thế thân, nhưng đồng thời lại tham luyến hơi ấm hiếm hoi đôi khi lưu lại trên đầu ngón tay người ấy.\n\nThời gian trôi đi, nhiệm vụ càng đi càng chệch hướng, nhưng tình tiết lại thuận buồm xuôi gió đến lạ kỳ.\nHệ thống: Đâu rồi một đại phản diện chỉ biết đến sự nghiệp, tàn nhẫn không tim không phổi cơ chứ?\n“Phản diện ở bên phản diện, chẳng lẽ không phải là chuyện đương nhiên hay sao?”",
        "slug": PROJECT_SLUG,
        "source_lang": "Chinese",
        "target_lang": "Vietnamese",
        "raw_links": {
            "52shuku": "https://www.52shuku.net/chongsheng/09_b/bkdLt.html",
            "fanqie": "https://fanqienovel.com/page/7595887977356610622"
        },
        "style_guide": "Đam mỹ hiện đại, xuyên thư, hệ thống, chủ công, song cường, cứu rỗi, hào môn thế gia, 1v1 song khiết, hỗ sủng, HE.\n\nQUY TẮC BẮT BUỘC:\n1. Định dạng đoạn văn: Bắt buộc cách nhau đúng 1 dòng trống (\\n\\n) giữa các đoạn văn và lời thoại. Tuyệt đối không dính liền dòng (\\n).\n2. Dấu ngoặc thoại: Lời thoại dùng ngoặc kép cong tiếng Việt “...”, không dùng gạch ngang đầu câu (— ...).\n3. Ngôi 3 trần thuật (Tự sự):\n   - Tần Mục (Công chính): Bắt buộc dùng 'hắn' trong văn trần thuật ngôi 3.\n   - Giản Vân Trầm (Thụ chính): Bắt buộc dùng 'cậu' trong văn trần thuật ngôi 3.\n   - Hệ thống: Dùng 'hệ thống / nó'.\n   - Khương Vân Hàn / nhân vật phụ khác: Dùng 'anh ta / gã / y'.\n4. Tuyệt đối phân biệt trần thuật vs lời thoại: Không đem đại từ mày/tao/ngươi/ta vào trần thuật ngôi 3.\n5. Xưng hô đối thoại Tần Mục ↔ Giản Vân Trầm:\n   - Tần Mục xưng 'tôi / anh', gọi Giản Vân Trầm là 'cậu / em / Giản Vân Trầm / nhóc con'.\n   - Giản Vân Trầm xưng 'tôi / em', gọi Tần Mục là 'anh / Tần Mục / Tần thiếu'.",
        "confidence_threshold": 0.8,
        "chunk_size": 20,
        "created_at": "2026-11-07T22:00:00+07:00",
        "chapters_count": len(chapters),
        "is_completed": False,
        "is_dropped": False,
        "drop_reason": ""
    }
    config_path = os.path.join(PROJECT_DIR, "config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
    print(f"[+] Đã tạo config.json")

    # Write memory files
    characters_data = {
        "characters": [
            {
                "id": "tan_muc",
                "name_cn": "秦穆",
                "name_hv": "Tần Mục",
                "role": "Công chính (Chủ công)",
                "archetype": "Giả hoàn khố chân phong lưu phong phê công, đại phản diện kiếp trước xuyên thư",
                "narrative_pronoun": "hắn",
                "dialogue_pronoun_self": "tôi / anh / ta",
                "dialogue_pronoun_target": "cậu / em / Giản Vân Trầm / nhóc con",
                "description": "Ở thế giới nguyên bản kiếp trước là đại phản diện từng ép thế giới tái khởi động nhiều lần. Xuyên thư thành pháo hôi si tình, bề ngoài phóng đãng bất cần nhưng thực chất trí tuệ siêu việt, nội tâm cuồng dã, chọn 'cán điệu phản diện' theo cách thức độc nhất vô nhị."
            },
            {
                "id": "gian_van_tram",
                "name_cn": "简云沉",
                "name_hv": "Giản Vân Trầm",
                "role": "Thụ chính",
                "archetype": "Cố chấp âm uất mỹ cường thảm thụ, phản diện nguyên tác",
                "narrative_pronoun": "cậu",
                "dialogue_pronoun_self": "tôi / em",
                "dialogue_pronoun_target": "anh / Tần Mục / Tần thiếu",
                "description": "Đứa con riêng không được thừa nhận của Khương gia, chịu nhiều bất công và chèn ép, nuôi chí trả thù và đoạt lại tất cả. Ban đầu căm ghét Tần Mục coi mình là thế thân nhưng dần chìm đắm trong sự bảo bọc và chiếm hữu của hắn."
            },
            {
                "id": "khuong_van_han",
                "name_cn": "姜云寒",
                "name_hv": "Khương Vân Hàn",
                "role": "Nam chính nguyên tác / Anh em cùng cha khác mẹ",
                "archetype": "Thiếu gia danh chính ngôn thuận của Khương gia",
                "narrative_pronoun": "anh ta / gã",
                "dialogue_pronoun_self": "tôi",
                "dialogue_pronoun_target": "cậu / Tần Mục / Giản Vân Trầm",
                "description": "Con trai hợp pháp của Khương gia, đối tượng mà nguyên thân Tần Mục từng si mê theo kịch bản nguyên tác, đối thủ tranh quyền của Giản Vân Trầm."
            },
            {
                "id": "he_thong",
                "name_cn": "系统",
                "name_hv": "Hệ Thống",
                "role": "Hệ thống phụ trợ",
                "archetype": "Hệ thống nhiệm vụ xuyên thư",
                "narrative_pronoun": "hệ thống / nó",
                "dialogue_pronoun_self": "bản hệ thống / tôi",
                "dialogue_pronoun_target": "ký chủ",
                "description": "Trói định với Tần Mục, ban đầu áp đặt quy tắc nhiệm vụ và đe dọa xóa sổ linh hồn, về sau kinh ngạc bất lực trước cách 'cán điệu' phản diện của Tần Mục."
            }
        ]
    }
    with open(os.path.join(MEMORY_DIR, "characters.json"), "w", encoding="utf-8") as f:
        json.dump(characters_data, f, ensure_ascii=False, indent=2)

    glossary_data = {
        "terms": [
            {"cn": "穿书", "vi": "xuyên thư", "category": "genre"},
            {"cn": "炮灰", "vi": "pháo hôi", "category": "trope"},
            {"cn": "反派", "vi": "phản diện", "category": "trope"},
            {"cn": "主攻", "vi": "chủ công", "category": "genre"},
            {"cn": "强强", "vi": "song cường", "category": "genre"},
            {"cn": "救赎", "vi": "cứu rỗi", "category": "genre"},
            {"cn": "疯批", "vi": "điên phê / kẻ điên cuồng", "category": "personality"},
            {"cn": "纨绔", "vi": "hoàn khố / công tử ăn chơi", "category": "personality"},
            {"cn": "私生子", "vi": "con riêng / con ngoài giá thú", "category": "social"},
            {"cn": "姜家", "vi": "Khương gia", "category": "organization"},
            {"cn": "秦家", "vi": "Tần gia", "category": "organization"},
            {"cn": "干掉反派", "vi": "cán điệu phản diện / xử đẹp phản diện", "category": "phrase"}
        ]
    }
    with open(os.path.join(MEMORY_DIR, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump(glossary_data, f, ensure_ascii=False, indent=2)

    relationships_data = {
        "relationships": [
            {
                "source": "tan_muc",
                "target": "gian_van_tram",
                "type": "Tình nhân / Song hướng lao tới / Cứu rỗi",
                "description": "Tần Mục che chở, trêu chọc và thuần hóa chú mèo hoang đầy gai nhọn Giản Vân Trầm; Giản Vân Trầm vừa đề phòng vừa quyến luyến hơi ấm của Tần Mục."
            },
            {
                "source": "gian_van_tram",
                "target": "khuong_van_han",
                "type": "Thù địch / Tranh đoạt gia tộc",
                "description": "Anh em cùng cha khác mẹ trong Khương gia, Giản Vân Trầm bị tước đoạt thân phận và quyết tâm báo thù lật đổ Khương gia."
            },
            {
                "source": "tan_muc",
                "target": "khuong_van_han",
                "type": "Pháo hôi nguyên tác -> Cắt đứt quan hệ",
                "description": "Tần Mục nguyên thân từng si tình mù quáng bám theo Khương Vân Hàn, nhưng Tần Mục sau khi xuyên thư đã hoàn toàn xem Khương Vân Hàn như kẻ xa lạ."
            }
        ]
    }
    with open(os.path.join(MEMORY_DIR, "relationships.json"), "w", encoding="utf-8") as f:
        json.dump(relationships_data, f, ensure_ascii=False, indent=2)

    timeline_data = {
        "events": [
            {
                "chapter": "ch_001",
                "title": "Chạm trán tại quán bar Mộng Huyễn",
                "description": "Tần Mục xuyên thư, gặp lại hệ thống, từ chối các lựa chọn cảm hóa/yêu đương mà chọn 'A. Cán điệu phản diện', bước đầu tiếp cận Giản Vân Trầm."
            }
        ]
    }
    with open(os.path.join(MEMORY_DIR, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)
    print(f"[+] Đã tạo các tệp memory: characters.json, glossary.json, relationships.json, timeline.json")

    # Write AGENTS.md
    agents_md = f"""# AGENT RULES: XUYÊN THÀNH PHÁO HÔI CÁN ĐIỆU PHẢN PHÁI, BẤT THỊ GIÁ CÁN PHÁP (穿成炮灰干掉反派，不是这干法！)

> **Tác giả:** Lăng Thần Cản Cảo Linh Cảm Hảo (凌晨赶稿灵感好)  
> **Thể loại:** Đam mỹ, hiện đại, xuyên thư, hệ thống, chủ công, song cường, cứu rỗi, hào môn thế gia, 1v1 song khiết, HE.  
> **Quy mô dự án:** {len(chapters)} chương (Đã có raw đầy đủ 100% từ 52shuku).  
> **Thư mục dự án:** `novel_projects/{PROJECT_SLUG}`

---

## ⛔ 1. QUY TẮC TỐI THƯỢNG: UNIVERSAL ZERO GOOGLE API KEY MANDATE

1. **AI Agent Tự Thân Dịch Thuật & Soát Lỗi Trực Tiếp:**
   - AI Agent tự đọc trực tiếp file nguyên tác thô (`chapters/ch_xxx/source.md`).
   - Tự phân tích ngữ cảnh, đối chiếu quy chuẩn nhân vật, văn phong chủ công song cường, đối đáp sắc bén, cuốn hút, cảm xúc sâu sắc.
   - Trực tiếp biên dịch sang tiếng Việt chuẩn xác, mượt mà, văn phong lôi cuốn, bảo toàn 1:1 số đoạn và đúng khoảng cách `\\n\\n`.
   - Trực tiếp ghi file kết quả (`translation.md`, `qc_report.md`, `meta.json`) bằng công cụ ghi file chuẩn.
2. **CẤM TUYỆT ĐỐI Gọi Tool / Script Bên Ngoài Dùng Google API Key:**
   - Tuyệt đối KHÔNG chạy script python hay batch file nào kết nối `GEMINI_API_KEY`, `GOOGLE_API_KEY`.
   - Bảo toàn 100% quota/credit và triệt tiêu vĩnh viễn nguy cơ dính lỗi 429 Resource Exhausted hay 503 High Demand.

---

## 📖 2. BẢO TOÀN NGUYÊN TÁC & QUY CHUẨN ĐỊNH DẠNG (1:1 ALIGNMENT)

1. **Bảo Toàn 100% Nguyên Tác (1:1 Paragraph Alignment):**
   - Số đoạn văn tiếng Việt trong `translation.md` phải khớp chính xác 1:1 với số đoạn văn trong `source.md`.
   - **Tuyệt đối không gộp đoạn, không chẻ đoạn, không thêm thắt hay bỏ sót bất kỳ dòng văn nào.**
2. **Khoảng Cách Đoạn Văn Chuẩn `\\n\\n`:**
   - Mọi đoạn trần thuật và lời thoại bắt buộc phải có đúng 1 dòng trống (`\\n\\n`) ngăn cách.
   - Tuyệt đối không để dính dòng (`\\n`).
3. **Dấu Thoại Chuẩn Ngoặc Kép Cong `“...”`:**
   - Sử dụng ngoặc kép cong tiếng Việt `“...”` cho toàn bộ lời thoại trực tiếp của nhân vật.
   - Tuyệt đối không dùng gạch ngang đầu dòng (`- `) hoặc ngoặc kép thẳng thô (`"..."`).
4. **Quy Cách Tag Đặc Thù:**
   - **Lựa chọn / Thông báo Hệ thống:** Đặt trong ngoặc vuông `[A. ...]`, `[Hệ thống: ...]`.
   - **Suy nghĩ nội tâm:** Tự nhiên, không dùng dấu ngoặc thoại trừ khi là độc thoại thầm thì.

---

## 👥 3. THIẾT LẬP NHÂN VẬT & MA TRẬN ĐẠI TỪ BẮT BUỘC

### 3.1. Bảng Phân Vai & Thiết Lập Nhân Vật

| Tên Hán Việt | Tên Gốc | Ngôi 3 Tự Sự | Vai Trò & Tính Cách | Thiết Lập Chi Tiết |
| :--- | :--- | :---: | :--- | :--- |
| **Tần Mục** | 秦穆 | **hắn** | **Công chính**<br>(Giả hoàn khố chân phong lưu phong phê công) | Ở thế giới kiếp trước là đại phản diện từng ép thế giới tái khởi động nhiều lần. Xuyên thư vào vai pháo hôi nam phụ si mê nhân vật chính. Khí chất phóng túng, sắc bén, nguy hiểm, bản lĩnh thượng thừa. Xưng **"tôi / anh"**, gọi Giản Vân Trầm là **"cậu / em / Giản Vân Trầm / nhóc con"**. |
| **Giản Vân Trầm** | 简云沉 | **cậu** | **Thụ chính**<br>(Cố chấp âm uất mỹ cường thảm thụ) | Đứa con riêng không thể lộ diện của Khương gia, lòng mang thù hận, nuôi chí đoạt lại quyền lực. Cực kỳ cảnh giác, tự ti nhưng quật cường, như loài hoa dại có gai. Xưng **"tôi / em"**, gọi Tần Mục là **"anh / Tần Mục / Tần thiếu"**. |
| **Khương Vân Hàn** | 姜云寒 | **anh ta / gã** | **Nam chính nguyên tác** | Thiếu gia chính thống của Khương gia, đối tượng nguyên thân si mê, đối thủ tranh đoạt của Giản Vân Trầm. |
| **Hệ thống** | 系统 | **hệ thống / nó** | **Hệ thống phụ trợ** | Hệ thống nhiệm vụ trói định với Tần Mục, đưa ra nhiệm vụ và cảnh báo. |

---

### 3.2. Ma Trận Xưng Hô Đối Thoại

| Cặp Giao Tiếp | Người Nói | Xưng | Gọi Đối Phương | Ngữ Cảnh & Sắc Thái |
| :--- | :--- | :---: | :---: | :--- |
| **Tần Mục ↔ Giản Vân Trầm** | Tần Mục | **tôi / anh** | **cậu / em / Giản Vân Trầm / nhóc con** | Trêu chọc, bá đạo, cưng chiều, khi đối đầu xưng "tôi - cậu", khi thân mật / tỏ tình xưng "anh - em". |
| | Giản Vân Trầm | **tôi / em** | **anh / Tần Mục / Tần thiếu** | Cảnh giác, lạnh lùng chuyển dần sang ỷ lại, đỏ mặt, quyến luyến. |
| **Tần Mục ↔ Khương Vân Hàn** | Tần Mục | **tôi** | **cậu Khương / anh** | Lạnh nhạt, trào phúng, xem như người xa lạ. |
| | Khương Vân Hàn | **tôi** | **Tần Mục** | Ngỡ ngàng, khó chịu khi bị pháo hôi bơ đẹp. |
| **Tần Mục ↔ Hệ Thống** | Tần Mục | **ta / tôi** | **mi / hệ thống** | Thong dong áp đảo, không coi lời đe dọa của hệ thống ra gì. |
| | Hệ Thống | **bản hệ thống / tôi** | **ký chủ** | Máy móc, ngỡ ngàng, sụp đổ trước nước đi dị của ký chủ. |

---

## 🎭 4. PHÂN ĐỊNH TUYỆT ĐỐI GIỮA TRẦN THUẬT VÀ ĐỐI THOẠI

- **Văn trần thuật ngôi thứ 3 (Tự sự):**
   - Tần Mục: Bắt buộc dùng **"hắn"**.
   - Giản Vân Trầm: Bắt buộc dùng **"cậu"**.
   - Khương Vân Hàn và nhân vật phụ khác: Dùng **"anh ta / gã / y"**.
   - ⚠️ **LƯU Ý NGHIÊM NGẶT:** Tuyệt đối không đem đại từ đối thoại ngôi 1/ngôi 2 (`mày`, `tao`, `ngươi`, `ta`) vào câu văn trần thuật ngôi 3.

---

## 🔍 5. TIÊU CHUẨN KIỂM ĐỊNH CHẤT LƯỢNG (QC CHECKLIST)

Mọi chương dịch xong trước khi được đánh dấu `qc_approved` phải vượt qua 6 lớp kiểm định:
1. **Paragraph Count 1:1:** Số đoạn văn bản dịch khớp chuẩn xác 100% với file `source.md`.
2. **Spacing Consistency:** Đúng `\\n\\n` giữa các đoạn, không có đoạn nào dính liền `\\n`.
3. **Dialogue Quotes:** Dùng toàn bộ ngoặc kép cong `“...”`.
4. **Pronoun Binding:** Đúng ngôi trần thuật (Tần Mục = hắn, Giản Vân Trầm = cậu).
5. **No Hallucination / Omission:** Dịch trọn vẹn từng câu, không cắt xén, không chế thêm tình tiết.
6. **Zero External API:** 100% công việc do Agent tự thực thi.
"""
    agents_path = os.path.join(PROJECT_DIR, "AGENTS.md")
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(agents_md.strip() + "\n")
    print(f"[+] Đã tạo AGENTS.md")

    # Write RULES.md
    rules_md = f"""# WORKSPACE RULES & PIPELINE CONVENTIONS: {PROJECT_SLUG.upper()}

## 1. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)
- **Universal Zero Google API Key Mandate:** Toàn bộ công việc dịch thuật, kiểm định QC, cập nhật timeline/memory đều do Agent tự thân thực thi. Tuyệt đối không gọi Google API ngoài.
- **1:1 Paragraph Alignment:** Bản dịch tiếng Việt phải tương ứng 1:1 với số đoạn văn gốc trong `source.md`.
- **Formatting `\\n\\n`:** Giữa các đoạn trần thuật và lời thoại phải cách nhau đúng một dòng trống.
- **Ngoặc kép cong `“...”`:** Dành cho tất cả các câu thoại trực tiếp.

## 2. QUY TRÌNH DỊCH TỪNG CHƯƠNG (4 PHA TIÊU CHUẨN)
- **Pha 1 (Pre-scan QA):** Quét các từ ngữ mới, tên riêng, kiểm tra ma trận đại từ, tạo `qa_clarifications.md`.
- **Pha 2 (Dịch thuật 1:1):** Dịch trung thực, mượt mà, văn phong đam mỹ chủ công song cường, lưu vào `translation.md`.
- **Pha 3 (Soát lỗi QC Multi-layer):** Kiểm tra 6 tiêu chí QC, tạo `qc_report.md` và `meta.json`.
- **Pha 4 (Cập nhật Memory & Tiến độ):** Cập nhật `timeline.json`, đồng bộ trạng thái trong `chapters_index.json` và `TOC.md`.
"""
    rules_path = os.path.join(PROJECT_DIR, "RULES.md")
    with open(rules_path, "w", encoding="utf-8") as f:
        f.write(rules_md.strip() + "\n")
    print(f"[+] Đã tạo RULES.md")

    # Write PLAN.md
    plan_md = f"""# KẾ HOẠCH DỊCH THUẬT: {PROJECT_SLUG.upper()}

> **Tên tác phẩm:** Xuyên Thành Pháo Hôi Cán Điệu Phản Phái, Bất Thị Giá Cán Pháp (穿成炮灰干掉反派，不是这干法！)  
> **Tác giả:** Lăng Thần Cản Cảo Linh Cảm Hảo (凌晨赶稿灵感好)  
> **Tổng số chương:** {len(chapters)} chương ({len(all_lines)} đoạn văn)  

---

## 📌 LỘ TRÌNH THỰC HIỆN BATCH (MỖI BATCH 5-10 CHƯƠNG)

- [ ] **Batch 1 (Chương 001 - 010):** Chạm trán tại quán bar Mộng Huyễn, Tần Mục chọn phương án A và bước đầu tiếp cận Giản Vân Trầm.
- [ ] **Batch 2 (Chương 011 - 020):** Sự giằng xé giữa Khương gia và mối quan hệ ngầm giữa hai người.
- [ ] **Batch 3 (Chương 021 - 030):** Tiến triển tình cảm và sự bất lực của hệ thống.
- [ ] **Batch 4 (Chương 031 - 050):** Hào môn tranh đấu, Giản Vân Trầm từng bước lật tẩy Khương gia.
- [ ] **Batch 5 (Chương 051 - 080):** Hỗ sủng, công phá vòng vây âm mưu.
- [ ] **Batch 6 (Chương 081 - 120):** Thân phận thật sự và cao trào cốt truyện.
- [ ] **Batch 7 (Chương 121 - 168):** Đại kết cục, phản diện ở bên phản diện.
- [ ] **Batch 8 (Chương 169 - 173):** Phiên ngoại cầu hôn và thế giới song song if-line của Tần Mục.

---
*Cập nhật tự động theo tiến độ dịch của Agent.*
"""
    plan_path = os.path.join(PROJECT_DIR, "PLAN.md")
    with open(plan_path, "w", encoding="utf-8") as f:
        f.write(plan_md.strip() + "\n")
    print(f"[+] Đã tạo PLAN.md")

    print("\n" + "=" * 60)
    print(f"🎉 KHỞI TẠO DỰ ÁN THÀNH CÔNG: {PROJECT_SLUG}")
    print(f"📁 Thư mục: novel_projects/{PROJECT_SLUG}")
    print(f"📚 Tổng số chương: {len(chapters)}")
    print("=" * 60)

if __name__ == '__main__':
    main()
