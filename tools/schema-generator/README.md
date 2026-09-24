# goatseo-schema-generator

Development tool that generates the `goatseo-schema` models from the official Schema.org ontology (N-Triples release, parsed into an internal representation, then mapped to Python). It is not published.

```bash
uv run goatseo-schema generate                  # newest vendored release in data/
uv run goatseo-schema generate --version latest # download from schema.org
uv run goatseo-schema generate --check          # fail if the committed code is stale
```
