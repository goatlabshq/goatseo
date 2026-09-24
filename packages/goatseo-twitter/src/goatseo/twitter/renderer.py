"""Renders Twitter/X Cards as ``<meta name="twitter:...">`` elements."""

from collections.abc import Iterator

from goatseo.core.html import Meta
from goatseo.core.urls import resolve_url
from goatseo.twitter.models import TwitterApp, TwitterCard


def _meta(key: str, value: str | int | None) -> Iterator[Meta]:
    if value is not None:
        yield Meta("name", f"twitter:{key}", str(value))


def _app(app: TwitterApp) -> Iterator[Meta]:
    for platform, store in (
        ("iphone", app.iphone),
        ("ipad", app.ipad),
        ("googleplay", app.googleplay),
    ):
        if store is not None:
            yield from _meta(f"app:id:{platform}", store.id)
            yield from _meta(f"app:name:{platform}", store.name)
            yield from _meta(f"app:url:{platform}", store.url)
    yield from _meta("app:country", app.country)


def twitter_elements(card: TwitterCard, *, base_url: str | None = None) -> Iterator[Meta]:
    yield from _meta("card", card.card.value)
    yield from _meta("site", card.site)
    yield from _meta("site:id", card.site_id)
    yield from _meta("creator", card.creator)
    yield from _meta("creator:id", card.creator_id)
    yield from _meta("title", card.title)
    yield from _meta("description", card.description)
    if card.image is not None:
        yield from _meta("image", resolve_url(card.image, base_url))
    yield from _meta("image:alt", card.image_alt)
    if card.player is not None:
        yield from _meta("player", card.player.url)
        yield from _meta("player:width", card.player.width)
        yield from _meta("player:height", card.player.height)
        yield from _meta("player:stream", card.player.stream)
    if card.app is not None:
        yield from _app(card.app)
