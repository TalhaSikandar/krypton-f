# Generated by Django 4.0 on 2024-06-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrawmaterial',
            name='quantity',
        ),
        migrations.AddField(
            model_name='productrawmaterial',
            name='required_quantity',
            field=models.IntegerField(blank=True, default=0, help_text='raw material required to make the product'),
        ),
        migrations.AddField(
            model_name='productrawmaterial',
            name='unit_weight',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('KG', 'Kilogram'), ('CM', 'Centimeter'), ('LITRE', 'Litre')], default='NORMAL', help_text='Enter the measuring weight', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='raw_materials',
            field=models.ManyToManyField(blank=True, related_name='products', through='products.ProductRawmaterial', to='raw_materials.Rawmaterial'),
        ),
    ]
