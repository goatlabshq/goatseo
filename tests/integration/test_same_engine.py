import asyncio
import re
import subprocess
import sys
from pathlib import Path
from types import ModuleType
from typing import Annotated, Final

import httpx
from django.http import HttpRequest, HttpResponse
from django.template import engines
from django.test import Client, override_settings
from django.urls import path
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from flask import Flask, render_template_string

from goatseo import SEO, StaticRequestContext
from goatseo.django import get_seo as django_seo
from goatseo.fastapi import GoatSEO, goatseo_head
from goatseo.flask import SEOExtension
from goatseo.flask import get_seo as flask_seo
from goatseo.opengraph import OpenGraph, OpenGraphImage
from goatseo.schema import Article, Person
from goatseo.twitter import TwitterCard, TwitterCardType

ROOT: Final = Path(__file__).resolve().parents[2]
URL: Final = "http://testserver/articles/hello"
CORE_PACKAGES: Final = (
    "goatseo",
    "goatseo-core",
    "goatseo-schema",
    "goatseo-opengraph",
    "goatseo-twitter",
    "goatseo-seo",
)
FRAMEWORKS: Final = ("django", "flask", "fastapi", "starlette", "werkzeug")


def configure_page(seo: SEO) -> SEO:
    return (
        seo.title("Hello World")
        .description("An interesting article about </script> & friends")
        .canonical("/articles/hello")
        .robots(max_image_preview="large")
        .hreflang({"en": "/articles/hello", "x-default": "/articles/hello"})
        .open_graph(
            OpenGraph(
                type="article", images=[OpenGraphImage(url="/hello.jpg", width=1200, height=630)]
            )
        )
        .twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE, site="@goatseo"))
        .schema(
            Article(
                headline="Hello World",
                description="</script><script>alert(1)</script>",
                author=Person(name="John Doe"),
            )
        )
    )


def expected() -> str:
    return configure_page(SEO()).render(StaticRequestContext(URL))


def render_with_django() -> str:
    def view(request: HttpRequest) -> HttpResponse:
        configure_page(django_seo(request))
        template = engines["django"].from_string("{% load goatseo %}{% goatseo_head %}")
        return HttpResponse(template.render({}, request))

    urls = ModuleType("goatseo_integration_urls")
    urls.__dict__["urlpatterns"] = [path("articles/hello", view)]
    with override_settings(ROOT_URLCONF=urls):
        return Client().get("/articles/hello").content.decode()


def render_with_fastapi() -> str:
    app = FastAPI()

    @app.get("/articles/hello", response_class=HTMLResponse)
    def view(request: Request, seo: Annotated[SEO, Depends(GoatSEO())]) -> str:
        return goatseo_head(configure_page(seo), request)

    async def fetch() -> str:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
            return (await client.get("/articles/hello")).text

    return asyncio.run(fetch())


def render_with_flask() -> str:
    app = Flask(__name__)
    SEOExtension(app)

    @app.get("/articles/hello")
    def view() -> str:
        configure_page(flask_seo())
        return render_template_string("{{ goatseo_head() }}")

    return app.test_client().get("/articles/hello", base_url="http://testserver").text


def test_every_adapter_renders_the_same_head() -> None:
    reference = expected()
    assert render_with_django() == reference
    assert render_with_fastapi() == reference
    assert render_with_flask() == reference


def test_rendered_head_is_complete() -> None:
    html = expected()
    for fragment in (
        "<title>Hello World</title>",
        '<link rel="canonical" href="http://testserver/articles/hello">',
        '<meta property="og:image" content="http://testserver/hello.jpg">',
        '<meta name="twitter:card" content="summary_large_image">',
        '"@type":"Person"',
        "about &lt;/script&gt; &amp; friends",
        "\\u003c/script\\u003e\\u003cscript\\u003e",
    ):
        assert fragment in html
    assert html.count("<script") == 1


def test_core_packages_import_no_web_framework() -> None:
    script = (
        "import sys, goatseo, goatseo.core, goatseo.opengraph, goatseo.twitter, goatseo.seo\n"
        "from goatseo.schema import Article\n"
        f"print(sorted(m for m in {FRAMEWORKS!r} if m in sys.modules))"
    )
    output = subprocess.run(  # noqa: S603
        [sys.executable, "-c", script], capture_output=True, text=True, check=True
    ).stdout
    assert output.strip() == "[]"


def test_core_sources_never_reference_a_web_framework() -> None:
    pattern = re.compile(rf"^\s*(?:from|import)\s+(?:{'|'.join(FRAMEWORKS)})\b", re.MULTILINE)
    sources = [
        source
        for package in CORE_PACKAGES
        for source in (ROOT / "packages" / package / "src").rglob("*.py")
    ]
    assert sources
    offenders = [str(s) for s in sources if pattern.search(s.read_text(encoding="utf-8"))]
    assert offenders == []
