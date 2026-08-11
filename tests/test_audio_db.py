"""Tests for audio-project metadata updates."""

import os
import sys
import tempfile
import unittest
from pathlib import Path
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


class _FakeChapterInsertDb:
    def fetch_one(self, sql, args):
        if sql.startswith("SELECT id FROM audio_chapters"):
            return None
        if sql.startswith("INSERT INTO audio_chapters") and "RETURNING *" in sql:
            return {
                "id": 12,
                "project_id": args[0],
                "chapter_number": args[1],
                "chapter_slug": args[2],
                "title": args[3],
                "audio_url": args[4],
                "duration_seconds": args[5],
                "text_content": args[6],
                "voice_label": args[7],
                "word_count": args[8],
                "created_at": args[9],
            }
        raise AssertionError(f"Unexpected query: {sql}")


class _FakePlaybackDb:
    def __init__(self):
        self.executed = None

    def fetch_one(self, sql, args):
        return None

    def execute(self, sql, args):
        self.executed = (sql, args)


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

    def test_inserts_chapter_with_returning_in_one_database_request(self):
        with patch.object(audio_db, "_get_db", return_value=_FakeChapterInsertDb()):
            chapter = audio_db.save_chapter(
                project_id=7,
                chapter_number=3,
                chapter_slug="chapter-3",
                title="Chapter 3: A Fate He Refuses to Escape",
                audio_url="https://audio.example/chapter-3.mp3",
                duration_seconds=120.5,
                text_content="Chapter text",
                voice_label="Brian Multilingual",
                word_count=250,
            )

        self.assertEqual(chapter.id, 12)
        self.assertEqual(chapter.chapter_number, 3)
        self.assertEqual(chapter.title, "Chapter 3: A Fate He Refuses to Escape")

    def test_playback_timestamp_has_subsecond_precision(self):
        fake_db = _FakePlaybackDb()
        with patch.object(audio_db, "_get_db", return_value=fake_db):
            audio_db.save_playback_state(12, 34.5)

        _, args = fake_db.executed
        self.assertRegex(args[2], r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z$")

    def test_summary_schema_migrates_and_persists_content(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            db = audio_db._SQLiteClient(Path(temp_dir) / "audio.db")
            # Simulate an existing database created before chapter summaries.
            db.execute(
                "CREATE TABLE audio_chapters ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER NOT NULL, "
                "chapter_number INTEGER NOT NULL DEFAULT 0, chapter_slug TEXT NOT NULL, "
                "title TEXT NOT NULL, audio_url TEXT, duration_seconds REAL NOT NULL DEFAULT 0, "
                "text_content TEXT, voice_label TEXT, word_count INTEGER NOT NULL DEFAULT 0, created_at TEXT)"
            )
            with patch.object(audio_db, "_get_db", return_value=db):
                audio_db.init_db()
                project = audio_db.create_project("Summary Project", "web_crawler")
                chapter = audio_db.save_chapter(
                    project.id, 1, "chapter-1", "Chapter 1", "https://audio", 10.0,
                    "Full chapter text", "Voice", 3,
                )
                updated = audio_db.save_chapter_summary(
                    chapter.id, "Stored summary", "gemini-test", "source-hash"
                )

            columns = {row["name"] for row in db.fetch("PRAGMA table_info(audio_chapters)")}
            self.assertIn("summary_text", columns)
            self.assertEqual(updated.summary_text, "Stored summary")
            self.assertEqual(updated.summary_model, "gemini-test")
            self.assertEqual(updated.summary_source_hash, "source-hash")
            self.assertIsNotNone(updated.summarized_at)
            db._conn.close()


if __name__ == "__main__":
    unittest.main()
