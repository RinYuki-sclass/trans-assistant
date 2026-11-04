"""
JJWXC (Tấn Giang) Series Tracker Server
- Cào danh sách truyện từ Tấn Giang (Thuần ái + Chủ công + Xuyên thư + Hoàn chính văn)
- Chiến lược lọc 2 tầng:
  + Tầng 1 (Remote): Lấy phổ rộng (bao gồm cả Khoái xuyên & Điềm văn) lưu vào SQLite local `data/jjwxc_tracker.db`
  + Tầng 2 (Local): Bộ lọc tức thì loại bỏ Khoái xuyên (快穿) và Điềm văn (甜文) + quét sâu từ khóa tiêu đề/văn án
- Tích hợp chuyển đổi Hán-Việt offline & lấy chi tiết văn án / ảnh bìa / CP từ API Tấn Giang
"""
import os
import sys
import re
import html
import json
import time
import sqlite3
import threading
import urllib.parse
from typing import Dict, List, Optional, Tuple

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bs4 import BeautifulSoup
from curl_cffi import requests as cf_requests
from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse, Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from jjwxc_hanviet import (
    to_hanviet,
    to_smart_title_vi,
    translate_tag,
    translate_category,
    detect_is_quick_trans,
    detect_is_sweet,
)
from free_translator import translate_free_google

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static", "jjwxc_tracker")
CACHE_IMG_DIR = os.path.join(DATA_DIR, "cache", "jjwxc_covers")
DB_PATH = os.path.join(DATA_DIR, "jjwxc_tracker.db")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(CACHE_IMG_DIR, exist_ok=True)

# URL mặc định: Thuần ái (xx2=2) + Chủ công (mainview3=3) + Tag Xuyên thư (bq=134) + Đã hoàn thành (isfinish=2) + Sắp xếp theo Tích phân (sortType=2)
# Không loại trừ Khoái xuyên trên URL để tránh sót truyện, lọc Khoái xuyên & Điềm văn ở Local!
DEFAULT_JJWXC_URL = (
    "https://www.jjwxc.net/bookbase.php?"
    "fw0=0&fbsj0=0&novelbefavoritedcount0=0&yc0=0&xx2=2&mainview3=3"
    "&sd0=0&lx0=0&fg0=0&collectiontypes=ors&notlikecollectiontypes=ors"
    "&bq=134&removebq=&searchkeywords=&sortType=2&isfinish=2"
)

db_lock = threading.Lock()

sync_state = {
    "is_syncing": False,
    "mode": "",          # "full" | "check_new"
    "current_page": 0,
    "total_pages": 0,
    "message": "Sẵn sàng",
    "last_sync_at": 0,
    "last_new_count": 0,
    "error": None,
}

IMPERSONATE_PROFILES = ["chrome120", "chrome124", "edge101", "safari17_0", "chrome116"]
_profile_idx = 0


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jjwxc_series (
                novel_id TEXT PRIMARY KEY,
                fixed_order INTEGER,
                title_cn TEXT,
                title_hv TEXT,
                title_vi TEXT,
                author_cn TEXT,
                author_hv TEXT,
                author_id TEXT,
                url TEXT,
                cover_url TEXT,
                category_cn TEXT,
                category_vi TEXT,
                status_cn TEXT,
                word_count INTEGER DEFAULT 0,
                points INTEGER DEFAULT 0,
                pub_date TEXT,
                tags_cn_json TEXT,
                tags_vi_json TEXT,
                short_desc_cn TEXT,
                short_desc_hv TEXT,
                short_desc_vi TEXT,
                full_desc_cn TEXT DEFAULT '',
                full_desc_hv TEXT DEFAULT '',
                full_desc_vi TEXT DEFAULT '',
                protagonist_cn TEXT DEFAULT '',
                protagonist_hv TEXT DEFAULT '',
                chapter_count INTEGER DEFAULT 0,
                fav_count INTEGER DEFAULT 0,
                review_score TEXT DEFAULT '',
                detail_fetched INTEGER DEFAULT 0,
                is_quick_trans INTEGER DEFAULT 0,
                is_sweet INTEGER DEFAULT 0,
                status TEXT DEFAULT 'unread',
                is_new INTEGER DEFAULT 0,
                first_seen_at INTEGER,
                updated_at INTEGER
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_fixed_order ON jjwxc_series(fixed_order)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_status ON jjwxc_series(status)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_qt ON jjwxc_series(is_quick_trans)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_sweet ON jjwxc_series(is_sweet)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_points ON jjwxc_series(points)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_jj_words ON jjwxc_series(word_count)")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS jjwxc_settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        defaults = {
            "target_url": DEFAULT_JJWXC_URL,
            "initial_sync_done": "0",
            "last_sync_at": "0",
            "bookmarked_order": "0",
            "hide_quick_trans": "1",
            "hide_sweet": "1",
            "excluded_tags": "[]",
        }
        for k, v in defaults.items():
            cur.execute("INSERT OR IGNORE INTO jjwxc_settings (key, value) VALUES (?, ?)", (k, v))

        conn.commit()
        conn.close()


