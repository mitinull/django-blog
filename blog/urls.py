from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("<slug:slug>", views.post_detail.as_view(), name="post-detail-page"),
    path("<slug:slug>/like", views.post_like.as_view(), name="post-like"),
]
