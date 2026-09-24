"""Reads the ``GOATSEO_DEFAULTS`` setting once and re-reads it when tests override it."""

from functools import cache
from typing import Final

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.signals import setting_changed
from django.dispatch import receiver
from goatseo.core import Metadata

SETTING: Final = "GOATSEO_DEFAULTS"


@cache
def site_defaults() -> Metadata | None:
    value: object = getattr(settings, SETTING, None)
    if value is None or isinstance(value, Metadata):
        return value
    raise ImproperlyConfigured(f"{SETTING} must be a goatseo.core.Metadata instance")


@receiver(setting_changed)
def _reset_defaults(*, setting: str, **_kwargs: object) -> None:
    if setting == SETTING:
        site_defaults.cache_clear()
