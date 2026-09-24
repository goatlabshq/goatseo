# Type safety

Static typing is part of the GoatSEO API contract. The whole repository, including the
generated Schema.org models and the framework adapters, passes Pyright with
`typeCheckingMode = "strict"`.

## Typed constructors

Every model is a Pydantic v2 model. Pydantic declares `dataclass_transform`, so Pyright
synthesizes an `__init__` from the fields and checks each keyword argument:

```python
from goatseo.schema import Article, ItemAvailability, Offer, Person

Article(headline=123)  # error: "Literal[123]" is not assignable to "str"
Offer(availability="InStock")  # error: expects ItemAvailability
Article(author=Person(name="John Doe"))  # ok

article = Article(author=Person(name="John Doe"))
reveal_type(article.author)
# Organization | Person | list[Organization | Person] | None
```

The same holds for `Metadata`, `OpenGraph` (whose `type` is a `Literal`), `TwitterCard`
(whose `card` is a `StrEnum`) and the `SEO` builder, whose keyword arguments are typed with
`Unpack[MetadataFields]` and `Unpack[RobotsDirectives]`.

## Typing features used

- `Protocol` for framework-neutral interfaces (`RequestContext`, `SupportsMetadata`,
  `ElementRenderer[T]`).
- PEP 695 generics and type aliases (`type JsonValue = ...`, `class ElementRenderer[T]`).
- `Self` return types for chaining, `@overload` for `SEO.hreflang`, `TypeIs` guards,
  `Final` constants, `Literal` and `StrEnum` for closed sets of values.
- `ParamSpec` and `Concatenate` in the Django `seo_defaults` decorator, so decorated views keep
  their signature.

`Any` is avoided. The only occurrences mirror third-party signatures that GoatSEO overrides
(Django's `get_context_data`), and each is commented.

## Type contract tests

`tests/typing` holds Pyright fixtures: small files that must fail type checking on the lines
marked as expected errors. A pytest test runs Pyright on them and fails if an error disappears,
so loosening a type is caught like any other regression.

## Known limitation: lazy Schema.org imports

`goatseo.schema` loads its generated modules on first attribute access through a module-level
`__getattr__` (see [performance](performance.md)). Pyright sees every real class through
`TYPE_CHECKING` imports, but a module with `__getattr__` accepts any attribute name, so

```python
from goatseo.schema import Aticle  # typo
```

is typed as `object` instead of being reported as a missing name. It still fails at runtime
with `ImportError`, and any use of the misspelled name as a class is reported by Pyright.

## Running the checks

```bash
uv run pyright
```
