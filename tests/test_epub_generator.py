"""
Unit tests for EPUB generator module
"""
import sys
import unittest
from pathlib import Path

# Add scripts directory to path
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR / "scripts"))

from epub_generator import create_epub


class TestEpubGenerator(unittest.TestCase):

    def test_create_simple_epub(self):
        chapters = [
            {
                "title": "Chương 1: Khởi Đầu",
                "paragraphs": [
                    "Đây là đoạn văn đầu tiên của chương 1.",
                    "Đây là đoạn văn thứ hai của chương 1."
                ],
                "word_count": 20
            },
            {
                "title": "Chương 2: Hành Trình Mới",
                "paragraphs": [
                    "Bầu trời xanh thẳm khi bình minh lên.",
                    "Cuộc hành trình mới chính thức bắt đầu."
                ],
                "word_count": 18
            }
        ]

        epub_bytes = create_epub(
            title="Truyện Thử Nghiệm",
            author="Tác Giả Antigravity",
            chapters=chapters,
            description="Mô tả cuốn sách thử nghiệm.",
            language="vi"
        )

        self.assertIsInstance(epub_bytes, bytes)
        self.assertGreater(len(epub_bytes), 1000)
        self.assertTrue(epub_bytes.startswith(b"PK"))  # EPUB is a ZIP archive starting with PK signature

    def test_create_epub_with_cover(self):
        # 1x1 transparent PNG bytes
        fake_png_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\rIDATx\x9cc\xf8\x0f\x00\x01\x01\x01\x00\x18\xdd\x8d\xb0\x00\x00\x00\x00IEND\xaeB`\x82'
        chapters = [{"title": "Chapter 1", "full_text": "Sample full text."}]

        epub_bytes = create_epub(
            title="Book with Cover",
            author="Author",
            chapters=chapters,
            cover_bytes=fake_png_bytes,
            cover_filename="cover.png"
        )

        self.assertIsInstance(epub_bytes, bytes)
        self.assertGreater(len(epub_bytes), 1000)


if __name__ == "__main__":
    unittest.main()
