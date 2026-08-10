"""
🗄️ db.py – Audio Metadata Database (Turso DB / SQLite)
Stores AudioProject, AudioChapter, and PlaybackState records.

Backend selection (automatic):
  - TURSO_DATABASE_URL + TURSO_AUTH_TOKEN set → Turso via HTTP (hrana) using httpx
  - Otherwise → local SQLite (data/audio_database.db)

No native Rust/C compilation required – httpx is used for all Turso calls.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── Auto-load .env so Turso credentials are available everywhere ──────
try:
    from dotenv import load_dotenv as _load_dotenv
    _load_dotenv(Path(__file__).resolve().parents[2] / '.env', override=False)
except Exception:
    pass

BASE_DIR = Path(__file__).resolve().parents[2]  # trans-tool root
DATA_DIR = BASE_DIR / "data"
DB_PATH  = DATA_DIR / "audio_database.db"


def _get_env(key: str) -> str:
    """Read from streamlit secrets first, then os.environ."""
    try:
        import streamlit as st
        val = st.secrets.get(key)
        if val:
            return str(val)
    except Exception:
        pass
    return os.environ.get(key, "")


# ═══════════════════════════════════════════════════════════════════════
# 1. DATA CLASSES  (returned by all CRUD helpers)
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class AudioProject:
    id: int
    title: str
    source_type: str
    source_url: str | None
    project_slug: str
    created_at: datetime | None = None


@dataclass
class AudioChapter:
    id: int
    project_id: int
    chapter_number: int
    chapter_slug: str
    title: str
    audio_url: str | None
    duration_seconds: float
    text_content: str | None
    voice_label: str | None
    word_count: int
    created_at: datetime | None = None
    playback: Any = None  # PlaybackState or None


@dataclass
class PlaybackState:
    id: int
    chapter_id: int
    last_position_sec: float
    updated_at: datetime | None = None


# ═══════════════════════════════════════════════════════════════════════
# 2. TURSO HTTP CLIENT
# ═══════════════════════════════════════════════════════════════════════

class _TursoClient:
    """Thin wrapper around the Turso hrana-over-HTTP REST API."""

    def __init__(self, db_url: str, auth_token: str):
        import httpx
        self._db_url  = db_url.rstrip("/")
        self._token   = auth_token
        self._http    = httpx.Client(
            timeout=30,
            headers={
                "Authorization": f"Bearer {auth_token}",
                "Content-Type": "application/json",
            },
        )

    def execute(self, sql: str, args: list | None = None) -> dict:
        payload = {
            "requests": [
                {
                    "type": "execute",
                    "stmt": {
                        "sql": sql,
                        "args": [self._encode(a) for a in (args or [])],
                    },
                },
                {"type": "close"},
            ]
        }
        resp = self._http.post(f"{self._db_url}/v2/pipeline", content=json.dumps(payload))
        resp.raise_for_status()
        data = resp.json()
        result = data["results"][0]
        if result.get("type") == "error":
            raise RuntimeError(result["error"]["message"])
        return result.get("response", {}).get("result", {})

    @staticmethod
    def _encode(v: Any) -> dict:
        if v is None:
            return {"type": "null"}
        if isinstance(v, bool):
            return {"type": "integer", "value": str(int(v))}
        if isinstance(v, int):
            return {"type": "integer", "value": str(v)}
        if isinstance(v, float):
            return {"type": "float", "value": v}
        return {"type": "text", "value": str(v)}

    @staticmethod
    def _decode_rows(result: dict) -> list[dict]:
        cols = [c["name"] for c in result.get("cols", [])]
        rows = []
        for row in result.get("rows", []):
            record = {}
            for col, cell in zip(cols, row):
                t = cell.get("type", "null")
                if t == "null":
                    record[col] = None
                elif t == "integer":
                    record[col] = int(cell["value"])
                elif t == "float":
                    record[col] = float(cell["value"])
                else:
                    record[col] = cell.get("value")
            rows.append(record)
        return rows

    def fetch(self, sql: str, args: list | None = None) -> list[dict]:
        result = self.execute(sql, args)
        return self._decode_rows(result)

    def fetch_one(self, sql: str, args: list | None = None) -> dict | None:
        rows = self.fetch(sql, args)
        return rows[0] if rows else None

    def last_insert_rowid(self) -> int:
        r = self.fetch_one("SELECT last_insert_rowid() AS id")
        return int(r["id"]) if r else 0


# ═══════════════════════════════════════════════════════════════════════
# 3. SQLITE LOCAL CLIENT
# ═══════════════════════════════════════════════════════════════════════

class _SQLiteClient:
    """Thin wrapper around stdlib sqlite3 for local use."""

    def __init__(self, db_path: Path):
        DATA_DIR.mkdir(exist_ok=True)
        self._path = db_path
        self._conn: sqlite3.Connection | None = None

    def _get_conn(self) -> sqlite3.Connection:
        if self._conn is None:
            self._conn = sqlite3.connect(str(self._path), check_same_thread=False)
            self._conn.row_factory = sqlite3.Row
        return self._conn

    def execute(self, sql: str, args: list | None = None) -> sqlite3.Cursor:
        return self._get_conn().execute(sql, args or [])

    def fetch(self, sql: str, args: list | None = None) -> list[dict]:
        cur = self.execute(sql, args)
        return [dict(row) for row in cur.fetchall()]

    def fetch_one(self, sql: str, args: list | None = None) -> dict | None:
        rows = self.fetch(sql, args)
        return rows[0] if rows else None

    def commit(self) -> None:
        if self._conn:
            self._conn.commit()

    def last_insert_rowid(self) -> int:
        r = self.fetch_one("SELECT last_insert_rowid() AS id")
        return int(r["id"]) if r else 0


# ═══════════════════════════════════════════════════════════════════════
# 4. DB SINGLETON
# ═══════════════════════════════════════════════════════════════════════

_db_client = None


def _get_db() -> "_TursoClient | _SQLiteClient":
    global _db_client
    try:
        import streamlit as st

        @st.cache_resource
        def _cached_db():
            return _build_db()
        return _cached_db()
    except Exception:
        pass

    if _db_client is None:
        _db_client = _build_db()
    return _db_client


def _build_db() -> "_TursoClient | _SQLiteClient":
    db_url     = _get_env("TURSO_DATABASE_URL")
    auth_token = _get_env("TURSO_AUTH_TOKEN")
    if db_url and auth_token:
        # Convert libsql:// → https:// for the HTTP API
        http_url = db_url.replace("libsql://", "https://")
        try:
            client = _TursoClient(http_url, auth_token)
            client.fetch("SELECT 1")  # connectivity check
            return client
        except Exception as e:
            import warnings
            warnings.warn(f"[audio/db] Turso connection failed ({e}), falling back to SQLite.")
    return _SQLiteClient(DB_PATH)


# ═══════════════════════════════════════════════════════════════════════
# 5. SCHEMA INIT
# ═══════════════════════════════════════════════════════════════════════

_DDL = [
    """CREATE TABLE IF NOT EXISTS audio_projects (
        id           INTEGER PRIMARY KEY AUTOINCREMENT,
        title        TEXT    NOT NULL,
        source_type  TEXT    NOT NULL DEFAULT 'web_crawler',
        source_url   TEXT,
        project_slug TEXT    NOT NULL UNIQUE,
        created_at   TEXT    DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
    )""",
    """CREATE TABLE IF NOT EXISTS audio_chapters (
        id               INTEGER PRIMARY KEY AUTOINCREMENT,
        project_id       INTEGER NOT NULL REFERENCES audio_projects(id) ON DELETE CASCADE,
        chapter_number   INTEGER NOT NULL DEFAULT 0,
        chapter_slug     TEXT    NOT NULL,
        title            TEXT    NOT NULL,
        audio_url        TEXT,
        duration_seconds REAL    NOT NULL DEFAULT 0.0,
        text_content     TEXT,
        voice_label      TEXT,
        word_count       INTEGER NOT NULL DEFAULT 0,
        created_at       TEXT    DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
    )""",
    """CREATE TABLE IF NOT EXISTS audio_playback_state (
        id                INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_id        INTEGER NOT NULL UNIQUE REFERENCES audio_chapters(id) ON DELETE CASCADE,
        last_position_sec REAL    NOT NULL DEFAULT 0.0,
        updated_at        TEXT    DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ','now'))
    )""",
]


def init_db() -> None:
    """Create all tables if they don't exist."""
    db = _get_db()
    for ddl in _DDL:
        db.execute(ddl)
    if isinstance(db, _SQLiteClient):
        db.commit()


