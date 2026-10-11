#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests/test_manhwa_pipeline.py
Unit tests verifying the Manhwa Translation Pipeline components:
1. Image processor functions (sort, slice, optimize)
2. Format compatibility with Web Streamlit parser (Tab 5 side-by-side, Tab 9 reformat, Google Doc regex)
"""

import os
import sys
import re
import unittest
from PIL import Image

# Add project root to sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.manhwa_image_processor import (
    get_windows_sort_key,
    sort_image_files,
    split_long_image,
    optimize_image_for_api,
    find_smart_cut_y
)


class TestManhwaPipeline(unittest.TestCase):

    def test_windows_sort(self):
        files = ["chapter_10.jpg", "chapter_2.jpg", "chapter_1.jpg", "chapter_1 (1).jpg", "chapter_1 (2).jpg"]
        sorted_files = sorted(files, key=get_windows_sort_key)
        expected = ["chapter_1.jpg", "chapter_1 (1).jpg", "chapter_1 (2).jpg", "chapter_2.jpg", "chapter_10.jpg"]
        self.assertEqual(sorted_files, expected)

    def test_smart_gutter_detection(self):
        # Create an image with an obvious white gutter band between y=2300 and y=2400
        test_img = Image.new("RGB", (800, 5000), color=(100, 100, 100))
        # Draw a white band (gutter) around 2350
        for y in range(2320, 2380):
            for x in range(800):
                test_img.putpixel((x, y), (255, 255, 255))
        
        cut_y, is_clean = find_smart_cut_y(test_img, target_y=2400, search_range=500)
        self.assertTrue(is_clean)
        self.assertTrue(2320 <= cut_y <= 2380)

    def test_image_split_and_optimize(self):
        # Create a tall dummy image: 800 x 6000 px
        test_img = Image.new("RGB", (800, 6000), color=(240, 240, 240))
        parts = split_long_image(test_img, max_h=2400, overlap=150)
        self.assertGreaterEqual(len(parts), 2)
        for p in parts:
            opt = optimize_image_for_api(p, max_w=1200, max_h=2800)
            self.assertIsInstance(opt, Image.Image)

    def test_web_side_by_side_parsing(self):
        sample_script = (
            "📄 ẢNH: 001.jpg\n\n"
            "[Han Yoojin]\n"
            "KR: 제 심장의 마석,\n"
            "Ma thạch trong ngực tôi,\n\n"
            "[Narrator]\n"
            "KR: 그 힘이 요동치기 시작했다.\n"
            "Năng lượng ấy bắt đầu rung chuyển dữ dội.\n\n"
            "📄 ẢNH: 002.jpg\n\n"
            "[Sung Hyunjae]\n"
            "KR: 한유진 군, 무슨 생각이지?\n"
            "Han Yoojin-gun, cậu đang nghĩ gì thế?\n"
        )

        # Logic from app.py:L2359
        parts = re.split(r'📄 ẢNH: (.*?)\n', sample_script)
        parsed_data = {}
        if len(parts) > 1:
            for i in range(1, len(parts), 2):
                fname = parts[i].strip()
                text = parts[i+1].strip() if i+1 < len(parts) else ""
                parsed_data[fname] = text

        self.assertIn("001.jpg", parsed_data)
        self.assertIn("002.jpg", parsed_data)
        self.assertIn("[Han Yoojin]", parsed_data["001.jpg"])
        self.assertIn("Ma thạch trong ngực tôi,", parsed_data["001.jpg"])
        self.assertIn("[Sung Hyunjae]", parsed_data["002.jpg"])

    def test_tab9_reformat_script(self):
        # Logic from app.py:L2944
        def reformat_translation_script(raw: str, case_mode: str, remove_empty_and_double_space: bool = False) -> str:
            result = []
            for line in raw.splitlines():
                stripped = line.strip()
                if not stripped:
                    continue
                if re.match(r'^\[.*\]', stripped):
                    continue
                if re.match(r'^KR\s*:', stripped):
                    continue
                result.append(line)
            join_char = '\n\n' if remove_empty_and_double_space else '\n'
            return join_char.join(result)

        input_text = (
            "[Han Yoojin]\n"
            "KR: 제 심장의 마석,\n"
            "Ma thạch trong ngực tôi,\n\n"
            "[Narrator]\n"
            "KR: 그 힘이 요동치기 시작했다.\n"
            "Năng lượng ấy bắt đầu rung chuyển dữ dội.\n\n"
            "[Sung Hyunjae]\n"
            "KR: 한유진 군, 무슨 생각이지?\n"
            "Han Yoojin-gun, cậu đang nghĩ gì thế?"
        )

        output_text = reformat_translation_script(input_text, case_mode="Giữ nguyên (As-is)")
        expected = (
            "Ma thạch trong ngực tôi,\n"
            "Năng lượng ấy bắt đầu rung chuyển dữ dội.\n"
            "Han Yoojin-gun, cậu đang nghĩ gì thế?"
        )
        self.assertEqual(output_text.strip(), expected.strip())

    def test_google_docs_tag_preservation(self):
        # Logic from app.py:L2533
        input_text = (
            "📄 ẢNH: 001.jpg\n\n"
            "[Han Yoojin]\n"
            "KR: 제 심장의 마석,\n"
            "Ma thạch trong ngực tôi,\n"
        )
        # Strips KR: and VI: prefixes, but keeps [Han Yoojin]
        gdoc_script = re.sub(r'^(?:KR|VI):\s*', '', input_text, flags=re.MULTILINE | re.IGNORECASE)
        self.assertIn("[Han Yoojin]", gdoc_script)
        self.assertNotIn("KR: ", gdoc_script)
        self.assertIn("Ma thạch trong ngực tôi,", gdoc_script)


if __name__ == "__main__":
    unittest.main()
