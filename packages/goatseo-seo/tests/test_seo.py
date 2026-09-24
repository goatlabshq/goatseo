import json
from collections.abc import Callable
from dataclasses import dataclass
from typing import Final

import pytest
from pydantic import ValidationError

from goatseo.core import (
    AlternateLink,
    HrefLang,
    JsonLd,
    Metadata,
    Precedence,
    Robots,
    SafeHtml,
    StaticRequestContext,
)
from goatseo.opengraph import OpenGraph, OpenGraphImage
from goatseo.schema import Article, Organization, Person
from goatseo.seo import SEO
from goatseo.twitter import TwitterCard, TwitterCardType

CONTEXT = StaticRequestContext("https://example.com/articles/hello?page=2")


def test_constructor_kwargs_form_the_request_layer() -> None:
    seo = SEO(title="Hello", description="Desc", canonical="https://example.com/a")
    assert seo.metadata == Metadata(
        title="Hello", description="Desc", canonical="https://example.com/a"
    )


def test_constructor_rejects_invalid_values() -> None:
    with pytest.raises(ValidationError):
        SEO(canonical="javascript:alert(1)")


def test_empty_seo_renders_nothing() -> None:
    assert SEO().render() == ""


type _Setter = Callable[[SEO], SEO]

SETTERS: Final[list[tuple[_Setter, Metadata]]] = [
    (lambda seo: seo.title("T"), Metadata(title="T")),
    (lambda seo: seo.description("D"), Metadata(description="D")),
    (lambda seo: seo.canonical("/c"), Metadata(canonical="/c")),
    (lambda seo: seo.language("fr-CA"), Metadata(language="fr-CA")),
    (lambda seo: seo.locale("fr_CA"), Metadata(locale="fr_CA")),
    (lambda seo: seo.site_name("S"), Metadata(site_name="S")),
    (lambda seo: seo.author("A"), Metadata(author="A")),
    (lambda seo: seo.publisher("P"), Metadata(publisher="P")),
    (lambda seo: seo.keywords("a", "b"), Metadata(keywords=("a", "b"))),
    (lambda seo: seo.theme_color("#fff"), Metadata(theme_color="#fff")),
    (lambda seo: seo.update(title="U", author="V"), Metadata(title="U", author="V")),
]


@pytest.mark.parametrize(("apply", "expected"), SETTERS)
def test_setters_update_metadata_and_chain(apply: Callable[[SEO], SEO], expected: Metadata) -> None:
    seo = SEO()
    assert apply(seo) is seo
    assert seo.metadata == expected


def test_setters_chain_fluently() -> None:
    seo = SEO().title("T").description("D").robots(index=False).hreflang("en", "/en")
    assert seo.metadata.title == "T"
    assert seo.metadata.robots == Robots(index=False)


def test_robots_with_keywords_and_model() -> None:
    assert SEO().robots(index=False, max_snippet=-1).metadata.robots == Robots(
        index=False, max_snippet=-1
    )
    merged = SEO().robots(Robots(index=True, follow=False), index=False).metadata.robots
    assert merged == Robots(index=False, follow=False)


def test_robots_merge_with_defaults() -> None:
    seo = SEO(defaults=Metadata(robots=Robots(index=True, follow=True)))
    assert seo.robots(index=False).metadata.robots == Robots(index=False, follow=True)


def test_hreflang_overloads_accumulate() -> None:
    seo = SEO().hreflang("en", "/en").hreflang({"fr": "/fr", "x-default": "/"})
    assert list(seo.metadata.hreflang or ()) == [
        HrefLang(hreflang="en", href="/en"),
        HrefLang(hreflang="fr", href="/fr"),
        HrefLang(hreflang="x-default", href="/"),
    ]


def test_alternate_links_accumulate() -> None:
    seo = SEO().alternate("/feed.xml", type="application/rss+xml", title="Feed")
    seo.alternate("/print", media="print")
    assert list(seo.metadata.alternates or ()) == [
        AlternateLink(href="/feed.xml", type="application/rss+xml", title="Feed"),
        AlternateLink(href="/print", media="print"),
    ]


@dataclass
class _Post:
    title: str
    summary: str

    def seo_metadata(self) -> Metadata:
        return Metadata(title=self.title, description=self.summary)


def test_precedence_between_layers() -> None:
    seo = SEO(defaults=Metadata(title="Site", site_name="Example", author="Site author"))
    seo.defaults(Metadata(title="Global", locale="en_US"), Precedence.GLOBAL)
    seo.defaults(Metadata(author="App"), Precedence.APPLICATION)
    seo.from_object(_Post("Post", "Post summary"))
    seo.defaults(Metadata(description="View description"), Precedence.VIEW)
    metadata = seo.metadata
    assert metadata.title == "Post"
    assert metadata.description == "View description"
    assert metadata.author == "App"
    assert metadata.site_name == "Example"
    assert metadata.locale == "en_US"
    assert seo.title("Request").metadata.title == "Request"


def test_defaults_merge_into_the_same_layer() -> None:
    seo = SEO().defaults(Metadata(title="A")).defaults(Metadata(description="B"))
    assert seo.metadata == Metadata(title="A", description="B")


