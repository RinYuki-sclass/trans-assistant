"""Regression checks for a no-rerun Audio Converter player."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class AudioPlayerFrontendTests(unittest.TestCase):
    def test_playback_events_do_not_trigger_streamlit_reruns(self):
        frontend = (
            ROOT / "scripts" / "audio" / "player_frontend" / "index.html"
        ).read_text(encoding="utf-8")

        self.assertNotIn("streamlit:setComponentValue", frontend)
        self.assertIn("localStorage.setItem", frontend)
        self.assertIn("audio-player-state:", frontend)

    def test_component_receives_project_id_for_scoped_storage(self):
        component = (
            ROOT / "scripts" / "audio" / "player_component.py"
        ).read_text(encoding="utf-8")

        self.assertIn("projectId=project_id", component)


if __name__ == "__main__":
    unittest.main()
