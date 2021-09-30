import odoo.addons.tarea5.mismodulos.modulo1 as milib
#import odoo.addons.tarea5.modUsuario.Usuario as milib

u = milib.Usuario(input("Usuario: "))

if u.Salida==0:
    print(u.MiNombre)
else:
    print(u.MiNombre)
    print("Hay un error")

 
c = milib.Clave(input("Contraseña: "))
while not c.Salida:
    c.test_nombre(input("Contraseña: "))

print(c.MiNombre)
