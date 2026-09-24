"""Open Graph protocol models (https://ogp.me)."""

import datetime as _dt
from collections.abc import Sequence
from typing import Annotated, Final, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, model_validator

from goatseo.core.metadata import Locale
from goatseo.core.urls import Url

type OpenGraphType = Literal[
    "website",
    "article",
    "book",
    "profile",
    "music.song",
    "music.album",
    "music.playlist",
    "music.radio_station",
    "video.movie",
    "video.episode",
    "video.tv_show",
    "video.other",
]
type Determiner = Literal["a", "an", "the", "", "auto"]
type Gender = Literal["male", "female"]
type Text = Annotated[str, Field(min_length=1)]


class _Model(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", str_strip_whitespace=True)


class OpenGraphImage(_Model):
    url: Url
    secure_url: Url | None = None
    type: Text | None = None
    width: PositiveInt | None = None
    height: PositiveInt | None = None
    alt: Text | None = None


class OpenGraphVideo(_Model):
    url: Url
    secure_url: Url | None = None
    type: Text | None = None
    width: PositiveInt | None = None
    height: PositiveInt | None = None


class OpenGraphAudio(_Model):
    url: Url
    secure_url: Url | None = None
    type: Text | None = None


class ArticleMetadata(_Model):
    published_time: _dt.datetime | _dt.date | None = None
    modified_time: _dt.datetime | _dt.date | None = None
    expiration_time: _dt.datetime | _dt.date | None = None
    authors: Sequence[Url] = ()
    section: Text | None = None
    tags: Sequence[Text] = ()


class ProfileMetadata(_Model):
    first_name: Text | None = None
    last_name: Text | None = None
    username: Text | None = None
    gender: Gender | None = None


class BookMetadata(_Model):
    authors: Sequence[Url] = ()
    isbn: Text | None = None
    release_date: _dt.datetime | _dt.date | None = None
    tags: Sequence[Text] = ()


class VideoActor(_Model):
    url: Url
    role: Text | None = None


class VideoMetadata(_Model):
    actors: Sequence[VideoActor] = ()
    directors: Sequence[Url] = ()
    writers: Sequence[Url] = ()
    duration: PositiveInt | None = None
    release_date: _dt.datetime | _dt.date | None = None
    tags: Sequence[Text] = ()
    series: Url | None = None


_TYPE_SPECIFIC_FIELDS: Final = ("article", "book", "profile")


class OpenGraph(_Model):
    title: Text | None = None
    type: OpenGraphType = "website"
    url: Url | None = None
    description: Text | None = None
    site_name: Text | None = None
    locale: Locale | None = None
    alternate_locales: Sequence[Locale] = ()
    determiner: Determiner | None = None
    images: Sequence[OpenGraphImage] = ()
    videos: Sequence[OpenGraphVideo] = ()
    audios: Sequence[OpenGraphAudio] = ()
    article: ArticleMetadata | None = None
    profile: ProfileMetadata | None = None
    book: BookMetadata | None = None
    video: VideoMetadata | None = None

    @model_validator(mode="after")
    def _metadata_matches_type(self) -> Self:
        for field in _TYPE_SPECIFIC_FIELDS:
            if getattr(self, field) is not None and self.type != field:
                raise ValueError(f"{field} metadata requires type={field!r}")
        if self.video is not None and not self.type.startswith("video."):
            raise ValueError("video metadata requires a video.* type")
        return self
