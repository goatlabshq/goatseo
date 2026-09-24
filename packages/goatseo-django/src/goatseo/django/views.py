"""View integration: a class-based view mixin and a function-based view decorator."""

from collections.abc import Callable
from functools import wraps
from typing import Any, Concatenate, Unpack

from django.http import HttpRequest, HttpResponseBase
from django.views.generic.base import ContextMixin
from goatseo.core import Metadata, MetadataFields, Precedence, SupportsMetadata
from goatseo.django.state import get_seo


class SEOMixin(ContextMixin):
    """Adds ``seo_metadata`` as the view layer and the view's ``object`` as the model layer.

    Combine it with any class-based view: ``class ArticleView(SEOMixin, DetailView)``.
    """

    request: HttpRequest
    seo_metadata: Metadata | None = None

    def get_seo_metadata(self) -> Metadata | None:
        return self.seo_metadata

    # Any mirrors django-stubs' signature of get_context_data, which this method overrides.
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        seo = get_seo(self.request)
        if (metadata := self.get_seo_metadata()) is not None:
            seo.defaults(metadata, Precedence.VIEW)
        source: object = getattr(self, "object", None)
        if isinstance(source, SupportsMetadata):
            seo.from_object(source)
        context = super().get_context_data(**kwargs)
        context["seo"] = seo
        return context


def seo_defaults[**P, R: HttpResponseBase](
    **fields: Unpack[MetadataFields],
) -> Callable[[Callable[Concatenate[HttpRequest, P], R]], Callable[Concatenate[HttpRequest, P], R]]:
    """Sets the view layer of a function-based view: ``@seo_defaults(title="Blog")``."""
    metadata = Metadata.model_validate(fields)

    def decorator(
        view: Callable[Concatenate[HttpRequest, P], R],
    ) -> Callable[Concatenate[HttpRequest, P], R]:
        @wraps(view)
        def wrapper(request: HttpRequest, *args: P.args, **kwargs: P.kwargs) -> R:
            get_seo(request).defaults(metadata, Precedence.VIEW)
            return view(request, *args, **kwargs)

        return wrapper

    return decorator
