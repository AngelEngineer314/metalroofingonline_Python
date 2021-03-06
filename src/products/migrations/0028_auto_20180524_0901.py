# Generated by Django 2.0.5 on 2018-05-23 23:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20180524_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(default='Default', verbose_name='Content'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='more_info',
            field=tinymce.models.HTMLField(default='default', verbose_name='Content'),
            preserve_default=False,
        ),
    ]
