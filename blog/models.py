from django.db import models


# Create your models here.


class Photographer(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True, unique=True)
    image = models.CharField(max_length=500)
    content = models.CharField(max_length=2000)
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
