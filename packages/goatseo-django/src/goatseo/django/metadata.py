"""Model metadata built from Django fields."""

from collections.abc import Sequence
from typing import TypeIs, Unpack

from goatseo.core import Metadata, MetadataFields


def _is_blank(value: object) -> bool:
    return isinstance(value, str) and not value.strip()


def _is_sequence(value: object) -> TypeIs[Sequence[object]]:
    return isinstance(value, Sequence) and not isinstance(value, str)


def _absent_if_blank(value: object) -> object:
    if _is_blank(value):
        return None
    if _is_sequence(value):
        return [item for item in value if not _is_blank(item)]
    return value


def model_metadata(**fields: Unpack[MetadataFields]) -> Metadata:
    """Builds ``Metadata`` where blank strings, as Django stores empty fields, mean "unset"."""
    values = {name: _absent_if_blank(value) for name, value in fields.items()}
    return Metadata.model_validate(values)
