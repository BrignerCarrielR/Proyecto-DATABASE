# Generated by Django 4.0.7 on 2022-09-07 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_licor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipolicor',
            old_name='nombre',
            new_name='tipoLicor',
        ),
    ]
