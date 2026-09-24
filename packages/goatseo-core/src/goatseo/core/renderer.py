"""Turns metadata into head elements; framework adapters only choose where to print them."""

from collections.abc import Iterable, Iterator
from typing import Protocol

from goatseo.core.html import HeadElement, Link, Meta, Title
from goatseo.core.metadata import Metadata
from goatseo.core.urls import resolve_url


class ElementRenderer[T](Protocol):
    def __call__(self, value: T, /) -> Iterable[HeadElement]: ...


def metadata_elements(metadata: Metadata, *, base_url: str | None = None) -> Iterator[HeadElement]:
    title = metadata.full_title
    if title is not None:
        yield Title(title)
    if metadata.description is not None:
        yield Meta("name", "description", metadata.description)
    if metadata.robots is not None and (directives := metadata.robots.directives()):
        yield Meta("name", "robots", ", ".join(directives))
    if metadata.author is not None:
        yield Meta("name", "author", metadata.author)
    if metadata.publisher is not None:
        yield Meta("name", "publisher", metadata.publisher)
    if metadata.keywords:
        yield Meta("name", "keywords", ", ".join(metadata.keywords))
    if metadata.theme_color is not None:
        yield Meta("name", "theme-color", metadata.theme_color)
    if metadata.canonical is not None:
        yield Link("canonical", resolve_url(metadata.canonical, base_url))
    for alternate in metadata.hreflang or ():
        yield Link("alternate", resolve_url(alternate.href, base_url), hreflang=alternate.hreflang)
    for link in metadata.alternates or ():
        yield Link(
            "alternate",
            resolve_url(link.href, base_url),
            type=link.type,
            title=link.title,
            media=link.media,
        )
