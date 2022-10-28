from rest_framework import serializers

from main.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
        read_only_fields = ('width', 'height', 'image', 'color')
