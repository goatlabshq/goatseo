import pytest
from flask import Flask, render_template_string

from goatseo.core import Metadata
from goatseo.flask import SEOExtension, get_seo

HEAD = "<head>{{ goatseo_head() }}</head>"


def create_app(extension: SEOExtension) -> Flask:
    app = Flask(__name__)
    extension.init_app(app)

    @app.get("/articles/<slug>")
    def article(slug: str) -> str:
        get_seo().title(slug.title()).canonical(f"/articles/{slug}")
        return render_template_string(HEAD)

    @app.get("/identity")
    def identity() -> str:
        return str(get_seo() is get_seo())

    @app.get("/context")
    def context() -> str:
        get_seo().title("From context")
        return render_template_string("{{ seo.metadata.title }}")

    @app.get("/noindex")
    def noindex() -> str:
        get_seo().robots(index=False)
        return "ok"

    @app.get("/xss")
    def xss() -> str:
        get_seo().title("</title><script>alert(1)</script>")
        return render_template_string(HEAD)

    return app


def test_head_global_renders_defaults_and_resolved_canonical() -> None:
    extension = SEOExtension(defaults=Metadata(title_template="{title} | Example"))
    response = create_app(extension).test_client().get("/articles/hello?page=2")
    assert response.text == (
        "<head><title>Hello | Example</title>\n"
        '<link rel="canonical" href="http://localhost/articles/hello"></head>'
    )


def test_constructor_registers_the_extension() -> None:
    app = Flask(__name__)
    extension = SEOExtension(app)
    assert app.extensions["goatseo"] is extension


def test_seo_is_scoped_to_the_request() -> None:
    app = create_app(SEOExtension())
    assert app.test_client().get("/identity").text == "True"
    with app.test_request_context("/"):
        first = get_seo()
    with app.test_request_context("/"):
        assert get_seo() is not first


def test_seo_is_exposed_to_templates() -> None:
    assert create_app(SEOExtension()).test_client().get("/context").text == "From context"


def test_robots_header_is_opt_in() -> None:
    assert "X-Robots-Tag" not in create_app(SEOExtension()).test_client().get("/noindex").headers
    response = create_app(SEOExtension(robots_header=True)).test_client().get("/noindex")
    assert response.headers["X-Robots-Tag"] == "noindex"


def test_missing_extension_is_reported() -> None:
    with Flask(__name__).test_request_context("/"), pytest.raises(RuntimeError):
        get_seo()


def test_autoescape_keeps_markup_and_escapes_payloads() -> None:
    html = create_app(SEOExtension()).test_client().get("/xss").text
    assert html.startswith("<head><title>")
    assert "<script>" not in html
    assert "&lt;/title&gt;&lt;script&gt;alert(1)&lt;/script&gt;" in html
