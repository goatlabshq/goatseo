import pytest

from goatseo.core import HrefLang, Issue, Metadata, Severity, audit


def _codes(issues: tuple[Issue, ...]) -> set[str]:
    return {issue.code for issue in issues}


def test_complete_metadata_has_no_issue() -> None:
    metadata = Metadata(
        title="A good title",
        description="A description long enough to be displayed nicely in search results.",
        canonical="https://example.com/",
    )
    assert audit(metadata) == ()


def test_empty_metadata() -> None:
    issues = audit(Metadata())
    assert _codes(issues) == {"missing-title", "missing-description", "missing-canonical"}
    assert next(i for i in issues if i.code == "missing-title").severity is Severity.ERROR


@pytest.mark.parametrize(
    ("metadata", "code"),
    [
        (Metadata(title="x" * 61), "title-too-long"),
        (Metadata(title="x" * 50, title_template="{title} | A long site name"), "title-too-long"),
        (Metadata(description="short"), "description-length"),
        (Metadata(description="x" * 161), "description-length"),
        (Metadata(canonical="/relative"), "relative-canonical"),
        (
            Metadata(
                hreflang=[HrefLang(hreflang="en", href="/a"), HrefLang(hreflang="EN", href="/b")]
            ),
            "duplicate-hreflang",
        ),
        (Metadata(hreflang=[HrefLang(hreflang="en", href="/a")]), "missing-x-default"),
    ],
)
def test_detects_issue(metadata: Metadata, code: str) -> None:
    assert code in _codes(audit(metadata))


def test_x_default_satisfies_hreflang_check() -> None:
    metadata = Metadata(
        hreflang=[HrefLang(hreflang="en", href="/a"), HrefLang(hreflang="x-default", href="/")]
    )
    assert "missing-x-default" not in _codes(audit(metadata))