def get_setting(key: str, default: str = "") -> str:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT value FROM jjwxc_settings WHERE key = ?", (key,))
    row = cur.fetchone()
    conn.close()
    return row["value"] if row else default


def set_setting(key: str, value: str):
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO jjwxc_settings (key, value) VALUES (?, ?)", (key, str(value)))
        conn.commit()
        conn.close()


def build_jjwxc_page_url(base_url: str, page: int, sort_type: Optional[str] = None) -> str:
    parsed = urllib.parse.urlparse(base_url)
    qs = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    qs["page"] = [str(page)]
    if sort_type is not None:
        qs["sortType"] = [str(sort_type)]
    new_query = urllib.parse.urlencode(qs, doseq=True)
    return urllib.parse.urlunparse(parsed._replace(query=new_query))


def parse_jjwxc_row(tr) -> Optional[Dict]:
    tds = tr.find_all("td")
    if len(tds) < 7:
        return None

    author_a = tds[0].find("a")
    author_cn = author_a.get_text(strip=True) if author_a else tds[0].get_text(strip=True)
    author_id = ""
    if author_a and author_a.get("href"):
        m_aid = re.search(r"authorid=(\d+)", author_a.get("href", ""))
        if m_aid:
            author_id = m_aid.group(1)

    book_a = tds[1].find("a")
    if not book_a:
        return None
    title_cn = book_a.get_text(strip=True)
    href = book_a.get("href", "")
    m_nid = re.search(r"novelid=(\d+)", href)
    if not m_nid:
        return None
    novel_id = m_nid.group(1)
    url = f"https://www.jjwxc.net/onebook.php?novelid={novel_id}"

    title_attr = book_a.get("title", "")
    short_desc_cn = ""
    tags_cn: List[str] = []
    for line in title_attr.splitlines():
        line = line.strip()
        if line.startswith("简介："):
            short_desc_cn = line[len("简介："):].strip()
        elif line.startswith("标签："):
            raw_tags = line[len("标签："):].strip()
            tags_cn = [t.strip() for t in raw_tags.split() if t.strip()]

    category_cn = tds[2].get_text(strip=True)
    status_cn = tds[3].get_text(strip=True)
    word_count = int(re.sub(r"\D", "", tds[4].get_text(strip=True)) or "0")
    points = int(re.sub(r"\D", "", tds[5].get_text(strip=True)) or "0")
    pub_date = tds[6].get_text(strip=True)

    tags_vi = [translate_tag(t) for t in tags_cn]
    is_qt = 1 if detect_is_quick_trans(title_cn, tags_cn, short_desc_cn) else 0
    is_sw = 1 if detect_is_sweet(tags_cn) else 0

    return {
        "novel_id": novel_id,
        "title_cn": title_cn,
        "title_hv": to_hanviet(title_cn),
        "title_vi": to_smart_title_vi(title_cn),
        "author_cn": author_cn,
        "author_hv": to_hanviet(author_cn),
        "author_id": author_id,
        "url": url,
        "category_cn": category_cn,
        "category_vi": translate_category(category_cn),
        "status_cn": status_cn,
        "word_count": word_count,
        "points": points,
        "pub_date": pub_date,
        "tags_cn_json": json.dumps(tags_cn, ensure_ascii=False),
        "tags_vi_json": json.dumps(tags_vi, ensure_ascii=False),
        "short_desc_cn": short_desc_cn,
        "short_desc_hv": to_hanviet(short_desc_cn) if short_desc_cn else "",
        "is_quick_trans": is_qt,
        "is_sweet": is_sw,
    }