def test_open_graph_derives_from_metadata() -> None:
    seo = SEO(
        title="Hello",
        description="Desc",
        canonical="/hello",
        defaults=Metadata(site_name="Example", locale="en_US", title_template="{title} | Ex"),
    ).open_graph()
    assert seo.graph == OpenGraph(
        title="Hello",
        description="Desc",
        url="/hello",
        site_name="Example",
        locale="en_US",
    )


def test_explicit_open_graph_values_win() -> None:
    seo = SEO(title="Page").open_graph(OpenGraph(title="Social", type="article"))
    graph = seo.graph
    assert graph is not None
    assert graph.title == "Social"
    assert graph.type == "article"


def test_twitter_derives_from_metadata_and_first_image() -> None:
    seo = SEO(title="Hello", description="Desc")
    seo.open_graph(OpenGraph(images=[OpenGraphImage(url="/a.png"), OpenGraphImage(url="/b.png")]))
    seo.twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE))
    assert seo.card == TwitterCard(
        card=TwitterCardType.SUMMARY_LARGE_IMAGE,
        title="Hello",
        description="Desc",
        image="/a.png",
    )


def test_twitter_without_open_graph() -> None:
    card = SEO(title="Hello").twitter().card
    assert card == TwitterCard(title="Hello")


def test_social_disabled_by_default() -> None:
    seo = SEO(title="Hello")
    assert seo.graph is None
    assert seo.card is None


def _json_ld(seo: SEO) -> object:
    scripts = [e for e in seo.elements() if isinstance(e, JsonLd)]
    assert len(scripts) == 1
    return scripts[0].data


def test_single_schema_renders_one_node() -> None:
    seo = SEO().schema(Article(headline="Hello", author=Person(name="John Doe")))
    assert _json_ld(seo) == {
        "@context": "https://schema.org",
        "@type": "Article",
        "author": {"@type": "Person", "name": "John Doe"},
        "headline": "Hello",
    }


def test_several_schemas_render_a_graph() -> None:
    organization = Organization(id="https://example.com/#org", name="Example")
    seo = SEO(schema=[organization]).schema(Article(headline="Hello"))
    assert len(seo.schemas) == 2
    assert _json_ld(seo) == {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": "https://example.com/#org", "name": "Example"},
            {"@type": "Article", "headline": "Hello"},
        ],
    }


def test_render_full_head_with_request_context() -> None:
    seo = SEO(title="Hello", description="Desc", canonical="/articles/hello")
    seo.open_graph(OpenGraph(images=[OpenGraphImage(url="/img.jpg")])).twitter()
    seo.schema(Article(headline="Hello"))
    html = seo.render(CONTEXT)
    assert isinstance(html, SafeHtml)
    assert html.split("\n") == [
        "<title>Hello</title>",
        '<meta name="description" content="Desc">',
        '<link rel="canonical" href="https://example.com/articles/hello">',
        '<meta property="og:title" content="Hello">',
        '<meta property="og:type" content="website">',
        '<meta property="og:url" content="https://example.com/articles/hello">',
        '<meta property="og:description" content="Desc">',
        '<meta property="og:image" content="https://example.com/img.jpg">',
        '<meta name="twitter:card" content="summary">',
        '<meta name="twitter:title" content="Hello">',
        '<meta name="twitter:description" content="Desc">',
        '<meta name="twitter:image" content="https://example.com/img.jpg">',
        (
            '<script type="application/ld+json">'
            '{"@context":"https://schema.org","@type":"Article","headline":"Hello"}</script>'
        ),
    ]


def test_render_options() -> None:
    seo = SEO(title="A", description="B").schema(Article(headline="H"))
    html = seo.render(separator="", json_indent=2)
    assert html.startswith('<title>A</title><meta name="description" content="B"><script')
    body = html.split('application/ld+json">', 1)[1].removesuffix("</script>")
    assert body.startswith("{\n  ")
    assert json.loads(body)["headline"] == "H"


def test_html_protocol_renders_without_context() -> None:
    seo = SEO(canonical="/a")
    assert seo.__html__() == '<link rel="canonical" href="/a">'


def test_copy_is_independent() -> None:
    original = SEO(title="Original").schema(Article(headline="A"))
    clone = original.copy().title("Clone").schema(Article(headline="B")).open_graph()
    assert original.metadata.title == "Original"
    assert len(original.schemas) == 1
    assert original.graph is None
    assert clone.metadata.title == "Clone"
    assert len(clone.schemas) == 2


def test_audit_uses_resolved_metadata() -> None:
    assert {issue.code for issue in SEO().audit()} >= {"missing-title", "missing-description"}
    assert "missing-title" not in {issue.code for issue in SEO(title="T").audit()}


def test_derived_twitter_text_is_shortened_to_card_limits() -> None:
    seo = SEO(title="t" * 100, description="d" * 300).twitter()
    card = seo.card
    assert card is not None
    assert card.title == "t" * 67 + "..."
    assert card.description == "d" * 197 + "..."


def test_hreflang_without_href_is_rejected() -> None:
    with pytest.raises(TypeError, match="needs an href"):
        SEO().hreflang("en")  # pyright: ignore[reportArgumentType]
