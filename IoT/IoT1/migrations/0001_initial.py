# Generated by Django 3.0.3 on 2020-05-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('private_key', models.CharField(default='----', max_length=5000)),
                ('token', models.CharField(default='Esto no es un token', max_length=100)),
                ('datos', models.CharField(default='Datos del dispositivo', max_length=10000)),
            ],
        ),
    ]