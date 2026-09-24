"""Builds the internal representation from the Schema.org N-Triples release."""

from collections import defaultdict
from collections.abc import Callable, Collection, Iterable
from dataclasses import dataclass, field
from typing import Final

from goatseo_schema_generator.ir import (
    EnumerationMember,
    Layer,
    Ontology,
    SchemaProperty,
    SchemaType,
    TypeKind,
)
from goatseo_schema_generator.ntriples import Iri, Literal, Triple

SCHEMA: Final = "https://schema.org/"
_RDF_TYPE: Final = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
_RDF_PROPERTY: Final = "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"
_RDFS_CLASS: Final = "http://www.w3.org/2000/01/rdf-schema#Class"
_RDFS_COMMENT: Final = "http://www.w3.org/2000/01/rdf-schema#comment"
_RDFS_SUBCLASS_OF: Final = "http://www.w3.org/2000/01/rdf-schema#subClassOf"
_DOMAIN: Final = SCHEMA + "domainIncludes"
_RANGE: Final = SCHEMA + "rangeIncludes"
_SUPERSEDED_BY: Final = SCHEMA + "supersededBy"
_IS_PART_OF: Final = SCHEMA + "isPartOf"
_INVERSE_OF: Final = SCHEMA + "inverseOf"
_DATATYPE: Final = "DataType"
_ENUMERATION: Final = "Enumeration"

DEFAULT_LAYERS: Final = frozenset({Layer.CORE, Layer.HEALTH_LIFESCI, Layer.BIB, Layer.AUTO})

_LAYERS: Final = {f"https://{layer.value}.schema.org": layer for layer in Layer}


@dataclass
class _Node:
    rdf_types: set[str] = field(default_factory=set[str])
    parents: set[str] = field(default_factory=set[str])
    domains: set[str] = field(default_factory=set[str])
    ranges: set[str] = field(default_factory=set[str])
    superseded_by: set[str] = field(default_factory=set[str])
    inverse_of: str | None = None
    comment: str | None = None
    layer: Layer = Layer.CORE


def _local_name(iri: str) -> str | None:
    return iri.removeprefix(SCHEMA) if iri.startswith(SCHEMA) else None


def _collect(triples: Iterable[Triple]) -> dict[str, _Node]:
    nodes: defaultdict[str, _Node] = defaultdict(_Node)
    for triple in triples:
        subject = _local_name(triple.subject.value)
        if subject is None:
            continue
        node = nodes[subject]
        predicate = triple.predicate.value
        term = triple.object
        if isinstance(term, Literal):
            if predicate == _RDFS_COMMENT:
                node.comment = term.value
            continue
        _apply_reference(node, predicate, term)
    return dict(nodes)


def _apply_reference(node: _Node, predicate: str, term: Iri) -> None:
    target = _local_name(term.value)
    if predicate == _RDF_TYPE:
        node.rdf_types.add(target if target is not None else term.value)
    elif predicate == _IS_PART_OF and term.value in _LAYERS:
        node.layer = _LAYERS[term.value]
    elif target is None:
        return
    elif predicate == _RDFS_SUBCLASS_OF:
        node.parents.add(target)
    elif predicate == _DOMAIN:
        node.domains.add(target)
    elif predicate == _RANGE:
        node.ranges.add(target)
    elif predicate == _SUPERSEDED_BY:
        node.superseded_by.add(target)
    elif predicate == _INVERSE_OF:
        node.inverse_of = target


def _closure(roots: Collection[str], children_of: Callable[[str], Iterable[str]]) -> set[str]:
    found: set[str] = set()
    stack = list(roots)
    while stack:
        current = stack.pop()
        if current not in found:
            found.add(current)
            stack.extend(children_of(current))
    return found


class _Builder:
    def __init__(self, nodes: dict[str, _Node], layers: Collection[Layer]) -> None:
        self._nodes = nodes
        self._layers = layers
        self._classes = {name for name, node in nodes.items() if _RDFS_CLASS in node.rdf_types} - {
            _DATATYPE
        }
        self._children: defaultdict[str, set[str]] = defaultdict(set)
        for name in self._classes:
            for parent in nodes[name].parents:
                self._children[parent].add(name)
        datatype_roots = {n for n in self._classes if _DATATYPE in nodes[n].rdf_types}
        self._datatypes = _closure(datatype_roots, self._children.__getitem__)
        self._enumerations = _closure({_ENUMERATION}, self._children.__getitem__)
        self._included = {name for name in self._classes if nodes[name].layer in layers}

    def build(self, version: str) -> Ontology:
        properties = self._properties()
        members = self._members()
        types: dict[str, SchemaType] = {}
        for name in sorted(self._included):
            node = self._nodes[name]
            types[name] = SchemaType(
                name=name,
                parent_types=self._included_parents(name),
                properties=tuple(p for p in properties if name in p.domains),
                description=node.comment,
                kind=self._kind(name),
                layer=node.layer,
                superseded_by=self._keep_types(node.superseded_by),
                members=tuple(m for m in members if name in m.enumerations),
            )
        return Ontology(
            version=version,
            types=types,
            properties={p.name: p for p in properties},
        )

    def _kind(self, name: str) -> TypeKind:
        if name in self._datatypes:
            return TypeKind.DATATYPE
        if name in self._enumerations:
            return TypeKind.ENUMERATION
        return TypeKind.CLASS

    def _keep_types(self, names: Iterable[str]) -> tuple[str, ...]:
        return tuple(sorted(n for n in names if n in self._included))

    def _included_parents(self, name: str) -> tuple[str, ...]:
        """Excluded parents are replaced by their nearest included ancestors."""
        parents: set[str] = set()
        stack = list(self._nodes[name].parents & self._classes)
        while stack:
            parent = stack.pop()
            if parent in self._included:
                parents.add(parent)
            else:
                stack.extend(self._nodes[parent].parents & self._classes)
        return tuple(sorted(parents))

    def _properties(self) -> tuple[SchemaProperty, ...]:
        properties: list[SchemaProperty] = []
        for name in sorted(self._nodes):
            node = self._nodes[name]
            if _RDF_PROPERTY not in node.rdf_types or node.layer not in self._layers:
                continue
            domains = self._keep_types(node.domains)
            ranges = self._keep_types(node.ranges)
            if not domains or not ranges:
                continue
            properties.append(
                SchemaProperty(
                    name=name,
                    domains=domains,
                    ranges=ranges,
                    description=node.comment,
                    layer=node.layer,
                    superseded_by=tuple(sorted(node.superseded_by)),
                    inverse_of=node.inverse_of,
                )
            )
        return tuple(properties)

    def _members(self) -> tuple[EnumerationMember, ...]:
        members: list[EnumerationMember] = []
        for name in sorted(self._nodes):
            node = self._nodes[name]
            if name in self._classes or node.layer not in self._layers:
                continue
            enumerations = self._keep_types(node.rdf_types & self._enumerations)
            if enumerations:
                members.append(
                    EnumerationMember(
                        name=name,
                        enumerations=enumerations,
                        description=node.comment,
                        layer=node.layer,
                        superseded_by=tuple(sorted(node.superseded_by)),
                    )
                )
        return tuple(members)


def build_ontology(
    triples: Iterable[Triple], version: str, layers: Collection[Layer] = DEFAULT_LAYERS
) -> Ontology:
    return _Builder(_collect(triples), layers).build(version)
