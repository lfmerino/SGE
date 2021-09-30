class Usuario:
#    usuario = ""
    nif = ""
    nombre = ""
    apellido = ""
    fecha_nac = ""
    direccion = ""
#    contraseña = ""

    def __init__(self, nif, nombre, apellido, fecha_nac, direccion):
        self.nif = nif
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.direccion = direccion
        pass


def menu():
    fin = False
    while not fin:
        print ("1 - Introducir datos del usuario")
        print ("2 - Buscar usuario")
        print ("3 - Salvar datos en CSV")
        print ("4 - Recuperar datos de un CSV")
        print (" ------------------------------ ")
        print ("5 - Salir") 
        opc = int(input ("Elige una opcion :: "))
        if (0<opc<6):
            fin = True
    return opc

def introducir_datos():
    # opt = "S"
    # while opt == "S":
        # nif = input("Introduzca el NIF del usuario: ")
        # nombre = input("Introduzca los nombre del usuario: ")
        # apellido = input("Introduzca el apellido del usuario: ")
        # fecha_nac = input("Introduzca la fecha de nacimiento: ")
        # direccion = input("Introduzca la dirección: ")
    #     u = Usuario() 
    #     clave = u.nif
    #     tabla[u.nif] = u
    #     opt = (input("Agregar otro usuario? [S]/N\n")).upper()
    # pass

    datos = 0
    while datos < 4:
        u = Usuario(datos,"nombre" + str(datos), "apellidos" + str(datos), "fecha" + str(datos), "don" + str(datos)) 
        clave = datos
        tabla[datos] = u
        datos = datos + 1
    pass

def buscarUsuario():
    patron = input("Introduzca el nombre o apellido del usuario\n")
    usuarios = tabla.values()
    for u in usuarios:
        print(u.nombre)
    pass

def salvarCSV():
    import csv
    
    campos = ['NIF', 'Nombre', 'Apellido', 'Fecha de Nacimiento', 'Dirección'] 
    datos=[]
    datos.append(campos)
    for ele in tabla.keys():
        datos.append([tabla[ele].nif,tabla[ele].nombre,tabla[ele].apellido,tabla[ele].fecha_nac,tabla[ele].direccion])
    
    ficheroCSV = open('tarea5.csv', 'w')
    with ficheroCSV:
        writer = csv.writer(ficheroCSV)
        writer.writerows(datos)
 
        print("Escritura finalizada")
    pass

def cargarCSV():
    print("Cargar")
    import csv

    with open('tarea5.csv', newline='') as ficheroCSV:
        reader = csv.reader(ficheroCSV, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            print(row)

    pass

def salir():
    pass

def error_menu():
    return "Ha habido un error en el menu"
    pass

###############################################################################
       
tabla = {}
opc = 0
opc_menu = {    
    0: menu,
    1: introducir_datos,
    2: buscarUsuario,
    3: salvarCSV,
    4: cargarCSV,
    5: salir    }

while not (opc == 5):
    opc = menu()
    opc_menu.get(opc, error_menu())()

for obj in tabla:
    print("Soy el objeto {} y mi nombre es {} {}".format(id(tabla[obj]), tabla[obj].nombre, tabla[obj].apellido))

# # # ************************************************************** # # #
