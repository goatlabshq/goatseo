# Contributing

## Setup

GoatSEO is a [uv](https://docs.astral.sh/uv/) workspace. Python 3.14 is required.

```bash
git clone https://github.com/goatlabshq/goatseo.git
cd goatseo
uv sync
uv run lefthook install
```

`uv sync` installs every package of the workspace in editable mode, plus the development
tools.

## Checks

```bash
uv run pytest
uv run pyright
uv run ruff check .
uv run ruff format --check .
uv run goatseo-schema generate --check
```

CI runs the same commands, builds every package with `uv build --all-packages` and validates
the distributions.

## Git hooks

[lefthook](https://lefthook.dev) runs the checks locally:

- **pre-commit**: Ruff lint and format on staged files.
- **commit-msg**: the message must be a conventional commit.
- **pre-push**: Pyright and the test suite.

## Commits

Commits are atomic and follow [Conventional Commits](https://www.conventionalcommits.org):
`type: description` on a single subject line, for example `feat: add book metadata to Open
Graph` or `fix: escape U+2028 in JSON-LD`. Commit types drive the version and the changelog.

## Releases

[release-please](https://github.com/googleapis/release-please) reads the conventional commits,
opens a release pull request that bumps the version of every package and updates
`CHANGELOG.md`, and publishes the packages when it is merged. Its configuration lives in
`release/config.json` and `release/.manifest.json`. All packages share one version and pin
each other exactly.

## Regenerating Schema.org models

Never edit `packages/goatseo-schema/src/goatseo/schema/_types.py`,
`_enumerations.py` or `_version.py` by hand:

```bash
uv run goatseo-schema generate                   # from the vendored release
uv run goatseo-schema generate --version latest  # download a newer release
```

See [schema generator](../topics/schema-generator.md).

## Type checking

The `goatseo` facade owns `goatseo/__init__.py`, and every other package contributes a
subpackage from its own `src/` directory. At runtime `pkgutil.extend_path` merges them, but
Pyright follows Python's rule that a regular package hides namespace portions found in other
path entries, and cannot merge a regular `goatseo` package with portions spread over several
editable roots.

`.typecheck/goatseo` solves this: it is a committed tree of symlinks exposing
`goatseo/__init__.py` and every `goatseo/<package>` directory in one place, and Pyright lists
`.typecheck` in `extraPaths`. Pyright resolves the symlinks, so errors are reported on the real
files. When you add a package, add its symlink:

```bash
ln -s ../../packages/goatseo-<name>/src/goatseo/<name> .typecheck/goatseo/<name>
```

## Code style

- English everywhere in the repository.
- Code explains itself: explicit names, small functions, named constants. Comments explain a
  *why* in at most two lines.
- Full annotations; no `Any` unless mirroring a third-party signature, with a comment.
- New behavior comes with tests; new public types come with a type contract test when a
  misuse should be rejected by Pyright.
