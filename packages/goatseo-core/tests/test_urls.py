import pytest

from goatseo.core.urls import (
    UnsafeUrlError,
    is_absolute,
    resolve_url,
    validate_absolute_url,
    validate_url,
)


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com",
        "http://example.com/path?q=1#top",
        "  https://example.com/padded  ",
        "/articles/hello",
        "/",
    ],
)
def test_accepts_http_and_root_relative_urls(url: str) -> None:
    assert validate_url(url) == url.strip()


@pytest.mark.parametrize(
    "url",
    [
        "javascript:alert(1)",
        "JavaScript:alert(1)",
        "data:text/html,<script>alert(1)</script>",
        "vbscript:msgbox",
        "ftp://example.com/file",
        "//evil.example.com/path",
        "articles/relative",
        "https://exa mple.com",
        "https://example.com/\nSet-Cookie:x",
        "https://example.com/\x00",
        "https://example.com/a\u2028b",
        "https:///no-host",
        "",
    ],
)
def test_rejects_unsafe_urls(url: str) -> None:
    with pytest.raises(UnsafeUrlError):
        validate_url(url)


def test_absolute_url_rejects_relative_path() -> None:
    with pytest.raises(UnsafeUrlError):
        validate_absolute_url("/relative")


def test_is_absolute() -> None:
    assert is_absolute("https://example.com/x")
    assert not is_absolute("/x")
    assert not is_absolute("example.com")


@pytest.mark.parametrize(
    ("url", "base", "expected"),
    [
        ("/a", "https://example.com/x/y", "https://example.com/a"),
        ("/a", None, "/a"),
        ("https://other.com/b", "https://example.com/", "https://other.com/b"),
    ],
)
def test_resolve_url(url: str, base: str | None, expected: str) -> None:
    assert resolve_url(url, base) == expected