def fetch_jjwxc_page(url: str, retries: int = 5) -> Tuple[List[Dict], int]:
    global _profile_idx
    last_err = None
    for attempt in range(retries):
        profile = IMPERSONATE_PROFILES[_profile_idx % len(IMPERSONATE_PROFILES)]
        _profile_idx += 1
        try:
            resp = cf_requests.get(
                url,
                impersonate=profile,
                headers={"Referer": "https://www.jjwxc.net/bookbase.php"},
                timeout=25,
            )
            if resp.status_code != 200:
                last_err = f"HTTP {resp.status_code}"
                time.sleep(2 * (attempt + 1))
                continue

            html_text = resp.content.decode("gb18030", errors="replace")
            soup = BeautifulSoup(html_text, "lxml")

            max_page = 1
            ctrl = soup.select_one(".controlbar1")
            if ctrl:
                m_pg = re.search(r"共\s*(\d+)\s*页", ctrl.get_text(" ", strip=True))
                if m_pg:
                    max_page = int(m_pg.group(1))

            rows = soup.select("table.cytable tr")
            items = []
            for tr in rows[1:]:
                parsed = parse_jjwxc_row(tr)
                if parsed:
                    items.append(parsed)

            return items, max_page
        except Exception as e:
            last_err = str(e)
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Không thể tải trang Tấn Giang {url}: {last_err}")


def upsert_jjwxc_batch(items: List[Dict], mark_as_new: bool = False) -> List[Dict]:
    now = int(time.time())
    new_items = []
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(fixed_order), 0) as max_ord FROM jjwxc_series")
        max_order = cur.fetchone()["max_ord"] or 0

        cur.execute("SELECT novel_id, full_desc_cn FROM jjwxc_series")
        existing_map = {r["novel_id"]: (r["full_desc_cn"] or "") for r in cur.fetchall()}

        for item in items:
            nid = item["novel_id"]
            if nid in existing_map:
                full_desc_existing = existing_map[nid]
                tags_cn = json.loads(item["tags_cn_json"])
                is_qt = 1 if detect_is_quick_trans(item["title_cn"], tags_cn, item["short_desc_cn"], full_desc_existing) else 0
                cur.execute("""
                    UPDATE jjwxc_series SET
                        title_cn = ?,
                        title_hv = ?,
                        title_vi = ?,
                        author_cn = ?,
                        author_hv = ?,
                        author_id = ?,
                        url = ?,
                        category_cn = ?,
                        category_vi = ?,
                        status_cn = ?,
                        word_count = ?,
                        points = ?,
                        pub_date = ?,
                        tags_cn_json = ?,
                        tags_vi_json = ?,
                        short_desc_cn = ?,
                        short_desc_hv = ?,
                        is_quick_trans = ?,
                        is_sweet = ?,
                        updated_at = ?
                    WHERE novel_id = ?
                """, (
                    item["title_cn"], item["title_hv"], item["title_vi"],
                    item["author_cn"], item["author_hv"], item["author_id"],
                    item["url"], item["category_cn"], item["category_vi"],
                    item["status_cn"], item["word_count"], item["points"],
                    item["pub_date"], item["tags_cn_json"], item["tags_vi_json"],
                    item["short_desc_cn"], item["short_desc_hv"],
                    is_qt, item["is_sweet"], now, nid
                ))
            else:
                max_order += 1
                existing_map[nid] = ""
                is_new_val = 1 if mark_as_new else 0
                cur.execute("""
                    INSERT INTO jjwxc_series (
                        novel_id, fixed_order, title_cn, title_hv, title_vi,
                        author_cn, author_hv, author_id, url,
                        category_cn, category_vi, status_cn, word_count, points, pub_date,
                        tags_cn_json, tags_vi_json, short_desc_cn, short_desc_hv,
                        is_quick_trans, is_sweet, status, is_new, first_seen_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'unread', ?, ?, ?)
                """, (
                    nid, max_order, item["title_cn"], item["title_hv"], item["title_vi"],
                    item["author_cn"], item["author_hv"], item["author_id"], item["url"],
                    item["category_cn"], item["category_vi"], item["status_cn"],
                    item["word_count"], item["points"], item["pub_date"],
                    item["tags_cn_json"], item["tags_vi_json"],
                    item["short_desc_cn"], item["short_desc_hv"],
                    item["is_quick_trans"], item["is_sweet"],
                    is_new_val, now, now
                ))
                item_copy = dict(item)
                item_copy["fixed_order"] = max_order
                new_items.append(item_copy)

        conn.commit()
        conn.close()
    return new_items


