# Packages

Every directory is an independently published distribution. All of them share the `goatseo`
import namespace.

| Directory           | Import              | Role                                                  |
| ------------------- | ------------------- | ----------------------------------------------------- |
| `goatseo`           | `goatseo`           | Facade: `from goatseo import SEO`, framework extras   |
| `goatseo-core`      | `goatseo.core`      | Metadata, precedence, URL safety, HTML rendering      |
| `goatseo-schema`    | `goatseo.schema`    | Generated Schema.org models and JSON-LD               |
| `goatseo-opengraph` | `goatseo.opengraph` | Open Graph models and renderer                        |
| `goatseo-twitter`   | `goatseo.twitter`   | Twitter/X Cards models and renderer                   |
| `goatseo-seo`       | `goatseo.seo`       | The `SEO` builder combining the packages above        |
| `goatseo-django`    | `goatseo.django`    | Django adapter                                        |
| `goatseo-fastapi`   | `goatseo.fastapi`   | FastAPI adapter                                       |
| `goatseo-flask`     | `goatseo.flask`     | Flask adapter                                         |

Rules:

- The engine packages (core, schema, opengraph, twitter, seo) never import a web framework.
- Only `goatseo` owns `goatseo/__init__.py`; the others are namespace portions.
- Each package has its own `pyproject.toml`, `README.md`, `LICENSE`, `src/` and `tests/`.
