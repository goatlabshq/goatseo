import subprocess
import sys
from pathlib import Path
from typing import Final

PROJECT: Final = Path(__file__).parent / "django_project"


def test_django_project_suite_passes() -> None:
    result = subprocess.run(
        [sys.executable, "-W", "error", "-m", "django", "test", "--settings", "blogsite.settings"],
        cwd=PROJECT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Ran 9 tests" in result.stderr
