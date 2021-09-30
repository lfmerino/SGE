#import pruebas.clases
import odoo.clases
nombre=input("Nombre:")
edad=int(input("Edad: "))
p=pruebas.clases.persona(nombre,edad)
print(p.nombre + ' ' + p.mayordeedad())
