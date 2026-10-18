import os
import re
import json
import urllib.parse
from typing import Dict, List, Optional
import requests
from crawler.haccbl_crawler import get_haccbl_manga_info, get_haccbl_chapter_images, download_chapter_images, get_scraper, clean_slug

def search_manga_haccbl(query: str) -> List[Dict]:
    """
    Tìm kiếm truyện tranh trên HaccBL và trả về danh sách kết quả
    """
    query = query.strip()
    if not query:
        return []
    scraper = get_scraper()
    search_url = f"https://haccbl.xyz/?s={urllib.parse.quote(query)}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': 'https://haccbl.xyz/'
    }
    res = scraper.get(search_url, headers=headers, timeout=15)
    if res.status_code != 200:
        return []

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')
    results = []
    for row in soup.select('div.uk-grid-small'):
        a = row.select_one('h3 a, h4 a, a.uk-link-reset')
        img = row.select_one('img')
        if a and a.get('href') and '/manga/' in a.get('href'):
            cover = (img.get('src') or img.get('data-src') or '') if img else ''
            title = a.text.strip()
            href = a.get('href').strip()
            slug = clean_slug(title)
            if not any(r['url'] == href for r in results):
                results.append({
                    'title': title,
                    'url': href,
                    'cover': cover,
                    'slug': slug,
                    'source': 'haccbl'
                })
    return results

def get_generic_manga_info(url: str) -> Dict:
    """
    Bóc tách thông tin truyện tự động từ các web truyện tranh (Madara, WordPress manga themes)
    """
    scraper = get_scraper()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Referer': url
    }
    res = scraper.get(url, headers=headers, timeout=20)
    if res.status_code != 200:
        raise Exception(f"Không thể truy cập trang truyện (HTTP {res.status_code})")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')

    # Title
    title_el = soup.select_one('h1, .post-title, .entry-title') or soup.find('title')
    title = title_el.text.strip() if title_el else "Unknown Manga"
    title = re.sub(r'\s*[-|]\s*.*?(đọc|truyện|nettruyen|manhwa).*?$', '', title, flags=re.IGNORECASE).strip()

    # Cover
    cover_el = soup.select_one('.summary_image img, .manga-poster img, .thumb img, .c-image-hover img, meta[property="og:image"]')
    cover_url = ""
    if cover_el:
        if cover_el.name == 'meta':
            cover_url = cover_el.get('content', '')
        else:
            cover_url = cover_el.get('data-src') or cover_el.get('data-lazy-src') or cover_el.get('src') or ''

    # Chapters
    chapters = []
    candidate_links = soup.select('li.wp-manga-chapter a, .listing-chapters_sub-head a, .chapter-name a, ul.sub-chap-list a, .list-chapter a, a[href*="/chapter-"], a[href*="/chuong-"], a[href*="/chap-"]')
    
    seen_urls = set()
    for a in candidate_links:
        href = a.get('href', '').strip()
        if not href or href in seen_urls:
            continue
        if '#' in href or 'facebook' in href or 'disqus' in href:
            continue
        seen_urls.add(href)
        ch_title = a.text.strip() or "Chapter"
        ch_slug = clean_slug(ch_title)
        chapters.append({
            'title': ch_title,
            'url': href,
            'slug': ch_slug
        })

    if len(chapters) > 1:
        num_first = re.search(r'\d+', chapters[0]['title'])
        num_last = re.search(r'\d+', chapters[-1]['title'])
        if num_first and num_last and int(num_first.group(0)) > int(num_last.group(0)):
            chapters.reverse()

    slug = clean_slug(title)

    return {
        'title': title,
        'slug': slug,
        'url': url,
        'cover': cover_url,
        'chapters': chapters,
        'total_chapters': len(chapters),
        'source': 'generic'
    }

def get_generic_chapter_images(url: str) -> Dict:
    """
    Bóc tách danh sách ảnh chapter từ URL truyện tranh thông thường
    """
    scraper = get_scraper()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Referer': url
    }
    res = scraper.get(url, headers=headers, timeout=20)
    if res.status_code != 200:
        raise Exception(f"Không thể truy cập chapter (HTTP {res.status_code})")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')

    images = []
    selectors = [
        '.reading-content img',
        '.entry-content img',
        '.page-break img',
        '#chapter-content img',
        '.container-chapter-reader img',
        '.chapter-image img',
        '.box_doc img',
        '.content-read img'
    ]
    img_tags = soup.select(', '.join(selectors))
    if not img_tags:
        img_tags = soup.find_all('img')

    for img in img_tags:
        src = img.get('data-original-src') or img.get('data-src') or img.get('data-lazy-src') or img.get('src')
        if src and not src.startswith('data:image'):
            src = src.strip()
            lower = src.lower()
            if any(k in lower for k in ['logo', 'icon', 'banner', 'avatar', 'ads', 'loading', 'placeholder']):
                continue
            if src not in images:
                images.append(src)

    title_el = soup.find('h1') or soup.find('title')
    title_text = title_el.text.strip() if title_el else "Chapter"

    return {
        'url': url,
        'title': title_text,
        'images': images,
        'total': len(images)
    }

def resolve_cubari_url(url: str) -> Optional[Dict]:
    """
    Hỗ trợ đọc link Cubari (gist, imgur, mangadex)
    Ví dụ: https://cubari.moe/read/gist/cmF3L2dpc3Q...
    """
    if "cubari.moe" not in url:
        return None

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
    Hỗ trợ HaccBL, Cubari và các trang manga tiêu chuẩn (Generic)
    """
    url = url.strip()
    
    # 1. Haccbl
    if "haccbl.xyz" in url:
        if "/chapter-" in url:
            m_manga = re.match(r'(https?://[^/]+/manga/[^/]+/)', url)
            if m_manga:
                manga_main_url = m_manga.group(1)
                return get_haccbl_manga_info(manga_main_url)
        return get_haccbl_manga_info(url)

    # 2. Cubari
    cubari_info = resolve_cubari_url(url)
    if cubari_info:
        return cubari_info

    # 3. Fallback sang Generic Webtoon/Manga Crawler
    try:
        return get_generic_manga_info(url)
    except Exception as e:
        raise Exception(f"Không thể phân tích trang truyện: {e}")

def detect_and_get_chapter_images(url: str, context_data: Optional[Dict] = None) -> Dict:
    """
    Lấy danh sách ảnh của chapter từ URL
    """
    url = url.strip()

    # 1. Haccbl
    if "haccbl.xyz" in url:
        return get_haccbl_chapter_images(url)

    # 2. Cubari virtual url
    if url.startswith("cubari://"):
        if context_data and 'raw_data' in context_data:
            parts = url.split('/')
            ch_num = parts[-1]
            ch_data = context_data['raw_data'].get('chapters', {}).get(ch_num, {})
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

    # 3. Fallback Generic Chapter Images
    try:
        return get_generic_chapter_images(url)
    except Exception as e:
        raise Exception(f"Không thể bóc tách ảnh chapter: {e}")
