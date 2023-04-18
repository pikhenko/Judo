from django.urls import path

from .views import index, team, photo, shedule

urlpatterns = [
    path('', index, name='index'),
    path('team/', team),
    path('photo/', photo),
    path('shedule/', shedule),
]
