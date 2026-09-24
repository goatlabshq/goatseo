import datetime as dt

import pytest
from pydantic import ValidationError

from goatseo.core import Meta
from goatseo.opengraph import (
    ArticleMetadata,
    BookMetadata,
    OpenGraph,
    OpenGraphAudio,
    OpenGraphImage,
    OpenGraphVideo,
    ProfileMetadata,
    VideoActor,
    VideoMetadata,
    open_graph_elements,
)


def _pairs(graph: OpenGraph, base_url: str | None = None) -> list[tuple[str, str]]:
    elements = list(open_graph_elements(graph, base_url=base_url))
    assert all(element.attribute == "property" for element in elements)
    return [(element.key, element.content) for element in elements]


def test_basic_properties() -> None:
    graph = OpenGraph(
        title="My article",
        type="website",
        url="https://example.com/a",
        description="Desc",
        site_name="Example",
        locale="en_US",
        alternate_locales=["fr_FR", "de_DE"],
        determiner="the",
    )
    assert _pairs(graph) == [
        ("og:title", "My article"),
        ("og:type", "website"),
        ("og:url", "https://example.com/a"),
        ("og:description", "Desc"),
        ("og:site_name", "Example"),
        ("og:locale", "en_US"),
        ("og:locale:alternate", "fr_FR"),
        ("og:locale:alternate", "de_DE"),
        ("og:determiner", "the"),
    ]


def test_default_graph_only_renders_type() -> None:
    assert _pairs(OpenGraph()) == [("og:type", "website")]


def test_empty_determiner_is_rendered() -> None:
    assert ("og:determiner", "") in _pairs(OpenGraph(determiner=""))


def test_structured_media() -> None:
    graph = OpenGraph(
        images=[
            OpenGraphImage(
                url="https://example.com/a.jpg",
                secure_url="https://example.com/a.jpg",
                type="image/jpeg",
                width=1200,
                height=630,
                alt="Alt",
            ),
            OpenGraphImage(url="https://example.com/b.jpg"),
        ],
        videos=[
            OpenGraphVideo(url="https://example.com/v.mp4", type="video/mp4", width=640, height=480)
        ],
        audios=[
            OpenGraphAudio(
                url="https://example.com/a.mp3",
                secure_url="https://example.com/s.mp3",
                type="audio/mpeg",
            )
        ],
    )
    assert _pairs(graph)[1:] == [
        ("og:image", "https://example.com/a.jpg"),
        ("og:image:secure_url", "https://example.com/a.jpg"),
        ("og:image:type", "image/jpeg"),
        ("og:image:width", "1200"),
        ("og:image:height", "630"),
        ("og:image:alt", "Alt"),
        ("og:image", "https://example.com/b.jpg"),
        ("og:video", "https://example.com/v.mp4"),
        ("og:video:type", "video/mp4"),
        ("og:video:width", "640"),
        ("og:video:height", "480"),
        ("og:audio", "https://example.com/a.mp3"),
        ("og:audio:secure_url", "https://example.com/s.mp3"),
        ("og:audio:type", "audio/mpeg"),
    ]


def test_article_metadata() -> None:
    graph = OpenGraph(
        type="article",
        article=ArticleMetadata(
            published_time=dt.datetime(2024, 1, 2, 3, 4, 5, tzinfo=dt.UTC),
            modified_time=dt.date(2024, 2, 1),
            expiration_time=dt.date(2030, 1, 1),
            authors=["https://example.com/jane", "/john"],
            section="Tech",
            tags=["python", "seo"],
        ),
    )
    assert _pairs(graph, "https://example.com/")[1:] == [
        ("article:published_time", "2024-01-02T03:04:05+00:00"),
        ("article:modified_time", "2024-02-01"),
        ("article:expiration_time", "2030-01-01"),
        ("article:author", "https://example.com/jane"),
        ("article:author", "https://example.com/john"),
        ("article:section", "Tech"),
        ("article:tag", "python"),
        ("article:tag", "seo"),
    ]


def test_profile_metadata() -> None:
    graph = OpenGraph(
        type="profile",
        profile=ProfileMetadata(first_name="Jane", last_name="Doe", username="jd", gender="female"),
    )
    assert _pairs(graph)[1:] == [
        ("profile:first_name", "Jane"),
        ("profile:last_name", "Doe"),
        ("profile:username", "jd"),
        ("profile:gender", "female"),
    ]


def test_book_metadata() -> None:
    graph = OpenGraph(
        type="book",
        book=BookMetadata(
            authors=["https://example.com/a"],
            isbn="978-3-16-148410-0",
            release_date=dt.date(2020, 5, 1),
            tags=["novel"],
        ),
    )
    assert _pairs(graph)[1:] == [
        ("book:author", "https://example.com/a"),
        ("book:isbn", "978-3-16-148410-0"),
        ("book:release_date", "2020-05-01"),
        ("book:tag", "novel"),
    ]


def test_video_metadata() -> None:
    graph = OpenGraph(
        type="video.movie",
        video=VideoMetadata(
            actors=[
                VideoActor(url="https://example.com/actor", role="Hero"),
                VideoActor(url="/other"),
            ],
            directors=["https://example.com/director"],
            writers=["https://example.com/writer"],
            duration=7200,
            release_date=dt.date(2021, 1, 1),
            tags=["drama"],
            series="https://example.com/series",
        ),
    )
    assert _pairs(graph, "https://example.com")[1:] == [
        ("video:actor", "https://example.com/actor"),
        ("video:actor:role", "Hero"),
        ("video:actor", "https://example.com/other"),
        ("video:director", "https://example.com/director"),
        ("video:writer", "https://example.com/writer"),
        ("video:duration", "7200"),
        ("video:release_date", "2021-01-01"),
        ("video:tag", "drama"),
        ("video:series", "https://example.com/series"),
    ]


def test_relative_urls_resolve_against_base() -> None:
    graph = OpenGraph(url="/a", images=[OpenGraphImage(url="/img.png", secure_url="/s.png")])
    pairs = _pairs(graph, "https://example.com/x/y")
    assert ("og:url", "https://example.com/a") in pairs
    assert ("og:image", "https://example.com/img.png") in pairs
    assert ("og:image:secure_url", "https://example.com/s.png") in pairs


def test_relative_urls_stay_relative_without_base() -> None:
    assert ("og:url", "/a") in _pairs(OpenGraph(url="/a"))


@pytest.mark.parametrize(
    "fields",
    [
        {"article": ArticleMetadata()},
        {"type": "website", "book": BookMetadata()},
        {"type": "article", "profile": ProfileMetadata()},
        {"type": "article", "video": VideoMetadata()},
    ],
)
def test_type_specific_metadata_requires_matching_type(fields: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        OpenGraph.model_validate(fields)


def test_video_metadata_accepts_every_video_type() -> None:
    for kind in ("video.movie", "video.episode", "video.tv_show", "video.other"):
        assert OpenGraph.model_validate({"type": kind, "video": VideoMetadata()}).video is not None


@pytest.mark.parametrize(
    "fields",
    [
        {"type": "blog"},
        {"url": "javascript:alert(1)"},
        {"locale": "en-US"},
        {"images": [{"url": "https://example.com/a.jpg", "width": 0}]},
        {"title": ""},
        {"unknown": "x"},
    ],
)
def test_rejects_invalid_values(fields: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        OpenGraph.model_validate(fields)


def test_elements_are_meta_instances() -> None:
    assert all(isinstance(e, Meta) for e in open_graph_elements(OpenGraph(title="x")))
