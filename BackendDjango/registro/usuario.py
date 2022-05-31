import email
from datetime import datetime


class Usuario:
    
    nombre=""
    telefono=""
    email=""
    password=""
    mensualidad=False
    inscripcion=False
    apellido=""
    fecha_nac = datetime(1, 1, 1)
    id = 0
        
    def __init__(self, nombre, telefono, email, password, mensualidad, inscripcion, apellido, fecha_nac, id):
            
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.password = password
        self.apellido = apellido
        self.inscripcion = inscripcion
        self.mensualidad = mensualidad
        self.fecha_nac = fecha_nac
        self.id = id
    
    