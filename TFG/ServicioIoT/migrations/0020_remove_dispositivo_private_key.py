# Generated by Django 3.0.3 on 2020-05-30 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0019_auto_20200528_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivo',
            name='private_key',
        ),
    ]
