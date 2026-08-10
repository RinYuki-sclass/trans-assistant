"""Tests for audio-project metadata updates."""

import os
import sys
import unittest
from unittest.mock import patch


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from audio import db as audio_db


class _FakeDb:
    def __init__(self):
        self.row = {
            "id": 7,
            "title": "Test Novel",
            "source_type": "web_crawler",
            "source_url": None,
            "project_slug": "test-novel",
            "created_at": None,
        }

    def execute(self, sql, args):
        if sql.startswith("UPDATE audio_projects") and args[1] == self.row["id"]:
            self.row["source_url"] = args[0]

    def fetch_one(self, sql, args):
        return dict(self.row) if args[0] == self.row["id"] else None


class AudioProjectSourceUrlTests(unittest.TestCase):
    def test_updates_existing_project_source_url(self):
        fake_db = _FakeDb()
        with patch.object(audio_db, "_get_db", return_value=fake_db):
            project = audio_db.update_project_source_url(
                7,
                "  https://example.com/series/test/  ",
            )

        self.assertEqual(project.source_url, "https://example.com/series/test/")

    def test_rejects_empty_source_url(self):
        with self.assertRaises(ValueError):
            audio_db.update_project_source_url(7, "  ")


if __name__ == "__main__":
    unittest.main()
