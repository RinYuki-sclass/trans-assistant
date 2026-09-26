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
        
        # Verify description / văn án page is created inside archive
        import zipfile, io
        z = zipfile.ZipFile(io.BytesIO(epub_bytes))
        self.assertTrue(any("description.xhtml" in n for n in z.namelist()))

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

    def test_create_epub_with_separate_summaries(self):
        import zipfile, io

        chapters = [
            {"title": "Chương 1: Khởi Đầu", "paragraphs": ["Nội dung chương 1 không bị chèn tóm tắt."], "word_count": 10},
            {"title": "Chương 2: Thử Thách", "paragraphs": ["Nội dung chương 2 hoàn toàn riêng biệt."], "word_count": 10},
        ]
        story_summary = "Đây là tóm tắt toàn bộ cốt truyện tổng quan."
        chapter_summaries = [
            {"chapter_id": "ch_001", "title": "Chương 1: Khởi Đầu", "summary": "Tóm tắt ngắn gọn chương 1."},
            {"chapter_id": "ch_002", "title": "Chương 2: Thử Thách", "summary": "Tóm tắt ngắn gọn chương 2."},
        ]

        # Case 1: before_chapters
        epub_bytes_before = create_epub(
            title="Truyện Tóm Tắt Tách Biệt",
            author="Tác Giả",
            chapters=chapters,
            story_summary=story_summary,
            chapter_summaries=chapter_summaries,
            summary_position="before_chapters",
        )
        z1 = zipfile.ZipFile(io.BytesIO(epub_bytes_before))
        names1 = z1.namelist()

        # Both summary pages exist as independent xhtml files
        self.assertTrue(any("story_summary.xhtml" in n for n in names1))
        self.assertTrue(any("chapter_summaries.xhtml" in n for n in names1))
        self.assertTrue(any("chap_0001.xhtml" in n for n in names1))

        # Check content of chap_0001.xhtml: MUST NOT contain summary text (strictly not interleaved)
        chap1_content = [z1.read(n).decode('utf-8') for n in names1 if "chap_0001.xhtml" in n][0]
        self.assertNotIn("Tóm tắt ngắn gọn chương 1", chap1_content)
        self.assertNotIn("tóm tắt toàn bộ cốt truyện", chap1_content)
        self.assertIn("Nội dung chương 1 không bị chèn tóm tắt", chap1_content)

        # Check content of story_summary.xhtml: Contains the overall story summary
        story_content = [z1.read(n).decode('utf-8') for n in names1 if "story_summary.xhtml" in n][0]
        self.assertIn("Đây là tóm tắt toàn bộ cốt truyện tổng quan", story_content)

        # Check content of chapter_summaries.xhtml: Contains chapter summaries
        ch_sum_content = [z1.read(n).decode('utf-8') for n in names1 if "chapter_summaries.xhtml" in n][0]
        self.assertIn("Tóm tắt ngắn gọn chương 1", ch_sum_content)
        self.assertIn("Tóm tắt ngắn gọn chương 2", ch_sum_content)

        # Case 2: after_chapters
        epub_bytes_after = create_epub(
            title="Truyện Tóm Tắt Sau",
            author="Tác Giả",
            chapters=chapters,
            story_summary=story_summary,
            chapter_summaries=chapter_summaries,
            summary_position="after_chapters",
        )
        z2 = zipfile.ZipFile(io.BytesIO(epub_bytes_after))
        names2 = z2.namelist()
        self.assertTrue(any("story_summary.xhtml" in n for n in names2))
        self.assertTrue(any("chapter_summaries.xhtml" in n for n in names2))

        # Case 3: include_summary=False
        epub_bytes_no_sum = create_epub(
            title="Truyện Không Tóm Tắt",
            author="Tác Giả",
            chapters=chapters,
            story_summary=story_summary,
            chapter_summaries=chapter_summaries,
            include_summary=False,
        )
        z3 = zipfile.ZipFile(io.BytesIO(epub_bytes_no_sum))
        names3 = z3.namelist()
        self.assertFalse(any("story_summary.xhtml" in n for n in names3))
        self.assertFalse(any("chapter_summaries.xhtml" in n for n in names3))


if __name__ == "__main__":
    unittest.main()
