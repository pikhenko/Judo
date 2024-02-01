from rest_framework import serializers

from backend.models import PhotoGallery


class PhotoGallerySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = PhotoGallery
