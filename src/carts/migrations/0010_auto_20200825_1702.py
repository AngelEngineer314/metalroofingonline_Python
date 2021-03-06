# Generated by Django 2.1.7 on 2020-08-25 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_auto_20200825_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='additional_drop_down',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.AdditionalDropDown'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carts.Cart'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_colour',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Colour'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_length',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Length'),
        ),
    ]
