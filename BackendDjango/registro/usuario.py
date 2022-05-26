class Usuario:
    
    nombre=""
    telefono=""
    domicilio=""
    contrasenia=""
    mensualidad=False
    inscripcion=False
    apellido=""
        
    def __init__(self, nombre, telefono, domicilio, contrasenia, mensualidad, inscripcion, apellido):
            
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio
        self.contrasenia = contrasenia
        self.apellido = apellido
        self.inscripcion = inscripcion
        self.mensualidad = mensualidad
    
    