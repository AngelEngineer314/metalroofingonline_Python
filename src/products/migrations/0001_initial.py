# Generated by Django 2.0.3 on 2018-04-23 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoryOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Accessory')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(blank=True, max_length=120, null=True)),
                ('additional_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ColourOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Colour')),
            ],
        ),
        migrations.CreateModel(
            name='Length',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LengthOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Length')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('vic_title', models.CharField(blank=True, max_length=120, null=True)),
                ('nsw_title', models.CharField(blank=True, max_length=120, null=True)),
                ('qld_title', models.CharField(blank=True, max_length=120, null=True)),
                ('vic_supplier_title', models.CharField(blank=True, max_length=120, null=True)),
                ('nsw_supplier_title', models.CharField(blank=True, max_length=120, null=True)),
                ('qld_supplier_title', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('more_info', models.TextField(blank=True, null=True)),
                ('vic_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('nsw_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('qld_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('vic_price_per_mm', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('nsw_price_per_mm', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('qld_price_per_mm', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('youtube_embed_link', models.TextField(blank=True, null=True)),
                ('from_supplier', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='lengthoption',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
        migrations.AddField(
            model_name='colouroption',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
        migrations.AddField(
            model_name='categoryoption',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
        migrations.AddField(
            model_name='accessoryoption',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='accessory',
            field=models.ForeignKey(blank=True, max_length=120, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
