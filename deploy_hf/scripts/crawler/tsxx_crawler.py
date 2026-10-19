import os
import re
import json
import time
import random
import string
import urllib.parse
import base64
import hashlib
from typing import Dict, List, Optional, Tuple
import requests
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Đường dẫn thư mục dữ liệu
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
ACCOUNT_FILE = os.path.join(DATA_DIR, "tsxx_account.json")

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}

_tsxx_session: Optional[requests.Session] = None

def clean_slug(text: str) -> str:
    """Tạo slug an toàn từ chuỗi tiếng Việt hoặc tiêu đề"""
    t = text.lower()
    t = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', t)
    t = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', t)
    t = re.sub(r'[ìíịỉĩ]', 'i', t)
    t = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', t)
    t = re.sub(r'[ùúụủũưừứựửữ]', 'u', t)
    t = re.sub(r'[ỳýỵỷỹ]', 'y', t)
    t = re.sub(r'đ', 'd', t)
    t = re.sub(r'[^a-z0-9]+', '-', t)
    return t.strip('-')

def decrypt_cryptojs_aes(passphrase: str, raw_str: str) -> str:
    """
    Giải mã chuỗi JSON mã hóa AES CryptoJS chuẩn CBC + PBKDF2 SHA512.
    Được sử dụng trên hệ thống Tủ Sách Xinh Xinh (tsxx).
    """
    raw_str = raw_str.strip()
    if '\\"' in raw_str:
        raw_str = raw_str.replace('\\"', '"').replace('\\\\', '\\')
    
    obj = json.loads(raw_str)
    ciphertext = base64.b64decode(obj['ciphertext'])
    salt = bytes.fromhex(obj['salt'])
    iv = bytes.fromhex(obj['iv'])
    
    # CryptoJS keySize: 64/8 words = 8 words = 32 bytes (AES-256)
    key = hashlib.pbkdf2_hmac('sha512', passphrase.encode('utf-8'), salt, 999, dklen=32)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data.decode('utf-8')

