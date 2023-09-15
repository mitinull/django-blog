from django.shortcuts import render

from django.http import Http404

# Create your views here.
data = [
    {
        "slug": "azadi-tower",
        "title": "Azadi Tower",
        "image": "azadi.jpg",
        "content": "this is the part of me!",
    },
    {
        "slug": "bike",
        "title": "Bike",
        "image": "bike.jpg",
        "content": """I'm taking my time on my ride!
            Are you taking your time on your ride?""",
    },
    {
        "slug": "milad-tower",
        "title": "Milad Tower",
        "image": "milad.jpg",
        "content": "This is huge!",
    },
]


def home(request):
    return render(request, "blog/index.html", {"posts": data})


def post_detail(request, slug):
    post = next((post for post in data if post["slug"] == slug), None)
    if post == None:
        raise Http404
    return render(request, "blog/post-detail.html", {"post": post})
