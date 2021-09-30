
##########################################################################
def pedirDatos():
    ape = input("Introduzca los apellidos del usuario: ")
    nom = input("Introduzca el nombre del usuario: ")
    fnac = input("Introduzca la fecha de nacimiento: ")
    don = input("Introduzca la dirección: ")
    con = input("Introduzca la contraseña: ")
    return (ape, nom, fnac, don, con)

def buscarUsuario():
    pass

##########################################################################
def salvarCSV():
    pass
    import csv
 
    with open('example4.csv', 'w') as csvfile:
        fieldnames = ['first_name', 'last_name', 'Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
        writer.writeheader()
        writer.writerow({'Grade': 'B', 'first_name': 'Alex', 'last_name': 'Brian'})
        writer.writerow({'Grade': 'A', 'first_name': 'Rachael',
                     'last_name': 'Rodriguez'})
        writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
        writer.writerow({'Grade': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})
 
        print("Writing complete")

##########################################################################
def cargarCSV():
    pass
    results = []
    with open('example.csv') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
        print (results)
        
##########################################################################
def menu():
    fin = False
    opc = 0
 
    while not fin:
        print ("1 - Introducir datos del usuario")
        print ("2 - Buscar usuario")
        print ("3 - Salvar datos en CSV")
        print ("4 - Recuperar datos de un CSV")
        print (" ------------------------------ ") 
        opc = int(input ("Elige una opcion :: "))
        if 0 < opc < 5:
            fin = True
        elif opc == 5:
            print("Cancelado por el usuario\n")
            break
        else:
            print ("Elija un número entre 1 y 4. 5 para salir\n")
    return opc

# # # ************************************************************** # # #
apellidos = "apellidos"
nombre = "nombre"
fechaNacimiento = "fechaNacimiento"
direccion = "direccion"
contraseña = "contraseña"
usuarios = []
singleUser = {}
opc = menu()
if opc == 1:
    print ("pedirDatos()\n")
    singleUser["Apellidos"],singleUser["Nombre"], singleUser["Fecha de Nacimiento"], singleUser["Direccion"], singleUser["Contraseña"] = pedirDatos()
    usuarios.append(singleUser)
    print(usuarios[len(usuarios)-1])
elif opc == 2:
    print ("buscarUsuario()\n")
elif opc == 3:
    print("salvarCSV()\n")
elif opc == 4:
    print("cargarCSV()\n")
else:
    pass


