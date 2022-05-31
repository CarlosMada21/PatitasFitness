"""BackendDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from cgitb import html
from django.contrib import admin
from django.urls import path, include
from registro.views import *
from registro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name ="signin"),
    path('insertar/', insertar),
    path('', inicio, name="inicio"),
    path('buscar/', buscar),
    path('registro/', include('registro.urls')),
    path('logout/', views.logout, name = "logout"),
    path('configuracion/', views.configuracion, name = "configuracion"),
    path('membresias/', views.membresias, name = "membresias"),
    path('citas/', views.citas, name = "citas"),
    path('eliminacion_cuenta/', views.eliminar, name = "eliminar"),
    path('editar_usuario/', views.editar_usuario, name = "editar_usuario"),
    path('editar/', editar),
    path('catalogo/', views.catalogo, name = "catalogo"),
    path('insertar_cita/', views.insertar_cita),
    path('signin_cita/', views.signin_cita, name ="signin_cita"),
    path('detalles_cuenta/', views.detalles_cuenta, name ="detalles_cuenta"),
    path('formas_de_pago/', views.formas_de_pago, name ="formas_de_pago"),
    path('direcciones/', views.direcciones, name ="direcciones"),
    path('agregar_datos_bancarios/', views.agregar_datos_bancarios, name ="agregar_datos_bancarios"),
    path('insertar_datos_bancarios/', views.insertar_datos_bancarios, name ="insertar_datos_bancarios"),
    path('eliminar_tarjeta/', views.eliminar_tarjeta, name ="eliminar_tarjeta"),
    path('editar_direcciones/', views.editar_direcciones, name ="editar_direcciones"),
    path('insertar_direccion/', views.insertar_direccion, name ="insertar_direccion"),
    path('eliminar_direccion/', views.eliminar_direccion, name ="eliminar_direccion"),
    
    
]
