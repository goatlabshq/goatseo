import datetime as dt

import pytest
from pydantic import ValidationError

from goatseo.core import (
    AlternateLink,
    HrefLang,
    Metadata,
    MetadataFields,
    Robots,
    merge_metadata,
)


@pytest.mark.parametrize("language", ["en", "fr-CA", "zh-Hant-TW", "haw"])
def test_accepts_language_tags(language: str) -> None:
    assert Metadata(language=language).language == language


@pytest.mark.parametrize("language", ["english", "e", "en_US", "fr CA", ""])
def test_rejects_invalid_language_tags(language: str) -> None:
    with pytest.raises(ValidationError):
        Metadata(language=language)


@pytest.mark.parametrize("locale", ["en_US", "fr", "fr_FR"])
def test_accepts_locales(locale: str) -> None:
    assert Metadata(locale=locale).locale == locale


@pytest.mark.parametrize("locale", ["en-US", "EN_us", "english"])
def test_rejects_invalid_locales(locale: str) -> None:
    with pytest.raises(ValidationError):
        Metadata(locale=locale)


def test_title_template_requires_placeholder() -> None:
    with pytest.raises(ValidationError):
        Metadata(title_template="No placeholder")


def test_full_title_applies_template() -> None:
    metadata = Metadata(title="Hello", title_template="{title} | Example")
    assert metadata.full_title == "Hello | Example"
    assert Metadata(title_template="{title} | Example").full_title is None
    assert Metadata(title="Hello").full_title == "Hello"


@pytest.mark.parametrize("color", ["#ffffff", "rgb(0, 0, 0)", "red", "hsl(10, 50%, 50%)"])
def test_accepts_theme_colors(color: str) -> None:
    assert Metadata(theme_color=color).theme_color == color


@pytest.mark.parametrize("color", ['red" onload="x', "<script>", "", "a;b"])
def test_rejects_invalid_theme_colors(color: str) -> None:
    with pytest.raises(ValidationError):
        Metadata(theme_color=color)


def test_rejects_unknown_fields_and_empty_text() -> None:
    with pytest.raises(ValidationError):
        Metadata.model_validate({"unknown": "x"})
    with pytest.raises(ValidationError):
        Metadata(title="   ")


def test_rejects_unsafe_canonical() -> None:
    with pytest.raises(ValidationError):
        Metadata(canonical="javascript:alert(1)")


def test_hreflang_accepts_x_default_and_rejects_garbage() -> None:
    assert HrefLang(hreflang="x-default", href="/").hreflang == "x-default"
    with pytest.raises(ValidationError):
        HrefLang(hreflang="not a tag", href="/")


def test_alternate_link_validates_href() -> None:
    with pytest.raises(ValidationError):
        AlternateLink(href="data:text/plain,x")


def test_metadata_fields_mirror_metadata_model() -> None:
    assert set(MetadataFields.__annotations__) == set(Metadata.model_fields)


@pytest.mark.parametrize(
    ("robots", "expected"),
    [
        (Robots(), ()),
        (Robots(index=True, follow=True), ("index", "follow")),
        (Robots(index=False, follow=False), ("noindex", "nofollow")),
        (
            Robots(archive=False, snippet=False, image_index=False, translate=False),
            ("noarchive", "nosnippet", "noimageindex", "notranslate"),
        ),
        (Robots(archive=True, snippet=True), ()),
        (
            Robots(max_snippet=-1, max_image_preview="large", max_video_preview=30),
            ("max-snippet:-1", "max-image-preview:large", "max-video-preview:30"),
        ),
        (
            Robots(unavailable_after=dt.datetime(2030, 1, 2, 3, 4, 5, tzinfo=dt.UTC)),
            ("unavailable_after:2030-01-02T03:04:05+00:00",),
        ),
    ],
)
def test_robots_directives(robots: Robots, expected: tuple[str, ...]) -> None:
    assert robots.directives() == expected


def test_robots_rejects_out_of_range_values() -> None:
    with pytest.raises(ValidationError):
        Robots(max_snippet=-2)


def test_robots_merge_per_directive() -> None:
    merged = Robots(index=False, follow=True, max_snippet=10).merged(Robots(index=True))
    assert merged == Robots(index=True, follow=True, max_snippet=10)
    assert merged.indexable
    assert not Robots(index=False).indexable


def test_merge_metadata_last_layer_wins() -> None:
    merged = merge_metadata(
        Metadata(title="Base", description="Base description", keywords=["a", "b"]),
        Metadata(title="Override", keywords=["c"]),
    )
    assert merged.title == "Override"
    assert merged.description == "Base description"
    assert list(merged.keywords or ()) == ["c"]


def test_merge_metadata_merges_robots() -> None:
    merged = merge_metadata(
        Metadata(robots=Robots(index=True, follow=False)),
        Metadata(robots=Robots(index=False)),
    )
    assert merged.robots == Robots(index=False, follow=False)


def test_empty_sequence_clears_lower_layer() -> None:
    merged = merge_metadata(Metadata(keywords=["a"]), Metadata(keywords=[]))
    assert list(merged.keywords or ()) == []


def test_merge_metadata_without_layers() -> None:
    assert merge_metadata() == Metadata()
