# Tools

Development tools of the workspace. They are never published.

- `schema-generator`: the `goatseo-schema` CLI that generates the Schema.org models of
  `packages/goatseo-schema` from the official ontology.

```bash
uv run goatseo-schema generate          # regenerate from the vendored release
uv run goatseo-schema generate --check  # fail if the generated code is stale
```
