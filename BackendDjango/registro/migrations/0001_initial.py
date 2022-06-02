# Generated by Django 4.0.4 on 2022-06-02 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
                ('fecha', models.DateField(null=True)),
                ('servicio', models.CharField(max_length=255, null=True)),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='datos_bancarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_tarjeta', models.CharField(max_length=16, null=True, unique=True)),
                ('mes_vencimiento', models.CharField(max_length=2, null=True)),
                ('anio_vencimiento', models.CharField(max_length=2, null=True)),
                ('cvv', models.CharField(max_length=3, null=True)),
                ('banco', models.CharField(max_length=25, null=True)),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=150)),
                ('num_ext', models.CharField(max_length=4, null=True)),
                ('num_int', models.CharField(max_length=4, null=True)),
                ('colonia', models.CharField(max_length=150)),
                ('cp', models.CharField(max_length=5, null=True)),
                ('alcaldia', models.CharField(max_length=150)),
                ('referencia', models.CharField(max_length=255)),
                ('entre_calles', models.CharField(max_length=255)),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ingreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True)),
                ('id_producto', models.IntegerField()),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('fecha_nac', models.DateField(null=True)),
                ('raza', models.CharField(max_length=255)),
                ('id_usuario', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(null=True, upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('apellido', models.CharField(max_length=100, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('fecha_nac', models.DateField(null=True)),
                ('mensualidad', models.BooleanField(default='False', null=True)),
                ('inscripcion', models.BooleanField(default='False', null=True)),
            ],
        ),
    ]
