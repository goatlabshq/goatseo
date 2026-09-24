# Installation

GoatSEO requires **Python 3.14** or newer.

## The main package

```bash
pip install goatseo
# or
uv add goatseo
```

`goatseo` installs the high-level API (`goatseo-seo`) together with the core, Schema.org,
Open Graph and Twitter/X packages. It never installs a web framework.

## Framework integrations

Install the adapter for your framework, either directly or through an extra:

=== "Django"

    ```bash
    pip install goatseo-django      # or: pip install "goatseo[django]"
    ```

=== "FastAPI"

    ```bash
    pip install goatseo-fastapi     # or: pip install "goatseo[fastapi]"
    ```

=== "Flask"

    ```bash
    pip install goatseo-flask       # or: pip install "goatseo[flask]"
    ```

Each adapter depends on `goatseo-seo` and its framework only.

## Individual packages

Every package is published independently, so a library that only needs typed metadata can
depend on `goatseo-core`, and a tool that only emits JSON-LD can depend on `goatseo-schema`.

| Distribution | Dependencies |
| --- | --- |
| `goatseo-core` | `pydantic` |
| `goatseo-schema` | `goatseo-core`, `pydantic` |
| `goatseo-opengraph` | `goatseo-core`, `pydantic` |
| `goatseo-twitter` | `goatseo-core`, `pydantic` |
| `goatseo-seo` | core, schema, opengraph, twitter |
| `goatseo-django` | `goatseo-seo`, `django>=5.2` |
| `goatseo-fastapi` | `goatseo-seo`, `fastapi>=0.115` |
| `goatseo-flask` | `goatseo-seo`, `flask>=3.1` |

All GoatSEO packages of one release share the same version and pin each other exactly.
