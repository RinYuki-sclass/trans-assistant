"""Regression tests for site-specific novel chapter extraction."""

import os
import sys
import unittest
from unittest.mock import Mock, patch

import httpx
from bs4 import BeautifulSoup


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio.crawler import (
    _extract_mistmint_next_content,
    _extract_paragraphs,
    _fetch_html,
    _get_with_retry,
    _parse_hyacinth_series_chapters,
    _parse_pienovels_series_chapters,
    MistmintHavenCrawler,
)


class HttpRetryTests(unittest.TestCase):
    @patch("audio.crawler.time.sleep")
    @patch("audio.crawler.httpx.Client")
    def test_html_retry_uses_fresh_connections(self, client_class, _sleep_mock):
        response = Mock(status_code=200, headers={}, text="<html>chapters</html>")
        response.raise_for_status = Mock()
        client = Mock()
        client.get.side_effect = [httpx.ReadTimeout("stale socket"), response]
        client_class.return_value.__enter__.return_value = client

        html = _fetch_html("https://pienovels.com/novels/test/")

        self.assertEqual(html, "<html>chapters</html>")
        self.assertEqual(client.get.call_count, 2)
        request_headers = client.get.call_args.kwargs["headers"]
        self.assertEqual(request_headers["Connection"], "close")
        limits = client_class.call_args.kwargs["limits"]
        self.assertEqual(limits.max_keepalive_connections, 0)

    @patch("audio.crawler.time.sleep")
    def test_retries_timeout_then_returns_response(self, sleep_mock):
        response = Mock(status_code=200, headers={})
        client = Mock()
        client.get.side_effect = [
            httpx.ReadTimeout("timed out"),
            httpx.ConnectError("temporary network error"),
            response,
        ]

        result = _get_with_retry(client, "https://example.com/chapters")

        self.assertIs(result, response)
        self.assertEqual(client.get.call_count, 3)
        self.assertEqual(sleep_mock.call_count, 2)

    @patch("audio.crawler.time.sleep")
    def test_retries_transient_http_status(self, sleep_mock):
        busy = Mock(status_code=503, headers={})
        success = Mock(status_code=200, headers={})
        client = Mock()
        client.get.side_effect = [busy, success]

        result = _get_with_retry(client, "https://example.com/chapters")

        self.assertIs(result, success)
        sleep_mock.assert_called_once()

    @patch("audio.crawler.time.sleep")
    def test_timeout_error_identifies_host_and_attempt_count(self, _sleep_mock):
        client = Mock()
        client.get.side_effect = httpx.ReadTimeout("timed out")

        with self.assertRaisesRegex(TimeoutError, r"example\.com.*3 lần thử"):
            _get_with_retry(client, "https://example.com/chapters")


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

    def test_extracts_only_links_for_the_requested_novel(self):
        crawler = MistmintHavenCrawler("rolling-in-bed-with-the-male-lead")
        soup = BeautifulSoup(
            """
            <a href="/novels/rolling-in-bed-with-the-male-lead/chapter-2">Second</a>
            <a href="/novels/another-novel/chapter-1">Wrong novel</a>
            <a href="/novels/rolling-in-bed-with-the-male-lead/chapter-1"> Chapter 1 </a>
            <a href="/novels/rolling-in-bed-with-the-male-lead/chapter-2">Duplicate</a>
            """,
            "html.parser",
        )

        chapters = crawler.extract_chapters_from_links(soup)

        self.assertEqual([chapter["chapter_number"] for chapter in chapters], [1, 2])
        self.assertEqual(chapters[0]["title"], "Chapter 1")
        self.assertTrue(chapters[1]["url"].endswith("/chapter-2"))

    def test_parses_volume_grouped_api_and_skips_hidden_or_non_numeric_entries(self):
        crawler = MistmintHavenCrawler("rolling-in-bed-with-the-male-lead")
        payload = {
            "data": [{
                "chapters": [
                    {"slug": "chapter-prologue", "title": None, "isHidden": False},
                    {"slug": "chapter-2", "title": "A New Day", "isHidden": False},
                    {"slug": "chapter-1", "title": None, "isHidden": False},
                    {"slug": "chapter-3", "title": None, "isHidden": True},
                ]
            }]
        }

        chapters = crawler._chapters_from_api_payload(payload)

        self.assertEqual(
            chapters,
            [
                {
                    "chapter_number": 1,
                    "title": "Chapter 1",
                    "url": f"{crawler.novel_url}/chapter-1",
                },
                {
                    "chapter_number": 2,
                    "title": "Chapter 2: A New Day",
                    "url": f"{crawler.novel_url}/chapter-2",
                },
            ],
        )

    def test_parses_multivolume_and_side_story_slugs(self):
        crawler = MistmintHavenCrawler("the-second-prince-wants-to-read-romance-novels")
        payload = {
            "data": [
                {
                    "volumeTitle": "Volume 1",
                    "chapters": [
                        {"slug": "volume-1-chapter-1", "chapterNumber": "1", "title": None, "price": 0, "isHidden": False},
                        {"slug": "volume-1-chapter-30", "chapterNumber": "30", "title": "End of Volume 1", "price": 0, "isHidden": False},
                    ]
                },
                {
                    "volumeTitle": "Side Story",
                    "chapters": [
                        {"slug": "side-story-chapter-116", "chapterNumber": "116", "title": None, "price": 8, "isHidden": False},
                        {"slug": "side-story-chapter-120", "chapterNumber": "120", "title": "End of Side Story", "price": 10, "isHidden": False},
                    ]
                }
            ]
        }

        chapters = crawler._chapters_from_api_payload(payload)

        self.assertEqual(len(chapters), 4)
        self.assertEqual(chapters[0]["chapter_number"], 1)
        self.assertEqual(chapters[0]["title"], "Chapter 1")
        self.assertEqual(chapters[0]["url"], f"{crawler.novel_url}/volume-1-chapter-1")
        self.assertEqual(chapters[0]["price"], 0)

        self.assertEqual(chapters[1]["chapter_number"], 30)
        self.assertEqual(chapters[1]["title"], "Chapter 30: End of Volume 1")
        self.assertEqual(chapters[1]["price"], 0)

        self.assertEqual(chapters[2]["chapter_number"], 116)
        self.assertEqual(chapters[2]["title"], "Chapter 116")
        self.assertEqual(chapters[2]["price"], 8)

        self.assertEqual(chapters[3]["chapter_number"], 120)
        self.assertEqual(chapters[3]["title"], "Chapter 120: End of Side Story")
        self.assertEqual(chapters[3]["price"], 10)



