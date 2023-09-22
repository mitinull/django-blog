from django.shortcuts import render

from django.http import Http404

from .models import Post

# Create your views here.
posts = Post.objects.all()


def home(request):
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    post = posts.get(slug=slug)
    if post == None:
        raise Http404
    return render(request, "blog/post-detail.html", {"post": post})
