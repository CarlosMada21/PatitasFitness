from calendar import c
from concurrent.futures.process import _ExceptionWithTraceback
# from tkinter import NE
from xmlrpc.client import Boolean
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context
from registro.models import *
from django.shortcuts import redirect
from django.db.utils import IntegrityError
import datetime
# from django.conf import USUARIO
# from BackendDjango.settings import LOGIN
# from BackendDjango import settings
from django.conf import settings
#from django.template.loader import get_template
from django.contrib import messages


def login(request):
    
    return render(request, "login.html")

def signin(request):
    
    return render(request, "signin.html")

def signin_cita(request):
    cita=True
    return render(request, "signin.html", {"cita":cita})

def redireccionar_login(request):
    return redirect(login)

def buscar(request):
    mensajeError=""
    email=request.GET['correo']
    acceso_denegado = False
    
    try:
        usr = usuario.objects.get(email=email)
        request.session['usr_id'] = usr.id

        if((usr.password)==request.GET["contrasenia"]):
            
            usr = usuario.objects.get(id=request.session.get('usr_id'))
            usr.login = True
            nombre=usr.nombre
            login=usr.login
            return render(request, "index.html", {'nombre': nombre, 'login':login})
        else:
            acceso_denegado = True
            mensajeError="Contraseña incorrecta, inténtalo de nuevo."
            return render(request, "signin.html", {"mensaje":mensajeError, "acceso_denegado": acceso_denegado})
        
    except usuario.DoesNotExist as e:
        acceso_denegado = True
        mensajeError="Parece que aún no tienes una cuenta con este correo electrónico."
        return render(request, "signin.html", {"mensaje":mensajeError, "acceso_denegado": acceso_denegado})

def insertar(request):

    insertado=False

    usr = usuario(email = request.GET["correo"], 
        password = request.GET["contrasenia"],
        nombre = request.GET["nombre"],
        apellido = request.GET["apellido"],
        telefono = request.GET["telefono"],
        fecha_nac = request.GET["anio"] + "-" + request.GET["mes"] + "-" + request.GET["dia"],
        login=True
    )

    try:
        usr.save()
        request.session['usr_id'] = usr.id
        
        return redirect('inicio')
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
    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        nombre=usr.nombre
        login=usr.login
        return render(request, "index.html", {'nombre': nombre, 'login':login})
    
    except Exception:
        return render(request, 'index.html', {"login":False})
    
def logout(request):
    try:
        request.session['usr_id']=0
        return render(request, 'index.html', {"login": False})
    except KeyError:
        print('No pudimos cerrar la sesión')
        return render(request, 'index.html', {"login": False})

def configuracion(request):
    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        nombre=usr.nombre
        login=usr.login
        return render(request, "configuracion.html", {'nombre': nombre, 'login':login})
    
    except Exception:
        return render(request, 'index.html', {"login":False})

def membresias(request):
    return render(request, "membresias.html")

def citas(request):
    
    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        nombre=usr.nombre
        login=usr.login
        return render(request, "citas.html", {'nombre': nombre, 'login':login})
    
    except Exception:
        return render(request, 'index.html', {"login":False})

def eliminar(request):
    eliminado=False
    mensaje = ""
    
    try:
        borrar_usr = usuario.objects.get(id=request.session.get('usr_id'))
        borrar_usr.delete()
        eliminado = True
        request.session['usr_id'] = 0
        return render(request, 'index.html', {"login": False})
    except Exception as e:
        if type(e) == usuario.DoesNotExist:
            mensaje="Ha ocurrido un problema al obtener tu usuario. Intenta más tarde."
            return render(request, "configuracion.html", {"eliminado": eliminado, "mensaje":mensaje})
        else:
            print(type(e))
            print(e)
            mensaje="Ha ocurrido un error inesperado"
            return render(request, "configuracion.html", {"eliminado": eliminado, "mensaje":mensaje})
        
def catalogo(request):
    try:
        if request.session.get('usr_id') != 0:
            usr = usuario.objects.get(id=request.session.get('usr_id'))
            return render(request, "catalogo.html", {"login":True, "nombre":usr.nombre})
        else:
            return render(request, "catalogo.html", {"login":False})
    except Exception:
        return render(request, "index.html", {"login":False})
     
