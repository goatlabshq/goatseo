"""GoatSEO: the type-safe SEO toolkit for Python."""

from pkgutil import extend_path

# Editable installs give each workspace package its own sys.path entry; extending __path__
# lets goatseo.core, goatseo.schema, ... resolve as portions of this regular package.
__path__ = extend_path(__path__, __name__)

from goatseo.core import (
    Metadata,
    Precedence,
    RequestContext,
    Robots,
    SafeHtml,
    StaticRequestContext,
    SupportsMetadata,
)
from goatseo.seo import SEO

__all__ = [
    "SEO",
    "Metadata",
    "Precedence",
    "RequestContext",
    "Robots",
    "SafeHtml",
    "StaticRequestContext",
    "SupportsMetadata",
]
