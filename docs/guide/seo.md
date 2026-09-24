# The SEO builder

`goatseo.SEO` (defined in `goatseo.seo`) collects everything about one page and renders its
head. It is framework-independent and cheap to create: build one per request.

## Construction

```python
from goatseo import SEO, Metadata

seo = SEO(
    title="My article",
    description="An interesting article",
    canonical="https://example.com/articles/hello",
    defaults=Metadata(site_name="Example"),  # SITE layer
)
```

`SEO(**metadata)` accepts every `Metadata` field as a keyword (typed through the
`MetadataFields` `TypedDict`) plus `defaults`, `open_graph`, `twitter` and `schema`.

## Setters

Every setter writes the request layer and returns the same object, so calls chain:

```python
(
    seo.title("My article")
    .description("An interesting article")
    .canonical("/articles/hello")
    .language("en")
    .locale("en_US")
    .site_name("Example")
    .author("Jane Doe")
    .publisher("Example Media")
    .keywords("python", "seo")
    .theme_color("#0f172a")
)
```

| Method | Effect |
| --- | --- |
| `update(**fields)` | Merge several metadata fields at once |
| `robots(robots=None, /, **directives)` | `seo.robots(index=False)` or `seo.robots(Robots(...))` |
| `hreflang(language, href)` / `hreflang(mapping)` | Append hreflang alternates |
| `alternate(href, *, type=None, title=None, media=None)` | Append a `rel="alternate"` link |
| `open_graph(graph=None)` | Enable Open Graph, optionally with an `OpenGraph` model |
| `twitter(card=None)` | Enable a Twitter/X card, optionally with a `TwitterCard` model |
| `schema(*items)` | Append Schema.org models rendered as JSON-LD |
| `defaults(metadata, precedence=Precedence.SITE)` | Merge a lower-precedence layer |
| `from_object(source, precedence=Precedence.MODEL)` | Use `source.seo_metadata()` as a layer |
| `copy()` | Independent copy, useful to derive a page from a template |

`hreflang` is overloaded: Pyright accepts either two strings or one mapping.

```python
seo.hreflang("fr", "/fr/articles/hello")
seo.hreflang({"en": "/articles/hello", "x-default": "/articles/hello"})
```

## Reading

| Member | Returns |
| --- | --- |
| `metadata` | The resolved `Metadata` after merging every layer |
| `graph` | The `OpenGraph` model with fallbacks applied, or `None` |
| `card` | The `TwitterCard` with fallbacks applied, or `None` |
| `schemas` | The Schema.org models, as a tuple |
| `audit()` | SEO issues found in the resolved metadata |

## Fallbacks

Open Graph and Twitter fields left empty are derived from the resolved metadata when
rendering:

- `og:title`, `og:description`, `og:url`, `og:site_name`, `og:locale` come from `title`,
  `description`, `canonical`, `site_name` and `locale`.
- `twitter:title`, `twitter:description` come from the metadata, `twitter:image` from the
  first Open Graph image.

Explicit values always win.

## Rendering

```python
seo.render()  # SafeHtml
seo.render(context, separator="", json_indent=2)
list(seo.elements(context))  # HeadElement objects
```

`context` is any `RequestContext` (an object with a `url` string property); relative URLs are
resolved against it. The rendering order is: metadata, Open Graph, Twitter, JSON-LD.

## Auditing

`seo.audit()` (or `goatseo.core.audit(metadata)`) reports problems that are valid HTML but
hurt search visibility:

| Code | Severity |
| --- | --- |
| `missing-title` | error |
| `title-too-long` (over 60 characters) | warning |
| `missing-description` | warning |
| `description-length` (outside 50 to 160 characters) | info |
| `missing-canonical`, `relative-canonical` | info |
| `duplicate-hreflang` | error |
| `missing-x-default` | info |

```python
for issue in seo.audit():
    print(issue.severity, issue.code, issue.message)
```
