# Open Graph

`goatseo.opengraph` implements the [Open Graph protocol](https://ogp.me) with frozen,
validated models and a dedicated renderer.

```python
from goatseo.opengraph import OpenGraph, OpenGraphImage

graph = OpenGraph(
    title="My article",
    description="An interesting article",
    url="https://example.com/articles/hello",
    type="article",
    site_name="Example",
    locale="en_US",
    images=[
        OpenGraphImage(
            url="https://example.com/images/hello.jpg",
            width=1200,
            height=630,
            alt="Article image",
        )
    ],
)
```

## Models

| Model | Fields |
| --- | --- |
| `OpenGraph` | `title`, `type`, `url`, `description`, `site_name`, `locale`, `alternate_locales`, `determiner`, `images`, `videos`, `audios`, `article`, `profile`, `book`, `video` |
| `OpenGraphImage` | `url`, `secure_url`, `type`, `width`, `height`, `alt` |
| `OpenGraphVideo` | `url`, `secure_url`, `type`, `width`, `height` |
| `OpenGraphAudio` | `url`, `secure_url`, `type` |
| `ArticleMetadata` | `published_time`, `modified_time`, `expiration_time`, `authors`, `section`, `tags` |
| `ProfileMetadata` | `first_name`, `last_name`, `username`, `gender` |
| `BookMetadata` | `authors`, `isbn`, `release_date`, `tags` |
| `VideoMetadata` | `actors` (`VideoActor(url, role)`), `directors`, `writers`, `duration`, `release_date`, `tags`, `series` |

`type` is the `OpenGraphType` literal: `website` (default), `article`, `book`, `profile`,
`music.song`, `music.album`, `music.playlist`, `music.radio_station`, `video.movie`,
`video.episode`, `video.tv_show`, `video.other`.

Type-specific metadata is checked against `type`: `article=` requires `type="article"`,
`video=` requires a `video.*` type, and so on.

```python
import datetime as dt
from goatseo.opengraph import ArticleMetadata, OpenGraph

OpenGraph(
    type="article",
    article=ArticleMetadata(
        published_time=dt.datetime(2026, 9, 1, 8, 0, tzinfo=dt.UTC),
        authors=["https://example.com/authors/jane"],
        tags=["python", "seo"],
    ),
)
```

URLs accept absolute http(s) URLs and root-relative paths; relative ones are resolved against
the request URL when rendering.

## Rendering

```python
from goatseo.core import render_elements
from goatseo.opengraph import open_graph_elements

render_elements(open_graph_elements(graph, base_url="https://example.com/"))
```

Structured properties are emitted in protocol order: each `og:image` is followed by its
`og:image:secure_url`, `og:image:type`, `og:image:width`, `og:image:height` and
`og:image:alt`. Dates render as ISO 8601.

## With the SEO builder

```python
seo.open_graph(graph)  # explicit model
seo.open_graph()  # everything derived from the page metadata
```

Empty fields fall back to the page metadata, see [fallbacks](seo.md#fallbacks).
