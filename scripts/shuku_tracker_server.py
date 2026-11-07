"""
52Shuku (52书库) BL Chủ Công Series Tracker Server
- Cào danh sách truyện Đam Mỹ Chủ Công Đã Hoàn (【完结】 / 【完结+番外】) từ https://www.52shuku.net/Tags/ZhuGongWen_BL/
- Hỗ trợ lọc Local tức thì:
  + Chỉ hiện Xuyên Thư (穿书) [Bật/Tắt linh hoạt]
  + Ẩn Khoái Xuyên (快穿) [Mặc định: BẬT]
  + Ẩn Điềm Văn / Điềm Sủng (甜文 / 甜宠文) [Mặc định: BẬT]
- Tự động bóc tách Tag chuyên đề (`所属专题`), Văn án đầy đủ + Gỡ mìn (`食用指南`), CP Nhân vật chính (`主角`),
  Số trang đọc / Ước tính số chữ từ trang `_2.html` và dịch sang Hán-Việt + Tiếng Việt!
"""
import os
import sys
import re
import html
import json
import time
import sqlite3
import threading
from typing import Dict, List, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bs4 import BeautifulSoup
from curl_cffi import requests as cf_requests
from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

from jjwxc_hanviet import (
    to_hanviet,
    to_smart_title_vi,
    translate_tag,
    detect_is_quick_trans,
)
from free_translator import translate_free_google

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static", "shuku_tracker")
DB_PATH = os.path.join(DATA_DIR, "shuku_tracker.db")
USER_DATA_JSON_PATH = os.path.join(DATA_DIR, "shuku_user_data.json")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)

DEFAULT_SHUKU_URL = "https://www.52shuku.net/Tags/ZhuGongWen_BL/"

db_lock = threading.Lock()

sync_state = {
    "is_syncing": False,
    "mode": "",
    "current_page": 0,
    "total_pages": 0,
    "message": "Sẵn sàng",
    "last_sync_at": 0,
    "last_new_count": 0,
    "error": None,
}

IMPERSONATE_PROFILES = ["chrome120", "chrome124", "edge101", "safari17_0", "chrome116"]
_profile_idx = 0

CHUANSHU_INDICATORS = [
    "穿书",
    "穿成",
    "穿进",
    "穿越进",
    "男配",
    "炮灰",
    "反派",
    "原著",
    "原文",
    "主角攻",
    "主角受",
    "原书",
    "书中",
    "剧情",
    "剧本",
    "龙傲天",
]

