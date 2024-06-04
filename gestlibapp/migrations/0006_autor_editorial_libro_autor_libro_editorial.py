# Generated by Django 5.0.4 on 2024-06-04 11:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestlibapp', '0005_cliente_cedula_cliente_libro_alter_cliente_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='nombre')),
                ('apellido', models.CharField(max_length=20, null=True, verbose_name='apellido')),
                ('nacionalidad', models.CharField(max_length=20, null=True, verbose_name='nacionalidad')),
            ],
        ),
        migrations.CreateModel(
            name='editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='nombre')),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestlibapp.autor'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestlibapp.editorial'),
        ),
    ]
