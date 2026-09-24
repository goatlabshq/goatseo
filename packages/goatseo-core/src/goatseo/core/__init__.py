"""Framework-independent SEO primitives."""

from goatseo.core.context import RequestContext, StaticRequestContext
from goatseo.core.html import HeadElement, JsonLd, Link, Meta, SafeHtml, Title, render_elements
from goatseo.core.metadata import (
    AlternateLink,
    HrefLang,
    Metadata,
    MetadataFields,
    Robots,
    RobotsDirectives,
    merge_metadata,
)
from goatseo.core.precedence import MetadataStack, Precedence, SupportsMetadata
from goatseo.core.renderer import ElementRenderer, metadata_elements
from goatseo.core.serialization import JsonObject, JsonValue, dumps_for_script
from goatseo.core.urls import AbsoluteUrl, UnsafeUrlError, Url, resolve_url
from goatseo.core.validation import Issue, Severity, audit

__all__ = [
    "AbsoluteUrl",
    "AlternateLink",
    "ElementRenderer",
    "HeadElement",
    "HrefLang",
    "Issue",
    "JsonLd",
    "JsonObject",
    "JsonValue",
    "Link",
    "Meta",
    "Metadata",
    "MetadataFields",
    "MetadataStack",
    "Precedence",
    "RequestContext",
    "Robots",
    "RobotsDirectives",
    "SafeHtml",
    "Severity",
    "StaticRequestContext",
    "SupportsMetadata",
    "Title",
    "UnsafeUrlError",
    "Url",
    "audit",
    "dumps_for_script",
    "merge_metadata",
    "metadata_elements",
    "render_elements",
    "resolve_url",
]
