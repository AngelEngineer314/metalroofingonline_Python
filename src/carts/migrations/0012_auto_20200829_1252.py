# Generated by Django 2.1.7 on 2020-08-29 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0011_auto_20200825_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=4, default=0.0, max_digits=100, null=True),
        ),
    ]