# ═══════════════════════════════════════════════════════════════════════
# 6. ROW → DATACLASS HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _parse_dt(s: str | None) -> datetime | None:
    if not s:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _row_to_project(row: dict) -> AudioProject:
    return AudioProject(
        id=int(row["id"]),
        title=row["title"],
        source_type=row["source_type"],
        source_url=row.get("source_url"),
        project_slug=row["project_slug"],
        created_at=_parse_dt(row.get("created_at")),
    )


def _row_to_chapter(row: dict) -> AudioChapter:
    return AudioChapter(
        id=int(row["id"]),
        project_id=int(row["project_id"]),
        chapter_number=int(row.get("chapter_number", 0)),
        chapter_slug=row["chapter_slug"],
        title=row["title"],
        audio_url=row.get("audio_url"),
        duration_seconds=float(row.get("duration_seconds", 0.0)),
        text_content=row.get("text_content"),
        voice_label=row.get("voice_label"),
        word_count=int(row.get("word_count", 0)),
        created_at=_parse_dt(row.get("created_at")),
    )


# ═══════════════════════════════════════════════════════════════════════
# 7. CRUD HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_]+', '-', s)
    return s[:80] or 'audio-project'


def _unique_slug(base: str) -> str:
    db = _get_db()
    candidate = base
    suffix = 2
    while True:
        row = db.fetch_one(
            "SELECT id FROM audio_projects WHERE project_slug = ?", [candidate]
        )
        if row is None:
            return candidate
        candidate = f"{base}-{suffix}"
        suffix += 1


