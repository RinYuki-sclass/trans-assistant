"""
🔊 tts_engine.py – Text-to-Speech Engine
Synthesizes chapter text into MP3 audio.
Primary: Google Cloud Text-to-Speech REST API.
Fallback: edge-tts (Microsoft/Google neural voices, zero-key) if 403 Forbidden occurs.
"""

import os
import io
import re
import asyncio
import base64
import httpx
from typing import Callable

# ── Voice catalogue: (language_code, google_voice_name, edge_voice_name) ──
VOICES = {
    # US English – Neural / Journey / Studio
    "🇺🇸 Jenny (Neural, US)":         ("en-US", "en-US-Neural2-F", "en-US-JennyNeural"),
    "🇺🇸 Guy / Matthew (Neural, US)": ("en-US", "en-US-Neural2-D", "en-US-GuyNeural"),
    "🇺🇸 Aria (US)":                  ("en-US", "en-US-Journey-F", "en-US-AriaNeural"),
    "🇺🇸 Christopher (US)":           ("en-US", "en-US-Journey-D", "en-US-ChristopherNeural"),
    "🇺🇸 Michelle (US)":              ("en-US", "en-US-Studio-O",  "en-US-MichelleNeural"),
    "🇺🇸 Eric (US)":                  ("en-US", "en-US-Wavenet-D", "en-US-EricNeural"),
    # Microsoft multilingual voice (Edge only; no Google substitution)
    "🌐 Brian (Multilingual, US)":    ("en-US", "", "en-US-BrianMultilingualNeural"),
    # UK English – Neural
    "🇬🇧 Sonia (Neural, UK)":         ("en-GB", "en-GB-Neural2-A", "en-GB-SoniaNeural"),
    "🇬🇧 Ryan (Neural, UK)":          ("en-GB", "en-GB-Neural2-B", "en-GB-RyanNeural"),
    "🇬🇧 Libby (UK)":                 ("en-GB", "en-GB-Wavenet-A", "en-GB-LibbyNeural"),
    "🇬🇧 Thomas (UK)":                ("en-GB", "en-GB-Wavenet-B", "en-GB-ThomasNeural"),
    # Vietnamese
    "🇻🇳 Hoai My (Neural, VN)":       ("vi-VN", "vi-VN-Neural2-A", "vi-VN-HoaiMyNeural"),
    "🇻🇳 Nam Minh (Neural, VN)":      ("vi-VN", "vi-VN-Wavenet-B", "vi-VN-NamMinhNeural"),
}

VOICE_NAMES = list(VOICES.keys())

_MAX_BYTES = 4800


def _get_api_key() -> str | None:
    """Read Google API key from streamlit secrets or env."""
    try:
        import streamlit as st
        for k in ["GOOGLE_TTS_API_KEY", "GEMINI_API_KEY_1"]:
            val = st.secrets.get(k)
            if val:
                return val
    except Exception:
        pass
    for k in ["GOOGLE_TTS_API_KEY", "GEMINI_API_KEY_1"]:
        val = os.environ.get(k)
        if val:
            return val
    return None


def _chunk_text(text: str, max_bytes: int = _MAX_BYTES) -> list[str]:
    """Split text into chunks ≤ max_bytes each on sentence/paragraph boundaries."""
    if len(text.encode("utf-8")) <= max_bytes:
        return [text]

    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        candidate = (current + " " + sentence).strip()
        if len(candidate.encode("utf-8")) <= max_bytes:
            current = candidate
        else:
            if current:
                chunks.append(current)
            if len(sentence.encode("utf-8")) > max_bytes:
                words = sentence.split()
                sub = ""
                for word in words:
                    c = (sub + " " + word).strip()
                    if len(c.encode("utf-8")) <= max_bytes:
                        sub = c
                    else:
                        if sub:
                            chunks.append(sub)
                        sub = word
                if sub:
                    current = sub
            else:
                current = sentence

    if current:
        chunks.append(current)

    return chunks


def _synthesize_google_cloud(
    text: str,
    language_code: str,
    voice_name: str,
    speaking_rate: float,
    pitch: float,
    api_key: str,
) -> bytes:
    """Call Google Cloud TTS REST API."""
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={api_key}"
    payload = {
        "input": {"text": text},
        "voice": {
            "languageCode": language_code,
            "name": voice_name,
        },
        "audioConfig": {
            "audioEncoding": "MP3",
            "speakingRate": speaking_rate,
            "pitch": pitch,
        },
    }

    with httpx.Client(timeout=30) as client:
        resp = client.post(url, json=payload)
        resp.raise_for_status()

    data = resp.json()
    audio_b64 = data.get("audioContent", "")
    if not audio_b64:
        raise RuntimeError("Google Cloud TTS returned empty audioContent.")

    return base64.b64decode(audio_b64)


