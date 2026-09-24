"""Internal representation of the Schema.org vocabulary, independent of RDF and Python."""

from collections.abc import Iterator, Mapping
from dataclasses import dataclass, field
from enum import StrEnum
from functools import cached_property


class Layer(StrEnum):
    CORE = "core"
    PENDING = "pending"
    HEALTH_LIFESCI = "health-lifesci"
    BIB = "bib"
    AUTO = "auto"
    META = "meta"
    ATTIC = "attic"


class TypeKind(StrEnum):
    CLASS = "class"
    ENUMERATION = "enumeration"
    DATATYPE = "datatype"


@dataclass(frozen=True, slots=True)
class SchemaProperty:
    name: str
    domains: tuple[str, ...]
    ranges: tuple[str, ...]
    description: str | None
    layer: Layer = Layer.CORE
    superseded_by: tuple[str, ...] = ()
    inverse_of: str | None = None

    @property
    def deprecated(self) -> bool:
        return bool(self.superseded_by)


@dataclass(frozen=True, slots=True)
class EnumerationMember:
    name: str
    enumerations: tuple[str, ...]
    description: str | None
    layer: Layer = Layer.CORE
    superseded_by: tuple[str, ...] = ()

    @property
    def deprecated(self) -> bool:
        return bool(self.superseded_by)


@dataclass(frozen=True, slots=True)
class SchemaType:
    name: str
    parent_types: tuple[str, ...]
    properties: tuple[SchemaProperty, ...]
    description: str | None
    kind: TypeKind = TypeKind.CLASS
    layer: Layer = Layer.CORE
    superseded_by: tuple[str, ...] = ()
    members: tuple[EnumerationMember, ...] = ()

    @property
    def deprecated(self) -> bool:
        return bool(self.superseded_by)


@dataclass(frozen=True)
class Ontology:
    """A closed vocabulary: every parent, domain and range refers to a type it contains."""

    version: str
    types: Mapping[str, SchemaType]
    properties: Mapping[str, SchemaProperty] = field(default_factory=dict[str, SchemaProperty])

    def ancestors(self, name: str) -> Iterator[str]:
        seen: set[str] = set()
        stack = list(self.types[name].parent_types)
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            yield current
            stack.extend(self.types[current].parent_types)

    @cached_property
    def children(self) -> Mapping[str, tuple[str, ...]]:
        children: dict[str, list[str]] = {name: [] for name in self.types}
        for schema_type in self.types.values():
            for parent in schema_type.parent_types:
                children[parent].append(schema_type.name)
        return {name: tuple(sorted(names)) for name, names in children.items()}

    def descendants(self, name: str) -> Iterator[str]:
        seen: set[str] = set()
        stack = list(self.children[name])
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            yield current
            stack.extend(self.children[current])

    def of_kind(self, kind: TypeKind) -> tuple[SchemaType, ...]:
        return tuple(t for _, t in sorted(self.types.items()) if t.kind is kind)
