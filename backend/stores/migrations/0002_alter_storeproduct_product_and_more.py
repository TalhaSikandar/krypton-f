# Generated by Django 4.0 on 2024-05-21 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='storeproduct',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
