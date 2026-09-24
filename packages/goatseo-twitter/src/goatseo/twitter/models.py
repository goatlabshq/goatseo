"""Twitter/X Cards models."""

import re
from enum import StrEnum
from typing import Annotated, Final, Self

from pydantic import AfterValidator, BaseModel, ConfigDict, Field, PositiveInt, model_validator

from goatseo.core.urls import AbsoluteUrl, Url

_HANDLE: Final = re.compile(r"^@?(\w{1,15})$")
_MAX_DESCRIPTION: Final = 200
_MAX_TITLE: Final = 70
_MAX_ALT: Final = 420


def validate_handle(value: str) -> str:
    match = _HANDLE.match(value)
    if match is None:
        raise ValueError(f"{value!r} is not a Twitter/X handle such as '@goatseo'")
    return f"@{match.group(1)}"


type Handle = Annotated[str, AfterValidator(validate_handle)]
type NumericId = Annotated[str, Field(pattern=r"^\d+$")]
type Text = Annotated[str, Field(min_length=1)]


class TwitterCardType(StrEnum):
    SUMMARY = "summary"
    SUMMARY_LARGE_IMAGE = "summary_large_image"
    APP = "app"
    PLAYER = "player"


class _Model(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", str_strip_whitespace=True)


class TwitterPlayer(_Model):
    url: AbsoluteUrl
    width: PositiveInt
    height: PositiveInt
    stream: AbsoluteUrl | None = None


class TwitterAppStore(_Model):
    id: Text
    name: Text | None = None
    url: Text | None = None


class TwitterApp(_Model):
    iphone: TwitterAppStore | None = None
    ipad: TwitterAppStore | None = None
    googleplay: TwitterAppStore | None = None
    country: Annotated[str, Field(pattern=r"^[A-Za-z]{2}$")] | None = None


class TwitterCard(_Model):
    card: TwitterCardType = TwitterCardType.SUMMARY
    site: Handle | None = None
    site_id: NumericId | None = None
    creator: Handle | None = None
    creator_id: NumericId | None = None
    title: Annotated[str, Field(min_length=1, max_length=_MAX_TITLE)] | None = None
    description: Annotated[str, Field(min_length=1, max_length=_MAX_DESCRIPTION)] | None = None
    image: Url | None = None
    image_alt: Annotated[str, Field(min_length=1, max_length=_MAX_ALT)] | None = None
    player: TwitterPlayer | None = None
    app: TwitterApp | None = None

    @model_validator(mode="after")
    def _card_requirements(self) -> Self:
        if self.card is TwitterCardType.PLAYER and self.player is None:
            raise ValueError("a player card requires player")
        if self.card is TwitterCardType.APP and self.app is None:
            raise ValueError("an app card requires app")
        return self
