import os
import re
import sys
import unittest


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio.summarizer import clean_chapter_text, split_text, summarize_chapter


class AudioSummarizerTests(unittest.TestCase):
    def test_clean_text_preserves_paragraphs_and_removes_extra_whitespace(self):
        self.assertEqual(clean_chapter_text(" A   B \n\n\n C\tD "), "A B\n\nC D")

    def test_split_text_keeps_all_content(self):
        source = "First paragraph.\n\n" + ("Long sentence. " * 30)
        chunks = split_text(source, 120)
        self.assertGreater(len(chunks), 1)
        self.assertEqual(
            re.sub(r"\s+", " ", " ".join(chunks)).strip(),
            re.sub(r"\s+", " ", source).strip(),
        )

    def test_short_chapter_uses_one_ai_call(self):
        calls = []

        def generate(prompt, max_output_tokens):
            calls.append((prompt, max_output_tokens))
            return "Summary"

        summary, stats = summarize_chapter("Short chapter text.", "Chapter 1", generate)
        self.assertEqual(summary, "Summary")
        self.assertEqual(stats.ai_calls, 1)
        self.assertEqual(len(calls), 1)

    def test_long_chapter_uses_map_reduce(self):
        calls = []

        def generate(prompt, max_output_tokens):
            calls.append(prompt)
            return "Compact notes"

        _, stats = summarize_chapter(
            "Sentence with plot information. " * 100,
            "Chapter 2",
            generate,
            direct_token_limit=100,
            chunk_token_limit=100,
        )
        self.assertGreater(stats.chunk_count, 1)
        self.assertEqual(stats.ai_calls, stats.chunk_count + 1)
        self.assertEqual(len(calls), stats.ai_calls)


if __name__ == "__main__":
    unittest.main()
