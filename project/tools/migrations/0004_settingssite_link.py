# Generated by Django 5.0.6 on 2024-06-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_alter_settingssite_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingssite',
            name='link',
            field=models.URLField(blank=True, verbose_name='Link Website:'),
        ),
    ]