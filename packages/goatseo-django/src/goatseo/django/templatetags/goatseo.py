"""Template tags: ``{% load goatseo %}`` then ``{% goatseo_head %}``."""

from django import template
from django.http import HttpRequest
from django.template.context import Context
from goatseo.core import SafeHtml, render_elements
from goatseo.django.state import get_seo, request_context
from goatseo.schema.jsonld import jsonld_element
from goatseo.seo import SEO

register = template.Library()


def _seo_and_request(context: Context) -> tuple[SEO, HttpRequest]:
    request: object = context.get("request")
    if not isinstance(request, HttpRequest):
        raise template.TemplateSyntaxError(
            "GoatSEO tags need 'django.template.context_processors.request' in the context"
        )
    seo: object = context.get("seo")
    return (seo if isinstance(seo, SEO) else get_seo(request)), request


@register.simple_tag(takes_context=True)
def goatseo_head(context: Context) -> SafeHtml:
    seo, request = _seo_and_request(context)
    return seo.render(request_context(request))


@register.simple_tag(takes_context=True)
def goatseo_jsonld(context: Context) -> SafeHtml:
    seo, _ = _seo_and_request(context)
    script = jsonld_element(seo.schemas)
    return render_elements([] if script is None else [script])
