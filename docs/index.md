# GoatSEO

**The type-safe SEO toolkit for Python.**

GoatSEO builds the `<head>` of your pages: title, description, canonical URL, robots
directives, hreflang alternates, Open Graph, Twitter/X Cards and Schema.org JSON-LD. Every
value is a validated, statically typed Pydantic model, and every byte of HTML it produces is
escaped.

```python
from goatseo import SEO
from goatseo.schema import Article, Person

seo = SEO(
    title="Hello World",
    description="An interesting article",
    canonical="https://example.com/articles/hello",
)
seo.schema(Article(headline="Hello World", author=Person(name="John Doe")))

print(seo.render())
```

## Why GoatSEO

- **Framework-agnostic core.** The SEO engine never imports Django, Flask, FastAPI or
  Starlette. Framework packages are thin adapters around the same `SEO` object.
- **Typed end to end.** The project passes Pyright in strict mode, and the generated
  Schema.org models expose precise constructor signatures: `Article(headline=123)` is a type
  error before it is a runtime error.
- **Generated Schema.org.** 789 model classes and 78 enumerations are generated from the official
  Schema.org ontology through a parser, an intermediate representation and a Python generator.
- **Safe output.** Attributes and text are HTML-escaped, JSON-LD cannot break out of its
  `<script>` element and URLs are restricted to `http`, `https` and root-relative paths.
- **Deterministic precedence.** Site, application, model, view and request metadata merge in
  a fixed order where the most specific value wins.

## Packages

| Distribution | Import | Purpose |
| --- | --- | --- |
| `goatseo` | `goatseo` | Facade: `from goatseo import SEO`, optional framework extras |
| `goatseo-core` | `goatseo.core` | Metadata, precedence, validation, HTML rendering |
| `goatseo-schema` | `goatseo.schema` | Generated Schema.org models and JSON-LD |
| `goatseo-opengraph` | `goatseo.opengraph` | Open Graph models and renderer |
| `goatseo-twitter` | `goatseo.twitter` | Twitter/X Cards models and renderer |
| `goatseo-seo` | `goatseo.seo` | The high-level `SEO` builder |
| `goatseo-django` | `goatseo.django` | Django adapter |
| `goatseo-fastapi` | `goatseo.fastapi` | FastAPI adapter |
| `goatseo-flask` | `goatseo.flask` | Flask adapter |

Continue with the [installation](getting-started/installation.md) and the
[quickstart](getting-started/quickstart.md).
