from django.shortcuts import render
from rest_framework import viewsets

from main.models import Photo
from main.serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer