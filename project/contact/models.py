from django.db import models

# Create your models here.
class ContactUs(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date:")
    name = models.CharField(max_length=100, verbose_name='Name:')
    phone = models.CharField(max_length=100, verbose_name='Phone:')
    email = models.EmailField(max_length=100, verbose_name='Email:')
    subject = models.CharField(max_length=200, verbose_name='عنوان پیام')
    text = models.TextField(verbose_name='متن پیام')
    is_read = models.BooleanField(verbose_name='has been read')

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'contact Users'

    def __str__(self):
        return self.subject