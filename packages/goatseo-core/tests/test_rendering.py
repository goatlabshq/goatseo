import json

import pytest

from goatseo.core import (
    AlternateLink,
    HrefLang,
    JsonLd,
    Link,
    Meta,
    Metadata,
    Robots,
    SafeHtml,
    Title,
    dumps_for_script,
    metadata_elements,
    render_elements,
)
from goatseo.core.html import HeadElement, render_element
from goatseo.core.serialization import JsonValue


def test_metadata_elements_order_and_content() -> None:
    metadata = Metadata(
        title="Hello",
        title_template="{title} | Site",
        description="A description",
        robots=Robots(index=False, follow=True),
        author="Jane",
        publisher="Acme",
        keywords=["seo", "python"],
        theme_color="#000000",
        canonical="/hello",
        hreflang=[HrefLang(hreflang="fr", href="/fr/hello")],
        alternates=[AlternateLink(href="/feed.xml", type="application/rss+xml", title="Feed")],
    )
    elements = list(metadata_elements(metadata, base_url="https://example.com/x"))
    assert elements == [
        Title("Hello | Site"),
        Meta("name", "description", "A description"),
        Meta("name", "robots", "noindex, follow"),
        Meta("name", "author", "Jane"),
        Meta("name", "publisher", "Acme"),
        Meta("name", "keywords", "seo, python"),
        Meta("name", "theme-color", "#000000"),
        Link("canonical", "https://example.com/hello"),
        Link("alternate", "https://example.com/fr/hello", hreflang="fr"),
        Link("alternate", "https://example.com/feed.xml", type="application/rss+xml", title="Feed"),
    ]


def test_empty_metadata_renders_nothing() -> None:
    assert list(metadata_elements(Metadata())) == []
    assert list(metadata_elements(Metadata(robots=Robots(), keywords=[]))) == []


def test_relative_urls_stay_relative_without_base() -> None:
    assert list(metadata_elements(Metadata(canonical="/a"))) == [Link("canonical", "/a")]


@pytest.mark.parametrize(
    ("element", "html"),
    [
        (Title("Hi"), "<title>Hi</title>"),
        (Meta("property", "og:title", "Hi"), '<meta property="og:title" content="Hi">'),
        (
            Link("alternate", "/x", hreflang="en", type="t", title="T", media="print"),
            '<link rel="alternate" hreflang="en" type="t" title="T" media="print" href="/x">',
        ),
        (
            JsonLd({"@type": "Thing"}),
            '<script type="application/ld+json">{"@type":"Thing"}</script>',
        ),
    ],
)
def test_render_element(element: HeadElement, html: str) -> None:
    assert render_element(element) == html


def test_render_elements_joins_and_marks_safe() -> None:
    html = render_elements([Title("A"), Meta("name", "description", "B")], separator="")
    assert isinstance(html, SafeHtml)
    assert html == '<title>A</title><meta name="description" content="B">'
    assert html.__html__() is html


def test_json_indent() -> None:
    html = render_element(JsonLd({"a": 1}), json_indent=2)
    assert html == '<script type="application/ld+json">{\n  "a": 1\n}</script>'


def test_dumps_for_script_is_valid_json() -> None:
    data: JsonValue = {"text": "é</script>&", "list": [1, 2.5, True, None]}
    text = dumps_for_script(data)
    assert json.loads(text) == data
    assert "é" in text


def test_dumps_for_script_rejects_nan() -> None:
    with pytest.raises(ValueError, match="Out of range"):
        dumps_for_script(float("nan"))
