# Core concepts

## Metadata

`goatseo.core.Metadata` is a frozen Pydantic model describing one page:

| Field | Type | Rendered as |
| --- | --- | --- |
| `title` | `str` | `<title>` (through `title_template`) |
| `title_template` | `str` containing `{title}` | applied to `title` |
| `description` | `str` | `<meta name="description">` |
| `canonical` | absolute http(s) URL or root-relative path | `<link rel="canonical">` |
| `robots` | `Robots` | `<meta name="robots">` |
| `language` | BCP 47 tag (`en`, `fr-CA`) | not rendered, available for `<html lang>` |
| `locale` | `en_US` style locale | default for `og:locale` |
| `site_name` | `str` | default for `og:site_name` |
| `author`, `publisher` | `str` | `<meta name="author">`, `<meta name="publisher">` |
| `keywords` | sequence of `str` | `<meta name="keywords">` |
| `theme_color` | CSS color | `<meta name="theme-color">` |
| `alternates` | sequence of `AlternateLink` | `<link rel="alternate" type=...>` |
| `hreflang` | sequence of `HrefLang` | `<link rel="alternate" hreflang=...>` |

Every field defaults to `None`, which means *not specified here, inherit from a lower layer*.
An empty sequence is a value: it clears what a lower layer set.

## Layers and precedence

Metadata comes from several places. GoatSEO orders them with `Precedence`:

```text
GLOBAL  <  SITE  <  APPLICATION  <  MODEL  <  VIEW  <  REQUEST
```

The most specific layer wins, field by field. `Robots` directives merge individually, so a
site-wide `max_snippet=-1` survives a page-level `index=False`.

```python
from goatseo.core import Metadata, MetadataStack, Precedence, Robots

stack = MetadataStack()
stack.set(Precedence.SITE, Metadata(site_name="Example", robots=Robots(max_snippet=-1)))
stack.set(Precedence.REQUEST, Metadata(title="Draft", robots=Robots(index=False)))
stack.resolve().robots.directives()  # ('noindex', 'max-snippet:-1')
```

`merge_metadata(*layers)` performs the same merge on an explicit list, least specific first.
The `SEO` builder wraps a `MetadataStack`: constructor keywords and setter methods write the
`REQUEST` layer, `defaults()` and `from_object()` write lower layers.

## Head elements

Rendering is split in two steps. Renderers turn models into **head elements**, plain frozen
dataclasses from `goatseo.core.html`:

- `Title(text)`
- `Meta(attribute, key, content)` where `attribute` is `"name"`, `"property"`,
  `"http-equiv"` or `"itemprop"`
- `Link(rel, href, hreflang=None, type=None, title=None, media=None)`
- `JsonLd(data)`

`render_elements(elements)` then serializes them, escaping every value. Models never contain
HTML, and renderers never concatenate user input into markup.

```text
Metadata ──► metadata_elements ─┐
OpenGraph ─► open_graph_elements ├─► HeadElement stream ─► render_elements ─► SafeHtml
TwitterCard ► twitter_elements ──┤
SchemaModel ► jsonld_element ────┘
```

## SafeHtml

`SafeHtml` is a `str` subclass with an `__html__` method. Django templates, Jinja2 and
MarkupSafe recognize `__html__` and insert the value without escaping it a second time. The
`SEO` object implements `__html__` too, so `{{ seo }}` renders the head in Jinja2.

## Request context

Relative URLs (`/articles/1`) are resolved at render time against a `RequestContext`, a
protocol with a single `url` property. Adapters build a `StaticRequestContext` from the
framework request; you can pass your own object with a `url` attribute.
