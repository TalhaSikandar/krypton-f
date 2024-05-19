# Generated by Django 4.0 on 2024-05-19 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('raw_materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Product Name', max_length=200)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'products',
                'ordering': ['product_name'],
            },
        ),
        migrations.CreateModel(
            name='ProductRawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='raw_materials.rawmaterial')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='raw_materials',
            field=models.ManyToManyField(blank=True, related_name='products', through='products.ProductRawMaterial', to='raw_materials.Rawmaterial'),
        ),
    ]
