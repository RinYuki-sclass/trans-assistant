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
    html = _fetch_html(url)
    soup = BeautifulSoup(html, "html.parser")

    title = _extract_title(soup, url)

    hostname = (urlparse(url).hostname or "").lower()
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