def insertar_cita(request):
    fecha_hora=request.POST["fecha_hora"]
    fecha=fecha_hora[6]+fecha_hora[7]+fecha_hora[8]+fecha_hora[9]+"-"+fecha_hora[0]+fecha_hora[1]+"-"+fecha_hora[3]+fecha_hora[4]
    hora=fecha_hora[11]+fecha_hora[12]+fecha_hora[14]+fecha_hora[15]+fecha_hora[17]+fecha_hora[18]
    
    d = datetime.time(int(fecha_hora[11] + fecha_hora[12]), int(fecha_hora[14]+fecha_hora[15]), int(fecha_hora[17]+fecha_hora[18]))
    
    servicio=request.POST["servicio"]
    id_usuario=request.session.get('usr_id')
    cita_agendada=False
    cita_no_agendada=False
    
    cita_solicitada = cita(hora = d, 
        fecha= fecha,
        servicio = servicio,
        id_usuario = id_usuario
    )
    try:
        cita_solicitada.save()
        cita_agendada = True
        mensaje="Cita agendada a las " + hora[0] + hora[1] + ":" + hora[2] + hora[3] + ":" + hora[4] + hora[5] + " del " + fecha
        return render(request, "citas.html", {"mensaje":mensaje, "cita_agendada": cita_agendada})
    
    except Exception:
        cita_no_agendada=True
        mensaje="No se pudo agendar tu cita"
        return render(request, "citas.html", {"mensaje":mensaje, "cita_no_agendada": cita_no_agendada})
    
#Función para reiniciar variables globales
def reset_globals():
    settings.LOGIN = False
    settings.USUARIO.nombre = ""
    settings.USUARIO.apellido = ""
    settings.USUARIO.password = ""
    settings.USUARIO.email = ""
    settings.USUARIO.telefono = ""
    settings.USUARIO.fecha_nac = datetime(1, 1, 1)
    settings.USUARIO.id = 0

def editar_usuario(request):
    # fecha =  settings.USUARIO.fecha_nac.strftime("%Y-%m-%d")
    # print(fecha)
    # dia = fecha[8:9]
    # mes = fecha[5:6]
    # anio = fecha[0:3]
    # print(dia + mes + anio)
    
    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        anio = usr.fecha_nac.strftime("%Y")
        mes = usr.fecha_nac.strftime("%m")
        dia = usr.fecha_nac.strftime("%d")
        nombre=usr.nombre
        apellido=usr.apellido
        password=usr.password
        telefono=usr.telefono
        login=usr.login
        return render(request, "editar_usuario.html", {"dia": dia, "mes": mes, "anio": anio, "nombre":nombre, "apellido":apellido, "telefono":telefono, "password":password, "login":login})
    
    except Exception:
        
        return render(request, 'index.html', {"login": False})
        
def editar(request):

    mensaje = ""
    cambiado = False

    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        
        usr.nombre = request.GET["nombre_e"]
        usr.apellido = request.GET["apellido_e"]
        usr.fecha_nac = request.GET["anio_e"] + "-" + request.GET["mes_e"] + "-" + request.GET["dia_e"]
        usr.telefono = request.GET["telefono_e"]
        usr.password = request.GET["password_e"]
        
        usr.save()
        
        # date(request.GET["anio_e"], request.GET["mes_e"], request.GET["dia_e"])

        mensaje = "Los datos han sido cambiado con éxito"
        cambiado = True
        return render(request, "index.html", {"mensaje_e": mensaje, "cambiado": cambiado, "login":True})

    except Exception as e:
        if type(e) == IntegrityError:
            cambiado = False
            mensaje = "Ocurrió un problema, vuelve a intentarlo"
            return render(request, "editar_usuario.html", {"mensaje_e": mensaje, "cambiado": cambiado})
        else:
            return render(request, "index.html", {"login": False})

def detalles_cuenta(request):
    # fecha =  settings.USUARIO.fecha_nac.strftime("%Y-%m-%d")
    '''
    anio = settings.USUARIO.fecha_nac.strftime("%Y")
    mes = settings.USUARIO.fecha_nac.strftime("%m")
    dia = settings.USUARIO.fecha_nac.strftime("%d")
    id=request.session.get('usr_id')
    nombre=request.session.get('usr_nombre')
    apellido=request.session.get('usr_apellido')
    email=request.session.get('usr_email')
    login=request.session.get('usr_login')
    password=request.session.get('usr_password')
    telefono=request.session.get('usr_tel')
    dia_nac=request.session.get('usr_dia_nac')
    mes_nac=request.session.get('usr_mes_nac')
    anio_nac=request.session.get('usr_anio_nac')'''
    try:
        usr = usuario.objects.get(id=request.session.get('usr_id'))
        anio = usr.fecha_nac.strftime("%Y")
        mes = usr.fecha_nac.strftime("%m")
        dia = usr.fecha_nac.strftime("%d")
        nombre=usr.nombre
        apellido=usr.apellido
        email=usr.email
        telefono=usr.telefono
        login=usr.login
        return render(request, "detalles_cuenta.html", {"dia": dia, "mes": mes, "anio": anio, "nombre":nombre, "apellido":apellido, "telefono":telefono, "email":email, "login":login})

    except Exception:
        
        return render(request, 'index.html', {"login": False})
    
