"""
Free Machine Translation module for fast zero-token translation.
Uses Google Translate free web API with paragraph chunking.
"""
import urllib.parse
import urllib.request
import json
import time

def translate_free_google(text: str, src_lang: str = "auto", tgt_lang: str = "vi") -> str:
    """
    Translate text using Google Translate free endpoint.
    Handles long text by splitting into paragraph batches.
    """
    if not text or not text.strip():
        return ""

    lang_map = {
        "chinese": "zh-CN",
        "zh": "zh-CN",
        "english": "en",
        "en": "en",
        "korean": "ko",
        "kr": "ko",
        "ko": "ko",
        "vietnamese": "vi",
        "vi": "vi",
        "auto": "auto"
    }
    sl = lang_map.get(src_lang.lower(), "auto")
    tl = lang_map.get(tgt_lang.lower(), "vi")

    paragraphs = text.split("\n")
    translated_batches = []

    buf = []
    buf_len = 0

    def _translate_chunk(chunk_text: str) -> str:
        if not chunk_text.strip():
            return ""
        encoded = urllib.parse.quote(chunk_text)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={sl}&tl={tl}&dt=t&q={encoded}"
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if data and isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
                    res_parts = [item[0] for item in data[0] if item and isinstance(item, list) and len(item) > 0 and item[0]]
                    return ''.join(res_parts)
        except Exception as ex:
            print(f"[free_translator] Error translating chunk: {ex}")
        return chunk_text

    for p in paragraphs:
        if buf_len + len(p) > 1200 and buf:
            chunk_str = "\n".join(buf)
            translated_batches.append(_translate_chunk(chunk_str))
            buf = []
            buf_len = 0
            time.sleep(0.05)
        buf.append(p)
        buf_len += len(p)

    if buf:
        chunk_str = "\n".join(buf)
        translated_batches.append(_translate_chunk(chunk_str))

    return "\n".join(translated_batches)
