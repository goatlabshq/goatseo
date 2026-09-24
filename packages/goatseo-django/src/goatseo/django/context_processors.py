from django.http import HttpRequest
from goatseo.django.state import get_seo
from goatseo.seo import SEO


def seo(request: HttpRequest) -> dict[str, SEO]:
    return {"seo": get_seo(request)}
