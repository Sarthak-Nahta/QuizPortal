# Generated by Django 3.1.2 on 2020-11-12 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='max_score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
