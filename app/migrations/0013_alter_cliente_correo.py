# Generated by Django 4.0.7 on 2022-09-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_nombre_tipolicor_tipolicor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
    ]
