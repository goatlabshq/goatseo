"""Runtime foundation shared by the generated Schema.org models."""

import types
import warnings
from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from typing import Annotated, ClassVar, TypeIs, Union, get_args, get_origin

from pydantic import BaseModel, ConfigDict, Field, GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class SchemaEnumeration(StrEnum):
    """Base of every generated enumeration; members serialize to their Schema.org IRI."""


class SchemaModel(BaseModel):
    """Base of every generated Schema.org type."""

    model_config = ConfigDict(extra="forbid", validate_assignment=True, defer_build=True)

    jsonld_type: ClassVar[str] = "Thing"

    id: Annotated[str, Field(min_length=1)] | None = None
    """JSON-LD node identifier, serialized as ``@id``."""


def _leaf_types(annotation: object) -> tuple[type, ...]:
    origin = get_origin(annotation)
    if origin is Union or isinstance(annotation, types.UnionType) or origin is list:
        return tuple(leaf for arg in get_args(annotation) for leaf in _leaf_types(arg))
    if isinstance(annotation, type) and annotation is not types.NoneType:
        return (annotation,)
    return ()


def is_multiple(value: object) -> TypeIs[list[object] | tuple[object, ...]]:
    return isinstance(value, list | tuple)


def _accepts(allowed: tuple[type, ...], value: object) -> bool:
    if isinstance(value, bool):
        return bool in allowed
    if isinstance(value, int) and float in allowed:
        return True
    return isinstance(value, allowed)


@dataclass(frozen=True, slots=True)
class prop:  # noqa: N801  (lowercase keeps the generated annotations readable)
    """Marks a field with its Schema.org property and validates values by ``isinstance``, so
    pydantic never builds a schema for the whole, deeply recursive Schema.org graph."""

    name: str
    superseded_by: tuple[str, ...] = ()

    def __get_pydantic_core_schema__(
        self, source: object, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_plain_validator_function(self._validator(_leaf_types(source)))

    def _validator(self, allowed: tuple[type, ...]) -> Callable[[object], object]:
        expected = " | ".join(sorted({t.__name__ for t in allowed}))

        def check(value: object) -> object:
            if not _accepts(allowed, value):
                raise ValueError(f"{self.name} expects {expected}, got {type(value).__name__}")
            return value

        def validate(value: object) -> object:
            if value is None:
                return None
            if self.superseded_by:
                warnings.warn(
                    f"Schema.org property {self.name!r} is superseded by "
                    f"{', '.join(self.superseded_by)}",
                    DeprecationWarning,
                    stacklevel=2,
                )
            if is_multiple(value):
                return [check(item) for item in value]
            return check(value)

        return validate
