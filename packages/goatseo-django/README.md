# goatseo-django

Django integration for GoatSEO: app config, request-scoped SEO state, `{% goatseo_head %}` template tag, context processor, optional `X-Robots-Tag` middleware and view helpers.

```bash
pip install goatseo-django
```

```python
from goatseo.django import get_seo


def article(request):
    get_seo(request).title("Hello")
    ...
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://midsonlajeanty.github.io/goatseo/).
