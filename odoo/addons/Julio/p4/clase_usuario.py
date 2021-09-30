# -*- coding: utf-8 -*-
class Usuario:
    # usuario = ""
    nif = ""
    nombre = ""
    apellido = ""
    fecha_nac = ""
    direccion = ""
    # contraseña = ""

    #def __init__(self, nif, nombre, apellido, fecha_nac, direccion):
    def __init__(self):
        '''self.nif = nif
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.direccion = direccion'''
        nif = input("Introduzca el NIF del usuario: ")
        nombre = input("Introduzca los nombre del usuario: ")
        apellido = input("Introduzca el apellido del usuario: ")
        fecha_nac = input("Introduzca la fecha de nacimiento: ")
        direccion = input("Introduzca la direcciÃ³n: ")
        pass
