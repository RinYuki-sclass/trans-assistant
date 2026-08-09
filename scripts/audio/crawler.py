"""Novel chapter crawler for supported WordPress and Next.js sites."""

import json
import re
from urllib.parse import urlparse

import httpx
from bs4 import BeautifulSoup


# ── CSS selectors ────────────────────────────────────────────────────
_CONTENT_SELECTORS = [
    "div#chapter-content-text",  # Mistmint Haven hydrated DOM
    "div.chapter-content-text",
    "div.entry-content",
    "div.post-content",
    "div.novel-content",
    "article .content",
    "div#content article",
    "article",
]

_NOISE_TAGS = [
    "script", "style", "nav", "footer", "header",
    "aside", "noscript", "iframe", "form",
    ".sharedaddy", ".jp-relatedposts", ".adsbygoogle",
    ".nav-links", ".post-navigation", ".wp-block-separator",
]

_AD_PATTERNS = re.compile(
    r"(advertisement|sponsored|subscribe now|support the author"
    r"|buy me a coffee|patreon|discord\.gg|bit\.ly|tinyurl"
    r"|if you (?:like|enjoy)|please (rate|review|comment)"
    r"|read more at|translator['\u2019]?s note)",
    re.IGNORECASE,
)


def _fetch_html(url: str, timeout: int = 20) -> str:
    """Fetch raw HTML from URL using httpx."""
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    with httpx.Client(follow_redirects=True, timeout=timeout) as client:
        resp = client.get(url, headers=headers)
        resp.raise_for_status()
        return resp.text


def _extract_content(soup: BeautifulSoup) -> BeautifulSoup | None:
    """Try multiple selectors to find the main content block."""
    for selector in _CONTENT_SELECTORS:
        el = soup.select_one(selector)
        if el and len(el.get_text(strip=True)) > 200:
            return el
    return None


def _extract_mistmint_next_content(soup: BeautifulSoup) -> BeautifulSoup | None:
    """Extract chapter HTML embedded in Mistmint Haven's Next.js flight data.

    The initial HTTP response contains the chapter as an encoded HTML string;
    ``#chapter-content-text`` is created only after JavaScript hydration.
    """
    best_fragment = None
    best_paragraph_count = 0

    for script in soup.find_all("script"):
        raw = script.string or script.get_text()
        if "self.__next_f.push(" not in raw:
            continue
        match = re.search(r"self\.__next_f\.push\((\[.*\])\)\s*$", raw, re.DOTALL)
        if not match:
            continue
        try:
            flight_entry = json.loads(match.group(1))
        except (json.JSONDecodeError, TypeError):
            continue
        if len(flight_entry) < 2 or not isinstance(flight_entry[1], str):
            continue

        payload = flight_entry[1]
        if "<p" not in payload:
            continue
        fragment = BeautifulSoup(payload, "html.parser")
        paragraph_count = len(fragment.find_all("p"))
        if paragraph_count > best_paragraph_count:
            best_fragment = fragment
            best_paragraph_count = paragraph_count

    return best_fragment if best_paragraph_count else None


def _clean_element(content_el: BeautifulSoup) -> None:
    """Remove noise tags and ad-like elements from content block."""
    for tag in content_el.find_all(_NOISE_TAGS[0].split(",") + _NOISE_TAGS[1:]):
        tag.decompose()
    for selector in _NOISE_TAGS[4:]:
        for el in content_el.select(selector):
            el.decompose()


def _extract_paragraphs(content_el: BeautifulSoup) -> list[str]:
    """
    Extract text paragraphs from the content block.
    Filters out short ad-like lines.
    """
    paragraphs: list[str] = []

    # Try <p> tags first
    p_tags = content_el.find_all("p")
    if p_tags:
        for p in p_tags:
            text = p.get_text(separator=" ", strip=True)
            text = re.sub(r"\s+", " ", text).strip()
            if len(text) < 10:
                continue
            if _AD_PATTERNS.search(text):
                continue
            paragraphs.append(text)
    else:
        # Fallback: split by newlines
        raw = content_el.get_text(separator="\n")
        for line in raw.splitlines():
            line = line.strip()
            if len(line) < 10:
                continue
            if _AD_PATTERNS.search(line):
                continue
            paragraphs.append(line)

    return paragraphs


