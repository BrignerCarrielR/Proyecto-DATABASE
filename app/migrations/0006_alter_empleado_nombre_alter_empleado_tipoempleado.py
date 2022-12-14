# Generated by Django 4.0.7 on 2022-09-06 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tipoEmpleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.tipoempleado'),
        ),
    ]
