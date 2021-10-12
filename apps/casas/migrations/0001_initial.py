# Generated by Django 3.2.8 on 2021-10-12 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('identificacion', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=60)),
                ('barrio', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('En reconstruccion', 'En reconstruccion'), ('Por terminar', 'Por terminar'), ('Terminada', 'Terminada')], default='En reconstruccion', max_length=30)),
                ('imagen_inicial', models.ImageField(upload_to='imagen_inicial')),
                ('imagen_final', models.ImageField(blank=True, null=True, upload_to='imagen_final')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='casas.propietario')),
            ],
        ),
    ]
