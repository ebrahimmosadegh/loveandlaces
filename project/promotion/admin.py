from django.contrib import admin
from .models import Promotion

# Register your models here.
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'image_tag']
    list_per_page = 10

    class Meta:
        model = Promotion
    
admin.site.register(Promotion, PromotionAdmin)