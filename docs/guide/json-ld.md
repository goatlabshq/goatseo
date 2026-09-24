# JSON-LD

Schema.org models serialize to JSON-LD with the functions of `goatseo.schema`:

| Function | Result |
| --- | --- |
| `to_jsonld(model, *, context="https://schema.org")` | One node; pass `context=None` to omit `@context` |
| `to_graph(models, *, context="https://schema.org")` | `{"@context": ..., "@graph": [...]}` |
| `jsonld_element(models)` | A `JsonLd` head element, or `None` for an empty list |

```python
from goatseo.schema import Article, Person, to_jsonld

to_jsonld(Article(headline="Hello World", author=Person(name="John Doe")))
```

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "author": {"@type": "Person", "name": "John Doe"},
  "headline": "Hello World"
}
```

Serialization rules:

- `@type` comes from the class, `@id` from the `id` field.
- `None` values and empty lists are omitted.
- Nested models become nested nodes without `@context`.
- Enumeration members become their IRI, dates and times ISO 8601 strings.
- Keys follow the field declaration order, inherited properties first.

The result is a `JsonObject` (`dict[str, JsonValue]`), a recursive type alias from
`goatseo.core` that covers exactly what JSON can represent.

## Embedding in HTML

JSON-LD is rendered inside `<script type="application/ld+json">`. A plain `json.dumps` is not
safe there: a string containing `</script>` would close the element and let the rest of the
value be parsed as HTML.

`goatseo.core.dumps_for_script` serializes with `allow_nan=False` and then escapes `<`, `>`,
`&`, U+2028 and U+2029 as JSON unicode escapes. The document is unchanged for a JSON parser,
and no sequence can end or corrupt the script element.

```python
from goatseo.core import render_elements
from goatseo.schema import Article, jsonld_element

render_elements([jsonld_element([Article(headline="</script><script>alert(1)</script>")])])
```

```html
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article","headline":"</script><script>alert(1)</script>"}</script>
```

Pass `json_indent=2` to `SEO.render` or `render_elements` for readable output during
development.
