# Django

`goatseo-django` provides request-scoped SEO state, template tags, a context processor, view
helpers and an optional middleware.

```bash
pip install goatseo-django
```

## Settings

```python
from goatseo import Metadata

INSTALLED_APPS = [
    # ...
    "goatseo.django",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "goatseo.django.context_processors.seo",
            ],
        },
    },
]

# Optional: mirror robots directives in the X-Robots-Tag header.
MIDDLEWARE = [
    # ...
    "goatseo.django.middleware.GoatSEOMiddleware",
]

GOATSEO_DEFAULTS = Metadata(site_name="Example", title_template="{title} | Example")
```

`GOATSEO_DEFAULTS` must be a `Metadata` instance (anything else raises
`ImproperlyConfigured`). It is read once and re-read when a test overrides it with
`override_settings`.

## Views

`get_seo(request)` returns the `SEO` object of the current request, creating it from
`GOATSEO_DEFAULTS` on first use.

```python
from django.shortcuts import get_object_or_404, render
from goatseo.django import get_seo
from goatseo.schema import Article as ArticleSchema, Person


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    seo = get_seo(request)
    seo.title(article.title)
    seo.description(article.summary)
    seo.schema(ArticleSchema(headline=article.title, author=Person(name=article.author_name)))
    return render(request, "article.html", {"article": article})
```

### Function-based views

`seo_defaults` sets the view layer; the view body can still override it:

```python
from goatseo.django import seo_defaults


@seo_defaults(title="Blog", description="Every article of the blog.")
def article_list(request): ...
```

### Class-based views

`SEOMixin` adds `seo_metadata` (or `get_seo_metadata()`) as the view layer and, when the view
has an `object` implementing `seo_metadata()`, uses it as the model layer. It also puts `seo`
in the template context.

```python
from django.views.generic import DetailView
from goatseo import Metadata
from goatseo.django import SEOMixin


class ArticleDetail(SEOMixin, DetailView):
    model = Article
    seo_metadata = Metadata(publisher="Example Media")
```

```python
class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()

    def seo_metadata(self) -> Metadata:
        return Metadata(title=self.title, description=self.summary)
```

## Templates

```django
{% load goatseo %}
<!doctype html>
<html lang="{{ seo.metadata.language|default:'en' }}">
<head>
  <meta charset="utf-8">
  {% goatseo_head %}
</head>
```

| Tag | Output |
| --- | --- |
| `{% goatseo_head %}` | Every element: metadata, Open Graph, Twitter, JSON-LD |
| `{% goatseo_jsonld %}` | Only the JSON-LD script |

Both tags need the `request` context processor. They use the `seo` context variable when it
holds an `SEO` object, otherwise `get_seo(request)`. Relative URLs are resolved with
`request.build_absolute_uri()`.

## Middleware

`GoatSEOMiddleware` is optional. When a view configured robots directives, it copies them to
the `X-Robots-Tag` header, unless the response already has one. It does nothing for requests
that never touched `get_seo`.
