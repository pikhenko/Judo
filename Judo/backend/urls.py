from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('team/', team),
    path('photo/', photo),
    path('shedule/', shedule),
]