import datetime as dt

from django.db import models
from django.urls import reverse

from goatseo import Metadata
from goatseo.django import model_metadata


class Article(models.Model):
    title: models.CharField[str, str] = models.CharField(max_length=200)
    slug: models.SlugField[str, str] = models.SlugField(unique=True)
    summary: models.TextField[str, str] = models.TextField()
    author: models.CharField[str, str] = models.CharField(max_length=100)
    published: models.DateTimeField[dt.datetime, dt.datetime] = models.DateTimeField()
    draft: models.BooleanField[bool, bool] = models.BooleanField(default=False)

    def get_absolute_url(self) -> str:
        return reverse("article", args=[self.slug])

    def seo_metadata(self) -> Metadata:
        return model_metadata(
            title=self.title,
            description=self.summary,
            canonical=self.get_absolute_url(),
            author=self.author,
        )
