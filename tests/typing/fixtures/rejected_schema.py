from goatseo.schema import Article, ItemAvailability, Offer, Person

Article(headline=123)  # expect-error
Article(author="not a person or organization")  # expect-error
Article(headline=["ok", 1])  # expect-error
Offer(availability="nope")  # expect-error
Offer(availability=ItemAvailability.InStock, price="10")
Person(unknown_property="x")  # expect-error
article = Article(headline="Hello")
article.headline = 1  # expect-error
