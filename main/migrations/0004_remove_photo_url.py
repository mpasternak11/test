# Generated by Django 4.1.1 on 2022-10-27 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_photo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='URL',
        ),
    ]
