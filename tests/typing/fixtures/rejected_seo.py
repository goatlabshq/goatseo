from goatseo import SEO, Metadata, Precedence, Robots

SEO(title=1)  # expect-error
SEO(unknown="x")  # expect-error
seo = SEO()
seo.robots(index="no")  # expect-error
seo.robots(Robots(), unknown=True)  # expect-error
seo.hreflang("en")  # expect-error
seo.hreflang({"en": 1})  # expect-error
seo.title("x").nonexistent  # expect-error
seo.defaults(Metadata(), "site")  # expect-error
seo.keywords(["a", "b"])  # expect-error
Metadata(keywords=1)  # expect-error
Metadata(robots={"index": False})  # expect-error
seo.defaults(Metadata(), Precedence.VIEW).schema("not a model")  # expect-error
