import goatseo
from goatseo import (
    SEO,
    Metadata,
    Precedence,
    RequestContext,
    Robots,
    SafeHtml,
    StaticRequestContext,
    SupportsMetadata,
)
from goatseo.schema import Article, Person


def test_public_api() -> None:
    assert set(goatseo.__all__) == {
        "SEO",
        "Metadata",
        "Precedence",
        "RequestContext",
        "Robots",
        "SafeHtml",
        "StaticRequestContext",
        "SupportsMetadata",
    }
    assert Precedence.REQUEST > Precedence.SITE
    assert isinstance(Metadata(), Metadata)
    assert Robots(index=False).directives() == ("noindex",)
    assert SupportsMetadata is not None


def test_namespace_portions_resolve() -> None:
    import goatseo.core
    import goatseo.opengraph
    import goatseo.schema
    import goatseo.seo
    import goatseo.twitter

    assert goatseo.seo.SEO is SEO
    assert goatseo.core.SafeHtml is SafeHtml
    assert goatseo.opengraph.OpenGraph.__module__ == "goatseo.opengraph.models"
    assert goatseo.schema.Article is Article
    assert goatseo.twitter.TwitterCard.__module__ == "goatseo.twitter.models"


def test_quickstart() -> None:
    seo = SEO(title="Hello World", description="An interesting article")
    seo.schema(Article(headline="Hello World", author=Person(name="John Doe")))
    context: RequestContext = StaticRequestContext("https://example.com/")
    html = seo.render(context)
    assert html.startswith("<title>Hello World</title>")
    assert '"author":{"@type":"Person","name":"John Doe"}' in html
