import json
import re
from typing import Final

import pytest

from goatseo.core import (
    AlternateLink,
    JsonLd,
    Metadata,
    dumps_for_script,
    metadata_elements,
    render_elements,
)
from goatseo.core.serialization import JsonValue

PAYLOADS: Final = [
    "</script>",
    "<script>alert(1)</script>",
    '"',
    "'",
    "<",
    ">",
    "&",
    '"><img src=x onerror=alert(1)>',
    "</title><script>alert(1)</script>",
    "<!--",
    "\u2028\u2029",
]


def _assert_inert(html: str) -> None:
    assert "<script" not in html
    for tag in re.findall(r"<[^>]*>", html):
        assert tag.count('"') % 2 == 0


@pytest.mark.parametrize("payload", PAYLOADS)
def test_text_fields_are_escaped(payload: str) -> None:
    metadata = Metadata(
        title=f"a{payload}",
        description=f"a{payload}",
        author=f"a{payload}",
        publisher=f"a{payload}",
        keywords=[f"a{payload}"],
    )
    html = render_elements(metadata_elements(metadata))
    _assert_inert(html)
    assert html.count("<title>") == 1
    assert html.count("</title>") == 1
    for raw in ("<script", '"><', "'"):
        if raw in payload:
            assert raw not in html


@pytest.mark.parametrize("payload", PAYLOADS)
def test_link_attributes_are_escaped(payload: str) -> None:
    link = AlternateLink(href="/feed", type=f"t{payload}", title=f"t{payload}", media=f"m{payload}")
    html = render_elements(metadata_elements(Metadata(alternates=[link])))
    _assert_inert(html)
    assert html.startswith("<link ")
    assert html.endswith(">")
    assert html.count("<") == 1


@pytest.mark.parametrize("payload", PAYLOADS)
def test_json_ld_cannot_close_the_script(payload: str) -> None:
    data: JsonValue = {"name": payload, "nested": [{"k": payload}], payload: "key"}
    html = render_elements([JsonLd(data)])
    body = html.removeprefix('<script type="application/ld+json">').removesuffix("</script>")
    assert "</script" not in body.lower()
    assert "<" not in body
    assert ">" not in body
    assert "&" not in body
    assert "\u2028" not in body
    assert "\u2029" not in body
    assert html.lower().count("</script") == 1
    assert json.loads(body) == data


def test_json_ld_escaping_matches_serializer() -> None:
    assert dumps_for_script("</script>") == '"\\u003c/script\\u003e"'
