from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from goatseo.django import SEOMixin, get_seo, seo_defaults
from goatseo.opengraph import ArticleMetadata, OpenGraph
from goatseo.schema import BlogPosting, Person
from goatseo.twitter import TwitterCard, TwitterCardType

from articles.models import Article


class ArticleDetail(SEOMixin, DetailView[Article]):
    model = Article

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        article = self.object
        seo = get_seo(self.request)
        seo.open_graph(
            OpenGraph(type="article", article=ArticleMetadata(published_time=article.published))
        )
        seo.twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE, site="@goatlabs"))
        seo.schema(
            BlogPosting(
                headline=article.title,
                date_published=article.published,
                author=Person(name=article.author),
            )
        )
        if article.draft:
            seo.robots(index=False)
        return context


@seo_defaults(title="Home", description="The GoatSEO demonstration blog.")
def home(request: HttpRequest) -> HttpResponse:
    get_seo(request).hreflang({"en": "/", "fr": "/fr/", "x-default": "/"})
    return render(request, "articles/home.html")
