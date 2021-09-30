import utiles

class Usuario:
    usuario = ""
    contraseña = ""
    nombre = ""
    nombreMostrador = ""
    contacto = ""
    direccion = ""
    telefono = ""
    correo = ""
    web = ""
    ciudad = ""
    cp = ""
    tipo = ""
    active = True

    # def __init__(self, nif, nombre, apellido, fecha_nac, direccion):
    #     self.nif = nif
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.fecha_nac = fecha_nac
    #     self.direccion = direccion
    #     pass
    
    def __init__(self, nombre, nombreMostrado, contacto, direccion, telefono, correo, web, ciudad, cp, tipo, active = True):
        self.nombre = nombre
        self.nombreMostrado = nombreMostrado
        self.contacto = contacto
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.web = web
        self.ciudad = ciudad
        self.cp = cp
        self.tipo = self.checkTipo(tipo)
        self.active = active
        self.usuario = utiles.creaLogin(self)
        self.contrasena = utiles.creaPasswd(self)
        pass

    def checkTipo(self, p = ""):
        valores = ["P", "T", "C"]
        if not( p.upper() in valores):
            print("El 'Tipo' no es correcto")
            return None
        else:
            return p
        
