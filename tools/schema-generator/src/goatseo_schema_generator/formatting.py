"""Formats generated code with Ruff, using the configuration that applies to the target file."""

import subprocess
import sys
from pathlib import Path
from typing import Final

_FIXES: Final = "I,RUF022"


def _ruff(arguments: list[str], source: str) -> str:
    completed = subprocess.run(  # noqa: S603
        [sys.executable, "-m", "ruff", *arguments],
        input=source,
        capture_output=True,
        text=True,
        check=True,
    )
    return completed.stdout


def format_source(source: str, target: Path) -> str:
    stdin = ["--stdin-filename", str(target), "-"]
    fixed = _ruff(["check", "--fix-only", "--exit-zero", "--select", _FIXES, *stdin], source)
    return _ruff(["format", *stdin], fixed)
