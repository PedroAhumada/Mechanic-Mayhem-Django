# Generated by Django 5.0.4 on 2024-05-26 00:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_empleado_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubirProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('nombre_mecanico', models.CharField(max_length=60)),
                ('valor', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=150)),
                ('nombre_cliente', models.CharField(max_length=60)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categorias')),
            ],
        ),
    ]
