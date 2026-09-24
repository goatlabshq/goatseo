import pytest
from pydantic import ValidationError

from goatseo.twitter import (
    TwitterApp,
    TwitterAppStore,
    TwitterCard,
    TwitterCardType,
    TwitterPlayer,
    twitter_elements,
)


def _pairs(card: TwitterCard, base_url: str | None = None) -> list[tuple[str, str]]:
    elements = list(twitter_elements(card, base_url=base_url))
    assert all(element.attribute == "name" for element in elements)
    return [(element.key, element.content) for element in elements]


def test_default_card_is_summary() -> None:
    assert _pairs(TwitterCard()) == [("twitter:card", "summary")]


@pytest.mark.parametrize(
    "card_type", [TwitterCardType.SUMMARY, TwitterCardType.SUMMARY_LARGE_IMAGE]
)
def test_summary_cards(card_type: TwitterCardType) -> None:
    card = TwitterCard(
        card=card_type,
        site="goatseo",
        site_id="123",
        creator="@jane_doe",
        creator_id="456",
        title="Title",
        description="Description",
        image="/image.jpg",
        image_alt="Alt",
    )
    assert _pairs(card, "https://example.com/page") == [
        ("twitter:card", card_type.value),
        ("twitter:site", "@goatseo"),
        ("twitter:site:id", "123"),
        ("twitter:creator", "@jane_doe"),
        ("twitter:creator:id", "456"),
        ("twitter:title", "Title"),
        ("twitter:description", "Description"),
        ("twitter:image", "https://example.com/image.jpg"),
        ("twitter:image:alt", "Alt"),
    ]


def test_player_card() -> None:
    card = TwitterCard(
        card=TwitterCardType.PLAYER,
        player=TwitterPlayer(
            url="https://example.com/player",
            width=640,
            height=360,
            stream="https://example.com/stream.mp4",
        ),
    )
    assert _pairs(card)[1:] == [
        ("twitter:player", "https://example.com/player"),
        ("twitter:player:width", "640"),
        ("twitter:player:height", "360"),
        ("twitter:player:stream", "https://example.com/stream.mp4"),
    ]


def test_app_card_renders_every_platform() -> None:
    store = TwitterAppStore(id="42", name="App", url="app://open")
    card = TwitterCard(
        card=TwitterCardType.APP,
        app=TwitterApp(iphone=store, ipad=TwitterAppStore(id="43"), googleplay=store, country="US"),
    )
    assert _pairs(card)[1:] == [
        ("twitter:app:id:iphone", "42"),
        ("twitter:app:name:iphone", "App"),
        ("twitter:app:url:iphone", "app://open"),
        ("twitter:app:id:ipad", "43"),
        ("twitter:app:id:googleplay", "42"),
        ("twitter:app:name:googleplay", "App"),
        ("twitter:app:url:googleplay", "app://open"),
        ("twitter:app:country", "US"),
    ]


@pytest.mark.parametrize(
    ("handle", "normalized"), [("goatseo", "@goatseo"), ("@goatseo", "@goatseo"), ("a_1", "@a_1")]
)
def test_handles_are_normalized(handle: str, normalized: str) -> None:
    assert TwitterCard(site=handle, creator=handle).site == normalized


@pytest.mark.parametrize("handle", ["", "@", "with space", "a" * 16, "@@double", "bad-dash"])
def test_invalid_handles_are_rejected(handle: str) -> None:
    with pytest.raises(ValidationError):
        TwitterCard(site=handle)


@pytest.mark.parametrize(
    "fields",
    [
        {"card": "player"},
        {"card": "app"},
        {"card": "gallery"},
        {"site_id": "abc"},
        {"title": "x" * 71},
        {"description": "x" * 201},
        {"image": "javascript:alert(1)"},
        {"card": "player", "player": {"url": "/relative", "width": 1, "height": 1}},
        {"card": "player", "player": {"url": "https://e.com", "width": 0, "height": 1}},
        {"app": {"country": "USA"}},
        {"unknown": 1},
    ],
)
def test_rejects_invalid_cards(fields: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        TwitterCard.model_validate(fields)
