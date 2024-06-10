from django.contrib import admin

from .models import FlowerWall, Gallery

# Register your models here.

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 0


class FlowerWallAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'image_tag']
    inlines = [GalleryInline]
    list_per_page = 10

    class Meta:
        model = FlowerWall
    


admin.site.register(FlowerWall, FlowerWallAdmin)
