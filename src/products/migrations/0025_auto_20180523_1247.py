# Generated by Django 2.0.5 on 2018-05-23 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20180522_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(help_text='Title for SEO', max_length=120),
        ),
    ]
