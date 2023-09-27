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
        return render(request, "blog/post-detail.html", {"post": post})

    def post(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs["slug"])
        data = request.POST
        print(data)
        new_comment = Comment(
            name=data.get("name"), message=data.get("comment"), post=post
        )
        new_comment.save()
        return HttpResponseRedirect(f'/{kwargs["slug"]}')
