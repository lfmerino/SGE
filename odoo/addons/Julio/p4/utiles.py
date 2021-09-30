# -*- coding: utf-8 -*-
def menu():
    try:
            print("\n\n\n")
            print ("1 - Introducir datos del usuario")
            print ("2 - Buscar usuario")
            print ("3 - Salvar datos en CSV")
            print ("4 - Recuperar datos de un CSV")
            print (" ------------------------------ ")
            print ("5 - Salir\n") 
            opc = int(input ("Elige una opcion :: "))
            return opc
    except:
        print("OOps... Hubo un error en la generación del menú")

def salir():
    pass

def error_menu():
    print("\n\nHa habido un error en el menu\n")

    pass