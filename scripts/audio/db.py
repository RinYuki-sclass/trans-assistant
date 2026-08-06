"""
🗄️ db.py – Audio Metadata Database (Turso DB / SQLite)
Stores AudioProject, AudioChapter, and PlaybackState records.
Follows the same Turso DB connection pattern as D:\\Nhung\\Rin Anki\\services\\database.py.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from pathlib import Path

try:
    import libsql
    _LIBSQL_AVAILABLE = True
except ImportError:
    import sqlite3 as _sqlite3
    _LIBSQL_AVAILABLE = False

from sqlalchemy import (
    Column, DateTime, Float, ForeignKey, Integer, String, Text,
    create_engine, text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker

BASE_DIR = Path(__file__).resolve().parents[2]  # trans-tool root
DATA_DIR = BASE_DIR / "data"
DB_PATH  = DATA_DIR / "audio_database.db"


def _get_env(key: str) -> str:
    """Read from streamlit secrets first, then os.environ."""
    try:
        import streamlit as st
        val = st.secrets.get(key)
        if val:
            return val
    except Exception:
        pass
    return os.environ.get(key, "")


# ── SQLAlchemy Base ─────────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ── Models ──────────────────────────────────────────────────────────

class AudioProject(Base):
    """Represents a crawl / novel-agent audio project."""
    __tablename__ = "audio_projects"

    id: Mapped[int]         = mapped_column(Integer, primary_key=True)
    title: Mapped[str]      = mapped_column(String(255), nullable=False)
    source_type: Mapped[str] = mapped_column(String(32), nullable=False, default="web_crawler")
    # "web_crawler" | "pasted_text" | "novel_agent"
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    project_slug: Mapped[str]      = mapped_column(String(120), nullable=False, unique=True)
    created_at: Mapped[datetime]   = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    chapters: Mapped[list["AudioChapter"]] = relationship(
        back_populates="project", cascade="all, delete"
    )


class AudioChapter(Base):
    """A single synthesized chapter / section."""
    __tablename__ = "audio_chapters"

    id: Mapped[int]            = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int]    = mapped_column(ForeignKey("audio_projects.id"), nullable=False)
    chapter_number: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    chapter_slug: Mapped[str]  = mapped_column(String(120), nullable=False)
    title: Mapped[str]         = mapped_column(String(255), nullable=False)
    audio_url: Mapped[str | None]     = mapped_column(Text, nullable=True)  # Cloudflare R2 URL
    duration_seconds: Mapped[float]   = mapped_column(Float, default=0.0)
    text_content: Mapped[str | None]  = mapped_column(Text, nullable=True)
    voice_label: Mapped[str | None]   = mapped_column(String(120), nullable=True)
    word_count: Mapped[int]           = mapped_column(Integer, default=0)
    created_at: Mapped[datetime]      = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    project: Mapped[AudioProject] = relationship(back_populates="chapters")
    playback: Mapped["PlaybackState | None"] = relationship(
        back_populates="chapter", cascade="all, delete", uselist=False
    )


class PlaybackState(Base):
    """Persists last playback position per chapter."""
    __tablename__ = "audio_playback_state"

    id: Mapped[int]          = mapped_column(Integer, primary_key=True)
    chapter_id: Mapped[int]  = mapped_column(
        ForeignKey("audio_chapters.id"), unique=True, nullable=False
    )
    last_position_sec: Mapped[float] = mapped_column(Float, default=0.0)
    updated_at: Mapped[datetime]     = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )

    chapter: Mapped[AudioChapter] = relationship(back_populates="playback")


# ── LibSQL proxy (same as Rin Anki pattern) ─────────────────────────
class _LibSQLConnectionProxy:
    def __init__(self, conn):
        self._conn = conn

    def __getattr__(self, name):
        return getattr(self._conn, name)

    def create_function(self, *args, **kwargs):
        return None


def _get_connection():
    db_url    = _get_env("TURSO_DATABASE_URL")
    auth_token = _get_env("TURSO_AUTH_TOKEN")

    if _LIBSQL_AVAILABLE:
        if db_url and auth_token:
            conn = libsql.connect(database=db_url, auth_token=auth_token)
        else:
            DATA_DIR.mkdir(exist_ok=True)
            conn = libsql.connect(str(DB_PATH))
    else:
        DATA_DIR.mkdir(exist_ok=True)
        conn = _sqlite3.connect(str(DB_PATH), check_same_thread=False)

    return _LibSQLConnectionProxy(conn)


def _get_engine():
    try:
        import streamlit as st

        @st.cache_resource
        def _cached():
            return create_engine(
                "sqlite://",
                creator=_get_connection,
                pool_pre_ping=True,
                future=True,
            )
        return _cached()
    except Exception:
        # Outside Streamlit (e.g. tests)
        return create_engine(
            "sqlite://",
            creator=_get_connection,
            pool_pre_ping=True,
            future=True,
        )


def get_session() -> Session:
    return sessionmaker(bind=_get_engine(), future=True)()


def init_db() -> None:
    """Create all tables if they don't exist."""
    engine = _get_engine()
    Base.metadata.create_all(engine)


