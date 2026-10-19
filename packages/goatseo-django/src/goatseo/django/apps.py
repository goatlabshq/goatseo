from django.apps import AppConfig
from django.core import checks
from goatseo.django.checks import TAG, check_defaults


class GoatSEOConfig(AppConfig):
    name = "goatseo.django"
    label = "goatseo"
    verbose_name = "GoatSEO"

    def ready(self) -> None:
        checks.register(check_defaults, TAG)
