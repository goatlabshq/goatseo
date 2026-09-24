# goatseo-schema

Every Schema.org type as a statically typed Pydantic model, generated from the official ontology, with safe JSON-LD serialization.

```bash
pip install goatseo-schema
```

```python
from goatseo.schema import Article, Person, to_jsonld

to_jsonld(Article(headline="Hello", author=Person(name="John Doe")))
```

Part of [GoatSEO](https://github.com/midsonlajeanty/goatseo). See the [documentation](https://github.com/midsonlajeanty/goatseo/tree/main/docs).
