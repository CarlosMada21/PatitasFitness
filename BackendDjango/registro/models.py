from django.db import models
import psycopg2 as Database

# Create your models here.
# -- coding: UTF8 --

# Create your models here.

class usuario(models.Model):
    email=models.EmailField(unique=True, null=False)
    password=models.CharField(max_length=20, null=True)
    nombre=models.CharField(max_length=100, null=True)
    apellido=models.CharField(max_length=100, null=True)
    telefono=models.CharField(max_length=10, null=True)
    fecha_nac=models.DateField(null=True)
    mensualidad=models.BooleanField(null=True, default='False')
    inscripcion=models.BooleanField(null=True, default='False')
    
class producto(models.Model):
    nombre=models.CharField(max_length=255, null=True)
    descripcion=models.CharField(max_length=100, null=True)
    precio=models.FloatField()
    imagen=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True)
    
class datos_bancarios(models.Model):
    num_tarjeta=models.CharField(max_length=16, null=True, unique=True)
    mes_vencimiento=models.CharField(max_length=2, null=True)
    anio_vencimiento=models.CharField(max_length=2, null=True)
    cvv=models.CharField(max_length=3, null=True)
    banco=models.CharField(max_length=25, null=True)
    id_usuario=models.IntegerField(null=False)

class cita(models.Model):
    hora=models.TimeField(auto_now=False, auto_now_add=False)
    fecha=models.DateField(null=True)
    servicio=models.CharField(max_length=255, null=True)
    id_usuario=models.IntegerField(null=False)
    
class direccion(models.Model):
    calle=models.CharField(max_length=150, null=False)
    num_ext=models.CharField(max_length=4, null=True)
    num_int=models.CharField(max_length=4, null=True)
    colonia=models.CharField(max_length=150, null=False)
    cp=models.CharField(max_length=5, null=True)
    alcaldia=models.CharField(max_length=150, null=False)
    referencia=models.CharField(max_length=255, null=False)
    entre_calles=models.CharField(max_length=255, null=False)
    id_usuario=models.IntegerField(null=False)

class mascota(models.Model):
    nombre=models.CharField(max_length=255, null=True)
    fecha_nac=models.DateField(null=True)    
    raza=models.CharField(max_length=255, null=False)
    id_usuario=models.IntegerField(null=False)
    
class ingreso(models.Model):
    fecha=models.DateField(null=True)    
    id_producto=models.IntegerField(null=False)
    id_usuario=models.IntegerField(null=False)