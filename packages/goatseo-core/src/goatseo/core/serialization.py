"""JSON values and serialization that is safe to embed inside an HTML ``<script>`` element."""

import json
from typing import Final

type JsonValue = str | int | float | bool | list[JsonValue] | dict[str, JsonValue] | None
type JsonObject = dict[str, JsonValue]

# Escaping these keeps "</script>", "<!--" and line separators from ending or corrupting
# the script element, while the JSON document itself stays byte-for-byte equivalent.
_SCRIPT_ESCAPES: Final = str.maketrans(
    {"<": "\\u003c", ">": "\\u003e", "&": "\\u0026", "\u2028": "\\u2028", "\u2029": "\\u2029"}
)


def dumps_for_script(value: JsonValue, *, indent: int | None = None) -> str:
    separators = (",", ": ") if indent is not None else (",", ":")
    text = json.dumps(
        value, ensure_ascii=False, allow_nan=False, indent=indent, separators=separators
    )
    return text.translate(_SCRIPT_ESCAPES)
