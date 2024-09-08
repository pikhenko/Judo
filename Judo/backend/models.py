from collections.abc import Iterable
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

from users.models import User, AgeGroup


class PostsPhoto(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'
        ordering = ['time_create', ]


class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('backend:read_post', kwargs={'post_slug': self.slug})
    
    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']


class Comment(models.Model):
    post = models.ForeignKey(Posts,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name="Пост")
    author = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80, verbose_name="Имя")
    email = models.EmailField()
    body = models.TextField(verbose_name="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'
        ordering = ['created',]
        indexes = [
            models.Index(fields=['created']),
        ]
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class PhotoGallery(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=False, blank=False)
    # description = models.TextField()
    date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        return self.category


def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    PhotoGallery.objects.filter(category=category).delete()
    category.delete()


class Schedule(models.Model):
    age_group = models.ForeignKey(AgeGroup,
                                  related_name='age_group',
                                  on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    time = models.TimeField()
    address = models.CharField(max_length=100, default='DEFAULT VALUE', verbose_name="Адрес")

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'


class News(models.Model):
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
class File(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/', verbose_name="Логотип")
    photo = models.ImageField(upload_to='photo/', null=True, blank=True, verbose_name="Фото тренера")
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'
