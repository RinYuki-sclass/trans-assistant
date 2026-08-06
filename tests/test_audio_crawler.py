"""Regression tests for site-specific novel chapter extraction."""

import os
import sys
import unittest

from bs4 import BeautifulSoup


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio.crawler import _extract_mistmint_next_content, _extract_paragraphs


class MistmintCrawlerTests(unittest.TestCase):
    def test_extracts_nextjs_flight_html(self):
        html = """
        <html><body>
          <script>self.__next_f.push([1,"\\u003cp\\u003eFirst chapter paragraph with enough text.\\u003c/p\\u003e\\u003cp\\u003eSecond chapter paragraph with enough text.\\u003c/p\\u003e"])</script>
        </body></html>
        """
        content = _extract_mistmint_next_content(BeautifulSoup(html, "html.parser"))

        self.assertIsNotNone(content)
        self.assertEqual(
            _extract_paragraphs(content),
            [
                "First chapter paragraph with enough text.",
                "Second chapter paragraph with enough text.",
            ],
        )

    def test_ignores_unrelated_nextjs_payload(self):
        html = '<script>self.__next_f.push([1,"metadata only"])</script>'
        content = _extract_mistmint_next_content(BeautifulSoup(html, "html.parser"))
        self.assertIsNone(content)


if __name__ == "__main__":
    unittest.main()
