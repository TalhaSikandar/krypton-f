# Generated by Django 4.0 on 2024-06-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raw_materials', '0002_rawmaterial_description_rawmaterial_unit_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='rawmaterial',
            name='price',
            field=models.PositiveIntegerField(default=0, help_text='enter price per unit'),
        ),
    ]
