import pytest

from goatseo_schema_generator.ir import (
    EnumerationMember,
    Ontology,
    SchemaProperty,
    SchemaType,
    TypeKind,
)
from goatseo_schema_generator.mapper import (
    ENUMERATION_BASE,
    MAX_ENUMERATION_UNION,
    MappingError,
    PyModel,
    TypeMapper,
    class_name,
    field_name,
    map_ontology,
    member_name,
    snake_case,
)


def _model(ontology: Ontology, name: str) -> PyModel:
    return next(m for m in map_ontology(ontology).models if m.name == name)


def _class(name: str, *parents: str, properties: tuple[SchemaProperty, ...] = ()) -> SchemaType:
    return SchemaType(name, parents, properties, None)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("name", "name"),
        ("datePublished", "date_published"),
        ("productID", "product_id"),
        ("isicV4", "isic_v4"),
        ("gtin13", "gtin13"),
        ("mainEntityOfPage", "main_entity_of_page"),
    ],
)
def test_snake_case(name: str, expected: str) -> None:
    assert snake_case(name) == expected


@pytest.mark.parametrize(
    ("name", "expected"),
    [("yield", "yield_"), ("id", "id_"), ("schema", "schema_"), ("jsonldType", "jsonld_type_")],
)
def test_keywords_and_reserved_names_get_a_suffix(name: str, expected: str) -> None:
    assert field_name(name) == expected


def test_invalid_property_name() -> None:
    with pytest.raises(MappingError):
        field_name("bad-name")


def test_class_aliases() -> None:
    assert class_name("3DModel") == "Model3D"
    assert class_name("Article") == "Article"
    with pytest.raises(MappingError, match="CLASS_ALIASES"):
        class_name("4DModel")


def test_member_name() -> None:
    assert member_name("InStock") == "InStock"
    assert member_name("3Stars") == "V3Stars"


def test_range_mapping(ontology: Ontology) -> None:
    mapper = TypeMapper(ontology)
    assert mapper.range_types("Text") == ("str",)
    assert mapper.range_types("URL") == ("str",)
    assert mapper.range_types("Number") == ("int", "float")
    assert mapper.range_types("Date") == ("_dt.date",)
    assert mapper.range_types("Person") == ("Person",)
    assert mapper.range_types("ItemAvailability") == ("ItemAvailability",)
    assert mapper.range_types("Enumeration") == ("Enumeration", "ItemAvailability")
    assert mapper.property_types(ontology.properties["value"]) == ("str", "bool", "int", "float")


def test_models_and_enums(ontology: Ontology) -> None:
    module = map_ontology(ontology)
    names = [m.name for m in module.models]
    assert "ItemAvailability" not in names
    assert "QualitativeValue" in names
    assert [e.name for e in module.enums] == ["ItemAvailability"]
    assert [m.name for m in module.enums[0].members] == ["InStock", "OutOfStock"]


def test_topological_order(ontology: Ontology) -> None:
    names = [m.name for m in map_ontology(ontology).models]
    assert names.index("Thing") < names.index("CreativeWork") < names.index("Article")
    assert names.index("Place") < names.index("LocalBusiness")


def test_fields_and_bases(ontology: Ontology) -> None:
    thing = _model(ontology, "Thing")
    assert thing.bases == ("SchemaModel",)
    fields = {f.name: f for f in thing.fields}
    assert fields["product_id"].schema_name == "productID"
    assert fields["old_name"].superseded_by == ("name",)
    creative_work = {f.name: f.types for f in _model(ontology, "CreativeWork").fields}
    assert creative_work["author"] == ("Organization", "Person")
    assert creative_work["yield_"] == ("int", "float")
    assert _model(ontology, "LocalBusiness").bases == ("Organization", "Place")


def test_inherited_properties_are_not_redeclared(ontology: Ontology) -> None:
    assert "about" in [f.name for f in _model(ontology, "CreativeWork").fields]
    assert "about" not in [f.name for f in _model(ontology, "Article").fields]


def test_redundant_bases_are_removed() -> None:
    ontology = Ontology(
        "1",
        {
            "Thing": _class("Thing"),
            "A": _class("A", "Thing"),
            "B": _class("B", "A", "Thing"),
        },
    )
    assert _model(ontology, "B").bases == ("A",)


def test_inconsistent_mro_is_reported() -> None:
    ontology = Ontology(
        "1",
        {
            "Thing": _class("Thing"),
            "X": _class("X", "Thing"),
            "Y": _class("Y", "Thing"),
            "P": _class("P", "X", "Y"),
            "Q": _class("Q", "Y", "X"),
            "R": _class("R", "P", "Q"),
        },
    )
    with pytest.raises(MappingError, match="method resolution order"):
        map_ontology(ontology)


def test_field_name_collision_is_reported() -> None:
    props = (
        SchemaProperty("fooBar", ("Thing",), ("Text",), None),
        SchemaProperty("foo_bar", ("Thing",), ("Text",), None),
    )
    ontology = Ontology(
        "1",
        {
            "Thing": _class("Thing", properties=props),
            "Text": SchemaType("Text", (), (), None, kind=TypeKind.DATATYPE),
        },
    )
    with pytest.raises(MappingError, match="two properties"):
        map_ontology(ontology)


def test_large_enumeration_unions_collapse_to_the_base() -> None:
    enums = {
        f"E{i}": SchemaType(
            f"E{i}",
            ("Enumeration",),
            (),
            None,
            kind=TypeKind.ENUMERATION,
            members=(EnumerationMember(f"M{i}", (f"E{i}",), None),),
        )
        for i in range(MAX_ENUMERATION_UNION + 1)
    }
    ontology = Ontology(
        "1",
        {
            "Thing": _class("Thing"),
            "Enumeration": SchemaType("Enumeration", ("Thing",), (), None, TypeKind.ENUMERATION),
            **enums,
        },
    )
    assert TypeMapper(ontology).range_types("Enumeration") == ("Enumeration", ENUMERATION_BASE)
    assert TypeMapper(ontology).range_types("E0") == ("E0",)


def test_unmapped_datatype_is_reported() -> None:
    ontology = Ontology("1", {"Money": SchemaType("Money", (), (), None, kind=TypeKind.DATATYPE)})
    with pytest.raises(MappingError, match="no Python mapping"):
        TypeMapper(ontology).range_types("Money")
