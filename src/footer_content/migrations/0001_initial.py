# Generated by Django 2.0.5 on 2018-12-18 13:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.CharField(max_length=120)),
                ('meta_title', models.CharField(blank=True, max_length=120, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=120, null=True)),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
            ],
        ),
    ]