def _synthesize_edge_tts(
    text: str,
    edge_voice: str,
    speaking_rate: float,
    pitch: float,
) -> bytes:
    """Synthesize audio using edge-tts (asynchronous stream)."""
    try:
        import edge_tts
    except ImportError as exc:
        raise RuntimeError(
            "Thiếu thư viện edge-tts cho voice fallback. "
            "Hãy chạy `pip install -r requirements.txt` rồi khởi động lại ứng dụng."
        ) from exc

    rate_pct = int(round((speaking_rate - 1.0) * 100))
    rate_str = f"{rate_pct:+d}%" if rate_pct != 0 else "+0%"

    pitch_hz = int(round(pitch))
    pitch_str = f"{pitch_hz:+d}Hz" if pitch_hz != 0 else "+0Hz"

    async def _synth():
        communicate = edge_tts.Communicate(text, edge_voice, rate=rate_str, pitch=pitch_str)
        mp3_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                mp3_data += chunk["data"]
        return mp3_data

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        try:
            import nest_asyncio
        except ImportError as exc:
            raise RuntimeError(
                "Thiếu thư viện nest-asyncio. "
                "Hãy chạy `pip install -r requirements.txt` rồi khởi động lại ứng dụng."
            ) from exc
        nest_asyncio.apply()
        return loop.run_until_complete(_synth())
    else:
        return asyncio.run(_synth())


def _synthesize_chunk(
    text: str,
    language_code: str,
    google_voice: str,
    edge_voice: str,
    speaking_rate: float,
    pitch: float,
) -> bytes:
    """Try Google Cloud TTS first; fall back to edge-tts if API returns 403 Forbidden or fails."""
    api_key = _get_api_key()

    if api_key and google_voice:
        try:
            return _synthesize_google_cloud(
                text, language_code, google_voice, speaking_rate, pitch, api_key
            )
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 403:
                print(f"[TTS Fallback] Google Cloud TTS returned 403 Forbidden. Falling back to Neural Voice engine ({edge_voice})...")
            else:
                print(f"[TTS Fallback] Google Cloud TTS error: {err}. Falling back to Neural Voice engine...")
        except Exception as e:
            print(f"[TTS Fallback] Google Cloud TTS failed: {e}. Falling back to Neural Voice engine...")

    # Fallback to edge-tts (no API key required, high quality neural voice)
    return _synthesize_edge_tts(text, edge_voice, speaking_rate, pitch)


# ── Korean Name & Syllable Phonetic Rules for English TTS ──────────
DEFAULT_KOREAN_PRONUNCIATIONS = {
    r"\bCheon\b": "Chun",
    r"\bcheon\b": "chun",
    r"\bSeong\b": "Sung",
    r"\bseong\b": "sung",
    r"\bMyeong\b": "Myung",
    r"\bmyeong\b": "myung",
    r"\bHyun\b": "Hyeon",
    r"\bhyun\b": "hyeon",
    r"\bEun\b": "Un",
    r"\beun\b": "un",
    r"\bGwang\b": "Guwang",
    r"\bgwang\b": "guwang",
    r"\bHye\b": "Hyeh",
    r"\bhye\b": "hyeh",
    r"\bYoung\b": "Yeong",
}


_LETTER = r"[^\W\d_]"
_STUTTER_PATTERN = re.compile(
    rf"(?<![\w-])(?P<prefixes>(?:{_LETTER}+-)+)(?P<word>{_LETTER}+)(?![\w-])",
    re.UNICODE,
)
_GASP_CUE = (
    r"(?:gasps?|gasping|sharp(?:ly)?\s+inhales?|inhales?\s+sharply|"
    r"catches?\s+(?:(?:his|her|their)\s+)?breath)"
)
_GASP_CUE_PATTERN = re.compile(
    rf"(?:\*{{1,2}}\s*{_GASP_CUE}\s*\*{{1,2}}|"
    rf"\(\s*{_GASP_CUE}\s*\)|\[\s*{_GASP_CUE}\s*\])",
    re.IGNORECASE,
)


