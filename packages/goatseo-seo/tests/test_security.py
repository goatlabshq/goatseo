import json
from typing import Final

import pytest

from goatseo.opengraph import OpenGraph
from goatseo.schema import Article, Person
from goatseo.seo import SEO
from goatseo.twitter import TwitterCard

PAYLOADS: Final = [
    "</script>",
    "<script>alert(1)</script>",
    "</SCRIPT ><script>alert(1)</script>",
    '"',
    "'",
    "<",
    ">",
    "&",
    "<!--",
    "\u2028\u2029",
]


@pytest.mark.parametrize("payload", PAYLOADS)
def test_untrusted_values_cannot_break_out(payload: str) -> None:
    value = f"x{payload}"
    seo = SEO(title=value, description=value, author=value, keywords=[value])
    seo.open_graph(OpenGraph(site_name=value)).twitter(TwitterCard(site="goatseo"))
    seo.schema(Article(headline=value, author=Person(name=value)))
    html = seo.render()
    head, script = html.rsplit("\n", 1)
    assert "<script" not in head.lower()
    assert "'" not in head
    body = script.removeprefix('<script type="application/ld+json">').removesuffix("</script>")
    assert "<" not in body
    assert ">" not in body
    assert json.loads(body)["author"] == {"@type": "Person", "name": value}
    assert html.lower().count("</script") == 1
