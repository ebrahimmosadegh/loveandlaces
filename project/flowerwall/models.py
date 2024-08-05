from django.db import models
from ckeditor.fields import RichTextField  # Import from ckeditor
from django.utils.text import slugify
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.html import format_html
from django.urls import reverse
from tools.views import unique_slug_generator
from tools.views import validate_image_extension , validate_video_extension

# Create your models here.

def upload_image_path(instance, filename):
    return f"Flowerwall/{instance.id}/{filename}"

def upload_image_gallery_path(instance, filename):
    return f"Flowerwall/{instance.flowerwall_id}/{filename}"

class FlowerWall(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date:")
    title = models.CharField(max_length=225, verbose_name="Title:")
    image = models.ImageField(upload_to=upload_image_path, null=False, blank=False, validators=[validate_image_extension], verbose_name="Cover Image:", help_text="resulotion(600*800)")
    video = models.FileField(upload_to=upload_image_path, null=True, blank=True, validators=[validate_video_extension], verbose_name="Video:", help_text="resulotion(9*16 or 1080*1920)")
    content = RichTextField(null=True)  # <-- here
    slug = models.SlugField(blank=True,null=True, unique=True, db_index=True)

    def get_absolute_url(self):
        return reverse("flowerwall", args=[self.slug])
    
    class Meta:
        verbose_name = 'FlowerWall'
        verbose_name_plural = 'Flower Walls'

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.id is None:
            saved_image = self.image
            saved_video = self.video
            self.image = None
            self.video = None
            super(FlowerWall, self).save(*args, **kwargs)
            self.image = saved_image
            self.video = saved_video
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        super(FlowerWall, self).save(*args, **kwargs)
    
    def image_tag(self):
        return format_html("<img src='{}' width=150>".format(self.image.url))
    image_tag.short_description = 'cover image'

@receiver(pre_save, sender=FlowerWall)
def delete_old_file_flowerwall(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        
    if instance.pk:
        g_image = FlowerWall.objects.get(pk=instance.pk)
        if instance.image and g_image.image != instance.image:
            g_image.image.delete(False)
        if instance.video and g_image.video != instance.video:
            g_image.video.delete(False)

@receiver(pre_delete, sender=FlowerWall)
def FlowerWall_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)
    instance.video.delete(False)


class Gallery(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date:")
    image = models.ImageField(upload_to=upload_image_gallery_path, null=True, blank=True, validators=[validate_image_extension], verbose_name="Gallery Image:", help_text="resulotion(600*800)")
    flowerwall = models.ForeignKey(FlowerWall, on_delete=models.CASCADE, verbose_name='flowerwall:')

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery Flower Wall'
    

@receiver(pre_save, sender=Gallery)
def delete_old_gallery(sender, instance, *args, **kwargs):
    if instance.pk:
            exi_image = Gallery.objects.get(pk=instance.pk)
            if instance.image and exi_image.image != instance.image:
                exi_image.image.delete(False)

@receiver(pre_delete, sender=Gallery)
def Gallery_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)