import datetime as dt
from typing import Annotated

import pytest
from pydantic import ValidationError

from goatseo.schema import (
    SCHEMA_ORG_VERSION,
    Answer,
    Article,
    BreadcrumbList,
    CreativeWork,
    EntryPoint,
    Event,
    FAQPage,
    ItemAvailability,
    ItemList,
    ListItem,
    LocalBusiness,
    Model3D,
    NewsArticle,
    Offer,
    Organization,
    Patient,
    Person,
    Place,
    Product,
    Question,
    Recipe,
    SchemaEnumeration,
    SchemaModel,
    SearchAction,
    Thing,
    WebSite,
)
from goatseo.schema.base import prop


class Measure(SchemaModel):
    ratio: Annotated[float | list[float] | None, prop("ratio")] = None
    count: Annotated[int | list[int] | None, prop("count")] = None


def test_version() -> None:
    assert SCHEMA_ORG_VERSION == "30.1"


def test_nested_models_keep_their_static_types() -> None:
    article = Article(headline="Hello", author=Person(name="John Doe"))
    assert isinstance(article.author, Person)
    assert article.author.name == "John Doe"
    assert article.headline == "Hello"


def test_inheritance() -> None:
    assert issubclass(Article, CreativeWork)
    assert issubclass(LocalBusiness, Organization)
    assert issubclass(LocalBusiness, Place)
    assert issubclass(Patient, Person)
    assert Model3D.jsonld_type == "3DModel"


def test_multiple_inheritance_merges_fields() -> None:
    shop = LocalBusiness(name="Shop", legal_name="Shop Inc", opening_hours="Mo-Fr 09:00-17:00")
    assert shop.legal_name == "Shop Inc"
    assert shop.opening_hours == "Mo-Fr 09:00-17:00"


def test_subclass_instances_are_accepted_for_parent_types() -> None:
    article = Article(is_part_of=NewsArticle(headline="Parent"), author=Patient(name="Jane"))
    assert isinstance(article.is_part_of, NewsArticle)
    assert isinstance(article.author, Patient)


def test_lists_of_values() -> None:
    article = Article(author=[Person(name="A"), Organization(name="B")], keywords=["a", "b"])
    assert isinstance(article.author, list)
    assert len(article.author) == 2


def test_tuples_are_normalized_to_lists() -> None:
    assert Article.model_validate({"keywords": ("a", "b")}).keywords == ["a", "b"]


def test_wrong_types_are_rejected() -> None:
    with pytest.raises(ValidationError, match="headline expects str"):
        Article.model_validate({"headline": 123})
    with pytest.raises(ValidationError, match=r"author expects Organization \| Person"):
        Article.model_validate({"author": "John Doe"})
    with pytest.raises(ValidationError):
        Article.model_validate({"author": [Person(name="A"), 3]})


def test_bool_is_not_a_number() -> None:
    with pytest.raises(ValidationError):
        ItemList.model_validate({"number_of_items": True})
    with pytest.raises(ValidationError):
        Measure.model_validate({"count": False})
    assert ItemList(number_of_items=3).number_of_items == 3


def test_int_is_accepted_for_float() -> None:
    assert Measure(ratio=2).ratio == 2
    with pytest.raises(ValidationError):
        Measure.model_validate({"ratio": True})


def test_dates_and_datetimes() -> None:
    event = Event(name="Launch", start_date=dt.datetime(2026, 1, 2, 10, 30, tzinfo=dt.UTC))
    assert isinstance(event.start_date, dt.datetime)
    assert Person(birth_date=dt.date(1990, 5, 1)).birth_date == dt.date(1990, 5, 1)
    with pytest.raises(ValidationError):
        Person.model_validate({"birth_date": "1990-05-01"})


def test_validate_assignment() -> None:
    person = Person(name="A")
    person.name = "B"
    assert person.name == "B"
    with pytest.raises(ValidationError):
        person.name = 3  # pyright: ignore[reportAttributeAccessIssue]


def test_extra_fields_are_forbidden() -> None:
    with pytest.raises(ValidationError):
        Person.model_validate({"nickname": "x"})
    with pytest.raises(ValidationError):
        Person.model_validate({"givenName": "x"})


def test_empty_id_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Person(id="")


def test_deprecated_property_warns() -> None:
    with pytest.warns(DeprecationWarning, match="superseded by award"):
        CreativeWork(awards="Prize")


def test_enumerations() -> None:
    assert issubclass(ItemAvailability, SchemaEnumeration)
    assert ItemAvailability.InStock == "https://schema.org/InStock"
    offer = Offer(price=10, price_currency="EUR", availability=ItemAvailability.InStock)
    assert offer.availability is ItemAvailability.InStock
    with pytest.raises(ValidationError):
        Offer.model_validate({"availability": "https://schema.org/InStock"})


def test_common_structured_data_types() -> None:
    faq = FAQPage(
        main_entity=[Question(name="Why?", accepted_answer=Answer(text="Because."))],
    )
    crumbs = BreadcrumbList(
        item_list_element=[ListItem(position=1, name="Home", item=Thing(id="https://e.com/"))]
    )
    site = WebSite(
        url="https://e.com",
        potential_action=SearchAction(
            target=EntryPoint(url_template="https://e.com/search?q={q}"), query="q"
        ),
    )
    recipe = Recipe(name="Soup", cook_time="PT30M", recipe_ingredient=["water", "salt"])
    product = Product(name="Goat", offers=Offer(price=9.99, availability=ItemAvailability.InStock))
    model = Model3D(name="Scan", content_url="https://e.com/scan.glb")
    for node in (faq, crumbs, site, recipe, product, model):
        assert isinstance(node, Thing)
