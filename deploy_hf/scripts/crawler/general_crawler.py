import os
import re
import json
import urllib.parse
from typing import Dict, List, Optional
import requests
from crawler.haccbl_crawler import get_haccbl_manga_info, get_haccbl_chapter_images, download_chapter_images
from crawler.tsxx_crawler import get_tsxx_manga_info, get_tsxx_chapter_images

def resolve_cubari_url(url: str) -> Optional[Dict]:
    """
    Hỗ trợ đọc link Cubari (gist, imgur, mangadex)
    Ví dụ: https://cubari.moe/read/gist/cmF3L2dpc3Q...
    """
    if "cubari.moe" not in url:
        return None

    # Phân tích cú pháp Cubari URL
    # /read/gist/<b64_url>/
    # /read/imgur/<album_id>/
    # /read/mangadex/<manga_id>/
    parts = [p for p in urllib.parse.urlparse(url).path.split('/') if p]
    if len(parts) >= 3 and parts[0] == 'read':
        source_type = parts[1]
        source_id = parts[2]
        
        if source_type == 'gist':
            try:
                raw_url = urllib.parse.unquote(source_id)
                if not raw_url.startswith('http'):
                    import base64
                    raw_url = base64.b64decode(source_id).decode('utf-8')
                res = requests.get(raw_url, timeout=15)
                if res.status_code == 200:
                    data = res.json()
                    title = data.get('title', 'Cubari Manga')
                    chapters = []
                    for ch_num, ch_data in sorted(data.get('chapters', {}).items(), key=lambda x: float(x[0]) if x[0].replace('.','',1).isdigit() else 999):
                        chapters.append({
                            'title': ch_data.get('title', f"Chapter {ch_num}"),
                            'number': float(ch_num) if ch_num.replace('.','',1).isdigit() else 0,
                            'slug': f"chapter-{ch_num}",
                            'url': f"cubari://gist/{source_id}/{ch_num}",
                            'groups': ch_data.get('groups', {})
                        })
                    return {
                        'title': title,
                        'slug': re.sub(r'\W+', '-', title.lower()).strip('-'),
                        'url': url,
                        'cover': data.get('cover', ''),
                        'chapters': chapters,
                        'total_chapters': len(chapters),
                        'raw_data': data
                    }
            except Exception as e:
                print(f"[Cubari] Lỗi đọc gist: {e}")

    return None

def detect_and_get_manga_info(url: str) -> Dict:
    """
    Nhận diện URL và lấy thông tin truyện + danh sách chapters
    """
    url = url.strip()
    
    # 1. Haccbl
    if "haccbl.xyz" in url:
        if "/chapter-" in url:
            # Người dùng dán thẳng link chapter -> tạo info cho chapter này và lấy link truyện gốc
            m_manga = re.match(r'(https?://[^/]+/manga/[^/]+/)', url)
            if m_manga:
                manga_main_url = m_manga.group(1)
                return get_haccbl_manga_info(manga_main_url)
        return get_haccbl_manga_info(url)

    # 2. tsxx (Tủ Sách Xinh Xinh)
    if "tsxx" in url or "tusachxinhxinh" in url:
        return get_tsxx_manga_info(url)

    # 3. Cubari
    cubari_info = resolve_cubari_url(url)
    if cubari_info:
        return cubari_info

    raise Exception("Chưa hỗ trợ định dạng URL này. Vui lòng sử dụng URL từ haccbl.xyz hoặc Cubari.")

def detect_and_get_chapter_images(url: str, context_data: Optional[Dict] = None) -> Dict:
    """
    Lấy danh sách ảnh của chapter từ URL
    """
    url = url.strip()

    # 1. Haccbl
    if "haccbl.xyz" in url:
        return get_haccbl_chapter_images(url)

    # 2. tsxx (Tủ Sách Xinh Xinh)
    if "tsxx" in url or "tusachxinhxinh" in url:
        return get_tsxx_chapter_images(url)

    # 3. Cubari virtual url
    if url.startswith("cubari://"):
        if context_data and 'raw_data' in context_data:
            parts = url.split('/')
            ch_num = parts[-1]
            ch_data = context_data['raw_data'].get('chapters', {}).get(ch_num, {})
            # Get first group images
            groups = ch_data.get('groups', {})
            images = []
            for g_name, g_imgs in groups.items():
                if isinstance(g_imgs, list):
                    images = g_imgs
                    break
                elif isinstance(g_imgs, dict) and 'pages' in g_imgs:
                    images = g_imgs['pages']
                    break
            return {
                'url': url,
                'title': ch_data.get('title', f"Chapter {ch_num}"),
                'images': images,
                'total': len(images)
            }

    raise Exception("Không thể nhận diện nguồn chapter từ URL này.")
