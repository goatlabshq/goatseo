from goatseo.opengraph import OpenGraph, OpenGraphImage
from goatseo.twitter import TwitterCard, TwitterCardType

OpenGraph(type="nope")  # expect-error
OpenGraph(images=[OpenGraphImage(url="https://example.com/a.png", width="wide")])  # expect-error
OpenGraph(images="https://example.com/a.png")  # expect-error
TwitterCard(card="summary")  # expect-error
TwitterCard(card=TwitterCardType.SUMMARY, title=1)  # expect-error
