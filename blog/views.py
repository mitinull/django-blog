from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpResponse, HttpResponseRedirect

from django.views import View

from .models import Post, Comment

# Create your views here.


def home(request):
    posts = Post.objects.all().order_by("date")
    return render(request, "blog/index.html", {"posts": posts})


class post_detail(View):
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        liked_posts = request.session.get("liked_posts") or []
        is_liked = kwargs["slug"] in liked_posts
        return render(
            request, "blog/post-detail.html", {"post": post, "liked": is_liked}
        )

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        data = request.POST
        print(data)
        new_comment = Comment(
            name=data.get("name"), message=data.get("comment"), post=post
        )
        new_comment.save()
        return HttpResponseRedirect(f'/{kwargs["slug"]}')


class post_like(View):
    def post(self, request, **kwargs):
        print("POST/like")
        body = request.POST
        liked_posts: list = request.session.get("liked_posts")
        if liked_posts:
            if body["liked"] and kwargs["slug"] not in request.session["liked_posts"]:
                liked_posts.append(kwargs["slug"])
                request.session["liked_posts"] = liked_posts
            else:
                liked_posts.remove(kwargs["slug"])
                request.session["liked_posts"] = liked_posts
        else:
            if body["liked"]:
                request.session["liked_posts"] = [kwargs["slug"]]
        return HttpResponseRedirect(f'/{kwargs["slug"]}')
