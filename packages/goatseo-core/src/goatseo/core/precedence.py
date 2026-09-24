"""Metadata layers resolved from the least to the most specific."""

from collections.abc import Mapping
from enum import IntEnum
from typing import Protocol, Self, runtime_checkable

from goatseo.core.metadata import Metadata, merge_metadata


class Precedence(IntEnum):
    GLOBAL = 0
    SITE = 10
    APPLICATION = 20
    MODEL = 30
    VIEW = 40
    REQUEST = 50


@runtime_checkable
class SupportsMetadata(Protocol):
    """Implemented by domain objects (a Django model, a dataclass...) that describe their page."""

    def seo_metadata(self) -> Metadata: ...


class MetadataStack:
    """Holds one metadata layer per precedence level; higher levels override lower ones."""

    __slots__ = ("_layers", "_resolved")

    def __init__(self, layers: Mapping[Precedence, Metadata] | None = None) -> None:
        self._layers: dict[Precedence, Metadata] = dict(layers or {})
        self._resolved: Metadata | None = None

    def set(self, precedence: Precedence, metadata: Metadata) -> Self:
        self._layers[precedence] = metadata
        self._resolved = None
        return self

    def update(self, precedence: Precedence, metadata: Metadata) -> Self:
        """Merges ``metadata`` into the layer at ``precedence`` instead of replacing it."""
        current = self._layers.get(precedence)
        return self.set(precedence, metadata if current is None else current.merged(metadata))

    def layer(self, precedence: Precedence) -> Metadata | None:
        return self._layers.get(precedence)

    def resolve(self) -> Metadata:
        if self._resolved is None:
            self._resolved = merge_metadata(*(self._layers[p] for p in sorted(self._layers)))
        return self._resolved

    def copy(self) -> MetadataStack:
        return MetadataStack(self._layers)
