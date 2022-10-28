from django.contrib import admin
from django.urls import path, include

from main.views import PhotoViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'photo', PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
