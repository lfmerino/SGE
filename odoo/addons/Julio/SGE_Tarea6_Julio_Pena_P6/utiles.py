import random
from datetime import datetime

def menu():
    try:
            print("\n\n\n")
            print("1 - Listar todos contactos")
            print("2 - Detalle del contacto")
            print("3 - Cargar fichero CSV")
            print("4 - Modificar contacto")
            print(" ------------------------------ ")
            print("5 - Salir\n") 
            opc = int(input ("Elige una opcion :: "))
            return opc
    except:
        print("OOps... Hubo un error en la generación del menú")

def salir():
    pass

def error_menu():
    print("\n\nHa habido un error en el menu\n")
    pass

def creaLogin(u):
        try:
            nombreLista = u.nombre.split()
            login = (nombreLista[0][0:1] + nombreLista[1]).lower()
            # print(login)
            return login
            pass
        except:
            print("OOps... Hubo un problema creadon el login")

def creaPasswd(u):
    try:
        sinvol = ["$", "%", "&"]
        nombreLista = u.nombre.split()
        # print(nombreLista)
        listaTemp = nombreLista[:]
        while (listaTemp == nombreLista): # Nos aseguramos de que han cambiado el orden
            random.shuffle(listaTemp)
        ya = datetime.now()
        contrasena = listaTemp[0][0:1] + str(ya.second) + listaTemp[1][1:2] + listaTemp[1][2:3].upper() + str(ya.minute) + listaTemp[2][4:5] + random.choice(sinvol)
        # print(resultado)
        return contrasena
        pass
    except:
        print("OOps... Hubo un problema creando la contraseña")