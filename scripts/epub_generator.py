"""
📚 epub_generator.py - Convert Crawled Web Novel Chapters to Standard EPUB Files
"""

import io
import uuid
import re
from typing import List, Dict, Optional, Union
from ebooklib import epub


DEFAULT_CSS = """
@namespace epub "http://www.idpf.org/2007/ops";
body {
    font-family: "Georgia", "Times New Roman", serif;
    line-height: 1.6;
    margin: 5%;
    padding: 0;
    color: #111111;
    background-color: #ffffff;
}
h1, h2, h3 {
    font-family: "Helvetica Neue", "Segoe UI", Arial, sans-serif;
    text-align: center;
    margin-top: 1.8em;
    margin-bottom: 1em;
    font-weight: bold;
    color: #2c3e50;
    line-height: 1.3;
}
h1.book-title {
    font-size: 2.2em;
    margin-top: 30%;
    margin-bottom: 0.5em;
}
p.author-name {
    text-align: center;
    font-size: 1.2em;
    font-style: italic;
    color: #555555;
    margin-bottom: 2em;
}
p {
    text-indent: 1.5em;
    margin-top: 0;
    margin-bottom: 0.6em;
    text-align: justify;
}
p.no-indent {
    text-indent: 0;
}
blockquote {
    margin: 1em 2em;
    font-style: italic;
    color: #444444;
}
hr.sigil_split {
    border: none;
    border-top: 1px solid #cccccc;
    margin: 2em auto;
    width: 50%;
}
"""

def create_epub(
    title: str,
    author: str = "Unknown / Web Novel",
    chapters: Optional[List[Dict[str, Union[str, List[str]]]]] = None,
    description: str = "",
    language: str = "vi",
    cover_bytes: Optional[bytes] = None,
    cover_filename: str = "cover.jpg",
    custom_css: Optional[str] = None
) -> bytes:
    """
    Generate an EPUB 3 ebook file in memory from a list of chapters.

    :param title: Title of the book
    :param author: Author or translator name
    :param chapters: List of chapter dicts containing:
                     {"title": "...", "paragraphs": ["p1", "p2", ...]} or {"title": "...", "full_text": "..."}
    :param description: Summary/description of the book
    :param language: Language code ('vi', 'en', etc.)
    :param cover_bytes: Raw bytes of cover image (JPEG/PNG)
    :param cover_filename: File name of cover image
    :param custom_css: Custom CSS string to replace default stylesheet
    :return: Raw EPUB file bytes
    """
    if chapters is None:
        chapters = []

    book = epub.EpubBook()

    # Metadata
    book_id = f"urn:uuid:{uuid.uuid4()}"
    book.set_identifier(book_id)
    book.set_title(title)
    book.set_language(language)
    book.add_author(author)

    if description:
        book.add_metadata("DC", "description", description)

    # Stylesheet
    style_content = custom_css if custom_css else DEFAULT_CSS
    nav_css = epub.EpubItem(
        uid="style_css",
        file_name="style/style.css",
        media_type="text/css",
        content=style_content.encode("utf-8")
    )
    book.add_item(nav_css)

    # Cover Page
    if cover_bytes:
        book.set_cover(cover_filename, cover_bytes)

    # Title Page
    title_html = f"""
    <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
    <head>
        <title>{_escape_html(title)}</title>
        <link rel="stylesheet" href="style/style.css" type="text/css"/>
    </head>
    <body>
        <div style="text-align: center; padding-top: 20%;">
            <h1 class="book-title">{_escape_html(title)}</h1>
            <p class="author-name">Tác giả / Nguồn: {_escape_html(author)}</p>
        </div>
    </body>
    </html>
    """
    title_page = epub.EpubHtml(
        title="Title Page",
        file_name="title_page.xhtml",
        lang=language
    )
    title_page.content = title_html
    title_page.add_item(nav_css)
    book.add_item(title_page)

    epub_chapters = []
    spine_items = ["nav", title_page]

    # Description / Văn Án Page (if provided)
    if description and description.strip():
        desc_lines = [p.strip() for p in description.strip().split('\n') if p.strip()]
        desc_html_body = ["<h2>Văn Án / Giới Thiệu</h2>"]
        for dl in desc_lines:
            desc_html_body.append(f"<p>{_escape_html(dl)}</p>")

        desc_content = f"""
        <!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
        <head>
            <title>Văn Án</title>
            <link rel="stylesheet" href="style/style.css" type="text/css"/>
        </head>
        <body>
            {''.join(desc_html_body)}
        </body>
        </html>
        """
        desc_page = epub.EpubHtml(
            title="Văn Án",
            file_name="description.xhtml",
            lang=language
        )
        desc_page.content = desc_content
        desc_page.add_item(nav_css)
        book.add_item(desc_page)
        epub_chapters.append(desc_page)
        spine_items.append(desc_page)

    # Process Chapters
    for idx, ch in enumerate(chapters, start=1):
        ch_title = ch.get("title", f"Chương {idx}")
        paragraphs = ch.get("paragraphs")
        full_text = ch.get("full_text")

        if not paragraphs and full_text:
            paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

        if not paragraphs:
            paragraphs = []

        # Convert paragraphs to XHTML <p> tags
        body_html_parts = []
        body_html_parts.append(f"<h2>{_escape_html(ch_title)}</h2>")

        for p in paragraphs:
            clean_p = _escape_html(p)
            body_html_parts.append(f"<p>{clean_p}</p>")

        ch_content = f"""
        <!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
        <head>
            <title>{_escape_html(ch_title)}</title>
            <link rel="stylesheet" href="style/style.css" type="text/css"/>
        </head>
        <body>
            {''.join(body_html_parts)}
        </body>
        </html>
        """

        filename = f"chap_{idx:04d}.xhtml"
        epub_ch = epub.EpubHtml(
            title=ch_title,
            file_name=filename,
            lang=language
        )
        epub_ch.content = ch_content
        epub_ch.add_item(nav_css)
        book.add_item(epub_ch)

        epub_chapters.append(epub_ch)
        spine_items.append(epub_ch)

    # Table of Contents
    book.toc = tuple(epub_chapters)

    # Add default NCX and Nav files
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = spine_items

    # Write EPUB to bytes buffer
    out_buffer = io.BytesIO()
    epub.write_epub(out_buffer, book, {})
    out_buffer.seek(0)
    return out_buffer.getvalue()


def _escape_html(text: str) -> str:
    """Escape special HTML characters safely."""
    if not text:
        return ""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
    )
