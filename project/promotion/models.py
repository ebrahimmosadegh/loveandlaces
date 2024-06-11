from django.db import models
from ckeditor.fields import RichTextField  # Import from ckeditor
from django.utils.text import slugify
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.html import format_html
from django.urls import reverse
from tools.views import unique_slug_generator
from tools.views import validate_image_extension, validate_video_extension

# Create your models here.

def upload_path(instance, filename):
    return f"promotion/{instance.id}/{filename}"

# Create your models here.
class Promotion(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date:")
    subtitle = models.CharField(blank=False, max_length=225, verbose_name="Subtitle:")
    title = models.CharField(blank=False, max_length=225, verbose_name="Title:")
    detail = models.TextField(blank=False, verbose_name="Detail:")
    subtitle_sec = models.CharField(blank=True, max_length=225, verbose_name="Subtitle Second:")
    title_sec = models.CharField(blank=True, max_length=225, verbose_name="Title Second:")
    detail_sec = models.TextField(blank=True, verbose_name="Detail Second:")
    image = models.ImageField(upload_to=upload_path, null=False, blank=False, validators=[validate_image_extension], verbose_name="Cover Image:", help_text="resulotion(1920*1000)")
    video = models.FileField(upload_to=upload_path, null=False, blank=False, validators=[validate_video_extension], verbose_name="Video:", help_text="resulotion(9*16 or 1080*1920)")
    slug = models.SlugField(blank=True, null=True, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("promotion", args=[self.slug])
    
    class Meta:
        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            saved_video = self.video
            self.image = None
            self.video = None
            super(Promotion, self).save(*args, **kwargs)
            self.image = saved_image
            self.video = saved_video
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super(Promotion, self).save(*args, **kwargs)
    
    def image_tag(self):
        return format_html("<img src='{}' width=150>".format(self.image.url))
    image_tag.short_description = 'cover image'

@receiver(pre_save, sender=Promotion)
def delete_old_file_Promotion(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
    if instance.pk:
        existing_video = Promotion.objects.get(pk=instance.pk)
        g_image = Promotion.objects.get(pk=instance.pk)
        if instance.video and existing_video.video != instance.video:
                existing_video.video.delete(False)
        if instance.image and g_image.image != instance.image:
            g_image.image.delete(False)

@receiver(pre_delete, sender=Promotion)
def Promotion_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
    instance.video.delete(False)