"""Django integration for GoatSEO."""

from goatseo.django.metadata import model_metadata
from goatseo.django.state import get_seo, request_context
from goatseo.django.views import SEOMixin, seo_defaults

__all__ = ["SEOMixin", "get_seo", "model_metadata", "request_context", "seo_defaults"]
