# Generated by Django 2.0.5 on 2018-05-22 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_auto_20180522_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.CharField(default='default', help_text='Description for SEO', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default='default', help_text='Title for SEO)', max_length=120),
            preserve_default=False,
        ),
    ]
