"""
☁️ r2_uploader.py – Cloudflare R2 Object Storage Uploader
Uploads MP3 audio files to Cloudflare R2 and returns the public CDN URL.
Uses boto3 with S3-compatible API endpoint.
"""

import os
import io
from pathlib import Path


def _get_r2_config() -> dict:
    """Read Cloudflare R2 credentials from streamlit secrets or env."""
    def _read(key: str) -> str:
        try:
            import streamlit as st
            val = st.secrets.get(key)
            if val:
                return val
        except Exception:
            pass
        return os.environ.get(key, "")

    account_id   = _read("R2_ACCOUNT_ID")
    access_key   = _read("R2_ACCESS_KEY_ID")
    secret_key   = _read("R2_SECRET_ACCESS_KEY")
    bucket       = _read("R2_BUCKET_NAME")
    public_domain = _read("R2_PUBLIC_DOMAIN")  # e.g. "audio.yourdomain.com" or blank for auto URL

    if not all([account_id, access_key, secret_key, bucket]):
        raise RuntimeError(
            "Missing Cloudflare R2 credentials. "
            "Set R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET_NAME "
            "in .env or Streamlit secrets."
        )

    endpoint = f"https://{account_id}.r2.cloudflarestorage.com"
    return {
        "account_id": account_id,
        "access_key": access_key,
        "secret_key": secret_key,
        "bucket": bucket,
        "endpoint": endpoint,
        "public_domain": public_domain,
    }


def _build_client(cfg: dict):
    """Build a boto3 S3 client pointed at Cloudflare R2."""
    import boto3
    from botocore.config import Config

    return boto3.client(
        "s3",
        endpoint_url=cfg["endpoint"],
        aws_access_key_id=cfg["access_key"],
        aws_secret_access_key=cfg["secret_key"],
        config=Config(signature_version="s3v4"),
    )


def generate_presigned_url(object_key: str, expires_in: int = 604800) -> str:
    """Generate a presigned GET URL for an R2 object (default 7 days)."""
    cfg = _get_r2_config()
    client = _build_client(cfg)
    return client.generate_presigned_url(
        "get_object",
        Params={"Bucket": cfg["bucket"], "Key": object_key},
        ExpiresIn=expires_in,
    )


def ensure_playable_url(audio_url: str | None, project_slug: str, chapter_slug: str) -> str:
    """
    Ensure the audio URL is browser-playable.
    If using raw R2 storage endpoint without signature/public domain, generates a presigned URL.
    """
    if not audio_url:
        object_key = f"audio/{project_slug}/{chapter_slug}.mp3"
        try:
            return generate_presigned_url(object_key)
        except Exception:
            return ""

    # If it's a raw R2 storage endpoint without auth params, convert to presigned URL
    if "r2.cloudflarestorage.com" in audio_url and "X-Amz-Signature" not in audio_url:
        object_key = f"audio/{project_slug}/{chapter_slug}.mp3"
        try:
            return generate_presigned_url(object_key)
        except Exception:
            return audio_url

    return audio_url


def upload_mp3(
    mp3_bytes: bytes,
    project_slug: str,
    chapter_slug: str,
) -> str:
    """
    Upload MP3 bytes to Cloudflare R2.

    Args:
        mp3_bytes:     Raw MP3 audio bytes.
        project_slug:  Sanitized project name.
        chapter_slug:  Sanitized chapter id.

    Returns:
        Public URL or Presigned GET URL to stream/download the audio file.
    """
    cfg = _get_r2_config()
    client = _build_client(cfg)

    object_key = f"audio/{project_slug}/{chapter_slug}.mp3"

    client.put_object(
        Bucket=cfg["bucket"],
        Key=object_key,
        Body=mp3_bytes,
        ContentType="audio/mpeg",
        CacheControl="public, max-age=31536000",
    )

    # Build public URL or presigned URL
    if cfg["public_domain"]:
        domain = cfg["public_domain"].replace("https://", "").replace("http://", "").strip("/")
        url = f"https://{domain}/{object_key}"
    else:
        # Generate S3 presigned URL for private buckets
        url = client.generate_presigned_url(
            "get_object",
            Params={"Bucket": cfg["bucket"], "Key": object_key},
            ExpiresIn=604800,  # 7 days
        )

    return url


def delete_mp3(project_slug: str, chapter_slug: str) -> None:
    """Delete an MP3 file from R2."""
    cfg = _get_r2_config()
    client = _build_client(cfg)
    object_key = f"audio/{project_slug}/{chapter_slug}.mp3"
    client.delete_object(Bucket=cfg["bucket"], Key=object_key)


def list_project_files(project_slug: str) -> list[str]:
    """List all MP3 object keys under a given project prefix."""
    cfg = _get_r2_config()
    client = _build_client(cfg)
    prefix = f"audio/{project_slug}/"
    resp = client.list_objects_v2(Bucket=cfg["bucket"], Prefix=prefix)
    return [obj["Key"] for obj in resp.get("Contents", [])]
