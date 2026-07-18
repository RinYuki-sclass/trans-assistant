"""
📖 Trans-Tool Web Interface
AI Novel Translation Tool with Diff View
"""

import streamlit as st
import difflib
import os
import sys
import time
import html as html_lib
import threading
import random
import json
from datetime import datetime, timezone, timedelta

def now_gmt7():
    return datetime.now(timezone(timedelta(hours=7)))
from dotenv import load_dotenv
import re
import shutil

# ============================================================
# CONFIG & PATHS
# ============================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'), override=True)

def get_env(key: str, default=None):
    """Read from st.secrets (Streamlit Cloud) first, then fall back to os.environ (local)."""
    try:
        return st.secrets[key]
    except Exception:
        return os.environ.get(key, default)

def get_windows_sort_key(filename):
    """Hỗ trợ sort Natural và format copy của Windows: '60.jpg' vs '60 (1).jpg'"""
    m = re.match(r'^(.*?)(?: \(([0-9]+)\))?(\.[a-zA-Z0-9_]+)?$', filename)
    if m:
        base, dup_num, ext = m.groups()
        base_parts = [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', base or "")]
        return base_parts + [int(dup_num) if dup_num else 0, ext or ""]
    return [filename]

# ============================================================
# LOGGING SYSTEM  
# ============================================================
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

# 50 con vật dễ thương — mỗi session được gán 1 tên ngẫu nhiên
ANIMAL_TOKENS = [
    "🦫 Hải Ly",     "🦊 Cáo",        "🐼 Gấu Trúc",   "🐧 Chim Cánh Cụt",
    "🦉 Cú Mèo",    "🦁 Sư Tử",      "🐯 Hổ",         "🐨 Koala",
    "🦒 Hươu Cao Cổ","🦓 Ngựa Vằn",  "🐘 Voi",         "🦏 Tê Giác",
    "🦛 Hà Mã",     "🐆 Báo",        "🐺 Sói",         "🦌 Nai",
    "🦔 Nhím",      "🐿️ Sóc",        "🐰 Thỏ",         "🦘 Kangaroo",
    "🐸 Ếch",       "🦎 Kỳ Nhông",   "🐢 Rùa",         "🦑 Mực",
    "🐙 Bạch Tuộc", "🦞 Tôm Hùm",   "🦀 Cua",         "🐡 Cá Nóc",
    "🐬 Cá Heo",    "🦈 Cá Mập",     "🦢 Thiên Nga",   "🦩 Hồng Hạc",
    "🦜 Vẹt",       "🦚 Công",        "🦃 Gà Tây",      "🦤 Chim Dodo",
    "🐦 Chim Sẻ",   "🦆 Vịt",         "🦅 Đại Bàng",    "🦋 Bướm",
    "🐝 Ong",       "🪲 Bọ Cánh Cứng","🦗 Dế",          "🕷️ Nhện",
    "🦂 Bọ Cạp",   "🐊 Cá Sấu",     "🦭 Hải Cẩu",    "🐻 Gấu",
    "🐮 Bò",        "🐷 Lợn",
]

def _get_cookie_manager():
    """CookieManager must be initialized in every run to handle browser communication."""
    import extra_streamlit_components as stx
    if 'cookie_manager' not in st.session_state:
        st.session_state['cookie_manager'] = stx.CookieManager(key="trans_tool_cookies")
    return st.session_state['cookie_manager']

def assign_animal_token() -> str:
    """
    Assign a random animal name that persists in the browser cookie across F5 reloads.
    Resets only when the user clears browser cookies/cache, or the app is redeployed.
    """
    # 1. Fast path: already in session_state this run
    if 'animal_token' in st.session_state:
        return st.session_state['animal_token']

    # 2. Try reading synchronously from browser headers (fixes F5 reset issue)
    try:
        import urllib.parse
        cookies_str = ""
        if hasattr(st, "context") and hasattr(st.context, "headers"):
            cookies_str = st.context.headers.get("Cookie", "") or st.context.headers.get("cookie", "")
        for item in cookies_str.split(";"):
            item = item.strip()
            if item.startswith("trans_animal="):
                val = urllib.parse.unquote(item.split("=", 1)[1])
                if val.startswith('"') and val.endswith('"'): val = val[1:-1]
                if val in ANIMAL_TOKENS:
                    st.session_state['animal_token'] = val
                    return val
    except Exception:
        pass

    # 2.5 Fallback to CookieManager
    try:
        cm = _get_cookie_manager()
        existing = cm.get("trans_animal")
        if existing and existing in ANIMAL_TOKENS:
            st.session_state['animal_token'] = existing
            return existing
    except Exception:
        pass

    # 3. First visit / cookie not set — pick a new animal and persist it
    token = random.choice(ANIMAL_TOKENS)
    st.session_state['animal_token'] = token
    try:
        from datetime import timedelta
        cm = _get_cookie_manager()
        cm.set("trans_animal", token, expires_at=now_gmt7() + timedelta(days=365))
    except Exception:
        pass
    return token


def get_device_type() -> str:
    """Get a simple device type label from the User-Agent header."""
    try:
        ua = st.context.headers.get("User-Agent", "")
        if "Mobile" in ua or "Android" in ua or "iPhone" in ua:
            return "Mobile"
        elif "Tablet" in ua or "iPad" in ua:
            return "Tablet"
        elif ua:
            return "Desktop"
    except Exception:
        pass
    return "Unknown"

def log_action(feature: str, details: str = ""):
    """Append one line to the daily log file. Never crashes the app."""
    if feature == "Truy cập":
        return
    try:
        today_str = now_gmt7().strftime("%Y-%m-%d")
        log_file = os.path.join(LOGS_DIR, f"{today_str}.log")
        token = assign_animal_token()
        device = get_device_type()
        ts = now_gmt7().strftime("%H:%M:%S")
        entry = f"[{today_str} {ts}] | {token:<18} | {device:<8} | {feature:<22} | {details}\n"
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    except Exception:
        pass

st.set_page_config(
    page_title="Trans-Tool | AI Novel Translator",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

PATHS = {
    'eng_trans': os.path.join(BASE_DIR, 'input', 'trans', 'eng.txt'),
    'kor_trans': os.path.join(BASE_DIR, 'input', 'trans', 'kor.txt'),
    'vi_qc': os.path.join(BASE_DIR, 'input', 'qc', 'vi_to_qc.txt'),
    'kor_qc': os.path.join(BASE_DIR, 'input', 'qc', 'kor.txt'),
    'eng_qc': os.path.join(BASE_DIR, 'input', 'qc', 'eng.txt'),
    'glossary': os.path.join(BASE_DIR, 'glossary', 'glossary.md'),
    'notes': os.path.join(BASE_DIR, 'glossary', 'personal_notes.md'),
    'output': os.path.join(BASE_DIR, 'output', 'vi_final.txt'),
    'output_prev': os.path.join(BASE_DIR, 'output', 'vi_previous.txt'),
    'qc_report': os.path.join(BASE_DIR, 'output', 'qc_report.txt'),
    'new_terms': os.path.join(BASE_DIR, 'output', 'new_glossary_terms.txt'),
    'qc_diff_dir': os.path.join(BASE_DIR, 'output', 'qc_diff'),
}

HIDE_LOCAL_FILE_OPTION = str(get_env("HIDE_LOCAL_FILE_OPTION")).strip().lower() in ("true", "1", "yes")

# ============================================================
# CUSTOM CSS
# ============================================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    .stApp { font-family: 'Inter', sans-serif; }
    .app-header {
        background: linear-gradient(135deg, #0D9488 0%, #0B7A70 100%);
        padding: 1.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem; color: #ffffff;
    }
    .app-header h1 { margin: 0; font-size: 1.8rem; font-weight: 700; }
    .app-header p { margin: 0.3rem 0 0; opacity: 0.85; font-size: 0.95rem; }
    .diff-container {
        font-family: 'Consolas', 'Courier New', monospace; font-size: 13px;
        line-height: 1.6; border-radius: 10px; overflow: hidden;
        border: 1px solid #D1CFC7; max-height: 600px; overflow-y: auto;
    }
    .diff-add { background: rgba(46,125,50,0.08); color: #2e7d32; padding: 3px 12px; border-left: 3px solid #2e7d32; }
    .diff-del { background: rgba(198,40,40,0.08); color: #c62828; padding: 3px 12px; border-left: 3px solid #c62828; }
    .diff-info { background: rgba(13,148,136,0.1); color: #0D9488; padding: 3px 12px; font-weight: 600; }
    .diff-ctx { color: #5c564d; padding: 3px 12px; }
    .glossary-box {
        background: #EFECE6; border: 1px solid #D1CFC7; border-radius: 10px;
        padding: 1rem; max-height: 500px; overflow-y: auto;
    }
    /* Side-by-side comparison */
    .sbs-table { width: 100%; border-collapse: collapse; font-size: 14px; line-height: 1.7; }
    .sbs-table th {
        background: #0D9488; color: #ffffff;
        padding: 10px 14px; text-align: left; position: sticky; top: 0; z-index: 1;
    }
    .sbs-table td {
        padding: 8px 14px; border-bottom: 1px solid #D1CFC7;
        vertical-align: top; word-wrap: break-word;
    }
    .sbs-table tr:hover td { background: rgba(13,148,136,0.08); }
    .sbs-num { color: #8c8273; font-size: 12px; text-align: center; min-width: 35px; user-select: none; }
    .sbs-src { color: #5c564d; max-width: 45%; }
    .sbs-vi { color: #a6701e; max-width: 45%; }
    .sbs-empty { color: #8c8273; font-style: italic; }
    .sbs-wrap {
        max-height: 650px; overflow-y: auto; border-radius: 10px;
        border: 1px solid #D1CFC7; background: #F8F6F0;
    }
    .term-hl {
        background-color: rgba(166, 112, 30, 0.1);
        color: #a6701e;
        border-bottom: 1px dashed #a6701e;
        border-radius: 2px;
        padding: 0 2px;
        cursor: help;
        transition: background-color 0.2s;
    }
    /* Sticky Manhwa Logic */
    /* 1. The Column MUST be tall (matching the image) to act as a 'runway' */
    div[data-testid="stColumn"]:has(.sticky-anchor) {
        height: inherit !important;
        min-height: 100% !important;
    }
    
    /* 2. Target the inner block to be sticky and small enough to slide */
    div[data-testid="stColumn"]:has(.sticky-anchor) [data-testid="stVerticalBlock"] {
        position: -webkit-sticky !important;
        position: sticky !important;
        top: 80px !important;
        z-index: 999;
        background: #EFECE6; /* Light theme secondary background */
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid #D1CFC7;
        height: auto !important;
        width: 100% !important; /* Ensure it fills the column width */
    }

    /* 3. Broadly allow overflow and prevent clipping */
    [data-testid="stHorizontalBlock"],
    [data-testid="stColumn"],
    [data-testid="stVerticalBlock"],
    [data-baseweb="tab-panel"],
    .main .block-container {
        overflow: visible !important;
    }
    /* Ngăn chặn chớp/mờ nháy khi click trên Streamlit (vô hiệu hóa Stale Dimming) */
    [data-testid="stApp"] [data-stale="true"],
    [data-stale="true"],
    iframe {
        opacity: 1 !important;
        filter: none !important;
        transition: none !important;
    }
    /* QC Diff Review cards */
    .qcd-card {
        border: 1px solid #D1CFC7; border-radius: 12px; padding: 1rem 1.2rem;
        margin-bottom: 0.8rem; background: #F8F6F0; transition: border-color 0.2s;
    }
    .qcd-card:hover { border-color: #0D9488; }
    .qcd-card-approved { border-color: #2e7d32; background: rgba(46,125,50,0.04); }
    .qcd-card-discarded { border-color: #c62828; background: rgba(198,40,40,0.04); opacity: 0.6; }
    .qcd-card-edited { border-color: #a6701e; background: rgba(166,112,30,0.04); }
    .qcd-card-manual { border-color: #d08400; background: rgba(208,132,0,0.06); }
    .qcd-diff-del { background: rgba(198,40,40,0.12); color: #c62828; text-decoration: line-through; padding: 1px 3px; border-radius: 3px; }
    .qcd-diff-add { background: rgba(46,125,50,0.12); color: #2e7d32; padding: 1px 3px; border-radius: 3px; font-weight: 500; }
    .qcd-badge {
        display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 11px;
        font-weight: 600; letter-spacing: 0.3px;
    }
    .qcd-badge-name { background: rgba(30,136,229,0.15); color: #1e88e5; }
    .qcd-badge-glossary { background: rgba(92,86,77,0.15); color: #5c564d; }
    .qcd-badge-honorific { background: rgba(166,112,30,0.15); color: #a6701e; }
    .qcd-badge-pronoun { background: rgba(138,59,168,0.15); color: #8a3ba8; }
    .qcd-badge-typo { background: rgba(198,40,40,0.15); color: #c62828; }
    .qcd-badge-grammar { background: rgba(46,125,50,0.15); color: #2e7d32; }
    .qcd-badge-spacing { background: rgba(140,130,115,0.15); color: #8c8273; }
    .qcd-badge-punctuation { background: rgba(216,67,21,0.15); color: #d84315; }
    .qcd-badge-consistency { background: rgba(13,148,136,0.15); color: #0D9488; }
    .qcd-badge-needs_manual_review { background: rgba(208,132,0,0.2); color: #d08400; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# API KEY ROTATOR + RPD TRACKER
# ============================================================
RPD_COUNTER_FILE = os.path.join(LOGS_DIR, "rpd_counter.json")
@st.cache_resource
def get_rpd_lock():
    return threading.Lock()

_rpd_lock = get_rpd_lock()

# RPD limits for each model per API key
RPD_LIMITS = {
    "gemini-2.5-flash": 1500,     # Đây là bản 1.5 Flash (ổn định nhất)
    "gemini-2.5-pro": 50,         
    "gemini-2.0-flash": 1500,     
    "gemini-3.1-flash-lite": 2000, 
    "gemini-2.5-flash-lite": 2000, 
}

def _load_rpd_counter() -> dict:
    """Load today's request counts from JSON file."""
    today = now_gmt7().strftime("%Y-%m-%d")
    try:
        if os.path.exists(RPD_COUNTER_FILE):
            with open(RPD_COUNTER_FILE, 'r') as f:
                data = json.load(f)
            if data.get('date') == today:
                return data
    except Exception:
        pass
    return {'date': today, 'counts': {}}

def _save_rpd_counter(data: dict):
    try:
        with open(RPD_COUNTER_FILE, 'w') as f:
            json.dump(data, f)
    except Exception:
        pass

def increment_rpd(key_idx: int, model: str):
    """Increment request count for key_idx and model. Thread-safe."""
    with _rpd_lock:
        data = _load_rpd_counter()
        k = f"{key_idx}_{model}"
        data['counts'][k] = data['counts'].get(k, 0) + 1
        _save_rpd_counter(data)

def increment_rpd_to_limit(key_idx: int, model: str, limit: int):
    """Set request count to limit to mark it as exhausted. Thread-safe."""
    with _rpd_lock:
        data = _load_rpd_counter()
        k = f"{key_idx}_{model}"
        data['counts'][k] = max(data['counts'].get(k, 0), limit)
        _save_rpd_counter(data)

def get_rpd_counts() -> dict:
    """Return counts dict for today."""
    with _rpd_lock:
        return _load_rpd_counter().get('counts', {})


class GeminiKeyRotator:
    """Thread-safe multi-key rotator with per-model RPD awareness."""
    def __init__(self, clients: list):
        self._clients = clients
        self._idx = 0
        self._lock = threading.Lock()
        self._blacklisted = set() # Store indices of permanently failed keys (e.g. leaked)

    @property
    def current(self):
        return self._clients[self._idx]

    @property
    def current_idx(self):
        return self._idx

    @property
    def total(self):
        return len(self._clients)

    def is_near_limit(self, idx: int, model: str, threshold: float = 0.95) -> bool:
        """True if key has used >= threshold of its RPD for the target model."""
        lim = RPD_LIMITS.get(model, 20)
        used = get_rpd_counts().get(f"{idx}_{model}", 0)
        return used >= lim * threshold

    def rotate(self, model: str, reason: str = ""):
        """Rotate to next key. Skips keys near RPD limit or blacklisted."""
        with self._lock:
            original = self._idx
            for _ in range(self.total):
                self._idx = (self._idx + 1) % self.total
                if self._idx not in self._blacklisted and not self.is_near_limit(self._idx, model):
                    break
                if self._idx == original:
                    break  # all exhausted or blacklisted, stay
        return self._idx
        
    def blacklist(self, idx: int):
        """Permanently disable a key for this session (e.g. 403 Leaked)."""
        with self._lock:
            self._blacklisted.add(idx)

    def mark_exhausted(self, idx: int, model: str):
        """Set request count in RPD file to the limit so it's skipped for this model."""
        lim = RPD_LIMITS.get(model, 20)
        increment_rpd_to_limit(idx, model, lim)

    def is_exhausted(self, model: str, threshold: float = 0.95) -> bool:
        """True if ALL keys have reached their RPD limit for this model."""
        with self._lock:
            for idx in range(self.total):
                if not self.is_near_limit(idx, model, threshold):
                    return False
        return True

    def ensure_best_key(self, model: str):
        """Before a call, proactively switch if current key is near limit."""
        with self._lock:
            if self.is_near_limit(self._idx, model) and self.total > 1:
                original = self._idx
                for _ in range(self.total):
                    self._idx = (self._idx + 1) % self.total
                    if not self.is_near_limit(self._idx, model):
                        break
                    if self._idx == original:
                        break

@st.cache_resource
def init_rotator():
    import json
    from google import genai
    keys = []
    i = 1
    while True:
        key = get_env(f"GEMINI_API_KEY_{i}") or (get_env("GEMINI_API_KEY") if i == 1 else None)
        if not key or key.strip() == "":
            break
        keys.append(key.strip())
        i += 1
        if i > 20:
            break
    if not keys:
        return None
    clients = [genai.Client(api_key=k) for k in keys]
    return GeminiKeyRotator(clients)

rotator = init_rotator()
client = rotator.current if rotator else None  # kept for backward compat

# ============================================================
# UTILITY FUNCTIONS
# ============================================================
def load_file(path, default=""):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return default

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def generate_with_retry(model, contents, system_instruction, status_w=None, retries=8, temp=0.3):
    from google.genai import types
    
    # Cấu hình bỏ qua bộ lọc an toàn để tránh bị AI từ chối dịch truyện tranh
    safety_settings = [
        types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
        types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
    ]
    
    config = types.GenerateContentConfig(
        system_instruction=system_instruction, 
        temperature=temp,
        safety_settings=safety_settings
    )
    
    # Chuỗi dự phòng thông minh (Waterfall)
    model_chain = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-3.1-flash-lite", "gemini-2.5-flash-lite"]
    
    if rotator and rotator.is_exhausted(model):
        for fallback in model_chain:
            if not rotator.is_exhausted(fallback):
                if status_w: status_w.warning(f"⚠️ `{model}` hết lượt! Chuyển sang dự phòng `{fallback}`.")
                model = fallback
                break

    for i in range(retries):
        if rotator:
            # Check if model has become exhausted dynamically
            if rotator.is_exhausted(model):
                for fallback in model_chain:
                    if not rotator.is_exhausted(fallback):
                        if status_w: status_w.warning(f"⚠️ `{model}` hết lượt! Chuyển sang dự phòng `{fallback}`.")
                        model = fallback
                        break
            rotator.ensure_best_key(model)
            active_client = rotator.current
            key_idx = rotator.current_idx
        else:
            return ""

        key_label = f"Key {key_idx + 1}"
        try:
            resp = active_client.models.generate_content(model=model, contents=contents, config=config)
            if resp and resp.text:
                increment_rpd(key_idx, model)
                return resp.text
            
            # Nếu không có text, có thể do bị chặn bởi lý do khác (finish_reason)
            if status_w: status_w.warning(f"⚠️ [{key_label}] AI không trả về text (Lần {i+1}). Đang thử lại...")
            time.sleep(3)
        except Exception as e:
            err_str = str(e)
            if "leaked" in err_str.lower() or "permission_denied" in err_str.lower() or "403" in err_str:
                # Bảo vệ chống lỗi Cache: Chỉ gọi blacklist nếu object đã được cập nhật
                if rotator and hasattr(rotator, 'blacklist'):
                    rotator.blacklist(key_idx)
                
                if rotator.total > 1:
                    new_idx = rotator.rotate(model)
                    if status_w: status_w.error(f"☠️ [{key_label}] Key bị khóa (Leaked)! Đã loại bỏ. Đang dùng Key {new_idx+1}...")
                else:
                    if status_w: status_w.error(f"☠️ [{key_label}] Key duy nhất đã bị khóa! Hãy thay Key mới.")
                    return ""
            elif "429" in err_str or "503" in err_str or "unavailable" in err_str.lower() or "quota" in err_str.lower() or "resource_exhausted" in err_str.lower():
                # Mark this key/model as exhausted if it's a quota / resource exhausted error
                if rotator and hasattr(rotator, 'mark_exhausted'):
                    if "quota" in err_str.lower() or "429" in err_str or "resource_exhausted" in err_str.lower():
                        rotator.mark_exhausted(key_idx, model)
                if rotator.total > 1:
                    new_idx = rotator.rotate(model)
                    if status_w:
                        status_w.warning(f"⚠️ [{key_label}] Server quá tải hoặc Hết lượt (503/429)! Đổi sang Key {new_idx + 1}... (Lần {i+1})")
                    time.sleep(3)
                else:
                    if status_w: status_w.warning(f"⚠️ Server Google đang quá tải. Đang thử lại sau 10s... (Lần {i+1})")
                    time.sleep(10)
            elif "safety" in err_str.lower():
                if status_w: status_w.warning(f"⚠️ [{key_label}] Nội dung bị lọc an toàn. Đang thử lại với cấu hình khác...")
                time.sleep(2)
            else:
                if status_w: status_w.error(f"❌ Lỗi API [{key_label}]: {err_str}")
                time.sleep(4)
    return ""

def optimize_image_for_api(img, max_dimension=3500):
    """
    Giảm kích thước ảnh và convert sang định dạng tối ưu để tránh lỗi payload/rate limit
    nhưng vẫn giữ độ nét tương đối cho OCR.
    """
    import PIL.Image, PIL.ImageEnhance
    import io
    
    # Chỉ xử lý nếu ảnh tồn tại và là loại hình ảnh
    if not isinstance(img, PIL.Image.Image):
        return img
        
    # Chuyển đổi sang RGB nếu đang ở định dạng có alpha (RGBA/P)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
        
    # --- Cải thiện chất lượng ảnh cho OCR ---
    # 1. Tăng độ tương phản để chữ đen trên nền trắng rõ hơn
    enhancer = PIL.ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.2)
    # 2. Tăng độ sắc nét để các nét chữ rời rạc dễ nhận diện hơn
    enhancer = PIL.ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.5)

    # Resize thông minh cho Manhwa: Ưu tiên giữ Width khoảng 1000-1100px
    # Google API hỗ trợ tốt nhất ở khoảng 3072px mỗi chiều, nhưng có thể nhận tới 5000px height.
    max_w = 1100
    max_h = 5000
    width, height = img.size
    if width > max_w or height > max_h:
        ratio = min(max_w / width, max_h / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        img = img.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)
    
    # Save qua bộ nhớ đệm
    img_byte_arr = io.BytesIO()
    # Lưu dưới chuẩn chất lượng JPEG tốt (88) để cân bằng giữa độ nét và dung lượng payload
    img.save(img_byte_arr, format='JPEG', quality=88)
    
    # Load lại ảnh nhẹ từ bytes
    img_byte_arr.seek(0)
    optimized_img = PIL.Image.open(img_byte_arr)
    return optimized_img

def split_long_image(img, max_h=5000, overlap=200):
    """
    Tự động cắt ảnh dài thành các phần nhỏ hơn với khoảng chồng lấp (overlap)
    để AI không bị mất nội dung ở đường cắt.
    """
    w, h = img.size
    if h <= max_h:
        return [img]
    
    parts = []
    y = 0
    while y < h:
        end_y = y + max_h
        if end_y > h:
            end_y = h
        
        box = (0, y, w, end_y)
        parts.append(img.crop(box))
        
        if end_y == h:
            break
        y = end_y - overlap
        if y < 0: y = 0
    return parts

def render_diff_html(text1, text2):
    """Render unified diff as colored HTML."""
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    diff_lines = list(difflib.unified_diff(lines1, lines2, fromfile="Bản cũ", tofile="Bản mới", lineterm=""))
    if not diff_lines:
        return '<div style="text-align:center;color:#51cf66;padding:2rem;font-size:1.1rem;">✅ Hai bản giống nhau hoàn toàn!</div>'
    html = ['<div class="diff-container">']
    for line in diff_lines:
        esc = html_lib.escape(line)
        if line.startswith('+++') or line.startswith('---'):
            html.append(f'<div class="diff-info">{esc}</div>')
        elif line.startswith('+'):
            html.append(f'<div class="diff-add">{esc}</div>')
        elif line.startswith('-'):
            html.append(f'<div class="diff-del">{esc}</div>')
        elif line.startswith('@@'):
            html.append(f'<div class="diff-info">{esc}</div>')
        else:
            html.append(f'<div class="diff-ctx">{esc}</div>')
    html.append('</div>')
    return '\n'.join(html)

def compute_diff_stats(text1, text2):
    sm = difflib.SequenceMatcher(None, text1.splitlines(), text2.splitlines())
    added = deleted = changed = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'insert': added += j2 - j1
        elif op == 'delete': deleted += i2 - i1
        elif op == 'replace': changed += max(i2 - i1, j2 - j1)
    return added, deleted, changed

@st.cache_data
def build_highlight_pattern(gl_text, notes_text):
    import re
    terms = set()
    for text in [gl_text, notes_text]:
        if not text: continue
        for line in text.splitlines():
            line = line.strip()
            if not line.startswith('-'): continue
            if '->' in line:
                parts = line.split('->')
                term_part = parts[-1].split('/')[0].strip() # in case of multiple with /
                if term_part: terms.add(term_part)
            else:
                m = re.match(r'- ([A-Za-z0-9\s\w]+)(?:[\(\[]|$)', line)
                if m:
                    name = m.group(1).strip()
                    if name and len(name) > 2: terms.add(name)
                    
    # Only keep terms with length >= 3 to avoid matching common short words
    valid_terms = [re.escape(t) for t in terms if len(t) >= 3]
    valid_terms.sort(key=len, reverse=True) # Sort longest first to prioritize exact full names
    if not valid_terms: return None
    
    # Word boundary doesn't always work perfectly with unicode if not re.UNICODE
    # But Python 3 re defaults to unicode. Using `\b` is generally fine.
    pattern_str = r'\b(' + '|'.join(valid_terms) + r')\b'
    try:
        return re.compile(pattern_str, re.IGNORECASE)
    except:
        return None

# ============================================================
# HEADER
# ============================================================
st.markdown("""<div class="app-header">
    <h1>📖 Trans-Tool</h1>
    <p>AI Novel Translation Tool — Dịch thuật tiểu thuyết thông minh với Diff View</p>
</div>""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.markdown("### ⚙️ Cấu hình")
    if rotator:
        if rotator.total == 1:
            st.success("🟢 API Key OK (1 key)")
        else:
            st.success(f"🟢 {rotator.total} API Keys — Key {rotator.current_idx + 1} đang dùng")
    else:
        st.error("🔴 Thiếu API Key!")
        
    if st.button("🔄 Tải lại API Keys", use_container_width=True, help="Click nếu bạn mới cập nhật file .env"):
        init_rotator.clear()
        st.rerun()

    # User-facing Model Selection & RPD guide
    model_guide = {
        "gemini-3-flash-preview": "📝 Dịch Thuật",
        "gemini-2.5-flash": "🔍 QC Review",
        "gemini-2.5-flash-lite": "🎨 Truyện Tranh",
        "gemini-3.1-flash-lite": "🛡️ Trợ thủ Fallback (500 RPD)"
    }
    
    st.markdown("**🤖 AI Models / Tự động điều phối**")
    st.caption("Ứng dụng tự động chọn model phù hợp nhất cho từng tác vụ và tự động chạy sang Fallback khi hết Rate Limit.")
    
    # RPD Usage tracker for ALL models — real-time via fragment
    if rotator and rotator.total > 0:
        @st.fragment(run_every=10)
        def _rpd_tracker():
            counts = get_rpd_counts()
            for mod, desc in model_guide.items():
                with st.expander(f"{desc} ({mod})", expanded=True):
                    lim = RPD_LIMITS.get(mod, 20)
                    for idx in range(rotator.total):
                        used = counts.get(f"{idx}_{mod}", 0)
                        label = f"Key {idx+1}"
                        pct = min(used / lim, 1.0) if lim > 0 else 0
                        if pct >= 0.95:
                            color = "#c62828"   # đỏ
                        elif pct >= 0.75:
                            color = "#d08400"   # cam
                        else:
                            color = "#2f9e44"   # xanh
                        st.markdown(
                            f"""
                            <div style='margin-bottom:6px'>
                            <div style='font-size:11px;color:#5c564d;display:flex;justify-content:space-between'>
                                <span>{label}</span><span style='color:{color}'>{used:,} / {lim:,}</span></div>
                            <div style='background:#D1CFC7;border-radius:4px;height:4px;overflow:hidden'>
                                <div style='width:{pct*100:.1f}%;background:{color};height:100%;border-radius:4px;
                                transition:width 0.3s'></div></div></div>
                            """,
                            unsafe_allow_html=True
                        )
        _rpd_tracker()

    chunk_size = st.slider("Đoạn/chunk (dịch)", 5, 30, 15, 5)


    st.divider()
    # Log viewer
    st.markdown("### 📋 Activity Logs")
    log_dates = sorted(
        [f.replace('.log', '') for f in os.listdir(LOGS_DIR) if f.endswith('.log')],
        reverse=True
    )
    if not log_dates:
        st.caption("Chưa có log nào.")
    else:
        selected_date = st.selectbox("Chọn ngày:", log_dates, key="log_date_sel")
        log_path = os.path.join(LOGS_DIR, f"{selected_date}.log")
        if os.path.exists(log_path):
            with open(log_path, 'r', encoding='utf-8') as f:
                lines = [l for l in f if "Truy cập" not in l]
            st.caption(f"{len(lines)} sự kiện (đã lọc Truy cập)")
            # Show last 50 entries, newest first
            log_text = "".join(reversed(lines[-50:]))
            st.code(log_text.strip(), language=None)
            st.download_button(
                "⬇️ Tải log", ''.join(lines),
                f"log_{selected_date}.txt",
                key="log_dl"
            )
    st.divider()
    st.caption(f"📅 {now_gmt7().strftime('%d/%m/%Y %H:%M')}")

# ============================================================
# MAIN NAVIGATION (Persistent on F5)
# ============================================================
MENU_ITEMS = ["🏠 Hướng dẫn", "📝 Dịch Thuật", "🔍 QC Review", "📊 So Sánh", "📖 Đối Chiếu", "🎨 Truyện Tranh", "📥 Tải Truyện", "📚 Glossary", "✂️ Cắt Ảnh", "📋 Reformat Script", "🔎 QC Diff", "🤖 Novel Agent"]

tabs = st.tabs(MENU_ITEMS)
current_menu = None # Not used


# Log page visit (once per session)
if 'session_logged' not in st.session_state:
    st.session_state['session_logged'] = True
    # log_action("Truy cập", "Mở ứng dụng")

# =================== TAB 0: HOME / HƯỚNG DẪN ===================
with tabs[0]:
    st.markdown("""
    ## Chào mừng bạn đến với **Trans-Tool** 👋  
    *Công cụ hỗ trợ Dịch thuật, Kiểm duyệt QC và Quét Truyện Tranh thông minh tích hợp AI cực mạnh do Team xây dựng.*

    Dưới đây là cẩm nang nhanh để bạn nắm rõ các chức năng và cách vận hành:

    ---

    ### 🧩 Các Tính Năng Cốt Lõi

    #### **1. 📝 Dịch Thuật (Bám sát Source Eng & Hàn)**  
    - AI nhận song song **Tiếng Anh (EN)** và **Tiếng Hàn (KR)** để cho ra bản dịch Tiếng Việt chuẩn xác nhất.
    - AI tuân thủ nghiêm ngặt từ điển thuật ngữ (`Glossary`) và các ghi chú dịch thuật riêng (`Notes`).
    - Tính năng **Re-Refine** hữu ích khi bạn đã có 1 bản dịch từ trước mà chỉ muốn AI sửa lại cấu trúc/văn phong, giúp tiết kiệm chi phí! 

    #### **2. 🔍 QC Review (Trợ lý bắt lỗi tinh vi)**
    - Ném cho AI bản dịch Tiếng Việt của bạn cùng với bản gốc. AI sẽ chỉ ra cụ thể: *Dòng nào sai sót, sai ý nghĩa, sai tên nhân vật hay bỏ sót hậu tố?*
    - **QC** cực kỳ khắt khe: Sẽ liên tục check chéo với Glossary của nhóm.
    - Đồng thời nó cũng tự động nhặt ra các **"Thuật ngữ mới"** chưa có trong từ điển để báo cáo cho Lead cập nhật!

    #### **3. 🎨 Dịch Truyện Tranh (Manhwa Translator)**
    - Quét và trích xuất chữ Hàn từ bong bóng thoại trong hình ảnh, sau đó dịch trực tiếp sang Tiếng Việt.
    - Chữ thoại sẽ được sắp xếp và dịch gọn gàng, liền mạch theo chuẩn khung tranh! Rất tiết kiệm công sức gõ text.

    #### **4. 📖 Đối Chiếu (Side-by-Side Review)**
    - Hỗ trợ dàn trang **Bản Dịch Tiếng Việt** nằm CẠNH **Bản Dịch Tiếng Anh/Hàn** để Edit/QC tự soát.
    - *Có tích hợp Highlight màu* cho những từ ngữ thuộc phạm vi Glossary, giúp bạn soi lỗi thuật ngữ siêu dễ.

    #### **5. 🤖 Novel Agent (Dịch Tiểu Thuyết Thông Minh)**
    - Hệ thống dịch tiểu thuyết dài hạn với **bộ nhớ xuyên suốt** — AI ghi nhớ nhân vật, thuật ngữ, mối quan hệ qua từng chương.
    - Quy trình **Human-in-the-loop**: AI phân tích trước, hỏi bạn những chỗ mơ hồ, rồi mới dịch — đảm bảo chất lượng cao nhất.
    - Gồm **6 sub-tab** với luồng làm việc tuần tự:

    **📁 Projects** — Tạo & quản lý project tiểu thuyết  
    - Bấm **🚀 Tạo Project** để tạo mới: đặt tên, chọn ngôn ngữ gốc/dịch, viết Style Guide (tùy chọn).  
    - Điều chỉnh **Ngưỡng tự động dịch (%)**: AI sẽ hỏi bạn khi confidence thấp hơn ngưỡng này.  
    - Chọn **Kích thước chunk** (số đoạn/chunk) — tiểu thuyết dài nên để 15-25.  
    - Bấm **✅ Chọn** để kích hoạt project trước khi sang các tab khác.

    **📥 Import Chapter** — Nhập chương mới vào project  
    - Đặt Chapter ID (tự động tăng: ch_001, ch_002...) và tiêu đề chương (tùy chọn).  
    - Dán văn bản gốc hoặc upload file .txt/.md → Hệ thống tự cắt thành chunks.  
    - Bấm **💾 Lưu Chapter & Tạo Chunks** để hoàn tất.

    **🔬 Analyze** — AI phân tích chương TRƯỚC khi dịch  
    - Chọn chapter rồi bấm **🔬 Chạy Context Analysis**.  
    - AI sẽ phát hiện: nhân vật mới, địa điểm, thuật ngữ, xưng hô mơ hồ, sự kiện timeline.  
    - Những mục có confidence thấp sẽ hiện ở mục **❓ Cần làm rõ** → Chuyển sang tab Clarifications.

    **❓ Clarifications** — Trả lời câu hỏi của AI  
    - AI liệt kê các thuật ngữ/xưng hô cần bạn chọn cách dịch (radio button hoặc nhập tay).  
    - Thuật ngữ đã được **approved** trong Glossary Memory sẽ tự động bỏ qua — AI đã học!  
    - Bấm **✅ Lưu tất cả câu trả lời** khi xong.

    **🌐 Translate** — Dịch chapter  
    - Kiểm tra pre-flight (Chunks ✅, Analysis ✅, Clarifications ✅) rồi chọn AI Model.  
    - Bấm **🌐 Dịch N chunks** để bắt đầu — AI dịch song song, có context chéo giữa các chunk.  
    - Sau khi dịch xong: review bản dịch, tải về .md, và bấm **🧠 Accept & Update Memory** để AI cập nhật bộ nhớ.  
    - Hỗ trợ **Batch translate** nhiều chapter cùng lúc.

    **🧠 Memory** — Bộ nhớ dài hạn của novel  
    - **Nhân vật**: Tên, giới tính, bí danh, xưng hô, phong cách nói — chỉnh sửa trực tiếp trong bảng.  
    - **Glossary**: Thuật ngữ gốc → dịch, loại, confidence, trạng thái Approved — có thể xuất ra .md.  
    - **Timeline**: Các sự kiện quan trọng theo chapter.  
    - **Quan hệ**: Biểu đồ quan hệ giữa các nhân vật.  
    - **Arc Summary**: Tóm tắt các arc/chương đã dịch.  
    - **Cấu hình Project**: Chỉnh Style Guide, ngưỡng confidence, chunk size...  
    - *Lưu ý: Memory được tích lũy qua từng chapter — càng dịch nhiều, AI càng chính xác!*

    #### **6. 🔎 QC Diff Review (Sửa lỗi dịch kiểu Git Diff)**
    - AI **không viết lại** cả đoạn — chỉ đề xuất **sửa tối thiểu** (minimal patch) giống Git diff.
    - Mỗi đoạn văn hiện dưới dạng **review card** với: diff inline (đỏ = xóa, xanh = thêm), loại lỗi, confidence, lý do.
    - Quy trình sử dụng:

    **Bước 1 — Nhập dữ liệu:**  
    - Dán bản dịch VI, source KR và EN (tùy chọn) vào các ô tương ứng.  
    - Điều chỉnh **Auto-approve threshold** (mặc định 97%): sửa lỗi Typo/Spacing có confidence ≥ ngưỡng sẽ tự động approve.

    **Bước 2 — Chạy QC Diff:**  
    - Bấm **🔬 Chạy QC Diff** → AI phân tích từng chunk, trả về danh sách sửa lỗi dạng JSON.  
    - Nếu >30% đoạn cần thay đổi → AI đánh dấu "⚠️ Cần kiểm tra thủ công" thay vị sửa.

    **Bước 3 — Duyệt sửa lỗi:**  
    - Mỗi card có 3 nút: **✅ Approve** / **❌ Discard** / **✏️ Edit** (sửa tay).  
    - Lọc theo: trạng thái (Pending/Approved/Discarded), loại lỗi (Tên/Glossary/Typo/...), confidence.  
    - **Batch approve**: bấm "Approve tất cả đang hiển thị" hoặc "Áp dụng cho N đoạn tương tự".

    **Bước 4 — Xuất bản dịch đã sửa:**  
    - Bấm **📥 Tạo bản dịch đã sửa** → áp dụng tất cả sửa lỗi đã Approve/Edit vào bản gốc.  
    - Tải xuống file .txt đã sửa.  
    - Mục **📋 Quy tắc đã học** hiển thị các quy tắc AI đã học từ reviewer (icon 👤 = sửa tay của bạn).

    ---

    ### 📋 Cách Sử Dụng
    * Hệ thống đã được cấu hình chung từ điển AI (Glossary) siêu xịn, nên các bạn dịch cứ thỏa sức nhé.
    * **Tuyệt đối ưu tiên tính năng Mặc định: 📋 PASTE (Dán Văn Bản)** ở tất cả các tab vì việc Copy/Paste trực tiếp nhanh hơn rất nhiều trong một quy trình làm việc Team.
    
    ### 🛡️ Cơ chế điều phối API Keys (Tự động)
    - App được tích hợp siêu luân phiên tới **20 API Keys** để tự động nhảy sang key khác khi một key hết hạn ngạch.
    - Cột `Cấu Hình` bên tay trái biểu thị sức khỏe (máu báo hiệu xanh/đỏ) của các Models thông minh, bạn có thể tự tin sử dụng mà chẳng âu lo.
    """)

# =================== TAB 1: DỊCH THUẬT ===================
with tabs[1]:
    if not client:
        st.warning("⚠️ Cấu hình API Key trong `.env` trước.")
        st.stop()

    st.markdown("#### 📥 Dữ liệu đầu vào")
    src_opts = ["📋 Paste"] if HIDE_LOCAL_FILE_OPTION else ["📂 File có sẵn (input/trans/)", "📋 Paste"]
    src_idx = 0 if len(src_opts) == 1 else 1
    src = st.radio("Nguồn:", src_opts, index=src_idx, horizontal=True, key="t_src")

    if not src.startswith("📋"):
        eng_text = load_file(PATHS['eng_trans'])
        kor_text = load_file(PATHS['kor_trans'])
        c1, c2 = st.columns(2)
        with c1: st.info(f"EN: {len(eng_text.splitlines())} dòng" if eng_text else "⚠️ Chưa có eng.txt")
        with c2: st.info(f"KR: {len(kor_text.splitlines())} dòng" if kor_text else "⚠️ Chưa có kor.txt")
    else:
        c1, c2 = st.columns(2)
        with c1: eng_text = st.text_area("Tiếng Anh", height=220, key="t_en")
        with c2: kor_text = st.text_area("Tiếng Hàn", height=220, key="t_kr")

    mode = st.radio("Chế độ:", ["🔄 Dịch mới (Draft+Refine)", "✨ Re-Refine (chỉnh vi_final)"], horizontal=True, key="t_mode")

    if st.button("🚀 Bắt đầu dịch", type="primary"):
        target_model = "gemini-2.5-flash"
        log_action("Dịch Thuật", f"Chế độ: {'Re-Refine' if mode.startswith('✨') else 'Dịch mới'} | EN: {len((eng_text or '').splitlines())} dòng | Model: {target_model}")

        if not eng_text.strip() and not kor_text.strip():
            st.error("❌ Thiếu dữ liệu EN hoặc KR! Vui lòng nhập ít nhất một ngôn ngữ nguồn.")
            st.stop()

        glossary = load_file(PATHS['glossary'])
        notes = load_file(PATHS['notes'])

        # Backup for diff
        prev = load_file(PATHS['output'])
        if prev: save_file(PATHS['output_prev'], prev)

        eng_p = [p.strip() for p in eng_text.split('\n') if p.strip()]
        kor_p = [p.strip() for p in kor_text.split('\n') if p.strip()]
        is_refine = mode.startswith("✨")

        draft_p = []
        if is_refine:
            dt = load_file(PATHS['output'])
            if not dt:
                st.error("❌ Không có vi_final.txt để re-refine!")
                st.stop()
            draft_p = [p.strip() for p in dt.split('\n') if p.strip()]

        n_chunks = (max(len(eng_p), len(kor_p)) + chunk_size - 1) // chunk_size
        final = [None] * n_chunks
        bar = st.progress(0, "Chuẩn bị...")
        status = st.status(f"🚀 {'Re-Refine' if is_refine else 'Dịch'} — {n_chunks} phần (Smart Chunking & Parallel)", expanded=True)
        t0 = time.time()

        def process_chunk(idx):
            s, e = idx * chunk_size, (idx+1) * chunk_size
            ec = "\n\n".join(eng_p[s:e])
            kc = "\n\n".join(kor_p[s:e])
            
            # Context Aware: get last 2 paragraphs from previous chunk
            prev_ec = ""
            prev_kc = ""
            if idx > 0:
                prev_s = max(0, (idx-1) * chunk_size)
                prev_ec = "\n".join(eng_p[prev_s:s][-2:])
                prev_kc = "\n".join(kor_p[prev_s:s][-2:])

            draft = ""
            if not is_refine:
                sys_d = (
                    "You are a professional novel translator. Translate English into natural Vietnamese. "
                    "STRICT RULE: ONLY include suffixes (-ie,-ah,-ya) IF present in source. "
                    "CRITICAL RULE: Translate line by line. DO NOT skip, merge, or omit any paragraphs. The number of output paragraphs MUST exactly match the 'TRANSLATE THIS' input. "
                    "Output ONLY the translation without any notes or confirmation."
                )
                prompt_d = f"--- PREVIOUS CONTEXT (For reference only) ---\n{prev_ec}\n\n--- TRANSLATE THIS ---\n{ec}" if prev_ec else ec
                draft = generate_with_retry(target_model, prompt_d, sys_d, None)
            else:
                draft = "\n\n".join(draft_p[s:e])

            sys_r = (
                "You are a strict novel editor. Refine Vietnamese translation comparing EN and KR sources. "
                "RULES: 1.Output ONLY final Vietnamese without any notes. 2.Follow source dialogue structure exactly. "
                "3.Keep suffixes from EN source. 4.Keep ahjussi,-ssi,-nim,-gun. "
                "5.Follow Glossary. 6.No creative rewriting. "
                "7.CRITICAL: DO NOT skip or merge any paragraphs. The number of output paragraphs MUST exactly match the input."
            )
            
            context_str = f"--- PREVIOUS CONTEXT (DO NOT TRANSLATE) ---\nEN: {prev_ec}\nKR: {prev_kc}\n\n" if prev_ec else ""
            pr = f"{context_str}--- GLOSSARY ---\n{glossary}\n\n--- NOTES ---\n{notes}\n\n--- EN ---\n{ec}\n\n--- KR ---\n{kc}\n\n--- DRAFT ---\n{draft}"
            refined = generate_with_retry(target_model, pr, sys_r, None)

            lines = refined.strip().split('\n')
            clean = [l for l in lines if not l.startswith(('Đây là', 'Bản dịch', 'Tuyệt vời', 'Đã sửa', 'Dưới đây là', 'Sau đây là', 'Sure'))]
            return idx, "\n".join(clean)

        import concurrent.futures
        completed = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            futures = [executor.submit(process_chunk, i) for i in range(n_chunks)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    idx, text = future.result()
                    final[idx] = text
                    completed += 1
                    bar.progress(completed / n_chunks, f"Hoàn thành {completed}/{n_chunks} phần...")
                    status.write(f"  ✅ Phần {idx+1} đã xong!")
                except Exception as e:
                    status.write(f"  ❌ Lỗi ở một phần: {e}")

        bar.progress(1.0, "✅ Hoàn tất!")
        status.update(label=f"✅ Xong trong {time.time()-t0:.0f}s!", state="complete")

        result = "\n\n".join(final)
        # Apply smart quotes
        # Mở rộng để thay thế cặp "" và ''
        import re
        result = re.sub(r'"([^"]*)"', r'“\1”', result)
        result = re.sub(r"'([^']*)'", r'‘\1’', result)
        save_file(PATHS['output'], result)
        st.session_state['trans_result'] = result
        st.session_state['_t_out_ver'] = st.session_state.get('_t_out_ver', 0) + 1
        st.balloons()

    if 'trans_result' in st.session_state:
        st.divider()
        st.markdown("#### 📤 Kết quả")
        st.text_area("Bản dịch", st.session_state['trans_result'], height=350, key=f"t_out_{st.session_state.get('_t_out_ver', 0)}")
        c1, c2 = st.columns([1, 3])
        with c1:
            st.download_button("⬇️ Tải file", st.session_state['trans_result'],
                               f"vi_final_{now_gmt7().strftime('%Y%m%d_%H%M')}.txt", use_container_width=True)
        with c2:
            st.info("💾 Đã lưu `output/vi_final.txt` | Bản cũ lưu tại `vi_previous.txt`")

# =================== TAB 2: QC REVIEW ===================
with tabs[2]:
    if not client:
        st.warning("⚠️ Cấu hình API Key trước.")
    else:
        st.markdown("#### 📥 Dữ liệu QC")
        qsrc_opts = ["📋 Paste"] if HIDE_LOCAL_FILE_OPTION else ["📂 File (input/qc/)", "📋 Paste"]
        qsrc_idx = 0 if len(qsrc_opts) == 1 else 1
        qsrc = st.radio("Nguồn:", qsrc_opts, index=qsrc_idx, horizontal=True, key="q_src")

        if not qsrc.startswith("📋"):
            vi_t = load_file(PATHS['vi_qc'])
            kr_t = load_file(PATHS['kor_qc'])
            en_t = load_file(PATHS['eng_qc'])
            st.info(f"VI: {len(vi_t.splitlines())} dòng | KR: {len(kr_t.splitlines())} | EN: {len(en_t.splitlines())}")
        else:
            vi_t = st.text_area("Bản dịch VI", height=200, key="q_vi")
            c1, c2 = st.columns(2)
            with c1: kr_t = st.text_area("Tiếng Hàn", height=200, key="q_kr")
            with c2: en_t = st.text_area("Tiếng Anh (tùy chọn)", height=200, key="q_en")

        qc_model = st.selectbox(
            "🤖 AI Model (QC):",
            ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-3.1-flash-lite"],
            index=0,
            key="q_model_sel",
            help="gemini-2.5-flash (tức 1.5-flash) thường ổn định và ít lỗi token nhất."
        )

        if st.button("🔍 Chạy QC", type="primary"):
            target_model = qc_model
            log_action("QC Review", f"VI: {len((vi_t or '').splitlines())} dòng | KR: {len((kr_t or '').splitlines())} dòng | Model: {target_model}")
            if not vi_t.strip():
                st.error("❌ Thiếu Bản dịch VI để đối chiếu!")
                st.stop()
            if not kr_t.strip() and not en_t.strip():
                st.error("❌ Cần ít nhất một ngôn ngữ nguồn (KR hoặc EN) để đối chiếu!")
                st.stop()

            glossary = load_file(PATHS['glossary'])
            notes = load_file(PATHS['notes'])
            vi_lines = vi_t.split('\n')
            kr_lines = kr_t.split('\n')
            en_lines = en_t.split('\n') if en_t else []

            lpc = 50
            nc = (max(len(vi_lines), len(kr_lines)) + lpc - 1) // lpc
            report = [f"# BÁO CÁO QC — {now_gmt7().strftime('%d/%m/%Y %H:%M')}\n"]
            new_terms = []

            bar = st.progress(0)
            status = st.status(f"🔍 QC — {nc} phần", expanded=True)

            for i in range(nc):
                si, ei = i*lpc, (i+1)*lpc
                bar.progress(i/nc, f"Phần {i+1}/{nc}...")
                status.write(f"📋 Phần {i+1}/{nc} — dòng {si+1}~{min(ei, len(vi_lines))}")

                vi_chunk = ""
                for idx, ln in enumerate(vi_lines[si:ei], start=si+1):
                    vi_chunk += f"{idx}: {ln}\n"
                kr_chunk = "\n".join(kr_lines[si:ei])
                en_ref = ""
                if en_lines:
                    en_ref = f"==== EN ====\n{chr(10).join(en_lines[si:ei])}\n\n"

                pqc = (
                    f"==== GLOSSARY ====\n{glossary}\n\n==== NOTES ====\n{notes}\n\n"
                    "==== TASK ====\nCompare VI translation with sources. Report by line number.\n"
                    "Format: ### Dòng [N]:\n- [Lỗi]: \"quote\" - reason\n- [Gợi ý]: fix\n\n"
                    f"==== KR ====\n{kr_chunk}\n\n{en_ref}==== VI ====\n{vi_chunk}"
                )
                rc = generate_with_retry(target_model, pqc, "Professional QC Editor.", status)
                if rc and rc.strip():
                    report.append(rc)
                    status.write(f"  ⚠️ Lỗi ở phần {i+1}")
                else:
                    status.write(f"  ✅ Phần {i+1} OK")

                # Extract new terms
                pe = (
                    f"Find terms in SOURCE not in GLOSSARY.\n==== GLOSSARY ====\n{glossary}\n{notes}\n\n"
                    f"==== SOURCE ====\n{kr_chunk}\n\nFormat: - [Term]: [Translation]"
                )
                ec = generate_with_retry(target_model, pe, "Glossary Extractor.", status)
                if ec and ec.strip(): new_terms.append(ec.strip())
                time.sleep(2)

            bar.progress(1.0, "✅ QC xong!")
            status.update(label="✅ QC Hoàn tất!", state="complete")

            rpt = "\n".join([str(r) for r in report if r])
            save_file(PATHS['qc_report'], rpt)
            st.session_state['qc_report'] = rpt

            if new_terms:
                nt = "\n".join(list(set(new_terms)))
                save_file(PATHS['new_terms'], nt)
                st.session_state['new_terms'] = nt

        if 'qc_report' in st.session_state:
            st.divider()
            st.markdown("#### 📋 Báo cáo QC")
            st.markdown(st.session_state['qc_report'])
            st.download_button("⬇️ Tải báo cáo", st.session_state['qc_report'], "qc_report.txt")
            if 'new_terms' in st.session_state:
                with st.expander("✨ Thuật ngữ mới gợi ý"):
                    st.markdown(st.session_state['new_terms'])

# =================== TAB 3: SO SÁNH (DIFF) ===================
with tabs[3]:
    st.markdown("#### 📊 So sánh bản dịch")
    st.caption("So sánh hai phiên bản dịch để thấy sự khác biệt — hữu ích sau khi Re-Refine.")

    diff_font = st.slider("🔤 Cỡ chữ (px)", 13, 22, 15, 1, key="diff_font")

    diff_src_opts = ["📋 Paste thủ công"] if HIDE_LOCAL_FILE_OPTION else ["📂 vi_previous.txt ↔ vi_final.txt (tự động)", "📋 Paste thủ công"]
        
    diff_src_idx = 0 if len(diff_src_opts) == 1 else 1
    diff_src = st.radio("Nguồn dữ liệu:", diff_src_opts, index=diff_src_idx, horizontal=True, key="d_src")

    if not diff_src.startswith("📋"):
        old_text = load_file(PATHS['output_prev'])
        new_text = load_file(PATHS['output'])
        if not old_text:
            st.warning("⚠️ Chưa có `vi_previous.txt`. Hãy dịch hoặc Re-Refine 1 lần để tạo bản backup.")
        elif not new_text:
            st.warning("⚠️ Chưa có `vi_final.txt`.")
        else:
            st.success(f"✅ Bản cũ: {len(old_text.splitlines())} dòng | Bản mới: {len(new_text.splitlines())} dòng")
    else:
        c1, c2 = st.columns(2)
        with c1:
            old_text = st.text_area("📄 Bản cũ", height=250, key="d_old", placeholder="Paste bản cũ...")
        with c2:
            new_text = st.text_area("📄 Bản mới", height=250, key="d_new", placeholder="Paste bản mới...")

    if st.button("🔍 So sánh", type="primary", key="d_btn"):
        log_action("So Sánh (Diff)", f"Bản cũ: {len((old_text or '').splitlines())} dòng | Bản mới: {len((new_text or '').splitlines())} dòng")
        if not old_text or not new_text:
            st.error("❌ Cần cả hai bản để so sánh!")
        else:
            added, deleted, changed = compute_diff_stats(old_text, new_text)

            st.divider()
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("➕ Thêm mới", f"{added} dòng")
            c2.metric("➖ Xóa bỏ", f"{deleted} dòng")
            c3.metric("✏️ Thay đổi", f"{changed} dòng")
            total_changes = added + deleted + changed
            total_lines = max(len(old_text.splitlines()), len(new_text.splitlines()))
            pct = (total_changes / total_lines * 100) if total_lines else 0
            c4.metric("📊 Tỷ lệ thay đổi", f"{pct:.1f}%")

            diff_html = render_diff_html(old_text, new_text)
            st.markdown(f'<div style="font-size:{diff_font}px;line-height:1.7;">{diff_html}</div>', unsafe_allow_html=True)

            st.session_state['last_diff'] = diff_html

# =================== TAB 4: ĐỐI CHIẾU SIDE-BY-SIDE ===================
with tabs[4]:
    st.markdown("#### 📖 Đối chiếu bản dịch với bản gốc")
    st.caption("Hiển thị song song từng dòng bản dịch và bản gốc để bạn tự đối chiếu, rà soát.")

    sbs_font = st.slider("🔤 Cỡ chữ (px)", 13, 22, 15, 1, key="sbs_font")
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        edit_mode = st.toggle("✏️ Chế độ chỉnh sửa tay", value=False, key="sbs_edit",
                              help="Bật để chỉnh sửa trực tiếp bản dịch VI theo từng dòng")
    with c_s2:
        hl_mode = st.toggle("✨ Highlight Thuật ngữ", value=True, key="sbs_hl",
                            help="Bôi sáng các thuật ngữ có trong Glossary")

    # --- Chọn nguồn ---
    sbs_src_opts = ["📋 Paste thủ công"] if HIDE_LOCAL_FILE_OPTION else ["📂 Từ file có sẵn", "📋 Paste thủ công"]
    sbs_src_idx = 0 if len(sbs_src_opts) == 1 else 1
    sbs_src = st.radio("Nguồn bản gốc:", sbs_src_opts, index=sbs_src_idx, horizontal=True, key="sbs_src")
    sbs_lang = st.radio("Ngôn ngữ gốc hiển thị:", ["🇺🇸 Tiếng Anh (EN)", "🇰🇷 Tiếng Hàn (KR)", "🇺🇸🇰🇷 Cả hai"], horizontal=True, key="sbs_lang")

    if not sbs_src.startswith("📋"):
        sbs_vi = load_file(PATHS['output'])
        sbs_en = load_file(PATHS['eng_trans'])
        sbs_kr = load_file(PATHS['kor_trans'])
        info_parts = []
        if sbs_vi: info_parts.append(f"VI: {len(sbs_vi.splitlines())} dòng")
        if sbs_en: info_parts.append(f"EN: {len(sbs_en.splitlines())} dòng")
        if sbs_kr: info_parts.append(f"KR: {len(sbs_kr.splitlines())} dòng")
        if info_parts:
            st.info(" | ".join(info_parts))
        if not sbs_vi:
            st.warning("⚠️ Chưa có `output/vi_final.txt`. Hãy dịch trước.")
    else:
        # Key widget thay đổi mỗi lần Lưu → Streamlit tạo widget mới, nhận value mới
        _vi_ver = st.session_state.get('_sbs_vi_ver', 0)
        _vi_default = ""
        if '_sbs_vi_pending' in st.session_state:
            _vi_default = st.session_state.pop('_sbs_vi_pending')
        sbs_vi = st.text_area("Bản dịch Tiếng Việt", value=_vi_default, height=180,
                               key=f"sbs_vi_in_{_vi_ver}", placeholder="Paste bản dịch VI...")
        c1, c2 = st.columns(2)
        with c1:
            sbs_en = st.text_area("Bản gốc EN", height=180, key="sbs_en_in", placeholder="Paste bản EN...")
        with c2:
            sbs_kr = st.text_area("Bản gốc KR", height=180, key="sbs_kr_in", placeholder="Paste bản KR...")

    if st.button("📖 Hiển thị đối chiếu", type="primary", key="sbs_btn"):
        log_action("Đối Chiếu (SBS)", f"VI: {len((sbs_vi or '').splitlines())} dòng | Ngôn ngữ: {sbs_lang}")
        if not sbs_vi:
            st.error("❌ Thiếu bản dịch VI!")
        else:
            st.session_state['sbs_current_page'] = 1
            st.session_state['sbs_data'] = {
                'vi': sbs_vi.splitlines(),
                'en': (sbs_en.splitlines() if sbs_en else []),
                'kr': (sbs_kr.splitlines() if sbs_kr else []),
            }

    # --- Hiển thị kết quả (dùng session_state để persist qua reruns) ---
    if 'sbs_data' in st.session_state:
        vi_lines = list(st.session_state['sbs_data']['vi'])
        en_lines = st.session_state['sbs_data']['en']
        kr_lines = st.session_state['sbs_data']['kr']

        show_en = "EN" in sbs_lang or "Cả hai" in sbs_lang
        show_kr = "KR" in sbs_lang or "Cả hai" in sbs_lang
        show_both = show_en and show_kr
        max_lines = max(len(vi_lines), len(en_lines), len(kr_lines))

        # Phân trang
        lines_per_page = 50
        total_pages = max(1, (max_lines + lines_per_page - 1) // lines_per_page)

        # Khởi tạo trạng thái trang nếu chưa có
        if 'sbs_current_page' not in st.session_state:
            st.session_state['sbs_current_page'] = 1
        
        def update_sbs_page(key):
            st.session_state['sbs_current_page'] = st.session_state[key]
            st.session_state['sbs_scroll_top'] = True

        page_options = list(range(1, total_pages + 1))
        page_format = lambda x: f"Trang {x} (dòng {(x-1)*lines_per_page+1}~{min(x*lines_per_page, max_lines)})"

        st.markdown('<div id="sbs-top-anchor"></div>', unsafe_allow_html=True)
        if st.session_state.pop('sbs_scroll_top', False):
            import streamlit.components.v1 as components
            components.html(
                '''<script>
                    const anchor = window.parent.document.getElementById('sbs-top-anchor');
                    if(anchor) anchor.scrollIntoView({behavior: 'smooth'});
                </script>''', height=0
            )

        st.divider()
        c1, c2, c3 = st.columns([1, 2, 1])
        with c2:
            # Dropdown phía TRÊN
            st.selectbox(f"Trang (tổng {total_pages})",
                         page_options,
                         index=st.session_state['sbs_current_page'] - 1,
                         key="sbs_top",
                         on_change=update_sbs_page,
                         args=("sbs_top",),
                         format_func=page_format)
        
        # Lấy giá trị trang hiện tại để tính toán start/end
        page = st.session_state['sbs_current_page']

        st.divider()
        c1, c2, c3 = st.columns([1, 2, 1])
        start = (page - 1) * lines_per_page
        end = min(start + lines_per_page, max_lines)

        if not edit_mode:
            # ===== CHẾ ĐỘ XEM (READ-ONLY) =====
            # Build highlight pattern
            hl_pattern = None
            if hl_mode:
                gl_text_hl = load_file(PATHS['glossary'])
                notes_text_hl = load_file(PATHS['notes'])
                hl_pattern = build_highlight_pattern(gl_text_hl, notes_text_hl)

            html_parts = [f'<div class="sbs-wrap"><table class="sbs-table" style="font-size:{sbs_font}px;line-height:1.8;">']
            if show_both:
                html_parts.append('<tr><th class="sbs-num">#</th><th>🇺🇸 English</th><th>🇰🇷 Korean</th><th>🇻🇳 Tiếng Việt</th></tr>')
            elif show_en:
                html_parts.append('<tr><th class="sbs-num">#</th><th>🇺🇸 English</th><th>🇻🇳 Tiếng Việt</th></tr>')
            else:
                html_parts.append('<tr><th class="sbs-num">#</th><th>🇰🇷 Korean</th><th>🇻🇳 Tiếng Việt</th></tr>')

            for idx in range(start, end):
                num = idx + 1
                vi_l = html_lib.escape(vi_lines[idx]) if idx < len(vi_lines) else '<span class="sbs-empty">—</span>'
                if hl_pattern and idx < len(vi_lines) and vi_lines[idx].strip():
                    vi_l = hl_pattern.sub(r'<span class="term-hl" title="Thuật ngữ Glossary">\1</span>', vi_l)
                
                en_l = html_lib.escape(en_lines[idx]) if idx < len(en_lines) else '<span class="sbs-empty">—</span>'
                kr_l = html_lib.escape(kr_lines[idx]) if idx < len(kr_lines) else '<span class="sbs-empty">—</span>'
                if show_both:
                    html_parts.append(f'<tr><td class="sbs-num">{num}</td><td class="sbs-src">{en_l}</td><td class="sbs-src">{kr_l}</td><td class="sbs-vi">{vi_l}</td></tr>')
                elif show_en:
                    html_parts.append(f'<tr><td class="sbs-num">{num}</td><td class="sbs-src">{en_l}</td><td class="sbs-vi">{vi_l}</td></tr>')
                else:
                    html_parts.append(f'<tr><td class="sbs-num">{num}</td><td class="sbs-src">{kr_l}</td><td class="sbs-vi">{vi_l}</td></tr>')

            html_parts.append('</table></div>')
            st.markdown('\n'.join(html_parts), unsafe_allow_html=True)
            st.caption(f"Hiển thị dòng {start+1} → {end} / {max_lines}")

            # Pagination ở dưới cho chế độ xem
            st.divider()
            cb1, cb2, cb3 = st.columns([1, 2, 1])
            with cb2:
                st.selectbox("Trang dưới",
                             page_options,
                             index=st.session_state['sbs_current_page'] - 1,
                             key="sbs_bottom_view",
                             on_change=update_sbs_page,
                             args=("sbs_bottom_view",),
                             format_func=page_format,
                             label_visibility="collapsed")
        else:
            # ===== CHẾ ĐỘ CHỈNH SỬA TAY (custom rows - tự giãn chiều cao) =====
            st.info("✏️ Chỉnh sửa trực tiếp ô **Tiếng Việt** bên phải. Bấm **💾 Lưu** khi xong.")

            # Xác định bố cục cột dựa vào nguồn hiển thị
            if show_en and show_kr:
                ratios = [1, 5, 5, 7]
                hdr_labels = ["#", "🇺🇸 EN", "🇰🇷 KR", "🇻🇳 Tiếng Việt"]
            elif show_en:
                ratios = [1, 6, 7]
                hdr_labels = ["#", "🇺🇸 EN", "🇻🇳 Tiếng Việt"]
            else:
                ratios = [1, 6, 7]
                hdr_labels = ["#", "🇰🇷 KR", "🇻🇳 Tiếng Việt"]

            # Header
            hdr_cols = st.columns(ratios)
            for i, lbl in enumerate(hdr_labels):
                hdr_cols[i].markdown(f"<small><b>{lbl}</b></small>", unsafe_allow_html=True)
            st.divider()

            # Từng dòng
            for idx in range(start, end):
                vi_val = vi_lines[idx] if idx < len(vi_lines) else ""
                # Tính chiều cao text_area dựa trên số dòng thực tế (tối thiểu 3 dòng)
                n_lines = max(3, len(vi_val.splitlines()) + 1) if vi_val else 3
                ta_height = min(400, max(100, n_lines * 26 + 20))

                cols = st.columns(ratios)
                with cols[0]:
                    st.markdown(
                        f"<div style='padding-top:8px;color:#888;font-size:12px;text-align:center'>{idx+1}</div>",
                        unsafe_allow_html=True
                    )
                src_col_i = 1
                if show_en:
                    with cols[src_col_i]:
                        en_val = html_lib.escape(en_lines[idx]) if idx < len(en_lines) else ""
                        st.markdown(
                            f"<div style='padding:6px 4px;font-size:13px;white-space:pre-wrap;word-break:break-word;line-height:1.5'>{en_val}</div>",
                            unsafe_allow_html=True
                        )
                    src_col_i += 1
                if show_kr:
                    with cols[src_col_i]:
                        kr_val = html_lib.escape(kr_lines[idx]) if idx < len(kr_lines) else ""
                        st.markdown(
                            f"<div style='padding:6px 4px;font-size:13px;white-space:pre-wrap;word-break:break-word;line-height:1.5'>{kr_val}</div>",
                            unsafe_allow_html=True
                        )
                with cols[-1]:
                    # Dùng key duy nhất cho mỗi dòng
                    st.text_area(
                        "VI", value=vi_val, height=ta_height,
                        key=f"vi_edit_p{page}_{idx}",
                        label_visibility="collapsed"
                    )
                st.divider()

            # Dropdown phía DƯỚI (Chế độ Sửa) - đưa lên trước nút Lưu
            st.divider()
            cb1, cb2, cb3 = st.columns([1, 2, 1])
            with cb2:
                st.selectbox("Trang dưới edit",
                             page_options,
                             index=st.session_state['sbs_current_page'] - 1,
                             key="sbs_bottom_edit",
                             on_change=update_sbs_page,
                             args=("sbs_bottom_edit",),
                             format_func=page_format,
                             label_visibility="collapsed")

            col_save, col_info = st.columns([1, 3])
            with col_save:
                if st.button("💾 Lưu thay đổi", type="primary", key="sbs_save"):
                    for idx in range(start, end):
                        new_val = st.session_state.get(
                            f"vi_edit_p{page}_{idx}",
                            vi_lines[idx] if idx < len(vi_lines) else ""
                        )
                        if idx < len(vi_lines):
                            vi_lines[idx] = new_val
                    st.session_state['sbs_data']['vi'] = vi_lines
                    full_text = "\n".join(vi_lines)
                    save_file(PATHS['output'], full_text)
                    # Cập nhật state để phản hồi ngay lập tức
                    st.session_state['_sbs_vi_pending'] = full_text
                    st.session_state['trans_result'] = full_text
                    st.session_state['_sbs_vi_ver'] = st.session_state.get('_sbs_vi_ver', 0) + 1
                    st.rerun()
            with col_info:
                st.caption(f"Đang sửa dòng {start+1} → {end} / {max_lines}")

# =================== TAB 5: TRUYỆN TRANH ===================
with tabs[5]:
    if not client:
        st.warning("⚠️ Cấu hình API Key trước.")
    else:
        st.markdown("#### 🎨 Dịch Truyện Tranh (Manhwa Translator)")
        st.caption("Tải lên các ảnh của chapter. AI sẽ nhìn ảnh, nhận diện bong bóng thoại (OCR Hàn) và dịch sang tiếng Việt.")
        
        mh_hist_dir = os.path.join(BASE_DIR, 'output', 'manhwa_history')
        os.makedirs(mh_hist_dir, exist_ok=True)
        
        sessions = sorted([d for d in os.listdir(mh_hist_dir) if os.path.isdir(os.path.join(mh_hist_dir, d))], reverse=True)
        
        st.divider()
        c_sess1, c_sess2 = st.columns([3, 1])
        with c_sess1:
            opts = ["+ TẠO PHIÊN BẢN MỚI"] + sessions
            # Retrieve default index from session_state if it exists
            default_ix = 0
            if 'current_mh_sess' in st.session_state and st.session_state['current_mh_sess'] in opts:
                default_ix = opts.index(st.session_state['current_mh_sess'])
                
            sess_choice = st.selectbox("📂 Chọn Chapter / Phiên bản đã lưu:", opts, index=default_ix)
            # Update state with current choice immediately so we remember it
            st.session_state['current_mh_sess'] = sess_choice
            
        with c_sess2:
            st.write(" ")
            if sess_choice != "+ TẠO PHIÊN BẢN MỚI":
                # Create two small columns for Rename and Delete
                cr1, cr2 = st.columns(2)
                with cr2:
                    if st.button("🗑️ Xóa", use_container_width=True, help="Xóa vĩnh viễn phiên bản này"):
                        import shutil
                        shutil.rmtree(os.path.join(mh_hist_dir, sess_choice))
                        st.success("✅ Đã xóa!")
                        st.rerun()
                with cr1:
                    if st.button("✏️ Đổi tên", use_container_width=True):
                        st.session_state['mh_rename_mode'] = sess_choice

        st.divider()

        # Logic đổi tên dùng session_state để không bị mất khi rerun
        if sess_choice != "+ TẠO PHIÊN BẢN MỚI" and st.session_state.get('mh_rename_mode') == sess_choice:
            with st.container(border=True):
                new_n = st.text_input("Nhập tên mới cho folder:", value=sess_choice, key="rename_val_input")
                c_rn1, c_rn2, c_rn3 = st.columns([1, 1, 3])
                if c_rn1.button("Lưu ✅", type="primary"):
                    new_n = new_n.strip().replace('/', '-').replace('\\', '-')
                    if new_n and new_n != sess_choice:
                        old_p = os.path.join(mh_hist_dir, sess_choice)
                        new_p = os.path.join(mh_hist_dir, new_n)
                        if os.path.exists(new_p):
                            st.error("❌ Tên này đã tồn tại!")
                        else:
                            try:
                                os.rename(old_p, new_p)
                                st.session_state['current_mh_sess'] = new_n
                                del st.session_state['mh_rename_mode']
                                st.success(f"✅ Đã đổi tên thành `{new_n}`")
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Lỗi: {e}")
                if c_rn2.button("Hủy ❌"):
                    del st.session_state['mh_rename_mode']
                    st.rerun()

        if sess_choice == "+ TẠO PHIÊN BẢN MỚI":
            # Initialize a stable default name if not exists
            if 'mh_new_sess_def' not in st.session_state:
                st.session_state['mh_new_sess_def'] = f"Chapter_{now_gmt7().strftime('%Y%m%d_%H%M')}"
                
            new_sess_name = st.text_input("Tên Chapter mới (Tạo thư mục):", 
                                         value=st.session_state['mh_new_sess_def'],
                                         key="mh_new_sess_input")
            
            # Use the user's input from the widget key to be safe
            final_sess_name = st.session_state["mh_new_sess_input"].strip().replace('/', '-').replace('\\', '-')
            if not final_sess_name:
                final_sess_name = st.session_state['mh_new_sess_def']
            
            # --- CHỌN NGUỒN ẢNH: Upload hoặc Google Drive ---
            try:
                from scripts.google_helper import is_configured as _gd_configured
                _has_gdrive = _gd_configured()
            except Exception:
                try:
                    from google_helper import is_configured as _gd_configured
                    _has_gdrive = _gd_configured()
                except Exception:
                    _has_gdrive = False

            img_source_opts = ["📁 Upload ảnh"]
            if _has_gdrive:
                img_source_opts.append("☁️ Google Drive")
            img_source = st.radio("Nguồn ảnh:", img_source_opts, horizontal=True, key="mh_img_source")
            uploaded_files = None
            drive_images_ready = False

            if img_source == "📁 Upload ảnh":
                uploaded_files = st.file_uploader("🖼️ Chọn ảnh truyện tranh (JPG, PNG, WEBP)", type=["png", "jpg", "jpeg", "webp"], accept_multiple_files=True)
            elif img_source == "☁️ Google Drive":
                try:
                    from scripts.google_helper import list_images_in_folder, list_subfolders, download_file_to_bytes, parse_folder_id_from_url
                except ImportError:
                    from google_helper import list_images_in_folder, list_subfolders, download_file_to_bytes, parse_folder_id_from_url

                drive_input = st.text_input("🔗 Link hoặc ID folder Google Drive chứa ảnh raw:", 
                                            placeholder="https://drive.google.com/drive/folders/... hoặc Folder ID",
                                            key="mh_drive_folder")
                if st.button("🔍 Quét folder Drive", key="mh_scan_drive"):
                    if not drive_input.strip():
                        st.error("❌ Hãy nhập link hoặc ID folder!")
                    else:
                        try:
                            fid = parse_folder_id_from_url(drive_input)
                            with st.spinner("⏳ Đang quét folder..."):
                                imgs = list_images_in_folder(fid)
                                subs = list_subfolders(fid)
                                # Also scan sub-folders for images
                                for sub in subs:
                                    sub_imgs = list_images_in_folder(sub["id"])
                                    for si in sub_imgs:
                                        si["_subfolder"] = sub["name"]
                                    imgs.extend(sub_imgs)
                            if imgs:
                                st.session_state['mh_drive_images'] = imgs
                                st.session_state['mh_drive_folder_id'] = fid
                                st.success(f"✅ Tìm thấy **{len(imgs)}** ảnh trên Drive!")
                            else:
                                st.warning("⚠️ Không tìm thấy ảnh nào trong folder này.")
                        except Exception as e:
                            st.error(f"❌ Lỗi khi quét Drive: {e}")

                if 'mh_drive_images' in st.session_state:
                    imgs_list = st.session_state['mh_drive_images']
                    st.caption(f"📋 {len(imgs_list)} ảnh: " + ", ".join([f"`{i['name']}`" for i in imgs_list[:10]]) + ("..." if len(imgs_list) > 10 else ""))
                    drive_images_ready = True

            stitch_mh = st.checkbox("🧩 Tự động nối dải ảnh trước khi dịch", value=False, help="Nếu ảnh bị cắt ngắn, ghép chúng lại thành dải dài (Stitching) sẽ giúp AI đọc chuẩn xác không bị đứt câu.")
            
            c1, c2 = st.columns([2, 1])
            with c1:
                target_model = st.selectbox("🤖 AI Model (Truyện tranh):", 
                                          ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-3.1-flash-lite"], 
                                          index=0, help="2.5-flash (tức 1.5-flash) thường ổn định và ít lỗi token nhất.")
            with c2:
                process_btn = st.button("🚀 Bắt đầu Quét & Dịch", type="primary", use_container_width=True)

            # --- TẢI ẢNH TỪ DRIVE NẾU CẦN ---
            if process_btn and drive_images_ready and not uploaded_files:
                import PIL.Image as _PILImg
                import io as _io
                drive_img_list = st.session_state.get('mh_drive_images', [])
                if drive_img_list:
                    status_dl = st.status(f"☁️ Đang tải {len(drive_img_list)} ảnh từ Drive...", expanded=True)
                    class DriveImg:
                        def __init__(self, name, img):
                            self.name = name
                            self.img = img
                    uploaded_files = []
                    for idx, dimg in enumerate(drive_img_list):
                        status_dl.write(f"📥 [{idx+1}/{len(drive_img_list)}] `{dimg['name']}`")
                        try:
                            img_bytes = download_file_to_bytes(dimg["id"])
                            pil_img = _PILImg.open(_io.BytesIO(img_bytes)).convert('RGB')
                            uploaded_files.append(DriveImg(dimg["name"], pil_img))
                        except Exception as e:
                            status_dl.write(f"   ⚠️ Lỗi tải `{dimg['name']}`: {e}")
                    status_dl.update(label=f"✅ Đã tải xong!", state="complete")
                    st.session_state['_mh_drive_sourced'] = True

            if process_btn and uploaded_files:
                # target_model đã được lấy từ selectbox ở trên
                log_action("Truyện Tranh", f"Ảnh: {len(uploaded_files)} | Session: {final_sess_name} | Model: {target_model}")
                import PIL.Image
                
                # --- STITCHING PRE-PROCESSING ---
                files_to_process = []
                if stitch_mh and len(uploaded_files) > 1:
                    status_stitch = st.status("🧩 Đang phân tích và ghép nối ảnh...", expanded=True)
                    # Sắp xếp thứ tự tự nhiên (Natural Sort) + xử lý Windows Duplicate (VD: ảnh (1) xếp sau ảnh gốc)
                    uploaded_files = sorted(uploaded_files, key=lambda x: get_windows_sort_key(x.name))
                    images = []
                    for uf in uploaded_files:
                        try:
                            im = PIL.Image.open(uf).convert('RGB')
                            images.append((uf.name, im))
                        except Exception:
                            pass
                    
                    if images:
                        stitched_chunks = []
                        current_chunk = []
                        current_h = 0
                        current_w = 0
                        MAX_HEIGHT = 5000
                        
                        for f, img in images:
                            if current_h + img.height > MAX_HEIGHT and current_chunk:
                                stitched_chunks.append((current_chunk, current_w, current_h))
                                current_chunk = [(f, img)]
                                current_h = img.height
                                current_w = img.width
                            else:
                                current_chunk.append((f, img))
                                current_h += img.height
                                current_w = max(current_w, img.width)
                                
                        if current_chunk:
                            stitched_chunks.append((current_chunk, current_w, current_h))
                            
                        class StitchedImg:
                            def __init__(self, name, img):
                                self.name = name
                                self.img = img
                                
                        for i, (chunk, w, h) in enumerate(stitched_chunks):
                            canvas = PIL.Image.new('RGB', (w, h), (255, 255, 255))
                            y_offset = 0
                            for f, img in chunk:
                                x_offset = (w - img.width) // 2
                                canvas.paste(img, (x_offset, y_offset))
                                y_offset += img.height
                            
                            fname = f"stitched_{i+1:03d}.jpg"
                            files_to_process.append(StitchedImg(fname, canvas))
                        
                        status_stitch.update(label=f"✅ Nối ảnh xong! (Ghép thành {len(files_to_process)} dải dài)", state="complete")
                
                if not files_to_process:
                    if st.session_state.get('_mh_drive_sourced'):
                        # Drive images are already PIL objects with .name and .img
                        files_to_process = uploaded_files
                    else:
                        class RawImg:
                            def __init__(self, name, uf):
                                self.name = name
                                self.img = PIL.Image.open(uf).convert('RGB')
                        files_to_process = [RawImg(uf.name, uf) for uf in uploaded_files]
                
                # --- TẠO THƯ MỤC VÀ LƯU ẢNH GỐC ĐỂ BACKUP ---
                sess_dir = os.path.join(mh_hist_dir, final_sess_name)
                sess_img_dir = os.path.join(sess_dir, 'images')
                os.makedirs(sess_img_dir, exist_ok=True)
                
                for fo in files_to_process:
                    save_path = os.path.join(sess_img_dir, fo.name)
                    if not os.path.exists(save_path):
                        fo.img.save(save_path, quality=90)
                
                glossary = load_file(PATHS['glossary'])
                notes = load_file(PATHS['notes'])
                
                status = st.status(f"🚀 Đang xử lý {len(files_to_process)} ảnh...", expanded=True)
                bar = st.progress(0)
                
                all_results = []
                t0 = time.time()
                
                for i, file_obj in enumerate(files_to_process):
                    fname = file_obj.name
                    bar.progress(i / len(files_to_process), f"Đang quét ảnh {i+1}/{len(files_to_process)}...")
                    
                    # --- XỬ LÝ SLICING NỘI BỘ CHO ẢNH QUÁ DÀI ---
                    MAX_H_LIMIT = 5000
                    raw_img = file_obj.img
                    if raw_img.height > MAX_H_LIMIT:
                        slices = split_long_image(raw_img, max_h=MAX_H_LIMIT, overlap=250)
                        status.write(f"✂️ Ảnh `{fname}` quá dài, chia làm {len(slices)} phần để OCR...")
                    else:
                        slices = [raw_img]
                    
                    combined_texts = []
                    for s_idx, slc_img in enumerate(slices):
                        part_info = f" (Phần {s_idx+1}/{len(slices)})" if len(slices) > 1 else ""
                        status.write(f"🖼️ Đang quét: `{fname}`{part_info}")
                        
                        max_attempts = 3
                        slice_res = ""
                        for attempt in range(1, max_attempts + 1):
                            try:
                                optimized_img = optimize_image_for_api(slc_img)
                                sys_m = (
                                    "You are an expert Manhwa/Webtoon translator and typesetter assistant. "
                                    "Your primary task is to accurately OCR the Korean text from speech bubbles and translate it into natural Vietnamese. "
                                    "Ignore small background SFX (Sound Effects) unless they are crucial to the plot. "
                                    "CRITICAL OCR RULE: You must be extremely precise with Korean transcription. Look for every small dash or dot. Do not guess or hallucinate based on context if the text is clear. "
                                    "CRITICAL FORMAT RULE: If a single speech bubble contains multiple lines of text, you MUST join them into a SINGLE line separated by a space in both the KR and VI output. Do NOT preserve line breaks within the same dialogue box.\n"
                                    "Format your output cleanly and exactly like this:\n"
                                    "[Khung thoại]\n"
                                    "KR: <Exact Korean transcription in a SINGLE line>\n"
                                    "<Natural Vietnamese translation in a SINGLE line>\n\n"
                                    "Rules: Follow the provided glossary. Ensure pronouns match the Korean nuances and glossary rules."
                                )
                                prompt = f"--- GLOSSARY ---\n{glossary}\n\n--- NOTES ---\n{notes}\n\n--- TASK ---\nExtract dialogues from this image and translate them to Vietnamese. Keep them in reading order (top to bottom, right to left generally)."
                                contents = [optimized_img, prompt]
                                res = generate_with_retry(target_model, contents, sys_m, status, temp=0.1)
                                
                                if res and res.strip():
                                    slice_res = res.strip()
                                    status.write(f"   ✅ Xong {part_info}")
                                    time.sleep(12) 
                                    break 
                                else:
                                    if attempt < max_attempts:
                                        status.write(f"   ⚠️ Thất bại {part_info} (Lần {attempt}/{max_attempts}). Thử lại...")
                                        time.sleep(20)
                                    else:
                                        slice_res = f"[LỖI: AI KHÔNG TRẢ VỀ KẾT QUẢ PHẦN {s_idx+1}]"
                            except Exception as e:
                                if attempt < max_attempts:
                                    status.write(f"   ⚠️ Lỗi {part_info}: {e}. Thử lại...")
                                    time.sleep(20)
                                else:
                                    slice_res = f"[LỖI HỆ THỐNG PHẦN {s_idx+1}: {e}]"
                        
                        combined_texts.append(slice_res)
                    
                    # Gộp kết quả của tất cả các slice vào 1 entry duy nhất cho ảnh gốc
                    final_image_text = "\n\n".join(combined_texts)
                    all_results.append(f"📄 ẢNH: {fname}\n\n{final_image_text}\n")
                    
                    # Lưu backup sau mỗi ảnh gốc hoàn tất
                    save_file(os.path.join(sess_dir, "script.txt"), "\n\n".join(all_results))
                        
                bar.progress(1.0, "✅ Hoàn tất tiến trình hiện tại!")
                status.update(label=f"✅ Kết thúc quá trình quét (Save Backup) trong {time.time()-t0:.0f}s", state="complete")
                
                st.balloons()
                st.session_state['current_mh_sess'] = final_sess_name
                if 'mh_new_sess_def' in st.session_state: del st.session_state['mh_new_sess_def']
                st.rerun()
            
        elif sess_choice != "+ TẠO PHIÊN BẢN MỚI":
            # Mode: View and Edit existing history
            sess_dir = os.path.join(mh_hist_dir, sess_choice)
            sess_script_path = os.path.join(sess_dir, "script.txt")
            sess_img_dir = os.path.join(sess_dir, "images")
            
            mh_content = load_file(sess_script_path)
            
            # Helper: Parse master script into a dict of {filename: content}
            import re
            parts = re.split(r'📄 ẢNH: (.*?)\n', mh_content)
            parsed_data = {}
            if len(parts) > 1:
                for i in range(1, len(parts), 2):
                    fname = parts[i].strip()
                    text = parts[i+1].strip() if i+1 < len(parts) else ""
                    parsed_data[fname] = text
            
            st.markdown(f"#### 📑 Biên tập Chapter: {sess_choice}")
            
            if os.path.exists(sess_img_dir):
                saved_imgs = sorted(os.listdir(sess_img_dir))
                
                # Tính năng: Dịch lại các ảnh lỗi
                failed_imgs = []
                for img_name in saved_imgs:
                    text = parsed_data.get(img_name, "").strip()
                    if "[LỖI" in text or text == "":
                        failed_imgs.append(img_name)
                        
                if failed_imgs and saved_imgs:
                    st.warning(f"⚠️ Phát hiện {len(failed_imgs)} ảnh bị lỗi trong quá trình dịch.")
                    if st.button("🔄 Dịch lại các ảnh bị lỗi", type="primary", use_container_width=True):
                        import PIL.Image
                        glossary = load_file(PATHS['glossary'])
                        notes = load_file(PATHS['notes'])
                        target_model = "gemini-3.1-flash-lite"
                        
                        status_retry = st.status(f"🚀 Đang dịch lại {len(failed_imgs)} ảnh lỗi...", expanded=True)
                        bar_retry = st.progress(0)
                        
                        for i, fname in enumerate(failed_imgs):
                            bar_retry.progress(i / len(failed_imgs), f"Đang quét lại ảnh {i+1}/{len(failed_imgs)}...")
                            status_retry.write(f"🖼️ Đang quét lại: `{fname}`")
                            
                            img_path = os.path.join(sess_img_dir, fname)
                            if not os.path.exists(img_path):
                                status_retry.write(f"   ❌ Không tìm thấy file gốc `{fname}`.")
                                continue
                                
                            max_attempts = 3
                            for attempt in range(1, max_attempts + 1):
                                try:
                                    raw_img = PIL.Image.open(img_path).convert('RGB')
                                    optimized_img = optimize_image_for_api(raw_img)
                                    
                                    sys_m = (
                                        "You are an expert Manhwa/Webtoon translator and typesetter assistant. "
                                        "You extract Korean text strictly from speech bubbles or important narrative boxes and translate it into natural, flowing Vietnamese. "
                                        "Ignore small background SFX (Sound Effects) unless they are crucial to the plot. "
                                        "CRITICAL RULE: If a single speech bubble contains multiple lines of text, you MUST join them into a SINGLE line separated by a space in both the KR and VI output. Do NOT preserve line breaks within the same dialogue box.\n"
                                        "Format your output cleanly and exactly like this:\n"
                                        "[Khung thoại]\n"
                                        "KR: <Korean text in a SINGLE line>\n"
                                        "<Vietnamese translation in a SINGLE line>\n\n"
                                        "Rules: Follow the provided glossary. Ensure pronouns match the Korean nuances and glossary rules."
                                    )
                                    
                                    prompt = f"--- GLOSSARY ---\n{glossary}\n\n--- NOTES ---\n{notes}\n\n--- TASK ---\nExtract dialogues from this image and translate them to Vietnamese. Keep them in reading order (top to bottom, right to left generally)."
                                    
                                    contents = [optimized_img, prompt]
                                    res = generate_with_retry(target_model, contents, sys_m, status_retry)
                                    
                                    if res and res.strip() and "[LỖI" not in res:
                                        parsed_data[fname] = res.strip()
                                        status_retry.write(f"   ✅ Xong `{fname}`")
                                        # Cập nhật master script ngay lập tức
                                        reconstructed = "\n\n".join([f"📄 ẢNH: {n}\n\n{parsed_data.get(n, '')}\n" for n in saved_imgs])
                                        save_file(sess_script_path, reconstructed)
                                        time.sleep(15) 
                                        break # Thành công
                                    else:
                                        if attempt < max_attempts:
                                            status_retry.write(f"   ⚠️ Thất bại `{fname}` (Lần {attempt}/{max_attempts}). Đang thử lại sau 20s...")
                                            time.sleep(20)
                                        else:
                                            status_retry.write(f"   ❌ Bỏ qua `{fname}` sau {max_attempts} lần thử.")
                                except Exception as e:
                                    if attempt < max_attempts:
                                        status_retry.write(f"   ⚠️ Lỗi `{fname}` (Lần {attempt}/{max_attempts}): {e}. Đang thử lại sau 20s...")
                                        time.sleep(20)
                                    else:
                                        status_retry.write(f"   ❌ Bỏ qua `{fname}` do lỗi hệ thống.")
                                        
                        bar_retry.progress(1.0, "✅ Hoàn tất dịch lại!")
                        status_retry.update(label=f"✅ Đã xử lý xong các ảnh lỗi", state="complete")
                        st.rerun()

                if saved_imgs:
                    st.divider()
                    
                    # Individual image-text rows
                    new_parsed_data = {}
                    for img_name in saved_imgs:
                        st.markdown(f"🖼️ **{img_name}**")
                        c1, c2 = st.columns([1, 1])
                        with c1:
                            st.image(os.path.join(sess_img_dir, img_name), use_container_width=True)
                        with c2:
                            st.markdown('<div class="sticky-anchor"></div>', unsafe_allow_html=True)
                            current_val = parsed_data.get(img_name, "")
                            st.markdown('<style>textarea[aria-label="Bản dịch:"] { font-size: 26px !important; line-height: 1.5 !important; }</style>', unsafe_allow_html=True)
                            input_val = st.text_area("Bản dịch:", current_val, height=500, key=f"mh_edit_{sess_choice}_{img_name}")
                            new_parsed_data[img_name] = input_val
                        st.divider()

                    # Reconstruct script for saving/downloading
                    reconstructed_script = "\n\n".join([f"📄 ẢNH: {n}\n\n{new_parsed_data.get(n, '')}\n" for n in saved_imgs])

                    # Check Google API availability
                    try:
                        from scripts.google_helper import is_configured as _gd_check, create_google_doc, get_root_folder_id, create_subfolder as _gd_mkdir
                        _has_gdocs = _gd_check()
                    except ImportError:
                        try:
                            from google_helper import is_configured as _gd_check, create_google_doc, get_root_folder_id, create_subfolder as _gd_mkdir
                            _has_gdocs = _gd_check()
                        except Exception:
                            _has_gdocs = False

                    # Bottom Actions
                    if _has_gdocs:
                        col_save, col_dl, col_gdoc = st.columns([1, 1, 1])
                    else:
                        col_save, col_dl = st.columns([1, 1])
                        col_gdoc = None

                    with col_dl:
                         st.download_button("⬇️ Tải Kịch bản (.txt)", reconstructed_script, 
                                           f"{sess_choice}.txt", use_container_width=True)
                    with col_save:
                        if st.button("💾 Lưu tất cả thay đổi", type="primary", use_container_width=True, key="mh_save_all"):
                            save_file(sess_script_path, reconstructed_script)
                            st.success("✅ Đã lưu toàn bộ bản dịch!")
                            st.rerun()

                    if col_gdoc is not None:
                        with col_gdoc:
                            if st.button("📤 Đẩy lên Google Docs", use_container_width=True, key="mh_push_gdoc"):
                                st.session_state['_show_gdoc_options'] = True

                    if st.session_state.get('_show_gdoc_options'):
                        try:
                            from scripts.google_helper import parse_folder_id_from_url as _parse_fid
                        except ImportError:
                            from google_helper import parse_folder_id_from_url as _parse_fid
                        gdoc_folder_input = st.text_input(
                            "📂 Folder Drive của Chapter (VD: folder '156'):",
                            placeholder="Paste link folder chapter trên Drive...",
                            key="gdoc_folder_input",
                            help="Doc sẽ được tạo trực tiếp trong folder này với tên '{chapter}'"
                        )
                        if st.button("✅ Xác nhận đẩy lên Docs", type="primary", key="gdoc_confirm"):
                            with st.spinner("☁️ Đang tạo Google Doc..."):
                                try:
                                    if gdoc_folder_input.strip():
                                        target_fid = _parse_fid(gdoc_folder_input)
                                    else:
                                        target_fid = get_root_folder_id()
                                        
                                    import re
                                    gdoc_script = reconstructed_script
                                    # 1. Bỏ "KR: " và "VI: "
                                    gdoc_script = re.sub(r'^(?:KR|VI):\s*', '', gdoc_script, flags=re.MULTILINE | re.IGNORECASE)
                                    
                                    # 2. Rút gọn ghi chú ẢNH
                                    parts = gdoc_script.split("📄 ẢNH: ")
                                    if len(parts) > 1:
                                        processed_gdoc = parts[0]
                                        current_group = None
                                        for part in parts[1:]:
                                            lines = part.split('\n', 1)
                                            img_name = lines[0].strip()
                                            content = lines[1] if len(lines) > 1 else ""
                                            
                                            group_name = img_name.split('_')[0] if '_' in img_name else img_name.rsplit('.', 1)[0]
                                            
                                            if group_name != current_group:
                                                processed_gdoc += f"\n📄 ẢNH: {group_name}\n"
                                                current_group = group_name
                                            
                                            processed_gdoc += content
                                        
                                        # Cleanup multiple newlines
                                        gdoc_script = re.sub(r'\n{3,}', '\n\n', processed_gdoc).strip()

                                    # Đặt Doc trực tiếp trong folder chapter, tên "{chapter}"
                                    result = create_google_doc(
                                        title=f"{sess_choice}",
                                        content=gdoc_script,
                                        folder_id=target_fid,
                                    )
                                    st.success(f"✅ Đã tạo Google Doc!")
                                    st.markdown(f"🔗 [Mở Google Docs]({result['doc_url']})")
                                    log_action("Google Docs", f"Tạo Doc: {sess_choice}")
                                    st.session_state['_show_gdoc_options'] = False
                                except Exception as e:
                                    st.error(f"❌ Lỗi tạo Google Doc: {e}")

                else:
                    st.info("Chưa có ảnh gốc nào được lưu lại cho Lịch sử này.")
            else:
                st.error("Không tìm thấy thư mục ảnh cho phiên bản này.")

# =================== TAB 6: TẢI TRUYỆN ===================
with tabs[6]:
    st.markdown("#### 📥 Tải ảnh truyện tranh hàng loạt")
    st.caption("Công cụ này sử dụng `gallery-dl` để tự động cào ảnh gốc từ các trang truyện (Naver, Kakao, Webtoons...) về rồi nén thành file ZIP cho bạn.")
    
    dl_url = st.text_input("🔗 Nhập Link Truyện (URL):", placeholder="https://comic.naver.com/webtoon/detail?titleId=...")
    stitch_images = st.checkbox("🧩 Tự động nối các dải ảnh bị cắt đứt (Stitching)", value=True, help="Ghép nối liền mạch các ảnh bị cắt ngắn (VD: Webtoon) thành 1 dải ảnh dài. Giới hạn 15,000px cấu hình mỗi file ảnh để tránh quá khổ cho AI và trình xem.")
    
    c1, c2 = st.columns([1, 1])
    with c1:
        submit_dl = st.button("🚀 Bắt đầu Tải & Nén", type="primary", use_container_width=True)
        
    if submit_dl:
        if not dl_url.strip():
            st.error("❌ Link không được bỏ trống!")
        else:
            log_action("Tải Truyện", f"URL: {dl_url[:40]}...")
            import tempfile, subprocess
            
            with st.spinner("⏳ Đang cào ảnh từ Web... Xin vui lòng đợi, quá trình này có thể mất vài phút! (Không F5 hay đóng trang)"):
                tmp_dir = tempfile.mkdtemp()
                zip_path = os.path.join(tempfile.gettempdir(), f"manhwa_{int(time.time())}")
                try:
                    # Execute gallery-dl module
                    res = subprocess.run([sys.executable, "-m", "gallery_dl", "--directory", tmp_dir, dl_url], capture_output=True, text=True)
                    
                    # Optional stitching logic
                    if stitch_images:
                        import PIL.Image
                        for root, dirs, files in os.walk(tmp_dir):
                            img_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))]
                            if not img_files:
                                continue
                            
                            # Sort properly using natural sorting + Windows Duplicate handling
                            img_files.sort(key=get_windows_sort_key)
                            
                            images = []
                            for f in img_files:
                                try:
                                    img = PIL.Image.open(os.path.join(root, f))
                                    if img.mode != 'RGB':
                                        img = img.convert('RGB')
                                    images.append((f, img))
                                except Exception:
                                    pass
                            
                            if not images:
                                continue
                            
                            stitched_chunks = []
                            current_chunk = []
                            current_h = 0
                            current_w = 0
                            MAX_HEIGHT = 15000
                            
                            for f, img in images:
                                if current_h + img.height > MAX_HEIGHT and current_chunk:
                                    stitched_chunks.append((current_chunk, current_w, current_h))
                                    current_chunk = [(f, img)]
                                    current_h = img.height
                                    current_w = img.width
                                else:
                                    current_chunk.append((f, img))
                                    current_h += img.height
                                    current_w = max(current_w, img.width)
                                    
                            if current_chunk:
                                stitched_chunks.append((current_chunk, current_w, current_h))
                                
                            # Create new images and delete old ones
                            for i, (chunk, w, h) in enumerate(stitched_chunks):
                                canvas = PIL.Image.new('RGB', (w, h), (255, 255, 255))
                                y_offset = 0
                                for f, img in chunk:
                                    x_offset = (w - img.width) // 2  # Center align
                                    canvas.paste(img, (x_offset, y_offset))
                                    y_offset += img.height
                                
                                save_path = os.path.join(root, f"stitched_{i+1:03d}.jpg")
                                canvas.save(save_path, 'JPEG', quality=90)
                                
                            for f, img in images:
                                img.close()
                                try:
                                    os.remove(os.path.join(root, f))
                                except Exception:
                                    pass

                    # Count downloaded/stitched images
                    total_files = 0
                    for root, dirs, files in os.walk(tmp_dir):
                        total_files += len([f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.gif'))])
                        
                    if total_files > 0:
                        st.success(f"✅ Đã tải về thành công **{total_files}** ảnh. Đang nén thành Zip...")
                        
                        # Zip the directory
                        shutil.make_archive(zip_path, 'zip', tmp_dir)
                        
                        with open(f"{zip_path}.zip", "rb") as f:
                            zip_data = f.read()
                            
                        mb_size = f"{len(zip_data) / (1024 * 1024):.2f}"
                        st.download_button(
                            label=f"⬇️ TẢI FILE ZIP ({mb_size} MB)",
                            data=zip_data,
                            file_name=f"truyen_{int(time.time())}.zip",
                            mime="application/zip",
                            type="primary",
                            use_container_width=True
                        )
                    else:
                        st.error("❌ Không tải được ảnh nào. Có thể trang web này không được hỗ trợ hoặc cần đăng nhập (Trả phí).")
                        if res.stderr or res.stdout:
                            with st.expander("Xem bảng log hệ thống"):
                                st.code(res.stderr + "\n" + res.stdout)
                                
                except Exception as e:
                    st.error(f"❌ Có lỗi hệ thống bất ngờ xảy ra: {e}")
                finally:
                    # Cleanup generated files from server disk
                    shutil.rmtree(tmp_dir, ignore_errors=True)
                    try:
                        os.remove(f"{zip_path}.zip")
                    except Exception:
                        pass

# =================== TAB 7: GLOSSARY ===================
with tabs[7]:
    st.markdown("#### 📚 Quản lý Glossary")

    g_tab1, g_tab2, g_tab3 = st.tabs(["📖 Glossary", "📝 Personal Notes", "🔄 Đồng bộ"])

    with g_tab1:
        gl = load_file(PATHS['glossary'])
        if gl:
            st.markdown(f'<div class="glossary-box">{gl[:8000]}{"..." if len(gl)>8000 else ""}</div>', unsafe_allow_html=True)
            st.caption(f"📏 {len(gl)} ký tự | {len(gl.splitlines())} dòng")
        else:
            st.info("Chưa có glossary. Chạy đồng bộ từ Google Sheets.")

    with g_tab2:
        notes = load_file(PATHS['notes'])
        edited = st.text_area("Chỉnh sửa Personal Notes:", notes, height=300, key="g_notes")
        if st.button("💾 Lưu Notes", key="g_save"):
            save_file(PATHS['notes'], edited)
            st.success("✅ Đã lưu!")
            st.rerun()

    with g_tab3:
        st.markdown("Đồng bộ glossary từ Google Sheets bằng script `update_glossary.py`.")
        if st.button("🔄 Chạy đồng bộ", key="g_sync"):
            with st.spinner("Đang đồng bộ..."):
                import subprocess
                result = subprocess.run(
                    [sys.executable, os.path.join(BASE_DIR, 'scripts', 'update_glossary.py')],
                    capture_output=True, text=True, cwd=BASE_DIR, encoding='utf-8'
                )
                if result.returncode == 0:
                    st.success("✅ Đồng bộ thành công!")
                    st.code(result.stdout)
                else:
                    st.error("❌ Lỗi đồng bộ!")
                    st.code(result.stderr)

# =================== TAB 8: CẮT ẢNH ===================
with tabs[8]:
    st.markdown("#### ✂️ Cắt Ảnh Dạng Strip (Giao diện Web)")
    st.caption("Công cụ được tích hợp trực tiếp trên Web. Bạn chỉ cần tải ảnh lên và dùng chuột click vào ảnh để đánh dấu nét cắt.")
    
    try:
        from streamlit_image_coordinates import streamlit_image_coordinates
        import PIL.Image
        from PIL import ImageDraw
    except ImportError:
        st.error("❌ Thiếu thư viện giao diện nâng cao.")
        st.info("Mở Terminal và gõ lệnh sau để cài nhé:\n`pip install streamlit-image-coordinates Pillow`")
        st.stop()
        
    upl_img = st.file_uploader("🖼️ Chọn ảnh manhwa dài để cắt", type=["png", "jpg", "jpeg", "webp"], key="cutter_uploader")
    
    if upl_img:
        # State tracking points
        if 'cut_points' not in st.session_state or st.session_state.get('last_upl_img') != upl_img.name:
            st.session_state['cut_points'] = []
            st.session_state['last_upl_img'] = upl_img.name
            
            # NÉN ẢNH VÀ RESIZE ĐỂ HIỂN THỊ (Giảm lag tối đa cho Web)
            sys_img = PIL.Image.open(upl_img)
            if sys_img.mode != 'RGB':
                sys_img = sys_img.convert('RGB')
                
            orig_w, orig_h = sys_img.size
            max_display_width = 1000
            display_scale = 1.0
            if orig_w > max_display_width:
                display_scale = max_display_width / orig_w
            
            # Lưu tỷ lệ để tính toán tọa độ cắt sau này
            st.session_state['disp_scale'] = display_scale
            
            if display_scale < 1.0:
                new_size = (int(orig_w * display_scale), int(orig_h * display_scale))
                # Dùng NEAREST cho tốc độ nhanh nhất như yêu cầu "giảm tối đa chất lượng"
                sys_img = sys_img.resize(new_size, PIL.Image.NEAREST)
                
            import io
            buf = io.BytesIO()
            sys_img.save(buf, format="JPEG", quality=40, optimize=True)
            buf.seek(0)
            st.session_state['disp_img_cache'] = PIL.Image.open(buf)
            
        original_img = PIL.Image.open(upl_img)
        if original_img.mode != 'RGB':
            original_img = original_img.convert('RGB')
            
        c1, c2 = st.columns([2, 1])
        
        with c2:
            st.markdown("### 🎛️ Bảng Điều Khiển")
            
            cb1, cb2 = st.columns(2)
            with cb1:
                if st.button("⏪ Hoàn tác", use_container_width=True):
                    if st.session_state['cut_points']:
                        st.session_state['cut_points'].pop()
                        st.rerun()
            with cb2:
                if st.button("🗑️ Xóa sạch", use_container_width=True):
                    st.session_state['cut_points'] = []
                    st.rerun()
                    
            st.write(f"📍 Đang có: **{len(st.session_state['cut_points'])} điểm cắt**")
            # Hiển thị list vị trí cắt để User có cơ sở kiểm chứng
            if st.session_state['cut_points']:
                st.code(", ".join([str(y) for y in st.session_state['cut_points']]))
            
            st.divider()
            if st.button("✂️ XÁC NHẬN CẮT VÀ LƯU", type="primary", use_container_width=True):
                if not st.session_state['cut_points']:
                    st.warning("⚠️ Bạn chưa click chọn điểm cắt nào trên ảnh!")
                else:
                    base_name = os.path.splitext(upl_img.name)[0]
                    ext = os.path.splitext(upl_img.name)[1]
                    
                    # Lưu trong output/<tên-ảnh>_cut
                    out_dir = os.path.join(BASE_DIR, 'output', f"{base_name}_cut")
                    os.makedirs(out_dir, exist_ok=True)
                    
                    w, h = original_img.size
                    pts = [0] + sorted(st.session_state['cut_points']) + [h]
                    part_num = 1
                    
                    for i in range(len(pts) - 1):
                        y1, y2 = pts[i], pts[i+1]
                        if y2 <= y1: continue
                        
                        box = (0, y1, w, y2)
                        cropped = original_img.crop(box)
                        
                        out_path = os.path.join(out_dir, f"{base_name}_{part_num:03d}{ext}")
                        if ext.lower() in ['.jpg', '.jpeg']:
                            cropped.save(out_path, quality=100, subsampling=0)
                        elif ext.lower() in ['.webp']:
                            cropped.save(out_path, quality=100, lossless=True)
                        else:
                            cropped.save(out_path)
                            
                        part_num += 1
                        
                    st.success(f"🎉 Thành công! Đã cắt thành **{part_num-1}** mảnh.")
                    st.info(f"📂 Đã lưu tại thư mục nội bộ:\n`{out_dir}`")
                    
                    # Tạo file ZIP để User tải về máy luôn
                    import shutil
                    zip_name = f"{base_name}_cut_package"
                    zip_path = os.path.join(BASE_DIR, 'output', zip_name)
                    shutil.make_archive(zip_path, 'zip', out_dir)
                    
                    with open(f"{zip_path}.zip", "rb") as f:
                        st.download_button(
                            label="⬇️ TẢI FILE ZIP CÁC PHẦN ĐÃ CẮT",
                            data=f.read(),
                            file_name=f"{zip_name}.zip",
                            mime="application/zip",
                            type="primary",
                            use_container_width=True
                        )
                    st.balloons()
            
            # Hiển thị list Preview các mảnh đã cắt nếu có
            base_name_preview = os.path.splitext(upl_img.name)[0]
            preview_dir = os.path.join(BASE_DIR, 'output', f"{base_name_preview}_cut")
            if os.path.exists(preview_dir):
                with st.expander("👁️ Xem trước các mảnh đã cắt"):
                    files = sorted([f for f in os.listdir(preview_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])
                    for f in files:
                        st.image(os.path.join(preview_dir, f), caption=f)
            
        with c1:
            st.info("👈 Click trực tiếp lên ảnh để đặt mốc. Vạch mốc sẽ hiện ở thanh Thước bên trái.")
            
            disp_img = st.session_state['disp_img_cache']
            scale = st.session_state.get('disp_scale', 1.0)
            
            # --- TỐI ƯU CỘT VỚI KÍCH THƯỚC CỐ ĐỊNH (FIXED PIXELS) ---
            # Ép Ruler và Ảnh hiển thị đúng pixel gốc để không bao giờ bị lệch height
            ruler_w = 50
            r_col, i_col = st.columns([ruler_w, disp_img.width], gap="small")
            
            with r_col:
                # Tạo ảnh Ruler
                ruler_img = PIL.Image.new("RGB", (ruler_w, disp_img.height), "#1a1b26")
                r_draw = ImageDraw.Draw(ruler_img)
                for y_pt in st.session_state['cut_points']:
                    disp_y = int(y_pt * scale)
                    r_draw.line([(5, disp_y), (ruler_w-5, disp_y)], fill="#3498db", width=12)
                
                # CHUYỂN RULER SANG BASE64 ĐỂ SET HEIGHT CỐ ĐỊNH BẰNG HTML
                import base64
                from io import BytesIO
                buffered = BytesIO()
                ruler_img.save(buffered, format="PNG")
                img_base64 = base64.b64encode(buffered.getvalue()).decode()
                
                # Ép trình duyệt hiển thị đúng pixel height bằng CSS
                st.markdown(
                    f'<img src="data:image/png;base64,{img_base64}" style="width:{ruler_w}px; height:{disp_img.height}px; display:block; border-radius:4px; margin-top: 1rem;">', 
                    unsafe_allow_html=True
                )
                
            with i_col:
                # Ép ảnh chính cũng phải hiển thị đúng pixel đã tính toán
                st.markdown(f"""
                    <style>
                        div[data-testid="stHorizontalBlock"] img {{
                            height: {disp_img.height}px !important;
                            max-width: none !important;
                        }}
                    </style>
                """, unsafe_allow_html=True)
                
                value = streamlit_image_coordinates(
                    disp_img, 
                    key="img_cutter_permanent_display"
                )
            
            if value is not None:
                clicked_y = int(value['y'] / scale)
                if clicked_y not in st.session_state['cut_points']:
                    st.session_state['cut_points'].append(clicked_y)
                    st.session_state['cut_points'].sort()
                    st.rerun()

# =================== TAB 9: REFORMAT SCRIPT ===================
with tabs[9]:
    st.subheader("📋 Reformat Script")
    st.caption("Lọc script dịch: giữ lại chỉ phần dịch tiếng Việt, bỏ header [Khung thoại] và dòng KR:.")

    def reformat_translation_script(raw: str, case_mode: str) -> str:
        import re
        result = []
        for line in raw.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if re.match(r'^\[.*\]', stripped):
                continue
            if re.match(r'^KR\s*:', stripped):
                continue
            
            # Xử lý viết hoa theo chế độ được chọn
            if case_mode == "VIẾT HOA TOÀN BỘ":
                line = line.upper()
            elif case_mode == "Viết hoa chữ cái đầu câu":
                parts = re.split(r'((?<=[.!?])\s+)', line)
                for i in range(0, len(parts), 2):
                    s = parts[i]
                    if s.isupper():
                        s = s.lower()
                    parts[i] = re.sub(r'([^\W\d_])', lambda m: m.group(1).upper(), s, count=1)
                line = "".join(parts)
                
            result.append(line)
        return '\n'.join(result)

    case_mode = st.radio(
        "Chế độ viết hoa (Case Mode):",
        options=["Giữ nguyên (As-is)", "VIẾT HOA TOÀN BỘ", "Viết hoa chữ cái đầu câu"],
        index=0,
        horizontal=True,
        key="reformat_case_mode"
    )

    rf_input = st.text_area(
        "Dán script dịch vào đây:",
        height=350,
        key="reformat_input",
        placeholder="[Khung thoại]\nKR: 화염 저항 아이템 협찬 성현제\nTrang bị kháng lửa\nNgười tài trợ\nSung Hyunjae\n\n[Khung thoại]\nKR: 지나간 자리마다 폐허!\nNơi cô đi qua đều trở thành phế tích!"
    )

    if st.button("▶ Reformat", key="reformat_btn", type="primary"):
        if rf_input.strip():
            reformatted = reformat_translation_script(rf_input, case_mode)
            st.session_state['reformat_output'] = reformatted
        else:
            st.warning("Vui lòng dán script vào ô trên.")

    if st.session_state.get('reformat_output'):
        st.text_area(
            "Kết quả:",
            value=st.session_state['reformat_output'],
            height=350,
            key="reformat_output_area"
        )
        st.download_button(
            label="⬇ Tải xuống .txt",
            data=st.session_state['reformat_output'],
            file_name="script_vi.txt",
            mime="text/plain",
            key="reformat_download"
        )

# =================== TAB 10: NOVEL AGENT ===================
# ============================================================
# NOVEL AGENT — Helper functions (isolated, no global glossary)
# ============================================================
NOVEL_PROJECTS_DIR = os.path.join(BASE_DIR, 'novel_projects')
os.makedirs(NOVEL_PROJECTS_DIR, exist_ok=True)

def na_project_dir(slug: str) -> str:
    return os.path.join(NOVEL_PROJECTS_DIR, slug)

def na_load_json(path: str, default=None):
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return default if default is not None else {}

def na_save_json(path: str, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def na_list_projects() -> list:
    if not os.path.exists(NOVEL_PROJECTS_DIR):
        return []
    result = []
    for name in sorted(os.listdir(NOVEL_PROJECTS_DIR)):
        cfg_path = os.path.join(NOVEL_PROJECTS_DIR, name, 'config.json')
        if os.path.exists(cfg_path):
            result.append(name)
    return result

def na_load_config(slug: str) -> dict:
    return na_load_json(os.path.join(na_project_dir(slug), 'config.json'), {})

def na_save_config(slug: str, cfg: dict):
    na_save_json(os.path.join(na_project_dir(slug), 'config.json'), cfg)

def na_chapter_dir(slug: str, chapter_id: str) -> str:
    return os.path.join(na_project_dir(slug), 'chapters', chapter_id)

def na_list_chapters(slug: str) -> list:
    ch_root = os.path.join(na_project_dir(slug), 'chapters')
    if not os.path.exists(ch_root):
        return []
    return sorted([d for d in os.listdir(ch_root)
                   if os.path.isdir(os.path.join(ch_root, d))])

def na_load_memory(slug: str) -> dict:
    mem_dir = os.path.join(na_project_dir(slug), 'memory')
    return {
        'characters': na_load_json(os.path.join(mem_dir, 'characters.json'), []),
        'glossary':   na_load_json(os.path.join(mem_dir, 'glossary.json'), []),
        'timeline':   na_load_json(os.path.join(mem_dir, 'timeline.json'), []),
        'relationships': na_load_json(os.path.join(mem_dir, 'relationships.json'), []),
    }

def na_save_memory(slug: str, memory: dict):
    mem_dir = os.path.join(na_project_dir(slug), 'memory')
    os.makedirs(mem_dir, exist_ok=True)
    for key in ['characters', 'glossary', 'timeline', 'relationships']:
        if key in memory:
            na_save_json(os.path.join(mem_dir, f'{key}.json'), memory[key])

def na_slugify(title: str) -> str:
    import re
    s = title.strip().lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    return s[:48] or 'novel'

def na_format_memory_for_prompt(memory: dict) -> str:
    lines = []
    if memory.get('characters'):
        lines.append('=== CHARACTERS ===')
        for c in memory['characters'][:30]:  # cap to avoid huge prompts
            aliases = ', '.join(c.get('aliases', []))
            lines.append(f"- {c.get('name','')} ({c.get('gender','')}) | Aliases: {aliases} | Speech: {c.get('speech_style','')} | Honorifics: {c.get('honorifics','')}")
    if memory.get('glossary'):
        lines.append('\n=== PROJECT GLOSSARY ===')
        for g in memory['glossary'][:60]:
            lines.append(f"- {g.get('original','')} → {g.get('translation','')} [{g.get('category','')}]")
    return '\n'.join(lines)

def na_format_clarifications_for_prompt(clarifications: dict) -> str:
    answers = clarifications.get('answers', {})
    questions = clarifications.get('questions', [])
    lines = []
    for q in questions:
        qid = q.get('id', '')
        if qid in answers:
            ans = answers[qid]
            chosen = ans.get('custom') or ans.get('choice', '')
            lines.append(f"- [{q.get('category','').upper()}] \"{q.get('original','')}\" → Use: {chosen}")
    return '\n'.join(lines) if lines else 'None'

def na_build_translation_prompt(cfg: dict, memory: dict, prev_summary: str,
                                 curr_analysis: dict, clarifications: dict,
                                 prev_chunk_tail: str, chunk_text: str) -> str:
    target_lang = cfg.get('target_lang', 'Vietnamese')
    style_guide = cfg.get('style_guide', '')
    mem_str = na_format_memory_for_prompt(memory)
    clar_str = na_format_clarifications_for_prompt(clarifications)
    ch_summary = curr_analysis.get('chapter_summary', '') if curr_analysis else ''

    parts = []
    if style_guide:
        parts.append(f"=== STYLE GUIDE ===\n{style_guide}")
    if prev_summary:
        parts.append(f"=== PREVIOUS CHAPTER SUMMARY ===\n{prev_summary}")
    if ch_summary:
        parts.append(f"=== CURRENT CHAPTER CONTEXT ===\n{ch_summary}")
    if mem_str:
        parts.append(f"=== NOVEL MEMORY ===\n{mem_str}")
    if clar_str and clar_str != 'None':
        parts.append(f"=== USER DECISIONS (Clarifications) ===\n{clar_str}")
    if prev_chunk_tail:
        parts.append(f"=== PREVIOUS CONTEXT (DO NOT RETRANSLATE) ===\n{prev_chunk_tail}")
    parts.append(f"=== TRANSLATE TO {target_lang.upper()} ===\n{chunk_text}")
    return '\n\n'.join(parts)

def na_get_prev_chapter_summary(slug: str, chapter_id: str) -> str:
    chapters = na_list_chapters(slug)
    if chapter_id not in chapters:
        return ''
    idx = chapters.index(chapter_id)
    if idx == 0:
        return ''
    prev_ch = chapters[idx - 1]
    summary = na_load_json(os.path.join(na_chapter_dir(slug, prev_ch), 'summary.json'), {})
    return summary.get('summary', '')

def na_save_chapter_as_md(slug: str, chapter_id: str, content: str):
    """Save translated chapter as .md with frontmatter."""
    cfg = na_load_config(slug)
    title = f"{cfg.get('title', slug)} — {chapter_id}"
    md_content = f"---\ntitle: {title}\n---\n\n{content}"
    out_path = os.path.join(na_chapter_dir(slug, chapter_id), 'translation.md')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    return out_path

# =================== TAB 11 RENDERING ===================
with tabs[11]:
    if not client:
        st.warning("⚠️ Cấu hình API Key trong `.env` trước.")
        st.stop()

    st.markdown("""
    <div style='background:linear-gradient(135deg,#0D9488 0%,#0B7A70 100%);
         border:1px solid #D1CFC7;border-radius:12px;padding:1.2rem 1.6rem;margin-bottom:1rem;color:#ffffff'>
      <h2 style='margin:0;color:#ffffff;font-size:1.5rem'>🤖 Novel Agent</h2>
      <p style='margin:0.3rem 0 0;color:rgba(255,255,255,0.85);font-size:0.9rem'>
        AI dịch tiểu thuyết — Ghi nhớ dài hạn · Human-in-the-loop · Nhất quán xuyên suốt
      </p>
    </div>
    """, unsafe_allow_html=True)

    na_sub = st.tabs(["📁 Projects", "📥 Import Chapter", "🔬 Analyze",
                      "❓ Clarifications", "🌐 Translate", "🧠 Memory"])

    # ── Helper: project selector (persistent) ──
    all_projects = na_list_projects()
    _na_proj_opts = ["(Chưa chọn project)"] + all_projects
    _na_proj_default = 0
    if st.session_state.get('na_project') in all_projects:
        _na_proj_default = _na_proj_opts.index(st.session_state['na_project'])

    # ===================== SUB-TAB 0: PROJECTS =====================
    with na_sub[0]:
        st.markdown("### 📁 Quản lý Projects")

        col_list, col_create = st.columns([2, 3])

        with col_list:
            st.markdown("**Projects hiện có:**")
            if not all_projects:
                st.info("Chưa có project nào. Tạo mới ở bên phải.")
            else:
                for p in all_projects:
                    pcfg = na_load_config(p)
                    n_ch = len(na_list_chapters(p))
                    active = (st.session_state.get('na_project') == p)
                    border_color = '#0D9488' if active else '#D1CFC7'
                    st.markdown(f"""
                    <div style='border:1px solid {border_color};border-radius:8px;
                         padding:0.7rem 1rem;margin-bottom:0.5rem;
                         background:{'rgba(13, 148, 136, 0.08)' if active else '#F8F6F0'}'>
                      <b style='color:#2D2A26'>{pcfg.get('title', p)}</b>
                      <span style='float:right;color:#8c8273;font-size:12px'>{n_ch} chương</span><br>
                      <span style='color:#5c564d;font-size:12px'>{pcfg.get('source_lang','?')} → {pcfg.get('target_lang','?')}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    c_sel, c_del = st.columns([3, 1])
                    with c_sel:
                        if st.button(f"✅ Chọn", key=f"na_sel_{p}", use_container_width=True):
                            st.session_state['na_project'] = p
                            st.rerun()
                    with c_del:
                        if st.button("🗑️", key=f"na_del_{p}", use_container_width=True,
                                     help="Xóa project này"):
                            st.session_state[f'na_del_confirm_{p}'] = True
                    if st.session_state.get(f'na_del_confirm_{p}'):
                        st.warning(f"Xóa project **{p}**? Không thể hoàn tác!")
                        c1d, c2d = st.columns(2)
                        if c1d.button("✅ Xác nhận xóa", key=f"na_del_ok_{p}", type="primary"):
                            import shutil as _shutil
                            _shutil.rmtree(na_project_dir(p), ignore_errors=True)
                            if st.session_state.get('na_project') == p:
                                del st.session_state['na_project']
                            del st.session_state[f'na_del_confirm_{p}']
                            st.rerun()
                        if c2d.button("❌ Hủy", key=f"na_del_cancel_{p}"):
                            del st.session_state[f'na_del_confirm_{p}']
                            st.rerun()

        with col_create:
            st.markdown("**Tạo project mới:**")
            with st.form("na_create_form"):
                na_title = st.text_input("Tên tiểu thuyết *", placeholder="VD: Thiên Đạo Đồ Thư Quán")
                c1f, c2f = st.columns(2)
                with c1f:
                    na_src_lang = st.selectbox("Ngôn ngữ gốc",
                        ["Chinese", "Korean", "Japanese", "English", "Other"])
                with c2f:
                    na_tgt_lang = st.selectbox("Ngôn ngữ dịch",
                        ["Vietnamese", "English"])
                na_style = st.text_area("Style Guide (tùy chọn)",
                    placeholder="VD: Dịch văn xuôi trang trọng. Giữ nguyên tên nhân vật phiên âm. Xưng hô theo cấp bậc võ lâm...",
                    height=100)
                na_threshold = st.slider(
                    "Ngưỡng tự động dịch (%)",
                    min_value=50, max_value=95, value=80,
                    help="AI sẽ hỏi khi confidence < ngưỡng này. ≥95% = tự dịch. 80-95% = đánh dấu review."
                )
                na_chunk_sz = st.slider("Kích thước chunk (đoạn văn/chunk)",
                                        5, 50, 20, 5,
                                        help="Số đoạn văn trong mỗi đơn vị dịch. Novel dài nên để 15-25.")
                submitted = st.form_submit_button("🚀 Tạo Project", type="primary", use_container_width=True)
                if submitted:
                    if not na_title.strip():
                        st.error("❌ Tên tiểu thuyết không được để trống!")
                    else:
                        slug = na_slugify(na_title)
                        if os.path.exists(na_project_dir(slug)):
                            slug = slug + f"-{int(time.time()) % 10000}"
                        cfg_new = {
                            'title': na_title.strip(),
                            'slug': slug,
                            'source_lang': na_src_lang,
                            'target_lang': na_tgt_lang,
                            'style_guide': na_style.strip(),
                            'confidence_threshold': na_threshold / 100,
                            'chunk_size': na_chunk_sz,
                            'created_at': now_gmt7().isoformat(),
                            'chapters_count': 0,
                        }
                        na_save_config(slug, cfg_new)
                        # Init empty memory
                        na_save_memory(slug, {'characters':[], 'glossary':[], 'timeline':[], 'relationships':[]})
                        st.session_state['na_project'] = slug
                        log_action("Novel Agent", f"Tạo project: {na_title}")
                        st.success(f"✅ Đã tạo project **{na_title}**!")
                        st.rerun()

        # Show active project banner
        if st.session_state.get('na_project') in all_projects:
            ap = st.session_state['na_project']
            apcfg = na_load_config(ap)
            st.success(f"🎯 Project đang chọn: **{apcfg.get('title', ap)}** ({apcfg.get('source_lang')} → {apcfg.get('target_lang')})")

    # ── Guard: require project selected for other tabs ──
    def _na_require_project():
        p = st.session_state.get('na_project')
        if p not in na_list_projects():
            st.warning("⚠️ Chọn hoặc tạo project ở tab **📁 Projects** trước.")
            return None
        return p

    # ===================== SUB-TAB 1: IMPORT CHAPTER =====================
    with na_sub[1]:
        st.markdown("### 📥 Import Chapter")
        na_proj = _na_require_project()
        if na_proj:
            na_cfg = na_load_config(na_proj)

            existing_chs = na_list_chapters(na_proj)
            # Auto chapter ID
            next_ch_num = len(existing_chs) + 1
            default_ch_id = f"ch_{next_ch_num:03d}"

            col_imp1, col_imp2 = st.columns([1, 2])
            with col_imp1:
                ch_id_input = st.text_input("Chapter ID", value=default_ch_id,
                                            help="VD: ch_001, ch_012, prologue")
                ch_id_input = ch_id_input.strip().replace(' ', '_')
            with col_imp2:
                ch_title_input = st.text_input("Tiêu đề chương (tùy chọn)",
                                               placeholder="VD: Chương 1 — Khởi Đầu")

            import_src = st.radio("Nguồn văn bản:",
                                  ["📋 Paste", "📄 Upload file (.txt / .md)"],
                                  horizontal=True, key="na_imp_src")

            raw_text = ""
            if import_src.startswith("📋"):
                raw_text = st.text_area("Dán nội dung chương:", height=300,
                                        key="na_imp_paste",
                                        placeholder="Paste văn bản gốc vào đây...")
            else:
                upl = st.file_uploader("Chọn file", type=["txt", "md"],
                                       key="na_imp_file")
                if upl:
                    import re as _re
                    raw_text = upl.read().decode('utf-8', errors='replace')
                    # Strip .md frontmatter if present
                    raw_text = _re.sub(r'^---[\s\S]*?---\s*', '', raw_text, count=1).strip()
                    st.success(f"✅ Đọc được {len(raw_text)} ký tự từ `{upl.name}`")

            if raw_text:
                # Preview stats
                paras = [p.strip() for p in raw_text.split('\n') if p.strip()]
                chunk_sz = na_cfg.get('chunk_size', 20)
                n_chunks = (len(paras) + chunk_sz - 1) // chunk_sz
                st.info(f"📊 {len(paras)} đoạn văn → {n_chunks} chunks (chunk_size={chunk_sz})")

                if st.button("💾 Lưu Chapter & Tạo Chunks", type="primary", key="na_imp_save"):
                    if not ch_id_input:
                        st.error("❌ Chapter ID không được để trống!")
                    else:
                        ch_dir = na_chapter_dir(na_proj, ch_id_input)
                        chunks_dir = os.path.join(ch_dir, 'chunks')
                        os.makedirs(chunks_dir, exist_ok=True)

                        # Save source as .md with frontmatter
                        title_str = ch_title_input.strip() or f"{na_cfg.get('title', na_proj)} — {ch_id_input}"
                        source_md = f"---\ntitle: {title_str}\n---\n\n{raw_text}"
                        with open(os.path.join(ch_dir, 'source.md'), 'w', encoding='utf-8') as _f:
                            _f.write(source_md)

                        # Save chunks
                        for ci in range(n_chunks):
                            s, e = ci * chunk_sz, (ci + 1) * chunk_sz
                            chunk_text = '\n'.join(paras[s:e])
                            with open(os.path.join(chunks_dir, f'chunk_{ci+1:03d}.md'), 'w', encoding='utf-8') as _f:
                                _f.write(f"---\ntitle: {title_str} — Chunk {ci+1}/{n_chunks}\n---\n\n{chunk_text}")

                        # Save chapter metadata
                        na_save_json(os.path.join(ch_dir, 'meta.json'), {
                            'chapter_id': ch_id_input,
                            'title': title_str,
                            'imported_at': now_gmt7().isoformat(),
                            'n_paragraphs': len(paras),
                            'n_chunks': n_chunks,
                            'chunk_size': chunk_sz,
                        })

                        log_action("Novel Agent", f"Import chapter: {ch_id_input} | {len(paras)} đoạn | {n_chunks} chunks")
                        st.success(f"✅ Đã lưu **{ch_id_input}** — {len(paras)} đoạn / {n_chunks} chunks")
                        st.rerun()

            # Show existing chapters
            if existing_chs:
                st.divider()
                st.markdown("**Chapters đã import:**")
                for ch in existing_chs:
                    meta = na_load_json(os.path.join(na_chapter_dir(na_proj, ch), 'meta.json'), {})
                    has_analysis = os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'analysis.json'))
                    has_trans = os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'translation.md'))
                    badges = (" ✅ Phân tích" if has_analysis else "") + (" 🌐 Dịch xong" if has_trans else "")
                    st.markdown(f"- **{ch}** — {meta.get('title', ch)} | {meta.get('n_paragraphs',0)} đoạn | {meta.get('n_chunks',0)} chunks{badges}")

    # ===================== SUB-TAB 2: ANALYZE =====================
    with na_sub[2]:
        st.markdown("### 🔬 Context Analyzer")
        st.caption("AI đọc toàn bộ chương để phát hiện nhân vật mới, thuật ngữ, xưng hô, tham chiếu mơ hồ — TRƯỚC khi dịch.")
        na_proj = _na_require_project()
        if na_proj:
            na_cfg = na_load_config(na_proj)
            chapters_av = na_list_chapters(na_proj)
            if not chapters_av:
                st.info("Chưa có chapter nào. Import chapter trước ở tab **📥 Import Chapter**.")
            else:
                sel_ch_a = st.selectbox("Chọn chapter:", chapters_av, key="na_ana_ch")
                ch_dir_a = na_chapter_dir(na_proj, sel_ch_a)
                source_path_a = os.path.join(ch_dir_a, 'source.md')
                analysis_path_a = os.path.join(ch_dir_a, 'analysis.json')

                if not os.path.exists(source_path_a):
                    st.error("❌ Không tìm thấy source.md. Hãy import lại chapter này.")
                else:
                    # Load source (strip frontmatter)
                    with open(source_path_a, 'r', encoding='utf-8') as _f:
                        src_full = _f.read()
                    import re as _re
                    src_body = _re.sub(r'^---[\s\S]*?---\s*', '', src_full, count=1).strip()

                    existing_analysis = na_load_json(analysis_path_a, None)
                    if existing_analysis:
                        st.success("✅ Đã có kết quả phân tích. Có thể chạy lại để cập nhật.")

                    threshold = na_cfg.get('confidence_threshold', 0.8)
                    st.info(f"Ngưỡng tự động dịch: **{int(threshold*100)}%** — AI sẽ đặt câu hỏi khi confidence < {int(threshold*100)}%")

                    if st.button("🔬 Chạy Context Analysis", type="primary", key="na_run_analysis"):
                        memory = na_load_memory(na_proj)
                        existing_chars = [c.get('name','') for c in memory.get('characters', [])]
                        existing_terms = [g.get('original','') for g in memory.get('glossary', [])]

                        sys_ana = (
                            f"You are an expert literary analyst and translation consultant for {na_cfg.get('source_lang','Chinese')} to {na_cfg.get('target_lang','Vietnamese')} novel translation.\n"
                            "Your ONLY task is to ANALYZE, not translate. Read the entire chapter and detect:\n"
                            "1. New characters (not in existing memory)\n"
                            "2. New locations\n"
                            "3. New organizations/factions\n"
                            "4. New skills/techniques/items\n"
                            "5. New terminology\n"
                            "6. Honorifics and pronouns with ambiguity\n"
                            "7. Relationship changes\n"
                            "8. Important timeline events\n"
                            "9. Ambiguous references that need user clarification (with your confidence 0-100%)\n"
                            "Output ONLY valid JSON in this exact schema:\n"
                            "{\"chapter_summary\": \"...\", \"new_characters\": [{\"name\": \"\", \"gender\": \"\", \"role\": \"\", \"description\": \"\"}], "
                            "\"new_locations\": [{\"name\": \"\", \"description\": \"\"}], "
                            "\"new_terms\": [{\"original\": \"\", \"suggested\": \"\", \"category\": \"skill|location|item|faction|other\", \"confidence\": 0.0}], "
                            "\"ambiguous\": [{\"id\": \"amb_001\", \"original\": \"\", \"suggested\": \"\", \"confidence\": 0.0, "
                            "\"question\": \"\", \"options\": [], \"category\": \"honorific|pronoun|name|term|relationship\"}]}"
                        )
                        prompt_ana = (
                            f"=== KNOWN CHARACTERS ===\n{', '.join(existing_chars) or 'None'}\n\n"
                            f"=== KNOWN GLOSSARY ===\n{', '.join(existing_terms) or 'None'}\n\n"
                            f"=== CHAPTER TEXT ===\n{src_body[:12000]}"
                        )

                        with st.spinner("🔬 AI đang phân tích chương... (30-60 giây)"):
                            raw_ana = generate_with_retry(
                                "gemini-2.5-flash", prompt_ana, sys_ana,
                                None, retries=3, temp=0.2
                            )

                        if raw_ana:
                            # Parse JSON (may have markdown fences)
                            import re as _re
                            json_match = _re.search(r'```(?:json)?\s*([\s\S]*?)```', raw_ana)
                            json_str = json_match.group(1) if json_match else raw_ana
                            # Remove trailing commas before } or ]
                            json_str = _re.sub(r',\s*([}\]])', r'\1', json_str.strip())
                            try:
                                analysis_data = json.loads(json_str)
                                analysis_data['chapter_id'] = sel_ch_a
                                analysis_data['analyzed_at'] = now_gmt7().isoformat()
                                na_save_json(analysis_path_a, analysis_data)
                                log_action("Novel Agent", f"Analysis: {sel_ch_a} | {len(analysis_data.get('ambiguous',[]))} ambiguous")
                                st.success("✅ Phân tích hoàn tất! Xem kết quả bên dưới.")
                                st.rerun()
                            except json.JSONDecodeError as je:
                                st.error(f"❌ AI không trả về JSON hợp lệ: {je}")
                                with st.expander("Xem raw output"):
                                    st.code(raw_ana)
                        else:
                            st.error("❌ AI không trả về kết quả. Thử lại.")

                    # Display existing analysis
                    if existing_analysis:
                        st.divider()
                        st.markdown("#### 📋 Kết quả phân tích")

                        with st.expander(f"📝 Tóm tắt chương", expanded=True):
                            st.markdown(existing_analysis.get('chapter_summary', '_Không có_'))

                        new_chars = existing_analysis.get('new_characters', [])
                        if new_chars:
                            with st.expander(f"🧑 Nhân vật mới ({len(new_chars)})"):
                                for c in new_chars:
                                    st.markdown(f"- **{c.get('name','')}** ({c.get('gender','?')}) — {c.get('role','')} | {c.get('description','')}")

                        new_locs = existing_analysis.get('new_locations', [])
                        if new_locs:
                            with st.expander(f"📍 Địa điểm mới ({len(new_locs)})"):
                                for loc in new_locs:
                                    st.markdown(f"- **{loc.get('name','')}** — {loc.get('description','')}")

                        new_terms = existing_analysis.get('new_terms', [])
                        if new_terms:
                            with st.expander(f"📖 Thuật ngữ mới ({len(new_terms)})"):
                                for t in new_terms:
                                    conf = int(t.get('confidence', 0) * 100)
                                    color = '#51cf66' if conf >= 80 else ('#f0a500' if conf >= 60 else '#ff6b6b')
                                    st.markdown(
                                        f"- `{t.get('original','')}` → **{t.get('suggested','')}** "
                                        f"[{t.get('category','')}] "
                                        f"<span style='color:{color}'>{conf}%</span>",
                                        unsafe_allow_html=True
                                    )

                        ambiguous = existing_analysis.get('ambiguous', [])
                        threshold_pct = int(na_cfg.get('confidence_threshold', 0.8) * 100)
                        need_qa = [a for a in ambiguous if int(a.get('confidence', 1.0) * 100) < threshold_pct]
                        if need_qa:
                            with st.expander(f"❓ Cần làm rõ ({len(need_qa)}) — confidence < {threshold_pct}%", expanded=True):
                                for a in need_qa:
                                    conf = int(a.get('confidence', 0) * 100)
                                    st.markdown(
                                        f"<span style='color:#f0a500'>⚠️</span> **{a.get('original','')}** "
                                        f"→ *{a.get('suggested','')}* ({conf}%) — {a.get('category','')}",
                                        unsafe_allow_html=True
                                    )
                        elif ambiguous:
                            st.success(f"✅ Tất cả {len(ambiguous)} thuật ngữ có confidence ≥ {threshold_pct}% — không cần hỏi.")

    # ===================== SUB-TAB 3: CLARIFICATIONS =====================
    with na_sub[3]:
        st.markdown("### ❓ Clarification Center")
        st.caption("Trả lời các câu hỏi của AI trước khi dịch. Chỉ hiển thị các mục có confidence thấp.")
        na_proj = _na_require_project()
        if na_proj:
            na_cfg = na_load_config(na_proj)
            chapters_av = na_list_chapters(na_proj)
            if not chapters_av:
                st.info("Chưa có chapter nào.")
            else:
                sel_ch_q = st.selectbox("Chọn chapter:", chapters_av, key="na_q_ch")
                analysis_path_q = os.path.join(na_chapter_dir(na_proj, sel_ch_q), 'analysis.json')
                clar_path_q = os.path.join(na_chapter_dir(na_proj, sel_ch_q), 'clarifications.json')

                if not os.path.exists(analysis_path_q):
                    st.warning("⚠️ Chưa có kết quả phân tích. Chạy **🔬 Analyze** trước.")
                else:
                    analysis_q = na_load_json(analysis_path_q, {})
                    clar_q = na_load_json(clar_path_q, {'chapter_id': sel_ch_q, 'questions': [], 'answers': {}})

                    threshold_q = na_cfg.get('confidence_threshold', 0.8)
                    ambiguous_q = analysis_q.get('ambiguous', [])
                    # Phase 2: Auto-learning — skip terms already approved in project glossary
                    memory_q = na_load_memory(na_proj)
                    approved_originals = {
                        g['original'] for g in memory_q.get('glossary', [])
                        if g.get('approved', False)
                    }
                    need_qa = [
                        a for a in ambiguous_q
                        if a.get('confidence', 1.0) < threshold_q
                        and a.get('original', '') not in approved_originals
                    ]
                    if approved_originals:
                        skipped = [
                            a for a in ambiguous_q
                            if a.get('original', '') in approved_originals
                        ]
                        if skipped:
                            _skip_names = ', '.join(
                                '`' + a.get('original', '') + '`' for a in skipped[:5]
                            )
                            _ellipsis = '...' if len(skipped) > 5 else ''
                            st.info(
                                f'🧠 Bỏ qua {len(skipped)} thuật ngữ '
                                f'đã được học (approved trong Glossary): '
                                f'{_skip_names}{_ellipsis}'
                            )

                    # Sync questions list
                    existing_q_ids = {q['id'] for q in clar_q.get('questions', [])}
                    for a in need_qa:
                        if a.get('id') not in existing_q_ids:
                            clar_q.setdefault('questions', []).append(a)

                    existing_answers = clar_q.get('answers', {})
                    pending = [q for q in clar_q.get('questions', []) if q['id'] not in existing_answers]
                    done = [q for q in clar_q.get('questions', []) if q['id'] in existing_answers]

                    if not clar_q.get('questions'):
                        st.success("✅ Không có câu hỏi nào — tất cả thuật ngữ đều có confidence cao. Có thể dịch ngay!")
                    else:
                        # Progress
                        n_total = len(clar_q.get('questions', []))
                        n_done = len(done)
                        st.progress(n_done / n_total if n_total else 1,
                                    f"Đã trả lời: {n_done}/{n_total} câu")

                        if pending:
                            st.markdown(f"**{len(pending)} câu hỏi chờ trả lời:**")
                            new_answers = dict(existing_answers)

                            for q in pending:
                                qid = q['id']
                                conf_pct = int(q.get('confidence', 0) * 100)
                                color = '#d08400' if conf_pct >= 60 else '#c62828'
                                cat_icon = {'honorific': '🎭', 'pronoun': '👤', 'name': '🏷️',
                                            'term': '📖', 'relationship': '🤝'}.get(q.get('category', ''), '❓')

                                with st.container():
                                    st.markdown(
                                        f"<div style='border:1px solid {color};border-radius:10px;"
                                        f"padding:1rem;margin-bottom:0.8rem;background:#EFECE6'>"
                                        f"<div style='display:flex;justify-content:space-between;align-items:center'>"
                                        f"<span style='font-size:0.9rem;color:#5c564d'>{cat_icon} {q.get('category','').upper()}</span>"
                                        f"<span style='color:{color};font-weight:600'>{conf_pct}% confidence</span></div>"
                                        f"<p style='margin:0.5rem 0;font-size:1.1rem;color:#2D2A26'>原文: "
                                        f"<code style='background:#D1CFC7;padding:2px 6px;border-radius:4px'>{q.get('original','')}</code></p>"
                                        f"<p style='margin:0;color:#0D9488'>💡 Gợi ý: <b>{q.get('suggested','')}</b></p>"
                                        f"<p style='margin:0.3rem 0 0;color:#5c564d;font-size:0.88rem'>{q.get('question','')}</p>"
                                        f"</div>",
                                        unsafe_allow_html=True
                                    )
                                    opts = q.get('options', []) + ["✏️ Nhập tay"]
                                    chosen = st.radio(
                                        "Chọn cách dịch:", opts,
                                        key=f"na_q_{qid}_radio",
                                        horizontal=True,
                                        label_visibility="collapsed"
                                    )
                                    custom_val = ""
                                    if chosen == "✏️ Nhập tay":
                                        custom_val = st.text_input(
                                            "Nhập bản dịch:", key=f"na_q_{qid}_custom",
                                            placeholder=f"Dịch cho '{q.get('original','')}'..."
                                        )
                                    new_answers[qid] = {
                                        'choice': chosen if chosen != "✏️ Nhập tay" else 'Custom',
                                        'custom': custom_val or None
                                    }

                            if st.button("✅ Lưu tất cả câu trả lời", type="primary", key="na_q_submit"):
                                clar_q['answers'] = new_answers
                                clar_q['answered_at'] = now_gmt7().isoformat()
                                na_save_json(clar_path_q, clar_q)
                                log_action("Novel Agent", f"Clarifications: {sel_ch_q} | {len(new_answers)} câu")
                                st.success("✅ Đã lưu câu trả lời!")
                                st.rerun()

                        if done:
                            with st.expander(f"✅ Đã trả lời ({len(done)} câu)"):
                                for q in done:
                                    ans = existing_answers[q['id']]
                                    chosen_disp = ans.get('custom') or ans.get('choice', '')
                                    st.markdown(f"- `{q.get('original','')}` → **{chosen_disp}**")

    # ===================== SUB-TAB 4: TRANSLATE =====================
    with na_sub[4]:
        st.markdown("### 🌐 Translation Engine")
        na_proj = _na_require_project()
        if na_proj:
            na_cfg = na_load_config(na_proj)
            chapters_av = na_list_chapters(na_proj)
            if not chapters_av:
                st.info("Chưa có chapter nào.")
            else:
                sel_ch_t = st.selectbox("Chọn chapter:", chapters_av, key="na_t_ch")
                ch_dir_t = na_chapter_dir(na_proj, sel_ch_t)
                chunks_dir_t = os.path.join(ch_dir_t, 'chunks')
                clar_path_t = os.path.join(ch_dir_t, 'clarifications.json')
                analysis_path_t = os.path.join(ch_dir_t, 'analysis.json')
                trans_path_t = os.path.join(ch_dir_t, 'translation.md')
                review_path_t = os.path.join(ch_dir_t, 'review_report.json')

                # Pre-flight checks
                has_chunks = os.path.exists(chunks_dir_t) and bool(os.listdir(chunks_dir_t))
                has_analysis = os.path.exists(analysis_path_t)
                has_clar = os.path.exists(clar_path_t)
                has_trans = os.path.exists(trans_path_t)

                c1pf, c2pf, c3pf = st.columns(3)
                c1pf.metric("Chunks", "✅" if has_chunks else "❌", "Import OK" if has_chunks else "Cần import")
                c2pf.metric("Analysis", "✅" if has_analysis else "⚠️", "OK" if has_analysis else "Nên chạy")
                c3pf.metric("Clarifications", "✅" if has_clar else "⚠️", "OK" if has_clar else "Tùy chọn")

                if not has_chunks:
                    st.error("❌ Chưa có chunks. Hãy import chapter trước.")
                else:
                    # Load chunks
                    chunk_files = sorted(os.listdir(chunks_dir_t))
                    n_chunks_t = len(chunk_files)

                    target_model_t = st.selectbox(
                        "AI Model (dịch):",
                        ["gemini-2.5-flash", "gemini-2.5-pro", "gemini-2.0-flash"],
                        key="na_t_model"
                    )

                    if not has_analysis:
                        st.warning("⚠️ Chưa phân tích chương. Context sẽ thiếu chi tiết — nên chạy Analyze trước.")

                    col_t1, col_t2, col_t3 = st.columns([1, 1, 1])
                    with col_t1:
                        run_translate = st.button(
                            f"🌐 Dịch {n_chunks_t} chunks", type="primary",
                            key="na_run_trans", use_container_width=True
                        )
                    with col_t2:
                        if has_trans:
                            st.download_button(
                                "⬇️ Tải bản dịch (.md)",
                                open(trans_path_t, 'r', encoding='utf-8').read(),
                                file_name=f"{sel_ch_t}_translation.md",
                                mime="text/markdown",
                                key="na_dl_trans",
                                use_container_width=True
                            )
                    with col_t3:
                        # Phase 2: Batch translate all pending chapters
                        pending_chapters = [
                            ch for ch in chapters_av
                            if not os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'translation.md'))
                            and os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'chunks'))
                            and bool(os.listdir(os.path.join(na_chapter_dir(na_proj, ch), 'chunks')))
                        ]
                        run_batch = st.button(
                            f"⚡ Batch: {len(pending_chapters)} chương chờ",
                            key="na_run_batch", use_container_width=True,
                            disabled=len(pending_chapters) == 0,
                            help="Dịch tuần tự tất cả các chương chưa có bản dịch"
                        )

                    if run_batch and pending_chapters:
                        log_action("Novel Agent", f"Batch translate: {len(pending_chapters)} chapters")
                        memory_batch = na_load_memory(na_proj)
                        batch_status = st.status(
                            f"⚡ Batch dịch {len(pending_chapters)} chương...", expanded=True
                        )
                        batch_bar = st.progress(0)
                        sys_trans_batch = (
                            f"You are a professional literary translator specializing in "
                            f"{na_cfg.get('source_lang','Chinese')} to {na_cfg.get('target_lang','Vietnamese')} novel translation.\n"
                            "RULES:\n"
                            "1. Output ONLY the translation. No notes, no commentary, no extra text.\n"
                            "2. Preserve paragraph structure exactly — same number of paragraphs as input.\n"
                            "3. Follow all style guide rules, character names, and glossary entries provided.\n"
                            "4. Apply all user clarification decisions exactly as specified.\n"
                            "5. DO NOT translate the 'PREVIOUS CONTEXT' section."
                        )
                        for b_idx, b_ch in enumerate(pending_chapters):
                            batch_status.write(f"📖 [{b_idx+1}/{len(pending_chapters)}] Đang dịch `{b_ch}`...")
                            b_ch_dir = na_chapter_dir(na_proj, b_ch)
                            b_chunks_dir = os.path.join(b_ch_dir, 'chunks')
                            b_chunk_files = sorted([
                                f for f in os.listdir(b_chunks_dir)
                                if f.endswith('.md') and '_trans' not in f
                            ])
                            b_analysis = na_load_json(os.path.join(b_ch_dir, 'analysis.json'), {})
                            b_clar = na_load_json(os.path.join(b_ch_dir, 'clarifications.json'),
                                                   {'answers': {}, 'questions': []})
                            b_prev_summary = na_get_prev_chapter_summary(na_proj, b_ch)
                            b_translated = []
                            for ci, cf in enumerate(b_chunk_files):
                                with open(os.path.join(b_chunks_dir, cf), 'r', encoding='utf-8') as _f:
                                    _raw = _f.read()
                                import re as _re
                                _body = _re.sub(r'^---[\s\S]*?---\s*', '', _raw, count=1).strip()
                                _tail = ''
                                if b_translated:
                                    _tail_lines = [l for l in b_translated[-1].split('\n') if l.strip()]
                                    _tail = '\n'.join(_tail_lines[-2:])
                                _prompt = na_build_translation_prompt(
                                    na_cfg, memory_batch, b_prev_summary,
                                    b_analysis, b_clar, _tail, _body
                                )
                                _res = generate_with_retry(
                                    target_model_t, _prompt, sys_trans_batch,
                                    batch_status, retries=5, temp=0.3
                                )
                                _trans_path = os.path.join(b_chunks_dir, cf.replace('.md', '_trans.md'))
                                with open(_trans_path, 'w', encoding='utf-8') as _f:
                                    _f.write(f"---\ntitle: {b_ch} chunk {ci+1}\n---\n\n{_res}")
                                b_translated.append(_res)
                            # Merge & save
                            b_merged = '\n\n'.join(b_translated)
                            na_save_chapter_as_md(na_proj, b_ch, b_merged)
                            batch_status.write(f"   ✅ `{b_ch}` xong ({len(b_chunk_files)} chunks)")
                            batch_bar.progress((b_idx + 1) / len(pending_chapters))
                        batch_status.update(label="✅ Batch hoàn tất!", state="complete")
                        st.balloons()
                        st.rerun()

                    if run_translate:
                        log_action("Novel Agent", f"Translate: {sel_ch_t} | {n_chunks_t} chunks | {target_model_t}")
                        memory_t = na_load_memory(na_proj)
                        analysis_t = na_load_json(analysis_path_t, {}) if has_analysis else {}
                        clar_t = na_load_json(clar_path_t, {'answers': {}, 'questions': []}) if has_clar else {'answers': {}, 'questions': []}
                        prev_summary_t = na_get_prev_chapter_summary(na_proj, sel_ch_t)

                        sys_trans = (
                            f"You are a professional literary translator specializing in {na_cfg.get('source_lang','Chinese')} to {na_cfg.get('target_lang','Vietnamese')} novel translation.\n"
                            "RULES:\n"
                            "1. Output ONLY the translation. No notes, no commentary, no extra text.\n"
                            "2. Preserve paragraph structure exactly — same number of paragraphs as input.\n"
                            "3. Follow all style guide rules, character names, and glossary entries provided.\n"
                            "4. Apply all user clarification decisions exactly as specified.\n"
                            "5. DO NOT translate the 'PREVIOUS CONTEXT' section."
                        )

                        translated_chunks = []
                        bar_t = st.progress(0, "Chuẩn bị dịch...")
                        status_t = st.status(f"🌐 Đang dịch {n_chunks_t} chunks...", expanded=True)

                        for ci, cf in enumerate(chunk_files):
                            chunk_path = os.path.join(chunks_dir_t, cf)
                            with open(chunk_path, 'r', encoding='utf-8') as _f:
                                chunk_raw = _f.read()
                            # Strip frontmatter
                            import re as _re
                            chunk_body = _re.sub(r'^---[\s\S]*?---\s*', '', chunk_raw, count=1).strip()

                            # Previous chunk tail (last 2 paragraphs)
                            prev_tail = ""
                            if translated_chunks:
                                tail_lines = [l for l in translated_chunks[-1].split('\n') if l.strip()]
                                prev_tail = '\n'.join(tail_lines[-2:])

                            prompt_t = na_build_translation_prompt(
                                na_cfg, memory_t, prev_summary_t,
                                analysis_t, clar_t, prev_tail, chunk_body
                            )

                            status_t.write(f"📄 Đang dịch chunk {ci+1}/{n_chunks_t}...")
                            result_t = generate_with_retry(
                                target_model_t, prompt_t, sys_trans,
                                status_t, retries=5, temp=0.3
                            )

                            # Save individual chunk translation
                            chunk_trans_path = os.path.join(chunks_dir_t, cf.replace('.md', '_trans.md'))
                            trans_title = f"{sel_ch_t} — Chunk {ci+1}/{n_chunks_t} [TRANSLATED]"
                            with open(chunk_trans_path, 'w', encoding='utf-8') as _f:
                                _f.write(f"---\ntitle: {trans_title}\n---\n\n{result_t}")

                            translated_chunks.append(result_t)
                            bar_t.progress((ci + 1) / n_chunks_t,
                                           f"✅ {ci+1}/{n_chunks_t} chunks")

                        # Merge all chunks
                        merged_trans = '\n\n'.join(translated_chunks)
                        out_md_path = na_save_chapter_as_md(na_proj, sel_ch_t, merged_trans)

                        status_t.update(label=f"✅ Dịch xong! Đang chạy Consistency Review...", state="running")

                        # ── Consistency Review agent ──
                        sys_rev = (
                            f"You are a strict literary editor reviewing a {na_cfg.get('target_lang','Vietnamese')} translation.\n"
                            "Review the translation for:\n"
                            "1. Terminology consistency (same terms translated the same way)\n"
                            "2. Character name consistency\n"
                            "3. Honorific consistency\n"
                            "4. Pronoun consistency\n"
                            "5. Missing or repeated sentences\n"
                            "6. Natural flow and readability\n"
                            "7. Any mistranslations based on the glossary provided\n"
                            "Output a structured report in Markdown with section headers. List each issue with line reference and suggested fix."
                        )
                        mem_str_rev = na_format_memory_for_prompt(memory_t)
                        prompt_rev = (
                            f"=== NOVEL MEMORY ===\n{mem_str_rev}\n\n"
                            f"=== TRANSLATION TO REVIEW ===\n{merged_trans[:8000]}"
                        )
                        review_result = generate_with_retry(
                            "gemini-2.5-flash", prompt_rev, sys_rev,
                            status_t, retries=3, temp=0.1
                        )
                        if review_result:
                            na_save_json(review_path_t, {
                                'chapter_id': sel_ch_t,
                                'reviewed_at': now_gmt7().isoformat(),
                                'report': review_result
                            })

                        status_t.update(label=f"✅ Hoàn tất!", state="complete")
                        st.session_state[f'na_trans_{sel_ch_t}'] = merged_trans
                        st.session_state[f'na_review_{sel_ch_t}'] = review_result
                        log_action("Novel Agent", f"Trans done: {sel_ch_t}")
                        st.balloons()

                    # ── Display results ──
                    if has_trans or st.session_state.get(f'na_trans_{sel_ch_t}'):
                        st.divider()
                        trans_content = st.session_state.get(f'na_trans_{sel_ch_t}')
                        if not trans_content and has_trans:
                            with open(trans_path_t, 'r', encoding='utf-8') as _f:
                                trans_content = _f.read()

                        with st.expander("📄 Xem bản dịch", expanded=False):
                            st.text_area("Bản dịch:", trans_content,
                                         height=400, key="na_trans_view")

                        # Review report
                        review_data = None
                        if os.path.exists(review_path_t):
                            review_data = na_load_json(review_path_t, {})
                        if review_data or st.session_state.get(f'na_review_{sel_ch_t}'):
                            report_text = review_data.get('report', '') if review_data else st.session_state.get(f'na_review_{sel_ch_t}', '')
                            with st.expander("🔍 Báo cáo Consistency Review", expanded=True):
                                st.markdown(report_text)

                        # ── Accept & Update Memory ──
                        st.divider()
                        st.markdown("#### 💾 Cập nhật Memory")
                        st.caption("Sau khi review và chỉnh sửa xong, bấm để AI trích xuất thuật ngữ mới và cập nhật bộ nhớ dài hạn của novel.")

                        if st.button("🧠 Accept & Update Memory", type="primary", key="na_update_mem",
                                     help="AI trích xuất thuật ngữ mới và tự động đánh dấu approved để không hỏi lại sau"):
                            memory_upd = na_load_memory(na_proj)
                            analysis_upd = na_load_json(analysis_path_t, {})

                            sys_mem = (
                                "You are a memory manager for a novel translation project.\n"
                                "Extract from the analysis and translation:\n"
                                "1. All new characters with their details\n"
                                "2. All new glossary terms with suggested translations\n"
                                "3. Timeline events (chapter_id, event description)\n"
                                "Output ONLY valid JSON:\n"
                                "{\"new_characters\": [{\"name\":\"\",\"gender\":\"\",\"aliases\":[],\"speech_style\":\"\",\"honorifics\":\"\",\"notes\":\"\"}],"
                                "\"new_glossary\": [{\"original\":\"\",\"translation\":\"\",\"category\":\"\",\"confidence\":0.9}],"
                                "\"new_timeline\": [{\"chapter_id\":\"\",\"event\":\"\"}]}"
                            )
                            prompt_mem = (
                                f"=== CHAPTER ID ===\n{sel_ch_t}\n\n"
                                f"=== ANALYSIS ===\n{json.dumps(analysis_upd, ensure_ascii=False)[:4000]}\n\n"
                                f"=== TRANSLATION SAMPLE ===\n{(trans_content or '')[:3000]}"
                            )

                            with st.spinner("🧠 AI đang cập nhật memory..."):
                                mem_raw = generate_with_retry(
                                    "gemini-2.5-flash", prompt_mem, sys_mem,
                                    None, retries=3, temp=0.2
                                )

                            if mem_raw:
                                import re as _re
                                jm = _re.search(r'```(?:json)?\s*([\s\S]*?)```', mem_raw)
                                js = (jm.group(1) if jm else mem_raw).strip()
                                js = _re.sub(r',\s*([}\]])', r'\1', js)
                                try:
                                    new_mem_data = json.loads(js)

                                    # Merge characters
                                    existing_char_names = {c['name'] for c in memory_upd['characters']}
                                    for nc in new_mem_data.get('new_characters', []):
                                        if nc.get('name') and nc['name'] not in existing_char_names:
                                            memory_upd['characters'].append(nc)

                                    # Merge glossary
                                    existing_gl_orig = {g['original'] for g in memory_upd['glossary']}
                                    for ng in new_mem_data.get('new_glossary', []):
                                        if ng.get('original') and ng['original'] not in existing_gl_orig:
                                            ng['chapter_first_seen'] = sel_ch_t
                                            ng['approved'] = False
                                            memory_upd['glossary'].append(ng)

                                    # Merge timeline
                                    for ev in new_mem_data.get('new_timeline', []):
                                        memory_upd['timeline'].append(ev)

                                    # Phase 2: Auto-approve new glossary terms for confidence learning
                                    for g in memory_upd['glossary']:
                                        if g.get('chapter_first_seen') == sel_ch_t and not g.get('approved'):
                                            g['approved'] = True  # mark learned

                                    na_save_memory(na_proj, memory_upd)

                                    # Generate and save chapter summary
                                    summary_text = analysis_upd.get('chapter_summary', '')
                                    na_save_json(os.path.join(ch_dir_t, 'summary.json'), {
                                        'chapter_id': sel_ch_t,
                                        'summary': summary_text,
                                        'generated_at': now_gmt7().isoformat()
                                    })

                                    n_new_c = len(new_mem_data.get('new_characters', []))
                                    n_new_g = len(new_mem_data.get('new_glossary', []))
                                    log_action("Novel Agent", f"Memory update: {sel_ch_t} | +{n_new_c} chars | +{n_new_g} terms")
                                    st.success(f"✅ Memory cập nhật: +{n_new_c} nhân vật, +{n_new_g} thuật ngữ")
                                    st.rerun()
                                except json.JSONDecodeError as je:
                                    st.error(f"❌ Lỗi parse JSON memory: {je}")
                                    with st.expander("Raw output"):
                                        st.code(mem_raw)

    # ===================== SUB-TAB 5: MEMORY =====================
    with na_sub[5]:
        st.markdown("### 🧠 Novel Memory")
        na_proj = _na_require_project()
        if na_proj:
            na_cfg = na_load_config(na_proj)
            memory_v = na_load_memory(na_proj)

            mem_tabs = st.tabs(["🧑 Nhân vật", "📖 Glossary", "📅 Timeline", "🕸️ Quan hệ", "📊 Arc Summary", "⚙️ Cấu hình Project"])

            with mem_tabs[0]:
                chars = memory_v.get('characters', [])
                if not chars:
                    st.info("Chưa có nhân vật nào trong memory. Dịch một chapter và bấm 'Accept & Update Memory'.")
                else:
                    st.caption(f"{len(chars)} nhân vật")
                    import pandas as pd
                    char_df = pd.DataFrame([{
                        'Tên': c.get('name',''),
                        'Giới tính': c.get('gender',''),
                        'Bí danh': ', '.join(c.get('aliases', [])),
                        'Xưng hô': c.get('honorifics',''),
                        'Phong cách': c.get('speech_style',''),
                        'Ghi chú': c.get('notes','')
                    } for c in chars])
                    edited_chars = st.data_editor(char_df, use_container_width=True,
                                                   num_rows="dynamic", key="na_mem_chars")
                    if st.button("💾 Lưu Nhân vật", key="na_save_chars"):
                        new_chars = []
                        for _, row in edited_chars.iterrows():
                            new_chars.append({
                                'name': row['Tên'], 'gender': row['Giới tính'],
                                'aliases': [a.strip() for a in str(row['Bí danh']).split(',') if a.strip()],
                                'honorifics': row['Xưng hô'],
                                'speech_style': row['Phong cách'], 'notes': row['Ghi chú']
                            })
                        memory_v['characters'] = new_chars
                        na_save_memory(na_proj, memory_v)
                        st.success("✅ Đã lưu!")

            with mem_tabs[1]:
                glossary_v = memory_v.get('glossary', [])
                if not glossary_v:
                    st.info("Chưa có thuật ngữ nào. Dịch chapter và bấm 'Accept & Update Memory'.")
                else:
                    st.caption(f"{len(glossary_v)} thuật ngữ")
                    import pandas as pd
                    gl_df = pd.DataFrame([{
                        'Gốc': g.get('original',''),
                        'Dịch': g.get('translation',''),
                        'Loại': g.get('category',''),
                        'Confidence': f"{int(g.get('confidence',0)*100)}%",
                        'Approved': g.get('approved', False),
                        'Lần đầu thấy': g.get('chapter_first_seen',''),
                        'Ghi chú': g.get('notes','')
                    } for g in glossary_v])
                    edited_gl = st.data_editor(gl_df, use_container_width=True,
                                                num_rows="dynamic", key="na_mem_gl")
                    if st.button("💾 Lưu Glossary", key="na_save_gl"):
                        new_gl = []
                        for _, row in edited_gl.iterrows():
                            try:
                                conf_val = float(str(row['Confidence']).replace('%','').strip()) / 100
                            except Exception:
                                conf_val = 0.9
                            new_gl.append({
                                'original': row['Gốc'], 'translation': row['Dịch'],
                                'category': row['Loại'], 'confidence': conf_val,
                                'approved': bool(row['Approved']),
                                'chapter_first_seen': row['Lần đầu thấy'],
                                'notes': row['Ghi chú']
                            })
                        memory_v['glossary'] = new_gl
                        na_save_memory(na_proj, memory_v)
                        st.success("✅ Đã lưu!")
                    # Download as MD
                    if st.button("⬇️ Xuất Glossary (.md)", key="na_dl_gl"):
                        lines = ["# Project Glossary\n"]
                        for g in glossary_v:
                            lines.append(f"- {g.get('original','')} → {g.get('translation','')} [{g.get('category','')}]")
                        st.download_button(
                            "Tải về", '\n'.join(lines),
                            f"{na_proj}_glossary.md", "text/markdown",
                            key="na_dl_gl_btn"
                        )

            with mem_tabs[2]:
                timeline_v = memory_v.get('timeline', [])
                if not timeline_v:
                    st.info("Chưa có sự kiện nào trong timeline.")
                else:
                    st.caption(f"{len(timeline_v)} sự kiện")
                    import pandas as pd
                    tl_df = pd.DataFrame([{
                        'Chapter': t.get('chapter_id',''),
                        'Sự kiện': t.get('event','')
                    } for t in timeline_v])
                    edited_tl = st.data_editor(tl_df, use_container_width=True,
                                                num_rows="dynamic", key="na_mem_tl")
                    if st.button("💾 Lưu Timeline", key="na_save_tl"):
                        new_tl = [{'chapter_id': row['Chapter'], 'event': row['Sự kiện']}
                                   for _, row in edited_tl.iterrows()]
                        memory_v['timeline'] = new_tl
                        na_save_memory(na_proj, memory_v)
                        st.success("✅ Đã lưu!")

            # ===================== MEMORY TAB 3: RELATIONSHIP GRAPH =====================
            with mem_tabs[3]:
                st.markdown("### 🕸️ Relationship Graph")
                st.caption("Biểu đồ quan hệ giữa các nhân vật. Chỉnh sửa trong bảng rồi bấm Lưu.")

                rels_v = memory_v.get('relationships', [])
                chars_v_for_rel = memory_v.get('characters', [])
                char_names_rel = [c.get('name','') for c in chars_v_for_rel if c.get('name')]

                if not rels_v and not char_names_rel:
                    st.info("Chưa có nhân vật nào. Dịch ít nhất 1 chapter và Accept Memory.")
                else:
                    # Editable relationship table
                    import pandas as pd
                    rel_df = pd.DataFrame(rels_v if rels_v else [],
                                          columns=['Nhân vật A', 'Quan hệ', 'Nhân vật B', 'Ghi chú'])
                    if rel_df.empty:
                        rel_df = pd.DataFrame([{
                            'Nhân vật A': char_names_rel[0] if char_names_rel else '',
                            'Quan hệ': '',
                            'Nhân vật B': char_names_rel[1] if len(char_names_rel) > 1 else '',
                            'Ghi chú': ''
                        }])
                    edited_rel = st.data_editor(
                        rel_df, use_container_width=True,
                        num_rows="dynamic", key="na_mem_rel"
                    )
                    if st.button("💾 Lưu Quan hệ", key="na_save_rel"):
                        new_rels = []
                        for _, row in edited_rel.iterrows():
                            if str(row.get('Nhân vật A','')).strip() and str(row.get('Nhân vật B','')).strip():
                                new_rels.append({
                                    'Nhân vật A': row['Nhân vật A'],
                                    'Quan hệ': row['Quan hệ'],
                                    'Nhân vật B': row['Nhân vật B'],
                                    'Ghi chú': row.get('Ghi chú','')
                                })
                        memory_v['relationships'] = new_rels
                        na_save_memory(na_proj, memory_v)
                        st.success("✅ Đã lưu!")
                        st.rerun()

                    # Auto-extract relationships from analysis
                    chapters_for_rel = na_list_chapters(na_proj)
                    if chapters_for_rel and st.button("🤖 AI tự trích xuất quan hệ từ Analysis",
                                                       key="na_auto_rel"):
                        sys_rel = (
                            "You are a relationship extractor for a novel translation project.\n"
                            "Based on character information, extract relationships.\n"
                            "Output ONLY valid JSON array:\n"
                            "[{\"Nhân vật A\": \"\", \"Quan hệ\": \"\", \"Nhân vật B\": \"\", \"Ghi chú\": \"\"}]"
                        )
                        all_chars_info = json.dumps(chars_v_for_rel, ensure_ascii=False)[:4000]
                        # Gather chapter summaries
                        all_summaries = []
                        for _ch in chapters_for_rel[-5:]:  # last 5 chapters
                            _s = na_load_json(os.path.join(na_chapter_dir(na_proj, _ch), 'summary.json'), {})
                            if _s.get('summary'):
                                all_summaries.append(f"{_ch}: {_s['summary']}")
                        prompt_rel = (
                            f"=== CHARACTERS ===\n{all_chars_info}\n\n"
                            f"=== RECENT SUMMARIES ===\n{'\n'.join(all_summaries)}"
                        )
                        with st.spinner("🤖 AI đang phân tích quan hệ..."):
                            rel_raw = generate_with_retry(
                                "gemini-2.5-flash", prompt_rel, sys_rel, None, retries=3, temp=0.2
                            )
                        if rel_raw:
                            import re as _re
                            _jm = _re.search(r'```(?:json)?\s*([\s\S]*?)```', rel_raw)
                            _js = (_jm.group(1) if _jm else rel_raw).strip()
                            _js = _re.sub(r',\s*([}\]])', r'\1', _js)
                            try:
                                extracted_rels = json.loads(_js)
                                memory_v['relationships'] = extracted_rels
                                na_save_memory(na_proj, memory_v)
                                st.success(f"✅ Trích xuất {len(extracted_rels)} quan hệ!")
                                st.rerun()
                            except Exception:
                                st.error("❌ Lỗi parse JSON")
                                st.code(rel_raw)

                    # Visual graph rendering using HTML/CSS/JS
                    st.divider()
                    st.markdown("**📊 Biểu đồ quan hệ:**")
                    saved_rels = memory_v.get('relationships', [])
                    if saved_rels:
                        # Build nodes and edges for visualization
                        all_nodes = set()
                        for r in saved_rels:
                            all_nodes.add(str(r.get('Nhân vật A', '')))
                            all_nodes.add(str(r.get('Nhân vật B', '')))
                        all_nodes = sorted([n for n in all_nodes if n])

                        # Assign stable positions in a circle
                        import math
                        n_nodes = len(all_nodes)
                        cx, cy, radius = 400, 280, 220
                        node_positions = {}
                        for i, name in enumerate(all_nodes):
                            angle = (2 * math.pi * i / n_nodes) - math.pi / 2
                            node_positions[name] = (
                                int(cx + radius * math.cos(angle)),
                                int(cy + radius * math.sin(angle))
                            )

                        # Theme-appropriate palette for nodes
                        palette = ['#0D9488', '#1e88e5', '#d84315', '#8a3ba8',
                                   '#2e7d32', '#d08400', '#c62828', '#5c564d']

                        # Build SVG
                        svg_parts = [
                            '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="560" '
                            'style="background:#F8F6F0;border-radius:12px;font-family:Inter,sans-serif">',
                            '<defs><marker id="arr" markerWidth="8" markerHeight="6" '
                            'refX="8" refY="3" orient="auto">'
                            '<polygon points="0 0, 8 3, 0 6" fill="#8c8273"/>'
                            '</marker></defs>'
                        ]

                        # Draw edges first
                        for r in saved_rels:
                            a = str(r.get('Nhân vật A', ''))
                            b = str(r.get('Nhân vật B', ''))
                            label = str(r.get('Quan hệ', ''))
                            if a in node_positions and b in node_positions:
                                x1, y1 = node_positions[a]
                                x2, y2 = node_positions[b]
                                mx, my = (x1+x2)//2, (y1+y2)//2
                                svg_parts.append(
                                    f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
                                    f'stroke="#8c8273" stroke-width="1.5" stroke-dasharray="4,3" '
                                    f'marker-end="url(#arr)"/>'
                                )
                                if label:
                                    svg_parts.append(
                                        f'<text x="{mx}" y="{my-6}" text-anchor="middle" '
                                        f'fill="#5c564d" font-size="10" '
                                        f'style="paint-order:stroke" stroke="#F8F6F0" stroke-width="3">'
                                        f'{label[:18]}</text>'
                                    )

                        # Draw nodes
                        for i, name in enumerate(all_nodes):
                            x, y = node_positions[name]
                            color = palette[i % len(palette)]
                            short = name[:12] + ('…' if len(name) > 12 else '')
                            svg_parts.append(
                                f'<circle cx="{x}" cy="{y}" r="28" fill="{color}" '
                                f'fill-opacity="0.15" stroke="{color}" stroke-width="2"/>'
                            )
                            svg_parts.append(
                                f'<text x="{x}" y="{y+5}" text-anchor="middle" '
                                f'fill="{color}" font-size="11" font-weight="600" '
                                f'style="paint-order:stroke" stroke="#F8F6F0" stroke-width="3">'
                                f'{short}</text>'
                            )

                        svg_parts.append('</svg>')
                        svg_html = ''.join(svg_parts)
                        st.markdown(
                            f'<div style="overflow-x:auto;border-radius:12px">{svg_html}</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.info("Thêm quan hệ vào bảng bên trên hoặc dùng nút AI tự trích xuất.")

            # ===================== MEMORY TAB 4: ARC SUMMARY =====================
            with mem_tabs[4]:
                st.markdown("### 📊 Arc Summary Generator")
                st.caption(
                    "Tạo tóm tắt cho nhiều chương liên tiếp (Arc/Volume). "
                    "Giúp AI trong các chương sau có ngữ cảnh tổng quan mà không cần nạp từng chương."
                )
                chapters_arc = na_list_chapters(na_proj)
                arcs_path = os.path.join(na_project_dir(na_proj), 'memory', 'arcs.json')
                existing_arcs = na_load_json(arcs_path, [])

                if not chapters_arc:
                    st.info("Chưa có chapter nào.")
                else:
                    col_arc1, col_arc2 = st.columns(2)
                    with col_arc1:
                        arc_name = st.text_input("Tên Arc/Volume",
                                                  placeholder="VD: Volume 1 — Khởi Đầu",
                                                  key="na_arc_name")
                    with col_arc2:
                        chapters_with_summary = [
                            ch for ch in chapters_arc
                            if os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'summary.json'))
                        ]
                        arc_chapters = st.multiselect(
                            "Chọn các chương thuộc Arc:",
                            chapters_arc,
                            default=chapters_with_summary,
                            key="na_arc_chs"
                        )

                    if st.button("📊 Tạo Arc Summary", type="primary", key="na_gen_arc",
                                  disabled=not arc_name or not arc_chapters):
                        # Gather chapter summaries
                        ch_summaries = []
                        for ch in arc_chapters:
                            s = na_load_json(
                                os.path.join(na_chapter_dir(na_proj, ch), 'summary.json'), {}
                            )
                            if s.get('summary'):
                                ch_summaries.append(f"**{ch}**: {s['summary']}")
                            else:
                                ch_summaries.append(f"**{ch}**: (chưa có summary)")

                        if not any('summary' in s for s in
                                   [na_load_json(os.path.join(na_chapter_dir(na_proj, ch), 'summary.json'), {})
                                    for ch in arc_chapters]):
                            st.warning(
                                "⚠️ Chưa có chapter summary nào. "
                                "Dịch chapter và bấm 'Accept & Update Memory' để tạo summary."
                            )
                        else:
                            sys_arc = (
                                "You are a novel editor creating an arc summary for a novel translation project.\n"
                                "Based on the provided chapter summaries, write a comprehensive arc summary that:\n"
                                "1. Covers the main plot points and events\n"
                                "2. Highlights character development\n"
                                "3. Notes important relationships and changes\n"
                                "4. Summarizes the overall arc theme and progression\n"
                                "Write in a clear, structured format. Be thorough but concise."
                            )
                            prompt_arc = (
                                f"=== ARC NAME ===\n{arc_name}\n\n"
                                f"=== CHAPTER SUMMARIES ===\n" +
                                "\n\n".join(ch_summaries)
                            )
                            with st.spinner("📊 AI đang tạo Arc Summary..."):
                                arc_result = generate_with_retry(
                                    "gemini-2.5-flash", prompt_arc, sys_arc,
                                    None, retries=3, temp=0.2
                                )
                            if arc_result:
                                new_arc = {
                                    'name': arc_name,
                                    'chapters': arc_chapters,
                                    'summary': arc_result,
                                    'generated_at': now_gmt7().isoformat()
                                }
                                # Update or append
                                arc_idx = next(
                                    (i for i, a in enumerate(existing_arcs) if a['name'] == arc_name),
                                    None
                                )
                                if arc_idx is not None:
                                    existing_arcs[arc_idx] = new_arc
                                else:
                                    existing_arcs.append(new_arc)
                                na_save_json(arcs_path, existing_arcs)
                                log_action("Novel Agent",
                                           f"Arc summary: {arc_name} | {len(arc_chapters)} chapters")
                                st.success(f"✅ Đã tạo Arc Summary cho **{arc_name}**!")
                                st.rerun()

                    # Display existing arcs
                    if existing_arcs:
                        st.divider()
                        st.markdown("**Arcs đã tạo:**")
                        for arc in existing_arcs:
                            with st.expander(
                                f"📊 {arc['name']} ({len(arc.get('chapters',[]))} chương)",
                                expanded=False
                            ):
                                st.caption(
                                    f"Chương: {', '.join(arc.get('chapters',[]))} | "
                                    f"Tạo lúc: {arc.get('generated_at','')[:16]}"
                                )
                                st.markdown(arc.get('summary',''))
                                c_dl_arc, c_del_arc = st.columns([3, 1])
                                with c_dl_arc:
                                    arc_md = (
                                        f"---\ntitle: {arc['name']}\n"
                                        f"chapters: {', '.join(arc.get('chapters',[]))}\n---\n\n"
                                        + arc.get('summary', '')
                                    )
                                    st.download_button(
                                        "⬇️ Tải Arc (.md)", arc_md,
                                        f"{na_slugify(arc['name'])}_arc_summary.md",
                                        "text/markdown",
                                        key=f"na_dl_arc_{arc['name']}"
                                    )
                                with c_del_arc:
                                    if st.button("🗑️", key=f"na_del_arc_{arc['name']}",
                                                  help="Xóa arc này"):
                                        existing_arcs = [a for a in existing_arcs
                                                          if a['name'] != arc['name']]
                                        na_save_json(arcs_path, existing_arcs)
                                        st.rerun()

            # ===================== MEMORY TAB 5: PROJECT CONFIG =====================
            with mem_tabs[5]:
                st.markdown("**Cấu hình project hiện tại:**")
                st.json(na_cfg)
                st.divider()
                st.markdown("**Chỉnh sửa Style Guide:**")
                new_style = st.text_area("Style Guide:", na_cfg.get('style_guide',''),
                                          height=200, key="na_cfg_style")
                new_thresh = st.slider("Ngưỡng confidence (%)",
                                       50, 95,
                                       int(na_cfg.get('confidence_threshold', 0.8) * 100),
                                       key="na_cfg_thresh")
                new_chunk = st.slider("Chunk size (đoạn/chunk)",
                                       5, 50,
                                       na_cfg.get('chunk_size', 20),
                                       5, key="na_cfg_chunk")

                # Phase 2: Stats panel
                st.divider()
                st.markdown("**📈 Thống kê project:**")
                all_chs_cfg = na_list_chapters(na_proj)
                mem_cfg = na_load_memory(na_proj)
                translated_chs = sum(
                    1 for ch in all_chs_cfg
                    if os.path.exists(os.path.join(na_chapter_dir(na_proj, ch), 'translation.md'))
                )
                approved_terms = sum(1 for g in mem_cfg.get('glossary', []) if g.get('approved'))
                c_s1, c_s2, c_s3, c_s4 = st.columns(4)
                c_s1.metric("📖 Chapters", len(all_chs_cfg))
                c_s2.metric("🌐 Đã dịch", translated_chs)
                c_s3.metric("🧑 Nhân vật", len(mem_cfg.get('characters', [])))
                c_s4.metric("📚 Thuật ngữ", f"{approved_terms}/{len(mem_cfg.get('glossary', []))} ✅")

                if st.button("💾 Lưu cấu hình", key="na_save_cfg"):
                    na_cfg['style_guide'] = new_style
                    na_cfg['confidence_threshold'] = new_thresh / 100
                    na_cfg['chunk_size'] = new_chunk
                    na_save_config(na_proj, na_cfg)
                    st.success("✅ Đã lưu cấu hình project!")
                    st.rerun()

                    na_cfg['chunk_size'] = new_chunk
                    na_save_config(na_proj, na_cfg)
                    st.success("✅ Đã lưu cấu hình project!")
                    st.rerun()

# =================== TAB 10: QC DIFF REVIEW ===================
# ================================================================
with tabs[10]:
    if not client:
        st.warning("⚠️ Cấu hình API Key trong `.env` trước.")
        st.stop()

    # ── Helper: word-level inline diff ──
    def qcd_render_word_diff(original: str, suggested: str) -> str:
        """Render word-level inline diff as HTML with red/green highlights."""
        import difflib as _dl
        import html as _html
        orig_words = original.split()
        sugg_words = suggested.split()
        sm = _dl.SequenceMatcher(None, orig_words, sugg_words)
        parts = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                parts.append(_html.escape(' '.join(orig_words[i1:i2])))
            elif op == 'delete':
                parts.append(f"<span class='qcd-diff-del'>{_html.escape(' '.join(orig_words[i1:i2]))}</span>")
            elif op == 'insert':
                parts.append(f"<span class='qcd-diff-add'>{_html.escape(' '.join(sugg_words[j1:j2]))}</span>")
            elif op == 'replace':
                parts.append(f"<span class='qcd-diff-del'>{_html.escape(' '.join(orig_words[i1:i2]))}</span>")
                parts.append(f"<span class='qcd-diff-add'>{_html.escape(' '.join(sugg_words[j1:j2]))}</span>")
        return ' '.join(parts)

    # ── Helper: category badge ──
    def qcd_badge(category: str) -> str:
        import html as _html
        cat_labels = {
            'name': '🏷️ Tên', 'glossary': '📖 Glossary', 'honorific': '🎭 Xưng hô',
            'pronoun': '👤 Đại từ', 'typo': '✏️ Typo', 'grammar': '📝 Ngữ pháp',
            'spacing': '⬜ Khoảng cách', 'punctuation': '❗ Dấu câu',
            'consistency': '🔄 Nhất quán', 'needs_manual_review': '⚠️ Cần kiểm tra thủ công',
        }
        label = cat_labels.get(category, f'❓ {category}')
        safe_cls = _html.escape(category.lower().replace(' ', '_'))
        return f"<span class='qcd-badge qcd-badge-{safe_cls}'>{label}</span>"

    # ── Helper: confidence color ──
    def qcd_conf_color(conf: int) -> str:
        if conf >= 90: return '#2e7d32'
        if conf >= 70: return '#a6701e'
        return '#c62828'

    # ── Helper: save/load QC Diff session ──
    def qcd_save_session(data: dict):
        os.makedirs(PATHS['qc_diff_dir'], exist_ok=True)
        ts = now_gmt7().strftime('%Y%m%d_%H%M%S')
        path = os.path.join(PATHS['qc_diff_dir'], f'session_{ts}.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        # Also save as latest
        latest = os.path.join(PATHS['qc_diff_dir'], 'latest_session.json')
        with open(latest, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return path

    def qcd_load_latest_session() -> dict:
        latest = os.path.join(PATHS['qc_diff_dir'], 'latest_session.json')
        if os.path.exists(latest):
            with open(latest, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    # ── Header ──
    st.markdown("""
    <div style='background:linear-gradient(135deg,#0D9488 0%,#0B7A70 100%);
         border:1px solid #D1CFC7;color:#ffffff;border-radius:12px;padding:1.2rem 1.6rem;margin-bottom:1rem'>
      <h2 style='margin:0;color:#ffffff;font-size:1.5rem'>🔎 QC Diff Review</h2>
      <p style='margin:0.3rem 0 0;color:rgba(255,255,255,0.85);font-size:0.9rem'>
        AI tạo bản sửa tối thiểu (minimal patch) · Duyệt từng đoạn · Batch approve · Học từ reviewer
      </p>
    </div>
    """, unsafe_allow_html=True)

    # ── Load previous session into session_state if not already loaded ──
    if 'qcd_suggestions' not in st.session_state:
        prev_session = qcd_load_latest_session()
        if prev_session.get('suggestions'):
            st.session_state['qcd_suggestions'] = prev_session['suggestions']
            st.session_state['qcd_accepted_rules'] = prev_session.get('accepted_rules', [])
            st.session_state['qcd_vi_paragraphs'] = prev_session.get('vi_paragraphs', [])
            st.session_state['qcd_metadata'] = prev_session.get('metadata', {})

    # ── Input Section ──
    st.markdown("#### 📥 Dữ liệu QC Diff")

    qcd_vi = st.text_area("Bản dịch Tiếng Việt:", height=200, key="qcd_vi_input",
                           placeholder="Dán toàn bộ bản dịch tiếng Việt cần QC vào đây...")
    qcd_c1, qcd_c2 = st.columns(2)
    with qcd_c1:
        qcd_kr = st.text_area("Tiếng Hàn (source):", height=180, key="qcd_kr_input")
    with qcd_c2:
        qcd_en = st.text_area("Tiếng Anh (tùy chọn):", height=180, key="qcd_en_input")

    # ── Settings ──
    qcd_s1, qcd_s2, qcd_s3 = st.columns([1, 1, 1])
    with qcd_s1:
        qcd_auto_threshold = st.slider(
            "Auto-approve threshold (%)", 90, 100, 97, 1, key="qcd_auto_thresh",
            help="Tự động approve các sửa lỗi Typo/Spacing có confidence ≥ ngưỡng này"
        )
    with qcd_s2:
        qcd_chunk_size = st.slider(
            "Đoạn văn / chunk", 10, 40, 20, 5, key="qcd_chunk_sz",
            help="Số đoạn văn gửi cho AI mỗi lần. Nhỏ hơn = chính xác hơn nhưng chậm hơn."
        )
    with qcd_s3:
        qcd_model = st.selectbox(
            "🤖 AI Model (QC):",
            ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-3.1-flash-lite"],
            index=0,
            key="qcd_model_sel",
            help="gemini-2.5-flash (tức 1.5-flash) thường ổn định và ít lỗi token nhất."
        )

    # ══════════════════════════════════════════════════════════════
    # RUN QC DIFF
    # ══════════════════════════════════════════════════════════════
    if st.button("🔬 Chạy QC Diff", type="primary", key="qcd_run_btn"):
        if not qcd_vi.strip():
            st.error("❌ Thiếu bản dịch VI!")
            st.stop()
        if not qcd_kr.strip() and not qcd_en.strip():
            st.error("❌ Cần ít nhất KR hoặc EN source!")
            st.stop()

        glossary = load_file(PATHS['glossary'])
        notes = load_file(PATHS['notes'])

        vi_paragraphs = [p.strip() for p in qcd_vi.split('\n') if p.strip()]
        kr_text = qcd_kr.strip()
        en_text = qcd_en.strip()

        n_paras = len(vi_paragraphs)
        chunk_sz = qcd_chunk_size
        n_chunks = (n_paras + chunk_sz - 1) // chunk_sz

        target_model = qcd_model
        log_action("QC Diff", f"VI: {n_paras} đoạn | {n_chunks} chunks | Model: {target_model}")

        all_suggestions = []
        bar = st.progress(0, "Chuẩn bị...")
        status = st.status(f"🔬 QC Diff — {n_chunks} chunks", expanded=True)

        sys_prompt = (
            "You are a strict QC editor for Vietnamese novel translation. "
            "Compare the Vietnamese translation against Korean/English sources and the glossary.\n\n"
            "CRITICAL RULES:\n"
            "1. NEVER rewrite an entire paragraph. Only propose MINIMAL, TARGETED edits.\n"
            "2. Only fix: glossary violations, character names, pronouns, typos, spacing, grammar, honorific consistency, terminology, punctuation.\n"
            "3. Preserve sentence order and punctuation unless incorrect.\n"
            "4. If >30% of a paragraph needs changing, set category to 'needs_manual_review' and leave suggested_text same as original.\n"
            "5. Keep all suffixes (-ie, -ah, -ya, -ssi, -nim, -gun) if present in source.\n"
            "6. Do NOT add speaker tags not present in source.\n"
            "7. Output ONLY a valid JSON array. No markdown fences, no explanation.\n\n"
            "OUTPUT FORMAT — JSON array of objects, one per paragraph that has issues. Skip correct paragraphs.\n"
            "[\n"
            "  {\n"
            '    "paragraph_idx": 1,\n'
            '    "original_text": "exact original text",\n'
            '    "suggested_text": "text with minimal fixes applied",\n'
            '    "category": "name|glossary|honorific|pronoun|typo|grammar|spacing|punctuation|consistency|needs_manual_review",\n'
            '    "confidence": 96,\n'
            '    "reason": "Brief explanation referencing glossary/source"\n'
            "  }\n"
            "]\n"
            "If no issues found, return an empty array: []"
        )

        for ci in range(n_chunks):
            s, e = ci * chunk_sz, min((ci + 1) * chunk_sz, n_paras)
            bar.progress(ci / n_chunks, f"Chunk {ci+1}/{n_chunks}...")
            status.write(f"📋 Chunk {ci+1}/{n_chunks} — đoạn {s+1}~{e}")

            # Build numbered VI chunk
            vi_chunk_numbered = ""
            for idx in range(s, e):
                vi_chunk_numbered += f"{idx+1}: {vi_paragraphs[idx]}\n"

            # KR/EN chunks (best-effort line alignment)
            kr_lines = kr_text.split('\n') if kr_text else []
            en_lines = en_text.split('\n') if en_text else []
            kr_chunk = '\n'.join(kr_lines[s:e]) if kr_lines else "(không có)"
            en_ref = ""
            if en_lines:
                en_ref = f"\n==== EN ====\n{chr(10).join(en_lines[s:e])}\n"

            user_prompt = (
                f"==== GLOSSARY ====\n{glossary[:3000]}\n\n"
                f"==== NOTES ====\n{notes[:1500]}\n\n"
                f"==== KR ====\n{kr_chunk}\n"
                f"{en_ref}\n"
                f"==== VI (with paragraph numbers) ====\n{vi_chunk_numbered}"
            )

            raw = generate_with_retry(target_model, user_prompt, sys_prompt, status, retries=3, temp=0.2)

            if raw and raw.strip():
                import re as _re
                # Strip markdown fences if present
                json_match = _re.search(r'```(?:json)?\s*([\s\S]*?)```', raw)
                json_str = json_match.group(1) if json_match else raw.strip()
                # Remove trailing commas
                json_str = _re.sub(r',\s*([}\]])', r'\1', json_str)
                try:
                    chunk_suggestions = json.loads(json_str)
                    if isinstance(chunk_suggestions, list):
                        for sug in chunk_suggestions:
                            sug['id'] = f"sug_{len(all_suggestions)+1:04d}"
                            sug['status'] = 'pending'
                            sug['reviewer_edit'] = None
                            # Ensure confidence is int
                            sug['confidence'] = int(sug.get('confidence', 80))
                            all_suggestions.append(sug)
                        status.write(f"  ⚠️ {len(chunk_suggestions)} sửa lỗi ở chunk {ci+1}")
                    else:
                        status.write(f"  ⚠️ Chunk {ci+1}: AI trả về không phải array")
                except json.JSONDecodeError:
                    status.write(f"  ❌ Chunk {ci+1}: Lỗi parse JSON")
                    # Store raw for debugging
                    all_suggestions.append({
                        'id': f"sug_err_{ci}", 'paragraph_idx': s+1,
                        'original_text': f'[Parse error chunk {ci+1}]',
                        'suggested_text': raw[:500], 'category': 'needs_manual_review',
                        'confidence': 0, 'reason': 'JSON parse error from AI',
                        'status': 'pending', 'reviewer_edit': None
                    })
            else:
                status.write(f"  ✅ Chunk {ci+1} — không có lỗi")

            time.sleep(1)

        bar.progress(1.0, "✅ QC Diff hoàn tất!")
        status.update(label=f"✅ Xong — {len(all_suggestions)} sửa lỗi", state="complete")

        # Auto-approve high-confidence typo/spacing fixes
        auto_count = 0
        for sug in all_suggestions:
            if (sug['confidence'] >= qcd_auto_threshold
                    and sug.get('category', '') in ('typo', 'spacing', 'punctuation')
                    and sug['status'] == 'pending'):
                sug['status'] = 'approved'
                auto_count += 1
        if auto_count:
            st.info(f"🤖 Tự động approve {auto_count} sửa lỗi typo/spacing/punctuation (confidence ≥ {qcd_auto_threshold}%)")

        # Save to session state
        st.session_state['qcd_suggestions'] = all_suggestions
        st.session_state['qcd_accepted_rules'] = []
        st.session_state['qcd_vi_paragraphs'] = vi_paragraphs
        st.session_state['qcd_metadata'] = {
            'created_at': now_gmt7().isoformat(),
            'n_paragraphs': n_paras,
            'model': target_model,
        }

        # Save session to file
        qcd_save_session({
            'metadata': st.session_state['qcd_metadata'],
            'suggestions': all_suggestions,
            'accepted_rules': [],
            'vi_paragraphs': vi_paragraphs,
        })
        st.rerun()

    # ══════════════════════════════════════════════════════════════
    # DISPLAY RESULTS
    # ══════════════════════════════════════════════════════════════
    if st.session_state.get('qcd_suggestions') is not None and len(st.session_state.get('qcd_suggestions', [])) > 0:
        suggestions = st.session_state['qcd_suggestions']
        accepted_rules = st.session_state.get('qcd_accepted_rules', [])
        vi_paragraphs = st.session_state.get('qcd_vi_paragraphs', [])
        meta = st.session_state.get('qcd_metadata', {})

        # ── Statistics Dashboard ──
        st.divider()
        st.markdown("#### 📊 Tổng quan QC Diff")

        total = len(suggestions)
        n_pending = sum(1 for s in suggestions if s['status'] == 'pending')
        n_approved = sum(1 for s in suggestions if s['status'] == 'approved')
        n_discarded = sum(1 for s in suggestions if s['status'] == 'discarded')
        n_edited = sum(1 for s in suggestions if s['status'] == 'edited')
        n_manual = sum(1 for s in suggestions if s.get('category') == 'needs_manual_review')

        mc1, mc2, mc3, mc4, mc5 = st.columns(5)
        mc1.metric("📝 Tổng sửa", total)
        mc2.metric("⏳ Chờ duyệt", n_pending)
        mc3.metric("✅ Đã duyệt", n_approved)
        mc4.metric("❌ Bỏ qua", n_discarded)
        mc5.metric("✏️ Sửa tay", n_edited)

        # Category breakdown
        cat_counts = {}
        for s in suggestions:
            cat = s.get('category', 'other')
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
        if cat_counts:
            with st.expander("📂 Phân loại chi tiết"):
                cat_cols = st.columns(min(len(cat_counts), 5))
                for i, (cat, cnt) in enumerate(sorted(cat_counts.items(), key=lambda x: -x[1])):
                    cat_labels = {
                        'name': '🏷️ Tên', 'glossary': '📖 Glossary', 'honorific': '🎭 Xưng hô',
                        'pronoun': '👤 Đại từ', 'typo': '✏️ Typo', 'grammar': '📝 Ngữ pháp',
                        'spacing': '⬜ Spacing', 'punctuation': '❗ Dấu câu',
                        'consistency': '🔄 Nhất quán', 'needs_manual_review': '⚠️ Manual',
                    }
                    cat_cols[i % len(cat_cols)].metric(cat_labels.get(cat, cat), cnt)

        # Progress bar
        if total > 0:
            reviewed = n_approved + n_discarded + n_edited
            st.progress(reviewed / total, f"Đã duyệt: {reviewed}/{total} ({reviewed*100//total}%)")

        # ── Filters ──
        st.divider()
        fc1, fc2, fc3 = st.columns(3)
        with fc1:
            filter_status = st.multiselect(
                "Lọc theo trạng thái:",
                ["pending", "approved", "discarded", "edited", "needs_manual_review"],
                default=["pending"],
                key="qcd_filter_status",
                format_func=lambda x: {'pending': '⏳ Chờ duyệt', 'approved': '✅ Đã duyệt',
                                        'discarded': '❌ Bỏ qua', 'edited': '✏️ Sửa tay',
                                        'needs_manual_review': '⚠️ Cần kiểm tra'}.get(x, x)
            )
        with fc2:
            all_cats = sorted(set(s.get('category', 'other') for s in suggestions))
            filter_cats = st.multiselect(
                "Lọc theo loại:",
                all_cats,
                default=[],
                key="qcd_filter_cats",
                format_func=lambda x: {
                    'name': '🏷️ Tên', 'glossary': '📖 Glossary', 'honorific': '🎭 Xưng hô',
                    'pronoun': '👤 Đại từ', 'typo': '✏️ Typo', 'grammar': '📝 Ngữ pháp',
                    'spacing': '⬜ Spacing', 'punctuation': '❗ Dấu câu',
                    'consistency': '🔄 Nhất quán', 'needs_manual_review': '⚠️ Manual',
                }.get(x, x)
            )
        with fc3:
            filter_conf_min = st.slider("Confidence tối thiểu:", 0, 100, 0, 5, key="qcd_filter_conf")

        # Apply filters
        filtered = suggestions
        if filter_status:
            filtered = [s for s in filtered if s['status'] in filter_status
                        or (s.get('category') == 'needs_manual_review' and 'needs_manual_review' in filter_status)]
        if filter_cats:
            filtered = [s for s in filtered if s.get('category', 'other') in filter_cats]
        if filter_conf_min > 0:
            filtered = [s for s in filtered if s.get('confidence', 0) >= filter_conf_min]

        st.caption(f"Hiển thị {len(filtered)}/{total} sửa lỗi")

        # ── Batch Operations ──
        batch_c1, batch_c2, batch_c3 = st.columns(3)
        with batch_c1:
            if st.button("✅ Approve tất cả đang hiển thị", key="qcd_batch_approve"):
                for s in filtered:
                    if s['status'] == 'pending':
                        s['status'] = 'approved'
                        # Create accepted rule
                        if s.get('original_text') != s.get('suggested_text'):
                            accepted_rules.append({
                                'id': f"rule_{len(accepted_rules)+1:04d}",
                                'type': s.get('category', 'other'),
                                'source': s.get('original_text', ''),
                                'target': s.get('suggested_text', ''),
                                'created_from_paragraph': s.get('paragraph_idx', 0),
                                'created_at': now_gmt7().isoformat(),
                            })
                st.session_state['qcd_accepted_rules'] = accepted_rules
                qcd_save_session({
                    'metadata': meta, 'suggestions': suggestions,
                    'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                })
                st.rerun()
        with batch_c2:
            if st.button("❌ Discard tất cả đang hiển thị", key="qcd_batch_discard"):
                for s in filtered:
                    if s['status'] == 'pending':
                        s['status'] = 'discarded'
                qcd_save_session({
                    'metadata': meta, 'suggestions': suggestions,
                    'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                })
                st.rerun()
        with batch_c3:
            if st.button("🔄 Reset tất cả về Pending", key="qcd_batch_reset"):
                for s in suggestions:
                    s['status'] = 'pending'
                    s['reviewer_edit'] = None
                st.session_state['qcd_accepted_rules'] = []
                qcd_save_session({
                    'metadata': meta, 'suggestions': suggestions,
                    'accepted_rules': [], 'vi_paragraphs': vi_paragraphs,
                })
                st.rerun()

        # ── Review Cards ──
        st.divider()
        st.markdown(f"#### 📋 Duyệt sửa lỗi ({len(filtered)})")

        for si, sug in enumerate(filtered):
            sug_id = sug['id']
            status_val = sug['status']
            category = sug.get('category', 'other')
            confidence = sug.get('confidence', 0)
            conf_color = qcd_conf_color(confidence)
            para_idx = sug.get('paragraph_idx', '?')
            original = sug.get('original_text', '')
            suggested = sug.get('suggested_text', '')
            reason = sug.get('reason', '')

            # Card CSS class
            card_class = {
                'approved': 'qcd-card-approved', 'discarded': 'qcd-card-discarded',
                'edited': 'qcd-card-edited',
            }.get(status_val, '')
            if category == 'needs_manual_review':
                card_class = 'qcd-card-manual'

            # Status icon
            status_icon = {
                'pending': '⏳', 'approved': '✅', 'discarded': '❌', 'edited': '✏️'
            }.get(status_val, '❓')

            # Render inline diff
            if category == 'needs_manual_review':
                diff_html = f"<em style='color:#d08400'>⚠️ Đoạn này cần kiểm tra thủ công — thay đổi quá 30%</em>"
            elif original == suggested:
                diff_html = f"<em style='color:#5c564d'>Không có thay đổi</em>"
            else:
                diff_html = qcd_render_word_diff(original, suggested)

            st.markdown(f"""
            <div class='qcd-card {card_class}'>
              <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:0.5rem'>
                <span style='font-weight:600;color:#2D2A26'>Đoạn {para_idx} {status_icon}</span>
                <div>
                  {qcd_badge(category)}
                  <span style='margin-left:8px;color:{conf_color};font-weight:600;font-size:13px'>{confidence}%</span>
                </div>
              </div>
              <div style='font-size:0.92rem;line-height:1.7;color:#2D2A26;margin-bottom:0.3rem'>
                {diff_html}
              </div>
              <div style='font-size:0.8rem;color:#5c564d;margin-top:0.4rem'>
                💡 {reason}
              </div>
            </div>
            """, unsafe_allow_html=True)

            # Action buttons (only for pending items)
            if status_val == 'pending':
                btn_cols = st.columns([1, 1, 1, 3])
                with btn_cols[0]:
                    if st.button("✅", key=f"qcd_appr_{sug_id}", help="Approve",
                                 use_container_width=True):
                        sug['status'] = 'approved'
                        # Create accepted rule
                        if original != suggested:
                            accepted_rules.append({
                                'id': f"rule_{len(accepted_rules)+1:04d}",
                                'type': category,
                                'source': original,
                                'target': suggested,
                                'created_from_paragraph': para_idx,
                                'created_at': now_gmt7().isoformat(),
                            })
                            st.session_state['qcd_accepted_rules'] = accepted_rules
                        qcd_save_session({
                            'metadata': meta, 'suggestions': suggestions,
                            'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                        })
                        st.rerun()
                with btn_cols[1]:
                    if st.button("❌", key=f"qcd_disc_{sug_id}", help="Discard",
                                 use_container_width=True):
                        sug['status'] = 'discarded'
                        qcd_save_session({
                            'metadata': meta, 'suggestions': suggestions,
                            'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                        })
                        st.rerun()
                with btn_cols[2]:
                    if st.button("✏️", key=f"qcd_edit_toggle_{sug_id}", help="Sửa tay",
                                 use_container_width=True):
                        st.session_state[f'qcd_editing_{sug_id}'] = True

                # Manual edit input
                if st.session_state.get(f'qcd_editing_{sug_id}'):
                    edit_val = st.text_area(
                        f"Sửa đoạn {para_idx}:",
                        value=suggested,
                        height=80,
                        key=f"qcd_edit_val_{sug_id}"
                    )
                    ec1, ec2 = st.columns(2)
                    with ec1:
                        if st.button("💾 Lưu sửa", key=f"qcd_edit_save_{sug_id}",
                                     type="primary", use_container_width=True):
                            sug['status'] = 'edited'
                            sug['reviewer_edit'] = edit_val
                            # Create rule from manual edit (learning from reviewer)
                            accepted_rules.append({
                                'id': f"rule_{len(accepted_rules)+1:04d}",
                                'type': category,
                                'source': original,
                                'target': edit_val,
                                'created_from_paragraph': para_idx,
                                'reviewer_override': True,
                                'created_at': now_gmt7().isoformat(),
                            })
                            st.session_state['qcd_accepted_rules'] = accepted_rules
                            del st.session_state[f'qcd_editing_{sug_id}']
                            qcd_save_session({
                                'metadata': meta, 'suggestions': suggestions,
                                'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                            })
                            st.rerun()
                    with ec2:
                        if st.button("❌ Hủy", key=f"qcd_edit_cancel_{sug_id}",
                                     use_container_width=True):
                            del st.session_state[f'qcd_editing_{sug_id}']
                            st.rerun()

            # Batch apply option for approved items
            elif status_val == 'approved' and original != suggested:
                # Check if there are other paragraphs with the same original text pattern
                same_pattern_count = sum(
                    1 for s2 in suggestions
                    if s2['id'] != sug_id
                    and s2['status'] == 'pending'
                    and s2.get('original_text', '') != s2.get('suggested_text', '')
                    and original in s2.get('original_text', '')
                )
                if same_pattern_count > 0:
                    if st.button(
                        f"🔄 Áp dụng cho {same_pattern_count} đoạn tương tự",
                        key=f"qcd_batch_{sug_id}",
                        help="Approve tất cả các đoạn có cùng lỗi"
                    ):
                        for s2 in suggestions:
                            if (s2['id'] != sug_id
                                    and s2['status'] == 'pending'
                                    and original in s2.get('original_text', '')):
                                s2['status'] = 'approved'
                        qcd_save_session({
                            'metadata': meta, 'suggestions': suggestions,
                            'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                        })
                        st.rerun()

        # ── Accepted Rules ──
        if accepted_rules:
            st.divider()
            with st.expander(f"📋 Quy tắc đã học ({len(accepted_rules)})", expanded=False):
                for rule in accepted_rules:
                    override_badge = " 👤" if rule.get('reviewer_override') else ""
                    cat_labels = {
                        'name': '🏷️', 'glossary': '📖', 'honorific': '🎭',
                        'pronoun': '👤', 'typo': '✏️', 'grammar': '📝',
                    }
                    icon = cat_labels.get(rule.get('type', ''), '❓')
                    st.markdown(
                        f"- {icon} `{rule.get('source', '')[:50]}` → "
                        f"**{rule.get('target', '')[:50]}** "
                        f"(đoạn {rule.get('created_from_paragraph', '?')}){override_badge}"
                    )

                # ── Apply & Export ──
        st.divider()
        st.markdown("#### 📥 Áp dụng & Xuất bản dịch đã sửa")

        if st.button("📥 Tạo bản dịch đã sửa", type="primary", key="qcd_apply_btn"):
            if not vi_paragraphs:
                st.error("❌ Không có dữ liệu bản dịch gốc!")
            else:
                corrected = list(vi_paragraphs)  # copy

                # Apply approved and edited suggestions
                applied_count = 0
                for sug in suggestions:
                    if sug['status'] in ('approved', 'edited'):
                        pidx = sug.get('paragraph_idx', 0)
                        if 1 <= pidx <= len(corrected):
                            if sug['status'] == 'edited' and sug.get('reviewer_edit'):
                                corrected[pidx - 1] = sug['reviewer_edit']
                            elif sug.get('suggested_text') and sug['original_text'] != sug['suggested_text']:
                                corrected[pidx - 1] = sug['suggested_text']
                            applied_count += 1

                # Also apply approved sync candidates
                sync_cands = st.session_state.get('qcd_sync_candidates', [])
                for sc in sync_cands:
                    if sc.get('status') == 'approved':
                        pidx = sc.get('paragraph_idx', 0)
                        if 1 <= pidx <= len(corrected):
                            corrected[pidx - 1] = sc.get('new_text', corrected[pidx - 1])
                            applied_count += 1

                corrected_text = '\n'.join(corrected)
                st.session_state['qcd_corrected'] = corrected_text
                st.success(f"✅ Đã áp dụng {applied_count} sửa lỗi (bao gồm sync)!")

        if st.session_state.get('qcd_corrected'):
            st.text_area("Bản dịch đã sửa:", value=st.session_state['qcd_corrected'],
                         height=300, key="qcd_corrected_area")
            st.download_button(
                "⬇ Tải xuống bản sửa (.txt)",
                data=st.session_state['qcd_corrected'],
                file_name=f"vi_qc_corrected_{now_gmt7().strftime('%Y%m%d_%H%M')}.txt",
                mime="text/plain",
                key="qcd_download"
            )

        # ══════════════════════════════════════════════════════════════
        # PHASE 3: CHAPTER SYNCHRONIZATION
        # ══════════════════════════════════════════════════════════════
        if accepted_rules:
            st.divider()
            st.markdown("""
            <div style='background:linear-gradient(135deg,#e0f2f1 0%,#b2dfdb 100%);
                 border:1px solid #0D9488;border-radius:12px;padding:1rem 1.4rem;margin-bottom:1rem'>
              <h4 style='margin:0;color:#0B7A70;font-size:1.2rem'>🔄 Chapter Synchronization</h4>
              <p style='margin:0.3rem 0 0;color:#5c564d;font-size:0.85rem'>
                Áp dụng các quy tắc đã duyệt vào toàn bộ chương — phát hiện xung đột, xem trước trước khi sửa
              </p>
            </div>
            """, unsafe_allow_html=True)

            # Helper: find all occurrences in paragraphs using accepted rules
            def qcd_find_sync_candidates(paragraphs, rules, existing_suggestions):
                import re as _re
                candidates = []
                # Build set of paragraph indices that have already been reviewed
                reviewed_para_indices = set()
                for s in existing_suggestions:
                    if s.get('status') in ('approved', 'edited', 'discarded'):
                        reviewed_para_indices.add(s.get('paragraph_idx', 0))

                # Build set of paragraph indices with approved suggestions (for conflict detection)
                approved_para_indices = set()
                for s in existing_suggestions:
                    if s.get('status') in ('approved', 'edited'):
                        approved_para_indices.add(s.get('paragraph_idx', 0))

                for rule in rules:
                    source = rule.get('source', '')
                    target = rule.get('target', '')
                    rule_type = rule.get('type', 'other')
                    if not source or not target or source == target:
                        continue

                    # Extract the key diff pattern from rule
                    # For short rules (single word/phrase), search directly
                    # For full paragraph rules, use word-level extraction
                    import difflib as _dl
                    src_words = source.split()
                    tgt_words = target.split()
                    sm = _dl.SequenceMatcher(None, src_words, tgt_words)

                    # Extract changed word pairs
                    change_pairs = []
                    for op, i1, i2, j1, j2 in sm.get_opcodes():
                        if op in ('replace', 'delete', 'insert'):
                            old_frag = ' '.join(src_words[i1:i2]) if i1 < i2 else ''
                            new_frag = ' '.join(tgt_words[j1:j2]) if j1 < j2 else ''
                            if old_frag:  # Only search for fragments that exist
                                change_pairs.append((old_frag, new_frag))

                    if not change_pairs:
                        continue

                    for pidx, para in enumerate(paragraphs, 1):
                        # Skip the paragraph that created this rule
                        if pidx == rule.get('created_from_paragraph', -1):
                            continue

                        for old_frag, new_frag in change_pairs:
                            # Case-insensitive search
                            if old_frag.lower() in para.lower():
                                # Apply replacement (preserve case of surrounding text)
                                pattern = _re.compile(_re.escape(old_frag), _re.IGNORECASE)
                                new_text = pattern.sub(new_frag, para)

                                if new_text != para:
                                    # Check for conflict
                                    conflict = pidx in approved_para_indices
                                    # Confidence: higher if exact case match
                                    conf = 95 if old_frag in para else 85

                                    cand_id = f"sync_{len(candidates)+1:04d}"
                                    candidates.append({
                                        'id': cand_id,
                                        'paragraph_idx': pidx,
                                        'matched_rule': rule['id'],
                                        'rule_type': rule_type,
                                        'old_fragment': old_frag,
                                        'new_fragment': new_frag,
                                        'old_text': para,
                                        'new_text': new_text,
                                        'confidence': conf,
                                        'conflict': conflict,
                                        'status': 'pending',
                                    })

                # Deduplicate by paragraph_idx + old_fragment
                seen = set()
                deduped = []
                for c in candidates:
                    key = (c['paragraph_idx'], c['old_fragment'])
                    if key not in seen:
                        seen.add(key)
                        deduped.append(c)

                return deduped

            # Run sync button
            if st.button("🔄 Quét Synchronization", type="primary", key="qcd_run_sync",
                         help="Tìm tất cả đoạn trong chương có cùng lỗi với các quy tắc đã duyệt"):
                sync_candidates = qcd_find_sync_candidates(vi_paragraphs, accepted_rules, suggestions)
                st.session_state['qcd_sync_candidates'] = sync_candidates

                # Save to session
                session_data = {
                    'metadata': meta, 'suggestions': suggestions,
                    'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                    'sync_candidates': sync_candidates,
                    'revisions': st.session_state.get('qcd_revisions', []),
                }
                qcd_save_session(session_data)

                if sync_candidates:
                    st.success(f"🔍 Tìm thấy **{len(sync_candidates)}** đoạn cần đồng bộ!")
                else:
                    st.info("✅ Không tìm thấy đoạn nào cần đồng bộ thêm.")
                st.rerun()

            # Display sync candidates
            sync_candidates = st.session_state.get('qcd_sync_candidates', [])
            if sync_candidates:
                n_sync_total = len(sync_candidates)
                n_sync_pending = sum(1 for c in sync_candidates if c['status'] == 'pending')
                n_sync_approved = sum(1 for c in sync_candidates if c['status'] == 'approved')
                n_sync_skipped = sum(1 for c in sync_candidates if c['status'] == 'skipped')
                n_sync_conflict = sum(1 for c in sync_candidates if c.get('conflict'))

                sc1, sc2, sc3, sc4 = st.columns(4)
                sc1.metric("🔍 Tìm thấy", n_sync_total)
                sc2.metric("⏳ Chờ duyệt", n_sync_pending)
                sc3.metric("✅ Đã duyệt", n_sync_approved)
                sc4.metric("⚠️ Xung đột", n_sync_conflict)

                if n_sync_total > 0:
                    st.progress(
                        (n_sync_approved + n_sync_skipped) / n_sync_total,
                        f"Đồng bộ: {n_sync_approved + n_sync_skipped}/{n_sync_total}"
                    )

                # Sync filter
                sync_fc1, sync_fc2 = st.columns(2)
                with sync_fc1:
                    sync_filter_status = st.multiselect(
                        "Lọc sync:",
                        ["pending", "approved", "skipped"],
                        default=["pending"],
                        key="qcd_sync_filter",
                        format_func=lambda x: {'pending': '⏳ Chờ', 'approved': '✅ Đã duyệt',
                                                'skipped': '⏭️ Bỏ qua'}.get(x, x)
                    )
                with sync_fc2:
                    sync_show_conflicts = st.checkbox("Chỉ hiện xung đột", key="qcd_sync_conflicts_only")

                filtered_sync = sync_candidates
                if sync_filter_status:
                    filtered_sync = [c for c in filtered_sync if c['status'] in sync_filter_status]
                if sync_show_conflicts:
                    filtered_sync = [c for c in filtered_sync if c.get('conflict')]

                # Batch sync operations
                sync_bc1, sync_bc2 = st.columns(2)
                with sync_bc1:
                    if st.button("✅ Approve tất cả (không xung đột)", key="qcd_sync_batch_approve"):
                        rev_batch = []
                        for c in sync_candidates:
                            if c['status'] == 'pending' and not c.get('conflict'):
                                c['status'] = 'approved'
                                rev_batch.append({
                                    'action': 'sync_approve',
                                    'candidate_id': c['id'],
                                    'paragraph_idx': c['paragraph_idx'],
                                    'old_text': c['old_text'],
                                    'new_text': c['new_text'],
                                    'timestamp': now_gmt7().isoformat(),
                                })
                        if rev_batch:
                            revisions = st.session_state.get('qcd_revisions', [])
                            revisions.extend(rev_batch)
                            st.session_state['qcd_revisions'] = revisions
                        qcd_save_session({
                            'metadata': meta, 'suggestions': suggestions,
                            'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                            'sync_candidates': sync_candidates,
                            'revisions': st.session_state.get('qcd_revisions', []),
                        })
                        st.rerun()
                with sync_bc2:
                    if st.button("⏭️ Bỏ qua tất cả đang hiển thị", key="qcd_sync_batch_skip"):
                        for c in filtered_sync:
                            if c['status'] == 'pending':
                                c['status'] = 'skipped'
                        qcd_save_session({
                            'metadata': meta, 'suggestions': suggestions,
                            'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                            'sync_candidates': sync_candidates,
                            'revisions': st.session_state.get('qcd_revisions', []),
                        })
                        st.rerun()

                # Sync candidate cards
                st.markdown(f"##### 🔄 Preview đồng bộ ({len(filtered_sync)})")

                for sci, sc in enumerate(filtered_sync):
                    sc_id = sc['id']
                    sc_status = sc['status']
                    sc_conflict = sc.get('conflict', False)
                    sc_pidx = sc['paragraph_idx']
                    sc_conf = sc.get('confidence', 85)
                    sc_rule_type = sc.get('rule_type', 'other')

                    # Card border color
                    if sc_conflict:
                        sc_border = '#d08400'
                        sc_bg = 'rgba(208,132,0,0.04)'
                    elif sc_status == 'approved':
                        sc_border = '#2e7d32'
                        sc_bg = 'rgba(46,125,50,0.04)'
                    elif sc_status == 'skipped':
                        sc_border = '#D1CFC7'
                        sc_bg = 'rgba(140,130,115,0.04)'
                    else:
                        sc_border = '#0D9488'
                        sc_bg = '#F8F6F0'

                    sc_status_icon = {'pending': '⏳', 'approved': '✅', 'skipped': '⏭️'}.get(sc_status, '❓')
                    conflict_badge = " <span style='color:#d08400;font-weight:600;font-size:11px'>⚠️ XUNG ĐỘT — đoạn đã được duyệt trước</span>" if sc_conflict else ""

                    # Inline diff for the change
                    sc_diff = qcd_render_word_diff(sc['old_text'], sc['new_text'])

                    st.markdown(f"""
                    <div style='border:1px solid {sc_border};border-radius:10px;padding:0.8rem 1rem;
                         margin-bottom:0.6rem;background:{sc_bg}'>
                      <div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:0.4rem'>
                        <span style='font-weight:600;color:#2D2A26'>Đoạn {sc_pidx} {sc_status_icon}</span>
                        <div>
                          {qcd_badge(sc_rule_type)}
                          <span style='margin-left:6px;color:{qcd_conf_color(sc_conf)};font-weight:600;font-size:12px'>{sc_conf}%</span>
                        </div>
                      </div>
                      {conflict_badge}
                      <div style='font-size:0.88rem;line-height:1.6;color:#2D2A26;margin:0.3rem 0'>
                        {sc_diff}
                      </div>
                      <div style='font-size:0.78rem;color:#8c8273'>
                        Quy tắc: <code>{sc.get('old_fragment','')}</code> → <code>{sc.get('new_fragment','')}</code>
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if sc_status == 'pending':
                        sc_btn1, sc_btn2, sc_btn3 = st.columns([1, 1, 4])
                        with sc_btn1:
                            btn_label = "✅ Approve" if not sc_conflict else "✅ Override"
                            if st.button(btn_label, key=f"qcd_sync_appr_{sc_id}",
                                         use_container_width=True):
                                sc['status'] = 'approved'
                                # Record revision
                                revisions = st.session_state.get('qcd_revisions', [])
                                revisions.append({
                                    'action': 'sync_approve',
                                    'candidate_id': sc_id,
                                    'paragraph_idx': sc_pidx,
                                    'old_text': sc['old_text'],
                                    'new_text': sc['new_text'],
                                    'conflict_override': sc_conflict,
                                    'timestamp': now_gmt7().isoformat(),
                                })
                                st.session_state['qcd_revisions'] = revisions
                                qcd_save_session({
                                    'metadata': meta, 'suggestions': suggestions,
                                    'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                                    'sync_candidates': sync_candidates,
                                    'revisions': revisions,
                                })
                                st.rerun()
                        with sc_btn2:
                            if st.button("⏭️ Bỏ qua", key=f"qcd_sync_skip_{sc_id}",
                                         use_container_width=True):
                                sc['status'] = 'skipped'
                                qcd_save_session({
                                    'metadata': meta, 'suggestions': suggestions,
                                    'accepted_rules': accepted_rules, 'vi_paragraphs': vi_paragraphs,
                                    'sync_candidates': sync_candidates,
                                    'revisions': st.session_state.get('qcd_revisions', []),
                                })
                                st.rerun()

        # ══════════════════════════════════════════════════════════════
        # PHASE 4: UNDO / REVISION HISTORY
        # ══════════════════════════════════════════════════════════════
        revisions = st.session_state.get('qcd_revisions', [])
        if revisions or any(s['status'] != 'pending' for s in suggestions):
            st.divider()
            st.markdown("""
            <div style='background:linear-gradient(135deg,#f3e5f5 0%,#e1bee7 100%);
                 border:1px solid #8a3ba8;border-radius:12px;padding:1rem 1.4rem;margin-bottom:1rem'>
              <h4 style='margin:0;color:#8a3ba8;font-size:1.2rem'>⏪ Revision History & Undo</h4>
              <p style='margin:0.3rem 0 0;color:#5c564d;font-size:0.85rem'>
                Mỗi hành động được lưu lại — có thể hoàn tác từng bước
              </p>
            </div>
            """, unsafe_allow_html=True)

            # Build revision list from all actions
            all_revisions = list(revisions)

            # Also build revisions from suggestion status changes (if not already tracked)
            for sug in suggestions:
                if sug['status'] in ('approved', 'discarded', 'edited'):
                    # Check if this suggestion already has a revision entry
                    existing_rev_ids = {r.get('suggestion_id') for r in all_revisions if r.get('suggestion_id')}
                    if sug['id'] not in existing_rev_ids:
                        rev_entry = {
                            'action': f"qc_{sug['status']}",
                            'suggestion_id': sug['id'],
                            'paragraph_idx': sug.get('paragraph_idx', '?'),
                            'old_text': sug.get('original_text', '')[:60],
                            'new_text': (sug.get('reviewer_edit') or sug.get('suggested_text', ''))[:60],
                            'category': sug.get('category', ''),
                            'timestamp': meta.get('created_at', ''),
                        }
                        all_revisions.append(rev_entry)

            n_revisions = len(all_revisions)

            with st.expander(f"📜 Lịch sử thay đổi ({n_revisions} hành động)", expanded=False):
                if not all_revisions:
                    st.info("Chưa có hành động nào.")
                else:
                    # Show in reverse chronological order
                    for ri, rev in enumerate(reversed(all_revisions)):
                        rev_idx = n_revisions - ri
                        action = rev.get('action', '?')
                        action_labels = {
                            'qc_approved': '✅ Approve', 'qc_discarded': '❌ Discard',
                            'qc_edited': '✏️ Edit', 'sync_approve': '🔄 Sync Approve',
                            'undo': '⏪ Undo',
                        }
                        action_label = action_labels.get(action, action)
                        pidx = rev.get('paragraph_idx', '?')
                        old_snip = rev.get('old_text', '')[:40]
                        new_snip = rev.get('new_text', '')[:40]
                        ts = rev.get('timestamp', '')[:19]
                        conflict_tag = " ⚠️" if rev.get('conflict_override') else ""

                        st.markdown(
                            f"**#{rev_idx}** {action_label}{conflict_tag} — "
                            f"Đoạn {pidx} — "
                            f"`{old_snip}` → `{new_snip}` "
                            f"<span style='color:#8c8273;font-size:11px'>{ts}</span>",
                            unsafe_allow_html=True
                        )

                        # Undo button for each revision (only for non-undo actions)
                        if action != 'undo':
                            if st.button(f"⏪ Undo", key=f"qcd_undo_{ri}_{rev_idx}",
                                         help=f"Hoàn tác hành động #{rev_idx}"):
                                # Find the suggestion or sync candidate and revert
                                undone = False

                                # Undo QC suggestion
                                sug_id = rev.get('suggestion_id')
                                if sug_id:
                                    for sug in suggestions:
                                        if sug['id'] == sug_id:
                                            sug['status'] = 'pending'
                                            sug['reviewer_edit'] = None
                                            undone = True
                                            break
                                    # Also remove the corresponding accepted rule
                                    st.session_state['qcd_accepted_rules'] = [
                                        r for r in accepted_rules
                                        if r.get('created_from_paragraph') != rev.get('paragraph_idx')
                                        or r.get('type') != rev.get('category')
                                    ]
                                    accepted_rules = st.session_state['qcd_accepted_rules']

                                # Undo sync candidate
                                cand_id = rev.get('candidate_id')
                                if cand_id:
                                    for sc in st.session_state.get('qcd_sync_candidates', []):
                                        if sc['id'] == cand_id:
                                            sc['status'] = 'pending'
                                            undone = True
                                            break

                                if undone:
                                    # Record undo as a revision
                                    revisions_updated = st.session_state.get('qcd_revisions', [])
                                    revisions_updated.append({
                                        'action': 'undo',
                                        'undone_revision': rev_idx,
                                        'paragraph_idx': pidx,
                                        'old_text': new_snip,
                                        'new_text': old_snip,
                                        'timestamp': now_gmt7().isoformat(),
                                    })
                                    st.session_state['qcd_revisions'] = revisions_updated

                                    qcd_save_session({
                                        'metadata': meta, 'suggestions': suggestions,
                                        'accepted_rules': accepted_rules,
                                        'vi_paragraphs': vi_paragraphs,
                                        'sync_candidates': st.session_state.get('qcd_sync_candidates', []),
                                        'revisions': revisions_updated,
                                    })
                                    st.success(f"⏪ Đã hoàn tác hành động #{rev_idx}!")
                                    st.rerun()
                                else:
                                    st.warning("Không tìm thấy mục để hoàn tác.")

        # ── Clear session ──
        st.divider()
        if st.button("🗑️ Xóa session QC Diff hiện tại", key="qcd_clear"):
            for k in list(st.session_state.keys()):
                if k.startswith('qcd_'):
                    del st.session_state[k]
            st.rerun()
