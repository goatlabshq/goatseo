# Configuration

GoatSEO has no global configuration object and never parses configuration per request.
Defaults are ordinary `Metadata` instances, validated once when your settings module loads.

```python
from goatseo import Metadata, Robots

SITE_DEFAULTS = Metadata(
    site_name="Example",
    title_template="{title} | Example",
    locale="en_US",
    language="en",
    theme_color="#0f172a",
    robots=Robots(max_snippet=-1, max_image_preview="large"),
)
```

## Where defaults go

| Framework | Setting |
| --- | --- |
| Plain Python | `SEO(defaults=SITE_DEFAULTS)` or `seo.defaults(SITE_DEFAULTS)` |
| Django | `GOATSEO_DEFAULTS = SITE_DEFAULTS` in `settings.py` |
| FastAPI | `GoatSEO(defaults=SITE_DEFAULTS)` dependency |
| Flask | `SEOExtension(app, defaults=SITE_DEFAULTS)` |

## Layering more defaults

Use `seo.defaults(metadata, precedence)` to add the application, model or view layers:

```python
from goatseo import Precedence

seo.defaults(Metadata(author="Blog team"), Precedence.APPLICATION)
seo.defaults(Metadata(description="All our articles."), Precedence.VIEW)
```

Calling `defaults` twice with the same precedence merges into that layer.

## Title template

`title_template` must contain `{title}`. It is applied with a plain substitution, not
`str.format`, so titles containing braces are safe:

```python
Metadata(title="Sets {a, b}", title_template="{title} | Example").full_title
# 'Sets {a, b} | Example'
```

## Robots

`Robots` fields are tri-state: `True`, `False` or `None` (not specified).

| Field | Directive |
| --- | --- |
| `index`, `follow` | `index` / `noindex`, `follow` / `nofollow` |
| `archive`, `snippet`, `image_index`, `translate` | `noarchive`, `nosnippet`, `noimageindex`, `notranslate` when `False` |
| `max_snippet`, `max_video_preview` | `max-snippet:N`, `max-video-preview:N` (`-1` means no limit) |
| `max_image_preview` | `max-image-preview:` followed by `none`, `standard` or `large` |
| `unavailable_after` | `unavailable_after:<ISO 8601>` |

The Django middleware and the Flask `robots_header=True` option copy the same directives to
the `X-Robots-Tag` response header.
