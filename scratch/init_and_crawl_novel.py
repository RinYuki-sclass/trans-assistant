import os
import sys
import time
import json
from datetime import datetime, timezone, timedelta

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"d:\Nhung\trans-tool")
from scripts.audio.crawler import fetch_series_chapters, crawl_chapter

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))

SLUG = "cứu-rỗi-soái-cường-thảm-phản-diện"
PROJECT_DIR = os.path.join(r"d:\Nhung\trans-tool\novel_projects", SLUG)
CZBOOKS_URL = "https://czbooks.net/n/sk52b1bp08h"
CHUNK_SZ = 20

def setup_project_structure():
    print(f"Setting up project directories at: {PROJECT_DIR}")
    chapters_dir = os.path.join(PROJECT_DIR, "chapters")
    memory_dir = os.path.join(PROJECT_DIR, "memory")
    os.makedirs(chapters_dir, exist_ok=True)
    os.makedirs(memory_dir, exist_ok=True)

    # 1. config.json
    config_path = os.path.join(PROJECT_DIR, "config.json")
    config_data = {
        "title": "Cứu Rỗi Soái Cường Thảm Phản Diện [Khoái Xuyên]",
        "author": "什司 (Thập Tư)",
        "description": "Có những nhân vật phản diện, bọn họ đẹp trai đến mức tuyệt luân, tàn nhẫn nghịch thiên, nhưng kết cục cuối cùng đều là bị nhân vật chính đầy vẻ chính nghĩa chém dưới mũi kiếm.\nNgười ngoài đều tiếc nuối: Đẹp trai như vậy, tiếc thay lại là một tên điên.\nThế nhưng chẳng một ai hay biết, những kẻ tưởng chừng như nhân cách khiếm khuyết kia, đã từng phải trải qua bao nhiêu nỗi thống khổ rợn người.\n【Nhiệm vụ của các ngươi, chính là cứu rỗi những phản diện này.】\nChấp hành quan nhìn đàn cún con đang gâu gâu kêu loạn, lo lắng đến bạc cả đầu.\n【Đinh đông, Hệ thống Uông Uông phiên bản thử nghiệm 1.0 đã mở nội trắc】\n\n* Thế giới 1 (Đô thị hiện đại): Cún Alaska — Thể thao sinh 188cm nhìn soái khí nhưng thực chất ngốc nghếch x Bá tổng u uất thần kinh chất Phó Vân Xuyên\n* Thế giới 2 (Giới giải trí): Cún Maltese — Tinh xảo kiêu kỳ tiểu thiếu gia x Thô hán bĩ soái võ thuật ảnh đế Thần Vũ\n* Thế giới 3 (Cổ đại): Cún Border Collie — Dưỡng tử thế gả một bụng mưu mô, tâm cơ phúc hắc cao IQ Thẩm Mặc Bạch x Tà nịnh bạo ngược Cẩm Y Vệ chỉ huy sứ Cố Thừa Minh",
        "slug": SLUG,
        "source_lang": "Chinese",
        "target_lang": "Vietnamese",
        "raw_links": {
            "czbooks_overview": "https://czbooks.net/n/sk52b1bp08h",
            "czbooks_first_chapter": "https://czbooks.net/n/sk52b1bp08h/sk2e5?chapterNumber=0",
            "jjwxc": "https://www.jjwxc.net/onebook.php?novelid=7862084",
            "novelupdates": "https://www.novelupdates.com/series/saving-the-handsome-strong-and-miserable-villain-quick-transmigration/"
        },
        "style_guide": "Truyện đam mỹ khoái xuyên, hệ thống cứu rỗi phản diện, điềm văn, đơn nguyên văn, manh sủng hệ cẩu công x phản diện si tình thảm thụ. Góc nhìn chủ công.\n\nQUY TẮC BẮT BUỘC:\n1. Văn phong & QC: Mạch lạc, tự nhiên, văn phong hiện đại/cổ phong tùy từng thế giới. Không dịch máy thô cứng. Lời thoại đặt trong dấu ngoặc kép “...”.\n2. Xưng hô đối thoại:\n   - Thế giới 1 (Hiện đại): Thể thao sinh x Bá tổng (Phó Vân Xuyên).\n   - Thế giới 2 (Showbiz): Tiểu thiếu gia x Ảnh đế Thần Vũ.\n   - Thế giới 3 (Cổ đại): Thẩm Mặc Bạch x Cố Thừa Minh (Chỉ huy sứ Cẩm Y Vệ). Xưng hô cổ phong trang nhã.\n3. Ngôi kể thứ 3 (Narration): Công dùng 'hắn' hoặc tên riêng; Thụ dùng 'y' hoặc chức danh/tên riêng (để tránh nhầm lẫn đại từ giữa 2 nhân vật nam).\n4. Bảo toàn 1:1: Giữ nguyên số lượng đoạn văn, cách dòng chuẩn \\n\\n, không thêm bớt tình tiết.",
        "confidence_threshold": 0.8,
        "chunk_size": CHUNK_SZ,
        "created_at": now_gmt7().isoformat(),
        "chapters_count": 124
    }
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)

    # 2. AGENTS.md
    agents_path = os.path.join(PROJECT_DIR, "AGENTS.md")
    agents_content = """# AGENT RULES: CỨU RỖI SOÁI CƯỜNG THẢM PHẢN DIỆN (拯救帅强惨反派[快穿])

## 1. THÔNG TIN DỰ ÁN & BỐI CẢNH
- **Tên truyện:** Cứu Rỗi Soái Cường Thảm Phản Diện [Khoái Xuyên] (拯救帅强惨反派[快穿] / 拯救帥強慘反派[快穿]).
- **Tên tiếng Anh:** Saving the Handsome, Strong, and Miserable Villain [Quick Transmigration].
- **Tác giả:** 什司 (Thập Tư).
- **Slug dự án:** `cứu-rỗi-soái-cường-thảm-phản-diện`.
- **Thể loại:** Đam mỹ, Khoái xuyên, Hệ thống cẩu cẩu (Uông Uông), Điềm văn, Manh sủng, Chữa lành, Đơn nguyên văn, HE.
- **Góc nhìn chính:** Chủ công (Hệ thống phân phái các cún cưng hóa thân công x Đại phản diện số khổ thụ).
- **Văn phong chuẩn:** Nhẹ nhàng, hài hước, ngọt ngào xen lẫn yếu tố chữa lành vết thương tâm hồn của phản diện. Lời thoại tự nhiên, giàu cảm xúc, không dịch máy (MTL).
- **Liên kết Raw & Tham khảo:**
  - 📖 **CZBooks:** [czbooks.net/n/sk52b1bp08h](https://czbooks.net/n/sk52b1bp08h)
  - 🏛️ **Bản quyền Tấn Giang (JJWXC):** [jjwxc.net/onebook.php?novelid=7862084](https://www.jjwxc.net/onebook.php?novelid=7862084)
  - 🌐 **NovelUpdates:** [novelupdates.com/series/saving-the-handsome-strong-and-miserable-villain-quick-transmigration/](https://www.novelupdates.com/series/saving-the-handsome-strong-and-miserable-villain-quick-transmigration/)

---

## 2. QUY CHUẨN THẾ GIỚI & NHÂN VẬT CHÍNH
### 🐾 Thế giới 1: Alaska (Đô thị hiện đại)
* **Công:** Cún Alaska — Thể thao sinh 188cm nhìn ngầu nhưng ngốc nghếch, nhiệt tình, trung thành.
* **Thụ:** **傅云川 / 傅雲川 (Phó Vân Xuyên)** — Đại phản diện số 1 của A thị, tính khí âm u, thần kinh chất, tàn nhẫn, luôn bị mọi người sợ hãi xa lánh.

### 🐾 Thế giới 2: Maltese (Giới giải trí)
* **Công:** Cún Maltese — Tinh tế, kiêu kỳ, ngạo kiều tiểu thiếu gia.
* **Thụ:** **臣武 (Thần Vũ)** — Ảnh đế võ thuật phong trần, thô hán bĩ soái, từng chịu nhiều bất công vùi dập trước khi nổi danh.

### 🐾 Thế giới 3: Border Collie (Cổ đại quyền mưu)
* **Công:** **沈墨白 (Thẩm Mặc Bạch)** — Cún Border Collie — Dưỡng tử nhà họ Thẩm, một bụng mưu mẹo, tâm cơ thâm trầm, phúc hắc, IQ cực cao, thay thế đích tử gả cho Cẩm Y Vệ.
* **Thụ:** **顾承明 / 顧承明 (Cố Thừa Minh)** — Cẩm Y Vệ chỉ huy sứ tà nịnh, bạo ngược, ai nghe tên cũng khiếp vía nhưng bên trong chịu nhiều u uất tổn thương.

---

## 3. QUY TẮC ĐẠI TỪ NGÔI KỂ THỨ 3 (NARRATION)
* **Công (Nhân vật chính / Ký chủ hệ cẩu):** Sử dụng đại từ **"hắn"** hoặc tên riêng.
* **Thụ (Phản diện ở từng thế giới: Phó Vân Xuyên / Thần Vũ / Cố Thừa Minh):** Sử dụng đại từ **"y"** hoặc danh xưng chức vụ/tên riêng.
* ⚠️ **LƯU Ý:**
  - Tuyệt đối không dùng lộn xộn "hắn" cho cả hai nhân vật nam trong cùng một câu để tránh độc giả bối rối.
  - Phân định rõ ràng: **Công = hắn**, **Thụ = y / tên riêng**.

---

## 4. QUY TẮC XƯNG HÔ ĐỐI THOẠI
* Bối cảnh hiện đại (Thế giới 1, 2): Dùng xưng hô lịch sự, thân mật tự nhiên: `tôi - anh`, `cậu - tôi`, xưng tên thân mật. Tuyệt đối không dùng `mày - tao` trừ khi đối đầu côn đồ cực đoan.
* Bối cảnh cổ đại (Thế giới 3): Dùng xưng hô cổ phong: `ta - chàng / tướng công / chỉ huy sứ / ngươi`.

---

## 5. NGUYÊN TẮC DỊCH THUẬT & QC BẮT BUỘC
1. **Bảo toàn 1:1 (Paragraph Alignment):** Mỗi đoạn văn gốc tương ứng chính xác 1 đoạn tiếng Việt.
2. **Khoảng cách dòng chuẩn:** Giữa các đoạn luôn cách nhau 1 dòng trống (`\\n\\n`).
3. **Dấu thoại chuẩn:** Dùng ngoặc kép `“...”` cho lời thoại trực tiếp, không dùng gạch ngang đầu câu (`— ...`).
4. **Không bỏ sót, không phóng tác (Zero Omission, Zero Addition).**
"""
    with open(agents_path, "w", encoding="utf-8") as f:
        f.write(agents_content)

    # 3. memory files
    characters_data = [
        {
            "name": "Fu Yunchuan",
            "hanviet_name": "Phó Vân Xuyên",
            "original_name": "傅云川 / 傅雲川",
            "gender": "Nam",
            "role": "Thụ (Thế giới 1 - Hiện đại)",
            "aliases": ["Phó tổng", "Phó tiên sinh", "bá tổng thần kinh"],
            "honorifics": "anh - tôi",
            "speech_style": "Âm u, lạnh lùng, thần kinh chất, gắt gỏng nhưng dễ mềm lòng trước cẩu câu",
            "notes": "Đại phản diện thế giới 1, sát thần A thị ai ai cũng sợ hãi"
        },
        {
            "name": "Chen Wu",
            "hanviet_name": "Thần Vũ",
            "original_name": "臣武",
            "gender": "Nam",
            "role": "Thụ (Thế giới 2 - Giới giải trí)",
            "aliases": ["Thần ảnh đế", "Vũ ca"],
            "honorifics": "anh - tôi / em",
            "speech_style": "Thô ráp, phóng khoáng, bĩ soái",
            "notes": "Ảnh đế võ thuật xuất thân khó khăn, bị chèn ép"
        },
        {
            "name": "Shen Mobai",
            "hanviet_name": "Thẩm Mặc Bạch",
            "original_name": "沈墨白",
            "gender": "Nam",
            "role": "Công (Thế giới 3 - Cổ đại)",
            "aliases": ["Thẩm công tử", "Thẩm phu nhân", "Mặc Bạch"],
            "honorifics": "ta - chàng / chỉ huy sứ",
            "speech_style": "Nhã nhặn, dịu dàng bề ngoài nhưng bụng dạ mưu sâu kế độc (Border Collie)",
            "notes": "Dưỡng tử Thẩm gia thế gả cho Cố Thừa Minh"
        },
        {
            "name": "Gu Chengming",
            "hanviet_name": "Cố Thừa Minh",
            "original_name": "顾承明 / 顧承明",
            "gender": "Nam",
            "role": "Thụ (Thế giới 3 - Cổ đại)",
            "aliases": ["Cố chỉ huy sứ", "Cố đại nhân", "sát thần Cẩm Y Vệ"],
            "honorifics": "ta - ngươi / phu nhân",
            "speech_style": "Sắc bén, uy nghiêm, tà nịnh, đa nghi sát khí nặng nề",
            "notes": "Cẩm Y Vệ chỉ huy sứ bạo ngược, phản diện triều đình"
        }
    ]
    with open(os.path.join(memory_dir, "characters.json"), "w", encoding="utf-8") as f:
        json.dump(characters_data, f, ensure_ascii=False, indent=2)

    glossary_data = [
        {"original": "汪汪大队", "translation": "Biệt đội Uông Uông", "hanviet": "Uông Uông đại đội", "category": "organization", "confidence": 1.0, "approved": True, "notes": "Hệ thống cẩu cẩu"},
        {"original": "汪汪系统", "translation": "Hệ thống Uông Uông", "hanviet": "Uông Uông hệ thống", "category": "term", "confidence": 1.0, "approved": True, "notes": "Hệ thống chấp hành nhiệm vụ cứu rỗi"},
        {"original": "傅云川", "translation": "Phó Vân Xuyên", "hanviet": "Phó Vân Xuyên", "category": "character", "confidence": 1.0, "approved": True, "notes": "Phản diện thế giới 1"},
        {"original": "臣武", "translation": "Thần Vũ", "hanviet": "Thần Vũ", "category": "character", "confidence": 1.0, "approved": True, "notes": "Phản diện thế giới 2"},
        {"original": "沈墨白", "translation": "Thẩm Mặc Bạch", "hanviet": "Thẩm Mặc Bạch", "category": "character", "confidence": 1.0, "approved": True, "notes": "Công thế giới 3"},
        {"original": "顾承明", "translation": "Cố Thừa Minh", "hanviet": "Cố Thừa Minh", "category": "character", "confidence": 1.0, "approved": True, "notes": "Thụ thế giới 3, Cẩm Y Vệ chỉ huy sứ"}
    ]
    with open(os.path.join(memory_dir, "glossary.json"), "w", encoding="utf-8") as f:
        json.dump(glossary_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(memory_dir, "relationships.json"), "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

    with open(os.path.join(memory_dir, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=2)

    with open(os.path.join(chapters_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("# Chapters Directory\nRaw and translation chunks stored here.\n")

    print("Project scaffold created successfully!")

def crawl_all_chapters():
    print(f"\nFetching series chapters list from CZBooks: {CZBOOKS_URL}...")
    res = fetch_series_chapters(CZBOOKS_URL)
    chapters = res.get('chapters', [])
    total_chapters = len(chapters)
    print(f"Total chapters discovered: {total_chapters}")

    if total_chapters == 0:
        print("ERROR: No chapters found!")
        return

    chapters_base_dir = os.path.join(PROJECT_DIR, "chapters")
    success_count = 0
    skipped_count = 0
    error_count = 0

    for i, ch_info in enumerate(chapters, start=1):
        ch_id = f"ch_{i:03d}"
        ch_dir = os.path.join(chapters_base_dir, ch_id)
        source_file = os.path.join(ch_dir, "source.md")

        if os.path.exists(source_file) and os.path.getsize(source_file) > 100:
            skipped_count += 1
            continue

        os.makedirs(ch_dir, exist_ok=True)
        ch_url = ch_info.get("url")
        raw_title = ch_info.get("title", f"第{i}頁")
        title_str = f"Chương {i}: {raw_title}"

        # Attempt crawl with retries
        c_res = None
        for attempt in range(3):
            try:
                c_res = crawl_chapter(ch_url)
                if c_res and c_res.get('full_text'):
                    break
            except Exception as ex:
                if attempt == 2:
                    print(f"  [ERROR] {ch_id} failed after 3 attempts: {ex}")
                time.sleep(1)

        if not c_res or not c_res.get('full_text'):
            print(f"  [FAIL] Could not crawl {ch_id} ({ch_url})")
            error_count += 1
            continue

        raw_text = c_res.get('full_text', '')
        paras = [p.strip() for p in raw_text.split('\n') if p.strip()]

        if not paras:
            print(f"  [WARN] {ch_id} has 0 paragraphs")
            error_count += 1
            continue

        # 1. Write source.md
        source_content = f"---\ntitle: {title_str}\n---\n\n{raw_text}\n"
        with open(source_file, "w", encoding="utf-8") as f:
            f.write(source_content)

        # 2. Write chunks
        chunks_dir = os.path.join(ch_dir, "chunks")
        os.makedirs(chunks_dir, exist_ok=True)
        n_chunks = (len(paras) + CHUNK_SZ - 1) // CHUNK_SZ

        for ci in range(n_chunks):
            s, e = ci * CHUNK_SZ, (ci + 1) * CHUNK_SZ
            chunk_paras = paras[s:e]
            chunk_content = f"---\ntitle: {title_str} — Chunk {ci+1}/{n_chunks}\n---\n\n" + "\n\n".join(chunk_paras) + "\n"
            with open(os.path.join(chunks_dir, f"chunk_{ci+1:03d}.md"), "w", encoding="utf-8") as f:
                f.write(chunk_content)

        # 3. Write meta.json
        meta_data = {
            "chapter_id": ch_id,
            "title": title_str,
            "imported_at": now_gmt7().isoformat(),
            "n_paragraphs": len(paras),
            "n_chunks": n_chunks,
            "chunk_size": CHUNK_SZ,
            "czbooks_url": ch_url
        }
        with open(os.path.join(ch_dir, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

        success_count += 1
        if i % 10 == 0 or i == total_chapters or i <= 5:
            print(f"[{i}/{total_chapters}] Successfully crawled & saved {ch_id} ({len(paras)} paras, {n_chunks} chunks)")

        # Brief delay to respect server
        time.sleep(0.3)

    print("\n" + "="*50)
    print(f"CRAWL SUMMARY FOR {SLUG}:")
    print(f"Total: {total_chapters}")
    print(f"Success: {success_count}")
    print(f"Skipped (already existed): {skipped_count}")
    print(f"Errors: {error_count}")
    print("="*50)

if __name__ == "__main__":
    setup_project_structure()
    crawl_all_chapters()
