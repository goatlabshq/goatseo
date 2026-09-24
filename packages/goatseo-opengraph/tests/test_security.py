from typing import Final

import pytest

from goatseo.core import render_elements
from goatseo.opengraph import ArticleMetadata, OpenGraph, OpenGraphImage, open_graph_elements

PAYLOADS: Final = [
    "</script>",
    "<script>alert(1)</script>",
    '"',
    "'",
    "<",
    ">",
    "&",
    '"><img src=x onerror=alert(1)>',
]


@pytest.mark.parametrize("payload", PAYLOADS)
def test_values_are_escaped(payload: str) -> None:
    graph = OpenGraph(
        title=f"a{payload}",
        description=f"a{payload}",
        site_name=f"a{payload}",
        type="article",
        images=[OpenGraphImage(url="https://example.com/i.png", alt=f"a{payload}")],
        article=ArticleMetadata(section=f"a{payload}", tags=[f"a{payload}"]),
    )
    html = render_elements(open_graph_elements(graph))
    lines = html.split("\n")
    assert all(line.startswith("<meta ") and line.endswith(">") for line in lines)
    assert all(line.count("<") == 1 and line.count(">") == 1 for line in lines)
    assert all(line.count('"') == 4 for line in lines)
    assert "'" not in html


@pytest.mark.parametrize("url", ["javascript:alert(1)", "data:text/html,x", "//evil.com"])
def test_unsafe_urls_are_rejected(url: str) -> None:
    with pytest.raises(ValueError, match="URL"):
        OpenGraph(url=url)


def test_quotes_in_urls_are_escaped() -> None:
    html = render_elements(open_graph_elements(OpenGraph(url='https://e.com/"onload=x')))
    assert 'content="https://e.com/&quot;onload=x"' in html
