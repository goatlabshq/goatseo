"""SEO audit: checks that are valid HTML-wise but hurt search visibility."""

from collections import Counter
from collections.abc import Iterator
from dataclasses import dataclass
from enum import StrEnum
from typing import Final

from goatseo.core.metadata import X_DEFAULT, Metadata
from goatseo.core.urls import is_absolute

TITLE_MAX_LENGTH: Final = 60
DESCRIPTION_MIN_LENGTH: Final = 50
DESCRIPTION_MAX_LENGTH: Final = 160


class Severity(StrEnum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass(frozen=True, slots=True)
class Issue:
    code: str
    severity: Severity
    field: str
    message: str


def _title_issues(metadata: Metadata) -> Iterator[Issue]:
    title = metadata.full_title
    if title is None:
        yield Issue("missing-title", Severity.ERROR, "title", "The page has no title.")
    elif len(title) > TITLE_MAX_LENGTH:
        yield Issue(
            "title-too-long",
            Severity.WARNING,
            "title",
            f"The title has {len(title)} characters; search engines show about {TITLE_MAX_LENGTH}.",
        )


def _description_issues(metadata: Metadata) -> Iterator[Issue]:
    description = metadata.description
    if description is None:
        yield Issue(
            "missing-description", Severity.WARNING, "description", "The page has no description."
        )
    elif not DESCRIPTION_MIN_LENGTH <= len(description) <= DESCRIPTION_MAX_LENGTH:
        yield Issue(
            "description-length",
            Severity.INFO,
            "description",
            f"The description has {len(description)} characters; aim for "
            f"{DESCRIPTION_MIN_LENGTH} to {DESCRIPTION_MAX_LENGTH}.",
        )


def _canonical_issues(metadata: Metadata) -> Iterator[Issue]:
    if metadata.canonical is None:
        yield Issue("missing-canonical", Severity.INFO, "canonical", "No canonical URL is set.")
    elif not is_absolute(metadata.canonical):
        yield Issue(
            "relative-canonical",
            Severity.INFO,
            "canonical",
            "The canonical URL is relative; it is resolved against the request URL.",
        )


def _hreflang_issues(metadata: Metadata) -> Iterator[Issue]:
    languages = Counter(link.hreflang.lower() for link in metadata.hreflang or ())
    for language, count in sorted(languages.items()):
        if count > 1:
            yield Issue(
                "duplicate-hreflang",
                Severity.ERROR,
                "hreflang",
                f"hreflang {language!r} is declared {count} times.",
            )
    if languages and X_DEFAULT not in languages:
        yield Issue(
            "missing-x-default",
            Severity.INFO,
            "hreflang",
            "hreflang alternates have no x-default entry.",
        )


def audit(metadata: Metadata) -> tuple[Issue, ...]:
    return (
        *_title_issues(metadata),
        *_description_issues(metadata),
        *_canonical_issues(metadata),
        *_hreflang_issues(metadata),
    )
