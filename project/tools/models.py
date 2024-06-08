from django.db import models
from django.core.validators import FileExtensionValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

def upload_media_path(instance, filename):
    return f"Settings/{filename}"

class SettingsSite(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name='Title website:')
    logo = models.FileField(upload_to=upload_media_path, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Logo:')
    link = models.URLField(blank=True, verbose_name='Link Website:')
    call = models.CharField(max_length=20, blank=True, verbose_name='Call number:')
    mobile = models.CharField(max_length=20, blank=True, verbose_name='Mobile number:')
    email = models.CharField(max_length=150, blank=True, verbose_name='Email:')
    address = models.CharField(max_length=200, blank=True, verbose_name='Address:')
    location_maps = models.CharField(max_length=600,blank=True, verbose_name='Location Maps:')
    hour_work = models.CharField(max_length=200, blank=True, verbose_name='Hour Work:')
    tag_keywords = models.TextField(verbose_name='Tag keywords:')
    tag_description = models.CharField(max_length=250, verbose_name='Tag description:')
    rules = models.TextField(verbose_name='Rules website:', blank=True)
    bg_home_img = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Background Home Video:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')
    home_video = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['mp4', 'mpg', 'mpeg', 'avi', 'mkv',])], verbose_name='Video Home:', help_text="acception format: "
        'video = [mp4, mpg, mpeg, avi, mkv]')
    bg_cover = models.FileField(upload_to=upload_media_path, blank=True, validators=[FileExtensionValidator(['jpg', 'png', 'svg', 'bmp', 'gif', 'jpeg',])], verbose_name='Background Cover About Us, Contact, Services,:', help_text="acception format: "
        'image = [jpg, png, bmp, gif, jpeg, svg]')
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
    
    class Meta:
        verbose_name = 'settings'
        verbose_name_plural = 'settings website'

    def __str__(self):
        return self.title

@receiver(pre_save, sender=SettingsSite)
def delete_old_image_category(sender, instance, *args, **kwargs):
        if instance.pk:
            g_file = SettingsSite.objects.get(pk=instance.pk)
            if instance.logo and g_file.logo != instance.logo:
                g_file.logo.delete(False)
            if instance.bg_home_img and g_file.bg_home_img != instance.bg_home_img:
                g_file.bg_home_img.delete(False)
            if instance.home_video and g_file.home_video != instance.home_video:
                g_file.home_video.delete(False)
            if instance.bg_cover and g_file.bg_cover != instance.bg_cover:
                g_file.bg_cover.delete(False)
            if instance.bg_aboutus_img and g_file.bg_aboutus_img != instance.bg_aboutus_img:
                g_file.bg_aboutus_img.delete(False)
            if instance.aboutus_video and g_file.aboutus_video != instance.aboutus_video:
                g_file.aboutus_video.delete(False)
            if instance.bg_404 and g_file.bg_404 != instance.bg_404:
                g_file.bg_404.delete(False)
            if instance.bg_500 and g_file.bg_500 != instance.bg_500:
                g_file.bg_500.delete(False)
            