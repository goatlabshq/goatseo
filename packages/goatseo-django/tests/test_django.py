from types import ModuleType

import pytest
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest, HttpResponse
from django.template import TemplateSyntaxError, engines
from django.test import Client, RequestFactory, override_settings
from django.urls import path
from django.views.generic import TemplateView

from goatseo.core import Metadata
from goatseo.django import SEOMixin, get_seo, seo_defaults
from goatseo.django.context_processors import seo as seo_processor
from goatseo.schema import Article, Person

XSS = "</title><script>alert(1)</script>"


def render(source: str, request: HttpRequest | None = None) -> str:
    return engines["django"].from_string(source).render({}, request)


class Page:
    def seo_metadata(self) -> Metadata:
        return Metadata(title="Object title", description="Object description")


class PageView(SEOMixin, TemplateView):
    template_name = "goatseo/head.html"
    seo_metadata = Metadata(title="View title")
    object: Page

    def setup(self, request: HttpRequest, *args: object, **kwargs: object) -> None:
        super().setup(request, *args, **kwargs)
        self.object = Page()


@seo_defaults(title="Blog", description="All posts")
def blog(request: HttpRequest) -> HttpResponse:
    get_seo(request).title("Post")
    return HttpResponse(render("{% load goatseo %}{% goatseo_head %}", request))


def noindex(request: HttpRequest) -> HttpResponse:
    get_seo(request).robots(index=False, follow=True)
    return HttpResponse("ok")


def explicit_header(request: HttpRequest) -> HttpResponse:
    get_seo(request).robots(index=False)
    response = HttpResponse("ok")
    response.headers["X-Robots-Tag"] = "none"
    return response


def plain(request: HttpRequest) -> HttpResponse:
    get_seo(request).title("Plain")
    return HttpResponse("ok")


def xss(request: HttpRequest) -> HttpResponse:
    get_seo(request).title(XSS).description('" onload="alert(1)')
    return HttpResponse(render("{% load goatseo %}{% goatseo_head %}", request))


URLS = ModuleType("goatseo_django_test_urls")
URLS.__dict__["urlpatterns"] = [
    path("pages/<int:pk>", PageView.as_view()),
    path("blog", blog),
    path("noindex", noindex),
    path("explicit", explicit_header),
    path("plain", plain),
    path("xss", xss),
]


@pytest.fixture
def client() -> Client:
    return Client()


def test_app_config_label() -> None:
    assert apps.get_app_config("goatseo").name == "goatseo.django"


def test_seo_is_scoped_to_the_request() -> None:
    factory = RequestFactory()
    first, second = factory.get("/"), factory.get("/")
    assert get_seo(first) is get_seo(first)
    assert get_seo(first) is not get_seo(second)


def test_defaults_setting_is_the_site_layer() -> None:
    defaults = Metadata(site_name="Example", title_template="{title} | Example")
    with override_settings(GOATSEO_DEFAULTS=defaults):
        seo = get_seo(RequestFactory().get("/")).title("Hello")
        assert seo.metadata.full_title == "Hello | Example"


def test_defaults_are_reread_when_the_setting_changes() -> None:
    with override_settings(GOATSEO_DEFAULTS=Metadata(site_name="First")):
        assert get_seo(RequestFactory().get("/")).metadata.site_name == "First"
    with override_settings(GOATSEO_DEFAULTS=Metadata(site_name="Second")):
        assert get_seo(RequestFactory().get("/")).metadata.site_name == "Second"
    assert get_seo(RequestFactory().get("/")).metadata.site_name is None


def test_invalid_defaults_setting_is_rejected() -> None:
    with (
        override_settings(GOATSEO_DEFAULTS={"title": "x"}),
        pytest.raises(ImproperlyConfigured),
    ):
        get_seo(RequestFactory().get("/"))


def test_context_processor_exposes_the_request_seo() -> None:
    request = RequestFactory().get("/")
    assert seo_processor(request) == {"seo": get_seo(request)}


def test_head_tag_resolves_canonical_against_the_request() -> None:
    request = RequestFactory().get("/articles/hello?page=2")
    get_seo(request).title("Hello").canonical("/articles/hello")
    html = render("{% load goatseo %}<head>{% goatseo_head %}</head>", request)
    assert html == (
        "<head><title>Hello</title>\n"
        '<link rel="canonical" href="http://testserver/articles/hello"></head>'
    )


def test_jsonld_tag_renders_only_the_schema() -> None:
    request = RequestFactory().get("/")
    get_seo(request).title("Hello").schema(Article(headline="Hi", author=Person(name="Jo")))
    html = render("{% load goatseo %}{% goatseo_jsonld %}", request)
    assert html == (
        '<script type="application/ld+json">{"@context":"https://schema.org",'
        '"@type":"Article","author":{"@type":"Person","name":"Jo"},"headline":"Hi"}</script>'
    )


def test_jsonld_tag_is_empty_without_schema() -> None:
    assert render("{% load goatseo %}{% goatseo_jsonld %}", RequestFactory().get("/")) == ""


def test_tags_require_the_request_in_the_context() -> None:
    with pytest.raises(TemplateSyntaxError):
        render("{% load goatseo %}{% goatseo_head %}")


@override_settings(ROOT_URLCONF=URLS)
def test_mixin_layers_view_over_model(client: Client) -> None:
    html = client.get("/pages/1").content.decode()
    assert "<title>View title</title>" in html
    assert '<meta name="description" content="Object description">' in html


@override_settings(ROOT_URLCONF=URLS)
def test_decorator_sets_the_view_layer(client: Client) -> None:
    html = client.get("/blog").content.decode()
    assert "<title>Post</title>" in html
    assert '<meta name="description" content="All posts">' in html


@override_settings(ROOT_URLCONF=URLS)
def test_middleware_adds_robots_header(client: Client) -> None:
    assert client.get("/noindex").headers["X-Robots-Tag"] == "noindex, follow"


@override_settings(ROOT_URLCONF=URLS)
def test_middleware_keeps_an_existing_header(client: Client) -> None:
    assert client.get("/explicit").headers["X-Robots-Tag"] == "none"


@override_settings(ROOT_URLCONF=URLS)
def test_middleware_skips_pages_without_directives(client: Client) -> None:
    assert "X-Robots-Tag" not in client.get("/plain").headers


@override_settings(ROOT_URLCONF=URLS)
def test_untrusted_values_are_escaped(client: Client) -> None:
    html = client.get("/xss").content.decode()
    assert "<script>" not in html
    assert "<title>&lt;/title&gt;&lt;script&gt;alert(1)&lt;/script&gt;</title>" in html
    assert 'content="&quot; onload=&quot;alert(1)"' in html
