# .typecheck

Symlinks exposing one merged `goatseo` package, used only by Pyright through
`extraPaths = [".typecheck"]` in the root `pyproject.toml`.

In the workspace, `goatseo/__init__.py` (facade) and its subpackages (`goatseo.core`,
`goatseo.schema`, ...) live in separate editable roots. Python merges them at runtime through
`pkgutil.extend_path`, but Pyright stops at the first regular `goatseo` package it finds and
cannot resolve the others. Installed wheels share one `site-packages/goatseo/` directory, so end
users never need this.

When adding a package, add its symlink:

```bash
ln -s ../../packages/goatseo-<name>/src/goatseo/<name> .typecheck/goatseo/<name>
```
