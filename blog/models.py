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
    # TODO: Add date field
    title = models.CharField(max_length=100)
    # TODO: Make it index instead of pk? when unique it's indexed also when it's slug
    slug = models.SlugField(primary_key=True, unique=True)
    image = models.CharField(max_length=500)
    # TODO: Change content to text field.
    # TODO: Add MinLengthValidator to content
    content = models.CharField(max_length=2000)
    # TODO: Change on delete to null
    # TODO: Add related name
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
