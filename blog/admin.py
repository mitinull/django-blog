from django.contrib import admin

from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Photographer)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
