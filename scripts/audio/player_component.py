"""Bidirectional Streamlit component used by the audio playlist player."""

from __future__ import annotations

import os
from typing import Any

import streamlit.components.v1 as components


_COMPONENT_DIR = os.path.join(os.path.dirname(__file__), "player_frontend")
_audio_player = components.declare_component(
    "audio_playlist_player",
    path=_COMPONENT_DIR,
)


def render_audio_player(
    playlist: list[dict[str, Any]],
    initial_index: int,
    project_title: str,
    project_id: int,
) -> dict[str, Any] | None:
    """Render the player and return its latest playback event, if any."""
    return _audio_player(
        playlist=playlist,
        initialIndex=initial_index,
        projectTitle=project_title,
        key=f"audio_playlist_player_{project_id}",
        default=None,
    )
