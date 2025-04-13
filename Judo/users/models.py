# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


class AgeGroup(models.Model):
    name = models.CharField(max_length=100, verbose_name="Возраст")
    
    class Meta:
        verbose_name = 'Возраст'
        verbose_name_plural = 'Возраст'
    
    def __str__(self):
        return self.name

    
class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='ava2.png', upload_to='profile_images')
    bio = models.TextField()
    age_group = models.ForeignKey(AgeGroup, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
