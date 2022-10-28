from django.db import models
from django.utils.translation import gettext as _
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')


class Photo(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=100)
    width = models.IntegerField(verbose_name=_('Width'), default=0)
    height = models.IntegerField(verbose_name=_('Height'), default=0)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True, height_field='height',
                              width_field='width')
    album_id = models.ForeignKey('Album', on_delete=models.PROTECT)
    color = models.CharField(verbose_name=_('Color'), max_length=20)
    URL = models.ImageField(verbose_name=_('URL'), storage=fs, blank=True)

    def __str__(self):
        return self.title


class Album(models.Model):
    album = models.CharField(verbose_name=_('Album'), max_length=20)

    def __str__(self):
        return self.album