# ── Projects ──────────────────────────────────────────────────────────

def upsert_project(
    title: str,
    source_type: str,
    source_url: str | None,
    project_slug: str,
) -> AudioProject:
    """Get or create an AudioProject by slug. Updates metadata if slug already exists."""
    db = _get_db()
    row = db.fetch_one(
        "SELECT * FROM audio_projects WHERE project_slug = ?", [project_slug]
    )
    if row:
        db.execute(
            "UPDATE audio_projects SET title=?, source_type=?, source_url=? WHERE project_slug=?",
            [title, source_type, source_url, project_slug],
        )
        if isinstance(db, _SQLiteClient):
            db.commit()
        row = db.fetch_one(
            "SELECT * FROM audio_projects WHERE project_slug = ?", [project_slug]
        )
    else:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        db.execute(
            "INSERT INTO audio_projects (title, source_type, source_url, project_slug, created_at) VALUES (?,?,?,?,?)",
            [title, source_type, source_url, project_slug, now],
        )
        if isinstance(db, _SQLiteClient):
            db.commit()
        rowid = db.last_insert_rowid()
        row = db.fetch_one("SELECT * FROM audio_projects WHERE id=?", [rowid])
    return _row_to_project(row)


def create_project(
    title: str,
    source_type: str = "pasted_text",
    source_url: str | None = None,
    project_slug: str | None = None,
) -> AudioProject:
    """Always create a brand-new AudioProject with a guaranteed-unique slug."""
    db = _get_db()
    base = project_slug or _slugify(title) or 'audio-project'
    slug = _unique_slug(base)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    db.execute(
        "INSERT INTO audio_projects (title, source_type, source_url, project_slug, created_at) VALUES (?,?,?,?,?)",
        [title, source_type, source_url, slug, now],
    )
    if isinstance(db, _SQLiteClient):
        db.commit()
    rowid = db.last_insert_rowid()
    row = db.fetch_one("SELECT * FROM audio_projects WHERE id=?", [rowid])
    return _row_to_project(row)


def list_projects() -> list[AudioProject]:
    db = _get_db()
    rows = db.fetch("SELECT * FROM audio_projects ORDER BY created_at DESC")
    return [_row_to_project(r) for r in rows]


def update_project_source_url(project_id: int, source_url: str) -> AudioProject:
    """Save the chapter-list source URL associated with an existing project."""
    source_url = source_url.strip()
    if not source_url:
        raise ValueError("source_url must not be empty")

    db = _get_db()
    db.execute(
        "UPDATE audio_projects SET source_url=? WHERE id=?",
        [source_url, project_id],
    )
    if isinstance(db, _SQLiteClient):
        db.commit()
    row = db.fetch_one("SELECT * FROM audio_projects WHERE id=?", [project_id])
    if row is None:
        raise ValueError(f"Audio project not found: {project_id}")
    return _row_to_project(row)


def delete_project(project_id: int) -> None:
    db = _get_db()
    db.execute("DELETE FROM audio_projects WHERE id=?", [project_id])
    if isinstance(db, _SQLiteClient):
        db.commit()


# ── Chapters ──────────────────────────────────────────────────────────

