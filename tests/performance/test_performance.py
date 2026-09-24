import subprocess
import sys
import time

import pytest

from goatseo import SEO, Metadata, StaticRequestContext
from goatseo.opengraph import ArticleMetadata, OpenGraph, OpenGraphImage
from goatseo.schema import Article, Organization, Person
from goatseo.twitter import TwitterCard, TwitterCardType

pytestmark = pytest.mark.performance

FACADE_IMPORT_BUDGET = 1.5
SCHEMA_IMPORT_BUDGET = 5.0
RENDER_BUDGET = 2.0
RENDER_ITERATIONS = 1000


def _timed_subprocess(code: str) -> tuple[float, str]:
    script = f"import time\nstart = time.perf_counter()\n{code}\nprint(time.perf_counter() - start)"
    completed = subprocess.run(  # noqa: S603
        [sys.executable, "-c", script], capture_output=True, text=True, check=True
    )
    *output, elapsed = completed.stdout.split()
    return float(elapsed), " ".join(output)


def test_facade_import_is_light() -> None:
    elapsed, output = _timed_subprocess(
        "import sys, goatseo\nprint('goatseo.schema._types' in sys.modules)"
    )
    assert output == "False"
    assert elapsed < FACADE_IMPORT_BUDGET


def test_schema_types_import_budget() -> None:
    elapsed, _ = _timed_subprocess("from goatseo.schema import Article")
    assert elapsed < SCHEMA_IMPORT_BUDGET


def test_render_budget() -> None:
    seo = SEO(
        title="Hello World",
        description="An interesting article about goats and search engines.",
        canonical="/articles/hello",
        defaults=Metadata(site_name="Example", title_template="{title} | Example"),
    )
    seo.open_graph(
        OpenGraph(
            type="article",
            images=[OpenGraphImage(url="/hello.jpg", width=1200, height=630, alt="Goat")],
            article=ArticleMetadata(section="Animals", tags=["goat", "seo"]),
        )
    )
    seo.twitter(TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE, site="@goatseo"))
    seo.schema(
        Article(
            headline="Hello World",
            author=Person(name="John Doe"),
            publisher=Organization(name="Example"),
        )
    )
    context = StaticRequestContext("https://example.com/articles/hello")
    seo.render(context)
    start = time.perf_counter()
    for _ in range(RENDER_ITERATIONS):
        seo.render(context)
    assert time.perf_counter() - start < RENDER_BUDGET
