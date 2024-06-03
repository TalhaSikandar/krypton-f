# Generated by Django 4.0 on 2024-06-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierrawmaterial',
            name='quantity',
        ),
        migrations.AddField(
            model_name='supplierrawmaterial',
            name='available_quantity',
            field=models.IntegerField(blank=True, default=0, help_text='available quantity supplier has', null=True),
        ),
        migrations.AddField(
            model_name='supplierrawmaterial',
            name='unit_weight',
            field=models.CharField(choices=[('NORMAL', 'Normal'), ('KG', 'Kilogram'), ('CM', 'Centimeter'), ('LITRE', 'Litre')], default='NORMAL', help_text='Enter the measuring unit', max_length=10),
        ),
    ]
