"""Head elements and their escaped HTML serialization."""

from collections.abc import Iterable
from dataclasses import dataclass
from html import escape
from typing import Literal, Self, final

from goatseo.core.serialization import JsonValue, dumps_for_script


@final
class SafeHtml(str):
    """Trusted HTML: ``__html__`` tells Django, Jinja and MarkupSafe not to escape it again."""

    __slots__ = ()

    def __html__(self) -> Self:
        return self


type MetaAttribute = Literal["name", "property", "http-equiv", "itemprop"]


@dataclass(frozen=True, slots=True)
class Title:
    text: str


@dataclass(frozen=True, slots=True)
class Meta:
    attribute: MetaAttribute
    key: str
    content: str


@dataclass(frozen=True, slots=True)
class Link:
    rel: str
    href: str
    hreflang: str | None = None
    type: str | None = None
    title: str | None = None
    media: str | None = None


@dataclass(frozen=True, slots=True)
class JsonLd:
    data: JsonValue


type HeadElement = Title | Meta | Link | JsonLd


def _attributes(pairs: Iterable[tuple[str, str | None]]) -> str:
    return "".join(
        f' {name}="{escape(value, quote=True)}"' for name, value in pairs if value is not None
    )


def render_element(element: HeadElement, *, json_indent: int | None = None) -> str:
    match element:
        case Title(text):
            return f"<title>{escape(text, quote=True)}</title>"
        case Meta(attribute, key, content):
            return f"<meta{_attributes([(attribute, key), ('content', content)])}>"
        case Link(rel, href, hreflang, type_, title, media):
            pairs = [
                ("rel", rel),
                ("hreflang", hreflang),
                ("type", type_),
                ("title", title),
                ("media", media),
                ("href", href),
            ]
            return f"<link{_attributes(pairs)}>"
        case JsonLd(data):
            payload = dumps_for_script(data, indent=json_indent)
            return f'<script type="application/ld+json">{payload}</script>'


def render_elements(
    elements: Iterable[HeadElement], *, separator: str = "\n", json_indent: int | None = None
) -> SafeHtml:
    return SafeHtml(separator.join(render_element(e, json_indent=json_indent) for e in elements))
