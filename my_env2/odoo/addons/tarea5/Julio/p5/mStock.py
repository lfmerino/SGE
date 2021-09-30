import sqlpost
import utiles

c=sqlpost.SqlPostgre()
opc = 0
opc_menu = {    
    0: utiles.menu,
    1: c.productos,
    2: c.producto,
    3: c.salvarCSV,
    4: utiles.salir }

while not (opc == 4):
    opc = utiles.menu()
    opc_menu.get(opc, utiles.error_menu)()

c.desconectar()