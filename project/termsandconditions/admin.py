from django.contrib import admin
from django.db import models  # Import models from django
from .models import termsAndConditions
from ckeditor.widgets import CKEditorWidget  # Import from ckeditor

class termsAndConditionsAdmin(admin.ModelAdmin):  # Use the regular ModelAdmin
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(termsAndConditions, termsAndConditionsAdmin)