def formas_de_pago(request):

    lista_tarjetas = recuperar_tarjetas(request)
    return render(request, "formas_de_pago.html", {"lista_tarjetas": lista_tarjetas})

def direcciones(request):

    lista_direcciones = recuperar_direcciones(request)
    return render(request, "direcciones.html", {"lista_direcciones": lista_direcciones})

def agregar_datos_bancarios(request):
    return render(request, "agregar_datos_bancarios.html")

def insertar_datos_bancarios(request):

    tarjeta_guardada = False

    numTarjeta = request.GET["num_tarjeta"]
    mes_v = request.GET["mes_v"]
    anio_v = request.GET["anio_v"]
    cvv = request.GET["cvv"]
    banco = request.GET["banco"]
    id_usuario = request.session.get('usr_id')

    nueva_tarjeta = datos_bancarios(
        num_tarjeta= numTarjeta,
        mes_vencimiento = mes_v,
        anio_vencimiento = anio_v,
        cvv = cvv,
        banco = banco,
        id_usuario = id_usuario,
        )

    try:
        nueva_tarjeta.save()
        tarjeta_guardada = True
        lista_tarjetas = recuperar_tarjetas(request)
        return render(request, "formas_de_pago.html", {"tarjeta_guardada": tarjeta_guardada, "lista_tarjetas": lista_tarjetas})

    except Exception:
        no_hay_tarjeta = True
        lista_tarjetas = recuperar_tarjetas(request)
        return render(request, "formas_de_pago.html", {"no_hay_tarjeta": no_hay_tarjeta, "lista_tarjetas": lista_tarjetas})

def recuperar_tarjetas(request):
    lista_tarjetas = datos_bancarios.objects.filter(id_usuario = request.session.get('usr_id'))
    return lista_tarjetas

def recuperar_citas(request):
    lista_citas = cita.objects.filter(id_usuario = request.session.get('usr_id'))
    return lista_citas

def eliminar_tarjeta(request):
    eliminada = False

    tarjeta_seleccionada = request.GET["tarjeta_seleccionada"]

    try:
        borrar_tarjeta = datos_bancarios.objects.get(num_tarjeta=tarjeta_seleccionada)
        borrar_tarjeta.delete()
        eliminada = True
        lista_tarjetas = recuperar_tarjetas(request)
        return render(request, "formas_de_pago.html", {"eliminada": eliminada, "lista_tarjetas": lista_tarjetas})

    except Exception:
        no_hay_tarjeta = True
        return render(request, "formas_de_pago.html", {"no_hay_tarjeta": no_hay_tarjeta})

def editar_direcciones(request):
    return render(request, "editar_direcciones.html")

def insertar_direccion(request):

    direccion_guardada = False

    colonia = request.GET["colonia"]
    alcaldia = request.GET["alcaldia"]
    calle = request.GET["calle"]
    num_ext = request.GET["no_ext"]
    num_int = request.GET["no_int"]
    cp = request.GET["cp"]
    entre_calles = request.GET["entre_calles"]
    referencia = request.GET["referencia"]
    id_usuario = request.session.get('usr_id')

    nueva_direccion= direccion(
        colonia = colonia,
        alcaldia = alcaldia,
        calle = calle,
        num_ext = num_ext,
        num_int = num_int,
        cp = cp,
        entre_calles = entre_calles,
        referencia = referencia,
        id_usuario = id_usuario,
        )

    try:
        nueva_direccion.save()
        direccion_guardada = True
        lista_direcciones = recuperar_direcciones(request)
        return render(request, "direcciones.html", {"direccion_guardada": direccion_guardada, "lista_direcciones": lista_direcciones})

    except Exception:
        no_hay_direccion = True
        lista_direcciones = recuperar_direcciones(request)
        return render(request, "direcciones.html", {"no_hay_direccion": no_hay_direccion, "lista_direcciones": lista_direcciones})

def recuperar_direcciones(request):
    lista_direcciones = direccion.objects.filter(id_usuario = request.session.get('usr_id'))
    return lista_direcciones

def eliminar_direccion(request):
    eliminada = False

    direccion_seleccionada = request.GET["direccion_seleccionada"]

    try:
        borrar_direccion = direccion.objects.get(id=direccion_seleccionada)
        borrar_direccion.delete()
        eliminada = True
        lista_direcciones = recuperar_direcciones(request)
        return render(request, "direcciones.html", {"eliminada": eliminada, "lista_direcciones": lista_direcciones})

    except Exception:
        no_hay_direccion= True
        return render(request, "direccione.html", {"no_hay_direccion": no_hay_direccion})

def citas_registradas(request):
    lista_citas=recuperar_citas(request)
    return render(request, "citas_registradas.html", {"lista_citas":lista_citas})