def _extract_title(soup: BeautifulSoup, url: str) -> str:
    """Extract chapter title from <h1>, <h2>, or page <title>."""
    for selector in ["h1.entry-title", "h1.post-title", "h1", "h2.entry-title", "h2"]:
        el = soup.select_one(selector)
        if el:
            return el.get_text(strip=True)
    # Fallback: derive from URL slug
    slug = url.rstrip("/").split("/")[-1]
    return slug.replace("-", " ").title()


def parse_lexical(node: dict) -> list[str]:
    """Extract clean text paragraphs from a Lexical rich text AST dict."""
    paragraphs: list[str] = []
    if not isinstance(node, dict):
        return paragraphs

    def walk(n):
        if not isinstance(n, dict):
            return
        n_type = n.get("type")
        if n_type in ("paragraph", "heading", "quote"):
            text_bits = []
            for child in n.get("children", []):
                if isinstance(child, dict):
                    if child.get("type") == "text":
                        text_bits.append(child.get("text", ""))
                    elif "children" in child:
                        for gc in child["children"]:
                            if isinstance(gc, dict) and gc.get("type") == "text":
                                text_bits.append(gc.get("text", ""))
            p_text = "".join(text_bits).strip()
            p_text = re.sub(r"\s+", " ", p_text).strip()
            if p_text and len(p_text) >= 1 and not _AD_PATTERNS.search(p_text):
                paragraphs.append(p_text)
        else:
            for key in ("root", "children"):
                val = n.get(key)
                if isinstance(val, dict):
                    walk(val)
                elif isinstance(val, list):
                    for item in val:
                        walk(item)

    walk(node)
    return paragraphs


def _fetch_zenith_chapter_by_id_or_slug(chapter_id_or_slug: str) -> tuple[str, list[str]]:
    """Fetch ZenithTL chapter title and paragraphs by ID or slug."""
    headers = {"User-Agent": "Mozilla/5.0"}
    with httpx.Client(headers=headers, timeout=20) as client:
        # Direct ID endpoint
        if re.match(r"^[a-f0-9]{24}$", chapter_id_or_slug, re.IGNORECASE):
            r = client.get(f"https://zenithtls.com/api/chapters/{chapter_id_or_slug}")
            if r.status_code == 200:
                d = r.json()
                title = d.get("title") or f"Chapter {d.get('chapterNumber', '')}"
                paragraphs = parse_lexical(d.get("content", {}))
                return title, paragraphs

        # Slug endpoint
        r = client.get(f"https://zenithtls.com/api/chapters?where[slug][equals]={chapter_id_or_slug}")
        if r.status_code == 200 and r.json().get("docs"):
            d = r.json()["docs"][0]
            title = d.get("title") or f"Chapter {d.get('chapterNumber', '')}"
            paragraphs = parse_lexical(d.get("content", {}))
            return title, paragraphs

        raise ValueError(f"Could not fetch ZenithTL chapter for '{chapter_id_or_slug}'")


