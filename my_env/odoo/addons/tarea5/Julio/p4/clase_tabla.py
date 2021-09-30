import clase_usuario
from csv import DictReader

class tabla:

    tt={}

    def __init__(self):
        self.tt = {}
        pass

    def introducir_datos():
        try:
            opt = "S"
            while opt == "S":
                nif = input("Introduzca el NIF del usuario: ")
                nombre = input("Introduzca los nombre del usuario: ")
                apellido = input("Introduzca el apellido del usuario: ")
                fecha_nac = input("Introduzca la fecha de nacimiento: ")
                direccion = input("Introduzca la dirección: ")
                u = clase_usuario.Usuario(nif,nombre,apellido,fecha_nac,direccion) 
                clave = u.nif
                tabla.tt[u.nif] = u
                opt = (input("Agregar otro usuario? [S]/N\n")).upper()
            pass
        except:
            print("OOps... Hemos encontrado un error al añadir usuarios")

    def buscarUsuario():
        try:
            resultado=[]
            patron = input("Introduzca el nombre o apellido del usuario\n")
            usuarios = tabla.tt.values()
        
            for u in usuarios:
                if (u.nombre == patron or u.apellido == patron):
                    resultado.append(u)
                    print(u.nombre)
            if resultado:
                for us in range(len(resultado)):
                    print("NIF: {}, Nombre: {}, Apellido: {}, Fecha de Nacimiento: {}, Dirección: {}\n\n".format(resultado[us].nif, resultado[us].nombre, resultado[us].apellido, resultado[us].fecha_nac, resultado[us].direccion))
            else:
                print("\nEl usuario '{}' no existe\n".format(patron))
            pass
        except:
            print("OOps... Hubo un error al buscar el usuario")

    def salvarCSV():
        import csv
        
        try:
            campos = ['NIF', 'Nombre', 'Apellido', 'Fecha de Nacimiento', 'Direccion'] 
            datos=[]
            datos.append(campos)
            for ele in tabla.tt.keys():
                datos.append([tabla.tt[ele].nif,tabla.tt[ele].nombre,tabla.tt[ele].apellido,tabla.tt[ele].fecha_nac,tabla.tt[ele].direccion])
            
            ficheroCSV = open('SGE.csv', 'w', newline="")
            with ficheroCSV:
                writer = csv.writer(ficheroCSV)
                writer.writerows(datos)
        
                print("Escritura finalizada")
        except:
            print("OOps... Hubo un error salvando el archivo")
        pass

    def cargarCSV():
        try:
            import csv

            if tabla.tt:
                print("Ya existen datos en el almacen\n")
            else:
                fich = input("Introduzca el nombre del fichero con la extensión: ")
                with open(fich, newline='') as ficheroCSV:
                    reader = DictReader(ficheroCSV)
                    print("leyendo datos...")
                    for row in reader:
                        tabla.tt[row['NIF']]=clase_usuario.Usuario(row['NIF'],row['Nombre'],row['Apellido'],row['Fecha de Nacimiento'],row['Direccion'])
                        
            pass
        except:
            print("OOps... Se ha encontrado un problema cargando el archivo '{}'".format(fich))
