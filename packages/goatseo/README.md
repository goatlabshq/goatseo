# goatseo

The type-safe SEO toolkit for Python. Installs the `SEO` builder with metadata, Open Graph, Twitter/X Cards and Schema.org support; framework adapters are available as extras.

```bash
pip install goatseo
pip install "goatseo[django]"  # or [fastapi], [flask]
```

```python
from goatseo import SEO

seo = SEO(title="Hello World", description="An interesting article")
print(seo.render())
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://github.com/midsonlajeanty/goatseo/tree/main/docs).
