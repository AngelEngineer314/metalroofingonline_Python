# Generated by Django 2.0.5 on 2019-05-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='billing_profile',
        ),
        migrations.AddField(
            model_name='address',
            name='phone_number',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line_1',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('billing', 'Billing address'), ('shipping', 'Shipping address')], default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='Australia', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='first_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='last_name',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.IntegerField(default='0', error_messages={'invalid': 'Please Enter Australian Postal Code'}),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(default='', max_length=120),
        ),
    ]
