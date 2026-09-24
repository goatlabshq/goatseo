# goatseo-opengraph

Typed Open Graph protocol models (images, video, audio, article, profile, book, video metadata) and their renderer.

```bash
pip install goatseo-opengraph
```

```python
from goatseo.opengraph import OpenGraph, open_graph_elements

elements = list(open_graph_elements(OpenGraph(title="Hello", type="article")))
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://github.com/midsonlajeanty/goatseo/tree/main/docs).
