"""Maps the Schema.org IR onto Python-level declarations."""

import keyword
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from typing import Final

from goatseo_schema_generator.ir import Ontology, SchemaProperty, SchemaType, TypeKind

DATATYPES: Final[Mapping[str, tuple[str, ...]]] = {
    "Boolean": ("bool",),
    "Integer": ("int",),
    "Float": ("float",),
    "Number": ("int", "float"),
    "Date": ("_dt.date",),
    "DateTime": ("_dt.datetime",),
    "Time": ("_dt.time",),
    "Text": ("str",),
    "URL": ("str",),
    "PronounceableText": ("str",),
    "CssSelectorType": ("str",),
    "XPathType": ("str",),
    "Quantity": ("str",),
    "Distance": ("str",),
    "Duration": ("str",),
    "Energy": ("str",),
    "Mass": ("str",),
}
_DATATYPE_ORDER: Final = ("str", "bool", "int", "float", "_dt.date", "_dt.datetime", "_dt.time")

CLASS_ALIASES: Final[Mapping[str, str]] = {"3DModel": "Model3D"}
ENUMERATION_BASE: Final = "SchemaEnumeration"
MODEL_BASE: Final = "SchemaModel"
# Beyond this many enumerations, a range accepts any enumeration instead of an unreadable union.
MAX_ENUMERATION_UNION: Final = 6

RESERVED_FIELD_NAMES: Final = frozenset(
    {
        "id",
        "jsonld_type",
        "prop",
        "model_config",
        "model_fields",
        "copy",
        "dict",
        "json",
        "schema",
        "construct",
        "validate",
        "fields",
        "parse_obj",
        "parse_raw",
        "update_forward_refs",
    }
)


class MappingError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class PyField:
    name: str
    schema_name: str
    types: tuple[str, ...]
    superseded_by: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PyModel:
    name: str
    schema_name: str
    bases: tuple[str, ...]
    fields: tuple[PyField, ...]
    description: str | None
    superseded_by: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PyEnumMember:
    name: str
    schema_name: str
    superseded_by: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PyEnum:
    name: str
    schema_name: str
    members: tuple[PyEnumMember, ...]
    description: str | None
    superseded_by: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class PyModule:
    version: str
    models: tuple[PyModel, ...]
    enums: tuple[PyEnum, ...]


_CAMEL_BOUNDARY: Final = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_IDENTIFIER: Final = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def snake_case(name: str) -> str:
    return _CAMEL_BOUNDARY.sub("_", name).lower()


def field_name(schema_name: str) -> str:
    name = snake_case(schema_name)
    if keyword.iskeyword(name) or name in RESERVED_FIELD_NAMES:
        name += "_"
    if not _IDENTIFIER.match(name):
        raise MappingError(f"property {schema_name!r} has no valid Python name")
    return name


def class_name(schema_name: str) -> str:
    name = CLASS_ALIASES.get(schema_name, schema_name)
    if not _IDENTIFIER.match(name) or keyword.iskeyword(name):
        raise MappingError(f"type {schema_name!r} needs an entry in CLASS_ALIASES")
    return name


def member_name(schema_name: str) -> str:
    if not _IDENTIFIER.match(schema_name) or keyword.iskeyword(schema_name):
        return f"V{schema_name}"
    return schema_name


