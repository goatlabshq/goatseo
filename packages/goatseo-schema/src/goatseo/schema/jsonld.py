"""JSON-LD serialization of Schema.org models."""

import datetime as _dt
from collections.abc import Iterable, Sequence
from enum import Enum
from typing import Final

from goatseo.core import JsonLd, JsonObject, JsonValue
from goatseo.schema.base import SchemaModel, is_multiple, prop

CONTEXT: Final = "https://schema.org"


def _property_name(model: type[SchemaModel], field: str) -> str:
    for marker in model.model_fields[field].metadata:
        if isinstance(marker, prop):
            return marker.name
    return field


def _value(value: object) -> JsonValue:
    match value:
        case SchemaModel():
            return _node(value)
        case Enum():
            return str(value.value)
        case str() | bool() | int() | float():
            return value
        case _dt.datetime() | _dt.date() | _dt.time():
            return value.isoformat()
        case _ if is_multiple(value):
            return [_value(item) for item in value]
        case _:
            raise TypeError(f"cannot serialize {type(value).__name__} to JSON-LD")


def _node(model: SchemaModel) -> JsonObject:
    node: JsonObject = {"@type": model.jsonld_type}
    if model.id is not None:
        node["@id"] = model.id
    cls = type(model)
    # __dict__ keeps declaration order and skips pydantic's attribute machinery.
    for field, value in model.__dict__.items():
        if field == "id" or value is None or value == []:
            continue
        node[_property_name(cls, field)] = _value(value)
    return node


def to_jsonld(model: SchemaModel, *, context: str | None = CONTEXT) -> JsonObject:
    node = _node(model)
    return node if context is None else {"@context": context, **node}


def to_graph(models: Sequence[SchemaModel], *, context: str = CONTEXT) -> JsonObject:
    """Several top-level nodes in one document, linked through their ``@id``."""
    return {"@context": context, "@graph": [_node(model) for model in models]}


def jsonld_element(models: Iterable[SchemaModel]) -> JsonLd | None:
    nodes = list(models)
    if not nodes:
        return None
    return JsonLd(to_jsonld(nodes[0]) if len(nodes) == 1 else to_graph(nodes))
