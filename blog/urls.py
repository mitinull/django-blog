from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("posts", views.all_posts, name="all-posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),
]
