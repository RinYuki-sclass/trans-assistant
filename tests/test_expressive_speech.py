"""Regression checks for expressive Audio Converter preprocessing."""

import os
import sys
import unittest


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio.tts_engine import VOICES, apply_expressive_speech, prepare_text_for_speech


class ExpressiveSpeechTests(unittest.TestCase):
    def test_brian_multilingual_voice_uses_edge_without_google_substitution(self):
        self.assertEqual(
            VOICES["🌐 Brian (Multilingual, US)"],
            ("en-US", "", "en-US-BrianMultilingualNeural"),
        )

    def test_expands_initial_sound_stutter(self):
        self.assertEqual(
            apply_expressive_speech("W-wait for me."),
            "Wait… wait for me.",
        )

    def test_expands_repeated_word_stutter(self):
        self.assertEqual(
            apply_expressive_speech("I-I-I can't."),
            "I… I… I can't.",
        )

    def test_replaces_bracketed_gasp_cues(self):
        self.assertEqual(
            apply_expressive_speech("She froze. *gasps* No!"),
            "She froze. Ah! No!",
        )
        self.assertEqual(
            apply_expressive_speech("[sharp inhale] Không!", "vi-VN"),
            "Á! Không!",
        )

    def test_preserves_normal_hyphenated_words_and_names(self):
        source = "well-being, mother-in-law, and Hyun-jae"
        self.assertEqual(apply_expressive_speech(source), source)

    def test_empty_text(self):
        self.assertEqual(apply_expressive_speech(""), "")

    def test_pronunciation_preview_matches_tts_preprocessing(self):
        self.assertEqual(
            prepare_text_for_speech(
                "H-Hyunjae met Cheon.",
                custom_map={"Hyunjae": "Hyeon-jae"},
                use_default_korean=True,
            ),
            "Hyeon-jae… Hyeon-jae met Chun.",
        )

    def test_pronunciation_preview_can_disable_optional_processing(self):
        source = "H-Hyunjae met Cheon."
        self.assertEqual(
            prepare_text_for_speech(
                source,
                custom_map={"Hyunjae": "Hyeon-jae"},
                use_default_korean=False,
                enhance_expressive_speech=False,
            ),
            "H-Hyeon-jae met Cheon.",
        )


if __name__ == "__main__":
    unittest.main()