def load_account_data() -> Dict:
    """Đọc thông tin tài khoản và cookies đã lưu"""
    if os.path.exists(ACCOUNT_FILE):
        try:
            with open(ACCOUNT_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_account_data(data: Dict):
    """Lưu thông tin tài khoản và cookies vào file"""
    os.makedirs(os.path.dirname(ACCOUNT_FILE), exist_ok=True)
    try:
        with open(ACCOUNT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"[tsxx] Lỗi lưu account data: {e}")

def auto_register_tsxx_account(session: requests.Session) -> Optional[Dict]:
    """
    Tự động đăng ký một tài khoản miễn phí trên tsxx4.online nếu chưa có tài khoản.
    Website tsxx hỗ trợ đăng ký mở không cần captcha.
    """
    try:
        reg_url = 'https://tsxx4.online/dang-ky/'
        r = session.get(reg_url, headers=DEFAULT_HEADERS, timeout=15)
        if r.status_code != 200:
            return None

        ur_params_match = re.search(r'var\s+user_registration_params\s*=\s*(\{.*?\});', r.text)
        if not ur_params_match:
            return None

        ur_params = json.loads(ur_params_match.group(1))
        security_nonce = ur_params.get('user_registration_form_data_save')
        ajax_url = ur_params.get('ajax_url')

        soup = BeautifulSoup(r.text, 'html.parser')
        nonce_el = soup.find('input', {'name': 'ur_frontend_form_nonce'})
        form_id_el = soup.find('input', {'name': 'ur-user-form-id'})

        if not nonce_el or not form_id_el:
            return None

        rand_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        username = f"cubari_{rand_suffix}"
        password = f"Cubari@{rand_suffix}#99"
        email = f"cubari_{rand_suffix}@gmail.com"

        form_data = [
            {"field_name": "user_login", "value": username},
            {"field_name": "user_pass", "value": password},
            {"field_name": "user_confirm_password", "value": password},
            {"field_name": "user_email", "value": email},
            {"field_name": "display_name", "value": username}
        ]

        payload = {
            "action": "user_registration_user_form_submit",
            "security": security_nonce,
            "form_data": json.dumps(form_data),
            "captchaResponse": "",
            "form_id": form_id_el.get('value'),
            "registration_language": "vi",
            "ur_frontend_form_nonce": nonce_el.get('value')
        }

        headers = dict(DEFAULT_HEADERS)
        headers['Referer'] = reg_url

        res = session.post(ajax_url, data=payload, headers=headers, timeout=20)
        data = res.json()
        if data.get('success'):
            print(f"[tsxx] Tự động tạo tài khoản thành công: {username}")
            account_data = {
                "username": username,
                "password": password,
                "email": email,
                "cookies": {}
            }
            save_account_data(account_data)
            return account_data
    except Exception as e:
        print(f"[tsxx] Lỗi khi tự động đăng ký tài khoản: {e}")
    return None

def safe_print(msg: str):
    try:
        print(msg)
    except Exception:
        try:
            print(msg.encode('ascii', errors='replace').decode('ascii'))
        except Exception:
            pass

def login_tsxx(session: requests.Session, username: str, password: str) -> bool:
    """Đăng nhập vào hệ thống tsxx4.online qua WordPress login form"""
    try:
        login_url = 'https://tsxx4.online/wp-login.php?itsec-hb-token=tsxx-login'
        login_data = {
            'log': username,
            'pwd': password,
            'rememberme': 'forever',
            'wp-submit': 'Đăng nhập',
            'redirect_to': 'https://tsxx4.online/'
        }
        headers = dict(DEFAULT_HEADERS)
        headers['Referer'] = 'https://tsxx4.online/dang-ky/'

        resp = session.post(login_url, data=login_data, headers=headers, allow_redirects=True, timeout=20)
        cookies = session.cookies.get_dict()
        if any('wordpress_logged_in_' in k for k in cookies.keys()):
            safe_print(f"[tsxx] Đăng nhập thành công với user {username}")
            acc_data = load_account_data()
            acc_data["username"] = username
            acc_data["password"] = password
            acc_data["cookies"] = cookies
            save_account_data(acc_data)
            return True
        else:
            safe_print("[tsxx] Đăng nhập thất bại (không tìm thấy cookie đăng nhập)")
            return False
    except Exception as e:
        safe_print(f"[tsxx] Lỗi đăng nhập: {e}")
        return False

def get_tsxx_session(force_refresh: bool = False) -> requests.Session:
    """Lấy hoặc khởi tạo requests.Session có xác thực trên tsxx"""
    global _tsxx_session
    if _tsxx_session is not None and not force_refresh:
        return _tsxx_session

    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)

    acc_data = load_account_data()
    username = acc_data.get("username", "").strip()
    password = acc_data.get("password", "").strip()
    saved_cookies = acc_data.get("cookies", {})

    # Kiểm tra xem cookie đã lưu có khớp với username hiện tại không
    cookie_user_match = True
    if saved_cookies and username:
        matched = False
        for k, v in saved_cookies.items():
            if 'wordpress_logged_in_' in k:
                val = urllib.parse.unquote(str(v))
                if val.startswith(f"{username}|"):
                    matched = True
                    break
        if not matched:
            cookie_user_match = False

    # 1. Thử dùng cookie đã lưu nếu khớp username
    if saved_cookies and cookie_user_match and not force_refresh:
        for k, v in saved_cookies.items():
            session.cookies.set(k, v, domain="tsxx4.online")
        _tsxx_session = session
        return _tsxx_session

    # 2. Thử đăng nhập bằng tài khoản đã lưu
    if username and password:
        if login_tsxx(session, username, password):
            _tsxx_session = session
            return _tsxx_session

    # 3. Tự động đăng ký tài khoản mới và đăng nhập
    new_acc = auto_register_tsxx_account(session)
    if new_acc:
        if login_tsxx(session, new_acc["username"], new_acc["password"]):
            _tsxx_session = session
            return _tsxx_session

    _tsxx_session = session
    return _tsxx_session

