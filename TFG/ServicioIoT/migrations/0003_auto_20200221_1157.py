# Generated by Django 3.0.3 on 2020-02-21 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServicioIoT', '0002_dispositivo_propietario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ServicioIoT.GrupoDispositivo'),
        ),
    ]
