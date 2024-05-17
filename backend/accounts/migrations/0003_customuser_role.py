# Generated by Django 4.0 on 2024-05-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_company_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager')], default='MANAGER', help_text='Your role in the Company', max_length=10),
        ),
    ]
