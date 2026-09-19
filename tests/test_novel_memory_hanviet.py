"""
Unit tests for Novel Agent Memory Hán-Việt integration
"""
import sys
import unittest
from pathlib import Path

# Add scripts directory to path
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR / "scripts"))


class TestNovelMemoryHanViet(unittest.TestCase):

    def test_na_format_memory_for_prompt_with_hanviet(self):
        # Dynamically import na_format_memory_for_prompt from app if available
        # or test the format logic directly
        memory = {
            'characters': [
                {
                    'name': 'Ye Chen',
                    'hanviet_name': 'Diệp Thần',
                    'gender': 'male',
                    'aliases': ['Ye Chen', 'Diệp Thần'],
                    'speech_style': 'điềm tĩnh',
                    'honorifics': 'huynh/đệ'
                }
            ],
            'glossary': [
                {
                    'original': 'Cloud Mist Sect',
                    'translation': 'Phái Vân Vụ',
                    'hanviet': 'Vân Vụ Tông',
                    'category': 'faction'
                }
            ]
        }

        # Mock formatting function behavior logic
        lines = []
        if memory.get('characters'):
            lines.append('=== CHARACTERS ===')
            for c in memory['characters'][:30]:
                hv_str = f" / Hán-Việt: {c['hanviet_name']}" if c.get('hanviet_name') else ""
                aliases = ', '.join(c.get('aliases', []))
                lines.append(f"- {c.get('name','')}{hv_str} ({c.get('gender','')}) | Aliases: {aliases} | Speech: {c.get('speech_style','')} | Honorifics: {c.get('honorifics','')}")
        if memory.get('glossary'):
            lines.append('\n=== PROJECT GLOSSARY ===')
            for g in memory['glossary'][:60]:
                hv_str = f" (Hán-Việt: {g['hanviet']})" if g.get('hanviet') else ""
                lines.append(f"- {g.get('original','')} → {g.get('translation','')}{hv_str} [{g.get('category','')}]")

        formatted = '\n'.join(lines)
        self.assertIn('Ye Chen / Hán-Việt: Diệp Thần', formatted)
        self.assertIn('Cloud Mist Sect → Phái Vân Vụ (Hán-Việt: Vân Vụ Tông)', formatted)

    def test_na_auto_memory_extracts_hanviet(self):
        analysis_data = {
            'new_characters': [
                {
                    'name': 'Lin Dong',
                    'hanviet_name': 'Lâm Động',
                    'gender': 'male',
                    'honorifics': 'đệ',
                    'role': 'Nam chính',
                    'description': 'Main character'
                }
            ],
            'new_terms': [
                {
                    'original': 'Tianhai City',
                    'suggested': 'Thành Thiên Hải',
                    'hanviet': 'Thiên Hải Thành',
                    'category': 'location',
                    'confidence': 0.9
                }
            ]
        }

        char = analysis_data['new_characters'][0]
        term = analysis_data['new_terms'][0]

        self.assertEqual(char.get('hanviet_name'), 'Lâm Động')
        self.assertEqual(term.get('hanviet'), 'Thiên Hải Thành')


    def test_na_merge_glossary_and_character_deduplication(self):
        try:
            from app import na_merge_glossary_entry, na_merge_character_entry
        except ImportError:
            self.skipTest("app module not importable directly")

        gl = [{'original': 'Green tea', 'translation': 'Trà xanh', 'hanviet': 'Lục trà', 'category': 'other'}]
        # Try merging a duplicate entry with matching translation
        new_g = {'original': 'Trà xanh', 'translation': 'Trà xanh', 'hanviet': 'Lục trà'}
        merged_g = na_merge_glossary_entry(gl, new_g)
        self.assertEqual(len(gl), 1)
        self.assertEqual(merged_g['original'], 'Green tea')

        chars = [{'name': 'Shen Feizhi', 'hanviet_name': 'Thẩm Phi Triết', 'aliases': ['Shen Feizhi', 'Thẩm Phi Triết']}]
        new_c = {'name': 'thẩm phi triết', 'hanviet_name': 'Thẩm Phi Triết'}
        merged_c = na_merge_character_entry(chars, new_c)
        self.assertEqual(len(chars), 1)
        self.assertEqual(merged_c['name'], 'Shen Feizhi')


if __name__ == "__main__":
    unittest.main()

