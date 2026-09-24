# goatseo-fastapi

FastAPI integration for GoatSEO: a per-request `SEO` dependency and a Jinja2 `goatseo_head` helper.

```bash
pip install goatseo-fastapi
```

```python
from typing import Annotated
from fastapi import Depends
from goatseo.fastapi import SEO, GoatSEO

SEODep = Annotated[SEO, Depends(GoatSEO())]
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://midsonlajeanty.github.io/goatseo/).
