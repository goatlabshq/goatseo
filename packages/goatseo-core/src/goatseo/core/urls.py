"""URL validation and resolution shared by every GoatSEO package."""

import unicodedata
from typing import Annotated, Final
from urllib.parse import urljoin, urlsplit

from pydantic import AfterValidator

ALLOWED_SCHEMES: Final = frozenset({"http", "https"})


class UnsafeUrlError(ValueError):
    pass


def _reject_invisible_characters(value: str) -> None:
    if any(char.isspace() or unicodedata.category(char).startswith("C") for char in value):
        raise UnsafeUrlError(f"URL {value!r} contains whitespace or control characters")


def is_absolute(url: str) -> bool:
    parts = urlsplit(url)
    return bool(parts.scheme and parts.netloc)


def validate_absolute_url(value: str) -> str:
    value = value.strip()
    _reject_invisible_characters(value)
    parts = urlsplit(value)
    if parts.scheme.lower() not in ALLOWED_SCHEMES or not parts.netloc:
        raise UnsafeUrlError(f"URL {value!r} must be an absolute http(s) URL")
    return value


def validate_url(value: str) -> str:
    """Accepts absolute http(s) URLs and root-relative paths such as ``/articles/1``."""
    value = value.strip()
    _reject_invisible_characters(value)
    if value.startswith("/") and not value.startswith("//"):
        return value
    return validate_absolute_url(value)


def resolve_url(url: str, base_url: str | None) -> str:
    if base_url is None or is_absolute(url):
        return url
    return validate_absolute_url(urljoin(base_url, url))


type AbsoluteUrl = Annotated[str, AfterValidator(validate_absolute_url)]
type Url = Annotated[str, AfterValidator(validate_url)]
