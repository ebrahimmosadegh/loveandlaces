from django.db import models
from ckeditor.fields import RichTextField  # Import from ckeditor
# Create your models here.
class termsAndConditions(models.Model):
    content = RichTextField(null=True)  # <-- here