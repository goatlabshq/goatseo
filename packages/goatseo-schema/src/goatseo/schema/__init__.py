"""Statically typed Schema.org models and JSON-LD serialization.

The generated types load on first access, so importing this package stays cheap.
"""

from importlib import import_module
from typing import TYPE_CHECKING, Final

from goatseo.schema._version import SCHEMA_ORG_VERSION as SCHEMA_ORG_VERSION
from goatseo.schema.base import SchemaEnumeration as SchemaEnumeration
from goatseo.schema.base import SchemaModel as SchemaModel
from goatseo.schema.jsonld import CONTEXT as CONTEXT
from goatseo.schema.jsonld import jsonld_element as jsonld_element
from goatseo.schema.jsonld import to_graph as to_graph
from goatseo.schema.jsonld import to_jsonld as to_jsonld

# No __all__: type checkers then export the wildcard names below, which exist at runtime
# only through __getattr__, and an explicit list would have to repeat 850 generated names.
if TYPE_CHECKING:
    from goatseo.schema._enumerations import *  # noqa: F403
    from goatseo.schema._types import *  # noqa: F403

_GENERATED_MODULES: Final = ("goatseo.schema._types", "goatseo.schema._enumerations")


def __getattr__(name: str) -> object:
    for module_name in _GENERATED_MODULES:
        module = import_module(module_name)
        if name in module.__dict__.get("__all__", ()):
            value: object = getattr(module, name)
            globals()[name] = value
            return value
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
