from django.shortcuts import render, get_object_or_404

from django.http import Http404

from .models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by("date")
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    # TODO: Add mail to author email?
    # TODO: Add date
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, "blog/post-detail.html", {"post": post})
