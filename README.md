# GoatSEO

**The type-safe SEO toolkit for Python.**

GoatSEO renders the SEO part of a page `<head>`: title, meta tags, canonical and hreflang links,
Open Graph, Twitter/X Cards and Schema.org JSON-LD. Everything is a strongly typed Pydantic model,
checked by Pyright in strict mode, and escaped safely on output.

The engine is framework-independent. Django, FastAPI and Flask are thin adapters over the same
`SEO` object, so a page is described once and renders identically everywhere.

- Complete metadata model with deterministic precedence (global, site, application, model, view,
  request)
- Open Graph (images, video, audio, article, profile, book and video metadata) and Twitter/X Cards
- Every Schema.org type (789 models, 78 enumerations) generated from the official ontology, with
  precise static types: `Article(headline=123)` is a type error
- Safe HTML and JSON-LD output: `</script>` in user data cannot break out of the page
- Lightweight at runtime: generated models are plain Python, loaded on first use

## Installation

```bash
pip install goatseo              # the engine
pip install "goatseo[django]"    # or [fastapi], [flask]
```

Python 3.14 or newer is required.

## Quickstart

```python
from goatseo import SEO, Metadata, StaticRequestContext
from goatseo.opengraph import OpenGraph
from goatseo.schema import Article, Person

seo = SEO(
    title="Hello World",
    description="An interesting article",
    canonical="/articles/hello",
    defaults=Metadata(site_name="Example", title_template="{title} | Example"),
)
seo.open_graph(OpenGraph(type="article"))
seo.schema(Article(headline="Hello World", author=Person(name="John Doe")))

print(seo.render(StaticRequestContext("https://example.com/articles/hello")))
```

```html
<title>Hello World | Example</title>
<meta name="description" content="An interesting article">
<link rel="canonical" href="https://example.com/articles/hello">
<meta property="og:title" content="Hello World">
<meta property="og:type" content="article">
...
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",...}</script>
```

### Django

```python
# settings.py
INSTALLED_APPS = [..., "goatseo.django"]
GOATSEO_DEFAULTS = Metadata(site_name="Example")

# views.py
from goatseo.django import get_seo


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    get_seo(request).title(article.title).description(article.summary)
    return render(request, "article.html", {"article": article})
```

```django
{% load goatseo %}
<head>{% goatseo_head %}</head>
```

### FastAPI

```python
from typing import Annotated
from fastapi import Depends, FastAPI, Request
from goatseo.fastapi import SEO, GoatSEO

goatseo = GoatSEO(defaults=Metadata(site_name="Example"))
goatseo.install(templates)
SEODep = Annotated[SEO, Depends(goatseo)]


@app.get("/articles/{slug}")
async def article(request: Request, slug: str, seo: SEODep):
    seo.title("My article")
    return templates.TemplateResponse(request, "article.html", {"seo": seo})
```

```jinja
<head>{{ goatseo_head(seo, request) }}</head>
```

### Flask

```python
from goatseo.flask import SEOExtension, get_seo

SEOExtension(app, defaults=Metadata(site_name="Example"))


@app.get("/articles/<slug>")
def article(slug: str):
    get_seo().title("My article")
    return render_template("article.html")
```

```jinja
<head>{{ goatseo_head() }}</head>
```

## Packages

| Package             | Purpose                                                        |
| ------------------- | -------------------------------------------------------------- |
| `goatseo`           | Main distribution: `from goatseo import SEO`, framework extras |
| `goatseo-core`      | Metadata, precedence, URL safety, HTML rendering, audit        |
| `goatseo-schema`    | Generated Schema.org models and JSON-LD                        |
| `goatseo-opengraph` | Open Graph models and renderer                                 |
| `goatseo-twitter`   | Twitter/X Cards models and renderer                            |
| `goatseo-seo`       | The `SEO` builder combining all of the above                   |
| `goatseo-django`    | Django app, template tags, middleware, view helpers            |
| `goatseo-fastapi`   | FastAPI dependency and Jinja2 helper                           |
| `goatseo-flask`     | Flask extension and Jinja2 global                              |

The core packages never import a web framework.

## Documentation

The [documentation](docs/index.md) covers concepts, every package, the Schema.org generator,
security, type safety, performance and the architecture. Build it locally with
`uv run --group docs mkdocs serve`.

## Development

```bash
uv sync                         # the whole workspace, editable
uv run pytest
uv run pyright
uv run ruff check .
uv run ruff format --check .
uv run goatseo-schema generate  # regenerate the Schema.org models
lefthook install                # git hooks
```

See [contributing](docs/reference/contributing.md) for the conventions.

## License

[MIT](LICENSE)
