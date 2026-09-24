"""Pipeline: N-Triples -> IR -> Python declarations -> formatted modules."""

from collections.abc import Collection, Mapping
from pathlib import Path

from goatseo_schema_generator.formatting import format_source
from goatseo_schema_generator.ir import Layer, Ontology
from goatseo_schema_generator.mapper import map_ontology
from goatseo_schema_generator.ntriples import parse
from goatseo_schema_generator.parser import DEFAULT_LAYERS, build_ontology
from goatseo_schema_generator.pyrender import render_enumerations, render_types, render_version


def load_ontology(
    source: Path, version: str, layers: Collection[Layer] = DEFAULT_LAYERS
) -> Ontology:
    with source.open(encoding="utf-8") as lines:
        return build_ontology(parse(lines), version, layers)


def render_modules(ontology: Ontology, output: Path) -> Mapping[Path, str]:
    module = map_ontology(ontology)
    sources = {
        "_types.py": render_types(module),
        "_enumerations.py": render_enumerations(module),
        "_version.py": render_version(module),
    }
    return {output / name: format_source(source, output / name) for name, source in sources.items()}


def stale_files(modules: Mapping[Path, str]) -> list[Path]:
    return [
        path
        for path, source in modules.items()
        if not path.exists() or path.read_text(encoding="utf-8") != source
    ]


def write_modules(modules: Mapping[Path, str]) -> None:
    for path, source in modules.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(source, encoding="utf-8")
