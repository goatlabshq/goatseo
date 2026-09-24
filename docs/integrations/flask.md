# Flask

`goatseo-flask` is a standard Flask extension with request-scoped state and a Jinja global.

```bash
pip install goatseo-flask
```

## Setup

```python
from flask import Flask
from goatseo import Metadata
from goatseo.flask import SEOExtension

app = Flask(__name__)
seo = SEOExtension(app, defaults=Metadata(site_name="Example"))
```

The application factory pattern works too:

```python
seo = SEOExtension(defaults=Metadata(site_name="Example"))


def create_app() -> Flask:
    app = Flask(__name__)
    seo.init_app(app)
    return app
```

Pass `robots_header=True` to copy robots directives to the `X-Robots-Tag` response header.

## Views

`get_seo()` returns the `SEO` object of the current request, created from the extension
defaults on first use and stored in `flask.g`.

```python
from flask import render_template
from goatseo.flask import get_seo
from goatseo.schema import Article, Person


@app.get("/articles/<slug>")
def article(slug: str):
    get_seo().title("My article").description("An interesting article").schema(
        Article(headline="My article", author=Person(name="John Doe"))
    )
    return render_template("article.html")
```

## Templates

```jinja
<head>
  <meta charset="utf-8">
  {{ goatseo_head() }}
</head>
```

`goatseo_head()` renders the current request's SEO object and resolves relative URLs against
`request.url`. A context processor also exposes `seo`, so templates can read
`{{ seo.metadata.language }}`.

## API

| Name | Purpose |
| --- | --- |
| `SEOExtension(app=None, *, defaults=None, robots_header=False)` | The extension |
| `SEOExtension.init_app(app)` | Registers the Jinja global, the context processor and the optional header hook |
| `get_seo()` | Request-scoped `SEO` object |
| `goatseo_head()` | Renders the current head as `SafeHtml` |
