# goatseo-flask

Flask integration for GoatSEO: the `SEOExtension`, request-scoped state through `get_seo()` and a `goatseo_head()` Jinja global.

```bash
pip install goatseo-flask
```

```python
from goatseo.flask import SEOExtension, get_seo

SEOExtension(app)
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://midsonlajeanty.github.io/goatseo/).