def run_jjwxc_sync(max_pages: int = 50, mode: str = "full"):
    if sync_state["is_syncing"]:
        return

    sync_state["is_syncing"] = True
    sync_state["error"] = None
    is_initial = get_setting("initial_sync_done", "0") == "0"
    sync_state["mode"] = "initial" if is_initial else mode
    target_url = get_setting("target_url", DEFAULT_JJWXC_URL)

    try:
        sync_state["current_page"] = 1
        sync_state["message"] = "Đang tải trang 1 từ Tấn Giang (JJWXC)..."
        first_items, detected_max_page = fetch_jjwxc_page(build_jjwxc_page_url(target_url, 1))
        total_pages = min(detected_max_page, max_pages)
        sync_state["total_pages"] = total_pages

        total_added = 0
        added = upsert_jjwxc_batch(first_items, mark_as_new=(not is_initial))
        total_added += len(added)

        pages_to_scan = total_pages if (is_initial or mode == "full") else min(3, total_pages)
        sync_state["total_pages"] = pages_to_scan

        for pg in range(2, pages_to_scan + 1):
            sync_state["current_page"] = pg
            sync_state["message"] = f"Đang cào danh sách Tấn Giang: Trang {pg}/{pages_to_scan} (100 bộ/trang)..."
            page_url = build_jjwxc_page_url(target_url, pg)
            items, _ = fetch_jjwxc_page(page_url)
            if not items:
                # JJWXC giới hạn 10 trang (1000 bộ) mỗi kiểu sắp xếp khi không đăng nhập;
                # tự động quét bổ sung qua sortType=3 (Mới đăng) và sortType=5 (Số chữ) để lấy trọn vẹn phần đuôi > 1000!
                if detected_max_page > 10 and (is_initial or mode == "full"):
                    for extra_sort in ("3", "5"):
                        for ex_pg in range(1, min(11, detected_max_page)):
                            sync_state["message"] = f"Đang quét mở rộng (>1000 bộ, sort={extra_sort}, trang {ex_pg})..."
                            ex_url = build_jjwxc_page_url(target_url, ex_pg, sort_type=extra_sort)
                            ex_items, _ = fetch_jjwxc_page(ex_url)
                            if not ex_items:
                                break
                            added_ex = upsert_jjwxc_batch(ex_items, mark_as_new=(not is_initial))
                            total_added += len(added_ex)
                            time.sleep(1.0)
                break
            added_pg = upsert_jjwxc_batch(items, mark_as_new=(not is_initial))
            total_added += len(added_pg)
            time.sleep(1.2)

        now = int(time.time())
        set_setting("initial_sync_done", "1")
        set_setting("last_sync_at", str(now))
        sync_state["last_sync_at"] = now
        sync_state["last_new_count"] = total_added
        sync_state["message"] = f"Hoàn tất đồng bộ {pages_to_scan} trang Tấn Giang ({total_added} bộ mới được lưu)."
    except Exception as e:
        sync_state["error"] = str(e)
        sync_state["message"] = f"Lỗi đồng bộ Tấn Giang: {e}"
    finally:
        sync_state["is_syncing"] = False


def clean_jjwxc_intro_html(raw_intro: str) -> str:
    if not raw_intro:
        return ""
    unescaped = html.unescape(raw_intro)
    unescaped = re.sub(r"<br\s*/?>", "\n", unescaped, flags=re.I)
    unescaped = re.sub(r"</p>", "\n", unescaped, flags=re.I)
    unescaped = re.sub(r"<[^>]+>", "", unescaped)
    lines = [ln.strip() for ln in unescaped.splitlines()]
    cleaned_lines = []
    prev_empty = False
    for ln in lines:
        if not ln:
            if not prev_empty and cleaned_lines:
                cleaned_lines.append("")
            prev_empty = True
        else:
            cleaned_lines.append(ln)
            prev_empty = False
    return "\n".join(cleaned_lines).strip()


