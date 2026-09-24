"""Checks that the built wheels install and work outside the repository."""

from importlib.resources import files

from goatseo import SEO, StaticRequestContext
from goatseo.schema import Article, Person

PACKAGES = ("core", "schema", "opengraph", "twitter", "seo", "django", "fastapi", "flask")

seo = SEO(title="Hello World", description="An interesting article", canonical="/hello")
seo.schema(Article(headline="Hello World", author=Person(name="John Doe")))
html = seo.render(StaticRequestContext("https://example.com/"))

assert '<link rel="canonical" href="https://example.com/hello">' in html, html
assert '"@type":"Article"' in html, html
assert files("goatseo").joinpath("py.typed").is_file()
for package in PACKAGES:
    assert files(f"goatseo.{package}").joinpath("py.typed").is_file(), package
