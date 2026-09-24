"""The high-level, framework-independent SEO builder."""

from collections.abc import Iterator, Mapping, Sequence
from typing import Final, Self, Unpack, overload

from goatseo.core import (
    AlternateLink,
    HeadElement,
    HrefLang,
    Issue,
    Metadata,
    MetadataFields,
    MetadataStack,
    Precedence,
    RequestContext,
    Robots,
    RobotsDirectives,
    SafeHtml,
    SupportsMetadata,
    audit,
    metadata_elements,
    render_elements,
)
from goatseo.opengraph import OpenGraph, open_graph_elements
from goatseo.schema.base import SchemaModel
from goatseo.schema.jsonld import jsonld_element
from goatseo.twitter import TwitterCard, twitter_elements

TWITTER_TITLE_LIMIT: Final = 70
TWITTER_DESCRIPTION_LIMIT: Final = 200
ELLIPSIS: Final = "..."


class SEO:
    """Collects the metadata of one page and renders its ``<head>`` elements.

    Keyword arguments and setter methods write the request layer; :meth:`defaults` and
    :meth:`from_object` fill the less specific layers they are overridden by.
    """

    __slots__ = ("_open_graph", "_schemas", "_stack", "_twitter")

    def __init__(
        self,
        *,
        defaults: Metadata | None = None,
        open_graph: OpenGraph | None = None,
        twitter: TwitterCard | None = None,
        schema: Sequence[SchemaModel] = (),
        **metadata: Unpack[MetadataFields],
    ) -> None:
        self._stack = MetadataStack()
        if defaults is not None:
            self._stack.set(Precedence.SITE, defaults)
        if metadata:
            self._stack.set(Precedence.REQUEST, Metadata.model_validate(metadata))
        self._open_graph = open_graph
        self._twitter = twitter
        self._schemas: list[SchemaModel] = list(schema)

    def copy(self) -> SEO:
        clone = SEO(open_graph=self._open_graph, twitter=self._twitter, schema=self._schemas)
        clone._stack = self._stack.copy()
        return clone

    def update(self, **fields: Unpack[MetadataFields]) -> Self:
        self._stack.update(Precedence.REQUEST, Metadata.model_validate(fields))
        return self

    def defaults(self, metadata: Metadata, precedence: Precedence = Precedence.SITE) -> Self:
        self._stack.update(precedence, metadata)
        return self

    def from_object(
        self, source: SupportsMetadata, precedence: Precedence = Precedence.MODEL
    ) -> Self:
        return self.defaults(source.seo_metadata(), precedence)

    def title(self, title: str) -> Self:
        return self.update(title=title)

    def description(self, description: str) -> Self:
        return self.update(description=description)

    def canonical(self, url: str) -> Self:
        return self.update(canonical=url)

    def language(self, language: str) -> Self:
        return self.update(language=language)

    def locale(self, locale: str) -> Self:
        return self.update(locale=locale)

    def site_name(self, site_name: str) -> Self:
        return self.update(site_name=site_name)

    def author(self, author: str) -> Self:
        return self.update(author=author)

    def publisher(self, publisher: str) -> Self:
        return self.update(publisher=publisher)

    def keywords(self, *keywords: str) -> Self:
        return self.update(keywords=keywords)

    def theme_color(self, color: str) -> Self:
        return self.update(theme_color=color)

    def robots(
        self, robots: Robots | None = None, /, **directives: Unpack[RobotsDirectives]
    ) -> Self:
        """``seo.robots(index=False)`` or ``seo.robots(Robots(...))``; directives merge."""
        value = Robots.model_validate(directives)
        return self.update(robots=value if robots is None else robots.merged(value))

    @overload
    def hreflang(self, language: str, href: str, /) -> Self: ...
    @overload
    def hreflang(self, alternates: Mapping[str, str], /) -> Self: ...
    def hreflang(self, language: str | Mapping[str, str], href: str | None = None, /) -> Self:
        if isinstance(language, Mapping):
            pairs = list(language.items())
        elif href is None:
            raise TypeError("hreflang(language, href) needs an href")
        else:
            pairs = [(language, href)]
        added = [HrefLang(hreflang=lang, href=url) for lang, url in pairs]
        current = self._request_layer().hreflang or ()
        return self.update(hreflang=[*current, *added])

    def alternate(
        self,
        href: str,
        *,
        type: str | None = None,  # noqa: A002
        title: str | None = None,
        media: str | None = None,
    ) -> Self:
        link = AlternateLink(href=href, type=type, title=title, media=media)
        return self.update(alternates=[*(self._request_layer().alternates or ()), link])

    def open_graph(self, graph: OpenGraph | None = None) -> Self:
        """Enables Open Graph; fields left empty are derived from the page metadata."""
        self._open_graph = graph or OpenGraph()
        return self

    def twitter(self, card: TwitterCard | None = None) -> Self:
        """Enables a Twitter/X card; fields left empty are derived from the page metadata."""
        self._twitter = card or TwitterCard()
        return self

    def schema(self, *items: SchemaModel) -> Self:
        self._schemas.extend(items)
        return self

    @property
    def metadata(self) -> Metadata:
        return self._stack.resolve()

    @property
    def schemas(self) -> tuple[SchemaModel, ...]:
        return tuple(self._schemas)

    @property
    def graph(self) -> OpenGraph | None:
        if self._open_graph is None:
            return None
        metadata = self.metadata
        fallbacks = {
            "title": metadata.title,
            "description": metadata.description,
            "url": metadata.canonical,
            "site_name": metadata.site_name,
            "locale": metadata.locale,
        }
        return _fill(self._open_graph, fallbacks)

    @property
    def card(self) -> TwitterCard | None:
        if self._twitter is None:
            return None
        graph = self.graph
        image = graph.images[0].url if graph is not None and graph.images else None
        fallbacks = {
            "title": _shorten(self.metadata.title, TWITTER_TITLE_LIMIT),
            "description": _shorten(self.metadata.description, TWITTER_DESCRIPTION_LIMIT),
            "image": image,
        }
        return _fill(self._twitter, fallbacks)

    def elements(self, context: RequestContext | None = None) -> Iterator[HeadElement]:
        base_url = context.url if context is not None else None
        yield from metadata_elements(self.metadata, base_url=base_url)
        if (graph := self.graph) is not None:
            yield from open_graph_elements(graph, base_url=base_url)
        if (card := self.card) is not None:
            yield from twitter_elements(card, base_url=base_url)
        if (script := jsonld_element(self._schemas)) is not None:
            yield script

    def render(
        self,
        context: RequestContext | None = None,
        *,
        separator: str = "\n",
        json_indent: int | None = None,
    ) -> SafeHtml:
        return render_elements(self.elements(context), separator=separator, json_indent=json_indent)

    def audit(self) -> tuple[Issue, ...]:
        return audit(self.metadata)

    def __html__(self) -> str:
        return self.render()

    def _request_layer(self) -> Metadata:
        return self._stack.layer(Precedence.REQUEST) or Metadata()


def _shorten(text: str | None, limit: int) -> str | None:
    if text is None or len(text) <= limit:
        return text
    return text[: limit - len(ELLIPSIS)].rstrip() + ELLIPSIS


def _fill[M: OpenGraph | TwitterCard](model: M, fallbacks: Mapping[str, object]) -> M:
    missing = {
        name: value
        for name, value in fallbacks.items()
        if value is not None and getattr(model, name) is None
    }
    return model.model_copy(update=missing) if missing else model
