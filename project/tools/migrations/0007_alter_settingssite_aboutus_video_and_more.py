# Generated by Django 5.0.6 on 2024-06-10 18:08

import django.core.validators
import tools.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_alter_settingssite_location_maps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingssite',
            name='aboutus_video',
            field=models.FileField(blank=True, help_text='resulotion(1080*1920) , acception format: video = [mp4, mpg, mpeg, avi, mkv]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv'])], verbose_name='Video About Us:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='bg_404',
            field=models.FileField(blank=True, help_text='resulotion(1920*1000) , acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background error 404:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='bg_500',
            field=models.FileField(blank=True, help_text='resulotion(1920*1000) , acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background error 500:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='bg_aboutus_img',
            field=models.FileField(blank=True, help_text='resulotion(970*800) , acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background About Us Video:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='bg_cover',
            field=models.FileField(blank=True, help_text='resulotion(1920*380) , acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background Cover About Us, Contact, Services,:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='bg_home_img',
            field=models.FileField(blank=True, help_text='resulotion(1720*500) , acception format: image = [jpg, png, bmp, gif, jpeg, svg]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Background Home Video:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='home_video',
            field=models.FileField(blank=True, help_text='resulotion(1080*1920) , acception format: video = [mp4, mpg, mpeg, avi, mkv]', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv'])], verbose_name='Video Home:'),
        ),
        migrations.AlterField(
            model_name='settingssite',
            name='logo',
            field=models.FileField(help_text='resulotion(80*80)', upload_to=tools.models.upload_media_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg'])], verbose_name='Logo:'),
        ),
    ]
