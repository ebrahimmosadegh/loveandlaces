# Generated by Django 5.0.6 on 2024-06-05 02:19

import django.core.validators
import tools.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingssite',
            name='background_profile',
        ),
        migrations.AddField(
            model_name='settingssite',
            name='bg_cover',
            field=models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background Cover About Us, Contact, Services,:'),
        ),
    ]