def fetch_series_chapters(url_or_identifier: str) -> dict:
    """
    Fetch series metadata and complete chapter list from ZenithTL.

    Returns:
        {
            "series_title": str,
            "series_id": str,
            "chapters": [
                {
                    "id": str,
                    "chapter_number": int,
                    "title": str,
                    "slug": str,
                    "price": float,
                    "url": str,
                }, ...
            ]
        }
    """
    parsed = urlparse(url_or_identifier)
    path_parts = [p for p in parsed.path.split("/") if p]

    # Extract series identifier
    series_id = ""
    if "series" in path_parts:
        idx = path_parts.index("series")
        if idx + 1 < len(path_parts):
            series_id = path_parts[idx + 1]
    elif path_parts:
        series_id = path_parts[-1]
    else:
        series_id = url_or_identifier.strip()

    headers = {"User-Agent": "Mozilla/5.0"}
    with httpx.Client(headers=headers, timeout=20) as client:
        novel_data = None

        # Lookup by 24-char hex ID
        if re.match(r"^[a-f0-9]{24}$", series_id, re.IGNORECASE):
            r = client.get(f"https://zenithtls.com/api/novels/{series_id}")
            if r.status_code == 200:
                novel_data = r.json()

        # Search by slug
        if not novel_data:
            r = client.get(f"https://zenithtls.com/api/novels?where[slug][equals]={series_id}")
            if r.status_code == 200 and r.json().get("docs"):
                novel_data = r.json()["docs"][0]

        if not novel_data:
            raise ValueError(f"Could not find novel series on ZenithTL for: {series_id}")

        novel_id = novel_data.get("id")
        series_title = novel_data.get("title", "ZenithTL Series")

        all_chapters = []
        page = 1
        while True:
            r = client.get(f"https://zenithtls.com/api/chapters?where[novel][equals]={novel_id}&limit=100&page={page}")
            r.raise_for_status()
            data = r.json()
            docs = data.get("docs", [])
            all_chapters.extend(docs)
            if page >= data.get("totalPages", 1) or not docs:
                break
            page += 1

        all_chapters.sort(key=lambda c: c.get("chapterNumber", 0))

        formatted_chapters = []
        for c in all_chapters:
            ch_num = c.get("chapterNumber", 0)
            ch_title = c.get("title") or f"Chapter {ch_num}"
            ch_id = c.get("id", "")
            ch_slug = c.get("slug") or ""
            price = c.get("price", 0)
            ch_url = f"https://zenithtls.com/chapter/{ch_id}" if ch_id else f"https://zenithtls.com/chapter/{ch_slug}"
            formatted_chapters.append({
                "id": ch_id,
                "chapter_number": ch_num,
                "title": ch_title,
                "slug": ch_slug,
                "price": price,
                "url": ch_url,
            })

        return {
            "series_title": series_title,
            "series_id": novel_id,
            "chapters": formatted_chapters,
        }


def crawl_chapter(url: str) -> dict:
    """
    Crawl a single chapter page and return a clean structured dict.

    Returns:
        {
            "url": str,
            "title": str,
            "paragraphs": list[str],   # cleaned paragraph list
            "full_text": str,           # joined text (for TTS)
            "word_count": int,
        }
    """
    hostname = (urlparse(url).hostname or "").lower()

    if hostname == "zenithtls.com" or hostname.endswith(".zenithtls.com"):
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split("/") if p]
        
        # Check if URL is a series page URL
        if "series" in path_parts and not any(k in path_parts for k in ("chapter", "ch")):
            # It's a series URL, fetch the chapter list and crawl the first available chapter as fallback
            series_info = fetch_series_chapters(url)
            if not series_info["chapters"]:
                raise ValueError(f"No chapters found for ZenithTL series: {url}")
            first_ch = series_info["chapters"][0]
            title, paragraphs = _fetch_zenith_chapter_by_id_or_slug(first_ch["id"])
            full_text = "\n\n".join(paragraphs)
            return {
                "url": url,
                "title": f"{series_info['series_title']} - {title}",
                "paragraphs": paragraphs,
                "full_text": full_text,
                "word_count": len(full_text.split()),
            }

        # Handle chapter URL or chapter ID
        identifier = path_parts[-1] if path_parts else url
        title, paragraphs = _fetch_zenith_chapter_by_id_or_slug(identifier)
        full_text = "\n\n".join(paragraphs)
        return {
            "url": url,
            "title": title,
            "paragraphs": paragraphs,
            "full_text": full_text,
            "word_count": len(full_text.split()),
        }

    html = _fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title = _extract_title(soup, url)

    if hostname == "mistminthaven.com" or hostname.endswith(".mistminthaven.com"):
        content_el = _extract_mistmint_next_content(soup) or _extract_content(soup)
    else:
        content_el = _extract_content(soup)
    if content_el is None:
        raise ValueError(
            f"Could not find main content block on page: {url}\n"
            "Try adding a new selector to _CONTENT_SELECTORS."
        )

    _clean_element(content_el)
    paragraphs = _extract_paragraphs(content_el)

    if not paragraphs:
        raise ValueError(f"No readable paragraphs extracted from: {url}")

    full_text = "\n\n".join(paragraphs)
    word_count = len(full_text.split())

    return {
        "url": url,
        "title": title,
        "paragraphs": paragraphs,
        "full_text": full_text,
        "word_count": word_count,
    }

