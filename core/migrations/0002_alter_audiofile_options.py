# Generated by Django 4.2.11 on 2024-10-29 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audiofile',
            options={'permissions': [('can_upload', 'Can upload files')]},
        ),
    ]