from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Photographer)
admin.site.register(Tag)
admin.site.register(Post)