def get_tsxx_manga_info(url: str) -> Dict:
    """
    Bóc tách thông tin truyện và danh sách chapters từ URL Tủ Sách Xinh Xinh (tsxx4.online).
    Hỗ trợ cả link tổng quan /truyen-tranh/.../ và link chapter trực tiếp.
    """
    session = get_tsxx_session()
    headers = dict(DEFAULT_HEADERS)
    headers['Referer'] = 'https://tsxx4.online/'

    # Nếu người dùng đưa vào link chapter, chuyển hướng sang trang tổng quan truyện
    overview_url = url
    if '/truyen-tranh/' not in url:
        r_temp = session.get(url, headers=headers, timeout=15)
        if r_temp.status_code == 200:
            soup_temp = BeautifulSoup(r_temp.text, 'html.parser')
            for a in soup_temp.find_all('a'):
                href = a.get('href') or ''
                if '/truyen-tranh/' in href:
                    overview_url = href
                    break

    res = session.get(overview_url, headers=headers, timeout=20)
    if res.status_code != 200:
        raise Exception(f"Không thể truy cập trang truyện tsxx (HTTP {res.status_code})")

    soup = BeautifulSoup(res.text, 'html.parser')

    # 1. Title
    title = "Unknown Manga"
    h2_title = soup.find('h2', class_='info-title')
    if h2_title and h2_title.text.strip():
        title = h2_title.text.strip()
    else:
        title_tag = soup.find('title')
        if title_tag:
            title = re.sub(r'\s*[-|–]\s*.*?(truyện tranh|tủ sách xinh xinh|tsxx).*?$', '', title_tag.text.strip(), flags=re.IGNORECASE).strip()

    # 2. Cover image
    cover_url = ""
    if h2_title:
        parent_row = h2_title.find_parent('div', class_='row') or h2_title.find_parent('div')
        if parent_row:
            cover_img = parent_row.find('img')
            if cover_img:
                cover_url = cover_img.get('data-lazy-src') or cover_img.get('data-src') or cover_img.get('src') or ''

    if not cover_url or cover_url.startswith('data:image'):
        og_img = soup.find('meta', property='og:image')
        if og_img and og_img.get('content'):
            cover_url = og_img.get('content')

    # 3. Chapter list
    chapters = []
    seen_urls = set()

    # Tìm bảng chương .chapter-table
    table = soup.find(class_='chapter-table') or soup.find(class_='table-wrapper')
    candidate_links = table.find_all('a') if table else soup.find_all('a')

    for a in candidate_links:
        href = a.get('href', '').strip()
        if not href or href in seen_urls:
            continue
        if '#' in href or 'comment' in href or '/truyen-tranh/' in href:
            continue

        # Link chapter trên tsxx có dạng: https://tsxx4.online/<slug>-chap-<num>/ hoặc link kết thúc bằng slug truyện (Chap 1)
        raw_text = a.text.strip()
        has_chap_num = re.search(r'chap(?:ter)?\s*\d+|chương\s*\d+', raw_text, re.IGNORECASE)
        has_chap_href = re.search(r'chap-\d+|chapter-\d+|-\d+/?$', href)
        if not (has_chap_num or has_chap_href):
            continue

        seen_urls.add(href)

        # Làm sạch text lặp lại trong bảng chương
        m_chap = re.search(r'(Chap(?:ter)?\s*\d+(?:\.\d+)?)', raw_text, re.IGNORECASE)
        if m_chap:
            ch_title = m_chap.group(1).title()
        else:
            lines = [l.strip() for l in raw_text.split('\n') if l.strip()]
            ch_title = lines[0] if lines else "Chapter"

        ch_slug = clean_slug(ch_title)
        chapters.append({
            'title': ch_title,
            'url': href,
            'slug': ch_slug
        })

    # Đảo ngược danh sách nếu trang hiển thị chương mới nhất lên đầu (đưa về chap 1 -> chap N)
    if len(chapters) > 1:
        num_first = re.search(r'\d+', chapters[0]['title'])
        num_last = re.search(r'\d+', chapters[-1]['title'])
        if num_first and num_last and int(num_first.group(0)) > int(num_last.group(0)):
            chapters.reverse()

    slug = clean_slug(title)

    return {
        'title': title,
        'slug': slug,
        'url': overview_url,
        'cover': cover_url,
        'chapters': chapters,
        'total_chapters': len(chapters),
        'source': 'tsxx'
    }

