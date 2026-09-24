"""FastAPI integration built on dependency injection and Jinja2 templates."""

from starlette.requests import Request
from starlette.templating import Jinja2Templates

from goatseo.core import Metadata, SafeHtml, StaticRequestContext
from goatseo.seo import SEO


def request_context(request: Request) -> StaticRequestContext:
    return StaticRequestContext(str(request.url))


def goatseo_head(seo: SEO, request: Request) -> SafeHtml:
    return seo.render(request_context(request))


class GoatSEO:
    """A dependency that gives each request a fresh :class:`SEO` built from site defaults.

    ``SEODep = Annotated[SEO, Depends(GoatSEO(defaults=...))]``; FastAPI caches it per request.
    """

    __slots__ = ("defaults",)

    def __init__(self, defaults: Metadata | None = None) -> None:
        self.defaults = defaults

    def __call__(self) -> SEO:
        return SEO(defaults=self.defaults)

    def install(self, templates: Jinja2Templates) -> None:
        """Exposes ``{{ goatseo_head(seo, request) }}`` to the templates."""
        # Jinja infers Environment.globals from its default entries, which rejects any callable.
        templates.env.globals["goatseo_head"] = goatseo_head  # pyright: ignore[reportArgumentType]
