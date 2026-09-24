from goatseo_schema_generator.ir import Layer, Ontology, TypeKind


def test_classes_and_inheritance(ontology: Ontology) -> None:
    assert ontology.version == "1.0"
    assert ontology.types["Article"].parent_types == ("CreativeWork",)
    assert ontology.types["LocalBusiness"].parent_types == ("Organization", "Place")
    assert set(ontology.ancestors("Article")) == {"CreativeWork", "Thing"}
    assert "Article" in set(ontology.descendants("Thing"))
    assert ontology.types["Thing"].description == "The most generic type of item."


def test_properties_domains_and_ranges(ontology: Ontology) -> None:
    author = ontology.properties["author"]
    assert author.domains == ("CreativeWork",)
    assert author.ranges == ("Organization", "Person")
    assert [p.name for p in ontology.types["CreativeWork"].properties] == [
        "about",
        "author",
        "datePublished",
        "yield",
    ]


def test_datatypes_include_subclasses(ontology: Ontology) -> None:
    datatypes = {t.name for t in ontology.of_kind(TypeKind.DATATYPE)}
    assert datatypes == {"Boolean", "Date", "Integer", "Number", "Text", "URL"}
    assert "DataType" not in ontology.types


def test_enumerations_and_members(ontology: Ontology) -> None:
    availability = ontology.types["ItemAvailability"]
    assert availability.kind is TypeKind.ENUMERATION
    assert [m.name for m in availability.members] == ["InStock", "OutOfStock"]
    assert ontology.types["QualitativeValue"].kind is TypeKind.ENUMERATION
    assert ontology.types["QualitativeValue"].members == ()


def test_deprecations(ontology: Ontology) -> None:
    assert ontology.types["OldType"].superseded_by == ("Article",)
    assert ontology.types["OldType"].deprecated
    assert ontology.properties["oldName"].deprecated
    assert not ontology.properties["name"].deprecated


def test_pending_layer_is_excluded_by_default(ontology: Ontology) -> None:
    assert "PendingWork" not in ontology.types
    assert "pendingProp" not in ontology.properties
    assert "draftOf" not in ontology.properties
    assert "onlyPending" not in ontology.properties


def test_excluded_parent_is_replaced_by_nearest_included_ancestor(ontology: Ontology) -> None:
    assert ontology.types["Draft"].parent_types == ("CreativeWork",)


def test_pending_layer_can_be_included(ontology_with_pending: Ontology) -> None:
    assert ontology_with_pending.types["PendingWork"].layer is Layer.PENDING
    assert ontology_with_pending.types["Draft"].parent_types == ("PendingWork",)
    assert ontology_with_pending.properties["onlyPending"].ranges == ("PendingWork",)


def test_non_schema_org_subjects_are_ignored(ontology: Ontology) -> None:
    assert "Ignored" not in ontology.types
    assert all(not name.startswith("http") for name in ontology.types)
