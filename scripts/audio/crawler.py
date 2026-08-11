"""Novel chapter crawler for supported WordPress and Next.js sites."""

import base64
import codecs
import json
import re
import time
import warnings
from urllib.parse import urljoin, urlparse, unquote

import httpx
from bs4 import BeautifulSoup


# ── CSS selectors ────────────────────────────────────────────────────
_CONTENT_SELECTORS = [
    "div#chapter-content-text",  # Mistmint Haven hydrated DOM
    "div.chapter-content-text",
    "div#chapterText",           # PIE NOVELS
    "div.chapter__content",      # Cherry Mist / Fictioneer
    "div#chapter-content",
    "div.fictioneer-chapter-text",
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
    timeout_config = httpx.Timeout(max(float(timeout), 60.0), connect=15.0)
    with httpx.Client(follow_redirects=True, timeout=timeout_config) as client:
        resp = _get_with_retry(client, url, headers=headers)
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
    with httpx.Client(
        headers=headers,
        follow_redirects=True,
        timeout=httpx.Timeout(60.0, connect=15.0),
    ) as client:
        # Direct ID endpoint
        if re.match(r"^[a-f0-9]{24}$", chapter_id_or_slug, re.IGNORECASE):
            r = _get_with_retry(client, f"https://zenithtls.com/api/chapters/{chapter_id_or_slug}")
            if r.status_code == 200:
                d = r.json()
                title = d.get("title") or f"Chapter {d.get('chapterNumber', '')}"
                paragraphs = parse_lexical(d.get("content", {}))
                return title, paragraphs

        # Slug endpoint
        r = _get_with_retry(client, f"https://zenithtls.com/api/chapters?where[slug][equals]={chapter_id_or_slug}")
        if r.status_code == 200 and r.json().get("docs"):
            d = r.json()["docs"][0]
            title = d.get("title") or f"Chapter {d.get('chapterNumber', '')}"
            paragraphs = parse_lexical(d.get("content", {}))
            return title, paragraphs

        raise ValueError(f"Could not fetch ZenithTL chapter for '{chapter_id_or_slug}'")


def _fetch_cherrymist_series_chapters(url: str) -> dict:
    """Fetch story series metadata and complete chapter list from Cherry Mist (Fictioneer theme)."""
    html = _fetch_html(url, timeout=25)
    soup = BeautifulSoup(html, "html.parser")

    h1 = soup.select_one("h1.story__title") or soup.select_one("h1.entry-title") or soup.find("h1")
    series_title = (h1.get_text(strip=True) if h1 else "Cherry Mist Story").strip()

    chapters = []
    seen_urls = set()

    groups = soup.select(".chapter-group, .story-chapters, .chapter-list")
    if not groups:
        groups = [soup]

    for group in groups:
        for a in group.find_all("a", href=True):
            ch_url = a["href"]
            if ch_url in seen_urls:
                continue
            if "/chapter/" in ch_url or "fcn_chapter" in ch_url or ("/story/" in url and "/story/" not in ch_url and "fictioneer" not in ch_url):
                seen_urls.add(ch_url)
                ch_title = a.get_text(strip=True)
                if not ch_title:
                    continue

                num_match = re.search(r"\d+", ch_title)
                ch_num = int(num_match.group()) if num_match else len(chapters) + 1

                chapters.append({
                    "id": ch_url,
                    "chapter_number": ch_num,
                    "title": ch_title,
                    "slug": ch_url.rstrip("/").split("/")[-1],
                    "price": 0,
                    "url": ch_url,
                })

    return {
        "series_title": series_title,
        "series_id": url,
        "chapters": chapters,
    }


_HYACINTH_CHAPTER_TITLE = re.compile(
    r"^Ch\.\s*(?:(\d+)|Side Story\s+(\d+))\b",
    re.IGNORECASE,
)

_RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def _get_with_retry(
    client: httpx.Client,
    url: str,
    *,
    attempts: int = 3,
    **kwargs,
) -> httpx.Response:
    """GET with short backoff for transient network/server failures."""
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    hostname = urlparse(url).hostname or url
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            response = client.get(url, **kwargs)
            if response.status_code not in _RETRYABLE_STATUS_CODES or attempt == attempts - 1:
                return response
            retry_after = response.headers.get("Retry-After", "")
            try:
                wait_seconds = min(5.0, max(0.0, float(retry_after)))
            except ValueError:
                wait_seconds = 0.75 * (2 ** attempt)
        except (httpx.TimeoutException, httpx.NetworkError) as exc:
            last_error = exc
            if attempt == attempts - 1:
                raise TimeoutError(
                    f"{hostname} không phản hồi sau {attempts} lần thử. "
                    "Vui lòng thử lại sau hoặc kiểm tra website nguồn."
                ) from exc
            wait_seconds = 0.75 * (2 ** attempt)
        time.sleep(wait_seconds)

    raise TimeoutError(f"Không thể kết nối tới {hostname}") from last_error


def _parse_hyacinth_series_chapters(html: str, series_url: str) -> dict:
    """Parse a Hyacinth Bloom series page into the common chapter schema."""
    soup = BeautifulSoup(html, "html.parser")
    heading = (
        soup.select_one("h1.entry-title")
        or soup.select_one("h1.post-title")
        or soup.find("h1")
    )
    series_title = heading.get_text(" ", strip=True) if heading else "Hyacinth Bloom Series"

    chapters = []
    seen_urls = set()
    for link in soup.select("a[href]"):
        title = link.get_text(" ", strip=True)
        match = _HYACINTH_CHAPTER_TITLE.match(title)
        if not match:
            continue

        chapter_url = urljoin(series_url, link["href"])
        if chapter_url in seen_urls:
            continue
        seen_urls.add(chapter_url)

        is_side_story = match.group(1) is None
        chapter_number = int(match.group(1) or match.group(2))
        chapters.append({
            "id": chapter_url,
            "chapter_number": chapter_number,
            "title": title,
            "slug": urlparse(chapter_url).path.rstrip("/").split("/")[-1],
            "price": 0,
            "url": chapter_url,
            "_sort_key": (1 if is_side_story else 0, chapter_number),
        })

    chapters.sort(key=lambda chapter: chapter.pop("_sort_key"))
    return {
        "series_title": series_title.strip(),
        "series_id": series_url,
        "chapters": chapters,
    }


def _fetch_hyacinth_series_chapters(url: str) -> dict:
    """Fetch a Hyacinth Bloom series page and its regular/side-story links."""
    html = _fetch_html(url, timeout=30)
    return _parse_hyacinth_series_chapters(html, url)


def _parse_pienovels_series_chapters(html: str, novel_url: str) -> dict:
    """Parse a PIE NOVELS novel page into the common chapter schema."""
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.select_one("h1.single-novel-title") or soup.find("h1")
    series_title = (
        heading.get_text(" ", strip=True)
        if heading
        else "PIE NOVELS Series"
    )

    chapters_by_url = {}
    for link in soup.select('a[href*="/chapters/"]'):
        chapter_url = urljoin(novel_url, link.get("href", "").strip())
        parsed = urlparse(chapter_url)
        if parsed.scheme != "https" or parsed.netloc.lower() != "pienovels.com":
            continue
        if not parsed.path.lower().startswith("/chapters/"):
            continue

        label_element = link.find("p")
        label = (
            label_element.get_text(" ", strip=True)
            if label_element
            else link.get_text(" ", strip=True)
        )
        number_match = re.search(r"\bChapter\s+(\d+)\b", label, re.IGNORECASE)
        if not number_match:
            number_match = re.search(
                r"/chapters/chapter-(\d+)(?:-|/|$)",
                chapter_url,
                re.IGNORECASE,
            )
        if not number_match:
            continue

        chapter_number = int(number_match.group(1))
        title = re.sub(
            rf"^\s*Chapter\s+{chapter_number}\s*:?\s*",
            "",
            label,
            flags=re.IGNORECASE,
        ).strip()
        if not title:
            title = f"Chapter {chapter_number}"

        paid_label = link.select_one(".paid-span")
        price_match = re.search(r"\d+(?:\.\d+)?", paid_label.get_text(" ", strip=True)) if paid_label else None
        price = float(price_match.group()) if price_match else 0
        if price.is_integer():
            price = int(price)

        chapters_by_url[chapter_url] = {
            "id": chapter_url,
            "chapter_number": chapter_number,
            "title": title,
            "slug": parsed.path.rstrip("/").split("/")[-1],
            "price": price,
            "url": chapter_url,
        }

    chapters = sorted(
        chapters_by_url.values(),
        key=lambda chapter: chapter["chapter_number"],
    )
    if not chapters:
        raise ValueError(f"No PIE NOVELS chapters found on: {novel_url}")
    return {
        "series_title": series_title.strip(),
        "series_id": novel_url,
        "chapters": chapters,
    }


def _fetch_pienovels_series_chapters(url: str) -> dict:
    """Fetch a PIE NOVELS novel page and its server-rendered chapter list."""
    html = _fetch_html(url, timeout=30)
    return _parse_pienovels_series_chapters(html, url)


class MistmintHavenCrawler:
    """Discover and fetch the numeric chapter list for a Mistmint Haven novel."""

    BASE_URL = "https://www.mistminthaven.com"
    API_BASE_URL = "https://api.mistminthaven.com"

    def __init__(self, novel_slug: str):
        novel_slug = novel_slug.strip().strip("/")
        if not novel_slug or "/" in novel_slug:
            raise ValueError(f"Invalid Mistmint Haven novel slug: {novel_slug!r}")
        self.novel_slug = novel_slug
        self.novel_url = f"{self.BASE_URL}/novels/{novel_slug}"
        self.headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/151.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "type": "reader",
        }

    def fetch(self) -> str:
        """Fetch the novel landing page for source inspection and title metadata."""
        with httpx.Client(
            headers=self.headers,
            follow_redirects=True,
            timeout=httpx.Timeout(60.0, connect=15.0),
        ) as client:
            response = _get_with_retry(client, self.novel_url)
            response.raise_for_status()
            return response.text

    def inspect_html(self, html: str) -> tuple[str, object]:
        """Select the best available chapter source in the required priority order."""
        soup = BeautifulSoup(html, "html.parser")
        chapters = self.extract_chapters_from_links(soup)
        if chapters:
            return "links", chapters

        chapters = self.extract_chapters_from_embedded_data(soup)
        if chapters:
            return "embedded", chapters

        return "api", self.discover_api(soup)

    def extract_chapters_from_links(self, soup: BeautifulSoup) -> list[dict]:
        """Extract confirmed numeric chapter links belonging to this novel only."""
        chapters_by_url = {}
        path_pattern = re.compile(
            rf"^/novels/{re.escape(self.novel_slug)}/chapter-(\d+)/?$",
            re.IGNORECASE,
        )
        for link in soup.select("a[href]"):
            chapter_url = urljoin(self.BASE_URL, link["href"])
            parsed = urlparse(chapter_url)
            if parsed.scheme != "https" or parsed.netloc.lower() != "www.mistminthaven.com":
                continue
            match = path_pattern.match(parsed.path)
            if not match:
                continue
            chapter_number = int(match.group(1))
            title = " ".join(link.get_text(" ", strip=True).split())
            chapters_by_url[chapter_url] = {
                "chapter_number": chapter_number,
                "title": title or f"Chapter {chapter_number}",
                "url": chapter_url,
            }
        return sorted(chapters_by_url.values(), key=lambda chapter: chapter["chapter_number"])

    def extract_chapters_from_embedded_data(self, soup: BeautifulSoup) -> list[dict]:
        """Extract chapter URLs if a future site build embeds them in script data."""
        candidates = []
        escaped_slug = re.escape(self.novel_slug)
        pattern = re.compile(
            rf"(?:https://www\.mistminthaven\.com)?"
            rf"(/novels/{escaped_slug}/chapter-(\d+)/?)",
            re.IGNORECASE,
        )
        for script in soup.find_all("script"):
            raw = script.string or script.get_text()
            if not raw:
                continue
            raw = raw.replace(r"\/", "/")
            for match in pattern.finditer(raw):
                number = int(match.group(2))
                candidates.append({
                    "chapter_number": number,
                    "title": f"Chapter {number}",
                    "url": urljoin(self.BASE_URL, match.group(1)),
                })
        return self._deduplicate(candidates)

    def discover_api(self, soup: BeautifulSoup | None = None) -> str:
        """Return the public endpoint used by Mistmint Haven's novel-page client."""
        return f"{self.API_BASE_URL}/api/novels/slug/{self.novel_slug}/chapters"

    def extract_chapters_from_api(self, api_url: str) -> list[dict]:
        """Fetch and normalize the volume-grouped chapter response from the site API."""
        with httpx.Client(
            headers=self.headers,
            follow_redirects=True,
            timeout=httpx.Timeout(60.0, connect=15.0),
        ) as client:
            response = _get_with_retry(
                client,
                api_url,
                headers={
                    "Origin": self.BASE_URL,
                    "Referer": f"{self.BASE_URL}/",
                },
            )
            response.raise_for_status()
            payload = response.json()
        return self._chapters_from_api_payload(payload)

    def _chapters_from_api_payload(self, payload: object) -> list[dict]:
        chapters = []
        volumes = payload.get("data", []) if isinstance(payload, dict) else []
        for volume in volumes if isinstance(volumes, list) else []:
            if not isinstance(volume, dict):
                continue
            for chapter in volume.get("chapters", []):
                if not isinstance(chapter, dict) or chapter.get("isHidden"):
                    continue
                slug = str(chapter.get("slug") or "")
                match = re.fullmatch(r"chapter-(\d+)", slug, re.IGNORECASE)
                if not match:
                    continue
                chapter_number = int(match.group(1))
                subtitle = " ".join(str(chapter.get("title") or "").split())
                title = f"Chapter {chapter_number}"
                if subtitle:
                    title = f"{title}: {subtitle}"
                chapters.append({
                    "chapter_number": chapter_number,
                    "title": title,
                    "url": f"{self.novel_url}/{slug}",
                })
        return self._deduplicate(chapters)

    @staticmethod
    def _deduplicate(chapters: list[dict]) -> list[dict]:
        chapters_by_url = {chapter["url"]: chapter for chapter in chapters}
        return sorted(chapters_by_url.values(), key=lambda chapter: chapter["chapter_number"])

    def validate(self, chapters: list[dict]) -> None:
        if not chapters:
            raise ValueError(f"No numeric chapters found for Mistmint Haven novel: {self.novel_slug}")

        numbers = [chapter["chapter_number"] for chapter in chapters]
        duplicate_numbers = sorted({number for number in numbers if numbers.count(number) > 1})
        if duplicate_numbers:
            warnings.warn(
                "Duplicate chapter number(s): " + ", ".join(map(str, duplicate_numbers)),
                stacklevel=2,
            )

        present = set(numbers)
        missing = [number for number in range(min(numbers), max(numbers) + 1) if number not in present]
        if missing:
            warnings.warn(
                "Missing chapter(s): " + ", ".join(map(str, missing)),
                stacklevel=2,
            )

    def crawl(self) -> list[dict]:
        html = self.fetch()
        source, data = self.inspect_html(html)
        chapters = data if source != "api" else self.extract_chapters_from_api(data)
        self.validate(chapters)
        return chapters


