import json
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError


ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_FILE = Path(__file__).resolve().parent / "available_models.txt"
RATE_LIMITS_URL = "https://aistudio.google.com/rate-limit"


def format_number(value):
    """Format an integer limit, while handling models that omit the field."""
    return f"{value:,}" if isinstance(value, int) else "N/A"


def format_actions(actions):
    return ", ".join(actions or []) or "N/A"


def load_rpd_quotas():
    """Load optional per-model RPD quotas from a JSON object in .env."""
    raw_quotas = os.getenv("GEMINI_RPD_QUOTAS", "").strip()
    if not raw_quotas:
        return {}

    try:
        quotas = json.loads(raw_quotas)
    except json.JSONDecodeError as error:
        raise ValueError(f"GEMINI_RPD_QUOTAS is not valid JSON: {error}") from error

    if not isinstance(quotas, dict):
        raise ValueError("GEMINI_RPD_QUOTAS must be a JSON object.")

    return quotas


def format_rpd_quota(model_name, quotas):
    short_name = model_name.removeprefix("models/")
    value = quotas.get(model_name, quotas.get(short_name))
    if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
        return f"{value:,} requests/day"
    return "Check AI Studio"


def model_line(model, rpd_quotas):
    name = (model.name or "N/A").removeprefix("models/")
    return (
        f"{name} | {model.display_name or 'N/A'} | "
        f"Input: {format_number(model.input_token_limit)} tokens | "
        f"Output: {format_number(model.output_token_limit)} tokens | "
        f"RPD quota: {format_rpd_quota(model.name or '', rpd_quotas)} | "
        f"Actions: {format_actions(model.supported_actions)}"
    )


def main():
    load_dotenv(ROOT_DIR / ".env")
    api_key = os.getenv("GEMINI_API_KEY_1")

    if not api_key:
        print("ERROR: GEMINI_API_KEY_1 is not set in .env.")
        return 1

    try:
        rpd_quotas = load_rpd_quotas()
    except ValueError as error:
        print(f"ERROR: {error}")
        return 1

    print("Checking models available to API Key 1...")

    try:
        with genai.Client(api_key=api_key) as client:
            models = sorted(
                client.models.list(),
                key=lambda model: (model.name or "").lower(),
            )
    except APIError as error:
        print(f"API Key 1 failed with APIError: {error}")
        return 1
    except Exception as error:
        print(f"API Key 1 failed: {error}")
        return 1

    header = [
        "=== Models available to API Key 1 ===",
        f"Models found: {len(models)}",
        "",
        "Token limits below come from the Gemini Models API.",
        "RPM/TPM/RPD quota is project- and tier-specific, not returned by the Models API.",
        'Optional: set GEMINI_RPD_QUOTAS={"gemini-2.5-flash": 250} in .env.',
        f"View the active rate limits for this key's project: {RATE_LIMITS_URL}",
        "",
    ]
    lines = header + [model_line(model, rpd_quotas) for model in models]
    report = "\n".join(lines) + "\n"

    OUTPUT_FILE.write_text(report, encoding="utf-8")
    print(report, end="")
    print(f"Saved report to: {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
