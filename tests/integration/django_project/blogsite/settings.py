import django_stubs_ext

from goatseo import Metadata, Robots

django_stubs_ext.monkeypatch()

SECRET_KEY = "goatseo-integration"  # noqa: S105
DEBUG = False
ALLOWED_HOSTS = ["testserver", "blog.example"]
ROOT_URLCONF = "blogsite.urls"
USE_TZ = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = ["goatseo.django", "articles"]
MIDDLEWARE = ["goatseo.django.middleware.GoatSEOMiddleware"]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "goatseo.django.context_processors.seo",
            ],
        },
    },
]

GOATSEO_DEFAULTS = Metadata(
    site_name="Goat Blog",
    title_template="{title} | Goat Blog",
    locale="en_US",
    robots=Robots(index=True, follow=True),
)
