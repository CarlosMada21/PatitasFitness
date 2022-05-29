from concurrent.futures.process import _ExceptionWithTraceback
from xmlrpc.client import Boolean
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from registro.models import usuario
from django.shortcuts import redirect
from django.db.utils import IntegrityError
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
    usuario_permitido=False
    logeado=False
    mensaje=""
    email=request.GET['correo']
    
    try:
        usr = usuario.objects.get(email=email)
        
        if((usr.password)==request.GET["contrasenia"]):
            logeado = True
            
            return render(request, "index.html", {"logeado": logeado, "nombre":usr.nombre})
        else:
            mensajeError="Contraseña incorrecta, inténtalo de nuevo."
            return render(request, "signin.html", {"usuario_permitido":usuario_permitido, "mensaje":mensajeError})
        
    except usuario.DoesNotExist as e:
        #print(type(e))
        #print(e)
        mensajeError="Parece que aún no tienes una cuenta con este correo electrónico."
        return render(request, "signin.html", {"usuario_permitido":usuario_permitido, "mensaje":mensajeError})

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
        insertado=True
        logeado=True
        return render(request, "index.html", {"insertado":insertado, "logeado": logeado, "nombre":usr.nombre})

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
    logeado=False
    return render(request, "index.html", {"logeado": logeado})