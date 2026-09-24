from goatseo_schema_generator.ir import Ontology
from goatseo_schema_generator.mapper import map_ontology
from goatseo_schema_generator.pyrender import (
    render_enumerations,
    render_types,
    render_version,
    summary,
)


def test_summary_cleans_markup() -> None:
    text = "A [[Thing]] with [docs](https://x.org) and <b>bold</b>. Second sentence."
    assert summary(text) == "A Thing with docs and bold."


def test_summary_keeps_abbreviations() -> None:
    assert summary("Some item, e.g. a book. Extra.") == "Some item, e.g. a book."


def test_summary_escapes_docstring_delimiters() -> None:
    assert summary('Quote """ and \\ backslash') == 'Quote \\"\\"\\" and \\\\ backslash'


def test_summary_truncates_and_handles_empty() -> None:
    assert summary(None) is None
    assert summary("") is None
    long = summary("word " * 100)
    assert long is not None
    assert long.endswith("...")
    assert len(long) <= 240


def test_rendered_modules(ontology: Ontology) -> None:
    module = map_ontology(ontology)
    types = render_types(module)
    assert "class Article(CreativeWork):" in types
    assert 'jsonld_type: ClassVar[str] = "Article"' in types
    assert 'prop("oldName", superseded_by=("name",))' in types
    assert "Deprecated: superseded by Article." in types
    assert "https://schema.org/Thing" in types
    enums = render_enumerations(module)
    assert 'InStock = "https://schema.org/InStock"' in enums
    assert 'SCHEMA_ORG_VERSION: Final = "1.0"' in render_version(module)
    compile(types, "_types.py", "exec")
    compile(enums, "_enumerations.py", "exec")