def fetch_and_cache_novel_detail(novel_id: str, translate_vi: bool = True) -> Optional[Dict]:
    """
    Gọi API `app-cdn.jjwxc.net/androidapi/novelbasicinfo?novelId=...` để lấy:
    - Ảnh bìa (`novelCover`)
    - Văn án đầy đủ (`novelIntro`)
    - CP Nhân vật chính (`protagonist`)
    - Số chương (`novelChapterCount`), Lượt cất giữ (`novelbefavoritedcount`), Điểm (`novelReviewScore`)
    Và cập nhật lại cờ `is_quick_trans` dựa trên toàn bộ văn án!
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM jjwxc_series WHERE novel_id = ?", (novel_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None

    item = dict(row)
    if item.get("detail_fetched") == 1 and item.get("full_desc_cn"):
        if translate_vi and not item.get("full_desc_vi"):
            vi_text = translate_free_google(item["full_desc_cn"], src_lang="zh-CN", tgt_lang="vi")
            short_vi = translate_free_google(item["short_desc_cn"], src_lang="zh-CN", tgt_lang="vi") if item.get("short_desc_cn") else ""
            with db_lock:
                conn = get_db_connection()
                conn.execute(
                    "UPDATE jjwxc_series SET full_desc_vi = ?, short_desc_vi = ? WHERE novel_id = ?",
                    (vi_text, short_vi, novel_id),
                )
                conn.commit()
                conn.close()
            item["full_desc_vi"] = vi_text
            item["short_desc_vi"] = short_vi
        return item

    api_url = f"https://app-cdn.jjwxc.net/androidapi/novelbasicinfo?novelId={novel_id}"
    resp = cf_requests.get(api_url, impersonate="chrome120", timeout=15)
    if resp.status_code != 200:
        return item

    data = resp.json()
    cover_url = (data.get("novelCover") or "").strip()
    raw_intro = data.get("novelIntro") or ""
    full_desc_cn = clean_jjwxc_intro_html(raw_intro)
    full_desc_hv = to_hanviet(full_desc_cn) if full_desc_cn else ""
    protagonist_cn = (data.get("protagonist") or "").strip()
    protagonist_hv = to_hanviet(protagonist_cn) if protagonist_cn else ""
    chapter_count = int(re.sub(r"\D", "", str(data.get("novelChapterCount") or "0")) or "0")
    fav_count = int(re.sub(r"\D", "", str(data.get("novelbefavoritedcount") or "0")) or "0")
    review_score = (data.get("novelReviewScore") or "").strip()

    tags_cn = json.loads(item.get("tags_cn_json") or "[]")
    is_qt = 1 if detect_is_quick_trans(item["title_cn"], tags_cn, item.get("short_desc_cn", ""), full_desc_cn) else 0

    full_desc_vi = ""
    short_desc_vi = item.get("short_desc_vi") or ""
    if translate_vi:
        if full_desc_cn:
            full_desc_vi = translate_free_google(full_desc_cn, src_lang="zh-CN", tgt_lang="vi")
        if item.get("short_desc_cn") and not short_desc_vi:
            short_desc_vi = translate_free_google(item["short_desc_cn"], src_lang="zh-CN", tgt_lang="vi")

    with db_lock:
        conn = get_db_connection()
        conn.execute("""
            UPDATE jjwxc_series SET
                cover_url = ?,
                full_desc_cn = ?,
                full_desc_hv = ?,
                full_desc_vi = ?,
                short_desc_vi = ?,
                protagonist_cn = ?,
                protagonist_hv = ?,
                chapter_count = ?,
                fav_count = ?,
                review_score = ?,
                is_quick_trans = ?,
                detail_fetched = 1,
                updated_at = ?
            WHERE novel_id = ?
        """, (
            cover_url, full_desc_cn, full_desc_hv, full_desc_vi, short_desc_vi,
            protagonist_cn, protagonist_hv, chapter_count, fav_count,
            review_score, is_qt, int(time.time()), novel_id
        ))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    updated_row = dict(conn.execute("SELECT * FROM jjwxc_series WHERE novel_id = ?", (novel_id,)).fetchone())
    conn.close()
    return updated_row


async def api_jjwxc_batch_meta(request):
    """
    Tải ngầm siêu tốc (song song) Điểm đánh giá (review_score), Lượt cất giữ (fav_count),
    Số chương, Ảnh bìa và CP Nhân vật chính cho các truyện trên trang hiện tại.
    """
    from concurrent.futures import ThreadPoolExecutor
    body = await request.json()
    novel_ids = [str(x).strip() for x in (body.get("novel_ids") or []) if str(x).strip()][:30]
    if not novel_ids:
        return JSONResponse({"ok": True, "items": {}})

    def _fetch_one(nid: str):
        try:
            return nid, fetch_and_cache_novel_detail(nid, translate_vi=False)
        except Exception:
            return nid, None

    results = {}
    with ThreadPoolExecutor(max_workers=8) as pool:
        for nid, item in pool.map(_fetch_one, novel_ids):
            if item:
                results[nid] = {
                    "novel_id": nid,
                    "cover_url": item.get("cover_url") or "",
                    "review_score": item.get("review_score") or "",
                    "fav_count": item.get("fav_count") or 0,
                    "chapter_count": item.get("chapter_count") or 0,
                    "protagonist_cn": item.get("protagonist_cn") or "",
                    "protagonist_hv": item.get("protagonist_hv") or "",
                    "is_quick_trans": item.get("is_quick_trans") or 0,
                }
    return JSONResponse({"ok": True, "items": results})


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

async def api_jjwxc_list_series(request):
    qp = request.query_params
    tab = qp.get("tab", "unread")  # unread | new | read | blacklist | bookmark | all
    page = max(1, int(qp.get("page", "1") or "1"))
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    search = qp.get("q", "").strip()
    tag_filter = qp.get("tag", "").strip()
    min_words = int(qp.get("min_words", "0") or "0")
    sort_by = qp.get("sort", "fixed_asc")

    # Nhận tham số filter trực tiếp từ query hoặc fallback về setting
    hide_qt_param = qp.get("hide_qt")
    if hide_qt_param is not None:
        hide_qt = hide_qt_param == "1"
        set_setting("hide_quick_trans", "1" if hide_qt else "0")
    else:
        hide_qt = get_setting("hide_quick_trans", "1") == "1"

    hide_sweet_param = qp.get("hide_sweet")
    if hide_sweet_param is not None:
        hide_sweet = hide_sweet_param == "1"
        set_setting("hide_sweet", "1" if hide_sweet else "0")
    else:
        hide_sweet = get_setting("hide_sweet", "1") == "1"

    excluded_tags_raw = get_setting("excluded_tags", "[]")
    try:
        excluded_tags = json.loads(excluded_tags_raw)
    except Exception:
        excluded_tags = []

    # Xây dựng mệnh đề lọc cơ sở cho các bộ lọc Local (Khoái xuyên, Điềm văn, Tag loại trừ)
    local_filter_clauses = []
    local_filter_params = []

    if hide_qt:
        local_filter_clauses.append("is_quick_trans = 0")
    if hide_sweet:
        local_filter_clauses.append("is_sweet = 0")
    if excluded_tags:
        for ex_tag in excluded_tags:
            local_filter_clauses.append("tags_cn_json NOT LIKE ? AND tags_vi_json NOT LIKE ?")
            local_filter_params.extend([f'%"{ex_tag}"%', f'%"{ex_tag}"%'])

    where_clauses = []
    params = []

    if tab == "unread":
        where_clauses.append("status = 'unread'")
    elif tab == "new":
        where_clauses.append("is_new = 1 AND status != 'blacklist'")
    elif tab == "read":
        where_clauses.append("status = 'read'")
    elif tab == "blacklist":
        where_clauses.append("status = 'blacklist'")
    elif tab == "bookmark":
        where_clauses.append("status = 'bookmark'")

    if tab in ("unread", "new", "all"):
        where_clauses.extend(local_filter_clauses)
        params.extend(local_filter_params)

    if search:
        where_clauses.append(
            "(title_cn LIKE ? OR title_hv LIKE ? OR title_vi LIKE ? "
            "OR author_cn LIKE ? OR author_hv LIKE ? "
            "OR short_desc_cn LIKE ? OR short_desc_hv LIKE ? OR full_desc_cn LIKE ?)"
        )
        like_q = f"%{search}%"
        params.extend([like_q] * 8)

    if tag_filter:
        where_clauses.append("(tags_cn_json LIKE ? OR tags_vi_json LIKE ?)")
        params.extend([f'%"{tag_filter}"%', f'%"{tag_filter}"%'])

    if min_words > 0:
        where_clauses.append("word_count >= ?")
        params.append(min_words)

    where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

    order_map = {
        "fixed_asc": "fixed_order ASC",
        "fixed_desc": "fixed_order DESC",
        "points_desc": "points DESC, fixed_order ASC",
        "fav_desc": "fav_count DESC, points DESC, fixed_order ASC",
        "score_desc": "CAST(REPLACE(review_score, '分', '') AS REAL) DESC, points DESC",
        "words_desc": "word_count DESC, fixed_order ASC",
        "words_asc": "word_count ASC, fixed_order ASC",
        "pub_desc": "pub_date DESC, fixed_order ASC",
    }
    order_sql = order_map.get(sort_by, "fixed_order ASC")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) as total FROM jjwxc_series {where_sql}", params)
    total_filtered = cur.fetchone()["total"]

    offset = (page - 1) * per_page
    cur.execute(
        f"SELECT * FROM jjwxc_series {where_sql} ORDER BY {order_sql} LIMIT ? OFFSET ?",
        params + [per_page, offset],
    )
    rows = [dict(r) for r in cur.fetchall()]
    for r in rows:
        try:
            r["tags_cn"] = json.loads(r.get("tags_cn_json") or "[]")
            r["tags_vi"] = json.loads(r.get("tags_vi_json") or "[]")
        except Exception:
            r["tags_cn"] = []
            r["tags_vi"] = []

    # Thống kê số lượng (sau khi áp dụng bộ lọc Local cho tab unread & new)
    lf_sql = (" AND " + " AND ".join(local_filter_clauses)) if local_filter_clauses else ""
    cur.execute(f"SELECT COUNT(*) as c FROM jjwxc_series WHERE status = 'unread' {lf_sql}", local_filter_params)
    unread_count = cur.fetchone()["c"]

    cur.execute(f"SELECT COUNT(*) as c FROM jjwxc_series WHERE is_new = 1 AND status != 'blacklist' {lf_sql}", local_filter_params)
    new_count = cur.fetchone()["c"]

    cur.execute("""
        SELECT
            SUM(CASE WHEN status = 'read' THEN 1 ELSE 0 END) as read_count,
            SUM(CASE WHEN status = 'blacklist' THEN 1 ELSE 0 END) as blacklist_count,
            SUM(CASE WHEN status = 'bookmark' THEN 1 ELSE 0 END) as bookmark_count,
            SUM(CASE WHEN is_quick_trans = 1 THEN 1 ELSE 0 END) as qt_total,
            SUM(CASE WHEN is_sweet = 1 THEN 1 ELSE 0 END) as sweet_total,
            COUNT(*) as all_raw_count
        FROM jjwxc_series
    """)
    stat_row = dict(cur.fetchone())
    conn.close()

    total_pages = max(1, (total_filtered + per_page - 1) // per_page)
    return JSONResponse({
        "items": rows,
        "page": page,
        "per_page": per_page,
        "total_items": total_filtered,
        "total_pages": total_pages,
        "counts": {
            "unread": unread_count or 0,
            "new": new_count or 0,
            "read": stat_row.get("read_count") or 0,
            "blacklist": stat_row.get("blacklist_count") or 0,
            "bookmark": stat_row.get("bookmark_count") or 0,
            "all_raw": stat_row.get("all_raw_count") or 0,
            "qt_hidden": stat_row.get("qt_total") or 0,
            "sweet_hidden": stat_row.get("sweet_total") or 0,
        },
        "filters": {
            "hide_quick_trans": hide_qt,
            "hide_sweet": hide_sweet,
            "excluded_tags": excluded_tags,
        },
        "sync_state": sync_state,
        "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
    })


async def api_jjwxc_detail(request):
    novel_id = request.query_params.get("novel_id", "").strip()
    translate_vi = request.query_params.get("tr", "1") == "1"
    if not novel_id:
        return JSONResponse({"error": "Thiếu novel_id"}, status_code=400)
    try:
        item = fetch_and_cache_novel_detail(novel_id, translate_vi=translate_vi)
        if not item:
            return JSONResponse({"error": "Không tìm thấy truyện"}, status_code=404)
        item["tags_cn"] = json.loads(item.get("tags_cn_json") or "[]")
        item["tags_vi"] = json.loads(item.get("tags_vi_json") or "[]")
        return JSONResponse({"ok": True, "item": item})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def api_jjwxc_update_status(request):
    body = await request.json()
    novel_id = str(body.get("novel_id") or "").strip()
    new_status = body.get("status")  # unread | read | blacklist | bookmark
    if not novel_id or new_status not in ("unread", "read", "blacklist", "bookmark"):
        return JSONResponse({"error": "Tham số không hợp lệ"}, status_code=400)

    with db_lock:
        conn = get_db_connection()
        conn.execute(
            "UPDATE jjwxc_series SET status = ?, is_new = 0, updated_at = ? WHERE novel_id = ?",
            (new_status, int(time.time()), novel_id),
        )
        conn.commit()
        conn.close()
    return JSONResponse({"ok": True, "novel_id": novel_id, "status": new_status})


async def api_jjwxc_bookmark(request):
    body = await request.json()
    fixed_order = int(body.get("fixed_order", 0) or 0)
    per_page = int(body.get("per_page", 25) or 25)
    set_setting("bookmarked_order", str(fixed_order))
    return JSONResponse({"ok": True, "bookmarked_order": fixed_order})


async def api_jjwxc_jump_bookmark(request):
    qp = request.query_params
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    bookmarked_order = int(get_setting("bookmarked_order", "0") or "0")
    if bookmarked_order <= 0:
        return JSONResponse({"ok": False, "message": "Chưa có vị trí nào được đánh dấu."})

    hide_qt = get_setting("hide_quick_trans", "1") == "1"
    hide_sweet = get_setting("hide_sweet", "1") == "1"
    clauses = ["status = 'unread'", "fixed_order <= ?"]
    if hide_qt:
        clauses.append("is_quick_trans = 0")
    if hide_sweet:
        clauses.append("is_sweet = 0")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) as pos FROM jjwxc_series WHERE {' AND '.join(clauses)}", (bookmarked_order,))
    pos = cur.fetchone()["pos"] or 1
    conn.close()
    target_page = max(1, (pos + per_page - 1) // per_page)
    return JSONResponse({"ok": True, "bookmarked_order": bookmarked_order, "target_page": target_page})


async def api_jjwxc_trigger_sync(request):
    body = await request.json()
    mode = body.get("mode", "full")
    if sync_state["is_syncing"]:
        return JSONResponse({"ok": False, "message": "Đang đồng bộ Tấn Giang, vui lòng đợi..."}, status_code=409)

    threading.Thread(
        target=run_jjwxc_sync,
        kwargs={"max_pages": 50, "mode": mode},
        daemon=True,
    ).start()
    return JSONResponse({"ok": True, "mode": mode})


async def api_jjwxc_sync_status(request):
    return JSONResponse({
        "sync_state": sync_state,
        "last_sync_at": int(get_setting("last_sync_at", "0") or "0"),
        "target_url": get_setting("target_url", DEFAULT_JJWXC_URL),
    })


async def api_jjwxc_settings(request):
    if request.method == "GET":
        return JSONResponse({
            "target_url": get_setting("target_url", DEFAULT_JJWXC_URL),
            "excluded_tags": json.loads(get_setting("excluded_tags", "[]") or "[]"),
            "hide_quick_trans": get_setting("hide_quick_trans", "1") == "1",
            "hide_sweet": get_setting("hide_sweet", "1") == "1",
            "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
        })
    body = await request.json()
    if "target_url" in body and body["target_url"].strip():
        set_setting("target_url", body["target_url"].strip())
    if "excluded_tags" in body and isinstance(body["excluded_tags"], list):
        set_setting("excluded_tags", json.dumps(body["excluded_tags"], ensure_ascii=False))
    if "hide_quick_trans" in body:
        set_setting("hide_quick_trans", "1" if body["hide_quick_trans"] else "0")
    if "hide_sweet" in body:
        set_setting("hide_sweet", "1" if body["hide_sweet"] else "0")
    return JSONResponse({"ok": True})


async def api_jjwxc_proxy_image(request):
    url = request.query_params.get("url", "").strip()
    if not url:
        return Response(status_code=404)
    safe_name = re.sub(r"[^a-zA-Z0-9._-]", "_", url.split("/")[-1] or "cover.jpg")
    cache_path = os.path.join(CACHE_IMG_DIR, safe_name)
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
        return FileResponse(cache_path)
    try:
        r = cf_requests.get(
            url,
            impersonate="chrome120",
            headers={"Referer": "https://www.jjwxc.net/"},
            timeout=15,
        )
        if r.status_code == 200 and r.content:
            with open(cache_path, "wb") as f:
                f.write(r.content)
            return Response(r.content, media_type=r.headers.get("content-type", "image/jpeg"))
    except Exception:
        pass
    return Response(status_code=404)


async def jjwxc_index_page(request):
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


def start_background_sync_if_needed():
    if get_setting("initial_sync_done", "0") == "0":
        threading.Thread(
            target=run_jjwxc_sync,
            kwargs={"max_pages": 50, "mode": "full"},
            daemon=True,
        ).start()


init_db()

routes = [
    Route("/", jjwxc_index_page),
    Route("/jjwxc", jjwxc_index_page),
    Route("/api/jjwxc/series", api_jjwxc_list_series, methods=["GET"]),
    Route("/api/jjwxc/detail", api_jjwxc_detail, methods=["GET"]),
    Route("/api/jjwxc/batch-meta", api_jjwxc_batch_meta, methods=["POST"]),
    Route("/api/jjwxc/status", api_jjwxc_update_status, methods=["POST"]),
    Route("/api/jjwxc/bookmark", api_jjwxc_bookmark, methods=["POST"]),
    Route("/api/jjwxc/jump-bookmark", api_jjwxc_jump_bookmark, methods=["GET"]),
    Route("/api/jjwxc/sync", api_jjwxc_trigger_sync, methods=["POST"]),
    Route("/api/jjwxc/sync-status", api_jjwxc_sync_status, methods=["GET"]),
    Route("/api/jjwxc/settings", api_jjwxc_settings, methods=["GET", "POST"]),
    Route("/api/jjwxc/proxy-image", api_jjwxc_proxy_image, methods=["GET"]),
    Mount("/static/jjwxc", StaticFiles(directory=STATIC_DIR), name="static_jjwxc"),
]

app = Starlette(
    debug=False,
    routes=routes,
    middleware=[Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])],
)

if __name__ == "__main__":
    start_background_sync_if_needed()
    port = int(os.environ.get("JJWXC_PORT", 8687))
    print(f"🏮 Tấn Giang (JJWXC) Series Tracker đang chạy tại: http://localhost:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")
