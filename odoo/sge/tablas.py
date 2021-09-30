# -*- coding: utf-8 -*-

import os
import pandas as pd
#from typing import Any, Hashable, Iterable, Optional

#def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
#	for dicc in it:
#		if dicc[clave] == valor:
#			return dicc
#	return None

os.system("clear")

datos = {'Apellidos':['vaquero diaz','lopez raya'],
	'Nombre':['tony', 'adrian'],
	'Fecha_nacimiento':['12-07-85','01-05-74'],
	'Direccion':['fray luis', 'limones'],
	'Contraseña':['123456', '987612']}

print ("Tabla de datos inicial\n")

tabla_datos = pd.DataFrame(datos, columns =['Apellidos','Nombre','Fecha_nacimiento','Direccion','Contraseña'])
tabla_datos

print (tabla_datos, "\n")

while True:

	print ("Elige una de estas opciones \n\
1 - Almacenar datos\n\
2 - Buscar datos\n\
3 - Añadir datos a un fichero .csv\n\
4 - Recuperar datos de un fichero .csv\n\
5 - Salir")

	opcion=input()

	if opcion == '1':

		print ("Introduce los apellidos")
		datos['Apellidos'].append (input())
		print ("Introduce el nombre")
		datos['Nombre'].append (input())
		print ("Introduce la fecha de nacimiento")
		datos['Fecha_nacimiento'].append (input())
		print ("Introduce la direccion")
		datos['Direccion'].append (input())
		print ("Introduce la contraseña")
		datos['Contraseña'].append (input())
		tabla_datos = pd.DataFrame(datos)
		tabla_datos
		print ("\nTabla de datos actual\n")
		print (tabla_datos)

	elif opcion == '2':

		print ("Seleccione una opcion\n\
1 - Nombre\n\
2 - Apellidos")

		opcion=input()

		if opcion == '1':

			nomb=input("Nombre: ")
			dat=datos['Nombre'].index(nomb)
			val=False

			for value in datos.values():
				if (nomb in value):
					val = True
					break
			print (val)
			print (dat)

		if opcion == '2':

                        nomb=input("Apellidos: ")
                        dat=datos['Apellidos'].index(nomb)
                        val=False

                        for value in datos.values():
                                if (nomb in value):
                                        val = True
                                        break
                        print (val)
                        print (dat)

		#for nomb in datos.items():
		#	print (nomb())
		#buscar_dicc(datos, "Name", "tony")
	elif opcion == '3':
		# tabla_datos.to_csv(index=False)
		#'Apellidos,Nombre,Fecha_nacimiento,Direccion,Contraseña\nvaquero diaz,tony,12-07-85,fray luis,123456\nlopez raya,adrian,01-05-74,limones,987612\n'
		#compression_opts = dict(method='zip',
		#	archive_name='out.csv')
		tabla_datos.to_csv('/usr/lib/python3/dist-packages/odoo/addons/sge/example.csv')
		#, index=False,
		#	compression=compression_opts)
	elif opcion == '4':
		d=pd.read_csv('/usr/lib/python3/dist-packages/odoo/addons/sge/data.csv')
		print ("\nTabla importada\n")
		print (d)
		tabla_datos=pd.concat([tabla_datos, d])
		tabla_datos
		tabla_datos.index=range(tabla_datos.shape[0])
		#ids=pd.DataFrame(tabla_datos)
		#({'id':[]},columns=['Apellidos'])
		#tabla_datos=pd.concat([ids,tabla_datos],axis=1)
		#tabla_datos
		#datos['Apellidos'].append (d)
		#datos['Nombre'].append (d)
		#datos['Fecha_nacimiento'].append (d)
		#datos['Direccion'].append(d)
		#datos['Contraseña'].append(d)
		print ("\nTabla de datos actual\n")
		print (tabla_datos)
	elif opcion == '5':
		break
	input()
