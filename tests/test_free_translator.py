"""
Unit tests for free_translator module
"""
import sys
import unittest
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR / "scripts"))

from free_translator import translate_free_google


class TestFreeTranslator(unittest.TestCase):

    def test_translate_free_google_empty(self):
        self.assertEqual(translate_free_google(""), "")
        self.assertEqual(translate_free_google("   "), "")

    def test_translate_free_google_english_to_vi(self):
        res = translate_free_google("Hello world", "en", "vi")
        self.assertIn("thế giới", res.lower())

    def test_translate_free_google_chinese_to_vi(self):
        res = translate_free_google("你好世界", "zh", "vi")
        self.assertIn("thế giới", res.lower())


if __name__ == "__main__":
    unittest.main()
