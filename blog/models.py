from django.db import models

from django.core.validators import MinLengthValidator


# Create your models here.


class Photographer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, primary_key=True)
    order = models.IntegerField(null=True)
    image = models.ImageField(upload_to="post-image-uploads")
    content = models.TextField(validators=[MinLengthValidator(10)])
    photographer = models.ForeignKey(
        Photographer, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag)
    num_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    date = models.DateTimeField(auto_now=True)
