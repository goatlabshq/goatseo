"""Strongly typed page metadata and its deterministic merge rules."""

import datetime as _dt
import re
from collections.abc import Sequence
from typing import Annotated, Final, Literal, Self, TypedDict

from pydantic import AfterValidator, BaseModel, ConfigDict, Field

from goatseo.core.urls import Url

TITLE_PLACEHOLDER: Final = "{title}"
X_DEFAULT: Final = "x-default"

_LANGUAGE_TAG: Final = re.compile(r"^[A-Za-z]{2,3}(?:-[A-Za-z0-9]{1,8})*$")
_LOCALE: Final = re.compile(r"^[a-z]{2,3}(?:_[A-Z]{2})?$")


def validate_language_tag(value: str) -> str:
    if not _LANGUAGE_TAG.match(value):
        raise ValueError(f"{value!r} is not a BCP 47 language tag such as 'en' or 'fr-CA'")
    return value


def validate_hreflang(value: str) -> str:
    return value if value == X_DEFAULT else validate_language_tag(value)


def validate_locale(value: str) -> str:
    if not _LOCALE.match(value):
        raise ValueError(f"{value!r} is not a locale such as 'en_US'")
    return value


def validate_title_template(value: str) -> str:
    if TITLE_PLACEHOLDER not in value:
        raise ValueError(f"title template {value!r} must contain {TITLE_PLACEHOLDER}")
    return value


type LanguageTag = Annotated[str, AfterValidator(validate_language_tag)]
type Locale = Annotated[str, AfterValidator(validate_locale)]
type NonEmptyText = Annotated[str, Field(min_length=1)]
type ImagePreview = Literal["none", "standard", "large"]


class _Model(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", str_strip_whitespace=True)


class RobotsDirectives(TypedDict, total=False):
    index: bool | None
    follow: bool | None
    archive: bool | None
    snippet: bool | None
    image_index: bool | None
    translate: bool | None
    max_snippet: int | None
    max_image_preview: ImagePreview | None
    max_video_preview: int | None
    unavailable_after: _dt.datetime | None


class Robots(_Model):
    """Robots directives; ``None`` means "not specified" and lets a lower layer decide."""

    index: bool | None = None
    follow: bool | None = None
    archive: bool | None = None
    snippet: bool | None = None
    image_index: bool | None = None
    translate: bool | None = None
    max_snippet: Annotated[int, Field(ge=-1)] | None = None
    max_image_preview: ImagePreview | None = None
    max_video_preview: Annotated[int, Field(ge=-1)] | None = None
    unavailable_after: _dt.datetime | None = None

    def merged(self, override: Robots) -> Robots:
        return self.model_copy(update=override.model_dump(exclude_none=True))

    def directives(self) -> tuple[str, ...]:
        flags = (
            (self.index, "index", "noindex"),
            (self.follow, "follow", "nofollow"),
            (self.archive, None, "noarchive"),
            (self.snippet, None, "nosnippet"),
            (self.image_index, None, "noimageindex"),
            (self.translate, None, "notranslate"),
        )
        directives = [
            positive if value else negative
            for value, positive, negative in flags
            if value is not None and (positive if value else negative)
        ]
        if self.max_snippet is not None:
            directives.append(f"max-snippet:{self.max_snippet}")
        if self.max_image_preview is not None:
            directives.append(f"max-image-preview:{self.max_image_preview}")
        if self.max_video_preview is not None:
            directives.append(f"max-video-preview:{self.max_video_preview}")
        if self.unavailable_after is not None:
            directives.append(f"unavailable_after:{self.unavailable_after.isoformat()}")
        return tuple(d for d in directives if d)

    @property
    def indexable(self) -> bool:
        return self.index is not False


class HrefLang(_Model):
    hreflang: Annotated[str, AfterValidator(validate_hreflang)]
    href: Url


class AlternateLink(_Model):
    """A ``<link rel="alternate">`` such as an RSS feed or a print version."""

    href: Url
    type: NonEmptyText | None = None
    title: NonEmptyText | None = None
    media: NonEmptyText | None = None


class Metadata(_Model):
    """Page metadata. Every field defaults to ``None``, meaning "inherit from a lower layer"."""

    title: NonEmptyText | None = None
    title_template: Annotated[str, AfterValidator(validate_title_template)] | None = None
    description: NonEmptyText | None = None
    canonical: Url | None = None
    robots: Robots | None = None
    language: LanguageTag | None = None
    locale: Locale | None = None
    site_name: NonEmptyText | None = None
    author: NonEmptyText | None = None
    publisher: NonEmptyText | None = None
    keywords: Sequence[NonEmptyText] | None = None
    theme_color: Annotated[str, Field(pattern=r"^[#(),.%\w\s-]{1,64}$")] | None = None
    alternates: Sequence[AlternateLink] | None = None
    hreflang: Sequence[HrefLang] | None = None

    def merged(self, override: Metadata) -> Self:
        """Returns a copy where every field set on ``override`` wins; robots merge per directive."""
        update = {
            name: getattr(override, name)
            for name in type(override).model_fields
            if getattr(override, name) is not None
        }
        if self.robots is not None and override.robots is not None:
            update["robots"] = self.robots.merged(override.robots)
        return self.model_copy(update=update)

    @property
    def full_title(self) -> str | None:
        if self.title is None or self.title_template is None:
            return self.title
        return self.title_template.replace(TITLE_PLACEHOLDER, self.title)


class MetadataFields(TypedDict, total=False):
    """Keyword arguments accepted wherever a :class:`Metadata` can be built inline."""

    title: str | None
    title_template: str | None
    description: str | None
    canonical: str | None
    robots: Robots | None
    language: str | None
    locale: str | None
    site_name: str | None
    author: str | None
    publisher: str | None
    keywords: Sequence[str] | None
    theme_color: str | None
    alternates: Sequence[AlternateLink] | None
    hreflang: Sequence[HrefLang] | None


def merge_metadata(*layers: Metadata) -> Metadata:
    """Merges layers from least to most specific: the last layer that sets a field wins."""
    result = Metadata()
    for layer in layers:
        result = result.merged(layer)
    return result
