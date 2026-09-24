import subprocess
import sys

import pytest

import goatseo.schema


def _run(code: str) -> str:
    completed = subprocess.run(  # noqa: S603
        [sys.executable, "-c", code], capture_output=True, text=True, check=True
    )
    return completed.stdout.strip()


def test_types_load_on_first_access() -> None:
    code = (
        "import sys, goatseo.schema\n"
        "print('goatseo.schema._types' in sys.modules)\n"
        "goatseo.schema.Article\n"
        "print('goatseo.schema._types' in sys.modules)"
    )
    assert _run(code).split() == ["False", "True"]


def test_unknown_names_raise_attribute_error() -> None:
    with pytest.raises(AttributeError, match="NotASchemaType"):
        _ = goatseo.schema.NotASchemaType


def test_resolved_names_are_cached() -> None:
    first = goatseo.schema.Article
    assert goatseo.schema.__dict__["Article"] is first
