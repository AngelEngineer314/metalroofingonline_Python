# Generated by Django 2.1.7 on 2020-08-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200825_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='length',
            field=models.DecimalField(decimal_places=4, default=0.0, max_digits=200),
        ),
    ]