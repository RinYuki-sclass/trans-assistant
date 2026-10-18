import os
import re
import json
import base64
import time
from typing import List, Dict, Optional, Callable
from urllib.parse import urlparse
import cloudscraper
from bs4 import BeautifulSoup
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

DEFAULT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
}

def get_scraper():
    return cloudscraper.create_scraper(browser={
        'browser': 'chrome',
        'platform': 'windows',
        'desktop': True
    })

def clean_slug(text: str) -> str:
    slug = re.sub(r'[\\/*?:"<>|]', "", text)
    slug = re.sub(r'\s+', '-', slug.strip())
    return slug.lower()

def decrypt_init_manga_chapter(html: str) -> List[str]:
    """
    Giải mã AES-CBC nội dung chương bảo vệ bằng InitManga trên haccbl.xyz
    """
    m_data = re.search(r'var InitMangaData\s*=\s*(\{.*?\});', html)
    m_enc = re.search(r'var InitMangaEncryptedChapter\s*=\s*(\{.*?\});', html)

    if not m_data or not m_enc:
        return []

    try:
        data_json = json.loads(m_data.group(1))
        enc_json = json.loads(m_enc.group(1))

        decryption_key_b64 = data_json.get('decryption_key', '')
        if not decryption_key_b64:
            return []

        key_str = base64.b64decode(decryption_key_b64).decode('utf-8', errors='ignore')
        salt = bytes.fromhex(enc_json['salt'])
        iv = bytes.fromhex(enc_json['iv'])
        ciphertext = base64.b64decode(enc_json['ciphertext'])

        # PBKDF2 HMAC SHA-512, 999 iterations, keySize 8 words = 32 bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=999
        )
        derived_key = kdf.derive(key_str.encode('utf-8'))

        cipher = Cipher(algorithms.AES(derived_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_plain = decryptor.update(ciphertext) + decryptor.finalize()

        pad_len = padded_plain[-1]
        if pad_len < 1 or pad_len > 16:
            plain = padded_plain.decode('utf-8', errors='ignore')
        else:
            plain = padded_plain[:-pad_len].decode('utf-8', errors='ignore')

        soup = BeautifulSoup(plain, 'html.parser')
        image_urls = []
        for img in soup.find_all('img'):
            src = img.get('data-original-src') or img.get('data-mce-src') or img.get('src')
            if src and not src.startswith('data:image'):
                src = src.strip()
                if src not in image_urls:
                    image_urls.append(src)

        return image_urls
    except Exception as e:
        print(f"[haccbl] Lỗi giải mã: {e}")
        return []

def get_haccbl_chapter_images(chapter_url: str) -> Dict:
    """
    Lấy danh sách link ảnh của 1 chapter trên haccbl.xyz
    """
    scraper = get_scraper()
    headers = dict(DEFAULT_HEADERS)
    headers['Referer'] = chapter_url

    res = scraper.get(chapter_url, headers=headers, timeout=20)
    if res.status_code != 200:
        raise Exception(f"Không thể truy cập chapter (HTTP {res.status_code})")

    images = decrypt_init_manga_chapter(res.text)

    # Nếu không phải InitManga encrypted, fallback tìm img thông thường
    if not images:
        soup = BeautifulSoup(res.text, 'html.parser')
        for img in soup.select('.reading-content img, .entry-content img, .wp-manga-chapter-img'):
            src = img.get('data-src') or img.get('data-lazy-src') or img.get('src')
            if src and not src.startswith('data:image') and src not in images:
                images.append(src.strip())

    # Lấy tiêu đề chapter & truyện
    soup = BeautifulSoup(res.text, 'html.parser')
    page_title = soup.find('title')
    title_text = page_title.text.strip() if page_title else "Chapter"

    return {
        'url': chapter_url,
        'title': title_text,
        'images': images,
        'total': len(images)
    }

def get_haccbl_manga_info(manga_url: str) -> Dict:
    """
    Lấy thông tin bộ truyện & danh sách tất cả các chapter trên haccbl.xyz
    """
    scraper = get_scraper()
    headers = dict(DEFAULT_HEADERS)
    res = scraper.get(manga_url, headers=headers, timeout=20)
    if res.status_code != 200:
        raise Exception(f"Không thể truy cập trang truyện (HTTP {res.status_code})")

    soup = BeautifulSoup(res.text, 'html.parser')

    # Tên truyện
    title_el = soup.find('h1') or soup.find('title')
    title = title_el.text.strip() if title_el else "Unknown Manga"

    # Ảnh bìa
    cover_url = ""
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src') or ''
        classes = img.get('class') or []
        if 'image-3-4' in classes and src and 'avatar' not in src:
            cover_url = src
            break

    # Lấy danh sách chapter
    parsed = urlparse(manga_url)
    slug = parsed.path.strip('/').split('/')[-1]

    raw_chapters = []
    # Tìm tất cả link có dạng /manga/{slug}/chapter-x/
    pattern = re.compile(rf'/{re.escape(slug)}/chapter-\d+/?')
    for a in soup.find_all('a', href=pattern):
        href = a['href'].split('#')[0].rstrip('/') + '/'
        ch_text = a.get_text(separator=' ', strip=True)
        ch_text = re.sub(r'\s+', ' ', ch_text)
        if href and not ch_text.lower().startswith('từ đầu') and not ch_text.lower().startswith('đọc'):
            # Lấy số chapter
            m_num = re.search(r'chapter-(\d+)', href)
            num = int(m_num.group(1)) if m_num else 0
            raw_chapters.append({
                'title': ch_text,
                'url': href,
                'number': num,
                'slug': f"chapter-{num}" if num else href.split('/')[-2]
            })

    # Khử trùng lặp và sắp xếp theo thứ tự chương
    seen_urls = set()
    chapters = []
    for ch in sorted(raw_chapters, key=lambda x: x['number']):
        if ch['url'] not in seen_urls:
            seen_urls.add(ch['url'])
            chapters.append(ch)

    return {
        'title': title,
        'slug': slug,
        'url': manga_url,
        'cover': cover_url,
        'chapters': chapters,
        'total_chapters': len(chapters)
    }

def download_chapter_images(
    images: List[str],
    save_dir: str,
    referer: str = "",
    progress_callback: Optional[Callable[[int, int, str], None]] = None
) -> List[str]:
    """
    Tải danh sách ảnh của chapter về thư mục local
    """
    os.makedirs(save_dir, exist_ok=True)
    scraper = get_scraper()
    headers = dict(DEFAULT_HEADERS)
    if referer:
        headers['Referer'] = referer

    saved_files = []
    total = len(images)

    import io
    from PIL import Image

    slice_counter = 0
    for idx, img_url in enumerate(images):
        retry = 3
        downloaded_bytes = None
        while retry > 0 and not downloaded_bytes:
            try:
                res = scraper.get(img_url, headers=headers, timeout=25)
                if res.status_code == 200 and len(res.content) > 500:
                    downloaded_bytes = res.content
                else:
                    retry -= 1
                    time.sleep(1)
            except Exception:
                retry -= 1
                time.sleep(1)

        if not downloaded_bytes:
            continue

        # Nén ảnh tối ưu: Tự động cắt các ảnh dài (>3000px) thành các lát nhỏ và lưu WebP
        try:
            im = Image.open(io.BytesIO(downloaded_bytes))
            w, h = im.size
            if h > 3000:
                top = 0
                while top < h:
                    bottom = min(top + 3000, h)
                    slice_im = im.crop((0, top, w, bottom))
                    slice_counter += 1
                    filename = f"{slice_counter:03d}.webp"
                    filepath = os.path.join(save_dir, filename)
                    if slice_im.mode not in ("RGB", "RGBA"):
                        slice_im = slice_im.convert("RGB")
                    slice_im.save(filepath, format="WEBP", quality=80, method=4)
                    saved_files.append(filepath)
                    top = bottom
            else:
                slice_counter += 1
                filename = f"{slice_counter:03d}.webp"
                filepath = os.path.join(save_dir, filename)
                if im.mode not in ("RGB", "RGBA"):
                    im = im.convert("RGB")
                im.save(filepath, format="WEBP", quality=80, method=4)
                saved_files.append(filepath)
        except Exception:
            # Fallback nếu PIL gặp lỗi định dạng đặc thù
            slice_counter += 1
            ext = ".jpg"
            if ".png" in img_url.lower():
                ext = ".png"
            elif ".webp" in img_url.lower():
                ext = ".webp"
            elif ".avif" in img_url.lower():
                ext = ".avif"
            filename = f"{slice_counter:03d}{ext}"
            filepath = os.path.join(save_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(downloaded_bytes)
            saved_files.append(filepath)

        if progress_callback:
            progress_callback(idx + 1, total, filename)

    return saved_files
