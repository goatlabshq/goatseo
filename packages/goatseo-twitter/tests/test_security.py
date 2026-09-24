from typing import Final

import pytest

from goatseo.core import render_elements
from goatseo.twitter import TwitterCard, twitter_elements

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
    card = TwitterCard(title=f"a{payload}", description=f"a{payload}", image_alt=f"a{payload}")
    html = render_elements(twitter_elements(card))
    lines = html.split("\n")
    assert all(line.count("<") == 1 and line.count(">") == 1 for line in lines)
    assert all(line.count('"') == 4 for line in lines)
    assert "'" not in html
