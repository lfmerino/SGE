class Usuario:
    # usuario = ""
    nif = ""
    nombre = ""
    apellido = ""
    fecha_nac = ""
    direccion = ""
    # contraseña = ""

    def __init__(self, nif, nombre, apellido, fecha_nac, direccion):
        self.nif = nif
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.direccion = direccion
        pass
