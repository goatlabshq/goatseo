"""System checks run by ``manage.py check``."""

from typing import Final

from django.conf import settings
from django.core.checks import CheckMessage, Error
from goatseo.core import Metadata
from goatseo.django.conf import SETTING

TAG: Final = "goatseo"


def check_defaults(**_kwargs: object) -> list[CheckMessage]:
    value: object = getattr(settings, SETTING, None)
    if value is None or isinstance(value, Metadata):
        return []
    return [
        Error(
            f"{SETTING} must be a goatseo.core.Metadata instance, not {type(value).__name__}.",
            hint=f"{SETTING} = Metadata(site_name=...)",
            id="goatseo.E001",
        )
    ]
