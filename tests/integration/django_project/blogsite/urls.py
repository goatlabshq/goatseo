from django.urls import path

from articles.views import ArticleDetail, home

urlpatterns = [
    path("", home, name="home"),
    path("articles/<slug:slug>/", ArticleDetail.as_view(), name="article"),
]
