# Quickstart

This page takes you from `pip install` to a rendered `<head>` in a few minutes.

## 1. Describe the page

```python
from goatseo import SEO, Metadata
from goatseo.schema import Article, Person

seo = SEO(
    defaults=Metadata(site_name="Example", title_template="{title} | Example"),
    title="Hello World",
    description="An interesting article about GoatSEO.",
    canonical="/articles/hello",
)
seo.open_graph()  # derive og:* tags from the metadata
seo.twitter()  # derive twitter:* tags from the metadata
seo.schema(Article(headline="Hello World", author=Person(name="John Doe")))
```

## 2. Render it

```python
from goatseo import StaticRequestContext

html = seo.render(StaticRequestContext("https://example.com/articles/hello"))
```

The request context resolves the relative canonical URL. The result is a `SafeHtml` string:

```html
<title>Hello World | Example</title>
<meta name="description" content="An interesting article about GoatSEO.">
<link rel="canonical" href="https://example.com/articles/hello">
<meta property="og:title" content="Hello World">
<meta property="og:type" content="website">
<meta property="og:url" content="https://example.com/articles/hello">
<meta property="og:description" content="An interesting article about GoatSEO.">
<meta property="og:site_name" content="Example">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Hello World">
<meta name="twitter:description" content="An interesting article about GoatSEO.">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","author":{"@type":"Person","name":"John Doe"},"headline":"Hello World"}</script>
```

## 3. Plug it into your framework

The `SEO` object is the same everywhere; only the glue changes.

=== "Django"

    ```python
    # settings.py
    from goatseo import Metadata

    INSTALLED_APPS = [..., "goatseo.django"]
    TEMPLATES[0]["OPTIONS"]["context_processors"] += [
        "django.template.context_processors.request",
        "goatseo.django.context_processors.seo",
    ]
    GOATSEO_DEFAULTS = Metadata(site_name="Example", title_template="{title} | Example")
    ```

    ```python
    # views.py
    from django.shortcuts import render
    from goatseo.django import get_seo


    def article_detail(request, slug):
        article = ...
        get_seo(request).title(article.title).description(article.summary)
        return render(request, "article.html", {"article": article})
    ```

    ```django
    {% load goatseo %}
    <head>{% goatseo_head %}</head>
    ```

=== "FastAPI"

    ```python
    from typing import Annotated

    from fastapi import Depends, FastAPI, Request
    from fastapi.responses import HTMLResponse
    from fastapi.templating import Jinja2Templates
    from goatseo import Metadata
    from goatseo.fastapi import SEO, GoatSEO

    app = FastAPI()
    templates = Jinja2Templates(directory="templates")
    goatseo = GoatSEO(defaults=Metadata(site_name="Example"))
    goatseo.install(templates)
    SEODep = Annotated[SEO, Depends(goatseo)]


    @app.get("/articles/{slug}", response_class=HTMLResponse)
    async def article(request: Request, slug: str, seo: SEODep):
        seo.title("My article").description("An interesting article")
        return templates.TemplateResponse(request, "article.html", {"seo": seo})
    ```

    ```jinja
    <head>{{ goatseo_head(seo, request) }}</head>
    ```

=== "Flask"

    ```python
    from flask import Flask, render_template
    from goatseo import Metadata
    from goatseo.flask import SEOExtension, get_seo

    app = Flask(__name__)
    SEOExtension(app, defaults=Metadata(site_name="Example"))


    @app.get("/articles/<slug>")
    def article(slug: str):
        get_seo().title("My article").description("An interesting article")
        return render_template("article.html")
    ```

    ```jinja
    <head>{{ goatseo_head() }}</head>
    ```

## Next steps

- [Core concepts](../guide/concepts.md): layers, precedence and rendering.
- [SEO builder](../guide/seo.md): every method of `SEO`.
- [Schema.org](../guide/schema-org.md): the generated models.
