"""Locates or downloads the official Schema.org release files."""

import json
import re
import urllib.request
from pathlib import Path
from typing import Final

RELEASE_URL: Final = "https://schema.org/version/{version}/schemaorg-current-https.nt"
VERSIONS_URL: Final = "https://raw.githubusercontent.com/schemaorg/schemaorg/main/versions.json"
DATA_DIRECTORY: Final = Path(__file__).resolve().parents[2] / "data"
_FILENAME: Final = re.compile(r"schemaorg-(?P<version>\d+(?:\.\d+)*)-current-https\.nt$")
_VERSION: Final = re.compile(r"^\d+(?:\.\d+)*$")
_TIMEOUT_SECONDS: Final = 60


class SourceError(RuntimeError):
    pass


def _fetch(url: str) -> bytes:
    if not url.startswith("https://"):
        raise SourceError(f"refusing to download over an insecure scheme: {url}")
    with urllib.request.urlopen(url, timeout=_TIMEOUT_SECONDS) as response:  # noqa: S310
        body: bytes = response.read()
        return body


def latest_version() -> str:
    payload: object = json.loads(_fetch(VERSIONS_URL))
    match payload:
        case {"schemaversion": str() as version} if _VERSION.match(version):
            return version
        case _:
            raise SourceError(f"cannot read the latest version from {VERSIONS_URL}")


def release_path(version: str, directory: Path = DATA_DIRECTORY) -> Path:
    return directory / f"schemaorg-{version}-current-https.nt"


def download(version: str, directory: Path = DATA_DIRECTORY) -> Path:
    if not _VERSION.match(version):
        raise SourceError(f"invalid Schema.org version {version!r}")
    target = release_path(version, directory)
    if not target.exists():
        directory.mkdir(parents=True, exist_ok=True)
        target.write_bytes(_fetch(RELEASE_URL.format(version=version)))
    return target


def vendored_releases(directory: Path = DATA_DIRECTORY) -> list[tuple[tuple[int, ...], Path]]:
    releases: list[tuple[tuple[int, ...], Path]] = []
    for path in directory.glob("schemaorg-*-current-https.nt"):
        version = version_from_filename(path)
        if version is not None:
            releases.append((tuple(int(part) for part in version.split(".")), path))
    return sorted(releases)


def newest_vendored(directory: Path = DATA_DIRECTORY) -> Path:
    releases = vendored_releases(directory)
    if not releases:
        raise SourceError(f"no Schema.org release in {directory}; pass --version or --source")
    return releases[-1][1]


def version_from_filename(path: Path) -> str | None:
    match = _FILENAME.search(path.name)
    return match.group("version") if match else None
