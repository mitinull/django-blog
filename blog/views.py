from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "blog/index.html")


def all_posts(request):
    return HttpResponse("All Posts")


def post_detail(request, slug):
    return HttpResponse("Post Detail")
