# Generated by Django 4.0 on 2024-06-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_remove_supplierrawmaterial_unit_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplierrawmaterial',
            name='available_quantity',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='available quantity supplier has', null=True),
        ),
    ]
