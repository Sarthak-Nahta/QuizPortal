# Generated by Django 3.1.2 on 2020-11-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201123_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='captcha_img',
            field=models.ImageField(upload_to='captcha_images'),
        ),
    ]