def get_tsxx_chapter_images(chapter_url: str) -> Dict:
    """
    Bóc tách danh sách ảnh của chapter từ URL tsxx4.online.
    Tự động giải mã nội dung bảo vệ (CryptoJS AES) và sinh link ảnh full chất lượng.
    """
    session = get_tsxx_session()
    headers = dict(DEFAULT_HEADERS)
    headers['Referer'] = 'https://tsxx4.online/'

    r = session.get(chapter_url, headers=headers, timeout=20)
    if r.status_code != 200:
        raise Exception(f"Không thể truy cập chapter tsxx (HTTP {r.status_code})")

    # Kiểm tra xem có bị yêu cầu đăng nhập không
    if "Bạn cần đăng nhập để xem nội dung chương này" in r.text or "var htmlContent = '';" in r.text:
        # Thử refresh session đăng nhập lại 1 lần
        session = get_tsxx_session(force_refresh=True)
        r = session.get(chapter_url, headers=headers, timeout=20)

    # 1. Trích xuất htmlContent
    idx = r.text.find('var htmlContent = ')
    if idx == -1:
        raise Exception("Không tìm thấy dữ liệu ảnh chương trên trang tsxx.")

    sub = r.text[idx + len('var htmlContent = '):]
    if not sub or sub.startswith("''") or sub.startswith('""'):
        raise Exception("Chương này đang bị khóa. Cần tài khoản thành viên tsxx để mở khóa nội dung.")

    quote_char = sub[0]
    end_idx = sub.find(f"{quote_char};", 1)
    if end_idx == -1:
        raise Exception("Lỗi cấu trúc dữ liệu mã hóa htmlContent của tsxx.")

    encrypted_json_str = sub[1:end_idx]

    # 2. Tìm passphrase và token thay thế trong script
    passphrase = 'qX3xRLguhD2Z9f7sWJ'
    token1, token2, token3 = 'qX3xRL', 'guhD2Z', '9f7sWJ'

    m_decrypt_call = re.search(r"CryptoJSAesDecrypt\s*\(\s*['\"]([^'\"]+)['\"]\s*\+\s*['\"]([^'\"]+)['\"]\s*\+\s*['\"]([^'\"]+)['\"]", r.text)
    if m_decrypt_call:
        token1, token2, token3 = m_decrypt_call.group(1), m_decrypt_call.group(2), m_decrypt_call.group(3)
        passphrase = token1 + token2 + token3

    # 3. Giải mã HTML
    decrypted_html = decrypt_cryptojs_aes(passphrase, encrypted_json_str)
    soup = BeautifulSoup(decrypted_html, 'html.parser')

    # 4. Thu thập toàn bộ link ảnh thực tế
    images = []
    attr_token = f"data-{token1.lower()}"

    for img in soup.find_all('img'):
        img_url = ""
        # Kiểm tra attribute chứa link mã hóa
        for attr_k, attr_v in img.attrs.items():
            if token2 in str(attr_v) or token3 in str(attr_v) or attr_k == attr_token:
                img_url = str(attr_v).replace(token1, '.').replace(token2, ':').replace(token3, '/')
                break

        if not img_url:
            src = img.get('data-src') or img.get('src') or ''
            if src and not src.startswith('data:image'):
                img_url = src

        if img_url and img_url.startswith('http'):
            images.append(img_url)

    # 5. Tiêu đề chapter từ trang gốc
    page_soup = BeautifulSoup(r.text, 'html.parser')
    title_text = "Chapter"
    title_tag = page_soup.find('title')
    if title_tag:
        raw_title = title_tag.text.strip()
        m_ch = re.search(r'([^-–|]+[-–|]\s*chap(?:ter)?\s*\d+)', raw_title, re.IGNORECASE)
        if m_ch:
            title_text = m_ch.group(1).strip()
        else:
            title_text = re.sub(r'\s*[-–|]\s*.*?(tủ sách xinh xinh|tsxx).*?$', '', raw_title, flags=re.IGNORECASE).strip()
    elif page_soup.find('h1'):
        title_text = page_soup.find('h1').text.strip()

    return {
        'url': chapter_url,
        'title': title_text,
        'images': images,
        'total': len(images)
    }
