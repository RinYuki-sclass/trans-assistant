import os
import sys
import re
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

from bs4 import BeautifulSoup
from curl_cffi import requests as cf_requests
from starlette.applications import Starlette
from starlette.responses import JSONResponse, FileResponse, Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
import uvicorn

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static", "nu_tracker")
CACHE_IMG_DIR = os.path.join(DATA_DIR, "cache", "nu_covers")
DB_PATH = os.path.join(DATA_DIR, "nu_tracker.db")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(CACHE_IMG_DIR, exist_ok=True)

DEFAULT_TARGET_URL = "https://www.novelupdates.com/series-finder/?sf=1&org=497&gi=560&mgi=and&sort=sdate&order=desc"

db_lock = threading.Lock()

sync_state = {
    "is_syncing": False,
    "mode": "",          # "initial" | "full" | "check_new"
    "current_page": 0,
    "total_pages": 0,
    "message": "Sẵn sàng",
    "last_sync_at": 0,
    "last_new_count": 0,
    "error": None,
}


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS series (
                series_id TEXT PRIMARY KEY,
                fixed_order INTEGER,
                title TEXT,
                url TEXT,
                image_url TEXT,
                origin TEXT,
                rating REAL,
                rating_text TEXT,
                chapters TEXT,
                chapters_num INTEGER,
                frequency TEXT,
                readers TEXT,
                readers_num INTEGER,
                reviews TEXT,
                reviews_num INTEGER,
                last_updated TEXT,
                genres_json TEXT,
                short_desc TEXT,
                full_desc TEXT,
                status TEXT DEFAULT 'unread',
                is_new INTEGER DEFAULT 0,
                first_seen_at INTEGER,
                updated_at INTEGER
            )
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_series_fixed_order ON series(fixed_order)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_series_status ON series(status)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_series_is_new ON series(is_new)")

        cur.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                series_id TEXT,
                title TEXT,
                url TEXT,
                image_url TEXT,
                created_at INTEGER,
                is_read INTEGER DEFAULT 0
            )
        """)

        defaults = {
            "target_url": DEFAULT_TARGET_URL,
            "initial_sync_done": "0",
            "last_sync_at": "0",
            "auto_check_minutes": "15",
            "bookmarked_order": "0",
            "excluded_tags": "[]",
        }
        for k, v in defaults.items():
            cur.execute("INSERT OR IGNORE INTO settings (key, value) VALUES (?, ?)", (k, v))

        conn.commit()
        conn.close()


def get_setting(key: str, default: str = "") -> str:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT value FROM settings WHERE key = ?", (key,))
    row = cur.fetchone()
    conn.close()
    return row["value"] if row else default


def set_setting(key: str, value: str):
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, str(value)))
        conn.commit()
        conn.close()


def extract_int(text: str) -> int:
    m = re.search(r"(\d[\d,]*)", text or "")
    if not m:
        return 0
    return int(m.group(1).replace(",", ""))


def parse_series_box(box) -> Optional[Dict]:
    a_el = box.select_one(".search_title a")
    if not a_el:
        return None
    title = a_el.get_text(strip=True)
    url = a_el.get("href", "").strip()
    if url.startswith("//"):
        url = "https:" + url

    sid_el = box.select_one("[id^=sid]")
    if sid_el and sid_el.get("id"):
        series_id = sid_el.get("id").strip()
    else:
        slug = url.rstrip("/").split("/")[-1]
        series_id = f"slug_{slug}" if slug else f"title_{hash(title)}"

    img_el = box.select_one(".search_img_nu img")
    image_url = img_el.get("src", "").strip() if img_el else ""
    if image_url.startswith("//"):
        image_url = "https:" + image_url

    ratings_el = box.select_one(".search_ratings")
    ratings_raw = ratings_el.get_text(" ", strip=True) if ratings_el else "KR (0.0)"
    origin_el = ratings_el.select_one("span") if ratings_el else None
    origin = origin_el.get_text(strip=True) if origin_el else "KR"
    rating_match = re.search(r"\(([\d.]+)\)", ratings_raw)
    rating_val = float(rating_match.group(1)) if rating_match else 0.0
    rating_text = f"({rating_val:.1f})" if rating_match else "(0.0)"

    chapters = "0 Chapters"
    frequency = "N/A"
    readers = "0 Readers"
    reviews = "0 Reviews"
    last_updated = "N/A"

    for ss in box.select(".search_stats .ss_desk"):
        txt = ss.get_text(" ", strip=True)
        icon = ss.select_one("i")
        cls = " ".join(icon.get("class", [])) if icon else ""
        if "fa-list-alt" in cls or "Chapter" in txt:
            chapters = txt
        elif "fa-bolt" in cls or "Every" in txt:
            frequency = txt
        elif "fa-user" in cls or "Reader" in txt:
            readers = txt
        elif "fa-pencil" in cls or "Review" in txt:
            reviews = txt
        elif "fa-calendar" in cls:
            last_updated = txt

    genres = [g.get_text(strip=True) for g in box.select(".search_genre a") if g.get_text(strip=True)]

    body_el = box.select_one(".search_body_nu")
    short_desc = ""
    full_desc = ""
    if body_el:
        body_clone = BeautifulSoup(str(body_el), "lxml").select_one(".search_body_nu")
        for sel in [".search_title", ".search_stats", ".search_genre", ".morelink", ".dots"]:
            for el in body_clone.select(sel):
                el.decompose()
        testhide = body_clone.select_one(".testhide")
        extra_paragraphs = []
        if testhide:
            for p_text in testhide.stripped_strings:
                if p_text and p_text not in ("<<less", "more>>"):
                    extra_paragraphs.append(p_text)
            testhide.decompose()
        short_desc = body_clone.get_text(" ", strip=True)
        if extra_paragraphs:
            full_desc = short_desc + "\n\n" + "\n\n".join(extra_paragraphs)
        else:
            full_desc = short_desc

    return {
        "series_id": series_id,
        "title": title,
        "url": url,
        "image_url": image_url,
        "origin": origin,
        "rating": rating_val,
        "rating_text": rating_text,
        "chapters": chapters,
        "chapters_num": extract_int(chapters),
        "frequency": frequency,
        "readers": readers,
        "readers_num": extract_int(readers),
        "reviews": reviews,
        "reviews_num": extract_int(reviews),
        "last_updated": last_updated,
        "genres_json": json.dumps(genres, ensure_ascii=False),
        "short_desc": short_desc,
        "full_desc": full_desc,
    }


def build_page_url(base_url: str, page: int, order: Optional[str] = None, sort: Optional[str] = None) -> str:
    parsed = urllib.parse.urlparse(base_url)
    qs = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    if order:
        qs["order"] = [order]
    if sort:
        qs["sort"] = [sort]
    if page > 1:
        qs["pg"] = [str(page)]
    elif "pg" in qs:
        del qs["pg"]
    new_query = urllib.parse.urlencode(qs, doseq=True)
    return urllib.parse.urlunparse(parsed._replace(query=new_query))


IMPERSONATE_PROFILES = ["chrome120", "chrome124", "edge101", "safari17_0", "chrome116"]
_profile_idx = 0


def fetch_page_series(url: str, retries: int = 8) -> Tuple[List[Dict], int]:
    global _profile_idx
    last_err = None
    for attempt in range(retries):
        profile = IMPERSONATE_PROFILES[_profile_idx % len(IMPERSONATE_PROFILES)]
        _profile_idx += 1
        try:
            resp = cf_requests.get(url, impersonate=profile, timeout=25)
            if resp.status_code == 429 or resp.status_code == 503:
                last_err = f"HTTP {resp.status_code}"
                wait_sec = 22 + attempt * 10
                old_msg = sync_state.get("message", "")
                for rem in range(wait_sec, 0, -1):
                    sync_state["message"] = f"Đang đợi {rem}s để vượt giới hạn tốc độ Cloudflare (Trang {sync_state.get('current_page', '?')})..."
                    time.sleep(1)
                sync_state["message"] = old_msg
                continue
            if resp.status_code != 200:
                last_err = f"HTTP {resp.status_code}"
                time.sleep(3 * (attempt + 1))
                continue
            soup = BeautifulSoup(resp.text, "lxml")
            boxes = soup.select(".search_main_box_nu")
            items = []
            for box in boxes:
                parsed = parse_series_box(box)
                if parsed:
                    items.append(parsed)

            max_page = 1
            pag = soup.select_one(".digg_pagination")
            if pag:
                for a in pag.select("a, em"):
                    txt = a.get_text(strip=True)
                    if txt.isdigit():
                        max_page = max(max_page, int(txt))
            return items, max_page
        except Exception as e:
            last_err = str(e)
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"Không thể tải trang {url}: {last_err}")


def upsert_series_batch(items: List[Dict], mark_as_new: bool = False) -> List[Dict]:
    """
    Lưu danh sách truyện vào DB:
    - Nếu series_id đã tồn tại: chỉ cập nhật thông tin phụ (chapters, readers, rating...),
      GIỮ NGUYÊN fixed_order và status!
    - Nếu series_id chưa tồn tại:
      + Cấp fixed_order = max_order + 1
      + Nếu mark_as_new=True: đặt is_new = 1 và ghi vào bảng notifications.
    Trả về danh sách các bộ MỚI phát hiện.
    """
    now = int(time.time())
    new_items = []
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COALESCE(MAX(fixed_order), 0) as max_ord FROM series")
        max_order = cur.fetchone()["max_ord"] or 0

        cur.execute("SELECT series_id FROM series")
        existing_ids = {r["series_id"] for r in cur.fetchall()}

        for item in items:
            sid = item["series_id"]
            if sid in existing_ids:
                cur.execute("""
                    UPDATE series SET
                        title = ?,
                        url = ?,
                        image_url = ?,
                        origin = ?,
                        rating = ?,
                        rating_text = ?,
                        chapters = ?,
                        chapters_num = ?,
                        frequency = ?,
                        readers = ?,
                        readers_num = ?,
                        reviews = ?,
                        reviews_num = ?,
                        last_updated = ?,
                        genres_json = ?,
                        short_desc = ?,
                        full_desc = ?,
                        updated_at = ?
                    WHERE series_id = ?
                """, (
                    item["title"], item["url"], item["image_url"],
                    item["origin"], item["rating"], item["rating_text"],
                    item["chapters"], item["chapters_num"], item["frequency"],
                    item["readers"], item["readers_num"], item["reviews"],
                    item["reviews_num"], item["last_updated"], item["genres_json"],
                    item["short_desc"], item["full_desc"], now, sid
                ))
            else:
                max_order += 1
                existing_ids.add(sid)
                is_new_val = 1 if mark_as_new else 0
                cur.execute("""
                    INSERT INTO series (
                        series_id, fixed_order, title, url, image_url,
                        origin, rating, rating_text, chapters, chapters_num,
                        frequency, readers, readers_num, reviews, reviews_num,
                        last_updated, genres_json, short_desc, full_desc,
                        status, is_new, first_seen_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'unread', ?, ?, ?)
                """, (
                    sid, max_order, item["title"], item["url"], item["image_url"],
                    item["origin"], item["rating"], item["rating_text"],
                    item["chapters"], item["chapters_num"], item["frequency"],
                    item["readers"], item["readers_num"], item["reviews"],
                    item["reviews_num"], item["last_updated"], item["genres_json"],
                    item["short_desc"], item["full_desc"],
                    is_new_val, now, now
                ))
                item_copy = dict(item)
                item_copy["fixed_order"] = max_order
                new_items.append(item_copy)

                if mark_as_new:
                    cur.execute("""
                        INSERT INTO notifications (series_id, title, url, image_url, created_at, is_read)
                        VALUES (?, ?, ?, ?, ?, 0)
                    """, (sid, item["title"], item["url"], item["image_url"], now))

        conn.commit()
        conn.close()
    return new_items


def run_full_snapshot_sync(max_desc_pages: int = 100, include_asc_tail: bool = True):
    """
    Quét toàn bộ danh sách để cố định thứ tự (Snapshot).
    - Nếu `initial_sync_done == '0'`, tự động tiếp tục từ `last_synced_page` (hoặc trang 1) cho tới hết 100 trang,
      và đặt `is_new = 0` (làm mốc chuẩn).
    - Nếu database đã có mốc chuẩn mà người dùng bấm Quét Toàn Bộ bổ sung, những bộ chưa từng có
      sẽ được nối vào cuối danh sách để không làm lệch thứ tự các trang cũ.
    """
    if sync_state["is_syncing"]:
        return

    sync_state["is_syncing"] = True
    sync_state["error"] = None
    is_initial = get_setting("initial_sync_done", "0") == "0"
    sync_state["mode"] = "initial" if is_initial else "full"
    target_url = get_setting("target_url", DEFAULT_TARGET_URL)

    try:
        resume_page = int(get_setting("last_synced_page", "1") or "1") if is_initial else 1
        sync_state["message"] = "Đang kiểm tra trang 1..."
        sync_state["current_page"] = 1
        first_items, detected_max_page = fetch_page_series(build_page_url(target_url, 1, order="desc"))
        total_desc = min(detected_max_page, max_desc_pages)
        asc_pages_to_scan = 38 if (detected_max_page >= 100 and include_asc_tail) else 0
        sync_state["total_pages"] = total_desc + asc_pages_to_scan

        total_added = 0
        new_found = upsert_series_batch(first_items, mark_as_new=(not is_initial))
        total_added += len(new_found)

        start_pg = max(2, resume_page)
        for pg in range(start_pg, total_desc + 1):
            sync_state["current_page"] = pg
            sync_state["message"] = f"Đang đồng bộ danh sách cố định: Trang {pg}/{total_desc}..."
            page_url = build_page_url(target_url, pg, order="desc")
            items, _ = fetch_page_series(page_url)
            if not items:
                break
            added = upsert_series_batch(items, mark_as_new=(not is_initial))
            total_added += len(added)
            if is_initial:
                set_setting("last_synced_page", str(pg))
            time.sleep(1.5)

        if asc_pages_to_scan > 0:
            asc_buffer = []
            for idx, pg in enumerate(range(asc_pages_to_scan, 0, -1), start=1):
                sync_state["current_page"] = total_desc + idx
                sync_state["message"] = f"Đang quét phần mở rộng (>Trang 100): {idx}/{asc_pages_to_scan}..."
                page_url = build_page_url(target_url, pg, order="asc")
                items, _ = fetch_page_series(page_url)
                if items:
                    asc_buffer.extend(reversed(items))
                time.sleep(1.5)
            if asc_buffer:
                added = upsert_series_batch(asc_buffer, mark_as_new=(not is_initial))
                total_added += len(added)

        now = int(time.time())
        set_setting("initial_sync_done", "1")
        set_setting("last_synced_page", str(total_desc))
        set_setting("last_sync_at", str(now))
        sync_state["last_sync_at"] = now
        sync_state["last_new_count"] = total_added if not is_initial else 0
        sync_state["message"] = f"Hoàn tất đồng bộ danh sách cố định ({total_added} bộ mới được thêm)."
    except Exception as e:
        sync_state["error"] = str(e)
        sync_state["message"] = f"Lỗi đồng bộ: {e}"
    finally:
        sync_state["is_syncing"] = False


def run_check_new_series(pages_to_check: int = 5):
    """
    Quét nhanh các trang đầu để phát hiện BỘ TRUYỆN MỚI XUẤT HIỆN.
    - Không làm thay đổi vị trí (`fixed_order`) của các bộ đã có.
    - Không bắn thông báo khi bộ cũ cập nhật chapter.
    - Chỉ bắn thông báo khi phát hiện `series_id` hoàn toàn mới chưa từng có trong DB.
    """
    if sync_state["is_syncing"]:
        return

    # Nếu chưa từng hoàn tất Initial Sync, tiếp tục chạy nốt Initial Sync thay vì báo bộ mới giả
    if get_setting("initial_sync_done", "0") == "0":
        run_full_snapshot_sync(max_desc_pages=100, include_asc_tail=True)
        return

    sync_state["is_syncing"] = True
    sync_state["error"] = None
    sync_state["mode"] = "check_new"
    sync_state["total_pages"] = pages_to_check + 1
    target_url = get_setting("target_url", DEFAULT_TARGET_URL)

    try:
        discovered_new = []
        # 1. Quét N trang đầu của sort=sdate (Last Updated)
        for pg in range(1, pages_to_check + 1):
            sync_state["current_page"] = pg
            sync_state["message"] = f"Đang kiểm tra bộ mới (Trang {pg}/{pages_to_check})..."
            url = build_page_url(target_url, pg, order="desc")
            items, _ = fetch_page_series(url)
            if not items:
                break
            added = upsert_series_batch(items, mark_as_new=True)
            discovered_new.extend(added)
            time.sleep(1.2)

        # 2. Quét thêm Trang 1 của sort=srel (Release Date) để bắt ngay cả bộ mới tạo chưa có chapter update mới
        sync_state["current_page"] = pages_to_check + 1
        sync_state["message"] = "Đang kiểm tra danh mục mới phát hành (Release Date)..."
        srel_url = build_page_url(target_url, 1, order="desc", sort="srel")
        srel_items, _ = fetch_page_series(srel_url)
        if srel_items:
            added_srel = upsert_series_batch(srel_items, mark_as_new=True)
            discovered_new.extend(added_srel)

        now = int(time.time())
        set_setting("last_sync_at", str(now))
        sync_state["last_sync_at"] = now
        sync_state["last_new_count"] = len(discovered_new)
        if discovered_new:
            sync_state["message"] = f"🎉 Phát hiện {len(discovered_new)} bộ truyện MỚI!"
        else:
            sync_state["message"] = "Đã kiểm tra xong: Không có bộ mới nào xuất hiện."
    except Exception as e:
        sync_state["error"] = str(e)
        sync_state["message"] = f"Lỗi khi kiểm tra bộ mới: {e}"
    finally:
        sync_state["is_syncing"] = False


def background_scheduler():
    """Tự động chạy khởi tạo nếu chưa hoàn tất Initial Sync, và định kỳ kiểm tra bộ mới."""
    time.sleep(2)
    if get_setting("initial_sync_done", "0") == "0":
        threading.Thread(
            target=run_full_snapshot_sync,
            kwargs={"max_desc_pages": 100, "include_asc_tail": True},
            daemon=True
        ).start()

    while True:
        time.sleep(30)
        if sync_state["is_syncing"]:
            continue
        try:
            # Nếu đợt quét khởi tạo 100 trang chưa xong, tự động chạy tiếp cho đến khi xong 100%
            if get_setting("initial_sync_done", "0") == "0":
                run_full_snapshot_sync(max_desc_pages=100, include_asc_tail=True)
                continue
            interval_min = int(get_setting("auto_check_minutes", "15") or "15")
            if interval_min <= 0:
                continue
            last_sync = int(get_setting("last_sync_at", "0") or "0")
            if int(time.time()) - last_sync >= interval_min * 60:
                run_check_new_series(pages_to_check=4)
        except Exception:
            pass


# ==============================================================================
# API ENDPOINTS
# ==============================================================================

async def api_list_series(request):
    qp = request.query_params
    tab = qp.get("tab", "unread")  # unread | new | read | blacklist | bookmark | all
    page = max(1, int(qp.get("page", "1") or "1"))
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    search = qp.get("q", "").strip()
    genre_filter = qp.get("genre", "").strip()
    min_rating = float(qp.get("min_rating", "0") or "0")
    min_chapters = int(qp.get("min_chapters", "0") or "0")
    sort_by = qp.get("sort", "fixed_asc")  # fixed_asc | fixed_desc | rating_desc | readers_desc | chapters_desc

    excluded_tags_raw = get_setting("excluded_tags", "[]")
    try:
        excluded_tags = json.loads(excluded_tags_raw)
    except Exception:
        excluded_tags = []

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

    if search:
        where_clauses.append("(title LIKE ? OR short_desc LIKE ? OR full_desc LIKE ?)")
        like_q = f"%{search}%"
        params.extend([like_q, like_q, like_q])

    if genre_filter:
        where_clauses.append("genres_json LIKE ?")
        params.append(f'%"{genre_filter}"%')

    if min_rating > 0:
        where_clauses.append("rating >= ?")
        params.append(min_rating)

    if min_chapters > 0:
        where_clauses.append("chapters_num >= ?")
        params.append(min_chapters)

    if tab in ("unread", "new") and excluded_tags:
        for ex_tag in excluded_tags:
            where_clauses.append("genres_json NOT LIKE ?")
            params.append(f'%"{ex_tag}"%')

    where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""

    order_map = {
        "fixed_asc": "fixed_order ASC",
        "fixed_desc": "fixed_order DESC",
        "rating_desc": "rating DESC, fixed_order ASC",
        "readers_desc": "readers_num DESC, fixed_order ASC",
        "chapters_desc": "chapters_num DESC, fixed_order ASC",
        "newest_seen": "first_seen_at DESC, fixed_order DESC",
    }
    order_sql = order_map.get(sort_by, "fixed_order ASC")

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(f"SELECT COUNT(*) as total FROM series {where_sql}", params)
    total_filtered = cur.fetchone()["total"]

    offset = (page - 1) * per_page
    cur.execute(
        f"SELECT * FROM series {where_sql} ORDER BY {order_sql} LIMIT ? OFFSET ?",
        params + [per_page, offset]
    )
    rows = [dict(r) for r in cur.fetchall()]
    for r in rows:
        try:
            r["genres"] = json.loads(r.get("genres_json") or "[]")
        except Exception:
            r["genres"] = []

    # Thống kê số lượng cho từng tab
    cur.execute("""
        SELECT
            SUM(CASE WHEN status = 'unread' THEN 1 ELSE 0 END) as unread_count,
            SUM(CASE WHEN is_new = 1 AND status != 'blacklist' THEN 1 ELSE 0 END) as new_count,
            SUM(CASE WHEN status = 'read' THEN 1 ELSE 0 END) as read_count,
            SUM(CASE WHEN status = 'blacklist' THEN 1 ELSE 0 END) as blacklist_count,
            SUM(CASE WHEN status = 'bookmark' THEN 1 ELSE 0 END) as bookmark_count,
            COUNT(*) as all_count
        FROM series
    """)
    counts = dict(cur.fetchone())

    cur.execute("SELECT COUNT(*) as c FROM notifications WHERE is_read = 0")
    unread_notif_count = cur.fetchone()["c"]

    conn.close()

    total_pages = max(1, (total_filtered + per_page - 1) // per_page)
    return JSONResponse({
        "items": rows,
        "page": page,
        "per_page": per_page,
        "total_items": total_filtered,
        "total_pages": total_pages,
        "counts": {
            "unread": counts.get("unread_count") or 0,
            "new": counts.get("new_count") or 0,
            "read": counts.get("read_count") or 0,
            "blacklist": counts.get("blacklist_count") or 0,
            "bookmark": counts.get("bookmark_count") or 0,
            "all": counts.get("all_count") or 0,
            "unread_notifications": unread_notif_count,
        },
        "sync_state": sync_state,
        "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
        "excluded_tags": excluded_tags,
    })


async def api_update_status(request):
    body = await request.json()
    series_id = body.get("series_id")
    new_status = body.get("status")  # unread | read | blacklist | bookmark
    mark_seen = body.get("mark_seen", True)

    if not series_id or new_status not in ("unread", "read", "blacklist", "bookmark"):
        return JSONResponse({"error": "Tham số không hợp lệ"}, status_code=400)

    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        if mark_seen:
            cur.execute(
                "UPDATE series SET status = ?, is_new = 0, updated_at = ? WHERE series_id = ?",
                (new_status, int(time.time()), series_id)
            )
            cur.execute("UPDATE notifications SET is_read = 1 WHERE series_id = ?", (series_id,))
        else:
            cur.execute(
                "UPDATE series SET status = ?, updated_at = ? WHERE series_id = ?",
                (new_status, int(time.time()), series_id)
            )
        conn.commit()
        conn.close()

    return JSONResponse({"ok": True, "series_id": series_id, "status": new_status})


async def api_mark_new_seen(request):
    body = await request.json()
    series_id = body.get("series_id")  # None = tất cả
    with db_lock:
        conn = get_db_connection()
        cur = conn.cursor()
        if series_id:
            cur.execute("UPDATE series SET is_new = 0 WHERE series_id = ?", (series_id,))
            cur.execute("UPDATE notifications SET is_read = 1 WHERE series_id = ?", (series_id,))
        else:
            cur.execute("UPDATE series SET is_new = 0 WHERE is_new = 1")
            cur.execute("UPDATE notifications SET is_read = 1 WHERE is_read = 0")
        conn.commit()
        conn.close()
    return JSONResponse({"ok": True})


async def api_bookmark_position(request):
    body = await request.json()
    fixed_order = int(body.get("fixed_order", 0) or 0)
    per_page = int(body.get("per_page", 25) or 25)
    set_setting("bookmarked_order", str(fixed_order))

    # Tính trang tương ứng trong tab unread
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) as pos FROM series WHERE status = 'unread' AND fixed_order <= ?",
        (fixed_order,)
    )
    pos = cur.fetchone()["pos"] or 1
    conn.close()
    target_page = max(1, (pos + per_page - 1) // per_page)
    return JSONResponse({"ok": True, "bookmarked_order": fixed_order, "target_page": target_page})


async def api_jump_bookmark(request):
    qp = request.query_params
    per_page = max(5, min(100, int(qp.get("per_page", "25") or "25")))
    bookmarked_order = int(get_setting("bookmarked_order", "0") or "0")
    if bookmarked_order <= 0:
        return JSONResponse({"ok": False, "message": "Chưa có vị trí nào được đánh dấu."})

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) as pos FROM series WHERE status = 'unread' AND fixed_order <= ?",
        (bookmarked_order,)
    )
    pos = cur.fetchone()["pos"] or 1
    conn.close()
    target_page = max(1, (pos + per_page - 1) // per_page)
    return JSONResponse({"ok": True, "bookmarked_order": bookmarked_order, "target_page": target_page})


async def api_trigger_sync(request):
    body = await request.json()
    mode = body.get("mode", "check_new")  # check_new | full
    pages = int(body.get("pages", 5) or 5)

    if sync_state["is_syncing"]:
        return JSONResponse({"ok": False, "message": "Đang trong tiến trình đồng bộ, vui lòng đợi..."}, status_code=409)

    if mode == "full":
        threading.Thread(
            target=run_full_snapshot_sync,
            kwargs={"max_desc_pages": 100, "include_asc_tail": True},
            daemon=True
        ).start()
    else:
        threading.Thread(
            target=run_check_new_series,
            kwargs={"pages_to_check": pages},
            daemon=True
        ).start()

    return JSONResponse({"ok": True, "mode": mode})


async def api_sync_status(request):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notifications WHERE is_read = 0 ORDER BY id DESC LIMIT 20")
    notifs = [dict(r) for r in cur.fetchall()]
    cur.execute("SELECT COUNT(*) as c FROM series WHERE is_new = 1 AND status != 'blacklist'")
    new_series_count = cur.fetchone()["c"]
    conn.close()
    return JSONResponse({
        "sync_state": sync_state,
        "unread_notifications": notifs,
        "new_series_count": new_series_count,
        "last_sync_at": int(get_setting("last_sync_at", "0") or "0"),
        "target_url": get_setting("target_url", DEFAULT_TARGET_URL),
        "auto_check_minutes": int(get_setting("auto_check_minutes", "15") or "15"),
    })


async def api_settings(request):
    if request.method == "GET":
        return JSONResponse({
            "target_url": get_setting("target_url", DEFAULT_TARGET_URL),
            "auto_check_minutes": int(get_setting("auto_check_minutes", "15") or "15"),
            "excluded_tags": json.loads(get_setting("excluded_tags", "[]") or "[]"),
            "bookmarked_order": int(get_setting("bookmarked_order", "0") or "0"),
        })
    body = await request.json()
    if "target_url" in body and body["target_url"].strip():
        set_setting("target_url", body["target_url"].strip())
    if "auto_check_minutes" in body:
        set_setting("auto_check_minutes", str(int(body["auto_check_minutes"])))
    if "excluded_tags" in body and isinstance(body["excluded_tags"], list):
        set_setting("excluded_tags", json.dumps(body["excluded_tags"], ensure_ascii=False))
    return JSONResponse({"ok": True})


async def api_proxy_image(request):
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
            impersonate="chrome",
            headers={"Referer": "https://www.novelupdates.com/"},
            timeout=15
        )
        if r.status_code == 200 and r.content:
            with open(cache_path, "wb") as f:
                f.write(r.content)
            return Response(r.content, media_type=r.headers.get("content-type", "image/jpeg"))
    except Exception:
        pass
    return Response(status_code=404)


async def index_page(request):
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


init_db()
threading.Thread(target=background_scheduler, daemon=True).start()

routes = [
    Route("/", index_page),
    Route("/api/series", api_list_series, methods=["GET"]),
    Route("/api/status", api_update_status, methods=["POST"]),
    Route("/api/mark-seen", api_mark_new_seen, methods=["POST"]),
    Route("/api/bookmark", api_bookmark_position, methods=["POST"]),
    Route("/api/jump-bookmark", api_jump_bookmark, methods=["GET"]),
    Route("/api/sync", api_trigger_sync, methods=["POST"]),
    Route("/api/sync-status", api_sync_status, methods=["GET"]),
    Route("/api/settings", api_settings, methods=["GET", "POST"]),
    Route("/api/proxy-image", api_proxy_image, methods=["GET"]),
    Mount("/static", StaticFiles(directory=STATIC_DIR), name="static"),
]

app = Starlette(
    debug=False,
    routes=routes,
    middleware=[Middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])],
)

if __name__ == "__main__":
    port = int(os.environ.get("NU_PORT", 8686))
    print(f"🚀 NovelUpdates Series Tracker đang chạy tại: http://localhost:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")
