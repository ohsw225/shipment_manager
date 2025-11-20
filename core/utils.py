import uuid
from pathlib import Path


def generate_request_id() -> str:
    return uuid.uuid4().hex


def safe_media_filename(stem: str, suffix: str, *, add_uuid: bool = True) -> str:
    base = stem
    if add_uuid:
        base = f"{stem}-{uuid.uuid4().hex}"
    suffix = suffix if suffix.startswith(".") else f".{suffix}"
    return str(Path(base).with_suffix(suffix).name)
