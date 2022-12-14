# Generated by Django 4.0.7 on 2022-09-07 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_empleado_tipoempleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('ruc', models.CharField(max_length=10, null=True, unique=True)),
                ('telefono', models.CharField(max_length=10, null=True, unique=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['id'],
            },
        ),
    ]
