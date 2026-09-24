# Architecture

> GoatSEO is a Python SEO engine first, and a framework integration library second.

## Package graph

```text
                 goatseo (facade)
                        │
                   goatseo-seo ◄──────────── goatseo-django
                        │       ◄──────────── goatseo-fastapi
                        │       ◄──────────── goatseo-flask
       ┌────────────────┼─────────────────┐
       │                │                 │
goatseo-opengraph  goatseo-twitter  goatseo-schema
       │                │                 │
       └────────────────┼─────────────────┘
                        │
                   goatseo-core ──► pydantic
```

| Package | Responsibility | May import |
| --- | --- | --- |
| `goatseo-core` | Metadata, precedence, URLs, validation, head elements, safe HTML and JSON | `pydantic` |
| `goatseo-schema` | Generated Schema.org models, JSON-LD serialization | core |
| `goatseo-opengraph` | Open Graph models and renderer | core |
| `goatseo-twitter` | Twitter/X Cards models and renderer | core |
| `goatseo-seo` | The `SEO` builder composing the above | core, schema, opengraph, twitter |
| `goatseo-django`, `goatseo-fastapi`, `goatseo-flask` | Thin adapters | seo and their framework |
| `goatseo` | `from goatseo import SEO`, framework extras | seo |

Dependency rules:

- Nothing below the adapters imports `django`, `flask`, `fastapi`, `starlette`, WSGI or ASGI
  code. Framework concepts reach the core only through `RequestContext`, a protocol with one
  `url` property.
- Models hold data; renderers turn data into head elements; one function turns head elements
  into HTML. No model contains markup or framework logic.
- Adapters only decide where state lives (the Django request, FastAPI dependencies,
  `flask.g`) and how templates print the result.

## Namespace layout

Every distribution contributes one subpackage of the `goatseo` import package:
`goatseo-core` owns `goatseo/core/`, `goatseo-schema` owns `goatseo/schema/`, and so on. Those
distributions ship no `goatseo/__init__.py`, which makes `goatseo` a namespace package when
only some of them are installed.

The `goatseo` facade distribution owns `goatseo/__init__.py`, so that `from goatseo import
SEO` works. Installed from wheels, all portions land in one `site-packages/goatseo`
directory and Python sees a regular package. In the development workspace each package is
installed in editable mode from its own `src/` directory, which would hide the other portions
behind the regular package; `goatseo/__init__.py` calls `pkgutil.extend_path` to add them to
`__path__`.

Pyright does not understand `extend_path`. The repository therefore contains
`.typecheck/goatseo`, a tree of symlinks presenting every portion under one directory, listed
in Pyright's `extraPaths`. See [contributing](contributing.md#type-checking).

## Rendering pipeline

```text
SEO
 ├─ MetadataStack ── resolve() ──► Metadata ──► metadata_elements ─┐
 ├─ OpenGraph (+ fallbacks) ─────────────────► open_graph_elements ├─► render_elements ─► SafeHtml
 ├─ TwitterCard (+ fallbacks) ───────────────► twitter_elements ───┤
 └─ SchemaModel items ───────────────────────► jsonld_element ─────┘
```

## Schema.org generation

Schema.org models are produced at development time by `tools/schema-generator` through
`RDF -> IR -> Python`, formatted with Ruff and committed. See
[schema generator](../topics/schema-generator.md).

## Repository layout

```text
goatseo/
├── packages/
│   ├── goatseo/            facade distribution
│   ├── goatseo-core/       src/goatseo/core
│   ├── goatseo-schema/     src/goatseo/schema (generated _types.py, _enumerations.py)
│   ├── goatseo-opengraph/
│   ├── goatseo-twitter/
│   ├── goatseo-seo/
│   ├── goatseo-django/
│   ├── goatseo-fastapi/
│   └── goatseo-flask/
├── tools/schema-generator/ generator and vendored ontology
├── tests/                  integration and typing tests
├── docs/
└── .typecheck/             symlinks for Pyright
```
