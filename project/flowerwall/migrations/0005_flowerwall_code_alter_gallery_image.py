# Generated by Django 5.0.6 on 2024-06-10 03:22

import flowerwall.models
import tools.views
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerwall', '0004_alter_flowerwall_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowerwall',
            name='code',
            field=models.IntegerField(default=1, unique=True, verbose_name='Code:'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=flowerwall.models.upload_image_gallery_path, validators=[tools.views.validate_image_extension], verbose_name='Gallery Image:'),
        ),
    ]