def apply_expressive_speech(text: str, language_code: str = "en-US") -> str:
    """Make common gasp cues and written stutters sound natural in plain-text TTS.

    Only hyphenated repetitions whose leading fragments prefix the final word are
    changed, so normal compounds and names such as ``well-being`` and
    ``Hyun-jae`` remain intact.
    """
    if not text:
        return ""

    gasp_interjection = "Á!" if language_code.startswith("vi") else "Ah!"
    processed = _GASP_CUE_PATTERN.sub(gasp_interjection, text)

    def _expand_stutter(match: re.Match[str]) -> str:
        prefixes = match.group("prefixes")[:-1].split("-")
        word = match.group("word")
        if not all(word.casefold().startswith(prefix.casefold()) for prefix in prefixes):
            return match.group(0)

        repetitions = [word] * (len(prefixes) + 1)
        if match.group(0)[0].isupper():
            repetitions[0] = repetitions[0][:1].upper() + repetitions[0][1:]
        return "… ".join(repetitions)

    return _STUTTER_PATTERN.sub(_expand_stutter, processed)


def apply_pronunciation_map(
    text: str,
    custom_map: dict[str, str] | None = None,
    use_default_korean: bool = True,
) -> str:
    """
    Pre-process chapter text to replace Korean names/terms with TTS-friendly phonetic spellings.
    """
    if not text:
        return ""

    processed = text

    # 1. Custom character name replacements (exact word match)
    if custom_map:
        for orig, replacement in custom_map.items():
            if orig and replacement and orig.strip():
                pattern = re.compile(rf"\b{re.escape(orig.strip())}\b")
                processed = pattern.sub(replacement.strip(), processed)

    # 2. Default Korean romanization phonetic adjustments if enabled
    if use_default_korean:
        for pattern, replacement in DEFAULT_KOREAN_PRONUNCIATIONS.items():
            processed = re.sub(pattern, replacement, processed)

    return processed


def prepare_text_for_speech(
    text: str,
    language_code: str = "en-US",
    custom_map: dict[str, str] | None = None,
    use_default_korean: bool = True,
    enhance_expressive_speech: bool = True,
) -> str:
    """Return the final text that will be sent to the TTS provider.

    Keeping this preprocessing in one public helper lets the Audio Converter
    show an accurate pronunciation preview before spending a TTS request.
    """
    expressive_text = (
        apply_expressive_speech(text, language_code)
        if enhance_expressive_speech else text
    )
    return apply_pronunciation_map(
        expressive_text, custom_map, use_default_korean
    )


def synthesize_text(
    text: str,
    voice_label: str = "🇺🇸 Jenny (Neural, US)",
    speaking_rate: float = 1.0,
    pitch: float = 0.0,
    custom_map: dict[str, str] | None = None,
    use_default_korean: bool = True,
    enhance_expressive_speech: bool = True,
    progress_callback: Callable[[int, int, str], None] | None = None,
) -> bytes:
    """Synthesize full text into MP3 bytes with chunking and pronunciation mapping."""
    if voice_label not in VOICES:
        voice_label = VOICE_NAMES[0]
    language_code, google_voice, edge_voice = VOICES[voice_label]

    # Expand performance cues before name replacement (e.g. H-Hyunjae).
    processed_text = prepare_text_for_speech(
        text,
        language_code,
        custom_map,
        use_default_korean,
        enhance_expressive_speech,
    )

    chunks = _chunk_text(processed_text)
    total = len(chunks)
    mp3_parts: list[bytes] = []

    for i, chunk in enumerate(chunks):
        if progress_callback:
            progress_callback(i, total, f"Synthesizing chunk {i + 1}/{total}…")

        part = _synthesize_chunk(
            chunk, language_code, google_voice, edge_voice, speaking_rate, pitch
        )
        mp3_parts.append(part)

    if progress_callback:
        progress_callback(total, total, "Done!")

    return b"".join(mp3_parts)


def synthesize_sample(
    voice_label: str = "🇺🇸 Jenny (Neural, US)",
    sample_text: str | None = None,
    speaking_rate: float = 1.0,
    pitch: float = 0.0,
    custom_map: dict[str, str] | None = None,
    use_default_korean: bool = True,
    enhance_expressive_speech: bool = True,
) -> bytes:
    """Synthesize short preview sample audio clip with pronunciation mapping."""
    if voice_label not in VOICES:
        voice_label = VOICE_NAMES[0]
    language_code, google_voice, edge_voice = VOICES[voice_label]

    if not sample_text:
        if language_code.startswith("vi"):
            sample_text = "Xin chào! Đây là bản nghe thử giọng đọc tiếng Việt bằng trí tuệ nhân tạo."
        elif language_code == "en-GB":
            sample_text = "Hello! This is a preview of the British English voice selection for your audio book."
        else:
            sample_text = "Hello! This is a preview of the American English voice selection for your audio book."

    processed_sample = prepare_text_for_speech(
        sample_text,
        language_code,
        custom_map,
        use_default_korean,
        enhance_expressive_speech,
    )

    return _synthesize_chunk(
        processed_sample, language_code, google_voice, edge_voice, speaking_rate, pitch
    )
