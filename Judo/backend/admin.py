from django.contrib import admin

from .models import *

class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('time_create', 'photo')

admin.site.register(Posts, PostsAdmin)
admin.site.register(Photo, PhotoAdmin)
