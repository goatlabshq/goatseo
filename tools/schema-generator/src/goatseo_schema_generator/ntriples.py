"""Minimal, strict N-Triples reader for the Schema.org release files."""

import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True, slots=True)
class Iri:
    value: str


@dataclass(frozen=True, slots=True)
class Literal:
    value: str
    language: str | None = None


type Term = Iri | Literal


@dataclass(frozen=True, slots=True)
class Triple:
    subject: Iri
    predicate: Iri
    object: Term


class NTriplesError(ValueError):
    def __init__(self, line_number: int, line: str) -> None:
        super().__init__(f"line {line_number}: cannot parse {line!r}")


_TRIPLE: Final = re.compile(
    r"""^<(?P<subject>[^>]*)>\s+<(?P<predicate>[^>]*)>\s+
    (?:<(?P<iri>[^>]*)>|"(?P<literal>(?:[^"\\]|\\.)*)"(?:@(?P<lang>[A-Za-z0-9-]+)|\^\^<[^>]*>)?)
    \s*\.\s*$""",
    re.VERBOSE,
)
_ESCAPE: Final = re.compile(r"\\(?:u([0-9A-Fa-f]{4})|U([0-9A-Fa-f]{8})|(.))")
_SIMPLE_ESCAPES: Final = {"t": "\t", "b": "\b", "n": "\n", "r": "\r", "f": "\f", '"': '"', "'": "'"}


def _unescape_match(match: re.Match[str]) -> str:
    short, long, char = match.groups()
    if short or long:
        return chr(int(short or long, 16))
    return _SIMPLE_ESCAPES.get(char, char)


def unescape(value: str) -> str:
    return _ESCAPE.sub(_unescape_match, value)


def parse_line(line: str, line_number: int) -> Triple | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    match = _TRIPLE.match(stripped)
    if match is None:
        raise NTriplesError(line_number, line)
    iri = match.group("iri")
    term: Term = (
        Iri(iri)
        if iri is not None
        else Literal(unescape(match.group("literal")), match.group("lang"))
    )
    return Triple(Iri(match.group("subject")), Iri(match.group("predicate")), term)


def parse(lines: Iterable[str]) -> Iterator[Triple]:
    for number, line in enumerate(lines, start=1):
        triple = parse_line(line, number)
        if triple is not None:
            yield triple
