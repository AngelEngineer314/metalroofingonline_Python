# Generated by Django 2.0.5 on 2018-06-19 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_auto_20180612_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title']},
        ),
    ]