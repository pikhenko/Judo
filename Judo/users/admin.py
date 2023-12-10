from django.contrib import admin
from .models import Profile, User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'bio']


class UserAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