class TypeMapper:
    def __init__(self, ontology: Ontology) -> None:
        self._ontology = ontology

    def is_model(self, schema_type: SchemaType) -> bool:
        return schema_type.kind is TypeKind.CLASS or (
            schema_type.kind is TypeKind.ENUMERATION and not schema_type.members
        )

    def is_enum(self, schema_type: SchemaType) -> bool:
        return schema_type.kind is TypeKind.ENUMERATION and bool(schema_type.members)

    def range_types(self, range_name: str) -> tuple[str, ...]:
        if range_name in DATATYPES:
            return DATATYPES[range_name]
        schema_type = self._ontology.types[range_name]
        if schema_type.kind is TypeKind.DATATYPE:
            raise MappingError(f"datatype {range_name!r} has no Python mapping")
        types = [class_name(range_name)] if self.is_model(schema_type) else []
        enums = sorted(
            class_name(name)
            for name in (range_name, *self._ontology.descendants(range_name))
            if self.is_enum(self._ontology.types[name])
        )
        types.extend([ENUMERATION_BASE] if len(enums) > MAX_ENUMERATION_UNION else enums)
        return tuple(types)

    def property_types(self, prop: SchemaProperty) -> tuple[str, ...]:
        found = {t for r in prop.ranges for t in self.range_types(r)}
        primitives = [t for t in _DATATYPE_ORDER if t in found]
        return (*primitives, *sorted(found - set(primitives)))

    def bases(self, schema_type: SchemaType) -> tuple[str, ...]:
        parents = [p for p in schema_type.parent_types if self.is_model(self._ontology.types[p])]
        redundant = {a for p in parents for a in self._ontology.ancestors(p)}
        kept = tuple(class_name(p) for p in parents if p not in redundant)
        return kept or (MODEL_BASE,)


def _model_fields(
    schema_type: SchemaType, mapper: TypeMapper, inherited: set[str]
) -> tuple[PyField, ...]:
    fields: list[PyField] = []
    seen: set[str] = set()
    for prop in sorted(schema_type.properties, key=lambda p: p.name):
        if prop.name in inherited:
            continue
        name = field_name(prop.name)
        if name in seen:
            raise MappingError(f"{schema_type.name}: two properties map to {name!r}")
        seen.add(name)
        fields.append(PyField(name, prop.name, mapper.property_types(prop), prop.superseded_by))
    return tuple(fields)


def _topological(ontology: Ontology, names: Iterable[str]) -> list[str]:
    pending = set(names)
    ordered: list[str] = []
    while pending:
        ready = sorted(
            n for n in pending if not any(p in pending for p in ontology.types[n].parent_types)
        )
        if not ready:
            raise MappingError(f"inheritance cycle among {sorted(pending)}")
        ordered.extend(ready)
        pending.difference_update(ready)
    return ordered


def _check_linearization(models: Iterable[PyModel]) -> None:
    classes: dict[str, type] = {MODEL_BASE: type(MODEL_BASE, (), {})}
    for model in models:
        try:
            classes[model.name] = type(model.name, tuple(classes[b] for b in model.bases), {})
        except TypeError as error:
            raise MappingError(f"{model.name}: no consistent method resolution order") from error


def map_ontology(ontology: Ontology) -> PyModule:
    mapper = TypeMapper(ontology)
    model_names = [n for n, t in ontology.types.items() if mapper.is_model(t)]
    declared: dict[str, set[str]] = {}
    models: list[PyModel] = []
    for name in _topological(ontology, model_names):
        schema_type = ontology.types[name]
        inherited = {
            prop
            for ancestor in ontology.ancestors(name)
            if ancestor in declared
            for prop in declared[ancestor]
        }
        fields = _model_fields(schema_type, mapper, inherited)
        declared[name] = {f.schema_name for f in fields} | inherited
        models.append(
            PyModel(
                name=class_name(name),
                schema_name=name,
                bases=mapper.bases(schema_type),
                fields=fields,
                description=schema_type.description,
                superseded_by=schema_type.superseded_by,
            )
        )
    _check_linearization(models)
    enums = tuple(
        PyEnum(
            name=class_name(t.name),
            schema_name=t.name,
            members=tuple(
                PyEnumMember(member_name(m.name), m.name, m.superseded_by) for m in t.members
            ),
            description=t.description,
            superseded_by=t.superseded_by,
        )
        for t in ontology.of_kind(TypeKind.ENUMERATION)
        if mapper.is_enum(t)
    )
    return PyModule(ontology.version, tuple(models), enums)