def _fetch_mistmint_series_chapters(url: str) -> dict:
    parsed = urlparse(url)
    path_parts = [part for part in parsed.path.split("/") if part]
    if "novels" not in path_parts or path_parts.index("novels") + 1 >= len(path_parts):
        raise ValueError(f"Invalid Mistmint Haven novel URL: {url}")
    slug = path_parts[path_parts.index("novels") + 1]
    crawler = MistmintHavenCrawler(slug)
    html = crawler.fetch()
    soup = BeautifulSoup(html, "html.parser")
    page_title = soup.title.get_text(" ", strip=True) if soup.title else slug.replace("-", " ").title()
    series_title = re.sub(r"\s*\|\s*Mistmint Haven\s*$", "", page_title).strip()
    source, data = crawler.inspect_html(html)
    chapters = data if source != "api" else crawler.extract_chapters_from_api(data)
    crawler.validate(chapters)
    return {
        "series_title": series_title,
        "series_id": slug,
        "chapters": [
            {
                "id": chapter["url"],
                "chapter_number": chapter["chapter_number"],
                "title": chapter["title"],
                "slug": chapter["url"].rstrip("/").split("/")[-1],
                "price": 0,
                "url": chapter["url"],
            }
            for chapter in chapters
        ],
    }


def fetch_series_chapters(url_or_identifier: str) -> dict:
    """
    Fetch series metadata and complete chapter list from ZenithTL, Cherry Mist, or supported sites.

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
    hostname = (urlparse(url_or_identifier).hostname or "").lower()
    if hostname == "cherrymist.cafe" or hostname.endswith(".cherrymist.cafe"):
        return _fetch_cherrymist_series_chapters(url_or_identifier)
    if hostname == "hyacinthbloom.com" or hostname.endswith(".hyacinthbloom.com"):
        return _fetch_hyacinth_series_chapters(url_or_identifier)
    if hostname == "mistminthaven.com" or hostname.endswith(".mistminthaven.com"):
        return _fetch_mistmint_series_chapters(url_or_identifier)
    if hostname == "pienovels.com" or hostname.endswith(".pienovels.com"):
        return _fetch_pienovels_series_chapters(url_or_identifier)

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
    with httpx.Client(
        headers=headers,
        follow_redirects=True,
        timeout=httpx.Timeout(60.0, connect=15.0),
    ) as client:
        novel_data = None

        # Lookup by 24-char hex ID
        if re.match(r"^[a-f0-9]{24}$", series_id, re.IGNORECASE):
            r = _get_with_retry(client, f"https://zenithtls.com/api/novels/{series_id}")
            if r.status_code == 200:
                novel_data = r.json()

        # Search by slug
        if not novel_data:
            r = _get_with_retry(client, f"https://zenithtls.com/api/novels?where[slug][equals]={series_id}")
            if r.status_code == 200 and r.json().get("docs"):
                novel_data = r.json()["docs"][0]

        if not novel_data:
            raise ValueError(f"Could not find novel series on ZenithTL for: {series_id}")

        novel_id = novel_data.get("id")
        series_title = novel_data.get("title", "ZenithTL Series")

        all_chapters = []
        page = 1
        while True:
            r = _get_with_retry(client, f"https://zenithtls.com/api/chapters?where[novel][equals]={novel_id}&limit=100&page={page}")
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


def _decode_cherrymist_ghost_content(soup: BeautifulSoup) -> BeautifulSoup | None:
    """Decode Cherry Mist's \"ghost\" content protection.

    The Fictioneer theme stores chapter content as an obfuscated payload
    inside ``<script type="application/json">`` tags:

    1. The HTML is URI-encoded (``encodeURIComponent``).
    2. Then base64-encoded (``btoa``).
    3. Then ROT13-rotated.
    4. Split across ``data-<poly>-0``, ``data-<poly>-1``, … attributes.

    The client-side JS reverses this on page load. We replicate that here.
    """
    ghost_script = None
    for tag in soup.find_all("script", type="application/json"):
        tag_id = tag.get("id") or ""
        if tag_id.startswith("ghost_") and tag.get("data-poly"):
            ghost_script = tag
            break

    if ghost_script is None:
        return None

    poly = ghost_script["data-poly"]
    total = int(ghost_script.get("data-total", 0))
    if total == 0:
        return None

    # Concatenate all data chunks
    encoded = ""
    for i in range(total):
        chunk = ghost_script.get(f"data-{poly}-{i}", "")
        encoded += chunk

    if not encoded:
        return None

    try:
        # Step 1: ROT13 decode
        rot13_decoded = codecs.decode(encoded, "rot_13")

        # Step 2: base64 decode
        raw_bytes = base64.b64decode(rot13_decoded)

        # Step 3: URI decode (the bytes are a percent-encoded UTF-8 string)
        html_str = unquote(raw_bytes.decode("latin-1"))

        fragment = BeautifulSoup(html_str, "html.parser")
        if len(fragment.get_text(strip=True)) > 50:
            return fragment
    except Exception:
        pass

    return None


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

    if hostname == "pienovels.com" or hostname.endswith(".pienovels.com"):
        parsed = urlparse(url)
        path_parts = [part for part in parsed.path.split("/") if part]
        if "novels" in path_parts:
            series_info = _fetch_pienovels_series_chapters(url)
            return crawl_chapter(series_info["chapters"][0]["url"])

    if hostname == "cherrymist.cafe" or hostname.endswith(".cherrymist.cafe"):
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split("/") if p]
        if "story" in path_parts and not any(k in path_parts for k in ("chapter", "ch")):
            series_info = _fetch_cherrymist_series_chapters(url)
            if not series_info["chapters"]:
                raise ValueError(f"No chapters found for Cherry Mist story: {url}")
            first_ch = series_info["chapters"][0]
            return crawl_chapter(first_ch["url"])

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

    html = _fetch_html(url, timeout=60)
    soup = BeautifulSoup(html, "html.parser")

    title = _extract_title(soup, url)

    # Cherry Mist / Fictioneer "ghost" content protection:
    # Content is ROT13 + base64 + URI-encoded, stored in data-a4f-N attributes
    if hostname == "cherrymist.cafe" or hostname.endswith(".cherrymist.cafe"):
        content_el = _decode_cherrymist_ghost_content(soup) or _extract_content(soup)
    elif hostname == "mistminthaven.com" or hostname.endswith(".mistminthaven.com"):
        content_el = _extract_mistmint_next_content(soup) or _extract_content(soup)
    else:
        content_el = _extract_content(soup)
    if content_el is None:
        if "fictioneerExtendedMembership" in html or "Membership Warning" in html or "oauth2" in html:
            raise ValueError(
                f"Chương truyện tại {url} bị khóa hoặc yêu cầu đăng nhập thành viên (Subscriber/Patreon) trên {hostname}."
            )
        raise ValueError(
            f"Không tìm thấy khối nội dung chính trên trang: {url}\n"
            "Chương truyện có thể bị khóa, chưa phát hành hoặc cần quyền truy cập."
        )

    _clean_element(content_el)
    paragraphs = _extract_paragraphs(content_el)

    if not paragraphs:
        if "fictioneerExtendedMembership" in html or "Membership Warning" in html or "oauth2" in html:
            raise ValueError(
                f"Chương truyện tại {url} bị khóa hoặc yêu cầu đăng nhập thành viên (Subscriber/Patreon) trên {hostname}."
            )
        raise ValueError(f"Không trích xuất được đoạn văn bản đọc được từ: {url}")

    full_text = "\n\n".join(paragraphs)
    word_count = len(full_text.split())

    return {
        "url": url,
        "title": title,
        "paragraphs": paragraphs,
        "full_text": full_text,
        "word_count": word_count,
    }


