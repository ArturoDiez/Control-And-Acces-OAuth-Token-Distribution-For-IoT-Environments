# Generated by Django 3.0.3 on 2020-02-21 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0003_auto_20200221_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivo',
            old_name='grupo',
            new_name='grupoid',
        ),
    ]
