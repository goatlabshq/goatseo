# Schema.org

`goatseo.schema` ships Pydantic models for the Schema.org vocabulary (version 30.1: core plus
the `health-lifesci`, `bib` and `auto` hosted extensions). They are
[generated](../topics/schema-generator.md) from the official ontology, never written by hand.

```python
from goatseo.schema import Article, Person

article = Article(
    headline="My article",
    description="An interesting article",
    author=Person(name="John Doe"),
)
```

## Naming

- Classes keep their Schema.org name: `Article`, `LocalBusiness`, `JobPosting`. Names that are
  not valid identifiers get an alias (`3DModel` is `Model3D`).
- Properties are snake_case: `datePublished` is `date_published`, `sameAs` is `same_as`.
  Python keywords and names reserved by Pydantic get a trailing underscore.
- The JSON-LD name of each field is kept in its annotation, so serialization uses the
  original camelCase names.

## Types

Each property accepts the union of its Schema.org ranges, a list of those values, or `None`:

```python
class Thing(SchemaModel):
    name: Annotated[str | list[str] | None, prop("name")] = None
    owner: Annotated[Organization | Person | list[Organization | Person] | None, prop("owner")] = (
        None
    )
```

Data types map to Python types:

| Schema.org | Python |
| --- | --- |
| `Text`, `URL`, `CssSelectorType`, `XPathType`, `PronounceableText` | `str` |
| `Quantity`, `Duration`, `Distance`, `Energy`, `Mass` | `str` (for example `"PT1H30M"`) |
| `Boolean` | `bool` |
| `Integer`, `Float`, `Number` | `int`, `float`, `int` or `float` |
| `Date`, `DateTime`, `Time` | `datetime.date`, `datetime.datetime`, `datetime.time` |

The inheritance of Schema.org is the inheritance of the classes, so a field typed
`CreativeWork` accepts an `Article`, and Pyright knows `article.author` is
`Organization | Person | list[Organization | Person] | None`.

Values are checked at runtime too: `Article(headline=123)` raises a `ValidationError`, and
assignments are validated.

## Enumerations

Enumerations with members are `StrEnum` subclasses of `SchemaEnumeration`; members serialize to
their IRI.

```python
from goatseo.schema import ItemAvailability, Offer

offer = Offer(price=19.99, price_currency="EUR", availability=ItemAvailability.InStock)
# "availability": "https://schema.org/InStock"
```

A range whose enumeration has many member-bearing subtypes accepts any `SchemaEnumeration`
rather than an unreadable union. Enumeration types without members (such as
`QualitativeValue`) are regular models, because Schema.org gives them properties.

## Deprecated properties

Properties superseded in Schema.org are still generated so existing data keeps working, but
setting one emits a `DeprecationWarning` naming its replacement:

```python
from goatseo.schema import CreativeWork

CreativeWork(awards="Best goat")  # DeprecationWarning: superseded by award
```

Deprecated types say so in their docstring.

## Identifiers and graphs

Every model has an `id` field serialized as `@id`. Use it to link nodes instead of nesting
them:

```python
from goatseo.schema import Organization, WebSite, to_graph

org = Organization(id="https://example.com/#org", name="Example")
site = WebSite(
    id="https://example.com/#website",
    url="https://example.com/",
    publisher=Organization(id="https://example.com/#org"),
)
to_graph([org, site])
# {"@context": "https://schema.org", "@graph": [{...}, {...}]}
```

With the SEO builder, one item renders as a single JSON-LD object and several items as one
`@graph` document:

```python
seo.schema(org, site)
```

See [JSON-LD](json-ld.md) for serialization details.
