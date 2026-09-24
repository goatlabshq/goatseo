# Performance

GoatSEO does its expensive work at development time. Schema.org is parsed and turned into
Python by the [generator](schema-generator.md); the installed packages contain ordinary
modules and never read the ontology.

## Import cost

Measured on CPython 3.14 (Apple silicon):

| Import | Time |
| --- | --- |
| `from goatseo import SEO` | about 0.1 s |
| `import goatseo.schema` | about 0.08 s |
| First access to a generated type (`from goatseo.schema import Article`) | about 0.7 s, once |

Most of the first two numbers is Pydantic itself. The third one is the creation of 789
Pydantic classes, dominated by Pydantic copying inherited fields down deep Schema.org
hierarchies.

To keep that cost out of applications that do not use Schema.org, `goatseo.schema` loads its
generated modules lazily: the package imports only the base classes and the JSON-LD
serializer, and a module-level `__getattr__` loads the generated types on first access. The
`SEO` builder depends only on those base classes, so rendering metadata, Open Graph and Twitter
never triggers the generated modules.

## Validation cost

Schema.org is a deeply recursive graph: `Thing` refers to `CreativeWork`, which refers to
`Person`, which refers back to `Thing`. Letting Pydantic build a full validation schema for one
model would build it for most of the vocabulary.

Generated fields carry a `prop` marker instead. It validates each value with an `isinstance`
check against the declared types and never asks Pydantic for the schema of nested models.
Models also use `defer_build=True`, so a class builds its (small) validator only when first
instantiated. Creating a first `Article` takes a few milliseconds.

## Rendering cost

- Metadata layers are merged once per `SEO` object and cached until a layer changes.
- Settings (`GOATSEO_DEFAULTS`, extension defaults) are validated once at startup, not per
  request.
- JSON-LD is serialized once, directly from the models, without an intermediate
  `model_dump`.
- No adapter performs database queries; model metadata comes from objects your view already
  loaded.
