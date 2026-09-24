# goatseo-core

Framework-independent primitives of GoatSEO: typed page metadata, deterministic precedence between metadata layers, URL safety, escaped HTML rendering of head elements and an SEO audit.

```bash
pip install goatseo-core
```

```python
from goatseo.core import Metadata, metadata_elements, render_elements

html = render_elements(metadata_elements(Metadata(title="Hello")))
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://midsonlajeanty.github.io/goatseo/).
