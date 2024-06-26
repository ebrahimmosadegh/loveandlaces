from django.contrib import admin
# Register your models here.
from .models import ContactUs

class ContactAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'email', 'subject', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'text']


admin.site.register(ContactUs, ContactAdmin)