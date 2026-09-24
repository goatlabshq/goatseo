# Customization

## Metadata from your domain objects

Any object with a `seo_metadata()` method satisfies the `SupportsMetadata` protocol. No base
class, no registration.

```python
from dataclasses import dataclass
from goatseo import Metadata, SEO


@dataclass
class Article:
    title: str
    summary: str
    slug: str

    def seo_metadata(self) -> Metadata:
        return Metadata(
            title=self.title,
            description=self.summary,
            canonical=f"/articles/{self.slug}",
        )


seo = SEO().from_object(Article("Hello", "An interesting article", "hello"))
```

`from_object` writes the `MODEL` layer, so values set by the view or the request still win.
The Django `SEOMixin` calls it automatically for `DetailView.object`.

## Adding head elements

`SEO.elements()` yields plain `HeadElement` dataclasses. Add your own and render them with the
same escaping:

```python
from goatseo.core import Link, Meta, render_elements

elements = [
    *seo.elements(context),
    Meta("name", "google-site-verification", "abc123"),
    Link("icon", "/favicon.svg", type="image/svg+xml"),
]
html = render_elements(elements)
```

## Custom renderers

A renderer is any callable matching `ElementRenderer[T]`: it takes a value and returns an
iterable of head elements. Writing one for your own model keeps the rendering rules (escaping,
URL resolution) in one place:

```python
from collections.abc import Iterator
from dataclasses import dataclass

from goatseo.core import ElementRenderer, HeadElement, Meta, render_elements


@dataclass(frozen=True)
class AppLinks:
    ios_url: str
    android_package: str


def app_links_elements(links: AppLinks) -> Iterator[HeadElement]:
    yield Meta("property", "al:ios:url", links.ios_url)
    yield Meta("property", "al:android:package", links.android_package)


renderer: ElementRenderer[AppLinks] = app_links_elements
render_elements(renderer(AppLinks("example://home", "com.example")))
```

The built-in renderers follow the same shape: `metadata_elements`, `open_graph_elements`,
`twitter_elements` and `jsonld_element`.

## Changing the output format

`render_elements(elements, separator="\n", json_indent=None)` controls the separator between
tags and the indentation of JSON-LD. `SEO.render` forwards both options.
