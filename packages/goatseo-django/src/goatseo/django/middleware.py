"""Optional middleware mirroring the page's robots directives in the ``X-Robots-Tag`` header."""

from collections.abc import Callable

from django.http import HttpRequest, HttpResponseBase
from goatseo.django.state import get_seo, has_seo

ROBOTS_HEADER = "X-Robots-Tag"


class GoatSEOMiddleware:
    def __init__(self, get_response: Callable[[HttpRequest], HttpResponseBase]) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponseBase:
        response = self.get_response(request)
        if has_seo(request) and ROBOTS_HEADER not in response.headers:
            robots = get_seo(request).metadata.robots
            if robots is not None and (directives := robots.directives()):
                response.headers[ROBOTS_HEADER] = ", ".join(directives)
        return response
