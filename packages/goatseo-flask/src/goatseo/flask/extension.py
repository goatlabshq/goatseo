"""Flask extension: request-scoped SEO state and a ``goatseo_head()`` Jinja global."""

from typing import Final

from flask import Flask, Response, current_app, g, request
from goatseo.core import Metadata, SafeHtml, StaticRequestContext
from goatseo.seo import SEO

EXTENSION_KEY: Final = "goatseo"
_STATE_KEY: Final = "_goatseo_seo"
ROBOTS_HEADER: Final = "X-Robots-Tag"


class SEOExtension:
    def __init__(
        self,
        app: Flask | None = None,
        *,
        defaults: Metadata | None = None,
        robots_header: bool = False,
    ) -> None:
        self.defaults = defaults
        self.robots_header = robots_header
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.extensions[EXTENSION_KEY] = self
        app.add_template_global(goatseo_head, "goatseo_head")
        app.context_processor(_inject_seo)
        if self.robots_header:
            app.after_request(_robots_header)


def _extension() -> SEOExtension:
    extension: object = current_app.extensions.get(EXTENSION_KEY)
    if not isinstance(extension, SEOExtension):
        raise RuntimeError("SEOExtension is not initialized on the current Flask app")
    return extension


def get_seo() -> SEO:
    """Returns the SEO object of the current request, created from the defaults on first use."""
    seo: object = g.get(_STATE_KEY)
    if not isinstance(seo, SEO):
        seo = SEO(defaults=_extension().defaults)
        setattr(g, _STATE_KEY, seo)
    return seo


def goatseo_head() -> SafeHtml:
    return get_seo().render(StaticRequestContext(request.url))


def _inject_seo() -> dict[str, SEO]:
    return {"seo": get_seo()}


def _robots_header(response: Response) -> Response:
    seo: object = g.get(_STATE_KEY)
    robots = seo.metadata.robots if isinstance(seo, SEO) else None
    if robots is not None and (directives := robots.directives()):
        response.headers.setdefault(ROBOTS_HEADER, ", ".join(directives))
    return response
