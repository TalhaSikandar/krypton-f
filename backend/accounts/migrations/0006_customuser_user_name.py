# Generated by Django 4.0 on 2024-05-18 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_name',
            field=models.CharField(default='krypton_user', max_length=255),
        ),
    ]
