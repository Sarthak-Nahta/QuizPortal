# Generated by Django 3.1.3 on 2020-11-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201123_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='captcha',
            name='captcha_input',
            field=models.CharField(max_length=10),
        ),
    ]
