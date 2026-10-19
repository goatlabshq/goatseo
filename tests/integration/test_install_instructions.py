import re
from pathlib import Path
from typing import Final

import pytest

ROOT: Final = Path(__file__).resolve().parents[2]
ADAPTER_ONLY_INSTALL: Final = re.compile(
    r"^\s*(?:pip install|uv add) goatseo-(?:django|fastapi|flask)\b", re.M
)
DOCUMENTS: Final = sorted(
    [ROOT / "README.md", *(ROOT / "docs").rglob("*.md"), *(ROOT / "packages").glob("*/README.md")]
)


@pytest.mark.parametrize("document", DOCUMENTS, ids=lambda path: str(path.relative_to(ROOT)))
def test_adapters_are_installed_with_the_facade(document: Path) -> None:
    # An adapter alone does not ship goatseo/__init__.py, so "from goatseo import ..." fails.
    assert not ADAPTER_ONLY_INSTALL.findall(document.read_text())
