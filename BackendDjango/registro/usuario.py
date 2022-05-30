import email
from datetime import date


class Usuario:
    
    nombre=""
    telefono=""
    email=""
    password=""
    mensualidad=False
    inscripcion=False
    apellido=""
    fecha_nac = date(1, 1, 1)
        
    def __init__(self, nombre, telefono, email, password, mensualidad, inscripcion, apellido, fecha_nac):
            
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.password = password
        self.apellido = apellido
        self.inscripcion = inscripcion
        self.mensualidad = mensualidad
        self.fecha_nac = fecha_nac
    
    