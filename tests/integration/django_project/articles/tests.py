import datetime as dt
import json
import re

from django.test import TestCase

from articles.models import Article

PUBLISHED = dt.datetime(2026, 10, 1, 9, 30, tzinfo=dt.UTC)
XSS = "</script><script>alert(1)</script>"
JSONLD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL)


def create_article(
    slug: str, title: str, *, draft: bool = False, summary: str | None = None
) -> Article:
    return Article.objects.create(
        title=title,
        slug=slug,
        summary=f"About {slug}." if summary is None else summary,
        author="Jane Doe",
        published=PUBLISHED,
        draft=draft,
    )


class ArticlePageTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        create_article("hello-world", "Hello World")
        create_article("draft", "Draft", draft=True)
        create_article("xss", XSS)
        create_article("blank", "Blank", summary="")

    def get_html(self, url: str, **headers: str) -> str:
        response = self.client.get(url, headers=headers)
        assert response.status_code == 200
        return response.content.decode()

    def test_model_metadata_fills_the_head(self) -> None:
        html = self.get_html("/articles/hello-world/")
        assert "<title>Hello World | Goat Blog</title>" in html
        assert '<meta name="description" content="About hello-world.">' in html
        assert '<meta name="author" content="Jane Doe">' in html
        assert '<link rel="canonical" href="http://testserver/articles/hello-world/">' in html
        assert '<meta name="robots" content="index, follow">' in html

    def test_view_adds_social_cards(self) -> None:
        html = self.get_html("/articles/hello-world/")
        assert '<meta property="og:type" content="article">' in html
        assert '<meta property="og:site_name" content="Goat Blog">' in html
        assert (
            '<meta property="article:published_time" content="2026-10-01T09:30:00+00:00">' in html
        )
        assert '<meta name="twitter:card" content="summary_large_image">' in html

    def test_view_adds_jsonld(self) -> None:
        match = JSONLD.search(self.get_html("/articles/hello-world/"))
        assert match is not None
        assert json.loads(match.group(1)) == {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "author": {"@type": "Person", "name": "Jane Doe"},
            "datePublished": "2026-10-01T09:30:00+00:00",
            "headline": "Hello World",
        }

    def test_draft_is_noindex_in_meta_and_header(self) -> None:
        response = self.client.get("/articles/draft/")
        assert '<meta name="robots" content="noindex, follow">' in response.content.decode()
        assert response.headers["X-Robots-Tag"] == "noindex, follow"

    def test_untrusted_title_is_escaped(self) -> None:
        html = self.get_html("/articles/xss/")
        assert "<script>alert(1)</script>" not in html
        assert html.count("</script>") == 1

    def test_canonical_follows_the_proxy_scheme(self) -> None:
        html = self.get_html(
            "/articles/hello-world/", host="blog.example", x_forwarded_proto="https"
        )
        assert '<link rel="canonical" href="https://blog.example/articles/hello-world/">' in html

    def test_blank_model_field_is_omitted(self) -> None:
        html = self.get_html("/articles/blank/")
        assert "<title>Blank | Goat Blog</title>" in html
        assert '<meta name="description"' not in html

    def test_missing_article_is_not_found(self) -> None:
        assert self.client.get("/articles/missing/").status_code == 404


class HomePageTests(TestCase):
    def test_decorator_and_request_layers_are_rendered(self) -> None:
        html = self.client.get("/").content.decode()
        assert "<title>Home | Goat Blog</title>" in html
        assert '<meta name="description" content="The GoatSEO demonstration blog.">' in html
        assert '<link rel="alternate" hreflang="fr" href="http://testserver/fr/">' in html
        assert '<link rel="alternate" hreflang="x-default" href="http://testserver/">' in html