def save_chapter(
    project_id: int,
    chapter_number: int,
    chapter_slug: str,
    title: str,
    audio_url: str,
    duration_seconds: float,
    text_content: str,
    voice_label: str,
    word_count: int,
) -> AudioChapter:
    """Insert or update an AudioChapter record."""
    db = _get_db()
    row = db.fetch_one(
        "SELECT id FROM audio_chapters WHERE project_id=? AND chapter_slug=?",
        [project_id, chapter_slug],
    )
    if row:
        db.execute(
            "UPDATE audio_chapters SET audio_url=?, duration_seconds=?, text_content=?, voice_label=?, word_count=? WHERE id=?",
            [audio_url, duration_seconds, text_content, voice_label, word_count, row["id"]],
        )
        if isinstance(db, _SQLiteClient):
            db.commit()
        updated = db.fetch_one("SELECT * FROM audio_chapters WHERE id=?", [row["id"]])
        return _row_to_chapter(updated)
    else:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        db.execute(
            "INSERT INTO audio_chapters (project_id, chapter_number, chapter_slug, title, audio_url, duration_seconds, text_content, voice_label, word_count, created_at) VALUES (?,?,?,?,?,?,?,?,?,?)",
            [project_id, chapter_number, chapter_slug, title, audio_url, duration_seconds, text_content, voice_label, word_count, now],
        )
        if isinstance(db, _SQLiteClient):
            db.commit()
        rowid = db.last_insert_rowid()
        new_row = db.fetch_one("SELECT * FROM audio_chapters WHERE id=?", [rowid])
        return _row_to_chapter(new_row)


def list_chapters(project_id: int) -> list[AudioChapter]:
    db = _get_db()
    rows = db.fetch(
        "SELECT * FROM audio_chapters WHERE project_id=? ORDER BY chapter_number",
        [project_id],
    )
    return [_row_to_chapter(r) for r in rows]


def delete_chapter(chapter_id: int) -> None:
    db = _get_db()
    db.execute("DELETE FROM audio_chapters WHERE id=?", [chapter_id])
    if isinstance(db, _SQLiteClient):
        db.commit()


# ── Playback State ────────────────────────────────────────────────────

def save_playback_state(chapter_id: int, position_sec: float) -> None:
    db = _get_db()
    row = db.fetch_one(
        "SELECT id FROM audio_playback_state WHERE chapter_id=?", [chapter_id]
    )
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if row:
        db.execute(
            "UPDATE audio_playback_state SET last_position_sec=?, updated_at=? WHERE chapter_id=?",
            [position_sec, now_str, chapter_id],
        )
    else:
        db.execute(
            "INSERT INTO audio_playback_state (chapter_id, last_position_sec, updated_at) VALUES (?,?,?)",
            [chapter_id, position_sec, now_str],
        )
    if isinstance(db, _SQLiteClient):
        db.commit()


def get_playback_state(chapter_id: int) -> float:
    db = _get_db()
    row = db.fetch_one(
        "SELECT last_position_sec FROM audio_playback_state WHERE chapter_id=?",
        [chapter_id],
    )
    return float(row["last_position_sec"]) if row else 0.0


def get_latest_listened_chapter(project_id: int) -> tuple[AudioChapter | None, float]:
    """Return (AudioChapter, position_sec) for the most recently listened chapter in a project."""
    db = _get_db()
    sql = """
        SELECT c.*, s.last_position_sec
        FROM audio_playback_state s
        JOIN audio_chapters c ON s.chapter_id = c.id
        WHERE c.project_id = ?
        ORDER BY s.updated_at DESC
        LIMIT 1
    """
    row = db.fetch_one(sql, [project_id])
    if not row:
        return None, 0.0
    ch = _row_to_chapter(row)
    pos = float(row.get("last_position_sec", 0.0))
    return ch, pos


def get_latest_listened_all_projects() -> dict[int, tuple[int, str, float]]:
    """Return map of project_id -> (chapter_number, chapter_title, position_sec) for all projects."""
    db = _get_db()
    sql = """
        SELECT c.project_id, c.chapter_number, c.title, s.last_position_sec
        FROM audio_playback_state s
        JOIN audio_chapters c ON s.chapter_id = c.id
        WHERE s.updated_at = (
            SELECT MAX(s2.updated_at)
            FROM audio_playback_state s2
            JOIN audio_chapters c2 ON s2.chapter_id = c2.id
            WHERE c2.project_id = c.project_id
        )
    """
    try:
        rows = db.fetch(sql)
        res = {}
        for r in rows:
            res[int(r["project_id"])] = (
                int(r.get("chapter_number", 0)),
                r.get("title", ""),
                float(r.get("last_position_sec", 0.0)),
            )
        return res
    except Exception:
        return {}

