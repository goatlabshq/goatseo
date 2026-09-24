# GoatSEO

uv workspace of independently published packages sharing the `goatseo` import namespace.

## Layout

- `packages/goatseo-{core,schema,opengraph,twitter,seo}`: framework-independent engine. These
  must never import `django`, `flask`, `fastapi`, `starlette` or `werkzeug`.
- `packages/goatseo-{django,fastapi,flask}`: thin adapters.
- `packages/goatseo`: facade distribution. It alone owns `goatseo/__init__.py`; every other
  package is a namespace portion (`goatseo/core/`, ...). `pkgutil.extend_path` in that file makes
  editable installs work at runtime.
- `tools/schema-generator`: dev-only CLI `goatseo-schema` (not published).

## Rules

- `packages/goatseo-schema/src/goatseo/schema/_types.py`, `_enumerations.py` and `_version.py`
  are generated. Never edit them; change the generator and run `uv run goatseo-schema generate`.
- `.typecheck/goatseo` is a symlink tree merging the facade and every portion. Pyright cannot
  merge a regular package with namespace portions spread over several editable roots, so it
  resolves `goatseo` through `extraPaths = [".typecheck"]`. Add a symlink there when adding a
  package.
- `goatseo.schema` loads the generated models lazily (module `__getattr__`) and deliberately has
  no `__all__`, so wildcard-imported names stay exported to type checkers. `goatseo.seo` must
  only import `goatseo.schema.base` and `goatseo.schema.jsonld`.
- Pydantic resolves annotations at runtime: keep typing-only imports as real imports.
- Internal dependency pins and versions carry `# x-release-please-version`; release-please
  (`release/`) bumps them all together.

## Commands

```bash
uv sync
uv run pytest
uv run pyright
uv run ruff check . && uv run ruff format --check .
uv run goatseo-schema generate --check
```
