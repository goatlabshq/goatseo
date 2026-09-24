# Security

GoatSEO treats every value as untrusted: titles, descriptions, URLs, Schema.org properties,
Open Graph and Twitter values may all come from users or a database.

## Escaping model

HTML is produced in exactly one place, `goatseo.core.html.render_element`:

- Text content (`<title>`) and every attribute value go through `html.escape(value, quote=True)`,
  which escapes `&`, `<`, `>`, `"` and `'`.
- Attribute names and tag names are fixed by the element dataclasses, never taken from data.
- Renderers build `Title`, `Meta`, `Link` and `JsonLd` objects; they never concatenate strings
  into markup.

```python
from goatseo import SEO

SEO(title='"><script>alert(1)</script>').render()
# <title>&quot;&gt;&lt;script&gt;alert(1)&lt;/script&gt;</title>
```

The output is a `SafeHtml` string. Treat it as trusted only because GoatSEO escaped it, and
do not concatenate unescaped user input to it.

## JSON-LD

Inside `<script>`, HTML escaping does not apply, so JSON-LD uses a dedicated serializer:
`dumps_for_script` escapes `<`, `>`, `&`, U+2028 and U+2029 as JSON unicode escapes and
rejects `NaN` and infinities. Payloads such as `</script><script>alert(1)</script>` or
`<!--` stay inside the JSON string. See [JSON-LD](../guide/json-ld.md#embedding-in-html).

## URLs

Every URL field (`canonical`, hreflang and alternate links, Open Graph and Twitter URLs)
is validated:

- Only `http` and `https` schemes are accepted, with a host. `javascript:`, `data:`,
  `vbscript:` and scheme-relative `//host` URLs are rejected.
- Root-relative paths (`/articles/1`) are accepted and resolved against the request URL.
- Whitespace and control characters anywhere in the URL are rejected, which blocks
  obfuscations such as `java\tscript:`.

Invalid values raise `pydantic.ValidationError` (`UnsafeUrlError` in the message) when the
model is built, before anything is rendered.

Schema.org `URL` properties are plain `str`, as Schema.org allows free text there, and are
protected by JSON-LD escaping rather than by scheme validation.

## Other validation

- Language tags, locales, Twitter handles and numeric ids are checked against strict patterns.
- `theme_color` only accepts characters found in CSS colors.
- Models forbid unknown fields, so a typo cannot silently drop data.

## Reporting a vulnerability

Please report security issues privately through GitHub security advisories on the
repository instead of opening a public issue.