class HyacinthBloomSeriesTests(unittest.TestCase):
    def test_extracts_deduplicates_and_sorts_chapter_links(self):
        html = """
        <html><body>
          <h1 class="entry-title">Earth Hero's Retirement Project</h1>
          <a href="/novel/chapter-2/">Ch. 2 The Second Chapter</a>
          <a href="/novel/side-story-10/">Ch. Side Story 10 Rehabilitation (10)</a>
          <a href="/novel/chapter-1/">Ch. 1 The First Chapter</a>
          <a href="/novel/chapter-2/">Ch. 2 The Second Chapter</a>
          <a href="/about/">About us</a>
        </body></html>
        """

        result = _parse_hyacinth_series_chapters(
            html,
            "https://hyacinthbloom.com/series/earth-heros-retirement-project/",
        )

        self.assertEqual(result["series_title"], "Earth Hero's Retirement Project")
        self.assertEqual(
            [(chapter["chapter_number"], chapter["title"]) for chapter in result["chapters"]],
            [
                (1, "Ch. 1 The First Chapter"),
                (2, "Ch. 2 The Second Chapter"),
                (10, "Ch. Side Story 10 Rehabilitation (10)"),
            ],
        )
        self.assertEqual(
            result["chapters"][0]["url"],
            "https://hyacinthbloom.com/novel/chapter-1/",
        )
        self.assertEqual(result["chapters"][2]["slug"], "side-story-10")


class PieNovelsSeriesTests(unittest.TestCase):
    def test_extracts_paid_and_free_chapters_in_numeric_order(self):
        html = """
        <h1 class="single-novel-title">A Test Novel</h1>
        <a class="paid-class2" href="/chapters/chapter-2-second-title/">
          <span class="paid-span">160</span>
          <p>Chapter 2: Second Title</p>
          <span>6 months ago</span>
        </a>
        <a class="free-class" href="https://pienovels.com/chapters/chapter-1-first-title/">
          <span>Free</span><p>Chapter 1: First Title</p>
        </a>
        <a href="https://other.example/chapters/chapter-3-wrong-site/">
          <p>Chapter 3: Wrong Site</p>
        </a>
        <a href="/chapters/chapter-2-second-title/"><p>Chapter 2: Second Title</p></a>
        """

        result = _parse_pienovels_series_chapters(
            html,
            "https://pienovels.com/novels/a-test-novel/",
        )

        self.assertEqual(result["series_title"], "A Test Novel")
        self.assertEqual(
            [(chapter["chapter_number"], chapter["title"]) for chapter in result["chapters"]],
            [(1, "First Title"), (2, "Second Title")],
        )
        self.assertEqual(result["chapters"][0]["price"], 0)
        self.assertEqual(result["chapters"][1]["slug"], "chapter-2-second-title")


if __name__ == "__main__":
    unittest.main()
