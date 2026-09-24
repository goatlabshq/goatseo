"""The only thing GoatSEO needs from a web framework: the URL of the current request."""

from dataclasses import dataclass
from typing import Protocol


class RequestContext(Protocol):
    @property
    def url(self) -> str: ...


@dataclass(frozen=True, slots=True)
class StaticRequestContext:
    url: str
