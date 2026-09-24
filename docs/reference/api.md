# API reference

Only the names listed here are public. Everything else, including modules whose name starts
with an underscore, may change without notice.

## `goatseo`

| Name | Purpose |
| --- | --- |
| `SEO` | The page builder (from `goatseo.seo`) |
| `Metadata`, `Robots`, `Precedence`, `SafeHtml` | Re-exported from `goatseo.core` |
| `RequestContext`, `StaticRequestContext`, `SupportsMetadata` | Re-exported from `goatseo.core` |

## `goatseo.core`

### Metadata

| Name | Signature | Purpose |
| --- | --- | --- |
| `Metadata` | `Metadata(*, title=None, title_template=None, description=None, canonical=None, robots=None, language=None, locale=None, site_name=None, author=None, publisher=None, keywords=None, theme_color=None, alternates=None, hreflang=None)` | Page metadata |
| `Metadata.merged` | `(override: Metadata) -> Self` | Copy where fields set on `override` win |
| `Metadata.full_title` | `str | None` property | Title with the template applied |
| `MetadataFields` | `TypedDict` | Keyword arguments mirroring `Metadata` |
| `Robots` | `Robots(*, index=None, follow=None, archive=None, snippet=None, image_index=None, translate=None, max_snippet=None, max_image_preview=None, max_video_preview=None, unavailable_after=None)` | Robots directives |
| `Robots.directives` | `() -> tuple[str, ...]` | Directives in `<meta name="robots">` syntax |
| `Robots.merged` | `(override: Robots) -> Robots` | Per-directive merge |
| `RobotsDirectives` | `TypedDict` | Keyword arguments mirroring `Robots` |
| `HrefLang` | `HrefLang(*, hreflang: str, href: str)` | One hreflang alternate (`x-default` allowed) |
| `AlternateLink` | `AlternateLink(*, href, type=None, title=None, media=None)` | `rel="alternate"` link |
| `merge_metadata` | `(*layers: Metadata) -> Metadata` | Merge from least to most specific |

### Precedence

| Name | Signature | Purpose |
| --- | --- | --- |
| `Precedence` | `IntEnum`: `GLOBAL`, `SITE`, `APPLICATION`, `MODEL`, `VIEW`, `REQUEST` | Layer order |
| `MetadataStack` | `MetadataStack(layers: Mapping[Precedence, Metadata] | None = None)` | One layer per precedence |
| `MetadataStack.set` / `.update` | `(precedence, metadata) -> Self` | Replace or merge a layer |
| `MetadataStack.layer` | `(precedence) -> Metadata | None` | Read one layer |
| `MetadataStack.resolve` | `() -> Metadata` | Merged result, cached |
| `SupportsMetadata` | `Protocol` with `seo_metadata() -> Metadata` | Domain objects describing a page |

### Rendering

| Name | Signature | Purpose |
| --- | --- | --- |
| `Title`, `Meta`, `Link`, `JsonLd` | frozen dataclasses | Head elements |
| `HeadElement` | `Title | Meta | Link | JsonLd` | Union of head elements |
| `render_elements` | `(elements, *, separator="\n", json_indent=None) -> SafeHtml` | Escaped HTML |
| `metadata_elements` | `(metadata, *, base_url=None) -> Iterator[HeadElement]` | Metadata renderer |
| `ElementRenderer[T]` | `Protocol`: `(value: T, /) -> Iterable[HeadElement]` | Renderer shape |
| `SafeHtml` | `str` subclass with `__html__` | Trusted HTML |
| `JsonValue`, `JsonObject` | recursive type aliases | JSON data |
| `dumps_for_script` | `(value: JsonValue, *, indent=None) -> str` | JSON safe inside `<script>` |

### URLs, context, audit

| Name | Signature | Purpose |
| --- | --- | --- |
| `Url`, `AbsoluteUrl` | `Annotated[str, ...]` aliases | Validated URL types |
| `resolve_url` | `(url: str, base_url: str | None) -> str` | Resolve a relative URL |
| `UnsafeUrlError` | `ValueError` subclass | Rejected URL |
| `RequestContext` | `Protocol` with a `url: str` property | Current request |
| `StaticRequestContext` | `StaticRequestContext(url: str)` | Simple implementation |
| `audit` | `(metadata: Metadata) -> tuple[Issue, ...]` | SEO audit |
| `Issue`, `Severity` | dataclass, `StrEnum` | Audit results |

## `goatseo.seo`

| Name | Signature | Purpose |
| --- | --- | --- |
| `SEO` | `SEO(*, defaults=None, open_graph=None, twitter=None, schema=(), **metadata)` | Page builder |

Methods are listed in [the SEO builder guide](../guide/seo.md).

## `goatseo.opengraph`

| Name | Purpose |
| --- | --- |
| `OpenGraph`, `OpenGraphType` | Open Graph object and its type literal |
| `OpenGraphImage`, `OpenGraphVideo`, `OpenGraphAudio` | Structured media |
| `ArticleMetadata`, `ProfileMetadata`, `BookMetadata`, `VideoMetadata`, `VideoActor` | Type-specific metadata |
| `open_graph_elements(graph, *, base_url=None)` | Renderer |

## `goatseo.twitter`

| Name | Purpose |
| --- | --- |
| `TwitterCard`, `TwitterCardType` | The card and its kind |
| `TwitterPlayer`, `TwitterApp`, `TwitterAppStore` | Player and app card details |
| `twitter_elements(card, *, base_url=None)` | Renderer |

## `goatseo.schema`

| Name | Purpose |
| --- | --- |
| Every Schema.org type (`Thing`, `Article`, `Person`, ...) | Generated models |
| Every Schema.org enumeration (`ItemAvailability`, `DayOfWeek`, ...) | Generated `StrEnum` classes |
| `SchemaModel`, `SchemaEnumeration` | Base classes |
| `to_jsonld(model, *, context=CONTEXT)` | One JSON-LD node |
| `to_graph(models, *, context=CONTEXT)` | `@graph` document |
| `jsonld_element(models)` | `JsonLd` head element or `None` |
| `CONTEXT`, `SCHEMA_ORG_VERSION` | `"https://schema.org"`, generated release |

## `goatseo.django`

| Name | Purpose |
| --- | --- |
| `get_seo(request)` | Request-scoped `SEO` |
| `request_context(request)` | `RequestContext` from an `HttpRequest` |
| `SEOMixin` | Class-based view mixin |
| `seo_defaults(**fields)` | Function-based view decorator |
| `goatseo.django.context_processors.seo` | Adds `seo` to template contexts |
| `goatseo.django.middleware.GoatSEOMiddleware` | `X-Robots-Tag` header |
| `{% goatseo_head %}`, `{% goatseo_jsonld %}` | Template tags (`{% load goatseo %}`) |

## `goatseo.fastapi`

| Name | Purpose |
| --- | --- |
| `SEO` | Re-export of `goatseo.seo.SEO` |
| `GoatSEO(defaults=None)` | Dependency and template installer |
| `goatseo_head(seo, request)` | Render for a Starlette request |
| `request_context(request)` | `RequestContext` from a Starlette request |

## `goatseo.flask`

| Name | Purpose |
| --- | --- |
| `SEOExtension(app=None, *, defaults=None, robots_header=False)` | The extension |
| `get_seo()` | Request-scoped `SEO` |
| `goatseo_head()` | Render for the current request |
