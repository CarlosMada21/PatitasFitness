from concurrent.futures.process import _ExceptionWithTraceback
from xmlrpc.client import Boolean
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from registro.models import usuario
from django.shortcuts import redirect
from django.db.utils import IntegrityError
from datetime import date
# from django.conf import USUARIO
# from BackendDjango.settings import LOGIN
# from BackendDjango import settings
from django.conf import settings
#from django.template.loader import get_template




def login(request):
    
    #cargador = get_template('login.html')
    #plantillaLogin=cargador.render()
    return render(request, "login.html")

def signin(request):
    
    return render(request, "signin.html")

def redireccionar_login(request):
    return redirect(login)

def buscar(request):
    mensaje=""
    email=request.GET['correo']
    acceso_denegado = False
    
    try:
        usr = usuario.objects.get(email=email)
        settings.USUARIO.nombre = usr.nombre
        settings.USUARIO.apellido = usr.apellido
        settings.USUARIO.password = usr.password
        settings.USUARIO.email = usr.email
        settings.USUARIO.telefono = usr.telefono
        settings.USUARIO.fecha_nac = usr.fecha_nac
        settings.USUARIO.inscripcion = usr.inscripcion
        settings.USUARIO.mensualidad = usr.mensualidad
        
        print(settings.USUARIO.password)
        print(request.GET["contrasenia"])

        if((settings.USUARIO.password)==request.GET["contrasenia"]):
            settings.LOGIN = True            
            return render(request, "index.html")
        else:
            acceso_denegado = True
            mensajeError="Contraseña incorrecta, inténtalo de nuevo."
            return render(request, "signin.html", {"mensaje":mensajeError, "acceso_denegado": acceso_denegado})
        
    except usuario.DoesNotExist as e:
        #print(type(e))
        #print(e)
        acceso_denegado = True
        mensajeError="Parece que aún no tienes una cuenta con este correo electrónico."
        return render(request, "signin.html", {"mensaje":mensajeError, "acceso_denegado": acceso_denegado})

def insertar(request):

    insertado=False
    logeado=False

    usr = usuario(email = request.GET["correo"], 
        password = request.GET["contrasenia"],
        nombre = request.GET["nombre"],
        apellido = request.GET["apellido"],
        telefono = request.GET["telefono"],
        fecha_nac = request.GET["anio"] + "-" + request.GET["mes"] + "-" + request.GET["dia"]
    )

    try:
        usr.save()
        settings.USUARIO.nombre = usr.nombre
        settings.USUARIO.apellido = usr.apellido
        settings.USUARIO.password = usr.password
        settings.USUARIO.email = usr.email
        settings.USUARIO.telefono = usr.telefono
        settings.USUARIO.fecha_nac = usr.fecha_nac

        insertado=True
        settings.LOGIN=True
        return render(request, "index.html", {"insertado":insertado})

    except Exception as e:
        if type(e) == IntegrityError:
            insertado=False
            #print(type(e))
            #print(e)
            return render(request, "login.html", {"insertado":insertado})
        else:
            print(type(e))
            print(e)
            return render(request, "index.html")
            
def inicio(request):
    return render(request, "index.html")

def logout(request):
    settings.LOGIN = False
    settings.USUARIO.nombre = ""
    settings.USUARIO.apellido = ""
    settings.USUARIO.password = ""
    settings.USUARIO.email = ""
    settings.USUARIO.telefono = ""
    settings.USUARIO.fecha_nac = date(1, 1, 1)
    return render(request, "index.html")