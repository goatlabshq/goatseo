import django
from django.conf import settings

TEMPLATES = {
    "goatseo/head.html": "{% load goatseo %}{% goatseo_head %}",
    "goatseo/jsonld.html": "{% load goatseo %}{% goatseo_jsonld %}",
}

if not settings.configured:
    settings.configure(
        SECRET_KEY="goatseo-tests",  # noqa: S106
        ALLOWED_HOSTS=["testserver"],
        INSTALLED_APPS=["goatseo.django"],
        MIDDLEWARE=["goatseo.django.middleware.GoatSEOMiddleware"],
        ROOT_URLCONF="goatseo.django",
        USE_TZ=True,
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "goatseo.django.context_processors.seo",
                    ],
                    "loaders": [("django.template.loaders.locmem.Loader", TEMPLATES)],
                },
            }
        ],
    )
    django.setup()
