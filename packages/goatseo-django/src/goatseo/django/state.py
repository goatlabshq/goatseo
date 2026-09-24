"""Request-scoped SEO state."""

from weakref import WeakKeyDictionary

from django.http import HttpRequest
from goatseo.core import StaticRequestContext
from goatseo.django.conf import site_defaults
from goatseo.seo import SEO

_STATE: WeakKeyDictionary[HttpRequest, SEO] = WeakKeyDictionary()


def get_seo(request: HttpRequest) -> SEO:
    """Returns the SEO object of ``request``, created from ``GOATSEO_DEFAULTS`` on first use."""
    seo = _STATE.get(request)
    if seo is None:
        seo = _STATE[request] = SEO(defaults=site_defaults())
    return seo


def has_seo(request: HttpRequest) -> bool:
    return request in _STATE


def request_context(request: HttpRequest) -> StaticRequestContext:
    return StaticRequestContext(request.build_absolute_uri())
