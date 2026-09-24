import datetime as dt
from typing import assert_type

from goatseo import SEO, Metadata, Precedence, Robots, SafeHtml
from goatseo.opengraph import ArticleMetadata, OpenGraph, OpenGraphImage
from goatseo.schema import Article, ItemAvailability, Offer, Organization, Person, Product
from goatseo.twitter import TwitterCard, TwitterCardType

article = Article(
    headline="Hello",
    author=[Person(name="Jane"), Organization(name="Acme")],
    date_published=dt.date(2024, 1, 1),
)
assert_type(article.author, Organization | Person | list[Organization | Person] | None)
assert_type(article.headline, str | list[str] | None)
product = Product(name="Goat", offers=Offer(price=10, availability=ItemAvailability.InStock))

seo = SEO(title="Hello", description="Desc", defaults=Metadata(site_name="Example"))
chained = (
    seo.robots(index=False)
    .robots(Robots(follow=True))
    .hreflang("en", "/en")
    .hreflang({"x-default": "/"})
    .keywords("a", "b")
    .defaults(Metadata(author="Jane"), Precedence.VIEW)
    .open_graph(
        OpenGraph(
            type="article",
            images=[OpenGraphImage(url="/a.png", width=1200, height=630)],
            article=ArticleMetadata(tags=["seo"]),
        )
    )
    .twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE))
    .schema(article, product)
)
assert_type(chained, SEO)
assert_type(seo.render(), SafeHtml)
assert_type(seo.metadata.title, str | None)
