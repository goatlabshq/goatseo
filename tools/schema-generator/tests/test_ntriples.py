import pytest

from goatseo_schema_generator.ntriples import Iri, Literal, NTriplesError, Triple, parse, unescape


def test_parses_iri_triple() -> None:
    [triple] = parse(["<https://schema.org/A> <http://p> <https://schema.org/B> ."])
    assert triple == Triple(
        Iri("https://schema.org/A"), Iri("http://p"), Iri("https://schema.org/B")
    )


def test_parses_literal_with_language() -> None:
    [triple] = parse(['<https://s/A> <http://p> "Hello"@en-GB .'])
    assert triple.object == Literal("Hello", "en-GB")


def test_parses_literal_with_datatype() -> None:
    [triple] = parse(['<https://s/A> <http://p> "3"^^<http://www.w3.org/2001/XMLSchema#int> .'])
    assert triple.object == Literal("3", None)


def test_unescapes_literals() -> None:
    [triple] = parse([r'<https://s/A> <http://p> "a \"q\" b\\c\ndé\U0001F600" .'])
    assert triple.object == Literal('a "q" b\\c\ndé\U0001f600')


@pytest.mark.parametrize(("escaped", "expected"), [(r"\t", "\t"), (r"\'", "'"), (r"A", "A")])
def test_unescape(escaped: str, expected: str) -> None:
    assert unescape(escaped) == expected


def test_skips_comments_and_blank_lines() -> None:
    lines = ["# comment", "", "   ", "<https://s/A> <http://p> <https://s/B> ."]
    assert len(list(parse(lines))) == 1


def test_malformed_line_reports_its_number() -> None:
    lines = ["<https://s/A> <http://p> <https://s/B> .", "not a triple"]
    with pytest.raises(NTriplesError, match="line 2"):
        list(parse(lines))
