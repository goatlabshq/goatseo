import datetime as dt

from goatseo.core import JsonLd, render_elements
from goatseo.schema import (
    CONTEXT,
    Article,
    ItemAvailability,
    Model3D,
    Offer,
    Organization,
    Person,
    Product,
    WebSite,
    jsonld_element,
    to_graph,
    to_jsonld,
)


def test_article() -> None:
    article = Article(headline="Hello World", author=Person(name="John Doe"))
    assert to_jsonld(article) == {
        "@context": "https://schema.org",
        "@type": "Article",
        "author": {"@type": "Person", "name": "John Doe"},
        "headline": "Hello World",
    }


def test_property_names_are_camel_case() -> None:
    article = Article(
        date_published=dt.date(2026, 1, 2),
        date_modified=dt.datetime(2026, 1, 3, 4, 5, tzinfo=dt.UTC),
        main_entity_of_page="https://e.com/a",
        is_accessible_for_free=True,
    )
    assert to_jsonld(article, context=None) == {
        "@type": "Article",
        "mainEntityOfPage": "https://e.com/a",
        "dateModified": "2026-01-03T04:05:00+00:00",
        "datePublished": "2026-01-02",
        "isAccessibleForFree": True,
    }


def test_id_enumerations_and_lists() -> None:
    product = Product(
        id="https://e.com/p#product",
        name="Goat",
        offers=[Offer(price=9.5, availability=ItemAvailability.InStock)],
    )
    assert to_jsonld(product) == {
        "@context": CONTEXT,
        "@type": "Product",
        "@id": "https://e.com/p#product",
        "name": "Goat",
        "offers": [{"@type": "Offer", "availability": "https://schema.org/InStock", "price": 9.5}],
    }


def test_empty_lists_and_aliases() -> None:
    assert to_jsonld(Model3D(name="Scan", keywords=[]), context=None) == {
        "@type": "3DModel",
        "name": "Scan",
    }


def test_graph() -> None:
    organization = Organization(id="https://e.com/#org", name="Example")
    site = WebSite(id="https://e.com/#site", publisher=Organization(id="https://e.com/#org"))
    assert to_graph([organization, site]) == {
        "@context": CONTEXT,
        "@graph": [
            {"@type": "Organization", "@id": "https://e.com/#org", "name": "Example"},
            {
                "@type": "WebSite",
                "@id": "https://e.com/#site",
                "publisher": {"@type": "Organization", "@id": "https://e.com/#org"},
            },
        ],
    }


def test_jsonld_element() -> None:
    person = Person(name="A")
    assert jsonld_element([]) is None
    assert jsonld_element([person]) == JsonLd(to_jsonld(person))
    element = jsonld_element([person, Person(name="B")])
    assert element is not None
    assert isinstance(element.data, dict)
    assert "@graph" in element.data


def test_script_injection_is_neutralized() -> None:
    payload = "</script><script>alert(1)</script><!-- \"' &"
    element = jsonld_element([Article(headline=payload)])
    assert element is not None
    html = render_elements([element])
    assert html.count("</script>") == 1
    assert "<script>alert" not in html
    assert "<!--" not in html
    assert "\\u003c/script\\u003e" in html
