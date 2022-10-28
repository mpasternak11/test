# Generated by Django 4.1.1 on 2022-10-27 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='URL',
            field=models.CharField(max_length=250, verbose_name='URL'),
        ),
    ]
