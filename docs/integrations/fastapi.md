# FastAPI

`goatseo-fastapi` integrates through dependency injection. Nothing in the core knows about
FastAPI or Starlette.

```bash
pip install goatseo-fastapi
```

## Dependency

`GoatSEO` is a dependency that creates a fresh `SEO` object from your site defaults. FastAPI
caches dependencies per request, so every dependency of one request shares the same object.

```python
from typing import Annotated

from fastapi import Depends, FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from goatseo import Metadata
from goatseo.fastapi import SEO, GoatSEO
from goatseo.schema import Article, Person

app = FastAPI()
templates = Jinja2Templates(directory="templates")

goatseo = GoatSEO(defaults=Metadata(site_name="Example", title_template="{title} | Example"))
goatseo.install(templates)
SEODep = Annotated[SEO, Depends(goatseo)]


@app.get("/articles/{slug}", response_class=HTMLResponse)
async def article(request: Request, slug: str, seo: SEODep):
    seo.title("My article").description("An interesting article")
    seo.schema(Article(headline="My article", author=Person(name="John Doe")))
    return templates.TemplateResponse(request, "article.html", {"seo": seo})
```

`goatseo.install(templates)` registers the `goatseo_head(seo, request)` Jinja global:

```jinja
<head>
  <meta charset="utf-8">
  {{ goatseo_head(seo, request) }}
</head>
```

The request is used to resolve relative URLs such as `canonical="/articles/hello"`.

## Without the dependency

`goatseo.fastapi.SEO` is the same class as `goatseo.SEO`, so you can build it inline:

```python
from goatseo.fastapi import SEO, goatseo_head


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    seo = SEO(title="About", description="Who we are")
    return f"<html><head>{goatseo_head(seo, request)}</head></html>"
```

## Helpers

| Name | Purpose |
| --- | --- |
| `GoatSEO(defaults=None)` | Dependency returning a new `SEO` built from `defaults` |
| `GoatSEO.install(templates)` | Adds `goatseo_head` to a `Jinja2Templates` environment |
| `goatseo_head(seo, request)` | Renders the head as `SafeHtml` |
| `request_context(request)` | Wraps a Starlette request as a `RequestContext` |
