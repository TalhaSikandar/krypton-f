# Generated by Django 4.0 on 2024-06-08 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('stores', '0005_alter_storeproduct_available_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stores', to='accounts.customuser'),
        ),
    ]
