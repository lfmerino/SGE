import clase_tabla
import utiles
from csv import DictReader
import clase_usuario

###############################################################################
t = clase_tabla.tabla
opc = 0
opc_menu = {    
    0: utiles.menu,
    1: t.introducir_datos,
    2: t.buscarUsuario,
    3: t.salvarCSV,
    4: t.cargarCSV,
    5: utiles.salir    }

while not (opc == 5):
    opc = utiles.menu()
    opc_menu.get(opc, utiles.error_menu)()

#for obj in t.tt: # Estas dos líneas son solo para pruebas
#    print("Soy el objeto {} y mi nombre es {} {}".format(id(t.tt[obj]), t.tt[obj].nombre, t.tt[obj].apellido))

# # # ************************************************************** # # #
