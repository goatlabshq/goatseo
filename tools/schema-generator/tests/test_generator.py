import json
from pathlib import Path

import pytest

from goatseo_schema_generator import sources
from goatseo_schema_generator.cli import main
from goatseo_schema_generator.generator import load_ontology, render_modules, stale_files


def test_generation_is_deterministic(fixture_source: Path, tmp_path: Path) -> None:
    first = render_modules(load_ontology(fixture_source, "1.0"), tmp_path)
    second = render_modules(load_ontology(fixture_source, "1.0"), tmp_path)
    assert first == second
    assert {p.name for p in first} == {"_types.py", "_enumerations.py", "_version.py"}


def test_check_reports_stale_then_fresh(fixture_source: Path, tmp_path: Path) -> None:
    arguments = ["generate", "--source", str(fixture_source), "--output", str(tmp_path)]
    assert main([*arguments, "--check"]) == 1
    assert main(arguments) == 0
    assert main([*arguments, "--check"]) == 0
    (tmp_path / "_types.py").write_text("# edited\n", encoding="utf-8")
    assert main([*arguments, "--check"]) == 1


def test_generated_code_is_formatted_and_executable(fixture_source: Path, tmp_path: Path) -> None:
    modules = render_modules(load_ontology(fixture_source, "1.0"), tmp_path)
    assert stale_files(modules) == list(modules)
    types = modules[tmp_path / "_types.py"]
    assert "author: Annotated[" in types
    for source in modules.values():
        compile(source, "generated.py", "exec")


def test_pending_terms_are_opt_in(fixture_source: Path, tmp_path: Path) -> None:
    base = ["generate", "--source", str(fixture_source), "--output", str(tmp_path)]
    main(base)
    assert "class PendingWork" not in (tmp_path / "_types.py").read_text(encoding="utf-8")
    main([*base, "--include-pending"])
    assert "class PendingWork" in (tmp_path / "_types.py").read_text(encoding="utf-8")


def test_committed_models_match_the_vendored_ontology() -> None:
    assert main(["generate", "--check"]) == 0


def test_version_from_filename() -> None:
    assert sources.version_from_filename(Path("schemaorg-30.1-current-https.nt")) == "30.1"
    assert sources.version_from_filename(Path("other.nt")) is None


def test_newest_vendored(tmp_path: Path) -> None:
    for version in ("9.0", "10.1", "10.0"):
        sources.release_path(version, tmp_path).write_text("", encoding="utf-8")
    assert sources.newest_vendored(tmp_path).name == "schemaorg-10.1-current-https.nt"
    with pytest.raises(sources.SourceError):
        sources.newest_vendored(tmp_path / "missing")


def test_latest_version_and_download(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    fetched: list[str] = []

    def fake_fetch(url: str) -> bytes:
        fetched.append(url)
        if url == sources.VERSIONS_URL:
            return json.dumps({"schemaversion": "31.0"}).encode()
        return b"<https://schema.org/A> <http://p> <https://schema.org/B> .\n"

    monkeypatch.setattr(sources, "_fetch", fake_fetch)
    assert sources.latest_version() == "31.0"
    path = sources.download("31.0", tmp_path)
    assert path.read_bytes().startswith(b"<https://schema.org/A>")
    sources.download("31.0", tmp_path)
    assert fetched == [sources.VERSIONS_URL, sources.RELEASE_URL.format(version="31.0")]


def test_invalid_sources(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    def fake_fetch(_url: str) -> bytes:
        return b'{"schemaversion": "../x"}'

    monkeypatch.setattr(sources, "_fetch", fake_fetch)
    with pytest.raises(sources.SourceError):
        sources.latest_version()
    with pytest.raises(sources.SourceError):
        sources.download("../../etc", tmp_path)


def test_insecure_scheme_is_refused() -> None:
    with pytest.raises(sources.SourceError, match="insecure"):
        sources._fetch("http://schema.org/x")  # pyright: ignore[reportPrivateUsage]
