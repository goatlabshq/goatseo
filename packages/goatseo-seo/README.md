# goatseo-seo

The high-level `SEO` builder of GoatSEO, combining metadata, Open Graph, Twitter/X Cards and Schema.org into one framework-independent object.

```bash
pip install goatseo-seo
```

```python
from goatseo.seo import SEO

SEO(title="Hello").robots(index=False).render()
```

Part of [GoatSEO](https://github.com/goatlabshq/goatseo). See the [documentation](https://goatlabshq.github.io/goatseo/).
