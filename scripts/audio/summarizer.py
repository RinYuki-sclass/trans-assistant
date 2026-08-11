"""Token-conscious chapter summarization helpers."""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass
from typing import Callable


GenerateFn = Callable[[str, int], str]


@dataclass(frozen=True)
class SummaryStats:
    estimated_input_tokens: int
    ai_calls: int
    chunk_count: int


def clean_chapter_text(text: str) -> str:
    """Remove token-wasting whitespace while preserving paragraph boundaries."""
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    paragraphs = []
    for paragraph in re.split(r"\n\s*\n", text):
        compact = re.sub(r"[ \t]+", " ", paragraph).strip()
        compact = re.sub(r"\n+", " ", compact)
        if compact:
            paragraphs.append(compact)
    return "\n\n".join(paragraphs)


def estimate_tokens(text: str) -> int:
    """Conservative language-agnostic estimate used only for UI/batching."""
    return math.ceil(len(text or "") / 3)


def summary_source_hash(text: str) -> str:
    return hashlib.sha256(clean_chapter_text(text).encode("utf-8")).hexdigest()


def split_text(text: str, max_chars: int) -> list[str]:
    """Split on paragraphs, then sentences, without dropping source text."""
    if max_chars < 100:
        raise ValueError("max_chars must be at least 100")
    text = clean_chapter_text(text)
    if len(text) <= max_chars:
        return [text] if text else []

    units = re.split(r"\n\n+", text)
    chunks: list[str] = []
    current = ""
    for unit in units:
        if len(unit) > max_chars:
            sentences = re.split(r"(?<=[.!?…])\s+", unit)
        else:
            sentences = [unit]
        for sentence in sentences:
            if len(sentence) > max_chars:
                pieces = [sentence[i:i + max_chars] for i in range(0, len(sentence), max_chars)]
            else:
                pieces = [sentence]
            for piece in pieces:
                separator = "\n\n" if current else ""
                if current and len(current) + len(separator) + len(piece) > max_chars:
                    chunks.append(current)
                    current = piece
                else:
                    current += separator + piece
    if current:
        chunks.append(current)
    return chunks


def _direct_prompt(title: str, text: str, language: str) -> str:
    return (
        f"Tóm tắt chapter truyện bằng {language}. Giữ đúng tên riêng và sự kiện; không suy diễn. "
        "Viết 180-280 từ, nêu diễn biến chính, thay đổi nhân vật và cliffhanger/kết chương. "
        "Không mở đầu bằng lời dẫn và không nhắc đến yêu cầu này.\n"
        f"TITLE: {title}\nTEXT:\n{text}"
    )


def summarize_chapter(
    text: str,
    title: str,
    generate: GenerateFn,
    language: str = "Tiếng Việt",
    direct_token_limit: int = 12_000,
    chunk_token_limit: int = 9_000,
) -> tuple[str, SummaryStats]:
    """Summarize in one call when possible, otherwise use compact map-reduce."""
    cleaned = clean_chapter_text(text)
    if not cleaned:
        raise ValueError("Chapter text is empty")

    estimated = estimate_tokens(cleaned)
    if estimated <= direct_token_limit:
        result = generate(_direct_prompt(title, cleaned, language), 600).strip()
        if not result:
            raise RuntimeError("AI returned an empty summary")
        return result, SummaryStats(estimated, 1, 1)

    chunks = split_text(cleaned, chunk_token_limit * 3)
    partials: list[str] = []
    for index, chunk in enumerate(chunks, 1):
        prompt = (
            f"Tóm tắt phần {index}/{len(chunks)} của chapter '{title}' bằng {language}. "
            "Chỉ giữ sự kiện, nhân vật, quan hệ, tiết lộ và chi tiết cần nối mạch; tối đa 130 từ.\n"
            f"TEXT:\n{chunk}"
        )
        partial = generate(prompt, 320).strip()
        if not partial:
            raise RuntimeError(f"AI returned an empty summary for chunk {index}")
        partials.append(f"[{index}] {partial}")

    reduce_prompt = (
        f"Hợp nhất các ghi chú theo thứ tự thành một summary chapter bằng {language}. "
        "Giữ đúng tên riêng, quan hệ nhân quả và cliffhanger; bỏ trùng lặp; 180-280 từ; không suy diễn.\n"
        f"TITLE: {title}\nNOTES:\n" + "\n".join(partials)
    )
    result = generate(reduce_prompt, 600).strip()
    if not result:
        raise RuntimeError("AI returned an empty final summary")
    return result, SummaryStats(estimated, len(chunks) + 1, len(chunks))
