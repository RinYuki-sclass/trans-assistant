"""
Script kiểm thử Crawler Tấn Giang (JJWXC) - Bước 1 & Bước 2:
- Kiểm tra lấy danh sách truyện từ bookbase.php (Thuần ái + Chủ công + Xuyên thư + Hoàn thành)
- Kiểm tra giải mã gb18030
- Kiểm tra bóc tách HTML & nhận diện cờ Khoái xuyên (快穿) / Điềm văn (甜文)
- Kiểm tra chuyển đổi Hán-Việt & API lấy chi tiết văn án / ảnh bìa từ app-cdn.jjwxc.net
"""
import os
import sys
import re
import json

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bs4 import BeautifulSoup
from curl_cffi import requests as cf_requests
from jjwxc_hanviet import (
    to_hanviet,
    to_smart_title_vi,
    translate_tag,
    translate_category,
    detect_is_quick_trans,
    detect_is_sweet,
)

TEST_URL = (
    "https://www.jjwxc.net/bookbase.php?"
    "fw0=0&fbsj0=0&novelbefavoritedcount0=0&yc0=0&xx2=2&mainview3=3"
    "&sd0=0&lx0=0&fg0=0&collectiontypes=ors&notlikecollectiontypes=ors"
    "&bq=134&removebq=&searchkeywords=&sortType=2&isfinish=2&page=1"
)


def test_crawl_page_1():
    print(f"[1] Đang tải trang 1 từ JJWXC:\n    {TEST_URL}")
    resp = cf_requests.get(TEST_URL, impersonate="chrome120", timeout=20)
    assert resp.status_code == 200, f"HTTP Error {resp.status_code}"

    html_text = resp.content.decode("gb18030", errors="replace")
    soup = BeautifulSoup(html_text, "lxml")

    # Tìm tổng số trang
    max_page = 1
    ctrl = soup.select_one(".controlbar1")
    if ctrl:
        m_pg = re.search(r"共\s*(\d+)\s*页", ctrl.get_text(" ", strip=True))
        if m_pg:
            max_page = int(m_pg.group(1))

    rows = soup.select("table.cytable tr")
    print(f"[2] Đã tải thành công! Tổng số trang phát hiện: {max_page} | Số dòng trên trang 1: {len(rows) - 1}")

    parsed_items = []
    for tr in rows[1:]:
        tds = tr.find_all("td")
        if len(tds) < 7:
            continue
        author_a = tds[0].find("a")
        author_cn = author_a.get_text(strip=True) if author_a else tds[0].get_text(strip=True)

        book_a = tds[1].find("a")
        if not book_a:
            continue
        title_cn = book_a.get_text(strip=True)
        href = book_a.get("href", "")
        m_id = re.search(r"novelid=(\d+)", href)
        if not m_id:
            continue
        novel_id = m_id.group(1)

        title_attr = book_a.get("title", "")
        short_desc = ""
        tags_cn = []
        for line in title_attr.splitlines():
            line = line.strip()
            if line.startswith("简介："):
                short_desc = line[len("简介："):].strip()
            elif line.startswith("标签："):
                raw_tags = line[len("标签："):].strip()
                tags_cn = [t for t in raw_tags.split() if t]

        category_cn = tds[2].get_text(strip=True)
        status_cn = tds[3].get_text(strip=True)
        word_count = int(re.sub(r"\D", "", tds[4].get_text(strip=True)) or "0")
        points = int(re.sub(r"\D", "", tds[5].get_text(strip=True)) or "0")
        pub_date = tds[6].get_text(strip=True)

        is_qt = detect_is_quick_trans(title_cn, tags_cn, short_desc)
        is_sw = detect_is_sweet(tags_cn)

        item = {
            "novel_id": novel_id,
            "title_cn": title_cn,
            "title_hv": to_hanviet(title_cn),
            "title_vi": to_smart_title_vi(title_cn),
            "author_cn": author_cn,
            "author_hv": to_hanviet(author_cn),
            "category_cn": category_cn,
            "category_vi": translate_category(category_cn),
            "status_cn": status_cn,
            "word_count": word_count,
            "points": points,
            "pub_date": pub_date,
            "short_desc": short_desc,
            "tags_cn": tags_cn,
            "tags_vi": [translate_tag(t) for t in tags_cn],
            "is_quick_trans": is_qt,
            "is_sweet": is_sw,
        }
        parsed_items.append(item)

    filtered_items = [
        it for it in parsed_items
        if not it["is_quick_trans"] and not it["is_sweet"]
    ]

    print(f"[3] Thống kê lọc Local trên {len(parsed_items)} bộ của Trang 1:")
    print(f"    - Tổng số bộ cào về: {len(parsed_items)}")
    print(f"    - Số bộ dính Khoái Xuyên (快穿): {sum(1 for x in parsed_items if x['is_quick_trans'])}")
    print(f"    - Số bộ dính Điềm Văn (甜文): {sum(1 for x in parsed_items if x['is_sweet'])}")
    print(f"    - ✅ Số bộ còn lại sau khi lọc sạch (Đơn thế giới & Không điềm văn): {len(filtered_items)}")

    print("\n[4] Top 5 bộ sau khi lọc trên Trang 1:")
    for idx, it in enumerate(filtered_items[:5], 1):
        print(f"  #{idx}. [{it['novel_id']}] {it['title_cn']}")
        print(f"      -> Hán Việt: {it['title_hv']}")
        print(f"      -> Dịch nhanh: {it['title_vi']}")
        print(f"      -> Tác giả: {it['author_hv']} ({it['author_cn']}) | Chữ: {it['word_count']:,}")
        print(f"      -> Tags: {', '.join(it['tags_vi'])}")
        print(f"      -> Tóm tắt ngắn: {it['short_desc']}")

    if filtered_items:
        sample_id = filtered_items[0]["novel_id"]
        print(f"\n[5] Kiểm tra API chi tiết novelbasicinfo cho novelId={sample_id}:")
        api_url = f"https://app-cdn.jjwxc.net/androidapi/novelbasicinfo?novelId={sample_id}"
        r_detail = cf_requests.get(api_url, impersonate="chrome120", timeout=15)
        data = r_detail.json()
        print(f"    - Ảnh bìa: {data.get('novelCover')}")
        print(f"    - Nhân vật: {data.get('protagonist')} -> {to_hanviet(data.get('protagonist', ''))}")
        print(f"    - Số chương: {data.get('novelChapterCount')} | Lượt cất giữ: {data.get('novelbefavoritedcount')} | Điểm: {data.get('novelReviewScore')}")


if __name__ == "__main__":
    test_crawl_page_1()
