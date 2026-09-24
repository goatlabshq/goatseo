"""Command line entry point: ``goatseo-schema generate``."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Final

from goatseo_schema_generator.generator import (
    load_ontology,
    render_modules,
    stale_files,
    write_modules,
)
from goatseo_schema_generator.ir import Layer
from goatseo_schema_generator.parser import DEFAULT_LAYERS
from goatseo_schema_generator.sources import (
    download,
    latest_version,
    newest_vendored,
    version_from_filename,
)

DEFAULT_OUTPUT: Final = (
    Path(__file__).resolve().parents[4] / "packages/goatseo-schema/src/goatseo/schema"
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="goatseo-schema")
    commands = parser.add_subparsers(dest="command", required=True)
    generate = commands.add_parser("generate", help="generate the Schema.org Python models")
    source = generate.add_mutually_exclusive_group()
    source.add_argument("--version", help="Schema.org release to download, or 'latest'")
    source.add_argument("--source", type=Path, help="local schemaorg-*-https.nt file")
    generate.add_argument("--schema-version", help="version label when --source has no version")
    generate.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    generate.add_argument(
        "--include-pending", action="store_true", help="also generate pending.schema.org terms"
    )
    generate.add_argument(
        "--check", action="store_true", help="fail when the generated files are out of date"
    )
    return parser


def _resolve_source(args: argparse.Namespace) -> tuple[Path, str]:
    version: str | None = args.version
    if version is not None:
        version = latest_version() if version == "latest" else version
        return download(version), version
    source: Path = args.source or newest_vendored()
    label: str | None = args.schema_version or version_from_filename(source)
    return source, label or "unknown"


def generate(args: argparse.Namespace) -> int:
    source, version = _resolve_source(args)
    layers = DEFAULT_LAYERS | {Layer.PENDING} if args.include_pending else DEFAULT_LAYERS
    output: Path = args.output
    modules = render_modules(load_ontology(source, version, layers), output)
    stale = stale_files(modules)
    if args.check:
        for path in stale:
            print(f"out of date: {path}", file=sys.stderr)
        return 1 if stale else 0
    write_modules(modules)
    print(f"Schema.org {version}: wrote {len(modules)} modules to {output}")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    return generate(args)


if __name__ == "__main__":
    raise SystemExit(main())
