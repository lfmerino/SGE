def menu():
    try:
            print("\n\n\n")
            print("1 - Listar todos los productos")
            print("2 - Detalle de producto")
            print("3 - Salvar fichero CSV")
            print(" ------------------------------ ")
            print("4 - Salir\n") 
            opc = int(input ("Elige una opcion :: "))
            return opc
    except:
        print("OOps... Hubo un error en la generación del menú")

def salir():
    pass

def error_menu():
    print("\n\nHa habido un error en el menu\n")
    pass
