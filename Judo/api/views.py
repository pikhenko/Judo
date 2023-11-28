from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


from backend.models import PhotoGallery

from .permissions import PostPermission
from .serializers import PhotoGallerySerializer

class CreateUpdateDestroyViewSet(viewsets.ModelViewSet):
    permission_classes = (PostPermission,)


# Create your views here.
class PhotoGalleryViewSet(CreateUpdateDestroyViewSet):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGallerySerializer
    pagination_class = LimitOffsetPagination