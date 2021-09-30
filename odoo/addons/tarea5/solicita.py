#import sys #Esta línea es solo para que funcione la línea posterior de sys.path.append
#sys.path.append('F:\Cursos\FP_DAW_DAM\Brianda\SGE\Tareas\Tarea5\odoo\addons\tarea5') #Esta línea es sólo para las pruebas en windows

#from modUsuario import *
import odoo.addons.tarea5.modUsuario.Usuario as milib

from modPasswd import *


#nombreUsuario = input("Introduzca el nombre de usuario: ")
u = milib.Usuario(input("Introduzca el nombre de usuario: "))


if (u.Salida== 0):
    # Aqui haremos lo que queramos. Ahora tengo mensajes en el método pero los quitaría
    print('Ya hemos cambiado el usuario')
else:
    # Otras cosas que queramos hacer
    print("No hemos podido cambiar el usuario")

contraseña = input("Introduzca la contraseña: ")
p = Passwd()
if (p.test_Passwd(contraseña)== 0):
    # Lo mismo que con el usuario pero con la contraseña
    print("Hemos cambiado la contraseña")
else:
    # Idem
    print("No hemos cambiado la contraseña")