# ── CRUD helpers ─────────────────────────────────────────────────────

def upsert_project(title: str, source_type: str, source_url: str | None, project_slug: str) -> AudioProject:
    """Get or create an AudioProject by slug. If slug already exists, updates its metadata."""
    with get_session() as session:
        proj = session.query(AudioProject).filter_by(project_slug=project_slug).first()
        if not proj:
            proj = AudioProject(
                title=title,
                source_type=source_type,
                source_url=source_url,
                project_slug=project_slug,
            )
            session.add(proj)
        else:
            # Update existing project's metadata
            proj.title = title
            proj.source_type = source_type
            if source_url is not None:
                proj.source_url = source_url
        session.commit()
        session.refresh(proj)
        return proj


def create_project(title: str, source_type: str = "pasted_text", source_url: str | None = None, project_slug: str | None = None) -> AudioProject:
    """Always create a new AudioProject with a guaranteed-unique slug."""
    import re as _re

    def _slugify(s: str) -> str:
        s = s.lower().strip()
        s = _re.sub(r'[^\w\s-]', '', s)
        s = _re.sub(r'[\s_]+', '-', s)
        return s[:80] or 'audio-project'

    with get_session() as session:
        # Build base slug
        base_slug = project_slug or _slugify(title) or 'audio-project'
        candidate = base_slug
        suffix = 2
        while session.query(AudioProject).filter_by(project_slug=candidate).first() is not None:
            candidate = f"{base_slug}-{suffix}"
            suffix += 1

        proj = AudioProject(
            title=title,
            source_type=source_type,
            source_url=source_url,
            project_slug=candidate,
        )
        session.add(proj)
        session.commit()
        session.refresh(proj)
        return proj


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
    with get_session() as session:
        ch = session.query(AudioChapter).filter_by(
            project_id=project_id, chapter_slug=chapter_slug
        ).first()
        if ch:
            ch.audio_url        = audio_url
            ch.duration_seconds = duration_seconds
            ch.text_content     = text_content
            ch.voice_label      = voice_label
            ch.word_count       = word_count
        else:
            ch = AudioChapter(
                project_id=project_id,
                chapter_number=chapter_number,
                chapter_slug=chapter_slug,
                title=title,
                audio_url=audio_url,
                duration_seconds=duration_seconds,
                text_content=text_content,
                voice_label=voice_label,
                word_count=word_count,
            )
            session.add(ch)
        session.commit()
        session.refresh(ch)
        return ch


def list_projects() -> list[AudioProject]:
    with get_session() as session:
        return session.query(AudioProject).order_by(AudioProject.created_at.desc()).all()


def list_chapters(project_id: int) -> list[AudioChapter]:
    with get_session() as session:
        return (
            session.query(AudioChapter)
            .filter_by(project_id=project_id)
            .order_by(AudioChapter.chapter_number)
            .all()
        )


def save_playback_state(chapter_id: int, position_sec: float) -> None:
    with get_session() as session:
        ps = session.query(PlaybackState).filter_by(chapter_id=chapter_id).first()
        if ps:
            ps.last_position_sec = position_sec
            ps.updated_at = datetime.now(timezone.utc)
        else:
            ps = PlaybackState(chapter_id=chapter_id, last_position_sec=position_sec)
            session.add(ps)
        session.commit()


def get_playback_state(chapter_id: int) -> float:
    with get_session() as session:
        ps = session.query(PlaybackState).filter_by(chapter_id=chapter_id).first()
        return ps.last_position_sec if ps else 0.0


def delete_chapter(chapter_id: int) -> None:
    with get_session() as session:
        ch = session.query(AudioChapter).get(chapter_id)
        if ch:
            session.delete(ch)
            session.commit()


def delete_project(project_id: int) -> None:
    with get_session() as session:
        proj = session.query(AudioProject).get(project_id)
        if proj:
            session.delete(proj)
            session.commit()
