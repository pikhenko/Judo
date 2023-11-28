from rest_framework import routers
from django.urls import include, path

from .views import PhotoGalleryViewSet

router = routers.DefaultRouter()
router.register('photogalary', PhotoGalleryViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]