# Generated by Django 4.0.7 on 2022-09-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_empleado_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='cedula',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='correo',
            field=models.EmailField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='telefono',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
