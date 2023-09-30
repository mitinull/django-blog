from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.urls import reverse

from .models import Post
from .forms import CommentForm

# Create your views here.


# def home(request):
#     posts = Post.objects.all().order_by("date")
#     return render(request, "blog/index.html", {"posts": posts})


class Home(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"


class post_detail(View):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        liked_posts = request.session.get("liked_posts") or []
        is_liked = kwargs["slug"] in liked_posts
        return render(
            request,
            "blog/post-detail.html",
            {"post": post, "liked": is_liked, "form": CommentForm()},
        )

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        liked_posts = request.session.get("liked_posts") or []
        is_liked = kwargs["slug"] in liked_posts
        data = request.POST
        form = CommentForm(data)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            return render(
                request,
                "blog/post-detail.html",
                {"post": post, "liked": is_liked, "form": form},
            )
        return HttpResponseRedirect(reverse("post-detail-page", args=[kwargs["slug"]]))


class post_like(View):
    def post(self, request, **kwargs):
        slug = kwargs["slug"]
        print("POST/like")
        body = request.POST
        liked_posts: list = request.session.get("liked_posts") or []

        if body["liked"] and kwargs["slug"] not in liked_posts:
            liked_posts.append(kwargs["slug"])
            request.session["liked_posts"] = liked_posts

            post = Post.objects.get(slug=slug)
            post.num_likes += 1
            post.save()
        else:
            liked_posts.remove(kwargs["slug"])
            request.session["liked_posts"] = liked_posts

            post = Post.objects.get(slug=slug)
            post.num_likes -= 1
            post.save()

        return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
