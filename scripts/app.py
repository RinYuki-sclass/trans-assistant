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
load_dotenv(os.path.join(BASE_DIR, '.env'))

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
        background: linear-gradient(135deg, #4f5b93 0%, #685b8c 100%);
        padding: 1.5rem 2rem; border-radius: 12px; margin-bottom: 1.5rem; color: #e5e9f0;
    }
    .app-header h1 { margin: 0; font-size: 1.8rem; font-weight: 700; }
    .app-header p { margin: 0.3rem 0 0; opacity: 0.85; font-size: 0.95rem; }
    .diff-container {
        font-family: 'Consolas', 'Courier New', monospace; font-size: 13px;
        line-height: 1.6; border-radius: 10px; overflow: hidden;
        border: 1px solid #414559; max-height: 600px; overflow-y: auto;
    }
    .diff-add { background: rgba(81,207,102,0.12); color: #51cf66; padding: 3px 12px; border-left: 3px solid #51cf66; }
    .diff-del { background: rgba(255,107,107,0.12); color: #ff6b6b; padding: 3px 12px; border-left: 3px solid #ff6b6b; }
    .diff-info { background: rgba(140,170,238,0.1); color: #8caaee; padding: 3px 12px; font-weight: 600; }
    .diff-ctx { color: #a5adce; padding: 3px 12px; }
    .glossary-box {
        background: #292c3c; border: 1px solid #414559; border-radius: 10px;
        padding: 1rem; max-height: 500px; overflow-y: auto;
    }
    /* Side-by-side comparison */
    .sbs-table { width: 100%; border-collapse: collapse; font-size: 14px; line-height: 1.7; }
    .sbs-table th {
        background: linear-gradient(135deg, #51576d, #414559); color: #c6d0f5;
        padding: 10px 14px; text-align: left; position: sticky; top: 0; z-index: 1;
    }
    .sbs-table td {
        padding: 8px 14px; border-bottom: 1px solid #414559;
        vertical-align: top; word-wrap: break-word;
    }
    .sbs-table tr:hover td { background: rgba(140,170,238,0.08); }
    .sbs-num { color: #737994; font-size: 12px; text-align: center; min-width: 35px; user-select: none; }
    .sbs-src { color: #a5adce; max-width: 45%; }
    .sbs-vi { color: #e5c890; max-width: 45%; }
    .sbs-empty { color: #51576d; font-style: italic; }
    .sbs-wrap {
        max-height: 650px; overflow-y: auto; border-radius: 10px;
        border: 1px solid #414559; background: #232634;
    }
    .term-hl {
        background-color: rgba(229, 200, 144, 0.15);
        color: #e5c890;
        border-bottom: 1px dashed #e5c890;
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
        background: #1a1b26; /* Dark theme background */
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 1px solid #414559;
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
    /* Ngăn chặn chớp/mờ nháy khi click trên Streamlit (vô hiệu hóa Stale Dimming) */
    [data-testid="stApp"] [data-stale="true"],
    [data-stale="true"],
    iframe {
        opacity: 1 !important;
        filter: none !important;
        transition: none !important;
    }
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
    "gemini-2.5-flash": 1500,     
    "gemini-2.5-pro": 50,         
    "gemini-2.0-flash": 1500,     
    "gemini-3.1-flash-lite-preview": 2000, 
    "gemini-2.5-flash-lite": 2000, # Dự phòng cấp 1
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

def generate_with_retry(model, contents, system_instruction, status_w=None, retries=8):
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
        temperature=0.3,
        safety_settings=safety_settings
    )
    
    # Chuỗi dự phòng thông minh
    fallback_1 = "gemini-2.5-flash-lite"
    fallback_2 = "gemini-2.0-flash"
    
    if rotator and rotator.is_exhausted(model):
        if model == "gemini-3.1-flash-lite-preview":
            if status_w: status_w.warning(f"⚠️ `{model}` hết lượt! Chuyển sang `{fallback_1}`.")
            model = fallback_1
        elif model == fallback_1:
            if status_w: status_w.warning(f"⚠️ `{model}` cũng hết lượt! Chuyển sang `{fallback_2}`.")
            model = fallback_2

    for i in range(retries):
        if rotator:
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

def optimize_image_for_api(img, max_dimension=2048):
    """
    Giảm kích thước ảnh và convert sang định dạng tối ưu để tránh lỗi payload/rate limit
    nhưng vẫn giữ độ nét tương đối cho OCR.
    """
    import PIL.Image
    import io
    
    # Chỉ xử lý nếu ảnh tồn tại và là loại hình ảnh
    if not isinstance(img, PIL.Image.Image):
        return img
        
    # Chuyển đổi sang RGB nếu đang ở định dạng có alpha (RGBA/P)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
        
    width, height = img.size
    
    # Resize nếu kích thước vượt ngưỡng (Manhwa dài thì height thường rất lớn)
    if width > max_dimension or height > max_dimension:
        # Tính tỷ lệ thu nhỏ
        ratio = min(max_dimension / width, max_dimension / height)
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        # Sử dụng LANCZOS để giữ nét chữ tốt nhất có thể
        img = img.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)
    
    # Save qua bộ nhớ đệm dạng thư viện tối ưu BytesIO thay vì truyền thẳng object nặng nề
    img_byte_arr = io.BytesIO()
    # Lưu dưới chuẩn chất lượng JPEG vừa phải để qua cửa Rate Limit (payload limit)
    img.save(img_byte_arr, format='JPEG', quality=85)
    
    # Load lại ảnh nhẹ từ bytes
    img_byte_arr.seek(0)
    optimized_img = PIL.Image.open(img_byte_arr)
    return optimized_img

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

    # User-facing Model Selection & RPD guide
    model_guide = {
        "gemini-3-flash-preview": "📝 Dịch Thuật",
        "gemini-2.5-flash": "🔍 QC Review",
        "gemini-2.5-flash-lite": "🎨 Truyện Tranh",
        "gemini-3.1-flash-lite-preview": "🛡️ Trợ thủ Fallback (500 RPD)"
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
                            color = "#ff6b6b"   # đỏ
                        elif pct >= 0.75:
                            color = "#f0a500"   # cam
                        else:
                            color = "#51cf66"   # xanh
                        st.markdown(
                            f"""
                            <div style='margin-bottom:6px'>
                            <div style='font-size:11px;color:#a5adce;display:flex;justify-content:space-between'>
                                <span>{label}</span><span style='color:{color}'>{used:,} / {lim:,}</span></div>
                            <div style='background:#292c3c;border-radius:4px;height:4px;overflow:hidden'>
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
                lines = f.readlines()
            st.caption(f"{len(lines)} sự kiện")
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
MENU_ITEMS = ["🏠 Hướng dẫn", "📝 Dịch Thuật", "🔍 QC Review", "📊 So Sánh", "📖 Đối Chiếu", "🎨 Truyện Tranh", "📥 Tải Truyện", "📚 Glossary", "✂️ Cắt Ảnh"]

tabs = st.tabs(MENU_ITEMS)
current_menu = None # Not used


# Log page visit (once per session)
if 'session_logged' not in st.session_state:
    st.session_state['session_logged'] = True
    log_action("Truy cập", "Mở ứng dụng")

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
                    "Output ONLY the translation."
                )
                prompt_d = f"--- PREVIOUS CONTEXT (For reference only) ---\n{prev_ec}\n\n--- TRANSLATE THIS ---\n{ec}" if prev_ec else ec
                draft = generate_with_retry(target_model, prompt_d, sys_d, None)
            else:
                draft = "\n\n".join(draft_p[s:e])

            sys_r = (
                "You are a strict novel editor. Refine Vietnamese translation comparing EN and KR sources. "
                "RULES: 1.Output ONLY final Vietnamese. 2.Follow source dialogue structure. "
                "3.Keep suffixes from EN source. 4.Keep ahjussi,-ssi,-nim,-gun. "
                "5.Follow Glossary. 6.No creative rewriting."
            )
            
            context_str = f"--- PREVIOUS CONTEXT (DO NOT TRANSLATE) ---\nEN: {prev_ec}\nKR: {prev_kc}\n\n" if prev_ec else ""
            pr = f"{context_str}--- GLOSSARY ---\n{glossary}\n\n--- NOTES ---\n{notes}\n\n--- EN ---\n{ec}\n\n--- KR ---\n{kc}\n\n--- DRAFT ---\n{draft}"
            refined = generate_with_retry(target_model, pr, sys_r, None)

            lines = refined.strip().split('\n')
            clean = [l for l in lines if not l.startswith(('*', 'Đây là', 'Bản dịch', 'Tuyệt vời', 'Đã sửa'))]
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

        if st.button("🔍 Chạy QC", type="primary"):
            target_model = "gemini-2.5-pro"
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
                st.info("🤖 Model: gemini-3.1-flash-lite (Thế hệ 3 Mới nhất)")
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
                target_model = "gemini-3.1-flash-lite-preview"
                log_action("Truyện Tranh", f"Ảnh: {len(uploaded_files)} | Session: {final_sess_name}")
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
                # --- TẠO THƯ MỤC VÀ LƯU ẢNH TRƯỚC ĐỂ BACKUP ---
                sess_dir = os.path.join(mh_hist_dir, final_sess_name)
                sess_img_dir = os.path.join(sess_dir, 'images')
                os.makedirs(sess_img_dir, exist_ok=True)
                
                for fo in files_to_process:
                    save_path = os.path.join(sess_img_dir, fo.name)
                    if not os.path.exists(save_path):
                        fo.img.save(save_path, quality=90)
                
                glossary = load_file(PATHS['glossary'])
                notes = load_file(PATHS['notes'])
                
                status = st.status(f"🚀 Đang xử lý {len(files_to_process)} ảnh/dải...", expanded=True)
                bar = st.progress(0)
                
                all_results = []
                t0 = time.time()
                consecutive_errors = 0
                
                for i, file_obj in enumerate(files_to_process):
                    fname = file_obj.name
                    bar.progress(i / len(files_to_process), f"Đang quét ảnh {i+1}/{len(files_to_process)}...")
                    status.write(f"🖼️ Đang quét ảnh: `{fname}`")
                    
                    try:
                        # Gửi prompt và ảnh
                        # Kiểm tra xem có lấy được file không
                        if hasattr(file_obj, 'img'):
                            raw_img = file_obj.img
                        else:
                            raw_img = PIL.Image.open(file_obj).convert('RGB')
                        
                        # Tối ưu kích thước và dung lượng ảnh trước khi gửi
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
                        res = generate_with_retry(target_model, contents, sys_m, status)
                        
                        if res and res.strip():
                            all_results.append(f"📄 ẢNH: {fname}\n\n{res}\n")
                            consecutive_errors = 0
                            status.write(f"   ✅ Xong `{fname}`")
                            # Incremental progress save
                            save_file(os.path.join(sess_dir, "script.txt"), "\n\n".join(all_results))
                            time.sleep(15) 
                        else:
                            consecutive_errors += 1
                            all_results.append(f"📄 ẢNH: {fname}\n\n[LỖI HOẶC HẾT TOKEN]\n")
                            status.write(f"   ⚠️ Thất bại `{fname}`")
                            save_file(os.path.join(sess_dir, "script.txt"), "\n\n".join(all_results))
                            
                            if consecutive_errors >= 2:
                                status.error("🚨 Quá trình dịch liên tục thất bại do Rate Limit hoặc lỗi API! Dừng sớm để bảo toàn dữ liệu.")
                                break
                    except Exception as e:
                        consecutive_errors += 1
                        all_results.append(f"📄 ẢNH: {fname}\n\n[LỖI HỆ THỐNG: {e}]\n")
                        status.write(f"   ❌ Lỗi `{fname}`: {e}")
                        save_file(os.path.join(sess_dir, "script.txt"), "\n\n".join(all_results))
                        
                        if consecutive_errors >= 2:
                            status.error("🚨 Quá trình dịch liên tục thất bại do lỗi phần mềm! Dừng sớm để bảo toàn dữ liệu.")
                            break
                        
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
                                    # Đặt Doc trực tiếp trong folder chapter, tên "{chapter}"
                                    result = create_google_doc(
                                        title=f"{sess_choice}",
                                        content=reconstructed_script,
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
                    
                    # Lưu thông tin cắt vào session để dùng cho upload Drive
                    st.session_state['_cut_out_dir'] = out_dir
                    st.session_state['_cut_base_name'] = base_name
                    st.session_state['_cut_part_count'] = part_num - 1
                    
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
                    
            # --- GOOGLE DRIVE UPLOAD ---
            if '_cut_out_dir' in st.session_state and os.path.exists(st.session_state.get('_cut_out_dir', '')):
                try:
                    from scripts.google_helper import is_configured as _gc_check
                    _has_gdrive_cut = _gc_check()
                except ImportError:
                    try:
                        from google_helper import is_configured as _gc_check
                        _has_gdrive_cut = _gc_check()
                    except Exception:
                        _has_gdrive_cut = False

                if _has_gdrive_cut:
                    st.divider()
                    st.markdown("#### ☁️ Upload lên Google Drive")
                    cut_dir = st.session_state['_cut_out_dir']
                    cut_base = st.session_state.get('_cut_base_name', 'cut')
                    cut_count = st.session_state.get('_cut_part_count', 0)
                    st.caption(f"📂 `{cut_base}` — {cut_count} mảnh đã cắt. Sẽ tạo folder `chunks/page_01/`, `page_02/`... trong folder chapter.")
                    
                    try:
                        from scripts.google_helper import parse_folder_id_from_url as _parse_fid_cut
                    except ImportError:
                        from google_helper import parse_folder_id_from_url as _parse_fid_cut
                    
                    cut_drive_folder = st.text_input(
                        "📂 Folder Drive của Chapter (VD: folder '156'):",
                        placeholder="Paste link folder chapter trên Drive...",
                        key="cut_drive_folder_input",
                        help="Ảnh sẽ được upload vào sub-folder 'chunks/page_XX/' bên trong folder này"
                    )
                    
                    if st.button("☁️ Upload lên Google Drive", type="primary", use_container_width=True, key="cut_upload_drive"):
                        try:
                            from scripts.google_helper import get_root_folder_id, create_subfolder, upload_file_to_drive, get_folder_url
                        except ImportError:
                            from google_helper import get_root_folder_id, create_subfolder, upload_file_to_drive, get_folder_url
                        
                        try:
                            if cut_drive_folder.strip():
                                chapter_fid = _parse_fid_cut(cut_drive_folder)
                            else:
                                chapter_fid = get_root_folder_id()
                            # Tạo folder 'chunks' bên trong folder chapter
                            chunks_fid = create_subfolder(chapter_fid, "chunks")
                            
                            # Lấy danh sách file đã cắt
                            cut_files = sorted([f for f in os.listdir(cut_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])
                            
                            bar_up = st.progress(0, "Đang upload...")
                            status_up = st.status(f"☁️ Upload {len(cut_files)} mảnh lên Drive...", expanded=True)
                            
                            for idx, fname in enumerate(cut_files):
                                page_num = idx + 1
                                page_folder_name = f"page_{page_num:02d}"
                                
                                # Tạo sub-folder chunks/page_XX
                                page_fid = create_subfolder(chunks_fid, page_folder_name)
                                
                                # Upload ảnh
                                local_path = os.path.join(cut_dir, fname)
                                upload_file_to_drive(local_path, page_fid, fname)
                                
                                bar_up.progress((idx + 1) / len(cut_files), f"Đã upload {idx+1}/{len(cut_files)}")
                                status_up.write(f"  ✅ `chunks/{page_folder_name}/{fname}`")
                            
                            bar_up.progress(1.0, "✅ Upload hoàn tất!")
                            status_up.update(label="✅ Upload Google Drive hoàn tất!", state="complete")
                            
                            folder_url = get_folder_url(chapter_fid)
                            st.success(f"🎉 Đã upload thành công {len(cut_files)} mảnh!")
                            st.markdown(f"🔗 [Mở folder trên Google Drive]({folder_url})")
                            log_action("Drive Upload", f"Upload {len(cut_files)} mảnh: {cut_base}")
                            st.balloons()
                            
                        except Exception as e:
                            st.error(f"❌ Lỗi upload Drive: {e}")
            
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
