# Generated by Django 5.0.6 on 2024-06-05 02:08

import django.core.validators
import tools.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, verbose_name='Title website:')),
                ('logo', models.FileField(upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Logo:')),
                ('call', models.CharField(blank=True, max_length=20, verbose_name='Call number:')),
                ('mobile', models.CharField(blank=True, max_length=20, verbose_name='Mobile number:')),
                ('email', models.CharField(blank=True, max_length=150, verbose_name='Email:')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Address:')),
                ('location_maps', models.URLField(blank=True, verbose_name='Location Maps:')),
                ('hour_work', models.CharField(blank=True, max_length=200, verbose_name='Hour Work:')),
                ('tag_keywords', models.TextField(verbose_name='Tag keywords:')),
                ('tag_description', models.CharField(max_length=250, verbose_name='Tag description:')),
                ('rules', models.TextField(blank=True, verbose_name='Rules website:')),
                ('bg_home_img', models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background Home Video:')),
                ('home_video', models.FileField(blank=True, help_text='acception format: video = [mp4, mpg, mpeg, avi, mkv]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv'])], verbose_name='Video Home:')),
                ('text_aboutus', models.TextField(verbose_name='Text About Us:')),
                ('bg_aboutus_img', models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background About Us Video:')),
                ('aboutus_video', models.FileField(blank=True, help_text='acception format: video = [mp4, mpg, mpeg, avi, mkv]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv'])], verbose_name='Video About Us:')),
                ('bg_404', models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background error 404:')),
                ('bg_500', models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background error 500:')),
                ('background_profile', models.FileField(blank=True, help_text='acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='بکگراند پروفایل سایت:')),
            ],
        ),
    ]
