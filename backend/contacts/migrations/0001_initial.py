# Generated by Django 4.0 on 2024-05-19 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(help_text='Enter City', max_length=50)),
                ('country', models.CharField(help_text='Enter Country', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
                'ordering': ['country'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(blank=True, help_text='Enter contact no', max_length=11, null=True)),
                ('email', models.EmailField(help_text='Enter email', max_length=254)),
                ('website', models.URLField(blank=True, default='', help_text='Enter your website url', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'ordering': ['contact_no'],
            },
        ),
    ]
