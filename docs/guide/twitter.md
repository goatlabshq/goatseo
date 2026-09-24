# Twitter/X Cards

`goatseo.twitter` models [Twitter/X Cards](https://developer.x.com/en/docs/x-for-websites/cards/overview/markup)
as validated objects, never as dictionaries.

```python
from goatseo.twitter import TwitterCard, TwitterCardType

card = TwitterCard(
    card=TwitterCardType.SUMMARY_LARGE_IMAGE,
    site="@example",
    creator="janedoe",  # normalized to "@janedoe"
    title="My article",
    description="An interesting article",
    image="https://example.com/image.jpg",
    image_alt="A goat on a mountain",
)
```

## Models

| Model | Fields |
| --- | --- |
| `TwitterCard` | `card`, `site`, `site_id`, `creator`, `creator_id`, `title`, `description`, `image`, `image_alt`, `player`, `app` |
| `TwitterPlayer` | `url`, `width`, `height`, `stream` |
| `TwitterApp` | `iphone`, `ipad`, `googleplay` (each a `TwitterAppStore`), `country` |
| `TwitterAppStore` | `id`, `name`, `url` |

`TwitterCardType` is a `StrEnum`: `SUMMARY` (default), `SUMMARY_LARGE_IMAGE`, `APP`,
`PLAYER`.

Validation rules:

- Handles must be 1 to 15 word characters, with or without a leading `@`.
- `site_id` and `creator_id` are numeric strings.
- `title` is at most 70 characters, `description` 200, `image_alt` 420.
- A `PLAYER` card requires `player`; an `APP` card requires `app`.
- Player URLs must be absolute http(s) URLs.

## Rendering

```python
from goatseo.core import render_elements
from goatseo.twitter import twitter_elements

render_elements(twitter_elements(card))
```

Cards render as `<meta name="twitter:...">`, for example `twitter:card`, `twitter:site`,
`twitter:image:alt`, `twitter:player:width` and `twitter:app:id:iphone`.

## With the SEO builder

```python
seo.twitter(card)  # explicit card
seo.twitter()  # summary card derived from the page metadata
```

Empty `title` and `description` fall back to the page metadata, and an empty `image` to the
first Open Graph image.
