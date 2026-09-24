# goatseo-twitter

Typed Twitter/X Cards models (summary, large image, app and player cards) and their renderer.

```bash
pip install goatseo-twitter
```

```python
from goatseo.twitter import TwitterCard, TwitterCardType, twitter_elements

card = TwitterCard(card=TwitterCardType.SUMMARY_LARGE_IMAGE, title="Hello")
```

Part of [GoatSEO](https://github.com/goatlabshq/goatseo). See the [documentation](https://goatlabshq.github.io/goatseo/).
