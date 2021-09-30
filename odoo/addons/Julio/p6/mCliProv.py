import utiles
import config
import sqlpost
import clase_usuario

o = sqlpost.SqlPostgre()
#o.conectar()
# o.cargarCSV()
# u = clase_usuario.Usuario("Minombre Apellido Bpellido", "contacto", "Dirección, 8", "555 39 39", "correo@punto.es", "http://web", "Madrid", "26008", "T")
# dicCSV = o.cargarCSV()
# resultado = o.csvAtabla(dicCSV)
# print("{} registros fueron actualizados y {} registros fueron dados de alta".format(resultado[0], resultado[1]))
opc = 0
opc_menu = {    
    0: utiles.menu,
    1: o.listarContactos, # Listar contactos
    2: o.detalleContacto, # Detalle del contacto
    3: o.cargarCSV, # Cargar fichero CSV
    4: o.modificarContacto, # Modificar contacto
    5: utiles.salir }

while not (opc == 5):
    opc = utiles.menu()
    opc_menu.get(opc, utiles.error_menu)()
#o.desconectar()