"""Renders the Python declarations as source code."""

import re
from collections.abc import Iterable
from typing import Final

from goatseo_schema_generator.mapper import (
    ENUMERATION_BASE,
    MODEL_BASE,
    PyEnum,
    PyField,
    PyModel,
    PyModule,
)

SCHEMA_ORG: Final = "https://schema.org/"
_HEADER: Final = '''"""Schema.org {what}, generated from Schema.org {version}.

Do not edit: run `uv run goatseo-schema generate` instead.
"""
'''
_WIKI_LINK: Final = re.compile(r"\[\[([^\]]+)\]\]")
_MARKDOWN_LINK: Final = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_HTML_TAG: Final = re.compile(r"<[^>]+>")
_SENTENCE_END: Final = re.compile(r"(?<!e\.g)(?<!i\.e)(?<!etc)\.(?:\s|$)")
_MAX_SUMMARY: Final = 240


def summary(description: str | None) -> str | None:
    if not description:
        return None
    text = _WIKI_LINK.sub(r"\1", description)
    text = _MARKDOWN_LINK.sub(r"\1", text)
    text = _HTML_TAG.sub("", text)
    text = " ".join(text.replace("\u2014", ", ").split()).replace(" ,", ",")
    end = _SENTENCE_END.search(text)
    if end is not None:
        text = text[: end.start() + 1]
    if len(text) > _MAX_SUMMARY:
        text = text[: _MAX_SUMMARY - 3].rstrip() + "..."
    return text.replace("\\", "\\\\").replace('"""', '\\"\\"\\"') or None


def _docstring(description: str | None, schema_name: str, superseded_by: tuple[str, ...]) -> str:
    lines = [summary(description) or schema_name, "", f"{SCHEMA_ORG}{schema_name}"]
    if superseded_by:
        lines += ["", f"Deprecated: superseded by {', '.join(superseded_by)}."]
    body = "\n    ".join(lines)
    return f'    """{body}\n    """\n'


def _annotation(field: PyField) -> str:
    union = " | ".join(field.types)
    marker = f'prop("{field.schema_name}"'
    if field.superseded_by:
        superseded = ", ".join(f'"{name}"' for name in field.superseded_by)
        marker += f", superseded_by=({superseded},)"
    return f"Annotated[{union} | list[{union}] | None, {marker})]"


def _render_model(model: PyModel) -> str:
    out = [f"class {model.name}({', '.join(model.bases)}):\n"]
    out.append(_docstring(model.description, model.schema_name, model.superseded_by))
    out.append(f'\n    jsonld_type: ClassVar[str] = "{model.schema_name}"\n')
    out.extend(f"    {f.name}: {_annotation(f)} = None\n" for f in model.fields)
    return "".join(out)


def _render_enum(enum: PyEnum) -> str:
    out = [f"class {enum.name}({ENUMERATION_BASE}):\n"]
    out.append(_docstring(enum.description, enum.schema_name, enum.superseded_by))
    out.append("\n")
    out.extend(f'    {m.name} = "{SCHEMA_ORG}{m.schema_name}"\n' for m in enum.members)
    return "".join(out)


def _all(names: Iterable[str]) -> str:
    return "__all__ = [\n" + "".join(f'    "{n}",\n' for n in sorted(names)) + "]\n"


def render_enumerations(module: PyModule) -> str:
    parts = [
        _HEADER.format(what="enumerations", version=module.version),
        f"\nfrom goatseo.schema.base import {ENUMERATION_BASE}\n\n",
        _all(e.name for e in module.enums),
    ]
    parts.extend(f"\n\n{_render_enum(e)}" for e in module.enums)
    return "".join(parts)


def render_types(module: PyModule) -> str:
    used = {t for m in module.models for f in m.fields for t in f.types}
    enums = sorted(e.name for e in module.enums if e.name in used)
    base_names = [ENUMERATION_BASE] if ENUMERATION_BASE in used else []
    imports = [
        "import datetime as _dt\n" if any(t.startswith("_dt.") for t in used) else "",
        "from typing import Annotated, ClassVar\n\n",
        f"from goatseo.schema.base import {', '.join([*base_names, MODEL_BASE, 'prop'])}\n",
    ]
    if enums:
        imports.append(
            "from goatseo.schema._enumerations import (\n"
            + "".join(f"    {name},\n" for name in enums)
            + ")\n"
        )
    parts = [
        _HEADER.format(what="types", version=module.version),
        "\n",
        *imports,
        "\n",
        _all(m.name for m in module.models),
    ]
    parts.extend(f"\n\n{_render_model(m)}" for m in module.models)
    return "".join(parts)


def render_version(module: PyModule) -> str:
    return (
        _HEADER.format(what="release", version=module.version)
        + f'\nfrom typing import Final\n\nSCHEMA_ORG_VERSION: Final = "{module.version}"\n'
    )
