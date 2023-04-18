from django.contrib import admin
from django.urls import path, include
from backend.views import *
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', include(('backend.urls', 'backend'))),
    path('auth/', include('django.contrib.auth.urls')),
]
