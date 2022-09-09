# Generated by Django 4.0.7 on 2022-09-07 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_licor_tipolicor_alter_tipolicor_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, unique=True)),
                ('stock', models.IntegerField(default=0)),
                ('precio', models.FloatField(null=True)),
                ('tipoLicor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipolicor')),
            ],
            options={
                'verbose_name': 'Licor',
                'verbose_name_plural': 'Licores',
                'ordering': ['id'],
            },
        ),
    ]