from django.contrib import admin

from .models import *


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('time_create', 'photo')


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created']
    search_fields = ['name', 'email', 'body']


class AgeGroupAdmin(admin.ModelAdmin):
    list_display = ['name']


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['age_group', 'day', 'time', 'address']


class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['image', 'category']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date', 'author']


class FileAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(PostsPhoto, PhotoAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AgeGroup, AgeGroupAdmin)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(File, FileAdmin)
