# Generated by Django 3.2 on 2021-04-18 17:58

from django.db import migrations, models
import eshop_settings.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_settings', '0002_sitesetting_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_settings.models.upload_image_path, verbose_name='تصویر لوگوی سایت'),
        ),
    ]