SWEET_INDICATORS = ["甜文", "甜宠文", "甜宠", "小甜饼", "种田文", "种田", "美食", "美食文"]


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS shuku_series (
                book_id TEXT PRIMARY KEY,
                fixed_order INTEGER,
                title_cn TEXT,
                title_hv TEXT,
                title_vi TEXT,
                author_cn TEXT,
                author_hv TEXT,
                status_badge TEXT,
                url TEXT,
                read_url TEXT,
                category_code TEXT,
                pub_date TEXT,
                page_count INTEGER DEFAULT 0,
                est_words INTEGER DEFAULT 0,
                tags_cn_json TEXT DEFAULT '[]',
                tags_vi_json TEXT DEFAULT '[]',
                short_desc_cn TEXT DEFAULT '',
                short_desc_hv TEXT DEFAULT '',
                short_desc_vi TEXT DEFAULT '',
                full_desc_cn TEXT DEFAULT '',
                full_desc_hv TEXT DEFAULT '',
                full_desc_vi TEXT DEFAULT '',
                full_desc_en TEXT DEFAULT '',
                protagonist_cn TEXT DEFAULT '',
                protagonist_hv TEXT DEFAULT '',
                one_line_cn TEXT DEFAULT '',
                one_line_hv TEXT DEFAULT '',
                detail_fetched INTEGER DEFAULT 0,
                is_chuanshu INTEGER DEFAULT 0,
                is_quick_trans INTEGER DEFAULT 0,
                is_sweet INTEGER DEFAULT 0,
                status TEXT DEFAULT 'unread',
                is_new INTEGER DEFAULT 0,
                first_seen_at INTEGER,
                updated_at INTEGER
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sk_fixed_order ON shuku_series(fixed_order)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sk_status ON shuku_series(status)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sk_cs ON shuku_series(is_chuanshu)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sk_qt ON shuku_series(is_quick_trans)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_sk_sw ON shuku_series(is_sweet)")
        try:
            cur.execute("ALTER TABLE shuku_series ADD COLUMN full_desc_en TEXT DEFAULT ''")
        except sqlite3.OperationalError:
            pass
        try:
            cur.execute("ALTER TABLE shuku_series ADD COLUMN source_site TEXT DEFAULT ''")
        except sqlite3.OperationalError:
            pass

        cur.execute("""
            CREATE TABLE IF NOT EXISTS shuku_settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        defaults = {
            "target_url": DEFAULT_SHUKU_URL,
            "initial_sync_done": "0",
            "last_sync_at": "0",
            "bookmarked_order": "0",
            "only_chuanshu": "1",
            "hide_quick_trans": "1",
            "hide_sweet": "1",
            "excluded_tags": "[]",
        }
        for k, v in defaults.items():
            cur.execute("INSERT OR IGNORE INTO shuku_settings (key, value) VALUES (?, ?)", (k, v))

        conn.commit()
        conn.close()
    sync_user_data_from_json()
    dump_user_data_to_json()




def dump_user_data_to_json():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT book_id, status, updated_at FROM shuku_series WHERE status != 'unread' AND status != ''")
        statuses = {}
        for r in cur.fetchall():
            statuses[str(r["book_id"])] = {
                "status": r["status"],
                "updated_at": r["updated_at"] or 0
            }
        cur.execute("SELECT value FROM shuku_settings WHERE key = 'bookmarked_order'")
        brow = cur.fetchone()
        bookmarked_order = int(brow["value"]) if brow and brow["value"] else 0
        conn.close()

        data = {
            "bookmarked_order": bookmarked_order,
            "statuses": statuses,
            "exported_at": int(time.time()),
        }
        temp_file = USER_DATA_JSON_PATH + ".tmp"
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        if os.path.exists(USER_DATA_JSON_PATH):
            try:
                os.replace(temp_file, USER_DATA_JSON_PATH)
            except OSError:
                os.remove(USER_DATA_JSON_PATH)
                os.replace(temp_file, USER_DATA_JSON_PATH)
        else:
            os.replace(temp_file, USER_DATA_JSON_PATH)
    except Exception as e:
        print(f"[dump_user_data_to_json] Lỗi: {e}")


def sync_user_data_from_json():
    if not os.path.exists(USER_DATA_JSON_PATH):
        return
    try:
        with open(USER_DATA_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        statuses = data.get("statuses") or {}
        bookmarked_order = int(data.get("bookmarked_order") or 0)

        with db_lock:
            conn = get_db_connection()
            cur = conn.cursor()
            for bid, sinfo in statuses.items():
                if isinstance(sinfo, dict):
                    st = sinfo.get("status")
                    up = sinfo.get("updated_at") or int(time.time())
                else:
                    st = str(sinfo)
                    up = int(time.time())
                if st in ("read", "blacklist", "bookmark", "unread"):
                    cur.execute(
                        "UPDATE shuku_series SET status = ?, is_new = 0, updated_at = ? WHERE book_id = ?",
                        (st, up, str(bid))
                    )
            if bookmarked_order > 0:
                cur.execute(
                    "INSERT OR REPLACE INTO shuku_settings (key, value) VALUES ('bookmarked_order', ?)",
                    (str(bookmarked_order),)
                )
            conn.commit()
            conn.close()
        print(f"[sync_user_data_from_json] Đã đồng bộ {len(statuses)} trạng thái và vị trí #{bookmarked_order} từ JSON vào SQLite.")
    except Exception as e:
        print(f"[sync_user_data_from_json] Lỗi: {e}")

def get_setting(key: str, default: str = "") -> str:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT value FROM shuku_settings WHERE key = ?", (key,))
    row = cur.fetchone()
    conn.close()
    return row["value"] if row else default


def set_setting(key: str, value: str):
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO shuku_settings (key, value) VALUES (?, ?)", (key, str(value)))
        conn.commit()
        conn.close()


def build_shuku_page_url(base_url: str, page: int) -> str:
    base = base_url.rstrip("/")
    if base.endswith(".html"):
        base = base.rsplit("/", 1)[0]
    if page <= 1:
        return f"{base}/"
    return f"{base}/index_{page}.html"


def detect_is_chuanshu_shuku(title_cn: str, tags_cn: List[str], desc_cn: str) -> bool:
    if "穿书" in (tags_cn or []) or "穿书文" in (tags_cn or []):
        return True
    combined = f"{title_cn or ''}\n{desc_cn or ''}"
    for kw in CHUANSHU_INDICATORS:
        if kw in combined:
            return True
    return False


def detect_is_sweet_shuku(tags_cn: List[str], desc_cn: str = "") -> bool:
    for t in (tags_cn or []):
        if any(sw in t for sw in SWEET_INDICATORS):
            return True
    if "内容标签：" in (desc_cn or "") or "内容标签:" in (desc_cn or ""):
        m = re.search(r"内容标签[：:]([^\n]+)", desc_cn)
        if m and any(sw in m.group(1) for sw in SWEET_INDICATORS):
            return True
    return False


_JJWXC_TITLES_CACHE = None


def _get_jjwxc_titles() -> set:
    global _JJWXC_TITLES_CACHE
    if _JJWXC_TITLES_CACHE is not None:
        return _JJWXC_TITLES_CACHE
    jj_db = os.path.join(DATA_DIR, "jjwxc_tracker.db")
    if not os.path.exists(jj_db):
        _JJWXC_TITLES_CACHE = set()
        return _JJWXC_TITLES_CACHE
    try:
        c = sqlite3.connect(jj_db)
        _JJWXC_TITLES_CACHE = set(r[0] for r in c.execute("SELECT title_cn FROM jjwxc_series").fetchall() if r[0])
        c.close()
    except Exception:
        _JJWXC_TITLES_CACHE = set()
    return _JJWXC_TITLES_CACHE


def detect_shuku_source(title_cn: str, short_desc_cn: str, full_desc_cn: str = "", detail_fetched: int = 0) -> str:
    """
    Nhận diện nguồn gốc truyện trên 52Shuku:
    - 'jjwxc'   : Tấn Giang (JJWXC) - có khung 内容标签 / 搜索关键字 / 一句话简介 / 立意 hoặc trùng kho JJWXC
    - 'fanqie'  : Fanqie (Cà Chua / 番茄小说) - có 【双男主...】 / 【主攻+...】 / 标签：双男主
    - 'changpei': Trường Bội (长佩 / Gongzicp)
    - 'feiwen'  : Phế Văn (废文 / Sosadfun)
    - 'haitang' : Hải Đường / PO18 (海棠 / PO18)
    - 'other'   : Nguồn khác (đã cào chi tiết nhưng không rõ nền tảng)
    """
    desc = f"{short_desc_cn or ''}\n{full_desc_cn or ''}"
    if any(k in desc for k in ("内容标签：", "内容标签:", "搜索关键字：", "一句话简介：", "立意：", "晋江")) or (title_cn in _get_jjwxc_titles()):
        return "jjwxc"
    if any(k in desc for k in ("长佩", "CP完结", "首发长佩", "gongzicp", "长佩文学", "首发CP")):
        return "changpei"
    if any(k in desc for k in ("废文", "sosad", "sosadfun", "feiwang", "废文网")):
        return "feiwen"
    if any(k in desc for k in ("海棠", "po18", "PO18", "海棠文化", "海棠文学")):
        return "haitang"
    if any(k in desc for k in ("番茄", "双男主", "标签：")) or re.search(r"【[^】]*(?:主攻|双洁|1v1|1V1|反派|快穿|穿书)[^】]*】", desc):
        return "fanqie"
    if detail_fetched == 1 and full_desc_cn:
        return "other"
    return ""


def parse_shuku_article(art) -> Optional[Dict]:
    a_el = art.select_one("header h2 a")
    if not a_el:
        return None
    raw_heading = a_el.get_text(strip=True)
    url = (a_el.get("href") or "").strip()
    if not url:
        return None

    # Extract book_id from URL, e.g., https://www.52shuku.net/chongsheng/05_b/bkfLa.html -> chongsheng_05_b_bkfLa
    m_path = re.search(r"52shuku\.net/([^/]+)/([^/]+)/([^/.]+)\.html", url)
    if m_path:
        cat_code = m_path.group(1)
        book_id = f"{m_path.group(1)}_{m_path.group(3)}"
    else:
        cat_code = "bl"
        book_id = re.sub(r"[^a-zA-Z0-9_-]", "_", url.split("/")[-1].replace(".html", ""))

    read_url = url.replace(".html", "_2.html")

    # Parse raw_heading: e.g. "直男，但标记龙傲天好兄弟_奶鲨【完结+番外】"
    status_badge = "完结"
    m_badge = re.search(r"【([^】]+)】", raw_heading)
    if m_badge:
        status_badge = m_badge.group(1).strip()
        raw_heading_clean = re.sub(r"【[^】]+】", "", raw_heading).strip()
    else:
        raw_heading_clean = raw_heading.strip()

    if "_" in raw_heading_clean:
        parts = raw_heading_clean.rsplit("_", 1)
        title_cn = parts[0].strip()
        author_cn = parts[1].strip()
    else:
        title_cn = raw_heading_clean
        author_cn = "Khuyết Danh"

    note_el = art.select_one(".note")
    raw_note = note_el.get_text(" ", strip=True) if note_el else ""
    # Strip leading "《...》作者：...【完结】 简介："
    short_desc_cn = re.sub(r"^《[^》]+》\s*作者[：:][^\s【]+(?:【[^】]+】)?\s*(?:简介[：:])?\s*", "", raw_note).strip()

    date_el = art.select_one(".auth-span .muted")
    pub_date = date_el.get_text(strip=True).strip("()") if date_el else ""

    tags_cn = ["主攻文"]
    if detect_is_chuanshu_shuku(title_cn, tags_cn, short_desc_cn):
        tags_cn.append("穿书")
    if detect_is_quick_trans(title_cn, tags_cn, short_desc_cn):
        tags_cn.append("快穿")
    if any(kw in f"{title_cn} {short_desc_cn}" for kw in ("生子", "怀孕", "揣崽", "生崽", "带球跑")):
        tags_cn.append("生子")

    tags_vi = [translate_tag(t) for t in tags_cn]
    if detect_is_sweet_shuku(tags_cn, short_desc_cn):
        return None
    is_cs = 1 if detect_is_chuanshu_shuku(title_cn, tags_cn, short_desc_cn) else 0
    is_qt = 1 if detect_is_quick_trans(title_cn, tags_cn, short_desc_cn) else 0
    is_sw = 0

    return {
        "book_id": book_id,
        "title_cn": title_cn,
        "title_hv": to_hanviet(title_cn),
        "title_vi": to_smart_title_vi(title_cn),
        "author_cn": author_cn,
        "author_hv": to_hanviet(author_cn),
        "status_badge": status_badge,
        "url": url,
        "read_url": read_url,
        "category_code": cat_code,
        "pub_date": pub_date,
        "tags_cn_json": json.dumps(tags_cn, ensure_ascii=False),
        "tags_vi_json": json.dumps(tags_vi, ensure_ascii=False),
        "short_desc_cn": short_desc_cn,
        "short_desc_hv": to_hanviet(short_desc_cn) if short_desc_cn else "",
        "is_chuanshu": is_cs,
        "is_quick_trans": is_qt,
        "is_sweet": is_sw,
    }


def fetch_shuku_list_page(url: str, retries: int = 4) -> Tuple[List[Dict], int]:
    global _profile_idx
    last_err = None
    for attempt in range(retries):
        profile = IMPERSONATE_PROFILES[_profile_idx % len(IMPERSONATE_PROFILES)]
        _profile_idx += 1
        try:
            resp = cf_requests.get(url, impersonate=profile, timeout=20)
            if resp.status_code != 200:
                last_err = f"HTTP {resp.status_code}"
                time.sleep(1.5 * (attempt + 1))
                continue

            html_text = resp.content.decode("utf-8", errors="replace")
            soup = BeautifulSoup(html_text, "lxml")

            max_page = 1
            pag = soup.select_one(".pagination2")
            if pag:
                for a in pag.select("a"):
                    href = a.get("href", "")
                    m_pg = re.search(r"index_(\d+)\.html", href)
                    if m_pg:
                        max_page = max(max_page, int(m_pg.group(1)))

            items = []
            for art in soup.select("article.excerpt"):
                parsed = parse_shuku_article(art)
                if parsed:
                    items.append(parsed)

            return items, max_page
        except Exception as e:
            last_err = str(e)
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Không thể tải trang 52shuku {url}: {last_err}")


def upsert_shuku_batch(items: List[Dict], mark_as_new: bool = False) -> List[Dict]:
    now = int(time.time())
    new_items = []
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(fixed_order), 0) as max_ord FROM shuku_series")
        max_order = cur.fetchone()["max_ord"] or 0

        cur.execute("SELECT book_id, detail_fetched FROM shuku_series")
        existing_map = {r["book_id"]: r["detail_fetched"] for r in cur.fetchall()}

        for item in items:
            bid = item["book_id"]
            if bid in existing_map:
                if existing_map[bid] == 0:
                    cur.execute("""
                        UPDATE shuku_series SET
                            title_cn = ?, title_hv = ?, title_vi = ?,
                            author_cn = ?, author_hv = ?, status_badge = ?,
                            pub_date = ?, short_desc_cn = ?, short_desc_hv = ?,
                            updated_at = ?
                        WHERE book_id = ?
                    """, (
                        item["title_cn"], item["title_hv"], item["title_vi"],
                        item["author_cn"], item["author_hv"], item["status_badge"],
                        item["pub_date"], item["short_desc_cn"], item["short_desc_hv"],
                        now, bid
                    ))
            else:
                max_order += 1
                existing_map[bid] = 0
                is_new_val = 1 if mark_as_new else 0
                src_site = detect_shuku_source(item["title_cn"], item["short_desc_cn"], "", 0)
                cur.execute("""
                    INSERT INTO shuku_series (
                        book_id, fixed_order, title_cn, title_hv, title_vi,
                        author_cn, author_hv, status_badge, url, read_url,
                        category_code, pub_date, tags_cn_json, tags_vi_json,
                        short_desc_cn, short_desc_hv,
                        is_chuanshu, is_quick_trans, is_sweet,
                        source_site, status, is_new, first_seen_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'unread', ?, ?, ?)
                """, (
                    bid, max_order, item["title_cn"], item["title_hv"], item["title_vi"],
                    item["author_cn"], item["author_hv"], item["status_badge"],
                    item["url"], item["read_url"], item["category_code"], item["pub_date"],
                    item["tags_cn_json"], item["tags_vi_json"],
                    item["short_desc_cn"], item["short_desc_hv"],
                    item["is_chuanshu"], item["is_quick_trans"], item["is_sweet"],
                    src_site, is_new_val, now, now
                ))
                item_copy = dict(item)
                item_copy["fixed_order"] = max_order
                new_items.append(item_copy)

        conn.commit()
        conn.close()
    return new_items


def run_shuku_sync(max_pages: int = 48, mode: str = "full"):
    if sync_state["is_syncing"]:
        return

    sync_state["is_syncing"] = True
    sync_state["error"] = None
    is_initial = get_setting("initial_sync_done", "0") == "0"
    sync_state["mode"] = "initial" if is_initial else mode
    target_url = get_setting("target_url", DEFAULT_SHUKU_URL)

    try:
        sync_state["current_page"] = 1
        sync_state["message"] = "Đang tải trang 1 từ 52shuku..."
        first_items, detected_max_page = fetch_shuku_list_page(build_shuku_page_url(target_url, 1))
        pages_to_scan = min(detected_max_page, max_pages) if (is_initial or mode == "full") else min(3, detected_max_page)
        sync_state["total_pages"] = pages_to_scan

        total_added = 0
        added = upsert_shuku_batch(first_items, mark_as_new=(not is_initial))
        total_added += len(added)

        for pg in range(2, pages_to_scan + 1):
            sync_state["current_page"] = pg
            sync_state["message"] = f"Đang cào danh sách 52shuku: Trang {pg}/{pages_to_scan}..."
            page_url = build_shuku_page_url(target_url, pg)
            items, _ = fetch_shuku_list_page(page_url)
            if not items:
                break
            added_pg = upsert_shuku_batch(items, mark_as_new=(not is_initial))
            total_added += len(added_pg)
            time.sleep(0.5)

        now = int(time.time())
        set_setting("initial_sync_done", "1")
        set_setting("last_sync_at", str(now))
        sync_state["last_sync_at"] = now
        sync_state["last_new_count"] = total_added
        sync_state["message"] = f"Hoàn tất đồng bộ {pages_to_scan} trang 52shuku ({total_added} bộ mới)."
    except Exception as e:
        sync_state["error"] = str(e)
        sync_state["message"] = f"Lỗi đồng bộ 52shuku: {e}"
    finally:
        sync_state["is_syncing"] = False


def fetch_and_cache_shuku_detail(book_id: str, translate_vi: bool = True) -> Optional[Dict]:
    """
    Lấy chi tiết từ trang index của truyện (`bkxxx.html`) và trang 1 (`bkxxx_2.html`):
    - Danh sách Tag chuyên đề (`所属专题`)
    - Tổng số trang đọc (`page_count`) & ước tính số chữ (`page_count * 2200`)
    - Toàn bộ Văn án đầy đủ + Hướng dẫn đọc/Gỡ mìn (`食用指南`) trước Chương 1
    - CP Nhân vật chính (`主角：...`) & Tóm tắt 1 câu (`一句话简介：...`)
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM shuku_series WHERE book_id = ?", (book_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None

    item = dict(row)
    if item.get("detail_fetched") == 1 and item.get("full_desc_cn"):
        if translate_vi and (not item.get("full_desc_vi") or not item.get("full_desc_en")):
            with ThreadPoolExecutor(max_workers=2) as pool:
                f_vi = pool.submit(translate_free_google, item["full_desc_cn"], "zh-CN", "vi") if not item.get("full_desc_vi") else None
                f_en = pool.submit(translate_free_google, item["full_desc_cn"], "zh-CN", "en") if not item.get("full_desc_en") else None
                vi_text = f_vi.result() if f_vi else item.get("full_desc_vi", "")
                en_text = f_en.result() if f_en else item.get("full_desc_en", "")
            with db_lock:
                conn = get_db_connection()
                conn.execute(
                    "UPDATE shuku_series SET full_desc_vi = ?, full_desc_en = ? WHERE book_id = ?",
                    (vi_text, en_text, book_id),
                )
                conn.commit()
                conn.close()
            item["full_desc_vi"] = vi_text
            item["full_desc_en"] = en_text
        return item

    url_main = item["url"]
    url_p1 = item["read_url"]

    tags_cn: List[str] = []
    page_count = 0
    full_desc_cn = item.get("short_desc_cn") or ""
    protagonist_cn = ""
    one_line_cn = ""

    # 1. Fetch main index page for tags (所属专题) and page count (ul.list li.mulu)
    try:
        r_main = cf_requests.get(url_main, impersonate="chrome120", timeout=15)
        if r_main.status_code == 200:
            s_main = BeautifulSoup(r_main.content.decode("utf-8", errors="replace"), "lxml")
            art_main = s_main.select_one("article.article-content")
            if art_main:
                mulu_items = art_main.select("ul.list li.mulu")
                page_count = len(mulu_items)
                for p_el in art_main.find_all("p"):
                    txt_p = p_el.get_text(" ", strip=True)
                    if "所属专题" in txt_p:
                        for a_tag in p_el.find_all("a"):
                            t_name = a_tag.get_text(strip=True)
                            if t_name and t_name != item["author_cn"] and t_name not in tags_cn:
                                tags_cn.append(t_name)
    except Exception:
        pass

    # 2. Fetch _2.html (Page 1 of reading) to extract complete synopsis before Chapter 1
    try:
        r_p1 = cf_requests.get(url_p1, impersonate="chrome120", timeout=15)
        if r_p1.status_code == 200:
            s_p1 = BeautifulSoup(r_p1.content.decode("utf-8", errors="replace"), "lxml")
            art_p1 = s_p1.select_one("article.article-content")
            if art_p1:
                # 52shuku chèn thẻ <a href="/Tags/...">...</a> vào giữa câu để SEO từ khóa (như 主攻, 龙傲天, 破镜重圆, 病娇...).
                # Nếu gọi get_text("\n") trực tiếp sẽ làm đứt câu tại mọi thẻ <a>!
                # Do đó phải unwrap toàn bộ thẻ inline (a, span, strong, b, em) và chuyển <br> thành \n trước khi lấy text.
                for br in art_p1.find_all("br"):
                    br.replace_with("\n")
                for inline_tag in art_p1.find_all(["a", "span", "strong", "b", "em", "i", "font"]):
                    inline_tag.unwrap()

                raw_paragraphs = []
                p_tags = art_p1.find_all("p")
                if p_tags:
                    for p_el in p_tags:
                        raw_paragraphs.append(p_el.get_text("", strip=False))
                else:
                    raw_paragraphs.append(art_p1.get_text("\n", strip=False))

                lines = []
                for blk in "\n".join(raw_paragraphs).splitlines():
                    ln = blk.strip()
                    if not ln or "52书库" in ln or "传送门" in ln or ln.startswith("目录"):
                        continue
                    lines.append(ln)

                intro_lines = []
                ch1_pat = re.compile(r"^(?:第\s*[1一]\s*[章回]|楔子|序章|Chapter\s*1|01\.|1\.)")
                for idx_ln, ln in enumerate(lines):
                    if idx_ln > 2 and ch1_pat.match(ln):
                        break
                    if ln.startswith("主角：") or ln.startswith("主角:"):
                        protagonist_cn = ln.split("┃")[0].strip()
                    elif ln.startswith("一句话简介：") or ln.startswith("一句话简介:"):
                        one_line_cn = re.sub(r"^一句话简介[：:]\s*", "", ln).strip()
                    elif ln.startswith("内容标签：") or ln.startswith("内容标签:"):
                        raw_inline_tags = re.sub(r"^内容标签[：:]\s*", "", ln).strip()
                        for rt in re.split(r"[\s,，、/]+", raw_inline_tags):
                            if rt and rt not in tags_cn:
                                tags_cn.append(rt)
                    intro_lines.append(ln)
                    if len(intro_lines) >= 55:
                        break

                if intro_lines:
                    full_desc_cn = "\n".join(intro_lines)
    except Exception:
        pass

    if not tags_cn:
        tags_cn = json.loads(item.get("tags_cn_json") or '["主攻文"]')
    if "生子" not in tags_cn and "生子文" not in tags_cn:
        if any(kw in f"{item.get('title_cn', '')} {full_desc_cn}" for kw in ("生子", "怀孕", "揣崽", "生崽", "带球跑")):
            tags_cn.append("生子")

    tags_vi = [translate_tag(t) for t in tags_cn]
    est_words = page_count * 2200 if page_count > 0 else 0
    full_desc_hv = to_hanviet(full_desc_cn) if full_desc_cn else ""
    protagonist_hv = to_hanviet(protagonist_cn) if protagonist_cn else ""
    one_line_hv = to_hanviet(one_line_cn) if one_line_cn else ""

    is_cs = 1 if detect_is_chuanshu_shuku(item["title_cn"], tags_cn, full_desc_cn) else 0
    is_qt = 1 if detect_is_quick_trans(item["title_cn"], tags_cn, item.get("short_desc_cn", ""), full_desc_cn) else 0
    is_sw = 1 if detect_is_sweet_shuku(tags_cn, full_desc_cn) else 0
    source_site = detect_shuku_source(item["title_cn"], item.get("short_desc_cn", ""), full_desc_cn, detail_fetched=1)

    if is_sw == 1:
        with db_lock:
            conn = get_db_connection()
            conn.execute("DELETE FROM shuku_series WHERE book_id = ?", (book_id,))
            conn.commit()
            conn.close()
        return None

    full_desc_vi = item.get("full_desc_vi") or ""
    full_desc_en = item.get("full_desc_en") or ""
    if translate_vi and full_desc_cn and (not full_desc_vi or not full_desc_en):
        with ThreadPoolExecutor(max_workers=2) as pool:
            f_vi = pool.submit(translate_free_google, full_desc_cn, "zh-CN", "vi") if not full_desc_vi else None
            f_en = pool.submit(translate_free_google, full_desc_cn, "zh-CN", "en") if not full_desc_en else None
            if f_vi:
                full_desc_vi = f_vi.result()
            if f_en:
                full_desc_en = f_en.result()

    with db_lock:
        conn = get_db_connection()
        conn.execute("""
            UPDATE shuku_series SET
                page_count = ?,
                est_words = ?,
                tags_cn_json = ?,
                tags_vi_json = ?,
                full_desc_cn = ?,
                full_desc_hv = ?,
                full_desc_vi = ?,
                full_desc_en = ?,
                protagonist_cn = ?,
                protagonist_hv = ?,
                one_line_cn = ?,
                one_line_hv = ?,
                is_chuanshu = ?,
                is_quick_trans = ?,
                is_sweet = ?,
                source_site = ?,
                detail_fetched = 1,
                updated_at = ?
            WHERE book_id = ?
        """, (
            page_count, est_words,
            json.dumps(tags_cn, ensure_ascii=False),
            json.dumps(tags_vi, ensure_ascii=False),
            full_desc_cn, full_desc_hv, full_desc_vi, full_desc_en,
            protagonist_cn, protagonist_hv,
            one_line_cn, one_line_hv,
            is_cs, is_qt, is_sw, source_site,
            int(time.time()), book_id
        ))
        conn.commit()
        conn.close()

    conn = get_db_connection()
    updated = dict(conn.execute("SELECT * FROM shuku_series WHERE book_id = ?", (book_id,)).fetchone())
    conn.close()
    return updated


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

async def api_shuku_list_series(request):
    qp = request.query_params
    tab = qp.get("tab", "unread")
    page = max(1, int(qp.get("page", "1") or "1"))
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    search = qp.get("q", "").strip()
    tag_filter = qp.get("tag", "").strip()
    source_filter = qp.get("src", "").strip()
    sort_by = qp.get("sort", "fixed_asc")

    only_cs_param = qp.get("only_cs")
    if only_cs_param is not None:
        only_cs = only_cs_param == "1"
        set_setting("only_chuanshu", "1" if only_cs else "0")
    else:
        only_cs = get_setting("only_chuanshu", "1") == "1"

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

    local_filter_clauses = []
    local_filter_params = []

    if only_cs:
        local_filter_clauses.append("is_chuanshu = 1")
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

    if source_filter == "non_jjwxc":
        where_clauses.append("source_site != 'jjwxc'")
    elif source_filter == "changpei_feiwen":
        where_clauses.append("source_site IN ('changpei', 'feiwen', 'haitang', 'changpei_feiwen')")
    elif source_filter in ("jjwxc", "fanqie", "changpei", "feiwen", "haitang", "other"):
        where_clauses.append("source_site = ?")
        params.append(source_filter)

    where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

    order_map = {
        "fixed_asc": "fixed_order ASC",
        "fixed_desc": "fixed_order DESC",
        "words_desc": "est_words DESC, fixed_order ASC",
        "pub_desc": "pub_date DESC, fixed_order ASC",
    }
    order_sql = order_map.get(sort_by, "fixed_order ASC")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) as total FROM shuku_series {where_sql}", params)
    total_filtered = cur.fetchone()["total"]

    offset = (page - 1) * per_page
    cur.execute(
        f"SELECT * FROM shuku_series {where_sql} ORDER BY {order_sql} LIMIT ? OFFSET ?",
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

    lf_sql = (" AND " + " AND ".join(local_filter_clauses)) if local_filter_clauses else ""
    cur.execute(f"SELECT COUNT(*) as c FROM shuku_series WHERE status = 'unread' {lf_sql}", local_filter_params)
    unread_count = cur.fetchone()["c"]

    cur.execute("""
        SELECT
            SUM(CASE WHEN status = 'read' THEN 1 ELSE 0 END) as read_count,
            SUM(CASE WHEN status = 'blacklist' THEN 1 ELSE 0 END) as blacklist_count,
            SUM(CASE WHEN status = 'bookmark' THEN 1 ELSE 0 END) as bookmark_count,
            SUM(CASE WHEN is_chuanshu = 1 THEN 1 ELSE 0 END) as cs_total,
            SUM(CASE WHEN is_quick_trans = 1 THEN 1 ELSE 0 END) as qt_total,
            SUM(CASE WHEN is_sweet = 1 THEN 1 ELSE 0 END) as sweet_total,
            COUNT(*) as all_raw_count
        FROM shuku_series
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
            "read": stat_row.get("read_count") or 0,
            "blacklist": stat_row.get("blacklist_count") or 0,
            "bookmark": stat_row.get("bookmark_count") or 0,
            "all_raw": stat_row.get("all_raw_count") or 0,
            "cs_total": stat_row.get("cs_total") or 0,
            "qt_hidden": stat_row.get("qt_total") or 0,
            "sweet_hidden": stat_row.get("sweet_total") or 0,
        },
        "filters": {
            "only_chuanshu": only_cs,
            "hide_quick_trans": hide_qt,
            "hide_sweet": hide_sweet,
            "excluded_tags": excluded_tags,
        },
        "sync_state": sync_state,
        "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
    })


async def api_shuku_detail(request):
    book_id = request.query_params.get("book_id", "").strip()
    translate_vi = request.query_params.get("tr", "1") == "1"
    if not book_id:
        return JSONResponse({"error": "Thiếu book_id"}, status_code=400)
    try:
        item = fetch_and_cache_shuku_detail(book_id, translate_vi=translate_vi)
        if not item:
            return JSONResponse({"error": "Không tìm thấy truyện"}, status_code=404)
        item["tags_cn"] = json.loads(item.get("tags_cn_json") or "[]")
        item["tags_vi"] = json.loads(item.get("tags_vi_json") or "[]")
        return JSONResponse({"ok": True, "item": item})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


async def api_shuku_batch_meta(request):
    body = await request.json()
    book_ids = [str(x).strip() for x in (body.get("book_ids") or []) if str(x).strip()][:25]
    if not book_ids:
        return JSONResponse({"ok": True, "items": {}})

    def _fetch_one(bid: str):
        try:
            return bid, fetch_and_cache_shuku_detail(bid, translate_vi=False)
        except Exception:
            return bid, None

    results = {}
    with ThreadPoolExecutor(max_workers=6) as pool:
        for bid, item in pool.map(_fetch_one, book_ids):
            if item:
                results[bid] = {
                    "book_id": bid,
                    "page_count": item.get("page_count") or 0,
                    "est_words": item.get("est_words") or 0,
                    "tags_cn": json.loads(item.get("tags_cn_json") or "[]"),
                    "tags_vi": json.loads(item.get("tags_vi_json") or "[]"),
                    "protagonist_cn": item.get("protagonist_cn") or "",
                    "protagonist_hv": item.get("protagonist_hv") or "",
                    "one_line_cn": item.get("one_line_cn") or "",
                    "one_line_hv": item.get("one_line_hv") or "",
                    "is_chuanshu": item.get("is_chuanshu") or 0,
                    "is_quick_trans": item.get("is_quick_trans") or 0,
                    "is_sweet": item.get("is_sweet") or 0,
                    "source_site": item.get("source_site") or "",
                }
    return JSONResponse({"ok": True, "items": results})


async def api_shuku_update_status(request):
    body = await request.json()
    book_id = str(body.get("book_id") or "").strip()
    new_status = body.get("status")
    if not book_id or new_status not in ("unread", "read", "blacklist", "bookmark"):
        return JSONResponse({"error": "Tham số không hợp lệ"}, status_code=400)

    with db_lock:
        conn = get_db_connection()
        conn.execute(
            "UPDATE shuku_series SET status = ?, is_new = 0, updated_at = ? WHERE book_id = ?",
            (new_status, int(time.time()), book_id),
        )
        conn.commit()
        conn.close()
    dump_user_data_to_json()
    return JSONResponse({"ok": True, "book_id": book_id, "status": new_status})


async def api_shuku_bookmark(request):
    body = await request.json()
    fixed_order = int(body.get("fixed_order", 0) or 0)
    set_setting("bookmarked_order", str(fixed_order))
    dump_user_data_to_json()
    return JSONResponse({"ok": True, "bookmarked_order": fixed_order})


async def api_shuku_jump_bookmark(request):
    qp = request.query_params
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    bookmarked_order = int(get_setting("bookmarked_order", "0") or "0")
    if bookmarked_order <= 0:
        return JSONResponse({"ok": False, "message": "Chưa có vị trí nào được đánh dấu."})

    only_cs = get_setting("only_chuanshu", "1") == "1"
    hide_qt = get_setting("hide_quick_trans", "1") == "1"
    hide_sweet = get_setting("hide_sweet", "1") == "1"
    clauses = ["status = 'unread'", "fixed_order <= ?"]
    if only_cs:
        clauses.append("is_chuanshu = 1")
    if hide_qt:
        clauses.append("is_quick_trans = 0")
    if hide_sweet:
        clauses.append("is_sweet = 0")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) as pos FROM shuku_series WHERE {' AND '.join(clauses)}", (bookmarked_order,))
    pos = cur.fetchone()["pos"] or 1
    conn.close()
    target_page = max(1, (pos + per_page - 1) // per_page)
    return JSONResponse({"ok": True, "bookmarked_order": bookmarked_order, "target_page": target_page})


async def api_shuku_trigger_sync(request):
    body = await request.json()
    mode = body.get("mode", "full")
    if sync_state["is_syncing"]:
        return JSONResponse({"ok": False, "message": "Đang đồng bộ 52shuku, vui lòng đợi..."}, status_code=409)

    threading.Thread(
        target=run_shuku_sync,
        kwargs={"max_pages": 48, "mode": mode},
        daemon=True,
    ).start()
    return JSONResponse({"ok": True, "mode": mode})


async def api_shuku_sync_status(request):
    return JSONResponse({
        "sync_state": sync_state,
        "last_sync_at": int(get_setting("last_sync_at", "0") or "0"),
        "target_url": get_setting("target_url", DEFAULT_SHUKU_URL),
    })


async def api_shuku_settings(request):
    if request.method == "GET":
        return JSONResponse({
            "target_url": get_setting("target_url", DEFAULT_SHUKU_URL),
            "excluded_tags": json.loads(get_setting("excluded_tags", "[]") or "[]"),
            "only_chuanshu": get_setting("only_chuanshu", "1") == "1",
            "hide_quick_trans": get_setting("hide_quick_trans", "1") == "1",
            "hide_sweet": get_setting("hide_sweet", "1") == "1",
            "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
        })
    body = await request.json()
    if "target_url" in body and body["target_url"].strip():
        set_setting("target_url", body["target_url"].strip())
    if "excluded_tags" in body and isinstance(body["excluded_tags"], list):
        set_setting("excluded_tags", json.dumps(body["excluded_tags"], ensure_ascii=False))
    return JSONResponse({"ok": True})


async def shuku_index_page(request):
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


def start_background_sync_if_needed():
    if get_setting("initial_sync_done", "0") == "0":
        threading.Thread(
            target=run_shuku_sync,
            kwargs={"max_pages": 48, "mode": "full"},
            daemon=True,
        ).start()


init_db()

routes = [
    Route("/", shuku_index_page),
    Route("/shuku", shuku_index_page),
    Route("/api/shuku/series", api_shuku_list_series, methods=["GET"]),
    Route("/api/shuku/detail", api_shuku_detail, methods=["GET"]),
    Route("/api/shuku/batch-meta", api_shuku_batch_meta, methods=["POST"]),
    Route("/api/shuku/status", api_shuku_update_status, methods=["POST"]),
    Route("/api/shuku/bookmark", api_shuku_bookmark, methods=["POST"]),
    Route("/api/shuku/jump-bookmark", api_shuku_jump_bookmark, methods=["GET"]),
    Route("/api/shuku/sync", api_shuku_trigger_sync, methods=["POST"]),
    Route("/api/shuku/sync-status", api_shuku_sync_status, methods=["GET"]),
    Route("/api/shuku/settings", api_shuku_settings, methods=["GET", "POST"]),
    Mount("/static/shuku", StaticFiles(directory=STATIC_DIR), name="static_shuku"),
]

try:
    from jjwxc_tracker_server import (
        jjwxc_index_page,
        api_jjwxc_list_series,
        api_jjwxc_detail,
        api_jjwxc_batch_meta,
        api_jjwxc_update_status,
        api_jjwxc_bookmark,
        api_jjwxc_jump_bookmark,
        api_jjwxc_trigger_sync,
        api_jjwxc_sync_status,
        api_jjwxc_settings,
        api_jjwxc_proxy_image,
    )
    routes.extend([
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
    ])
except Exception:
    pass

app = Starlette(
    debug=False,
    routes=routes,
    middleware=[Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])],
)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=int(os.environ.get("SHUKU_PORT", 8688)))
    args = parser.parse_args()
    start_background_sync_if_needed()
    print(f"📖 52Shuku Series Tracker đang chạy tại: http://localhost:{args.port}")
    uvicorn.run(app, host="127.0.0.1", port=args.port, log_level="warning")
