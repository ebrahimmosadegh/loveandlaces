from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
# Create your models here.
def upload_media_path(instance, filename):
    return f"Settings/{filename}"

class SettingsSite(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Title website:')
    logo = models.FileField(upload_to=upload_media_path, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Logo:')
    call = models.CharField(max_length=20, blank=True, verbose_name='Call number:')
    mobile = models.CharField(max_length=20, blank=True, verbose_name='Mobile number:')
    email = models.CharField(max_length=150, blank=True, verbose_name='Email:')
    address = models.CharField(max_length=200, blank=True, verbose_name='Address:')
    location_maps = models.URLField(blank=True, verbose_name='Location Maps:')
    hour_work = models.CharField(max_length=200, blank=True, verbose_name='Hour Work:')
    tag_keywords = models.TextField(verbose_name='Tag keywords:')
    tag_description = models.CharField(max_length=250, verbose_name='Tag description:')
    rules = models.TextField(verbose_name='Rules website:', blank=True)
    bg_home_img = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Background Home Video:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')
    home_video = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv',])], verbose_name='Video Home:', help_text="acception format: "
        'video = [mp4, mpg, mpeg, avi, mkv]')
    text_aboutus = models.TextField(verbose_name='Text About Us:')
    bg_aboutus_img = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Background About Us Video:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')
    aboutus_video = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv',])], verbose_name='Video About Us:', help_text="acception format: "
        'video = [mp4, mpg, mpeg, avi, mkv]')
    bg_404 = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Background error 404:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')
    bg_500 = models.FileField(upload_to=upload_media_path, blank=True, validators=[
        FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg', ])], verbose_name='Background error 500:',
                                      help_text="acception format: "
                                                'image = [jpg, png, bmp, gif, jpeg, svg]')
    background_profile = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='بکگراند پروفایل سایت:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')