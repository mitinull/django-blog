from django.shortcuts import render

from django.http import Http404

from .models import Post

# Create your views here.


# TODO: Moving query inside functions
posts = Post.objects.all()


def home(request):
    return render(request, "blog/index.html", {"posts": posts})


def post_detail(request, slug):
    # TODO: Add get_object_or_404 ?
    # TODO: Add mail to author email?
    # TODO: Add date
    post = posts.get(slug=slug)
    if post == None:
        raise Http404
    return render(request, "blog/post-detail.html", {"post": post})
