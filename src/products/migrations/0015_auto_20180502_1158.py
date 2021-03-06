# Generated by Django 2.0.3 on 2018-05-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20180502_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionaldropdown',
            name='additional_cost',
        ),
        migrations.AddField(
            model_name='additionaldropdown',
            name='additional_cost_nsw',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='additionaldropdown',
            name='additional_cost_qld',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='additionaldropdown',
            name='additional_cost_vic',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]
