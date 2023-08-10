from django.db import models
from django.urls import reverse


class Photo(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'


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
