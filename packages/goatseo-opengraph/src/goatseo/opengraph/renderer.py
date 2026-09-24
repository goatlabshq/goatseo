"""Renders Open Graph models as ``<meta property="og:...">`` elements."""

import datetime as _dt
from collections.abc import Iterable, Iterator

from goatseo.core.html import Meta
from goatseo.core.urls import resolve_url
from goatseo.opengraph.models import (
    ArticleMetadata,
    BookMetadata,
    OpenGraph,
    OpenGraphAudio,
    OpenGraphImage,
    OpenGraphVideo,
    ProfileMetadata,
    VideoMetadata,
)

type _Value = str | int | _dt.date | None


def _text(value: _Value) -> str | None:
    match value:
        case None:
            return None
        case _dt.date():
            return value.isoformat()
        case _:
            return str(value)


class _Writer:
    def __init__(self, base_url: str | None) -> None:
        self._base_url = base_url
        self.elements: list[Meta] = []

    def add(self, key: str, value: _Value) -> None:
        text = _text(value)
        if text is not None:
            self.elements.append(Meta("property", key, text))

    def add_url(self, key: str, url: str | None) -> None:
        if url is not None:
            self.add(key, resolve_url(url, self._base_url))

    def add_all(self, key: str, values: Iterable[_Value]) -> None:
        for value in values:
            self.add(key, value)

    def add_urls(self, key: str, urls: Iterable[str]) -> None:
        for url in urls:
            self.add_url(key, url)


def _media(
    writer: _Writer, prefix: str, media: OpenGraphImage | OpenGraphVideo | OpenGraphAudio
) -> None:
    writer.add_url(prefix, media.url)
    writer.add_url(f"{prefix}:secure_url", media.secure_url)
    writer.add(f"{prefix}:type", media.type)
    if not isinstance(media, OpenGraphAudio):
        writer.add(f"{prefix}:width", media.width)
        writer.add(f"{prefix}:height", media.height)
    if isinstance(media, OpenGraphImage):
        writer.add(f"{prefix}:alt", media.alt)


def _article(writer: _Writer, article: ArticleMetadata) -> None:
    writer.add("article:published_time", article.published_time)
    writer.add("article:modified_time", article.modified_time)
    writer.add("article:expiration_time", article.expiration_time)
    writer.add_urls("article:author", article.authors)
    writer.add("article:section", article.section)
    writer.add_all("article:tag", article.tags)


def _profile(writer: _Writer, profile: ProfileMetadata) -> None:
    writer.add("profile:first_name", profile.first_name)
    writer.add("profile:last_name", profile.last_name)
    writer.add("profile:username", profile.username)
    writer.add("profile:gender", profile.gender)


def _book(writer: _Writer, book: BookMetadata) -> None:
    writer.add_urls("book:author", book.authors)
    writer.add("book:isbn", book.isbn)
    writer.add("book:release_date", book.release_date)
    writer.add_all("book:tag", book.tags)


def _video(writer: _Writer, video: VideoMetadata) -> None:
    for actor in video.actors:
        writer.add_url("video:actor", actor.url)
        writer.add("video:actor:role", actor.role)
    writer.add_urls("video:director", video.directors)
    writer.add_urls("video:writer", video.writers)
    writer.add("video:duration", video.duration)
    writer.add("video:release_date", video.release_date)
    writer.add_all("video:tag", video.tags)
    writer.add_url("video:series", video.series)


def open_graph_elements(graph: OpenGraph, *, base_url: str | None = None) -> Iterator[Meta]:
    writer = _Writer(base_url)
    writer.add("og:title", graph.title)
    writer.add("og:type", graph.type)
    writer.add_url("og:url", graph.url)
    writer.add("og:description", graph.description)
    writer.add("og:site_name", graph.site_name)
    writer.add("og:locale", graph.locale)
    writer.add_all("og:locale:alternate", graph.alternate_locales)
    writer.add("og:determiner", graph.determiner)
    for image in graph.images:
        _media(writer, "og:image", image)
    for video in graph.videos:
        _media(writer, "og:video", video)
    for audio in graph.audios:
        _media(writer, "og:audio", audio)
    if graph.article is not None:
        _article(writer, graph.article)
    if graph.profile is not None:
        _profile(writer, graph.profile)
    if graph.book is not None:
        _book(writer, graph.book)
    if graph.video is not None:
        _video(writer, graph.video)
    return iter(writer.elements)
