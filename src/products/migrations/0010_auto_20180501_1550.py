# Generated by Django 2.0.3 on 2018-05-01 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_additionaldropdown_additionaldropdownoption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionaldropdown',
            name='AdditionalDropDown',
        ),
        migrations.RemoveField(
            model_name='additionaldropdownoption',
            name='option',
        ),
    ]