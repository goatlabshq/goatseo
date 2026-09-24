import asyncio
from typing import Annotated

import httpx
from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from jinja2 import DictLoader, Environment
from starlette.templating import Jinja2Templates

from goatseo.core import Metadata
from goatseo.fastapi import SEO, GoatSEO, goatseo_head, request_context

goatseo = GoatSEO(defaults=Metadata(site_name="Example", title_template="{title} | Example"))
SEODep = Annotated[SEO, Depends(goatseo)]
templates = Jinja2Templates(
    env=Environment(
        loader=DictLoader({"page.html": "<head>{{ goatseo_head(seo, request) }}</head>"}),
        autoescape=True,
    )
)
goatseo.install(templates)
app = FastAPI()
seen: list[SEO] = []


@app.get("/articles/{slug}", response_class=HTMLResponse)
def article(request: Request, slug: str, seo: SEODep) -> HTMLResponse:
    seo.title(slug.title()).canonical(f"/articles/{slug}")
    return templates.TemplateResponse(request, "page.html", {"seo": seo})


@app.get("/shared", response_class=PlainTextResponse)
def shared(first: SEODep, second: SEODep) -> str:
    seen.append(first)
    return str(first is second)


@app.get("/manual", response_class=HTMLResponse)
def manual(request: Request) -> str:
    seo = SEO(title="My article", description="An interesting article")
    return goatseo_head(seo, request)


@app.get("/xss", response_class=HTMLResponse)
def xss(request: Request, seo: SEODep) -> HTMLResponse:
    seo.title("</title><script>alert(1)</script>")
    return templates.TemplateResponse(request, "page.html", {"seo": seo})


def get(url: str, application: FastAPI = app) -> httpx.Response:
    async def fetch() -> httpx.Response:
        transport = httpx.ASGITransport(app=application)
        async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
            return await client.get(url)

    return asyncio.run(fetch())


def test_dependency_is_shared_within_a_request_and_fresh_per_request() -> None:
    seen.clear()
    assert get("/shared").text == "True"
    get("/shared")
    assert len(seen) == 2
    assert seen[0] is not seen[1]


def test_dependency_applies_site_defaults() -> None:
    seo = goatseo()
    assert seo.title("Hi").metadata.full_title == "Hi | Example"


def test_template_global_renders_the_head() -> None:
    assert get("/articles/hello?page=2").text == (
        "<head><title>Hello | Example</title>\n"
        '<link rel="canonical" href="http://testserver/articles/hello"></head>'
    )


def test_manual_seo_inside_a_route() -> None:
    assert get("/manual").text == (
        '<title>My article</title>\n<meta name="description" content="An interesting article">'
    )


def test_untrusted_values_are_escaped() -> None:
    html = get("/xss").text
    assert "<script>" not in html
    assert "&lt;/title&gt;&lt;script&gt;alert(1)&lt;/script&gt;" in html


def test_request_context_uses_the_full_url() -> None:
    captured: list[str] = []
    probe = FastAPI()

    @probe.get("/probe")
    def endpoint(request: Request) -> None:
        captured.append(request_context(request).url)

    get("/probe?q=1", probe)
    assert captured == ["http://testserver/probe?q=1"]
