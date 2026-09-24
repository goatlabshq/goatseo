"""Type-checked against the installed wheels in CI: every public name must be exported."""

from goatseo import SEO, Metadata, Precedence, Robots, SafeHtml, StaticRequestContext
from goatseo.core import HrefLang, MetadataStack, audit, render_elements
from goatseo.django import SEOMixin, get_seo, seo_defaults
from goatseo.fastapi import GoatSEO, goatseo_head
from goatseo.flask import SEOExtension
from goatseo.opengraph import ArticleMetadata, OpenGraph, OpenGraphImage
from goatseo.schema import (
    Article,
    ItemAvailability,
    Offer,
    Person,
    Product,
    SchemaModel,
    to_jsonld,
)
from goatseo.twitter import TwitterCard, TwitterCardType

seo = SEO(title="Hello", defaults=Metadata(site_name="Example", robots=Robots(index=True)))
seo.defaults(Metadata(language="en"), Precedence.APPLICATION)
seo.open_graph(
    OpenGraph(
        type="article",
        images=[OpenGraphImage(url="https://example.com/a.jpg")],
        article=ArticleMetadata(section="News"),
    )
)
seo.twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE))
article = Article(headline="Hello", author=Person(name="John Doe"))
product = Product(name="Goat", offers=Offer(availability=ItemAvailability.InStock))
seo.schema(article, product)

html: SafeHtml = seo.render(StaticRequestContext("https://example.com/"))
node: SchemaModel = article
stack = MetadataStack().set(Precedence.SITE, Metadata(hreflang=[HrefLang(hreflang="en", href="/")]))
issues = audit(stack.resolve())
print(html, to_jsonld(node), issues, render_elements([]))
print(SEOMixin, get_seo, seo_defaults, GoatSEO, goatseo_head, SEOExtension)
